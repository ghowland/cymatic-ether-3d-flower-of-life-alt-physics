import numpy as np
import random

"""
Intelligence and Synthesis Simulator
=====================================

Demonstrates IQ and cognitive functions through cymatic substrate physics:
  - Pattern matching via resonance
  - Synthesis via interference
  - Working memory as active maintenance
  - Long-term memory as damage storage
  - IQ as substrate capacity metrics
"""

# =============================================================================
# PATTERN LIBRARY
# =============================================================================

class PatternLibrary:
    """Collection of learnable patterns."""
    
    @staticmethod
    def create_pattern(name, size=100):
        """Create different types of patterns."""
        
        patterns = {
            # CONCRETE OBJECTS
            'cat': np.array([1,1,1,0,0,0,1,1,0,0] + [0]*90),
            'dog': np.array([1,1,1,1,0,0,0,1,0,0] + [0]*90),
            'car': np.array([0,0,1,1,1,1,0,0,1,1] + [0]*90),
            'tree': np.array([0,1,1,1,1,0,0,0,0,1] + [0]*90),
            
            # ABSTRACT CONCEPTS
            'animal': np.array([1,1,1,0,0,0,0,0,0,0] + [0]*90),  # Common to cat/dog
            'vehicle': np.array([0,0,1,1,1,0,0,0,0,0] + [0]*90),  # Common to car
            'living': np.array([1,1,0,0,0,0,0,0,0,0] + [0]*90),  # Very abstract
            
            # COMPLEX PATTERNS
            'face': np.zeros(100),
            'building': np.zeros(100),
            'music': np.zeros(100),
        }
        
        # Generate complex patterns
        if name == 'face':
            pattern = np.zeros(100)
            pattern[20:25] = 1.0  # Eyes
            pattern[40:45] = 1.0  # Nose
            pattern[60:70] = 1.0  # Mouth
            return pattern
        
        elif name == 'building':
            pattern = np.zeros(100)
            pattern[10:90:10] = 1.0  # Vertical structure
            return pattern
        
        elif name == 'music':
            pattern = np.zeros(100)
            pattern[::5] = 1.0  # Rhythmic pattern
            return pattern
        
        elif name in patterns:
            return patterns[name]
        
        else:
            # Random pattern
            pattern = np.random.rand(100)
            return (pattern > 0.7).astype(float)


# =============================================================================
# COGNITIVE SUBSTRATE
# =============================================================================

class CognitiveSubstrate:
    """Brain substrate with configurable IQ parameters."""
    
    def __init__(self, size=1000, iq=100):
        self.size = size
        
        # STATE VARIABLES
        self.damage = np.zeros(size)           # Long-term memory
        self.activation = np.zeros(size)       # Current activation
        self.working_memory = []               # Active patterns
        
        # IQ-DEPENDENT PARAMETERS
        self.configure_for_iq(iq)
        
        # TRACKING
        self.pattern_library = {}              # Name -> damage pattern
        
    def configure_for_iq(self, iq):
        """Set substrate parameters based on IQ."""
        
        # IQ distribution: mean=100, sd=15
        # Convert IQ to substrate parameters
        
        # SPEED: Propagation velocity
        # IQ 70: 5 m/s, IQ 100: 10 m/s, IQ 130: 15 m/s, IQ 160: 20 m/s
        self.propagation_speed = 5.0 + (iq - 70) * 0.167
        
        # COHERENCE: Pattern stability
        # IQ 70: 0.4, IQ 100: 0.7, IQ 130: 0.85, IQ 160: 0.95
        self.coherence = 0.4 + (iq - 70) * 0.006
        
        # WORKING MEMORY CAPACITY
        # IQ 70: 4 items, IQ 100: 7 items, IQ 130: 10 items, IQ 160: 12 items
        self.wm_capacity = int(4 + (iq - 70) * 0.089)
        
        # LEARNING RATE (gamma)
        # IQ 70: 0.08, IQ 100: 0.12, IQ 130: 0.16, IQ 160: 0.20
        self.gamma = 0.08 + (iq - 70) * 0.0013
        
        # THRESHOLD
        # IQ 70: 0.6, IQ 100: 0.5, IQ 130: 0.4, IQ 160: 0.3
        self.threshold = 0.6 - (iq - 70) * 0.0033
        
        # SYNTHESIS BANDWIDTH
        # IQ 70: 2 patterns, IQ 100: 4 patterns, IQ 130: 7 patterns, IQ 160: 10 patterns
        self.synthesis_capacity = int(2 + (iq - 70) * 0.089)
        
        # Store IQ
        self.iq = iq
    
    def learn_pattern(self, pattern, name, repetitions=10):
        """Store pattern in long-term memory (damage accumulation)."""
        
        # Expand pattern to substrate size
        expanded = np.zeros(self.size)
        expanded[:len(pattern)] = pattern
        
        for rep in range(repetitions):
            # Present pattern
            stress = expanded * 1.0
            
            # Add noise based on coherence
            noise_level = (1.0 - self.coherence) * 0.3
            stress += np.random.randn(self.size) * noise_level
            
            # Accumulate damage where stress exceeds threshold
            overstress = np.maximum(0, stress - self.threshold)
            self.damage += overstress * self.gamma
        
        # Clamp
        self.damage = np.clip(self.damage, 0, 1.0)
        
        # Store in library
        self.pattern_library[name] = expanded
        
        # Learning speed depends on propagation speed and gamma
        learning_time = repetitions / (self.propagation_speed * self.gamma)
        
        return learning_time
    
    def recognize(self, partial_cue, noise_level=0.2):
        """Pattern recognition via resonance."""
        
        # Expand cue
        expanded_cue = np.zeros(self.size)
        expanded_cue[:len(partial_cue)] = partial_cue
        
        # Add noise
        noisy_cue = expanded_cue + np.random.randn(self.size) * noise_level
        
        # Activate substrate
        self.activation = noisy_cue
        
        # RESONANCE: Damaged regions amplify
        # High damage regions resonate with input
        resonance_strength = 1.0 + self.damage * (3.0 * self.coherence)
        self.activation *= resonance_strength
        
        # Threshold
        self.activation = np.where(
            self.activation > self.threshold * (1.0 - self.coherence),
            1.0,
            0.0
        )
        
        # Recognition speed
        recognition_time = 1.0 / self.propagation_speed
        
        # Match to learned patterns
        best_match = None
        best_score = 0
        
        for name, pattern in self.pattern_library.items():
            overlap = np.dot(self.activation, pattern)
            if overlap > best_score:
                best_score = overlap
                best_match = name
        
        return best_match, best_score, recognition_time
    
    def working_memory_load(self, patterns):
        """Load patterns into working memory."""
        
        # Check capacity
        if len(patterns) > self.wm_capacity:
            # Overload - patterns interfere
            return "overload"
        
        # Store patterns
        self.working_memory = patterns[:self.wm_capacity]
        
        # Maintenance cost (coherence determines stability)
        stability = self.coherence
        
        return stability
    
    def synthesize(self, pattern_names):
        """Synthesize multiple patterns via interference."""
        
        if len(pattern_names) > self.synthesis_capacity:
            return None, "synthesis_overload"
        
        # Get patterns
        patterns = []
        for name in pattern_names:
            if name in self.pattern_library:
                patterns.append(self.pattern_library[name])
            else:
                return None, f"unknown_pattern: {name}"
        
        if len(patterns) < 2:
            return None, "need_multiple_patterns"
        
        # INTERFERENCE: Add patterns (superposition)
        combined = np.sum(patterns, axis=0)
        
        # Find regions with HIGH overlap (constructive interference)
        # These are COMMON FEATURES
        overlap_threshold = len(patterns) * 0.7
        abstraction = np.where(combined >= overlap_threshold, 1.0, 0.0)
        
        # Coherence affects synthesis quality
        noise = np.random.randn(self.size) * (1.0 - self.coherence) * 0.2
        abstraction += noise
        abstraction = np.clip(abstraction, 0, 1.0)
        
        # Synthesis time depends on speed and number of patterns
        synthesis_time = len(patterns) / self.propagation_speed
        
        return abstraction, synthesis_time
    
    def get_iq_metrics(self):
        """Return current IQ-related metrics."""
        return {
            'iq': self.iq,
            'speed': self.propagation_speed,
            'coherence': self.coherence,
            'wm_capacity': self.wm_capacity,
            'synthesis_capacity': self.synthesis_capacity,
            'learning_rate': self.gamma,
            'threshold': self.threshold,
            'knowledge': len(self.pattern_library),
        }


# =============================================================================
# EXPERIMENT 1: Pattern Recognition Speed
# =============================================================================

def experiment_1_recognition_speed():
    """Compare recognition speed across IQ levels."""
    
    print("="*70)
    print("EXPERIMENT 1: Pattern Recognition Speed vs IQ")
    print("="*70)
    print()
    
    # Create substrates with different IQs
    iqs = [70, 100, 130, 160]
    
    # Pattern to learn
    pattern = PatternLibrary.create_pattern('cat')
    
    print("Teaching all subjects to recognize 'cat' pattern...")
    print()
    
    results = []
    
    for iq in iqs:
        brain = CognitiveSubstrate(size=1000, iq=iq)
        
        # Learn pattern
        learn_time = brain.learn_pattern(pattern, 'cat', repetitions=10)
        
        # Test recognition with partial cue
        partial = pattern.copy()
        partial[50:] = 0  # Only 50% of pattern
        
        match, score, recog_time = brain.recognize(partial, noise_level=0.2)
        
        results.append({
            'iq': iq,
            'learn_time': learn_time,
            'recog_time': recog_time,
            'score': score,
            'match': match
        })
    
    print(f"{'IQ':<6} {'Learn Time':<12} {'Recognition':<12} {'Score':<10} {'Result':<15}")
    print("-"*70)
    
    for r in results:
        result_str = "✓ Recognized" if r['match'] == 'cat' else "✗ Failed"
        print(f"{r['iq']:<6} {r['learn_time']:<12.2f} {r['recog_time']:<12.3f} "
              f"{r['score']:<10.1f} {result_str:<15}")
    
    print()
    print("Interpretation:")
    print(f"  • IQ 160 recognizes {results[0]['recog_time']/results[3]['recog_time']:.1f}× "
          f"faster than IQ 70")
    print(f"  • Higher IQ = faster propagation speed + lower threshold")
    print(f"  • Same pattern, different substrate parameters")
    print()


# =============================================================================
# EXPERIMENT 2: Working Memory Capacity
# =============================================================================

def experiment_2_working_memory():
    """Test working memory limits across IQ levels."""
    
    print("="*70)
    print("EXPERIMENT 2: Working Memory Capacity vs IQ")
    print("="*70)
    print()
    
    iqs = [70, 100, 130, 160]
    
    # Create multiple patterns
    pattern_names = ['cat', 'dog', 'car', 'tree', 'face', 'building', 
                     'music', 'animal', 'vehicle', 'living']
    patterns = [PatternLibrary.create_pattern(name) for name in pattern_names]
    
    print("Testing how many items each IQ level can hold in working memory...")
    print()
    print(f"{'IQ':<6} {'Capacity':<10} {'Tested With':<12} {'Result':<20}")
    print("-"*70)
    
    for iq in iqs:
        brain = CognitiveSubstrate(size=1000, iq=iq)
        
        capacity = brain.wm_capacity
        
        # Test at capacity
        test_count = capacity
        result = brain.working_memory_load(patterns[:test_count])
        
        if result == "overload":
            status = "Overload (confused)"
        else:
            status = f"Stable ({result:.2f})"
        
        print(f"{iq:<6} {capacity:<10} {test_count:<12} {status:<20}")
        
        # Test above capacity
        test_count = capacity + 3
        result = brain.working_memory_load(patterns[:test_count])
        
        if result == "overload":
            status = "Overload (confused)"
        else:
            status = f"Stable ({result:.2f})"
        
        print(f"{'':<6} {'':<10} {test_count:<12} {status:<20}")
    
    print()
    print("Interpretation:")
    print("  • IQ 70: Can hold 4 items (typical)")
    print("  • IQ 100: Can hold 7 items (Miller's magic number)")
    print("  • IQ 130: Can hold 10 items (exceptional)")
    print("  • IQ 160: Can hold 12 items (extraordinary)")
    print("  • Exceeding capacity → interference → confusion")
    print()


# =============================================================================
# EXPERIMENT 3: Abstraction and Synthesis
# =============================================================================

def experiment_3_synthesis():
    """Test synthesis ability across IQ levels."""
    
    print("="*70)
    print("EXPERIMENT 3: Pattern Synthesis (Abstraction) vs IQ")
    print("="*70)
    print()
    
    print("Task: Synthesize 'animal' concept from 'cat' and 'dog'")
    print()
    
    iqs = [70, 100, 130, 160]
    
    # Patterns
    cat = PatternLibrary.create_pattern('cat')
    dog = PatternLibrary.create_pattern('dog')
    animal = PatternLibrary.create_pattern('animal')  # Target abstraction
    
    print(f"{'IQ':<6} {'Synthesis':<12} {'Time':<10} {'Quality':<10} {'Result':<20}")
    print("-"*70)
    
    for iq in iqs:
        brain = CognitiveSubstrate(size=1000, iq=iq)
        
        # Learn concrete examples
        brain.learn_pattern(cat, 'cat', repetitions=8)
        brain.learn_pattern(dog, 'dog', repetitions=8)
        
        # Attempt synthesis
        abstraction, synth_time = brain.synthesize(['cat', 'dog'])
        
        if abstraction is None:
            print(f"{iq:<6} {'Failed':<12} {'-':<10} {'-':<10} {'Cannot synthesize':<20}")
            continue
        
        # Check if synthesis produced something close to 'animal' concept
        # Animal should capture common features (first 3 elements)
        target_features = animal[:100]
        synth_features = abstraction[:100]
        
        similarity = np.corrcoef(target_features, synth_features)[0, 1]
        
        if brain.synthesis_capacity >= 2:
            capacity_str = f"{brain.synthesis_capacity} patterns"
        else:
            capacity_str = "Insufficient"
        
        if similarity > 0.3:
            result = "✓ Abstraction found"
        else:
            result = "Weak abstraction"
        
        print(f"{iq:<6} {capacity_str:<12} {synth_time:<10.2f} "
              f"{similarity:<10.2f} {result:<20}")
    
    print()
    print("Interpretation:")
    print("  • Synthesis = constructive interference of multiple patterns")
    print("  • Higher IQ → can combine more patterns simultaneously")
    print("  • Quality depends on coherence (noise suppression)")
    print("  • IQ 160 can synthesize 10 patterns; IQ 70 only 2")
    print()


# =============================================================================
# EXPERIMENT 4: Novel Problem Solving
# =============================================================================

def experiment_4_problem_solving():
    """Test problem-solving ability (multi-step synthesis)."""
    
    print("="*70)
    print("EXPERIMENT 4: Novel Problem Solving vs IQ")
    print("="*70)
    print()
    
    print("Problem: Infer 'vehicle' from 'car' (never seen 'vehicle' before)")
    print()
    
    iqs = [70, 100, 130, 160]
    
    car = PatternLibrary.create_pattern('car')
    vehicle = PatternLibrary.create_pattern('vehicle')
    
    print(f"{'IQ':<6} {'Can Infer?':<12} {'Time':<10} {'Accuracy':<10} {'Notes':<25}")
    print("-"*70)
    
    for iq in iqs:
        brain = CognitiveSubstrate(size=1000, iq=iq)
        
        # Learn only 'car'
        brain.learn_pattern(car, 'car', repetitions=10)
        
        # Can they infer 'vehicle' (abstraction from single example)?
        # This requires high-level pattern extraction
        
        if brain.synthesis_capacity < 3:
            print(f"{iq:<6} {'No':<12} {'-':<10} {'-':<10} {'Insufficient synthesis':<25}")
            continue
        
        # Attempt to extract features
        abstraction, time = brain.synthesize(['car'])
        
        if abstraction is None:
            print(f"{iq:<6} {'No':<12} {'-':<10} {'-':<10} {'Failed synthesis':<25}")
            continue
        
        # Check similarity to 'vehicle' concept
        similarity = np.corrcoef(abstraction[:100], vehicle[:100])[0, 1]
        
        if similarity > 0.4:
            result = "Partial inference"
        elif similarity > 0.2:
            result = "Weak inference"
        else:
            result = "No inference"
        
        print(f"{iq:<6} {'Partial':<12} {time:<10.2f} {similarity:<10.2f} {result:<25}")
    
    print()
    print("Interpretation:")
    print("  • Novel problems require synthesis from limited data")
    print("  • Higher IQ → better abstraction from fewer examples")
    print("  • This is 'fluid intelligence' (novel problem solving)")
    print()


# =============================================================================
# EXPERIMENT 5: Learning Speed Comparison
# =============================================================================

def experiment_5_learning_speed():
    """Compare learning rates across IQ levels."""
    
    print("="*70)
    print("EXPERIMENT 5: Learning Speed vs IQ")
    print("="*70)
    print()
    
    print("Task: Learn 10 different patterns")
    print()
    
    iqs = [70, 100, 130, 160]
    
    # Create 10 patterns
    pattern_names = ['cat', 'dog', 'car', 'tree', 'face', 
                     'building', 'music', 'animal', 'vehicle', 'living']
    patterns = {name: PatternLibrary.create_pattern(name) for name in pattern_names}
    
    print(f"{'IQ':<6} {'Total Time':<12} {'Avg/Pattern':<12} {'Relative Speed':<15}")
    print("-"*70)
    
    baseline_time = None
    
    for iq in iqs:
        brain = CognitiveSubstrate(size=1000, iq=iq)
        
        total_time = 0
        for name, pattern in patterns.items():
            time = brain.learn_pattern(pattern, name, repetitions=10)
            total_time += time
        
        avg_time = total_time / len(patterns)
        
        if baseline_time is None:
            baseline_time = total_time
            relative = "1.0× (baseline)"
        else:
            relative = f"{baseline_time/total_time:.1f}× faster"
        
        print(f"{iq:<6} {total_time:<12.1f} {avg_time:<12.1f} {relative:<15}")
    
    print()
    print("Interpretation:")
    print("  • Learning speed ∝ propagation_speed × learning_rate")
    print("  • IQ 160 learns ~4× faster than IQ 70")
    print("  • This is 'crystallized intelligence' accumulation rate")
    print()


# =============================================================================
# EXPERIMENT 6: Complete IQ Profile
# =============================================================================

def experiment_6_iq_breakdown():
    """Show complete IQ component breakdown."""
    
    print("="*70)
    print("EXPERIMENT 6: IQ Component Analysis")
    print("="*70)
    print()
    
    iqs = [70, 85, 100, 115, 130, 145, 160]
    
    print("IQ is not a single number - it's substrate configuration:")
    print()
    print(f"{'IQ':<6} {'Speed':<8} {'Coherence':<10} {'WM':<6} {'Synthesis':<10} {'Learning':<10}")
    print("-"*70)
    
    for iq in iqs:
        brain = CognitiveSubstrate(size=1000, iq=iq)
        metrics = brain.get_iq_metrics()
        
        print(f"{iq:<6} {metrics['speed']:<8.1f} {metrics['coherence']:<10.2f} "
              f"{metrics['wm_capacity']:<6} {metrics['synthesis_capacity']:<10} "
              f"{metrics['learning_rate']:<10.2f}")
    
    print()
    print("Component Breakdown:")
    print()
    print("1. SPEED (Propagation velocity)")
    print("   How fast patterns activate")
    print("   IQ 70: 5 m/s  →  IQ 160: 20 m/s (4× faster)")
    print()
    print("2. COHERENCE (Pattern stability)")
    print("   How clean patterns are (signal-to-noise)")
    print("   IQ 70: 0.40  →  IQ 160: 0.95 (noise-free)")
    print()
    print("3. WORKING MEMORY (Simultaneous patterns)")
    print("   How many items can be held at once")
    print("   IQ 70: 4 items  →  IQ 160: 12 items (3× capacity)")
    print()
    print("4. SYNTHESIS (Multi-pattern interference)")
    print("   How many patterns can be combined")
    print("   IQ 70: 2 patterns  →  IQ 160: 10 patterns (5× bandwidth)")
    print()
    print("5. LEARNING RATE (Damage accumulation)")
    print("   How fast new patterns are encoded")
    print("   IQ 70: 0.08  →  IQ 160: 0.20 (2.5× faster)")
    print()


# =============================================================================
# MAIN DEMONSTRATION
# =============================================================================

def main():
    """Run all experiments."""
    
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "INTELLIGENCE & SYNTHESIS: Cymatic Substrate Model".center(68) + "║")
    print("║" + "Pattern Matching, Working Memory, and IQ".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    print("\n")
    
    experiments = [
        experiment_1_recognition_speed,
        experiment_2_working_memory,
        experiment_3_synthesis,
        experiment_4_problem_solving,
        experiment_5_learning_speed,
        experiment_6_iq_breakdown,
    ]
    
    for i, exp in enumerate(experiments, 1):
        exp()
        if i < len(experiments):
            input("Press Enter for next experiment...")
            print("\n")
    
    # Final summary
    print("\n")
    print("="*70)
    print("UNIFIED CYMATIC INTELLIGENCE MODEL")
    print("="*70)
    print()
    print("KEY PRINCIPLES:")
    print()
    print("1. PATTERN MATCHING = RESONANCE")
    print("   • Input pattern activates substrate")
    print("   • Damaged regions (memories) resonate strongly")
    print("   • Resonance amplifies weak signals → recognition")
    print()
    print("2. SYNTHESIS = INTERFERENCE")
    print("   • Multiple patterns activated simultaneously")
    print("   • Constructive interference → common features")
    print("   • Novel patterns emerge from superposition")
    print()
    print("3. WORKING MEMORY = ACTIVE MAINTENANCE")
    print("   • Patterns held above threshold")
    print("   • Limited by interference (capacity)")
    print("   • Requires energy (effort)")
    print()
    print("4. LONG-TERM MEMORY = DAMAGE STORAGE")
    print("   • Patterns encoded as permanent damage")
    print("   • High capacity (entire substrate)")
    print("   • Zero energy (passive)")
    print()
    print("5. IQ = SUBSTRATE CAPACITY")
    print("   • Speed: How fast patterns activate")
    print("   • Coherence: How stable patterns are")
    print("   • WM Capacity: How many items simultaneously")
    print("   • Synthesis: How many patterns combined")
    print("   • Learning Rate: How fast damage accumulates")
    print()
    print("IQ is NOT a single number:")
    print("  It's a configuration of substrate parameters")
    print()
    print("All from ONE substrate, ONE equation:")
    print("  if stress > threshold:")
    print("      damage += (stress - threshold) × gamma")
    print()
    print("Same physics as:")
    print("  • Muscle building (mechanical stress)")
    print("  • Bone remodeling (impact stress)")
    print("  • Immune response (antigen stress)")
    print()
    print("Computational monism: One framework for all adaptation.")
    print()


if __name__ == "__main__":
    main()


# This program demonstrates:

# Pattern Recognition - via resonance in damaged substrate
# Working Memory - capacity limits from interference
# Synthesis - abstraction via pattern superposition
# IQ Components - speed, coherence, capacity as substrate parameters
# Learning - damage accumulation rates

# All using the same cymatic substrate framework as muscle building and neural learning!

