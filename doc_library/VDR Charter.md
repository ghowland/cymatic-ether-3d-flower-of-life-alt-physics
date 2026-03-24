# VDR Charter

## Purpose

VDR is a pure-mathematics program for exact finite discrete representation.

Its purpose is not to optimize for elegance, brevity, familiarity, or immediate computational speed. Its purpose is to preserve exact value-bearing structure without collapse into approximation, limit processes, hidden infinite completion, or scalar reduction inside the system.

VDR therefore operates under different design priorities than conventional mathematical formalisms. It may be larger, slower, and less aesthetically compact than standard notation, especially in early or incomplete forms. This is not treated as a foundational defect. The primary standards for VDR are exactness, inspectability, finite structure, explicit failure, and recoverable equality.

VDR is developed first as a pure mathematical system. Scientific and physical applications are downstream uses, not premises of the foundation. Physics is not part of the axiomatic basis of VDR, but it is recognized as an important later test of expressive strength and practical utility.

---

## Scope

VDR is a pure-mathematics system for exact finite discrete representation in native triple form.

Its practical target domain is not arbitrary writable scalar strings, but the mathematically and scientifically meaningful values required by established scientific computation. These values must be admitted either by exact specification in VDR form or by exact derivation from accepted rules and constructions.

Scalar projection is secondary to native VDR identity, but mandatory for interoperability, benchmarking, validation, and comparison with measured data.

VDR does not claim in advance that every scalar notation artifact, every writable decimal object, or every arbitrary real-like expression belongs to its domain. Objects without constructive meaning are not automatically in scope. The target of VDR is exact constructive value, not arbitrary symbolic writability.

Short scope statement:

VDR is pure mathematics first, aimed at exact finite discrete representation of the mathematically and scientifically meaningful values required by established scientific computation.

---

## Foundational Principles

### 1. Pure Mathematics First

VDR is founded as a pure mathematical system. Scientific and physical applications are downstream uses, not premises of the foundation.

### 2. Finite Discrete Exactness

A valid VDR object is completely given by finite discrete structure.

Native VDR reasoning does not depend on:
- approximation,
- limits,
- hidden infinite tails,
- deferred completion,
- epsilon-style acceptance,
- or asymptotic convergence.

### 3. Triple Irreducibility

A valid VDR object is natively triple-structured.

Inside VDR, triple form is primary and may not be replaced by scalar form without leaving the system.

### 4. Structural Conservation

Value-bearing structure produced by valid VDR construction is preserved rather than discarded for simplification, truncation, or scalar convenience.

No exact residual structure may be treated as nonessential merely because another notation would suppress it.

### 5. Internal Structural Equality Priority

Inside VDR, structural equality and structural non-equality are primary native relations.

Approximate agreement, tolerance bounds, and “close enough” are never native substitutes for equality.

### 6. Finite Native Operations

Primitive operations on valid finite VDR inputs must terminate in finite time with either:
- a valid finite VDR result, or
- explicit failure / undefined status.

No native operation may depend on nonterminating search, infinite descent, or approximation rescue.

### 7. Inspectability

Every valid VDR object must be finitely traversable and exactly inspectable in its parts.

A valid VDR object must be knowable by finite reading of its structure. No hidden continuation may be required to complete what the object is.

---

## Interoperability Requirements

### 8. Mandatory Scalar Projection

Outside VDR, scalar projection is required for:
- interoperability,
- benchmarking,
- validation,
- measurement comparison,
- and communication with existing mathematical and computational practice.

A VDR system that cannot project outward to scalar form cannot be tested against the scalar world in which it is intended to be useful.

### 9. Secondary External Role of Scalars

Scalar projection is not native VDR identity.

It is an external comparison layer. When scalar projection is lossy, that loss belongs to the target scalar system, not to missing information in the VDR object itself.

VDR is exact internally even when exported scalar representations are approximate.

### 10. Exact Specification and Exact Derivation

Objects may enter or exist within VDR in two distinct ways:

- Exact specification:
  - an object is admitted directly in valid native VDR form

- Exact derivation:
  - an object is obtained from prior admitted objects, axioms, or rules by an exact finite VDR construction

Specification states what the object is in VDR.
Derivation states how it is obtained in VDR.

These are not identical and must not be conflated.

### 11. Restricted External Scope

VDR targets mathematically and scientifically meaningful values, especially the values required by established scientific computation.

VDR does not automatically target arbitrary notation artifacts, malformed scalar strings, or expressions lacking exact constructive meaning.

Thus VDR’s practical admission boundary is determined by exact constructive significance, not by mere writability in an external notation.

---

## Native and External Distinctions

### 12. Native Identity

A VDR object is natively an exact triple-structured object.
Its native identity is not exhausted by any scalar image or external decimal rendering.

### 13. Derivational Provenance

A VDR object may possess derivational provenance when it is shown to arise from prior axioms, rules, or constructions.
This provenance is part of the system’s exact intelligibility, but is distinct from the object’s mere admission by specification.

### 14. Scalar Projection

A VDR object may be projected outward into scalar form for external comparison.

Scalar projection says how a VDR object is compared outside VDR.
It does not define what the object is inside VDR.

Shortest distinction:

- specification says what the object is in VDR
- derivation says how it is obtained in VDR
- scalar projection says how it is compared outside VDR

---

## Success Criteria and Practical Validation Tests

The following are not foundational axioms. They are standards by which VDR should be judged as a serious practical program.

### 15. Equality Recovery

For supported domains, equality and non-equality should be decidable from VDR structure itself.

This is one of the central practical reasons for VDR to exist.

### 16. Reach Beyond Standard Scalar Practice

VDR should support important value classes beyond ordinary fractions and floating-point methods.

If it cannot reach beyond what existing scalar methods already provide, its foundational cost is unlikely to be justified.

### 17. Practical Utility

VDR does not justify itself by elegance, compactness, or immediate speed.

It may be larger, slower, and harder to use than scalar methods. Its justification is practical only if its exact internal structure yields useful capabilities that scalar-only approximation pipelines do not preserve.

### 18. Long-Chain Computational Advantage

On at least some important classes of long computations, VDR should export scalar results that outperform approximation-dominant scalar pipelines enough to justify adoption.

This advantage may appear through:
- reduced drift,
- stronger equality recovery,
- better stability under repeated operations,
- greater auditability,
- or other exactness-preserving effects unavailable to scalar-only workflows.

### 19. Benchmarkability

VDR results should be comparable against:
- conventional scalar mathematics,
- conventional software implementations,
- and measured data where relevant.

Without benchmarkability, VDR cannot establish practical standing in the world where scalar methods currently dominate.

---

## Research Ambitions

The following are ambitions of the VDR program, not prerequisites of the foundational charter.

### 20. Broad Exact Representational Reach

A major ambition of VDR is to extend exact finite representation to wider classes of values arising in mathematics and scientific modeling.

### 21. Support for Conventionally Nonterminating Values

A major ambition of VDR is to support values now commonly handled through:
- symbolic constants,
- infinite expansions,
- approximation-based real analysis,
- or nonterminating scalar representations.

This includes values such as:
- irrational constants,
- transcendental constants,
- and other non-rational targets,
provided they admit exact constructive VDR form.

### 22. Eventual Scientific Ceiling

A strong long-term ambition is to support enough exact structure for domains now handled by real-number approximations in established scientific computation.

This is the practical ceiling by which VDR’s expressive power may eventually be judged.

### 23. Physics as a Hard Downstream Test

Physics is not part of the foundation of VDR.

However, eventual support for the values, constants, and operations used in physics is an important outer test of whether VDR has the expressive strength and practical utility to matter beyond niche mathematical use.

### 24. Possible Derivational Discovery

If VDR succeeds at exact finite representation beyond current scalar practice, it may permit derivation of values now treated as primitive givens in mathematics or physics.

This is not assumed by the foundation.
It is a possible downstream result of success.

---

## Completeness Horizon

VDR is complete only in the strongest sense if it can do all of the following:

1. represent the mathematically and scientifically meaningful values required by established scientific computation in exact finite VDR structure,
2. admit those objects by exact specification or exact derivation,
3. preserve exact native equality without approximation inside the system,
4. project outward into scalar form for comparison with existing mathematics and measurement,
5. and maintain enough practical advantage over approximation-dominant scalar pipelines to justify adoption.

This is the horizon of the program, not a claim of current completion.

---

## Practical Standard of Judgment

VDR is not entertainment mathematics.

It is not pursued merely for novelty, aesthetic deviation, or symbolic complexity. It is pursued because exact equality, preserved structure, and finite inspectability may open mathematical and practical possibilities that approximation-dominant scalar systems cannot provide.

If VDR succeeds, it should create a better path to utility in domains where loss of equality currently hides structure, accumulates drift, or blocks exact understanding.

If VDR fails to meet that practical ceiling, then that failure should be documented clearly, so that the boundary itself becomes useful knowledge for future work.

---

## Charter Summary

VDR is a pure mathematical program for exact finite discrete representation in irreducible triple form.

Its foundation is:
- finite exactness,
- triple irreducibility,
- structural conservation,
- equality priority,
- finite terminating operations,
- and inspectability.

Its interoperability requirement is:
- mandatory scalar projection for external comparison without granting scalar form native authority inside the system.

Its practical standard is:
- useful exactness and long-chain computational advantage sufficient to justify adoption over approximation-dominant scalar workflows.

Its ambition is:
- broad exact representational reach across the values required by established scientific computation, including values now treated as nonterminating, symbolic, or approximation-bound.

That is the VDR charter.

---


# VDR
## Foundational Axioms v1

### 1. Primitive Object Axiom
A VDR object is a triple of the form

$$
[V, D, R]
$$

where:
- \(V\) is the value slot,
- \(D\) is the denominator slot,
- \(R\) is the residual slot.

A valid native VDR object always has exactly these three slots.

### 2. Triple Irreducibility Axiom
Inside VDR, the triple is irreducible.

No valid VDR object may be replaced internally by:
- a scalar,
- a pair,
- a single integer,
- or any reduced shorthand that discards one of the three slots.

Even when \(R = 0\), the object remains a VDR triple.

### 3. Integer Slot Axiom
For every valid VDR object:

$$
V \in \mathbb{Z}
$$

$$
D \in \mathbb{Z} \setminus \{0\}
$$

So:
- the value slot is always an integer,
- the denominator slot is always a nonzero integer.

### 4. Residual Slot Axiom
For every valid VDR object, the residual slot \(R\) is a valid residual object.

A residual object may contain exact finite residual structure, including nested VDR objects, according to the residual formation rules.

### 5. Residual Locality Axiom
Recursive VDR structure may appear only in the residual slot.

No VDR object may appear recursively inside:
- \(V\),
- or \(D\).

Thus recursion is local to the third slot only.

### 6. Finite Structure Axiom
Every valid VDR object must have finite structure.

Its full recursive expansion must:
- terminate after finite depth,
- contain finitely many nodes,
- and have finite branching at every node.

No infinite VDR object is valid.

### 7. Exactness Axiom
A valid VDR object is exact as written.

No valid VDR object may depend for its identity on:
- approximation,
- limit interpretation,
- hidden continuation,
- deferred tail completion,
- or epsilon-style acceptance.

### 8. Structural Conservation Axiom
Any exact residual structure present in a valid VDR object is value-bearing structure.

It may not be discarded, ignored, or replaced internally merely for convenience, simplification, or scalar resemblance.

### 9. Inspectability Axiom
Every valid VDR object must be finitely inspectable.

That means:
- every slot can be read exactly,
- every nested node can be traversed,
- and the total object can be known by finite inspection of its structure.

### 10. Finite Operation Axiom
Every primitive native VDR operation must, on valid finite inputs, terminate in finite time with either:
- a valid finite VDR result,
- or explicit failure / undefined status.

No native operation may rely on nonterminating search or approximation rescue.

### 11. Native Equality Priority Axiom
Inside VDR, exact equality and exact non-equality are primary.

Approximate agreement, tolerance, or scalar closeness are never native substitutes for equality.

The exact equality relations themselves may be defined in later axioms, but they must be exact and finite in character.

### 12. Scalar Externality Axiom
Scalar form is not the native identity of a VDR object.

Any mapping from a VDR object to:
- a rational,
- a real,
- a decimal,
- a float,
- or another scalar system

is an external projection, not an internal reduction of the VDR object.

### 13. Admissibility Axiom
A VDR object is valid if and only if it satisfies:
- triple form,
- integer slot constraints,
- residual formation constraints,
- residual locality,
- finite structure,
- exactness,
- and inspectability.

### 14. Foundation-First Axiom
These foundational axioms define only:
- what a VDR object is,
- and what constraints validity imposes.

They do not yet define:
- arithmetic,
- normalization,
- scalar projection rules,
- derivation procedures,
- or application-layer interpretation.

Those belong to later layers.

---

# VDR
## Residual Formation Rules v1

These rules define what may appear in the third slot \(R\) of a valid VDR object.

They do not yet define arithmetic meaning, normalization, or scalar projection. They define admissible residual structure only.

### 15. Residual Domain Rule
A valid residual object belongs to the residual domain \( \mathcal{R} \).

Every residual slot \(R\) in a valid VDR object must satisfy:

$$
R \in \mathcal{R}
$$

### 16. Atomic Residual Rule
An atomic residual is any integer:

$$
r \in \mathbb{Z}
$$

Every integer is a valid residual object.

So:

$$
\mathbb{Z} \subseteq \mathcal{R}
$$

In particular, \(0\) is a valid residual object.

### 17. Nested Residual Rule
A residual object may also be formed from:
- one atomic integer base,
- together with a finite collection of child VDR objects.

So a residual may take the form:

$$
R = r + X_1 + X_2 + \dots + X_n
$$

where:
- \(r \in \mathbb{Z}\),
- each \(X_i\) is a valid VDR object,
- \(n \in \mathbb{N}\) is finite.

This is a structural formation rule, not yet an arithmetic interpretation rule.

### 18. Finite Child Rule
A residual object may contain only finitely many immediate child VDR objects.

No valid residual may contain:
- infinitely many children,
- or an implicitly infinite child list.

### 19. Residual Recursion Rule
If a child \(X_i\) appears in a residual, then that child must itself be a valid VDR object satisfying all foundational axioms and residual formation rules.

Thus residual structure is recursively closed over valid finite VDR objects.

### 20. Residual Locality Rule
Nested VDR objects may appear only as children in residual structure.

Residual recursion may not move into:
- the value slot \(V\),
- or the denominator slot \(D\).

This restates at the residual layer that recursion is confined to the third slot.

### 21. Residual Exactness Rule
A valid residual object is exact as written.

No valid residual may rely on:
- approximation,
- hidden infinite continuation,
- deferred terms,
- ellipsis,
- or limit-style completion.

If the residual cannot be fully and finitely written, it is not valid in v1.

### 22. Residual Inspectability Rule
A valid residual object must be finitely inspectable.

That means:
- its atomic integer part can be read exactly,
- its child list can be enumerated exactly,
- and each child can be recursively inspected in finite time.

### 23. Residual Zero Rule
The integer \(0\) is the canonical atomic residual with no additional child structure.

It is a valid residual object and serves as the simplest closed residual form.

### 24. Residual Structural Form Rule
At v1, residual structure is admitted in one of two forms only:

1. atomic form:
$$
R = r \quad \text{where } r \in \mathbb{Z}
$$

2. atomic-plus-children form:
$$
R = r + X_1 + X_2 + \dots + X_n
$$

where \(n\) is finite.

No other primitive residual forms are admitted at this stage.

### 25. Residual Admissibility Rule
A residual object is valid in v1 if and only if it satisfies:
- atomic integer base,
- finite child collection if present,
- recursive child validity,
- exactness,
- and finite inspectability.

### 26. Residual Meaning Deferral Rule
These residual formation rules define only admissible structure.

They do not yet decide:
- how residuals compare,
- how residuals combine,
- how residuals project to scalars,
- or how residuals participate in arithmetic.

Those belong to later semantic and operational layers.

This gives you a clean structural base:
- residuals are integers plus finite child VDR structure
- recursion is only through residuals
- everything stays finite and exact

---

# VDR
## Structural Equality and Validity Rules v1

These rules define:
- when a VDR object is valid as a native object,
- and when two VDR objects are structurally equal as written.

They do not yet define value equality, normalization, arithmetic, or scalar projection.

---

### 27. Raw Validity Rule
A VDR object is raw-valid in v1 if and only if it satisfies:
- the foundational axioms,
- the residual formation rules,
- and the triple form requirement.

So a raw-valid object must be:
- exactly a triple,
- integer-based in \(V\) and \(D\),
- nonzero in \(D\),
- finite in full recursive structure,
- exact,
- and finitely inspectable.

---

### 28. Triple Form Validity Rule
A raw-valid VDR object must have the form:

$$
[V, D, R]
$$

with exactly three slots.

No raw-valid object may have:
- fewer than three slots,
- more than three slots,
- missing slots,
- or alternate primitive shapes.

---

### 29. Denominator Nonzero Validity Rule
A raw-valid VDR object must satisfy:

$$
D \neq 0
$$

Any object with denominator slot \(D = 0\) is invalid.

---

### 30. Residual Validity Rule
A raw-valid VDR object must have a residual slot \(R\) that is itself a valid residual object under the residual formation rules v1.

So if:

$$
[V, D, R]
$$

is raw-valid, then:

$$
R \in \mathcal{R}
$$

and \(R\) must be finitely exact and recursively valid.

---

### 31. Recursive Validity Rule
If a VDR object contains child VDR objects in its residual slot, then each child must itself be raw-valid.

Thus raw validity is recursive through the residual slot.

A single invalid child makes the parent invalid.

---

### 32. Finite Whole-Object Validity Rule
A raw-valid VDR object must remain finite when considered as a whole recursive structure.

This means:
- finite depth,
- finite total node count,
- and finite child count at every node.

No object with infinite recursive expansion is valid.

---

### 33. Structural Equality Rule
Two raw-valid VDR objects are structurally equal if and only if they match exactly, slot by slot, recursively and in order.

Write structural equality as:

$$
X \equiv_s Y
$$

For VDR objects:

$$
[V_1,D_1,R_1] \equiv_s [V_2,D_2,R_2]
$$

if and only if:
- \(V_1 = V_2\),
- \(D_1 = D_2\),
- and \(R_1 \equiv_s R_2\).

---

### 34. Atomic Residual Structural Equality Rule
For atomic residual integers:

$$
r_1 \equiv_s r_2
\iff
r_1 = r_2
$$

So atomic residual structural equality is ordinary integer equality.

---

### 35. Composite Residual Structural Equality Rule
For composite residuals of the form:

$$
R_1 = r_1 + X_1 + X_2 + \dots + X_n
$$

and

$$
R_2 = s_1 + Y_1 + Y_2 + \dots + Y_m
$$

we have:

$$
R_1 \equiv_s R_2
$$

if and only if:
- \(r_1 = s_1\),
- \(n = m\),
- and for each index \(i\), \(X_i \equiv_s Y_i\).

So in v1:
- child count matters,
- child order matters,
- exact recursive match matters.

---

### 36. Structural Inequality Rule
Two VDR objects are structurally unequal if they fail structural equality at any level.

Any difference in:
- value slot,
- denominator slot,
- atomic residual base,
- child count,
- child order,
- or any descendant structure

makes the objects structurally unequal.

---

### 37. Structural Equality Scope Rule
Structural equality is equality of representation as written.

It does not yet mean:
- value equality,
- normalized equality,
- scalar equality,
- or arithmetic equivalence.

Those may be introduced later as distinct relations.

---

### 38. Raw Validity vs Canonicality Rule
A raw-valid VDR object need not be canonical, simplified, normalized, reduced, or uniquely presented.

At v1, validity concerns admissible exact structure only.

Canonical form, if later introduced, is a separate layer.

---

### 39. Raw Validity vs Derivation Rule
A raw-valid VDR object need not be derivable from prior objects in v1.

It may be admitted by exact specification alone, provided it satisfies all validity constraints.

Thus:
- validity is not the same as derivability,
- and admissibility is not the same as provenance.

---

### 40. Structural Layer Closure Rule
The v1 structural layer defines only:
- admissible objects,
- admissible residuals,
- recursive validity,
- and structural equality.

It does not yet define:
- value semantics,
- normalization,
- arithmetic,
- scalar projection,
- or completeness of representation classes.

Those belong to later layers.

---

## Summary of v1 Structural Layer

At this stage, VDR now has:

1. foundational object rules
2. residual formation rules
3. raw validity rules
4. structural equality

So you can now clearly say:
- what counts as a legal VDR object
- and when two legal VDR objects are exactly the same as written

That is enough to begin a data model and parser.

---

# VDR
## Native Semantic Rules v1

These rules define the first native semantic layer of VDR.

They do not yet define:
- normalization,
- arithmetic,
- canonical equivalence,
- or scalar export algorithms.

Their purpose is to state what kind of object a VDR is natively, and what semantic commitments follow from the charter and structural layer.

---

### 41. Native Object Rule
A valid VDR object is natively an exact triple-structured object.

Its native meaning is not exhausted by any scalar reading, decimal rendering, rational collapse, or external comparison image.

A VDR object is first an object of VDR, not first a number in another system.

---

### 42. Triple-State Semantic Rule
The three slots of a VDR object are semantically distinct.

For:

$$
[V,D,R]
$$

- \(V\) is not identical to \(D\),
- \(D\) is not identical to \(R\),
- \(R\) is not metadata,
- and no slot may be semantically erased merely because another notation would compress the form.

Thus the triple is semantically structured, not merely syntactically grouped.

---

### 43. Residual Significance Rule
The residual slot \(R\) is exact value-bearing native structure.

A nonzero residual is not:
- error,
- noise,
- approximation residue,
- ignored remainder,
- or dispensable annotation.

It is part of the exact native object.

---

### 44. Closed and Active Semantic Rule
A VDR object may be semantically classified in one of two native states:

1. Closed:
$$
[V,D,0]
$$

2. Active:
$$
[V,D,R]
\quad\text{with } R \neq 0
$$

A closed object has no residual structure beyond zero.
An active object contains additional exact residual structure still present in the object.

This is a native semantic distinction, not yet a value-equality rule.

---

### 45. Global Closure Rule
A VDR object is globally closed if and only if:
- its top-level residual is zero,
- and every descendant residual in its full recursive structure is also zero.

Thus closure is global across the whole object, not merely local at the top node.

---

### 46. Residual Completion Rule
Native VDR semantics treat the residual as completion structure of the parent triple.

Thus for:

$$
[V,D,R]
$$

the residual is read natively as exact completion of the triple-state, not as discarded leftover.

At v1 this states semantic role only.
It does not yet define arithmetic flattening or scalar projection.

---

### 47. Non-Error Rule
No valid residual structure may be interpreted natively as numerical defect.

A nonzero residual does not mean the VDR object has failed to settle.
It means the exact object includes further structure.

Failure and active residual are not the same thing.

---

### 48. Recursive Completion Rule
If a residual contains child VDR objects, then each child is itself a native VDR object with its own exact triple-state and residual significance.

Thus native semantic structure is recursively compositional:
- each child remains fully a VDR object,
- and residual nesting preserves native identity at every level.

---

### 49. Structural Meaning Priority Rule
At v1, native semantic meaning follows native structure before any scalar interpretation.

So if two objects differ structurally, they are natively distinct as written unless and until a later semantic or normalization layer proves a further equivalence relation.

This preserves the priority of internal structure over external projection.

---

### 50. No Native Scalar Collapse Rule
Inside VDR, no object may be semantically identified with:
- a rational,
- a real,
- a decimal,
- a float,
- or any scalar value
merely because an external projection may later associate the object with one.

Native VDR identity is not scalar identity.

---

### 51. Semantic Deferral Rule
At v1, native semantics do not yet fully determine:
- value equality,
- arithmetic behavior,
- normalization targets,
- or scalar projection formulas.

They establish only that:
- VDR objects are native exact triple-states,
- residual structure is exact completion structure,
- closure and activity are semantically meaningful,
- and scalar interpretation is external rather than primary.

---

### 52. Native Distinctness Rule
Two raw-valid VDR objects that are structurally distinct remain semantically distinct at the native layer unless a later rule explicitly introduces a stronger equivalence relation.

Thus native v1 semantics do not silently identify different structures.

---

### 53. Semantic Layer Boundary Rule
The v1 native semantic layer commits VDR to:
- triple-state ontology,
- residual significance,
- closure/activity distinction,
- recursive completion structure,
- and anti-collapse semantics.

It does not yet commit VDR to:
- additive flattening,
- denominator rebasing rules,
- child absorption,
- normalized comparison,
- or scalar numerical interpretation.

Those belong to later layers.

---

## Summary of Native Semantics v1

At this stage, VDR says:

- a VDR object is natively a triple-state
- the residual is exact completion structure
- residual is not error
- active and closed objects are semantically distinct
- closure is global
- scalar identity is external, not native
- structural difference remains meaningful unless a later layer proves equivalence

This is the right place to stop before normalization.

---

# VDR
## Normalization Rules v1

These rules define the first canonicalization layer of VDR.

They do not define full arithmetic, value equality, or general scalar meaning. Their purpose is to specify when a raw-valid VDR object may be rewritten into a more canonical structural form without changing its native exact status.

Normalization in v1 is:
- exact,
- finite,
- deterministic where defined,
- and representation-oriented.

It is not a condition of raw validity.

---

### 54. Normalization Existence Rule
Every raw-valid VDR object may be submitted to a normalization procedure.

If normalization succeeds, it returns a raw-valid VDR object in normalized form.
If a proposed normalization step would violate foundational or semantic constraints, that step is invalid.

Normalization does not create non-VDR objects.

---

### 55. Normalization Non-Validity Rule
A raw-valid VDR object need not already be normalized.

Validity and normalization are distinct.

Thus a VDR object may be:
- valid but non-normal,
- or valid and normal.

---

### 56. Normalization Preservation Rule
Every valid normalization step must preserve native exact structure in the sense intended by the normalization layer.

Normalization may change representation, but it may not:
- discard value-bearing residual structure,
- collapse a VDR object into scalar form,
- introduce approximation,
- or violate triple irreducibility.

---

### 57. Finite Normalization Rule
Normalization must terminate in finite time on every finite raw-valid VDR object for which the normalization rules are defined.

Normalization may not rely on:
- infinite descent,
- approximation,
- hidden completion,
- or nonterminating search.

---

### 58. Child Normalization Rule
If a VDR object contains child VDR objects in its residual structure, normalization proceeds recursively on the children as part of whole-object normalization.

Thus normalized parent form requires normalized child form wherever child normalization is defined.

---

### 59. Atomic Residual Consolidation Rule
Within a residual, all atomic integer contribution at the same residual level must be consolidated into a single integer base in normalized form.

So normalized residual structure at a given level has exactly one atomic integer base.

At v1 this is a structural canonicality rule, not yet an arithmetic law across denominators.

---

### 60. Zero Residual Canonical Rule
A normalized closed VDR object has residual exactly:

$$
0
$$

No alternate zero-like residual structure is allowed in normal form.

Thus closed normalized objects use the canonical residual zero.

---

### 61. Sign Placement Rule
Normalization may adopt a fixed sign convention for the value and denominator slots.

A standard v1 convention is:
- denominator positive in normalized form

So if:

$$
[V,D,R]
\quad\text{with } D < 0
$$

then normalization may rewrite sign placement to produce an equivalent normalized sign arrangement.

This is a canonicality rule, not a raw-validity rule.

---

### 62. Closed Fraction Reduction Rule
For a closed VDR object:

$$
[V,D,0]
$$

normalization reduces the pair \((V,D)\) by their greatest common divisor, subject to the chosen sign convention.

Thus closed normalized form uses reduced numerator and denominator.

This rule applies only to closed nodes at v1.

---

### 63. Child Same-Denominator Absorption Rule
If a parent VDR object has a child VDR in its residual whose top-level denominator matches the parent denominator, then that child should not remain a separate child in normalized form when exact absorption into the parent level is defined.

In such cases, normalization should absorb that same-denominator child into the parent’s local structure rather than preserve redundant denominator duplication.

At v1 this rule is admitted as a canonicality principle, with exact absorption mechanics to be made explicit in later operational rules.

---

### 64. Duplicate Child Ordering Rule
Normalized residual child lists must be ordered by a fixed deterministic rule.

A v1 canonical ordering may be:
1. by denominator magnitude,
2. then by value slot,
3. then by residual structure.

Any deterministic total ordering is acceptable if used consistently.

---

### 65. Child List Canonicality Rule
In normalized form, immediate residual children must appear in canonical order.

Thus two raw-valid objects differing only by child order may normalize to the same child ordering pattern once normalization is fully defined.

At v1 this is a canonical structural policy, not yet a statement of full value equality.

---

### 66. Duplicate-Structure Merge Rule
If two immediate residual children are identical in normalized structure and a later-defined merge operation preserves native exact structure, normalization may merge them.

At v1 this is a reserved canonicality rule:
- permitted in principle,
- but dependent on later semantic and operational definitions.

So it is not yet mandatory except where an exact merge law is later supplied.

---

### 67. Redundant Child Exclusion Rule
A normalized residual should not contain structurally redundant child configurations when a simpler exact local representation is already available under the normalization rules.

This is a general anti-redundancy principle for canonical form.

At v1 it guides normalization policy without yet exhausting all cases.

---

### 68. Child Zero Canonical Rule
A normalized residual child may not remain in a non-canonical zero form if an exact canonical zero representation is available.

So zero-like child structures should normalize to their canonical zero representation where defined.

Exact zero-child elimination mechanics may be refined later.

---

### 69. Normal Form Rule
A raw-valid VDR object is in v1 normal form if and only if all of the following hold:

1. it is raw-valid,
2. all child VDR objects are themselves in normal form,
3. its sign placement follows the chosen canonical sign convention,
4. any closed node is reduced by gcd,
5. its residual has exactly one atomic integer base at each level,
6. its child list is in canonical order,
7. no same-denominator child remains unabsorbed where exact absorption is defined,
8. no locally redundant canonical simplification remains unapplied where defined.

---

### 70. Normalization Scope Rule
The v1 normalization layer defines:
- canonical sign placement,
- closed-node reduction,
- residual atomic consolidation,
- child ordering,
- and reserved same-denominator absorption policy.

It does not yet fully define:
- value equality,
- arithmetic equivalence,
- full child merge laws,
- cross-denominator simplification,
- or scalar projection semantics.

Those belong to later layers.

---

### 71. Normalization Optionality Rule
Normalization is required for canonical comparison, serialization, and stable implementation behavior where those are defined.

Normalization is not required merely for an object to exist validly in VDR.

Thus raw authoring and canonical representation remain distinct.

---

## Summary of Normalization v1

At this stage, normalization gives you:

- valid versus normal distinction
- canonical sign handling
- reduced closed forms
- one atomic residual base per level
- deterministic child ordering
- a placeholder principle for same-denominator absorption
- anti-redundancy direction without overcommitting semantics too early

This is enough to support:
- canonical storage goals
- parser / serializer planning
- and later equality refinement

---

# VDR
## Value Equality Rules v1

These rules define the first non-structural equality layer of VDR.

They do not yet define full arithmetic or full scalar semantics. Their purpose is to distinguish:
- equality as written,
from
- equality as a normalized native VDR object.

At v1, value equality remains internal to VDR and is not yet identified with external scalar equality.

---

### 72. Equality Layer Distinction Rule
VDR distinguishes at least two equality relations:

1. Structural equality
2. Value equality

These are not identical.

Structural equality asks:
- are two VDR objects written the same, slot by slot?

Value equality asks:
- do two VDR objects settle to the same normalized native VDR form under the currently defined normalization rules?

---

### 73. Structural Equality Priority Rule
Structural equality remains the primary equality relation of raw representation.

If two objects are structurally equal, then they are also value-equal.

So:

$$
X \equiv_s Y \implies X \equiv_v Y
$$

for all raw-valid VDR objects \(X, Y\).

---

### 74. Value Equality Rule
Two raw-valid VDR objects are value-equal in v1 if and only if their normalized forms are structurally equal.

Write value equality as:

$$
X \equiv_v Y
$$

Then:

$$
X \equiv_v Y
\iff
\mathrm{norm}(X) \equiv_s \mathrm{norm}(Y)
$$

provided normalization is defined for both objects.

---

### 75. Normalization Dependence Rule
Value equality in v1 is defined through normalization.

Thus value equality depends only on currently admitted normalization rules, not yet on:
- scalar projection,
- arithmetic equivalence,
- or external numeric interpretation.

This keeps v1 value equality internal to VDR.

---

### 76. Reflexivity Rule
For every raw-valid VDR object \(X\),

$$
X \equiv_v X
$$

So value equality is reflexive.

---

### 77. Symmetry Rule
For all raw-valid VDR objects \(X, Y\),

$$
X \equiv_v Y \implies Y \equiv_v X
$$

So value equality is symmetric.

---

### 78. Transitivity Rule
For all raw-valid VDR objects \(X, Y, Z\),

$$
X \equiv_v Y \land Y \equiv_v Z \implies X \equiv_v Z
$$

So value equality is transitive.

---

### 79. Structural Difference Compatibility Rule
Two VDR objects may be structurally unequal while still being value-equal.

This occurs when their raw forms differ but normalization settles them to the same canonical native form.

Thus:

$$
X \not\equiv_s Y
$$

does not imply

$$
X \not\equiv_v Y
$$

---

### 80. Structural Equality Sufficiency Rule
If two raw-valid VDR objects are structurally equal, then no further normalization comparison is needed.

Structural equality is sufficient for value equality.

So structural equality is the strongest exact match relation at v1.

---

### 81. Closed Reduced Equality Rule
For closed VDR objects, value equality is determined by normalized reduced closed form.

Thus differently written closed objects may be value-equal if normalization reduces them to the same canonical closed triple.

Examples include:
- sign-normalized forms,
- gcd-reduced forms,
- and other later-allowed closed canonical rewrites.

At v1, this remains internal and normalization-based.

---

### 82. Child Order Insensitivity Through Normalization Rule
If two raw-valid VDR objects differ only by immediate child order at a residual level, and normalization reorders those children canonically, then they may be value-equal even though not structurally equal.

So child order may matter structurally but not necessarily at the level of value equality after normalization.

---

### 83. Same-Denominator Child Absorption Compatibility Rule
If same-denominator child absorption is defined and normalization absorbs such child structure into the parent level, then a raw-valid object with explicit same-denominator child structure may be value-equal to the corresponding absorbed normalized form.

Thus same-denominator redundancy may disappear at the level of value equality once the normalization rule is made explicit enough to apply.

---

### 84. No External Collapse Rule
Value equality in v1 does not mean:
- scalar equality,
- rational equality,
- decimal equality,
- float equality,
- or equality under any external system.

It is purely an internal VDR equality relation defined through normalization.

---

### 85. No Approximation Equality Rule
No approximate test may establish value equality in v1.

Value equality may not be decided by:
- tolerance,
- epsilon bounds,
- decimal closeness,
- floating-point comparison,
- or convergent estimate.

Only exact normalization-based comparison is valid.

---

### 86. Value Distinctness Rule
If two normalized raw-valid VDR objects are structurally unequal, then they are value-distinct in v1.

So:

$$
\mathrm{norm}(X) \not\equiv_s \mathrm{norm}(Y)
\implies
X \not\equiv_v Y
$$

provided normalization is defined for both.

---

### 87. Equality Scope Rule
The v1 equality layer defines only:
- structural equality,
- value equality through normalization,
- and their formal relation.

It does not yet define:
- arithmetic equality,
- derivational equivalence,
- semantic equality under scalar projection,
- or equality across broader representational classes.

Those belong to later layers.

---

### 88. Equality Decidability Rule
For every raw-valid finite VDR object for which normalization is defined and terminating, value equality is decidable in finite time by:
1. normalizing both objects,
2. then applying structural equality to the normalized results.

This gives v1 an exact finite equality test within its admitted normalization scope.

---

## Summary of Value Equality v1

At this stage, VDR has:

- structural equality:
  exact same object as written

- value equality:
  same normalized native object

So v1 now supports the idea that:
- multiple raw forms may represent one canonical native form
- but equality remains entirely internal and exact
- and scalar comparison is still deferred

---

# VDR
## Scalar Projection Rules v1

These rules define the first external comparison layer of VDR.

They do not redefine native VDR identity. Their purpose is to specify how a VDR object may be mapped outward into scalar-oriented systems for:
- interoperability,
- benchmarking,
- validation,
- comparison with conventional mathematics,
- and comparison with measured data.

Scalar projection is external, secondary, and may be lossy in practical target systems.

---

### 89. Projection Externality Rule
Scalar projection is an external operation on a valid VDR object.

It does not change what the object is inside VDR.

So if a VDR object \(X\) is projected outward into some scalar target \(S\), the projection is a comparison image of \(X\), not a reduction of native VDR identity.

---

### 90. Projection Domain Rule
Scalar projection is defined only for raw-valid VDR objects.

A projection procedure may require normalization first where the target comparison protocol depends on canonical form.

Invalid VDR objects have no scalar projection.

---

### 91. Projection Target Rule
A scalar projection may target external systems such as:
- rational form,
- real-number form,
- decimal form,
- floating-point form,
- or another scalar comparison system.

Different targets may require different projection procedures.

Thus scalar projection is target-dependent.

---

### 92. Projection Layer Distinction Rule
Scalar projection is not:
- structural equality,
- value equality,
- derivation,
- or normalization.

It is a separate external mapping layer.

So two VDR objects may:
- be distinct natively,
- yet share some external scalar projection,
or
- fail to share an external scalar projection,
depending on the projection target and level of approximation.

---

### 93. Meaningful Projection Rule
Every supported projection must preserve as much exact VDR information as the target scalar system can faithfully receive.

If loss occurs during projection, that loss belongs to the target scalar system or target format, not to missing information in the source VDR object.

---

### 94. Exact Projection Preference Rule
If a VDR object can be projected into a target scalar system exactly, then exact projection is preferred over approximate projection.

Approximation is permitted only when the target system cannot receive the object exactly in finite form.

---

### 95. Rational Closed Projection Rule
For a closed VDR object:

$$
[V,D,0]
$$

the rational projection is:

$$
\pi_{\mathbb{Q}}([V,D,0]) = \frac{V}{D}
$$

provided the target system admits rational representation.

This is the canonical exact scalar projection for closed nodes at v1.

---

### 96. Normalized Closed Projection Rule
If a closed VDR object is not in normalized closed form, it may first be normalized before projection.

So scalar comparison may use either:
- raw closed form as written, or
- normalized closed form,
provided the target projection rule is clear and deterministic.

The normalized route is preferred for stable comparison.

---

### 97. Active Projection Deferral Rule
For an active VDR object:

$$
[V,D,R]
\quad\text{with } R \neq 0
$$

full scalar projection is not completely defined in v1.

At this stage, active projection is acknowledged as required by the charter, but its general exact formula is deferred pending fuller semantic and arithmetic development.

So v1 supports full exact scalar projection only for the closed subclass.

---

### 98. Partial Projection Rule
Where full projection of an active object is not yet defined, a partial external report may still be given in structured form, for example:
- normalized top-level closed part,
- residual presence,
- child structure,
- and any exact closed projections of closed descendants.

This is not yet a full scalar collapse, but it supports early interoperability and inspection.

---

### 99. Approximate Export Rule
If an external scalar target requires approximation in order to represent a supported projected value, that approximation must be marked as external and target-imposed.

Thus decimal or floating export may be approximate even when the VDR source object is exact.

Approximate export is never native VDR identity.

---

### 100. Projection Determinism Rule
For any fixed:
- valid VDR object,
- projection target,
- and projection procedure,

the scalar projection result must be deterministic.

Repeated projection under the same rules must produce the same result.

---

### 101. Equality Preservation Preference Rule
If two VDR objects are value-equal in a domain for which exact scalar projection is defined, then their exact scalar projections should agree in that target system.

At v1 this is fully guaranteed only for the closed subclass, where normalization and rational projection are already defined.

---

### 102. Projection Scope Rule
The v1 scalar projection layer defines:
- externality of projection,
- target dependence,
- exact rational projection for closed objects,
- approximate export as target-imposed loss,
- and deferral of full active-object projection.

It does not yet fully define:
- scalar projection for general active nested objects,
- exact scalar equality across all VDR objects,
- inverse construction from all scalar systems into VDR,
- or practical precision-control algorithms.

Those belong to later layers.

---

### 103. Interoperability Minimum Rule
Even before full active projection is defined, VDR satisfies a minimal interoperability condition at v1 if:
- closed VDR objects can be projected exactly to rational/scalar form,
- invalid objects are rejected,
- and active objects can at least be reported in exact structured external form.

This is a minimal starting point, not the final interoperability goal.

---

### 104. Charter Consistency Rule
The incompleteness of active scalar projection in v1 does not violate the charter, provided it is treated explicitly as unfinished scope rather than silently assumed solved.

The charter requires scalar projection as a program requirement.
It does not require that every projection formula be complete in v1.

---

## Summary of Scalar Projection v1

At this stage, VDR now has:

- exact scalar projection for closed objects
- deterministic external projection behavior
- explicit acknowledgement that active projection is still unfinished
- strict separation between native VDR identity and scalar export
- target-imposed loss, not VDR-imposed loss, when approximation is necessary

This is enough for:
- early closed-case validation
- exact rational comparisons
- implementation scaffolding
- and honest statement of what remains unsolved

---

# VDR
## Minimal Arithmetic Rules v1
### Closed Objects Only

These rules define the first arithmetic layer of VDR for the closed subclass only.

They apply only to VDR objects of the form:

$$
[V,D,0]
$$

with:
- \(V \in \mathbb{Z}\),
- \(D \in \mathbb{Z}\setminus\{0\}\).

They do not yet define general arithmetic for active objects with nonzero residuals.

---

### 105. Closed Arithmetic Domain Rule
A closed VDR object is any valid VDR object of the form:

$$
[V,D,0]
$$

The minimal arithmetic rules v1 apply only to this closed subclass.

If an operand is active, these rules do not apply unless a later rule explicitly reduces that case to a closed one.

---

### 106. Closed Arithmetic Exactness Rule
Closed arithmetic in v1 is exact.

It may not use:
- approximation,
- decimal fitting,
- floating-point conversion,
- epsilon comparison,
- or limit-based reasoning.

Every valid closed arithmetic operation must produce a raw-valid closed VDR object, subject to later normalization.

---

### 107. Closed Addition Rule
For two closed VDR objects:

$$
[V_1,D_1,0] + [V_2,D_2,0]
$$

their sum is defined as:

$$
[V_1D_2 + V_2D_1,\; D_1D_2,\; 0]
$$

subject to normalization.

---

### 108. Closed Subtraction Rule
For two closed VDR objects:

$$
[V_1,D_1,0] - [V_2,D_2,0]
$$

their difference is defined as:

$$
[V_1D_2 - V_2D_1,\; D_1D_2,\; 0]
$$

subject to normalization.

---

### 109. Closed Multiplication Rule
For two closed VDR objects:

$$
[V_1,D_1,0] \times [V_2,D_2,0]
$$

their product is defined as:

$$
[V_1V_2,\; D_1D_2,\; 0]
$$

subject to normalization.

---

### 110. Closed Division Rule
For two closed VDR objects:

$$
[V_1,D_1,0] \div [V_2,D_2,0]
$$

division is valid if and only if:

$$
V_2 \neq 0
$$

and the quotient is defined as:

$$
[V_1D_2,\; D_1V_2,\; 0]
$$

subject to normalization.

---

### 111. Division by Closed Zero Exclusion Rule
Division by a closed zero object is invalid.

So if the divisor is of the form:

$$
[0,D,0]
$$

for any nonzero \(D\), then division is undefined.

---

### 112. Closed Additive Identity Rule
The closed additive identity is:

$$
[0,1,0]
$$

For every closed VDR object \(X\),

$$
X + [0,1,0] \equiv_v X
$$

after normalization.

---

### 113. Closed Multiplicative Identity Rule
The closed multiplicative identity is:

$$
[1,1,0]
$$

For every closed VDR object \(X\),

$$
X \times [1,1,0] \equiv_v X
$$

after normalization.

---

### 114. Closed Additive Inverse Rule
For every closed VDR object:

$$
[V,D,0]
$$

its additive inverse is:

$$
[-V,D,0]
$$

subject to normalization sign conventions.

Then:

$$
[V,D,0] + [-V,D,0] \equiv_v [0,1,0]
$$

after normalization.

---

### 115. Closed Negation Rule
Closed negation is exact and acts on the value slot:

$$
-[V,D,0] = [-V,D,0]
$$

Normalization may later relocate sign according to canonical sign rules.

---

### 116. Closed Arithmetic Closure Rule
If two inputs are valid closed VDR objects, then any valid operation among:
- addition,
- subtraction,
- multiplication,
- and division when divisor is nonzero,

must return a raw-valid closed VDR object.

So the closed subclass is arithmetically closed under these operations, except for division by closed zero.

---

### 117. Closed Arithmetic Normalization Rule
The direct output of a closed arithmetic rule need not already be in normal form.

After any closed arithmetic operation, normalization may be applied to:
- reduce gcd,
- standardize sign placement,
- and restore canonical closed form.

---

### 118. Closed Arithmetic Compatibility Rule
The closed arithmetic rules are compatible with the closed scalar projection rule:

$$
\pi_{\mathbb{Q}}([V,D,0]) = \frac{V}{D}
$$

in the sense that the arithmetic forms are constructed to match ordinary rational arithmetic under exact projection.

This is an interoperability compatibility statement, not a reduction of VDR identity to rational identity.

---

### 119. Closed Arithmetic Commutativity Rule
For valid closed operands \(X, Y\),

$$
X + Y \equiv_v Y + X
$$

and

$$
X \times Y \equiv_v Y \times X
$$

after normalization.

---

### 120. Closed Arithmetic Associativity Rule
For valid closed operands \(X, Y, Z\),

$$
(X + Y) + Z \equiv_v X + (Y + Z)
$$

and

$$
(X \times Y) \times Z \equiv_v X \times (Y \times Z)
$$

after normalization.

---

### 121. Closed Distributivity Rule
For valid closed operands \(X, Y, Z\),

$$
X \times (Y + Z) \equiv_v (X \times Y) + (X \times Z)
$$

after normalization.

---

### 122. Closed Arithmetic Scope Rule
The minimal arithmetic layer v1 defines exact arithmetic only for closed VDR objects.

It does not yet define:
- arithmetic on active objects,
- residual arithmetic,
- same-denominator child absorption during active operations,
- rebasing,
- lifting,
- or active scalar-preserving arithmetic.

Those belong to later layers.

---

## Summary of Minimal Arithmetic v1

At this stage, VDR supports exact arithmetic for the closed subclass:
- addition,
- subtraction,
- multiplication,
- division by nonzero closed objects,
- identities,
- inverses,
- and rational compatibility under closed projection.

This gives you a fully workable rational core inside VDR.

That is enough for:
- a first implementation of closed VDR arithmetic
- exact validation against rational arithmetic
- and a solid base before touching active residual arithmetic

---

# VDR
## Rebase Rules v1
### Closed Objects Only

These rules define the first rebasing layer of VDR for the closed subclass only.

They apply only to VDR objects of the form:

$$
[V,D,0]
$$

Rebasing changes the explicit top-level denominator while preserving closed exact value.

They do not yet define general rebasing for active objects with nonzero residuals.

---

### 123. Closed Rebase Domain Rule
For a valid closed VDR object:

$$
X = [V,D,0]
$$

and a target denominator:

$$
B \in \mathbb{Z}\setminus\{0\}
$$

the closed rebase operation, when valid, produces another closed VDR object:

$$
\mathrm{rebase}(X,B) = [V',B,0]
$$

with the same closed projected value.

---

### 124. Closed Rebase Purpose Rule
Closed rebasing changes the explicit denominator of a closed VDR object without changing its exact closed value.

Thus rebasing is a representational operation, not a value-changing operation.

---

### 125. Closed Rebase Validity Rule
A closed rebase from:

$$
[V,D,0]
$$

to target denominator \(B\) is valid if and only if there exists an integer \(V'\) such that:

$$
\frac{V'}{B} = \frac{V}{D}
$$

Equivalently, closed rebasing is valid if and only if:

$$
V' = \frac{VB}{D} \in \mathbb{Z}
$$

---

### 126. Closed Rebase Construction Rule
If closed rebasing is valid, then:

$$
\mathrm{rebase}([V,D,0],B)
=
\left[\frac{VB}{D},\; B,\; 0\right]
$$

provided the numerator computed is an integer.

---

### 127. Closed Rebase Failure Rule
If:

$$
\frac{VB}{D} \notin \mathbb{Z}
$$

then closed rebasing to denominator \(B\) fails in v1.

At this stage, failure does not trigger active rebasing automatically.
That belongs to a later layer.

So closed v1 rebasing is:
- exact where possible,
- explicit failure where not possible.

---

### 128. Same-Denominator Identity Rule
For every valid closed VDR object:

$$
\mathrm{rebase}([V,D,0],D) = [V,D,0]
$$

So rebasing to the same denominator is identity.

---

### 129. Sign-Compatible Rebase Rule
Closed rebasing may target either positive or negative nonzero denominators.

If the target denominator \(B\) is negative, rebasing is still allowed provided the resulting numerator is an integer.

Sign normalization, if desired, may later rewrite the result into canonical sign form.

---

### 130. Closed Rebase Equality Preservation Rule
If closed rebasing succeeds, then rebasing preserves value equality:

$$
\mathrm{rebase}([V,D,0],B) \equiv_v [V,D,0]
$$

This follows through normalization and closed projection compatibility.

---

### 131. Closed Rebase Structural Nonidentity Rule
Closed rebasing generally does not preserve structural equality.

So even when rebasing succeeds:

$$
\mathrm{rebase}([V,D,0],B) \not\equiv_s [V,D,0]
$$

in general, unless \(B = D\) and the representation is unchanged.

Thus rebasing is a change of representation, not of value.

---

### 132. Closed Rebase Projection Compatibility Rule
If closed rebasing succeeds, then rational projection is preserved:

$$
\pi_{\mathbb{Q}}(\mathrm{rebase}([V,D,0],B))
=
\pi_{\mathbb{Q}}([V,D,0])
$$

So rebasing is compatible with closed scalar projection.

---

### 133. Closed Rebase Determinism Rule
For a fixed closed VDR object and fixed target denominator, the closed rebase result is unique when it exists.

So closed rebasing is deterministic.

---

### 134. Closed Rebase Termination Rule
Closed rebasing must terminate in finite time.

It requires only:
- integer multiplication,
- integer divisibility check,
- and integer construction of the rebased numerator.

No approximation or nonterminating process is involved.

---

### 135. Closed Rebase Canonicality Rule
Closed rebasing itself is not normalization.

A rebased closed object may still require normalization for:
- sign placement,
- gcd reduction,
- or canonical closed form.

Thus rebasing and normalization are distinct layers.

---

### 136. Closed Rebase Arithmetic Compatibility Rule
If closed rebasing succeeds on operands or results, it must preserve compatibility with closed arithmetic and value equality.

So rebasing is a representational tool that may be used before or after closed arithmetic, provided all rebases involved are valid.

---

### 137. Closed Rebase Scope Rule
The v1 closed rebase layer defines only:
- exact denominator change for closed objects,
- explicit success/failure,
- and value-preserving representational rebasing.

It does not yet define:
- active rebasing,
- residual transport,
- same-denominator child absorption mechanics,
- quotient selection,
- or scalar-aware active completion.

Those belong to later layers.

---

## Summary of Closed Rebase v1

At this stage, VDR supports exact rebasing for closed objects when the target denominator is compatible with the represented closed value.

So for:

$$
[V,D,0]
$$

and target \(B \neq 0\),

- if \(VB/D\) is an integer, rebasing succeeds exactly
- otherwise rebasing fails explicitly

This gives you:
- exact denominator change,
- no approximation,
- deterministic behavior,
- and a clean base before active rebasing is introduced

---

# VDR
## Active Rebase Rules v1

These rules extend rebasing beyond the closed subclass.

They define the first exact rebasing layer for active VDR objects, where rebasing to a new denominator may require preservation of unresolved exact structure in the residual slot.

The purpose of active rebasing is:
- to preserve exact native VDR structure,
- to preserve value equality inside VDR,
- and to avoid approximation when closed rebasing alone is insufficient.

These rules are first-pass and conservative.

---

### 138. Active Rebase Domain Rule
For a valid VDR object:

$$
X = [V,D,R]
$$

with:

$$
D \neq 0
$$

and target denominator:

$$
B \in \mathbb{Z}\setminus\{0\}
$$

the active rebase operation, when valid, produces a valid VDR object:

$$
\mathrm{rebase}(X,B) = [V',B,R']
$$

such that rebasing preserves native value equality.

---

### 139. Closed Rebase Priority Rule
If a VDR object is closed and closed rebasing succeeds, then closed rebasing must be used directly.

So active rebasing is not used when a valid closed rebased form already exists.

Closure is preferred where exact closure is available.

---

### 140. Active Rebase Trigger Rule
Active rebasing is used when:
- a target denominator \(B\) is requested,
- exact closed rebasing is not available in the intended representation layer,
- and exact residual-preserving rebasing is still possible.

Thus active rebasing is the exact non-approximate extension of rebasing beyond closed direct denominator transfer.

---

### 141. Rebased Form Rule
For:

$$
X = [V,D,R]
$$

and target denominator \(B\neq 0\),

an active rebase result has the form:

$$
[Q,B,R']
$$

where:
- \(Q \in \mathbb{Z}\),
- \(R'\) is exact residual structure,
- and the rebased object remains a valid VDR object.

At v1, \(Q\) is the rebased top-level value slot and \(R'\) is the exact residual structure required to preserve rebase equality.

---

### 142. Quotient-Residual Decomposition Rule
To actively rebase:

$$
[V,D,R]
$$

to denominator \(B\), form the integer-scaled numerator demand:

$$
N = VB
$$

Then choose integers \(Q\) and \(S\) such that:

$$
N = QD + S
$$

This decomposes the target top-level denominator change into:
- a quotient part \(Q\),
- and a residual mismatch part \(S\).

At v1, this decomposition is exact and finite.

---

### 143. Residual Child Construction Rule
The residual mismatch part \(S\) is preserved exactly by constructing the closed child:

$$
[S,D,0]
$$

This child is inserted into the rebased residual structure rather than discarded or approximated away.

So the simplest active rebased form begins with:

$$
[Q,B,[S,D,0]]
$$

before any further residual combination or normalization.

---

### 144. Existing Residual Preservation Rule
If the original object already has residual structure \(R\), then active rebasing must preserve that residual structure exactly rather than erase it.

So rebasing must account for both:
- the newly introduced denominator mismatch residual,
- and the original residual structure already present in the source object.

---

### 145. Rebased Residual Combination Rule
For a source object:

$$
[V,D,R]
$$

rebased to denominator \(B\), the first-pass active rebased residual is formed by combining:
1. the newly constructed residual child from quotient mismatch,
2. and the preserved original residual structure, carried into the rebased object.

At v1 this combined rebased residual may be written schematically as:

$$
R' = [S,D,0] + R
$$

subject to later refinement by normalization and residual transport rules.

This is a structural preservation rule, not yet a final arithmetic combination law.

---

### 146. Exact Preservation Rule
If active rebasing succeeds, it must preserve native value equality:

$$
\mathrm{rebase}([V,D,R],B) \equiv_v [V,D,R]
$$

This is the defining requirement of active rebasing.

---

### 147. No Approximation Rebase Rule
Active rebasing may not use:
- decimal fitting,
- floating conversion,
- truncation,
- epsilon acceptance,
- or limit-style reasoning.

If exact finite rebasing is not possible, rebasing must fail rather than approximate.

---

### 148. Rebase Failure Rule
Active rebasing fails if:
- the target denominator is zero,
- exact finite residual preservation cannot be constructed,
- rebasing would require invalid structure,
- or the rebased object cannot be normalized and validated within the current layer.

Failure is explicit and valid.

---

### 149. Rebase Structural Nonidentity Rule
Active rebasing generally changes representation and so does not preserve structural equality.

Thus:

$$
\mathrm{rebase}(X,B) \not\equiv_s X
$$

in general, even when:

$$
\mathrm{rebase}(X,B) \equiv_v X
$$

---

### 150. Rebase Determinism Rule
For a fixed source object, fixed target denominator, and fixed quotient-selection rule, active rebasing must be deterministic.

At v1, quotient selection is exact but not yet fully canonically optimized.
A later quotient-selection layer may refine which valid \(Q\) is preferred when multiple exact decompositions are available.

---

### 151. Rebase Termination Rule
Active rebasing must terminate in finite time whenever it succeeds.

It may not rely on:
- infinite search,
- hidden completion,
- or asymptotic convergence.

At v1, only finitely expressible rebased structures are admitted.

---

### 152. Normalization Compatibility Rule
If active rebasing succeeds, the rebased result must remain a raw-valid VDR object and must be compatible with later normalization rules.

Thus active rebasing is a representational transformation inside VDR, not an escape from VDR structure.

---

### 153. Reserved Residual Transport Rule
The rule:

$$
R' = [S,D,0] + R
$$

is only a first-pass structural preservation rule.

A later layer may replace this with a more precise residual transport mechanism when:
- denominator-sensitive completion semantics,
- lift operators,
- or exact child absorption laws
are formally introduced.

So v1 active rebasing preserves structure conservatively without claiming that residual transport is fully solved.

---

### 154. Active Rebase Scope Rule
The v1 active rebase layer defines:
- exact quotient-residual decomposition,
- exact preservation of mismatch through residual child construction,
- preservation of existing residual structure,
- value-preserving rebased representation in principle,
- and explicit failure instead of approximation.

It does not yet fully define:
- canonical quotient selection,
- denominator-sensitive residual transport,
- full active arithmetic,
- full scalar projection for active objects,
- or final normalized active rebasing behavior.

Those belong to later layers.

---

## Summary of Active Rebase v1

At this stage, active rebasing says:

- rebasing to a new denominator may produce an active VDR object
- denominator mismatch is preserved exactly as residual child structure
- prior residual structure is not discarded
- exactness is preserved
- failure is explicit if finite exact rebasing cannot be constructed

This gives you the first exact extension beyond closed rebasing.

Important note:
this is still intentionally provisional.
It preserves the rebasing idea without pretending the deeper residual transport problem is solved.

---

# VDR
## Residual Transport / Lift Rules v1

These rules define the first transport layer for residual structure during
operations such as active rebasing and later active arithmetic.

The purpose of `lift` is to preserve exact residual structure when a VDR
object is moved into a new denominator context, without approximation and
without collapsing the residual into scalar form.

This is a first-pass structural transport layer. It is conservative and
keeps exact native structure primary.

---

### 155. Lift Domain Rule
`lift` is defined on:
- valid residual objects,
- valid child VDR objects appearing in residual structure,
- and nonzero integer scale factors.

Formally, v1 admits:

$$
\mathrm{lift} : \mathcal{R} \times (\mathbb{Z}\setminus\{0\}) \to \mathcal{R}
$$

and the corresponding child action:

$$
\mathrm{lift} : \mathcal{V} \times (\mathbb{Z}\setminus\{0\}) \to \mathcal{V}
$$

where:
- \( \mathcal{R} \) is the residual domain,
- \( \mathcal{V} \) is the domain of valid VDR objects.

Lift by zero is invalid.

---

### 156. Lift Purpose Rule
`lift` transports exact residual structure into a new denominator frame.

It is used when:
- a parent denominator context changes,
- but existing residual structure must remain exact and native,
- and scalar collapse is forbidden.

Thus `lift` is a structural transport operation, not a scalar evaluation.

---

### 157. Atomic Lift Rule
For an atomic residual integer:

$$
r \in \mathbb{Z}
$$

define:

$$
\mathrm{lift}(r,k) = kr
$$

for every nonzero integer \(k\).

So atomic residual transport is exact integer scaling.

---

### 158. Composite Residual Lift Rule
For a composite residual of the form:

$$
R = r + X_1 + X_2 + \dots + X_n
$$

define:

$$
\mathrm{lift}(R,k)
=
kr + \mathrm{lift}(X_1,k) + \mathrm{lift}(X_2,k) + \dots + \mathrm{lift}(X_n,k)
$$

where:
- \(r \in \mathbb{Z}\),
- each \(X_i\) is a valid child VDR object,
- \(n\) is finite.

This is a structural distribution rule over residual form.

---

### 159. Child Lift Rule
For a child VDR object:

$$
X = [V,D,R]
$$

define:

$$
\mathrm{lift}(X,k) = [kV,\; D,\; \mathrm{lift}(R,k)]
$$

where \(k \neq 0\).

So lift:
- scales the value slot,
- preserves the child denominator slot,
- and recursively lifts the child residual.

At v1, this preserves child denominator identity while transporting the
child into a new outer denominator context.

---

### 160. Lift Identity Rule
Lift by \(1\) is identity.

For every valid residual object \(R\),

$$
\mathrm{lift}(R,1) = R
$$

and for every valid child VDR object \(X\),

$$
\mathrm{lift}(X,1) = X
$$

---

### 161. Lift Sign Rule
Lift by \(-1\) negates transported structure.

For atomic residuals:

$$
\mathrm{lift}(r,-1) = -r
$$

For child VDR objects:

$$
\mathrm{lift}([V,D,R],-1) = [-V,D,\mathrm{lift}(R,-1)]
$$

So lift is sign-compatible with exact negation.

---

### 162. Lift Composition Rule
Lift composes multiplicatively.

For every valid residual object \(R\) and nonzero integers \(a,b\),

$$
\mathrm{lift}(\mathrm{lift}(R,a),b)
=
\mathrm{lift}(R,ab)
$$

Likewise for valid child VDR objects \(X\),

$$
\mathrm{lift}(\mathrm{lift}(X,a),b)
=
\mathrm{lift}(X,ab)
$$

This ensures multi-stage transport is coherent.

---

### 163. Lift Exactness Rule
Lift may not introduce:
- approximation,
- floating conversion,
- decimal fitting,
- hidden continuation,
- or invalid recursive structure.

It is an exact native transport operation only.

---

### 164. Lift Validity Preservation Rule
If \(R\) is a valid residual object and \(k \neq 0\), then
\(\mathrm{lift}(R,k)\) is a valid residual object.

If \(X\) is a valid child VDR object and \(k \neq 0\), then
\(\mathrm{lift}(X,k)\) is a valid VDR object.

So lift preserves raw validity.

---

### 165. Lift Finiteness Rule
Because every valid residual and child VDR object is finite, every valid
lift operation terminates in finite time.

Lift may not rely on infinite descent or hidden infinite expansion.

---

### 166. Lift Structural Preservation Rule
Lift preserves recursive locality.

It may not:
- move structure out of the residual slot,
- introduce recursion into \(V\) or \(D\),
- or destroy the finite tree structure of the object.

Thus lift transports structure without changing the foundational shape of
VDR.

---

### 167. Lift Zero Rule
For the atomic residual zero:

$$
\mathrm{lift}(0,k) = 0
$$

for every nonzero integer \(k\).

So closed residual zero remains zero under transport.

---

### 168. Lift Addition-Shaped Distribution Rule
Where residual structure is written in composite form, lift distributes over
the admitted residual decomposition:

$$
\mathrm{lift}(R_1 + R_2, k)
=
\mathrm{lift}(R_1,k) + \mathrm{lift}(R_2,k)
$$

provided both sides are read as valid residual structural expressions in the
v1 sense.

This is a structural distribution law, not yet a full arithmetic statement.

---

### 169. Lift Rebase Support Rule
Lift exists in v1 primarily to support active rebasing and later active
arithmetic.

When denominator context changes but residual structure must be preserved,
`lift` is the canonical first-pass transport operator.

---

### 170. Reserved Semantic Refinement Rule
The v1 lift rules define exact structural transport, but they do not yet
fully settle the deeper semantic question of how transported residuals
contribute to external scalar meaning in all active cases.

Thus v1 lift is admitted as:
- exact,
- finite,
- deterministic,
- structurally valid,
- and operationally useful,

while leaving full denominator-sensitive active semantics to later layers.

---

### 171. Lift Scope Rule
The v1 lift layer defines:
- exact transport of residual integers,
- recursive transport of child VDR objects,
- validity preservation,
- structural preservation,
- and support for active rebase.

It does not yet fully define:
- full active scalar projection,
- full active arithmetic semantics,
- quotient optimization,
- or complete denominator-sensitive completion laws.

Those belong to later layers.

---

## Summary of Lift v1

At this stage, `lift` gives VDR:

- a finite exact transport operator,
- defined on residuals and child VDR objects,
- compatible with sign and composition,
- preserving validity and structure,
- ready to support active rebasing and later arithmetic.

This is the minimal exact transport layer needed before more serious active
operations are built.

---

# VDR
## Denominator-Sensitive Completion Semantics v1

These rules refine native semantics for active VDR objects.

Their purpose is to make explicit that residual structure is interpreted in
the denominator frame of its parent, rather than as an externally added
scalar term detached from that frame.

This layer is introduced to support:
- active rebasing,
- residual transport,
- and later active arithmetic,
while preserving the charter principle that residual structure is exact
completion rather than approximation residue.

---

### 172. Parent-Frame Completion Rule
For a VDR object:

$$
[V,D,R]
$$

the residual \(R\) is interpreted natively as completion structure in the
denominator frame of the parent denominator \(D\).

Thus \(R\) is not interpreted as a free-standing scalar addend independent
of \(D\).

---

### 173. Closed Completion Rule
For a closed VDR object:

$$
[V,D,0]
$$

the native completed content is fully settled at the top level.

The closed external rational projection remains:

$$
\pi_{\mathbb{Q}}([V,D,0]) = \frac{V}{D}
$$

So closed nodes are unchanged by this semantic refinement.

---

### 174. Residual Numerator-Space Rule
At v1, residual completion is interpreted in numerator-space relative to the
parent denominator.

This means the residual contributes as exact numerator-side completion of the
parent frame, not as an externally detached scalar term.

So the parent denominator governs how the residual is understood.

---

### 175. Parent-Sensitive Completion Function Rule
Introduce a parent-sensitive completion function:

$$
\rho_D(R)
$$

which interprets residual \(R\) relative to parent denominator \(D\).

The native external comparison form of a VDR object is then guided by:

$$
\Pi([V,D,R]) = \frac{V + \rho_D(R)}{D}
$$

where \( \Pi \) is an external scalar-comparison interpretation schema.

At v1, this is a semantic guiding rule, not yet a full executable projection
algorithm for all active cases.

---

### 176. Atomic Residual Completion Rule
For an atomic residual integer \(r\),

$$
\rho_D(r) = r
$$

So an atomic residual contributes as numerator-side completion in the parent
frame.

This yields the guiding schema:

$$
\Pi([V,D,r]) = \frac{V+r}{D}
$$

for atomic-residual active objects, where external comparison is defined.

---

### 177. Child Residual Completion Rule
For a child VDR object \(X\) appearing in the residual of a parent with
denominator \(D\), the child contributes through its own projected value as
numerator-side completion of the parent frame.

So the parent-sensitive residual interpretation takes the form:

$$
\rho_D(r + X_1 + \dots + X_n)
=
r + \Pi(X_1) + \dots + \Pi(X_n)
$$

as a first-pass semantic schema.

Accordingly:

$$
\Pi([V,D,r + X_1 + \dots + X_n])
=
\frac{V + r + \Pi(X_1) + \dots + \Pi(X_n)}{D}
$$

This expresses denominator-sensitive completion:
child contributions are divided by the parent denominator through the parent
frame, not added externally after the parent ratio is already complete.

---

### 178. Completion Not External Addition Rule
Even though the comparison schema may be written in additive form, native VDR
semantics do not treat residual structure as an externally attached scalar
sum.

The additive-looking schema is only an external comparison image of the
native completion relation.

So native completion remains ontologically primary.

---

### 179. Rebase Compatibility Rule
Under denominator-sensitive completion semantics, a rebased object of the
form:

$$
[Q,B,[S,D,0]]
$$

has the comparison schema:

$$
\Pi([Q,B,[S,D,0]])
=
\frac{Q + \Pi([S,D,0])}{B}
=
\frac{Q + S/D}{B}
$$

which equals:

$$
\frac{QD + S}{BD}
$$

This is exactly the required form for preserving the source value when:

$$
VB = QD + S
$$

Thus denominator-sensitive completion makes active rebasing semantically
coherent.

---

### 180. Lift Compatibility Rule
Under denominator-sensitive completion semantics, lifted residual structure
remains parent-frame sensitive.

So `lift` is interpreted as transporting numerator-side completion structure
into the new parent denominator frame without collapsing child denominator
identity.

This is why child lift preserves the child denominator while scaling the
child value slot and residual recursively.

---

### 181. Same-Denominator Child Absorption Rule
If a child VDR object in a residual has the same denominator as the parent,
then under denominator-sensitive completion semantics its contribution already
lives in the same parent denominator frame.

Therefore such a child is a candidate for canonical absorption into the
parent level during normalization, rather than retention as a separate child.

This justifies the reserved same-denominator absorption rule introduced
earlier.

---

### 182. Recursive Completion Rule
If a child VDR object \(X\) appears in a residual, then \(X\) is itself
interpreted by the same denominator-sensitive completion semantics.

So completion is recursively compositional.

At v1 this recursion is finite because all valid VDR objects are finite.

---

### 183. Exactness of Completion Rule
Denominator-sensitive completion semantics may not introduce:
- approximation,
- infinite expansion,
- limit behavior,
- or hidden deferred evaluation.

Any active interpretation admitted by this layer must remain finite and exact
in structure.

---

### 184. Structural Priority Rule
The parent-sensitive completion schema does not override native structural
priority.

Two VDR objects may project to the same external comparison form while still
remaining structurally distinct and natively non-identical unless a later
value-equality or equivalence rule identifies them.

So scalar comparison image is still secondary.

---

### 185. Active Projection Preparation Rule
This semantic layer prepares the way for full active scalar projection, but
does not yet complete it as an implementation layer.

At v1 it gives the semantic law that active external comparison must follow,
without yet requiring every active projection procedure to be fully built.

---

### 186. Completion Scope Rule
The denominator-sensitive completion layer defines:
- parent-frame interpretation of residuals,
- numerator-space completion,
- recursive child contribution under the parent denominator,
- semantic justification for active rebasing,
- and semantic justification for lift.

It does not yet fully define:
- all active arithmetic laws,
- full executable active scalar projection algorithms,
- canonical quotient choice beyond current rebase rules,
- or all equivalence classes induced by completion.

Those belong to later layers.

---

## Summary of Denominator-Sensitive Completion Semantics v1

At this stage, VDR now has the key semantic refinement it needed:

- residuals complete the parent in the parent denominator frame
- child VDRs contribute through the parent denominator, not as detached
  external sums
- active rebasing of the form

$$
[Q,B,[S,D,0]]
$$

now projects coherently as:

$$
\frac{Q + S/D}{B}
$$

which fixes the earlier rebase-scaling problem

This is a major semantic stabilization point.

---

# VDR
## Active Scalar Projection Rules v1

These rules extend scalar projection beyond the closed subclass.

They use the denominator-sensitive completion semantics introduced earlier to
define the first active external comparison layer for VDR objects with
nonzero residual structure.

This layer remains external and secondary:
it does not redefine native VDR identity.

Its purpose is to make active VDR objects comparable to conventional scalar
systems in a principled exact way where possible, and in a controlled
approximate way where necessary.

---

### 187. Active Projection Domain Rule
An active VDR object is any valid VDR object of the form:

$$
[V,D,R]
\quad\text{with } R \neq 0
$$

The active scalar projection rules v1 apply to valid active VDR objects.

Closed objects remain projected by the closed projection rules.

---

### 188. Active Projection Principle Rule
Active scalar projection follows denominator-sensitive completion semantics.

For a valid active VDR object:

$$
[V,D,R]
$$

its scalar comparison image is determined by:

$$
\Pi([V,D,R]) = \frac{V + \rho_D(R)}{D}
$$

where:
- \(D \neq 0\),
- \(\rho_D(R)\) is the parent-sensitive residual completion function.

At v1 this is the governing exact semantic law for active scalar projection.

---

### 189. Atomic Active Projection Rule
If the residual is atomic:

$$
R = r
\quad\text{with } r \in \mathbb{Z}
$$

then:

$$
\rho_D(r) = r
$$

and therefore:

$$
\Pi([V,D,r]) = \frac{V+r}{D}
$$

So atomic active residuals project exactly as numerator-side completion.

---

### 190. Composite Active Projection Rule
If the residual has composite form:

$$
R = r + X_1 + X_2 + \dots + X_n
$$

where:
- \(r \in \mathbb{Z}\),
- each \(X_i\) is a valid child VDR object,
- \(n\) is finite,

then:

$$
\rho_D(R) = r + \Pi(X_1) + \Pi(X_2) + \dots + \Pi(X_n)
$$

and therefore:

$$
\Pi([V,D,R])
=
\frac{V + r + \Pi(X_1) + \Pi(X_2) + \dots + \Pi(X_n)}{D}
$$

This is the exact recursive active projection schema in v1.

---

### 191. Closed Child Projection Rule
If a child in the residual is closed:

$$
X = [A,B,0]
$$

then its contribution is:

$$
\Pi(X) = \frac{A}{B}
$$

and so in the parent frame it contributes as:

$$
\frac{A/B}{D}
$$

through the parent denominator-sensitive completion rule.

---

### 192. Recursive Projection Termination Rule
Because every valid VDR object is finite, active scalar projection terminates
after finitely many recursive applications of:
- closed projection,
- atomic residual completion,
- and composite residual expansion.

So exact active projection is finite on all finite valid VDR objects in v1.

---

### 193. Projection Exactness Rule
Exact active scalar projection may not use:
- approximation,
- floating conversion,
- decimal fitting,
- epsilon acceptance,
- or infinite completion.

If exact recursive projection is defined for a valid finite active object, it
must terminate with an exact scalar comparison expression.

---

### 194. Projection Target Interpretation Rule
The result of active projection may be rendered into different target systems:

- exact rational expression where possible
- exact symbolic scalar expression where needed
- decimal or floating approximation where the target format requires loss

Thus active projection has two layers:
1. exact scalar comparison form,
2. target-specific rendering.

---

### 195. Exact Rational Collapse Rule
If the exact recursive active projection of a valid finite VDR object reduces
to a rational number, then the preferred external scalar result is that exact
rational value.

So when active structure projects exactly to a rational, rational comparison
is preferred over decimal approximation.

---

### 196. Exact Symbolic Projection Rule
If the exact recursive active projection yields a finite exact scalar
expression that is not yet reduced to a single rational fraction at the
current layer, that expression may still serve as a valid exact external
comparison form.

Thus exact projection need not always collapse immediately to one reduced
fraction before later simplification.

---

### 197. Approximate Rendering Rule
If an external target system such as decimal or floating-point format cannot
receive the exact projected scalar comparison form losslessly, then an
approximate rendering may be produced.

Such approximation is:
- external,
- target-imposed,
- and not a loss of native VDR exactness.

---

### 198. Deterministic Projection Rule
For a fixed valid VDR object and fixed target projection procedure, active
scalar projection must be deterministic.

Repeated projection under the same rules must produce the same exact scalar
comparison form and the same target rendering.

---

### 199. Value Equality Projection Compatibility Rule
If two VDR objects are value-equal in a domain where active scalar projection
is defined exactly, then their exact scalar comparison forms should agree.

At v1 this is a semantic compatibility expectation and should hold for all
cases covered by the recursive projection rules.

---

### 200. Structural Distinctness Preservation Rule
Even if two VDR objects project to the same exact scalar comparison form, they
need not be structurally equal and need not be natively identical.

Scalar projection agreement does not collapse native VDR distinction.

---

### 201. Benchmark Export Rule
When VDR is used for comparison against conventional scalar pipelines,
benchmarking should occur at the scalar rendering layer after exact VDR
computation is complete.

Thus:
- internal work stays exact in VDR,
- projection occurs at the boundary,
- and approximation enters only if required by the external target system.

This rule supports the charter’s practical validation strategy.

---

### 202. Active Projection Scope Rule
The v1 active projection layer defines:
- exact recursive scalar comparison for finite active VDR objects,
- denominator-sensitive parent-frame projection,
- exact projection preference where possible,
- approximate external rendering where necessary,
- and preservation of native structural distinction.

It does not yet fully define:
- optimized simplification of exact scalar comparison forms,
- active arithmetic laws inside VDR,
- or a complete inbound construction algorithm from all scalar systems.

Those belong to later layers.

---

## Summary of Active Scalar Projection v1

At this stage, VDR now supports scalar projection for active objects by the
exact recursive schema:

$$
\Pi([V,D,R]) = \frac{V + \rho_D(R)}{D}
$$

with:

$$
\rho_D(r + X_1 + \dots + X_n)
=
r + \Pi(X_1) + \dots + \Pi(X_n)
$$

This gives you:

- full finite recursive external comparison semantics
- exact projection where possible
- approximate rendering only at the target boundary
- compatibility with active rebasing and denominator-sensitive completion
- preservation of native structural distinction

This is a major interoperability milestone.

---

# VDR
## Active Arithmetic Rules v1

These rules extend arithmetic beyond the closed subclass.

They define the first exact arithmetic layer for VDR objects with nonzero
residual structure, using:
- denominator-sensitive completion semantics,
- active scalar projection,
- and residual transport.

This layer is intentionally conservative.
Its purpose is to preserve exact VDR structure without approximation.

Where a fully internal structural construction is not yet settled, the rule
states what must be preserved and what is deferred.

---

### 203. Active Arithmetic Domain Rule
The active arithmetic rules apply to valid VDR objects of the form:

$$
[V,D,R]
$$

where the residual \(R\) may be zero or nonzero.

Thus the active arithmetic layer extends arithmetic to the general finite VDR
domain, including mixed closed/active inputs.

---

### 204. Exactness Preservation Rule
Every valid active arithmetic operation must preserve:
- finite exact structure,
- triple irreducibility,
- residual significance,
- and value equality as defined or extended by the active arithmetic layer.

No active arithmetic rule may use:
- approximation,
- decimal fitting,
- floating conversion,
- epsilon acceptance,
- or limit completion.

---

### 205. Closed Compatibility Rule
When both operands are closed, active arithmetic agrees with the minimal
closed arithmetic rules v1.

So the active arithmetic layer extends the closed layer; it does not replace
or contradict it.

---

### 206. Same-Denominator Addition Rule
For two valid VDR objects with the same denominator:

$$
[V_1,D,R_1]
+
[V_2,D,R_2]
$$

their sum is defined by:

$$
[V_1 + V_2,\; D,\; R_1 \oplus R_2]
$$

where \( \oplus \) is exact residual combination at the same parent
denominator frame.

At v1, \( \oplus \) is defined structurally by:
- combining atomic residual bases,
- concatenating child structures,
- then applying normalization where available.

So same-denominator addition preserves the shared denominator frame.

---

### 207. Same-Denominator Residual Combination Rule
For residuals:

$$
R_1 = r_1 + X_1 + \dots + X_n
$$

and

$$
R_2 = r_2 + Y_1 + \dots + Y_m
$$

their same-frame combination is:

$$
R_1 \oplus R_2
=
(r_1 + r_2) + X_1 + \dots + X_n + Y_1 + \dots + Y_m
$$

subject to later normalization:
- atomic consolidation,
- child ordering,
- same-denominator absorption,
- and other canonical rules.

For atomic residuals, this reduces to ordinary integer addition.

---

### 208. Same-Denominator Subtraction Rule
For two valid VDR objects with the same denominator:

$$
[V_1,D,R_1]
-
[V_2,D,R_2]
$$

their difference is defined by:

$$
[V_1 - V_2,\; D,\; R_1 \ominus R_2]
$$

where \( \ominus \) is exact residual subtraction in the shared denominator
frame.

At v1, \( R_1 \ominus R_2 \) is defined structurally by:
- subtracting atomic residual bases,
- appending negated child structures from the second residual,
- then normalizing where defined.

---

### 209. Residual Negation Rule
Residual negation is defined recursively.

For atomic residuals:

$$
-(r) = -r
$$

For composite residuals:

$$
-(r + X_1 + \dots + X_n)
=
-r + (-X_1) + \dots + (-X_n)
$$

For child VDR objects:

$$
-[V,D,R] = [-V,D,-R]
$$

subject to later sign normalization.

---

### 210. Additive Inverse Rule
For every valid VDR object:

$$
X = [V,D,R]
$$

its additive inverse is:

$$
-X = [-V,D,-R]
$$

Then, where addition is defined,

$$
X + (-X)
$$

must normalize to the additive identity in the corresponding exact sense.

At v1 this is exact structurally and may require normalization to expose the
identity form.

---

### 211. Different-Denominator Addition Rule
For two valid VDR objects:

$$
[V_1,D_1,R_1]
+
[V_2,D_2,R_2]
$$

with \(D_1 \neq D_2\), addition is performed by moving both operands into a
shared denominator frame using exact rebasing where possible.

The preferred shared frame at v1 is:

$$
D_1D_2
$$

unless a later normalization or rebase rule selects a simpler valid shared
denominator.

So addition proceeds by:
1. rebasing the first operand to denominator \(D_1D_2\),
2. rebasing the second operand to denominator \(D_1D_2\),
3. applying same-denominator addition,
4. normalizing the result.

---

### 212. Different-Denominator Subtraction Rule
For two valid VDR objects:

$$
[V_1,D_1,R_1]
-
[V_2,D_2,R_2]
$$

with \(D_1 \neq D_2\), subtraction is performed by:
1. rebasing both operands to a shared denominator frame,
2. applying same-denominator subtraction,
3. normalizing the result.

At v1 the default shared frame is:

$$
D_1D_2
$$

unless a simpler valid exact shared frame is already available.

---

### 213. Multiplication Rule
For two valid VDR objects:

$$
X = [V_1,D_1,R_1]
\quad\text{and}\quad
Y = [V_2,D_2,R_2]
$$

their product must preserve exact denominator-sensitive completion semantics.

At v1, multiplication is governed by the semantic requirement:

$$
\Pi(X \times Y) = \Pi(X)\Pi(Y)
$$

and the result must be represented by a valid finite VDR object if such a
representation can be constructed exactly.

Where both inputs are closed, this reduces to the closed multiplication rule.

Where either input is active, exact internal product construction is admitted
as a required operation but is not yet fully canonically specified in a
single structural formula at v1.

Thus active multiplication is semantically constrained but operationally
provisional.

---

### 214. Division Rule
For two valid VDR objects:

$$
X \div Y
$$

division is valid only if the projected value of \(Y\) is not exact zero in
the domain where division is being considered.

At v1, division is governed by the semantic requirement:

$$
\Pi(X \div Y) = \frac{\Pi(X)}{\Pi(Y)}
$$

and the result must be represented by a valid finite VDR object if such a
representation can be constructed exactly.

Where both inputs are closed, this reduces to the closed division rule.

Where the divisor is active, exact internal quotient construction is admitted
in principle but not yet fully canonically specified at v1.

---

### 215. Explicit Failure Rule
If an active arithmetic operation would require:
- approximation,
- invalid structure,
- nonterminating construction,
- or a representational step not yet defined in the current layer,

then the operation must fail explicitly rather than silently approximate.

Failure is valid behavior in v1.

---

### 216. Addition Projection Compatibility Rule
Where active addition is defined exactly,

$$
\Pi(X + Y) = \Pi(X) + \Pi(Y)
$$

must hold under the active scalar projection rules.

This is the external comparison compatibility requirement for exact active
addition.

---

### 217. Subtraction Projection Compatibility Rule
Where active subtraction is defined exactly,

$$
\Pi(X - Y) = \Pi(X) - \Pi(Y)
$$

must hold under active scalar projection.

---

### 218. Multiplication Projection Compatibility Rule
Where active multiplication is defined exactly,

$$
\Pi(X \times Y) = \Pi(X)\Pi(Y)
$$

must hold under active scalar projection.

---

### 219. Division Projection Compatibility Rule
Where active division is defined exactly,

$$
\Pi(X \div Y) = \frac{\Pi(X)}{\Pi(Y)}
$$

must hold under active scalar projection.

---

### 220. Commutativity Rule
Where the relevant operations are defined exactly and succeed:

$$
X + Y \equiv_v Y + X
$$

and

$$
X \times Y \equiv_v Y \times X
$$

after normalization.

---

### 221. Associativity Rule
Where the relevant operations are defined exactly and succeed:

$$
(X + Y) + Z \equiv_v X + (Y + Z)
$$

and

$$
(X \times Y) \times Z \equiv_v X \times (Y \times Z)
$$

after normalization.

---

### 222. Distributivity Rule
Where the relevant operations are defined exactly and succeed:

$$
X \times (Y + Z) \equiv_v (X \times Y) + (X \times Z)
$$

after normalization.

---

### 223. Identity Rule
The additive identity remains:

$$
[0,1,0]
$$

The multiplicative identity remains:

$$
[1,1,0]
$$

Where active arithmetic is defined and succeeds, these identities behave as
exact identities under value equality.

---

### 224. Arithmetic Scope Rule
The v1 active arithmetic layer defines:
- exact same-denominator addition and subtraction,
- recursive residual negation,
- different-denominator addition/subtraction by exact rebasing,
- semantic constraints for multiplication and division,
- explicit failure instead of approximation,
- and compatibility with active scalar projection.

It does not yet fully define:
- a canonical constructive formula for all active products,
- a canonical constructive formula for all active quotients,
- complete active simplification laws,
- or optimized denominator selection beyond current rebasing rules.

Those belong to later refinement layers.

---

## Summary of Active Arithmetic v1

At this stage, VDR now supports:

- exact addition and subtraction for general finite VDR objects
- exact different-denominator combination via rebasing
- recursive residual negation
- semantic constraints for multiplication and division
- explicit failure where full exact finite construction is not yet settled

This is enough to begin:
- implementation of active addition/subtraction,
- testing projection compatibility,
- and exploring active structure computationally

It is not yet the final arithmetic system.

---

# VDR
## Inbound Construction Rules v1

These rules define the first admission layer by which objects external to VDR
may enter the system as valid VDR objects.

They serve the charter requirement that VDR must be able to connect to
existing scalar practice while preserving native exactness once inside VDR.

Inbound construction is external-to-internal.
It is not the same as scalar projection, which is internal-to-external.

This v1 layer is intentionally conservative.

---

### 225. Inbound Construction Purpose Rule
Inbound construction is the process of taking an accepted external
specification and producing a valid VDR object.

Its purpose is to admit external mathematical or scientific values into VDR
without approximation where exact admission is possible.

---

### 226. Inbound/Projection Distinction Rule
Inbound construction and scalar projection are distinct operations.

- Inbound construction:
  external specification \(\to\) VDR object

- Scalar projection:
  VDR object \(\to\) external comparison form

They are not inverses in general, especially when the external target system
is lossy.

---

### 227. Accepted External Specification Rule
At v1, accepted external specifications are limited to external forms whose
exact meaning is already clear and finite.

This includes, at minimum:
- integers,
- rational fractions,
- and exact closed scalar forms reducible to rational input.

Other external forms may be admitted later by additional rules.

---

### 228. Integer Inbound Rule
For any integer:

$$
n \in \mathbb{Z}
$$

the canonical inbound construction is:

$$
\mathrm{in}(n) = [n,1,0]
$$

Thus every integer is admitted exactly as a closed VDR object.

---

### 229. Rational Inbound Rule
For any rational number given exactly as:

$$
\frac{a}{b}
\quad\text{with } a \in \mathbb{Z},\; b \in \mathbb{Z}\setminus\{0\}
$$

the canonical inbound construction is:

$$
\mathrm{in}\!\left(\frac{a}{b}\right) = [a,b,0]
$$

subject to later normalization.

Thus every exact rational input is admitted exactly as a closed VDR object.

---

### 230. Reduced Rational Inbound Preference Rule
If an exact rational input is already known in reduced form, reduced form is
preferred for stable construction.

If not, raw fraction input may still be admitted and later normalized.

So inbound construction does not require canonicality at admission time.

---

### 231. Sign-Compatible Inbound Rule
Negative numerators and negative denominators are both admitted at inbound
construction time so long as the denominator is nonzero.

Sign normalization, if desired, is deferred to normalization rules.

---

### 232. Closed Exactness Rule
Every integer or rational admitted under the v1 inbound rules enters VDR as a
closed exact object.

So the v1 inbound layer guarantees exact admission for the closed rational
subclass.

---

### 233. Exact Specification Admission Rule
An object may also enter VDR by direct exact specification in native VDR form,
provided it is raw-valid under the foundational and structural rules.

Thus inbound admission at v1 includes both:
- accepted external scalar construction,
- and direct exact VDR specification.

These are distinct admission paths.

---

### 234. Direct Active Specification Rule
A valid active VDR object may be admitted directly by exact specification:

$$
[V,D,R]
$$

provided:
- \(V \in \mathbb{Z}\),
- \(D \neq 0\),
- \(R\) is a valid residual object,
- and the whole structure is finite and raw-valid.

At v1 this direct route allows active objects to exist in VDR even before
general external active-construction algorithms are complete.

---

### 235. Active External Construction Deferral Rule
General inbound construction of active VDR objects from external scalar
descriptions is not fully defined in v1.

At this stage, active objects may be:
- directly specified in native VDR form,
- or later derived internally,
but there is not yet a complete external-to-active admission algorithm for
all supported target classes.

---

### 236. Exact Construction Rule
No v1 inbound construction may use:
- decimal fitting,
- floating approximation,
- epsilon acceptance,
- or limit-based admission
as a justification for exact VDR entry.

If an external input is admitted exactly, the admission must be exact.

---

### 237. Approximate Inbound Rejection Rule
An approximate external scalar input does not become exact merely by being
placed into VDR syntax.

If the source is only approximate and no exact constructive VDR admission is
available, then exact inbound construction fails.

Approximate data may be handled in later application layers, but not as exact
native admission in v1.

---

### 238. Exhaustive Construction Reservation Rule
For some future target classes, exact inbound construction may require
exhaustive search, exhaustive derivation, or other finite constructive
discovery procedures.

This is allowed in principle, provided:
- the procedure is exact,
- finite when successful,
- and does not rely on approximation as proof of admission.

Such procedures are reserved for later layers.

---

### 239. External Scope Limitation Rule
VDR v1 does not claim exact inbound construction for:
- arbitrary writable decimal strings,
- malformed notation artifacts,
- or external expressions lacking exact constructive meaning.

Thus v1 inbound scope is narrower than “all external scalar notation.”

---

### 240. Inbound Determinism Rule
For any accepted external specification and fixed inbound construction rule,
the resulting admitted VDR object must be deterministic.

Different admitted raw forms may still later normalize to a common canonical
form, but a given inbound rule must not be ambiguous.

---

### 241. Inbound Normalization Compatibility Rule
Inbound construction need not produce normal form directly.

However, every exactly admitted inbound object must remain compatible with
later normalization and value equality rules.

So exact admission and canonical form are distinct layers.

---

### 242. Projection Compatibility Rule
For every external object admitted exactly into the closed rational subclass,
inbound construction and scalar projection are compatible in the following
sense:

If \(x\) is an accepted integer or rational input, then:

$$
\Pi(\mathrm{in}(x)) = x
$$

under the exact closed projection rules.

At v1, this compatibility is guaranteed for the closed rational subclass.

---

### 243. Inbound Scope Rule
The v1 inbound construction layer defines:
- exact admission for integers,
- exact admission for rational fractions,
- direct native specification of valid VDR objects,
- rejection of approximate admission as exact admission,
- and explicit deferral of general external active construction.

It does not yet fully define:
- exact admission of irrational constants,
- exact admission of transcendental values,
- exhaustive admission procedures for broader target classes,
- or exact admission of all values required by established scientific
  computation.

Those belong to later layers.

---

## Summary of Inbound Construction v1

At this stage, VDR supports:

- exact admission of integers
- exact admission of rationals
- direct exact specification of native VDR objects
- explicit refusal to treat approximate inputs as exact just by syntax
- a clean separation between inbound construction and scalar projection

This is enough to begin:
- implementation of exact closed admission,
- parser support for native VDR objects,
- and later experimentation with broader construction classes

It is not yet the final inbound story.

---

# VDR
## Supported Domain Examples v1

These examples do not extend the formal axioms.
They clarify the present working boundary of VDR by giving concrete cases in
three classes:

1. clearly in scope,
2. clearly out of scope,
3. open or unresolved.

This document exists because, at v1, examples are more informative than an
overconfident universal scope claim.

The purpose of these examples is to make the current intent of VDR easier to
inspect, implement, criticize, and refine.

---

## A. Clearly In Scope at v1

These are objects or classes currently admitted by the foundational and
inbound rules.

### 1. Integers
Examples:
- \(0\)
- \(1\)
- \(-7\)
- \(10^{12}\)

Inbound construction:
- all integers enter exactly as closed VDR objects of the form

$$
[n,1,0]
$$

Status:
- fully in scope

---

### 2. Exact Rational Fractions
Examples:
- \(1/2\)
- \(-3/5\)
- \(14/7\)
- \(22/7\)

Inbound construction:
- exact rational input enters as

$$
[a,b,0]
\quad\text{with } b \neq 0
$$

Status:
- fully in scope

---

### 3. Non-Normal Closed Forms
Examples:
- \([2,4,0]\)
- \([1,-2,0]\)
- \([-6,-9,0]\)

These are exact raw-valid VDR objects even if not normalized.

Status:
- fully in scope as raw-valid objects
- normalization may later reduce them canonically

---

### 4. Directly Specified Active Objects
Examples:
- \([3,5,1]\)
- \([2,7,-1]\)
- \([4,9,[1,3,0]]\)
- \([1,2,1 + [1,3,0]]\)

These are admitted provided they satisfy raw-validity rules:
- triple form,
- nonzero denominator,
- valid residual structure,
- finite nesting.

Status:
- in scope as native VDR objects by exact specification

---

### 5. Finite Nested Residual Structures
Examples:
- \([1,2,[1,3,0]]\)
- \([2,5,1 + [1,4,0] + [3,7,0]]\)
- \([4,11,-2 + [1,3,[1,2,0]]]\)

These are finite native VDR structures with recursive residuals.

Status:
- in scope if raw-valid and finite

---

### 6. Closed Arithmetic Cases
Examples:
- \([1,2,0] + [1,3,0]\)
- \([3,4,0] - [1,2,0]\)
- \([2,3,0] \times [3,5,0]\)
- \([2,3,0] \div [4,5,0]\)

Status:
- fully in scope under minimal arithmetic v1

---

### 7. Closed Rebasing Cases
Examples:
- rebase \([1,2,0]\) to denominator \(4\), yielding \([2,4,0]\)
- rebase \([3,5,0]\) to denominator \(10\), yielding \([6,10,0]\)

Status:
- fully in scope when integer transfer succeeds

---

### 8. Active Rebase / Projection Exploration Cases
Examples:
- \([1,2,0]\) rebased actively toward denominator \(3\)
- \([1,2,[1,3,0]]\) projected by denominator-sensitive completion

These are in scope for exploratory formal work under v1’s provisional active
layers.

Status:
- in scope as development cases
- not yet fully mature in all operational details

---

## B. Clearly Out of Scope at v1

These are not currently admitted as exact inbound constructions, or they
violate the structural foundations of VDR.

### 9. Zero-Denominator Objects
Examples:
- \([1,0,0]\)
- \([3,0,[1,2,0]]\)

Status:
- invalid by foundational rule

---

### 10. Infinite Residual Trees
Examples:
- a residual with infinitely many child VDRs
- infinite nesting with no finite terminal depth
- any VDR object requiring ellipsis to complete

Status:
- out of scope
- invalid in terminating VDR

---

### 11. Approximate Admission Disguised as Exact Admission
Examples:
- importing a floating approximation of \( \pi \) and treating it as exact
- importing a measured decimal and declaring it exact merely by wrapping it
  into VDR syntax
- treating truncated decimal output as native VDR identity

Status:
- out of scope as exact admission

---

### 12. Arbitrary Notation Artifacts Without Constructive Meaning
Examples:
- `0.3333...751`
- malformed decimal strings claiming both infinite continuation and a final
  terminal digit
- externally written scalar forms with no exact constructive meaning

Status:
- out of scope

---

### 13. Infinite Decimal Tail Objects Taken Literally
Examples:
- “all decimal digits of a number” when no finite exact constructive rule is
  given
- values admitted only by saying “continue forever”

Status:
- out of scope as exact finite VDR admission

---

### 14. Implicit Approximation Acceptance
Examples:
- “close enough to be treated as equal”
- “admit this because the float is precise enough”
- “normalize by truncating a long residual”

Status:
- out of scope by charter and foundational rules

---

## C. Open / Unresolved Cases at v1

These are important targets or possibilities, but are not yet settled by the
current specification.

### 15. Algebraic Irrationals
Examples:
- \( \sqrt{2} \)
- \( \sqrt{3} \)
- roots of exact polynomial equations

Status:
- unresolved

Reason:
- VDR does not yet provide a general exact inbound construction rule for these

---

### 16. Named Transcendental Constants
Examples:
- \( \pi \)
- \( e \)

Status:
- unresolved

Reason:
- these are major target values for the long-term ambition of VDR,
  but v1 does not yet provide exact admission rules for them

---

### 17. Constants Required by Established Scientific Computation
Examples:
- fine-structure constant
- Planck-related constants
- measured or model-dependent scientific constants

Status:
- unresolved

Reason:
- some are measured approximations rather than exact mathematical givens
- others may require derivation, exact construction, or domain-specific
  interpretation beyond current v1 rules

---

### 18. Exact Inbound Construction by Exhaustive Discovery
Examples:
- a finite but nontrivial discovery process that constructs a VDR object from
  a scientifically meaningful external specification

Status:
- allowed in principle
- unresolved in concrete algorithmic form

---

### 19. Full Active Multiplication and Division
Examples:
- exact product of two active nested VDR objects
- exact quotient of active structures with nontrivial residuals

Status:
- semantically constrained, but operationally unresolved in full canonical
  form

---

### 20. Full Canonical Quotient Selection in Active Rebasing
Examples:
- choosing among multiple exact quotient/residual decompositions
- minimizing complexity of rebased active form

Status:
- unresolved refinement layer

---

### 21. Domain Ceiling
Examples:
- all algebraic numbers
- all computable reals
- all values required by established scientific computation
- all mathematically meaningful scalar values

Status:
- explicitly open research boundary

Reason:
- the charter sets ambition, but v1 does not claim completion at this scale

---

## D. Working Scope Summary

At v1, VDR clearly supports:
- integers
- exact rationals
- raw-valid finite native triple structures
- direct specification of active objects
- exact closed arithmetic
- partial active semantics and projection

At v1, VDR clearly rejects:
- zero denominators
- infinite structures
- approximate admission as exactness
- malformed notation artifacts
- hidden infinite tails

At v1, VDR leaves open:
- exact admission of algebraic irrationals
- exact admission of transcendental constants
- exact construction of scientific constants
- the full practical ceiling of the system

---

## E. Why These Examples Matter

These examples clarify that VDR is not:
- “all scalar notation rewritten”
- nor “just fractions”

It is a growing exact finite domain with:
- a clear rational core,
- an admitted native active structure,
- a strict anti-approximation boundary,
- and an open research frontier.

This example-based boundary is appropriate at v1 because the exact full scope
of VDR is still under investigation.

---

## Summary

Supported Domain Examples v1 gives three things:

1. a clear set of cases everyone can agree are already inside VDR
2. a clear set of cases everyone can agree are outside VDR
3. an explicit open frontier for further work

This is useful for:
- implementation planning
- paper clarity
- criticism by outsiders
- and preventing accidental overclaiming

---

# VDR
## Reference Data Model v1

This document gives a practical implementation-oriented data model for VDR
based on the current v1 rules.

It is not a replacement for the axioms.
Its purpose is to provide a canonical implementation shape for:
- parsers,
- serializers,
- validators,
- test harnesses,
- and early libraries.

The reference data model must reflect the current formal layers:
- foundational object rules,
- residual formation rules,
- structural validity,
- normalization,
- equality,
- scalar projection,
- arithmetic,
- rebasing,
- and active semantics.

At v1, the data model is finite, exact, tree-structured, and integer-based.

---

## 1. Core Types

### 1.1. VDR Object Type
A VDR object is a record with exactly three fields:

- `v`: integer
- `d`: nonzero integer
- `r`: residual

Abstractly:

```text
VDR = {
  v: Int,
  d: IntNonZero,
  r: Residual
}
```

This corresponds to the formal triple:

$$
[V,D,R]
$$

---

### 1.2. Residual Type
A residual is one of two admissible shapes:

1. atomic integer residual
2. composite residual with one integer base and a finite list of child VDRs

Abstractly:

```text
Residual =
  | AtomicResidual(Int)
  | CompositeResidual {
      base: Int,
      children: List<VDR>
    }
```

This reflects the formal residual rules:
- atomic form: \(r\)
- composite form: \(r + X_1 + \dots + X_n\)

Implementation note:
- an atomic residual `r` may be treated as syntactic sugar for
  `CompositeResidual { base: r, children: [] }`
- however, v1 keeps both forms explicit because the formal layer distinguishes
  them structurally

---

### 1.3. Normalized Residual Convention
For normalization and serialization purposes, a canonical internal
implementation may choose to store all residuals in expanded composite form:

```text
CompositeResidual {
  base: Int,
  children: List<VDR>
}
```

with atomic residuals represented as:

```text
CompositeResidual {
  base: r,
  children: []
}
```

This is an implementation convenience, not a formal replacement of the
admissible syntax layer.

---

## 2. Primitive Value Domains

### 2.1. Integer Domain
The `v` field and residual integer bases belong to the implementation’s exact
integer type.

At v1 this must be:
- mathematically exact,
- not floating,
- not approximate.

Preferred implementation type:
- arbitrary-precision signed integer.

---

### 2.2. Nonzero Integer Domain
The `d` field must belong to the exact integer domain with the additional
constraint:

```text
d != 0
```

This should be enforced by:
- constructor validation,
- smart type,
- or explicit validation logic.

---

## 3. Tree Structure

### 3.1. Finite Rooted Tree Model
A VDR object is a finite rooted tree.

- each VDR node is a tree node
- each node stores one integer value slot `v`
- one nonzero integer denominator slot `d`
- and one residual object `r`
- residual children form the outgoing tree edges

---

### 3.2. Recursion Locality
Only the residual contains recursive child VDR objects.

So:
- `v` is always atomic integer
- `d` is always atomic nonzero integer
- recursion occurs only through `r.children`

This should be reflected directly in the data model.

---

### 3.3. Finiteness Constraint
All VDR values in the reference model must be finite.

So:
- finite node count
- finite child list at every residual
- finite recursion depth

An implementation must reject cyclic or infinite structure.

Recommended practical rule:
- no pointer-sharing semantics unless treated as copied tree structure for
  logical validity
- no graph cycles

---

## 4. Canonical Structural Encoding

### 4.1. Raw Encoding
A raw-valid VDR object may preserve:
- unreduced denominators,
- noncanonical sign placement,
- arbitrary admissible child order,
- and explicit same-denominator child structure.

Raw form is allowed for authoring, parsing, and intermediate computation.

---

### 4.2. Canonical Encoding
A normalized VDR object should obey:
- chosen sign convention
- reduced closed nodes
- single residual integer base per level
- canonical child order
- absorbed same-denominator child structure where defined
- no redundant zero-like child forms where canonical zero is available

The data model should support both:
- raw representation
- and normalized representation

without changing the underlying core type.

---

## 5. Required Operations on the Data Model

The reference model must support at least the following operation classes.

### 5.1. Validation
Functions to check:
- exact triple shape
- integer fields
- nonzero denominator
- residual validity
- recursive child validity
- finiteness
- absence of invalid recursion shape

Example API shape:

```text
validate(vdr) -> Valid | Invalid(reason)
```

---

### 5.2. Structural Equality
Exact recursive equality:
- same `v`
- same `d`
- same residual structure
- same child order
- same descendant structure

Example API shape:

```text
structuralEqual(x, y) -> Bool
```

---

### 5.3. Normalization
Normalization must produce canonical form where defined.

Example API shape:

```text
normalize(vdr) -> VDR | Failure(reason)
```

---

### 5.4. Value Equality
Value equality at v1 is normalization-based structural equality.

Example API shape:

```text
valueEqual(x, y) -> Bool | Failure(reason)
```

where implementation may do:
1. normalize both
2. compare structurally

---

### 5.5. Closed Projection
Exact rational projection for closed nodes:

```text
projectClosed(x) -> Rational | Failure(reason)
```

---

### 5.6. Active Projection
Recursive parent-sensitive projection for active objects:

```text
projectScalarExact(x) -> ExactScalarForm | Failure(reason)
projectDecimal(x, precision) -> DecimalApprox | Failure(reason)
projectFloat(x, format) -> FloatApprox | Failure(reason)
```

At v1 the exact target form may be:
- rational when collapsible
- or symbolic scalar expression when not yet reduced

---

### 5.7. Arithmetic
The model must support:
- closed arithmetic
- active addition / subtraction
- active negation
- rebasing
- lift / residual transport

Example API shape:

```text
add(x, y) -> VDR | Failure(reason)
sub(x, y) -> VDR | Failure(reason)
mul(x, y) -> VDR | Failure(reason)   // provisional for active v1
div(x, y) -> VDR | Failure(reason)   // provisional for active v1
neg(x) -> VDR
rebase(x, targetD) -> VDR | Failure(reason)
liftResidual(r, k) -> Residual | Failure(reason)
```

---

## 6. Reference Serialized Forms

### 6.1. Native Text Form
A direct text serialization should preserve the triple structure explicitly.

Recommended canonical text style:

```text
[v, d, r]
```

Examples:

```text
[1, 2, 0]
[3, 5, 1]
[1, 2, 1 + [1, 3, 0]]
[2, 7, -1 + [1, 3, 0] + [2, 5, 0]]
```

This is human-readable but not necessarily the only serialization.

---

### 6.2. Structured Data Form
For implementation and interchange, a JSON-like form may be used.

Example closed node:

```json
{
  "v": 1,
  "d": 2,
  "r": { "kind": "atomic", "value": 0 }
}
```

Example composite residual:

```json
{
  "v": 1,
  "d": 2,
  "r": {
    "kind": "composite",
    "base": 1,
    "children": [
      {
        "v": 1,
        "d": 3,
        "r": { "kind": "atomic", "value": 0 }
      }
    ]
  }
}
```

---

### 6.3. Canonical Serialized Form
For reproducible storage and hashing, canonical serialization should use:
- normalized VDR object
- deterministic child ordering
- deterministic sign placement
- explicit composite residual encoding if chosen system-wide

This should be implementation-defined but fixed once chosen.

---

## 7. Suggested Auxiliary Types

### 7.1. Exact Scalar Form
Because active scalar projection may yield exact forms not immediately reduced
to one rational at the current layer, implementations may use an exact scalar
comparison type such as:

```text
ExactScalarForm =
  | Rational(a, b)
  | Sum(List<ExactScalarForm>)
  | Quotient(ExactScalarForm, ExactScalarForm)
  | Integer(n)
```

or any equivalent exact symbolic form.

This is not a VDR object.
It is an external comparison form.

---

### 7.2. Failure Type
Because explicit failure is part of the charter, implementations should use a
structured failure type rather than silent null/none behavior.

Example:

```text
Failure =
  | InvalidStructure
  | ZeroDenominator
  | NonFiniteStructure
  | RebaseImpossible
  | ApproximationRequired
  | UnsupportedInV1
  | NormalizationFailure
  | ProjectionFailure
  | ArithmeticFailure
```

---

## 8. Minimal Reference Invariants

Any conforming v1 implementation should preserve at least these invariants:

1. every VDR object has exactly three fields
2. denominator is never zero
3. recursion occurs only through residual children
4. every object is finite
5. every operation either:
   - returns exact finite VDR / exact external form,
   - or explicit failure
6. normalization does not leave the VDR domain
7. structural equality is exact recursive equality
8. scalar projection does not redefine native identity

---

## 9. Implementation Levels

### 9.1. Minimal v1 Implementation
A minimal conforming implementation may support:
- exact integer type
- VDR parsing / serialization
- validation
- structural equality
- normalization for closed objects
- closed arithmetic
- rational closed projection
- direct active object parsing
- active projection by recursive exact comparison form

---

### 9.2. Stronger v1 Implementation
A stronger v1 implementation may additionally support:
- active addition / subtraction
- rebasing
- lift
- normalization of active forms
- exact symbolic scalar output
- decimal export at requested precision
- benchmark tools against scalar pipelines

---

## 10. Summary

Reference Data Model v1 gives VDR a practical implementation shape:

- finite rooted tree
- exact integers only
- recursion only in residual children
- raw and normalized forms
- explicit validation
- explicit failure
- separate native VDR objects from external scalar comparison objects

This is enough to begin:
- parser design
- serializer design
- Python/Zig reference libraries
- test generation
- equality testing
- and closed-core execution

---

We came to a Path A/B fork with the design, and chose Path B, that [2,5,1] does not equal [3,5,0] it is "11/5 = [2, 5, 1]" and Active VDR based a process state object.

---

Agreed.

The affected layers are mainly:

- Native Semantic Rules v1
- Denominator-Sensitive Completion Semantics v1
- Active Scalar Projection Rules v1
- Active Rebase Rules v1
- Active Arithmetic Rules v1
- Active Rebase Repair Notes v1
- some worked examples that assumed additive active projection

Best move is to rewrite them narrowly and cleanly around:

- closed objects may project numerically
- active objects are native operation-state objects
- active residual is not scalar-additive by default
- active scalar projection is deferred or only allowed under later domain-specific interpretation

I’ll start with the semantic layers in order.

# VDR
## Revised Native Semantic Rules v1
### Path B Commitment

These rules replace the earlier active-semantics direction with a
state-carrying interpretation.

They define the native semantic layer of VDR under the decision that active
VDR objects are not ordinary scalar values by default.

Closed VDR objects may still admit direct scalar interpretation.
Active VDR objects are instead exact operation-state objects.

---

### 41. Native Object Rule
A valid VDR object is natively an exact triple-structured object.

Its native meaning is not exhausted by any scalar reading, decimal rendering,
rational collapse, or external comparison image.

A VDR object is first an object of VDR, not first a number in another system.

---

### 42. Triple-State Semantic Rule
For:

$$
[V,D,R]
$$

the three slots are semantically distinct:

- \(V\) is the settled value slot
- \(D\) is the denominator frame slot
- \(R\) is the residual state slot

No slot is reducible to another, and no slot may be erased merely because a
conventional scalar notation would compress the form.

---

### 43. Residual State Rule
The residual slot \(R\) is exact native state.

A nonzero residual is not:
- error,
- noise,
- approximation residue,
- delayed numerator addition,
- or dispensable annotation.

It is preserved exact unresolved state carried by the object.

---

### 44. Closed and Active Semantic Rule
A VDR object is semantically classified in one of two native states:

1. Closed:
$$
[V,D,0]
$$

2. Active:
$$
[V,D,R]
\quad\text{with } R \neq 0
$$

A closed object has no residual state.
An active object carries exact residual state.

This distinction is native and foundational.

---

### 45. Global Closure Rule
A VDR object is globally closed if and only if:
- its top-level residual is zero,
- and every descendant residual in its full recursive structure is also zero.

Closure is global across the full recursive object.

---

### 46. Operation-State Rule
An active VDR object is an exact operation-state object.

It records:
- a settled value slot,
- a denominator frame,
- and residual state left exact rather than collapsed.

Thus active VDR objects are not ordinary scalar values by default.

---

### 47. Non-Additivity of Residual Rule
At the native semantic layer, a residual is not automatically interpreted as
additive scalar completion of the value slot.

So, in general:

$$
[V,D,R] \not\equiv [V+r,D,0]
$$

merely because \(R\) contains atomic residual \(r\).

In particular, active residual does not collapse by default into the value
slot.

---

### 48. Example Distinctness Rule
Objects such as:

$$
[2,5,1],\quad [2,5,0],\quad [2,5,-1]
$$

are three distinct native VDR objects.

They are not identified merely by any additive scalar reading.

This expresses the state-carrying role of residual.

---

### 49. Recursive State Rule
If a residual contains child VDR objects, each child is itself a full native
VDR object.

Thus recursive nesting is recursive state structure, not merely recursive
number expansion.

---

### 50. No Native Scalar Collapse Rule
Inside VDR, no active object may be semantically identified with:
- a rational,
- a real,
- a decimal,
- a float,
- or any scalar value
merely because some later interpretation layer may map it outward.

Closed objects may later admit scalar projection.
Active objects do not collapse to scalar identity by default.

---

### 51. Structural Meaning Priority Rule
At the native layer, structure comes before any external interpretation.

If two active VDR objects differ structurally, they remain natively distinct
unless a later exact equivalence rule explicitly identifies them.

---

### 52. Semantic Deferral Rule
At v1 under Path B, native semantics do not yet fully define:
- active scalar meaning,
- active scalar equality,
- active arithmetic collapse,
- or domain-specific interpretation of residual state.

They establish only that:
- active objects are exact operation-state objects,
- residual is exact preserved state,
- closure and activity are semantically meaningful,
- and scalar collapse is not native.

---

### 53. Semantic Layer Boundary Rule
The native semantic layer now commits VDR to:
- triple-state ontology
- residual state significance
- closure/activity distinction
- recursive state structure
- and anti-collapse semantics

It does not yet commit VDR to:
- additive residual semantics
- general scalar projection of active objects
- temporal or physical interpretation
- or scalar arithmetic on active states

Those belong to later layers if introduced.

---

# VDR
## Revised Denominator-Sensitive Completion Semantics v1
### Path B Commitment

These rules replace the earlier additive-completion reading.

Under Path B, denominator-sensitive semantics no longer treat active residual
as scalar-additive completion by default.

Instead, the denominator frame determines how residual state is held,
interpreted, and constrained inside the parent object.

This layer remains native to VDR.
It does not define general scalar projection for active objects.

---

### 172. Parent-Frame State Rule
For a VDR object:

$$
[V,D,R]
$$

the residual \(R\) is held in the denominator frame determined by the parent
denominator \(D\).

Thus residual state is denominator-sensitive:
it is not free-floating and not independent of the parent frame.

---

### 173. Closed Completion Rule
For a closed VDR object:

$$
[V,D,0]
$$

the object is fully settled in its denominator frame.

Closed objects retain the exact scalar projection rule:

$$
\Pi([V,D,0]) = \frac{V}{D}
$$

So the closed subclass is unchanged.

---

### 174. Active Frame-Sensitivity Rule
For an active VDR object:

$$
[V,D,R]
\quad\text{with } R \neq 0
$$

the residual is interpreted as exact state relative to the parent denominator
frame \(D\).

It is not interpreted by default as:
- numerator correction,
- denominator correction,
- additive scalar tail,
- or free-standing scalar remainder.

---

### 175. Denominator-Constrained State Rule
The denominator slot \(D\) constrains the meaning of residual state.

Thus two objects with the same value slot and residual structure but different
denominators are natively different operation-state objects:

$$
[V,D_1,R] \neq [V,D_2,R]
\quad\text{in native semantics if } D_1 \neq D_2
$$

unless a later exact rule explicitly identifies them in some domain.

---

### 176. Residual Non-Collapse Rule
At the native semantic layer, the residual does not collapse automatically
into the value slot even when written as an atomic integer.

So in general:

$$
[V,D,r] \not\equiv [V+r,D,0]
$$

for \(r \neq 0\).

The residual is state, not delayed simplification.

---

### 177. Child State Rule
If a child VDR object appears in the residual of a parent, that child is
itself a full state object nested inside the parent’s residual structure.

Thus a child in the residual is not automatically interpreted as:
- scalar addition,
- fractional correction,
- or direct numeric completion of the parent.

It is nested exact state.

---

### 178. Recursive Frame Rule
Because child VDR objects are themselves full VDR objects, denominator
sensitivity is recursive.

Each child carries:
- its own denominator frame,
- its own residual state,
- and its own closure/activity status,

while still appearing as state-bearing structure inside the parent residual.

---

### 179. No Additive Completion Rule
At v1 under Path B, there is no general native law of the form:

$$
[V,D,R] = \frac{V + f(R)}{D}
$$

for active objects.

Any such scalarization of active state is deferred to later interpretation
layers, if introduced at all.

This rule explicitly rejects the earlier additive-completion path as
foundational semantics.

---

### 180. Closed/Active Boundary Rule
The closed subclass admits direct scalar comparison through rational
projection.

The active subclass does not inherit that scalar comparability by default.

Thus VDR now has a semantic boundary:
- closed objects are scalar-projectable in the current layer
- active objects are exact state objects first

---

### 181. Rebase Sensitivity Rule
Because residual state is held in a denominator frame, changing the
denominator of an active object changes the frame in which residual state is
held.

Therefore active rebasing cannot be defined merely by preserving scalar value.
It must preserve exact state in a denominator-sensitive way.

This rule motivates a separate active rebase theory.

---

### 182. Lift Sensitivity Rule
Residual transport across denominator changes must be interpreted as
state-transport, not scalar-additive transport.

Thus any lift-like operation must preserve:
- exact residual state,
- recursive structure,
- and denominator-frame sensitivity,

rather than merely preserving a scalarized contribution.

---

### 183. Native Completion Deferral Rule
The word “completion” in active VDR no longer means scalar completion by
default.

At v1 under Path B, it means only that the residual belongs to the exact
native state of the object and is required to fully specify that state.

So active completion is ontological completion of the object, not scalar
completion of a number.

---

### 184. Structural Priority Rule
Two active objects may remain natively distinct even if some later external
interpretation layer maps them to the same scalar or observational output.

Native structural state remains primary over any later scalar image.

---

### 185. Domain Interpretation Deferral Rule
If active VDR objects later receive:
- temporal interpretation,
- update interpretation,
- physical interpretation,
- process interpretation,
- or scalar interpretation,

those must be added as later domain-specific interpretation layers.

They are not part of v1 foundational semantics.

---

### 186. Completion Scope Rule
The revised denominator-sensitive semantics now define only:

- residual state is held in a parent denominator frame
- active objects are denominator-sensitive operation-state objects
- residuals do not collapse additively by default
- child VDRs are nested state, not automatic numeric correction
- closed objects remain scalar-projectable
- active objects remain non-scalar by default

They do not yet define:
- general active scalar projection
- scalar-preserving active rebasing
- active arithmetic as scalar arithmetic
- or any domain-specific execution meaning of active state

Those belong to later layers if introduced.

---

## Summary of Revised Denominator-Sensitive Semantics v1

At this stage, VDR now says:

- the denominator frame matters natively
- active residual is frame-sensitive state
- active residual is not additive scalar completion
- nested children are nested state objects
- closed objects remain the scalar-projectable subclass
- active objects are exact operation-state objects by default

This preserves the ontological role of the residual and prevents active VDR
from collapsing back into decorated fraction arithmetic.

---

# VDR
## Revised Active Scalar Projection Rules v1
### Path B Commitment

These rules replace the earlier additive active projection layer.

Under Path B, active VDR objects are not ordinary scalar values by default.
Therefore active scalar projection is no longer a general built-in operation
of the foundational layer.

Instead, active scalar projection is restricted, deferred, or domain-specific.

Closed objects retain exact scalar projection.
Active objects remain exact operation-state objects unless an additional
interpretation layer explicitly defines how they are projected outward.

---

### 187. Active Projection Non-Default Rule
For an active VDR object:

$$
[V,D,R]
\quad\text{with } R \neq 0
$$

there is no general scalar projection by default at v1.

So unlike closed objects, active objects do not automatically admit an
external scalar value.

---

### 188. Closed Projection Boundary Rule
The exact scalar projection rule:

$$
\Pi([V,D,0]) = \frac{V}{D}
$$

applies only to the closed subclass.

It may not be extended to active objects merely by treating residual state as
scalar addition, correction, or completion.

---

### 189. Active Projection Deferral Rule
General projection of active objects into:
- rational form,
- real-number form,
- decimal form,
- float form,
- or any scalar comparison image

is deferred at v1 unless a later interpretation layer explicitly defines it.

Thus active scalar projection is not foundationally built in.

---

### 190. Structured External Report Rule
Although active scalar projection is not generally defined, a valid active VDR
object may still be reported externally in exact structured form.

Such a report may include:
- the value slot \(V\),
- the denominator frame \(D\),
- the residual structure \(R\),
- closure/activity status,
- and the recursively visible child structure.

This is an external structured report, not a scalar collapse.

---

### 191. Closed-Descendant Projection Rule
If an active VDR object contains closed descendant children, those descendants
may individually admit exact scalar projection under the closed rules.

However, the existence of scalar-projectable descendants does not imply that
the parent active object itself has a scalar projection.

---

### 192. Scalar Projection by Additional Interpretation Rule
An active object may admit scalar projection only if an additional exact
interpretation layer is supplied that explicitly defines:
- what the residual state means in scalar terms,
- how denominator-frame sensitivity is resolved,
- and how projection preserves the intended interpretation.

Such a layer is outside foundational v1.

---

### 193. No Additive Recovery Rule
At v1 under Path B, active scalar projection may not be recovered by any rule
of the form:

$$
[V,D,R] \mapsto \frac{V + f(R)}{D}
$$

unless such a rule is introduced explicitly in a later interpretation layer.

This forbids silent fallback to additive active semantics.

---

### 194. Approximate Export Prohibition Rule
Because general active scalar projection is not defined by default, an active
object may not be exported approximately to decimal or float merely by
inventing a scalar reading.

Approximate external scalar export of active objects is invalid unless an
exact interpretation layer first defines what scalar quantity is being
approximated.

So approximation may not substitute for missing meaning.

---

### 195. Native/External Separation Rule
The absence of default active scalar projection does not make active objects
meaningless.

It means only that their native exact identity is not exhausted by any scalar
comparison image in the foundational layer.

Thus active VDR remains exact and well-defined even when scalar comparison is
deferred.

---

### 196. Deterministic Structured Reporting Rule
For a fixed valid active VDR object and fixed reporting format, structured
external reporting must be deterministic.

The same active object must produce the same external structured report under
the same reporting rules.

---

### 197. Equality Independence Rule
Native structural equality and native value equality of active objects do not
depend on scalar projection.

They remain fully internal VDR relations.

Thus active objects may still be:
- validated,
- normalized,
- compared internally,
- and manipulated structurally
even when scalar projection is absent.

---

### 198. Benchmark Boundary Rule
At v1, benchmark comparison with scalar systems applies directly only to:
- the closed rational core,
- and any later active subclasses for which a scalar interpretation layer has
  been explicitly defined.

So active objects without such an interpretation are outside scalar benchmark
comparison at the current layer.

---

### 199. Interpretation-Layer Reservation Rule
Future layers may define one or more distinct scalar interpretations of active
objects, for example:
- observational interpretations,
- evaluation interpretations,
- execution-step interpretations,
- physical interpretations,
- or other domain-specific scalarizations.

These are reserved possibilities, not part of foundational v1.

---

### 200. Active Projection Scope Rule
The revised active projection layer now defines only:

- active objects do not have default scalar projection
- closed scalar projection remains intact
- active objects may be externally reported in exact structured form
- closed descendants may project individually
- scalar projection of active objects requires an added interpretation layer
- approximation may not replace missing semantics

It does not define:
- a general scalar value for active objects
- decimal export of active objects by default
- float export of active objects by default
- or active scalar equality

Those are deferred.

---

## Summary of Revised Active Scalar Projection v1

At this stage, VDR now has a clean boundary:

- closed objects admit exact scalar projection
- active objects do not admit general scalar projection by default
- active objects may still be externally reported exactly as structured
  operation-state objects
- scalar projection of active objects requires an added interpretation layer

This preserves the Path B commitment:
active VDR objects are exact native state, not ordinary scalar values.

---

