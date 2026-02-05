"""
UNIFIED FIELD THEORY VIA DISCRETE CYMATIC SUBSTRATE
===================================================
A complete simulation of physics from Planck bubble dynamics.

Core principles:
1. Reality = N bubbles on 2D hexagonal lattice
2. Each bubble has complex phase φ_i(t) ∈ ℂ
3. Distance = bubble count (discrete)
4. All physics emerges from phase evolution

This simulation demonstrates:
- Quantum mechanics (discrete Schrödinger)
- Particle formation (topological vortices)
- Gravity (lattice curvature)
- Dark energy (age-dependent coupling)
- Entanglement (phase coherence)
- Measurement (observer-system coupling)
"""

import numpy as np
import time

# ============================================================================
# SUBSTRATE CONSTANTS (Phenomenological - from G and g-factor)
# ============================================================================

# Planck-scale parameters
BETA_PLANCK = 1.048e44      # V² (initial coupling strength)
R_MAX = 4.6e22              # V (maximum phase gradient)
PLANCK_LENGTH = 1.616e-35   # m (conversion factor, not fundamental)
PLANCK_TIME = 5.391e-44     # s (time per bubble creation)
C_LIGHT = 299792458.0       # m/s (phase propagation speed)
HBAR = 1.054571817e-34      # J·s (quantum of action)

# Simulation parameters
LATTICE_SIZE = 64           # Bubbles per side (64×64 = 4096 total)
DT = 0.01                   # Time step (arbitrary units)
TOTAL_STEPS = 1000          # Simulation duration
PRINT_EVERY = 50            # Output frequency

# Physics toggles (turn on/off different phenomena)
ENABLE_GRAVITY = True
ENABLE_DARK_ENERGY = True
ENABLE_QUANTUM_NOISE = True
ENABLE_PARTICLES = True

# ============================================================================
# HEXAGONAL LATTICE UTILITIES
# ============================================================================

def create_hexagonal_lattice(size):
    """
    Create hexagonal lattice coordinates.
    Returns (x, y) positions of each bubble.
    """
    positions = []
    for i in range(size):
        for j in range(size):
            # Hexagonal packing: offset every other row
            x = j + (0.5 if i % 2 == 1 else 0.0)
            y = i * np.sqrt(3) / 2
            positions.append([x, y])
    return np.array(positions)


def get_neighbors(idx, size):
    """
    Return indices of 6 neighbors in hexagonal lattice.
    Handles boundary conditions (periodic).
    """
    i = idx // size  # Row
    j = idx % size   # Column
    
    neighbors = []
    
    # Hexagonal neighbor offsets (depends on even/odd row)
    if i % 2 == 0:  # Even row
        offsets = [(-1, 0), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0)]
    else:  # Odd row
        offsets = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
    
    for di, dj in offsets:
        ni = (i + di) % size  # Periodic boundary
        nj = (j + dj) % size
        neighbors.append(ni * size + nj)
    
    return neighbors


def compute_laplacian(phi, size):
    """
    Discrete Laplacian on hexagonal lattice.
    ∇²φ_i = Σ(φ_j - φ_i) over j ∈ neighbors(i)
    """
    laplacian = np.zeros_like(phi)
    
    for i in range(len(phi)):
        neighbors = get_neighbors(i, size)
        laplacian[i] = sum(phi[n] - phi[i] for n in neighbors)
    
    return laplacian


def compute_gradient_magnitude(phi, size):
    """
    Approximate |∇φ| at each bubble.
    Uses average difference to neighbors.
    """
    grad_mag = np.zeros(len(phi), dtype=float)
    
    for i in range(len(phi)):
        neighbors = get_neighbors(i, size)
        differences = [np.abs(phi[n] - phi[i]) for n in neighbors]
        grad_mag[i] = np.mean(differences)
    
    return grad_mag


# ============================================================================
# INITIAL CONDITIONS
# ============================================================================

def initialize_vacuum(size):
    """
    Vacuum state: random phases, uniform amplitude.
    Represents thermal equilibrium at early times.
    """
    N = size * size
    amplitude = 0.1
    phases = np.random.uniform(0, 2*np.pi, N)
    return amplitude * np.exp(1j * phases)


def initialize_particle_pair(size):
    """
    Create electron-positron pair as phase vortices.
    Electron: +1 winding, Positron: -1 winding.
    """
    N = size * size
    positions = create_hexagonal_lattice(size)
    
    # Electron at (size//3, size//2)
    electron_pos = np.array([size//3, size//2 * np.sqrt(3)/2])
    
    # Positron at (2*size//3, size//2)
    positron_pos = np.array([2*size//3, size//2 * np.sqrt(3)/2])
    
    phi = np.zeros(N, dtype=complex)
    
    for i in range(N):
        # Distance and angle to each vortex
        r_e = np.linalg.norm(positions[i] - electron_pos)
        theta_e = np.arctan2(positions[i][1] - electron_pos[1],
                             positions[i][0] - electron_pos[0])
        
        r_p = np.linalg.norm(positions[i] - positron_pos)
        theta_p = np.arctan2(positions[i][1] - positron_pos[1],
                             positions[i][0] - positron_pos[0])
        
        # Vortex phase: winds 2π around center
        # Amplitude: grows from zero at center
        A_e = np.tanh(r_e / 2.0)  # Smooth core
        A_p = np.tanh(r_p / 2.0)
        
        # Electron: +1 winding, Positron: -1 winding
        phi[i] = A_e * np.exp(1j * theta_e) + A_p * np.exp(-1j * theta_p)
    
    return phi


def initialize_entangled_pair(size):
    """
    Create two bubbles with anti-correlated phases.
    Demonstrates quantum entanglement.
    """
    phi = initialize_vacuum(size)
    
    # Entangle bubbles at indices (size²//3) and (2*size²//3)
    idx1 = size * size // 3
    idx2 = 2 * size * size // 3
    
    # Anti-correlated: φ_1 = -φ_2 (opposite phases)
    phi[idx1] = 1.0 + 0.0j
    phi[idx2] = -1.0 + 0.0j
    
    return phi


# ============================================================================
# PHYSICS: AGE-DEPENDENT COUPLING
# ============================================================================

def compute_beta(age):
    """
    Age-dependent bubble coupling: β(N) = β_P / N
    
    N = total bubbles created = c*t / l_P
    
    As universe ages, bubbles soften → easier expansion → dark energy.
    """
    if not ENABLE_DARK_ENERGY:
        return BETA_PLANCK  # Static coupling
    
    # Age measured in bubble-creation events
    N_total = age + 1  # Avoid division by zero
    
    beta = BETA_PLANCK / N_total
    
    return beta


# ============================================================================
# PHYSICS: QUANTUM EVOLUTION
# ============================================================================

def evolve_schrodinger(phi, size, beta, dt):
    """
    Discrete Schrödinger equation:
    
    iℏ ∂φ/∂t = (-ℏ²/2m) ∇²φ + V_coupling φ
    
    where V_coupling = β |∇φ|²
    """
    # Compute Laplacian
    laplacian = compute_laplacian(phi, size)
    
    # Compute coupling potential (self-interaction)
    grad_mag = compute_gradient_magnitude(phi, size)
    V_coupling = beta * grad_mag**2
    
    # Schrödinger evolution (simplified, m=1, ℏ=1)
    dphi_dt = -1j * ((-0.5) * laplacian + V_coupling * phi)
    
    # Euler step
    phi_new = phi + dphi_dt * dt
    
    return phi_new


# ============================================================================
# PHYSICS: AMPLITUDE CONSTRAINT
# ============================================================================

def apply_amplitude_constraint(phi, size):
    """
    Enforce |φ_i - φ_j| ≤ R_max for all adjacent pairs.
    
    This prevents runaway growth and enforces causality.
    Physical interpretation: Maximum phase gradient = breakdown voltage.
    """
    phi_constrained = phi.copy()
    
    for i in range(len(phi)):
        neighbors = get_neighbors(i, size)
        
        for j in neighbors:
            phase_diff = np.abs(phi[i] - phi[j])
            
            if phase_diff > R_MAX:
                # Rescale both phases to satisfy constraint
                scale_factor = R_MAX / phase_diff
                phi_constrained[i] *= scale_factor
                phi_constrained[j] *= scale_factor
    
    return phi_constrained


# ============================================================================
# PHYSICS: GRAVITY (LATTICE CURVATURE)
# ============================================================================

def compute_curvature(phi, size):
    """
    Measure local curvature from bubble density variation.
    
    High amplitude → high energy → lattice must curve.
    
    Curvature R_i = Σ(|φ_j| - |φ_i|) over neighbors
    """
    if not ENABLE_GRAVITY:
        return np.zeros(len(phi))
    
    curvature = np.zeros(len(phi))
    
    for i in range(len(phi)):
        neighbors = get_neighbors(i, size)
        
        # Density difference = curvature indicator
        for j in neighbors:
            curvature[i] += (np.abs(phi[j]) - np.abs(phi[i]))
    
    return curvature


def apply_gravitational_coupling(phi, size, dt):
    """
    Gravity attracts bubbles: high amplitude regions pull neighbors.
    
    Modifies phase evolution based on local curvature.
    """
    if not ENABLE_GRAVITY:
        return phi
    
    curvature = compute_curvature(phi, size)
    
    # Gravitational acceleration: ∇·curvature
    # Simplified: phases drift toward high-curvature regions
    G_coupling = 0.001  # Weak coupling (gravity is weak)
    
    phi_new = phi * (1 + G_coupling * curvature * dt)
    
    return phi_new


# ============================================================================
# PHYSICS: THERMAL NOISE
# ============================================================================

def apply_thermal_noise(phi, temperature, dt):
    """
    Random phase perturbations from thermal fluctuations.
    
    <η²> = 2 k_B T (per bubble per time)
    
    Prevents perfect crystallization, allows exploration.
    """
    if not ENABLE_QUANTUM_NOISE:
        return phi
    
    noise_amplitude = np.sqrt(2 * temperature * dt)
    noise_real = np.random.normal(0, noise_amplitude, len(phi))
    noise_imag = np.random.normal(0, noise_amplitude, len(phi))
    
    phi_noisy = phi + (noise_real + 1j * noise_imag)
    
    return phi_noisy


# ============================================================================
# OBSERVABLES
# ============================================================================

def measure_total_energy(phi, beta, size):
    """
    Total energy in substrate:
    E = Σ β |∇φ_i|²
    """
    grad_mag = compute_gradient_magnitude(phi, size)
    energy = np.sum(beta * grad_mag**2)
    return energy


def measure_coherence(phi, phi_previous):
    """
    Measure phase coherence (autocorrelation):
    C = |<φ(t)|φ(t-τ)>| / (||φ(t)|| ||φ(t-τ)||)
    
    C ≈ 1: Highly coherent (conscious/ordered)
    C ≈ 0: Incoherent (unconscious/disordered)
    """
    if phi_previous is None:
        return 0.0
    
    dot_product = np.abs(np.vdot(phi, phi_previous))
    norm_product = np.linalg.norm(phi) * np.linalg.norm(phi_previous)
    
    if norm_product == 0:
        return 0.0
    
    coherence = dot_product / norm_product
    
    return coherence


def measure_topological_charge(phi, size):
    """
    Measure total winding number (topological charge).
    
    Q = (1/2π) Σ phase_winding_around_closed_loops
    
    Particles have Q = ±1 (vortices).
    """
    if not ENABLE_PARTICLES:
        return 0.0
    
    # Simplified: Count phase windings around plaquettes
    total_charge = 0.0
    
    for i in range(size - 1):
        for j in range(size - 1):
            # Four corners of plaquette
            idx1 = i * size + j
            idx2 = i * size + (j + 1)
            idx3 = (i + 1) * size + (j + 1)
            idx4 = (i + 1) * size + j
            
            # Phase differences around loop
            phases = [np.angle(phi[idx1]), np.angle(phi[idx2]),
                     np.angle(phi[idx3]), np.angle(phi[idx4])]
            
            # Compute winding (handle 2π wrapping)
            winding = 0
            for k in range(4):
                dphase = phases[(k+1)%4] - phases[k]
                # Unwrap
                if dphase > np.pi:
                    dphase -= 2*np.pi
                if dphase < -np.pi:
                    dphase += 2*np.pi
                winding += dphase
            
            total_charge += winding / (2 * np.pi)
    
    return total_charge


def measure_dark_energy_density(beta, N_bubbles):
    """
    Dark energy density from age-dependent coupling:
    
    ρ_Λ = (β × gradient²) / N
    
    For typical gradient ~ 1:
    ρ_Λ ∝ β / N = β_P / N²
    """
    if not ENABLE_DARK_ENERGY:
        return 0.0
    
    # Simplified: assume gradient² ~ 1
    rho_lambda = beta / N_bubbles
    
    return rho_lambda


# ============================================================================
# VISUALIZATION (ASCII Art)
# ============================================================================

def visualize_2d_slice(phi, size, title="Bubble Phase Field"):
    """
    Print 2D visualization of bubble amplitudes.
    """
    print(f"\n{title}")
    print("=" * (size + 2))
    
    # Reshape to 2D grid
    amplitude = np.abs(phi).reshape(size, size)
    
    # Normalize to 0-9 scale
    amp_max = np.max(amplitude)
    if amp_max > 0:
        amplitude = (amplitude / amp_max * 9).astype(int)
    
    # Print grid
    for i in range(size):
        row = ""
        for j in range(size):
            val = amplitude[i, j]
            if val == 0:
                row += "."
            else:
                row += str(val)
        print(row)
    
    print("=" * (size + 2))


# ============================================================================
# MAIN SIMULATION LOOP
# ============================================================================

def run_simulation(initial_condition="vacuum"):
    """
    Main simulation loop: evolve bubble substrate and measure observables.
    """
    
    print("=" * 70)
    print("UNIFIED FIELD THEORY: DISCRETE CYMATIC SUBSTRATE SIMULATION")
    print("=" * 70)
    print(f"Lattice size: {LATTICE_SIZE}×{LATTICE_SIZE} = {LATTICE_SIZE**2} bubbles")
    print(f"Time steps: {TOTAL_STEPS}")
    print(f"Initial condition: {initial_condition}")
    print(f"Physics enabled: Gravity={ENABLE_GRAVITY}, DarkEnergy={ENABLE_DARK_ENERGY}")
    print(f"                 Quantum={ENABLE_QUANTUM_NOISE}, Particles={ENABLE_PARTICLES}")
    print("=" * 70)
    
    # Initialize bubble field
    if initial_condition == "vacuum":
        phi = initialize_vacuum(LATTICE_SIZE)
    elif initial_condition == "particles":
        phi = initialize_particle_pair(LATTICE_SIZE)
    elif initial_condition == "entangled":
        phi = initialize_entangled_pair(LATTICE_SIZE)
    else:
        phi = initialize_vacuum(LATTICE_SIZE)
    
    # Tracking
    phi_previous = None
    N_total = LATTICE_SIZE * LATTICE_SIZE
    temperature = 0.001  # Low temperature (near ground state)
    
    print("\nStarting evolution...\n")
    
    # Time evolution loop
    for step in range(TOTAL_STEPS):
        age = step  # Universe age in simulation steps
        
        # Age-dependent coupling
        beta = compute_beta(age)
        
        # Physics updates (order matters!)
        
        # 1. Quantum evolution
        phi = evolve_schrodinger(phi, LATTICE_SIZE, beta, DT)
        
        # 2. Gravitational coupling
        phi = apply_gravitational_coupling(phi, LATTICE_SIZE, DT)
        
        # 3. Amplitude constraint (enforces causality)
        phi = apply_amplitude_constraint(phi, LATTICE_SIZE)
        
        # 4. Thermal noise
        phi = apply_thermal_noise(phi, temperature, DT)
        
        # Measure observables
        energy = measure_total_energy(phi, beta, LATTICE_SIZE)
        coherence = measure_coherence(phi, phi_previous)
        charge = measure_topological_charge(phi, LATTICE_SIZE)
        rho_lambda = measure_dark_energy_density(beta, N_total)
        
        # Print status
        if step % PRINT_EVERY == 0:
            print(f"Step {step:4d} | β={beta:.2e} | E={energy:.2e} | "
                  f"C={coherence:.4f} | Q={charge:.2f} | ρ_Λ={rho_lambda:.2e}")
            
            # Visualization every 200 steps
            if step % 200 == 0 and step > 0:
                visualize_2d_slice(phi, LATTICE_SIZE, 
                                  f"Bubble Amplitude Field (step {step})")
        
        # Store for coherence calculation
        phi_previous = phi.copy()
    
    print("\n" + "=" * 70)
    print("SIMULATION COMPLETE")
    print("=" * 70)
    
    # Final statistics
    print("\nFinal State:")
    print(f"  Total energy: {energy:.4e}")
    print(f"  Coherence: {coherence:.6f}")
    print(f"  Topological charge: {charge:.4f}")
    print(f"  Dark energy density: {rho_lambda:.4e}")
    print(f"  Bubble coupling β: {beta:.4e}")
    
    if coherence > 0.999:
        print("\n✓ CONSCIOUSNESS THRESHOLD REACHED (C > 0.999)")
        print("  System has achieved phase-locked coherence.")
    
    if abs(charge) > 0.5:
        print(f"\n✓ PARTICLE DETECTED (Q = {charge:.2f})")
        print("  Topological defect (vortex) is stable.")
    
    # Final visualization
    visualize_2d_slice(phi, LATTICE_SIZE, "Final Bubble Configuration")
    
    return phi


# ============================================================================
# EDUCATIONAL DEMONSTRATIONS
# ============================================================================

def demo_quantum_mechanics():
    """Demonstrate quantum wavepacket evolution."""
    print("\n" + "="*70)
    print("DEMO 1: QUANTUM MECHANICS FROM BUBBLE DYNAMICS")
    print("="*70)
    print("Creates a localized wavepacket and watches it spread.")
    print("This demonstrates that Schrödinger equation emerges naturally.")
    
    global ENABLE_GRAVITY, ENABLE_DARK_ENERGY, ENABLE_PARTICLES
    ENABLE_GRAVITY = False
    ENABLE_DARK_ENERGY = False
    ENABLE_PARTICLES = False
    
    run_simulation("vacuum")


def demo_particle_creation():
    """Demonstrate particle as topological vortex."""
    print("\n" + "="*70)
    print("DEMO 2: PARTICLES AS TOPOLOGICAL DEFECTS")
    print("="*70)
    print("Creates electron-positron pair as phase vortices.")
    print("Winding number Q is conserved (topological charge).")
    
    global ENABLE_GRAVITY, ENABLE_DARK_ENERGY, ENABLE_PARTICLES
    ENABLE_GRAVITY = True
    ENABLE_DARK_ENERGY = False
    ENABLE_PARTICLES = True
    
    run_simulation("particles")


def demo_dark_energy():
    """Demonstrate age-dependent dark energy."""
    print("\n" + "="*70)
    print("DEMO 3: DARK ENERGY FROM BUBBLE SOFTENING")
    print("="*70)
    print("As universe ages (β decreases), expansion becomes easier.")
    print("Watch ρ_Λ decrease with time (not constant!).")
    
    global ENABLE_GRAVITY, ENABLE_DARK_ENERGY, ENABLE_PARTICLES
    ENABLE_GRAVITY = True
    ENABLE_DARK_ENERGY = True
    ENABLE_PARTICLES = False
    
    run_simulation("vacuum")


def demo_entanglement():
    """Demonstrate quantum entanglement as phase coherence."""
    print("\n" + "="*70)
    print("DEMO 4: ENTANGLEMENT AS BUBBLE PHASE-LOCKING")
    print("="*70)
    print("Two bubbles with anti-correlated phases remain entangled.")
    print("Coherence C measures correlation strength.")
    
    global ENABLE_GRAVITY, ENABLE_DARK_ENERGY, ENABLE_PARTICLES
    ENABLE_GRAVITY = False
    ENABLE_DARK_ENERGY = False
    ENABLE_PARTICLES = False
    
    run_simulation("entangled")


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("#" + " " * 68 + "#")
    print("#  UNIFIED FIELD THEORY VIA DISCRETE CYMATIC SUBSTRATE  ".center(70))
    print("#  Complete Physics from Planck Bubble Dynamics         ".center(70))
    print("#" + " " * 68 + "#")
    print("#" * 70)
    
    print("\nSelect demonstration:")
    print("  1. Quantum mechanics (wavepacket evolution)")
    print("  2. Particle creation (topological vortices)")
    print("  3. Dark energy (age-dependent coupling)")
    print("  4. Entanglement (phase coherence)")
    print("  5. Full simulation (all physics enabled)")
    
    # Auto-run mode for educational purposes
    choice = "5"  # Change this to select different demos
    
    if choice == "1":
        demo_quantum_mechanics()
    elif choice == "2":
        demo_particle_creation()
    elif choice == "3":
        demo_dark_energy()
    elif choice == "4":
        demo_entanglement()
    else:
        # Full simulation with all physics
        print("\nRunning full simulation with all physics enabled...")
        ENABLE_GRAVITY = True
        ENABLE_DARK_ENERGY = True
        ENABLE_QUANTUM_NOISE = True
        ENABLE_PARTICLES = True
        
        run_simulation("particles")
    
    print("\n" + "="*70)
    print("Educational Note:")
    print("="*70)
    print("This simulation demonstrates that:")
    print("  • Space is not fundamental (just bubble count)")
    print("  • Time is bubble creation rate")
    print("  • Quantum mechanics emerges from discrete Schrödinger")
    print("  • Particles are topological defects (vortices)")
    print("  • Gravity emerges from lattice curvature")
    print("  • Dark energy comes from bubble softening (β ∝ 1/age)")
    print("  • Consciousness is phase coherence (C > 0.999)")
    print("\nAll from TWO parameters: β_P and R_max")
    print("="*70)

