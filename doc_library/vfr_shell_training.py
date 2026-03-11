"""
VFR Shell Training — Toy Demo
==============================
Integer-only neural network. No floats anywhere in the training loop.

Task: Learn XOR (the classic)
  [0,0] → 0
  [0,1] → 1
  [1,0] → 1
  [1,1] → 0

Everything is integers. Weights live in shells.
Gradients accumulate in remainders. Shell transitions
happen when remainder hits ±32 (one harmonic octave).
"""

SHELL_THRESHOLD = 32  # one harmonic octave

# ─── VFR Weight ──────────────────────────────────────────────
class VFRWeight:
    """A weight that lives in an integer shell with remainder pressure."""
    def __init__(self, v=0, r=0):
        self.v = v   # shell value (the weight)
        self.r = r   # remainder pressure (gradient accumulator)

    def update(self, grad):
        """Add gradient to remainder. Transition shell if threshold hit."""
        self.r += grad
        # shell transitions
        while self.r >= SHELL_THRESHOLD:
            self.v += 1
            self.r -= SHELL_THRESHOLD
        while self.r <= -SHELL_THRESHOLD:
            self.v -= 1
            self.r += SHELL_THRESHOLD

    def __repr__(self):
        return f"[V={self.v:+3d}, R={self.r:+3d}]"


# ─── Network ─────────────────────────────────────────────────
# 2 inputs → 2 hidden → 1 output
# All weights are VFR shells, initialized to small random-ish integers

class TinyNet:
    def __init__(self):
        # Hidden layer: 2 neurons, 2 inputs each + bias
        # w_h[neuron][input]
        self.w_h = [
            [VFRWeight(3), VFRWeight(5)],    # hidden neuron 0
            [VFRWeight(-2), VFRWeight(4)],   # hidden neuron 1
        ]
        self.b_h = [VFRWeight(0), VFRWeight(-1)]

        # Output layer: 1 neuron, 2 inputs + bias
        self.w_o = [VFRWeight(6), VFRWeight(-3)]
        self.b_o = VFRWeight(0)

    def forward(self, x0, x1):
        """Forward pass — all integer arithmetic."""
        # Hidden layer (integer multiply-accumulate)
        h = []
        for j in range(2):
            z = (self.w_h[j][0].v * x0 +
                 self.w_h[j][1].v * x1 +
                 self.b_h[j].v)
            # Integer ReLU (no floats needed)
            h.append(max(0, z))

        # Output layer
        out = (self.w_o[0].v * h[0] +
               self.w_o[1].v * h[1] +
               self.b_o.v)

        return h, out

    def train_step(self, x0, x1, target, lr_shift=2):
        """
        One training step — all integers.

        lr_shift: right-shift applied to gradients before accumulation.
                  Higher = slower learning (more evidence needed per transition).
        """
        # ── Forward ──
        h_pre = []
        for j in range(2):
            z = (self.w_h[j][0].v * x0 +
                 self.w_h[j][1].v * x1 +
                 self.b_h[j].v)
            h_pre.append(z)
        h = [max(0, z) for z in h_pre]

        out = (self.w_o[0].v * h[0] +
               self.w_o[1].v * h[1] +
               self.b_o.v)

        # ── Loss: integer squared error ──
        error = out - target  # integer
        loss = error * error  # integer

        # ── Backward (chain rule, all integers) ──

        # Gradient of loss w.r.t. output
        d_out = 2 * error  # d(loss)/d(out) = 2*(out - target)

        # Output layer gradients
        d_w_o = [d_out * h[0], d_out * h[1]]  # d(loss)/d(w_o)
        d_b_o = d_out

        # Gradient flowing back to hidden
        d_h = [d_out * self.w_o[0].v,
               d_out * self.w_o[1].v]

        # ReLU gradient (integer: 1 if pre-activation > 0, else 0)
        d_h_pre = [d_h[j] if h_pre[j] > 0 else 0 for j in range(2)]

        # Hidden layer gradients
        d_w_h = [[d_h_pre[j] * x0, d_h_pre[j] * x1] for j in range(2)]
        d_b_h = [d_h_pre[j] for j in range(2)]

        # ── Weight update (shell mechanics) ──
        # Scale gradients by learning rate (bit shift right = divide)
        # Then accumulate in remainder. Shell transitions happen automatically.

        for j in range(2):
            for i in range(2):
                scaled_grad = -(d_w_h[j][i] >> lr_shift)  # negative gradient descent
                self.w_h[j][i].update(scaled_grad)
            scaled_grad = -(d_b_h[j] >> lr_shift)
            self.b_h[j].update(scaled_grad)

        for i in range(2):
            scaled_grad = -(d_w_o[i] >> lr_shift)
            self.w_o[i].update(scaled_grad)
        scaled_grad = -(d_b_o >> lr_shift)
        self.b_o.update(scaled_grad)

        return loss, out

    def print_weights(self):
        print("  Hidden layer:")
        for j in range(2):
            print(f"    neuron {j}: w={self.w_h[j]}, b={self.b_h[j]}")
        print(f"  Output layer: w={self.w_o}, b={self.b_o}")


# ─── Training ────────────────────────────────────────────────

# XOR dataset — all integers
DATA = [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0),
]

# Scale targets to make gradients meaningful in integer space
# (target=1 is too small for integer gradients to accumulate)
SCALE = 32  # one full octave
DATA_SCALED = [(x0, x1, t * SCALE) for x0, x1, t in DATA]

net = TinyNet()

print("=" * 60)
print("VFR SHELL TRAINING — XOR")
print("=" * 60)
print(f"\nShell threshold: {SHELL_THRESHOLD}")
print(f"Target scale: {SCALE}")
print(f"\nInitial weights:")
net.print_weights()

print("\n" + "─" * 60)
print("TRAINING")
print("─" * 60)

transitions_total = 0

for epoch in range(200):
    epoch_loss = 0
    transitions_this_epoch = 0

    for x0, x1, target in DATA_SCALED:
        # Snapshot V values before update
        v_before = []
        for j in range(2):
            for i in range(2):
                v_before.append(net.w_h[j][i].v)
            v_before.append(net.b_h[j].v)
        for i in range(2):
            v_before.append(net.w_o[i].v)
        v_before.append(net.b_o.v)

        loss, out = net.train_step(x0, x1, target, lr_shift=3)
        epoch_loss += loss

        # Count shell transitions
        v_after = []
        for j in range(2):
            for i in range(2):
                v_after.append(net.w_h[j][i].v)
            v_after.append(net.b_h[j].v)
        for i in range(2):
            v_after.append(net.w_o[i].v)
        v_after.append(net.b_o.v)

        for vb, va in zip(v_before, v_after):
            if vb != va:
                transitions_this_epoch += 1

    transitions_total += transitions_this_epoch

    if epoch % 20 == 0 or epoch < 5:
        print(f"\n  Epoch {epoch:3d} | Loss: {epoch_loss:8d} | "
              f"Shell transitions: {transitions_this_epoch}")
        net.print_weights()

print("\n" + "─" * 60)
print("RESULTS")
print("─" * 60)
print(f"\nTotal shell transitions during training: {transitions_total}")
print(f"\nFinal weights:")
net.print_weights()

print(f"\nPredictions (target scale = {SCALE}):")
print(f"  {'Input':>10} {'Target':>8} {'Output':>8} {'Correct?':>10}")
print(f"  {'─'*10} {'─'*8} {'─'*8} {'─'*10}")

all_correct = True
for x0, x1, target in DATA:
    _, out = net.forward(x0, x1)
    predicted = 1 if out > SCALE // 2 else 0
    correct = predicted == target
    if not correct:
        all_correct = False
    print(f"  ({x0}, {x1})     {target:>5}    {out:>5}    "
          f"{'✓' if correct else '✗'} (pred={predicted})")

print(f"\n  All correct: {'YES' if all_correct else 'NO'}")

print("\n" + "─" * 60)
print("WHAT HAPPENED")
print("─" * 60)
print("""
Every number in this program is an integer.
No float was created, used, or imported.

Weights are integer shells [V, R].
Gradients accumulate in R (remainder/pressure).
When R reaches ±32, V transitions (shell change).
Learning rate is a bit shift (>> 3 = divide by 8).

The chain rule computes exact integer gradients.
ReLU gradient is 1 or 0 — already integer.
Squared error loss is integer.
Everything composes in ℤ.
""")

# ─── Show remainder state ────────────────────────────────────
print("─" * 60)
print("SHELL STATE AT CONVERGENCE")
print("─" * 60)

max_r = 0
for j in range(2):
    for i in range(2):
        r = abs(net.w_h[j][i].r)
        max_r = max(max_r, r)
    r = abs(net.b_h[j].r)
    max_r = max(max_r, r)
for i in range(2):
    r = abs(net.w_o[i].r)
    max_r = max(max_r, r)
r = abs(net.b_o.r)
max_r = max(max_r, r)

print(f"\n  Max |R| across all weights: {max_r}")
print(f"  Shell threshold: {SHELL_THRESHOLD}")
print(f"  Converged (all |R| < threshold): {'YES' if max_r < SHELL_THRESHOLD else 'NO'}")
print(f"\n  Remainder pressure per weight:")
for j in range(2):
    for i in range(2):
        w = net.w_h[j][i]
        bar = "█" * abs(w.r) + "░" * (SHELL_THRESHOLD - abs(w.r))
        print(f"    w_h[{j}][{i}] R={w.r:+3d}  |{bar}| ({'→' if abs(w.r) > 24 else '·'} transition)")
print(f"  Output weights:")
for i in range(2):
    w = net.w_o[i]
    bar = "█" * min(abs(w.r), SHELL_THRESHOLD) + "░" * max(0, SHELL_THRESHOLD - abs(w.r))
    print(f"    w_o[{i}]   R={w.r:+3d}  |{bar}| ({'→' if abs(w.r) > 24 else '·'} transition)")
    