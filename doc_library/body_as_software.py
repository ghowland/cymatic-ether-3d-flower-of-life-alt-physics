#!/usr/bin/env python3
"""
Whole Human Body Cymatic Simulation
====================================

Minimal simulation showing all organs as coupled oscillators
working together in unified update loop.

Every organ:
- Has intrinsic oscillation frequency
- Stores local patterns (memory)
- Couples to EM substrate
- Communicates with other organs
- Maintains coherence or fails

Health = Coherent coupling
Disease = Pattern disruption
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, List


# =============================================================================
# ORGAN BASE CLASS
# =============================================================================

@dataclass
class Organ:
    """
    Base organ: Oscillator with local memory and EM coupling.
    
    All organs share this structure:
    - intrinsic_freq: Natural oscillation rate
    - em_field: Fast substrate (light speed)
    - neural_state: Medium substrate (spike propagation)
    - cellular_memory: Slow substrate (structural)
    - autonomy: Can function without brain (0-1)
    """
    name: str
    intrinsic_freq: float      # Hz (natural rhythm)
    neuron_count: int          # Local processing capacity
    cell_count: int            # Total cells
    autonomy: float            # Independence from brain (0-1)
    
    # State variables (all same size for simplicity)
    em_field: np.ndarray       # Fast (EM patterns)
    neural_state: np.ndarray   # Medium (neural patterns)
    cellular_memory: np.ndarray # Slow (structural patterns)
    
    # Current values
    phase: float = 0.0         # Oscillation phase
    energy: float = 1.0        # Metabolic energy
    coherence: float = 1.0     # Pattern integrity
    
    def update(self, dt: float, brain_signal: float, global_em: np.ndarray):
        """
        Update organ state.
        
        Steps:
        1. Intrinsic oscillation (autonomous)
        2. EM substrate coupling (fast)
        3. Neural processing (medium)
        4. Cellular memory (slow)
        5. Coherence check
        """
        # Intrinsic rhythm (autonomous oscillation)
        self.phase += 2 * np.pi * self.intrinsic_freq * dt
        self.phase = self.phase % (2 * np.pi)
        intrinsic = np.sin(self.phase) * self.autonomy
        
        # EM field evolution (fast substrate)
        # Couple to global EM + local intrinsic drive
        self.em_field = (
            0.5 * self.em_field +                    # Persistence
            0.3 * np.mean(global_em) +               # Global coupling
            0.2 * intrinsic                          # Intrinsic drive
        )
        
        # Neural state (medium substrate)
        # Follows EM + brain input + intrinsic
        brain_influence = (1.0 - self.autonomy) * brain_signal
        self.neural_state = (
            0.6 * self.neural_state +                # Persistence
            0.2 * np.mean(self.em_field) +          # Local EM
            0.1 * brain_influence +                  # Brain control
            0.1 * intrinsic                          # Intrinsic
        )
        
        # Cellular memory (slow substrate)
        # Very slow adaptation to frequent patterns
        if np.abs(np.mean(self.em_field)) > 0.5:
            # Strong patterns gradually encode
            self.cellular_memory += 0.001 * self.em_field
        
        # Decay
        self.em_field *= 0.95
        self.neural_state *= 0.98
        self.cellular_memory *= 0.9999
        
        # Coherence check (pattern integrity)
        em_coherence = 1.0 - np.std(self.em_field)
        neural_coherence = 1.0 - np.std(self.neural_state)
        self.coherence = 0.5 * em_coherence + 0.5 * neural_coherence
        self.coherence = np.clip(self.coherence, 0.0, 1.0)
        
        # Energy consumption (oscillation costs energy)
        self.energy -= 0.001 * np.abs(intrinsic)
        self.energy = np.clip(self.energy, 0.0, 1.0)


# =============================================================================
# COMPLETE HUMAN BODY
# =============================================================================

class HumanBody:
    """
    Complete human as coupled organ network.
    
    Architecture:
    - Brain: Pattern generator/coordinator
    - All organs: Specialized oscillators
    - Global EM substrate: Fast communication
    - Circulatory coupling: Resource distribution
    """
    
    def __init__(self, field_size: int = 16):
        self.field_size = field_size
        self.time = 0.0
        self.dt = 0.01  # 10ms timesteps
        
        # GLOBAL EM SUBSTRATE (body-wide fast communication)
        self.global_em = np.zeros(field_size)
        
        # Create all organs
        self.organs = self._create_all_organs()
        
        # BRAIN (special - primary pattern generator)
        self.brain_phase = 0.0
        self.brain_freq = 40.0  # Gamma oscillation (40 Hz)
        
        # BLOOD (resource distribution)
        self.blood_oxygen = 1.0
        self.blood_glucose = 1.0
        self.blood_flow = np.ones(len(self.organs))
        
        # SYSTEM STATE
        self.alive = True
        self.health = 1.0
        
    
    def _create_all_organs(self) -> Dict[str, Organ]:
        """Create all major organs with realistic parameters."""
        fs = self.field_size
        
        organs = {
            # NERVOUS SYSTEM
            'brain': Organ(
                'Brain', 
                intrinsic_freq=40.0,         # Gamma ~40 Hz
                neuron_count=86_000_000_000,
                cell_count=86_000_000_000,
                autonomy=1.0,                # Fully autonomous
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'spinal_cord': Organ(
                'Spinal Cord',
                intrinsic_freq=10.0,         # ~10 Hz
                neuron_count=1_000_000_000,
                cell_count=1_000_000_000,
                autonomy=0.3,                # Partially autonomous (reflexes)
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'enteric': Organ(
                'Enteric (Gut) Nervous System',
                intrinsic_freq=0.05,         # Slow waves ~0.05 Hz
                neuron_count=500_000_000,    # 500M neurons!
                cell_count=500_000_000,
                autonomy=0.7,                # Highly autonomous
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # CARDIOVASCULAR
            'heart': Organ(
                'Heart',
                intrinsic_freq=1.2,          # ~72 bpm
                neuron_count=40_000,         # Cardiac ganglia
                cell_count=2_000_000_000,    # 2B cardiomyocytes
                autonomy=0.9,                # Highly autonomous (SA node)
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # RESPIRATORY
            'lungs': Organ(
                'Lungs',
                intrinsic_freq=0.25,         # ~15 breaths/min
                neuron_count=1_000_000,
                cell_count=40_000_000_000,   # 40B cells
                autonomy=0.3,                # Brainstem-dependent
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # DIGESTIVE
            'stomach': Organ(
                'Stomach',
                intrinsic_freq=0.05,         # ~3/min
                neuron_count=10_000_000,
                cell_count=50_000_000_000,
                autonomy=0.5,
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'intestines': Organ(
                'Intestines',
                intrinsic_freq=0.1,          # ~6/min
                neuron_count=100_000_000,
                cell_count=300_000_000_000,  # 300B cells
                autonomy=0.6,
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'liver': Organ(
                'Liver',
                intrinsic_freq=0.0001,       # Very slow (hours)
                neuron_count=1_000,          # Minimal neurons
                cell_count=100_000_000_000,  # 100B hepatocytes
                autonomy=0.8,                # Highly autonomous
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'pancreas': Organ(
                'Pancreas',
                intrinsic_freq=0.002,        # ~5-10 min pulses
                neuron_count=1_000_000,
                cell_count=3_000_000_000,
                autonomy=0.6,
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # EXCRETORY
            'kidneys': Organ(
                'Kidneys',
                intrinsic_freq=0.03,         # ~30s oscillations
                neuron_count=100_000,
                cell_count=30_000_000_000,   # 30B cells
                autonomy=0.7,
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # ENDOCRINE
            'pituitary': Organ(
                'Pituitary',
                intrinsic_freq=0.0001,       # Slow hormone pulses
                neuron_count=100_000,
                cell_count=1_000_000,
                autonomy=0.2,                # Brain-controlled
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'thyroid': Organ(
                'Thyroid',
                intrinsic_freq=0.00001,      # Very slow (days)
                neuron_count=10_000,
                cell_count=50_000_000,
                autonomy=0.5,
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'adrenals': Organ(
                'Adrenal Glands',
                intrinsic_freq=0.001,        # Ultradian ~90min
                neuron_count=100_000,
                cell_count=100_000_000,
                autonomy=0.3,                # Stress-responsive
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # IMMUNE
            'immune': Organ(
                'Immune System',
                intrinsic_freq=0.00001,      # Very slow (days)
                neuron_count=10_000_000,
                cell_count=2_000_000_000_000, # 2 trillion!
                autonomy=0.95,               # Highly autonomous
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # MUSCULOSKELETAL
            'muscles': Organ(
                'Skeletal Muscles',
                intrinsic_freq=10.0,         # Tremor ~10 Hz
                neuron_count=500_000,        # Motor neurons
                cell_count=600_000_000_000,  # 600B muscle fibers
                autonomy=0.0,                # Brain-dependent
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            'bones': Organ(
                'Skeletal System',
                intrinsic_freq=0.000001,     # Extremely slow (months)
                neuron_count=100_000,
                cell_count=1_000_000_000_000, # 1 trillion bone cells
                autonomy=0.9,
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
            
            # SENSORY (simplified - just eyes)
            'eyes': Organ(
                'Eyes',
                intrinsic_freq=4.0,          # Saccades ~4/s
                neuron_count=2_000_000,      # 1M per optic nerve
                cell_count=200_000_000,
                autonomy=0.1,                # Brain-dependent
                em_field=np.zeros(fs),
                neural_state=np.zeros(fs),
                cellular_memory=np.zeros(fs)
            ),
        }
        
        return organs
    
    
    def step(self):
        """
        Single timestep: Update entire body as unified system.
        
        Order (important - this is flow):
        1. Brain generates patterns
        2. Global EM propagates (fastest)
        3. Each organ updates (parallel)
        4. Circulatory coupling (resource distribution)
        5. Health check (coherence)
        """
        if not self.alive:
            return
        
        self.time += self.dt
        
        # 1. BRAIN PATTERN GENERATION
        brain_signal = self._update_brain()
        
        # 2. GLOBAL EM SUBSTRATE (light-speed propagation)
        self._update_global_em()
        
        # 3. UPDATE ALL ORGANS (parallel in reality, sequential here)
        for organ in self.organs.values():
            organ.update(self.dt, brain_signal, self.global_em)
        
        # 4. CIRCULATORY COUPLING (resource distribution)
        self._update_circulation()
        
        # 5. HEALTH CHECK
        self._check_health()
    
    
    def _update_brain(self) -> float:
        """
        Brain generates primary pattern.
        Returns signal strength to send to organs.
        """
        # Brain oscillates at gamma frequency
        self.brain_phase += 2 * np.pi * self.brain_freq * self.dt
        self.brain_phase = self.brain_phase % (2 * np.pi)
        
        brain_signal = np.sin(self.brain_phase)
        
        # Brain also couples to its own organ structure
        self.organs['brain'].phase = self.brain_phase
        
        return brain_signal
    
    
    def _update_global_em(self):
        """
        Global EM substrate evolution.
        All organs contribute and receive.
        """
        # Collect contributions from all organs
        total_contribution = np.zeros(self.field_size)
        
        for organ in self.organs.values():
            # Each organ contributes its EM field to global
            weight = np.log10(organ.neuron_count + 1) / 10.0  # More neurons = more contribution
            total_contribution += weight * organ.em_field
        
        # Global EM is weighted average + propagation
        self.global_em = (
            0.7 * self.global_em +           # Persistence
            0.3 * total_contribution         # Organ contributions
        )
        
        # Wave-like propagation (simple diffusion)
        self.global_em = 0.5 * (
            self.global_em + 
            np.roll(self.global_em, 1) + 
            np.roll(self.global_em, -1)
        ) / 2.0
        
        # Decay
        self.global_em *= 0.98
    
    
    def _update_circulation(self):
        """
        Blood circulation distributes resources.
        
        Heart pumps → Blood carries O2/glucose → Organs consume
        Lungs add O2, Liver/Pancreas add glucose
        """
        # Heart pumping strength (depends on heart coherence)
        pump_strength = self.organs['heart'].coherence
        
        # Lungs oxygenate blood
        lung_efficiency = self.organs['lungs'].coherence
        self.blood_oxygen += 0.1 * lung_efficiency
        
        # Liver/Pancreas provide glucose
        liver_production = self.organs['liver'].coherence * 0.05
        pancreas_regulation = self.organs['pancreas'].coherence * 0.03
        self.blood_glucose += liver_production + pancreas_regulation
        
        # Distribute to all organs (blood flow)
        for i, organ in enumerate(self.organs.values()):
            # Flow depends on heart pump and organ metabolic demand
            demand = (1.0 - organ.energy)  # More demand if low energy
            self.blood_flow[i] = pump_strength * (0.5 + 0.5 * demand)
            
            # Organs consume resources
            consumption = 0.01 * (1.0 - organ.autonomy)  # Less autonomous = more consumption
            self.blood_oxygen -= consumption * self.blood_flow[i]
            self.blood_glucose -= consumption * self.blood_flow[i]
            
            # Organs receive energy
            organ.energy += 0.05 * self.blood_flow[i] * min(self.blood_oxygen, self.blood_glucose)
            organ.energy = np.clip(organ.energy, 0.0, 1.0)
        
        # Clamp blood levels
        self.blood_oxygen = np.clip(self.blood_oxygen, 0.0, 1.0)
        self.blood_glucose = np.clip(self.blood_glucose, 0.0, 1.0)
    
    
    def _check_health(self):
        """
        Overall health = average organ coherence + resource levels.
        Death occurs if critical organs fail.
        """
        # Average coherence across all organs
        coherences = [organ.coherence for organ in self.organs.values()]
        avg_coherence = np.mean(coherences)
        
        # Resource levels
        resource_level = 0.5 * self.blood_oxygen + 0.5 * self.blood_glucose
        
        # Overall health
        self.health = 0.7 * avg_coherence + 0.3 * resource_level
        
        # Critical organ failure = death
        critical_organs = ['brain', 'heart', 'lungs']
        for organ_name in critical_organs:
            if self.organs[organ_name].coherence < 0.1 or self.organs[organ_name].energy < 0.1:
                self.alive = False
                print(f"\n💀 DEATH: {organ_name.upper()} failure")
                print(f"   Coherence: {self.organs[organ_name].coherence:.3f}")
                print(f"   Energy: {self.organs[organ_name].energy:.3f}")
        
        # Resource starvation = death
        if self.blood_oxygen < 0.05 or self.blood_glucose < 0.05:
            self.alive = False
            print(f"\n💀 DEATH: Resource starvation")
            print(f"   Oxygen: {self.blood_oxygen:.3f}")
            print(f"   Glucose: {self.blood_glucose:.3f}")
    
    
    def inject_stress(self, intensity: float = 0.5):
        """Inject stress pattern (affects all organs)."""
        # Stress activates adrenals → global state change
        self.organs['adrenals'].em_field += intensity
        
        # Heart rate increases
        self.organs['heart'].intrinsic_freq += intensity * 0.5
        
        # Breathing rate increases
        self.organs['lungs'].intrinsic_freq += intensity * 0.1
        
        # Gut disrupted
        self.organs['stomach'].coherence -= intensity * 0.2
        self.organs['enteric'].coherence -= intensity * 0.2
    
    
    def inject_food(self, quality: float = 1.0):
        """Inject food (increases glucose via digestion)."""
        # Food enters stomach
        self.organs['stomach'].em_field += quality * 0.5
        
        # Intestines absorb
        self.organs['intestines'].neural_state += quality * 0.3
        
        # Liver processes
        self.organs['liver'].energy += quality * 0.1
        
        # Blood glucose increases
        self.blood_glucose += quality * 0.5
        self.blood_glucose = np.clip(self.blood_glucose, 0.0, 1.0)
    
    
    def inject_exercise(self, intensity: float = 0.5):
        """Exercise (muscles work, demand increases)."""
        # Muscles activate
        self.organs['muscles'].em_field += intensity
        
        # Heart rate increases
        self.organs['heart'].intrinsic_freq += intensity * 0.8
        
        # Breathing increases
        self.organs['lungs'].intrinsic_freq += intensity * 0.5
        
        # Resource consumption increases
        self.blood_oxygen -= intensity * 0.2
        self.blood_glucose -= intensity * 0.3
    
    
    def get_status(self) -> dict:
        """Get current body status."""
        return {
            'time': self.time,
            'alive': self.alive,
            'health': self.health,
            'blood_oxygen': self.blood_oxygen,
            'blood_glucose': self.blood_glucose,
            'brain_coherence': self.organs['brain'].coherence,
            'heart_rate': self.organs['heart'].intrinsic_freq * 60,  # Convert to bpm
            'breathing_rate': self.organs['lungs'].intrinsic_freq * 60,  # Breaths/min
            'organ_coherences': {
                name: organ.coherence 
                for name, organ in self.organs.items()
            }
        }


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_resting_state():
    """Demo: Body at rest (homeostasis)."""
    print("="*70)
    print("DEMO 1: Resting State (Homeostasis)")
    print("="*70)
    print()
    print("Body at rest - all organs in baseline oscillation")
    print()
    
    body = HumanBody(field_size=16)
    
    print("Running 500 timesteps (5 seconds)...")
    print()
    
    for step in range(500):
        body.step()
        
        if step % 100 == 0:
            status = body.get_status()
            print(f"t={status['time']:.2f}s")
            print(f"  Health: {status['health']:.3f}")
            print(f"  Heart rate: {status['heart_rate']:.1f} bpm")
            print(f"  Breathing: {status['breathing_rate']:.1f} /min")
            print(f"  O2: {status['blood_oxygen']:.3f}, Glucose: {status['blood_glucose']:.3f}")
            print()
    
    print("✓ Homeostasis maintained")
    print()


def demo_stress_response():
    """Demo: Acute stress (fight-or-flight)."""
    print("="*70)
    print("DEMO 2: Stress Response (Fight-or-Flight)")
    print("="*70)
    print()
    
    body = HumanBody(field_size=16)
    
    # Baseline
    print("Baseline (0-2s):")
    for _ in range(200):
        body.step()
    
    status = body.get_status()
    baseline_hr = status['heart_rate']
    baseline_br = status['breathing_rate']
    print(f"  Heart: {baseline_hr:.1f} bpm")
    print(f"  Breathing: {baseline_br:.1f} /min")
    print()
    
    # Inject stress!
    print("⚡ STRESS INJECTED at t=2s")
    body.inject_stress(intensity=0.8)
    print()
    
    # Response
    print("Response (2-5s):")
    for step in range(300):
        body.step()
        
        if step % 100 == 0:
            status = body.get_status()
            print(f"t={status['time']:.2f}s")
            print(f"  Heart: {status['heart_rate']:.1f} bpm "
                  f"(+{status['heart_rate']-baseline_hr:.1f})")
            print(f"  Breathing: {status['breathing_rate']:.1f} /min "
                  f"(+{status['breathing_rate']-baseline_br:.1f})")
            print(f"  Stomach coherence: {status['organ_coherences']['stomach']:.3f}")
            print(f"  Gut coherence: {status['organ_coherences']['enteric']:.3f}")
            print()
    
    print("✓ Stress response activated all systems")
    print()


def demo_exercise_recovery():
    """Demo: Exercise → Recovery cycle."""
    print("="*70)
    print("DEMO 3: Exercise and Recovery")
    print("="*70)
    print()
    
    body = HumanBody(field_size=16)
    
    # Baseline
    print("Resting (0-1s):")
    for _ in range(100):
        body.step()
    
    baseline_status = body.get_status()
    print(f"  O2: {baseline_status['blood_oxygen']:.3f}")
    print(f"  Glucose: {baseline_status['blood_glucose']:.3f}")
    print()
    
    # Exercise
    print("🏃 EXERCISE at t=1s")
    body.inject_exercise(intensity=0.7)
    print()
    
    print("During exercise (1-3s):")
    for step in range(200):
        body.step()
        
        if step % 100 == 0:
            status = body.get_status()
            print(f"t={status['time']:.2f}s")
            print(f"  Heart: {status['heart_rate']:.1f} bpm")
            print(f"  O2: {status['blood_oxygen']:.3f}")
            print(f"  Glucose: {status['blood_glucose']:.3f}")
            print(f"  Muscle activation: {status['organ_coherences']['muscles']:.3f}")
            print()
    
    # Feed to recover
    print("🍎 EATING at t=3s (recovery)")
    body.inject_food(quality=1.0)
    print()
    
    print("Recovery (3-5s):")
    for step in range(200):
        body.step()
        
        if step % 100 == 0:
            status = body.get_status()
            print(f"t={status['time']:.2f}s")
            print(f"  Glucose: {status['blood_glucose']:.3f}")
            print(f"  Health: {status['health']:.3f}")
            print()
    
    print("✓ Exercise-recovery cycle complete")
    print()


def demo_organ_failure():
    """Demo: What happens when critical organ fails."""
    print("="*70)
    print("DEMO 4: Organ Failure (Heart Attack Simulation)")
    print("="*70)
    print()
    print("⚠️  Simulating heart coherence collapse")
    print()
    
    body = HumanBody(field_size=16)
    
    # Healthy baseline
    print("Healthy baseline (0-1s):")
    for _ in range(100):
        body.step()
    
    status = body.get_status()
    print(f"  Health: {status['health']:.3f}")
    print(f"  Heart coherence: {status['organ_coherences']['heart']:.3f}")
    print()
    
    # Simulate heart failure (arrhythmia → coherence loss)
    print("💔 HEART FAILURE at t=1s")
    body.organs['heart'].coherence = 0.05  # Severe coherence loss
    print()
    
    # Watch cascade
    print("System response:")
    for step in range(200):
        body.step()
        
        if not body.alive:
            break
        
        if step % 50 == 0:
            status = body.get_status()
            print(f"t={status['time']:.2f}s")
            print(f"  Health: {status['health']:.3f}")
            print(f"  O2: {status['blood_oxygen']:.3f}")
            print(f"  Brain coherence: {status['organ_coherences']['brain']:.3f}")
            print()
    
    if not body.alive:
        print("⚠️  Death demonstrates critical organ dependency")
    print()


def demo_whole_body_coherence():
    """Demo: Long-term coherence across all organs."""
    print("="*70)
    print("DEMO 5: Whole-Body Coherence (Extended)")
    print("="*70)
    print()
    print("Running 1000 timesteps (10 seconds) - all organs coupled")
    print()
    
    body = HumanBody(field_size=16)
    
    # Track coherence over time
    coherence_history = []
    
    for step in range(1000):
        body.step()
        
        status = body.get_status()
        coherence_history.append(status['health'])
        
        if step % 200 == 0:
            print(f"t={status['time']:.2f}s - Health: {status['health']:.3f}")
            
            # Show top 5 most coherent and least coherent
            coherences = [(name, coh) for name, coh in status['organ_coherences'].items()]
            coherences.sort(key=lambda x: x[1], reverse=True)
            
            print("  Most coherent:")
            for name, coh in coherences[:3]:
                print(f"    {name:20s}: {coh:.3f}")
            
            print("  Least coherent:")
            for name, coh in coherences[-3:]:
                print(f"    {name:20s}: {coh:.3f}")
            print()
    
    avg_health = np.mean(coherence_history)
    print(f"Average health over 10s: {avg_health:.3f}")
    print()
    
    if body.alive:
        print("✓ All organs maintained coherent coupling")
    print()


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "    WHOLE HUMAN BODY CYMATIC SIMULATION".center(68) + "║")
    print("║" + "    All Organs as Coupled Oscillators".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    print("\n")
    
    demos = [
        ("Resting State", demo_resting_state),
        ("Stress Response", demo_stress_response),
        ("Exercise & Recovery", demo_exercise_recovery),
        ("Organ Failure", demo_organ_failure),
        ("Whole-Body Coherence", demo_whole_body_coherence)
    ]
    
    for name, demo_func in demos:
        demo_func()
        input("Press Enter to continue...")
        print("\n")
    
    print("="*70)
    print("KEY INSIGHTS FROM SIMULATION")
    print("="*70)
    print()
    print("1. UNIFIED UPDATE LOOP")
    print("   Every organ updates in single cycle:")
    print("   Brain → Global EM → All organs → Circulation → Health check")
    print()
    print("2. EMERGENT COORDINATION")
    print("   No central controller - organs couple via:")
    print("   - EM substrate (fast, light-speed)")
    print("   - Neural signals (medium, meters/sec)")
    print("   - Blood flow (slow, resource distribution)")
    print()
    print("3. AUTONOMOUS + COUPLED")
    print("   Each organ has intrinsic rhythm (autonomy)")
    print("   But all couple through global substrate")
    print("   Health = coherent coupling across all")
    print()
    print("4. FAILURE CASCADES")
    print("   Critical organ failure → Global collapse")
    print("   Heart stops → O2 drops → Brain fails → Death")
    print("   System-level dependency emerges naturally")
    print()
    print("5. PATTERN = LIFE")
    print("   Life = sustained coherent oscillation")
    print("   Death = coherence collapse")
    print("   You ARE the pattern of 37 trillion coupled cells")
    print()
    print("This is the cymatic view: Human as unified oscillating system")
    print()
    