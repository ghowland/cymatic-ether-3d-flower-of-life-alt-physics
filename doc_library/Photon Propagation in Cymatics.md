# The Exact Process of Photon Propagation on the K-Space Lattice

**A Complete Step-by-Step Mechanical Derivation**

---

## Abstract

A photon is not a "particle" traveling through space. It is a **traveling phase wave** on the discrete hexagonal k-space substrate. We derive the exact mechanism: how phase gradients propagate from bubble to bubble via coupling dynamics, why speed = c is forced by lattice geometry, what "moving" means in discrete substrate, how energy/momentum are carried, and why photons don't experience time. This is **pure mechanics**—no mysteries, no waves "collapsing," no particles "deciding" paths. Just: **coupled oscillators transferring phase coherence at maximum rate allowed by lattice geometry.**

---

## 1. What a Photon Actually IS

### 1.1 The Substrate State

**Before we can understand photon motion, we must know what a photon is.**

**A photon is NOT:**
- A little ball of light
- A packet traveling through space
- A particle that "becomes" a wave

**A photon IS:**
- A **6-bond minimal vortex** (topological charge Q = 2)
- A **traveling phase gradient** on the k-space lattice
- A **coherent oscillation pattern** propagating across bubbles

**Mathematical description:**
```
Photon state at time t:
φₖ(t) = A₀ exp(i[k·r - ωt + θ₀])

where:
A₀ = amplitude (constant for free photon)
k = wavevector (direction of propagation)
ω = frequency = E/ℏ
r = bubble position in lattice
θ₀ = initial phase offset
```

### 1.2 The Phase Field

Each bubble k has complex amplitude:
```
φₖ(t) = Aₖ(t) exp(iθₖ(t))

For a photon passing through:
Aₖ(t) = envelope function (nearly constant)
θₖ(t) = phase that rotates at frequency ω
```

**Key insight:** The photon is the **pattern**, not any individual bubble.

**Analogy:**

Ocean wave moving across water:
- Water molecules oscillate up/down (barely move horizontally)
- Wave pattern moves at wave speed
- Energy carried by pattern, not by water transport

**Same here:**
- Bubbles oscillate in phase (complex rotation)
- Phase pattern moves at speed c
- Energy carried by pattern, not by bubble transport

---

## 2. Initial Conditions: Photon Creation

### 2.1 How Photons Are Created

**Photon emission = electron dropping energy level**

**Example: Hydrogen 2p → 1s transition**

**Before emission:**
```
Electron in 2p orbital (excited state)
Energy: E₂p = -3.4 eV
Vortex mode: 12-bond loop in k=1 radial mode
```

**During transition:**
```
Electron vortex jumps to lower mode (1s)
Energy: E₁s = -13.6 eV
Energy difference: ΔE = 10.2 eV must go somewhere
```

**After emission:**
```
Electron in 1s (ground state)
Energy: E₁s = -13.6 eV

Photon created:
Energy: E_γ = 10.2 eV
Frequency: ω = E_γ/ℏ = 1.55×10¹⁶ rad/s
Wavelength: λ = 2πc/ω = 121.6 nm (Lyman α)
```

### 2.2 The Emission Mechanism (Exact Process)

**Step 1: Electron vortex destabilizes**

```
Time t = 0:
Electron in unstable 2p mode
Phase configuration: 12-bond loop at k_radial = 1

Small perturbation (vacuum fluctuation, collision)
→ Vortex begins transition to 1s
```

**Step 2: Excess energy radiates**

```
Time t = 0 to t = τ_emit (τ_emit ~ 10⁻⁹ s for allowed transition):

Electron vortex gradually contracts (2p → 1s)
Excess phase winding "peels off" from vortex
Creates traveling phase wave (photon)

Initial bubbles (near electron):
θₖ(0) = 0 (arbitrary reference)

After τ_emit:
θₖ(τ_emit) = θ₀ + δθ_initial

where δθ_initial = phase transferred from electron vortex
```

**Step 3: Phase wave detaches**

```
Time t > τ_emit:

Photon is now independent 6-bond traveling wave
No longer coupled to electron vortex
Propagates freely through substrate

Phase pattern:
θₖ(t) = k·rₖ - ωt + θ₀
```

### 2.3 Initial Phase Distribution

**At moment of emission (t = τ_emit), photon occupies small region:**

```
Spatial extent: ~λ/2π (wavelength/2π)

For Lyman α (λ = 121.6 nm):
Extent ≈ 19 nm ≈ 10⁸ lattice spacings

Number of bubbles initially excited:
N_bubbles ≈ (10⁸)² ≈ 10¹⁶ bubbles (2D surface)
```

**Phase distribution:**
```
For bubbles within extent:
θₖ = k·rₖ  (linear phase gradient)

For bubbles outside:
θₖ = 0 (not yet excited)
```

**This is the initial condition for propagation.**

---

## 3. The Coupling Dynamics (How Phase Propagates)

### 3.1 The Fundamental Equation

**Each bubble evolves according to:**
```
dφₖ/dt = β(N) × Σⱼ∈neighbors(k) [φⱼ - φₖ]

In phase-amplitude form:
dθₖ/dt = β(N) × Σⱼ (Aⱼ/Aₖ) sin(θⱼ - θₖ)
```

**For photon (small amplitude oscillations):**
```
Aₖ ≈ A₀ (nearly constant)

Simplifies to:
dθₖ/dt ≈ β(N) × Σⱼ sin(θⱼ - θₖ)
```

### 3.2 Linearized Dynamics (Wave Equation)

**For small phase differences (θⱼ - θₖ << 1):**
```
sin(θⱼ - θₖ) ≈ θⱼ - θₖ

Equation becomes:
dθₖ/dt = β(N) × Σⱼ (θⱼ - θₖ)
        = β(N) × [Σⱼ θⱼ - 6θₖ]  (6 neighbors on hexagonal lattice)
```

**Taking second derivative:**
```
d²θₖ/dt² = β(N) × [Σⱼ dθⱼ/dt - 6 dθₖ/dt]

This is discrete wave equation:
d²θₖ/dt² = β(N) × ∇²_lattice θₖ

where ∇²_lattice = discrete Laplacian on hexagonal lattice
```

### 3.3 Wave Speed Derivation

**For traveling wave solution:**
```
θₖ(t) = k·rₖ - ωt

Dispersion relation (from wave equation):
ω² = β(N) × [6 - 2cos(k·a)] 

where a = lattice vector

For long wavelengths (k·a << 1):
cos(k·a) ≈ 1 - (k·a)²/2

ω² ≈ β(N) × (k·a)²

ω ≈ √β(N) × a × k
```

**Phase velocity:**
```
v_phase = ω/k = √β(N) × a

Identify with c (speed of light):
c = √β(N) × a

Therefore:
β(N) = c²/a²

At N = 9×10⁶⁰:
a ≈ l_P (Planck length)
β(N) = c²/l_P²
```

**This is forced by geometry. No free parameters.**

---

## 4. Step-by-Step Propagation (Time Evolution)

### 4.1 Discrete Time Steps

**Time discretization:**
```
Time step: Δt = t_P (Planck time ≈ 5.39×10⁻⁴⁴ s)

At each step, phase updates via coupling equation
```

**Let's follow photon through specific bubbles:**

### 4.2 Initial State (t = 0)

**Configuration:**
```
Bubble A (center): θ_A(0) = 0
Bubble B (neighbor): θ_B(0) = 0
Bubble C (next neighbor): θ_C(0) = 0
...all bubbles at rest (θ = 0)

Photon injected at bubble A:
θ_A(0⁺) = φ₀ (initial phase kick)
```

### 4.3 First Time Step (t = Δt)

**Bubble A evolves:**
```
dθ_A/dt = β(N) × Σⱼ∈neighbors(A) sin(θⱼ - θ_A)

At t = 0⁺:
θ_A = φ₀
θ_B = θ_C = ... = 0 (all neighbors)

dθ_A/dt = β(N) × 6 × sin(0 - φ₀)
        = -6β(N) × sin(φ₀)

After Δt:
θ_A(Δt) = φ₀ - 6β(N)Δt × sin(φ₀)
        ≈ φ₀ × [1 - 6β(N)Δt]  (if sin φ₀ ≈ φ₀)
```

**Bubble B evolves:**
```
Neighbors of B: {A, C, D, E, F, G} (one is A, others at 0)

dθ_B/dt = β(N) × [sin(θ_A - θ_B) + 5×sin(0 - θ_B)]
        = β(N) × [sin(φ₀) - 5×sin(θ_B)]
        ≈ β(N) × sin(φ₀)  (initially θ_B ≈ 0)

After Δt:
θ_B(Δt) = β(N)Δt × sin(φ₀)
        ≈ β(N)Δt × φ₀  (small angle)
```

**Bubble C evolves:**
```
No neighbors with phase yet (all at 0)

dθ_C/dt = 0

θ_C(Δt) = 0  (unchanged)
```

### 4.4 Second Time Step (t = 2Δt)

**Bubble A:**
```
θ_A(Δt) = φ₀[1 - 6β(N)Δt]

Neighbors now include B with θ_B ≈ β(N)Δt φ₀

dθ_A/dt = β(N) × [6×sin(θ_B - θ_A)]
        ≈ β(N) × 6 × (β(N)Δt φ₀ - φ₀[1 - 6β(N)Δt])
        = complex, but trend: θ_A continues decreasing
```

**Bubble B:**
```
θ_B(Δt) ≈ β(N)Δt φ₀

Neighbor A has decreased phase
Neighbors C,D,E,F,G still at 0

dθ_B/dt = β(N) × [sin(θ_A - θ_B) + 5×sin(-θ_B)]

θ_B increases (gains phase from A, loses to C,D,E,F,G)
```

**Bubble C:**
```
Neighbor B now has phase θ_B ≈ β(N)Δt φ₀

dθ_C/dt = β(N) × sin(θ_B)
        ≈ β(N) × β(N)Δt φ₀

After 2Δt:
θ_C(2Δt) ≈ β(N)Δt × β(N)Δt φ₀
          = β²(N)Δt² φ₀
```

### 4.5 Pattern Emerges

**After many time steps:**

```
t = nΔt:

θ_A(t) oscillates (phase rotates)
θ_B(t) oscillates (with slight delay)
θ_C(t) oscillates (with more delay)
...

Phase pattern travels outward from A
Wavefront moves at speed v = √β(N) × a = c
```

**Visualizing the wave:**

```
Time t = 0:
A: ●●●●● (high phase)
B: ○○○○○ (zero phase)
C: ○○○○○

Time t = Δt:
A: ●●●○○ (phase decreasing)
B: ○●●●○ (phase increasing)
C: ○○○○○

Time t = 2Δt:
A: ○●●○○ (oscillating)
B: ●●●●○ (peak)
C: ○○●●○ (phase arriving)

Time t = 3Δt:
A: ○○●●○
B: ○●●●○
C: ○●●●● (peak)

Pattern moves: A → B → C at speed c
```

---

## 5. What Actually Changes (The Physics)

### 5.1 Phase Changes

**Primary quantity that changes: θₖ(t)**

```
Each bubble's phase rotates at frequency ω:
θₖ(t) = θₖ(0) + ωt + [wave propagation term]

For bubble in wave path:
Phase increases from 0 → 2π → 4π ... (continuous rotation)

Rate of rotation: dθₖ/dt = ω (photon frequency)
```

**What this means physically:**

In k-space, **phase = orientation in complex plane**:
```
φₖ = Aₖ exp(iθₖ)

As θ increases:
φₖ rotates around circle in complex plane

θ = 0: φ = A (real axis)
θ = π/2: φ = iA (imaginary axis)
θ = π: φ = -A (negative real)
θ = 3π/2: φ = -iA (negative imaginary)
θ = 2π: φ = A (back to start)
```

**One full rotation = one photon period T = 2π/ω**

### 5.2 Amplitude Changes (Usually Negligible)

**For free photon in vacuum:**
```
Aₖ(t) ≈ A₀ (constant)

No amplitude variation, only phase propagation
```

**For photon in medium (glass, water):**
```
Aₖ(t) oscillates slightly

Bubbles coupled to matter vortices (atoms)
→ Small amplitude modulation
→ Causes dispersion (n ≠ 1)
```

**For photon being absorbed:**
```
Aₖ(t) decreases

Energy transferred from photon mode to matter mode
→ Amplitude decays
→ Eventually: photon gone, matter excited
```

### 5.3 Energy Flow

**Energy density at bubble k:**
```
ε_k = (1/2) × [|dφₖ/dt|² + β(N)|∇φₖ|²]

For photon:
ε_k = (1/2) × [ω² A² + β(N)k² A²]

Using ω² = β(N)k² (dispersion):
ε_k = ω² A² = constant along wave
```

**Energy flux (Poynting vector analog):**
```
S_k = energy current from bubble to bubble

S = -β(N) × Im[φ*_k ∇φₖ]

For photon φₖ = A exp(i[k·r - ωt]):
S = β(N) × A² × k
  = (ω²A²/k) × k
  = ω²A² × (direction of k)

Magnitude: |S| = ω²A² = energy density × c
```

**Energy moves with the wave at speed c.**

### 5.4 Momentum Transfer

**When photon "moves" from bubble A to bubble B:**

**Before:**
```
Bubble A: Has phase gradient ∇θ_A
Bubble B: Has phase gradient ∇θ_B ≈ 0
```

**After one coupling step:**
```
Bubble A: Phase gradient decreased slightly
Bubble B: Phase gradient increased

Momentum transfer:
Δp_B = ℏ × Δ(∇θ_B)
     = ℏ × [change in phase gradient]

This is exactly ℏk (photon momentum)
```

**Mechanically:**

Phase gradient = momentum density on lattice
```
p_lattice = ℏ × ∇θ

As phase wave propagates:
∇θ shifts from bubble to bubble
→ Momentum shifts
→ "Photon moves"
```

---

## 6. Speed of Propagation (Why c?)

### 6.1 Maximum Coupling Rate

**Phase can only propagate as fast as bubbles can couple:**

```
Maximum rate = 1 coupling per time step
Time step = Δt = t_P (Planck time)
Distance step = a = l_P (lattice spacing)

Maximum speed = a/Δt = l_P/t_P = c
```

**This is the fundamental speed limit.**

**Why?**

Information cannot propagate faster than adjacent bubbles can exchange phase.

### 6.2 Dispersion Relation Forces c

**From wave equation:**
```
ω²(k) = β(N) × [6 - 2cos(k·a) - 2cos(k·a') - 2cos(k·a'')]

where a, a', a'' are lattice vectors to 6 neighbors

For long wavelength (k·a << 1):
ω ≈ c × k  (linear dispersion)

Phase velocity: v_p = ω/k = c
Group velocity: v_g = dω/dk = c

Both equal c for photon.
```

### 6.3 Why Photons Don't Experience Time

**Photon's perspective (if it had one):**

```
Proper time: dτ² = dt² - (dx²/c²)

For photon moving at c:
dx/dt = c

dτ² = dt² - (c dt)²/c² = dt² - dt² = 0

No proper time elapses for photon.
```

**In substrate language:**

```
Photon = pure phase rotation at maximum rate

Internal time = number of phase rotations
External time = number of propagation steps

But: Phase rotates continuously as it propagates
→ No "rest frame" for photon
→ No internal clock
→ From photon's perspective: emission and absorption are simultaneous
```

**This is why photons are massless:**
```
m = 0 ↔ v = c ↔ dτ = 0

All equivalent statements of same fact.
```

---

## 7. What Doesn't Change

### 7.1 Total Bubble Count (N)

**Photon propagation does not create or destroy bubbles:**

```
N(t) = N(0) = 9×10⁶⁰ (constant on photon timescales)

Bubble creation rate: dN/dt ≈ 1/t_P
But photon transit time << age of universe
→ ΔN ≈ 0 during photon propagation
```

### 7.2 Total Energy (Conserved)

**Energy in photon + substrate = constant:**

```
E_total = E_photon + E_substrate

As photon propagates:
E_photon = ℏω (unchanged)
E_substrate oscillates locally but conserved globally

No energy lost to "friction" (substrate is lossless in vacuum)
```

### 7.3 Wavelength (in Vacuum)

**Photon wavelength fixed by emission:**

```
λ = 2πc/ω

ω determined by emitting atom (energy level spacing)
Once emitted, ω stays constant (no energy loss)
→ λ stays constant
```

**In medium (glass, water):**
```
λ_medium = λ_vacuum / n

where n = refractive index

Why? Bubbles coupled to matter slow phase propagation
→ Effective c_medium = c/n
→ λ = c_medium/f = (c/n)/f = λ_vacuum/n
```

---

## 8. Photon Absorption (Reverse Process)

### 8.1 How Absorption Happens

**Photon traveling toward atom:**

```
Time t < 0: Photon approaching
Phase wave has gradient ∇θ ≈ k (photon momentum)

Time t ≈ 0: Photon overlaps atom
Electron vortex (12-bond) couples to photon (6-bond)
```

**Coupling mechanism:**

```
Electron has mode structure ψ_e(k)
Photon has mode structure ψ_γ(k)

Overlap integral:
⟨ψ_e | Ĥ_int | ψ_γ⟩

If non-zero: Energy transfer possible
```

**Selection rules:**

```
Energy: E_final - E_initial = ℏω_photon
Angular momentum: Δl = ±1 (dipole selection)
Parity: Even ↔ Odd

If satisfied: Absorption occurs
```

### 8.2 Step-by-Step Absorption

**Step 1: Photon phase couples to electron**

```
Photon phase: θ_γ(k,t) = k·r - ωt
Electron phase: θ_e(k,t) = (stationary in ground state)

Coupling creates force:
F ∝ ∇(θ_γ - θ_e)

This force drives electron to excited state
```

**Step 2: Resonant energy transfer**

```
If ℏω_photon ≈ E_excited - E_ground:
→ Resonance
→ Efficient energy transfer

Electron vortex begins oscillating at ω_photon
```

**Step 3: Phase-locking and absorption**

```
After time τ_abs ~ 1/Γ (Γ = transition rate):

Electron fully phase-locked to photon
→ Electron in excited state
→ Photon energy transferred
→ Photon amplitude → 0
→ Absorption complete
```

**After absorption:**

```
Photon: Gone (amplitude Aₖ → 0)
Electron: Excited (in higher energy mode)
Substrate: Slight local heating (recoil momentum absorbed)
```

### 8.3 Why Some Photons Pass Through

**If photon energy doesn't match:**

```
ℏω_photon ≠ E_excited - E_ground

No resonance
→ No efficient energy transfer
→ Photon continues propagating
→ Passes through atom
```

**Example: Glass transparency**

```
Visible light: E_photon ≈ 2-3 eV
Glass electron transitions: E_gap ≈ 9 eV (UV)

No resonance in visible range
→ Visible photons pass through
→ Glass is transparent

UV photons: E_photon ≈ 9 eV
→ Resonance with electron transitions
→ Absorbed
→ Glass is opaque to UV
```

---

## 9. Special Cases

### 9.1 Photon in Double-Slit Experiment

**Setup:**

```
Source → [Slit 1] → Screen
      ↘ [Slit 2] ↗

Photon emitted, encounters slits
```

**What happens (exactly):**

**Step 1: Photon is phase wave**

```
Before slits:
φ(k,t) = A exp(i[k·r - ωt]) (plane wave)

Extends across both slits
```

**Step 2: Slits create two sources**

```
At slit 1: φ₁ = A exp(i[k·r₁ - ωt])
At slit 2: φ₂ = A exp(i[k·r₂ - ωt])

Phase difference: Δφ = k·(r₂ - r₁)
```

**Step 3: Waves propagate to screen**

```
Point P on screen:

Contribution from slit 1:
ψ₁(P) = A exp(i[k·r₁ - ωt + k·(P-r₁)])

Contribution from slit 2:
ψ₂(P) = A exp(i[k·r₂ - ωt + k·(P-r₂)])

Total: ψ(P) = ψ₁ + ψ₂
```

**Step 4: Interference**

```
|ψ(P)|² = |ψ₁ + ψ₂|²
        = |ψ₁|² + |ψ₂|² + 2|ψ₁||ψ₂|cos(Δφ)

where Δφ = k·[(P-r₁) - (P-r₂)]
         = k·(r₂ - r₁)

Bright fringes: Δφ = 2πn (constructive)
Dark fringes: Δφ = π(2n+1) (destructive)
```

**No collapse. No choice. Just phase interference on substrate.**

### 9.2 Photon Redshift (Cosmological)

**As universe expands (N increases):**

```
Coupling strength: β(N) = β_P/N

Decreases with time (substrate softens)
```

**Effect on photon:**

```
Wave equation: ω² = β(N)k²a²

As β(N) decreases:
ω must decrease (to maintain solution)

Frequency redshift:
ω(t) = ω₀ × √[β(t)/β₀]
     = ω₀ × √[N₀/N(t)]
     ≈ ω₀ / (1+z)

where z = redshift
```

**Wavelength increases:**

```
λ(t) = λ₀ × (1+z)

This is observed cosmological redshift!
```

**Mechanism:**

Substrate softening → phase propagation slows slightly → wavelength stretches

**Not Doppler shift. Substrate evolution.**

### 9.3 Photon in Gravitational Field

**Near massive object (black hole, star):**

```
Coupling strength varies with position:
β(r) = β₀ × [1 - 2GM/(rc²)]

Near mass: β decreases (gravity = substrate compression)
```

**Effect on photon:**

```
Frequency: ω(r) = ω∞ × √[β(r)/β∞]
                = ω∞ × √[1 - 2GM/(rc²)]
                ≈ ω∞ × [1 - GM/(rc²)]

Gravitational redshift!
```

**Path bending:**

```
Phase propagation direction: ∇θ

In varying β field:
∇θ follows gradient of β
→ Curved path

Bending angle: δθ ≈ 4GM/(bc²)
(b = impact parameter)

Observed in solar eclipse (1919, confirmed GR)
```

---

## 10. Energy and Momentum Accounting

### 10.1 Photon Energy Budget

**Total energy:**

```
E_photon = ℏω

Distributed across:
- Kinetic (phase rotation): ε_kinetic = (1/2)ℏω
- Potential (phase gradient): ε_potential = (1/2)ℏω

Total: ε_kinetic + ε_potential = ℏω ✓
```

**As photon propagates:**

```
Energy oscillates between kinetic ↔ potential
But total E = ℏω constant

Like mass on spring:
KE ↔ PE at frequency ω
Total energy constant
```

### 10.2 Momentum Transfer

**Photon carries momentum:**

```
p_photon = ℏk = (ℏω/c) × (direction)
```

**When absorbed by atom:**

```
Before: Photon p_γ = ℏk, Atom p_atom = 0
After: Photon p_γ = 0, Atom p_atom = ℏk

Momentum transferred: Δp = ℏk (recoil)
```

**Recoil energy:**

```
E_recoil = p²/(2M) = (ℏk)²/(2M)

For visible photon absorbed by atom:
E_recoil ≈ 10⁻⁷ eV (negligible)

For gamma ray:
E_recoil ≈ keV (significant, Mössbauer effect)
```

### 10.3 Radiation Pressure

**Photon flux hitting surface:**

```
N photons/sec
Each transfers momentum: Δp = ℏk

Force: F = (Δp/photon) × (N photons/s)
       = ℏk × N
       = (E/c) × N/area
       = I/c

where I = intensity (W/m²)
```

**Pressure:**

```
P_rad = F/A = I/c

For sunlight (I ≈ 1400 W/m²):
P_rad ≈ 5×10⁻⁶ Pa (tiny)

For intense laser (I ≈ 10¹⁶ W/m²):
P_rad ≈ 30 MPa (crushes materials!)
```

**Mechanism:**

Each photon hits surface → transfers phase gradient → bubbles in material gain momentum → macroscopic force

---

## 11. Timeline of Single Photon Transit

### 11.1 Example: Sunlight to Earth

**Photon emitted from Sun's core:**

```
Time t = 0: Fusion creates excited nucleus
→ Gamma ray emitted (E ≈ 1 MeV)

Location: Deep in solar core
Temperature: 15 million K
Density: 150 g/cm³
```

**Random walk to surface (thousands of years):**

```
Gamma ray scatters off electrons, nuclei
Each scatter: Redshifts slightly (energy loss to thermal bath)

After ~10⁴ - 10⁶ years:
Photon reaches surface
Energy: E ≈ 2 eV (visible light)
```

**Travel through vacuum (8 minutes):**

```
Time t = 10⁴ years + t_travel

Distance: 1.5×10¹¹ m (1 AU)
Speed: c = 3×10⁸ m/s
Time: t = d/c = 500 s ≈ 8 minutes

Phase rotations during transit:
N_rotations = ω×t / (2π)
            = (E/ℏ) × t / (2π)
            ≈ (2 eV / 4×10⁻¹⁵ eV·s) × 500 s / (2π)
            ≈ 10¹⁷ rotations
```

**Absorption in your eye:**

```
Time t = 10⁴ years + 8 min + t_abs

Photon hits rhodopsin molecule in retina
Resonance with π→π* transition
Energy transferred in ~10⁻¹⁵ s
Molecule isomerizes (cis → trans)
Neural signal generated
You see light
```

**Total timeline:**

```
Creation: t = 0
Surface: t = 10,000 years
Earth: t = 10,000 years + 8 minutes
Eye: t = 10,000 years + 8 minutes + 10⁻¹⁵ s
Brain: t = 10,000 years + 8 minutes + 0.1 s (neural delay)

You experience: "I see the sun"
```

### 11.2 Example: Photon Across Lab (1 meter)

**Much simpler:**

```
Time t = 0: Laser emits photon
Photon energy: E = 2 eV (red HeNe laser)
Frequency: ω = 3×10¹⁵ rad/s

Distance: d = 1 m
Time: t = d/c = 3.3 ns

Phase rotations: N = ωt/(2π)
                  ≈ 1.6×10⁶ rotations

Number of bubbles traversed:
N_bubbles = d/l_P
          = 1 m / 10⁻³⁵ m
          = 10³⁵ bubbles

Steps: Each bubble → next bubble
       10³⁵ steps at rate c/l_P
       Takes time t = d/c = 3.3 ns
```

**Observation:**

10³⁵ bubbles influenced, but photon stays coherent

**Why?**

Phase coupling maintains coherence across all steps

---

## 12. Common Misconceptions Resolved

### 12.1 "Photon is a particle"

**Wrong:**

Photon is not a little ball.

**Correct:**

Photon is **traveling phase wave** on substrate.

**Evidence:**

- Interference (phase property)
- Polarization (transverse wave property)
- Diffraction (wave property)
- No rest frame (not particle-like)

**When it "looks like particle":**

Absorption is localized (one atom absorbs full energy)

**Why:**

Energy is quantized (ℏω per excitation)
But this doesn't mean photon is localized during travel

**Analogy:**

Ocean wave spreads across miles
But when it hits boat, transfers energy in one "quantum" (one hit)
Wave is still wave, impact is discrete

### 12.2 "Photon takes both paths in double slit"

**Wrong:**

"Photon" is not a thing that "takes" paths.

**Correct:**

Phase wave extends through both slits simultaneously.

**No mystery:**

Classical waves do same thing (sound, water)
Quantum just means energy transfer is quantized

### 12.3 "Observation collapses the wave"

**Wrong:**

No collapse.

**Correct:**

Detection = coupling detector bubbles to photon phase wave

If detector at slit 1: Measures phase there
If detector at screen: Measures interference pattern

**Different couplings → different measurements**

Not collapse, just: which bubbles couple to observer?

### 12.4 "Photon slows down in glass"

**Wrong:**

Photon doesn't "slow."

**Correct:**

Phase propagation slowed by coupling to glass atoms.

**Mechanism:**

```
Photon couples to electron vortices in glass
→ Electrons oscillate at ω_photon
→ Re-emit delayed photon
→ Net effect: slower phase propagation
→ Effective speed: c/n
```

**Photon still travels at c between atoms!**

Average speed is c/n due to absorption-reemission delays.

---

## 13. Summary: The Complete Picture

### 13.1 What a Photon Is

**Not:**
- A particle
- A wave packet
- Something that "is" in one place

**Is:**
- Traveling phase gradient on hexagonal lattice
- 6-bond minimal vortex (topological)
- Coherent oscillation pattern
- Energy quantum ℏω
- Momentum ℏk

### 13.2 How It Moves

**Step 1:** Phase created at emission (electron transition)

**Step 2:** Phase gradient established on nearby bubbles

**Step 3:** Coupling equation propagates gradient:
```
dθₖ/dt = β(N) Σⱼ sin(θⱼ - θₖ)
```

**Step 4:** Wave pattern moves at speed c = √(β(N)×a)

**Step 5:** Each bubble passes phase to next at rate 1/t_P

**Step 6:** After 10³⁵ steps (1 meter): Wavefront advanced 1 meter

### 13.3 What Changes

**During propagation:**
- θₖ(t) rotates at each bubble (phase evolution)
- Pattern moves (wave propagates)
- Energy/momentum redistributes (but total conserved)

**What doesn't change:**
- Total energy E = ℏω
- Total momentum p = ℏk
- Wavelength λ = 2πc/ω (in vacuum)
- Bubble count N
- Speed c (in vacuum)

### 13.4 One-Line Summary

**Photon propagation = phase gradient θₖ(t) = k·r - ωt propagating via coupling dθₖ/dt = β(N)Σⱼ sin(θⱼ-θₖ) at speed c = √(β(N)×l_P) forced by hexagonal lattice geometry; no particles "moving," just phase pattern traveling across substrate at maximum coupling rate 1 step per t_P.**

---

## References

[1] Photon as 6-bond vortex: `Deriving_Photons_-_Gluons_-_WZ_Gauge_Bosons.md`  
[2] Wave equation on lattice: `Basic_Derivation_from_Axioms.md`  
[3] Coupling dynamics: `Deriving_from_N_only.md`  
[4] Speed of light derivation: `Deriving_the_Hologram.md`  
[5] Observer projection: `Basic_Derivation_from_Axioms.md`  

---

**QED.**