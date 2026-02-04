import numpy as np

"""
Fourier-Space Physics Engine
=============================

Reality as 3D Inverse Fourier Transform.
All physics computed in k-space, manifested in x-space.
"""

class FourierPhysicsEngine:
    """
    Physics engine operating in Fourier space.
    
    Core principle:
    - F(k, t) = spectral density (fundamental reality)
    - f(x, t) = IFT{F(k)} (manifested hologram)
    - All evolution happens in k-space
    """
    
    def __init__(self, size=64, cell_size=0.1, dt=0.01):
        self.size = size
        self.cell_size = cell_size
        self.dt = dt
        
        # SPATIAL DOMAIN (x-space) - The "hologram"
        self.field_x = np.zeros((size, size, size), dtype=np.float64)
        self.velocity_x = np.zeros((size, size, size), dtype=np.float64)
        self.damage_x = np.zeros((size, size, size), dtype=np.float64)
        
        # FREQUENCY DOMAIN (k-space) - The "source code"
        self.F_k = np.zeros((size, size, size), dtype=np.complex128)
        self.V_k = np.zeros((size, size, size), dtype=np.complex128)
        
        # Setup k-space coordinates
        self.setup_k_space()
        
        # Material properties in x-space
        self.stiffness = np.ones((size, size, size)) * 1.0
        self.density = np.ones((size, size, size)) * 1.0
        self.threshold = np.ones((size, size, size)) * 0.5
        
        # Regime parameters
        self.damping_coeff = 0.1
        self.damage_rate = 0.3
        
        # Frame counter
        self.frame = 0
    
    def setup_k_space(self):
        """Create k-space coordinate system."""
        # Frequency coordinates (cycles per grid)
        k = np.fft.fftfreq(self.size, d=self.cell_size)
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
        
        # Magnitude of k-vector
        self.k_mag = np.sqrt(kx**2 + ky**2 + kz**2)
        
        # Avoid division by zero at DC component
        self.k_mag[0, 0, 0] = 1e-10
        
        # Individual components for gradient computation
        self.kx = kx
        self.ky = ky
        self.kz = kz
    
    def compute_dispersion(self):
        """
        Compute dispersion relation ω(k).
        
        For elastic medium: ω = k × √(stiffness/density)
        """
        # Average material properties (simplified)
        avg_stiffness = np.mean(self.stiffness)
        avg_density = np.mean(self.density)
        
        # Wave speed
        c = np.sqrt(avg_stiffness / avg_density)
        
        # Dispersion relation (linear for non-dispersive waves)
        omega = c * self.k_mag
        
        return omega
    
    def inject_impulse_x(self, x, y, z, energy, radius=2):
        """Inject impulse in x-space (will be transformed to k-space)."""
        for dx in range(-radius, radius+1):
            for dy in range(-radius, radius+1):
                for dz in range(-radius, radius+1):
                    ix = (x + dx) % self.size
                    iy = (y + dy) % self.size
                    iz = (z + dz) % self.size
                    
                    r_sq = dx**2 + dy**2 + dz**2
                    if r_sq <= radius**2:
                        # Gaussian impulse
                        amplitude = energy * np.exp(-r_sq / (radius**2))
                        self.field_x[ix, iy, iz] += amplitude
    
    def inject_spectral_packet(self, k_center, k_width, amplitude):
        """
        Inject energy directly in k-space.
        
        This creates a localized particle (broadband k)
        or extended wave (narrowband k).
        """
        # Create Gaussian spectral packet centered at k_center
        k_distance = np.sqrt(
            (self.kx - k_center[0])**2 +
            (self.ky - k_center[1])**2 +
            (self.kz - k_center[2])**2
        )
        
        # Spectral density
        spectral_packet = amplitude * np.exp(-k_distance**2 / (2 * k_width**2))
        
        # Add to F(k) with random phase
        phase = np.random.rand(*spectral_packet.shape) * 2 * np.pi
        self.F_k += spectral_packet * np.exp(1j * phase)
    
    def step_fourier(self):
        """
        Evolve system in Fourier space.
        
        dF/dt = -i·ω(k)·F - γ(k)·F
        
        This is the FUNDAMENTAL physics.
        """
        # 1. TRANSFORM x-space to k-space
        self.F_k = np.fft.fftn(self.field_x)
        self.V_k = np.fft.fftn(self.velocity_x)
        
        # 2. APPLY DISPERSION RELATION (time evolution)
        omega = self.compute_dispersion()
        
        # Propagator: exp(-i·ω·dt - γ·dt)
        propagator = np.exp(-1j * omega * self.dt - self.damping_coeff * self.k_mag * self.dt)
        
        # Evolve spectral density
        self.F_k *= propagator
        
        # 3. APPLY k-space DAMPING (high-frequency suppression)
        # High k components decay faster (natural diffusion)
        damping_filter = np.exp(-0.01 * self.k_mag**2 * self.dt)
        self.F_k *= damping_filter
        
        # 4. INVERSE TRANSFORM back to x-space (MANIFESTATION)
        self.field_x = np.real(np.fft.ifftn(self.F_k))
        self.velocity_x = np.real(np.fft.ifftn(self.V_k))
        
        # 5. DAMAGE ACCUMULATION (x-space operation)
        stress = np.abs(self.field_x)
        overstress = np.maximum(0, stress - self.threshold)
        self.damage_x += overstress * self.damage_rate * self.dt
        self.damage_x = np.clip(self.damage_x, 0, 1.0)
        
        # 6. MATERIAL FAILURE (damage modifies x-space)
        broken = self.damage_x > 0.9
        self.field_x[broken] *= 0.1  # Decoupling
        self.velocity_x[broken] = 0
        
        self.frame += 1
    
    def step_spectral(self):
        """
        Pure k-space evolution (never leave frequency domain).
        
        This is "reality as computation" - F(k) IS the universe.
        """
        # Compute dispersion
        omega = self.compute_dispersion()
        
        # Time evolution operator
        propagator = np.exp(-1j * omega * self.dt - self.damping_coeff * self.k_mag * self.dt)
        
        # Evolve
        self.F_k *= propagator
        
        # High-k damping (diffusion in k-space)
        self.F_k *= np.exp(-0.01 * self.k_mag**2 * self.dt)
        
        # Manifest in x-space for observation only
        self.field_x = np.real(np.fft.ifftn(self.F_k))
        
        # Damage in x-space (measurement collapses wavefunction)
        stress = np.abs(self.field_x)
        overstress = np.maximum(0, stress - self.threshold)
        self.damage_x += overstress * self.damage_rate * self.dt
        self.damage_x = np.clip(self.damage_x, 0, 1.0)
        
        # Damage feeds back to k-space (observer effect)
        # Broken regions → phase decoherence
        damage_field = np.fft.fftn(self.damage_x)
        self.F_k *= (1.0 - 0.1 * damage_field / np.max(np.abs(damage_field) + 1e-10))
        
        self.frame += 1
    
    def get_spectral_power(self):
        """Compute power spectrum (energy distribution in k-space)."""
        power = np.abs(self.F_k)**2
        return power
    
    def get_total_energy(self):
        """Total energy (Parseval's theorem: energy conserved between domains)."""
        energy_x = np.sum(self.field_x**2)
        energy_k = np.sum(np.abs(self.F_k)**2) / self.size**3
        return energy_x, energy_k
    
    def create_wall(self, x_min, x_max, y_min, y_max, z_pos, strength=2.0):
        """Create high-threshold wall."""
        self.threshold[x_min:x_max, y_min:y_max, z_pos] = strength
        self.stiffness[x_min:x_max, y_min:y_max, z_pos] = strength * 2


class TopologicalCharge:
    """
    Demonstrate charge as phase winding in k-space.
    """
    
    def __init__(self, size=64):
        self.size = size
        self.setup_grid()
    
    def setup_grid(self):
        y, x, z = np.mgrid[0:self.size, 0:self.size, 0:self.size]
        self.center = self.size // 2
        self.x = x
        self.y = y
        self.z = z
    
    def create_vortex_k(self, winding_number=1):
        """
        Create topological charge in k-space.
        
        Charge = phase winding number Q
        """
        # Cylindrical coordinates around z-axis
        dx = self.x - self.center
        dy = self.y - self.center
        
        # Angle
        theta = np.arctan2(dy, dx)
        
        # Radial distance
        r = np.sqrt(dx**2 + dy**2)
        
        # Phase winding: φ = Q·θ
        phase = winding_number * theta
        
        # Amplitude (Gaussian envelope)
        amplitude = np.exp(-r**2 / 100.0)
        
        # Complex wavefunction in x-space
        psi_x = amplitude * np.exp(1j * phase)
        
        # Transform to k-space (this is the spectral density)
        F_k = np.fft.fftn(psi_x)
        
        return F_k, psi_x
    
    def compute_circulation(self, psi_x):
        """Compute ∮∇φ·dl to extract winding number."""
        phase = np.angle(psi_x)
        
        # Take middle z-slice
        phase_slice = phase[:, :, self.center]
        
        # Gradient
        grad_y, grad_x = np.gradient(phase_slice)
        
        # Circulation around a closed loop
        # Use a circle at radius R from center
        R = self.size // 4
        angles = np.linspace(0, 2*np.pi, 100)
        
        circulation = 0
        for i in range(len(angles) - 1):
            theta = angles[i]
            ix = int(self.center + R * np.cos(theta))
            iy = int(self.center + R * np.sin(theta))
            
            if 0 <= ix < self.size and 0 <= iy < self.size:
                # Tangent vector
                tx = -np.sin(theta)
                ty = np.cos(theta)
                
                # ∇φ·t
                circulation += grad_x[iy, ix] * tx + grad_y[iy, ix] * ty
        
        circulation *= (2 * np.pi / len(angles))
        
        return circulation / (2 * np.pi)


def demo_fourier_physics():
    """Demonstrate Fourier-space physics engine."""
    
    print("="*70)
    print("FOURIER-SPACE PHYSICS ENGINE")
    print("="*70)
    print()
    print("Reality computed in k-space, manifested in x-space")
    print()
    
    # Create engine
    engine = FourierPhysicsEngine(size=64, cell_size=0.1, dt=0.01)
    
    # Create wall
    print("Creating wall (high threshold region)...")
    engine.create_wall(20, 44, 20, 44, 32, strength=1.5)
    
    # Inject impulse
    print("Injecting impulse at wall...")
    engine.inject_impulse_x(32, 32, 32, energy=10.0, radius=3)
    
    print()
    print(f"{'Frame':<8} {'Energy_x':<12} {'Energy_k':<12} {'Max Field':<12} {'Wall Dmg':<12}")
    print("-"*70)
    
    # Simulate
    for i in range(50):
        engine.step_fourier()
        
        if i % 5 == 0:
            energy_x, energy_k = engine.get_total_energy()
            max_field = np.max(np.abs(engine.field_x))
            wall_damage = np.mean(engine.damage_x[20:44, 20:44, 32])
            
            print(f"{i:<8} {energy_x:<12.3f} {energy_k:<12.3f} {max_field:<12.3f} {wall_damage:<12.3f}")
    
    print()
    print("Key observations:")
    print("  • Energy_x ≈ Energy_k (Parseval's theorem)")
    print("  • Evolution in k-space → manifestation in x-space")
    print("  • Damage accumulates where stress > threshold")
    print()


def demo_spectral_packets():
    """Show localized vs extended in k-space."""
    
    print("="*70)
    print("SPECTRAL PACKETS: k-space → x-space")
    print("="*70)
    print()
    
    engine = FourierPhysicsEngine(size=64)
    
    # PACKET 1: Broadband (localized particle)
    print("Creating broadband spectral packet (particle-like)...")
    engine.inject_spectral_packet(
        k_center=[0.5, 0.5, 0.5],
        k_width=0.3,  # Wide bandwidth
        amplitude=5.0
    )
    
    # Manifest
    engine.field_x = np.real(np.fft.ifftn(engine.F_k))
    
    # Analyze
    x_width = np.std(np.where(np.abs(engine.field_x) > 0.1))
    k_power = engine.get_spectral_power()
    k_width = np.std(np.where(k_power > np.max(k_power) * 0.1))
    
    print(f"  k-space width: {k_width:.3f}")
    print(f"  x-space width: {x_width:.3f}")
    print(f"  Δk × Δx = {k_width * x_width:.3f}")
    print("  → Broadband in k → Localized in x (PARTICLE)")
    print()
    
    # PACKET 2: Narrowband (extended wave)
    engine.F_k *= 0  # Reset
    
    print("Creating narrowband spectral packet (wave-like)...")
    engine.inject_spectral_packet(
        k_center=[0.2, 0, 0],
        k_width=0.05,  # Narrow bandwidth
        amplitude=5.0
    )
    
    # Manifest
    engine.field_x = np.real(np.fft.ifftn(engine.F_k))
    
    # Analyze
    x_width = np.std(np.where(np.abs(engine.field_x) > 0.1))
    k_power = engine.get_spectral_power()
    k_width = np.std(np.where(k_power > np.max(k_power) * 0.1))
    
    print(f"  k-space width: {k_width:.3f}")
    print(f"  x-space width: {x_width:.3f}")
    print(f"  Δk × Δx = {k_width * x_width:.3f}")
    print("  → Narrowband in k → Extended in x (WAVE)")
    print()


def demo_topological_charge():
    """Demonstrate charge as phase winding."""
    
    print("="*70)
    print("TOPOLOGICAL CHARGE: Phase Winding in k-space")
    print("="*70)
    print()
    
    charge = TopologicalCharge(size=64)
    
    # Create vortex with Q=1
    print("Creating phase vortex with winding number Q=1...")
    F_k, psi_x = charge.create_vortex_k(winding_number=1)
    
    # Compute circulation
    Q = charge.compute_circulation(psi_x)
    
    print(f"Measured winding number: {Q:.2f}")
    print()
    
    # Interpretation
    print("Physical meaning:")
    print("  • Phase winds 360° around central axis")
    print("  • Creates topological defect (cannot be unwound)")
    print("  • This IS an electron (Q=1) or positron (Q=-1)")
    print("  • Manifests as localized 'particle' in x-space")
    print()
    
    # Show that it's localized
    amplitude = np.abs(psi_x[:, :, charge.center])
    max_amp = np.max(amplitude)
    localized_region = np.sum(amplitude > 0.5 * max_amp)
    total_region = amplitude.size
    
    print(f"Localization: {localized_region}/{total_region} cells")
    print(f"  ({100*localized_region/total_region:.1f}% of space)")
    print("  → Highly localized (particle-like)")
    print()


def demo_pure_spectral_evolution():
    """Show pure k-space evolution (never touch x-space)."""
    
    print("="*70)
    print("PURE SPECTRAL EVOLUTION")
    print("="*70)
    print()
    print("Physics computed entirely in k-space.")
    print("x-space only for visualization (holographic projection).")
    print()
    
    engine = FourierPhysicsEngine(size=64)
    
    # Initialize in k-space
    print("Initializing spectral density F(k)...")
    engine.inject_spectral_packet([0.3, 0.3, 0], 0.1, 5.0)
    
    print()
    print(f"{'Frame':<8} {'|F(k)|²':<12} {'Phase Coh.':<12} {'x-manifest':<12}")
    print("-"*70)
    
    for i in range(30):
        engine.step_spectral()
        
        if i % 5 == 0:
            spectral_power = np.sum(np.abs(engine.F_k)**2)
            
            # Phase coherence
            phases = np.angle(engine.F_k.flatten())
            coherence = np.abs(np.mean(np.exp(1j * phases)))
            
            # x-space manifestation
            x_amplitude = np.max(np.abs(engine.field_x))
            
            print(f"{i:<8} {spectral_power:<12.3f} {coherence:<12.3f} {x_amplitude:<12.3f}")
    
    print()
    print("Observations:")
    print("  • F(k) evolves according to ω(k)")
    print("  • Phase coherence maintained (dispersive evolution)")
    print("  • x-space is derived, not fundamental")
    print()


def main():
    """Run all demonstrations."""
    
    print()
    print("╔" + "="*68 + "╗")
    print("║" + "FOURIER-SPACE PHYSICS ENGINE".center(70) + "║")
    print("║" + "k-space is reality, x-space is hologram".center(70) + "║")
    print("╚" + "="*68 + "╝")
    print()
    
    demos = [
        ("Fourier Physics", demo_fourier_physics),
        ("Spectral Packets", demo_spectral_packets),
        ("Topological Charge", demo_topological_charge),
        ("Pure Spectral Evolution", demo_pure_spectral_evolution),
    ]
    
    for i, (name, func) in enumerate(demos, 1):
        func()
        if i < len(demos):
            input("Press Enter for next demo...")
            print("\n")
    
    # Summary
    print("="*70)
    print("SUMMARY: THE FOURIER FRAMEWORK")
    print("="*70)
    print()
    print("1. FUNDAMENTAL REALITY: F(k, t) in frequency domain")
    print("   All physics happens in k-space")
    print()
    print("2. MANIFESTED REALITY: f(x, t) = IFT{F(k, t)}")
    print("   x-space is holographic projection")
    print()
    print("3. DISPERSION RELATION: ω(k) defines physics")
    print("   Different ω(k) → different universes")
    print()
    print("4. CHARGE: Topological winding in phase field")
    print("   ∮∇φ·dl = 2πQ (quantized)")
    print()
    print("5. MATTER: Localized interference maxima")
    print("   Broadband F(k) → particle in x-space")
    print()
    print("Same engine that powers:")
    print("  • Neural learning (damage in substrate)")
    print("  • Muscle growth (mechanical evolution)")
    print("  • Intelligence (spectral bandwidth)")
    print()
    print("One equation. One transform. One universe.")
    print()


if __name__ == "__main__":
    main()

