#!/usr/bin/env python3
"""
Minimal 3D Flower of Life Universe Simulator
============================================

Simulates reality as wave patterns in a 3D close-packed substrate.

The Isotropic Vector Matrix (IVM) / 3D Flower of Life has 12 neighbors 
per cell - the maximum uniform connectivity in 3D space.

Each cell oscillates based on its 12 neighbors. Stable patterns = matter.
Propagating waves = light. All from one simple update rule.
"""

import numpy as np


# =============================================================================
# 3D LATTICE GEOMETRY (IVM / Flower of Life)
# =============================================================================

def get_ivm_neighbors():
    """
    Returns the 12 neighbor offsets for IVM (face-centered cubic packing).
    
    In IVM, each cell has 12 equidistant neighbors forming a cuboctahedron.
    This is the 3D Flower of Life geometry.
    
    These offsets define the 12 directions to neighbors in FCC lattice:
    - 6 face neighbors (±1,±1,0) and permutations  
    - NOT edge or corner neighbors (those are farther)
    """
    neighbors = [
        # Face neighbors in x-y plane shifted
        ( 1,  1,  0), ( 1, -1,  0),
        (-1,  1,  0), (-1, -1,  0),
        # Face neighbors in x-z plane shifted  
        ( 1,  0,  1), ( 1,  0, -1),
        (-1,  0,  1), (-1,  0, -1),
        # Face neighbors in y-z plane shifted
        ( 0,  1,  1), ( 0,  1, -1),
        ( 0, -1,  1), ( 0, -1, -1),
    ]
    return neighbors


# =============================================================================
# SUBSTRATE STATE
# =============================================================================

def create_substrate(size):
    """
    Create the ether substrate - the medium that supports all patterns.
    
    Args:
        size: edge length of cubic volume
        
    Returns:
        field: 3D array of displacements (the wave state)
        velocity: 3D array of velocities (rate of change)
    """
    field = np.zeros((size, size, size), dtype=np.float32)
    velocity = np.zeros((size, size, size), dtype=np.float32)
    return field, velocity


# =============================================================================
# WAVE DYNAMICS
# =============================================================================

def update_substrate(field, velocity, dt, coupling, damping):
    """
    Update the substrate using the wave equation on IVM lattice.
    
    Physics:
        Each cell wants to match its 12 neighbors (coupling).
        This creates wave propagation through the medium.
        
    The update rule:
        acceleration = coupling * (average_of_neighbors - current_value) - damping * velocity
        velocity += acceleration * dt
        field += velocity * dt
        
    This is the continuous elastic medium wave equation discretized on IVM.
    
    Args:
        field: current displacement state
        velocity: current velocity state  
        dt: time step
        coupling: how strongly cells pull toward neighbors (wave speed²)
        damping: energy dissipation factor
        
    Returns:
        updated field, updated velocity
    """
    size = field.shape[0]
    neighbors = get_ivm_neighbors()
    
    # Calculate acceleration from neighbor coupling
    acceleration = np.zeros_like(field)
    
    for z in range(1, size - 1):
        for y in range(1, size - 1):
            for x in range(1, size - 1):
                
                # Sum the 12 neighbors
                neighbor_sum = 0.0
                neighbor_count = 0
                
                for dx, dy, dz in neighbors:
                    nx, ny, nz = x + dx, y + dy, z + dz
                    
                    # Check bounds
                    if 0 <= nx < size and 0 <= ny < size and 0 <= nz < size:
                        neighbor_sum += field[nz, ny, nx]
                        neighbor_count += 1
                
                # Average of neighbors
                if neighbor_count > 0:
                    neighbor_avg = neighbor_sum / neighbor_count
                    
                    # Acceleration toward average (elastic restoring force)
                    acceleration[z, y, x] = coupling * (neighbor_avg - field[z, y, x])
                    
                    # Damping (energy loss)
                    acceleration[z, y, x] -= damping * velocity[z, y, x]
    
    # Update velocity and field
    velocity += acceleration * dt
    field += velocity * dt
    
    return field, velocity


# =============================================================================
# PATTERN INITIALIZATION
# =============================================================================

def add_spherical_pulse(field, center, radius, amplitude):
    """
    Add a spherical wave pulse - like dropping a stone in 3D water.
    
    This creates a localized disturbance that will propagate outward.
    """
    cx, cy, cz = center
    size = field.shape[0]
    
    for z in range(size):
        for y in range(size):
            for x in range(size):
                # Distance from center
                dist = np.sqrt((x - cx)**2 + (y - cy)**2 + (z - cz)**2)
                
                # Gaussian pulse
                if dist < radius * 2:
                    field[z, y, x] += amplitude * np.exp(-(dist**2) / (2 * radius**2))
    
    return field


def add_standing_wave(field, wavelength, amplitude, axis=0):
    """
    Add a standing wave pattern - analog of stable matter.
    
    Standing waves persist over time because they're in resonance
    with the lattice geometry. These are the "particles" in this model.
    
    Args:
        axis: 0=x, 1=y, 2=z direction for the wave
    """
    size = field.shape[0]
    
    for z in range(size):
        for y in range(size):
            for x in range(size):
                if axis == 0:
                    pos = x
                elif axis == 1:
                    pos = y
                else:
                    pos = z
                    
                # Sine wave at specific wavelength
                field[z, y, x] += amplitude * np.sin(2 * np.pi * pos / wavelength)
    
    return field


def add_interference_pattern(field, center1, center2, wavelength, amplitude):
    """
    Add two spherical sources creating interference - matter formation analog.
    
    Where waves constructively interfere, stable patterns (matter) can form.
    This demonstrates the Flower of Life principle: overlapping patterns
    create stable nodes.
    """
    size = field.shape[0]
    
    for z in range(size):
        for y in range(size):
            for x in range(size):
                # Distance from each source
                dist1 = np.sqrt((x - center1[0])**2 + 
                              (y - center1[1])**2 + 
                              (z - center1[2])**2)
                dist2 = np.sqrt((x - center2[0])**2 + 
                              (y - center2[1])**2 + 
                              (z - center2[2])**2)
                
                # Spherical waves from each source
                if dist1 > 0:
                    wave1 = amplitude * np.sin(2 * np.pi * dist1 / wavelength) / dist1
                else:
                    wave1 = amplitude
                    
                if dist2 > 0:
                    wave2 = amplitude * np.sin(2 * np.pi * dist2 / wavelength) / dist2
                else:
                    wave2 = amplitude
                
                field[z, y, x] += wave1 + wave2
    
    return field


# =============================================================================
# ANALYSIS
# =============================================================================

def measure_energy(field, velocity):
    """
    Measure total energy in the substrate.
    
    Energy = kinetic (velocity²) + potential (displacement²)
    
    In the pedagogical model:
    - High energy density = mass
    - Energy propagation = light
    """
    kinetic = np.sum(velocity**2) / 2
    potential = np.sum(field**2) / 2
    return kinetic + potential


def find_stable_patterns(field, threshold):
    """
    Identify regions of high sustained amplitude - matter analogs.
    
    Stable high-amplitude regions are like persistent particles.
    """
    amplitude = np.abs(field)
    stable_regions = amplitude > threshold
    return np.sum(stable_regions)


# =============================================================================
# MAIN SIMULATION
# =============================================================================

def run_simulation():
    """
    Run the cymatic universe simulation.
    """
    print("Initializing 3D Flower of Life Universe...")
    
    # Parameters
    size = 40           # Lattice size (40x40x40 cells)
    dt = 0.1            # Time step
    coupling = 0.5      # Wave propagation strength
    damping = 0.01      # Energy dissipation
    steps = 200         # Number of time steps
    
    # Create substrate
    field, velocity = create_substrate(size)
    
    # Initialize with interference pattern (matter formation)
    center1 = (size // 3, size // 2, size // 2)
    center2 = (2 * size // 3, size // 2, size // 2)
    wavelength = 6
    amplitude = 2.0
    
    field = add_interference_pattern(field, center1, center2, wavelength, amplitude)
    
    print(f"Substrate: {size}³ cells")
    print(f"Each cell has 12 IVM neighbors")
    print(f"Running {steps} time steps...")
    print()
    
    # Run simulation
    for step in range(steps):
        field, velocity = update_substrate(field, velocity, dt, coupling, damping)
        
        # Periodic measurement
        if step % 20 == 0:
            energy = measure_energy(field, velocity)
            stable = find_stable_patterns(field, threshold=0.5)
            max_amplitude = np.max(np.abs(field))
            
            print(f"Step {step:3d}  |  Energy: {energy:8.2f}  |  "
                  f"Stable cells: {stable:5d}  |  Max amplitude: {max_amplitude:6.3f}")
    
    print()
    print("Simulation complete.")
    print()
    print("What this shows:")
    print("- The substrate oscillates according to IVM (12-neighbor) geometry")
    print("- Interference patterns create stable high-energy regions")  
    print("- These stable patterns are analogs of 'matter'")
    print("- Energy propagates as waves (analog of 'light')")
    print("- All from one simple rule: match your 12 neighbors")
    
    return field, velocity


# =============================================================================
# VISUALIZATION (optional)
# =============================================================================

def save_slice_image(field, filename):
    """
    Save a 2D slice through the 3D field to see patterns.
    
    This shows a cross-section of the substrate so you can see
    wave interference patterns.
    """
    try:
        import matplotlib.pyplot as plt
        
        # Take middle slice
        slice_2d = field[field.shape[0] // 2, :, :]
        
        plt.figure(figsize=(8, 8))
        plt.imshow(slice_2d, cmap='RdBu', origin='lower', 
                   vmin=-2, vmax=2, interpolation='bilinear')
        plt.colorbar(label='Displacement')
        plt.title('2D Slice Through 3D Substrate')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Saved visualization: {filename}")
        
    except ImportError:
        print("matplotlib not available - skipping visualization")


# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":
    field, velocity = run_simulation()
    
    # Save visualization of final state
    save_slice_image(field, "/mnt/user-data/outputs/fol_universe_final.png")
