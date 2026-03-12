# Integer ALU Based Computing — Rendering Pipeline Specification v1.0

**Sovereign Volumetric Engine on VFR Hardware: Complete 2D and 3D Graphics Pipeline**

---

## 1. Overview

The rendering pipeline operates entirely in integer arithmetic on VFR hardware. There is no GPU, no floating point, no triangle rasterization, no texture sampling, and no OpenGL/Vulkan driver stack. The ARM processor owns the framebuffer and HDMI output. The FPGA cores perform all beam-casting, shading, and physics computation. The result is a pixel buffer written directly to display memory.

The pipeline has two layers: a 3D volumetric beam-caster for world geometry, and a 2D layout renderer for UI. The 3D layer writes first. The 2D layer composites on top. Both are pure integer operations on VFR batch data.

---

## 2. Framebuffer

### 2.1 Structure

The framebuffer is a flat array of pixel values in DDR3, memory-mapped to the HDMI output controller on the ARM processing system.

```
Resolution: 1920 × 1080
Pixel format: ARGB8888 (4 bytes per pixel)
Size: 1920 × 1080 × 4 = 8,294,400 bytes (~8 MB)
Double buffered: 2 × 8 MB = 16 MB total
Location: DDR3 at 0x0100_0000
```

The ARM swaps front and back buffers each frame. The FPGA writes to the back buffer via DMA. The ARM composites the 2D UI layer onto the back buffer after the FPGA finishes the 3D pass. Then the ARM flips.

### 2.2 Pixel as VFR

A pixel is a VFR pair at the framebuffer's domain scale:

```
[color: i32, alpha: i8]

Where color packs as:
  bits 23-16: red   (0-255)
  bits 15-8:  green (0-255)
  bits 7-0:   blue  (0-255)
```

The framebuffer is a batch:

```
[F=pixel, count=2_073_600, depth=1]
[color, alpha] [color, alpha] [color, alpha] ...
```

Each FPGA core writes its portion of this batch. The ARM reads the completed batch and pushes it to the display controller.

---

## 3. The 3D Pipeline: Sovereign Volumetric Engine

### 3.1 World Representation

The world is not a mesh. It is a database of Build Boxes. Each Build Box is a ContentRect — an arbitrary-sized volume in 3D space containing a Sparse Voxel Directed Acyclic Graph (SVDAG).

```
Build Box batch:
[F=world, count=N, depth=12]

Each Build Box:
  [rect_x,        rx]    pair 0:  2D position X
  [rect_y,        ry]    pair 1:  2D position Y (Z in world)
  [rect_w,        rw]    pair 2:  width
  [rect_h,        rh]    pair 3:  height (depth in world)
  [y_floor,       rf]    pair 4:  vertical floor
  [y_ceiling,     rc]    pair 5:  vertical ceiling
  [svdag_root,     0]    pair 6:  index into SVDAG node pool
  [resolution,     0]    pair 7:  SVDAG drill depth (6-12)
  [material_id,    0]    pair 8:  default material
  [mutator_scale, rs]    pair 9:  noise scale (VFR fixed-point)
  [mutator_rot,   rr]    pair 10: noise rotation
  [mutator_warp,   0]    pair 11: warp function selector
```

A dragon, a chair, a skyscraper, and a pebble are all Build Boxes. They differ only in dimensions, SVDAG root, and material. The renderer processes them identically.

### 3.2 SVDAG: The Geometry Database

The SVDAG is a flat array of nodes in DDR3, loaded to shared BRAM on the FPGA at scene start.

```
SVDAG Node: 5 bytes (one VFR pair)
  [child_offset: i32, child_mask: i8]

  child_mask: 8 bits, one per octant
    bit = 1: solid (drill deeper or leaf)
    bit = 0: air (beam passes through)
  
  child_offset: index into node pool
    high bit set (0x8000_0000): this is a leaf pointer
    high bit clear: this is an interior node pointer
```

The entire world geometry is stored in one flat node pool. Multiple Build Boxes can point to the same SVDAG root. 1000 identical stone pillars share one set of nodes. This is geometric deduplication — the DAG advantage.

```
SVDAG Leaf: 5 bytes (one VFR pair)
  [material_id: i32, flags: i8]

  flags:
    bit 0: has_procedural_hit (PHE active)
    bit 1: has_cymatic_state
    bits 2-7: reserved
```

### 3.3 Beam-Casting: Rendering as Search

For every pixel, the renderer shoots a beam into the world and finds the first solid voxel it hits. This is a search, not a draw call.

**Phase 1 — Broad Phase (Box Culling)**

The beam checks for intersection with Build Box axis-aligned bounding boxes. This is 6 integer comparisons per box. A 2D spatial hash pre-filters boxes by screen tile, reducing the search from N boxes to typically 2-5 candidates.

```
For each beam:
  tile = screen_position / tile_size
  candidates = spatial_hash[tile]
  for each candidate box:
    if beam intersects box AABB:
      enter narrow phase
```

AABB intersection is:

```
SUB  V1, beam_origin_x, box_min_x
SUB  V2, box_max_x, beam_origin_x
CMP  V1, V2          ; check X range
JGT  miss

; repeat for Y and Z
; all three pass = hit, compute entry point
```

Six subtracts and six compares. Pure ALU.

**Phase 2 — Narrow Phase (SVDAG Drill)**

The beam enters the Build Box. Its world-space position is converted to local coordinates (0 to max_resolution) within the box using integer scaling:

```
local_x = ((world_x - box_min_x) * resolution) / box_width
local_y = ((world_y - box_min_y) * resolution) / box_height
local_z = ((world_z - box_min_z) * resolution) / box_depth
```

Division by box dimensions uses precomputed reciprocal multiplies (no hardware divider needed).

The drill descends the SVDAG:

```
node_index = svdag_root
for depth in 0..resolution_depth:
    node = node_pool[node_index]
    
    ; Compute octant from local coordinates
    ; At each depth, the relevant bit is (local_coord >> (max_depth - depth - 1)) & 1
    octant_x = (local_x >> (max_depth - depth - 1)) & 1
    octant_y = (local_y >> (max_depth - depth - 1)) & 1
    octant_z = (local_z >> (max_depth - depth - 1)) & 1
    octant = octant_x | (octant_y << 1) | (octant_z << 2)
    
    ; Check child_mask
    bit = (node.child_mask >> octant) & 1
    if bit == 0:
        return AIR  ; beam passes through
    
    ; Count set bits before this octant to find child index
    mask_below = node.child_mask & ((1 << octant) - 1)
    child_index = popcount(mask_below)
    node_index = node.child_offset + child_index
    
    ; Check if leaf
    if node_index & 0x80000000:
        leaf_index = node_index & 0x7FFFFFFF
        return LEAF_HIT(leaf_index, local_x, local_y, local_z)
```

Every operation is shift, mask, compare, popcount, add. The popcount (count set bits) can be implemented as a lookup table in BRAM (256 entries for 8-bit values) or as a sequence of shifts and adds.

The drill terminates the instant it hits a solid leaf. No overdraw. No depth buffer. The first hit IS the result.

**Phase 3 — Procedural Hit Evaluator (Conditional Solidity)**

After the SVDAG reports a leaf hit, the PHE optionally rejects it based on math. This turns solid into air without changing the SVDAG.

```
if leaf.has_procedural_hit:
    ; Edge softening: reject near box boundaries
    dist_to_edge = min(
        local_x, resolution - local_x,
        local_y, resolution - local_y,
        local_z, resolution - local_z
    )
    if dist_to_edge < edge_fuzz_radius:
        noise_val = integer_noise(local_x, local_y, local_z)
        if noise_val > threshold:
            return AIR  ; rejected, beam continues
    
    ; Implicit shape: cylinder
    dx = local_x - center_x
    dy = local_y - center_y
    radius_sq = (dx * dx + dy * dy) >> fixed_point_shift
    if radius_sq > max_radius_sq:
        return AIR  ; outside cylinder, rejected
```

The PHE only subtracts from solidity. It never adds. The beam logic remains monotonic. Physics uses the same PHE, so visual softness is physically real.

**Phase 4 — Shading: Gouraud + Procedural Noise**

Two-layer shading, both integer.

**Macro Layer: Gouraud Interpolation**

Each Build Box stores 8 corner colors (8 VFR pairs). The hit point's local coordinates trilinearly interpolate between them.

```
; Trilinear interpolation: 7 LERPs
; Each LERP: result = a + ((b - a) * t) >> shift

; Interpolate along X for 4 pairs of corners
c00 = lerp(corner[0], corner[1], local_x)
c01 = lerp(corner[2], corner[3], local_x)
c10 = lerp(corner[4], corner[5], local_x)
c11 = lerp(corner[6], corner[7], local_x)

; Interpolate along Y for 2 pairs
c0 = lerp(c00, c01, local_y)
c1 = lerp(c10, c11, local_y)

; Interpolate along Z for final color
base_color = lerp(c0, c1, local_z)
```

Each LERP is: subtract, multiply, shift, add. Four ALU operations. Seven LERPs = 28 ALU operations total. The result is a smooth color gradient across the entire Build Box volume.

Integer LERP implementation:

```
; lerp(a, b, t) where t is 0-255 (8-bit fixed point)
SUB  V1, Vb, Va          ; b - a
MUL  V1, V1, Vt          ; (b - a) * t
SHR  V1, V1, 8           ; >> 8 to normalize
ADD  V1, V1, Va          ; + a
```

**Micro Layer: Integer Perlin Noise**

The leaf's material_id selects a noise function. The mutator settings transform the coordinate before noise evaluation.

```
; Apply mutator rotation (simplified 2D rotation for noise field)
; rotated_x = (local_x * cos_table[rot] - local_z * sin_table[rot]) >> shift
; rotated_z = (local_x * sin_table[rot] + local_z * cos_table[rot]) >> shift

; Apply mutator scale
scaled_x = (rotated_x * mutator_scale) >> shift
scaled_y = (local_y * mutator_scale) >> shift
scaled_z = (rotated_z * mutator_scale) >> shift

; Integer Perlin noise
; 1. Hash coordinates to gradient indices
hash_x = permutation_table[(scaled_x >> 8) & 255]
hash_y = permutation_table[(hash_x + (scaled_y >> 8)) & 255]
hash_z = permutation_table[(hash_y + (scaled_z >> 8)) & 255]

; 2. Compute distance vectors to lattice corners (fractional part)
fx = scaled_x & 255    ; 8-bit fractional
fy = scaled_y & 255
fz = scaled_z & 255

; 3. Fade function: 6t^5 - 15t^4 + 10t^3 (integer approximation)
; Use lookup table: fade_table[256] precomputed
fade_x = fade_table[fx]
fade_y = fade_table[fy]
fade_z = fade_table[fz]

; 4. Gradient dot products and interpolation
; 8 gradient lookups, 7 LERPs (same structure as Gouraud)
noise_value = interpolate_gradients(hash, fade_x, fade_y, fade_z)
```

The permutation table and fade table are preloaded in shared BRAM. Each is 256 entries of i32. Total: 2 KB. The noise evaluation is ~50 integer operations.

**Final Color Composition**

```
; Combine Gouraud base with Perlin detail
; detail modulates base color per channel
final_r = (base_r * (256 + noise_value)) >> 8
final_g = (base_g * (256 + noise_value)) >> 8
final_b = (base_b * (256 + noise_value)) >> 8

; Apply material tint from leaf
final_r = (final_r * tint_r) >> 8
final_g = (final_g * tint_g) >> 8
final_b = (final_b * tint_b) >> 8

; Pack to pixel
pixel = (final_r << 16) | (final_g << 8) | final_b
```

Three multiplies and three shifts per channel. Nine operations total for final composition.

### 3.4 Radiance: Cached Lighting

Lighting is not computed per-pixel per-frame. It is probed, cached, and smoothly interpolated.

```
RadianceCell: depth 8 (8 VFR pairs per cell)
  [radiance_color,    0]    pair 0: current cached color
  [target_color,      0]    pair 1: probed target color
  [source_mask_lo,    0]    pair 2: which lights contribute (low 32 bits)
  [source_mask_hi,    0]    pair 3: which lights contribute (high 32 bits)
  [lerp_factor,      rl]    pair 4: interpolation progress (0-255 fixed)
  [epochs,            0]    pair 5: packed geometry + light epoch counters
  [priority,          0]    pair 6: probe urgency (0-255)
  [validity,          0]    pair 7: frames since last probe
```

Per frame, each beam hit checks the radiance cell:

```
if geometry_epoch_changed OR light_epoch_changed:
    if probe_budget_remaining > 0 OR priority > 128:
        ; Perform radiance probe (cast shadow rays to light sources)
        target_color = probe_lights(hit_position, light_sources)
        lerp_factor = 0   ; start smooth transition
        update epochs
        decrement probe budget
    else:
        ; Defer: increase priority, use stale data
        priority += 1

; Every frame: smooth LERP toward target
if lerp_factor < 255:
    lerp_factor = min(255, lerp_factor + lerp_rate)
    radiance = lerp(radiance, target_color, lerp_factor)
```

This gives free temporal anti-aliasing. Light changes spread smoothly over 2-5 frames. Instant events (explosions, muzzle flashes) set a snap flag that bypasses the LERP.

The radiance grid is coarser than pixel resolution. One cell covers a small spatial region. Multiple pixels share a cell. This amortizes probe cost.

### 3.5 Cymatic Physics Integration

Active voxels with cymatic state modulate the shading:

```
if leaf.has_cymatic_state:
    ; Load cymatic state for this voxel
    phi = cymatic_states[leaf.cymatic_index].phi
    temperature = cymatic_states[leaf.cymatic_index].temperature
    
    ; Temperature tint: hot voxels glow red
    if temperature > ambient:
        heat = ((temperature - ambient) * 256) / heat_range
        final_r = min(255, final_r + heat)
    
    ; Phi oscillation: subtle brightness pulse
    brightness = 256 + ((phi * 13) >> 8)    ; ±5% modulation
    final_r = (final_r * brightness) >> 8
    final_g = (final_g * brightness) >> 8
    final_b = (final_b * brightness) >> 8
```

Cymatic updates (wave propagation, CLRI enforcement, destruction) run as a separate batch pass on the FPGA before rendering. The 12-neighbor IVM averaging is 12 loads and accumulates per active voxel — a small batch operation.

### 3.6 Epsilon Splats: Post-Shading Signal Modulation

After all beams resolve, epsilon splats apply visual interference (glass, fog, glow, haze) to the pixel buffer.

```
Splat batch:
[F=splat, count=N, depth=6]

Each splat:
  [anchor_x,   0]    pair 0
  [anchor_y,   0]    pair 1
  [anchor_z,   0]    pair 2
  [radius,    rr]    pair 3
  [color,      0]    pair 4: packed ARGB
  [strength,  rs]    pair 5: intensity + blend mode in remainder
```

For each pixel, the renderer checks nearby splats (spatial hash culled) and applies color modulation:

```
for each splat near pixel:
    dist = distance(pixel_world_pos, splat_anchor)
    if dist < splat_radius:
        influence = ((splat_radius - dist) * 256) / splat_radius
        influence = (influence * splat_strength) >> 8
        
        ; Apply blend mode
        if blend_mode == ADD:
            pixel_r = min(255, pixel_r + (splat_r * influence) >> 8)
        if blend_mode == MULTIPLY:
            pixel_r = (pixel_r * (256 - influence + (splat_r * influence >> 8))) >> 8
```

Splats never affect beam traversal or physics. They are signal-domain only. Evaluated after all geometry and lighting is resolved. Deterministically ordered by layer index, no depth sorting.

### 3.7 Parallel Beam-Casting on FPGA

The screen is divided into horizontal bands. Each FPGA core owns a band. Each core casts all beams for its band independently.

```
Screen: 1920 × 1080
Cores: 30
Rows per core: 1080 / 30 = 36 rows
Pixels per core: 1920 × 36 = 69,120 pixels

Per pixel: ~200 cycles (AABB test + SVDAG drill + shading)
Per core: 69,120 × 200 = 13,824,000 cycles
At 150 MHz: 13,824,000 / 150,000,000 = 92.2 ms
```

92ms exceeds the 16.67ms budget at full resolution. Solutions:

**Reduced resolution beam-cast:** Cast at 960×540 (quarter pixels), upscale to 1080p. Each core handles 18 rows of 960 pixels = 17,280 beams. At 200 cycles each: 23ms. Still tight.

**Stochastic beam-casting:** Cast a distribution of beams, not one per pixel. Each core casts ~10,000 beams per frame into its band. Results accumulate into the pixel buffer with spatial filtering. Coverage builds over frames. At 200 cycles per beam: 10,000 × 200 / 150M = 13.3ms. Fits in budget.

**Adaptive resolution:** Near the player, cast at full density. At distance, reduce drill depth (automatic LOD via shallower SVDAG traversal). Background geometry at depth 4-5 costs ~50 cycles instead of 200.

**Hybrid ARM+FPGA:** The ARM casts background beams at reduced resolution during FPGA compute. The FPGA handles foreground at full resolution. Both write to the same framebuffer.

The optimal strategy combines all of these. The compiler analyzes scene composition and selects beam density per screen region.

### 3.8 Cycle Budget Per Pixel

```
Operation                    Cycles
─────────                    ──────
Spatial hash lookup              5
AABB intersection (2 boxes)     15
World-to-local transform        10
SVDAG drill (8 levels)          50
Popcount per level               3 × 8 = 24
PHE evaluation                  15
Gouraud interpolation           28
Perlin noise                    50
Color composition                9
Radiance lookup + LERP          15
Cymatic modulation               8
─────────────────────────────────────
Total per beam:               ~229 cycles

At 150 MHz: 1.53 µs per beam
```

---

## 4. The 2D Pipeline: Clay UI Renderer

### 4.1 Architecture

The 2D UI layer uses the Clay layout library. Clay computes layout rectangles, text positions, colors, and borders. On conventional platforms, Clay outputs are rendered via raylib and OpenGL. On VFR hardware, Clay outputs are rendered directly to the framebuffer by the ARM processor using integer pixel operations.

Clay does not need the FPGA. The ARM handles all 2D rendering because UI element counts are small (hundreds, not millions) and the operations are simple (filled rectangles, text blitting, borders).

### 4.2 Clay Output to Framebuffer

Clay produces a render command list. Each command is one of:

```
Rectangle: x, y, width, height, color, corner_radius
Text: x, y, string, font_id, size, color
Border: x, y, width, height, thickness, color
Image: x, y, width, height, image_id
Scissor: x, y, width, height (clip region)
```

The ARM iterates this list and writes pixels directly:

**Filled Rectangle:**

```zig
fn drawRect(fb: *Framebuffer, x: i32, y: i32, w: i32, h: i32, color: u32) void {
    var row: i32 = y;
    while (row < y + h) : (row += 1) {
        var col: i32 = x;
        while (col < x + w) : (col += 1) {
            fb.pixels[@intCast(usize, row * fb.pitch + col)] = color;
        }
    }
}
```

**Rounded corners** use a quarter-circle distance check at each corner:

```zig
fn isInsideRoundedRect(px: i32, py: i32, x: i32, y: i32, w: i32, h: i32, r: i32) bool {
    // Check if in corner region
    // If so, check distance squared against radius squared
    // Integer only: dx*dx + dy*dy <= r*r
}
```

**Text rendering** uses a bitmap font stored as a flat array. Each glyph is a fixed grid of 1-bit pixels. To draw a character:

```zig
fn drawGlyph(fb: *Framebuffer, glyph: []const u8, x: i32, y: i32, color: u32) void {
    for (glyph, 0..) |row_bits, row| {
        var bit: u5 = 7;
        while (bit >= 0) : (bit -= 1) {
            if ((row_bits >> bit) & 1 == 1) {
                fb.pixels[...] = color;
            }
        }
    }
}
```

**Alpha blending** for semi-transparent UI elements:

```zig
fn blend(dst: u32, src: u32, alpha: u8) u32 {
    // Per channel: result = dst + ((src - dst) * alpha) >> 8
    const dr = (dst >> 16) & 0xFF;
    const sr = (src >> 16) & 0xFF;
    const rr = dr + (((sr - dr) * alpha) >> 8);
    // repeat for green, blue
    return (rr << 16) | (rg << 8) | rb;
}
```

All integer. No floating point. No GPU. The ARM's 667 MHz is more than sufficient for a few hundred UI elements per frame.

### 4.3 UI Performance

```
Typical UI: 200 elements
Average element: 100×50 pixels = 5,000 pixels
Total pixels: 200 × 5,000 = 1,000,000 pixels
Per pixel: ~5 cycles (store, maybe blend)
Total: 5,000,000 cycles
At 667 MHz: 7.5 ms on one ARM core

With simple optimizations (skip fully occluded, memset for solid rects):
Realistic: ~2 ms per frame for full UI pass
```

The second ARM core handles UI rendering while the first ARM core manages FPGA dispatch and I/O. The two operations are fully parallel.

### 4.4 Composition Order

```
1. FPGA writes 3D pixel buffer to back framebuffer (beam-cast results)
2. ARM reads FPGA completion signal
3. ARM composites 2D UI elements on top of 3D buffer
4. ARM applies any full-screen post effects (fade, flash)
5. ARM flips front/back buffer
6. HDMI controller displays front buffer
```

The 3D and 2D layers never interfere. The 3D layer writes every pixel in its bands. The 2D layer overwrites only where UI elements exist. No depth testing between layers — UI is always on top.

---

## 5. Skeletal Animation on VFR

### 5.1 Build Box Skeletons

A character is 15-20 ContentRects linked to bones. The skeleton is a batch of bone transforms:

```
Bone batch:
[F=skeleton, count=20, depth=4]

Each bone:
  [parent_index,  0]    pair 0: -1 for root
  [rot_angle,    rr]    pair 1: rotation (VFR fixed-point)
  [offset_x,     rx]    pair 2: offset from parent
  [offset_y,     ry]    pair 3: offset from parent
```

Each frame, forward kinematics propagates transforms from root to leaves:

```
for each bone in topological order:
    if bone.parent == -1:
        world_transform[bone] = local_transform[bone]
    else:
        world_transform[bone] = compose(
            world_transform[bone.parent],
            local_transform[bone]
        )
```

Compose is integer matrix multiply. One multiply per bone. 20 bones = 20 multiplies. Trivial cost.

### 5.2 Beam-Casting Animated Characters

When a beam hits a character's Build Box, the box's world transform is already computed. The beam converts to the box's local space and drills the SVDAG as normal. The SVDAG inside never changes. Only the box's position and rotation change per frame.

Where boxes overlap at joints (elbow, knee), the beam hits whichever box's solid voxel it reaches first. This creates seamless joints without blend weights or vertex skinning. The renderer doesn't know it's drawing a character — it's just casting beams into Build Boxes.

### 5.3 Character Animation as Batch

Animation keyframes are batches of bone rotations at different times:

```
Keyframe batch:
[F=anim, count=num_keyframes, depth=20]

Each keyframe: 20 bone rotations (one per bone)
```

Interpolation between keyframes is a LERP per bone — the same integer LERP used for Gouraud shading. Animation blending (walk to run transition) is a second LERP between two keyframe results.

---

## 6. Geometric Deduplication

### 6.1 DAG Sharing

Multiple Build Boxes can reference the same SVDAG root. In a cathedral with 1000 stone pillars, there is one pillar SVDAG. Each Build Box points to it with different dimensions and mutator settings.

```
Pillar A: dimensions 0.3×3.0×0.3, mutator_rotation=0
Pillar B: dimensions 0.3×5.0×0.3, mutator_rotation=45
Pillar C: dimensions 0.5×3.0×0.5, mutator_rotation=90
```

Same SVDAG. Different box sizes stretch the normalized coordinate space. Different mutators rotate the noise field. Visual variety from a few bytes of metadata. Zero additional geometry memory.

### 6.2 Cache Implications

On the FPGA, the shared SVDAG nodes load into shared BRAM once. All cores reference the same data. When beam-casting a row of identical pillars, the SVDAG nodes are already in BRAM from the first pillar. Subsequent pillars are effectively free — the drill accesses cached data.

---

## 7. Complete Frame Pipeline

```
Per frame (16.67 ms budget at 60 FPS):

1. ARM: Process input (USB keyboard/mouse)               0.5 ms
2. ARM: Process network (Ethernet packets)                0.5 ms
3. ARM: Update game state (Silo entity pipeline)
   → Dispatch to FPGA                                    0.1 ms
4. FPGA: Entity batch processing (7 fused passes)
   → Fact generation, state machines, Prolog,
     UtilityAI, logic blocks, envelopes, traces           1.0 ms
5. FPGA: Cymatic physics update (active regions)          0.5 ms
6. FPGA: Skeletal animation (bone transforms)             0.1 ms
7. FPGA: Beam-casting (stochastic, banded)
   → SVDAG drill, PHE, Gouraud, Perlin, radiance        10.0 ms
8. ARM: Composites 2D UI (Clay layout to framebuffer)     2.0 ms
9. ARM: Epsilon splat pass                                0.5 ms
10. ARM: Flip framebuffer                                 0.01 ms
                                                    ─────────────
Total:                                                  ~15.2 ms
Headroom:                                                ~1.5 ms
```

Steps 1-3 run on ARM. Steps 4-7 run on FPGA while ARM handles steps 1-2 in parallel. Step 8 runs on ARM core 1 while ARM core 0 manages FPGA communication. Steps overlap wherever possible.

---

## 8. Automatic LOD

The SVDAG provides free level-of-detail. Drill depth determines resolution:

```
Distance from camera    Drill depth    Effective resolution
< 5 meters              8-12           256³ - 4096³
5-20 meters             6-8            64³ - 256³
20-100 meters           4-6            16³ - 64³
> 100 meters            2-4            4³ - 16³
```

Distant geometry costs fewer cycles per beam because the drill terminates earlier. The renderer adjusts drill depth per Build Box based on screen-space size. No separate LOD meshes. No LOD transitions. The same SVDAG at different traversal depths.

---

## 9. Summary

| Component | Implementation |
|---|---|
| 3D geometry | SVDAG in flat node pool, integer bitmask traversal |
| Rendering method | Beam-casting (search, not rasterization) |
| Shading macro | Gouraud trilinear interpolation, 8 corner colors, integer LERP |
| Shading micro | Integer Perlin noise, permutation table in BRAM |
| Conditional solidity | Procedural Hit Evaluator (PHE), integer math, solid→air only |
| Lighting | Radiance cell cache, epoch-driven probing, smooth LERP |
| Physics visualization | Cymatic state modulation (temperature tint, phi oscillation) |
| Transparency effects | Epsilon splats, signal-domain only, layer-ordered |
| Skeletal animation | Build Box transforms, integer matrix compose, no vertex skinning |
| Geometric deduplication | DAG sharing, multiple boxes reference same SVDAG |
| LOD | Automatic via drill depth, no separate models |
| 2D UI | Clay layout engine, ARM direct framebuffer writes |
| Text | Bitmap font, bit-blit to framebuffer |
| Alpha blending | Integer per-channel LERP |
| Framebuffer | 1920×1080 ARGB8888, double buffered, HDMI output from ARM |
| 3D parallelism | Screen banded across FPGA cores, each core casts its band |
| 2D parallelism | ARM core 1 renders UI while core 0 manages FPGA |
| Floating point | None. Entire pipeline is integer VFR arithmetic. |
| GPU dependency | None. No OpenGL, Vulkan, or GPU driver. |
| Texture files | None. All surface detail is procedural math. |
| Triangle meshes | None. All geometry is volumetric SVDAG. |

---

*Integer ALU Based Computing — Rendering Pipeline Specification v1.0*
*Companion document to ISA v1.0, Compiler v1.0, Silo-VFR Mapping v1.0, and Motherboard v2.0*