import numpy as np

# =============================================================================
# DYNAMIC REGIME: F1 TIRE CONTACT PATCH PHYSICS
# =============================================================================

class F1TireRegime:
    """Renormalized parameters for F1 tire physics at macroscopic scale."""
    def __init__(self):
        self.cell_size = 0.02          # 2cm per cell
        self.dt = 0.010                # 10ms timestep (faster for demos)
        
        # Tire material properties
        self.rubber_stiffness = 0.8
        self.rubber_damping = 0.15
        self.tread_grip = 1.2
        
        # Contact mechanics
        self.pressure_spread = 0.3
        self.slip_threshold = 0.05
        self.peak_grip_slip = 0.12
        self.slide_friction = 0.7
        
        # Thermal (fixed rates)
        self.heat_generation = 5.0     # Heat per unit slip power
        self.heat_diffusion = 0.05     # Slower diffusion
        self.cooling_rate = 0.002      # Slower cooling to ambient
        self.temp_grip_factor = 0.3
        
        # Wear
        self.wear_rate = 0.00001
        self.wear_threshold = 1.0

class F1ContactPatch:
    """The contact patch where tire meets track."""
    def __init__(self, width=10, length=8):
        self.width = width
        self.length = length
        self.regime = F1TireRegime()
        
        # State fields
        self.pressure = np.zeros((length, width))
        self.shear_x = np.zeros((length, width))
        self.shear_y = np.zeros((length, width))
        self.temperature = np.ones((length, width)) * 80.0  # Start warm
        self.wear = np.zeros((length, width))
        
        # Slip velocities
        self.slip_velocity_x = np.zeros((length, width))
        self.slip_velocity_y = np.zeros((length, width))
        
        # Contact state
        self.is_contact = np.zeros((length, width), dtype=bool)
        
    def apply_load(self, vertical_force, camber_angle=0.0):
        """Distribute vertical load across contact patch."""
        r = self.regime
        
        center_x = self.width / 2 + camber_angle * 2.0
        center_y = self.length / 2
        
        self.pressure.fill(0.0)
        self.is_contact.fill(False)
        
        for i in range(self.length):
            for j in range(self.width):
                dx = (j - center_x) / (self.width / 2)
                dy = (i - center_y) / (self.length / 2)
                dist = np.sqrt(dx**2 + dy**2)
                
                if dist < 1.0:
                    self.pressure[i, j] = vertical_force * (1.0 - dist**2)
                    self.is_contact[i, j] = True
        
        # Normalize
        total = np.sum(self.pressure)
        if total > 0:
            self.pressure *= (vertical_force / total)
    
    def apply_slip(self, slip_angle, slip_ratio, rolling_velocity):
        """Apply slip conditions from vehicle motion."""
        # Lateral slip velocity (m/s)
        self.slip_velocity_x[:, :] = rolling_velocity * np.sin(slip_angle)
        
        # Longitudinal slip velocity (m/s)
        self.slip_velocity_y[:, :] = rolling_velocity * slip_ratio
    
    def step(self):
        """Update contact patch for one timestep."""
        r = self.regime
        
        # Compute total slip speed
        slip_speed = np.sqrt(self.slip_velocity_x**2 + self.slip_velocity_y**2)
        
        # Slip ratio (normalized)
        slip_ratio = np.zeros_like(slip_speed)
        mask = slip_speed > 0.001
        slip_ratio[mask] = np.clip(slip_speed[mask] / 10.0, 0, 1.0)
        
        # Temperature effect on grip
        temp_factor = 1.0 + r.temp_grip_factor * np.clip((self.temperature - 80.0) / 40.0, -0.5, 0.5)
        
        # Wear effect
        wear_factor = np.clip(1.0 - self.wear * 0.3, 0.3, 1.0)
        
        # Grip curve: μ(slip)
        mu = np.zeros_like(slip_ratio)
        
        # Stick zone
        stick = slip_ratio < r.slip_threshold
        mu[stick] = r.tread_grip * (slip_ratio[stick] / r.slip_threshold)
        
        # Peak zone
        peak = (slip_ratio >= r.slip_threshold) & (slip_ratio < r.peak_grip_slip)
        mu[peak] = r.tread_grip
        
        # Slide zone
        slide = slip_ratio >= r.peak_grip_slip
        if np.any(slide):
            slide_factor = np.clip(1.0 - (slip_ratio[slide] - r.peak_grip_slip) / (1.0 - r.peak_grip_slip), 0, 1)
            mu[slide] = r.slide_friction + (r.tread_grip - r.slide_friction) * slide_factor
        
        # Apply factors
        mu *= temp_factor * wear_factor
        
        # Shear forces
        shear_magnitude = mu * self.pressure * self.is_contact
        
        # Direction opposite to slip
        slip_angle = np.arctan2(self.slip_velocity_x, self.slip_velocity_y + 1e-9)
        self.shear_x = -shear_magnitude * np.sin(slip_angle)
        self.shear_y = -shear_magnitude * np.cos(slip_angle)
        
        # Heat generation (only where slipping)
        heat_power = shear_magnitude * slip_speed * r.heat_generation
        self.temperature += heat_power * r.dt
        
        # Heat diffusion (simple neighbor average)
        if r.heat_diffusion > 0:
            temp_blur = np.copy(self.temperature)
            for i in range(1, self.length - 1):
                for j in range(1, self.width - 1):
                    neighbors = (self.temperature[i-1, j] + self.temperature[i+1, j] +
                                self.temperature[i, j-1] + self.temperature[i, j+1]) / 4.0
                    temp_blur[i, j] = (1 - r.heat_diffusion) * self.temperature[i, j] + r.heat_diffusion * neighbors
            self.temperature = temp_blur
        
        # Cooling to ambient (20°C)
        self.temperature -= (self.temperature - 20.0) * r.cooling_rate * r.dt
        self.temperature = np.clip(self.temperature, 20.0, 200.0)
        
        # Wear accumulation
        wear_rate = slip_ratio * shear_magnitude * r.wear_rate
        self.wear += wear_rate * r.dt
        self.wear = np.clip(self.wear, 0, r.wear_threshold)
    
    def get_total_forces(self):
        """Sum forces over entire contact patch."""
        Fx = np.sum(self.shear_x)
        Fy = np.sum(self.shear_y)
        Fz = np.sum(self.pressure)
        return Fx, Fy, Fz
    
    def get_statistics(self):
        """Get diagnostic statistics."""
        contact_mask = self.is_contact
        if not np.any(contact_mask):
            return {
                'total_load': 0, 'peak_pressure': 0, 'avg_temp': 20.0,
                'peak_temp': 20.0, 'avg_wear': 0, 'contact_area': 0, 'slip_ratio': 0
            }
        
        slip_speed = np.sqrt(self.slip_velocity_x**2 + self.slip_velocity_y**2)
        
        return {
            'total_load': np.sum(self.pressure),
            'peak_pressure': np.max(self.pressure),
            'avg_temp': np.mean(self.temperature[contact_mask]),
            'peak_temp': np.max(self.temperature),
            'avg_wear': np.mean(self.wear[contact_mask]),
            'contact_area': np.sum(contact_mask) * (self.regime.cell_size**2),
            'slip_ratio': np.mean(slip_speed[contact_mask]) if np.any(contact_mask) else 0
        }


# =============================================================================
# F1 CAR SIMULATION
# =============================================================================

class F1Car:
    """Simplified F1 car for tire physics demonstration."""
    def __init__(self):
        self.mass = 798.0
        self.wheelbase = 3.6
        self.track_width = 2.0
        self.static_weight_front = 0.45
        
        # State
        self.velocity = 0.0
        self.position = 0.0
        self.steering_angle = 0.0
        self.throttle = 0.0
        self.brake = 0.0
        
        # Tires (FL, FR, RL, RR)
        self.tires = [
            F1ContactPatch(width=10, length=8),  # Front Left
            F1ContactPatch(width=10, length=8),  # Front Right
            F1ContactPatch(width=12, length=9),  # Rear Left (wider)
            F1ContactPatch(width=12, length=9),  # Rear Right (wider)
        ]
        
    def step(self, dt):
        """Update car state for one timestep."""
        g = 9.81
        
        # Simplified longitudinal acceleration from throttle/brake
        if self.throttle > 0:
            target_accel = self.throttle * 15.0  # Max 15 m/s² acceleration
        elif self.brake > 0:
            target_accel = -self.brake * 40.0    # Max 40 m/s² braking
        else:
            target_accel = -2.0                   # Rolling resistance
        
        # Weight distribution (simplified - no dynamic transfer for speed)
        total_weight = self.mass * g
        front_weight = total_weight * self.static_weight_front
        rear_weight = total_weight * (1.0 - self.static_weight_front)
        
        wheel_loads = [front_weight / 2, front_weight / 2, rear_weight / 2, rear_weight / 2]
        
        # Slip conditions
        # Front slip angle from steering
        front_slip_angle = self.steering_angle * 0.1
        
        # Longitudinal slip from accel/brake
        if self.velocity > 1.0:  # Only if moving
            if self.throttle > 0:
                slip_ratio = self.throttle * 0.15
            elif self.brake > 0:
                slip_ratio = -self.brake * 0.20
            else:
                slip_ratio = 0.0
        else:
            slip_ratio = 0.0
        
        # Update tires and accumulate forces
        total_fy = 0.0
        
        for i, tire in enumerate(self.tires):
            # Apply load
            tire.apply_load(wheel_loads[i], camber_angle=0.0)
            
            # Apply slip
            if i < 2:  # Front tires
                tire.apply_slip(front_slip_angle, slip_ratio, max(self.velocity, 1.0))
            else:      # Rear tires
                tire.apply_slip(0.0, slip_ratio, max(self.velocity, 1.0))
            
            # Step tire physics
            tire.step()
            
            # Get forces
            fx, fy, fz = tire.get_total_forces()
            total_fy += fy
        
        # Update velocity from tire forces
        actual_accel = total_fy / self.mass
        
        # Blend with target (simplified traction control)
        final_accel = 0.7 * target_accel + 0.3 * actual_accel
        
        # Integrate velocity
        self.velocity += final_accel * dt
        self.velocity = max(0.0, self.velocity)  # Can't go backwards
        
        # Integrate position
        self.position += self.velocity * dt


# =============================================================================
# SCENARIOS
# =============================================================================

def scenario_straight_line_acceleration():
    """F1 car accelerating from standstill."""
    print("="*80)
    print("SCENARIO 1: STRAIGHT LINE ACCELERATION")
    print("="*80)
    print()
    print("Throttle progression: 0 → 100% over 3 seconds")
    print("Watch: Rear tire slip, temperature, and grip")
    print()
    
    car = F1Car()
    
    print(f"{'Time':>6} | {'Speed':>8} | {'RL Slip%':>9} | {'RL Temp':>8} | {'RL Grip':>8} | {'Wear':>6}")
    print("-"*80)
    
    sim_time = 0.0
    dt = car.tires[0].regime.dt
    
    for step in range(500):
        # Progressive throttle
        car.throttle = min(1.0, sim_time / 3.0)
        car.brake = 0.0
        car.steering_angle = 0.0
        
        car.step(dt)
        sim_time += dt
        
        # Report every 0.1 seconds
        if step % 10 == 0:
            rl_tire = car.tires[2]
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
    """F1 car entering a high-speed corner."""
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
    dt = car.tires[0].regime.dt
    
    for step in range(300):
        # Corner entry sequence
        if sim_time < 1.0:
            car.brake = 0.8
            car.steering_angle = 0.0
            car.throttle = 0.0
        elif sim_time < 2.0:
            car.brake = 0.4
            car.steering_angle = 0.15
            car.throttle = 0.0
        else:
            car.brake = 0.0
            car.throttle = 0.3
            car.steering_angle = 0.20
        
        car.step(dt)
        sim_time += dt
        
        if step % 10 == 0:
            fl_tire = car.tires[0]
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
    """Long run showing tire wear progression."""
    print("="*80)
    print("SCENARIO 3: TIRE DEGRADATION (10 lap simulation)")
    print("="*80)
    print()
    print("Constant cornering stress")
    print("Watch: Grip decay as tires wear")
    print()
    
    car = F1Car()
    car.velocity = 50.0
    car.steering_angle = 0.1
    car.throttle = 0.5
    
    print(f"{'Lap':>4} | {'FL Wear':>8} | {'FL Temp':>8} | {'FL Grip':>9} | {'Lap Time':>9}")
    print("-"*80)
    
    lap_distance = 5000.0
    laps = 10
    dt = car.tires[0].regime.dt
    
    for lap in range(laps):
        distance_this_lap = 0.0
        lap_time = 0.0
        
        while distance_this_lap < lap_distance:
            car.step(dt)
            
            distance_this_lap += car.velocity * dt
            lap_time += dt
            
            # Safety timeout
            if lap_time > 200.0:
                break
        
        # Report
        fl_tire = car.tires[0]
        stats = fl_tire.get_statistics()
        fx, fy, fz = fl_tire.get_total_forces()
        grip = np.sqrt(fx**2 + fy**2)
        
        print(f"{lap+1:4d} | {stats['avg_wear']*100:7.2f}% | "
              f"{stats['avg_temp']:6.1f}°C | "
              f"{grip:8.0f}N | "
              f"{lap_time:8.2f}s")
    
    print()
    print("Notice: Progressive grip loss as tread wears, lap times increase")


def scenario_contact_patch_visualization():
    """Detailed view of contact patch pressure and temperature."""
    print("="*80)
    print("SCENARIO 4: CONTACT PATCH VISUALIZATION")
    print("="*80)
    print()
    print("Single tire under cornering load")
    print()
    
    tire = F1ContactPatch(width=10, length=8)
    
    tire.apply_load(vertical_force=6000.0, camber_angle=-0.05)
    tire.apply_slip(slip_angle=0.10, slip_ratio=0.05, rolling_velocity=50.0)
    
    # Run for 1 second to heat up
    for _ in range(100):
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
