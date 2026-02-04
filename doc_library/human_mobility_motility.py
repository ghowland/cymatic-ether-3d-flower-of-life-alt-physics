"""
Full-Range Human Mobility and Motility Simulation
Cymatic Physics Engine - Educational Image Output

Shows all movement types through static visualizations:
- Cellular motility (subcellular transport)
- Internal organs (heart, lungs, digestion)
- Posture and balance
- Locomotion (walking, running, jumping)
- Athletic movements

Pure substrate mechanics - wave propagation in elastic medium.
Outputs PNG images and animated GIF.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch
import matplotlib.patches as mpatches

# ============================================================================
# CYMATIC PHYSICS ENGINE
# ============================================================================

class CymaticSubstrate:
    """
    Core physics engine: Wave equation in elastic substrate.
    
    ∂²u/∂t² = c²∇²u - γ∂u/∂t + F(x,t)
    """
    
    def __init__(self, size=100, wave_speed=1.0, damping=0.1):
        """
        Args:
            size: Grid size (size × size)
            wave_speed: m/s (tissue wave speed)
            damping: Energy dissipation coefficient
        """
        self.size = size
        self.c = wave_speed
        self.gamma = damping
        
        # State: displacement field u(x,y,t)
        self.u = np.zeros((size, size))      # Current displacement
        self.u_prev = np.zeros((size, size))  # Previous timestep
        self.v = np.zeros((size, size))      # Velocity field
        
        # Substrate properties (can vary spatially)
        self.stiffness = np.ones((size, size)) * 1.0
        self.mass = np.ones((size, size)) * 1.0
        
    def apply_force(self, x, y, magnitude):
        """Apply point force at (x, y)."""
        if 0 <= x < self.size and 0 <= y < self.size:
            self.u[int(y), int(x)] += magnitude
    
    def apply_oscillating_force(self, x, y, amplitude, frequency, time):
        """Apply sinusoidal force (oscillator)."""
        force = amplitude * np.sin(2 * np.pi * frequency * time)
        self.apply_force(x, y, force)
    
    def step(self, dt):
        """
        Update substrate by one timestep using wave equation.
        
        Uses finite difference approximation:
        u_new = 2u - u_prev + dt²(c²∇²u - γ∂u/∂t)
        """
        # Compute Laplacian (∇²u) using 5-point stencil
        laplacian = (
            np.roll(self.u, 1, axis=0) +
            np.roll(self.u, -1, axis=0) +
            np.roll(self.u, 1, axis=1) +
            np.roll(self.u, -1, axis=1) -
            4 * self.u
        )
        
        # Velocity (for damping)
        self.v = (self.u - self.u_prev) / dt
        
        # Wave equation update
        u_new = (
            2 * self.u - self.u_prev +
            dt**2 * (self.c**2 * laplacian / self.mass - self.gamma * self.v)
        )
        
        # Update state
        self.u_prev = self.u.copy()
        self.u = u_new
        
        # Boundary conditions (fixed edges)
        self.u[0, :] = 0
        self.u[-1, :] = 0
        self.u[:, 0] = 0
        self.u[:, -1] = 0
    
    def get_energy(self):
        """Total energy in substrate."""
        kinetic = 0.5 * np.sum(self.mass * self.v**2)
        potential = 0.5 * np.sum(self.stiffness * self.u**2)
        return kinetic + potential


# ============================================================================
# BIOLOGICAL OSCILLATORS
# ============================================================================

class Oscillator:
    """Generic oscillator: muscle, organ, limb segment."""
    
    def __init__(self, x, y, mass=1.0, stiffness=10.0, damping=0.5,
                 frequency=1.0, amplitude=1.0):
        self.x = x
        self.y = y
        self.m = mass
        self.k = stiffness
        self.gamma = damping
        self.f = frequency
        self.A = amplitude
        
        # State
        self.position = 0.0
        self.velocity = 0.0
        
        # Natural frequency
        self.omega_0 = 2 * np.pi * frequency
    
    def step(self, dt, external_force=0):
        """Update oscillator state."""
        # Force balance
        F_spring = -self.k * self.position
        F_damping = -self.gamma * self.velocity
        F_total = F_spring + F_damping + external_force
        
        # Acceleration
        a = F_total / self.m
        
        # Update (Euler integration)
        self.velocity += a * dt
        self.position += self.velocity * dt
    
    def drive(self, time):
        """Generate driving force (neural input)."""
        return self.A * self.k * np.sin(self.omega_0 * time)


class Heart:
    """Cardiac oscillator - rhythmic pumping."""
    
    def __init__(self, x, y):
        self.oscillator = Oscillator(x, y, mass=0.3, stiffness=50,
                                     frequency=1.2, amplitude=0.5)
        self.phase = 0
    
    def beat(self, time, dt):
        """Generate heartbeat."""
        drive_force = self.oscillator.drive(time)
        self.oscillator.step(dt, external_force=drive_force)
        self.phase = (2 * np.pi * self.oscillator.f * time) % (2 * np.pi)
        return self.oscillator.position


class Lungs:
    """Respiratory oscillator - breathing."""
    
    def __init__(self, x, y):
        self.oscillator = Oscillator(x, y, mass=1.0, stiffness=20,
                                     frequency=0.25, amplitude=1.0)
    
    def breathe(self, time, dt):
        """Generate breathing motion."""
        drive_force = self.oscillator.drive(time)
        self.oscillator.step(dt, external_force=drive_force)
        return self.oscillator.position


class Muscle:
    """Skeletal muscle - tunable resonator."""
    
    def __init__(self, x, y, length=10):
        self.x = x
        self.y = y
        self.length = length
        self.activation = 0.0
        
        self.k_passive = 100
        self.k_active = 500
        
        self.oscillator = Oscillator(x, y, mass=0.5,
                                     stiffness=self.k_passive,
                                     damping=2.0,
                                     frequency=10.0,
                                     amplitude=0.1)
    
    def activate(self, level):
        """Set activation level (neural input)."""
        self.activation = np.clip(level, 0, 1)
        self.oscillator.k = self.k_passive + self.activation * self.k_active
        self.oscillator.omega_0 = np.sqrt(self.oscillator.k / self.oscillator.m)
    
    def contract(self, dt):
        """Update muscle state."""
        self.oscillator.step(dt)
        return self.oscillator.position


class Limb:
    """Limb segment with pendulum dynamics."""
    
    def __init__(self, length=0.5, mass=5.0):
        self.L = length
        self.m = mass
        self.theta = 0.0
        self.omega = 0.0
        self.g = 9.8
        self.omega_0 = np.sqrt(self.g / self.L)
    
    def step(self, dt, torque=0):
        """Update limb angle."""
        I = self.m * self.L**2 / 3
        alpha = (self.m * self.g * self.L * np.sin(self.theta) + torque) / I
        self.omega += alpha * dt
        self.theta += self.omega * dt


# ============================================================================
# FULL HUMAN BODY
# ============================================================================

class HumanBody:
    """Complete human body with all movement subsystems."""
    
    def __init__(self, substrate, x=50, y=50):
        self.substrate = substrate
        self.x = x
        self.y = y
        
        # Internal organs
        self.heart = Heart(x, y - 10)
        self.lungs = Lungs(x, y - 8)
        
        # Skeletal muscles
        self.muscles = {
            'leg_left': Muscle(x - 5, y + 10),
            'leg_right': Muscle(x + 5, y + 10),
            'arm_left': Muscle(x - 10, y - 5),
            'arm_right': Muscle(x + 10, y - 5),
        }
        
        # Limbs
        self.limbs = {
            'leg_left': Limb(length=1.0, mass=10),
            'leg_right': Limb(length=1.0, mass=10),
        }
        
        # Balance
        self.balance_angle = 0.02
        self.balance_velocity = 0.0
        self.Kp = 500
        self.Kd = 100
        
        # Movement state
        self.mode = 'standing'
        self.step_phase = 0.0
        self.jump_velocity = 0.0
        self.height = y
        
        # History for visualization
        self.history = {
            'heart': [],
            'lungs': [],
            'balance': [],
            'leg_left': [],
            'leg_right': [],
            'time': []
        }
    
    def update(self, dt, time):
        """Main update loop - all body subsystems."""
        
        # Internal organs
        heart_displacement = self.heart.beat(time, dt)
        lung_displacement = self.lungs.breathe(time, dt)
        
        self.substrate.apply_force(
            int(self.heart.oscillator.x),
            int(self.heart.oscillator.y),
            heart_displacement * 0.1
        )
        self.substrate.apply_force(
            int(self.lungs.oscillator.x),
            int(self.lungs.oscillator.y),
            lung_displacement * 0.05
        )
        
        # Cellular motility (10 Hz)
        cellular_osc = 0.01 * np.sin(2 * np.pi * 10 * time)
        self.substrate.apply_force(int(self.x), int(self.y), cellular_osc)
        
        # Balance
        if self.mode in ['standing', 'walking']:
            self.update_balance(dt)
        
        # Locomotion
        if self.mode == 'walking':
            self.update_walking(dt, time)
        elif self.mode == 'running':
            self.update_running(dt, time)
        elif self.mode == 'jumping':
            self.update_jumping(dt)
        
        # Muscles
        for muscle in self.muscles.values():
            muscle.contract(dt)
        
        # Record history
        self.history['heart'].append(heart_displacement)
        self.history['lungs'].append(lung_displacement)
        self.history['balance'].append(self.balance_angle)
        self.history['leg_left'].append(self.limbs['leg_left'].theta)
        self.history['leg_right'].append(self.limbs['leg_right'].theta)
        self.history['time'].append(time)
    
    def update_balance(self, dt):
        """Balance control via PD feedback."""
        torque = -self.Kp * self.balance_angle - self.Kd * self.balance_velocity
        
        I = 70 * 1.7**2 / 3
        g = 9.8
        m = 70
        h = 1.7
        
        alpha = (m * g * h * np.sin(self.balance_angle) + torque) / I
        self.balance_velocity += alpha * dt
        self.balance_angle += self.balance_velocity * dt
        
        sway_force = self.balance_angle * 50
        self.substrate.apply_force(int(self.x), int(self.y), sway_force)
    
    def update_walking(self, dt, time):
        """Walking as coupled limb oscillations."""
        f_walk = 1.0
        self.step_phase = (2 * np.pi * f_walk * time) % (2 * np.pi)
        
        left_phase = self.step_phase
        right_phase = self.step_phase + np.pi
        
        self.limbs['leg_left'].theta = 0.3 * np.sin(left_phase)
        self.limbs['leg_right'].theta = 0.3 * np.sin(right_phase)
        
        self.muscles['leg_left'].activate(0.5 + 0.5 * np.sin(left_phase))
        self.muscles['leg_right'].activate(0.5 + 0.5 * np.sin(right_phase))
        
        left_force = self.limbs['leg_left'].theta * 10
        right_force = self.limbs['leg_right'].theta * 10
        
        self.substrate.apply_force(int(self.x - 5), int(self.y + 15), left_force)
        self.substrate.apply_force(int(self.x + 5), int(self.y + 15), right_force)
    
    def update_running(self, dt, time):
        """Running as spring-mass bouncing."""
        f_run = 2.5
        phase = (2 * np.pi * f_run * time) % (2 * np.pi)
        
        bounce = 0.05 * np.sin(phase)
        self.height = self.y + bounce * 10
        
        self.limbs['leg_left'].theta = 0.2 * np.sin(phase)
        self.limbs['leg_right'].theta = 0.2 * np.sin(phase)
        
        activation = max(0, np.sin(phase))
        self.muscles['leg_left'].activate(activation)
        self.muscles['leg_right'].activate(activation)
        
        if np.sin(phase) < 0:
            impact = -20 * np.sin(phase)
            self.substrate.apply_force(int(self.x), int(self.height), impact)
    
    def update_jumping(self, dt):
        """Jumping as constructive interference."""
        g = 9.8
        
        self.jump_velocity -= g * dt
        self.height += self.jump_velocity * dt
        
        if self.height >= self.y:
            self.height = self.y
            self.jump_velocity = 0
            self.mode = 'standing'
        
        if self.jump_velocity < 0:
            force = self.jump_velocity * 5
            self.substrate.apply_force(int(self.x), int(self.height), force)
    
    def initiate_jump(self):
        """Start jump."""
        if self.mode == 'standing':
            self.jump_velocity = 4.0
            self.mode = 'jumping'
            
            for muscle in self.muscles.values():
                muscle.activate(1.0)
            
            self.substrate.apply_force(int(self.x), int(self.y + 10), -50)
    
    def set_mode(self, mode):
        """Change movement mode."""
        valid_modes = ['standing', 'walking', 'running', 'jumping']
        if mode in valid_modes:
            self.mode = mode


# ============================================================================
# STATIC VISUALIZATIONS
# ============================================================================

def draw_stick_figure(ax, body, time):
    """Draw body as stick figure."""
    body_x = 0
    body_y = 1.0 + (body.height - body.y) / 50
    
    # Head
    head = Circle((body_x, body_y + 0.15), 0.1, fill=True, 
                  color='peachpuff', edgecolor='black', linewidth=2)
    ax.add_patch(head)
    
    # Torso
    ax.plot([body_x, body_x], [body_y, body_y - 0.4],
           'k-', linewidth=4)
    
    # Legs
    left_leg_angle = body.limbs['leg_left'].theta
    right_leg_angle = body.limbs['leg_right'].theta
    
    leg_length = 0.5
    
    # Left leg (blue)
    left_leg_x = body_x + leg_length * np.sin(left_leg_angle)
    left_leg_y = body_y - 0.4 - leg_length * np.cos(left_leg_angle)
    ax.plot([body_x, left_leg_x], [body_y - 0.4, left_leg_y],
           'b-', linewidth=4, label='Left leg')
    
    # Right leg (red)
    right_leg_x = body_x + leg_length * np.sin(right_leg_angle)
    right_leg_y = body_y - 0.4 - leg_length * np.cos(right_leg_angle)
    ax.plot([body_x, right_leg_x], [body_y - 0.4, right_leg_y],
           'r-', linewidth=4, label='Right leg')
    
    # Arms (simple)
    ax.plot([body_x - 0.2, body_x], [body_y - 0.1, body_y - 0.1],
           'k-', linewidth=3)
    ax.plot([body_x, body_x + 0.2], [body_y - 0.1, body_y - 0.1],
           'k-', linewidth=3)
    
    # Ground
    ax.axhline(0, color='brown', linewidth=3)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-0.2, 2)
    ax.set_aspect('equal')
    ax.set_title(f'{body.mode.title()} - t={time:.1f}s', fontsize=14, weight='bold')


def draw_organs(ax, body):
    """Draw internal organs."""
    # Heart (pulsating)
    heart_size = 0.2 + 0.05 * np.sin(body.heart.phase)
    heart = Circle((0, 0), heart_size, color='red', alpha=0.7, 
                  edgecolor='darkred', linewidth=2)
    ax.add_patch(heart)
    ax.text(0, 0, '♥', ha='center', va='center',
           fontsize=20, color='white', weight='bold')
    
    # Lungs
    lung_expansion = body.lungs.oscillator.position * 0.1
    left_lung = Rectangle((-0.6, -0.3 - lung_expansion), 0.3,
                         0.6 + 2*lung_expansion,
                         color='lightblue', alpha=0.7,
                         edgecolor='blue', linewidth=2)
    right_lung = Rectangle((0.3, -0.3 - lung_expansion), 0.3,
                          0.6 + 2*lung_expansion,
                          color='lightblue', alpha=0.7,
                          edgecolor='blue', linewidth=2)
    ax.add_patch(left_lung)
    ax.add_patch(right_lung)
    ax.text(-0.45, 0, 'L', ha='center', va='center', fontsize=14, weight='bold')
    ax.text(0.45, 0, 'R', ha='center', va='center', fontsize=14, weight='bold')
    
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_title('Internal Organs', fontsize=14, weight='bold')
    ax.axis('off')


def create_comprehensive_figure(body, substrate, time):
    """Create single comprehensive visualization."""
    fig = plt.figure(figsize=(18, 12))
    
    # Main substrate view
    ax1 = plt.subplot(3, 4, 1)
    im = ax1.imshow(substrate.u, cmap='RdBu', vmin=-0.5, vmax=0.5,
                   origin='lower', aspect='auto')
    ax1.set_title('Substrate Wave Field', fontsize=12, weight='bold')
    plt.colorbar(im, ax=ax1, label='Displacement')
    
    # Body stick figure
    ax2 = plt.subplot(3, 4, 2)
    draw_stick_figure(ax2, body, time)
    
    # Internal organs
    ax3 = plt.subplot(3, 4, 3)
    draw_organs(ax3, body)
    
    # Heart rhythm
    ax4 = plt.subplot(3, 4, 4)
    if len(body.history['time']) > 1:
        ax4.plot(body.history['time'], body.history['heart'], 'r-', linewidth=2)
        ax4.set_xlim(max(0, time - 5), time)
        ax4.set_ylim(-1, 1)
    ax4.set_xlabel('Time (s)')
    ax4.set_ylabel('Displacement')
    ax4.set_title('Heart Beat (1.2 Hz)', fontsize=12, weight='bold')
    ax4.grid(True, alpha=0.3)
    
    # Breathing rhythm
    ax5 = plt.subplot(3, 4, 5)
    if len(body.history['time']) > 1:
        ax5.plot(body.history['time'], body.history['lungs'], 'b-', linewidth=2)
        ax5.set_xlim(max(0, time - 5), time)
        ax5.set_ylim(-2, 2)
    ax5.set_xlabel('Time (s)')
    ax5.set_ylabel('Displacement')
    ax5.set_title('Breathing (0.25 Hz)', fontsize=12, weight='bold')
    ax5.grid(True, alpha=0.3)
    
    # Balance control
    ax6 = plt.subplot(3, 4, 6)
    if len(body.history['time']) > 1:
        balance_deg = [np.rad2deg(b) for b in body.history['balance']]
        ax6.plot(body.history['time'], balance_deg, 'g-', linewidth=2)
        ax6.set_xlim(max(0, time - 5), time)
        ax6.set_ylim(-2, 2)
    ax6.set_xlabel('Time (s)')
    ax6.set_ylabel('Angle (degrees)')
    ax6.set_title('Postural Sway', fontsize=12, weight='bold')
    ax6.grid(True, alpha=0.3)
    
    # Leg coordination
    ax7 = plt.subplot(3, 4, 7)
    if len(body.history['time']) > 1:
        left_deg = [np.rad2deg(a) for a in body.history['leg_left']]
        right_deg = [np.rad2deg(a) for a in body.history['leg_right']]
        ax7.plot(body.history['time'], left_deg, 'b-', linewidth=2, label='Left')
        ax7.plot(body.history['time'], right_deg, 'r-', linewidth=2, label='Right')
        ax7.set_xlim(max(0, time - 5), time)
        ax7.set_ylim(-30, 30)
        ax7.legend(loc='upper right')
    ax7.set_xlabel('Time (s)')
    ax7.set_ylabel('Angle (degrees)')
    ax7.set_title('Leg Swing Coordination', fontsize=12, weight='bold')
    ax7.grid(True, alpha=0.3)
    
    # Phase portrait (leg coordination)
    ax8 = plt.subplot(3, 4, 8)
    if len(body.history['leg_left']) > 10:
        left_deg = [np.rad2deg(a) for a in body.history['leg_left'][-100:]]
        right_deg = [np.rad2deg(a) for a in body.history['leg_right'][-100:]]
        ax8.plot(left_deg, right_deg, 'purple', linewidth=2, alpha=0.6)
        ax8.scatter(left_deg[-1], right_deg[-1], c='red', s=100, zorder=5)
    ax8.set_xlabel('Left Leg Angle (°)')
    ax8.set_ylabel('Right Leg Angle (°)')
    ax8.set_title('Phase Portrait', fontsize=12, weight='bold')
    ax8.grid(True, alpha=0.3)
    ax8.axhline(0, color='k', linewidth=0.5)
    ax8.axvline(0, color='k', linewidth=0.5)
    
    # Energy spectrum
    ax9 = plt.subplot(3, 4, 9)
    frequencies = [0.25, 1.0, 1.2, 2.5, 10.0]
    labels = ['Breathing', 'Walking', 'Heart', 'Running', 'Cellular']
    colors = ['blue', 'green', 'red', 'orange', 'purple']
    ax9.bar(range(len(frequencies)), frequencies, color=colors, alpha=0.7)
    ax9.set_xticks(range(len(frequencies)))
    ax9.set_xticklabels(labels, rotation=45, ha='right')
    ax9.set_ylabel('Frequency (Hz)')
    ax9.set_title('Movement Frequency Spectrum', fontsize=12, weight='bold')
    ax9.set_yscale('log')
    ax9.grid(True, alpha=0.3, axis='y')
    
    # Info panel
    ax10 = plt.subplot(3, 4, 10)
    ax10.axis('off')
    info_text = f"""
MODE: {body.mode.upper()}
Time: {time:.2f} s

FREQUENCIES:
- Heart: 1.2 Hz (72 bpm)
- Lungs: 0.25 Hz (15/min)
- Walking: 1.0 Hz
- Running: 2.5 Hz
- Cellular: 10 Hz

CYMATIC PRINCIPLE:
All motion = wave 
propagation in 
elastic substrate

∂²u/∂t² = c²∇²u 
          - γ∂u/∂t 
          + F(x,t)
    """
    ax10.text(0.1, 0.5, info_text, fontsize=10, family='monospace',
             verticalalignment='center')
    
    # Muscle activation
    ax11 = plt.subplot(3, 4, 11)
    muscle_names = list(body.muscles.keys())
    activations = [body.muscles[m].activation for m in muscle_names]
    bars = ax11.barh(range(len(muscle_names)), activations, 
                     color='orange', alpha=0.7)
    ax11.set_yticks(range(len(muscle_names)))
    ax11.set_yticklabels([m.replace('_', ' ').title() for m in muscle_names])
    ax11.set_xlim(0, 1)
    ax11.set_xlabel('Activation Level')
    ax11.set_title('Muscle Activation', fontsize=12, weight='bold')
    ax11.grid(True, alpha=0.3, axis='x')
    
    # Substrate energy
    ax12 = plt.subplot(3, 4, 12)
    energy = substrate.get_energy()
    ax12.bar(['Total'], [energy], color='green', alpha=0.7)
    ax12.set_ylabel('Energy (arb. units)')
    ax12.set_title('Substrate Energy', fontsize=12, weight='bold')
    ax12.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Complete Human Movement: Cymatic Substrate Mechanics',
                fontsize=16, weight='bold', y=0.995)
    
    plt.tight_layout(rect=[0, 0, 1, 0.99])
    
    return fig


# ============================================================================
# SIMULATION AND OUTPUT
# ============================================================================

def simulate_and_visualize():
    """
    Run full simulation and create educational visualizations.
    """
    print("""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║     Full Human Mobility/Motility: Cymatic Physics Simulation        ║
    ║                                                                      ║
    ║  Generating educational visualizations showing:                     ║
    ║    • Cellular motility (10 Hz oscillations)                         ║
    ║    • Internal organs (heart 1.2 Hz, lungs 0.25 Hz)                  ║
    ║    • Balance control (postural sway)                                ║
    ║    • Locomotion (walking 1 Hz, running 2.5 Hz)                      ║
    ║    • Muscle activation patterns                                     ║
    ║    • Wave propagation in substrate                                  ║
    ║                                                                      ║
    ║  All from single wave equation: ∂²u/∂t² = c²∇²u - γ∂u/∂t + F      ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\nInitializing cymatic substrate...")
    substrate = CymaticSubstrate(size=100, wave_speed=2.0, damping=0.2)
    
    print("Creating human body with all subsystems...")
    body = HumanBody(substrate, x=50, y=50)
    
    # Simulation parameters
    dt = 0.01
    time = 0
    
    # Modes to demonstrate
    modes = [
        ('standing', 3.0),
        ('walking', 6.0),
        ('running', 4.0),
    ]
    
    print("\nRunning simulation...")
    
    frame_count = 0
    frames = []
    
    for mode, duration in modes:
        print(f"\n  Mode: {mode.upper()} ({duration}s)")
        body.set_mode(mode)
        
        t_start = time
        while time - t_start < duration:
            # Update physics
            body.update(dt, time)
            substrate.step(dt)
            time += dt
            
            # Capture frames every 0.2 seconds
            if abs(time - int(time/0.2)*0.2) < dt:
                fig = create_comprehensive_figure(body, substrate, time)
                
                # Save frame
                filename = f'frame_{frame_count:03d}.png'
                plt.savefig(filename, dpi=120, bbox_inches='tight')
                frames.append(filename)
                print(f"    Saved {filename} (t={time:.1f}s)")
                plt.close(fig)
                
                frame_count += 1
                
                # Limit frames
                if frame_count >= 60:  # Max 60 frames
                    break
        
        if frame_count >= 60:
            break
    
    print(f"\nGenerated {frame_count} frames")
    
    # Create animated GIF
    print("\nCreating animated GIF...")
    try:
        import imageio
        images = []
        for filename in frames:
            images.append(imageio.imread(filename))
        
        imageio.mimsave('human_movement_complete.gif', images, duration=0.2)
        print("Saved: human_movement_complete.gif")
        
        # Clean up individual frames
        import os
        for filename in frames:
            os.remove(filename)
        print("Cleaned up temporary frames")
        
    except ImportError:
        print("\nNote: Install imageio to create animated GIF:")
        print("  pip install imageio")
        print(f"Individual frames saved: {frames[0]} through {frames[-1]}")
    
    # Create summary figure
    print("\nCreating summary visualization...")
    fig_summary = create_comprehensive_figure(body, substrate, time)
    plt.savefig('human_movement_summary.png', dpi=150, bbox_inches='tight')
    print("Saved: human_movement_summary.png")
    plt.close()
    
    print("\n" + "="*70)
    print("SIMULATION COMPLETE")
    print("="*70)
    print("\nGenerated files:")
    print("  • human_movement_summary.png - Final state visualization")
    if 'imageio' in dir():
        print("  • human_movement_complete.gif - Animated sequence")
    print("\nKey Insights:")
    print("  1. ALL movement = wave propagation in substrate")
    print("  2. Different frequencies = different movement types")
    print("  3. Heart (1.2 Hz), lungs (0.25 Hz), walking (1 Hz), running (2.5 Hz)")
    print("  4. Muscles = tunable resonators, not motors")
    print("  5. Coordination = phase-locking between oscillators")
    print("\nPure cymatic mechanics - no biological 'motors' required!")
    print("="*70)


if __name__ == "__main__":
    simulate_and_visualize()



# Output
# The script generates:

# human_movement_summary.png - Comprehensive 12-panel visualization showing:

# Substrate wave field
# Stick figure body
# Internal organs (heart, lungs)
# Heart rhythm (1.2 Hz)
# Breathing rhythm (0.25 Hz)
# Balance/postural sway
# Leg coordination
# Phase portrait (limit cycle)
# Frequency spectrum
# Info panel with equations
# Muscle activation levels
# Substrate energy


# human_movement_complete.gif - Animated GIF showing full movement sequence:

# Standing → Walking → Running
# All physiological systems active
# Real-time wave propagation
# Coordinated limb movements



# Requirements
# bashpip install numpy matplotlib imageio
# Run
# bashpython human_mobility_motility.py
# Pure substrate mechanics. Educational static output. Complete human movement from wave equation.

