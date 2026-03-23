Here is the revised axiom draft with negative denominators allowed and normalization treated as optional/later rather than built into validity.

# Terminating VDR
## Revised First-Pass Axioms

## 0. Primitive Form

A VDR object is an ordered triple:

$$
[V, D, R]
$$

where:
- \(V\) is the value slot
- \(D\) is the denominator slot
- \(R\) is the remainder slot

A VDR object is a structured exact object, not a scalar by default.

---

## 1. Domain Axiom

For every valid VDR object:

- \(V \in \mathbb{Z}\)
- \(D \in \mathbb{Z} \setminus \{0\}\)
- \(R \in \mathcal{R}\)

where \(\mathcal{R}\) is the set of valid remainder objects.

The denominator may be positive or negative, but it may never be zero.

---

## 2. Triple Form Axiom

Every valid VDR object must have exactly three slots:

$$
[V, D, R]
$$

No valid VDR object may have:
- fewer than 3 slots,
- more than 3 slots,
- or recursive structure in \(V\) or \(D\).

Recursion is permitted only in the third slot.

---

## 3. Remainder Structure Axiom

The remainder slot \(R\) may take one of two forms:

1. Atomic remainder:
$$
R = r \quad\text{where } r \in \mathbb{Z}
$$

2. Nested remainder:
$$
R = r + X_1 + X_2 + \dots + X_n
$$

where:
- \(r \in \mathbb{Z}\)
- each \(X_i\) is a valid VDR object
- \(n \in \mathbb{N}\) is finite

Thus the remainder is:
- integer-valued at minimum,
- and may include a finite sum of nested VDRs.

---

## 4. Recursion Locality Axiom

Nested VDR objects may appear only in the remainder slot of a parent VDR.

That is:
- \(V\) may not contain VDRs,
- \(D\) may not contain VDRs,
- and nested VDRs inside a child VDR must again appear only in that child’s remainder slot.

This enforces a rooted recursive tree structure with branching only through \(R\).

---

## 5. Finite Closure Axiom

Every valid VDR object must terminate after finite recursive expansion.

Equivalently:
- the recursion tree of any VDR object is finite,
- every branch has finite depth,
- and every node has finite arity.

No infinite nested VDR structure is permitted.

---

## 6. Exactness Axiom

A VDR object is exact as written.

No valid VDR object may be interpreted as:
- an approximation,
- a limit process,
- an epsilon-neighborhood,
- or an implicitly infinite expansion.

All structure needed to complete the object must be present finitely within the object.

If the object cannot be finitely expressed, it is not a valid terminating VDR object.

---

## 7. Base Ratio Axiom

The primitive closed form of a VDR object is:

$$
[V, D, 0]
$$

Its scalar core is:

$$
\mathrm{core}([V,D,0]) = \frac{V}{D}
$$

This defines only the settled zero-remainder case, not the full meaning of nonzero remainders.

---

## 8. Active Remainder Axiom

If \(R \neq 0\), then the VDR object is not closed.

That is:
- \([V,D,0]\) is a closed object,
- \([V,D,R]\) with \(R \neq 0\) is an active object.

The remainder is not error.
It is exact structure required to complete the object.

A nonzero remainder indicates that the object carries unresolved exact state.

---

## 9. Closure Criterion Axiom

A VDR object is fully closed if and only if all remainders in its entire recursion tree are zero.

That is:
- its top-level remainder is zero,
- and every nested VDR appearing in its remainder is also closed.

Closure is global, not merely local.

---

## 10. Integer Remainder Conservation Axiom

The remainder slot must preserve integer exactness at every level.

No valid operation may transform a valid VDR into one whose remainder requires:
- floating-point representation,
- decimal approximation,
- irrational primitive insertion,
- or nonterminating expansion.

If such an operation would occur, then:
- either the operation is invalid in terminating VDR,
- or the object must be transformed into a deeper finite VDR structure that preserves exactness.

---

## 11. Sign Freedom Axiom

The signs of \(V\), \(D\), and atomic remainder \(r\) are all meaningful and permitted.

No validity rule may forbid negative numerators, negative denominators, or negative atomic remainders.

Any later simplification or normalization rule must not be confused with ontological validity.

---

## 12. Representation Validity vs Normalization Axiom

A VDR object may be valid without being normalized.

For example, both:
- \([1,-2,0]\)
- and \([-1,2,0]\)

may be valid representations if both satisfy all other axioms.

Normalization, if introduced, is a secondary operation for comparison, simplification, or canonical display, not a condition of validity.

---

## 13. Nest Denominator Uniqueness Axiom

Within a single parent remainder expansion:

$$
R = r + X_1 + X_2 + \dots + X_n
$$

the immediate child VDR objects \(X_i\) should have pairwise distinct top-level denominators unless an explicit non-normal form is intended.

That is, for immediate children:
$$
D_i \neq D_j \quad \text{for } i \neq j
$$

This is a structural preference for clean decomposition, not yet a strict validity condition unless later elevated.

---

## 14. Reduction Preference Axiom

If two immediate nested VDR children in the same remainder layer share the same denominator, the system may combine them through a reduction rule.

This establishes reduction as permitted, not mandatory for validity.

Thus:
- duplicate-denominator siblings are allowed in raw form,
- but reduction to merged form is preferred where useful.

---

## 15. Discrete Knowability Axiom

A valid terminating VDR object must be finitely inspectable.

This means:
- every node can be enumerated,
- every slot can be read exactly,
- and the total structure can be traversed in finite time.

This excludes:
- hidden infinite tails,
- deferred unresolved continuations,
- or symbolic placeholders that require nonterminating completion.

---

## 16. Solvability Axiom

Every primitive VDR operation must terminate on valid terminating VDR inputs.

This means:
- arithmetic,
- comparison,
- normalization,
- and closure checking
must all halt in finite time on finite VDR objects.

Any candidate operation that requires infinite descent, infinite expansion, or epsilon-style convergence is invalid as a terminating VDR operation.

---

## 17. Countability Axiom

The set of valid terminating VDR objects is countable.

Reason:
- every VDR object is finite,
- built from integers,
- and contains only finite recursive structure.

Thus terminating VDR belongs to the domain of discrete exact objects.

---

## 18. Non-Infinity Axiom

Infinity is not a valid VDR object, nor may infinity appear as hidden completion logic for a VDR object.

A terminating VDR system rejects:
- actual infinite expansion,
- actual infinite depth,
- actual infinite arity,
- and “exact by infinite continuation.”

Any object requiring such structure is outside terminating VDR.

---

## 19. Representation Priority Axiom

If a quantity admits both:
- a terminating exact VDR representation,
- and a nonterminating conventional representation,

then the terminating VDR representation is ontologically preferred inside the system.

This establishes VDR priority for exact discrete ontology, without denying the utility of conventional notation.

---

## 20. Pure-Math Interpretation Axiom

In the foundational system, remainder \(R\) is interpreted only as exact residual structure.

It is not initially identified with:
- momentum,
- pressure,
- force,
- energy,
- or any physical quantity.

These may later be introduced as domain interpretations of \(R\), but they are not part of the pure-math axioms.

---

## 21. Physics-Layer Extension Rule

A domain-specific interpretation may map VDR structure into physical semantics, provided it does not violate the foundational axioms above.

For example:
- a physics model may interpret \(R\) as momentum-like state,
but only after the pure terminating VDR structure is defined.

Thus:
- pure math first,
- physics second.

---

# Immediate Consequences

From these axioms:

1. Every valid object is finite.
2. Every valid object is exactly inspectable.
3. No valid object depends on epsilon reasoning.
4. No valid object depends on infinite completion.
5. Negative denominators are allowed.
6. Canonical sign placement is optional, not foundational.
7. Structure is preserved rather than approximated away.
8. The system is suitable, in principle, for exact computable ontology.

---

# Still Needed

These axioms define admissible structure, but not yet operations.

Still needed:
- equality axiom
- ordering axiom
- normalization algorithm
- addition rule
- subtraction rule
- multiplication rule
- division rule
- modulo rule
- optional shell-lock rule
- scalar interpretation rule for nonzero \(R\)
- equivalence of different nested decompositions

If you want, next I can draft:
- equality + normalization axioms,
- non-nested arithmetic rules,
- or a shell/modulo extension layer.

---

# Terminating VDR
## Equality + Normalization Axioms

These axioms assume the previously defined terminating VDR structure:
- strict triple form
- finite nesting
- recursion only in \(R\)
- exactness
- no infinity

They define:
- what it means for two VDR objects to be equal,
- and what normalization means without making normalization a condition of validity.

---

## 22. Equality Domain Axiom

Equality in terminating VDR has two distinct forms:

1. Structural Equality
2. Value Equality

These are not identical.

A VDR system must distinguish:
- objects that are written the same,
from
- objects that mean the same.

---

## 23. Structural Equality Axiom

Two VDR objects are structurally equal if and only if all corresponding slots match exactly, recursively and in order.

Formally:

$$
[V_1, D_1, R_1] \equiv_s [V_2, D_2, R_2]
$$

if and only if:
- \(V_1 = V_2\)
- \(D_1 = D_2\)
- \(R_1 \equiv_s R_2\)

For atomic remainder:
- \(r_1 \equiv_s r_2 \iff r_1 = r_2\)

For nested remainder:
- the atomic part must match,
- the child list length must match,
- and each corresponding child must be structurally equal in the same order.

Structural equality is exact representation identity.

---

## 24. Value Equality Axiom

Two VDR objects are value-equal if they denote the same exact terminating VDR value after normalization and closure-preserving reduction.

Formally:

$$
X \equiv_v Y
$$

if and only if:
$$
\mathrm{norm}(X) \equiv_s \mathrm{norm}(Y)
$$

Thus value equality is defined through normalized structural equality.

---

## 25. Closed Base Equality Axiom

For closed VDRs of the form:

$$
[V_1,D_1,0],\quad [V_2,D_2,0]
$$

value equality requires:

$$
V_1 \cdot D_2 = V_2 \cdot D_1
$$

provided:
- \(D_1 \neq 0\)
- \(D_2 \neq 0\)

So for closed VDRs:
- \([1,-2,0] \equiv_v [-1,2,0]\)
- \([2,4,0] \equiv_v [1,2,0]\)

even though they are not structurally equal.

---

## 26. Active Equality Axiom

For VDR objects with nonzero remainder, equality must preserve exact residual structure.

That is:
- equality is not determined only by the scalar core \(V/D\)
- the remainder is part of the value

Therefore:

$$
[V,D,R_1] \equiv_v [V,D,R_2]
$$

only if the normalized remainder structures are equal.

In particular:
- \([1,1,0] \not\equiv_v [1,1,1]\)
- \([1,1,1] \not\equiv_v [1,1,-1]\)

even though they share the same base ratio.

---

## 27. Remainder Equality Axiom

Remainder equality is recursive.

Two remainders are value-equal if and only if:
- their atomic parts reduce to the same integer,
- and their nested child VDR sets reduce to value-equal normalized forms.

Thus the remainder slot participates fully in exact equality.

The remainder is not metadata.
It is ontological value.

---

## 28. Order Irrelevance of Sibling Residual Terms Axiom

Within a nested remainder expansion, the order of sibling child VDR terms does not affect value equality.

So if:

$$
R = r + X_1 + X_2 + \dots + X_n
$$

then any permutation of the \(X_i\) is value-equal to the original remainder.

Thus remainder child order is:
- structurally relevant before normalization,
- but not value-relevant after normalization.

Normalization may reorder siblings canonically.

---

## 29. Raw Validity Axiom

A valid VDR object need not be normalized.

Examples of valid but non-normal forms:
- \([1,-2,0]\)
- \([2,4,0]\)
- \([3,6,0]\)
- nested remainders with repeated denominators
- nested remainders in arbitrary sibling order

Validity concerns admissibility.
Normalization concerns canonical representation.

---

## 30. Normalization Existence Axiom

Every valid terminating VDR object must admit a finite normalization procedure.

That is, for every valid VDR \(X\), there exists a finite normalized form:

$$
\mathrm{norm}(X)
$$

such that:
- \(\mathrm{norm}(X)\) is value-equal to \(X\)
- \(\mathrm{norm}(X)\) is structurally canonical under the normalization rules

---

## 31. Normalization Termination Axiom

Normalization must terminate in finite time on every valid terminating VDR object.

Normalization may not:
- introduce infinite expansion,
- recurse forever,
- or rely on limit procedures.

This follows from finite closure.

---

## 32. Sign Normalization Axiom

Normalization may relocate sign between \(V\) and \(D\), but must preserve value.

A canonical sign convention may be adopted, for example:
- denominator positive in normalized form

Thus:
- raw form may allow negative \(D\)
- normalized form may require \(D > 0\)

So:
- \([1,-2,0]\) normalizes to \([-1,2,0]\)

This is a normalization rule, not a validity rule.

---

## 33. Fraction Reduction Axiom

For closed or partially closed VDR nodes, normalization reduces the pair \((V,D)\) by their greatest common divisor whenever possible.

If:

$$
g = \gcd(V,D)
$$

then:

$$
[V,D,R] \mapsto [V/g, D/g, R']
$$

only if the transformation preserves exact remainder structure appropriately.

For closed VDRs:
- \([2,4,0] \mapsto [1,2,0]\)

For active VDRs, reduction is permitted only if remainder semantics remain exact under the transformed scale.

Thus closed reduction is immediate; active reduction requires compatibility with remainder interpretation.

---

## 34. Zero Denominator Exclusion Axiom

Normalization may never produce a denominator of zero.

Any operation that would require \(D = 0\) is invalid.

---

## 35. Remainder Flattening Axiom

Within a remainder, nested sums of sibling child VDR terms may be flattened into a single local child collection if no semantic distinction is lost.

Thus:

$$
r + (X_1 + X_2) + X_3
$$

may normalize to:

$$
r + X_1 + X_2 + X_3
$$

provided all remain in the same remainder level.

Flattening improves canonicality.

---

## 36. Atomic Remainder Consolidation Axiom

The atomic integer parts of a remainder must be combined into a single integer during normalization.

So:
- \(1 + 2 + X + Y\) normalizes to \(3 + X + Y\)

There should be exactly one atomic integer remainder part per node in normalized form.

---

## 37. Duplicate-Denominator Merge Axiom

If multiple immediate child VDRs in the same remainder level share the same normalized denominator and compatible structure, normalization should merge them.

For example, if:

$$
R = r + [V_1,D,R_1] + [V_2,D,R_2]
$$

and the merge is defined and exact, then normalization may replace them with a single child term.

This preserves the preference:
- one immediate child per denominator where possible.

---

## 38. Canonical Sibling Ordering Axiom

Normalized remainder children must be ordered canonically.

A valid canonical ordering may be:
1. by denominator magnitude
2. then by numerator
3. then by remainder structure

Any deterministic total ordering is acceptable, provided it is fixed system-wide.

This ensures normalized forms compare cleanly.

---

## 39. Normal Form Axiom

A VDR object is in normal form if and only if all of the following hold:

1. It is valid.
2. Every child VDR is itself in normal form.
3. Sign placement follows the system’s chosen canonical convention.
4. Closed \((V,D)\) pairs are reduced by gcd where permitted.
5. Atomic remainder parts are consolidated.
6. Duplicate-denominator sibling children are merged where permitted.
7. Sibling remainder children are in canonical order.

Normal form is unique if the normalization rules are complete and deterministic.

---

## 40. Normalized Equality Axiom

Two VDR objects are value-equal if and only if their normal forms are structurally equal.

$$
X \equiv_v Y \iff \mathrm{norm}(X) \equiv_s \mathrm{norm}(Y)
$$

This is the master equality rule.

---

## 41. Equality Preservation Axiom

Any valid normalization step must preserve value equality.

If:
$$
X \mapsto X'
$$

is a normalization step, then:
$$
X \equiv_v X'
$$

Normalization changes representation, never value.

---

## 42. Distinction Preservation Axiom

Normalization may not collapse genuinely distinct active remainder states.

So if two VDR objects differ in meaningful remainder structure, normalization must not erase that distinction merely because their scalar cores match.

This prevents:
- active state from being reduced away into simple fraction equality.

---

## 43. Closed-Form Preference Axiom

If a VDR object can be normalized into a fully closed form with all remainders zero, that closed form is preferred over any active equivalent representation.

Thus, where exact closure is possible, the normalized form should settle there.

This gives the system a preference for closure without forcing all raw forms to begin closed.

---

## 44. Canonicality Optionality Axiom

Canonical normal form is required for:
- equality testing,
- comparison,
- serialization,
- exact lookup,
- and reproducible computation.

Canonical normal form is not required for:
- intermediate authoring,
- raw construction,
- exploratory manipulation,
- or pre-normalized internal computation.

This preserves computation freedom while still enabling exact identity.

---

# Immediate Consequences

From these axioms:

1. Structural equality and value equality are separated cleanly.
2. Negative denominators remain valid in raw form.
3. Normalization can choose a canonical sign convention later.
4. Closed fractions reduce naturally.
5. Active remainder structure remains part of exact value.
6. Sibling order is not value-significant after normalization.
7. Every valid terminating VDR should have a finite normalized form.

---

# Still Needed

To complete the foundational layer, the next major pieces are:

- ordering axioms
- addition rules
- subtraction rules
- multiplication rules
- division rules
- remainder merge rules
- optional modulo/shell rules
- scalar interpretation of active objects

If you want, next I can draft:
- non-nested arithmetic rules,
- ordering axioms,
- or the modulo/shell extension layer.

---

# Terminating VDR
## Arithmetic Axioms
### First-Pass Arithmetic Layer

These axioms extend the prior VDR system with arithmetic. They are intentionally conservative:
- pure-math first
- exact
- finite
- no approximation
- no infinity
- no premature physics semantics

This first pass handles:
- closed and active VDR objects
- arithmetic as exact structure-preserving transformation
- recursive finite closure

It does not yet define modulo-shell behavior.

---

## 45. Arithmetic Closure Axiom

For any primitive arithmetic operation \( \odot \in \{+, -, \times, \div\} \),

if:
- the operation is valid,
- the result can be represented as a terminating exact VDR object,

then the result must itself be a valid terminating VDR object.

If exact finite terminating representation is impossible, the operation is invalid in terminating VDR.

---

## 46. Closed Addition Axiom

For two closed VDR objects:

$$
[V_1,D_1,0] + [V_2,D_2,0]
$$

their sum is the closed VDR:

$$
[V_1D_2 + V_2D_1,\; D_1D_2,\; 0]
$$

subject to later normalization.

Example:
$$
[1,2,0] + [1,3,0] = [5,6,0]
$$

---

## 47. Closed Subtraction Axiom

For two closed VDR objects:

$$
[V_1,D_1,0] - [V_2,D_2,0]
$$

their difference is:

$$
[V_1D_2 - V_2D_1,\; D_1D_2,\; 0]
$$

subject to later normalization.

Example:
$$
[3,4,0] - [1,2,0] = [2,8,0] \mapsto [1,4,0]
$$

---

## 48. Closed Multiplication Axiom

For two closed VDR objects:

$$
[V_1,D_1,0] \times [V_2,D_2,0]
$$

their product is:

$$
[V_1V_2,\; D_1D_2,\; 0]
$$

subject to later normalization.

Example:
$$
[2,3,0] \times [3,5,0] = [6,15,0] \mapsto [2,5,0]
$$

---

## 49. Closed Division Axiom

For two closed VDR objects:

$$
[V_1,D_1,0] \div [V_2,D_2,0]
$$

the division is valid if and only if:
- \(V_2 \neq 0\)

and yields:

$$
[V_1D_2,\; D_1V_2,\; 0]
$$

subject to later normalization.

Example:
$$
[2,3,0] \div [4,5,0] = [10,12,0] \mapsto [5,6,0]
$$

---

## 50. Zero-Division Exclusion Axiom

Division by a VDR object whose closed scalar core is zero is invalid.

At minimum:
- \([0,D,0]\) may not appear in divisor position.

If active zero states later exist, their divisibility rules must be explicitly defined, not assumed.

---

## 51. Active Arithmetic Preservation Axiom

If either operand has nonzero remainder, arithmetic must preserve that active structure exactly.

That is:
- active remainder may not be discarded,
- collapsed into approximation,
- or replaced by epsilon behavior.

Arithmetic on active VDRs must produce a valid exact VDR result whose remainder captures all unresolved structure introduced by the operation.

---

## 52. Common-Denominator Addition Axiom

For VDR objects sharing a denominator and with atomic remainders:

$$
[V_1,D,R_1] + [V_2,D,R_2]
$$

their sum is:

$$
[V_1+V_2,\; D,\; R_1+R_2]
$$

before any remainder reduction or nesting normalization.

Example:
$$
[3,5,1] + [2,5,-1] = [5,5,0]
$$

This may later normalize to a closed form.

---

## 53. Common-Denominator Subtraction Axiom

For VDR objects sharing a denominator and with atomic remainders:

$$
[V_1,D,R_1] - [V_2,D,R_2]
$$

their difference is:

$$
[V_1-V_2,\; D,\; R_1-R_2]
$$

before normalization.

Example:
$$
[7,5,1] - [2,5,1] = [5,5,0]
$$

---

## 54. Different-Denominator Addition Axiom

For two VDR objects with possibly different denominators:

$$
[V_1,D_1,R_1] + [V_2,D_2,R_2]
$$

their sum is formed by cross-scaling the closed components:

$$
[V_1D_2 + V_2D_1,\; D_1D_2,\; R']
$$

where \(R'\) is the exact remainder combination induced by:
- scaled contribution of \(R_1\),
- scaled contribution of \(R_2\),
- and any necessary residual structure from the denominator merge.

In the first-pass arithmetic layer, this may be expressed conservatively as:

$$
R' = \mathrm{lift}(R_1,D_2) + \mathrm{lift}(R_2,D_1)
$$

where `lift` is a structure-preserving remainder scaling operator to be defined.

Thus denominator unification must also unify remainder scale.

---

## 55. Different-Denominator Subtraction Axiom

Similarly:

$$
[V_1,D_1,R_1] - [V_2,D_2,R_2]
$$

yields:

$$
[V_1D_2 - V_2D_1,\; D_1D_2,\; R']
$$

with:

$$
R' = \mathrm{lift}(R_1,D_2) - \mathrm{lift}(R_2,D_1)
$$

Again, exact remainder lifting must be preserved.

---

## 56. Remainder Lift Axiom

When denominators are unified by multiplication, the remainder must be lifted into the new denominator context.

For atomic remainder \(r\):

$$
\mathrm{lift}(r,k) = kr
$$

For nested remainder:

$$
\mathrm{lift}(r + X_1 + \dots + X_n,\; k)
=
kr + \mathrm{lift}(X_1,k) + \dots + \mathrm{lift}(X_n,k)
$$

For child VDR:

$$
\mathrm{lift}([V,D,R],k) = [kV,\; D,\; \mathrm{lift}(R,k)]
$$

unless later refinement proves a better canonical scaling law.

This axiom ensures remainder participates in scale transformation.

---

## 57. Active Multiplication Axiom

For active VDR multiplication:

$$
[V_1,D_1,R_1] \times [V_2,D_2,R_2]
$$

the product is:

$$
[V_1V_2,\; D_1D_2,\; R']
$$

where \(R'\) must include all exact active structure induced by:
- multiplication of closed parts with active parts,
- multiplication of active parts with each other,
- and any cross-term structure.

In first-pass form:

$$
R' =
\mathrm{mul\_left}(R_1, V_2, D_2)
+
\mathrm{mul\_right}(R_2, V_1, D_1)
+
\mathrm{mul\_cross}(R_1,R_2)
$$

with these operators to be defined exactly in later arithmetic refinement.

This axiom prevents “active parts vanish under multiplication.”

---

## 58. Active Division Axiom

For active VDR division:

$$
[V_1,D_1,R_1] \div [V_2,D_2,R_2]
$$

the division is valid only if:
- the divisor is not exact-zero,
- and the result admits finite exact VDR representation.

The quotient has the form:

$$
[V_1D_2,\; D_1V_2,\; R']
$$

where \(R'\) captures all exact active residual structure induced by the division.

If exact finite remainder closure cannot be achieved, the division is invalid in terminating VDR.

This is a strong restriction and may exclude many cases.

---

## 59. Additive Identity Axiom

The additive identity is:

$$
[0,1,0]
$$

For every valid VDR \(X\):

$$
X + [0,1,0] \equiv_v X
$$

---

## 60. Multiplicative Identity Axiom

The multiplicative identity is:

$$
[1,1,0]
$$

For every valid VDR \(X\):

$$
X \times [1,1,0] \equiv_v X
$$

---

## 61. Additive Inverse Axiom

For every valid VDR object:

$$
X = [V,D,R]
$$

there exists an additive inverse:

$$
-X = [-V,D,-R]
$$

provided remainder negation is defined recursively.

Then:

$$
X + (-X) \equiv_v [0,1,0]
$$

after normalization and closure-preserving reduction.

---

## 62. Recursive Remainder Negation Axiom

Remainder negation is recursive.

For atomic remainder:
$$
-(r) = -r
$$

For nested remainder:
$$
-(r + X_1 + \dots + X_n)
=
-r + (-X_1) + \dots + (-X_n)
$$

For child VDR:
$$
-[V,D,R] = [-V,D,-R]
$$

unless later normalization moves sign to \(D\).

---

## 63. Commutativity Axiom (Addition)

Addition is value-commutative:

$$
X + Y \equiv_v Y + X
$$

though raw structural forms before normalization may differ.

---

## 64. Commutativity Axiom (Multiplication)

Multiplication is value-commutative:

$$
X \times Y \equiv_v Y \times X
$$

again, possibly requiring normalization to reveal equality.

---

## 65. Associativity Axiom (Addition)

Addition is value-associative:

$$
(X + Y) + Z \equiv_v X + (Y + Z)
$$

provided all intermediate results remain valid terminating VDRs.

---

## 66. Associativity Axiom (Multiplication)

Multiplication is value-associative:

$$
(X \times Y) \times Z \equiv_v X \times (Y \times Z)
$$

provided all intermediate results remain valid terminating VDRs.

---

## 67. Distributivity Axiom

Multiplication distributes over addition:

$$
X \times (Y + Z) \equiv_v (X \times Y) + (X \times Z)
$$

provided all resulting terms admit valid finite exact VDR form.

---

## 68. Active-Closure Preference Axiom

If an arithmetic result yields a remainder structure that normalizes to zero globally, the result should normalize to a closed form.

Example:
$$
[3,5,1] + [2,5,-1] = [5,5,0] \mapsto [1,1,0]
$$

So active arithmetic may produce closure when exact cancellation occurs.

---

## 69. No Approximation Rescue Axiom

If arithmetic on valid VDR objects would require:
- truncation,
- decimal approximation,
- float conversion,
- infinite continuation,
- or epsilon tests

then the operation is not valid in terminating VDR arithmetic.

No approximation may be smuggled in to force closure.

---

## 70. Arithmetic Exactness Axiom

All arithmetic must preserve:
- finite closure,
- exact inspectability,
- countability,
- and computable termination.

Arithmetic is not merely symbolic rewriting.
It is a transformation of exact finite objects into exact finite objects.

---

# Immediate Consequences

From these arithmetic axioms:

1. Closed VDRs behave like exact fractions.
2. Active remainder participates in arithmetic, not as error but as exact state.
3. Addition and subtraction on equal denominators are straightforward.
4. Denominator unification requires remainder lifting.
5. Multiplication and division of active objects require a deeper remainder algebra still to be completed.
6. Approximation is forbidden at every stage.

---

# What Still Needs Definition

These axioms establish arithmetic shape, but several operators remain schematic:

- exact definition of `lift`
- exact multiplication of active remainders
- exact division of active remainders
- full normalization after arithmetic
- equivalence rules for nested remainder decompositions
- optional modulo/shell arithmetic

So the next rigorous step should probably be:

1. fully define `lift`
2. define arithmetic for atomic-remainder VDRs only
3. then extend to nested remainders
4. then add modulo-shell layer

If you want, next I can do one of these:
- make `lift` fully formal,
- restrict and fully define arithmetic for atomic-remainder VDR only,
- or draft the modulo/shell extension.

---

# Terminating VDR
## Exact Definition of Lift

Good place to tighten. `lift` has to be exact, recursive, finite, and purely structural.

The purpose of `lift` is:

- when denominator context is scaled by an integer factor \(k\),
- the remainder structure must be transported into the new denominator frame
- without approximation,
- without loss of structure,
- and while preserving exact value equality.

This definition assumes:
- terminating VDR
- finite nesting
- pure-math interpretation only

---

## 71. Lift Domain Axiom

Lift is a total operation on:
- valid remainder objects
- and nonzero integer scale factors

Formally:

$$
\mathrm{lift} : \mathcal{R} \times (\mathbb{Z}\setminus\{0\}) \to \mathcal{R}
$$

where:
- \(\mathcal{R}\) is the set of valid remainder objects,
- \(k \in \mathbb{Z}\setminus\{0\}\)

Lift by zero is invalid.

---

## 72. Lift Purpose Axiom

Lift transforms a remainder object from one denominator context into another scaled denominator context.

If a VDR object:

$$
[V,D,R]
$$

is rewritten into a denominator-scaled form:

$$
[kV,\; kD,\; R']
$$

then \(R'\) must be:

$$
R' = \mathrm{lift}(R,k)
$$

such that exact value is preserved.

Thus lift is the denominator-frame transport operator for remainder.

---

## 73. Atomic Lift Axiom

For atomic integer remainder \(r\), lift by factor \(k\) is:

$$
\mathrm{lift}(r,k) = kr
$$

for all:
- \(r \in \mathbb{Z}\)
- \(k \in \mathbb{Z}\setminus\{0\}\)

Examples:
- \(\mathrm{lift}(1,3)=3\)
- \(\mathrm{lift}(-2,5)=-10\)
- \(\mathrm{lift}(4,-2)=-8\)

Atomic lift is exact integer multiplication.

---

## 74. Recursive Lift Axiom

For nested remainder:

$$
R = r + X_1 + X_2 + \dots + X_n
$$

lift is defined recursively by:

$$
\mathrm{lift}(R,k)
=
kr + \mathrm{lift}(X_1,k) + \mathrm{lift}(X_2,k) + \dots + \mathrm{lift}(X_n,k)
$$

where:
- \(r \in \mathbb{Z}\)
- each \(X_i\) is a valid VDR object
- \(n\) is finite

Thus lift distributes over finite remainder decomposition.

---

## 75. VDR Lift Axiom

For a child VDR object:

$$
X = [V,D,R]
$$

lift by factor \(k\) is defined as:

$$
\mathrm{lift}(X,k) = [kV,\; D,\; \mathrm{lift}(R,k)]
$$

That is:
- the child numerator is scaled by \(k\),
- the child denominator remains unchanged,
- the child remainder is recursively lifted.

This keeps the child’s internal denominator structure intact while transporting it into the parent’s scaled frame.

---

## 76. Lift Structure Preservation Axiom

Lift must preserve:
- finite depth,
- finite branching,
- exact tree shape,
- and recursion locality.

Lift may scale coefficients, but it may not:
- create infinite nesting,
- move recursion outside the third slot,
- or collapse nested structure unless a later normalization step does so explicitly.

---

## 77. Lift Identity Axiom

Lift by \(1\) is identity:

$$
\mathrm{lift}(R,1) = R
$$

for every valid remainder object \(R\).

For child VDR:
$$
\mathrm{lift}([V,D,R],1) = [V,D,R]
$$

---

## 78. Lift Sign Axiom

Lift by \(-1\) negates the lifted structure:

$$
\mathrm{lift}(R,-1) = -R
$$

recursively.

Thus:
- \(\mathrm{lift}(r,-1) = -r\)
- \(\mathrm{lift}([V,D,R],-1) = [-V,D,\mathrm{lift}(R,-1)]\)

This gives sign consistency between lift and additive inversion.

---

## 79. Lift Composition Axiom

Lift composes multiplicatively:

$$
\mathrm{lift}(\mathrm{lift}(R,a),b) = \mathrm{lift}(R,ab)
$$

for all valid \(R\) and nonzero integers \(a,b\).

Similarly for child VDRs:

$$
\mathrm{lift}(\mathrm{lift}(X,a),b) = \mathrm{lift}(X,ab)
$$

This is essential for exact multi-stage denominator unification.

---

## 80. Lift Additivity Axiom

Lift distributes over finite remainder addition:

$$
\mathrm{lift}(R_1 + R_2, k)
=
\mathrm{lift}(R_1,k) + \mathrm{lift}(R_2,k)
$$

for all valid finite remainder objects.

This follows from recursive definition but is elevated here as a formal arithmetic law.

---

## 81. Lift Zero Remainder Axiom

Lift preserves zero:

$$
\mathrm{lift}(0,k)=0
$$

for all nonzero integers \(k\).

Thus a closed object remains closed under denominator scaling.

Example:
$$
[V,D,0] \mapsto [kV,kD,0]
$$

---

## 82. Lift Equality Preservation Axiom

If two remainder objects are value-equal, then their lifts by the same scale factor are value-equal:

$$
R_1 \equiv_v R_2 \implies \mathrm{lift}(R_1,k)\equiv_v \mathrm{lift}(R_2,k)
$$

Likewise for VDR objects:

$$
X_1 \equiv_v X_2 \implies \mathrm{lift}(X_1,k)\equiv_v \mathrm{lift}(X_2,k)
$$

This ensures lift is compatible with the equality system.

---

## 83. Lift Normalization Compatibility Axiom

Lift need not produce normal form directly.

However:

$$
\mathrm{norm}(\mathrm{lift}(X,k))
$$

must exist and terminate for all valid terminating VDR objects \(X\) and nonzero integers \(k\).

Thus lift preserves finite normalizability.

---

## 84. Lift Exactness Axiom

Lift may not introduce:
- decimal approximation,
- float conversion,
- irrational symbols,
- hidden infinite expansions,
- or epsilon-based reasoning.

Lift is exact integer-structural transport only.

---

## 85. Lift Denominator Invariance Axiom

Lift does not alter denominators of nested child VDR nodes directly.

That is, for:

$$
X=[V,D,R]
$$

$$
\mathrm{lift}(X,k)=[kV,D,\mathrm{lift}(R,k)]
$$

not:

$$
[kV,kD,\dots]
$$

This is intentional:
- the child node keeps its own internal denominator identity,
- while the numerator and remainder absorb the outer frame scaling.

This distinguishes:
- local denominator structure
from
- external denominator transport.

---

## 86. Parent Reframing Axiom

Lift exists because denominator scaling at a parent level does not imply denominator rewriting at all descendant levels.

Instead:
- the parent denominator frame changes,
- child contributions must be reweighted into that frame,
- and lift performs that reweighting by acting on child numerators and child remainder structures.

This is the reason lift acts on \(V\) and \(R\), but not directly on child \(D\).

---

## 87. Finite Lift Axiom

Because every valid VDR is finite, every lift operation must terminate after a finite number of recursive applications.

Lift is therefore a computable exact operation in terminating VDR.

---

# Summary of Exact Lift

For atomic integer remainder:
$$
\mathrm{lift}(r,k)=kr
$$

For nested remainder:
$$
\mathrm{lift}(r + X_1 + \dots + X_n, k)
=
kr + \mathrm{lift}(X_1,k)+\dots+\mathrm{lift}(X_n,k)
$$

For child VDR:
$$
\mathrm{lift}([V,D,R],k)=[kV,D,\mathrm{lift}(R,k)]
$$

This is the exact finite recursive definition.

---

# Why this is the correct first-pass lift
This definition gives you:

- exact denominator-context scaling
- finite recursive transport
- compatibility with sign
- compatibility with equality
- compatibility with normalization
- no approximation
- no damage to child denominator identity

It is also simple enough to compute.

---

# What this still leaves open
Now that `lift` is exact, the next big questions are:

1. Is this the only valid lift?
2. Does this preserve the intended semantics of active remainder in all arithmetic cases?
3. Should there be a second operator for denominator absorption or rebasing?
4. How should multiplication/division of active VDRs use lifted remainders exactly?

Those are next-layer questions.

If you want, next I can:
- rewrite the arithmetic axioms using this exact `lift`,
- test `lift` on concrete examples,
- or define `rebase` as a second operator distinct from `lift`.

---

# Terminating VDR
## Rebase Axioms
### Supporting Lift

Good. If `lift` is “transport remainder through a denominator scale factor,” then `rebase` should be the companion operation that changes the denominator frame of a VDR node itself while preserving exact value.

So:

- `lift` acts through remainder structure when parent denominator changes
- `rebase` changes the denominator context of a VDR object directly

That separation is useful.

---

## 88. Rebase Domain Axiom

Rebase is a total operation on:
- valid VDR objects
- and nonzero integer target denominators

Formally:

$$
\mathrm{rebase} : \mathcal{V} \times (\mathbb{Z}\setminus\{0\}) \to \mathcal{V}
$$

where:
- \(\mathcal{V}\) is the set of valid terminating VDR objects,
- \(B \in \mathbb{Z}\setminus\{0\}\) is the target denominator.

Rebase to denominator zero is invalid.

---

## 89. Rebase Purpose Axiom

Rebase transforms a VDR object into an exactly value-equal VDR object whose top-level denominator is the requested target denominator.

If:

$$
X = [V,D,R]
$$

then:

$$
\mathrm{rebase}(X,B) = [V',B,R']
$$

such that:

$$
[V',B,R'] \equiv_v [V,D,R]
$$

Thus rebase changes top-level denominator frame while preserving exact value.

---

## 90. Closed Rebase Axiom

For a closed VDR object:

$$
[V,D,0]
$$

rebasing to denominator \(B\) is valid if and only if:

$$
\frac{VB}{D} \in \mathbb{Z}
$$

In that case:

$$
\mathrm{rebase}([V,D,0],B) = \left[\frac{VB}{D},\; B,\; 0\right]
$$

If \(\frac{VB}{D}\) is not an integer, then closed rebase cannot remain closed and must use active remainder structure, if such a finite exact form exists.

---

## 91. Exact Closed Rebase Criterion

A closed VDR may be rebased into another closed VDR only when the target denominator is compatible with exact numerator transfer.

Equivalently, closed-to-closed rebase is possible iff:

$$
D \mid VB
$$

If not, exactness cannot be preserved in a closed form.

---

## 92. Active Rebase Axiom

For an active VDR:

$$
[V,D,R]
$$

rebasing to denominator \(B\) yields:

$$
\mathrm{rebase}([V,D,R],B) = [V',B,R']
$$

where:
- \(V'\) is the rebased top-level numerator,
- \(R'\) is the exact residual structure required to preserve value equality.

The result must satisfy:

$$
[V',B,R'] \equiv_v [V,D,R]
$$

and remain a valid terminating VDR object.

---

## 93. Rebase Construction Axiom

Rebase is defined by denominator unification followed by exact residual preservation.

Specifically, for:

$$
X = [V,D,R]
$$

and target denominator \(B\),

let:

$$
g = \gcd(D,B)
$$

$$
m = \frac{B}{g}, \qquad n = \frac{D}{g}
$$

Then rebase must preserve the relation between the original and target denominator frames by transporting unresolved structure through exact finite operations rather than approximation.

In first-pass constructive form:
- scale the top-level value by \(m\),
- scale the original frame by \(m\),
- then resolve the mismatch between \(mD\) and \(B\) through exact remainder construction.

This means rebase is not merely “change denominator”; it is “reconstruct exact object in a new denominator frame.”

---

## 94. Rebase Through Lift Axiom

Rebase is supported by lift.

If a VDR object is expanded into a denominator-multiplied frame, then its remainder must be transported by lift before the top-level denominator is replaced.

So a valid rebase procedure may use:

1. denominator alignment,
2. numerator scaling,
3. remainder lift,
4. normalization into target denominator.

Thus lift is a necessary sub-operation of exact rebase.

---

## 95. Same-Denominator Rebase Axiom

Rebasing a VDR object to its current denominator is identity:

$$
\mathrm{rebase}([V,D,R],D) = [V,D,R]
$$

for every valid VDR object.

---

## 96. Sign Rebase Axiom

Rebase may target positive or negative denominators.

Thus:
- \(\mathrm{rebase}(X,B)\) and \(\mathrm{rebase}(X,-B)\) are both permitted when \(B \neq 0\),
- provided exact value is preserved.

Sign normalization is not required at the level of validity.

---

## 97. Rebase Equality Preservation Axiom

Rebase preserves value equality:

$$
\mathrm{rebase}(X,B) \equiv_v X
$$

for every valid rebasing operation.

Representation changes, value does not.

---

## 98. Rebase Structural Non-Identity Axiom

Rebase need not preserve structural equality.

That is:
- rebased objects are generally not structurally equal to their original form,
- only value-equal.

Thus:

$$
\mathrm{rebase}(X,B) \not\equiv_s X
$$

in general.

---

## 99. Rebase Termination Axiom

Rebase must terminate in finite time on all valid terminating VDR objects for which an exact rebased form exists.

If no finite exact rebased form exists, the rebase operation is invalid in terminating VDR.

Rebase may not use:
- infinite expansion,
- decimal conversion,
- limit procedures,
- or epsilon tests.

---

## 100. Rebase Exactness Axiom

Rebase may not introduce:
- approximation,
- irrational primitive insertion,
- float conversion,
- decimal truncation,
- or hidden infinite continuation.

Rebase is exact finite reconstruction only.

---

## 101. Rebase Normalizability Axiom

If rebase succeeds, the result must be finitely normalizable.

That is:

$$
\mathrm{norm}(\mathrm{rebase}(X,B))
$$

must exist and terminate.

---

## 102. Rebase Closure Preservation Axiom

If a VDR object is closed and a closed exact rebase exists, rebase must preserve closure:

$$
[V,D,0] \mapsto [V',B,0]
$$

If a closed exact rebase does not exist, rebase may produce an active VDR only if that active VDR is exact and finite.

Thus closure is preferred but not forced beyond exactness.

---

## 103. Rebase Minimal Residual Axiom

When multiple exact finite rebased forms exist for the same target denominator, normalization should prefer the one with minimal active remainder complexity.

This may be defined later by:
- smallest recursion depth,
- fewest nested children,
- smallest absolute atomic remainder,
- or another fixed metric.

This is a normalization preference, not a validity rule.

---

## 104. Rebase Composition Axiom

If rebasing through two target denominators is valid, the composition must preserve value:

$$
\mathrm{rebase}(\mathrm{rebase}(X,B_1),B_2) \equiv_v \mathrm{rebase}(X,B_2)
$$

provided both paths terminate and all rebases are valid.

Normalization may be required to compare the results.

---

## 105. Rebase and Normalization Commutativity Axiom

Normalization and rebase need not structurally commute, but they must commute up to value equality:

$$
\mathrm{norm}(\mathrm{rebase}(X,B)) \equiv_v \mathrm{rebase}(\mathrm{norm}(X),B)
$$

This ensures rebasing works consistently on raw and normalized forms.

---

## 106. Child Denominator Integrity Axiom

Rebase changes only the top-level denominator of the target VDR node.

It does not directly rewrite denominators of nested child VDR nodes unless such rewriting is explicitly part of a deeper normalization/rebase step applied to those children.

Thus:
- local denominator identity is preserved within nested structure,
- top-level denominator frame is what rebase changes.

This mirrors the logic behind lift.

---

## 107. Rebase Failure Axiom

Rebase fails if any of the following are true:

1. Target denominator is zero
2. Exact finite representation cannot be constructed
3. Construction requires infinite recursion
4. Construction requires approximation
5. Construction violates VDR validity axioms

Failure is a legitimate outcome.

Not every denominator target must be reachable inside terminating VDR.

---

# Summary of Rebase

For a VDR object:

$$
X = [V,D,R]
$$

and target denominator \(B \neq 0\),

`rebase(X,B)` means:

- produce a new VDR object
- with top-level denominator \(B\)
- exactly value-equal to \(X\)
- using finite exact reconstruction
- typically supported by lift for residual transport

So:
- `lift` transports residual structure under frame scaling
- `rebase` changes the explicit denominator frame of the object itself

That gives you a clean two-operator system.

---

# Relationship Between Lift and Rebase

- `lift(R,k)` acts on remainder structure under scaling
- `rebase([V,D,R],B)` acts on the VDR node as a whole

You can think of it as:

- `lift` is internal transport
- `rebase` is external frame change

That seems like the correct separation.

---

# Still Needed

To make rebase fully constructive, the next thing to define is:

- the exact algorithm for active rebasing when closed rebasing does not land cleanly
- i.e. how \(R'\) is built when \((VB)/D\) is not an integer

That is probably the next key problem.

If you want, next I can:
- define constructive active rebasing,
- rewrite arithmetic using both `lift` and `rebase`,
- or give worked examples of rebase on simple VDR objects.

---

# Terminating VDR
## Axioms for Exact Active Rebasing
### When Closed Rebasing Does Not Land Cleanly

Good. This is the key step.

We want to define what happens when:

$$
X = [V,D,R]
$$

is rebased to target denominator \(B\),
but the closed rebasing condition fails.

That means:

$$
\frac{VB}{D} \notin \mathbb{Z}
$$

for the closed core, or more generally the object cannot be rewritten into a closed top-level VDR with denominator \(B\).

So instead of failing immediately, we construct an exact active rebased form.

The goal is:

$$
\mathrm{rebase}(X,B) = [Q,B,R']
$$

such that:
- exact value is preserved,
- no approximation is introduced,
- the result is finite,
- and the unresolved part becomes exact remainder structure.

---

## 108. Active Rebase Trigger Axiom

Active rebasing is required exactly when closed rebasing is impossible but exact finite rebasing remains possible.

For a closed core \([V,D,0]\), active rebasing is triggered when:

$$
\frac{VB}{D} \notin \mathbb{Z}
$$

and an exact finite active representation exists.

Thus active rebasing is the exact alternative to failed closed rebasing.

---

## 109. Quotient-Residual Decomposition Axiom

For rebasing \([V,D,R]\) into denominator \(B\), define the scaled numerator demand:

$$
N = VB
$$

Then divide \(N\) by \(D\) using integer division:

$$
N = QD + S
$$

where:
- \(Q \in \mathbb{Z}\)
- \(S \in \mathbb{Z}\)
- \(|S| < |D|\) in the chosen division convention

Then the rebased top-level object begins as:

$$
[Q,B,R']
$$

where \(R'\) captures the exact residual contribution from \(S\) plus the rebased original remainder.

So the quotient becomes the new top-level \(V\), and the residual becomes active remainder structure.

---

## 110. Residual Core Rebase Axiom

For a closed source object:

$$
[V,D,0]
$$

rebased to \(B\),

let:

$$
VB = QD + S
$$

Then:

$$
\mathrm{rebase}([V,D,0],B) = [Q,B,\rho(S,D,B)]
$$

where:
- \(\rho(S,D,B)\) is the exact residual-construction operator.

Thus the residual term is not discarded.
It becomes the exact active remainder required to preserve value.

---

## 111. Residual Construction Axiom

The residual-construction operator is defined by:

$$
\rho(S,D,B) = [S,D,0]
$$

embedded into the remainder slot of the rebased object.

Thus:

$$
\mathrm{rebase}([V,D,0],B) = [Q,B,[S,D,0]]
$$

whenever closed rebasing does not land cleanly.

This is the simplest exact active rebasing rule.

It means:
- the unresolved part remains an exact child VDR,
- not a decimal tail,
- not an approximation,
- not a symbolic “error.”

---

## 112. Exactness of Active Rebase Axiom

With the above construction:

$$
[Q,B,[S,D,0]]
$$

must be exactly value-equal to the original object:

$$
[Q,B,[S,D,0]] \equiv_v [V,D,0]
$$

This is the foundational correctness condition of active rebasing.

---

## 113. Recursive Rebase Axiom

If the child residual VDR:

$$
[S,D,0]
$$

can itself be rebased into denominator \(B\) exactly and finitely, then rebasing may continue recursively until either:
- full closure is reached,
- or a stable active finite normal form is reached.

Thus active rebasing may recurse through the remainder slot, but only finitely.

This gives:

$$
\mathrm{rebase}([V,D,0],B)
=
[Q,B,\mathrm{rebase}([S,D,0],B)]
$$

when such recursive rebasing is valid and terminating.

---

## 114. Finite Active Rebase Axiom

Recursive active rebasing is valid only if it terminates after finite depth.

If repeated rebasing of the residual would produce an infinite chain, then:
- the target denominator \(B\) is not valid for exact terminating rebase.

Thus active rebasing is permitted only when the residual chain is finitely closable.

---

## 115. Active Rebase Canonical Form Axiom

When closed rebasing fails but active rebasing succeeds, the canonical first-pass rebased form is:

$$
[Q,B,[S,D,0]]
$$

with:
- \(Q\) from integer division of \(VB\) by \(D\),
- \(S\) the exact residual numerator,
- and \([S,D,0]\) embedded as the remainder child.

This gives a simple universal fallback form.

---

## 116. Active Remainder Preservation Axiom

If the source object already has active remainder:

$$
[V,D,R]
$$

then rebasing to denominator \(B\) proceeds by:

1. computing the closed-core quotient/residual decomposition of \(VB\),
2. lifting the original remainder into the new denominator context,
3. combining the rebased residual core with the lifted original remainder.

Thus:

$$
\mathrm{rebase}([V,D,R],B)
=
[Q,B,\; [S,D,0] + \mathrm{lift}(R,B)]
$$

before normalization.

This is the exact first-pass active rebasing rule for already-active objects.

---

## 117. Active Residual Combination Axiom

The total active remainder after rebasing is the exact sum of:
- the residual generated by quotient failure,
- and the lifted original remainder.

Thus rebasing preserves both:
- newly introduced denominator mismatch,
- and pre-existing active state.

Neither may be discarded.

---

## 118. Zero Residual Rebase Collapse Axiom

If the quotient residual \(S = 0\), then active rebasing collapses back to closed rebasing.

So:

$$
\mathrm{rebase}([V,D,0],B) = [Q,B,0]
$$

when:
$$
VB = QD
$$

This ensures active rebasing is used only when actually necessary.

---

## 119. Sign of Residual Axiom

The sign of \(S\) is preserved exactly in the residual child:

$$
[S,D,0]
$$

No sign normalization is forced at the active rebase stage.

For example:
- positive mismatch gives positive residual child,
- negative mismatch gives negative residual child.

Sign handling remains exact and explicit.

---

## 120. Residual Child Integrity Axiom

The residual child:

$$
[S,D,0]
$$

must remain structurally exact at creation.

It may later be:
- normalized,
- rebased again,
- reduced,
- or merged with sibling residual children,

but its initial role is to preserve the unresolved exact part of the source value.

---

## 121. Termination Criterion for Active Rebase Axiom

An active rebase succeeds if and only if the recursive rebasing of all generated residual children reaches a finite exact normal form.

If any residual branch would require infinite continuation, the rebase operation fails.

This is the decisive anti-infinity requirement.

---

## 122. Exact Active Rebase Failure Axiom

Active rebasing is invalid if:
- the quotient residual construction creates an infinite recursive chain,
- exact residual preservation would require nonterminating expansion,
- or normalization cannot finitely close the rebased structure.

Thus exact active rebasing is permitted only for finitely resolvable targets.

---

## 123. Active Rebase Minimality Axiom

If multiple active rebased forms are possible, the preferred one is the one that:
1. minimizes recursion depth,
2. minimizes residual child count,
3. minimizes unreduced denominator complexity,
4. preserves exactness.

This is a normalization preference, not a validity rule.

---

## 124. Recursive Exactness Axiom

At every recursive active rebase step, the residual child must preserve exact value:

If:

$$
VB = QD + S
$$

then:

$$
[V,D,0] \equiv_v [Q,B,[S,D,0]]
$$

and if rebased recursively:

$$
[S,D,0] \equiv_v \mathrm{rebase}([S,D,0],B)
$$

Thus exactness must hold at every level, not just globally.

---

## 125. No Hidden Series Axiom

Active rebasing may never be interpreted as:
- decimal expansion,
- continued approximation,
- or hidden infinite series.

The residual child is a complete finite exact object, not a placeholder for “more digits.”

This is crucial.

---

# Core Exact Algorithm

Given source:

$$
X=[V,D,R]
$$

and target denominator \(B\neq 0\),

## Step 1: Scale top-level numerator
$$
N = VB
$$

## Step 2: Integer divide by source denominator
$$
N = QD + S
$$

## Step 3: Construct rebased top-level node
$$
[Q,B,\dots]
$$

## Step 4: Construct exact residual child
$$
[S,D,0]
$$

## Step 5: Lift any existing source remainder
$$
\mathrm{lift}(R,B)
$$

## Step 6: Combine into exact active remainder
$$
R' = [S,D,0] + \mathrm{lift}(R,B)
$$

## Step 7: Normalize / recurse if finite exact closure exists

Final first-pass result:

$$
\mathrm{rebase}([V,D,R],B)
=
[Q,B,\; [S,D,0] + \mathrm{lift}(R,B)]
$$

---

# Why this works
This gives you:
- exact quotient extraction
- exact unresolved residual preservation
- exact transport of prior active state
- recursion only in remainder
- finite structure if and only if finite closure exists

It is the natural exact active rebase rule.

---

# What this implies
This is the key test for your whole system:

A target denominator is acceptable only if repeated exact rebasing terminates.

That means not every denominator target is valid for every object in terminating VDR.

And that is exactly what your philosophy requires.

---

# Next best step
Now that active rebasing is defined, the natural next move is to test it on concrete values:
- simple rational cases
- cases that terminate after one active step
- cases that fail because they would recurse forever

That will tell you whether the system is actually workable.

If you want, next I can:
- run worked examples of active rebasing on a few rationals,
- derive a criterion for which target denominators produce finite exact rebase,
- or rewrite the arithmetic axioms cleanly using this active rebase algorithm.

---

