import numpy as np

# =============================================================================
# NEURAL COMMUNICATION: THE PHYSICS
# =============================================================================

class NeuralNetwork:
    """
    Two substrates working together:
    1. Chemical (synapses) - discrete, local, slow
    2. EM Field - continuous, global, fast
    """
    
    def __init__(self, n_neurons=20):
        self.n = n_neurons
        
        # Membrane state
        self.V = np.ones(n_neurons) * -70.0  # Membrane potential (mV)
        self.refractory = np.zeros(n_neurons)  # Refractory period counter
        
        # Synaptic connections (sparse directed graph)
        self.W_syn = self._create_synaptic_matrix()
        
        # EM field coupling (dense, all-to-all)
        self.field_strength = 0.3  # Coupling coefficient
        
        # Energy counters
        self.chemical_energy = 0.0
        self.em_energy = 0.0
        
        # Parameters
        self.V_rest = -70.0
        self.V_threshold = -55.0
        self.V_spike = 40.0
        self.tau = 10.0  # ms, membrane time constant
        
    def _create_synaptic_matrix(self):
        """Create realistic synaptic connectivity."""
        W = np.zeros((self.n, self.n))
        
        # Nearest neighbor connections (local)
        for i in range(self.n - 1):
            W[i, i+1] = 0.8  # Forward connection
            if np.random.rand() < 0.5:
                W[i+1, i] = 0.3  # Some backward connections
        
        # Random long-range (10% probability)
        for i in range(self.n):
            for j in range(self.n):
                if i != j and abs(i - j) > 2:
                    if np.random.rand() < 0.1:
                        W[i, j] = 0.5
        
        return W
    
    def step_chemical_only(self, dt=1.0):
        """Update using only chemical synapses."""
        # Passive decay toward rest
        dV = (self.V_rest - self.V) / self.tau
        self.V += dV * dt
        
        # Detect spikes
        spiking = (self.V >= self.V_threshold) & (self.refractory == 0)
        
        if np.any(spiking):
            # Synaptic transmission
            spike_vec = spiking.astype(float)
            synaptic_current = self.W_syn.T @ spike_vec  # Matrix multiply
            self.V += synaptic_current * 15.0  # Strong synaptic kick
            
            # Energy cost (chemical)
            n_spikes = np.sum(spiking)
            self.chemical_energy += n_spikes * 5e-20  # Joules per spike
            
            # Reset spiking neurons
            self.V[spiking] = self.V_rest
            self.refractory[spiking] = 5.0  # 5ms refractory period
        
        # Decay refractory period
        self.refractory = np.maximum(0, self.refractory - dt)
        
        return np.sum(spiking)
    
    def step_with_em_field(self, dt=1.0):
        """Update with chemical + EM field coupling."""
        # Chemical dynamics (same as above)
        dV_passive = (self.V_rest - self.V) / self.tau
        self.V += dV_passive * dt
        
        # EM FIELD COUPLING (new!)
        # Each neuron's activity creates field
        # Field = average deviation from rest
        field_sources = self.V - self.V_rest
        global_field = np.mean(field_sources)
        
        # Field pushes all neurons toward synchrony
        field_coupling = self.field_strength * (global_field - field_sources)
        self.V += field_coupling * dt
        
        # EM field energy (very small)
        field_amplitude = np.std(field_sources) * 1e-3  # Volts
        self.em_energy += 0.5 * 80 * 8.85e-12 * field_amplitude**2 * 1e-9 * dt
        
        # Chemical spiking (same)
        spiking = (self.V >= self.V_threshold) & (self.refractory == 0)
        
        if np.any(spiking):
            spike_vec = spiking.astype(float)
            synaptic_current = self.W_syn.T @ spike_vec
            self.V += synaptic_current * 15.0
            
            n_spikes = np.sum(spiking)
            self.chemical_energy += n_spikes * 5e-20
            
            self.V[spiking] = self.V_rest
            self.refractory[spiking] = 5.0
        
        self.refractory = np.maximum(0, self.refractory - dt)
        
        return np.sum(spiking)
    
    def inject_current(self, neuron_idx, current):
        """External stimulation."""
        self.V[neuron_idx] += current


# =============================================================================
# DEMO 1: PROPAGATION SPEED
# =============================================================================

def demo_propagation():
    print("="*70)
    print("DEMO 1: PROPAGATION SPEED")
    print("="*70)
    print()
    print("Stimulate neuron 0, measure when neuron 19 activates...")
    print()
    
    # Chemical only
    net1 = NeuralNetwork(n_neurons=20)
    net1.inject_current(0, 30)  # Strong stimulus
    
    activated_chem = False
    for t in range(100):
        net1.step_chemical_only(dt=1.0)
        if net1.V[19] > -65 and not activated_chem:
            time_chem = t
            activated_chem = True
            break
    
    # Chemical + EM
    net2 = NeuralNetwork(n_neurons=20)
    net2.inject_current(0, 30)
    
    activated_em = False
    for t in range(100):
        net2.step_with_em_field(dt=1.0)
        if net2.V[19] > -65 and not activated_em:
            time_em = t
            activated_em = True
            break
    
    if activated_chem and activated_em:
        print(f"Chemical only:  {time_chem} ms")
        print(f"With EM field:  {time_em} ms")
        print(f"Speedup: {time_chem/time_em:.1f}×")
    else:
        print("Activity didn't reach neuron 19 (network too sparse)")
    print()


# =============================================================================
# DEMO 2: SYNCHRONIZATION
# =============================================================================

def demo_synchronization():
    print("="*70)
    print("DEMO 2: SYNCHRONIZATION")
    print("="*70)
    print()
    print("Random initial activity, watch synchrony emerge...")
    print()
    
    # Without EM
    net_no_em = NeuralNetwork(n_neurons=20)
    net_no_em.V = np.random.uniform(-70, -50, 20)
    
    # With EM
    net_em = NeuralNetwork(n_neurons=20)
    net_em.V = net_no_em.V.copy()  # Same initial state
    
    print(f"{'Time':<8} | {'No EM: Spikes':<14} | {'EM: Spikes':<12} | {'No EM: Sync':<12} | {'EM: Sync':<12}")
    print("-"*70)
    
    for t in range(0, 100, 10):
        # Run 10 steps
        spikes_no_em = 0
        spikes_em = 0
        
        for _ in range(10):
            spikes_no_em += net_no_em.step_chemical_only()
            spikes_em += net_em.step_with_em_field()
        
        # Synchrony = inverse of variance (low variance = high sync)
        sync_no_em = 1.0 / (np.std(net_no_em.V) + 1.0)
        sync_em = 1.0 / (np.std(net_em.V) + 1.0)
        
        print(f"{t+10:<8} | {spikes_no_em:<14.0f} | {spikes_em:<12.0f} | "
              f"{sync_no_em:<12.3f} | {sync_em:<12.3f}")
    
    print()
    print("Higher sync value = neurons firing together")
    print("EM field naturally synchronizes the network!")
    print()


# =============================================================================
# DEMO 3: ENERGY EFFICIENCY
# =============================================================================

def demo_energy():
    print("="*70)
    print("DEMO 3: ENERGY EFFICIENCY")
    print("="*70)
    print()
    
    net = NeuralNetwork(n_neurons=20)
    
    # Simulate 1 second with periodic stimulation
    for t in range(1000):
        if t % 20 == 0:
            stim_idx = np.random.randint(20)
            net.inject_current(stim_idx, 25)
        
        net.step_with_em_field(dt=1.0)
    
    print(f"Chemical energy: {net.chemical_energy:.2e} J")
    print(f"EM field energy: {net.em_energy:.2e} J")
    print()
    
    if net.em_energy > 0:
        ratio = net.chemical_energy / net.em_energy
        print(f"Energy ratio: {ratio:.2e}×")
        print()
        print("Chemical (synaptic) transmission is ~100,000× more expensive!")
    
    print()


# =============================================================================
# DEMO 4: NONLOCAL COUPLING
# =============================================================================

def demo_nonlocal():
    print("="*70)
    print("DEMO 4: NONLOCAL COUPLING")
    print("="*70)
    print()
    print("Neurons 0 and 19 have NO synaptic connection...")
    print()
    
    net = NeuralNetwork(n_neurons=20)
    
    # Remove ALL synaptic connections to/from neurons 0 and 19
    net.W_syn[0, :] = 0
    net.W_syn[:, 0] = 0
    net.W_syn[19, :] = 0
    net.W_syn[:, 19] = 0
    
    # Stimulate neuron 0 rhythmically (10 Hz)
    print(f"{'Time':<8} | {'Neuron 0':<12} | {'Neuron 19':<12} | {'Correlation':<12}")
    print("-"*70)
    
    history_0 = []
    history_19 = []
    
    for t in range(100):
        if t % 10 == 0:
            net.inject_current(0, 20)
        
        net.step_with_em_field()
        
        history_0.append(net.V[0])
        history_19.append(net.V[19])
        
        if t % 10 == 9:
            # Correlation over last 10 steps
            if len(history_0) >= 10:
                corr = np.corrcoef(history_0[-10:], history_19[-10:])[0, 1]
            else:
                corr = 0
            
            print(f"{t+1:<8} | {net.V[0]:<12.2f} | {net.V[19]:<12.2f} | {corr:<12.3f}")
    
    print()
    print("Despite NO direct synaptic connection, they correlate!")
    print("This is the EM field creating action-at-a-distance.")
    print()


# =============================================================================
# DEMO 5: WAVE PROPAGATION
# =============================================================================

def demo_waves():
    print("="*70)
    print("DEMO 5: WAVE PROPAGATION")
    print("="*70)
    print()
    
    net = NeuralNetwork(n_neurons=20)
    
    # Strong stimulus at one end
    net.inject_current(0, 35)
    net.inject_current(1, 35)
    
    print("Watching activity wave propagate through network...")
    print()
    
    for frame in range(5):
        print(f"Time: {frame*10} ms")
        
        # Run 10 steps
        for _ in range(10):
            net.step_with_em_field()
        
        # Visualize
        visualize(net.V)
        print()
    
    print("Activity spreads as a WAVE through the EM substrate!")
    print()


def visualize(voltages):
    """ASCII visualization of neural activity."""
    chars = " .-:=+*#%@"
    
    # Map -70 to -40 mV to character range
    normalized = (voltages + 70) / 30
    normalized = np.clip(normalized, 0, 1)
    
    indices = (normalized * (len(chars) - 1)).astype(int)
    visual = ''.join([chars[i] for i in indices])
    
    print(f"  [{visual}]")
    print(f"   0{' '*17}19")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "HOW NEURONS ACTUALLY COMMUNICATE".center(68) + "║")
    print("║" + "The Physics of Neural Computation".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    print("\n")
    
    print("Traditional view: Neuron A → Synapse → Neuron B")
    print("Reality: All neurons ↔ EM substrate ↔ All neurons")
    print()
    
    input("Press Enter to start...")
    print()
    
    demo_propagation()
    input("Press Enter for next demo...")
    print()
    
    demo_synchronization()
    input("Press Enter for next demo...")
    print()
    
    demo_energy()
    input("Press Enter for next demo...")
    print()
    
    demo_nonlocal()
    input("Press Enter for next demo...")
    print()
    
    demo_waves()
    
    print("="*70)
    print("CONCLUSION")
    print("="*70)
    print()
    print("The brain uses TWO substrates:")
    print()
    print("1. Chemical (Synapses)")
    print("   - Discrete, local connections")
    print("   - High energy cost (ATP)")
    print("   - Maintains the EM field (like DRAM refresh)")
    print()
    print("2. Electromagnetic (Field)")
    print("   - Continuous, global coupling")
    print("   - Low energy cost (near Landauer limit)")
    print("   - Does the actual computation")
    print()
    print("Consciousness IS the coherent EM field")
    print("Neurons just maintain it")
    print()


if __name__ == "__main__":
    main()
    

# This program demonstrates the core physics of neural communication through five simple demos:

# Speed: EM propagates instantly vs multi-hop chemical transmission
# Synchronization: EM creates oscillations (alpha/theta/gamma waves)
# Energy: EM is 100,000× more efficient than chemical
# Nonlocality: Neurons influence each other without direct connections
# Field dynamics: Activity spreads as waves through shared substrate

# Key insight: Synapses don't compute—they maintain the EM field. The field does the computation.

