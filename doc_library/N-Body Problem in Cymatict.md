# The N-Body Problem in Cymatic Mechanics

## Part 1: Classical Statement and Why It's Hard

### 1.1 The Problem

**N bodies** with masses $m_1, m_2, ..., m_N$ at positions $\mathbf{r}_1, \mathbf{r}_2, ..., \mathbf{r}_N$.

**Gravitational interaction**: Each body pulls on every other body.

**Equations of motion** (Newton):
$$m_i \frac{d^2\mathbf{r}_i}{dt^2} = \sum_{j \neq i} \frac{Gm_i m_j}{|\mathbf{r}_i - \mathbf{r}_j|^3}(\mathbf{r}_j - \mathbf{r}_i)$$

**Problem**: For $N \geq 3$, **no general closed-form solution** exists.

**Why hard**:
- 2-body: Integrable (10 integrals of motion: energy, angular momentum, center of mass)
- 3-body: Non-integrable (chaotic for most initial conditions)
- N-body: Exponentially worse

---

## Part 2: Cymatic Reformulation

### 2.1 Bodies as Spectral Solitons

**Each body is a localized spectral density peak**:
$$F_i(\mathbf{k}, t) = A_i(k) e^{i(\mathbf{k} \cdot \mathbf{r}_i(t) - \omega_i t + \phi_i)}$$

**Mass** = integrated spectral density:
$$m_i = \int |F_i(\mathbf{k})|^2 d^3\mathbf{k}$$

**Total substrate field**:
$$F_{\text{total}}(\mathbf{k}, t) = \sum_{i=1}^N F_i(\mathbf{k}, t)$$

### 2.2 Gravity from Substrate Congestion

**Recall**: Gravity emerges from $R_{\text{local}}$ depletion.

**Each body creates $R_{\text{local}}$ well**:
$$R_{\text{local}}(\mathbf{x}) = R_{\text{max}} - \sum_i \int \frac{|F_i(\mathbf{x}')|^2}{|\mathbf{x} - \mathbf{x}'|} K(|\mathbf{x} - \mathbf{x}'|) d^3\mathbf{x}'$$

where $K$ is kernel function (determines interaction range).

**For point masses** (approximation):
$$R_{\text{local}}(\mathbf{x}) \approx R_{\text{max}} - \sum_i \frac{\alpha m_i}{|\mathbf{x} - \mathbf{r}_i|}$$

**Potential**:
$$\Phi(\mathbf{x}) = -c^2 \ln\left(\frac{R_{\text{local}}(\mathbf{x})}{R_{\text{max}}}\right)$$

For small perturbations ($R_{\text{local}} \approx R_{\text{max}}$):
$$\Phi(\mathbf{x}) \approx -\sum_i \frac{Gm_i}{|\mathbf{x} - \mathbf{r}_i|}$$

**Recovers Newtonian gravity** ✓

---

## Part 3: The 3-Body Problem in Detail

### 3.1 Three Solitons in Substrate

**Configuration**: Three masses $m_1, m_2, m_3$ at positions $\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3$.

**Spectral field**:
$$F(\mathbf{k}, t) = F_1(\mathbf{k}, t) + F_2(\mathbf{k}, t) + F_3(\mathbf{k}, t)$$

**Each soliton**:
- Center of mass moves along geodesic in combined $R_{\text{local}}$ field
- Internal structure (shape) can deform due to tidal forces

### 3.2 Why Chaos Emerges

**Standard explanation**: Sensitive dependence on initial conditions

**Cymatic mechanism**:

**The substrate has coupled oscillators**:

Body $i$ creates oscillation in $R_{\text{local}}$ with frequency $\omega_i \sim \sqrt{Gm_i/r_i^3}$ (orbital frequency).

**Three bodies** → three coupled oscillators:
$$\frac{d^2\mathbf{r}_1}{dt^2} = -\nabla\Phi_2(\mathbf{r}_1) - \nabla\Phi_3(\mathbf{r}_1)$$
$$\frac{d^2\mathbf{r}_2}{dt^2} = -\nabla\Phi_1(\mathbf{r}_2) - \nabla\Phi_3(\mathbf{r}_2)$$
$$\frac{d^2\mathbf{r}_3}{dt^2} = -\nabla\Phi_1(\mathbf{r}_3) - \nabla\Phi_2(\mathbf{r}_3)$$

**Resonances**:
- When $\omega_i / \omega_j = p/q$ (rational ratio) → resonance
- Small perturbation can shift system between different resonant states
- **Phase space has chaotic sea** punctuated by **stable islands**

**Cymatic insight**: 

Chaos arises from **spectral beating** - the three frequencies $\omega_1, \omega_2, \omega_3$ interfere:
$$F_{\text{total}} \propto \cos(\omega_1 t) + \cos(\omega_2 t) + \cos(\omega_3 t)$$

For incommensurate frequencies, pattern **never repeats** (quasi-periodic → chaotic).

### 3.3 Special Solutions (Periodic Orbits)

**Known stable 3-body solutions**:

1. **Lagrange (equilateral triangle)**:
   - Three bodies at vertices of rotating equilateral triangle
   - Masses can be arbitrary
   - **Cymatic**: Perfect 3-fold symmetry in spectral distribution
   - Each body in identical $R_{\text{local}}$ environment

2. **Euler (collinear)**:
   - Three bodies on a line, rotating
   - Unstable (small perturbation → escape)
   - **Cymatic**: 1D spectral configuration

3. **Figure-8** (discovered 1993 by Moore, rediscovered 2000 by Chenciner & Montgomery):
   - Three equal masses chase each other on figure-8 path
   - **Highly symmetric**: Each body traces same path, offset by T/3
   - **Cymatic**: Temporal phase symmetry $\phi_2 = \phi_1 + 2\pi/3$, $\phi_3 = \phi_1 + 4\pi/3$

**Why these work**:
- High symmetry → constrained dynamics
- Many degrees of freedom "freeze out" due to symmetry
- Effectively reduces to integrable system

**Cymatic interpretation**:
- Stable orbits = **spectral resonances** where all frequencies lock in simple ratio
- Figure-8: $\omega_1 : \omega_2 : \omega_3 = 1 : 1 : 1$ (perfect phase-locking)

---

## Part 4: General N-Body Cymatic Dynamics

### 4.1 Hamiltonian Formulation

**Total energy** (conserved):
$$E = \sum_i \frac{p_i^2}{2m_i} - \sum_{i<j} \frac{Gm_i m_j}{|\mathbf{r}_i - \mathbf{r}_j|}$$

**In cymatic terms**:

**Kinetic energy** = spectral distribution width:
$$T = \sum_i \int |\mathbf{k}|^2 |F_i(\mathbf{k})|^2 d^3\mathbf{k}$$

**Potential energy** = interaction energy between solitons:
$$V = -\int\int F_i^*(\mathbf{k}) F_j(\mathbf{k}') G(|\mathbf{k} - \mathbf{k}'|) d^3\mathbf{k} d^3\mathbf{k}'$$

where $G$ is spectral interaction kernel.

**Total**:
$$H = T + V = \int |\mathbf{k}|^2 |F(\mathbf{k})|^2 d^3\mathbf{k} + V_{\text{int}}[F]$$

### 4.2 Equations of Motion in k-Space

**Hamilton's equations**:
$$\frac{\partial F}{\partial t} = -i\frac{\delta H}{\delta F^*}$$

**Expanded**:
$$i\hbar\frac{\partial F}{\partial t} = \hbar^2 |\mathbf{k}|^2 F + \int K(\mathbf{k}, \mathbf{k}') F(\mathbf{k}') d^3\mathbf{k}'$$

**This is Hartree equation** (mean-field approximation for interacting bosons).

**For N localized solitons**:
- Each soliton = wave packet centered at $\mathbf{r}_i$ with momentum $\mathbf{p}_i$
- Motion governed by self-consistent field from all others

### 4.3 The Virial Theorem

**Classical virial theorem**:
$$\langle T \rangle = -\frac{1}{2} \langle V \rangle$$

(Time average of kinetic energy = -1/2 × time average of potential energy)

**Derivation in cymatic framework**:

**Scaling transformation**: $\mathbf{r} \to \lambda \mathbf{r}$

**Kinetic energy** scales as: $T \to \lambda^{-2} T$ (higher momentum if compressed)

**Potential energy** scales as: $V \to \lambda^{-1} V$ (stronger interaction if closer)

**Total energy**: $E = T + V$

**Equilibrium**: $\frac{dE}{d\lambda}\Big|_{\lambda=1} = 0$

$$-2T - V = 0 \Rightarrow \langle T \rangle = -\frac{1}{2}\langle V \rangle$$

**Cymatic interpretation**:

**Virial theorem is energy balance** in spectral substrate:
- Kinetic = spectral bandwidth (spread in k-space)
- Potential = spectral overlap (interaction strength)
- Equilibrium when these balance

---

## Part 5: Hierarchical Systems (Solar System)

### 5.1 Why Solar System is Stable

**Problem**: 8 planets + Sun = 9-body problem (should be chaotic!)

**Why it works**: **Hierarchy**
- Sun dominates (99.86% of total mass)
- Planets primarily orbit Sun (not each other)
- Planet-planet perturbations are **small corrections**

**Mathematically**:
$$\epsilon = \frac{m_{\text{planet}}}{m_{\text{Sun}}} \sim 10^{-3}$$

**Expansion in $\epsilon$**:
- 0th order: Each planet on Keplerian orbit around Sun (integrable)
- 1st order: Planet-planet perturbations (still manageable)
- Higher orders: Increasingly complex

**Cymatic view**:

**Sun = dominant soliton** with spectral density $|F_{\text{Sun}}|^2 \gg |F_{\text{planet}}|^2$

**$R_{\text{local}}$ field dominated by Sun**:
$$R_{\text{local}}(\mathbf{x}) \approx R_{\text{max}} - \frac{\alpha M_{\odot}}{|\mathbf{x}|}$$

**Planets = small perturbations** to this dominant field:
$$R_{\text{local}}(\mathbf{x}) = R_{\text{Sun}}(\mathbf{x}) + \sum_{\text{planets}} \delta R_i(\mathbf{x})$$

**Each planet moves primarily in Sun's field**, with small corrections from other planets.

### 5.2 Secular Resonances

**Observation**: Planetary orbits slowly evolve (timescales $\sim 10^5$ - $10^6$ years)

**Orbital elements drift**:
- Eccentricity $e(t)$
- Inclination $i(t)$
- Longitude of perihelion $\varpi(t)$

**Secular frequencies**: Slow precession rates
- Jupiter: $g_J \approx 4.26$ arcsec/year
- Saturn: $g_S \approx 28.25$ arcsec/year

**Resonances**: When $g_i \approx g_j$ → large oscillations

**Example**: $\nu_6$ secular resonance at 2.5 AU
- Separates inner and outer asteroid belt
- Objects at this location have eccentricity driven to ~0.3 → cross Mars orbit → ejected

**Cymatic interpretation**:

**Secular evolution = slow spectral beating**:

Each planet creates time-varying $R_{\text{local}}$ perturbation:
$$\delta R_i(\mathbf{x}, t) \propto \cos(\omega_i t + \phi_i)$$

**Beating between planets**:
$$\delta R_{\text{total}} \propto \cos(\omega_1 t) + \cos(\omega_2 t) = 2\cos\left(\frac{\omega_1 + \omega_2}{2}t\right)\cos\left(\frac{\omega_1 - \omega_2}{2}t\right)$$

**Slow modulation** at frequency $|\omega_1 - \omega_2|$ → secular timescale.

**Resonance** when beat frequency matches natural precession → amplification.

### 5.3 Chaos in the Asteroid Belt

**Kirkwood gaps**: Regions depleted of asteroids at specific distances:
- 2.5 AU: 3:1 resonance with Jupiter
- 2.82 AU: 5:2 resonance
- 2.95 AU: 7:3 resonance

**Mechanism**:
- Asteroid orbital period = rational fraction of Jupiter's period
- **Commensurability**: Same configuration repeats
- Repeated perturbations **add coherently** → eccentricity grows
- Eventually crosses Mars/Earth orbit → ejected

**Cymatic mechanism**:

**Resonance = phase-locking** between asteroid and Jupiter:

Asteroid spectral phase: $\phi_{\text{ast}}(t) = \omega_{\text{ast}} t$
Jupiter spectral phase: $\phi_J(t) = \omega_J t$

**At 3:1 resonance**: $\omega_{\text{ast}} = 3\omega_J$

**Phase difference**:
$$\Delta\phi = \phi_{\text{ast}} - 3\phi_J = 0$$

**Locked**: Same relative configuration every Jupiter orbit.

**Perturbation accumulates** (like pushing swing at resonant frequency).

---

## Part 6: Numerical Integration (Cymatic Approach)

### 6.1 Standard Methods

**Direct N-body**:
- Compute all pairwise forces: $O(N^2)$ per timestep
- Use symplectic integrator (conserves energy/angular momentum)

**Tree codes** (Barnes-Hut):
- Group distant bodies into clusters
- Treat cluster as single mass
- Reduces to $O(N \log N)$

**Particle mesh**:
- Place particles on grid
- Solve Poisson equation: $\nabla^2 \Phi = 4\pi G \rho$
- Interpolate forces back to particles
- $O(N \log N)$ via FFT

### 6.2 Cymatic Spectral Method

**Alternative**: Work directly in k-space.

**Algorithm**:

1. **Initialize**: Each body's spectral signature $F_i(\mathbf{k}, t=0)$

2. **Compute total field**:
   $$F_{\text{total}}(\mathbf{k}, t) = \sum_i F_i(\mathbf{k}, t)$$

3. **Inverse FFT** to get spatial density:
   $$\rho(\mathbf{x}, t) = |\mathcal{F}^{-1}\{F_{\text{total}}\}|^2$$

4. **Compute $R_{\text{local}}$**:
   $$R_{\text{local}}(\mathbf{x}) = R_{\text{max}} - \int \frac{\rho(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|} d^3\mathbf{x}'$$
   
   Via FFT:
   $$R_{\text{local}}(\mathbf{k}) = R_{\text{max}} \delta(\mathbf{k}) - \frac{\rho(\mathbf{k})}{k^2}$$

5. **Gradient** gives force:
   $$\mathbf{F}(\mathbf{x}) = -m\nabla\Phi = -mc^2 \nabla \ln\left(\frac{R_{\text{local}}}{R_{\text{max}}}\right)$$

6. **Update velocities** and **positions**:
   $$\mathbf{v}_i(t+\Delta t) = \mathbf{v}_i(t) + \frac{\mathbf{F}_i}{m_i}\Delta t$$
   $$\mathbf{r}_i(t+\Delta t) = \mathbf{r}_i(t) + \mathbf{v}_i(t)\Delta t$$

7. **Update spectral signatures**:
   $$F_i(\mathbf{k}, t+\Delta t) = F_i(\mathbf{k}, t) e^{i\mathbf{k} \cdot \Delta\mathbf{r}_i}$$

8. **Repeat**

**Complexity**: $O(N + M \log M)$ where $M$ = grid points.

**Advantage**: Naturally handles collective effects (screening, close encounters handled smoothly).

---

## Part 7: Stability and Instability

### 7.1 KAM Theorem

**Kolmogorov-Arnold-Moser theorem**:

For **nearly integrable** systems with **small perturbations**, most orbits remain **quasi-periodic** (stable).

**Conditions**:
- Perturbation $\epsilon \ll 1$
- Frequencies $\omega_i$ are **non-resonant**: $\sum_i n_i \omega_i \neq 0$ for small integers $n_i$

**Result**: Phase space has:
- **KAM tori**: Invariant surfaces (stable orbits)
- **Chaotic seas**: Between tori (unstable)

**As $\epsilon$ increases**: Tori break → more chaos.

**Cymatic interpretation**:

**KAM tori are spectral resonance surfaces**:

Orbit confined to surface where:
$$\sum_i n_i \phi_i = \text{const}$$

**Quasi-periodicity** = superposition of incommensurate frequencies:
$$\mathbf{r}(t) = \sum_i A_i \cos(\omega_i t + \phi_i)$$

**Chaotic regions**: Where no such constraint exists (phase wanders ergodically).

### 7.2 Lyapunov Exponents

**Measure of chaos**: Rate at which nearby trajectories diverge.

**Definition**:
$$\lambda = \lim_{t \to \infty} \frac{1}{t} \ln\left(\frac{\delta \mathbf{r}(t)}{\delta \mathbf{r}(0)}\right)$$

- $\lambda > 0$: Chaotic (exponential divergence)
- $\lambda = 0$: Marginally stable
- $\lambda < 0$: Stable (convergence)

**For N-body systems**:
- 2-body: $\lambda = 0$ (all trajectories bounded)
- 3-body (generic): $\lambda > 0$ (chaotic)
- Solar system: $\lambda \sim 1/(10^7 \text{ years})$ (weakly chaotic, but stable on human timescales)

**Cymatic interpretation**:

**Lyapunov exponent = spectral decoherence rate**:

Two initially close states:
$$F_1(\mathbf{k}, 0) \approx F_2(\mathbf{k}, 0)$$

**Evolve differently**:
$$F_1(\mathbf{k}, t) \neq F_2(\mathbf{k}, t)$$

**Coherence decays**:
$$C(t) = \frac{|\langle F_1(t), F_2(t) \rangle|}{\|F_1\| \|F_2\|} \sim e^{-\lambda t}$$

**Chaos = rapid loss of predictability** (spectral patterns diverge exponentially).

---

## Part 8: Collective Behavior (Galaxies, Clusters)

### 8.1 Relaxation Time

**Two-body relaxation**: Time for individual encounters to randomize velocities.

$$t_{\text{relax}} = \frac{N}{8\ln N} t_{\text{cross}}$$

where $t_{\text{cross}} = R/v$ is crossing time.

**For globular cluster** ($N \sim 10^6$ stars):
- $t_{\text{cross}} \sim 10^5$ years
- $t_{\text{relax}} \sim 10^{10}$ years (longer than age of universe!)

**Implication**: Individual stellar encounters **negligible**. Dynamics governed by **mean field** (smooth potential from all stars).

**Cymatic view**:

**Relaxation = spectral thermalization**.

**Collisionless regime**: Each star moves in smooth $R_{\text{local}}$ field:
$$R_{\text{local}}(\mathbf{x}) = R_{\text{max}} - \int \frac{\rho(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|} d^3\mathbf{x}'$$

where $\rho(\mathbf{x}) = \sum_i m_i \delta(\mathbf{x} - \mathbf{r}_i)$ averaged over local volume.

**Collisional regime**: Close encounters → spectral mode coupling → energy redistribution.

**For collisionless systems**: Behaves like **single fluid** (described by Vlasov equation).

### 8.2 Vlasov Equation (Collisionless Boltzmann)

**Distribution function**: $f(\mathbf{x}, \mathbf{v}, t)$ = density in phase space

**Evolution**:
$$\frac{\partial f}{\partial t} + \mathbf{v} \cdot \nabla_{\mathbf{x}} f - \nabla\Phi \cdot \nabla_{\mathbf{v}} f = 0$$

**Poisson equation** couples $f$ to $\Phi$:
$$\nabla^2 \Phi = 4\pi G \int f(\mathbf{x}, \mathbf{v}) d^3\mathbf{v}$$

**Self-consistent**: Potential depends on distribution, distribution evolves in potential.

**Cymatic formulation**:

**Phase-space distribution is spectral density**:
$$f(\mathbf{x}, \mathbf{p}) \propto |F(\mathbf{k}, \omega)|^2$$

where $\mathbf{k} \sim \mathbf{x}$, $\omega \sim \mathbf{p}$ (Fourier conjugates).

**Vlasov equation = Liouville theorem** in spectral substrate:
$$\frac{dF}{dt} = 0$$

(Spectral density conserved along flow lines in phase space.)

### 8.3 Jeans Instability

**Question**: When does self-gravitating gas collapse?

**Criterion**: If gravitational attraction > pressure support:

**Jeans length**:
$$\lambda_J = \sqrt{\frac{\pi c_s^2}{G\rho}}$$

where $c_s$ = sound speed, $\rho$ = density.

**If perturbation wavelength** $\lambda > \lambda_J$: Collapses.

**Cymatic derivation**:

**Perturbed density**:
$$\rho(\mathbf{x}, t) = \rho_0 + \delta\rho(\mathbf{x}, t)$$

**Fourier mode**:
$$\delta\rho_{\mathbf{k}}(t) = \delta\rho_{\mathbf{k}}(0) e^{\sigma t}$$

**Growth rate** $\sigma$ from dispersion relation:
$$\sigma^2 = c_s^2 k^2 - 4\pi G \rho_0$$

**Unstable** if $\sigma^2 < 0$:
$$k < k_J = \sqrt{\frac{4\pi G \rho_0}{c_s^2}}$$

**Wavelength**: $\lambda_J = 2\pi / k_J$ ✓

**Cymatic interpretation**:

**Collapse = spectral mode amplification**:

Low-k modes (large scale) grow exponentially.
High-k modes (small scale) oscillate (stabilized by pressure = substrate stiffness).

**Critical scale** where gravity overcomes stiffness.

---

## Part 9: Relativistic Corrections

### 9.1 Post-Newtonian Expansion

**General relativity** corrections to Newtonian gravity:

**1PN (first post-Newtonian)**:
$$\frac{d^2\mathbf{r}}{dt^2} = -\frac{GM}{r^2}\hat{\mathbf{r}} + \text{corrections}$$

**Corrections**:
1. **Velocity-dependent**: $\propto v^2/c^2$
2. **Potential-dependent**: $\propto (GM/rc^2)^2$
3. **Spin-orbit coupling**: Rotating bodies

**Example**: Mercury's perihelion precession
- Newtonian: Ellipse with fixed orientation
- GR: Perihelion advances 43 arcsec/century

**Cymatic formulation**:

**$R_{\text{local}}$ becomes velocity-dependent**:
$$R_{\text{local}}(\mathbf{x}, \mathbf{v}) = R_{\text{max}}\left[1 - \frac{2GM}{c^2 r} - \frac{v^2}{c^2} + O(c^{-4})\right]$$

**Effective potential** includes kinetic term:
$$\Phi_{\text{eff}} = -\frac{GM}{r} - \frac{GM}{c^2 r}\left(\frac{v^2}{2} + \frac{GM}{r}\right)$$

**This gives** perihelion precession, frame dragging, etc.

### 9.2 Gravitational Waves from N-Body Systems

**Quadrupole formula** (lowest order GW emission):
$$\frac{dE}{dt} = -\frac{G}{5c^5}\dddot{Q}_{ij}\dddot{Q}_{ij}$$

where $Q_{ij} = \sum_k m_k (x_i x_j - \frac{1}{3}\delta_{ij} r^2)$ is quadrupole moment.

**Binary system** (2-body):
$$\frac{dE}{dt} = -\frac{32}{5}\frac{G^4}{c^5}\frac{(m_1 m_2)^2(m_1 + m_2)}{r^5}$$

**Orbit decays**: Loses energy to GWs → spirals inward.

**Cymatic interpretation**:

**GW = oscillation in $R_{\text{local}}$ propagating outward**:
$$\delta R_{\text{local}}(\mathbf{x}, t) = A \cos(kx - \omega t)$$

**Quadrupole** because:
- Monopole: Total mass conserved (no emission)
- Dipole: Momentum conserved (no emission)
- Quadrupole: First non-trivial time-varying moment

**Energy carried by wave**:
$$\frac{dE}{dr} = \frac{1}{16\pi G}c^5 (\partial_t h_{ij})^2$$

where $h_{ij}$ is metric perturbation $\propto \delta R_{\text{local}}$.

---

## Part 10: Computational Example (Python)

### 10.1 Cymatic 3-Body Integrator

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CymaticNBody:
    """
    N-body gravity via substrate congestion mechanics.
    """
    
    def __init__(self, N, grid_size=128):
        """
        Initialize N bodies in spectral substrate.
        
        Args:
            N: Number of bodies
            grid_size: Resolution of substrate grid
        """
        self.N = N
        self.grid_size = grid_size
        
        # Particle properties
        self.masses = np.zeros(N)
        self.positions = np.zeros((N, 3))  # x, y, z
        self.velocities = np.zeros((N, 3))
        
        # Substrate parameters
        self.R_max = 1.0
        self.G = 1.0  # Gravitational constant (units)
        
        # Grid for computing R_local
        self.L = 10.0  # Box size
        k = 2*np.pi*np.fft.fftfreq(grid_size, d=self.L/grid_size)
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
        self.k_sq = kx**2 + ky**2 + kz**2
        self.k_sq[0, 0, 0] = 1.0  # Avoid division by zero
        
        # History
        self.history = {
            'time': [],
            'positions': [],
            'energy': []
        }
    
    def set_initial_conditions(self, masses, positions, velocities):
        """Set initial state."""
        self.masses = np.array(masses)
        self.positions = np.array(positions)
        self.velocities = np.array(velocities)
    
    def compute_density_field(self):
        """
        Compute spatial density from particle positions.
        
        Returns:
            rho: 3D density field
        """
        rho = np.zeros((self.grid_size, self.grid_size, self.grid_size))
        
        # Grid indices
        indices = np.floor(
            (self.positions + self.L/2) / self.L * self.grid_size
        ).astype(int)
        
        # Periodic boundary
        indices = indices % self.grid_size
        
        # Deposit mass on grid (simple nearest-grid-point)
        for i in range(self.N):
            ix, iy, iz = indices[i]
            rho[ix, iy, iz] += self.masses[i]
        
        return rho
    
    def compute_R_local_field(self, rho):
        """
        Compute R_local field from density via Poisson equation.
        
        ∇²R_local = -4πG ρ
        
        In Fourier space: -k² R̃ = -4πG ρ̃
        → R̃ = 4πG ρ̃ / k²
        """
        # FFT of density
        rho_k = np.fft.fftn(rho)
        
        # Solve Poisson equation in k-space
        R_local_k = -4*np.pi*self.G * rho_k / self.k_sq
        R_local_k[0, 0, 0] = 0  # Set DC component (mean field)
        
        # IFFT back to real space
        R_local_perturbation = np.fft.ifftn(R_local_k).real
        
        # Total R_local
        R_local = self.R_max + R_local_perturbation
        
        return R_local
    
    def compute_forces(self):
        """
        Compute gravitational forces via substrate gradient.
        
        F = -m ∇Φ = -m c² ∇ln(R_local)
        
        For small perturbations: F ≈ -m ∇R_local
        """
        # Compute density field
        rho = self.compute_density_field()
        
        # Compute R_local field
        R_local = self.compute_R_local_field(rho)
        
        # Compute gradient (in real space via finite differences)
        grad_R = np.gradient(R_local, self.L/self.grid_size)
        
        # Interpolate forces at particle positions
        forces = np.zeros((self.N, 3))
        
        indices = np.floor(
            (self.positions + self.L/2) / self.L * self.grid_size
        ).astype(int)
        indices = indices % self.grid_size
        
        for i in range(self.N):
            ix, iy, iz = indices[i]
            # F = -m * ∇R_local (approximation for small perturbations)
            forces[i, 0] = -self.masses[i] * grad_R[0][ix, iy, iz]
            forces[i, 1] = -self.masses[i] * grad_R[1][ix, iy, iz]
            forces[i, 2] = -self.masses[i] * grad_R[2][ix, iy, iz]
        
        return forces
    
    def compute_energy(self):
        """Compute total energy (kinetic + potential)."""
        # Kinetic
        KE = 0.5 * np.sum(self.masses[:, np.newaxis] * self.velocities**2)
        
        # Potential (pairwise)
        PE = 0.0
        for i in range(self.N):
            for j in range(i+1, self.N):
                r_ij = np.linalg.norm(self.positions[i] - self.positions[j])
                if r_ij > 0:
                    PE -= self.G * self.masses[i] * self.masses[j] / r_ij
        
        return KE + PE
    
    def step(self, dt):
        """
        Advance system by one timestep using leapfrog integrator.
        """
        # Compute forces
        forces = self.compute_forces()
        
        # Leapfrog (symplectic integrator):
        # v(t+dt/2) = v(t) + a(t) * dt/2
        # x(t+dt) = x(t) + v(t+dt/2) * dt
        # v(t+dt) = v(t+dt/2) + a(t+dt) * dt/2
        
        # Half-step velocity update
        self.velocities += 0.5 * forces / self.masses[:, np.newaxis] * dt
        
        # Full-step position update
        self.positions += self.velocities * dt
        
        # Apply periodic boundary conditions
        self.positions = self.positions % self.L - self.L/2
        
        # Recompute forces at new positions
        forces = self.compute_forces()
        
        # Half-step velocity update
        self.velocities += 0.5 * forces / self.masses[:, np.newaxis] * dt
    
    def simulate(self, T_total, dt):
        """
        Run simulation for total time T_total.
        """
        num_steps = int(T_total / dt)
        
        for step in range(num_steps):
            t = step * dt
            
            # Record state
            if step % 10 == 0:
                self.history['time'].append(t)
                self.history['positions'].append(self.positions.copy())
                self.history['energy'].append(self.compute_energy())
            
            # Advance
            self.step(dt)
            
            if step % 100 == 0:
                E = self.history['energy'][-1]
                print(f"Step {step}/{num_steps}, t={t:.2f}, E={E:.6f}")


# ============================================================================
# Example: Figure-8 Three-Body Orbit
# ============================================================================

def setup_figure_8():
    """
    Initialize famous figure-8 periodic orbit.
    
    Three equal masses chase each other on figure-8 path.
    """
    sim = CymaticNBody(N=3, grid_size=64)
    
    # Equal masses
    masses = [1.0, 1.0, 1.0]
    
    # Initial positions (from Chenciner & Montgomery 2000)
    positions = [
        [-0.97000436, 0.24308753, 0.0],
        [0.0, 0.0, 0.0],
        [0.97000436, -0.24308753, 0.0]
    ]
    
    # Initial velocities
    velocities = [
        [0.466203685, 0.43236573, 0.0],
        [-0.93240737, -0.86473146, 0.0],
        [0.466203685, 0.43236573, 0.0]
    ]
    
    sim.set_initial_conditions(masses, positions, velocities)
    
    return sim


def setup_solar_system_analog():
    """
    Sun + 2 planets (simplified)
    """
    sim = CymaticNBody(N=3, grid_size=64)
    
    # Sun-dominated system
    masses = [100.0, 1.0, 0.5]  # Sun, Jupiter-like, Earth-like
    
    # Circular orbits
    positions = [
        [0.0, 0.0, 0.0],      # Sun at center
        [2.0, 0.0, 0.0],      # Jupiter
        [1.0, 0.0, 0.0]       # Earth
    ]
    
    # Velocities for circular orbits: v = sqrt(GM/r)
    G = 1.0
    M_sun = masses[0]
    
    v_jupiter = np.sqrt(G * M_sun / 2.0)
    v_earth = np.sqrt(G * M_sun / 1.0)
    
    velocities = [
        [0.0, 0.0, 0.0],
        [0.0, v_jupiter, 0.0],
        [0.0, v_earth, 0.0]
    ]
    
    sim.set_initial_conditions(masses, positions, velocities)
    
    return sim


# ============================================================================
# Visualization
# ============================================================================

def plot_orbits(sim):
    """
    Plot orbital trajectories.
    """
    positions = np.array(sim.history['positions'])  # (time, bodies, xyz)
    
    fig = plt.figure(figsize=(12, 5))
    
    # 2D projection (xy plane)
    ax1 = fig.add_subplot(121)
    for i in range(sim.N):
        x = positions[:, i, 0]
        y = positions[:, i, 1]
        ax1.plot(x, y, label=f'Body {i+1}', linewidth=2)
    
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Orbital Trajectories (xy plane)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.axis('equal')
    
    # Energy conservation
    ax2 = fig.add_subplot(122)
    time = sim.history['time']
    energy = sim.history['energy']
    
    # Relative energy error
    E0 = energy[0]
    rel_error = [(E - E0)/abs(E0) for E in energy]
    
    ax2.plot(time, rel_error, linewidth=2)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Relative Energy Error')
    ax2.set_title('Energy Conservation')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cymatic_nbody_orbits.png', dpi=150)
    print("Saved: cymatic_nbody_orbits.png")
    plt.close()


# ============================================================================
# Run Simulation
# ============================================================================

if __name__ == "__main__":
    print("Cymatic N-Body Gravity Simulation")
    print("="*60)
    
    # Choose scenario
    print("\nInitializing Figure-8 three-body orbit...")
    sim = setup_figure_8()
    
    # Simulate
    print("\nRunning simulation...")
    T_total = 20.0  # Total time
    dt = 0.01       # Timestep
    
    sim.simulate(T_total, dt)
    
    # Plot
    print("\nGenerating plots...")
    plot_orbits(sim)
    
    print("\nSimulation complete!")
    print(f"Final energy error: {(sim.history['energy'][-1] - sim.history['energy'][0])/abs(sim.history['energy'][0]):.2e}")
```

---

## Part 11: Key Insights from Cymatic N-Body

### 11.1 What's Different?

**Standard approach**: 
- Bodies = point masses
- Gravity = action-at-a-distance force
- Numerical integration of trajectories

**Cymatic approach**:
- Bodies = spectral solitons
- Gravity = substrate congestion (local field effect)
- Evolution via spectral dynamics

**Advantages**:
1. **Naturally handles close encounters** (no singularities - solitons have finite width)
2. **Collective effects** emerge automatically (mean-field from substrate)
3. **Relativistic corrections** straightforward (velocity-dependent $R_{\text{local}}$)
4. **Connects to other physics** (same substrate describes QM, thermodynamics)

### 11.2 Predictions

**Testable differences**:

1. **Extreme mass ratios**: 
   - Standard: Breakdown when $m_1/m_2 \to 0$ (need special treatment)
   - Cymatic: Smooth (test particle in substrate field)

2. **Dense systems**: 
   - Standard: Collisions problematic
   - Cymatic: Soliton merger/scattering natural

3. **Cosmological scales**:
   - Standard: Dark matter as new particle
   - Cymatic: Non-resonant spectral noise (from framework)

### 11.3 Open Questions

1. **Do solitons deform tidally?**
   - Expected: Yes, but how much?
   - Affects: Binary inspiral waveforms (GW astronomy)

2. **Can solitons merge softly?**
   - Standard: Black hole merger = singularity
   - Cymatic: Smooth spectral reconfiguration?

3. **What about 1000-body?**
   - Numerical cost: $O(N \log N)$ with FFT
   - Accuracy: How well does discrete grid approximate continuous substrate?

---

## Part 12: Summary

**The N-body problem in cymatics**:

**3-body**: 
- Chaos from spectral beating (incommensurate frequencies)
- Stable orbits at high-symmetry resonances
- Phase-locking explains periodic solutions

**N-body**:
- Hierarchical systems stable (dominant soliton + perturbations)
- Collisionless regime = mean-field (Vlasov equation)
- Relaxation = spectral thermalization

**Key formula** (substrate gravity):
$$\mathbf{F}_i = -m_i \nabla \Phi = -m_i c^2 \nabla \ln\left(\frac{R_{\text{local}}}{R_{\text{max}}}\right)$$

where
$$R_{\text{local}}(\mathbf{x}) = R_{\text{max}} - \sum_{j} \frac{\alpha m_j}{|\mathbf{x} - \mathbf{r}_j|}$$

**Advantages**:
- No singularities (solitons have finite size)
- Collective effects natural
- Connects gravity to QM via shared substrate

**Status**: Complete cymatic reformulation of N-body problem. Reproduces Newtonian dynamics in appropriate limit, offers new perspective on chaos, stability, and collective behavior.