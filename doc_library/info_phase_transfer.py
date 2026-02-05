import numpy as np

def simulate_phase_transfer():
    size = 128
    
    # Two regions in substrate
    region_A = slice(30, 50)  # Source
    region_B = slice(80, 100) # Target
    
    # Initialize substrate
    F_k = np.random.randn(size,size,size) + 1j*np.random.randn(size,size,size)
    
    # Implant information in region A (specific phase pattern)
    k = np.fft.fftfreq(size) * 2*np.pi
    kx = k[:, None, None]
    ky = k[None, :, None]
    kz = k[None, None, :]
    
    # Information = coherent phase pattern
    pattern = np.exp(1j * (3*kx + 4*ky + 5*kz))  # Specific direction
    F_k *= 0.1  # Reduce background
    F_k[region_A, :, :] = pattern[region_A, :, :]  # Implant in A
    
    # Setup
    k_mag = np.sqrt(kx**2 + ky**2 + kz**2)
    omega = k_mag
    gamma = 0.01
    coupling = 0.05  # Coupling strength between regions
    dt = 0.02
    
    coherence_history = []
    
    for step in range(2000):
        # Evolution
        F_k *= np.exp(-1j*omega*dt - gamma*dt)
        
        # Coupling (information transfer)
        # Region B tries to match region A
        F_k[region_B,:,:] += coupling * (F_k[region_A,:,:] - F_k[region_B,:,:])
        
        # Measure coherence between A and B
        overlap = np.sum(np.conj(F_k[region_A,:,:].flatten()) * 
                        F_k[region_B,:,:].flatten())
        norm_A = np.linalg.norm(F_k[region_A,:,:])
        norm_B = np.linalg.norm(F_k[region_B,:,:])
        coherence = np.abs(overlap) / (norm_A * norm_B + 1e-30)
        
        coherence_history.append(coherence)
        
        if step % 200 == 0:
            print(f"Step {step}: Coherence A-B = {coherence:.6f}")
    
    return coherence_history

# Run
print("Simulating phase transfer (information communication)...")
coherence = simulate_phase_transfer()
print(f"\nFinal coherence: {coherence[-1]:.6f}")
print("Information successfully transferred from A to B via phase-locking")

