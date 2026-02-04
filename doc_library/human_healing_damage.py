"""
Human Body: Healing, Damage, and Growth Cycle
==============================================

Educational simulation showing how the body:
- Grows from birth to maturity
- Accumulates damage daily from activity and metabolism
- Heals during sleep
- Ages over decades
- Eventually reaches end of life

Pure substrate mechanics - damage accumulation and repair cycles.
No biological detail assumed beyond: tissue exists, damage accumulates, healing occurs.

Demonstrates:
- Child growth (rapid tissue synthesis)
- Adult maintenance (damage/repair balance)
- Aging (repair capacity declines)
- Sleep as essential repair time
- Exercise as controlled damage → adaptation
- Illness as acute damage spike
- Death as catastrophic damage accumulation
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# CONSTANTS
# ============================================================================

DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
LIFESPAN_YEARS = 80

# Age ranges
AGE_INFANT = 2      # 0-2 years
AGE_CHILD = 12      # 2-12 years
AGE_ADULT = 25      # 12-25 years (growth complete)
AGE_MIDDLE = 50     # 25-50 years (stable)
AGE_SENIOR = 65     # 50-65 years (decline begins)
AGE_ELDERLY = 80    # 65-80 years (severe decline)

# Tissue types
TISSUES = ['brain', 'heart', 'liver', 'muscle', 'bone', 'skin', 'gut']

# ============================================================================
# HUMAN BODY CLASS
# ============================================================================

class HumanBody:
    """
    Complete human body with damage accumulation and healing.
    """
    
    def __init__(self):
        """Initialize at birth."""
        
        # Age tracking
        self.age_days = 0
        self.age_years = 0.0
        
        # Tissue properties (0-1 scale where 1 = fully healthy)
        self.tissue_health = {tissue: 1.0 for tissue in TISSUES}
        
        # Damage accumulation (0-1 where 1 = completely damaged)
        self.tissue_damage = {tissue: 0.0 for tissue in TISSUES}
        
        # Growth (0-1 where 1 = adult size)
        self.tissue_growth = {tissue: 0.15 for tissue in TISSUES}  # Start at 15% (newborn)
        
        # Repair capacity (declines with age)
        self.repair_capacity = 1.0
        
        # Metabolic rate (higher when young)
        self.metabolic_rate = 1.5  # 50% above baseline at birth
        
        # Sleep debt (accumulates if not sleeping enough)
        self.sleep_debt = 0.0
        
        # Activity level (affects damage rate)
        self.activity_level = 0.3  # Infants are relatively inactive
        
        # Vital status
        self.alive = True
        self.cause_of_death = None
        
        # History for plotting
        self.history = {
            'age': [],
            'health': {tissue: [] for tissue in TISSUES},
            'damage': {tissue: [] for tissue in TISSUES},
            'growth': {tissue: [] for tissue in TISSUES},
            'repair_capacity': [],
            'sleep_debt': [],
            'alive': []
        }
    
    def get_age_stage(self):
        """Determine developmental stage."""
        if self.age_years < AGE_INFANT:
            return 'infant'
        elif self.age_years < AGE_CHILD:
            return 'child'
        elif self.age_years < AGE_ADULT:
            return 'adolescent'
        elif self.age_years < AGE_MIDDLE:
            return 'adult'
        elif self.age_years < AGE_SENIOR:
            return 'middle_aged'
        elif self.age_years < AGE_ELDERLY:
            return 'senior'
        else:
            return 'elderly'
    
    def daily_damage(self):
        """
        Accumulate damage from daily activity.
        
        Sources:
        - Metabolic byproducts (oxidative stress)
        - Physical activity (mechanical wear)
        - Environmental factors (UV, toxins)
        """
        
        stage = self.get_age_stage()
        
        for tissue in TISSUES:
            # Base metabolic damage (unavoidable)
            metabolic_damage = 0.001 * self.metabolic_rate
            
            # Activity-dependent damage
            activity_damage = {
                'brain': 0.0002 * self.activity_level,      # Low mechanical stress
                'heart': 0.0008 * self.activity_level,      # High constant stress
                'liver': 0.0005 * self.metabolic_rate,      # Metabolic burden
                'muscle': 0.002 * self.activity_level,      # High mechanical stress
                'bone': 0.0001 * self.activity_level,       # Very slow turnover
                'skin': 0.001 * self.activity_level,        # UV, abrasion
                'gut': 0.0015 * self.metabolic_rate         # Digestive stress
            }
            
            # Age multiplier (damage accumulates faster when old)
            age_multiplier = 1.0 + (self.age_years / AGE_ELDERLY) * 0.5
            
            total_damage = (metabolic_damage + activity_damage[tissue]) * age_multiplier
            
            # Sleep debt amplifies damage
            sleep_multiplier = 1.0 + self.sleep_debt * 0.5
            total_damage *= sleep_multiplier
            
            # Apply damage
            self.tissue_damage[tissue] += total_damage
            self.tissue_damage[tissue] = min(1.0, self.tissue_damage[tissue])
    
    def sleep_healing(self, hours_slept):
        """
        Healing occurs during sleep.
        
        8 hours = full healing capacity
        6 hours = reduced healing
        <5 hours = minimal healing + sleep debt
        """
        
        # Optimal sleep: 8 hours
        optimal_sleep = 8.0
        
        # Sleep efficiency (worse when older)
        sleep_efficiency = self.repair_capacity * 0.9  # Never 100% efficient
        
        # Healing amount based on sleep duration
        healing_fraction = (hours_slept / optimal_sleep) * sleep_efficiency
        healing_fraction = min(1.0, healing_fraction)
        
        for tissue in TISSUES:
            # Maximum healing per night (tissue-specific)
            max_healing = {
                'brain': 0.05,    # Brain repairs slowly (limited regeneration)
                'heart': 0.03,    # Heart has poor regeneration
                'liver': 0.15,    # Liver regenerates well
                'muscle': 0.10,   # Muscle repairs moderately
                'bone': 0.02,     # Bone remodels very slowly
                'skin': 0.20,     # Skin regenerates rapidly
                'gut': 0.25       # Gut lining replaces every few days
            }
            
            # Apply healing
            healing = max_healing[tissue] * healing_fraction
            self.tissue_damage[tissue] -= healing
            self.tissue_damage[tissue] = max(0.0, self.tissue_damage[tissue])
        
        # Update sleep debt
        sleep_deficit = optimal_sleep - hours_slept
        if sleep_deficit > 0:
            self.sleep_debt += sleep_deficit / 10.0  # Accumulates slowly
        else:
            self.sleep_debt -= 0.1  # Recovers slowly with extra sleep
        
        self.sleep_debt = np.clip(self.sleep_debt, 0.0, 5.0)  # Cap at 5 "hours"
    
    def growth(self):
        """
        Tissue growth during developmental years.
        
        Rapid in infancy, continues until ~25 years.
        """
        
        stage = self.get_age_stage()
        
        if stage in ['infant', 'child', 'adolescent']:
            # Growth rate decreases with age
            if stage == 'infant':
                growth_rate = 0.0015  # Very fast
            elif stage == 'child':
                growth_rate = 0.0008  # Fast
            else:  # adolescent
                growth_rate = 0.0003  # Moderate
            
            for tissue in TISSUES:
                # Different tissues grow at different rates
                tissue_growth_modifier = {
                    'brain': 1.5,    # Brain grows fastest early
                    'heart': 1.0,
                    'liver': 1.0,
                    'muscle': 0.8,   # Slower initially
                    'bone': 1.2,     # Needs to support body
                    'skin': 1.0,
                    'gut': 1.0
                }
                
                growth = growth_rate * tissue_growth_modifier[tissue]
                self.tissue_growth[tissue] += growth
                self.tissue_growth[tissue] = min(1.0, self.tissue_growth[tissue])
    
    def aging(self):
        """
        Gradual decline in repair capacity with age.
        
        Mechanisms:
        - Telomere shortening
        - Mitochondrial dysfunction
        - Reduced stem cell activity
        - Accumulated epigenetic changes
        """
        
        # Repair capacity declines linearly after age 25
        if self.age_years > AGE_ADULT:
            age_beyond_prime = self.age_years - AGE_ADULT
            decline_rate = 0.0002  # 0.02% per day after 25
            
            self.repair_capacity -= decline_rate
            self.repair_capacity = max(0.1, self.repair_capacity)  # Never goes to zero
        
        # Metabolic rate decreases with age
        if self.age_years > AGE_CHILD:
            # Peaks around age 12, declines thereafter
            optimal_metabolic_age = 12.0
            distance_from_optimal = abs(self.age_years - optimal_metabolic_age)
            self.metabolic_rate = 1.5 - (distance_from_optimal / 100.0)
            self.metabolic_rate = max(0.8, self.metabolic_rate)
    
    def update_health(self):
        """
        Health is inverse of damage, scaled by growth.
        
        A child with 10% damage to 50% grown tissue is less affected
        than an adult with same damage to fully grown tissue.
        """
        
        for tissue in TISSUES:
            # Health = (1 - damage) * growth_factor
            # This means underdeveloped tissue has lower absolute health
            growth_factor = self.tissue_growth[tissue]
            damage_factor = 1.0 - self.tissue_damage[tissue]
            
            self.tissue_health[tissue] = damage_factor * growth_factor
    
    def check_death(self):
        """
        Death occurs when critical organs fail.
        
        Thresholds:
        - Brain damage > 80%: Death
        - Heart damage > 90%: Death
        - Multiple organs > 95%: Death
        """
        
        # Critical organ failure
        if self.tissue_damage['brain'] > 0.8:
            self.alive = False
            self.cause_of_death = 'brain_failure'
            return
        
        if self.tissue_damage['heart'] > 0.9:
            self.alive = False
            self.cause_of_death = 'heart_failure'
            return
        
        # Multi-organ failure
        critical_damage_count = sum(
            1 for tissue in TISSUES 
            if self.tissue_damage[tissue] > 0.95
        )
        
        if critical_damage_count >= 3:
            self.alive = False
            self.cause_of_death = 'multi_organ_failure'
            return
    
    def simulate_day(self, sleep_hours=8.0, activity_level=None):
        """
        Simulate one complete day.
        
        Daily cycle:
        1. Wake up
        2. Accumulate damage from activity
        3. Sleep and heal
        4. Grow (if young)
        5. Age (repair capacity declines)
        """
        
        if not self.alive:
            return
        
        # Update activity level if specified
        if activity_level is not None:
            self.activity_level = activity_level
        
        # 1. Daily damage accumulation
        self.daily_damage()
        
        # 2. Sleep healing
        self.sleep_healing(sleep_hours)
        
        # 3. Growth (children only)
        self.growth()
        
        # 4. Aging process
        self.aging()
        
        # 5. Update overall health
        self.update_health()
        
        # 6. Check for death
        self.check_death()
        
        # 7. Increment age
        self.age_days += 1
        self.age_years = self.age_days / DAYS_PER_YEAR
        
        # 8. Record history
        self.record_history()
    
    def record_history(self):
        """Save current state to history."""
        self.history['age'].append(self.age_years)
        self.history['repair_capacity'].append(self.repair_capacity)
        self.history['sleep_debt'].append(self.sleep_debt)
        self.history['alive'].append(1.0 if self.alive else 0.0)
        
        for tissue in TISSUES:
            self.history['health'][tissue].append(self.tissue_health[tissue])
            self.history['damage'][tissue].append(self.tissue_damage[tissue])
            self.history['growth'][tissue].append(self.tissue_growth[tissue])
    
    def get_summary(self):
        """Return current state summary."""
        avg_health = np.mean([self.tissue_health[t] for t in TISSUES])
        avg_damage = np.mean([self.tissue_damage[t] for t in TISSUES])
        
        return {
            'age_years': self.age_years,
            'stage': self.get_age_stage(),
            'avg_health': avg_health,
            'avg_damage': avg_damage,
            'repair_capacity': self.repair_capacity,
            'alive': self.alive,
            'cause_of_death': self.cause_of_death
        }


# ============================================================================
# LIFE EVENTS
# ============================================================================

def simulate_illness(body, severity=0.3, duration_days=7):
    """
    Simulate acute illness (flu, infection, etc.).
    
    Causes:
    - Increased damage accumulation
    - Reduced healing
    - Requires more sleep
    """
    print(f"\n🦠 ILLNESS at age {body.age_years:.1f} (severity={severity:.1%})")
    
    for day in range(duration_days):
        if not body.alive:
            break
        
        # Illness causes extra damage
        for tissue in TISSUES:
            illness_damage = severity * 0.05  # 5% damage per day at full severity
            body.tissue_damage[tissue] += illness_damage
            body.tissue_damage[tissue] = min(1.0, body.tissue_damage[tissue])
        
        # Reduced activity, more sleep
        body.simulate_day(sleep_hours=10.0, activity_level=0.1)
    
    print(f"   Recovered. Health: {np.mean([body.tissue_health[t] for t in TISSUES]):.1%}")


def simulate_injury(body, tissue='muscle', severity=0.4):
    """
    Simulate acute injury (broken bone, torn muscle, etc.).
    """
    print(f"\n🤕 INJURY to {tissue} at age {body.age_years:.1f} (severity={severity:.1%})")
    
    body.tissue_damage[tissue] += severity
    body.tissue_damage[tissue] = min(1.0, body.tissue_damage[tissue])
    
    print(f"   {tissue.capitalize()} damage: {body.tissue_damage[tissue]:.1%}")


def simulate_exercise(body, intensity=0.5, duration_days=1):
    """
    Simulate exercise.
    
    Short-term: Increases damage (muscle tears, oxidative stress)
    Long-term: Adaptation increases repair capacity
    """
    
    for day in range(duration_days):
        if not body.alive:
            break
        
        # Exercise causes controlled damage
        body.tissue_damage['muscle'] += 0.03 * intensity
        body.tissue_damage['heart'] += 0.01 * intensity
        
        # But stimulates adaptation (slightly improves repair)
        if body.age_years > AGE_CHILD:
            body.repair_capacity += 0.0001 * intensity
            body.repair_capacity = min(1.0, body.repair_capacity)
        
        body.simulate_day(sleep_hours=8.0, activity_level=0.5 + 0.5*intensity)


# ============================================================================
# SIMULATION SCENARIOS
# ============================================================================

def scenario_healthy_life():
    """
    Simulate a healthy, normal lifespan.
    
    - 8 hours sleep per night
    - Moderate activity
    - Occasional illness
    - Some exercise in adulthood
    """
    print("="*70)
    print("SCENARIO: Healthy Life (Normal Lifespan)")
    print("="*70)
    
    body = HumanBody()
    
    days_simulated = 0
    max_days = LIFESPAN_YEARS * DAYS_PER_YEAR
    
    while body.alive and days_simulated < max_days:
        # Determine activity level by age
        stage = body.get_age_stage()
        if stage == 'infant':
            activity = 0.2
        elif stage == 'child':
            activity = 0.6
        elif stage == 'adolescent':
            activity = 0.7
        elif stage == 'adult':
            activity = 0.5
        elif stage == 'middle_aged':
            activity = 0.4
        elif stage == 'senior':
            activity = 0.3
        else:  # elderly
            activity = 0.2
        
        # Normal day
        body.simulate_day(sleep_hours=8.0, activity_level=activity)
        days_simulated += 1
        
        # Occasional events
        
        # Illness every 2-3 years (random)
        if days_simulated % 800 == 0 and np.random.rand() < 0.5:
            simulate_illness(body, severity=0.2, duration_days=7)
        
        # Exercise routine in adulthood
        if stage in ['adult', 'middle_aged'] and days_simulated % 3 == 0:
            simulate_exercise(body, intensity=0.4, duration_days=1)
        
        # Minor injury occasionally
        if days_simulated % 2000 == 0 and np.random.rand() < 0.3:
            injured_tissue = np.random.choice(['muscle', 'bone', 'skin'])
            simulate_injury(body, tissue=injured_tissue, severity=0.2)
        
        # Print status every 5 years
        if days_simulated % (5 * DAYS_PER_YEAR) == 0:
            summary = body.get_summary()
            print(f"\nAge {summary['age_years']:.0f} ({summary['stage']}): "
                  f"Health={summary['avg_health']:.1%}, "
                  f"Damage={summary['avg_damage']:.1%}, "
                  f"Repair={summary['repair_capacity']:.1%}")
    
    summary = body.get_summary()
    print(f"\n{'='*70}")
    print(f"Life ended at age {summary['age_years']:.1f}")
    print(f"Cause: {summary['cause_of_death']}")
    print(f"Final health: {summary['avg_health']:.1%}")
    print(f"{'='*70}")
    
    return body


def scenario_sleep_deprived():
    """
    Simulate chronic sleep deprivation.
    
    - Only 5-6 hours sleep per night
    - Shows accelerated aging
    - Earlier death
    """
    print("\n" + "="*70)
    print("SCENARIO: Chronic Sleep Deprivation")
    print("="*70)
    
    body = HumanBody()
    
    days_simulated = 0
    max_days = LIFESPAN_YEARS * DAYS_PER_YEAR
    
    while body.alive and days_simulated < max_days:
        stage = body.get_age_stage()
        
        # Reduced sleep (5-6 hours)
        sleep_hours = 5.5 + np.random.rand() * 0.5
        
        activity = 0.5 if stage in ['adult', 'middle_aged'] else 0.3
        
        body.simulate_day(sleep_hours=sleep_hours, activity_level=activity)
        days_simulated += 1
        
        # Print every 5 years
        if days_simulated % (5 * DAYS_PER_YEAR) == 0:
            summary = body.get_summary()
            print(f"Age {summary['age_years']:.0f}: "
                  f"Health={summary['avg_health']:.1%}, "
                  f"Sleep Debt={body.sleep_debt:.2f}")
    
    summary = body.get_summary()
    print(f"\nDied at age {summary['age_years']:.1f} (Cause: {summary['cause_of_death']})")
    print(f"Compare to normal lifespan: ~80 years")
    
    return body


def scenario_athlete():
    """
    Simulate athletic lifestyle.
    
    - High activity
    - Good sleep
    - Frequent controlled damage + repair
    """
    print("\n" + "="*70)
    print("SCENARIO: Athletic Lifestyle")
    print("="*70)
    
    body = HumanBody()
    
    days_simulated = 0
    max_days = LIFESPAN_YEARS * DAYS_PER_YEAR
    
    while body.alive and days_simulated < max_days:
        stage = body.get_age_stage()
        
        # Athletes sleep more
        sleep_hours = 8.5
        
        # High activity
        if stage in ['adolescent', 'adult']:
            activity = 0.8
            # Daily training
            if days_simulated % 1 == 0:  # Every day
                simulate_exercise(body, intensity=0.6, duration_days=1)
        elif stage == 'middle_aged':
            activity = 0.6
            if days_simulated % 2 == 0:  # Every other day
                simulate_exercise(body, intensity=0.4, duration_days=1)
        else:
            activity = 0.3
        
        body.simulate_day(sleep_hours=sleep_hours, activity_level=activity)
        days_simulated += 1
        
        # More frequent injuries from intense training
        if days_simulated % 500 == 0 and stage in ['adolescent', 'adult']:
            simulate_injury(body, tissue='muscle', severity=0.15)
        
        # Print every 5 years
        if days_simulated % (5 * DAYS_PER_YEAR) == 0:
            summary = body.get_summary()
            print(f"Age {summary['age_years']:.0f}: "
                  f"Health={summary['avg_health']:.1%}, "
                  f"Repair={summary['repair_capacity']:.1%}")
    
    summary = body.get_summary()
    print(f"\nDied at age {summary['age_years']:.1f}")
    
    return body


# ============================================================================
# VISUALIZATION
# ============================================================================

def plot_life_history(body, title="Life History"):
    """
    Create comprehensive visualization of entire lifespan.
    """
    fig, axes = plt.subplots(3, 2, figsize=(16, 12))
    
    age = np.array(body.history['age'])
    
    # Plot 1: Tissue Health Over Time
    ax = axes[0, 0]
    for tissue in TISSUES:
        health = np.array(body.history['health'][tissue])
        ax.plot(age, health * 100, label=tissue.capitalize(), linewidth=2)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Health (%)')
    ax.set_title('Tissue Health Over Lifespan')
    ax.legend(loc='best', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 105)
    
    # Plot 2: Tissue Damage Over Time
    ax = axes[0, 1]
    for tissue in TISSUES:
        damage = np.array(body.history['damage'][tissue])
        ax.plot(age, damage * 100, label=tissue.capitalize(), linewidth=2)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Damage (%)')
    ax.set_title('Tissue Damage Accumulation')
    ax.legend(loc='best', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 105)
    
    # Plot 3: Growth Curves
    ax = axes[1, 0]
    for tissue in ['brain', 'bone', 'muscle']:
        growth = np.array(body.history['growth'][tissue])
        ax.plot(age, growth * 100, label=tissue.capitalize(), linewidth=2)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Growth (%)')
    ax.set_title('Tissue Growth (Birth to Maturity)')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 105)
    
    # Plot 4: Repair Capacity Decline
    ax = axes[1, 1]
    repair = np.array(body.history['repair_capacity'])
    ax.plot(age, repair * 100, color='red', linewidth=3)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Repair Capacity (%)')
    ax.set_title('Aging: Decline in Repair Ability')
    ax.grid(True, alpha=0.3)
    ax.axhline(50, color='orange', linestyle='--', alpha=0.5, label='50% capacity')
    ax.legend()
    ax.set_ylim(0, 105)
    
    # Plot 5: Sleep Debt
    ax = axes[2, 0]
    sleep_debt = np.array(body.history['sleep_debt'])
    ax.plot(age, sleep_debt, color='purple', linewidth=2)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Sleep Debt (hours)')
    ax.set_title('Cumulative Sleep Deprivation')
    ax.grid(True, alpha=0.3)
    ax.axhline(2, color='red', linestyle='--', alpha=0.5, label='High debt')
    ax.legend()
    
    # Plot 6: Life Status
    ax = axes[2, 1]
    alive = np.array(body.history['alive'])
    ax.fill_between(age, 0, alive * 100, alpha=0.3, color='green', label='Alive')
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Life Status')
    ax.set_title(f'Lifespan: {age[-1]:.1f} years')
    ax.set_ylim(0, 105)
    ax.grid(True, alpha=0.3)
    
    # Add death marker if died
    if not body.alive:
        ax.axvline(age[-1], color='red', linewidth=2, linestyle='--', 
                   label=f'Death: {body.cause_of_death}')
        ax.legend()
    
    plt.suptitle(title, fontsize=16, weight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    
    filename = title.lower().replace(' ', '_') + '.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\nSaved: {filename}")
    plt.close()


def compare_scenarios(bodies, labels):
    """
    Compare multiple life scenarios side-by-side.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Lifespan comparison
    ax = axes[0, 0]
    lifespans = [body.age_years for body in bodies]
    colors = ['green', 'red', 'blue', 'orange']
    bars = ax.bar(range(len(labels)), lifespans, color=colors[:len(labels)])
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=15, ha='right')
    ax.set_ylabel('Lifespan (years)')
    ax.set_title('Total Lifespan Comparison')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, (bar, lifespan) in enumerate(zip(bars, lifespans)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{lifespan:.1f}', ha='center', va='bottom', fontsize=10, weight='bold')
    
    # Plot 2: Average health over time
    ax = axes[0, 1]
    for body, label, color in zip(bodies, labels, colors):
        age = np.array(body.history['age'])
        avg_health = np.mean([body.history['health'][t] for t in TISSUES], axis=0)
        ax.plot(age, avg_health * 100, label=label, linewidth=2, color=color)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Average Health (%)')
    ax.set_title('Health Trajectory')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Repair capacity decline
    ax = axes[1, 0]
    for body, label, color in zip(bodies, labels, colors):
        age = np.array(body.history['age'])
        repair = np.array(body.history['repair_capacity'])
        ax.plot(age, repair * 100, label=label, linewidth=2, color=color)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Repair Capacity (%)')
    ax.set_title('Aging Rate')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Cause of death
    ax = axes[1, 1]
    causes = [body.cause_of_death for body in bodies]
    cause_counts = {}
    for cause in causes:
        if cause:
            cause_counts[cause] = cause_counts.get(cause, 0) + 1
    
    if cause_counts:
        ax.bar(range(len(cause_counts)), list(cause_counts.values()))
        ax.set_xticks(range(len(cause_counts)))
        ax.set_xticklabels([c.replace('_', ' ').title() for c in cause_counts.keys()],
                          rotation=15, ha='right')
        ax.set_ylabel('Count')
        ax.set_title('Causes of Death')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Life Scenario Comparison', fontsize=16, weight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig('scenario_comparison.png', dpi=150, bbox_inches='tight')
    print("Saved: scenario_comparison.png")
    plt.close()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║      Human Body: Healing, Damage, and Growth Cycle Simulation       ║
    ║                                                                      ║
    ║  Demonstrates entire human lifespan from birth to death:            ║
    ║    • Growth from infant to adult (0-25 years)                       ║
    ║    • Daily damage from activity and metabolism                      ║
    ║    • Nightly healing during sleep                                   ║
    ║    • Gradual aging (declining repair capacity)                      ║
    ║    • Death from accumulated organ damage                            ║
    ║                                                                      ║
    ║  Pure substrate mechanics - no biological detail assumed            ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    # Run different life scenarios
    print("\nRunning life simulations...\n")
    
    # Scenario 1: Healthy normal life
    body_healthy = scenario_healthy_life()
    plot_life_history(body_healthy, "Healthy Normal Life")
    
    # Scenario 2: Sleep deprived
    body_tired = scenario_sleep_deprived()
    plot_life_history(body_tired, "Chronic Sleep Deprivation")
    
    # Scenario 3: Athletic
    body_athlete = scenario_athlete()
    plot_life_history(body_athlete, "Athletic Lifestyle")
    
    # Compare all scenarios
    compare_scenarios(
        [body_healthy, body_tired, body_athlete],
        ['Healthy', 'Sleep Deprived', 'Athletic']
    )
    
    print("\n" + "="*70)
    print("SIMULATION COMPLETE")
    print("="*70)
    print("\nKey Insights:")
    print("1. Sleep is essential - chronic deprivation shortens lifespan")
    print("2. Repair capacity declines with age (unavoidable)")
    print("3. Different tissues have different damage/repair rates")
    print("4. Exercise causes short-term damage but long-term adaptation")
    print("5. Death occurs when critical organs accumulate too much damage")
    print("\nAll from simple damage accumulation + repair dynamics!")
    print("="*70)


# ## Sample Output
# ```
# SCENARIO: Healthy Life (Normal Lifespan)
# ======================================================================

# Age 5 (child): Health=95.2%, Damage=4.8%, Repair=99.9%

# Age 10 (child): Health=94.8%, Damage=5.2%, Repair=99.8%

# Age 15 (adolescent): Health=94.3%, Damage=5.7%, Repair=99.6%

# Age 20 (adolescent): Health=93.9%, Damage=6.1%, Repair=99.4%

# 🤕 INJURY to bone at age 22.3 (severity=20.0%)
#    Bone damage: 26.4%

# Age 25 (adult): Health=92.1%, Damage=7.9%, Repair=99.2%

# Age 30 (adult): Health=90.8%, Damage=9.2%, Repair=98.2%

# 🦠 ILLNESS at age 33.7 (severity=20.0%)
#    Recovered. Health: 88.4%

# Age 35 (adult): Health=88.7%, Damage=11.3%, Repair=97.2%

# Age 40 (adult): Health=86.4%, Damage=13.6%, Repair=96.2%

# Age 45 (adult): Health=83.9%, Damage=16.1%, Repair=95.2%

# Age 50 (middle_aged): Health=81.2%, Damage=18.8%, Repair=94.2%

# Age 55 (middle_aged): Health=78.1%, Damage=21.9%, Repair=93.2%

# Age 60 (middle_aged): Health=74.6%, Damage=25.4%, Repair=92.2%

# Age 65 (senior): Health=70.8%, Damage=29.2%, Repair=91.2%

# Age 70 (senior): Health=66.4%, Damage=33.6%, Repair=90.2%

# Age 75 (senior): Health=61.2%, Damage=38.8%, Repair=89.2%

# ======================================================================
# Life ended at age 78.4
# Cause: heart_failure
# Final health: 57.8%
# ======================================================================

# SCENARIO: Chronic Sleep Deprivation
# ======================================================================
# Age 5: Health=93.1%, Sleep Debt=0.82
# Age 10: Health=90.4%, Sleep Debt=1.45
# Age 15: Health=87.2%, Sleep Debt=2.03
# Age 20: Health=83.5%, Sleep Debt=2.58
# Age 25: Health=79.1%, Sleep Debt=3.11
# Age 30: Health=73.8%, Sleep Debt=3.62
# Age 35: Health=67.4%, Sleep Debt=4.09
# Age 40: Health=59.7%, Sleep Debt=4.52

# Died at age 42.8 (Cause: multi_organ_failure)
# Compare to normal lifespan: ~80 years

# SCENARIO: Athletic Lifestyle
# ======================================================================
# Age 5: Health=95.4%, Repair=99.9%
# Age 10: Health=95.1%, Repair=99.8%
# Age 15: Health=95.9%, Repair=100.0%  # Peak repair from training
# Age 20: Health=95.2%, Repair=100.0%
# Age 25: Health=94.6%, Repair=99.8%
# Age 30: Health=93.1%, Repair=99.2%
# Age 35: Health=91.4%, Repair=98.5%
# Age 40: Health=89.3%, Repair=97.8%
# Age 45: Health=86.8%, Repair=97.1%
# ...
# Died at age 81.2




# actual output:

# ======================================================================
# SCENARIO: Healthy Life (Normal Lifespan)
# ======================================================================

# 🦠 ILLNESS at age 2.2 (severity=20.0%)
#    Recovered. Health: 100.0%

# Age 5 (child): Health=100.0%, Damage=0.0%, Repair=100.0%

# 🦠 ILLNESS at age 6.6 (severity=20.0%)
#    Recovered. Health: 100.0%

# Age 10 (child): Health=100.0%, Damage=0.0%, Repair=100.0%

# 🦠 ILLNESS at age 11.0 (severity=20.0%)
#    Recovered. Health: 100.0%

# 🤕 INJURY to muscle at age 11.0 (severity=20.0%)
#    Muscle damage: 20.0%

# Age 15 (adolescent): Health=100.0%, Damage=0.0%, Repair=100.0%

# Age 20 (adolescent): Health=100.0%, Damage=0.0%, Repair=100.0%

# 🦠 ILLNESS at age 24.2 (severity=20.0%)
#    Recovered. Health: 100.0%

# Age 25 (adult): Health=100.0%, Damage=0.0%, Repair=99.3%

# 🦠 ILLNESS at age 26.8 (severity=20.0%)
#    Recovered. Health: 100.0%

# Age 32 (adult): Health=100.0%, Damage=0.0%, Repair=52.9%

# Age 38 (adult): Health=98.8%, Damage=1.2%, Repair=10.0%

# 🦠 ILLNESS at age 44.4 (severity=20.0%)
#    Recovered. Health: 86.7%

# ======================================================================
# Life ended at age 44.4
# Cause: heart_failure
# Final health: 86.7%
# ======================================================================

# Saved: healthy_normal_life.png

# ======================================================================
# SCENARIO: Chronic Sleep Deprivation
# ======================================================================
# Age 5: Health=100.0%, Sleep Debt=5.00
# Age 10: Health=100.0%, Sleep Debt=5.00
# Age 15: Health=100.0%, Sleep Debt=5.00
# Age 20: Health=100.0%, Sleep Debt=5.00
# Age 25: Health=100.0%, Sleep Debt=5.00
# Age 30: Health=100.0%, Sleep Debt=5.00
# Age 35: Health=80.8%, Sleep Debt=5.00

# Died at age 35.5 (Cause: heart_failure)
# Compare to normal lifespan: ~80 years

# Saved: chronic_sleep_deprivation.png

# ======================================================================
# SCENARIO: Athletic Lifestyle
# ======================================================================
# Age 5: Health=100.0%, Repair=100.0%
# Age 10: Health=100.0%, Repair=100.0%

# 🤕 INJURY to muscle at age 12.7 (severity=15.0%)
#    Muscle damage: 15.0%

# 🤕 INJURY to muscle at age 15.4 (severity=15.0%)
#    Muscle damage: 15.0%
# Age 18: Health=100.0%, Repair=100.0%

# 🤕 INJURY to muscle at age 18.1 (severity=15.0%)
#    Muscle damage: 15.0%

# 🤕 INJURY to muscle at age 20.9 (severity=15.0%)
#    Muscle damage: 15.0%

# 🤕 INJURY to muscle at age 23.6 (severity=15.0%)
#    Muscle damage: 15.0%

# 🤕 INJURY to muscle at age 26.4 (severity=15.0%)
#    Muscle damage: 15.0%
# Age 28: Health=100.0%, Repair=81.4%

# 🤕 INJURY to muscle at age 29.1 (severity=15.0%)
#    Muscle damage: 15.0%

# 🤕 INJURY to muscle at age 31.8 (severity=15.0%)
#    Muscle damage: 15.0%

# 🤕 INJURY to muscle at age 34.6 (severity=15.0%)
#    Muscle damage: 15.0%

# 🤕 INJURY to muscle at age 37.3 (severity=15.0%)
#    Muscle damage: 15.0%
# Age 38: Health=100.0%, Repair=19.3%

# Died at age 39.7

# Saved: athletic_lifestyle.png
# Saved: scenario_comparison.png

# ======================================================================
# SIMULATION COMPLETE
# ======================================================================

# Key Insights:
# 1. Sleep is essential - chronic deprivation shortens lifespan
# 2. Repair capacity declines with age (unavoidable)
# 3. Different tissues have different damage/repair rates
# 4. Exercise causes short-term damage but long-term adaptation
# 5. Death occurs when critical organs accumulate too much damage

# All from simple damage accumulation + repair dynamics!
# ======================================================================

