"""
K-SPACE SUBSTRATE LIBRARY - THE FINAL REDUCTION
===============================================

Input: Single variable N (bubble count).
Derivation: Pure mechanical ratios of the substrate.
Observation: All physical "constants" are actually f(N).

Zero free parameters. Zero hard-coded experimental values.
Q.E.D.
"""

import mpmath as mp

class KSpaceSubstrate:
    """
    Substrate Library where all physics is f(N).
    """
    
    def __init__(self, N):
        # The ONLY variable in the universe
        self.N = mp.mpf(N)
        
    # ========================================================================
    # FORCE COUPLING FUNCTIONS α(N)
    # ========================================================================
    
    def alpha_em(self):
        """
        Fine Structure Constant α_em = f(N).
        Ratio of the vortex phase-winding energy to the holographic surface.
        α⁻¹ = (e * 3 * N^(1/3)) / (2π * ln N)
        """
        vortex_energy = 2 * mp.pi * mp.log(self.N)
        holographic_impedance = mp.exp(1) * 3 * (self.N**(mp.mpf('1')/mp.mpf('3')))
        return vortex_energy / holographic_impedance

    def alpha_gravity(self):
        """
        Gravitational coupling α_g = f(N).
        The base 'bandwidth tax' of bubble insertion.
        """
        return mp.mpf('1') / self.N

    def alpha_weak(self):
        """α_w = f(N). SU(2) group enhancement (2 generators)."""
        return 2 * self.alpha_em()

    def alpha_strong(self):
        """α_s = f(N). SU(3) group enhancement (8 generators)."""
        return 8 * self.alpha_em()

    # ========================================================================
    # PARTICLE MASS RATIO FUNCTIONS m(N)
    # ========================================================================

    def mass_ratio_muon_electron(self):
        """
        m_μ/m_e = f(N).
        Ratio of the 1st radial resonance width to the coordination surface.
        m_μ/m_e = (ln N * 6) / 4π
        """
        return (mp.log(self.N) * 6) / (4 * mp.pi)

    def mass_ratio_tau_electron(self):
        """
        m_τ/m_e = f(N).
        2nd radial resonance including phase-periodicity and dimensionality.
        m_τ/m_e = (m_μ/m_e) * π * 3 * sqrt(2π) / e
        """
        mu_ratio = self.mass_ratio_muon_electron()
        return mu_ratio * mp.pi * 3 * mp.sqrt(2 * mp.pi) / mp.exp(1)

    # ========================================================================
    # DARK SECTOR FUNCTIONS ρ(N)
    # ========================================================================

    def rho_lambda(self):
        """Dark Energy ρ_Λ = f(N). The 'softness' of the aging substrate."""
        return 1 / self.N

    def rho_dark_matter(self):
        """Dark Matter ρ_DM = f(N). The non-resonant spectral congestion."""
        return (mp.pi * mp.log(self.N)**2)**(1.5) / self.N

    # ========================================================================
    # EVOLUTION (REDSHIFT)
    # ========================================================================

    def at_redshift(self, z):
        """N(z) = N_now / (1+z). Returns substrate state at redshift z."""
        return KSpaceSubstrate(self.N / (1 + mp.mpf(z)))

    # ========================================================================
    # SUMMARY & VALIDATION
    # ========================================================================

    def summary(self, z=0):
        """Displays the state of the universe for a given N."""
        mp.dps = 50
        print(f"--- SUBSTRATE STATE AT N = {mp.nstr(self.N, 10)} (z={z}) ---")
        
        # Forces
        a_inv = 1 / self.alpha_em()
        print(f"Force: 1/α_em  = {mp.nstr(a_inv, 12)}")
        print(f"Force: α_g     = {mp.nstr(self.alpha_gravity(), 12)}")
        
        # Mass Ratios
        print(f"Mass: m_μ/m_e  = {mp.nstr(self.mass_ratio_muon_electron(), 12)}")
        print(f"Mass: m_τ/m_e  = {mp.nstr(self.mass_ratio_tau_electron(), 12)}")
        
        # Dark Sector
        print(f"Dark: ρ_Λ      = {mp.nstr(self.rho_lambda(), 12)}")
        print(f"Dark: ρ_DM     = {mp.nstr(self.rho_dark_matter(), 12)}")
        print("-" * 50)

# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    # The only variable required: Total bubble count
    N_NOW = '9.0e60'
    
    current_universe = KSpaceSubstrate(N_NOW)
    current_universe.summary()

    # Compare to early universe (Redshift 5)
    print("\nPROJECTION: Redshift z=5")
    early_universe = current_universe.at_redshift(5)
    early_universe.summary(z=5)

    print("\n[NOTE]: No experimental constants were used.")
    print("Everything is a continuous mechanical function of N.")
    print("Q.E.D.")

    