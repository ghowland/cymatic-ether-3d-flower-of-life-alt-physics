import numpy as np


def simulate_learning():
    size = 64
    
    # Initialize random substrate (naive state)
    F_k = (np.random.randn(size,size,size) + 
           1j*np.random.randn(size,size,size)) * 0.5
    
    # Define "knowledge" pattern to be learned
    k = np.fft.fftfreq(size) * 2*np.pi
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    k_mag = np.sqrt(kx**2 + ky**2 + kz**2)
    
    # Target = Gaussian in k-space (specific concept)
    F_target = np.exp(-k_mag**2 / (2*0.5**2)) * np.exp(1j * np.pi/4)
    F_target = F_target.astype(np.complex128)
    
    # Learning parameters
    omega = k_mag
    gamma = 0.005
    dt = 0.02
    T = 0.01  # Thermal noise
    exposure_strength = 0.1  # How strongly pattern is presented
    
    coherence_history = []
    
    print("Learning simulation: Repeated exposure to pattern")
    
    for epoch in range(10):  # 10 learning epochs
        for step in range(200):  # 200 steps per epoch
            # Natural evolution
            F_k *= np.exp(-1j*omega*dt - gamma*dt)
            
            # Exposure to target pattern (learning input)
            F_k += exposure_strength * F_target * dt
            
            # Thermal noise
            noise = T * (np.random.randn(*F_k.shape) + 
                        1j*np.random.randn(*F_k.shape))
            F_k += noise
            
            # Amplitude constraint (creates phase-locking)
            f_x = np.fft.ifftn(F_k)
            if np.max(np.abs(f_x)) > 4.0:
                violation = np.abs(f_x) > 4.0
                violation_k = np.fft.fftn(violation.astype(float))
                F_k *= np.exp(-0.2 * np.abs(violation_k))
        
        # Measure learning progress
        overlap = np.sum(np.conj(F_k) * F_target)
        coherence = np.abs(overlap) / (np.linalg.norm(F_k) * 
                                       np.linalg.norm(F_target) + 1e-30)
        coherence_history.append(coherence)
        
        print(f"Epoch {epoch+1}: Coherence with target = {coherence:.6f}")
    
    return coherence_history

# Run
coherences = simulate_learning()
print(f"\nLearning complete. Final coherence: {coherences[-1]:.6f}")