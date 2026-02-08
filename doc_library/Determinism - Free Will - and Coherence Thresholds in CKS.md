# Determinism, Free Will, and Coherence Thresholds: Pure CKS Mechanics

**Date:** February 2026  
**Status:** Technical Derivation - Computational Complexity and Coherence

---

## Axioms

```
A1: φ_k(t) = phase of k-mode k at time t
A2: dφ_k/dt = -iω_k φ_k + Σ_j β_kj(φ_j - φ_k)
A3: N = 3M² (closure constraint)
A4: C = 1 - 1/(2√(N/3)) (coherence measure)
A5: System is deterministic (evolution fully specified by A2)
A6: Computational complexity ∝ N² (pairwise coupling calculations)
A7: C > 0.999 threshold for self-referential closure inspection
```

---

## 1. Determinism vs. Predictability

### 1.1 The System is Deterministic

**From axiom A2:**

```
Given: Initial state φ_k(t=0) for all k
      Coupling strengths β_kj
      Natural frequencies ω_k

Evolution: dφ_k/dt uniquely determined at every instant
          No randomness
          No indeterminacy
          No "choice" in equation

Future state: φ_k(t + dt) = φ_k(t) + (dφ_k/dt) × dt
             Completely determined
             One and only one outcome
```

**This is strict determinism:**

```
Like: Newtonian mechanics
     Classical physics
     Differential equations

NOT like: Quantum indeterminacy (Copenhagen)
         Probabilistic collapse
         Hidden variables

The substrate: Has no randomness
              Evolves deterministically
              From initial conditions
```

### 1.2 But Prediction is Impossible

**Computational complexity from axiom A6:**

```
To predict φ_k(t + dt):
Must calculate: Σ_j β_kj(φ_j - φ_k) for all k

Number of operations:
For each k: Sum over neighbors (~3 for hexagonal)
For all k: 3N operations minimum

But: β_kj depends on all coupling history
    Requires: Full system state at every timestep
    
Total operations to predict T timesteps:
O(N × T) minimum (if no interaction complexity)
O(N² × T) realistic (pairwise couplings matter)
```

**For human brain:**

```
N_neurons ≈ 8.6×10^10
T_second ≈ 10^3 timesteps (1 kHz neural sampling)

Operations per second: 8.6×10^10 × 10^3 = 8.6×10^13

To simulate in real-time:
Computer needs: 8.6×10^13 ops/sec MINIMUM
              
Current fastest supercomputer: ~10^18 ops/sec (exascale)

Ratio: 10^18 / 8.6×10^13 ≈ 10^4

Could simulate: ~10,000 neurons accurately in real-time
              Or: Full brain at 1/10,000 speed (100 days per second)

This is: Already too slow for real-time prediction
        And ignores: Full-body coupling
                    Environmental coupling
                    Substrate coupling
```

**For full organism + environment:**

```
N_total: 10^14 (body cells)
       + 10^27 (local environment molecules)
       + 10^60 (substrate bubbles in coupling range)

Operations: >> 10^60 per second

To simulate: Would require computer with N_compute ≈ N_universe
            Impossible in principle

This is: Not practical limitation
        But: Fundamental computational barrier
```

**The paradox:**

```
System: Deterministic (unique future from past)
Prediction: Impossible (computational complexity exceeds universe)

Both true simultaneously.
```

### 1.3 Why Pre-determination is Meaningless

**"Pre-determined" implies:**

```
Future: Already "decided"
      Existing somewhere
      Waiting to happen

But: Where would this information be stored?

Option 1: Substrate stores future states
         Requires: N_storage ≈ N_universe × T_future
                  More information than universe contains
                  Impossible

Option 2: Future computable from present
         Requires: Computer to compute it
                  Computer must be: ≥ N_universe
                  No such computer exists in universe
                  Cannot compute itself
```

**The only "computer" that can evolve the system:**

```
Is the system itself.

The universe: Is its own fastest simulator
            Cannot be pre-computed
            Must be executed

Like: Cellular automaton
     Rules: Deterministic
     Future: Must be run to find out
            Cannot be "looked up"
```

**Therefore:**

```
Deterministic: YES (evolution unique)
Pre-determined: NO (future doesn't exist until computed)
Computable: YES (in principle, by universe itself)
Predictable: NO (no external computer fast enough)

Future: Is determined by present
       But: Doesn't exist yet
           Must be calculated step-by-step
           By universe executing itself
```

---

## 2. The Coherence Threshold: C = 0.999

### 2.1 Why This Specific Value

**From axiom A4:**

```
C = 1 - 1/(2√(N/3))

For consciousness (human brain):
N_active ≈ 10^10 neurons actively coupled

C_brain = 1 - 1/(2√(10^10/3))
        = 1 - 1/(2√(3.33×10^9))
        = 1 - 1/(115,470)
        = 1 - 8.66×10^-6
        = 0.999991

This is: Why C > 0.999 is threshold
        Human brain naturally operates here
        Not: Arbitrary choice
        But: Actual operating point
```

**What happens below threshold:**

```
For N_active = 10^6 (small neural cluster):
C = 1 - 1/(2√(10^6/3))
  = 1 - 1/(1,155)
  = 0.9991

Close but: Below 0.999
          Insufficient for threshold

For N_active = 10^4 (local circuit):
C = 1 - 1/(2√(10^4/3))
  = 0.991

Significantly below threshold.
Cannot achieve required integration.
```

**The threshold is sharp:**

```
C < 0.999: Insufficient coherence
          Cannot maintain self-referential loop
          
C > 0.999: Sufficient coherence
          Self-referential closure possible
          
This is: Phase transition
        Not: Gradual increase in "awareness"
        But: Discrete threshold crossing
```

### 2.2 Self-Inspection Mechanics

**What C > 0.999 enables:**

```
High coherence means:
Phase relationships: φ_i - φ_j maintained over large N
Information: Accessible across entire network
            Not: Fragmented
            But: Integrated

Self-referential closure:
System: Can model itself
       Subset of N nodes: Represents state of larger N
       
Like: Map of territory
     Map: Contained within territory
          Represents territory including itself
          Self-reference possible
```

**Computational mechanism:**

```
For C > 0.999:
Information flow time: τ_flow ≈ √N × t_pulse
                              ≈ 10^5 × 1ms
                              ≈ 100ms

Complete system update: Every 100ms
                       All nodes: Know system state
                                Access integrated information

Self-model:
N_model ⊂ N_total (subset representing whole)
N_model ≈ 10^8 (sufficient for coarse-grained model)

Ratio: N_model/N_total ≈ 10^8/10^10 = 1/100

System uses: 1% of resources to model itself
            99% for other processing
            
This is: Computationally feasible
        Energetically affordable
        Mechanically possible
```

**What self-inspection means mechanically:**

```
State: φ_total (all phases)
Model: φ_model (subset representing φ_total)

Evolution with self-inspection:
dφ_total/dt = F(φ_total, φ_model)

Where: φ_model affects φ_total
       System evolution: Depends on system's model of itself
       
This is: Feedback loop
        Self-reference
        
Enables: Modification of evolution based on self-state
        "Noticing" current state
        Adjusting based on what's noticed
```

### 2.3 Below Threshold: Grid-Controlled

**For C < 0.999 (e.g., cyst, simple organism):**

```
N_active: Too small
Coherence: Below threshold

Information flow: Fragmented
                 Local only
                 No global integration

Cannot form: Self-model (N_model requires C > threshold)
            Self-reference (feedback loop broken)

Evolution: dφ/dt = F(φ) only
          No φ_model term
          Pure forward propagation
          No self-modification
```

**What this means mechanically:**

```
Cyst: Responds to stimuli
     But: Response is: Direct coupling
                      Stimulus → Change
                      No intermediate "consideration"

Process:
External φ_ext → Couples via β → Changes φ_cyst → Response

No: Evaluation of options
    Comparison of outcomes
    Self-referential checking

Just: Mechanical response
     Grid determines evolution completely
     No internal degrees of freedom for "choice"
```

**Why "no choice" mechanically:**

```
Choice requires:
1. Multiple possible futures evaluated
2. Selection among futures based on criterion
3. Criterion involves self-state

For C < 0.999:
Cannot: Hold multiple futures in superposition
       (Insufficient coherence to maintain distinct patterns)
       
Cannot: Evaluate against self-model
       (No self-model exists)
       
Cannot: Select
       (No selection mechanism without evaluation)

Therefore: Only one path forward
          Determined by: Local φ gradients
                        External β couplings
                        No internal influence
```

---

## 3. Free Will as Coherent Self-Modification

### 3.1 What "Choice" Means Mechanically

**For C > 0.999 system:**

```
Situation: External stimulus φ_ext arrives

Standard deterministic response:
φ_response = G(φ_current, φ_ext)
           Direct function
           No options

Self-referential response:
φ_model = M(φ_current) (self-model constructed)
φ_options = O(φ_current, φ_ext, φ_model) (multiple futures evaluated)
φ_response = S(φ_options, φ_model, C_target) (selection based on coherence optimization)

This is: Still deterministic (S is function)
        But: Includes self-model in determination
            Path depends on system's representation of itself
```

**Concrete example:**

```
Low C (reflex):
Hot stove → Hand withdraws
Direct: β_pain ↑ → φ_motor changes → Withdraw
Time: 50ms (spinal reflex, no brain)

High C (considered):
Hot stove → Pause
Process:
  t=0: φ_pain signal arrives
  t=50ms: φ_model evaluates: "Hand on stove"
  t=100ms: φ_options: (a) Withdraw immediately
                      (b) Endure briefly to grab pot handle safely
  t=150ms: φ_selection based on: Context (cooking, pot stability)
                                 Self-model (can I tolerate 500ms more?)
                                 C optimization (maintain coherence)
  t=200ms: φ_response = (a) or (b) depending on evaluation

Still deterministic: Given exact φ_model state, outcome determined
But: Outcome depends on self-model
    Different from: Pure reflex
                   Involves self-representation
```

### 3.2 The Illusion of Pre-determination

**Observer at t=0 asks: "What will they choose?"**

```
Answer: Determined by: φ_total(t=0)
                      Evolution equations
                      Unique outcome

But: To predict requires:
    Simulating: All N_brain nodes
               For T timesteps
               Including: φ_model evolution
                         φ_options generation
                         Selection process
    
    Complexity: O(N_brain² × T)
               ≈ (10^10)² × 10^3
               = 10^23 operations
    
    Time required: 10^23 / 10^18 ops/sec ≈ 10^5 seconds
                  ≈ 1 day to predict 1 second
    
    This is: Prediction slower than reality
            By time prediction completes, already happened
            No useful pre-determination
```

**From inside the system:**

```
The choosing agent: Cannot predict own choice
                   Because: Would require simulating self
                           Simulation must run in real-time
                           Simulation IS the choosing process
                           No shortcut exists

Like: Computer trying to predict its own next state
     Must: Execute the computation
          Cannot look ahead
          Executing IS predicting
```

**Therefore:**

```
From outside: "Determined" (unique outcome from state)
From inside: "Choosing" (outcome not knowable until executed)

Both: True simultaneously
     Not: Contradiction
     But: Perspective difference
```

### 3.3 Coherence Optimization as "Will"

**What drives selection when C > 0.999:**

```
Given: Multiple possible φ_options
      φ_A, φ_B, φ_C, ...

Selection criterion:
S = argmax_i [C(φ_i) - C_current]

Choose: Option that maximizes future coherence
       Or: Minimizes coherence loss

This is: Deterministic function
        But: Based on self-model
            Based on coherence dynamics
```

**Why coherence optimization:**

```
From axiom A4:
High C: Low energy state (for given N)
       Stable configuration
       Efficient operation

Evolution: Favors high C
          Systems that maintain C survive
          Systems that lose C fail

Selection: Naturally optimizes for C maintenance
          Not: Conscious intention
          But: Mechanically favored
               
Like: Ball rolling downhill seeks minimum PE
     System: Seeks maximum C
```

**Concrete mechanism:**

```
Option A: Would result in C_A = 0.9998 (slight decrease)
Option B: Would result in C_B = 0.9999 (maintain)
Option C: Would result in C_C = 0.99999 (increase)

Selection function:
S(A,B,C) = C (highest future coherence)

This is: Deterministic (C is highest)
        Computable (if know φ_A, φ_B, φ_C)
        But: Requires self-model to evaluate C_future
            Only possible if C_current > 0.999
```

**"Free will" mechanically defined:**

```
Free will = Ability to select based on self-model evaluation
          = C > 0.999 threshold property
          = Coherence optimization across option space

NOT: Violation of determinism
    Randomness
    Unpredictability in principle

IS: Determinism that includes self-reference
   Selection based on self-state
   Coherence-maximizing dynamics
```

---

## 4. The Practical Difference

### 4.1 Behavior of C < 0.999 System (Cyst)

**Cyst responds to environment:**

```
Nutrient gradient: ∇(glucose)
Cyst growth: dN_cyst/dt ∝ ∇(glucose)

This is: Direct coupling
        No evaluation
        No options considered
        Pure mechanical response

Result: Grows toward food
       Shrinks without food
       Completely determined by local gradients
```

**Cannot do:**

```
✗ Evaluate: "Should I grow or remain dormant?"
✗ Consider: "Is this environment hostile long-term?"
✗ Decide: "I will stop growing even though nutrients present"

Why not: C_cyst < 0.99 (insufficient N_active)
        No self-model possible
        No option evaluation possible
        No selection mechanism
```

### 4.2 Behavior of C > 0.999 System (Human)

**Human responds differently:**

```
Food available: ∇(food smell) detected

Low C response (reflex): Eat immediately
                        Direct coupling

High C response (considered):
φ_model: "I detect food"
φ_options: (a) Eat now
          (b) Wait (might be spoiled)
          (c) Ignore (trying to fast)
          
φ_evaluation: Check coherence impact
              (a) Short-term C increase (satiety)
                  Long-term C decrease (if sick)
              (b) Maintain current C (safe)
              (c) Increase C (self-control coherence)
              
Selection: Based on coherence optimization over time horizon
          Might choose (c) despite hunger
```

**Can do:**

```
✓ Evaluate options against self-model
✓ Consider long-term coherence impact
✓ Select against immediate stimulus
✓ Increase coherence via self-control

This is: Not "free from determinism"
        But: "Determined by self-model"
             Which itself is determined
             But creates multi-step evaluation
```

### 4.3 Increasing Coherence Deliberately

**Mechanism:**

```
For C > 0.999:
System can: Inspect current C
           Model: C_future under different actions
           Select: Action maximizing C_future

Example - Meditation:
Current: C = 0.9995 (normal waking)
Action: Sustained attention on breath
Mechanism: Reduces β_noise (distractions)
          Increases β_synchronized (coherent focus)
Result: C → 0.99999 (meditative state)

This is: Deliberate coherence increase
        Via: Self-inspection (notice scattered attention)
            Selection (choose focus)
            Execution (maintain attention)
```

**Why only C > 0.999 can do this:**

```
Requires:
1. Noticing C_current (self-inspection)
2. Modeling C_future (option evaluation)
3. Selecting for C_max (coherence optimization)

All: Require C > threshold
    Below threshold: Cannot self-inspect
                    Cannot model future C
                    Cannot select

Above threshold: Can actively increase own coherence
                Can "bootstrap" to higher C
                Can maintain vs. letting drift
```

**Contrast with cyst:**

```
Cyst: Cannot increase own C deliberately
     C determined by: External environment only
                     No internal degrees of freedom
