"""
Generate Standard Model vs K-Space Substrate comparison table in Excel format.

Creates comprehensive comparison across all parameters, predictions, and frameworks.
"""

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows

# ============================================================================
# DATA: PARAMETER COMPARISON
# ============================================================================

def create_parameter_comparison():
    """Standard Model parameters vs K-Space derivation."""
    
    data = {
        'Parameter': [
            'Electron mass (m_e)',
            'Muon mass (m_μ)',
            'Tau mass (m_τ)',
            'Up quark mass (m_u)',
            'Down quark mass (m_d)',
            'Charm quark mass (m_c)',
            'Strange quark mass (m_s)',
            'Top quark mass (m_t)',
            'Bottom quark mass (m_b)',
            'Electron coupling (α)',
            'Weak coupling (g_W)',
            'Strong coupling (g_S)',
            'Higgs VEV (v)',
            'Higgs mass (m_H)',
            'CKM angle θ₁₂',
            'CKM angle θ₁₃',
            'CKM angle θ₂₃',
            'CKM phase δ',
            'Neutrino Δm²₂₁',
            'Neutrino Δm²₃₁',
            'Cosmological constant (Λ)',
            'Newton constant (G)',
            'Planck constant (ℏ)',
            'Speed of light (c)',
            'Electric constant (ε₀)'
        ],
        
        'Standard Model Value': [
            '0.511 MeV',
            '105.66 MeV',
            '1776.86 MeV',
            '2.2 MeV',
            '4.7 MeV',
            '1.28 GeV',
            '95 MeV',
            '173.1 GeV',
            '4.18 GeV',
            '1/137.036',
            '0.653',
            '1.221 (at m_Z)',
            '246 GeV',
            '125.1 GeV',
            '13.04°',
            '0.201°',
            '2.38°',
            '1.20',
            '7.53×10⁻⁵ eV²',
            '2.453×10⁻³ eV²',
            '~10⁻⁵² m⁻²',
            '6.67430×10⁻¹¹ m³/kg/s²',
            '1.05457×10⁻³⁴ J·s',
            '299792458 m/s',
            '8.854×10⁻¹² F/m'
        ],
        
        'SM Status': [
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured',
            'Measured (ρ_Λ)',
            'Measured',
            'Defined',
            'Defined',
            'Derived'
        ],
        
        'K-Space Substrate': [
            'Q=+1 vortex, r_core=√N modes',
            'Q=+1, different topology',
            'Q=+1, higher winding',
            'Q=+1/3, color topology',
            'Q=-1/3, color topology',
            'Q=+1/3, excited state',
            'Q=-1/3, excited state',
            'Q=+1/3, highest mass state',
            'Q=-1/3, heavy state',
            'α(N) = α₀(N₀/N)',
            'β_I/β_spatial (coupling ratio)',
            'β_c/β_spatial (coupling ratio)',
            'Average k-mode occupation',
            'Condensate energy density',
            'Topology angle',
            'Topology angle',
            'Topology angle',
            'Phase winding',
            'Mode splitting',
            'Mode splitting',
            'ρ_Λ(N) = β(N)/N ∝ 1/N²',
            'G(N) = c⁴R²_max/(8πβN)',
            '1 mode occupation (substrate unit)',
            '1 bubble/t_P (substrate unit)',
            'Substrate permittivity'
        ],
        
        'K-Space Status': [
            'Derived (4 decimals)',
            'Topology TBD',
            'Topology TBD',
            'Topology TBD',
            'Topology TBD',
            'Topology TBD',
            'Topology TBD',
            'Topology TBD',
            'Topology TBD',
            'Derived (evolves)',
            'Derived (ratio)',
            'Derived (ratio)',
            'Derived',
            'Derived',
            'Topological',
            'Topological',
            'Topological',
            'Topological',
            'Topological',
            'Topological',
            'Derived (testable)',
            'Derived (matches)',
            'Substrate unit',
            'Substrate unit',
            'Substrate unit'
        ]
    }
    
    return pd.DataFrame(data)

# ============================================================================
# DATA: PREDICTIONS COMPARISON
# ============================================================================

def create_predictions_comparison():
    """Testable predictions comparison."""
    
    data = {
        'Observable': [
            'Dark energy density ρ_Λ(z)',
            'Fine structure α(z)',
            'Newton constant G(t)',
            'Electron g-factor drift',
            'Entanglement fidelity vs path',
            'Brain coherence C',
            'Higgs mass',
            'Proton decay',
            'Neutrino masses',
            'Graviton',
            'Dark matter particle',
            'Black hole singularity',
            'Big Bang singularity',
            'Cosmic inflation',
            'Quantum gravity scale'
        ],
        
        'Standard Model Prediction': [
            'Constant (Λ)',
            'Constant (exactly)',
            'Constant (exactly)',
            'Constant (exactly)',
            'Independent of path',
            'Not addressed',
            'Not predicted (measured)',
            'Possible (GUT scale)',
            '0 (massless)',
            'Required for QG',
            'Requires BSM physics',
            'r→0 density→∞',
            't→0 density→∞',
            'Requires inflaton field',
            'E_Planck ~ 10¹⁹ GeV'
        ],
        
        'K-Space Prediction': [
            'ρ_Λ ∝ (1+z)²',
            'α ∝ (1+z)',
            'G ∝ 1/N',
            'dg/dt ∝ -1/t',
            'F ∝ exp(-curvature)',
            'C > 0.999 when conscious',
            'Condensate density (derived)',
            'Impossible (Q conserved)',
            'Non-zero (mode splitting)',
            'Not needed (β variation)',
            'Topological defect',
            'Minimum 1 mode (finite)',
            'N=1 (finite)',
            'Early high β (derived)',
            'k_max = 1/l_P (discrete)'
        ],
        
        'Test Method': [
            'High-z supernovae',
            'Quasar absorption spectra',
            'Lunar laser ranging',
            'Ultra-precision measurements',
            'Curved vs straight path EPR',
            'EEG/MEG phase coherence',
            'LHC measurements',
            'Proton decay experiments',
            'Neutrino oscillations',
            'Gravitational wave detection',
            'Direct detection experiments',
            'Event horizon observations',
            'CMB observations',
            'CMB power spectrum',
            'Planck-scale experiments'
        ],
        
        'Timeline': [
            '2025-2045 (Euclid, Rubin)',
            '2026-2035 (existing data)',
            '2050-2100 (long baseline)',
            '2040+ (precision tech)',
            '2026-2030 (feasible now)',
            '2026+ (technology exists)',
            'Ongoing (LHC)',
            'Ongoing (Super-K, etc.)',
            'Confirmed (matches)',
            'Ongoing (LIGO/Virgo)',
            'Ongoing (LUX, Xenon)',
            'Ongoing (EHT)',
            'Complete (WMAP, Planck)',
            'Complete (Planck satellite)',
            'Far future (>2100)'
        ],
        
        'Current Status': [
            'Testable soon',
            'Testable now',
            'Need precision',
            'Need precision',
            'Testable now',
            'Testable now',
            'Measured',
            'No decay observed',
            'Confirmed non-zero',
            'Waves detected',
            'Not detected',
            'No singularity seen',
            'Unknown',
            'Observed',
            'Inaccessible'
        ]
    }
    
    return pd.DataFrame(data)

# ============================================================================
# DATA: FRAMEWORK COMPARISON
# ============================================================================

def create_framework_comparison():
    """Overall framework comparison."""
    
    data = {
        'Feature': [
            'Free parameters',
            'Fundamental entities',
            'Spacetime',
            'Gravity mechanism',
            'Quantum mechanics',
            'Particle origin',
            'Force unification',
            'Dark energy',
            'Dark matter',
            'Consciousness',
            'Measurement problem',
            'Wave-particle duality',
            'Entanglement',
            'Singularities',
            'UV divergences',
            'Computational',
            'Falsifiable',
            'Testable predictions',
            'Mathematical maturity',
            'Experimental validation'
        ],
        
        'Standard Model': [
            '19 (+ 6 for Λ,ν)',
            'Quantum fields on spacetime',
            'Continuous background',
            'Outside SM (requires GR)',
            'Fundamental (Copenhagen)',
            'Field excitations',
            'Partial (EM+Weak)',
            'Λ (ad hoc constant)',
            'Requires new particles',
            'Not addressed',
            'Interpretation-dependent',
            'Complementarity principle',
            'Non-local correlation',
            'Present (r→0, t→0)',
            'Require renormalization',
            'QFT (difficult)',
            'Very flexible',
            'Many (confirmed)',
            'Very mature (50+ years)',
            'Extensive (13+ decimals)'
        ],
        
        'K-Space Substrate': [
            '0 (in substrate units)',
            'Discrete k-modes',
            'Emergent (bubble count)',
            'Coupling variation β(x)',
            'Emergent (discrete→continuum)',
            'Topological defects',
            'Complete (all gradients)',
            'Derived: ρ_Λ ∝ 1/N²',
            'Topological defects',
            'C > 0.999 (mechanical)',
            'Observer coupling (mechanical)',
            'No duality (k-mode patterns)',
            'K-space correlation (local)',
            'None (discrete minimum)',
            'None (finite modes)',
            'Discrete (easy)',
            'Clear predictions',
            '5 major tests',
            'Young (2025-2026)',
            'Limited (4-11 decimals)'
        ],
        
        'String Theory': [
            '~10⁵⁰⁰ (landscape)',
            '1D strings in 10-11D',
            '10-11 dimensions',
            'Graviton exchange',
            'String vibrations',
            'Vibrational modes',
            'Complete (claimed)',
            'Anthropic landscape',
            'Lightest SUSY particle',
            'Not addressed',
            'String measurement',
            'String/particle correspondence',
            'String connections',
            'Resolved (string scale)',
            'Finite (string theory)',
            'Extremely difficult',
            'Very difficult',
            'Few (no unique predictions)',
            'Mature (40+ years)',
            'None (no tests)'
        ],
        
        'Loop Quantum Gravity': [
            'Several',
            'Spin networks',
            'Discrete (spin foam)',
            'Emergent (network geometry)',
            'Background independent',
            'Network excitations',
            'Gravity only',
            'Not addressed',
            'Not addressed',
            'Not addressed',
            'Spin network collapse',
            'Not clear',
            'Not clear',
            'Resolved (discrete)',
            'Finite (discrete)',
            'Difficult',
            'Testable in principle',
            'Few (Planck scale)',
            'Mature (30+ years)',
            'None (too high energy)'
        ]
    }
    
    return pd.DataFrame(data)

# ============================================================================
# EXCEL GENERATION
# ============================================================================

def create_excel_workbook():
    """Generate complete Excel comparison workbook."""
    
    wb = Workbook()
    
    # Remove default sheet
    wb.remove(wb.active)
    
    # Create sheets
    ws1 = wb.create_sheet("Parameters")
    ws2 = wb.create_sheet("Predictions")
    ws3 = wb.create_sheet("Frameworks")
    ws4 = wb.create_sheet("Summary")
    
    # Style definitions
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True, size=11)
    
    k_space_fill = PatternFill(start_color="E7F4E4", end_color="E7F4E4", fill_type="solid")
    sm_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
    
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # ========================================================================
    # SHEET 1: Parameters
    # ========================================================================
    
    df1 = create_parameter_comparison()
    
    for r_idx, row in enumerate(dataframe_to_rows(df1, index=False, header=True), 1):
        for c_idx, value in enumerate(row, 1):
            cell = ws1.cell(row=r_idx, column=c_idx, value=value)
            cell.border = border
            cell.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
            
            if r_idx == 1:  # Header
                cell.fill = header_fill
                cell.font = header_font
            elif c_idx == 3:  # SM Status column
                cell.fill = sm_fill
            elif c_idx == 5:  # K-Space Status column
                cell.fill = k_space_fill
    
    # Column widths
    ws1.column_dimensions['A'].width = 25
    ws1.column_dimensions['B'].width = 20
    ws1.column_dimensions['C'].width = 15
    ws1.column_dimensions['D'].width = 35
    ws1.column_dimensions['E'].width = 20
    
    # ========================================================================
    # SHEET 2: Predictions
    # ========================================================================
    
    df2 = create_predictions_comparison()
    
    for r_idx, row in enumerate(dataframe_to_rows(df2, index=False, header=True), 1):
        for c_idx, value in enumerate(row, 1):
            cell = ws2.cell(row=r_idx, column=c_idx, value=value)
            cell.border = border
            cell.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
            
            if r_idx == 1:
                cell.fill = header_fill
                cell.font = header_font
    
    ws2.column_dimensions['A'].width = 25
    ws2.column_dimensions['B'].width = 25
    ws2.column_dimensions['C'].width = 30
    ws2.column_dimensions['D'].width = 30
    ws2.column_dimensions['E'].width = 25
    ws2.column_dimensions['F'].width = 20
    
    # ========================================================================
    # SHEET 3: Frameworks
    # ========================================================================
    
    df3 = create_framework_comparison()
    
    for r_idx, row in enumerate(dataframe_to_rows(df3, index=False, header=True), 1):
        for c_idx, value in enumerate(row, 1):
            cell = ws3.cell(row=r_idx, column=c_idx, value=value)
            cell.border = border
            cell.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
            
            if r_idx == 1:
                cell.fill = header_fill
                cell.font = header_font
    
    ws3.column_dimensions['A'].width = 25
    ws3.column_dimensions['B'].width = 30
    ws3.column_dimensions['C'].width = 30
    ws3.column_dimensions['D'].width = 30
    ws3.column_dimensions['E'].width = 30
    
    # ========================================================================
    # SHEET 4: Summary
    # ========================================================================
    
    summary_data = [
        ['Comparison Summary', '', '', ''],
        ['', '', '', ''],
        ['Category', 'Standard Model', 'K-Space Substrate', 'Advantage'],
        ['Free Parameters', '19-25', '0 (substrate units)', 'K-Space'],
        ['Predictive Power', 'Measured inputs', 'Derived outputs', 'K-Space'],
        ['Gravity Included', 'No (requires GR)', 'Yes (unified)', 'K-Space'],
        ['Dark Energy', 'Ad hoc Λ', 'Derived: ρ_Λ ∝ 1/N²', 'K-Space'],
        ['Consciousness', 'Not addressed', 'Derived: C > 0.999', 'K-Space'],
        ['UV Divergences', 'Require renormalization', 'None (finite modes)', 'K-Space'],
        ['Experimental Validation', '13+ decimals, 50+ years', '4-11 decimals, new', 'SM'],
        ['Mathematical Maturity', 'Very mature', 'Young framework', 'SM'],
        ['Falsifiability', 'Difficult (flexible)', 'Clear (5 tests)', 'K-Space'],
        ['', '', '', ''],
        ['Overall Assessment', '', '', ''],
        ['', '', '', ''],
        ['Standard Model:', 'Mature, extensively tested, but incomplete', '', ''],
        ['K-Space Substrate:', 'More fundamental, testable, needs validation', '', ''],
        ['', '', '', ''],
        ['Key Insight:', 'SM is effective theory, K-Space claims deeper structure', '', ''],
    ]
    
    for r_idx, row in enumerate(summary_data, 1):
        for c_idx, value in enumerate(row, 1):
            cell = ws4.cell(row=r_idx, column=c_idx, value=value)
            
            if r_idx == 1:
                cell.font = Font(size=16, bold=True)
                cell.alignment = Alignment(horizontal='center')
            elif r_idx == 3:
                cell.fill = header_fill
                cell.font = header_font
                cell.border = border
            elif r_idx in [16, 17, 20]:
                cell.font = Font(bold=True)
            elif r_idx > 3 and r_idx < 13:
                cell.border = border
    
    ws4.column_dimensions['A'].width = 25
    ws4.column_dimensions['B'].width = 35
    ws4.column_dimensions['C'].width = 35
    ws4.column_dimensions['D'].width = 15
    
    # Merge cells for title
    ws4.merge_cells('A1:D1')
    
    return wb

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("Generating Standard Model vs K-Space Substrate comparison...")
    print()
    
    wb = create_excel_workbook()
    
    filename = 'Standard_Model_vs_K-Space_Comparison.xlsx'
    wb.save(filename)
    
    print(f"✓ Excel workbook created: {filename}")
    print()
    print("Contents:")
    print("  • Sheet 1: Parameters (25 parameters compared)")
    print("  • Sheet 2: Predictions (15 testable predictions)")
    print("  • Sheet 3: Frameworks (4 frameworks: SM, K-Space, String, LQG)")
    print("  • Sheet 4: Summary (overall assessment)")
    print()
    print("=" * 70)

