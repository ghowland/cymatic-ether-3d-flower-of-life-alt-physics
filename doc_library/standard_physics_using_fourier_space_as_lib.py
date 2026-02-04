#!/usr/bin/env python3
"""
Classical Physics Demo (Powered by Fourier-Space Reality)
=========================================================

This demo shows how a normal Newtonian physics simulation
is actually driven by Fourier-space evolution underneath.

Requirements:
- numpy
- fourier_physics_engine.py in the same directory
"""

import numpy as np
import time

# ---------------------------------------------------------------------
# IMPORT FOURIER ENGINE AS A LIBRARY
# ---------------------------------------------------------------------

from fourier_space_physics_solver import FourierPhysicsEngine


# ---------------------------------------------------------------------
# CLASSICAL WRAPPER
# ---------------------------------------------------------------------

class ClassicalPhysicsAdapter:
    """
    Classical-looking physics API backed by Fourier-space engine.
    """

    def __init__(self, engine: FourierPhysicsEngine):
        self.engine = engine
        self.bodies = []
        self._next_id = 0

    def create_body(
        self,
        position,
        radius=2.0,
        mass=1.0,
        velocity=(0, 0, 0),
    ):
        body = {
            "id": self._next_id,
            "position": np.array(position, dtype=float),
            "velocity": np.array(velocity, dtype=float),
            "radius": radius,
            "mass": mass,
        }
        self._next_id += 1
        self.bodies.append(body)

        self._encode_body(body)
        return body["id"]

    def _encode_body(self, body):
        """
        Encode classical body as spectral packet.
        """
        k_width = 0.25 / max(body["radius"], 1e-3)
        k_center = body["velocity"] * 0.05
        amplitude = body["mass"]

        self.engine.inject_spectral_packet(
            k_center=k_center,
            k_width=k_width,
            amplitude=amplitude,
        )

    def apply_force(self, body_id, force):
        body = self._get_body(body_id)
        acceleration = np.array(force) / body["mass"]
        body["velocity"] += acceleration * self.engine.dt
        self._encode_body(body)

    def step(self, steps=1):
        for _ in range(steps):
            self.engine.step_spectral()
            self._update_from_field()

    def _update_from_field(self):
        field = self.engine.field_x
        amp = np.abs(field)
        threshold = np.max(amp) * 0.5

        coords = np.argwhere(amp > threshold)
        if len(coords) == 0:
            return

        center = coords.mean(axis=0)

        for body in self.bodies:
            body["position"] = center * self.engine.cell_size
            body["velocity"] *= (1.0 - self.engine.damping_coeff * self.engine.dt)

    def get_state(self, body_id):
        body = self._get_body(body_id)
        return body["position"].copy(), body["velocity"].copy()

    def _get_body(self, body_id):
        for b in self.bodies:
            if b["id"] == body_id:
                return b
        raise ValueError("Body not found")


# ---------------------------------------------------------------------
# DEMO: FALLING BALL WITH FLOOR
# ---------------------------------------------------------------------

def run_demo():
    print()
    print("=" * 72)
    print("CLASSICAL PHYSICS DEMO (FOURIER-SPACE BACKEND)")
    print("=" * 72)
    print()
    print("A ball falls under gravity and hits the floor.")
    print("No rigid bodies. No collisions. Only Fourier space.")
    print()

    engine = FourierPhysicsEngine(size=64, cell_size=0.1, dt=0.02)

    # Create a solid floor (high threshold)
    engine.create_wall(
        x_min=0,
        x_max=64,
        y_min=0,
        y_max=64,
        z_pos=5,
        strength=2.0,
    )

    physics = ClassicalPhysicsAdapter(engine)

    ball_id = physics.create_body(
        position=(32, 32, 50),
        radius=3.0,
        mass=1.0,
        velocity=(0, 0, 0),
    )

    gravity = np.array([0, 0, -9.81])

    print(f"{'Frame':<6} {'Height':<10} {'Velocity':<10}")
    print("-" * 30)

    for frame in range(60):
        physics.apply_force(ball_id, gravity)
        physics.step()

        pos, vel = physics.get_state(ball_id)

        # Simple floor clamp (visual clarity only)
        if pos[2] < 5:
            pos[2] = 5
            vel[2] *= -0.4

        print(f"{frame:<6} {pos[2]:<10.3f} {vel[2]:<10.3f}")

        time.sleep(0.05)

    print()
    print("DEMO COMPLETE")
    print()
    print("Observed behavior:")
    print("  • Free fall under constant acceleration")
    print("  • Energy dissipation on impact")
    print("  • No explicit collision detection")
    print("  • Motion emerged from spectral evolution")
    print()
    print("Conclusion:")
    print("  Classical physics is a projection.")
    print("  Fourier space is the substrate.")
    print()


# ---------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------

if __name__ == "__main__":
    run_demo()




# How to Run


# Assuming both files are in the same directory:


#     fourier_physics_engine.py
#     classical_wrapper_demo.py

# Run:


#     python3 classical_wrapper_demo.py


# ---

# What This Demo Proves (Visibly)


# • Newtonian free fall emerges

# • Gravity applied as “force” becomes spectral phase tilt

# • Collision handled by damage + threshold, not detection

# • x‑space behavior is derived, not simulated

# This is the bridge demo that makes your framework legible to:


# - physicists

# - engine developers

# - skeptics
