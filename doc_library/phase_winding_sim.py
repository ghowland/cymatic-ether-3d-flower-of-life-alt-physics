import numpy as np
import time

def run_phase_winding_demo():
    """
    Cymatic Phase-Winding Simulation: 
    Demonstrates Matter/Charge as a Topological Constraint.
    """
    # 1. SETUP SUBSTRATE
    grid_size = 64
    # The 'Phase Map' represents the state of the substrate at every point
    # We use complex numbers: amplitude * exp(i * phase)
    substrate = np.ones((grid_size, grid_size), dtype=complex)
    
    # Create coordinate grids
    y, x = np.mgrid[0:grid_size, 0:grid_size]
    center = grid_size // 2
    
    print("--- CYMATIC PHASE-WINDING SIMULATION ---")
    print("Logic: We are 'tying a knot' in the phase of the vacuum.")
    print("The 'Object' you see is the result of Phase Discontinuity.\n")

    # 2. INJECT TOPOLOGICAL CHARGE (The 'Winding')
    # We calculate the angle of every point relative to the center
    angles = np.arctan2(y - center, x - center)
    
    # Winding Number (Q): How many times the phase spins 360 degrees
    # Q = 1 (Proton/Electron), Q = 2 (Higher Charge), etc.
    winding_number = 1 
    
    # Apply the winding to the substrate phase
    # substrate = 1.0 * exp(i * angle * Q)
    substrate = np.exp(1j * angles * winding_number)

    # 3. ANALYSIS: DERIVE MANIFESTATION
    # In Cymatic Ontology, 'Physical Matter' is the Spatial Gradient of the Phase.
    # Where phase changes rapidly (the center of the knot), 'Mass' appears.
    
    # Calculate the gradient (how fast phase changes)
    dy, dx = np.gradient(substrate)
    gradient_magnitude = np.abs(dx) + np.abs(dy)
    
    # 4. VISUALIZATION (ASCII)
    # We will 'render' the phase map and the resulting 'matter'
    def render_grid(data, label, is_phase=False):
        print(f"--- {label} ---")
        chars = " .:-=+*#%@"
        # Normalize for display
        d_min, d_max = data.min(), data.max()
        if d_max == d_min: d_max += 1e-9
        
        normalized = ((data - d_min) / (d_max - d_min) * (len(chars)-1)).astype(int)
        
        for row in normalized[::2]: # Step by 2 for better ASCII aspect ratio
            line = "".join(chars[val] for val in row)
            print(line)
        print("\n")

    # Show the Phase Map (The 'Software' / 'k-space' organization)
    # We show the angle of the complex numbers
    render_grid(np.angle(substrate), "PHASE MAP (The Underlying Organization)")

    # Show the Manifested Reality (The 'Hardware' / 'x-space' manifestation)
    # Matter appears where the phase is forced to 'bend' too sharply
    render_grid(gradient_magnitude, "MANIFESTED MATTER (The Topological Defect)")

    print("EXPLANATION:")
    print("1. Look at the PHASE MAP: It is a 'Vortex' of information.")
    print("2. Look at MANIFESTED MATTER: A 'Particle' appears at the center.")
    print("3. This particle is not 'placed' there; it is a GEOMETRIC NECESSITY.")
    print("4. You cannot remove the center dot without untwisting the whole map.")
    print("5. This is why Charge is Quantized and Conserved.")

if __name__ == "__main__":
    run_phase_winding_demo()



# This simulation demonstrates Charge as a Topological Defect.

# In the Cymatic Ontology, an "Electron" or "Charge" isn't a solid ball; it is a Vortex in the Phase Map. This script creates a 2D substrate where the "Matter" you see is actually the result of Phase Winding.

# The "Charge" is created by forcing the phases of the vacuum to "wind" around a central point. Because the phase must be continuous, it creates a "knot" (a singularity) that cannot be undone without an equal and opposite anti-knot.

# How to read this "Cymatic" code:

# 1. 


# substrate = np.exp(1j * angles * winding_number):

# This is the core of the theory. We aren't defining an object's position. We are defining a Phase-Field. The winding_number is the "Charge" (\(Q\)). If you change it to 2, the knot becomes "tighter," and the manifested particle becomes "heavier" (more gradient density).



# 2. 
# gradient_magnitude:

# This represents the 3D-IFT logic. Matter is where the substrate's phase is under the most stress. In the very center of the vortex, the phase is mathematically undefined (a singularity). In physics, we call this a "Point Particle." In cymatics, we call it a Phase-Anchor.



# 3. 
# Conservation of Charge:

# Try to imagine "erasing" that central dot. You can't. To get rid of the dot, you would have to change the phase of every single pixel in the entire universe (the grid) to be the same. This is why you can only destroy a charge with an Anti-Charge (a winding in the opposite direction, which "unwinds" the substrate).
