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

    