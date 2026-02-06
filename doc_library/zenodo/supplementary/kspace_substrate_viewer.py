"""
K-Space Substrate Viewer
Interactive high-resolution substrate slice visualization
Navigate with arrow keys, zoom with +/-, reset with R
"""

import numpy as np
import pygame
import sys
from dataclasses import dataclass

@dataclass
class ViewState:
    center_x: float = 0.0
    center_y: float = 0.0
    zoom: float = 1.0
    substrate_size: int = 2048  # High resolution substrate
    
class KSpaceSubstrate:
    def __init__(self, size=2048):
        self.size = size
        self.substrate = self._generate_substrate()
        
    def _generate_substrate(self):
        """Generate high-resolution k-space substrate with phase patterns"""
        print(f"Generating {self.size}x{self.size} substrate...")
        
        # Create coordinate grids
        x = np.linspace(0, 40, self.size)
        y = np.linspace(0, 40, self.size)
        X, Y = np.meshgrid(x, y)
        
        # Multiple wave interference patterns (cymatic-like)
        # Create several overlapping wave sources
        substrate = np.zeros((self.size, self.size))
        
        # Wave sources at various positions
        sources = [
            (10, 10, 0.8, 2.5),
            (30, 10, 0.8, 2.3),
            (20, 20, 0.9, 2.7),
            (10, 30, 0.7, 2.4),
            (30, 30, 0.8, 2.6),
        ]
        
        for sx, sy, amplitude, frequency in sources:
            r = np.sqrt((X - sx)**2 + (Y - sy)**2)
            substrate += amplitude * np.sin(frequency * r) * np.exp(-r / 15)
        
        # Add fine structure
        substrate += 0.3 * np.sin(X * 0.5) * np.cos(Y * 0.5)
        substrate += 0.2 * np.sin(X * 0.8 + Y * 0.8)
        
        # Add subtle noise for texture
        substrate += 0.1 * np.random.randn(self.size, self.size)
        
        # Normalize
        substrate = (substrate - substrate.min()) / (substrate.max() - substrate.min())
        substrate = substrate * 4.0 - 2.0  # Scale to [-2, 2] like original
        
        print("Substrate generation complete")
        return substrate
    
    def get_view(self, center_x, center_y, zoom, view_width, view_height):
        """Extract a view from the substrate"""
        # Calculate substrate coordinates
        half_w = (view_width / 2) / zoom
        half_h = (view_height / 2) / zoom
        
        # Map from world coordinates to substrate indices
        substrate_x_min = int((center_x - half_w) * self.size / 40)
        substrate_x_max = int((center_x + half_w) * self.size / 40)
        substrate_y_min = int((center_y - half_h) * self.size / 40)
        substrate_y_max = int((center_y + half_h) * self.size / 40)
        
        # Clamp to substrate bounds
        substrate_x_min = max(0, min(self.size - 1, substrate_x_min))
        substrate_x_max = max(0, min(self.size, substrate_x_max))
        substrate_y_min = max(0, min(self.size - 1, substrate_y_min))
        substrate_y_max = max(0, min(self.size, substrate_y_max))
        
        # Extract region
        if substrate_x_max <= substrate_x_min or substrate_y_max <= substrate_y_min:
            return np.zeros((view_height, view_width))
        
        region = self.substrate[substrate_y_min:substrate_y_max, 
                               substrate_x_min:substrate_x_max]
        
        # Resize to view dimensions using high-quality interpolation
        if region.shape[0] > 0 and region.shape[1] > 0:
            # Use numpy for smooth scaling
            y_scale = view_height / region.shape[0]
            x_scale = view_width / region.shape[1]
            
            # Bilinear interpolation for smooth rendering
            scaled = self._bilinear_scale(region, view_height, view_width)
            return scaled
        
        return np.zeros((view_height, view_width))
    
    def _bilinear_scale(self, img, new_height, new_width):
        """Smooth bilinear scaling"""
        old_height, old_width = img.shape
        
        # Create output array
        scaled = np.zeros((new_height, new_width))
        
        # Calculate scaling ratios
        y_ratio = old_height / new_height
        x_ratio = old_width / new_width
        
        # Sample with bilinear interpolation
        for i in range(new_height):
            for j in range(new_width):
                # Source coordinates (floating point)
                y = i * y_ratio
                x = j * x_ratio
                
                # Integer parts
                y0 = int(y)
                x0 = int(x)
                y1 = min(y0 + 1, old_height - 1)
                x1 = min(x0 + 1, old_width - 1)
                
                # Fractional parts
                dy = y - y0
                dx = x - x0
                
                # Bilinear interpolation
                scaled[i, j] = (
                    img[y0, x0] * (1 - dx) * (1 - dy) +
                    img[y0, x1] * dx * (1 - dy) +
                    img[y1, x0] * (1 - dx) * dy +
                    img[y1, x1] * dx * dy
                )
        
        return scaled

def colormap_displacement(value):
    """Convert displacement value to RGB (blue-white-red colormap)"""
    # Normalize from [-2, 2] to [0, 1]
    normalized = (value + 2.0) / 4.0
    normalized = np.clip(normalized, 0, 1)
    
    if normalized < 0.5:
        # Blue to white
        t = normalized * 2
        r = int(t * 255)
        g = int(t * 255)
        b = 255
    else:
        # White to red
        t = (normalized - 0.5) * 2
        r = 255
        g = int((1 - t) * 255)
        b = int((1 - t) * 255)
    
    return (r, g, b)

def main():
    # Initialize Pygame
    pygame.init()
    
    # Screen settings
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 900
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("K-Space Substrate Viewer")
    
    # View state
    view = ViewState(center_x=20.0, center_y=20.0, zoom=1.0)
    
    # Generate substrate
    substrate = KSpaceSubstrate(size=2048)
    
    # Movement settings
    pan_speed = 0.5  # World units per keypress
    zoom_speed = 1.2
    
    # FPS
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    # Reset view
                    view.center_x = 20.0
                    view.center_y = 20.0
                    view.zoom = 1.0
                elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                    view.zoom *= zoom_speed
                elif event.key == pygame.K_MINUS:
                    view.zoom /= zoom_speed
                    view.zoom = max(0.1, view.zoom)
        
        # Continuous key handling for smooth movement
        keys = pygame.key.get_pressed()
        move_speed = pan_speed / view.zoom
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            view.center_x -= move_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            view.center_x += move_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            view.center_y -= move_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            view.center_y += move_speed
        
        # Clamp view to substrate bounds
        view.center_x = np.clip(view.center_x, 0, 40)
        view.center_y = np.clip(view.center_y, 0, 40)
        
        # Get current view
        view_data = substrate.get_view(
            view.center_x, view.center_y, view.zoom,
            SCREEN_WIDTH, SCREEN_HEIGHT
        )
        
        # Convert to RGB
        rgb_array = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8)
        for i in range(SCREEN_HEIGHT):
            for j in range(SCREEN_WIDTH):
                rgb_array[i, j] = colormap_displacement(view_data[i, j])
        
        # Blit to screen
        surf = pygame.surfarray.make_surface(rgb_array.swapaxes(0, 1))
        screen.blit(surf, (0, 0))
        
        # Draw UI overlay
        fps = clock.get_fps()
        fps_text = font.render(f"FPS: {fps:.1f}", True, (255, 255, 255))
        zoom_text = font.render(f"Zoom: {view.zoom:.2f}x", True, (255, 255, 255))
        pos_text = font.render(f"Pos: ({view.center_x:.1f}, {view.center_y:.1f})", 
                              True, (255, 255, 255))
        
        # Draw semi-transparent background for text
        info_rect = pygame.Rect(10, 10, 300, 100)
        s = pygame.Surface((300, 100))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        screen.blit(s, (10, 10))
        
        screen.blit(fps_text, (20, 20))
        screen.blit(zoom_text, (20, 50))
        screen.blit(pos_text, (20, 80))
        
        # Draw controls hint
        hint_text = font.render("Arrow keys: Move | +/-: Zoom | R: Reset | ESC: Quit", 
                               True, (255, 255, 255))
        hint_rect = pygame.Rect(10, SCREEN_HEIGHT - 50, SCREEN_WIDTH - 20, 40)
        s2 = pygame.Surface((SCREEN_WIDTH - 20, 40))
        s2.set_alpha(128)
        s2.fill((0, 0, 0))
        screen.blit(s2, (10, SCREEN_HEIGHT - 50))
        screen.blit(hint_text, (20, SCREEN_HEIGHT - 40))
        
        pygame.display.flip()
        clock.tick(60)  # Target 60 FPS
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

