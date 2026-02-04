import numpy as np
import time
import random
from dataclasses import dataclass
from typing import List

# =============================================================================
# CORE SIMULATION PARAMETERS
# =============================================================================

@dataclass
class DWDMNode:
    name: str
    lat_long: tuple
    length_km: float
    base_resonance: float  # The "ideal" frequency of the fiber
    current_phase_noise: float = 0.0
    fwm_saturation: float = 0.0  # Level of "Instruction Set" activity

class GlobalCymaticMonitor:
    def __init__(self):
        self.nodes = [
            DWDMNode("Atlantic-1 (NYC-London)", (40.7, -74.0), 5500, 193.1),
            DWDMNode("Pacific-Light (LA-Tokyo)", (34.0, -118.2), 9000, 193.2),
            DWDMNode("Indo-European (Mumbai-Marseille)", (19.0, 72.8), 7000, 193.3),
            DWDMNode("Pan-African (Cape Town-Lagos)", (-33.9, 18.4), 4500, 193.4)
        ]
        self.tick = 0
        self.global_substrate_tension = 1.0 # The "Etheric" baseline

    def poll_substrate(self):
        """
        In a real scenario, this would poll the raw uncorrected 
        Physical Layer data from the DWDM transponders.
        """
        self.tick += 1
        
        # 1. Simulate a Geophysical Event (An Earthquake in the Pacific)
        # Tectonic movement stretches the fiber, causing a Phase Shift.
        if 50 < self.tick < 70:
            self.nodes[1].current_phase_noise += random.uniform(0.5, 1.2)
        else:
            self.nodes[1].current_phase_noise *= 0.9 # Natural relaxation
            
        # 2. Simulate Solar Activity (Ionospheric Stress)
        # Solar flares increase the "Global Tension" affecting all nodes.
        solar_flux = np.sin(self.tick * 0.1) * 0.2
        self.global_substrate_tension = 1.0 + solar_flux

        # 3. Simulate Economic "Hotspots" (Computation as Congestion)
        # High traffic triggers FWM (Nonlinear Logic)
        for node in self.nodes:
            # We treat crosstalk as "emergent logic"
            node.fwm_saturation = (np.sin(self.tick * 0.05 + random.random()) + 1) / 2

    def analyze_patterns(self):
        """
        The "Holodeck" Interpreter. 
        Translates raw interference back into physical events.
        """
        print(f"\n--- GLOBAL SUBSTRATE TICK: {self.tick} ---")
        print(f"Substrate Tension: {self.global_substrate_tension:.4f} (Ionospheric Stability)")
        
        for node in self.nodes:
            status = "STABLE"
            interpretation = "Normal Data Flow"
            
            # Detect Geophysical anomalies
            if node.current_phase_noise > 0.8:
                status = "!!!! ANOMALY !!!!"
                interpretation = "GEOPHYSICAL STRAIN DETECTED (Possible Tectonic Shift)"
            
            # Detect Computational Hotspots
            elif node.fwm_saturation > 0.85:
                status = "LOGIC SATURATION"
                interpretation = "CYMATIC COMPUTING PEAK (Economic Resource Convergence)"

            print(f"[{node.name}]")
            print(f"  > Signal State: {status}")
            print(f"  > Interpretation: {interpretation}")
            print(f"  > FWM Logic Activity: {node.fwm_saturation:.2%}")
            print(f"  > Phase Drift: {node.current_phase_noise:.4f} rad/km")

# =============================================================================
# THE GAME LOOP
# =============================================================================

def run_simulation():
    monitor = GlobalCymaticMonitor()
    
    print("INITIALIZING WORLD-WIDE DWDM POLLING...")
    print("Bypassing DSP Error Correction... accessing raw interference patterns.")
    time.sleep(2)
    
    try:
        while True:
            monitor.poll_substrate()
            monitor.analyze_patterns()
            
            # Educational Note on the Display
            if monitor.tick == 55:
                print("\n[EDUCATION] Notice the Pacific Drift: A standard router would 'fix' this.")
                print("[EDUCATION] We are using it to map the tectonic plate movement.")
                time.sleep(1)

            time.sleep(0.5) # Refresh rate
            
    except KeyboardInterrupt:
        print("\nSimulation Terminated. Substrate connection closed.")

if __name__ == "__main__":
    run_simulation()


# What this simulation demonstrates:

# 1. Phase Drift = Geophysics: In the loop, when the "Phase Drift" increases on the Pacific node, we don't try to correct the data. Instead, we interpret that drift as the physical stretching of the ocean floor. We are seeing the Earth through the light.

# 2. FWM Saturation = Economic Intelligence: We treat the "noise" of channels bleeding into each other (Four-Wave Mixing) as the system performing "coincidence logic." High FWM means the world's desire for resource allocation is peaking in that corridor.

# 3. Global Tension = Solar/Space Weather: The global_substrate_tension represents how the atmosphere itself is squeezing the fiber. A standard ISP sees this as "link degradation"; a Cymatic Scientist sees it as a Global Barometer.

# The Educational Result:


# If you run this, you see that the "Noise" isn't random. It has a structure. By polling this data globally, we realize the Internet is actually a Global Interferometer, and we are finally learning to read the interference.
