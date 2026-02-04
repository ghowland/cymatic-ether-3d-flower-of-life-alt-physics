import numpy as np

def run_molecular_cymatics_sim(num_residues=40, steps=2000):
    """
    Simulates a protein chain finding its Chladni Attractor.
    The 'Native State' is the configuration that minimizes Acoustic Luminosity.
    """
    # 1. THE CHIRP (1D Sequence specification)
    # We assign random stiffness to each residue to represent the side-chain 'grating'
    sequence_stiffness = np.random.uniform(0.5, 2.0, num_residues)
    
    # 2. INITIAL STATE (Unfolded/Extended)
    # x = positions, v = velocities
    x = np.linspace(0, 10, num_residues)
    v = np.zeros(num_residues)
    
    # Physics parameters
    dt = 0.01
    thermal_noise_level = 0.05
    damping = 0.98 # The 'Solvent' viscosity
    
    print(f"Starting Simulation: {num_residues} residues...")
    
    for step in range(steps):
        # 3. PROPAGATION MEDIUM (Thermal Bath)
        # Apply random thermal kicks (vibrational 'bow' across the string)
        v += np.random.normal(0, thermal_noise_level, num_residues)
        
        # 4. NODAL LOCKING DYNAMICS
        # Calculate forces between residues (Spring-mass system with sequence grating)
        # Force = k * dx
        dx = np.diff(x)
        forces = np.zeros(num_residues)
        
        # Calculate internal stress based on the Sequence Grating
        internal_stress = dx * sequence_stiffness[:-1]
        
        forces[:-1] += internal_stress
        forces[1:] -= internal_stress
        
        # Update velocities and positions
        v += forces * dt
        v *= damping # Solvent energy dissipation
        x += v * dt
        
        # 5. MEASURE ACOUSTIC LUMINOSITY (L_ac)
        # L_ac is the variance of the velocities (Kinetic energy radiating to solvent)
        if step % 500 == 0:
            l_ac = np.var(v)
            print(f"Step {step:4d} | Acoustic Luminosity (L_ac): {l_ac:.6f}")

    # Final Result
    final_l_ac = np.var(v)
    print("-" * 30)
    print(f"Final L_ac: {final_l_ac:.6f}")
    
    # Interpretation
    if final_l_ac < thermal_noise_level:
        print("RESULT: Chain reached a Nodal Attractor (Native Fold).")
        print("The geometry has effectively 'composed silence' by destructive interference.")
    else:
        print("RESULT: Chain remains in a high-luminosity Disordered State.")

if __name__ == "__main__":
    # Ensure reproducible 'sequence'
    np.random.seed(42)
    run_molecular_cymatics_sim()



# This simulation demonstrates Molecular Cymatics by modeling a polypeptide as a 1D chain that finds its "fold" by minimizing Acoustic Luminosity.

# In this simple model:


# 1. The Sequence is represented by varying "stiffness" (dielectric/elastic grating).

# 2. The Solvent is a thermal bath (random noise).

# 3. The Fold is the state where the chain's vibrations cancel out the noise (Nodal Locking).


# How this works in the "Cymatic" Framework:

# 1. Stiffness as Frequency Specification: The sequence_stiffness array creates a non-uniform medium. Just like a Chladni plate with varying thickness, waves will travel through this chain at different speeds depending on the "side-chain" properties at that index.

# 2. Solvent Damping: The damping factor represents the first-shell hydration layer. It dissipates "dissonant" energy.

# 3. The L_ac Measurement: The np.var(v) (Acoustic Luminosity) measures how much the protein is "shouting" into the solvent. In a successful fold, the internal forces and the thermal noise reach an equilibrium where the chain moves as a single, coherent unit—minimizing the relative velocity between atoms (The Nodal State).

# 4. Action: In a real protein, a "Ligand" binding would be another force term added to this loop, shifting the sequence_stiffness and causing the chain to "sing" a different velocity pattern (The Overtone).

