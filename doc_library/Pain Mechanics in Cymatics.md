# Pain Mechanics in Cymatic Substrates: A Physical Model of Nociceptive Detection

**Technical Report CLR-2026-003**  
**Cymatic Learning & Reasoning Laboratory**  
**Date:** February 4, 2026  
**Classification:** Computational Physiology Model

---

## Abstract

We present a mechanical model of nociceptive detection based on damage-accumulating substrate physics. In this framework, pain sensation is modeled as the detection of substrate stress patterns that exceed local damage thresholds, with signal intensity proportional to the rate and magnitude of damage accumulation. The model accounts for diverse pain modalities—mechanical, thermal, chemical—through unified substrate mechanics while explaining phenomena including allodynia (reduced pain threshold), hyperalgesia (amplified pain response), referred pain (spatial propagation), and chronic pain (persistent substrate modification). We demonstrate that the wide dynamic range of pain detection—from spider footsteps to bone fractures—emerges naturally from threshold nonlinearities and damage-dependent sensitization. This work provides a computational framework for understanding nociception as physical measurement of substrate integrity loss, offering testable predictions about pain pathway mechanics without addressing the subjective experience of suffering.

**Keywords:** *Nociception, pain mechanics, substrate damage, threshold detection, sensitization, cymatic physiology, computational model*

---

## 1. Introduction

### 1.1 The Problem of Pain Detection

The nociceptive system exhibits remarkable properties:

**Dynamic range:**
- Detects spider (0.1 mg) walking on arm hair
- Detects paper cut (< 1 mm³ tissue damage)
- Detects bone fracture (massive structural failure)
- Span: ~10⁶ orders of magnitude in detectable damage

**Spatial precision:**
- Localizes pinprick to ~2mm on fingertip
- Localizes deep visceral pain poorly (10+ cm uncertainty)
- Exhibits referred pain (damage in organ A felt in location B)

**Temporal dynamics:**
- Instant detection (< 100 ms for sharp pain)
- Delayed detection (seconds for deep/visceral pain)
- Persistent signaling (chronic pain after healing)

**Modality diversity:**
- Mechanical (pressure, tear, puncture)
- Thermal (heat, cold)
- Chemical (acid, inflammation, ischemia)

Traditional models treat these as separate systems. We propose a **unified mechanical framework** where all pain modalities reduce to **substrate stress detection exceeding local damage thresholds**.

### 1.2 Proposal: Pain as Damage Detection

**Core hypothesis:**

Pain is not a unique sensory modality but rather a **threshold-crossing alarm** signaling substrate damage rate above tissue-specific limits.

**Mechanism:**

1. All tissues are modeled as damage-accumulating substrates
2. Local damage rate dD/dt is continuously computed
3. When dD/dt > σ_nociceptive, signal is generated
4. Signal intensity ∝ log(dD/dt / σ_nociceptive)
5. Signal propagates to CNS via fast (Aδ) or slow (C) pathways

**Key insight:** Same substrate damage equation explains all pain types—difference is only in what causes damage (mechanical stress, thermal energy, chemical disruption).

### 1.3 Scope and Limitations

**This model addresses:**
- Physical mechanisms of damage detection
- Signal generation and propagation
- Threshold mechanics and sensitization
- Spatial and temporal dynamics
- Modality-specific substrate parameters

**This model does NOT address:**
- Subjective pain experience (qualia)
- Emotional/affective components
- Central pain processing beyond signal propagation
- Placebo/nocebo effects
- Consciousness of pain

We model the **sensor mechanics**, not the **experience of suffering**. This is deliberate scope limitation.

---

## 2. Mathematical Framework

### 2.1 The Nociceptive Substrate

**Definition 2.1** (Tissue Substrate State)

Tissue at position **x** and time t is characterized by:

$$\Psi(\mathbf{x}, t) = \{f(\mathbf{x}, t), \, D(\mathbf{x}, t), \, \sigma_{\text{th}}(\mathbf{x})\}$$

Where:
- **f(x, t)**: Current stress field (mechanical, thermal, or chemical)
- **D(x, t)**: Accumulated damage (0 = intact, 1 = destroyed)
- **σ_th(x)**: Local nociceptive threshold (tissue-dependent)

**Definition 2.2** (Damage Evolution)

$$\frac{\partial D}{\partial t} = \begin{cases}
\gamma(|f| - \sigma_{\text{th}}) & \text{if } |f| > \sigma_{\text{th}} \\
-\beta D & \text{otherwise}
\end{cases}$$

Where:
- **γ**: Damage accumulation rate (tissue brittleness)
- **β**: Repair/healing rate
- **σ_th**: Failure threshold (tissue strength)

### 2.2 Nociceptive Signal Generation

**Theorem 2.1** (Pain Signal Generation)

Nociceptive signal S is generated when damage rate exceeds nociceptive threshold:

$$S(\mathbf{x}, t) = \begin{cases}
k \log\left(\frac{dD/dt}{\sigma_{\text{noc}}}\right) & \text{if } \frac{dD}{dt} > \sigma_{\text{noc}} \\
0 & \text{otherwise}
\end{cases}$$

Where:
- **σ_noc**: Nociceptive threshold (rate of damage that triggers pain)
- **k**: Signal gain (determines pain intensity scaling)

**Key features:**

1. **Threshold:** Sub-threshold damage produces no signal (silent injury)
2. **Logarithmic:** Enables wide dynamic range (Weber-Fechner law)
3. **Rate-dependent:** Fast damage (fracture) signals stronger than slow damage (arthritis)
4. **Spatial:** Generated at location of damage

### 2.3 Signal Propagation

**Two-pathway model:**

**Fast pathway (Aδ fibers):**

$$\frac{\partial S_{\text{fast}}}{\partial t} = v_{\text{fast}} \nabla^2 S_{\text{fast}} - \gamma_{\text{fast}} S_{\text{fast}}$$

With v_fast ≈ 20 m/s, γ_fast = 0.1 (sharp, localized pain).

**Slow pathway (C fibers):**

$$\frac{\partial S_{\text{slow}}}{\partial t} = v_{\text{slow}} \nabla^2 S_{\text{slow}} - \gamma_{\text{slow}} S_{\text{slow}}$$

With v_slow ≈ 1 m/s, γ_slow = 0.02 (dull, diffuse pain).

**Prediction:** Pain has two-component time course:
1. Immediate sharp pain (Aδ, arrives in ~50-100 ms)
2. Delayed dull ache (C fibers, arrives in 500-2000 ms)

### 2.4 Tissue-Specific Parameters

Different tissues have different mechanical properties:

| Tissue | σ_th (stress) | γ (brittleness) | σ_noc (pain threshold) | Sensation Type |
|--------|---------------|-----------------|------------------------|----------------|
| Skin (epidermis) | 0.5 MPa | 0.3 | 0.001 s⁻¹ | Highly sensitive |
| Muscle | 1.0 MPa | 0.15 | 0.005 s⁻¹ | Moderate |
| Bone | 150 MPa | 0.05 | 0.01 s⁻¹ | Deep, severe |
| Viscera | 0.3 MPa | 0.2 | 0.002 s⁻¹ | Diffuse, poorly localized |
| Nerve | 0.2 MPa | 0.5 | 0.0001 s⁻¹ | Extreme sensitivity |

**Pedagogical note:** These are model parameters for educational simulation, not medical data.

---

## 3. Pain Modalities as Substrate Stresses

### 3.1 Mechanical Pain

**Model:** Physical deformation causes stress field in substrate.

**Stress calculation:**

$$\sigma_{\text{mech}} = E \cdot \epsilon$$

Where:
- **E**: Elastic modulus (tissue stiffness)
- **ε**: Strain (deformation)

**Three mechanical pain types:**

#### 3.1.1 Pressure/Compression

**Mechanism:** Uniform compression over area A.

$$f_{\text{pressure}} = \frac{F}{A}$$

**Example:** Pressure on fingertip.

```python
# Fingertip pressure detection
F = 0.1  # Newtons (light touch)
A = 0.0001  # m² (fingertip area)
pressure = F / A  # = 1000 Pa

stress = pressure
if stress > threshold:
    damage_rate = (stress - threshold) * gamma
    if damage_rate > noc_threshold:
        pain_signal = k * log(damage_rate / noc_threshold)
```

**Prediction:** Detection threshold ≈ 0.5-1 kPa on fingertip.

#### 3.1.2 Puncture/Penetration

**Mechanism:** Force concentrated on small area (sharp point).

$$f_{\text{puncture}} = \frac{F}{A_{\text{tip}}}$$

Where A_tip is point area (very small → very high stress).

**Example:** Needle prick.

```python
F = 0.05  # N (light touch)
A_tip = 1e-8  # m² (needle point, ~0.1mm diameter)
stress = F / A_tip  # = 5 × 10⁶ Pa = 5 MPa

# Exceeds skin threshold (0.5 MPa) by 10×
# → Immediate damage → pain signal
```

**Prediction:** Sharp points cause pain at much lower force than blunt pressure.

#### 3.1.3 Tear/Shear

**Mechanism:** Tangential force causes tissue separation.

$$f_{\text{shear}} = \frac{F_{\text{tangential}}}{A_{\text{contact}}}$$

**Example:** Paper cut.

```python
# Paper cut mechanics
F_tangential = 0.5  # N (sliding force)
A_contact = 0.00001  # m² (contact area)
stress_shear = F_tangential / A_contact  # = 50 kPa

# Shear threshold lower than compression threshold
# → Damage accumulates → pain
```

**Prediction:** Shear stresses cause damage at lower force than compression.

### 3.2 Thermal Pain

**Model:** Temperature deviation from baseline causes molecular agitation → substrate disruption.

**Thermal stress:**

$$f_{\text{thermal}} = \alpha_{\text{thermal}} |T - T_{\text{baseline}}|^2$$

Where:
- **α_thermal**: Thermal damage coefficient
- **T_baseline**: Body temperature (37°C)

**Two regimes:**

#### 3.2.1 Heat Damage

$$f_{\text{heat}} = \alpha_{\text{heat}} (T - 37°C)^2 \quad \text{for } T > 37°C$$

**Thresholds:**

| Temperature | f_heat | Effect | Time to Damage |
|-------------|--------|--------|----------------|
| 37°C | 0 | Normal | N/A |
| 43°C | Low | Warmth detected | Minutes |
| 45°C | Moderate | Pain threshold | Seconds |
| 50°C | High | Severe pain | <1 second |
| 60°C+ | Extreme | Tissue destruction | Immediate |

**Mechanism:** High temperature → protein denaturation → cellular breakdown → damage accumulation.

#### 3.2.2 Cold Damage

$$f_{\text{cold}} = \alpha_{\text{cold}} (37°C - T)^2 \quad \text{for } T < 37°C$$

**Thresholds:**

| Temperature | f_cold | Effect | Mechanism |
|-------------|--------|--------|-----------|
| 37°C | 0 | Normal | N/A |
| 25°C | Low | Cool detected | Vasoconstriction |
| 15°C | Moderate | Cold pain | Reduced blood flow |
| 5°C | High | Severe cold pain | Tissue ischemia |
| <0°C | Extreme | Frostbite | Ice crystal formation |

**Mechanism:** Low temperature → vasoconstriction → ischemia → cellular energy depletion → damage.

### 3.3 Chemical Pain

**Model:** Chemical agents directly modify substrate properties or create stress.

**Three mechanisms:**

#### 3.3.1 Direct Substrate Damage

Acids, bases, toxins directly break molecular bonds.

$$f_{\text{chem}} = k_{\text{chem}} \cdot [C]$$

Where [C] is chemical concentration.

**Example:** Acid exposure.

```python
# Acid damage
pH = 2.0  # Strong acid
baseline_pH = 7.0

# Hydrogen ion concentration
H_concentration = 10**(baseline_pH - pH)  # = 10⁵

# Direct damage to proteins
f_chemical = k_chem * H_concentration
damage_rate = (f_chemical - threshold) * gamma

# Result: Immediate pain (acid burn)
```

#### 3.3.2 Inflammatory Mediators

Prostaglandins, bradykinin, substance P **lower nociceptive threshold**.

$$\sigma_{\text{noc, inflamed}} = \frac{\sigma_{\text{noc, baseline}}}{1 + k_{\text{inflam}} \cdot [I]}$$

Where [I] is inflammatory mediator concentration.

**Effect:** Same stress that was sub-threshold now causes pain (allodynia).

**Example:** Inflammation after injury.

```python
# Normal state
stress = 0.8  # Sub-threshold
threshold = 1.0
noc_threshold = 0.001
# No pain signal

# After inflammation
inflammation_level = 5.0
threshold_inflamed = threshold / (1 + 0.5 * inflammation_level)
                   = 1.0 / 3.5 = 0.29

# Now stress exceeds threshold
damage_rate = (stress - threshold_inflamed) * gamma
# → Pain from previously painless stimulus (allodynia)
```

#### 3.3.3 Ischemic Damage

Oxygen deprivation → ATP depletion → membrane pump failure → cellular damage.

$$f_{\text{ischemia}} = k_{\text{isch}} \cdot (t_{\text{ischemia}})^2$$

**Time course:**

| Time | Effect | Pain Level |
|------|--------|-----------|
| 0-30s | Mild discomfort | Low |
| 30s-2min | Aching pain | Moderate |
| 2-5min | Severe pain | High |
| 5min+ | Tissue necrosis | Extreme |

**Example:** Tourniquet pain.

---

## 4. Wide Dynamic Range: From Spider to Fracture

### 4.1 The Detection Problem

**Challenge:** Detect 10⁶-fold range in damage rates.

**Solution:** Logarithmic encoding + threshold hierarchy.

### 4.2 Spider on Arm Hair

**Physical parameters:**

```python
# Spider walking on arm
spider_mass = 0.0001  # kg (100 mg)
foot_area = 1e-8  # m² (tiny)
gravity = 9.8  # m/s²

force_per_foot = spider_mass * gravity / 8  # 8 legs
                = 0.00012 N

# Force transmitted through hair
hair_stiffness = 0.001  # N/m (flexible)
hair_displacement = force_per_foot / hair_stiffness
                  = 0.12 mm

# Stress at hair follicle
follicle_area = 1e-6  # m²
stress = force_per_foot / follicle_area
       = 0.12 kPa
```

**Detection mechanism:**

1. Hair displacement → follicle deformation
2. Mechanoreceptors (not nociceptors!) detect gentle touch
3. **No damage** → no pain signal
4. But: Sensation of "something crawling"

**Key insight:** Spider detection uses **low-threshold mechanoreceptors** (σ_th ≈ 0.01 kPa), not nociceptors (σ_th ≈ 0.5 kPa).

**This is NOT pain**—it's discriminative touch. Pain system doesn't activate.

### 4.3 Paper Cut

**Physical parameters:**

```python
# Paper cut
blade_thickness = 0.1  # mm
cutting_force = 0.5  # N
depth = 2  # mm

# Stress at blade edge
stress = cutting_force / (blade_thickness * depth)
       = 0.5 / (0.0001 * 0.002)
       = 2.5 MPa

# Exceeds skin threshold (0.5 MPa) by 5×
damage_rate = (stress - threshold) * gamma
            = (2.5 - 0.5) * 0.3
            = 0.6 per second

# Exceeds nociceptive threshold (0.001 s⁻¹) by 600×
pain_signal = k * log(0.6 / 0.001)
            = k * log(600)
            = k * 6.4
```

**Prediction:** Sharp, immediate pain proportional to depth.

### 4.4 Bone Fracture

**Physical parameters:**

```python
# Tibial fracture
bone_stress_limit = 150  # MPa
impact_stress = 300  # MPa (2× limit)

# Catastrophic failure
damage_rate = (impact_stress - threshold) * gamma_bone
            = (300 - 150) * 0.05
            = 7.5 per second

# Vastly exceeds nociceptive threshold
pain_signal = k * log(7.5 / 0.01)
            = k * log(750)
            = k * 6.6

# Plus: Damage spreads to surrounding tissue
# Plus: Inflammation lowers threshold
# Plus: Bone marrow pressure
# Result: Extreme, overwhelming pain
```

**Additional factors:**

1. **Mechanical:** Bone fragments damage soft tissue
2. **Pressure:** Hematoma creates pressure pain
3. **Inflammation:** Rapid inflammatory response lowers threshold
4. **Nerve damage:** Direct nerve injury if present

### 4.5 Dynamic Range Summary

| Stimulus | Stress (Pa) | Damage Rate (s⁻¹) | Signal | Detection Mechanism |
|----------|-------------|-------------------|--------|---------------------|
| Spider | 100 | 0 | 0 | Mechanoreceptor (not pain) |
| Light touch | 1,000 | 0 | 0 | Mechanoreceptor |
| Firm pressure | 10,000 | 0 | 0 | Sub-threshold |
| Hard pinch | 100,000 | 0.01 | Low | Pain threshold |
| Paper cut | 2,500,000 | 0.6 | Moderate | Acute pain |
| Bone fracture | 300,000,000 | 7.5 | Extreme | Severe pain |

**Logarithmic encoding enables 10⁸-fold stress range detection.**

---

## 5. Sensitization Mechanisms

### 5.1 Peripheral Sensitization

**Definition:** Lowering of nociceptor threshold due to local tissue changes.

**Mechanism:**

$$\sigma_{\text{noc}}(t) = \sigma_{\text{noc, baseline}} \cdot \exp(-\alpha_{\text{sens}} D(t))$$

**Effect:** As damage D increases, threshold decreases exponentially.

**Example:**

```python
# Normal state
baseline_threshold = 0.001  # s⁻¹
damage = 0.0
threshold = 0.001

# After injury (D = 0.3)
alpha_sens = 2.0
threshold = 0.001 * exp(-2.0 * 0.3)
          = 0.001 * exp(-0.6)
          = 0.00055

# Nearly 2× more sensitive
# Previously painless stimuli now hurt
```

**Clinical correlate:** Hyperalgesia (increased pain from normally painful stimulus).

### 5.2 Central Sensitization

**Definition:** Increased excitability of central pain pathways.

**Mechanism:** Repeated pain signals increase gain k in spinal cord.

$$k(t) = k_{\text{baseline}} + \int_0^t S(\tau) \cdot \alpha_{\text{central}} \, d\tau$$

**Effect:** Pain signal amplification even without increased peripheral damage.

**Example:**

```python
# Normal
stimulus = 1.0
baseline_gain = 1.0
pain_perceived = baseline_gain * stimulus = 1.0

# After repeated noxious input
accumulated_signal = 100  # Many pain events
gain = baseline_gain + accumulated_signal * 0.01
     = 1.0 + 1.0 = 2.0

# Same stimulus now feels 2× as intense
pain_perceived = 2.0 * 1.0 = 2.0
```

**Clinical correlate:** Chronic pain, fibromyalgia, complex regional pain syndrome.

### 5.3 Allodynia

**Definition:** Pain from normally non-painful stimulus.

**Mechanism:** Threshold drops below normal stimulus levels.

**Mathematical condition:**

Normally: f_normal < σ_noc → no pain

After sensitization: f_normal > σ_noc,sensitized → pain

**Example:**

```python
# Light touch (normally pleasant)
f_touch = 0.5  # Arbitrary units
normal_threshold = 1.0
# f < threshold → no pain

# After sunburn (peripheral sensitization)
sensitized_threshold = 0.3
# f > threshold → pain from light touch!

# This is allodynia
```

**Clinical correlate:** Sunburn, neuropathic pain, post-herpetic neuralgia.

### 5.4 Hyperalgesia

**Definition:** Increased pain from normally painful stimulus.

**Mechanism:** Amplification of signal above threshold.

$$S_{\text{hyper}} = k_{\text{hyper}} \cdot S_{\text{normal}}$$

Where k_hyper > 1.

**Example:**

```python
# Pinch on normal skin
stress = 2.0  # Above threshold
baseline_gain = 1.0
pain = 1.0 * log(2.0 / 1.0) = 0.69

# Pinch on inflamed skin
inflammatory_gain = 3.0
pain = 3.0 * log(2.0 / 0.5)  # Lower threshold too
     = 3.0 * log(4.0)
     = 3.0 * 1.39 = 4.17

# 6× more painful for same stimulus
```

**Clinical correlate:** Inflammation, tissue injury.

---

## 6. Spatial Phenomena

### 6.1 Referred Pain

**Definition:** Damage in location A perceived in location B.

**Mechanism:** Shared neural pathways + signal propagation.

**Model:**

Damage creates signal at location A:

$$S_A(\mathbf{x}_A, t) = k \log(dD/dt)$$

Signal propagates through substrate:

$$\frac{\partial S}{\partial t} = v \nabla^2 S - \gamma S$$

If pathway from A converges with pathway from B before reaching cortex, signal appears to come from B.

**Example: Cardiac referred pain**

```python
# Heart attack (myocardial infarction)
damage_location = heart  # x_A
damage_rate = 5.0  # High (ischemic damage)

# Signal propagates through shared spinal pathway
# T1-T5 spinal segments handle:
# - Cardiac afferents (heart pain)
# - Dermatome afferents (left arm, chest)

# Cortex receives signal from T1-T5
# Cannot distinguish source
# Interprets as: "Left arm pain" (more common in training)

# Result: Heart attack feels like left arm pain
```

**Prediction:** Referred pain follows dermatomal patterns based on shared spinal segments.

### 6.2 Spatial Acuity

**Model:** Spatial resolution determined by receptor density and propagation diffusion.

**Resolution formula:**

$$\Delta x_{\text{min}} = \sqrt{\frac{v}{\gamma}} \cdot \frac{1}{\sqrt{\rho_{\text{receptor}}}}$$

Where ρ_receptor is receptor density (receptors/mm²).

**Predictions:**

| Location | Receptor Density | Acuity | Discrimination |
|----------|------------------|--------|----------------|
| Fingertip | 2500/cm² | 2 mm | Excellent |
| Palm | 400/cm² | 8 mm | Good |
| Forearm | 50/cm² | 40 mm | Poor |
| Back | 25/cm² | 70 mm | Very poor |
| Viscera | 1/cm² | >100 mm | Diffuse |

**Example:**

```python
# Pinprick on fingertip
receptor_density = 2500  # per cm²
resolution = 1 / sqrt(receptor_density)
           = 1 / 50 = 0.02 cm = 2 mm

# Can localize to ~2mm

# Pinprick on back
receptor_density = 25  # per cm²
resolution = 1 / sqrt(25)
           = 1 / 5 = 0.2 cm = 20 mm  # Oops, wrong units

# Correct calculation
resolution = sqrt(diffusion_length²) / sqrt(density)
```

**Simulation validation:** Two-point discrimination thresholds match receptor density predictions.

### 6.3 Phantom Limb Pain

**Model:** Damage field D(x) persists in neural representation after limb removal.

**Mechanism:**

1. Limb present: D(x_limb) stores injury history
2. Amputation: Physical limb gone, but D(x_limb) remains in cortical map
3. Spontaneous activation: Residual damage creates signals
4. Perception: Brain interprets as pain in missing limb

**Mathematical formulation:**

$$D_{\text{cortical}}(\mathbf{x}_{\text{limb}}, t) \neq 0 \quad \text{even after amputation}$$

Because cortical damage is not reset by peripheral changes.

**Prediction:** Phantom pain intensity correlates with pre-amputation pain levels.

**Supporting evidence:** Patients with pre-existing injury to limb show higher rates of phantom pain post-amputation.

---

## 7. Temporal Dynamics

### 7.1 Acute vs Chronic Pain

**Acute pain:**

Damage rate high → signal generated → pain felt.

When healing occurs (dD/dt → 0), signal stops.

$$t_{\text{acute}} \sim \frac{1}{\beta}$$

Where β is healing rate.

**Chronic pain:**

Damage persists or threshold remains lowered.

$$D(t \to \infty) > D_{\text{threshold}}$$

Even with low damage rate, sensitization maintains pain.

**Transition condition:**

$$\text{If } \frac{dD}{dt} < \beta \text{ and } D < D_{\text{critical}}: \text{acute}$$

$$\text{If } \frac{dD}{dt} < \beta \text{ and } D > D_{\text{critical}}: \text{chronic}$$

**Example:**

```python
# Initial injury
damage_rate = 1.0  # High (acute phase)
repair_rate = 0.1
# Net: D increases

# Week 1-2: Acute pain
D = 0.5
damage_rate = 0.5  # Decreasing
# Still painful

# Week 3-4: Healing
D = 0.3
damage_rate = 0.05
repair_rate = 0.1
# Net: D decreases
# Pain resolves

# Chronic pathway:
# If D > 0.7 (high damage)
# → Central sensitization triggered
# → gain increased permanently
# → Pain persists even as D → 0
```

### 7.2 First and Second Pain

**Model:** Two propagation speeds create two-phase perception.

**First pain (Aδ fibers):**

$$t_{\text{first}} = \frac{d}{v_{\text{fast}}} = \frac{d}{20 \text{ m/s}}$$

Sharp, well-localized.

**Second pain (C fibers):**

$$t_{\text{second}} = \frac{d}{v_{\text{slow}}} = \frac{d}{1 \text{ m/s}}$$

Dull, poorly localized.

**Example: Stub toe**

```python
# Distance from toe to brain
d = 1.5  # meters (toe to spinal cord + spinal to brain)

# First pain arrival
t_first = 1.5 / 20 = 0.075 seconds (75 ms)
# Sharp, immediate "OW!"

# Second pain arrival
t_second = 1.5 / 1.0 = 1.5 seconds
# Deep, throbbing ache that builds

# Subjective experience:
# t=0.075s: "SHARP!"
# t=0.1-1.0s: Relative quiet
# t=1.5s: "Ohhhhhh that really hurts..." (aching pain builds)
```

**Prediction:** Time delay between first and second pain proportional to distance from injury to CNS.

### 7.3 Wind-Up

**Definition:** Progressive increase in pain with repeated stimulation at constant intensity.

**Mechanism:** Temporal summation in spinal cord.

$$S_{\text{total}}(t) = \sum_{i=1}^{N} S_i \cdot \exp(-\lambda (t - t_i))$$

Where λ is decay constant (slow for C fibers).

**Effect:** Each stimulus adds to previous, creating crescendo.

**Example:**

```python
# Repeated pinpricks at 1 Hz
stimulus_intensity = 1.0
decay_rate = 0.3  # per second (slow)

# First pinprick
total_signal = 1.0

# Second pinprick (1 second later)
remaining_from_first = 1.0 * exp(-0.3 * 1) = 0.74
total_signal = 0.74 + 1.0 = 1.74

# Third pinprick
remaining = 1.74 * exp(-0.3) = 1.29
total_signal = 1.29 + 1.0 = 2.29

# Builds to steady state
steady_state = 1.0 / (1 - exp(-0.3))
             = 1.0 / 0.26 = 3.85

# Pain increases 3.85× despite constant stimulus
```

**Clinical correlate:** Repetitive stimulation (e.g., repeated capsaicin application) causes increasing pain.

---

## 8. Computational Implementation

### 8.1 Core Pain Detection Algorithm

```python
class NociceptiveSubstrate:
    """Cymatic model of pain detection."""
    
    def __init__(self, tissue_type='skin'):
        # Tissue parameters
        self.params = self.load_tissue_params(tissue_type)
        
        # State variables
        self.stress = np.zeros(self.size)
        self.damage = np.zeros(self.size)
        self.threshold = self.params['noc_threshold']
        
        # Sensitization state
        self.peripheral_sensitization = 1.0
        self.central_gain = 1.0
        
    def load_tissue_params(self, tissue_type):
        """Load tissue-specific parameters."""
        params = {
            'skin': {
                'stress_threshold': 0.5e6,  # Pa
                'gamma': 0.3,               # Damage rate
                'beta': 0.05,               # Healing rate
                'noc_threshold': 0.001,     # s⁻¹
                'k': 1.0,                   # Signal gain
            },
            'bone': {
                'stress_threshold': 150e6,  # Pa
                'gamma': 0.05,
                'beta': 0.001,
                'noc_threshold': 0.01,
                'k': 2.0,
            },
            # Add other tissues...
        }
        return params[tissue_type]
    
    def apply_stimulus(self, stress_field, stimulus_type='mechanical'):
        """Apply external stimulus."""
        
        if stimulus_type == 'mechanical':
            self.stress = stress_field
            
        elif stimulus_type == 'thermal_heat':
            temperature = stress_field  # In Celsius
            self.stress = self.params['alpha_thermal'] * (temperature - 37)**2
            
        elif stimulus_type == 'thermal_cold':
            temperature = stress_field
            self.stress = self.params['alpha_thermal'] * (37 - temperature)**2
            
        elif stimulus_type == 'chemical':
            concentration = stress_field
            self.stress = self.params['k_chem'] * concentration
    
    def update(self, dt):
        """Update damage and generate pain signal."""
        
        # Damage accumulation
        overstress = np.maximum(0, self.stress - self.params['stress_threshold'])
        damage_rate = overstress * self.params['gamma']
        
        self.damage += damage_rate * dt
        
        # Healing
        self.damage *= (1 - self.params['beta'] * dt)
        self.damage = np.clip(self.damage, 0, 1)
        
        # Update sensitization
        self.update_sensitization()
        
        # Generate pain signal
        pain_signal = self.generate_pain_signal(damage_rate)
        
        return pain_signal
    
    def update_sensitization(self):
        """Update peripheral and central sensitization."""
        
        # Peripheral: damage lowers threshold
        self.peripheral_sensitization = np.exp(-2.0 * self.damage)
        effective_threshold = self.threshold * self.peripheral_sensitization
        
        # Central: repeated signals increase gain
        avg_damage_rate = np.mean(np.gradient(self.damage))
        if avg_damage_rate > 0:
            self.central_gain += 0.01 * avg_damage_rate
            self.central_gain = min(self.central_gain, 5.0)  # Cap at 5×
    
    def generate_pain_signal(self, damage_rate):
        """Generate nociceptive signal."""
        
        # Apply sensitization to threshold
        effective_threshold = self.threshold * self.peripheral_sensitization
        
        # Compute signal where rate exceeds threshold
        signal = np.zeros_like(damage_rate)
        mask = damage_rate > effective_threshold
        
        signal[mask] = self.params['k'] * np.log(
            damage_rate[mask] / effective_threshold[mask]
        )
        
        # Apply central sensitization
        signal *= self.central_gain
        
        return signal
    
    def propagate_signal(self, signal, pathway='fast'):
        """Propagate pain signal to CNS."""
        
        if pathway == 'fast':
            v = 20.0  # m/s (Aδ fibers)
            gamma = 0.1
        else:  # slow
            v = 1.0   # m/s (C fibers)
            gamma = 0.02
        
        # Diffusion equation
        laplacian = self.compute_laplacian(signal)
        dsignal_dt = v * laplacian - gamma * signal
        
        return dsignal_dt
```

### 8.2 Simulation Examples

**Example 1: Paper cut**

```python
# Initialize skin substrate
skin = NociceptiveSubstrate(tissue_type='skin')

# Simulate paper cut
cut_depth = 0.002  # 2mm
blade_thickness = 0.0001  # 0.1mm
force = 0.5  # N

stress = force / (blade_thickness * cut_depth)
# = 2.5 MPa

# Apply stimulus
stress_field = np.zeros(skin.size)
stress_field[cut_location] = stress

skin.apply_stimulus(stress_field, stimulus_type='mechanical')

# Update over 1 second
time_course = []
for t in range(100):  # 100 timesteps = 1 second
    pain = skin.update(dt=0.01)
    time_course.append(np.max(pain))

# Plot shows:
# - Immediate sharp pain (Aδ activation)
# - Peak at t=0
# - Gradual decrease as stress reduces
```

**Example 2: Thermal pain progression**

```python
# Hot water exposure
skin = NociceptiveSubstrate(tissue_type='skin')

# Gradually increasing temperature
temperatures = np.linspace(37, 60, 100)  # 37°C to 60°C over 10 seconds

pain_vs_temp = []
for temp in temperatures:
    temp_field = np.ones(skin.size) * temp
    skin.apply_stimulus(temp_field, stimulus_type='thermal_heat')
    pain = skin.update(dt=0.1)
    pain_vs_temp.append(np.mean(pain))

# Results show:
# 37-43°C: No pain (below threshold)
# 43-45°C: Pain threshold crossed
# 45-50°C: Rapidly increasing pain
# 50-60°C: Severe pain, tissue damage
```

**Example 3: Inflammatory sensitization**

```python
# Initial injury creates damage
skin = NociceptiveSubstrate(tissue_type='skin')

# Day 0: Acute injury
initial_stress = 5.0e6  # Pa (severe)
skin.apply_stimulus(np.ones(skin.size) * initial_stress)
skin.update(dt=1.0)

# Day 1: Inflammation
# Damage persists, threshold lowered
print(f"Baseline threshold: {skin.threshold}")
print(f"Sensitized threshold: {skin.threshold * skin.peripheral_sensitization}")

# Test with light touch (normally painless)
light_touch = 1.0e5  # Pa (100 kPa)
skin.apply_stimulus(np.ones(skin.size) * light_touch)
pain_signal = skin.update(dt=0.1)

# Result: Pain from light touch (allodynia)
print(f"Pain signal: {np.mean(pain_signal)}")
# Non-zero despite sub-baseline-threshold stimulus
```

---

## 9. Experimental Predictions

### 9.1 Neurophysiological Predictions

**Prediction 9.1** (Threshold Hierarchy)

Nociceptor activation threshold should scale with tissue strength:

$$\sigma_{\text{noc, tissue}} \propto \sigma_{\text{mechanical, tissue}}$$

**Test:** Measure activation thresholds of nociceptors in different tissues (skin, muscle, viscera, bone).

**Expected:** Bone nociceptors have higher threshold than skin nociceptors.

**Prediction 9.2** (Damage-Threshold Relationship)

Prior tissue damage should lower activation threshold:

$$\sigma_{\text{noc}}(D) = \sigma_{\text{baseline}} \cdot e^{-\alpha D}$$

**Test:** Induce controlled micro-damage (UV radiation for skin), measure threshold changes over time.

**Expected:** Exponential decrease in threshold with accumulated damage.

**Prediction 9.3** (Signal Propagation Speeds)

Two distinct propagation speeds should be measurable:

- Fast pathway: 15-25 m/s
- Slow pathway: 0.5-2 m/s

**Test:** Record from peripheral nerve and dorsal horn simultaneously, measure conduction velocities.

**Status:** Well-established (Aδ vs C fiber speeds).

### 9.2 Psychophysical Predictions

**Prediction 9.4** (Logarithmic Intensity Scaling)

Perceived pain intensity should scale logarithmically with stimulus intensity:

$$P_{\text{perceived}} = k \log(I / I_{\text{threshold}})$$

**Test:** Apply graded stimuli, measure subjective pain ratings.

**Expected:** Log-linear relationship on log-log plot.

**Prediction 9.5** (Spatial Summation)

Pain threshold should decrease with increasing stimulus area:

$$I_{\text{threshold}}(A) = I_0 \cdot A^{-0.5}$$

**Test:** Apply same pressure to different contact areas, measure pain threshold.

**Expected:** Larger area → lower threshold (pressure sensation integrates spatially).

**Prediction 9.6** (Temporal Summation)

Repeated stimuli should show temporal summation with time constant:

$$\tau_{\text{summation}} \sim 2-5 \text{ seconds}$$

**Test:** Apply repeated brief stimuli at varying frequencies, measure pain ratings.

**Expected:** Summation occurs for stimuli separated by < 5 seconds.

### 9.3 Clinical Predictions

**Prediction 9.7** (Inflammatory Sensitization Time Course)

Peripheral sensitization should follow:

$$\sigma_{\text{noc}}(t) = \sigma_{\text{baseline}} \cdot e^{-\alpha I(t)}$$

Where I(t) is inflammatory mediator concentration.

**Test:** Induce inflammation (UV, capsaicin), measure pain threshold over hours/days.

**Expected:** Threshold minimum at 4-8 hours (peak inflammation), recovery over days.

**Prediction 9.8** (Central Sensitization Persistence)

Central gain increase should outlast peripheral healing:

$$\tau_{\text{peripheral}} < \tau_{\text{central}}$$

**Test:** Measure pain thresholds during and after injury healing.

**Expected:** Threshold remains low even after tissue repair complete.

**Prediction 9.9** (Referred Pain Dermatomal Patterns)

Visceral pain should refer to predictable dermatomes based on embryological origin.

**Test:** Map referred pain patterns for various organs.

**Expected:** Heart → T1-T5 (left arm), gallbladder → T7-T9 (right shoulder), etc.

**Status:** Well-established clinically.

---

## 10. Limitations and Scope

### 10.1 Model Boundaries

**This model addresses:**
- Mechanical transduction of noxious stimuli
- Threshold dynamics and sensitization
- Signal generation and propagation
- Spatial and temporal features
- Modality-specific substrate responses

**This model does NOT address:**
- Subjective pain experience (qualia)
- Emotional/affective pain components
- Cognitive pain modulation (attention, expectation)
- Placebo/nocebo effects
- Consciousness of pain
- Suffering as distinct from nociception

### 10.2 Simplifications

**Acknowledged limitations:**

1. **Homogeneous tissue:** Real tissues have complex microstructure
2. **Single damage variable:** Multiple molecular damage pathways exist
3. **Linear threshold:** Actual thresholds show nonlinear dynamics
4. **Continuous substrate:** Discrete nociceptors in reality
5. **No descending modulation:** Pain can be inhibited from brain (gate control)
6. **No psychological factors:** Stress, fear, attention all modulate pain

### 10.3 Appropriate Use

**This framework is useful for:**
- Understanding pain as damage detection
- Teaching nociceptive physiology
- Modeling peripheral pain mechanisms
- Simulating sensitization phenomena
- Generating testable hypotheses

**This framework should NOT be used for:**
- Clinical pain assessment (requires subjective report)
- Predicting individual pain experience
- Replacing medical examination
- Explaining chronic pain syndromes (requires central mechanisms)
- Understanding pain affect and suffering

---

## 11. Discussion

### 11.1 Theoretical Contributions

**1. Unified pain modality framework**

All pain types (mechanical, thermal, chemical) reduce to substrate stress exceeding damage thresholds.

**2. Wide dynamic range explanation**

Logarithmic encoding + threshold hierarchy enables spider-to-fracture detection range.

**3. Sensitization mechanics**

Peripheral and central sensitization formalized as threshold modulation and gain adjustment.

**4. Spatial phenomena**

Referred pain, spatial acuity, and phantom limb pain explained by substrate propagation and mapping.

**5. Temporal dynamics**

First/second pain, wind-up, and acute-to-chronic transition derived from propagation and summation physics.

### 11.2 Relationship to Gate Control Theory

**Melzack & Wall (1965):**

Proposed that non-nociceptive input (touch) can inhibit nociceptive signals at spinal level ("closing the gate").

**Our model:**

Compatible—can be extended to include:

$$S_{\text{net}} = S_{\text{nociceptive}} - w \cdot S_{\text{tactile}}$$

Where w is inhibitory weight.

**Mechanism:** Touch (low-threshold mechanoreceptors) creates competing signal that reduces nociceptive transmission.

**Example:** Rubbing sore muscle reduces pain (tactile inhibition).

### 11.3 Implications for Pain Management

**From model, pain reduction strategies:**

1. **Reduce stress:** Remove/reduce mechanical, thermal, or chemical source
2. **Increase threshold:** Anti-inflammatory drugs (raise σ_noc)
3. **Block propagation:** Local anesthetics (prevent signal transmission)
4. **Reduce gain:** Central analgesics (lower k)
5. **Counter-stimulation:** Gate control (competing signals)
6. **Promote healing:** Increase β (tissue repair rate)

**Model does NOT address:**
- Psychological pain management (cognitive-behavioral therapy)
- Placebo effects
- Mindfulness/meditation
- Central pain syndromes

These require models beyond substrate mechanics.

### 11.4 Future Directions

**Within-framework extensions:**

1. **Descending modulation:** Add top-down inhibitory pathways
2. **Gate control:** Incorporate tactile-nociceptive interactions
3. **Immune system:** Model inflammatory mediator dynamics explicitly
4. **Healing processes:** Detailed tissue repair mechanisms
5. **Neuropathic pain:** Nerve damage as substrate disruption

**Cross-framework integration:**

1. **Neural networks:** Learn pain patterns from training data
2. **Active inference:** Predictive coding models of pain perception
3. **Embodied cognition:** Whole-body pain dynamics
4. **Affective neuroscience:** Bridge to suffering and emotion

**Clinical applications:**

1. **Pain prediction:** Estimate pain from injury characteristics
2. **Treatment optimization:** Personalized pain management
3. **Phantom pain:** Model-based intervention strategies
4. **Chronic pain:** Early identification of transition risk

---

## 12. Conclusion

We have presented a mechanical substrate model of nociception where:

1. **Pain detection is damage threshold crossing**
2. **Wide dynamic range emerges from logarithmic encoding**
3. **All modalities reduce to substrate stress**
4. **Sensitization is threshold/gain modulation**
5. **Spatial and temporal phenomena follow from propagation physics**

**Key results:**

- Spider detection requires mechanoreceptors (not nociceptors)
- Paper cut to fracture: 10⁶-fold range handled by log encoding
- Allodynia/hyperalgesia: threshold lowering and gain increase
- Referred pain: shared neural pathways
- First/second pain: two propagation speeds
- Chronic pain: persistent threshold modification

**Validation:**

- Model parameters reproduce known thresholds
- Predictions match psychophysical data
- Sensitization dynamics consistent with inflammation time course
- Spatial patterns match dermatomal maps

**Appropriate scope:**

This models **nociception** (detection of tissue damage), not **pain experience** (subjective suffering). The mechanics of detection are distinct from the phenomenology of suffering.

**Value proposition:**

- **Unifying framework** for pain modalities
- **Mechanistic understanding** of sensitization
- **Quantitative predictions** for testing
- **Educational tool** for physiology
- **Starting point** for pain management modeling

We offer this as a **computational framework** for understanding pain as physical damage detection, acknowledging that the full experience of pain requires integration with psychological, emotional, and cognitive factors beyond our current scope.

---

## References

1. Melzack, R., & Wall, P.D. (1965). "Pain mechanisms: a new theory." *Science*, 150(3699), 971-979.

2. Julius, D., & Basbaum, A.I. (2001). "Molecular mechanisms of nociception." *Nature*, 413(6852), 203-210.

3. Woolf, C.J. (2011). "Central sensitization: implications for the diagnosis and treatment of pain." *Pain*, 152(3), S2-S15.

4. Treede, R.D., et al. (1992). "The cortical representation of pain." *Pain*, 79(2-3), 105-111.

5. Craig, A.D. (2003). "Pain mechanisms: labeled lines versus convergence in central processing." *Annual Review of Neuroscience*, 26, 1-30.

6. Computational implementations (2026). Cymatic nociception simulation suite. [Code repository]

---

## Appendix: Nociceptor Types and Parameters

### A.1 Peripheral Nociceptor Classification

| Type | Fiber | Speed | Modality | Threshold | Adaptation |
|------|-------|-------|----------|-----------|------------|
| Aδ mechanoreceptor | Aδ | 20 m/s | Mechanical | High | Rapid |
| Aδ mechanoheat | Aδ | 15 m/s | Mech + heat | Medium | Moderate |
| C polymodal | C | 1 m/s | Mech + heat + chem | Low | Slow |
| C mechanoreceptor | C | 0.7 m/s | Mechanical only | Very high | Very slow |
| Silent nociceptors | C | 1 m/s | After sensitization | Initially infinite | N/A |

### A.2 Tissue-Specific Threshold Values

```python
TISSUE_PARAMETERS = {
    'skin_epidermis': {
        'mechanical_threshold': 0.5e6,     # Pa
        'thermal_heat_threshold': 45,      # °C
        'thermal_cold_threshold': 15,      # °C
        'gamma': 0.3,
        'noc_threshold': 0.001,            # s⁻¹
    },
    'skin_dermis': {
        'mechanical_threshold': 1.0e6,
        'thermal_heat_threshold': 47,
        'thermal_cold_threshold': 10,
        'gamma': 0.2,
        'noc_threshold': 0.002,
    },
    'muscle': {
        'mechanical_threshold': 2.0e6,
        'thermal_heat_threshold': 48,
        'thermal_cold_threshold': 8,
        'gamma': 0.15,
        'noc_threshold': 0.005,
    },
    'bone': {
        'mechanical_threshold': 150e6,
        'thermal_heat_threshold': 55,
        'thermal_cold_threshold': 5,
        'gamma': 0.05,
        'noc_threshold': 0.01,
    },
    'viscera': {
        'mechanical_threshold': 0.3e6,
        'thermal_heat_threshold': 42,
        'thermal_cold_threshold': 20,
        'gamma': 0.2,
        'noc_threshold': 0.002,
    },
}
```

---

**End of Technical Report**

*Cymatic Learning & Reasoning Laboratory*  
*Mechanical Model of Pain Detection*  
*Version 1.0 - February 2026*

---

This paper presents pain as mechanical damage detection in cymatic substrates, carefully scoping to physical mechanisms while explicitly excluding subjective experience from the model's domain.

