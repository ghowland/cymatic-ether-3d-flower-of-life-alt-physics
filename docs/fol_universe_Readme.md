# 3D Flower of Life Universe Simulator

## What This Is

A minimal Python implementation of reality as cymatics - wave patterns in a continuous medium.

**The Core Idea:**
- Space = elastic medium (not empty void)
- Matter = stable standing wave patterns  
- Light = propagating waves
- All physics = interference patterns in this medium

## The Geometry

The substrate uses **Isotropic Vector Matrix (IVM)** geometry - also called the 3D Flower of Life:
- Each cell has **12 equidistant neighbors**
- This is maximum uniform connectivity in 3D
- Forms face-centered cubic (FCC) close packing
- Same geometry as closest-packed spheres

## The Physics

**Update Rule:**
Each cell oscillates based on its 12 neighbors:
```
acceleration = coupling * (neighbor_average - current_value) - damping * velocity
```

That's it. One rule. Everything emerges from this.

**What Emerges:**
- Wave propagation (light analog)
- Standing waves (matter analog)  
- Interference patterns (structure formation)
- Energy conservation (with damping)

## Running It

```bash
python3 fol_universe.py
```

**Requirements:**
- Python 3
- numpy
- matplotlib (optional, for visualization)

**What You'll See:**
- Energy oscillating as waves propagate
- Stable cells forming where interference constructive
- Patterns emerging from simple local rules

## The Code Structure

```
get_ivm_neighbors()           # 12-neighbor geometry
create_substrate()            # Initialize field + velocity
update_substrate()            # Wave equation on IVM lattice
add_interference_pattern()    # Initial conditions
run_simulation()              # Main loop
```

~250 lines total. No classes, no decorators, just functions and arrays.

## Pedagogical Mapping

| Physics Concept | Implementation | Why It Works |
|----------------|---------------|--------------|
| Space/Ether | 3D array `field` | Continuous medium |
| Matter | High amplitude stable regions | Resonant standing waves |
| Mass | Energy density (amplitude²) | Integration over pattern |
| Light | Propagating disturbance | Wave through medium |
| Inertia | Pattern stability | Resists disruption |
| Force | Pressure gradient | Neighbor asymmetry |

## What This Demonstrates

1. **Locality** - Each cell updates from immediate neighbors only
2. **Isotropy** - Same rules everywhere (no preferred direction)
3. **Emergence** - Complex patterns from simple rules
4. **Resonance** - Certain wavelengths persist (quantization analog)
5. **Interference** - Overlapping patterns create structure

## Limitations

This is a **teaching model**, not a physics engine:
- 2nd order accurate (not spectral)
- No relativity
- Simplified boundary conditions
- Classical wave equation only
- 40³ cells (not Planck scale)

But it shows the **core principle**: persistent patterns in a continuous medium.

## Extending It

Ideas for experimentation:
- Different initial patterns (pulses, vortices)
- Variable coupling (medium properties)
- Multiple wavelengths (spectrum)
- Boundary reflections (confinement)
- Pattern tracking (particle analog)
- Energy injection (field sources)

## The Pedagogical Value

This lets students:
- **See** that complex physics can emerge from simple rules
- **Feel** the locality (only neighbors matter)
- **Visualize** matter as pattern, not substance
- **Experiment** with substrate properties
- **Understand** quantization as resonance, not magic

## Key Insight

> "Reality might be patterns reconstructing themselves in a medium, where 'things' are stable interference patterns that persist because they're in resonance with the substrate geometry."

Whether this is "true" physics or "useful pedagogy" is separate from whether it helps students build intuition.

This code makes the idea concrete and testable.
