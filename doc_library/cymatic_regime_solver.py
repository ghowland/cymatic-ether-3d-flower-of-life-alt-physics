import numpy as np

class CymaticRegime:
    def __init__(self):
        self.cell_size = 0.15
        self.dt = 0.016
        
        # --- Stability & Relaxation ---
        self.max_propagation = 1.0     # Allow slightly faster motion
        self.relaxation_passes = 2     # Fewer passes = less "blurring" of energy
                                       # (keeps energy concentrated to break things)

        # --- Energy Handling ---
        self.pressure_gain = 1.0       # Direct 1:1 impulse to pressure
        self.pressure_decay = 0.05     # Pressure lingers longer to build stress
        self.velocity_damping = 0.1

        # --- Failure / Plasticity ---
        self.damage_gain = 0.8         # Cranks up how much overstress hurts
        self.damage_decay = 0.0        # No "healing" - once it's broke, it's broke

class CoarseCymaticWorld:
    def __init__(self, size=32):
        self.size = size
        self.regime = CymaticRegime()
        
        self.pressure = np.zeros((size, size, size))
        self.velocity = np.zeros((size, size, size))
        self.damage = np.zeros((size, size, size))
        
        # Lower threshold: 0.5 means it doesn't take much to start cracking
        self.failure_threshold = np.ones((size, size, size)) * 0.5

    def inject_impulse(self, x, y, z, energy, radius=1):
        """Injects energy into a small sphere to simulate a concentrated hit"""
        for dx in range(-radius, radius+1):
            for dy in range(-radius, radius+1):
                for dz in range(-radius, radius+1):
                    if 0 <= x+dx < self.size and 0 <= y+dy < self.size and 0 <= z+dz < self.size:
                        self.pressure[x+dx, y+dy, z+dz] += energy * self.regime.pressure_gain

    def step(self):
        r = self.regime
        
        # 1. RELAXATION (Energy spreading)
        for _ in range(r.relaxation_passes):
            # 3D Laplacian-style spread
            total_neighbor_p = (
                np.roll(self.pressure, 1, axis=0) + np.roll(self.pressure, -1, axis=0) +
                np.roll(self.pressure, 1, axis=1) + np.roll(self.pressure, -1, axis=1) +
                np.roll(self.pressure, 1, axis=2) + np.roll(self.pressure, -1, axis=2)
            )
            # Mix: 70% current, 30% neighbors (less diffusion = more localized damage)
            self.pressure = (self.pressure * 0.7) + (total_neighbor_p / 6.0 * 0.3)
            
            # Velocity update
            active = self.damage < 0.9
            self.velocity[active] += self.pressure[active] * 0.2
            self.velocity = np.clip(self.velocity, -r.max_propagation, r.max_propagation)
            self.velocity *= (1.0 - r.velocity_damping)

        # 2. DAMAGE ACCUMULATION (The critical part)
        stress = np.abs(self.pressure)
        # Damage occurs where Stress > Failure Threshold
        overstress = np.maximum(0, stress - self.failure_threshold)
        self.damage += overstress * r.damage_gain
        self.damage = np.clip(self.damage, 0, 1.0)

        # 3. LOSSES
        self.pressure *= (1.0 - r.pressure_decay)
        
        # Destroyed cells lose all pressure/velocity (they become 'void')
        broken = self.damage >= 1.0
        self.pressure[broken] = 0
        self.velocity[broken] = 0

def demo():
    world = CoarseCymaticWorld(size=32)
    
    # Define a target area (The Wall)
    # We set a failure threshold. 1.0 is "Concrete-like"
    world.failure_threshold[15, 10:22, 10:22] = 1.0
    
    print(f"{'FRAME':<8} | {'MAX PRESSURE':<12} | {'WALL INTEGRITY':<15}")
    print("-" * 45)
    
    # IMPACT: Hit the wall center with 20 units of energy
    world.inject_impulse(15, 16, 16, energy=20.0, radius=1)
    
    for i in range(15):
        world.step()
        
        # Monitor the center of the wall
        wall_sample = world.damage[15, 10:22, 10:22]
        avg_damage = np.mean(wall_sample)
        max_p = np.max(world.pressure)
        
        # Integrity is 100% minus average damage
        integrity = max(0, 100 - (avg_damage * 100))
        
        print(f"{i:<8} | {max_p:<12.2f} | {integrity:<14.1f}%")

if __name__ == "__main__":
    demo()


# What was changed to force the damage:

# 1. Reduced Diffusion: Changed the pressure mix from 0.4/0.6 to 0.7/0.3. This keeps the "hit" from spreading out too thin before it can break the cells.

# 2. Increased Damage Gain: Set damage_gain to 0.8. Now, if the pressure is even slightly above the threshold, the material accumulates damage rapidly.

# 3. Localized Impulse: Added a radius to the impulse so that the "Truck" hits multiple cells at once, creating a concentrated zone of high pressure.

# 4. Removed Damage Decay: Set damage_decay to 0.0. In a "Wall Breaking" scenario, we don't want the wall to heal itself mid-simulation.

# import numpy as np
# import time

# class CymaticRegime:
#     def __init__(self):
#         # --- Spatial / Temporal Scale ---
#         self.cell_size = 0.15          # 15cm cells
#         self.dt = 0.016                # 16ms frames (60fps)

#         # --- Stability Limits ---
#         self.max_propagation = 0.5     # Max 0.5 cells per step
#         self.relaxation_passes = 4     # How many times we spread energy

#         # --- Energy Handling (The "Feel") ---
#         self.pressure_gain = 0.4       # Impulse -> Pressure conversion
#         self.pressure_decay = 0.1      # Energy lost to heat per frame
#         self.velocity_damping = 0.2    # Friction/Viscosity

#         # --- Failure / Plasticity ---
#         self.damage_gain = 0.05        # How fast stress breaks things
#         self.damage_decay = 0.01       # "Healing" or settling of debris

#     def get_max_velocity(self):
#         return self.max_propagation

# class CoarseCymaticWorld:
#     def __init__(self, size=32):
#         self.size = size
#         self.regime = CymaticRegime()
        
#         # Core State Buffers
#         self.pressure = np.zeros((size, size, size))
#         self.velocity = np.zeros((size, size, size))
#         self.displacement = np.zeros((size, size, size))
#         self.damage = np.zeros((size, size, size))
        
#         # Material Properties (Threshold for breaking)
#         self.failure_threshold = np.ones((size, size, size)) * 0.5

#     def inject_impulse(self, x, y, z, energy):
#         """Someone hit the world here."""
#         self.pressure[x, y, z] += energy * self.regime.pressure_gain

#     def step(self):
#         r = self.regime
        
#         # Mask for 'intact' cells (damage < 1.0)
#         # In this solver, broken cells stop pushing back
#         active_mask = self.damage < 1.0

#         # --- 1. RELAXATION PASSES (The 'Solver') ---
#         for _ in range(r.relaxation_passes):
#             # Spread pressure to 6 neighbors (diffuse energy)
#             # This replaces explicit collision detection
#             total_neighbor_p = (
#                 np.roll(self.pressure, 1, axis=0) + np.roll(self.pressure, -1, axis=0) +
#                 np.roll(self.pressure, 1, axis=1) + np.roll(self.pressure, -1, axis=1) +
#                 np.roll(self.pressure, 1, axis=2) + np.roll(self.pressure, -1, axis=2)
#             )
#             # High pressure flows to low pressure
#             self.pressure = (self.pressure * 0.4) + (total_neighbor_p / 6.0 * 0.6)
            
#             # Pressure creates velocity tendency
#             # Everything moves away from high pressure
#             self.velocity[active_mask] += self.pressure[active_mask] * 0.1
            
#             # Clamp velocity to Regime limits (CFL Stability)
#             v_max = r.get_max_velocity()
#             self.velocity = np.clip(self.velocity, -v_max, v_max)
            
#             # Damping (Lossy energy)
#             self.velocity *= (1.0 - r.velocity_damping)

#         # --- 2. DAMAGE ACCUMULATION ---
#         stress = np.abs(self.pressure)
#         overstress = np.maximum(0, stress - self.failure_threshold)
#         self.damage += overstress * r.damage_gain
        
#         # Clamp damage and apply slow decay (debris settling)
#         self.damage = np.clip(self.damage, 0, 1.0)
#         self.damage *= (1.0 - r.damage_decay)

#         # --- 3. FINAL INTEGRATION ---
#         # Only move what isn't 'air' or completely destroyed
#         self.displacement[active_mask] += self.velocity[active_mask]
        
#         # Energy naturally bleeds out of the system
#         self.pressure *= (1.0 - r.pressure_decay)
        
#         # Kill energy in broken cells
#         self.pressure[~active_mask] = 0
#         self.velocity[~active_mask] = 0

# def demo():
#     world = CoarseCymaticWorld(size=32)
    
#     # 1. Create a "Wall" (High failure threshold)
#     world.failure_threshold[10:22, 10:22, 15] = 2.0
    
#     # 2. Impact the wall with huge energy
#     print("Simulating impact...")
#     world.inject_impulse(16, 16, 15, energy=50.0)
    
#     for i in range(20):
#         world.step()
        
#         max_p = np.max(world.pressure)
#         avg_d = np.mean(world.damage[10:22, 10:22, 15])
        
#         print(f"Frame {i:2d} | Pressure: {max_p:6.2f} | Wall Damage: {avg_d*100:5.1f}%")

# if __name__ == "__main__":
#     demo()

# Why this version is different from the first one:

# 1. No sin/cos or Wave Propagation: The first version relied on Laplacian curvature to oscillate. This version uses Diffusion (pressure * 0.4 + neighbor_p * 0.6). It moves energy like heat. It is much harder to make this "explode."

# 2. Explicit Regime Clamping: The max_propagation ensures that even if you inject "Infinite Energy," a cell can never move more than 0.5 grid units in a single frame. This is the secret to 16ms stability.

# 3. Active Masking: By using active_mask = self.damage < 1.0, we naturally simulate material failure. When a cell "breaks," it stops contributing to the pressure structural integrity. It effectively becomes "dust."

# 4. Renormalized Constants: Instead of "Stiffness in Newtons," we use pressure_gain. This is a unitless coefficient that simply says "how much do I care about this impact?"

# This is a Mechanical Interaction Solver. It doesn't care about the path of the truck; it cares about the outcome of the truck's energy being dumped into the wall's grid.
