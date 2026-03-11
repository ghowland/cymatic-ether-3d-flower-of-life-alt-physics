# ZigLLM — Technical Specification Outline

## Integer-Only Transformer Training and Inference for Zig + C Code Generation

**Status:** Architecture Specification — Draft 1
**Date:** March 11, 2026
**Language:** Zig 0.14 (entire stack)
**Hardware:** CPU-only, 64 GB RAM, AVX2
**Dependencies:** None

---

## 1. PROJECT GOALS

### 1.1 Primary Goal

Train a 1B parameter transformer model that generates correct Zig 0.14 code
and understands C library interfaces, using entirely integer arithmetic with
VFR shell-based weight updates. No floats anywhere in the system.

### 1.2 Secondary Goals

- Demonstrate that integer-only training converges on a real (non-toy) task
- Measure long-tail accuracy on rare Zig patterns vs equivalent float model
- Validate shell transition dynamics as a training diagnostic
- Prove CPU-only training is viable for focused, single-domain models
- Produce a useful tool: a Zig code assistant that runs on commodity hardware

### 1.3 Non-Goals

- General-purpose language understanding
- Multi-language code generation beyond Zig and C
- Conversational ability, helpfulness, or safety alignment
- GPU acceleration (future work, not this project)
- Competing with commercial LLMs on general benchmarks

---

## 2. SYSTEM OVERVIEW

The system has four major phases, each a standalone Zig binary:

```
Phase 1: TOKENIZE    zig-tokenize     Raw text → token IDs (flat binary file)
Phase 2: TRAIN       zig-train        Token IDs → trained weights
Phase 3: INFER       zig-infer        Prompt → generated Zig code
Phase 4: EVAL        zig-eval         Generated code → compile → pass/fail
```

All four share a common library of data structures and integer arithmetic
routines. No phase depends on any external tool, library, or runtime.

---

## 3. DATA STRUCTURES

### 3.1 Core Arithmetic Types

```
VFRWeight
    v: i32          The shell value. The actual weight used in computation.
    r: i16          The remainder. Accumulated gradient pressure toward
                    the next shell. When |r| >= SHELL_THRESHOLD, v changes
                    and r resets via modulo. This is live data, not error.

VFRConfig
    shell_threshold: i16    Typically 32 (one harmonic octave).
    octave: u8              Per-layer power of 32. Determines bit shift
                            for domain conversion. Octave 2 means F=1024,
                            shift=10.
```

VFRWeight is the fundamental unit. Every learnable parameter in the model
is one of these. The v field is what participates in forward/backward
computation. The r field is only touched during the weight update step.

During forward and backward passes, only v is read. During the update step,
only r is read and written (and v if a shell transition occurs). This
separation enables clean memory access patterns.

### 3.2 Tensor Types

```
IntTensor
    data: []i32             Flat array of integer values.
    shape: [4]u32           Up to 4 dimensions: [batch, seq, rows, cols].
                            Unused dims set to 1.
    stride: [4]u32          Stride per dimension for indexing.

WeightMatrix
    weights: []VFRWeight    Flat array of VFRWeight structs.
    rows: u32               Matrix height.
    cols: u32               Matrix width.
    octave: u8              This matrix's harmonic octave.
```

IntTensor is used for activations, gradients, and intermediate values
during forward/backward passes. It holds i32 values.

WeightMatrix is used for all learnable parameters. It wraps a flat array
of VFRWeight structs plus the matrix dimensions and the octave for this
layer.

Matmul between a WeightMatrix and an IntTensor reads only the v field
of each VFRWeight, multiplies against the i32 activation, accumulates
into an i64 register, then shifts right by the octave to produce an
i32 result.

### 3.3 Model Architecture

```
TransformerConfig
    vocab_size: u32         Token vocabulary size. Probably 8000-16000
                            for Zig+C only.
    d_model: u32            Hidden dimension. 2048 for a 1B model.
    n_layers: u32           Number of transformer layers. 24 for 1B.
    n_heads: u32            Attention heads. 16 for d_model=2048.
    d_head: u32             Per-head dimension. d_model / n_heads = 128.
    d_ff: u32               Feedforward intermediate size. 4 × d_model = 8192.
    max_seq_len: u32        Maximum sequence length. 2048 or 4096.
    octave_embed: u8        Octave for embedding layer.
    octave_attn: u8         Octave for attention layers.
    octave_ff: u8           Octave for feedforward layers.
    octave_output: u8       Octave for output logits.

EmbeddingTable
    table: WeightMatrix     Shape: [vocab_size, d_model].
                            Each row is one token's embedding vector.
                            Indexed by token ID. Pure integer lookup.

AttentionLayer
    wq: WeightMatrix        Query projection.  [d_model, d_model]
    wk: WeightMatrix        Key projection.    [d_model, d_model]
    wv: WeightMatrix        Value projection.  [d_model, d_model]
    wo: WeightMatrix        Output projection. [d_model, d_model]
    norm: LayerNorm         Pre-attention normalization.

FeedForwardLayer
    w1: WeightMatrix        Up projection.   [d_model, d_ff]
    w2: WeightMatrix        Down projection. [d_ff, d_model]
    norm: LayerNorm         Pre-feedforward normalization.

LayerNorm
    scale: []VFRWeight      Per-dimension scale. [d_model]
    bias: []VFRWeight       Per-dimension bias.  [d_model]
    octave: u8              Normalization octave.

TransformerBlock
    attention: AttentionLayer
    feedforward: FeedForwardLayer

TransformerModel
    config: TransformerConfig
    embedding: EmbeddingTable
    layers: []TransformerBlock    Array of n_layers blocks.
    output_norm: LayerNorm        Final layer norm.
    output_proj: WeightMatrix     [d_model, vocab_size]. Produces logits.
```

The total parameter count for a 1B model at these dimensions:

    Embedding:      vocab_size × d_model         ~16K × 2048     = 33M
    Per layer:
      QKV + O:      4 × d_model × d_model        4 × 2048 × 2048 = 16.8M
      FF:           2 × d_model × d_ff            2 × 2048 × 8192 = 33.6M
      Norms:        4 × d_model                                    = 8K
      Subtotal per layer:                                          ≈ 50.4M
    24 layers:                                                     = 1,210M
    Output proj:    d_model × vocab_size                           = 33M
    Total:                                                         ≈ 1,276M

At 6 bytes per parameter (i32 + i16): 7.6 GB weight storage.
Training state total: ~22 GB. Fits comfortably in 64 GB.

### 3.4 Tokenizer Types

```
TokenizerConfig
    vocab_size: u32         Target vocabulary size.
    min_frequency: u32      Minimum pair frequency for BPE merge.
    special_tokens: [][]u8  Reserved tokens: PAD, BOS, EOS, UNK.

BPEMerge
    pair: [2]u16            The two token IDs that merge.
    result: u16             The new token ID produced.

Tokenizer
    merges: []BPEMerge              Ordered list of BPE merges.
    vocab: [][]u8                   Token ID → byte sequence.
    token_to_id: HashMap([]u8, u16) Byte sequence → token ID.
```

The tokenizer is trained once on the Zig+C corpus and produces a merge
table. The merge table is a flat list of integer pairs — no floats.
BPE is inherently integer: count co-occurrences, merge the most frequent
pair, repeat.

The vocabulary is small (8K-16K) because Zig and C have limited syntax.
The tokenizer should be Zig-aware: Zig keywords, operators, and common
standard library identifiers should be single tokens where possible.

### 3.5 Training State

```
TrainingConfig
    batch_size: u32         Sequences per batch. Probably 32-64.
    seq_len: u32            Tokens per sequence. 2048.
    lr_octave_shift: u8     Learning rate as octave bit shift. Higher = slower.
    lr_warmup_steps: u32    Steps to ramp up from high shift to target.
    lr_total_steps: u32     Total training steps.
    checkpoint_interval: u32  Steps between weight saves.
    log_interval: u32       Steps between metric prints.

TrainingState
    step: u64               Current global training step.
    epoch: u32              Current epoch (pass through data).
    loss_accumulator: i64   Running loss sum for logging.
    transition_count: u64   Shell transitions this logging interval.
    tokens_seen: u64        Total tokens processed.

Checkpoint
    config: TransformerConfig
    training_state: TrainingState
    weights: raw byte dump of all VFRWeight arrays
```

Checkpointing is simple: dump the VFRWeight arrays to disk as raw bytes.
The weights are i32 + i16 packed structs — no serialization format needed.
Just write the bytes and read them back. Exact. No precision loss from
format conversion.

### 3.6 Inference State

```
KVCache
    keys: []IntTensor       One [seq_len, d_head] tensor per layer per head.
    values: []IntTensor     Same shape. Cached to avoid recomputation
                            during autoregressive generation.
    length: u32             Current sequence position.

GenerationConfig
    max_tokens: u32         Maximum tokens to generate.
    temperature: u8         Sampling temperature as integer scale.
                            0 = greedy (argmax). Higher = more random.
    top_k: u16              Only consider top K logits. 0 = no limit.
```

The KV cache stores integer activations from previous positions so each
new token only requires computing one position through the network rather
than the full sequence. This is standard transformer inference, but with
i32 values instead of floats.

---

## 4. PROCESSES

### 4.1 Tokenization (zig-tokenize)

**Input:** Directory of .zig and .c source files.
**Output:** Binary file of u16 token IDs. Separate tokenizer model file.

**Process:**

1. Walk the source directory, read all .zig and .c files.
2. Concatenate into a raw byte stream with file-boundary tokens.
3. Train BPE on the byte stream:
   a. Initialize vocabulary with individual bytes (256 entries).
   b. Add special tokens (PAD, BOS, EOS, UNK, FILE_SEP).
   c. Count all adjacent token pairs in the corpus.
   d. Find the pair with highest count.
   e. Create a new token for that pair, add to vocabulary.
   f. Replace all occurrences in the corpus.
   g. Repeat from (c) until vocab_size reached.
4. Apply final tokenization to the full corpus.
5. Write token IDs as flat binary (u16 per token).
6. Write tokenizer model (merge table + vocabulary) for inference use.

All operations are integer counting and replacement. BPE is natively ℤ.

The tokenizer should handle Zig-specific patterns well:
- `comptime`, `anytype`, `@import` should be single tokens early.
- Common std lib paths like `std.mem.Allocator` should merge efficiently.
- C interop patterns like `@cImport`, `@cInclude` should be single tokens.

### 4.2 Training (zig-train)

**Input:** Token binary file + tokenizer model + training config.
**Output:** Checkpoint files (weight dumps).

**Process per training step:**

**4.2.1 Data Loading**

Memory-map the token binary file. Each batch is a contiguous slice of
batch_size × seq_len tokens. The input is tokens[0..n-1] and the target
is tokens[1..n] (next-token prediction, standard causal LM setup).

No shuffling for the first version. Just stream through the data
sequentially. Multiple epochs cycle back to the beginning.

**4.2.2 Forward Pass**

For each token position in the sequence:

1. Embed: look up the i32 vector for each token ID from the embedding
   table. This is a direct integer array index. No computation.

2. For each transformer layer:

   a. Layer norm: compute mean and variance of the i32 activation vector
      across the d_model dimension. Subtract mean, divide by standard
      deviation. This is the one step that requires care — integer
      division for the variance. Use the layer norm's octave for
      precision. Apply scale and bias (VFRWeights).

   b. Attention:
      - Compute Q = norm_output × wq (integer matmul, i32 × i32 → i64 accumulator → shift → i32)
      - Compute K = norm_output × wk (same)
      - Compute V = norm_output × wv (same)
      - Split Q, K, V into n_heads chunks of d_head each.
      - Per head: scores = Q × K^T (integer matmul). Scores are i32.
      - Causal mask: set future positions to large negative integer.
      - Softmax: via integer lookup table. Maps i32 scores to i32
        probabilities at the softmax octave. See section 4.2.7.
      - Weighted sum: probabilities × V (integer matmul).
      - Concatenate heads, project through wo.
      - Add residual connection (integer addition, same octave).

   c. Layer norm again for feedforward.

   d. Feedforward:
      - Up project: x × w1 (integer matmul → i32).
      - GELU activation: via integer lookup table. See section 4.2.7.
      - Down project: gelu_output × w2 (integer matmul → i32).
      - Add residual connection.

3. Final layer norm.

4. Output projection: norm_output × output_proj → logits (i32 per vocab token).

**4.2.3 Loss Computation**

Integer cross-entropy loss. The logits are i32 values for each vocabulary
token. The target is the correct next token ID.

The loss for one position is: -log(softmax(logit[target]))

In integer:
- Compute log-softmax via lookup table at the loss octave.
- The loss is the negative of the log-softmax value at the target index.
- Sum across all positions in the batch.
- The total loss is an i64 (sum of many i32 loss values).

The loss value itself is a diagnostic for humans. Its absolute scale
doesn't matter for training. What matters is that the gradients derived
from it are exact.

**4.2.4 Backward Pass**

Reverse the forward pass, applying the chain rule at each step.

For the output layer:
- Gradient of cross-entropy with respect to logits: softmax(logits) - one_hot(target).
  In integer: the softmax values (already computed) minus 1 at the target position
  and 0 elsewhere, scaled to the gradient octave.

For each transformer layer (in reverse order):

- Gradients through residual connections: addition, so gradient passes through unchanged.
- Gradients through feedforward: transpose of the matmuls.
  d_w2 = gelu_output^T × d_output, d_gelu = d_output × w2^T.
- Gradients through GELU: multiply by GELU derivative (lookup table).
  d_w1 = input^T × d_gelu_pre, d_input = d_gelu_pre × w1^T.
- Gradients through attention: same chain of transposed matmuls.
- Gradients through layer norm: requires derivative of the normalization.

Every gradient is an integer matmul (transposed) or an element-wise
integer operation. The chain rule over integer operations produces
integer gradients. No approximation.

**4.2.5 Shell Update**

For every VFRWeight in the model:

1. Read the gradient for this weight (i32).
2. Scale the gradient by the learning rate (right shift by lr_octave_shift).
3. Negate (gradient descent, not ascent).
4. Add the scaled gradient to the weight's remainder r (i16).
5. If r >= shell_threshold: v += r / shell_threshold; r = r mod shell_threshold.
6. If r <= -shell_threshold: v -= (-r) / shell_threshold; r = -((-r) mod shell_threshold).

This is the only step that modifies the weights. It is entirely integer:
addition, bit shift, comparison, modulo.

The shell update can optionally track:
- Number of transitions this step (convergence diagnostic).
- Maximum |r| across all weights (distance from convergence).
- Mean |r| (average pressure).

**4.2.6 Learning Rate Schedule**

The learning rate is an octave shift (u8). Higher shift = smaller
effective learning rate.

Schedule:
- Warmup: start at shift+4 (very slow), decrease to target shift over
  warmup_steps. Each decrease doubles the effective learning rate.
- Main training: hold at target shift.
- Decay: increase shift by 1 every N steps (halving effective LR).

The schedule is entirely integer: a u8 value that changes at step
boundaries. No float cosine schedule. Discrete octave steps.

**4.2.7 Lookup Tables for Transcendentals**

Three lookup tables, computed once at program startup:

Softmax LUT:
- Input: i32 score (range determined by octave).
- Output: i32 probability at softmax octave.
- Size: covers the practical input range. Probably 64K entries.
- Computed using high-precision integer arithmetic or nested VFR at
  depth 3-4 during table generation (this is the one place where the
  program does extended precision math, at startup, once).

GELU LUT:
- Input: i32 activation.
- Output: i32 activated value.
- Same approach. Precomputed. Covers practical range.

Log-softmax LUT:
- Input: i32 probability.
- Output: i32 log-probability at loss octave.
- Used only in loss computation.

Between table entries, use linear interpolation in integer:
  result = table[i] + ((table[i+1] - table[i]) × frac) >> frac_bits
This is one multiply, one add, one shift. Integer.

### 4.3 Inference (zig-infer)

**Input:** Trained weights + tokenizer model + text prompt.
**Output:** Generated Zig code as text.

**Process:**

1. Load trained weights from checkpoint file (raw byte read into
   VFRWeight arrays — instant, no parsing).
2. Load tokenizer model.
3. Tokenize the input prompt into token IDs.
4. Initialize KV cache (empty).
5. Run the prompt through the forward pass to populate the KV cache.
   This processes all prompt tokens in parallel (no generation yet).
6. Autoregressive generation loop:
   a. Take the last token's logits (i32 array over vocabulary).
   b. Apply temperature scaling (integer multiply + shift).
   c. Apply top-k filtering (partial integer sort, zero out the rest).
   d. Convert filtered logits to probabilities (softmax LUT).
   e. Sample from the probability distribution (integer random +
      cumulative sum comparison — no floats).
   f. Append the sampled token to the sequence.
   g. Run one forward pass for the new position only, using KV cache.
   h. Repeat until EOS token or max_tokens reached.
7. Detokenize: convert token IDs back to bytes using vocabulary table.
8. Output the generated text.

Temperature=0 (greedy) is just argmax over i32 values. Integer comparison.
Deterministic — same prompt always produces same output.

### 4.4 Evaluation (zig-eval)

**Input:** Test set of Zig coding problems with expected behavior.
**Output:** Pass/fail report with accuracy metrics.

**Process:**

1. Load a test suite of Zig problems. Each problem has:
   - A prompt (natural language description or partial code).
   - Expected behavior (compiles, produces output X, passes test Y).

2. For each problem:
   a. Feed the prompt to zig-infer.
   b. Capture the generated code.
   c. Write the code to a temporary .zig file.
   d. Invoke the Zig compiler on the file.
   e. If compilation succeeds, run the binary.
   f. Compare output against expected behavior.
   g. Record: compile pass/fail, runtime pass/fail, output match.

3. Aggregate metrics:
   - Compilation rate (% of generated code that compiles).
   - Pass rate (% that produces correct output).
   - Breakdown by problem difficulty / pattern type.
   - Long-tail analysis (accuracy on rare Zig patterns).

The evaluation is binary and unambiguous. The code compiles or it doesn't.
The output matches or it doesn't. No subjective scoring. No human judgment.

---

## 5. MODULE STRUCTURE

```
zigllm/
├── src/
│   ├── core/
│   │   ├── vfr.zig           VFRWeight struct, shell update, octave ops
│   │   ├── tensor.zig        IntTensor struct, indexing, slicing
│   │   ├── matmul.zig        Integer matmul with i64 accumulators, AVX2
│   │   ├── lut.zig           Lookup table generation and interpolation
│   │   └── random.zig        Integer PRNG for weight init and sampling
│   │
│   ├── model/
│   │   ├── config.zig        TransformerConfig, all hyperparameters
│   │   ├── embedding.zig     EmbeddingTable, token → vector lookup
│   │   ├── attention.zig     AttentionLayer, QKV projections, causal mask
│   │   ├── feedforward.zig   FeedForwardLayer, up/down projections
│   │   ├── layernorm.zig     Integer layer normalization
│   │   ├── transformer.zig   Full model: stack of TransformerBlocks
│   │   └── init.zig          Weight initialization strategies
│   │
│   ├── training/
│   │   ├── forward.zig       Forward pass, activation caching for backward
│   │   ├── backward.zig      Backward pass, gradient computation
│   │   ├── loss.zig          Integer cross-entropy loss
│   │   ├── optimizer.zig     Shell update: gradient → remainder → transition
│   │   ├── schedule.zig      Learning rate octave schedule
│   │   ├── checkpoint.zig    Save/load raw weight bytes
│   │   └── metrics.zig       Shell transition count, loss tracking, convergence
│   │
│   ├── tokenizer/
│   │   ├── bpe.zig           BPE training and encoding/decoding
│   │   ├── vocab.zig         Vocabulary management, special tokens
│   │   └── zig_aware.zig     Zig-specific tokenization rules
│   │
│   ├── inference/
│   │   ├── generate.zig      Autoregressive generation loop
│   │   ├── kv_cache.zig      KV cache management
│   │   ├── sample.zig        Temperature, top-k, integer sampling
│   │   └── server.zig        Simple TCP server for interactive use (optional)
│   │
│   └── eval/
│       ├── runner.zig         Test suite runner
│       ├── compiler.zig       Invoke Zig compiler on generated code
│       └── report.zig         Accuracy metrics and reporting
│
├── data/
│   ├── raw/                   Raw .zig and .c source files
│   ├── tokens/                Tokenized binary files
│   └── eval/                  Test problems
│
├── checkpoints/               Saved weight files
│
├── tools/
│   ├── zig-tokenize.zig       Tokenizer training + corpus tokenization
│   ├── zig-train.zig          Training binary entry point
│   ├── zig-infer.zig          Inference binary entry point
│   └── zig-eval.zig           Evaluation binary entry point
│
└── build.zig                  Build all four binaries
```

### 5.1 Build Outputs

```
zig build tokenize   →   zig-out/bin/zig-tokenize
zig build train      →   zig-out/bin/zig-train
zig build infer      →   zig-out/bin/zig-infer
zig build eval       →   zig-out/bin/zig-eval
```

Four binaries. No shared libraries. No runtime dependencies.
Each binary is fully self-contained.

---

## 6. DATA PIPELINE

### 6.1 Corpus Assembly

Source data, in priority order:

```
Zig (primary):
    Zig compiler source          (self-hosted, ~200K lines)
    Zig standard library         (~150K lines)
    Public GitHub Zig repos      (scraped, deduplicated)
    Zig package index repos      (gyro, zigmod ecosystem)
    Zig language reference       (official docs as text)

C (interop):
    musl libc source             (clean, readable C)
    SQLite source                (single-file, famously clean)
    Linux kernel headers         (API surface Zig commonly wraps)
    stb single-header libraries  (common Zig interop targets)
    raylib source                (Zig game dev community uses this)
    Vulkan/OpenGL headers        (graphics interop)
    curl, zlib, openssl headers  (common system libraries)
    POSIX man pages              (API documentation as text)

Technical English:
    Zig issue tracker            (technical discussions, filtered)
    Zig community docs/guides
    Zig release notes and changelogs
    Selected C programming texts (K&R level quality)

Typo tolerance (synthetic):
    Generated by corrupting clean Zig questions
    Swap adjacent letters, drop letters, common substitutions
    Paired: corrupted → clean
```

### 6.2 Preprocessing

1. Clone/download all sources.
2. For code: strip comments optionally (or keep — comments teach intent).
   Remove license headers (repetitive). Deduplicate at file level.
3. For docs: convert to plain text. Strip HTML/markdown formatting.
4. For typo data: generate N corrupted variants per clean source.
5. Concatenate with FILE_SEP tokens between documents.
6. Estimate total corpus size. Target: 5-10 billion tokens.

### 6.3 Tokenization

Run zig-tokenize on the concatenated corpus:
1. Train BPE to target vocab size (8K-16K).
2. Apply trained tokenizer to full corpus.
3. Output: flat binary of u16 token IDs.
4. Output: tokenizer model file (merges + vocab).

---

## 7. TRAINING PLAN

### 7.1 Hyperparameters (Starting Point)

```
Model:
    vocab_size:     16384  (14 bits, power of 2)
    d_model:        2048
    n_layers:       24
    n_heads:        16
    d_head:         128
    d_ff:           8192
    max_seq_len:    2048

Training:
    batch_size:     32
    seq_len:        2048
    lr_octave_shift: 4     (effective LR = gradient >> 4)
    lr_warmup:      2000 steps
    shell_threshold: 32
    octave_attn:    2
    octave_ff:      2
    octave_output:  3

Hardware:
    RAM:            64 GB
    Compute:        CPU, AVX2
    Parallelism:    Multi-threaded matmul across CPU cores
```

### 7.2 Training Duration Estimate

```
Tokens per step:     batch_size × seq_len = 32 × 2048 = 65,536
Total tokens:        5 billion (1 epoch)
Steps per epoch:     5B / 65,536 ≈ 76,294
Target epochs:       1-3 (code models often train <1 epoch on deduplicated data)
Total steps:         ~76K to 229K

Time per step estimate:
    Forward matmul ops per layer: ~4 × 2048 × 2048 × 32 = ~537M i32 multiplies
    24 layers: ~12.9B multiplies per step
    AVX2 at ~8 ops/cycle, 3 GHz, 8 cores: ~19.2 Gops/sec
    Time per step: ~0.67 seconds

    Plus backward (~2× forward): ~1.34 seconds
    Plus overhead: ~0.3 seconds
    Total per step: ~2.3 seconds

Total training time:
    76K steps × 2.3 sec = ~48 hours (1 epoch)
    229K steps × 2.3 sec = ~146 hours (3 epochs)

Estimate: 2-6 days depending on epochs.
```

These are rough estimates. Actual performance depends on memory bandwidth,
cache behavior, and how well the matmul exploits AVX2. Could be 2× faster
or 2× slower.

### 7.3 Monitoring

During training, log at every log_interval:

```
Step | Tokens | Loss | Transitions | Max|R| | Mean|R| | Converging?
-----+--------+------+-------------+--------+---------+------------
1000 | 65.5M  | 8421 | 142,391     | 31     | 14.2    | No
2000 | 131M   | 5102 | 98,204      | 30     | 12.8    | Trending
...
70K  | 4.6B   | 1203 | 412         | 27     | 6.1     | Nearly
76K  | 5.0B   | 1198 | 38          | 24     | 5.8     | Yes
```

The transition count is the primary convergence signal. When it reaches
near-zero, the model has settled into its ground state.

---

## 8. EVALUATION PLAN

### 8.1 Test Categories

```
Basic syntax:
    "Write a function that adds two i32 values"
    "Write a for loop over a slice"
    "Write a struct with three fields"

Standard library:
    "Read a file using std.fs"
    "Sort a slice using std.sort"
    "Use an ArrayList to collect values"

Memory management:
    "Write a function that takes an allocator and allocates a buffer"
    "Implement a simple arena allocator"

C interop:
    "Import and call printf via @cImport"
    "Wrap a C struct for use in Zig"
    "Link against libcurl and make an HTTP GET"

Comptime:
    "Write a comptime function that generates a lookup table"
    "Use inline for to unroll a loop"
    "Write a generic data structure using anytype"

Error handling:
    "Write a function that returns an error union"
    "Use errdefer to clean up on failure"

Edge cases / long tail:
    "Use @Vector for SIMD operations"
    "Write a packed struct with specific bit layout"
    "Implement an async frame" (if applicable to 0.14)
```

### 8.2 Success Metrics

```
Tier 1 (must achieve):
    Basic syntax compilation rate     > 90%
    Basic syntax correctness          > 80%

Tier 2 (strong result):
    Standard library compilation      > 80%
    C interop compilation             > 70%
    Overall correctness               > 60%

Tier 3 (exceptional):
    Comptime patterns correct         > 50%
    Edge cases compile                > 40%
    Deterministic output              = 100% (guaranteed by integer arithmetic)
```

---

## 9. FUTURE EXPANSION

Things deliberately left out of v1 that could be added later:

```
- GPU acceleration via Vulkan compute shaders (integer kernels)
- Larger model (3B) if 1B proves the concept
- Additional languages (Rust, C++) if there's demand
- Lattice embeddings replacing learned embedding table
- Nested VFR for weights that need sub-shell precision
- Interactive REPL mode for live code assistance
- Fine-tuning on user's personal codebase
- Distributed training across multiple machines
```

None of these change the fundamental architecture. The integer arithmetic,
shell transitions, and octave system remain the same. They're extensions,
not redesigns.

---

## 10. SUMMARY

```
What:     1B parameter Zig+C code model
How:      Integer-only VFR shell training on CPU
Where:    64 GB RAM, no GPU required
Data:     5-10B tokens of Zig source, C libraries, technical docs
Time:     2-6 days training
Size:     ~7.6 GB weights on disk
Output:   A single Zig binary that generates Zig code
Eval:     Does the generated code compile? Does it pass tests?
Stack:    Zig all the way down. No Python. No floats. No dependencies.
```
