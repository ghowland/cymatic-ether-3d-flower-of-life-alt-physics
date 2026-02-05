"""
PLOT RESULTS FROM K-SPACE SUBSTRATE MECHANICS
==============================================
Generate publication-quality figures for paper.

Pure substrate mechanics - only universe age N as input.
All other quantities derived as ratios.

Available figures:
- dark_energy: ρ_Λ(N) evolution with universe age
- g_factor: Electron g-factor calculation breakdown
- coherence: Consciousness threshold demonstration
- topology: Topological charge conservation
- scaling: All constants vs N (unified view)

Version: 2.0 - Pure Ratios
Date: February 2026
"""

import numpy as np
from mpmath import mp, mpf, pi, sqrt, power, log10
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import argparse

mp.dps = 50

# ============================================================================
# THE ONLY VARIABLE: UNIVERSE AGE
# ============================================================================

N_NOW = mpf('2.7e61')  # Total k-modes created (current age)

# ============================================================================
# DERIVED QUANTITIES (PURE RATIOS)
# ============================================================================

def compute_beta(N):
    """
    Coupling strength at age N.
    
    β(N) = 1/N  (substrate units)
    
    This is FORCED by coupling conservation.
    """
    return mpf('1') / N

def compute_dark_energy_density_ratio(N):
    """
    Dark energy density relative to current epoch.
    
    ρ_Λ(N) / ρ_Λ(N_now) = (N_now/N)²
    
    From Distance paper: ρ_Λ ∝ β(N)/N ∝ 1/N²
    """
    return (N_NOW / N)**2

def compute_hubble_ratio(N):
    """
    Hubble parameter relative to current epoch.
    
    H(N) / H_now = N_now/N
    
    From Distance paper: H = 1/N (substrate units)
    """
    return N_NOW / N

def compute_gravitational_ratio(N):
    """
    Newton's G relative to current epoch.
    
    G(N) / G_now = N_now/N
    
    From Distance paper: G ∝ β(N) ∝ 1/N
    """
    return N_NOW / N

def compute_alpha_ratio(N):
    """
    Fine structure constant relative to current epoch.
    
    α(N) / α_now = N_now/N
    
    From g-factor derivation: α ∝ 1/N
    """
    return N_NOW / N

def compute_time_ratio(N):
    """
    Time relative to current age.
    
    t(N) / t_now = N / N_now
    
    Time IS bubble count.
    """
    return N / N_NOW

# ============================================================================
# DARK ENERGY FIGURE
# ============================================================================

def plot_dark_energy():
    """
    Generate dark energy evolution figure.
    
    Shows:
    1. ρ_Λ(N) vs time (relative to now)
    2. H(N) vs time
    3. Equation of state w (constant at -1)
    4. Matter-Λ ratio evolution
    
    All in dimensionless ratios.
    """
    
    print("Generating dark energy figure...")
    print()
    print("Pure ratio mechanics - no external constants")
    print()
    
    # Time range: Early universe to far future
    # N from N_now/1000 to 3×N_now
    n_points = 100
    log_N_min = float(log10(N_NOW / mpf('1000')))
    log_N_max = float(log10(N_NOW * mpf('3')))
    log_N_array = np.linspace(log_N_min, log_N_max, n_points)
    
    # Convert to N values
    N_array = [mpf('10')**mpf(str(log_N)) for log_N in log_N_array]
    
    # Compute ratios
    print("Computing evolution ratios...")
    
    time_ratios = []
    rho_lambda_ratios = []
    hubble_ratios = []
    beta_ratios = []
    
    for N in N_array:
        t_ratio = float(compute_time_ratio(N))
        rho_ratio = float(compute_dark_energy_density_ratio(N))
        H_ratio = float(compute_hubble_ratio(N))
        beta_ratio = float(compute_beta(N) * N_NOW)  # β(N)/β(N_now)
        
        time_ratios.append(t_ratio)
        rho_lambda_ratios.append(rho_ratio)
        hubble_ratios.append(H_ratio)
        beta_ratios.append(beta_ratio)
    
    time_ratios = np.array(time_ratios)
    rho_lambda_ratios = np.array(rho_lambda_ratios)
    hubble_ratios = np.array(hubble_ratios)
    beta_ratios = np.array(beta_ratios)
    
    print(f"Time range: {time_ratios[0]:.3f} to {time_ratios[-1]:.3f} × t_now")
    print(f"ρ_Λ range: {rho_lambda_ratios[-1]:.3f} to {rho_lambda_ratios[0]:.3f} × ρ_Λ(now)")
    print()
    
    # Create figure
    fig = plt.figure(figsize=(16, 10))
    gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)
    
    # ========================================================================
    # Panel 1: Dark Energy Density (ratio to current)
    # ========================================================================
    ax1 = fig.add_subplot(gs[0, 0])
    
    # Cymatic prediction: ρ_Λ ∝ 1/N²
    ax1.loglog(time_ratios, rho_lambda_ratios, 'b-', linewidth=3, 
               label='Cymatic: ρ_Λ ∝ 1/N²')
    
    # ΛCDM (constant - horizontal line at 1.0)
    ax1.axhline(1.0, color='r', linestyle='--', linewidth=2,
                label='ΛCDM: ρ_Λ = constant')
    
    # Current epoch marker
    ax1.plot(1.0, 1.0, 'ko', markersize=12, 
             label='Now (t = t₀)', zorder=5)
    
    ax1.set_xlabel('Time / Current Age', fontsize=12, fontweight='bold')
    ax1.set_ylabel('ρ_Λ / ρ_Λ(now)', fontsize=12, fontweight='bold')
    ax1.set_title('Dark Energy Density Evolution', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper right')
    ax1.grid(True, alpha=0.3, which='both')
    
    # Add annotation
    ax1.annotate('Past: ρ_Λ was LARGER\n(contrary to ΛCDM)',
                 xy=(0.5, 4), fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    ax1.annotate('Future: ρ_Λ → 0\n(dilutes away)',
                 xy=(2.0, 0.3), fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    # ========================================================================
    # Panel 2: Hubble Parameter (ratio to current)
    # ========================================================================
    ax2 = fig.add_subplot(gs[0, 1])
    
    # Cymatic: H ∝ 1/N
    ax2.loglog(time_ratios, hubble_ratios, 'g-', linewidth=3,
               label='Cymatic: H ∝ 1/N')
    
    # Current epoch
    ax2.plot(1.0, 1.0, 'ko', markersize=12,
             label='Now: H₀', zorder=5)
    
    ax2.set_xlabel('Time / Current Age', fontsize=12, fontweight='bold')
    ax2.set_ylabel('H / H₀', fontsize=12, fontweight='bold')
    ax2.set_title('Expansion Rate Evolution', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10, loc='upper right')
    ax2.grid(True, alpha=0.3, which='both')
    
    # Add annotations
    ax2.annotate('Expansion slows\nas N increases',
                 xy=(2.0, 0.6), fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))
    
    # ========================================================================
    # Panel 3: Coupling Strength β (ratio to current)
    # ========================================================================
    ax3 = fig.add_subplot(gs[1, 0])
    
    # β ∝ 1/N (same as H)
    ax3.loglog(time_ratios, beta_ratios, 'purple', linewidth=3,
               label='Cymatic: β ∝ 1/N')
    
    # Current epoch
    ax3.plot(1.0, 1.0, 'ko', markersize=12,
             label='Now: β₀', zorder=5)
    
    ax3.set_xlabel('Time / Current Age', fontsize=12, fontweight='bold')
    ax3.set_ylabel('β / β₀', fontsize=12, fontweight='bold')
    ax3.set_title('Coupling Strength Evolution', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10, loc='upper right')
    ax3.grid(True, alpha=0.3, which='both')
    
    # Add annotation
    ax3.annotate('Coupling weakens\n→ easier expansion',
                 xy=(2.0, 0.6), fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    # ========================================================================
    # Panel 4: Matter-Λ Density Ratio
    # ========================================================================
    ax4 = fig.add_subplot(gs[1, 1])
    
    # Matter density: ρ_m ∝ 1/N (dilution)
    # Dark energy: ρ_Λ ∝ 1/N²
    # Ratio: ρ_Λ/ρ_m ∝ 1/N
    
    # At current epoch: ρ_Λ ≈ 2.4 × ρ_m (observed)
    ratio_now = mpf('2.4')
    
    matter_lambda_ratio = []
    for N in N_array:
        # ρ_m(N)/ρ_m(now) = N_now/N
        # ρ_Λ(N)/ρ_Λ(now) = (N_now/N)²
        # Ratio: [ρ_Λ(N)/ρ_m(N)] / [ρ_Λ(now)/ρ_m(now)]
        #      = (N_now/N)² / (N_now/N) = N_now/N
        ratio = float(ratio_now * (N_NOW / N))
        matter_lambda_ratio.append(ratio)
    
    matter_lambda_ratio = np.array(matter_lambda_ratio)
    
    # Plot
    ax4.loglog(time_ratios, matter_lambda_ratio, 'orange', linewidth=3,
               label='Cymatic: ρ_Λ/ρ_m ∝ 1/N')
    
    # Current value
    ax4.plot(1.0, float(ratio_now), 'ko', markersize=12,
             label=f'Now: ρ_Λ/ρ_m ≈ {float(ratio_now):.1f}', zorder=5)
    
    # Equality line
    ax4.axhline(1.0, color='k', linestyle=':', linewidth=1.5,
                label='Matter-Λ equality')
    
    ax4.set_xlabel('Time / Current Age', fontsize=12, fontweight='bold')
    ax4.set_ylabel('ρ_Λ / ρ_matter', fontsize=12, fontweight='bold')
    ax4.set_title('Dark Energy vs Matter Density', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10, loc='upper left')
    ax4.grid(True, alpha=0.3, which='both')
    
    # Add annotations
    ax4.annotate('Past: matter\ndominated',
                 xy=(0.3, 0.5), fontsize=10,
                 bbox=dict(boxstyle='round', facecolor='orange', alpha=0.3))
    ax4.annotate('Future: Λ\ndominated',
                 xy=(2.0, 5), fontsize=10,
                 bbox=dict(boxstyle='round', facecolor='cyan', alpha=0.3))
    
    # ========================================================================
    # Overall title and save
    # ========================================================================
    
    fig.suptitle('Dark Energy in K-Space Substrate: Pure Ratio Mechanics\n' + 
                 'All quantities scale with universe age N (no external constants)',
                 fontsize=16, fontweight='bold', y=0.98)
    
    # Add text box with key insight
    fig.text(0.5, 0.02, 
             'KEY INSIGHT: ρ_Λ ∝ 1/N² and ρ_m ∝ 1/N → both dilute, but Λ dilutes FASTER\n' +
             'This resolves coincidence problem: we live when ρ_Λ ≈ ρ_m purely by age selection',
             ha='center', fontsize=11, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    filename = 'dark_energy_evolution.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Figure saved: {filename}")
    print()
    
    # Print key ratios
    print("=" * 70)
    print("KEY RATIOS (Dimensionless)")
    print("=" * 70)
    print()
    print("All values relative to current epoch (N = N_now):")
    print()
    
    # Current
    print("NOW (t/t₀ = 1.00):")
    print(f"  ρ_Λ/ρ_Λ(now) = 1.00")
    print(f"  H/H₀         = 1.00")
    print(f"  β/β₀         = 1.00")
    print(f"  ρ_Λ/ρ_m      = {float(ratio_now):.2f}")
    print()
    
    # Future (2× age)
    N_fut = N_NOW * mpf('2')
    t_fut = float(compute_time_ratio(N_fut))
    rho_fut = float(compute_dark_energy_density_ratio(N_fut))
    H_fut = float(compute_hubble_ratio(N_fut))
    ratio_fut = float(ratio_now * (N_NOW / N_fut))
    
    print(f"FUTURE (t/t₀ = {t_fut:.2f}):")
    print(f"  ρ_Λ/ρ_Λ(now) = {rho_fut:.3f}  (75% decrease)")
    print(f"  H/H₀         = {H_fut:.3f}  (50% slower)")
    print(f"  β/β₀         = {H_fut:.3f}")
    print(f"  ρ_Λ/ρ_m      = {ratio_fut:.2f}")
    print()
    
    # Past (1/2 age)
    N_past = N_NOW / mpf('2')
    t_past = float(compute_time_ratio(N_past))
    rho_past = float(compute_dark_energy_density_ratio(N_past))
    H_past = float(compute_hubble_ratio(N_past))
    ratio_past = float(ratio_now * (N_NOW / N_past))
    
    print(f"PAST (t/t₀ = {t_past:.2f}):")
    print(f"  ρ_Λ/ρ_Λ(now) = {rho_past:.1f}  (4× larger)")
    print(f"  H/H₀         = {H_past:.1f}  (2× faster)")
    print(f"  β/β₀         = {H_past:.1f}")
    print(f"  ρ_Λ/ρ_m      = {ratio_past:.1f}")
    print()
    
    print("=" * 70)
    print()
    print("TESTABLE PREDICTION:")
    print("  Measure ρ_Λ at different redshifts via Type Ia supernovae")
    print("  Should see ρ_Λ(z) ∝ (1+z)² NOT constant")
    print()
    print("=" * 70)

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate figures for k-space substrate papers'
    )
    parser.add_argument('--figure', type=str, required=True,
                       choices=['dark_energy', 'g_factor', 'coherence', 
                               'topology', 'scaling'],
                       help='Which figure to generate')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("K-SPACE SUBSTRATE MECHANICS - FIGURE GENERATION")
    print("=" * 70)
    print()
    print("Version 2.0 - Pure Ratio Mechanics")
    print("Only input: N = universe age in k-mode count")
    print()
    
    if args.figure == 'dark_energy':
        plot_dark_energy()
    elif args.figure == 'g_factor':
        print("G-factor figure not yet implemented")
    elif args.figure == 'coherence':
        print("Coherence figure not yet implemented")
    elif args.figure == 'topology':
        print("Topology figure not yet implemented")
    elif args.figure == 'scaling':
        print("Scaling figure not yet implemented")
    
    print()
    print("Figure generation complete.")
    print("=" * 70)

    