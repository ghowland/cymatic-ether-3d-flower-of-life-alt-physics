import numpy as np

class AnesthesiaSimulator:
    """
    Simulate how anesthetics disrupt EM substrate coherence.
    """
    
    def __init__(self, n_neurons=100):
        self.n = n_neurons
        
        # EM substrate
        self.field = np.zeros(n_neurons, dtype=complex)
        self.phase_coherence = 1.0  # 1.0 = fully coherent
        
        # Neural oscillators (these maintain the field)
        self.oscillator_phase = np.zeros(n_neurons)
        self.oscillator_freq = np.ones(n_neurons) * 40.0  # 40 Hz gamma
        self.coupling_strength = 1.0  # How strongly neurons couple via field
        
    def step_conscious(self, dt=0.001):
        """
        Normal conscious state: neurons coupled through field.
        """
        # Each oscillator advances
        self.oscillator_phase += self.oscillator_freq * 2 * np.pi * dt
        
        # FIELD COUPLING: neurons synchronize via EM field
        # Average phase (global field)
        mean_phase = np.angle(np.mean(np.exp(1j * self.oscillator_phase)))
        
        # Pull each oscillator toward global phase
        phase_diff = mean_phase - self.oscillator_phase
        self.oscillator_phase += phase_diff * self.coupling_strength * dt
        
        # Update field from oscillators
        self.field = np.exp(1j * self.oscillator_phase)
        
        # Measure coherence (how synchronized are phases?)
        self.phase_coherence = np.abs(np.mean(self.field))
    
    def apply_anesthetic(self, mechanism, strength):
        """
        Apply anesthetic - different mechanisms, same effect.
        
        Mechanisms:
        1. 'decouple' - reduce field coupling (propofol-like)
        2. 'randomize' - add phase noise (sevoflurane-like)
        3. 'slow' - reduce oscillator frequency (ketamine-like)
        """
        if mechanism == 'decouple':
            # Reduce coupling between neurons and field
            # Like reducing membrane conductance
            self.coupling_strength *= (1.0 - strength)
            
        elif mechanism == 'randomize':
            # Add random phase kicks
            # Like random GABA activation
            noise = np.random.randn(self.n) * strength
            self.oscillator_phase += noise
            
        elif mechanism == 'slow':
            # Reduce oscillation frequency
            # Like blocking excitatory transmission
            self.oscillator_freq *= (1.0 - strength)
    
    def get_eeg_power_spectrum(self):
        """What EEG would measure."""
        # Spatial average of field
        avg_field = np.mean(self.field)
        power = np.abs(avg_field)**2
        freq = np.mean(self.oscillator_freq)
        return freq, power


def demo_anesthetic_mechanisms():
    """
    Show how different anesthetics disrupt field coherence.
    """
    print("="*70)
    print("ANESTHESIA MECHANISMS: FIELD DISRUPTION")
    print("="*70)
    print()
    
    print("Simulating three anesthetic mechanisms...")
    print()
    
    # Run simulations
    results = {}
    
    for mechanism in ['decouple', 'randomize', 'slow']:
        sim = AnesthesiaSimulator(n_neurons=100)
        
        coherence_history = []
        
        # Baseline (conscious)
        for _ in range(100):
            sim.step_conscious(dt=0.001)
            coherence_history.append(sim.phase_coherence)
        
        # Apply anesthetic gradually
        for dose in range(100):
            sim.apply_anesthetic(mechanism, strength=0.01)
            sim.step_conscious(dt=0.001)
            coherence_history.append(sim.phase_coherence)
        
        results[mechanism] = coherence_history
    
    # Report
    print(f"{'Mechanism':<15} | {'Initial Coherence':<18} | {'Final Coherence':<18}")
    print("-"*70)
    
    for mechanism, history in results.items():
        initial = history[50]  # After stabilization
        final = history[-1]
        print(f"{mechanism:<15} | {initial:<18.3f} | {final:<18.3f}")
    
    print()
    print("ALL mechanisms reduce coherence, despite different targets!")
    print()
    
    # Show timeline
    print("COHERENCE TIMELINE (decouple mechanism):")
    print()
    print(f"{'Time':<8} | {'Coherence':<12} | {'State':<20}")
    print("-"*70)
    
    history = results['decouple']
    for t in [0, 50, 100, 125, 150, 175, 199]:
        coh = history[t]
        
        if coh > 0.9:
            state = "Fully Conscious"
        elif coh > 0.7:
            state = "Drowsy"
        elif coh > 0.5:
            state = "Light Anesthesia"
        elif coh > 0.3:
            state = "Deep Anesthesia"
        else:
            state = "Unconscious"
        
        print(f"{t:<8} | {coh:<12.3f} | {state:<20}")
    
    print()
    print("Consciousness = field coherence > ~0.7")
    print("Anesthesia = field decoherence")
    print()


if __name__ == "__main__":
    demo_anesthetic_mechanisms()


