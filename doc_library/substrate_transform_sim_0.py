"""
Substrate-and-Transform Game Loop  (numpy only, ~100 lines)
----------------------------------------------------------
A minimal, mechanically *honest* demo of Computational Monism.
No sprites, no physics engines, no entities—just the loop.
Arrow keys move a viewpoint through the hologram.
"""

import numpy as np
import os
import sys
import termios
import tty

# ---------- 1.  SUBSTRATE PARAMETERS  ---------------------------------
SIZE        = 64          # cubic lattice (keep power of two for speed)
CELL        = 0.1         # not used for physics, only for human scale
DT          = 0.01        # Planck-tick (arbitrary units)
R_MAX       = 0.35        # congestion deletion threshold
TEMP        = 0.004       # temperature of thermal bath
DISP_COEFF  = 0.06        # dispersion coefficient  (omega = c * |k|)
DAMP        = 0.02        # substrate damping
SEED        = 42

# ---------- 2.  K-SPACE LATTICE  --------------------------------------
kvec = 2 * np.pi * np.fft.fftfreq(SIZE, d=1.0)
kx, ky, kz = np.meshgrid(kvec, kvec, kvec, indexing='ij')
k_mag = np.sqrt(kx**2 + ky**2 + kz**2)
k_mag[0,0,0] = 1e-10          # avoid /0
omega = DISP_COEFF * k_mag

# ---------- 3.  INITIAL CONDITIONS  -----------------------------------
rng = np.random.default_rng(SEED)
F_k = rng.normal(0, 0.1, size=(SIZE,SIZE,SIZE)) + \
      1j * rng.normal(0, 0.1, size=(SIZE,SIZE,SIZE))

# ---------- 4.  PROPAGATOR (PRE-COMPUTED)  -----------------------------
propagator = np.exp(-1j * omega * DT - DAMP * DT)

# ---------- 5.  CONGESTION FILTER  ------------------------------------
def apply_congestion(field_k):
    field_x = np.real(np.fft.ifftn(field_k, norm='ortho'))
    overload = np.abs(field_x) > R_MAX
    # delete overloaded modes (set to zero in k-space)
    mask = np.fft.fftn(overload.astype(float), norm='ortho')
    # soft deletion (smooth roll-off)
    field_k *= (1.0 - 0.9 * mask / (np.abs(mask).max() + 1e-10))
    return field_k

# ---------- 6.  THERMAL PERTURBATION  ---------------------------------
def thermal_noise(field_k, temp):
    noise = rng.normal(0, temp, size=field_k.shape) + \
            1j * rng.normal(0, temp, size=field_k.shape)
    return field_k + noise

# ---------- 7.  ONE FULL TICK  ----------------------------------------
def tick(field_k):
    # 1. spectral evolution
    field_k *= propagator
    # 2. congestion filter (gravity/selection)
    field_k = apply_congestion(field_k)
    # 3. entropy injection
    field_k = thermal_noise(field_k, TEMP)
    return field_k

# ---------- 8.  NON-BLOCKING KEYBOARD  -------------------------------
def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch

# ---------- 9.  SIMPLE TERMINAL RENDER  ------------------------------
def render_slice(field_x, z):
    """ASCII render of a single z-slice."""
    slice_ = field_x[:, :, z]
    # normalize to 0-1
    img = np.abs(slice_)
    img /= img.max() + 1e-10
    # dither to characters
    chars = np.asarray([' ', '░', '▒', '▓', '█'])[np.minimum(4, (img*5).astype(int))]
    for row in chars:
        print(''.join(row))

# ---------- 10.  MAIN LOOP  -----------------------------------------
def main():
    z = SIZE // 2
    print("\033[2J")          # clear screen
    while True:
        global F_k
        F_k = tick(F_k)
        field_x = np.real(np.fft.ifftn(F_k, norm='ortho'))
        print(f"\033[H")      # cursor home
        print("Substrate-and-Transform  |  Arrow keys move z-slice  |  Q to quit")
        print(f"z = {z:2d}   max|f_x| = {np.abs(field_x).max():5.3f}")
        render_slice(field_x, z)
        key = get_key()
        if key == 'q':
            break
        elif key == '\x1b':          # escape sequence
            get_key(); get_key()       # consume arrow keys
        elif key == 'A':               # up arrow
            z = max(0, z-1)
        elif key == 'B':               # down arrow
            z = min(SIZE-1, z+1)

if __name__ == "__main__":
    main()

    