"""
Full-Range Human Mobility and Motility Simulation
Cymatic Physics Engine - Educational Image Output

Shows all movement types through static visualizations:
- Cellular motility (subcellular transport)
- Internal organs (heart, lungs, digestion)
- Posture and balance
- Locomotion (walking, running, jumping)
- Athletic movements

Pure substrate mechanics - wave propagation in elastic medium.
Outputs PNG images and animated GIF.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch
import matplotlib.patches as mpatches

# ============================================================================
# CYMATIC PHYSICS ENGINE
# ============================================================================

class CymaticSubstrate:
    """
    Core physics engine: Wave equation in elastic substrate.
    
    ∂²u/∂t² = c²∇²u - γ∂u/∂t + F(x,t)
    """
    
    def __init__(self, size=100, wave_speed=1.0, damping=0.1):
        """
        Args:
            size: Grid size (size × size)
            wave_speed: m/s (tissue wave speed)
            damping: Energy dissipation coefficient
        """
        self.size = size
        self.c = wave_speed
        self.gamma = damping
        
        # State: displacement field u(x,y,t)
        self.u = np.zeros((size, size))      # Current displacement
        self.u_prev = np.zeros((size, size))  # Previous timestep
        self.v = np.zeros((size, size))      # Velocity field
        
        # Substrate properties (can vary spatially)
        self.stiffness = np.ones((size, size)) * 1.0
        self.mass = np.ones((size, size)) * 1.0
        
    def apply_force(self, x, y, magnitude):
        """Apply point force at (x, y)."""
        if 0 <= x < self.size and 0 <= y < self.size:
            self.u[int(y), int(x)] += magnitude
    
    def apply_oscillating_force(self, x, y, amplitude, frequency, time):
        """Apply sinusoidal force (oscillator)."""
        force = amplitude * np.sin(2 * np.pi * frequency * time)
        self.apply_force(x, y, force)
    
    def step(self, dt):
        """
        Update substrate by one timestep using wave equation.
        
        Uses finite difference approximation:
        u_new = 2u - u_prev + dt²(c²∇²u - γ∂u/∂t)
        """
        # Compute Laplacian (∇²u) using 5-point stencil
        laplacian = (
            np.roll(self.u, 1, axis=0) +
            np.roll(self.u, -1, axis=0) +
            np.roll(self.u, 1, axis=1) +
            np.roll(self.u, -1, axis=1) -
            4 * self.u
        )
        
        # Velocity (for damping)
        self.v = (self.u - self.u_prev) / dt
        
        # Wave equation update
        u_new = (
            2 * self.u - self.u_prev +
            dt**2 * (self.c**2 * laplacian / self.mass - self.gamma * self.v)
        )
        
        # Update state
        self.u_prev = self.u.copy()
        self.u = u_new
        
        # Boundary conditions (fixed edges)
        self.u[0, :] = 0
        self.u[-1, :] = 0
        self.u[:, 0] = 0
        self.u[:, -1] = 0
    
    def get_energy(self):
        """Total energy in substrate."""
        kinetic = 0.5 * np.sum(self.mass * self.v**2)
        potential = 0.5 * np.sum(self.stiffness * self.u**2)
        return kinetic + potential


# ============================================================================
# BIOLOGICAL OSCILLATORS
# ============================================================================

class Oscillator:
    """Generic oscillator: muscle, organ, limb segment."""
    
    def __init__(self, x, y, mass=1.0, stiffness=10.0, damping=0.5,
                 frequency=1.0, amplitude=1.0):
        self.x = x
        self.y = y
        self.m = mass
        self.k = stiffness
        self.gamma = damping
        self.f = frequency
        self.A = amplitude
        
        # State
        self.position = 0.0
        self.velocity = 0.0
        
        # Natural frequency
        self.omega_0 = 2 * np.pi * frequency
    
    def step(self, dt, external_force=0):
        """Update oscillator state."""
        # Force balance
        F_spring = -self.k * self.position
        F_damping = -self.gamma * self.velocity
        F_total = F_spring + F_damping + external_force
        
        # Acceleration
        a = F_total / self.m
        
        # Update (Euler integration)
        self.velocity += a * dt
        self.position += self.velocity * dt
    
    def drive(self, time):
        """Generate driving force (neural input)."""
        return self.A * self.k * np.sin(self.omega_0 * time)


class Heart:
    """Cardiac oscillator - rhythmic pumping."""
    
    def __init__(self, x, y):
        self.oscillator = Oscillator(x, y, mass=0.3, stiffness=50,
                                     frequency=1.2, amplitude=0.5)
        self.phase = 0
    
    def beat(self, time, dt):
        """Generate heartbeat."""
        drive_force = self.oscillator.drive(time)
        self.oscillator.step(dt, external_force=drive_force)
        self.phase = (2 * np.pi * self.oscillator.f * time) % (2 * np.pi)
        return self.oscillator.position


class Lungs:
    """Respiratory oscillator - breathing."""
    
    def __init__(self, x, y):
        self.oscillator = Oscillator(x, y, mass=1.0, stiffness=20,
                                     frequency=0.25, amplitude=1.0)
    
    def breathe(self, time, dt):
        """Generate breathing motion."""
        drive_force = self.oscillator.drive(time)
        self.oscillator.step(dt, external_force=drive_force)
        return self.oscillator.position


class Muscle:
    """Skeletal muscle - tunable resonator."""
    
    def __init__(self, x, y, length=10):
        self.x = x
        self.y = y
        self.length = length
        self.activation = 0.0
        
        self.k_passive = 100
        self.k_active = 500
        
        self.oscillator = Oscillator(x, y, mass=0.5,
                                     stiffness=self.k_passive,
                                     damping=2.0,
                                     frequency=10.0,
                                     amplitude=0.1)
    
    def activate(self, level):
        """Set activation level (neural input)."""
        self.activation = np.clip(level, 0, 1)
        self.oscillator.k = self.k_passive + self.activation * self.k_active
        self.oscillator.omega_0 = np.sqrt(self.oscillator.k / self.oscillator.m)
    
    def contract(self, dt):
        """Update muscle state."""
        self.oscillator.step(dt)
        return self.oscillator.position


class Limb:
    """Limb segment with pendulum dynamics."""
    
    def __init__(self, length=0.5, mass=5.0):
        self.L = length
        self.m = mass
        self.theta = 0.0
        self.omega = 0.0
        self.g = 9.8
        self.omega_0 = np.sqrt(self.g / self.L)
    
    def step(self, dt, torque=0):
        """Update limb angle."""
        I = self.m * self.L**2 / 3
        alpha = (self.m * self.g * self.L * np.sin(self.theta) + torque) / I
        self.omega += alpha * dt
        self.theta += self.omega * dt


# ============================================================================
# FULL HUMAN BODY
# =======================================================================
