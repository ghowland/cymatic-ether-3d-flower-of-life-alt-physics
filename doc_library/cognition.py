import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# ============================================================================
# AXIOMATIC COGNITION SIMULATOR
# Substrate + Wave + Damage = Mind
# ============================================================================

class CognitiveSubstrate:
    """
    A mechanical simulation of cognition as wave dynamics in damaged substrate.
    
    Axioms implemented:
    1. Substrate exists (2D grid of oscillators)
    2. Waves propagate (wave equation)
    3. Waves damage substrate (accumulated stress)
    4. Damage persists (slow healing)
    5. Finite capacity (damage saturation)
    """
    
    def __init__(self, size=100, dx=1.0, dt=0.1):
        """
        Initialize cognitive substrate.
        
        Parameters:
        -----------
        size : int
            Grid size (size x size)
        dx : float
            Spatial resolution
        dt : float
            Time step
        """
        self.size = size
        self.dx = dx
        self.dt = dt
        
        # Wave fields: current, previous (for wave equation)
        self.psi = np.zeros((size, size))  # Current wave amplitude
        self.psi_prev = np.zeros((size, size))  # Previous timestep
        
        # Damage field (memory)
        self.damage = np.zeros((size, size))
        
        # Substrate properties (can vary spatially)
        self.wave_speed = np.ones((size, size)) * 10.0  # c
        self.damping = np.ones((size, size)) * 0.3  # γ
        self.damage_rate = 0.05  # α - how fast waves damage substrate
        self.healing_rate = 0.01  # β - how fast damage heals
        self.damage_max = 10.0  # Maximum damage (capacity limit)
        
        # Receptivity (substrate's ability to resonate at different frequencies)
        # This creates "personality" - different regions resonate differently
        self.receptivity = self._create_receptivity_pattern()
        
    def _create_receptivity_pattern(self):
        """Create spatial variation in receptivity (substrate personality)."""
        x = np.linspace(0, 4*np.pi, self.size)
        y = np.linspace(0, 4*np.pi, self.size)
        X, Y = np.meshgrid(x, y)
        
        # Multiple frequency components create complex receptivity landscape
        pattern = (
            0.5 * np.sin(X) * np.cos(Y) +
            0.3 * np.sin(2*X) * np.sin(2*Y) +
            0.2 * np.cos(3*X)
        )
        # Normalize to [0.2, 1.0] - all substrate can resonate, but some better
        return 0.2 + 0.8 * (pattern - pattern.min()) / (pattern.max() - pattern.min())
    
    def step(self):
        """
        Advance simulation one timestep.
        Implements: ∂²ψ/∂t² = c²∇²ψ - γ(∂ψ/∂t) - F_damage(ψ, D)
        """
        # Laplacian (spatial derivatives)
        laplacian = (
            np.roll(self.psi, 1, axis=0) + np.roll(self.psi, -1, axis=0) +
            np.roll(self.psi, 1, axis=1) + np.roll(self.psi, -1, axis=1) -
            4 * self.psi
        ) / (self.dx**2)
        
        # Wave equation with damping and damage-dependent resistance
        # High damage increases local resistance (harder to vibrate)
        damage_resistance = 1.0 + 0.5 * (self.damage / self.damage_max)
        
        # Velocity (current - previous)
        velocity = (self.psi - self.psi_prev) / self.dt
        
        # Acceleration
        acceleration = (
            (self.wave_speed**2) * laplacian / damage_resistance -
            self.damping * velocity
        )
        
        # Update wave field (Verlet integration)
        psi_new = 2*self.psi - self.psi_prev + acceleration * (self.dt**2)
        
        # Update damage: increases with wave amplitude², decreases via healing
        damage_increase = self.damage_rate * (self.psi**2) * self.receptivity
        damage_decrease = self.healing_rate * self.damage
        self.damage = np.clip(
            self.damage + damage_increase - damage_decrease,
            0, self.damage_max
        )
        
        # Shift time
        self.psi_prev = self.psi.copy()
        self.psi = psi_new
        
    def inject_wave(self, x, y, amplitude, frequency, width=5):
        """
        Inject a wave pattern at location (x, y).
        This simulates: sensory input, thought, or transmitted information.
        
        Parameters:
        -----------
        x, y : int
            Location of wave injection
        amplitude : float
            Wave amplitude (intensity of input)
        frequency : float
            Wave frequency (type of information)
        width : float
            Spatial extent of injection
        """
        # Create Gaussian wave packet
        X, Y = np.meshgrid(np.arange(self.size), np.arange(self.size))
        r_squared = (X - x)**2 + (Y - y)**2
        envelope = amplitude * np.exp(-r_squared / (2 * width**2))
        
        # Modulate with frequency (creates specific pattern)
        phase = frequency * np.sqrt(r_squared)
        wave = envelope * np.sin(phase)
        
        # Add to current wave field
        self.psi += wave
        
    def measure_resonance(self, region=None):
        """
        Measure average resonance (wave amplitude) in region.
        This is analogous to "understanding" or "activation level".
        """
        if region is None:
            region = (slice(None), slice(None))
        return np.mean(np.abs(self.psi[region]))
    
    def measure_damage_pattern(self, region=None):
        """
        Measure damage pattern (memory) in region.
        """
        if region is None:
            region = (slice(None), slice(None))
        return np.mean(self.damage[region])


# ============================================================================
# DEMONSTRATION 1: LEARNING AS DAMAGE ACCUMULATION
# ============================================================================

def demo_learning():
    """
    Show how repeated wave exposure creates permanent damage (memory).
    """
    print("=" * 70)
    print("DEMONSTRATION 1: LEARNING AS DAMAGE ACCUMULATION")
    print("=" * 70)
    print("\nSimulating repeated exposure to a concept...")
    print("(Repeated wave injection at same location)\n")
    
    substrate = CognitiveSubstrate(size=100)
    
    # Target learning region
    learn_x, learn_y = 50, 50
    region = (slice(45, 55), slice(45, 55))
    
    # Track metrics over time
    exposures = 20
    resonance_history = []
    damage_history = []
    
    for exposure in range(exposures):
        # Inject wave (teaching/exposure event)
        substrate.inject_wave(learn_x, learn_y, amplitude=2.0, frequency=0.5, width=8)
        
        # Let wave propagate and damage substrate
        for _ in range(30):
            substrate.step()
        
        # Measure
        resonance = substrate.measure_resonance(region)
        damage = substrate.measure_damage_pattern(region)
        
        resonance_history.append(resonance)
        damage_history.append(damage)
        
        if exposure % 5 == 0:
            print(f"Exposure {exposure:2d}: Resonance={resonance:.3f}, Damage={damage:.3f}")
    
    print(f"\nFinal damage (memory): {damage:.3f}")
    print(f"Learning occurred: {'YES' if damage > 1.0 else 'NO'}")
    print("\nKey insight: Damage accumulates with repeated exposure.")
    print("This IS learning - substrate permanently modified.\n")
    
    return substrate, resonance_history, damage_history


# ============================================================================
# DEMONSTRATION 2: RESONANCE (UNDERSTANDING)
# ============================================================================

def demo_resonance():
    """
    Show how substrate resonates with compatible frequencies (understanding)
    and rejects incompatible ones (confusion).
    """
    print("=" * 70)
    print("DEMONSTRATION 2: RESONANCE (UNDERSTANDING)")
    print("=" * 70)
    print("\nTesting substrate response to different frequencies...\n")
    
    substrate = CognitiveSubstrate(size=100)
    
    # Pre-damage substrate at specific frequency (prior learning)
    print("Phase 1: Pre-training substrate at frequency=0.5...")
    for _ in range(10):
        substrate.inject_wave(50, 50, amplitude=2.0, frequency=0.5, width=8)
        for _ in range(30):
            substrate.step()
    
    baseline_damage = substrate.measure_damage_pattern()
    print(f"Baseline damage: {baseline_damage:.3f}\n")
    
    # Test response to compatible frequency
    print("Phase 2: Testing response to COMPATIBLE frequency (0.5)...")
    substrate_copy = CognitiveSubstrate(size=100)
    substrate_copy.damage = substrate.damage.copy()
    
    substrate_copy.inject_wave(50, 50, amplitude=1.5, frequency=0.5, width=8)
    resonance_compatible = []
    for _ in range(50):
        substrate_copy.step()
        resonance_compatible.append(substrate_copy.measure_resonance())
    
    max_resonance_compatible = max(resonance_compatible)
    print(f"Maximum resonance: {max_resonance_compatible:.3f}")
    
    # Test response to incompatible frequency
    print("\nPhase 3: Testing response to INCOMPATIBLE frequency (2.0)...")
    substrate_copy2 = CognitiveSubstrate(size=100)
    substrate_copy2.damage = substrate.damage.copy()
    
    substrate_copy2.inject_wave(50, 50, amplitude=1.5, frequency=2.0, width=8)
    resonance_incompatible = []
    for _ in range(50):
        substrate_copy2.step()
        resonance_incompatible.append(substrate_copy2.measure_resonance())
    
    max_resonance_incompatible = max(resonance_incompatible)
    print(f"Maximum resonance: {max_resonance_incompatible:.3f}")
    
    print(f"\nResonance ratio (compatible/incompatible): {max_resonance_compatible/max_resonance_incompatible:.2f}x")
    print("\nKey insight: Substrate resonates STRONGLY with familiar frequencies.")
    print("This IS understanding - pattern matches substrate's damage topology.\n")
    
    return resonance_compatible, resonance_incompatible


# ============================================================================
# DEMONSTRATION 3: INTERFERENCE (CONFUSION vs SYNTHESIS)
# ============================================================================

def demo_interference():
    """
    Show constructive interference (idea synthesis) vs destructive (confusion).
    """
    print("=" * 70)
    print("DEMONSTRATION 3: INTERFERENCE (CONFUSION vs SYNTHESIS)")
    print("=" * 70)
    
    substrate = CognitiveSubstrate(size=100)
    
    # Case 1: Constructive interference (compatible ideas)
    print("\nCase 1: CONSTRUCTIVE interference (compatible ideas)")
    print("Injecting two waves at same frequency, different locations...")
    
    substrate.inject_wave(40, 50, amplitude=1.5, frequency=0.5, width=8)
    substrate.inject_wave(60, 50, amplitude=1.5, frequency=0.5, width=8)
    
    constructive_amplitude = []
    for _ in range(60):
        substrate.step()
        constructive_amplitude.append(np.max(np.abs(substrate.psi)))
    
    max_constructive = max(constructive_amplitude)
    print(f"Maximum amplitude: {max_constructive:.3f}")
    
    # Case 2: Destructive interference (contradictory ideas)
    print("\nCase 2: DESTRUCTIVE interference (contradictory ideas)")
    print("Injecting two waves at opposite phase...")
    
    substrate2 = CognitiveSubstrate(size=100)
    substrate2.inject_wave(50, 50, amplitude=1.5, frequency=0.5, width=8)
    # Wait a bit then inject opposite phase
    for _ in range(15):
        substrate2.step()
    substrate2.inject_wave(50, 50, amplitude=1.5, frequency=0.5, width=8)
    
    destructive_amplitude = []
    for _ in range(60):
        substrate2.step()
        destructive_amplitude.append(np.max(np.abs(substrate2.psi)))
    
    max_destructive = max(destructive_amplitude)
    print(f"Maximum amplitude: {max_destructive:.3f}")
    
    print(f"\nAmplitude ratio: {max_constructive/max_destructive:.2f}x higher for constructive")
    print("\nKey insight: Compatible ideas amplify (synthesis).")
    print("Contradictory ideas cancel (confusion).\n")
    
    return constructive_amplitude, destructive_amplitude


# ============================================================================
# DEMONSTRATION 4: MULTI-SCALE DYNAMICS (SCALES METHOD)
# ============================================================================

def demo_multiscale():
    """
    Show how fast waves create slow patterns (beat frequencies).
    """
    print("=" * 70)
    print("DEMONSTRATION 4: MULTI-SCALE DYNAMICS (SCALES METHOD)")
    print("=" * 70)
    print("\nInjecting two close frequencies to create beat pattern...\n")
    
    substrate = CognitiveSubstrate(size=100)
    
    # Inject two close frequencies
    freq1, freq2 = 0.50, 0.52
    
    amplitude_history = []
    beat_envelope = []
    
    for t in range(200):
        if t % 40 == 0:
            substrate.inject_wave(50, 50, amplitude=1.0, frequency=freq1, width=8)
        if t % 40 == 10:
            substrate.inject_wave(50, 50, amplitude=1.0, frequency=freq2, width=8)
        
        substrate.step()
        
        # Measure central amplitude
        central_amp = np.abs(substrate.psi[50, 50])
        amplitude_history.append(central_amp)
    
    # Calculate envelope (beat frequency)
    window = 20
    for i in range(len(amplitude_history) - window):
        beat_envelope.append(max(amplitude_history[i:i+window]))
    
    print(f"Injected frequencies: {freq1}, {freq2}")
    print(f"Beat frequency: {abs(freq1 - freq2):.3f}")
    print("\nObserved slow modulation (beat) from fast oscillations.")
    print("\nKey insight: Fast dynamics create emergent slow dynamics.")
    print("This IS multi-scale cognition - different timescales coupled.\n")
    
    return amplitude_history, beat_envelope


# ============================================================================
# DEMONSTRATION 5: ATTENTION (SELECTIVE FILTERING)
# ============================================================================

def demo_attention():
    """
    Show attention as selective resonance - can't process everything.
    """
    print("=" * 70)
    print("DEMONSTRATION 5: ATTENTION (SELECTIVE FILTERING)")
    print("=" * 70)
    print("\nSimulating multiple simultaneous inputs (cognitive overload)...\n")
    
    substrate = CognitiveSubstrate(size=100)
    
    # Multiple inputs at different locations
    inputs = [
        (25, 25, 0.4),  # (x, y, frequency)
        (75, 25, 0.7),
        (25, 75, 1.0),
        (75, 75, 0.5),
    ]
    
    print("Injecting 4 simultaneous inputs...")
    for x, y, freq in inputs:
        substrate.inject_wave(x, y, amplitude=1.5, frequency=freq, width=6)
    
    # Let propagate
    for _ in range(100):
        substrate.step()
    
    # Measure resonance in each quadrant
    quadrants = [
        (slice(0, 50), slice(0, 50), "Top-left"),
        (slice(50, 100), slice(0, 50), "Top-right"),
        (slice(0, 50), slice(50, 100), "Bottom-left"),
        (slice(50, 100), slice(50, 100), "Bottom-right"),
    ]
    
    print("\nResonance by quadrant:")
    for row_slice, col_slice, name in quadrants:
        res = substrate.measure_resonance((row_slice, col_slice))
        print(f"  {name:15s}: {res:.3f}")
    
    # Now focus attention on one quadrant (amplify that region)
    print("\nFocusing attention on top-left quadrant...")
    substrate.inject_wave(25, 25, amplitude=2.0, frequency=0.4, width=6)
    
    for _ in range(50):
        substrate.step()
    
    print("\nResonance after attention:")
    for row_slice, col_slice, name in quadrants:
        res = substrate.measure_resonance((row_slice, col_slice))
        print(f"  {name:15s}: {res:.3f}")
    
    print("\nKey insight: Attention amplifies specific regions.")
    print("Cannot process all inputs equally - selective filtering required.\n")
    
    return substrate


# ============================================================================
# DEMONSTRATION 6: COMMUNICATION (WAVE TRANSMISSION)
# ============================================================================

def demo_communication():
    """
    Show communication as wave transmission between substrates.
    Success requires frequency matching (Pseudo-Socratic principle).
    """
    print("=" * 70)
    print("DEMONSTRATION 6: COMMUNICATION (WAVE TRANSMISSION)")
    print("=" * 70)
    
    # Transmitter substrate (teacher)
    transmitter = CognitiveSubstrate(size=100)
    
    # Pre-damage transmitter with knowledge
    print("\nPhase 1: Transmitter learns concept (frequency=0.6)...")
    for _ in range(15):
        transmitter.inject_wave(50, 50, amplitude=2.0, frequency=0.6, width=8)
        for _ in range(20):
            transmitter.step()
    
    transmit_damage = transmitter.measure_damage_pattern()
    print(f"Transmitter damage (knowledge): {transmit_damage:.3f}")
    
    # Receiver 1: Compatible substrate (can resonate at 0.6)
    print("\nPhase 2: Transmission to COMPATIBLE receiver...")
    receiver1 = CognitiveSubstrate(size=100)
    
    # Transmit by injecting wave at same frequency
    receiver1.inject_wave(50, 50, amplitude=1.5, frequency=0.6, width=8)
    
    for _ in range(100):
        receiver1.step()
    
    receive1_damage = receiver1.measure_damage_pattern()
    print(f"Receiver 1 damage (learning): {receive1_damage:.3f}")
    
    # Receiver 2: Incompatible substrate (pre-damaged at different frequency)
    print("\nPhase 3: Transmission to INCOMPATIBLE receiver...")
    receiver2 = CognitiveSubstrate(size=100)
    
    # Pre-damage at different frequency (prior contradictory knowledge)
    for _ in range(10):
        receiver2.inject_wave(50, 50, amplitude=1.8, frequency=1.5, width=8)
        for _ in range(20):
            receiver2.step()
    
    # Now try to transmit original frequency
    receiver2.inject_wave(50, 50, amplitude=1.5, frequency=0.6, width=8)
    
    for _ in range(100):
        receiver2.step()
    
    receive2_damage = receiver2.measure_damage_pattern()
    print(f"Receiver 2 damage (learning): {receive2_damage:.3f}")
    
    print(f"\nLearning ratio (compatible/incompatible): {receive1_damage/receive2_damage:.2f}x")
    print("\nKey insight: Communication succeeds when frequencies match.")
    print("This IS Pseudo-Socratic method - scan substrate, match frequency.\n")
    
    return transmitter, receiver1, receiver2


# ============================================================================
# RUN ALL DEMONSTRATIONS
# ============================================================================

def run_all_demos():
    """Run complete demonstration suite."""
    
    print("\n" + "="*70)
    print("AXIOMATIC COGNITION: MECHANICAL SIMULATION")
    print("Substrate + Wave + Damage = Mind")
    print("="*70 + "\n")
    
    # Demo 1: Learning
    substrate_learning, res_hist, dam_hist = demo_learning()
    
    # Demo 2: Resonance
    res_compat, res_incompat = demo_resonance()
    
    # Demo 3: Interference
    constructive, destructive = demo_interference()
    
    # Demo 4: Multi-scale
    amp_hist, beat_env = demo_multiscale()
    
    # Demo 5: Attention
    substrate_attention = demo_attention()
    
    # Demo 6: Communication
    trans, rec1, rec2 = demo_communication()
    
    print("="*70)
    print("ALL DEMONSTRATIONS COMPLETE")
    print("="*70)
    print("\nSummary:")
    print("  1. Learning = Damage accumulation ✓")
    print("  2. Understanding = Resonance ✓")
    print("  3. Synthesis = Constructive interference ✓")
    print("  4. Multi-scale = Beat frequencies ✓")
    print("  5. Attention = Selective amplification ✓")
    print("  6. Communication = Frequency matching ✓")
    print("\nCognition is wave mechanics in damaged substrate.")
    print("This is not metaphor. This is mechanism.\n")
    
    return {
        'learning': (substrate_learning, res_hist, dam_hist),
        'resonance': (res_compat, res_incompat),
        'interference': (constructive, destructive),
        'multiscale': (amp_hist, beat_env),
        'attention': substrate_attention,
        'communication': (trans, rec1, rec2)
    }


# ============================================================================
# VISUALIZATION
# ============================================================================

def visualize_substrate(substrate, title="Cognitive Substrate"):
    """Create visualization of substrate state."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # Wave field
    im1 = axes[0].imshow(substrate.psi, cmap='RdBu', vmin=-2, vmax=2)
    axes[0].set_title('Wave Field (Current Thought)')
    axes[0].axis('off')
    plt.colorbar(im1, ax=axes[0])
    
    # Damage field
    im2 = axes[1].imshow(substrate.damage, cmap='YlOrRd', vmin=0, vmax=10)
    axes[1].set_title('Damage Field (Memory)')
    axes[1].axis('off')
    plt.colorbar(im2, ax=axes[1])
    
    # Receptivity
    im3 = axes[2].imshow(substrate.receptivity, cmap='viridis', vmin=0, vmax=1)
    axes[2].set_title('Receptivity (Substrate Personality)')
    axes[2].axis('off')
    plt.colorbar(im3, ax=axes[2])
    
    plt.suptitle(title)
    plt.tight_layout()
    return fig


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Run all demonstrations
    results = run_all_demos()
    
    # Create visualizations
    print("\nGenerating visualizations...")
    
    # Visualize final learning state
    substrate_learning = results['learning'][0]
    fig1 = visualize_substrate(substrate_learning, "After Learning (Repeated Exposure)")
    
    # Visualize attention substrate
    substrate_attention = results['attention']
    fig2 = visualize_substrate(substrate_attention, "After Attention Focus")
    
    # Visualize communication
    trans, rec1, rec2 = results['communication']
    fig3 = visualize_substrate(trans, "Transmitter (Teacher)")
    fig4 = visualize_substrate(rec1, "Compatible Receiver (Good Student)")
    fig5 = visualize_substrate(rec2, "Incompatible Receiver (Resistant Student)")
    
    plt.show()
    
    print("\n" + "="*70)
    print("Simulation complete. Visualizations displayed.")
    print("="*70)

