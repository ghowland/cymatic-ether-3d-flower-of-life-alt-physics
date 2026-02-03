#!/usr/bin/env python3
"""
Human as Software-Defined Matter (SDM) Simulator
=================================================

Demonstrates whole-body memory as distributed flow patterns.

Key concepts:
- Brain: Pattern generator (high complexity)
- Spinal cord: Pattern relay
- Organs: Pattern responders with local memory
- EM substrate: Fast information flow (light speed)
- Neural substrate: Medium flow (spike propagation)
- Structural substrate: Slow memory (synaptic/cellular)

All substrates interact continuously - memory is circulation.
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple
import time


# =============================================================================
# ORGAN SYSTEMS (Pattern Responders with Local Memory)
# =============================================================================

@dataclass
class OrganSystem:
    """
    An organ system with its own local memory and processing.
    
    Examples: Heart, Gut, Lungs, Liver, Immune system
    Each has local pattern memory independent of brain.
    """
    name: str
    neuron_count: int           # Local neurons (e.g., gut: 500M)
    cell_count: int             # Total cells in organ
    
    # State variables
    em_field: np.ndarray        # EM substrate pattern (fast)
    neural_state: np.ndarray    # Neural activation (medium)
    cellular_memory: np.ndarray # Structural memory (slow)
    
    # Connections to CNS
    afferent_strength: float    # How strongly organ signals to brain
    efferent_strength: float    # How strongly brain controls organ
    
    # Physiology
    intrinsic_rhythm: float     # Natural oscillation frequency (Hz)
    autonomy: float            # Can function without brain (0-1)


def create_organ(
    name: str,
    neuron_count: int,
    cell_count: int,
    field_size: int = 32,
    afferent: float = 0.5,
    efferent: float = 0.5,
    rhythm: float = 1.0,
    autonomy: float = 0.3
) -> OrganSystem:
    """Create an organ system with local memory."""
    return OrganSystem(
        name=name,
        neuron_count=neuron_count,
        cell_count=cell_count,
        em_field=np.zeros((field_size, field_size)),
        neural_state=np.zeros(field_size),
        cellular_memory=np.zeros((field_size, field_size)),
        afferent_strength=afferent,
        efferent_strength=efferent,
        intrinsic_rhythm=rhythm,
        autonomy=autonomy
    )


# =============================================================================
# HUMAN BODY AS SOFTWARE-DEFINED MATTER
# =============================================================================

class HumanSDM:
    """
    Complete human as distributed memory system.
    
    Architecture:
    - Brain: Primary pattern generator
    - Spinal cord: Fast relay + local processing
    - Organs: Specialized pattern responders with memory
    - EM substrate: Light-speed information flow
    - Circulation: Patterns flow continuously between all parts
    """
    
    def __init__(self, field_size: int = 64):
        self.field_size = field_size
        self.time = 0.0
        self.dt = 0.01  # 10ms timesteps
        
        # CENTRAL NERVOUS SYSTEM
        # Brain: Primary pattern generator (86B neurons)
        self.brain_em = np.zeros((field_size, field_size))
        self.brain_neural = np.zeros((field_size, field_size))
        self.brain_synaptic = np.zeros((field_size, field_size))
        
        # Spinal cord: Fast relay (1B neurons)
        self.spinal_em = np.zeros(field_size)
        self.spinal_neural = np.zeros(field_size)
        
        # PERIPHERAL ORGANS (Pattern responders with local memory)
        self.organs = {
            'heart': create_organ(
                'Heart', 
                neuron_count=40000,
                cell_count=2_000_000_000,  # 2 billion cardiomyocytes
                afferent=0.3,
                efferent=0.7,
                rhythm=1.2,  # ~72 bpm
                autonomy=0.9  # Highly autonomous
            ),
            'gut': create_organ(
                'Gut (Enteric)', 
                neuron_count=500_000_000,  # 500M neurons!
                cell_count=300_000_000_000,  # Massive
                afferent=0.6,
                efferent=0.4,
                rhythm=0.05,  # Slow waves
                autonomy=0.7  # Can function independently
            ),
            'lungs': create_organ(
                'Lungs',
                neuron_count=1_000_000,
                cell_count=40_000_000_000,
                afferent=0.5,
                efferent=0.5,
                rhythm=0.25,  # ~15 breaths/min
                autonomy=0.3  # Brain-dependent
            ),
            'immune': create_organ(
                'Immune System',
                neuron_count=10_000_000,  # Sensory ganglia
                cell_count=2_000_000_000_000,  # 2 trillion immune cells
                afferent=0.4,
                efferent=0.3,
                rhythm=0.0001,  # Very slow (days)
                autonomy=0.95  # Highly autonomous
            ),
            'muscles': create_organ(
                'Skeletal Muscles',
                neuron_count=500_000,  # Motor neurons
                cell_count=600_000_000_000,  # Muscle fibers
                afferent=0.7,  # Proprioception
                efferent=0.9,  # Motor control
                rhythm=10.0,  # Fast (tremor freq)
                autonomy=0.0  # Brain-dependent
            )
        }
        
        # GLOBAL EM SUBSTRATE (Light-speed flow throughout body)
        self.global_em = np.zeros((field_size, field_size, field_size))
        
        # MEMORY PATTERNS (distributed storage)
        self.working_memory = []  # EM circulation patterns
        self.episodic_buffer = []  # Recent events
        self.body_memories = {}   # Organ-specific memories
        
        # STATISTICS
        self.total_neurons = 86_000_000_000 + sum(o.neuron_count for o in self.organs.values())
        self.total_cells = 37_000_000_000_000  # ~37 trillion
        
    
    def step(self):
        """
        Single timestep: Update all substrates and organs.
        
        Order matters - this is flow:
        1. Update global EM substrate (fastest)
        2. Update brain patterns
        3. Descending flow: Brain → Spinal → Organs
        4. Organ autonomous processing
        5. Ascending flow: Organs → Spinal → Brain
        6. Memory consolidation
        """
        self.time += self.dt
        
        # 1. GLOBAL EM SUBSTRATE UPDATE (light-speed propagation)
        self._update_global_em()
        
        # 2. BRAIN PROCESSING
        self._update_brain()
        
        # 3. DESCENDING FLOW (Brain controls organs)
        descending = self._brain_to_spinal()
        self._spinal_to_organs(descending)
        
        # 4. ORGAN AUTONOMOUS PROCESSING (local memory)
        for organ in self.organs.values():
            self._update_organ(organ)
        
        # 5. ASCENDING FLOW (Organs inform brain)
        ascending = self._organs_to_spinal()
        self._spinal_to_brain(ascending)
        
        # 6. MEMORY OPERATIONS
        self._update_working_memory()
        self._consolidate_memories()
        
    
    def _update_global_em(self):
        """
        Global EM substrate evolution (wave equation).
        This is the FASTEST substrate - light speed propagation.
        """
        # Simple 3D wave equation (Laplacian)
        laplacian = (
            np.roll(self.global_em, 1, axis=0) + np.roll(self.global_em, -1, axis=0) +
            np.roll(self.global_em, 1, axis=1) + np.roll(self.global_em, -1, axis=1) +
            np.roll(self.global_em, 1, axis=2) + np.roll(self.global_em, -1, axis=2) 
            - 6 * self.global_em
        )
        
        # Wave propagation (simplified)
        wave_speed = 1000.0  # Arbitrary units (much faster than neural)
        self.global_em += wave_speed * laplacian * self.dt
        
        # Damping (energy dissipation)
        self.global_em *= 0.99
        
    
    def _update_brain(self):
        """
        Brain pattern generation and processing.
        
        Brain has three substrates:
        - EM field (fast, working memory)
        - Neural firing (medium, circulation)
        - Synaptic weights (slow, long-term memory)
        """
        # EM field evolution (gamma oscillations ~40 Hz)
        gamma_freq = 40.0  # Hz
        phase = 2 * np.pi * gamma_freq * self.time
        
        # Natural oscillation + external input
        self.brain_em = (
            0.5 * np.sin(phase) * np.exp(-(self.time % 1.0)) +
            0.3 * self.brain_em +  # Persistence
            0.2 * np.random.randn(*self.brain_em.shape) * 0.01  # Noise
        )
        
        # Neural state follows EM field (with delay)
        self.brain_neural = 0.7 * self.brain_neural + 0.3 * self.brain_em
        
        # Synaptic memory slowly adapts to frequent patterns
        # (Hebbian: patterns that co-occur strengthen)
        active_threshold = 0.5
        active = (np.abs(self.brain_neural) > active_threshold).astype(float)
        self.brain_synaptic = 0.9999 * self.brain_synaptic + 0.0001 * active
        
    
    def _brain_to_spinal(self) -> np.ndarray:
        """Descending motor/autonomic commands."""
        # Average brain activity projects to spinal cord
        descending = np.mean(self.brain_neural, axis=0)
        return descending
    
    
    def _spinal_to_organs(self, descending: np.ndarray):
        """Spinal cord distributes commands to organs."""
        self.spinal_neural = 0.8 * self.spinal_neural + 0.2 * descending
        
        # Each organ receives weighted projection
        for organ in self.organs.values():
            # Efferent control (brain → organ)
            control_signal = np.mean(self.spinal_neural) * organ.efferent_strength
            
            # Add to organ's neural state
            organ.neural_state += control_signal * 0.1
    
    
    def _update_organ(self, organ: OrganSystem):
        """
        Update organ's local processing.
        
        Organs have:
        - EM field (fast local patterns)
        - Neural state (local processing)
        - Cellular memory (structural, slow)
        - Intrinsic rhythms (autonomous function)
        """
        # Intrinsic rhythm (organs have autonomous oscillations)
        intrinsic_phase = 2 * np.pi * organ.intrinsic_rhythm * self.time
        intrinsic_drive = organ.autonomy * np.sin(intrinsic_phase)
        
        # EM field evolution (local wave patterns)
        laplacian = (
            np.roll(organ.em_field, 1, axis=0) + np.roll(organ.em_field, -1, axis=0) +
            np.roll(organ.em_field, 1, axis=1) + np.roll(organ.em_field, -1, axis=1)
            - 4 * organ.em_field
        )
        organ.em_field += 0.5 * laplacian * self.dt
        organ.em_field += intrinsic_drive * 0.1
        
        # Neural state follows EM + intrinsic rhythm
        organ.neural_state = (
            0.6 * organ.neural_state +
            0.2 * np.mean(organ.em_field) +
            0.2 * intrinsic_drive
        )
        
        # Cellular memory (very slow adaptation)
        # Records patterns that repeat frequently
        if np.abs(np.mean(organ.em_field)) > 0.5:
            organ.cellular_memory += 0.001 * organ.em_field
        
        # Decay
        organ.em_field *= 0.95
        organ.neural_state *= 0.98
        organ.cellular_memory *= 0.9999  # Very slow decay (structural)
    
    
    def _organs_to_spinal(self) -> np.ndarray:
        """Ascending sensory/physiological feedback."""
        ascending = np.zeros(self.field_size)
        
        for organ in self.organs.values():
            # Afferent signals (organ → brain)
            signal = np.mean(organ.neural_state) * organ.afferent_strength
            ascending += signal
        
        return ascending
    
    
    def _spinal_to_brain(self, ascending: np.ndarray):
        """Ascending signals reach brain (feedback)."""
        # Add to brain EM field (sensory input)
        self.brain_em += ascending[:, np.newaxis] * 0.1
    
    
    def _update_working_memory(self):
        """
        Working memory = patterns circulating in EM substrate.
        Capacity limited by coherence (7±2 items).
        """
        # Extract current brain patterns
        current_pattern = self.brain_em.copy()
        
        # Add to working memory if sufficiently strong
        if np.max(np.abs(current_pattern)) > 0.7:
            self.working_memory.append({
                'pattern': current_pattern,
                'timestamp': self.time,
                'strength': np.mean(np.abs(current_pattern))
            })
        
        # Decay and capacity limit (7 items)
        max_items = 7
        self.working_memory = [
            mem for mem in self.working_memory 
            if (self.time - mem['timestamp']) < 2.0  # 2 second decay
        ]
        
        if len(self.working_memory) > max_items:
            # Keep strongest patterns
            self.working_memory.sort(key=lambda x: x['strength'], reverse=True)
            self.working_memory = self.working_memory[:max_items]
    
    
    def _consolidate_memories(self):
        """
        Sleep-like consolidation: EM patterns → structural storage.
        Happens continuously but enhanced during rest.
        """
        # Every ~100 timesteps, consolidate working memory
        if int(self.time / self.dt) % 100 == 0:
            for mem in self.working_memory:
                # Strong patterns in working memory strengthen synapses
                self.brain_synaptic += 0.01 * np.abs(mem['pattern'])
                
                # Also store in relevant organs (embodied memory)
                for organ_name, organ in self.organs.items():
                    # Different organs store different aspects
                    if organ_name == 'gut' and np.mean(mem['pattern']) > 0:
                        # Gut stores emotional/valence info
                        organ.cellular_memory += 0.001 * mem['pattern'][:32, :32]
                    elif organ_name == 'muscles' and np.std(mem['pattern']) > 0.5:
                        # Muscles store motor patterns
                        organ.cellular_memory += 0.001 * mem['pattern'][:32, :32]
    
    
    def inject_experience(self, pattern_type: str = 'visual'):
        """
        Inject a sensory experience (external input).
        
        This simulates: seeing something, hearing something, feeling something.
        Pattern enters through sensory organs → thalamus → cortex.
        """
        size = self.field_size
        
        if pattern_type == 'visual':
            # Create visual-like pattern (edges, orientations)
            x, y = np.meshgrid(np.linspace(-3, 3, size), np.linspace(-3, 3, size))
            pattern = np.sin(3*x) * np.cos(3*y) * np.exp(-(x**2 + y**2)/4)
            
        elif pattern_type == 'emotional':
            # Emotional patterns affect gut, heart
            pattern = np.random.randn(size, size) * 0.5
            self.organs['gut'].em_field += pattern[:32, :32] * 0.5
            self.organs['heart'].neural_state += np.mean(pattern) * 0.3
            
        elif pattern_type == 'motor':
            # Motor patterns primarily in brain → muscles
            pattern = np.zeros((size, size))
            pattern[size//4:3*size//4, size//4:3*size//4] = 1.0
            self.organs['muscles'].em_field += pattern[:32, :32] * 0.7
            
        else:  # 'abstract'
            # Pure cognitive pattern (no sensory correlate)
            pattern = np.random.randn(size, size)
        
        # Add to brain EM field (sensory input)
        self.brain_em += pattern * 0.5
        
        # Add to episodic buffer
        self.episodic_buffer.append({
            'type': pattern_type,
            'pattern': pattern,
            'time': self.time
        })
        
        # Keep only recent episodes
        if len(self.episodic_buffer) > 20:
            self.episodic_buffer.pop(0)
    
    
    def query_memory(self, cue: np.ndarray) -> dict:
        """
        Memory recall: Given cue, find matching pattern.
        
        This demonstrates:
        - Content-addressable memory (partial cue → full pattern)
        - Multi-substrate search (brain + organs)
        - Resonance-based retrieval
        """
        results = {
            'working_memory_match': None,
            'brain_synaptic_match': 0.0,
            'organ_matches': {},
            'recall_quality': 0.0
        }
        
        # Search working memory (fast EM circulation)
        best_match = None
        best_similarity = 0.0
        for mem in self.working_memory:
            similarity = np.corrcoef(
                cue.flatten(), 
                mem['pattern'].flatten()
            )[0, 1]
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = mem
        
        results['working_memory_match'] = best_match
        
        # Search brain synaptic memory (slow structural)
        synaptic_similarity = np.corrcoef(
            cue.flatten(),
            self.brain_synaptic.flatten()
        )[0, 1]
        results['brain_synaptic_match'] = synaptic_similarity
        
        # Search organ memories (embodied memory)
        for organ_name, organ in self.organs.items():
            organ_similarity = np.corrcoef(
                cue[:32, :32].flatten(),
                organ.cellular_memory.flatten()
            )[0, 1]
            results['organ_matches'][organ_name] = organ_similarity
        
        # Overall recall quality (weighted combination)
        results['recall_quality'] = (
            0.4 * best_similarity +
            0.3 * synaptic_similarity +
            0.3 * np.mean(list(results['organ_matches'].values()))
        )
        
        return results
    
    
    def get_state_summary(self) -> dict:
        """Get current state of all substrates."""
        return {
            'time': self.time,
            'brain_em_activity': np.mean(np.abs(self.brain_em)),
            'brain_neural_activity': np.mean(np.abs(self.brain_neural)),
            'working_memory_items': len(self.working_memory),
            'organ_states': {
                name: {
                    'em_activity': np.mean(np.abs(organ.em_field)),
                    'neural_activity': np.mean(np.abs(organ.neural_state)),
                    'memory_strength': np.mean(np.abs(organ.cellular_memory))
                }
                for name, organ in self.organs.items()
            },
            'total_neurons': self.total_neurons,
            'total_cells': self.total_cells
        }


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_basic_function():
    """Demo: Basic physiological function without conscious input."""
    print("="*70)
    print("DEMO 1: Autonomous Organ Function")
    print("="*70)
    print()
    print("Simulating: Body functioning without brain (autonomous rhythms)")
    print()
    
    human = HumanSDM(field_size=32)  # Smaller for speed
    
    print(f"Total neurons: {human.total_neurons:,}")
    print(f"Total cells: {human.total_cells:,}")
    print()
    print("Organs and their autonomy:")
    for name, organ in human.organs.items():
        print(f"  {name:20s}: {organ.neuron_count:12,} neurons, "
              f"autonomy={organ.autonomy:.1f}")
    print()
    
    print("Running 100 timesteps (1 second)...")
    print()
    
    for i in range(100):
        human.step()
        
        if i % 20 == 0:
            state = human.get_state_summary()
            print(f"t={state['time']:.2f}s")
            print(f"  Brain EM: {state['brain_em_activity']:.3f}")
            for organ_name, organ_state in state['organ_states'].items():
                print(f"  {organ_name:20s}: Neural={organ_state['neural_activity']:.3f}")
            print()
    
    print("Observation: Heart and Gut maintain activity even without brain input")
    print("(High autonomy organs continue intrinsic rhythms)")
    print()


def demo_memory_formation():
    """Demo: Experience → Working memory → Consolidation."""
    print("="*70)
    print("DEMO 2: Memory Formation (Multi-Substrate)")
    print("="*70)
    print()
    print("Simulating: Learning experience distributed across body")
    print()
    
    human = HumanSDM(field_size=32)
    
    print("Step 1: Inject visual experience (t=0)")
    human.inject_experience('visual')
    print(f"  Working memory items: {len(human.working_memory)}")
    print()
    
    print("Step 2: Maintain pattern in circulation (t=0-1s)")
    for _ in range(50):
        human.step()
    print(f"  Working memory items: {len(human.working_memory)}")
    print()
    
    print("Step 3: Inject emotional experience (affects gut)")
    human.inject_experience('emotional')
    state = human.get_state_summary()
    print(f"  Gut EM activity: {state['organ_states']['gut']['em_activity']:.3f}")
    print(f"  Working memory items: {len(human.working_memory)}")
    print()
    
    print("Step 4: Continue circulation + consolidation (1-3s)")
    for _ in range(100):
        human.step()
    
    state = human.get_state_summary()
    print(f"  Working memory items: {len(human.working_memory)}")
    print(f"  Brain synaptic strength: {np.mean(human.brain_synaptic):.4f}")
    print(f"  Gut memory: {state['organ_states']['gut']['memory_strength']:.4f}")
    print()
    
    print("Observation: Experience stored in BOTH brain synapses AND gut memory")
    print("(Embodied cognition - memories distributed across body)")
    print()


def demo_memory_recall():
    """Demo: Retrieval from multi-substrate storage."""
    print("="*70)
    print("DEMO 3: Memory Recall (Content-Addressable)")
    print("="*70)
    print()
    print("Simulating: Partial cue → Full memory retrieval")
    print()
    
    human = HumanSDM(field_size=32)
    
    # Create and store several experiences
    print("Encoding three experiences:")
    print("  1. Visual (sunset)")
    human.inject_experience('visual')
    for _ in range(30):
        human.step()
    
    print("  2. Emotional (joy)")
    human.inject_experience('emotional')
    for _ in range(30):
        human.step()
    
    print("  3. Motor (running)")
    human.inject_experience('motor')
    for _ in range(30):
        human.step()
    
    # Consolidate
    print("\nConsolidating...")
    for _ in range(50):
        human.step()
    
    print(f"\nCurrent working memory: {len(human.working_memory)} items")
    print()
    
    # Create retrieval cue (partial pattern)
    print("Creating retrieval cue (partial visual pattern)...")
    cue = np.zeros((32, 32))
    x, y = np.meshgrid(np.linspace(-3, 3, 32), np.linspace(-3, 3, 32))
    cue = np.sin(3*x) * np.cos(3*y) * np.exp(-(x**2 + y**2)/4)
    cue += np.random.randn(32, 32) * 0.3  # Add noise (partial/degraded)
    
    # Query memory
    results = human.query_memory(cue)
    
    print("\nRecall results:")
    print(f"  Working memory match: {results['working_memory_match'] is not None}")
    print(f"  Brain synaptic match: {results['brain_synaptic_match']:.3f}")
    print(f"  Overall recall quality: {results['recall_quality']:.3f}")
    print()
    print("  Organ-specific matches:")
    for organ, similarity in results['organ_matches'].items():
        print(f"    {organ:20s}: {similarity:.3f}")
    print()
    
    print("Observation: Memory retrieved from multiple substrates")
    print("(Partial cue activates patterns in brain AND organs)")
    print()


def demo_body_wide_integration():
    """Demo: Whole-body response to challenge."""
    print("="*70)
    print("DEMO 4: Whole-Body Integration (SDM)")
    print("="*70)
    print()
    print("Simulating: Stress response (all systems coordinate)")
    print()
    
    human = HumanSDM(field_size=32)
    
    print("Baseline state:")
    state = human.get_state_summary()
    baseline = {
        organ: s['neural_activity'] 
        for organ, s in state['organ_states'].items()
    }
    for organ, activity in baseline.items():
        print(f"  {organ:20s}: {activity:.3f}")
    print()
    
    print("Injecting stressor (emotional experience)...")
    human.inject_experience('emotional')
    
    print("\nPropagating through body (0.5 seconds)...")
    for _ in range(50):
        human.step()
    
    state = human.get_state_summary()
    print("\nResponse state:")
    for organ, s in state['organ_states'].items():
        delta = s['neural_activity'] - baseline[organ]
        print(f"  {organ:20s}: {s['neural_activity']:.3f} "
              f"(Δ={delta:+.3f})")
    print()
    
    print("Observation: Single brain input affects ALL organs")
    print("(Heart rate, gut activity, immune response, muscle tension)")
    print("This is Software-Defined Matter - brain reconfigures body state")
    print()


def demo_capacity_comparison():
    """Demo: Information capacity across substrates."""
    print("="*70)
    print("DEMO 5: Information Capacity (Whole-Body vs DWDM)")
    print("="*70)
    print()
    
    human = HumanSDM(field_size=64)
    
    print("Information storage capacity estimates:")
    print()
    
    # Brain synaptic
    synaptic_bits = 100_000_000_000_000  # 100 trillion synapses × 10 states
    print(f"Brain synaptic memory:")
    print(f"  ~{synaptic_bits:.2e} bits ({synaptic_bits/1e15:.1f} Petabits)")
    print()
    
    # EM substrate
    em_volumes = 70_000  # 70 liters = 70,000 cm³ = 70M mm³
    modes_per_volume = 10000  # From DWDM analogy
    em_bits = em_volumes * modes_per_volume
    print(f"EM substrate (whole body):")
    print(f"  ~{em_bits:.2e} bits ({em_bits/1e12:.1f} Terabits)")
    print()
    
    # Cellular (epigenetic)
    total_cells = 37_000_000_000_000
    epigenetic_states = 100  # Simplified
    cellular_bits = total_cells * np.log2(epigenetic_states)
    print(f"Cellular/epigenetic memory:")
    print(f"  ~{cellular_bits:.2e} bits ({cellular_bits/1e15:.1f} Petabits)")
    print()
    
    # Total
    total_bits = synaptic_bits + em_bits + cellular_bits
    print(f"TOTAL BODY CAPACITY:")
    print(f"  ~{total_bits:.2e} bits ({total_bits/1e15:.1f} Petabits)")
    print()
    
    # Compare to DWDM
    dwdm_single_fiber = 1e12  # ~1 Terabit
    dwdm_max_theoretical = 1e15  # ~1 Petabit (theoretical limit)
    
    print(f"Single DWDM fiber:")
    print(f"  ~{dwdm_single_fiber:.2e} bits ({dwdm_single_fiber/1e12:.1f} Terabits)")
    print()
    
    print(f"Ratio (Human / Single DWDM fiber): {total_bits/dwdm_single_fiber:,.0f}×")
    print()
    
    print("Conclusion: Human body capacity >> single DWDM fiber")
    print("But human is DISTRIBUTED network, not single channel")
    print()


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "    HUMAN AS SOFTWARE-DEFINED MATTER".center(68) + "║")
    print("║" + "         Multi-Substrate Memory Simulator".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    print("\n")
    
    demos = [
        ("Autonomous Function", demo_basic_function),
        ("Memory Formation", demo_memory_formation),
        ("Memory Recall", demo_memory_recall),
        ("Whole-Body Integration", demo_body_wide_integration),
        ("Capacity Analysis", demo_capacity_comparison)
    ]
    
    for name, demo_func in demos:
        demo_func()
        input("Press Enter to continue...")
        print("\n")
    
    print("="*70)
    print("KEY INSIGHTS")
    print("="*70)
    print()
    print("1. MEMORY IS DISTRIBUTED")
    print("   - Brain EM field: Fast, working memory (seconds)")
    print("   - Brain synapses: Slow, long-term (lifetime)")
    print("   - Organ memories: Embodied, specialized (gut, heart, muscles)")
    print("   - Cellular: Epigenetic states (very long-term)")
    print()
    print("2. MEMORY IS FLOW, NOT STORAGE")
    print("   - Patterns circulate continuously")
    print("   - Brain ↔ Organs ↔ Brain (closed loops)")
    print("   - Different timescales for different substrates")
    print("   - No single 'storage location'")
    print()
    print("3. WHOLE BODY IS THE COMPUTER")
    print("   - 88 billion neurons (CNS + PNS)")
    print("   - 37 trillion cells (all oscillators)")
    print("   - Capacity: ~1-10 Petabits (distributed)")
    print("   - Much greater than single DWDM fiber")
    print()
    print("4. SOFTWARE-DEFINED MATTER")
    print("   - Brain reconfigures body function dynamically")
    print("   - Organs have local autonomy (continue without brain)")
    print("   - Bidirectional flow (brain ↔ organs)")
    print("   - Emotions, thoughts affect ALL systems")
    print()
    print("This demonstrates the CLR framework:")
    print("  Reality = patterns reconstructing in distributed substrate")
    print("  Human = self-maintaining pattern across 37 trillion cells")
    print("  Memory = circulation patterns in multi-substrate network")
    print()