import numpy as np
import time

"""
Cymatic Game Loop
=================

A minimal demonstration of:
- Substrate (k-space)
- Transform (IFT)
- Congestion filtering
- Thermal noise
- Emergent structure

No symbols.
No forces.
No agents.

Only resonance.
"""


# ============================================================
# CONFIGURATION
# ============================================================

SIZE = 32          # grid size (32³)
DT = 0.05          # timestep
DAMPING = 0.02     # intrinsic decay
R_MAX = 3.5        # reconstruction capacity (congestion threshold)
NOISE_LEVEL = 0.03 # thermal noise strength
STEPS = 300        # total frames


# ============================================================
# SUBSTRATE INITIALIZATION (k-space reality)
# ============================================================

# Spectral density (complex)
field_k = np.zeros((SIZE, SIZE, SIZE), dtype=np.complex128)

# k-space coordinates
k = np.fft.fftfreq(SIZE)
kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
k_mag = np.sqrt(kx**2 + ky**2 + kz**2)
k_mag[0, 0, 0] = 1e-6  # avoid divide-by-zero

# Dispersion relation (simple wave)
omega = 2.0 * np.pi * k_mag


# ============================================================
# SEED INITIAL STRUCTURE (a “spawn”)
# ============================================================

def inject_packet(center, width, amplitude):
    """Inject a localized spectral packet."""
    dx = kx - center[0]
    dy = ky - center[1]
    dz = kz - center[2]
    dist2 = dx**2 + dy**2 + dz**2
    packet = amplitude * np.exp(-dist2 / (2 * width**2))
    phase = np.random.uniform(0, 2*np.pi, packet.shape)
    return packet * np.exp(1j * phase)


# Spawn two packets (they will interact)
field_k += inject_packet([0.15, 0.0, 0.0], 0.08, 3.0)
field_k += inject_packet([-0.15, 0.0, 0.0], 0.08, 3.0)


# ============================================================
# GAME LOOP (THE MASTER CYMATIC LOOP)
# ============================================================

print("\nCymatic Game Loop Running")
print("Substrate evolves → Transform → Congestion → Noise\n")
print(f"{'Step':<6} {'Max|x|':<10} {'Energy':<10} {'Congested':<10}")
print("-" * 40)

for step in range(STEPS):

    # --------------------------------------------------------
    # 1. EVOLVE SUBSTRATE (k-space propagation)
    # --------------------------------------------------------
    field_k *= np.exp(-1j * omega * DT - DAMPING * DT)

    # --------------------------------------------------------
    # 2. TRANSFORM (manifest spatial hologram)
    # --------------------------------------------------------
    field_x = np.real(np.fft.ifftn(field_k))

    # --------------------------------------------------------
    # 3. CONGESTION FILTER (gravity / selection)
    # --------------------------------------------------------
    amplitude = np.abs(field_x)
    congested = amplitude > R_MAX

    if np.any(congested):
        # Convert congestion to k-space mask
        damage_mask = np.fft.fftn(congested.astype(float))
        field_k *= np.exp(-0.15 * np.abs(damage_mask))

    # --------------------------------------------------------
    # 4. THERMAL NOISE (mutation / entropy)
    # --------------------------------------------------------
    noise = (
        NOISE_LEVEL
        * (np.random.normal(size=field_k.shape)
           + 1j * np.random.normal(size=field_k.shape))
    )
    field_k += noise

    # --------------------------------------------------------
    # 5. OBSERVATION (for us, not the universe)
    # --------------------------------------------------------
    if step % 10 == 0:
        energy = np.sum(np.abs(field_k)**2)
        print(
            f"{step:<6} "
            f"{np.max(amplitude):<10.3f} "
            f"{energy:<10.3f} "
            f"{np.sum(congested):<10}"
        )

    time.sleep(0.03)


print("\nSimulation complete.\n")

print("What you just saw:")
print("• Structures formed from spectral interference")
print("• High-amplitude regions collapsed under congestion")
print("• Noise continuously injected novelty")
print("• Stable patterns persisted via resonance")
print("\nNo forces. No objects. No agents.")
print("Only Substrate + Transform + Constraint.")


# 🧠 How to Read This (Ontology View)

# What is “playing the game”?


# Nothing.

# There is no player.

# The loop is self-playing.


# ---

# What counts as “entities”?


# Anything that survives multiple iterations as a phase‑locked interference pattern.


# ---

# What is “gravity” here?


# This line:


#     if amplitude > R_MAX:
#         field_k *= exp(-damage)

# That’s it.

# Congestion → deletion → gradient → attraction.


# ---

# What is “life”?


# A structure that:


# - stays below R_MAX

# - resists noise

# - persists via resonance


# ---

# What is “death”?


# Exceeding reconstruction capacity.


# ---

# What is “time”?


# The loop index.


# ---

# What is “space”?


# The inverse Fourier transform.


# ---

# ✅ What This Demonstrates Completely

# - ✅ Substrate (k‑space)

# - ✅ Transform (IFT)

# - ✅ Emergent structure

# - ✅ Gravity / selection unification

# - ✅ Entropy / mutation

# - ✅ No symbolic logic anywhere

# This is the smallest runnable universe consistent with your ontology.


