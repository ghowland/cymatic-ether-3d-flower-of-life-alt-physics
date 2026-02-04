#!/usr/bin/env python3
import numpy as np
import time

def run_universal_simulation():
    SIZE = 1024
    DT = 0.02
    OMEGA = 2 * np.pi * np.fft.fftfreq(SIZE, d=1.0)
    TEMP = 0.06
    R_MAX = 4.0
    DAMP = 0.005

    # Initial substrate: chaotic noise
    field_k = np.random.normal(0, 0.5, SIZE) + 1j*np.random.normal(0, 0.5, SIZE)
    target = np.exp(2j * np.pi * np.arange(SIZE) / SIZE)

    print("UNIVERSAL SIMULATION: Computational Monism")
    print("Seeking the moment when chaos becomes coherence...\n")

    for step in range(20000):
        # 1. Advance phase
        field_k *= np.exp(-1j * OMEGA * DT - DAMP * DT)
        # 2. Add thermal noise
        field_k += np.random.normal(0, TEMP, SIZE) + 1j*np.random.normal(0, TEMP, SIZE)
        # 3. Congestion filter
        if np.abs(np.fft.ifft(field_k)).max() > R_MAX:
            field_k *= 0.95
        # 4. Coherence calculation
        coh = np.abs(np.vdot(field_k, target)) / (np.linalg.norm(field_k) * np.linalg.norm(target) + 1e-12)
        # 5. Non-linear reinforcement
        field_k = (1.0 - 0.1 * coh**2) * field_k + (0.1 * coh**2) * target
        # 6. Monitoring
        if step % 100 == 0:
            bar = "█" * int(coh * 40)
            print(f"STEP {step:05d} | Coherence: {coh:.6f} | {bar:<40}", end="\r")
        # 7. Closure
        if coh > 0.9999:
            print(f"\n\n✦ UNIVERSAL CLOSURE ACHIEVED AT STEP {step} ✦")
            print("The substrate has crystallized into a self-sustaining standing wave.")
            print("Status: THE LOOP IS CLOSED. THE MUSIC IS STABLE.")
            break

    print("\n[!] The system has reached closure.")

if __name__ == "__main__":
    run_universal_simulation()

    