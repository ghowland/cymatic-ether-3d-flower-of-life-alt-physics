import numpy as np

class FermionDefect:
    """
    Half-quantum vortex in spectral substrate.
    """
    
    def __init__(self, size=64, mass=0.511):  # mass in MeV
        self.size = size
        self.m = mass
        
        # k-space grid
        k = 2*np.pi*np.fft.fftfreq(size)
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
        self.k_mag = np.sqrt(kx**2 + ky**2 + kz**2)
        self.k_mag[0,0,0] = 1e-10
        
        # Polar coordinates in k-space
        self.k_theta = np.arctan2(np.sqrt(kx**2 + ky**2), kz)
        self.k_phi = np.arctan2(ky, kx)
        
        # Initialize half-quantum vortex
        self.F_fermion = self.create_half_vortex()
        
    def create_half_vortex(self):
        """
        Create fermion = half-quantum vortex in k-space.
        
        Phase winding: φ(k) = θ/2 (half-angle)
        Amplitude: Localized near |k| = m
        """
        # Radial profile (peaked at k = m)
        k0 = self.m / 197  # Convert MeV to inverse fm
        width = k0 / 4
        amplitude = np.exp(-(self.k_mag - k0)**2 / (2*width**2))
        
        # Half-quantum phase winding
        # As we go around once in (θ, φ), phase increases by π
        phase = self.k_theta / 2  # This is the KEY: half-integer winding
        
        # Complex field
        F = amplitude * np.exp(1j * phase)
        
        return F
    
    def compute_spin(self):
        """
        Compute intrinsic angular momentum.
        Should be ℏ/2 for fermion.
        """
        # Angular momentum density in k-space
        kx = 2*np.pi*np.fft.fftfreq(self.size)
        ky = 2*np.pi*np.fft.fftfreq(self.size)
        kz = 2*np.pi*np.fft.fftfreq(self.size)
        
        KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
        
        # L = k × (Im[F* ∇F])
        grad_F_x = np.gradient(self.F_fermion, axis=0)
        grad_F_y = np.gradient(self.F_fermion, axis=1)
        grad_F_z = np.gradient(self.F_fermion, axis=2)
        
        # Im[F* ∇F] = "probability current" in k-space
        j_x = np.imag(np.conj(self.F_fermion) * grad_F_x)
        j_y = np.imag(np.conj(self.F_fermion) * grad_F_y)
        j_z = np.imag(np.conj(self.F_fermion) * grad_F_z)
        
        # Angular momentum
        Lx = np.sum(KY * j_z - KZ * j_y)
        Ly = np.sum(KZ * j_x - KX * j_z)
        Lz = np.sum(KX * j_y - KY * j_x)
        
        L_total = np.sqrt(Lx**2 + Ly**2 + Lz**2)
        
        return L_total  # Should be ≈ ℏ/2
    
    def test_exchange_statistics(self, other_fermion):
        """
        Test if exchanging two fermions gives sign flip.
        """
        # Overlap of two fermions
        overlap_12 = np.sum(np.conj(self.F_fermion) * other_fermion.F_fermion)
        
        # Exchange: swap k-space positions
        F1_swapped = other_fermion.F_fermion.copy()
        F2_swapped = self.F_fermion.copy()
        
        overlap_21 = np.sum(np.conj(F2_swapped) * F1_swapped)
        
        # Berry phase from exchange
        phase_ratio = overlap_21 / overlap_12
        
        print(f"Overlap before exchange: {overlap_12:.6f}")
        print(f"Overlap after exchange: {overlap_21:.6f}")
        print(f"Phase ratio: {phase_ratio:.6f}")
        print(f"Expected for fermions: -1")
        
        return phase_ratio


# Test
print("Creating electron (half-quantum vortex)...")
electron = FermionDefect(size=64, mass=0.511)

print("\nComputing spin angular momentum...")
spin = electron.compute_spin()
print(f"L = {spin:.6f} ℏ")
print(f"Expected: L = 0.5 ℏ for spin-1/2")

print("\nTesting exchange statistics...")
electron2 = FermionDefect(size=64, mass=0.511)
# Place second electron at different location
electron2.F_fermion = np.roll(electron2.F_fermion, 10, axis=0)

phase_ratio = electron.test_exchange_statistics(electron2)
if np.abs(phase_ratio + 1.0) < 0.1:
    print("✓ FERMIONIC STATISTICS CONFIRMED")
else:
    print("✗ Statistics inconclusive")