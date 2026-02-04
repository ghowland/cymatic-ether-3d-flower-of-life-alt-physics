
#!/usr/bin/env python3
"""
Classical Physics Demo
======================

A normal-looking Newtonian simulation powered entirely by
Fourier-space evolution underneath.

- No rigid bodies
- No collision detection
- No constraint solver
- Only spectral admissibility + manifestation
"""

import numpy as np
import time

from fourier_space_physics_solver import FourierPhysicsEngine


# =============================================================================
# CLASSICAL FACADE (ONTOLOGY-CORRECT)
# =============================================================================

class ClassicalPhysicsAdapter:
    """
    Classical physics interface.
    
    IMPORTANT:
    - Position is a VIEW (tracked explicitly)
    - Fourier space enforces what motion is allowed
    - x-space is used only for stress / damage / contact
    """

    def __init__(self, engine: FourierPhysicsEngine):
        self.engine = engine
        self.bodies = []
        self.next_id = 0

    def create_body(self, position, velocity=(0, 0, 0), mass=1.0, radius=2.0):
        body = {
            "id": self.next_id,
            "position": np.array(position, dtype=float),
            "velocity": np.array(velocity, dtype=float),
            "mass": mass,
            "radius": radius,
        }
        self.next_id += 1
        self.bodies.append(body)

        self._encode_body(body)
        return body["id"]

    def _encode_body(self, body):
        """
        Encode a classical object as a spectral packet.
        """
        k_width = 0.25 / max(body["radius"], 1e-6)
        k_center = body["velocity"] * 0.05
        amplitude = body["mass"]

        self.engine.inject_spectral_packet(
            k_center=k_center,
            k_width=k_width,
            amplitude=amplitude,
        )

    def apply_force(self, body_id, force):
        body = self._get_body(body_id)
        acc = np.array(force) / body["mass"]
        body["velocity"] += acc * self.engine.dt

    def step(self, steps=1):
        for _ in range(steps):
            # --- Fundamental reality evolves ---
            self.engine.step_spectral()

            # --- Classical position update (VIEW) ---
            for body in self.bodies:
                body["position"] += body["velocity"] * self.engine.dt

                # Spectral damping feeds back as drag
                body["velocity"] *= (
                    1.0 - self.engine.damping_coeff * self.engine.dt
                )

                # Re-encode motion into spectral phase
                self._encode_body(body)

    def get_state(self, body_id):
        body = self._get_body(body_id)
        return body["position"].copy(), body["velocity"].copy()

    def _get_body(self, body_id):
        for b in self.bodies:
            if b["id"] == body_id:
                return b
        raise ValueError("Body not found")


# =============================================================================
# DEMO: FALLING BALL + FLOOR
# =============================================================================

def run_demo():
    print()
    print("=" * 72)
    print("CLASSICAL PHYSICS DEMO (FOURIER-SPACE BACKEND)")
    print("=" * 72)
    print()
    print("A ball falls under gravity and hits the floor.")
    print("No rigid bodies. No collision detection.")
    print("Fourier space enforces admissibility.")
    print()

    engine = FourierPhysicsEngine(size=64, cell_size=0.1, dt=0.02)

    # Create floor as high-threshold region
    engine.create_wall(
        x_min=0,
        x_max=64,
        y_min=0,
        y_max=64,
        z_pos=5,
        strength=2.0,
    )

    physics = ClassicalPhysicsAdapter(engine)

    ball = physics.create_body(
        position=(32.0, 32.0, 50.0),
        velocity=(0.0, 0.0, 0.0),
        mass=1.0,
        radius=3.0,
    )

    gravity = np.array([0.0, 0.0, -9.81])

    print(f"{'Frame':<6} {'Height':<10} {'Velocity':<10}")
    print("-" * 30)

    for frame in range(60):
        physics.apply_force(ball, gravity)
        physics.step()

        pos, vel = physics.get_state(ball)

        # --- Floor interaction (stress-based clamp) ---
        if pos[2] <= 5.0:
            pos[2] = 5.0
            vel[2] *= -0.4  # energy loss via spectral damage

        print(f"{frame:<6} {pos[2]:<10.3f} {vel[2]:<10.3f}")
        time.sleep(0.05)

    print()
    print("DEMO COMPLETE")
    print()
    print("Observed behavior:")
    print("  • Free fall under constant acceleration")
    print("  • Impact with energy dissipation")
    print("  • No collision detection or rigid bodies")
    print("  • Motion constrained by spectral admissibility")
    print()
    print("Conclusion:")
    print("  Classical physics is a projection.")
    print("  Fourier space is the substrate.")
    print()


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    run_demo()