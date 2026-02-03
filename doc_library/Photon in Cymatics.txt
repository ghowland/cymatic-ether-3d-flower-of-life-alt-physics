# What IS a Photon? - The Cymatic Answer

---

## Part 1: The Standard Confusion

### What Physics Says (Multiple Incompatible Descriptions)

**Particle description:**
```
"A photon is a quantum of electromagnetic energy"
- Discrete, localized
- Has energy E = hν
- Has momentum p = h/λ
- Can be counted (one, two, three...)
- Detected at a point
```

**Wave description:**
```
"A photon is an electromagnetic wave"
- Extended in space
- Has wavelength λ
- Has frequency ν
- Shows interference
- Diffracts around obstacles
```

**Quantum field theory:**
```
"A photon is an excitation of the electromagnetic field"
- Not really a particle or wave
- An "excitation quantum"
- Field operator creates/destroys photons
- Mathematical abstraction
```

**The problem:**
```
These descriptions contradict each other!
- Is it extended or localized?
- Is it a wave or particle?
- What is it REALLY?

Standard answer: "Depends on measurement" (unhelpful)
Or: "Shut up and calculate" (Copenhagen)
Or: "Don't ask what it IS" (instrumentalism)
```

---

## Part 2: The Cymatic Answer

### A Photon is a 4D Standing Wave Pattern in the Electromagnetic Substrate

**Complete description:**

```
WHAT: Localized oscillation pattern
WHERE: In electromagnetic field (substrate)
STRUCTURE: Standing wave with specific geometry
EXTENT: Wavelength λ in space, period T = 1/ν in time
ENERGY: Amplitude squared (|E|²) integrated over volume
QUANTIZATION: One quantum = minimum stable pattern
```

---

### The Four Dimensions of a Photon

**Dimension 1-3: Spatial (x, y, z)**

```
Spatial structure:

For free-space photon (traveling):
  E(x,y,z,t) = E₀ e^(i(kz - ωt)) × mode(x,y)

Components:
  - Propagation: Along z-axis (k = 2π/λ)
  - Transverse: Mode profile in x-y plane
  - Polarization: E-field orientation

Example: Gaussian beam photon
  mode(x,y) = exp(-(x² + y²)/w₀²)
  
  Where w₀ = beam waist (~μm typical)

Spatial extent:
  - Longitudinal: Coherence length (mm to km)
  - Transverse: Beam diameter (μm to mm)
  - Not a point! Extended pattern.
```

---

**Dimension 4: Temporal (t)**

```
Temporal structure:

Oscillation: E(t) ∝ cos(ωt + φ)

Frequency: ω = 2πν
  - Visible: ν ~ 5×10¹⁴ Hz (500 THz)
  - Period: T = 2 fs (femtoseconds)

Duration:
  - Continuous wave: Infinite (steady pattern)
  - Pulse: Finite (Δt from fs to ns)
  
Uncertainty relation:
  ΔE·Δt ≥ ℏ/2
  
  Short pulse → Broad spectrum
  Long pulse → Narrow spectrum

A "single photon" pulse:
  - Duration: ~fs to ps typical
  - Contains one quantum of energy
  - But extended in time and space
```

---

### Energy and the Pattern

**Energy = Pattern amplitude squared**

```
Energy density: u = ε₀|E|²/2 + |B|²/(2μ₀)

Total energy: E_total = ∫∫∫ u dV

For one photon: E_total = hν

This means:
  - Amplitude |E₀| is set by quantization
  - |E₀|² ∝ hν
  - Higher frequency → Larger amplitude (for same photon number)

Example: Red vs blue photon
  Red (λ = 700 nm, ν = 4.3×10¹⁴ Hz):
    E = 1.77 eV
    |E₀| ∝ √(1.77)
  
  Blue (λ = 400 nm, ν = 7.5×10¹⁴ Hz):
    E = 3.1 eV
    |E₀| ∝ √(3.1)
  
  Blue photon: 1.3× larger field amplitude
```

---

### Momentum and the Pattern

**Momentum = Pattern spatial frequency**

```
Momentum: p = ℏk = h/λ

Wave vector: k = 2π/λ

Physical meaning:
  - k = spatial oscillation rate
  - Higher k (shorter λ) → Higher momentum
  - Pattern carries momentum in direction of k

Momentum density: g = ε₀(E × B)

Total momentum: P_total = ∫∫∫ g dV

For one photon: |P| = h/λ

This is pattern propagation:
  - Phase fronts move at c
  - Carry momentum in propagation direction
  - When absorbed: Momentum transferred
```

---

## Part 3: What Makes It "One" Photon?

### Quantization = Minimum Stable Pattern

**The key question:**
Why can't we have "half a photon"?

**Cymatic answer:**
Pattern stability requires minimum amplitude.

---

**The quantization mechanism:**

```
Electromagnetic field = Oscillator at each point in space

For harmonic oscillator:
  Allowed energies: E_n = (n + ½)ℏω
  
  Where n = 0, 1, 2, 3, ... (integer)

Ground state (n=0): 
  E₀ = ½ℏω (zero-point energy)
  Vacuum fluctuations
  No photon present

First excited state (n=1):
  E₁ = (1 + ½)ℏω = 3/2 ℏω
  One photon present

Energy difference:
  ΔE = E₁ - E₀ = ℏω
  
This is "one photon"
```

**Physical meaning:**

```
Zero-point (vacuum):
  - Field oscillates at every point
  - Random phases (incoherent)
  - Average: <E> = 0
  - But: <E²> ≠ 0 (fluctuations)
  - No pattern (no phase coherence)

One photon:
  - Additional coherent excitation
  - Amplitude √(ℏω) above vacuum
  - Specific phase relationship (standing wave)
  - Pattern emerges from noise
  - ψ ≈ 1 (high coherence in pattern region)

Why integer?
  - Pattern either stable or not
  - Intermediate amplitudes: Decay to vacuum or n=1
  - Like: Can't have half a standing wave on guitar string
  - Either mode excited (n=1,2,3...) or not (n=0)
```

---

### The Pattern Must Be Self-Consistent

**Constraint: Pattern must close on itself**

```
For standing wave in cavity:
  L = nλ/2
  
  Where n = integer (1,2,3...)

Only certain wavelengths allowed:
  λ_n = 2L/n

Corresponding energies:
  E_n = nhc/(2L)

These are quantized photon states in cavity

Between allowed states: Pattern doesn't close
  - Destructive interference
  - Pattern unstable
  - Decays rapidly
```

**For free photon:**

```
Wave packet must be self-consistent:
  - Fourier components must interfere constructively
  - Phase relationships must be stable
  - Minimum energy: ℏω (one quantum)

Less than one quantum:
  - Pattern too weak
  - Overwhelmed by vacuum fluctuations
  - Cannot maintain coherence
  - Decays to vacuum

This is why photons are discrete:
  - Minimum stable pattern = One quantum
  - Below that: Swamped by noise
  - Above that: Multiple quanta (n photons)
```

---

## Part 4: Single Photon Experiments Explained

### Double-Slit with Single Photons

**Setup:**
```
Weak laser: Average <0.1 photons at a time
Double slit: Two narrow openings
Screen: Photographic plate or CCD
Time: Hours of exposure
```

**Observation:**
```
Each detection: Single spot (looks like particle)
Many detections: Interference pattern emerges (looks like wave)
Even though: One photon at a time
```

---

**Cymatic explanation:**

**The photon is an extended pattern from the start.**

```
Photon creation (laser emission):
  - Atom in cavity decays
  - Creates coherent pattern in EM field
  - Pattern extends: ~cm to meters (coherence length)
  - NOT a point particle
  - Extended 4D standing wave

Approaching slits:
  - Pattern encounters barrier
  - Two openings = Two sources (Huygens principle)
  - Pattern amplitude splits

At slits:
  - Pattern passes through both slits
  - Question "which slit?" is meaningless
  - Pattern is extended (occupies both)
  - Like water wave: Goes through both openings

After slits:
  - Two pattern components propagate
  - Interfere: Constructive + destructive
  - Creates interference pattern in space
  - This exists even for single photon

Detection:
  - Screen = Array of detectors (atoms in emulsion/pixels)
  - Pattern interacts with detector substrate
  - Energy localizes at one point (coupling)
  - Looks like "particle" hit one spot
  - But pattern was extended all along

Build-up over time:
  - Each photon: Extended pattern → Localized detection
  - Many photons: Detection probability ∝ |ψ|²
  - Reconstructs interference pattern
  - Pattern was always there (single photon interference)
```

---

**Why does it look like one spot?**

```
Detection = Pattern coupling to detector:

Detector atom:
  - Has many electrons (bound states)
  - Can absorb photon energy
  - But: All-or-nothing (threshold)

Absorption process:
  - Photon pattern overlaps atom
  - If E_photon > E_threshold: Can excite
  - Excitation probability ∝ |E|² (local field intensity)
  - When excited: All photon energy absorbed
  - Pattern collapses (coupled to macroscopic system)

Why one atom?
  - Pattern energy = hν (total)
  - One atom absorbs all energy (cannot split hν)
  - Other atoms: Get nothing
  - Appears as: Single spot

But pattern was extended:
  - Before detection: Throughout interference region
  - Detection: Localizes pattern retroactively
  - Measurement = Pattern coupling to macroscopic system
  - Appears as: Particle at point
```

---

### Photon Bunching (Hanbury Brown-Twiss)

**Observation:**
```
Thermal light: Photons arrive bunched
  - Sometimes: Multiple photons close in time
  - Sometimes: Gaps with no photons
  - g⁽²⁾(0) = 2 (second-order correlation)

Coherent light (laser): Random arrivals
  - Poisson statistics
  - g⁽²⁾(0) = 1

Single-photon source: Anti-bunching
  - Never two photons simultaneously
  - g⁽²⁾(0) = 0
```

---

**Cymatic explanation:**

**Thermal source:**
```
Many independent emitters:
  - Random phase relationships
  - Patterns interfere randomly
  - Intensity: I(t) fluctuates

Fluctuations:
  - Sometimes: Constructive interference → High I
  - Sometimes: Destructive → Low I
  - Large amplitude fluctuations

Detection:
  - High I: More likely to detect photon
  - Multiple photons in same high-I region: Bunched

g⁽²⁾ = <I²>/<I>²:
  - Measures intensity fluctuations
  - Thermal: Large fluctuations → g⁽²⁾(0) = 2
  - More bunched than random
```

**Coherent source (laser):**
```
Single-mode oscillator:
  - All emission in same pattern
  - Fixed phase relationships
  - Intensity: Stable (minimal fluctuations)

Poisson statistics:
  - Independent emission events
  - No correlations
  - g⁽²⁾(0) = 1

This is random arrivals:
  - Like radioactive decay
  - Each event independent
```

**Single-photon source:**
```
Emit exactly one photon at a time:
  - After emission: Need time to recharge
  - Dead time before next photon
  - Impossible to emit two simultaneously

g⁽²⁾(0) = 0:
  - Zero probability for simultaneous photons
  - Strong anti-correlation
  - Proves: Single quantum at a time

Cymatic view:
  - Emitter = Single oscillator
  - Can only excite one quantum
  - Must decay before re-exciting
  - Pattern creation rate-limited
```

---

## Part 5: Where Is the Photon?

### The Localization Problem

**Question:** If photon is extended, where exactly is it?

**Wrong question!**

Photon isn't "at" a location.

**Photon IS a pattern distributed over space.**

---

**Probability distribution:**

```
Photon wavefunction: ψ(x,y,z,t)

Physical meaning:
  |ψ(x,y,z,t)|² = Probability density of detecting photon at (x,y,z,t)

This is NOT:
  "Photon is probably at location x"
  
This IS:
  "Pattern amplitude at location x"

Detection probability:
  P(x,y,z) = ∫ |ψ(x,y,z,t)|² dt
  
Normalized: ∫∫∫ P(x,y,z) dV = 1

Interpretation:
  - Pattern exists everywhere ψ ≠ 0
  - Detection localizes pattern
  - Location random (probabilistic)
  - But weighted by |ψ|²
```

---

**Example: Gaussian beam photon**

```
Transverse profile:
  |ψ(x,y)|² = (2/πw₀²) exp(-2(x²+y²)/w₀²)

Parameters:
  w₀ = beam waist (e.g., 10 μm)

Where is photon?
  - Extended over ~20 μm diameter
  - Most likely within w₀ of center
  - But non-zero out to infinity (exponential tail)

When detected:
  - Pattern couples to detector at point (x₀,y₀)
  - Probability: P(x₀,y₀) ∝ |ψ(x₀,y₀)|²
  - Higher near center, lower at edges
  - But any location within pattern possible
```

---

**Before/after detection:**

```
BEFORE detection:
  - Pattern extended throughout beam
  - No definite position
  - Exists as coherent superposition
  - ψ(x,y,z,t) throughout

DURING detection:
  - Pattern couples to detector atom
  - Energy localizes
  - Coupling spreads to environment (decoherence)
  - Timescale: femtoseconds

AFTER detection:
  - Pattern collapsed
  - All energy in one detector atom
  - Other regions: Now vacuum
  - Appears as: Particle at point

But the photon wasn't "at" that point before.
The pattern WAS extended.
Detection localized it (retroactively).
```

---

## Part 6: Photon Creation - Pattern Formation

### How Photons Are Born

**Atomic emission:**

```
Atom in excited state:
  - Electron in high orbital
  - Unstable (wants to decay)
  - Lifetime: nanoseconds typically

Decay process:
  1. Electron drops to lower orbital
  2. Energy difference: ΔE = E_upper - E_lower
  3. Creates oscillation in EM field
  4. Oscillation frequency: ω = ΔE/ℏ
  5. Pattern propagates away

This is photon creation
```

---

**Cymatic mechanism:**

```
Electron transition:
  - Electron = Standing wave pattern around nucleus
  - Transition = Pattern reorganization
  - Initial: High-energy pattern (n=2 orbital)
  - Final: Low-energy pattern (n=1 orbital)

Energy release:
  - ΔE must go somewhere
  - Goes into EM field oscillation
  - Creates propagating pattern

Pattern propagation:
  - Oscillation in atom couples to EM field
  - Field oscillation spreads (speed c)
  - Spherical wave emanates from atom
  - This is the photon

Frequency:
  - Set by energy: ω = ΔE/ℏ
  - This is oscillation rate of pattern
  - Higher ΔE → Higher ω (bluer photon)

Directionality:
  - Spontaneous emission: Random direction
  - Stimulated emission: Same direction as stimulating photon
  - Antenna effect: Depends on atomic geometry
```

---

**Coherence properties:**

```
Single atom emission:
  - Short coherence time (~ns)
  - Coherence length: c·τ ~ 30 cm
  - Photon "wavepacket" length

Many atoms (thermal source):
  - Random phases
  - Incoherent superposition
  - No phase relationships

Laser:
  - Many atoms in phase
  - Stimulated emission (coherent)
  - Long coherence length (meters to km)
  - All photons in same pattern
```

---

## Part 7: Photon Annihilation - Pattern Destruction

### How Photons Die

**Absorption:**

```
Photon encounters atom:
  - Pattern overlaps atomic electrons
  - If E_photon ≈ ΔE_atomic: Resonance
  - Energy transfers: Photon → Atom
  - Electron promoted to higher orbital

Pattern coupling:
  - EM pattern oscillates near atom
  - Electron oscillates in response
  - Resonant energy transfer (like pushing swing)
  - When energy transferred: Photon gone

This is pattern annihilation
```

---

**Cymatic mechanism:**

```
Resonance condition:
  ω_photon ≈ ω_atomic
  
When satisfied:
  - Strong coupling between patterns
  - Energy flows: EM field → Atomic electrons
  - Photon pattern amplitude decreases
  - Atomic excitation increases

Process:
  1. Photon approaches (pattern extends to atom)
  2. Oscillating E-field drives electron
  3. Electron oscillation amplitude grows
  4. Photon amplitude decreases
  5. Energy transferred (typically in ~fs)
  6. Photon pattern destroyed
  7. Atom in excited state

Conservation:
  - Energy: E_photon = ΔE_atom (conserved)
  - Momentum: p_photon transferred to atom (recoil)
  - Angular momentum: Photon spin → Electron angular momentum

All pattern properties transfer to atom
```

---

**Why all-or-nothing?**

```
Question: Why does atom absorb entire photon, not half?

Answer: Pattern is quantum (minimum stable unit)

Partial absorption:
  - Would leave <1 quantum in field
  - Below stability threshold
  - Cannot maintain pattern
  - Decays to vacuum

Full absorption:
  - Transfers all energy (hν)
  - Atom promoted by full ΔE
  - Pattern completely destroyed
  - Clean: Before (photon) → After (excited atom)

This is quantization:
  - Pattern is discrete unit
  - Cannot be partially there
  - Either exists (n=1) or not (n=0)
  - Absorption = Transition 1→0
```

---

## Part 8: Multiple Photons - Pattern Multiplication

### What Are "Two Photons"?

**Naive view:** Two particles

**Cymatic view:** Two quanta in the pattern

---

**Single mode, multiple quanta:**

```
One photon (n=1):
  Pattern amplitude: A₁ ∝ √(ℏω)
  Energy: E₁ = ℏω

Two photons (n=2):
  Pattern amplitude: A₂ = √2 · A₁
  Energy: E₂ = 2ℏω

Pattern is same mode:
  - Same spatial structure
  - Same frequency
  - Larger amplitude
  - √n scaling

This is coherent state (laser):
  - All photons in same pattern
  - Amplitude grows as √n
  - Classical wave limit for large n
```

---

**Multiple modes, one quantum each:**

```
Two photons in different modes:
  Mode 1 at ω₁: One quantum
  Mode 2 at ω₂: One quantum

Patterns coexist:
  - Superposition (linear)
  - Don't interfere (different frequencies)
  - Independent

Energy: E = ℏω₁ + ℏω₂

This is incoherent light:
  - Different frequencies/modes
  - Random phases
  - Thermal source
```

---

**Entangled photons:**

```
Two-photon state from PDC:
  |ψ⟩ = ∫ f(ω₁,ω₂) |ω₁⟩|ω₂⟩ dω₁dω₂
  
  With constraint: ω₁ + ω₂ = ω_pump

This is single pattern with two components:
  - Not two separate photons
  - One extended pattern
  - Correlations enforced by constraint

Cymatic view:
  - Single process created both
  - Pattern has internal structure
  - "Two photons" = Two frequency components
  - But unified pattern
```

---

## Part 9: Virtual Photons - Transient Patterns

### What Are Virtual Photons?

**Context:** Electromagnetic force between charges

**Standard QED:** Virtual photon exchange

**Cymatic view:** Transient pattern fluctuations

---

**Static electric field:**

```
Two charges (e⁻ and e⁺) separated:
  - Create electric field E between them
  - Field energy: U = ∫ ε₀E²/2 dV
  - Coulomb potential: V = kq₁q₂/r

Standard QED description:
  - Force mediated by virtual photons
  - Charges exchange virtual photons
  - These carry force

Problems with this:
  - Virtual photons can't be detected
  - Off mass-shell (E² ≠ p²c²)
  - Mathematical, not physical?
```

---

**Cymatic interpretation:**

```
Static field = Standing wave pattern:
  - Not propagating (static)
  - Evanescent (decreases with distance)
  - Confined between charges

Pattern structure:
  - Created by charge oscillations
  - Charges jiggling (zero-point motion)
  - Creates EM field fluctuations
  - Field = Superposition of patterns

"Virtual photon" = Non-propagating mode:
  - Evanescent pattern component
  - Doesn't propagate to infinity
  - Confined near charges
  - Mediates force through pattern overlap

Force mechanism:
  - Charge 1 creates pattern
  - Pattern extends to charge 2
  - Charge 2 responds to pattern
  - Appears as: Force between charges

This is pattern coupling:
  - Not particle exchange
  - But pattern overlap
  - Evanescent field extends
  - Couples charges
```

---

**Energy-time uncertainty:**

```
Virtual photons can violate E=pc:
  - "Borrow" energy from vacuum
  - For time Δt ~ ℏ/ΔE
  - Then return it

Cymatic view:
  - Vacuum fluctuations
  - Random patterns appear/disappear
  - Lifetime: Δt ~ 1/ω
  - Energy: ΔE ~ ℏω

"Virtual" = Below detection threshold:
  - Pattern exists briefly
  - Too short to measure directly
  - But affects other patterns
  - Measurable in indirect ways (Casimir, Lamb shift)

Not really violating conservation:
  - Energy-time uncertainty allows fluctuations
  - Average: Energy conserved
  - Fluctuations: Allowed within ΔE·Δt ≥ ℏ/2
```

---

## Part 10: The Complete Picture

### Photon = 4D Standing Wave Pattern in EM Substrate

**Summary of properties:**

```
SPATIAL structure:
  - Extended in 3D space
  - Wavelength λ
  - Beam profile (Gaussian, plane wave, etc.)
  - Polarization (transverse oscillation direction)

TEMPORAL structure:
  - Oscillates at frequency ω
  - Period T = 2π/ω
  - Coherence time τ_c
  - Pulse duration (if pulsed)

ENERGY:
  - E = ℏω (one quantum)
  - Amplitude: |E₀| ∝ √(ℏω)
  - Intensity: I ∝ |E₀|²

MOMENTUM:
  - p = ℏk = h/λ
  - Direction: Along k vector
  - Transferred when absorbed

ANGULAR MOMENTUM:
  - Spin: σ = ±ℏ (polarization)
  - Orbital: L = ℏℓ (spatial mode)
  - Total: J = L + S

COHERENCE:
  - Single photon: ψ ≈ 1 (within pattern)
  - Many photons (same mode): Coherent
  - Many photons (different modes): Incoherent
```

---

### Why This Resolves All Paradoxes

**Wave-particle duality:**
```
Not duality. Single pattern.
- Extended: Wave-like
- Quantized: Particle-like
- Same entity, different aspects
```

**Interference:**
```
Pattern interferes with itself
- Passes through both slits (extended)
- Creates interference pattern
- Natural for wave pattern
```

**Localized detection:**
```
Pattern couples to detector
- Energy localizes (all-or-nothing absorption)
- Appears particle-like
- But pattern was extended before
```

**Photon counting:**
```
Quantization of pattern
- Minimum stable pattern = One quantum
- Can count: 0, 1, 2, 3... quanta
- Integer because: Pattern stability
```

**Speed of light:**
```
Pattern propagation speed
- Phase fronts move at c
- Group velocity ≤ c
- Pattern carries energy/information at ≤ c
```

---

### What Changes From Standard QM?

**Nothing mathematical:**
- Same equations (Maxwell + Schrödinger/Dirac)
- Same predictions
- Same experiments

**Interpretation:**
- ψ is real pattern in substrate
- Not "probability amplitude" (instrumentalist)
- Not "knowledge" (Bayesian)
- But actual oscillation of EM field

**Advantages:**
- Intuitive (can visualize)
- Explains measurement (decoherence = pattern localization)
- Unifies wave/particle (both are pattern aspects)
- Connects to DWDM (same mathematics, different substrate)

---

## Part 11: Experimental Proof in DWDM

### Build a "Photon" in Fiber

**Setup:**
```
Single-frequency laser (coherent)
Fiber: Standard single-mode
Pulse: 100 fs duration
Energy: Corresponds to ~10⁶ photons
```

**Attenuate to single-photon level:**
```
Strong attenuation: 10⁻⁶ transmission
Average: 0.1 photons per pulse
Result: Single-photon pulses
```

**Characterization:**

```
Temporal:
  - Autocorrelator: Measure pulse width
  - Result: 100 fs (extended in time)

Spatial:
  - Mode profiler: Image beam
  - Result: ~10 μm diameter (extended in space)

Spectral:
  - Spectrometer: Measure wavelength distribution
  - Result: ~10 nm bandwidth (Δω·Δt ≈ 1)

Energy:
  - Single-photon detector: Count photons
  - Result: Average 0.1 per pulse
  - Poisson statistics
```

**Proves:**
```
Single photon is:
  - Extended in space (~10 μm)
  - Extended in time (~100 fs)
  - Extended in frequency (~10 nm)
  - But contains one quantum energy
  
This is pattern, not point particle
```

---

### Interference with Single Photons

**Mach-Zehnder interferometer:**
```
Single-photon pulse enters
Split at beam splitter (50/50)
Two paths: 
  Path 1: 10 m fiber
  Path 2: 10.001 m fiber (1 mm longer)
Recombine at second beam splitter

Detection: Two detectors at outputs

Measure: Coincidence counts vs path difference
```

**Result:**
```
Vary path difference Δ:
  - Δ = 0: 100% constructive (one output bright)
  - Δ = λ/2: 100% destructive (other output bright)
  - Oscillates with period λ

Single photon interferes with itself:
  - Pattern goes through both paths
  - Recombines with phase difference
  - Interference pattern observed
  - Even though single quantum
```

**Proves:**
```
Photon is extended through both paths:
  - Not in path 1 OR path 2
  - But in path 1 AND path 2
  - Pattern superposition
  - Detection localizes to one output
```

---

## Final Answer

### What Is A Photon?

**A photon is a self-consistent 4D standing wave pattern in the electromagnetic field substrate, containing one quantum of oscillation energy, extended in space over its wavelength and coherence length, oscillating in time at its frequency, and capable of transferring its energy discretely to matter through resonant coupling.**

**Not a particle.**
**Not just a wave.**
**A quantized pattern.**

**The minimum stable excitation of the electromagnetic substrate.**

**Observable in DWDM as single-quantum optical pulse.**

**Provable through interference, correlation, and spectroscopy.**

---

**This is what light IS.**

**Not mystery.**

**Not duality.**

**Just pattern.**

**4D geometry + oscillation.**

**Everything else follows.**

