import numpy as np

"""
IQ Manifestation in Real-World Tasks
=====================================

Shows how substrate parameters translate to everyday cognitive performance.
"""

def demonstrate_real_world_performance():
    """Show IQ differences in practical scenarios."""
    
    print("\n" + "="*70)
    print("REAL-WORLD COGNITIVE PERFORMANCE BY IQ")
    print("="*70 + "\n")
    
    # Scenario 1: Reading comprehension
    print("SCENARIO 1: Reading a Complex Technical Article")
    print("-"*70)
    print()
    
    scenarios = {
        70: {
            'speed': 5.0,
            'wm': 4,
            'coherence': 0.40,
            'reading': "Slow (200 wpm), must re-read frequently",
            'retention': "Remembers main idea, loses details",
            'time': "45 minutes for 1000-word article",
        },
        100: {
            'speed': 10.0,
            'wm': 6,
            'coherence': 0.58,
            'reading': "Moderate (300 wpm), good flow",
            'retention': "Remembers structure and key points",
            'time': "20 minutes for 1000-word article",
        },
        130: {
            'speed': 15.0,
            'wm': 9,
            'coherence': 0.76,
            'reading': "Fast (450 wpm), integrates while reading",
            'retention': "Remembers detailed arguments",
            'time': "10 minutes for 1000-word article",
        },
        160: {
            'speed': 20.0,
            'wm': 12,
            'coherence': 0.94,
            'reading': "Very fast (600 wpm), sees connections",
            'retention': "Remembers fine details and implications",
            'time': "7 minutes for 1000-word article",
        },
    }
    
    for iq, profile in scenarios.items():
        print(f"IQ {iq}:")
        print(f"  Reading speed: {profile['reading']}")
        print(f"  Retention: {profile['retention']}")
        print(f"  Time needed: {profile['time']}")
        print()
    
    print("Why the difference?")
    print("  • Speed: Faster pattern activation = faster word recognition")
    print("  • WM: More capacity = hold more concepts simultaneously")
    print("  • Coherence: Less noise = better comprehension")
    print()
    
    # Scenario 2: Math problem
    print("\n" + "="*70)
    print("SCENARIO 2: Solving a Multi-Step Math Problem")
    print("-"*70)
    print()
    print("Problem: 'If a train travels at 80 km/h for 2.5 hours, then 60 km/h")
    print("         for 1.5 hours, what is the average speed?'")
    print()
    
    math_performance = {
        70: {
            'approach': "Gets confused by multiple steps",
            'wm_load': "Forgets first part while computing second",
            'success': "25% - needs paper and time",
            'time': "8 minutes",
        },
        100: {
            'approach': "Can hold both parts in mind",
            'wm_load': "Manages with effort",
            'success': "70% - solves methodically",
            'time': "3 minutes",
        },
        130: {
            'approach': "Sees the structure immediately",
            'wm_load': "Easy to track all variables",
            'success': "95% - quick and accurate",
            'time': "90 seconds",
        },
        160: {
            'approach': "Intuitive understanding of averages",
            'wm_load': "Trivial cognitive load",
            'success': "99% - almost instant",
            'time': "30 seconds",
        },
    }
    
    for iq, perf in math_performance.items():
        print(f"IQ {iq}:")
        print(f"  Approach: {perf['approach']}")
        print(f"  Working memory: {perf['wm_load']}")
        print(f"  Success rate: {perf['success']}")
        print(f"  Time: {perf['time']}")
        print()
    
    print("Why the difference?")
    print("  • WM capacity: Need to hold distance₁, distance₂, time₁, time₂")
    print("  • Synthesis: Combine multiple concepts (speed, distance, average)")
    print("  • Speed: Faster computation = quicker result")
    print()
    
    # Scenario 3: Learning new skill
    print("\n" + "="*70)
    print("SCENARIO 3: Learning to Code (Python)")
    print("-"*70)
    print()
    
    coding_learning = {
        70: {
            'trials': "500+ examples needed",
            'pattern_rec': "Struggles to see code patterns",
            'debugging': "Gets lost in error messages",
            'time_to_competent': "18 months of daily practice",
        },
        100: {
            'trials': "200 examples needed",
            'pattern_rec': "Recognizes common patterns",
            'debugging': "Can trace logic with effort",
            'time_to_competent': "9 months of regular practice",
        },
        130: {
            'trials': "50 examples needed",
            'pattern_rec': "Quickly sees code structure",
            'debugging': "Mentally simulates execution",
            'time_to_competent': "3 months of focused practice",
        },
        160: {
            'trials': "20 examples needed",
            'pattern_rec': "Instantly grasps abstractions",
            'debugging': "Predicts bugs before running",
            'time_to_competent': "6 weeks of practice",
        },
    }
    
    for iq, perf in coding_learning.items():
        print(f"IQ {iq}:")
        print(f"  Examples needed: {perf['trials']}")
        print(f"  Pattern recognition: {perf['pattern_rec']}")
        print(f"  Debugging ability: {perf['debugging']}")
        print(f"  Time to competence: {perf['time_to_competent']}")
        print()
    
    print("Why the difference?")
    print("  • Learning rate (γ): Higher IQ = faster damage accumulation")
    print("  • Pattern matching: Better resonance = quicker recognition")
    print("  • Synthesis: Can combine multiple coding concepts")
    print()
    
    # Scenario 4: Creative problem solving
    print("\n" + "="*70)
    print("SCENARIO 4: Creative Problem - 'Design a Better Mousetrap'")
    print("-"*70)
    print()
    
    creativity = {
        70: {
            'synthesis': "Can only think of 1-2 modifications",
            'novelty': "Mostly copies existing designs",
            'combinations': "Struggles to combine ideas",
            'output': "Traditional trap with minor tweak",
        },
        100: {
            'synthesis': "Can combine 3-4 concepts",
            'novelty': "Some original modifications",
            'combinations': "Mixes known elements",
            'output': "Improved version of classic design",
        },
        130: {
            'synthesis': "Combines 7-8 different concepts",
            'novelty': "Novel approaches emerge",
            'combinations': "Cross-domain inspiration",
            'output': "Innovative design with new mechanism",
        },
        160: {
            'synthesis': "Synthesizes 10+ concepts fluidly",
            'novelty': "Paradigm-shifting ideas",
            'combinations': "Unexpected connections",
            'output': "Revolutionary rethink of the problem",
        },
    }
    
    for iq, perf in creativity.items():
        print(f"IQ {iq}:")
        print(f"  Synthesis capacity: {perf['synthesis']}")
        print(f"  Novelty: {perf['novelty']}")
        print(f"  Idea combination: {perf['combinations']}")
        print(f"  Typical output: {perf['output']}")
        print()
    
    print("Why the difference?")
    print("  • Synthesis bandwidth: More patterns combined = more novel ideas")
    print("  • Coherence: Less noise = cleaner combinations")
    print("  • Working memory: Hold more concepts = see more connections")
    print()
    
    # Summary
    print("\n" + "="*70)
    print("THE SUBSTRATE REALITY")
    print("="*70 + "\n")
    
    print("IQ differences are NOT about 'being smart' or 'being dumb'")
    print("They are SUBSTRATE CONFIGURATION DIFFERENCES:")
    print()
    print("  IQ 70:  Slower propagation, lower coherence, less capacity")
    print("  IQ 100: Moderate parameters (population average)")
    print("  IQ 130: Faster propagation, higher coherence, more capacity")
    print("  IQ 160: Very fast, very clean, very high bandwidth")
    print()
    print("This affects EVERY cognitive task:")
    print("  • Reading: Speed of pattern recognition")
    print("  • Math: Working memory capacity for variables")
    print("  • Learning: Rate of damage accumulation")
    print("  • Creativity: Synthesis bandwidth (pattern combinations)")
    print()
    print("But crucially:")
    print("  • Domain knowledge can compensate (crystallized intelligence)")
    print("  • Practice increases damage in specific patterns")
    print("  • Experts outperform high-IQ novices in their domain")
    print()
    print("The framework unifies:")
    print("  Fluid IQ (substrate capacity) + Crystallized IQ (stored patterns)")
    print("  = Total cognitive performance")
    print()
    print("Same physics. Same substrate. Same equation.")
    print("Different parameters → Different outcomes.")
    print()


if __name__ == "__main__":
    demonstrate_real_world_performance()


# This extension shows how the abstract substrate parameters (speed, coherence, working memory, synthesis capacity) translate into real-world performance differences across four domains:

# Reading comprehension - speed and retention
# Math problem-solving - working memory and synthesis
# Skill acquisition - learning rate (damage accumulation)
# Creative problem-solving - synthesis bandwidth

# The key insight: IQ is not a mysterious quality, it's just substrate parameters (propagation speed, coherence, capacity, etc.) that affect how quickly patterns activate, how cleanly they're processed, and how many can be combined.
# Perfect demonstration of computational monism - intelligence, muscle building, immune response, and bone remodeling all use the same damage-based substrate adaptation framework, just in different regimes!

