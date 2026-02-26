next, we will create a new physics engine in zig 0.15.1 using logismos, similar to havok, but it is only kspace, no xspace at all.

we will build the entire physics engine as only kspace, and then in another project, we will create the renderer for xspace, which then renders the physics system's data

we will mimic the idea of havok, but we will do it completely by the CKS axioms.  we will write pure functions where possible, we will only use structs for composition, and we will make "fat structs" so that we dont have complex structure to hide what the physics engine is doing, we make structs where natural parent-child container boundaries appear and we name them appropriately like "purpose + spefic + Child chain" because these are structs, ex:

```
pub const Soliton = struct {
  hex_plates: []**LatticeNode,
  parent: ?**Soliton, // null only for N=1
};

pub const LatticeNode = struct {
  side: [2]LatticeNodeSide,
  dipoles: [3]**LatticeNodeDipoleState,
  adjacents: [3]?**LatticeNode, // 0=alpha, 1=beta, 2=gamma.  If they exist
};


pub const LatticeNodeDipoleState = struct { // Does this exist?
  // Whats in here?
};

pub const LatticeNodeSide = struct {
  modes: []LatticeNodeSideMode, // Whats the limit?
};

pub const LatticeNodeSideMode = struct {
  data: []u8, // Not const.  Whats the payload?  How big can it be?  How small?
};

```

this is an example, not the what to use, please use it as a template and try to fill in the anwsers to the questions as fields ands comments

---

