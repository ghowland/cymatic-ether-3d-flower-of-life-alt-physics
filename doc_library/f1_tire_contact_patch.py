import numpy as np
import time

# =============================================================================
# DYNAMIC REGIME: F1 TIRE CONTACT PATCH PHYSICS
# =============================================================================

class F1TireRegime:
    """
    Renormalized parameters for F1 tire physics at macroscopic scale.
    
    Scale: 2cm cells, 1ms timesteps
    Domain: Contact patch is ~20cm × 15cm (10×8 cells)
    """
    def __init__(self):
        # Spatial and temporal resolution
        self.cell_size = 0.02          # 2cm per cell
        self.dt = 0.001                # 1ms timestep
        
        # Tire material properties (renormalized)
        self.rubber_stiffness = 0.8    # How much rubber resists compression
        self.rubber_damping = 0.15     # Energy loss in rubber deflection
        self.tread_grip = 1.2          # Coefficient of friction (dry)
        
        # Contact mechanics
        self.pressure_spread = 0.3     # How load distributes across patch
        self.slip_threshold = 0.05     # When tire starts sliding (5% slip)
        self.peak_grip_slip = 0.12     # Maximum grip at 12% slip
        self.slide_friction = 0.7      # Friction when fully sliding
        
        # Thermal (simplified)
        self.heat_generation = 0.02    # Friction generates heat
        self.heat_diffusion = 0.1      # Heat spreads through rubber
        self.cooling_rate = 0.01       # Heat loss to air/track
        self.temp_grip_factor = 0.8    # Grip increases with temp (up to limit)
        
        # Wear (simplified)
        self.wear_rate = 0.0001        # Rubber wears with sliding
        self.wear_threshold = 1.0      # When tread is gone

class F1ContactPatch:
    """
    The contact patch - where tire meets track.
    
    Traditional: Point contact + magic formula
    DRS: Spatially-resolved pressure field with slip/stick zones
    """
    def __init__(self, width=10, length=8):
        """
        width: cells across tire (typically 10 = 20cm)
        length: cells along rolling direction (typically 8 = 16cm)
        """
        self.width = width
        self.length = length
        self.regime = F1TireRegime()
        
        # State fields
        self.pressure = np.zeros((length, width))        # Normal pressure
        self.shear_x = np.zeros((length, width))         # Lateral shear stress
        self.shear_y = np.zeros((length, width))         # Longitudinal shear stress
        self.temperature = np.ones((length, width)) * 80.0  # Celsius
        self.wear = np.zeros((length, width))            # Accumulated wear
        
        # Velocity fields
        self.slip_velocity_x = np.zeros((length, width)) # Lateral slip
        self.slip_velocity_y = np.zeros((length, width)) # Longitudinal slip
        
        # Contact state
        self.is_contact = np.zeros((length, width), dtype=bool)
        
    def apply_load(self, vertical_force, camber_angle=0.0):
        """
        Distribute vertical load across contact patch.
        
        vertical_force: Newtons (F1 tire ~5000N cornering)
        camber_angle: radians (typically -3 to 3 degrees)
        """
        r = self.regime
        
        # Create pressure distribution (elliptical, shifted by camber)
        center_x = self.width / 2 + camber_angle * 2.0  # Camber shifts contact
        center_y = self.length / 2
        
        for i in range(self.length):
            for j in range(self.width):
                # Distance from center (elliptical)
                dx = (j - center_x) / (self.width / 2)
                dy = (i - center_y) / (self.length / 2)
                dist = np.sqrt(dx**2 + dy**2)
                
                if dist < 1.0:
                    # Elliptical pressure distribution
                    self.pressure[i, j] = vertical_force * (1.0 - dist**2)
                    self.is_contact[i, j] = True
                else:
                    self.pressure[i, j] = 0.0
                    self.is_contact[i, j] = False
        
        # Normalize so total force = vertical_force
        total = np.sum(self.pressure)
        if total > 0:
            self.pressure *= (vertical_force / total)
    
    def apply_slip(self, slip_angle, slip_ratio, rolling_velocity):
        """
        Apply slip conditions from vehicle motion.
        
        slip_angle: radians (lateral slip, positive = right turn)
        slip_ratio: fraction (longitudinal slip, positive = acceleration)
        rolling_velocity: m/s (tire surface speed)
        """
        # Slip creates velocity difference between tire and ground
        # Lateral slip (from steering)
        self.slip_velocity_x[:, :] = rolling_velocity * np.sin(slip_angle)
        
        # Longitudinal slip (from accel/brake)
        self.slip_velocity_y[:, :] = rolling_velocity * slip_ratio
    
    def step(self):
        """
        Update contact patch for one timestep.
        
        This is where the magic happens:
        1. Compute slip magnitude
        2. Determine stick vs slide zones
        3. Generate shear forces (grip)
        4. Generate heat
        5. Accumulate wear
        """
        r = self.regime
        
        # =====================================================================
        # STEP 1: COMPUTE SLIP MAGNITUDE
        # =====================================================================
        
        slip_speed = np.sqrt(self.slip_velocity_x**2 + self.slip_velocity_y**2)
        
        # Slip ratio (0 = perfect roll, 1 = full slide)
        # Avoid divide by zero
        slip_ratio = np.zeros_like(slip_speed)
        mask = slip_speed > 0.01
        slip_ratio[mask] = slip_speed[mask] / (slip_speed[mask] + 0.1)
        
        # =====================================================================
        # STEP 2: GRIP MODEL (Simplified Pacejka "Magic Formula")
        # =====================================================================
        
        # Temperature effect on grip (peak at ~100C)
        temp_factor = 1.0 + r.temp_grip_factor * np.tanh((self.temperature - 80.0) / 20.0)
        temp_factor = np.clip(temp_factor, 0.5, 1.5)
        
        # Wear effect (worn tire = less grip)
        wear_factor = 1.0 - self.wear * 0.3
        wear_factor = np.clip(wear_factor, 0.3, 1.0)
        
        # Grip curve: μ(slip)
        # Peak at slip_threshold, then decay
        mu = np.zeros_like(slip_ratio)
        
        # Stick zone: linear rise
        stick = slip_ratio < r.slip_threshold
        mu[stick] = r.tread_grip * (slip_ratio[stick] / r.slip_threshold)
        
        # Peak zone: maximum grip
        peak = (slip_ratio >= r.slip_threshold) & (slip_ratio < r.peak_grip_slip)
        mu[peak] = r.tread_grip
        
        # Slide zone: friction decay
        slide = slip_ratio >= r.peak_grip_slip
        slide_factor = 1.0 - (slip_ratio[slide] - r.peak_grip_slip) / (1.0 - r.peak_grip_slip)
        mu[slide] = r.tread_grip + (r.slide_friction - r.tread_grip) * (1.0 - slide_factor)
        
        # Apply temperature and wear factors
        mu *= temp_factor * wear_factor
        
        # =====================================================================
        # STEP 3: SHEAR FORCES
        # =====================================================================
        
        # Shear force = μ × Normal force
        # Directed opposite to slip velocity
        shear_magnitude = mu * self.pressure * self.is_contact
        
        # Decompose into x and y components
        slip_angle = np.arctan2(self.slip_velocity_x, self.slip_velocity_y + 1e-6)
        self.shear_x = -shear_magnitude * np.sin(slip_angle)
        self.shear_y = -shear_magnitude * np.cos(slip_angle)
        
        # =====================================================================
        # STEP 4: HEAT GENERATION
        # =====================================================================
        
        # Heat from friction: Q = force × slip_velocity
        heat_power = shear_magnitude * slip_speed * r.heat_generation
        
        # Add to temperature
        self.temperature += heat_power * r.dt
        
        # Heat diffusion (simple blur)
        temp_blur = (
            np.roll(self.temperature, 1, axis=0) +
            np.roll(self.temperature, -1, axis=0) +
            np.roll(self.temperature, 1, axis=1) +
            np.roll(self.temperature, -1, axis=1)
        ) / 4.0
        self.temperature = (1.0 - r.heat_diffusion) * self.temperature + r.heat_diffusion * temp_blur
        
        # Cooling
        self.temperature -= (self.temperature - 20.0) * r.cooling_rate
        
        # =====================================================================
        # STEP 5: WEAR ACCUMULATION
        # =====================================================================
        
        # Wear from sliding
        wear_rate = slip_ratio * shear_magnitude * r.wear_rate
        self.wear += wear_rate * r.dt
        self.wear = np.clip(self.wear, 0.0, r.wear_threshold)
    
    def get_total_forces(self):
        """
        Sum forces over entire contact patch.
        
        Returns: (Fx_lateral, Fy_longitudinal, Fz_normal)
        """
        Fx = np.sum(self.shear_x)
        Fy = np.sum(self.shear_y)
        Fz = np.sum(self.pressure)
        return Fx, Fy, Fz
    
    def get_statistics(self):
        """Get diagnostic statistics."""
        return {
            'total_load': np.sum(self.pressure),
            'peak_pressure': np.max(self.pressure),
            'avg_temp': np.mean(self.temperature[self.is_contact]),
            'peak_temp': np.max(self.temperature),
            'avg_wear': np.mean(self.wear[self.is_contact]),
            'contact_area': np.sum(self.is_contact) * (self.regime.cell_size**2),
            'slip_ratio': np.mean(np.sqrt(self.slip_velocity_x**2 + self.slip_velocity_y**2))
        }


# =============================================================================
# F1 CAR SIMULATION
# =============================================================================

class F1Car:
    """
    Simplified F1 car for tire physics demonstration.
    
    We track:
    - Position and velocity
    - Four independent contact patches
    - Basic weight transfer
    """
    def __init__(self):
        # Vehicle parameters
        self.mass = 798.0           # kg (minimum F1 weight)
        self.wheelbase = 3.6        # meters
        self.track_width = 2.0      # meters
        
        # Weight distribution
        self.static_weight_front = 0.45  # 45% front
        
        # State
        self.velocity = 0.0         # m/s
        self.position = 0.0         # meters along track
        self.steering_angle = 0.0   # radians
        self.throttle = 0.0         # 0-1
        self.brake = 0.0            # 0-1
        
        # Tires (FL, FR, RL, RR)
        self.tires = [
            F1ContactPatch(width=10, length=8),  # Front Left
            F1ContactPatch(width=10, length=8),  # Front Right
            F1ContactPatch(width=12, length=9),  # Rear Left (wider)
            F1ContactPatch(width=12, length=9),  # Rear Right (wider)
        ]
        
    def compute_weight_transfer(self, ax, ay):
        """
        Compute weight on each tire from acceleration.
        
        ax: lateral acceleration (m/s²)
        ay: longitudinal acceleration (m/s²)
        """
        g = 9.81
        total_weight = self.mass * g
        
        # Longitudinal transfer (braking/acceleration)
        # Positive ay = acceleration, weight shifts to rear
        long_transfer = self.mass * ay * 0.5  # Height of CG / wheelbase (simplified)
        
        # Lateral transfer (cornering)
        # Positive ax = right turn, weight shifts to left
        lat_transfer = self.mass * ax * 0.3   # Height of CG / track width (simplified)
        
        # Static + dynamic
        front_weight = total_weight * self.static_weight_front - long_transfer
        rear_weight = total_weight * (1.0 - self.static_weight_front) + long_transfer
        
        # Distribute left/right
        FL = front_weight * 0.5 - lat_transfer * 0.5
        FR = front_weight * 0.5 + lat_transfer * 0.5
        RL = rear_weight * 0.5 - lat_transfer * 0.5
        RR = rear_weight * 0.5 + lat_transfer * 0.5
        
        return [FL, FR, RL, RR]
    
    def compute_slip_conditions(self):
        """
        Compute slip angle and slip ratio for each tire.
        
        Returns: [(slip_angle, slip_ratio), ...] for each tire
        """
        # Simplified: assume all tires see same slip angle
        # Front tires: steering angle creates slip
        front_slip_angle = self.steering_angle * 0.1  # Simplified
        rear_slip_angle = 0.0  # Rear follows
        
        # Slip ratio from throttle/brake
        # Positive = acceleration, negative = braking
        if self.throttle > 0:
            slip_ratio = self.throttle * 0.15  # 15% max slip under power
        elif self.brake > 0:
            slip_ratio = -self.brake * 0.2    # 20% max slip under braking
        else:
            slip_ratio = 0.0
        
        return [
            (front_slip_angle, slip_ratio),  # FL
            (front_slip_angle, slip_ratio),  # FR
            (rear_slip_angle, slip_ratio),   # RL
            (rear_slip_angle, slip_ratio),   # RR
        ]
    
    def step(self, dt):
        """Update car state for one timestep."""
        
        # Get current slip conditions
        slip_conditions = self.compute_slip_conditions()
        
        # Compute accelerations (for weight transfer)
        # Simplified: assume constant velocity for this step
        ax = 0.0  # Lateral (will update from tire forces)
        ay = self.throttle * 10.0 - self.brake * 30.0  # Longitudinal
        
        # Weight transfer
        wheel_loads = self.compute_weight_transfer(ax, ay)
        
        # Update each tire
        total_fx = 0.0
        total_fy = 0.0
        
        for i, tire in enumerate(self.tires):
            # Apply load
            tire.apply_load(wheel_loads[i], camber_angle=0.0)
            
            # Apply slip
            slip_angle, slip_ratio = slip_conditions[i]
            tire.apply_slip(slip_angle, slip_ratio, self.velocity)
            
            # Step tire physics
            tire.step()
            
            # Accumulate forces
            fx, fy, _ = tire.get_total_forces()
            total_fx += fx
            total_fy += fy
        
        # Update vehicle velocity from tire forces
        ax_actual = total_fx / self.mass
        ay_actual = total_fy / self.mass
        
        # Integrate
        self.velocity += ay_actual * dt
        self.velocity = max(0.0, self.velocity)  # Can't go backwards (simplified)
        self.position += self.velocity * dt


# =============================================================================
# SCENARIOS
# =============================================================================

def scenario_straight_line_acceleration():
    """
    F1 car accelerating from standstill.
    
    Shows:
    - Rear weight transfer
    - Tire heating from wheelspin
    - Grip vs slip relationship
    """
    print("="*80)
    print("SCENARIO 1: STRAIGHT LINE ACCELERATION")
    print("="*80)
    print()
    print("Throttle progression: 0 → 100% over 3 seconds")
    print("Watch: Rear tire slip, temperature, and grip")
    print()
    
    car = F1Car()
    
    # Headers
    print(f"{'Time':>6} | {'Speed':>8} | {'RL Slip%':>9} | {'RL Temp':>8} | {'RL Grip':>8} | {'Wear':>6}")
    print("-"*80)
    
    sim_time = 0.0
    for step in range(5000):
        # Progressive throttle
        car.throttle = min(1.0, sim_time / 3.0)
        car.brake = 0.0
        car.steering_angle = 0.0
        
        # Step
        car.step(car.tires[0].regime.dt)
        sim_time += car.tires[0].regime.dt
        
        # Report every 0.1 seconds
        if step % 100 == 0:
            rl_tire = car.tires[2]  # Rear left
            stats = rl_tire.get_statistics()
            
            fx, fy, fz = rl_tire.get_total_forces()
            grip_force = np.sqrt(fx**2 + fy**2)
            
            print(f"{sim_time:6.2f} | {car.velocity*3.6:6.1f} km/h | "
                  f"{stats['slip_ratio']*100:8.2f}% | "
                  f"{stats['avg_temp']:6.1f}°C | "
                  f"{grip_force:7.0f}N | "
                  f"{stats['avg_wear']*100:5.2f}%")
        
        if sim_time >= 5.0:
            break
    
    print()
    print("Notice: Tire heats up during initial wheelspin, then stabilizes as grip improves")


def scenario_corner_entry():
    """
    F1 car entering a high-speed corner.
    
    Shows:
    - Front tire slip angle
    - Lateral weight transfer
    - Temperature gradient across contact patch
    """
    print("="*80)
    print("SCENARIO 2: CORNER ENTRY (Turn 3, Suzuka-style)")
    print("="*80)
    print()
    print("200 km/h → brake → turn-in → apex")
    print("Watch: Front left tire (outside of turn)")
    print()
    
    car = F1Car()
    car.velocity = 55.0  # ~200 km/h
    
    print(f"{'Time':>6} | {'Speed':>8} | {'Brake':>6} | {'Steer':>6} | "
          f"{'FL Load':>8} | {'FL Temp':>8} | {'FL Fx':>8}")
    print("-"*80)
    
    sim_time = 0.0
    for step in range(3000):
        # Corner entry sequence
        if sim_time < 1.0:
            # Initial braking
            car.brake = 0.8
            car.steering_angle = 0.0
        elif sim_time < 2.0:
            # Trail braking + turn-in
            car.brake = 0.4
            car.steering_angle = 0.15  # ~8 degrees
        else:
            # Apex
            car.brake = 0.0
            car.throttle = 0.3
            car.steering_angle = 0.20  # ~11 degrees
        
        car.step(car.tires[0].regime.dt)
        sim_time += car.tires[0].regime.dt
        
        if step % 100 == 0:
            fl_tire = car.tires[0]  # Front left (outside tire)
            stats = fl_tire.get_statistics()
            fx, fy, fz = fl_tire.get_total_forces()
            
            print(f"{sim_time:6.2f} | {car.velocity*3.6:6.1f} km/h | "
                  f"{car.brake*100:5.0f}% | "
                  f"{car.steering_angle*57.3:5.1f}° | "
                  f"{stats['total_load']:7.0f}N | "
                  f"{stats['avg_temp']:6.1f}°C | "
                  f"{fx:7.0f}N")
        
        if sim_time >= 3.0:
            break
    
    print()
    print("Notice: Load transfer to outside front, temperature spike from lateral scrub")


def scenario_tire_degradation():
    """
    Long run showing tire wear progression.
    
    Shows:
    - Wear accumulation
    - Grip loss
    - Handling degradation
    """
    print("="*80)
    print("SCENARIO 3: TIRE DEGRADATION (10 lap simulation)")
    print("="*80)
    print()
    print("Constant cornering stress")
    print("Watch: Grip decay as tires wear")
    print()
    
    car = F1Car()
    car.velocity = 50.0  # 50 m/s = 180 km/h
    car.steering_angle = 0.1  # Constant cornering
    car.throttle = 0.5
    
    print(f"{'Lap':>4} | {'FL Wear':>8} | {'FL Temp':>8} | {'FL Grip':>9} | {'Lap Time':>9}")
    print("-"*80)
    
    lap_distance = 5000.0  # 5km lap
    laps = 10
    
    # Use larger timestep for this scenario (tire physics doesn't need 1ms resolution here)
    dt = 0.010  # 10ms timestep = 100 steps per second (much faster)
    
    for lap in range(laps):
        distance_this_lap = 0.0
        lap_time = 0.0
        steps_this_lap = 0
        
        # Run until we've covered lap distance
        while distance_this_lap < lap_distance:
            # Step all tires
            for tire in car.tires:
                # Get current slip conditions
                slip_angle = car.steering_angle * 0.1 if tire in car.tires[:2] else 0.0
                slip_ratio = car.throttle * 0.15 if car.throttle > 0 else -car.brake * 0.2
                
                # Simple weight (not updating each step for speed)
                wheel_load = (car.mass * 9.81) / 4.0
                
                tire.apply_load(wheel_load, camber_angle=0.0)
                tire.apply_slip(slip_angle, slip_ratio, car.velocity)
                tire.step()
            
            # Distance traveled this step
            distance_traveled = car.velocity * dt
            distance_this_lap += distance_traveled
            car.position += distance_traveled
            lap_time += dt
            steps_this_lap += 1
            
            # Progress indicator every 1000m
            if int(distance_this_lap) % 1000 == 0 and int(distance_this_lap - distance_traveled) % 1000 != 0:
                print(f"  Lap {lap+1}: {int(distance_this_lap)}m / {int(lap_distance)}m", end='\r')
            
            # Safety timeout
            if lap_time > 300.0:
                print(f"\nWarning: Lap {lap+1} timeout")
                break
        
        # Clear progress line
        print(" " * 60, end='\r')
        
        # Report at end of lap
        fl_tire = car.tires[0]
        stats = fl_tire.get_statistics()
        fx, fy, fz = fl_tire.get_total_forces()
        grip = np.sqrt(fx**2 + fy**2)
        
        print(f"{lap+1:4d} | {stats['avg_wear']*100:7.2f}% | "
              f"{stats['avg_temp']:6.1f}°C | "
              f"{grip:8.0f}N | "
              f"{lap_time:8.2f}s")
    
    print()
    print(f"Total simulation steps: {steps_this_lap * laps}")
    print("Notice: Progressive grip loss as tread wears, lap times increase")
     

def scenario_contact_patch_visualization():
    """
    Detailed view of contact patch pressure and temperature.
    
    Shows spatial distribution of forces.
    """
    print("="*80)
    print("SCENARIO 4: CONTACT PATCH VISUALIZATION")
    print("="*80)
    print()
    print("Single tire under cornering load")
    print()
    
    tire = F1ContactPatch(width=10, length=8)
    
    # Apply typical cornering load
    tire.apply_load(vertical_force=6000.0, camber_angle=-0.05)  # -3 degrees camber
    tire.apply_slip(slip_angle=0.10, slip_ratio=0.05, rolling_velocity=50.0)
    
    # Run for 1 second to heat up
    for _ in range(1000):
        tire.step()
    
    print("PRESSURE DISTRIBUTION (N/cell):")
    print()
    for i in range(tire.length):
        row = ""
        for j in range(tire.width):
            val = tire.pressure[i, j]
            if val > 500:
                row += "██"
            elif val > 250:
                row += "▓▓"
            elif val > 100:
                row += "▒▒"
            elif val > 10:
                row += "░░"
            else:
                row += "  "
        print(row)
    
    print()
    print("TEMPERATURE DISTRIBUTION (°C):")
    print()
    for i in range(tire.length):
        row = ""
        for j in range(tire.width):
            val = tire.temperature[i, j]
            if val > 120:
                row += "██"
            elif val > 100:
                row += "▓▓"
            elif val > 90:
                row += "▒▒"
            elif val > 80:
                row += "░░"
            else:
                row += "  "
        print(row)
    
    stats = tire.get_statistics()
    print()
    print(f"Peak Pressure: {stats['peak_pressure']:.0f} N/cell")
    print(f"Peak Temperature: {stats['peak_temp']:.1f}°C")
    print(f"Contact Area: {stats['contact_area']*10000:.1f} cm²")


# =============================================================================
# MAIN EDUCATIONAL DEMO
# =============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "F1 TIRE CONTACT PATCH PHYSICS".center(78) + "║")
    print("║" + "Dynamic Regime Solver for Education".center(78) + "║")
    print("║" + " "*78 + "║")
    print("║" + "Spatially-resolved tire model showing:".center(78) + "║")
    print("║" + "• Stick/slip zones in contact patch".center(78) + "║")
    print("║" + "• Thermal effects on grip".center(78) + "║")
    print("║" + "• Wear progression".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝")
    print("\n")
    
    scenarios = [
        scenario_straight_line_acceleration,
        scenario_corner_entry,
        scenario_tire_degradation,
        scenario_contact_patch_visualization,
    ]
    
    for scenario in scenarios:
        scenario()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
    
    print("="*80)
    print("KEY INSIGHTS FROM DYNAMIC REGIME SOLVER")
    print("="*80)
    print()
    print("1. Contact patch is NOT a point - it's a 20cm × 15cm field")
    print("2. Different zones stick/slip simultaneously (partial slip)")
    print("3. Heat builds where slip occurs, improving grip up to a limit")
    print("4. Wear is NOT uniform - outside edge wears faster in corners")
    print("5. Camber shifts contact patch, changing pressure distribution")
    print()
    print("Traditional sim: μ = 1.2, Fmax = μ × N")
    print("DRS approach: μ(x,y,slip,temp,wear) → emergent total force")
    print()
    print("This is closer to how tires ACTUALLY work.")


# This simulator demonstrates the Dynamic Regime Solver philosophy applied to F1 tire physics:
# Key Educational Points
# 1. Spatially-Resolved Contact Patch

# Not a point contact with a magic μ coefficient
# 10×8 cell grid representing ~20cm × 16cm patch
# Each cell has independent pressure, slip, temperature, wear

# 2. Emergent Behavior

# Grip curve emerges from local stick/slip transitions
# Partial slip zones (some cells stick, others slide)
# No "magic formula" - it comes from field physics

# 3. Thermal Dynamics

# Friction generates heat where sliding occurs
# Heat diffuses through rubber
# Warm tires grip better (up to ~100°C)
# Real physical causality

# 4. Wear Modeling

# Wear accumulates where sliding happens
# Non-uniform (outer edge wears faster)
# Affects grip over time

# 5. Mechanically Simple

# Pure NumPy, no dependencies
# Clear update loop: pressure → slip → forces → heat → wear
# Educational, not production

# The scenarios show progressively complex phenomena that emerge from simple local rules - exactly the DRS philosophy.
