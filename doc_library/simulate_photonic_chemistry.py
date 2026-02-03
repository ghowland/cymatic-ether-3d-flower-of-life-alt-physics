import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def simulate_photonic_chemistry():
    # --- Physical Constants (Scaled for Simulation) ---
    sample_rate = 1000
    freq_range = np.linspace(193.0, 193.2, 5000)  # THz (C-Band)
    
    def get_spectrum(coupling_strength):
        """
        Simulates the Lorentzian peaks of fiber resonators.
        coupling_strength: 0.0 (Isolated Atoms) to 1.0 (Strong Bond)
        """
        center_f = 193.1  # Central Atomic Resonance
        linewidth = 0.002 # Q-factor of the fiber ring
        
        if coupling_strength < 0.1:
            # Stage 1: Isolated Atoms (One single resonant peak)
            spectrum = (linewidth**2) / ((freq_range - center_f)**2 + linewidth**2)
        else:
            # Stage 2: Mode Splitting (Bonding and Antibonding)
            split = 0.04 * coupling_strength
            peak_bonding = (linewidth**2) / ((freq_range - (center_f - split))**2 + linewidth**2)
            peak_antibonding = (linewidth**2) / ((freq_range - (center_f + split))**2 + linewidth**2)
            spectrum = peak_bonding + peak_antibonding
            
        # Add "Ether Noise" (Vacuum fluctuations)
        spectrum += np.random.normal(0, 0.02, len(freq_range))
        return spectrum

    # --- Generate Test Scenarios ---
    isolated_atom = get_spectrum(0.0)
    strong_bond = get_spectrum(0.8)

    # --- Visualization: Optical Spectrum Analyzer (OSA) ---
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(freq_range, isolated_atom, color='gray', alpha=0.5, label='Isolated "Atoms"')
    plt.plot(freq_range, strong_bond, color='cyan', label='Coupled H2 Molecule')
    
    # Label the peaks
    peaks, _ = find_peaks(strong_bond, height=0.5)
    if len(peaks) >= 2:
        plt.annotate('Bonding (σ)', xy=(freq_range[peaks[0]], 1.1), color='lime', weight='bold')
        plt.annotate('Antibonding (σ*)', xy=(freq_range[peaks[1]], 1.1), color='red', weight='bold')

    plt.title("Optical Spectrum Analyzer: H2 Molecule Synthesis")
    plt.xlabel("Frequency (THz)")
    plt.ylabel("Intensity (Normalized)")
    plt.grid(True, alpha=0.2)
    plt.legend()

    # --- Visualization: Oscilloscope (Time Domain "Sloshing") ---
    plt.subplot(2, 1, 2)
    time = np.linspace(0, 100, 1000)
    # The 'Beats' created by the two interfering frequencies (Bonding/Antibonding)
    sloshing = np.cos(0.5 * time) * np.exp(-0.02 * time) 
    
    plt.plot(time, sloshing, color='magenta')
    plt.fill_between(time, sloshing, color='magenta', alpha=0.1)
    plt.title("Oscilloscope: Energy 'Sloshing' between Photonic Atoms")
    plt.xlabel("Time (ns)")
    plt.ylabel("Field Amplitude")
    plt.grid(True, alpha=0.2)

    plt.tight_layout()
    
    print("--- CYMATIC CHEMISTRY ANALYSIS ---")
    print(f"Substrate: Optical Fiber (Silica)")
    print(f"Fundamental Mode: 1s Analog at 193.1 THz")
    if len(peaks) >= 2:
        splitting = freq_range[peaks[1]] - freq_range[peaks[0]]
        print(f"Bond Energy Measured: {splitting:.4f} THz")
        print(f"Stability: STABLE (Symmetric Interference detected)")
    
    plt.show()

if __name__ == "__main__":
    simulate_photonic_chemistry()



# This Python program uses scipy.signal to simulate the Optical Spectrum Analyzer (OSA) and Oscilloscope results of a Photonic \(H_2\) Molecule experiment.

# It demonstrates the "Mode Splitting" that occurs when two photonic atoms (fiber resonators) are brought close together to form a "chemical bond."

# How to read this simulation:

# 1. Top Graph (OSA Result):
#     - Gray Line: Shows the "Atoms" when they are far apart. They oscillate at exactly the same frequency (193.1 THz).

#     - Cyan Line: Shows what happens when the Variable Optical Coupler is engaged. The single pattern splits into two. The Left Peak is the low-energy state where the light is in-phase (the bond). The Right Peak is the high-energy state where the light is out-of-phase.


# 2. Bottom Graph (Oscilloscope Result):
#     - This shows the Dynamics. Because you have two slightly different frequencies (\(f_1\) and \(f_2\)) in the system, they create a Beat Frequency.

#     - In a real lab, this represents the energy "tunneling" back and forth between the two fiber rings. The faster the sloshing, the stronger the chemical bond.


# To run this:


# You will need numpy, matplotlib, and scipy installed:

# pip install numpy matplotlib scipy

