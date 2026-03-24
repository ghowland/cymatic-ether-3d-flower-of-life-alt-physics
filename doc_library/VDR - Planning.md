# VDR
## Implementation Plan v1

This document defines a practical first implementation plan for VDR based on
the current v1 charter, axioms, and reference data model.

Its purpose is not to finish VDR.
Its purpose is to identify the smallest useful implementation path that:
- is faithful to the current formal layer,
- produces executable artifacts,
- supports criticism and testing,
- and can grow without immediate redesign.

The implementation plan assumes:
- exact integers,
- finite tree structure,
- explicit failure,
- raw and normalized forms,
- and external scalar comparison only at the projection boundary.

---

## 1. Implementation Goals

The v1 implementation should aim to produce:

1. a parser for native VDR notation
2. an internal exact data model
3. a validator for raw-valid objects
4. a normalizer for the currently defined normalization layer
5. structural equality
6. value equality via normalization
7. exact closed arithmetic
8. exact closed rebasing
9. exact residual transport (`lift`)
10. active addition and subtraction
11. exact scalar projection:
    - exact rational for closed cases
    - exact recursive scalar form for active cases
12. decimal / float export at requested precision
13. a test suite
14. benchmark scaffolding

This is enough to make VDR executable and inspectable without pretending the
whole long-term theory is finished.

---

## 2. Implementation Strategy

### 2.1. Build the Rational Core First
The first stable executable core should be:

- exact integer support
- raw VDR parsing
- validation
- normalization of closed forms
- structural equality
- value equality
- closed arithmetic
- closed rebasing
- exact rational projection

This creates a trustworthy base before more difficult active mechanics are
added.

---

### 2.2. Add Native Active Structure Second
Once the rational core is stable, add:

- active object parsing
- residual validation
- recursive tree traversal
- residual negation
- same-denominator active addition/subtraction
- active projection by exact recursive comparison form

This makes active VDR usable even before all optimization layers are settled.

---

### 2.3. Add Rebase / Lift / Normalization Refinements Third
After active structure works, add:

- active rebasing
- residual transport (`lift`)
- active normalization policies
- same-denominator child absorption where operationally defined
- canonical child ordering
- exact symbolic scalar output

This stage is where semantic correctness must be checked carefully.

---

### 2.4. Benchmark and Compare Fourth
Only after the core executes reliably should benchmarking begin.

Benchmarking should compare:
- scalar-only pipelines
- VDR internal exact computation plus final scalar export

especially on long operation chains where drift matters.

---

## 3. Suggested Language Split

### 3.1. Python Reference Implementation
Python is recommended first for:
- speed of iteration
- exact integer support
- symbolic recursion
- parser experimentation
- test harnesses
- benchmark scripting
- quick paper examples

The Python version should be the truth-first reference implementation.

---

### 3.2. Zig Systems Implementation
Zig is recommended second for:
- explicit memory control
- serialization discipline
- performance investigation
- strong systems-level library packaging
- future production-oriented experimentation

The Zig version should follow the Python reference, not precede it.

---

## 4. Recommended Repository Structure

```text
vdr/
  charter/
    VDR_Charter.md
  spec/
    foundational_axioms_v1.md
    residual_rules_v1.md
    structural_equality_validity_v1.md
    native_semantics_v1.md
    normalization_v1.md
    value_equality_v1.md
    scalar_projection_v1.md
    minimal_arithmetic_v1.md
    closed_rebase_v1.md
    active_rebase_v1.md
    lift_v1.md
    completion_semantics_v1.md
    active_scalar_projection_v1.md
    active_arithmetic_v1.md
    inbound_construction_v1.md
    supported_domain_examples_v1.md
    reference_data_model_v1.md
    implementation_plan_v1.md
  python/
    vdr/
      model.py
      validate.py
      normalize.py
      equality.py
      project.py
      arithmetic.py
      rebase.py
      lift.py
      parse.py
      serialize.py
      errors.py
    tests/
    benchmarks/
  zig/
    src/
    tests/
  examples/
  papers/
```

This keeps:
- spec,
- reference implementation,
- examples,
- and publication materials
separate but aligned.

---

## 5. Python Module Plan

### 5.1. `model.py`
Defines:
- VDR node type
- residual type
- constructors
- exact invariants where possible

---

### 5.2. `errors.py`
Defines explicit failure categories, such as:
- invalid structure
- zero denominator
- unsupported in v1
- normalization failure
- projection failure
- arithmetic failure
- rebase impossible

---

### 5.3. `validate.py`
Implements:
- raw validity checking
- residual validity checking
- finiteness
- recursion locality
- denominator nonzero enforcement

Primary functions:

```python
validate_vdr(x)
validate_residual(r)
```

---

### 5.4. `normalize.py`
Implements:
- sign normalization
- closed gcd reduction
- residual atomic consolidation
- child ordering
- currently defined active canonicalization steps

Primary functions:

```python
normalize(x)
normalize_residual(r)
```

---

### 5.5. `equality.py`
Implements:
- structural equality
- value equality via normalization

Primary functions:

```python
structural_equal(x, y)
value_equal(x, y)
```

---

### 5.6. `project.py`
Implements:
- closed rational projection
- active exact scalar comparison form
- decimal / float export wrappers

Primary functions:

```python
project_closed(x)
project_exact(x)
project_decimal(x, precision)
project_float(x, format_spec)
```

---

### 5.7. `arithmetic.py`
Implements:
- closed add/sub/mul/div
- active add/sub
- negation
- later provisional hooks for active mul/div

Primary functions:

```python
add(x, y)
sub(x, y)
mul(x, y)
div(x, y)
neg(x)
```

---

### 5.8. `rebase.py`
Implements:
- closed rebase
- active rebase
- target denominator checks

Primary functions:

```python
rebase(x, target_d)
rebase_closed(x, target_d)
rebase_active(x, target_d)
```

---

### 5.9. `lift.py`
Implements:
- residual transport
- child transport
- composition and sign behavior

Primary functions:

```python
lift_residual(r, k)
lift_vdr(x, k)
```

---

### 5.10. `parse.py`
Implements:
- parser for bracket notation
- residual parsing
- tree construction
- syntax errors

Example accepted input:

```text
[1,2,0]
[1,2,1+[1,3,0]]
```

---

### 5.11. `serialize.py`
Implements:
- raw serializer
- normalized serializer
- canonical serializer for hashing / fixtures

Primary functions:

```python
to_text(x)
to_canonical_text(x)
to_json(x)
from_json(obj)
```

---

## 6. Data Representation Choices

### 6.1. Exact Integer Type
Use Python `int` as the exact integer base in the reference implementation.

This matches:
- arbitrary precision
- exactness
- zero-denominator checks
- gcd normalization

---

### 6.2. Residual Internal Representation
Strong recommendation:
internally store residuals in canonical composite shape:

```python
Residual(base: int, children: list[VDR])
```

with atomic residuals represented as:
- `base = r`
- `children = []`

This simplifies:
- normalization
- equality
- arithmetic combination
- projection
- serialization

Even if the parser accepts the lighter atomic notation.

---

### 6.3. Exact Scalar Comparison Representation
Use an external exact comparison type rather than collapsing immediately to
float.

Possible Python forms:
- `fractions.Fraction` for exact rational collapses
- custom symbolic tree for exact active projection where needed

Recommendation:
define a small custom exact scalar expression type even if many cases reduce
to `Fraction`.

---

## 7. Phased Milestones

### Milestone 1. Parser + Validator
Deliver:
- parser
- data model
- raw validity checks
- test cases for good/bad objects

Success condition:
- can read and validate all current supported-domain examples

---

### Milestone 2. Closed Core
Deliver:
- closed normalization
- structural equality
- value equality
- closed arithmetic
- closed projection
- closed rebasing

Success condition:
- exact agreement with rational arithmetic on a large closed test corpus

---

### Milestone 3. Active Structural Core
Deliver:
- active object support
- residual negation
- same-denominator active add/sub
- recursive exact projection
- basic active normalization

Success condition:
- active examples parse, normalize, and project deterministically

---

### Milestone 4. Rebase + Lift
Deliver:
- active rebase
- residual transport
- compatibility tests with projection semantics

Success condition:
- rebased objects project compatibly with source objects on supported cases

---

### Milestone 5. Export Layer
Deliver:
- exact scalar comparison output
- decimal export at chosen precision
- float export adapters

Success condition:
- VDR results can be benchmarked against scalar-only pipelines

---

### Milestone 6. Benchmarks
Deliver:
- long-chain arithmetic benchmark tasks
- drift comparison tasks
- reversible-operation tasks
- scalar vs VDR comparison reports

Success condition:
- identify at least some nontrivial task class where VDR shows a practical
  advantage worth reporting

---

## 8. Testing Plan

### 8.1. Validation Tests
Test:
- valid closed forms
- valid active forms
- invalid denominator-zero forms
- invalid infinite / malformed syntax
- invalid residual structures

---

### 8.2. Equality Tests
Test:
- structural equality exact match
- normalized equality on reduced closed forms
- child-order normalization cases
- sign normalization cases

---

### 8.3. Closed Arithmetic Tests
Test exact agreement with rational arithmetic for:
- addition
- subtraction
- multiplication
- division
- identity laws
- inverse laws

---

### 8.4. Rebase Tests
Test:
- successful closed rebase
- failed closed rebase
- active rebase preservation on supported examples
- compatibility of rebase with exact projection

---

### 8.5. Projection Tests
Test:
- exact closed rational projection
- active exact recursive projection
- decimal export consistency at chosen precision

---

### 8.6. Property Tests
Where practical, use randomized property tests for closed core laws:
- commutativity
- associativity
- distributivity
- normalization idempotence
- projection compatibility

---

## 9. Benchmark Plan Hooks

The implementation should include benchmark hooks for later tasks such as:
- repeated multiply/divide chains
- repeated add/subtract cancellation chains
- rebasing-heavy workloads
- scalar drift comparison after final export
- “return to start” operation loops

These need not be solved in v1, but the implementation should make them easy
to add.

---

## 10. Publication Readiness Criteria

The implementation is ready to support a first paper / release when all of
the following are true:

1. parser and validator are stable
2. closed core is exact and tested
3. active projection is implemented in its current v1 scope
4. active add/sub and rebasing are implemented in current v1 scope
5. failure cases are explicit
6. examples are reproducible
7. benchmark scaffolding exists
8. claims are clearly separated into:
   - implemented
   - specified
   - provisional
   - aspirational

---

## 11. Immediate Build Order

If starting now, the recommended exact order is:

1. `model.py`
2. `errors.py`
3. `validate.py`
4. `parse.py`
5. `serialize.py`
6. `normalize.py`
7. `equality.py`
8. `project.py` for closed cases
9. `arithmetic.py` for closed cases
10. `rebase.py` for closed cases
11. active projection
12. active add/sub
13. `lift.py`
14. active rebasing
15. decimal / float export
16. benchmarks

This minimizes confusion and gives a working exact rational core quickly.

---

## 12. Summary

Implementation Plan v1 gives a practical route from theory to executable VDR:

- build the exact rational core first
- extend to active structure second
- add rebase/lift/active semantics third
- benchmark only after correctness stabilizes

This matches the charter:
- exactness first
- utility later
- explicit failure over false completion
- interoperability at the boundary

This is enough to begin writing the first Python reference library now.

Next likely step is one of:

1. Paper Outline v1
2. Benchmark Plan v1
3. Canonical Quotient Selection Rules v1
4. Python Reference Skeleton v1

My recommendation:
Benchmark Plan v1 next, because your charter treats practical utility as a
hard test of whether VDR matters.

---

# VDR
## Benchmark Plan v1

This document defines the first benchmark plan for VDR.

At v1, benchmarking is not about speed.
It is about:
- correctness,
- exactness preservation,
- drift resistance,
- interoperability,
- and practical usefulness relative to approximation-dominant scalar methods.

Performance benchmarking is explicitly deferred to a later stage.

The purpose of the v1 benchmark plan is to answer:

- Does VDR preserve exact structure where scalar pipelines lose it?
- Does VDR export better final scalar results on some important long-chain
  tasks?
- Does VDR recover equality where scalar approximation only gives tolerance?
- Are the current v1 rules coherent enough to survive repeated use?

---

## 1. Benchmark Principles

### 1.1. Correctness First
The primary benchmark standard for v1 is correctness, not speed.

A slower method that preserves exactness is preferable to a faster method that
silently drifts, truncates, or collapses structure incorrectly.

---

### 1.2. Exact Internal / Approximate Boundary Rule
Benchmarks must distinguish between:
- exact internal VDR computation,
- and approximate external scalar rendering.

Approximation is permitted only at the export boundary when the target scalar
system requires it.

---

### 1.3. Comparable Output Rule
To compare VDR with conventional scalar pipelines, the final outputs must be
rendered into a shared comparison form.

At v1, this means one or more of:
- exact rational comparison where possible
- exact symbolic comparison form where possible
- decimal output at specified precision
- float output in fixed format

Comparison must always specify:
- the target format
- the precision used
- and whether loss is target-imposed

---

### 1.4. Long-Chain Priority Rule
VDR’s practical benchmark value is expected to appear most strongly in long
operation chains rather than one-step convenience cases.

Therefore, v1 benchmark design prioritizes:
- repeated operations,
- reversible chains,
- cancellation chains,
- rebasing-heavy chains,
- and situations where scalar drift accumulates.

---

### 1.5. Honest Failure Rule
If VDR cannot yet perform a benchmark exactly within v1 scope, this must be
recorded explicitly as:
- unsupported,
- deferred,
- or failed.

No benchmark result may be rescued by silently substituting approximation for
missing exact VDR behavior.

---

## 2. Benchmark Categories

### 2.1. Closed Correctness Benchmarks
Purpose:
- verify the exact rational core

Tasks:
- closed addition
- closed subtraction
- closed multiplication
- closed division
- closed rebasing
- normalization consistency
- projection consistency

Reference comparison:
- exact rational arithmetic

Success condition:
- exact agreement in all supported cases

---

### 2.2. Active Structural Correctness Benchmarks
Purpose:
- verify active object handling without collapsing native structure

Tasks:
- parse active objects
- validate active objects
- normalize active objects
- compare structural equality
- compare value equality where defined
- preserve child structure under lift and rebase

Success condition:
- deterministic exact behavior with no invalid collapse

---

### 2.3. Active Projection Benchmarks
Purpose:
- verify denominator-sensitive completion semantics

Tasks:
- project active objects recursively
- compare active rebased forms against source forms
- verify same projected scalar meaning on exact supported examples
- verify projection determinism

Success condition:
- exact recursive projection compatibility on supported examples

---

### 2.4. Equality Recovery Benchmarks
Purpose:
- test whether VDR recovers exact equality in cases where scalar workflows
  normally use tolerance

Tasks:
- normalize equivalent closed forms
- compare raw-distinct but normalized-equal VDR forms
- repeated operation chains returning exactly to origin
- same-denominator absorption cases when implemented

Success condition:
- exact equality is recovered internally without epsilon tests

---

### 2.5. Drift Resistance Benchmarks
Purpose:
- test whether VDR internal exactness yields better final exported scalar
  results after many operations

Tasks:
- repeated reversible operation loops
- repeated cancellation chains
- repeated multiply/divide inverses
- repeated rebase / unrebase chains
- mixed active/closed long chains within supported scope

Reference comparison:
- decimal or float-only pipelines performing analogous operations directly

Success condition:
- VDR final export shows less drift on at least some nontrivial task classes

---

### 2.6. Interoperability Benchmarks
Purpose:
- verify that VDR can meet the scalar world at the boundary

Tasks:
- exact rational inbound / outbound roundtrips
- active exact projection to exact external comparison form
- decimal export at chosen precisions
- float export with specified formats
- stability of serialization / parsing / normalization pipelines

Success condition:
- deterministic and inspectable boundary behavior

---

## 3. Benchmark Task Families

### 3.1. Rational Roundtrip Family
Examples:
- admit rational
- project rational
- normalize
- compare against original exact rational

Cases:
- \(1/2\)
- \(-3/7\)
- \(22/7\)
- large numerators / denominators

Purpose:
- establish baseline exactness

---

### 3.2. Closed Return-to-Origin Family
Examples:
- start with \(x\)
- add \(a\), subtract \(a\)
- multiply by \(b\), divide by \(b\)
- rebase to \(kD\), rebase back to \(D\)

Expected result:
- exact return to original VDR value under value equality

Scalar comparison:
- float/decimal versions will often drift or require tolerance

Purpose:
- expose exact equality recovery

---

### 3.3. Long Cancellation Family
Examples:
- repeated additions and subtractions designed to telescope
- chains with large denominator growth and later collapse
- alternating inverse operations

Expected result:
- exact VDR recovery at end
- scalar pipelines may accumulate error

Purpose:
- test long-chain exactness

---

### 3.4. Rebase Stress Family
Examples:
- repeated denominator changes among compatible targets
- successful / failed closed rebases
- active rebases followed by projection checks
- lift-supported rebasing chains

Expected result:
- value-preserving rebasing where defined
- explicit failure where not defined
- no silent approximation

Purpose:
- test denominator-sensitive mechanics

---

### 3.5. Active Projection Equivalence Family
Examples:
- source active object and rebased active object
- project both
- compare exact scalar comparison forms

Expected result:
- exact agreement of projection where semantics require it

Purpose:
- verify active rebase correctness

---

### 3.6. Mixed Exact-to-Approximate Export Family
Examples:
- exact VDR chain done internally
- final decimal export at precision \(p\)
- compare to scalar-only decimal chain done natively

Expected result:
- VDR export should be more stable on some selected long-chain cases

Purpose:
- test practical utility at the scalar boundary

---

## 4. Benchmark Metrics

At v1, metrics should be correctness-oriented.

### 4.1. Exact Agreement Metric
For exact domains:
- pass if structural or value-equality condition is met exactly
- fail otherwise

Used for:
- closed arithmetic
- normalization
- equality
- exact projection

---

### 4.2. Drift Metric
For approximate boundary comparisons:
measure:
- absolute error
- relative error
- return-to-origin deviation
- deviation after \(N\) operations

Used for:
- decimal export benchmarks
- float export benchmarks
- long-chain comparison tasks

---

### 4.3. Failure Honesty Metric
Count:
- successful exact cases
- explicit unsupported cases
- explicit failures
- silent mismatches

Success requires:
- no silent mismatch accepted as valid exactness

---

### 4.4. Determinism Metric
Run the same benchmark multiple times and verify:
- same normalized VDR output
- same exact projection output
- same decimal/float export under fixed settings

Used for:
- parser
- normalization
- projection
- rebasing
- arithmetic

---

## 5. Reference Comparison Systems

VDR should be compared against:

1. exact rational arithmetic for closed-core truth checking
2. decimal arithmetic at fixed precision
3. binary floating-point arithmetic at fixed format
4. optional symbolic comparison systems for exact scalar forms

At v1, the most important comparison is:
- VDR exact internal result versus decimal/float drift after long chains

---

## 6. Minimum Benchmark Set for v1

A minimal publishable benchmark set should include:

1. closed rational arithmetic correctness
2. closed rebase correctness
3. normalization + value equality tests
4. active projection correctness on selected examples
5. return-to-origin chains
6. repeated cancellation chains
7. at least one long-chain export comparison showing less scalar drift from VDR

This is enough to support a first serious claim of practical promise.

---

## 7. Benchmark Reporting Format

Each benchmark report should include:

- benchmark name
- category
- exact input
- VDR internal result
- normalized result
- exact scalar comparison form if available
- decimal / float export format if used
- scalar-only comparison pipeline
- operation count
- outcome:
  - exact pass
  - export advantage
  - unsupported
  - failure

This makes every benchmark inspectable and reproducible.

---

## 8. Deferred Benchmark Areas

The following are explicitly deferred beyond v1:

- runtime performance benchmarking
- memory usage benchmarking
- large-scale asymptotic optimization
- transcendental constant derivation benchmarks
- CODATA-level scientific constant derivation benchmarks
- hardware-level numerical comparisons

These are important later, but not part of correctness-first benchmarking.

---

## 9. v1 Success Threshold

The benchmark plan should be considered successful at v1 if it shows all of
the following:

1. the closed core is exactly correct
2. active projection is semantically coherent on supported examples
3. exact equality recovery works internally where defined
4. failures are explicit rather than approximate
5. at least one meaningful long-chain benchmark shows a practical boundary
   advantage over approximation-dominant scalar computation

This does not prove final VDR success.
It proves that VDR is worth taking seriously.

---

## 10. Summary

Benchmark Plan v1 is correctness-first.

It does not ask:
- “is VDR faster?”

It asks:
- “is VDR exact where it claims to be exact?”
- “does it preserve equality where scalar pipelines drift?”
- “can it export useful scalar results after long exact internal work?”
- “does it justify continued development?”

That is the right benchmark standard for the current stage of VDR.

---

# VDR
## Paper Outline v1

This document gives the first paper outline for presenting VDR as a formal
program.

It is intended for:
- a Zenodo paper,
- early external review,
- implementation-aligned documentation,
- and future revision into a stronger formal publication.

The purpose of the v1 paper is not to claim final completion.
Its purpose is to present:
- the charter,
- the foundational system,
- the current exact core,
- the open frontier,
- and the standards by which VDR should be judged.

This outline is written for a serious but early-stage mathematical paper.

---

## Proposed Title

Possible title options:

1. VDR: A Finite Exact Triple-Structured Framework for Discrete Value
   Representation
2. VDR: A Charter and v1 Formal Core for Exact Finite Representation Beyond
   Approximation
3. VDR: Exact Triple-Structured Representation with Finite Residual
   Completion
4. VDR: A Pure-Mathematics Program for Exact Finite Discrete Representation

Recommended v1 title:

VDR: A Charter and v1 Formal Core for Exact Finite Discrete Representation

---

## Proposed Abstract

This paper introduces VDR, a pure-mathematics program for exact finite
discrete representation in irreducible triple form. VDR is motivated by the
loss of exact equality that occurs when mathematical and scientific practice
depends on approximation-dominant scalar systems such as floating-point,
decimal truncation, and limit-based representations. VDR treats exact
value-bearing residual structure as primary rather than discardable, and
defines a native domain of finite triple-structured objects with exact
recursive completion.

This v1 paper presents the VDR charter, foundational axioms, residual
formation rules, structural validity, normalization, internal equality,
scalar projection, exact closed arithmetic, first-pass active rebasing and
transport, inbound construction for the rational core, and a reference data
model for implementation. The paper does not claim final completion of VDR’s
long-term ambitions, such as exact admission of transcendental constants or
full replacement of practical real-number roles. Instead, it establishes a
coherent exact finite core, identifies the open research frontier, and gives
correctness-first implementation and benchmarking plans.

---

## Section-by-Section Outline

### 1. Introduction
Purpose:
- introduce the problem VDR addresses
- state why a new exact finite framework is being attempted
- set expectations honestly

Key points:
- approximation-dominant scalar practice is useful but loses exact equality
- VDR is not just a new notation for fractions
- VDR is a finite exact triple-structured representation program
- this paper presents the charter and v1 formal core, not a final theory

Possible subsection:
- 1.1 Why VDR exists
- 1.2 What this paper does and does not claim

---

### 2. Motivation and Problem Statement
Purpose:
- explain the practical and conceptual motivation without overstating final
  claims

Key points:
- loss of equality under approximation
- hidden drift across long computation chains
- scalar systems compress structure for utility, but at a cost
- VDR seeks to preserve exact residual structure rather than discard it

Possible subsection:
- 2.1 Equality versus approximation
- 2.2 Why finite exact structure matters
- 2.3 Why triple irreducibility matters

---

### 3. Charter of VDR
Purpose:
- present the governing charter clearly before technical rules

Contents:
- purpose
- scope
- foundational principles
- interoperability requirements
- success criteria / practical validation tests
- research ambitions
- completeness horizon
- practical standard of judgment

This section should likely appear almost verbatim from the charter document,
lightly polished for paper form.

---

### 4. Foundational Formal Layer
Purpose:
- define what a VDR object is at the most basic level

Contents:
- primitive object axiom
- triple irreducibility
- integer slot constraints
- residual locality
- finite structure
- exactness
- inspectability
- admissibility

This is the first formal definition section.

---

### 5. Residual Formation and Structural Validity
Purpose:
- define admissible residuals and raw-valid objects

Contents:
- residual domain
- atomic and composite residuals
- recursive child validity
- raw validity
- finite whole-object validity
- structural equality

This section gives the formal syntax and validity layer.

---

### 6. Native Semantics
Purpose:
- explain what VDR means natively before any scalar comparison

Contents:
- native object rule
- triple-state semantics
- residual significance
- active versus closed distinction
- global closure
- residual as completion structure
- no native scalar collapse

This is where the paper makes clear that VDR is not internally just rational
arithmetic with annotations.

---

### 7. Normalization and Internal Equality
Purpose:
- define canonical form and the first non-structural equality relation

Contents:
- normalization rules
- sign placement
- closed reduction
- residual consolidation
- canonical child order
- same-denominator absorption policy
- value equality via normalization

This section should distinguish carefully:
- structural equality
- value equality

---

### 8. Scalar Projection and Interoperability
Purpose:
- define how VDR meets conventional scalar mathematics externally

Contents:
- projection externality
- closed scalar projection
- denominator-sensitive completion semantics
- active scalar projection
- exact versus approximate export
- projection determinism
- structural distinctness despite equal projection

This section is critical because it explains how VDR is validated against the
existing scalar world without collapsing into it.

---

### 9. Exact Rational Core
Purpose:
- present the fully workable current exact core

Contents:
- closed arithmetic
- closed rebasing
- rational inbound construction
- rational projection compatibility
- exact closed examples

This is likely the strongest currently mature part of the paper.

---

### 10. First-Pass Active Layer
Purpose:
- present the current active structure honestly, without overstating maturity

Contents:
- active rebasing
- residual transport / lift
- denominator-sensitive completion
- active scalar projection
- active addition and subtraction
- semantic constraints on multiplication and division
- explicit failure for unsupported exact constructions

This section should explicitly mark:
- what is formal,
- what is provisional,
- what is deferred.

---

### 11. Supported Domain Examples
Purpose:
- clarify current boundary of the system by examples rather than universal
  claims

Contents:
- clearly in scope
- clearly out of scope
- open / unresolved
- working scope summary

This section is important for honesty and reader orientation.

---

### 12. Reference Data Model and Implementation Path
Purpose:
- show that the system is not merely philosophical; it is implementable

Contents:
- reference data model
- tree structure
- exact integer requirement
- parser / serializer strategy
- module plan
- implementation milestones

This section makes the work legible to programmers and computational
mathematicians.

---

### 13. Benchmark Plan
Purpose:
- define how VDR should be judged in the current stage

Contents:
- correctness-first benchmark philosophy
- exactness tests
- equality recovery tests
- drift resistance tests
- boundary export tests
- deferred performance benchmarking

This section is crucial for avoiding vague claims of usefulness.

---

### 14. Open Problems and Research Frontier
Purpose:
- state clearly what is not solved yet

Contents:
- exact admission of algebraic irrationals
- exact admission of transcendental constants
- full active multiplication/division
- canonical quotient selection
- broader admitted target class
- long-term scientific ceiling

This section protects the paper from overclaiming.

---

### 15. Discussion
Purpose:
- interpret the significance of the work without overstating proof of success

Key themes:
- VDR as exact finite alternative, not yet replacement
- difference between native identity and scalar comparison
- tradeoff between elegance and exactness
- possible future value if long-chain utility is confirmed
- what failure would still teach

---

### 16. Conclusion
Purpose:
- close with a clear statement of what has been achieved

Key points:
- VDR now has a charter and a coherent v1 formal core
- the rational closed core is exact and implementable
- the active layer is structurally and semantically framed, though not final
- the project is now concrete enough for implementation, criticism, and
  benchmark testing

---

## Suggested Appendices

### Appendix A. Full Axiom Listing v1
Include:
- foundational axioms
- residual rules
- validity and equality rules
- normalization rules
- projection rules
- arithmetic rules
- rebasing and lift rules
- inbound rules

This is useful for serious readers and implementers.

---

### Appendix B. Worked Examples
Include:
- closed arithmetic examples
- normalization examples
- rebase examples
- active projection examples
- direct-specification examples

---

### Appendix C. Example Serialization Forms
Include:
- native text notation
- JSON-like representation
- normalized serialization examples

---

### Appendix D. Benchmark Fixture Set
Include:
- small exact fixtures
- long-chain fixtures
- return-to-origin examples
- active projection check cases

---

## Recommended Order of Writing

To produce the paper efficiently, write in this order:

1. Charter
2. Foundational formal layer
3. Rational closed core
4. Scalar projection section
5. Active semantic layer
6. Supported domain examples
7. Data model / implementation section
8. Benchmark section
9. Open problems
10. Introduction and conclusion last

This reduces revision churn.

---

## Tone Guidance for the Paper

The paper should be:
- exact
- careful
- explicit about what is solved and unsolved
- resistant to overclaiming
- implementation-aware
- open to falsification

Avoid:
- claiming universal success too early
- treating ambitions as theorems
- overstating physics implications
- implying all reals are already solved

Prefer:
- “v1 formal core”
- “current exact rational core”
- “active layer provisional but structured”
- “open research boundary”
- “benchmark-driven practical evaluation”

---

## Minimal Publishable Claim

The v1 paper can safely claim:

- a coherent charter for an exact finite representation program
- a formal triple-structured object model
- exact finite structural validity and equality
- an exact rational closed core with arithmetic and rebasing
- denominator-sensitive active semantics and projection at a first-pass level
- a reference implementation path
- a correctness-first benchmark plan
- an explicit open frontier rather than false completion

That is enough for a serious early paper.

---

## Summary

Paper Outline v1 gives a clear path to a first public VDR paper that is:
- mathematically honest
- technically structured
- implementation-aware
- and ambitious without pretending completion

It should be strong enough for:
- Zenodo publication
- code-linked documentation
- external criticism
- and future refinement

---

# VDR
## Worked Examples v1

This document collects worked examples for the current v1 formal layer.

Its purpose is to make the system inspectable through concrete cases rather
than abstract rules alone.

These examples are chosen to illustrate:
- raw validity,
- normalization,
- structural equality,
- value equality,
- closed arithmetic,
- closed rebasing,
- active specification,
- denominator-sensitive completion,
- active scalar projection,
- active rebasing,
- and exact failure cases.

These are v1 examples only.
They do not claim that all future VDR behavior is settled.

---

## 1. Closed Object Examples

### Example 1.1. Simple closed rational
Object:

$$
[1,2,0]
$$

Interpretation status:
- raw-valid
- closed
- already normalized under standard sign convention
- exact rational projection:

$$
\Pi([1,2,0]) = \frac{1}{2}
$$

---

### Example 1.2. Non-normal closed rational
Object:

$$
[2,4,0]
$$

Status:
- raw-valid
- closed
- not normalized

Normalization:

$$
[2,4,0] \mapsto [1,2,0]
$$

So:
- structurally distinct from \([1,2,0]\)
- but value-equal after normalization

---

### Example 1.3. Negative denominator
Object:

$$
[1,-2,0]
$$

Status:
- raw-valid
- closed
- not normalized if denominator-positive convention is chosen

Normalization:

$$
[1,-2,0] \mapsto [-1,2,0]
$$

So:
- negative denominators are valid
- sign normalization is canonicality, not validity

---

## 2. Structural Equality and Value Equality

### Example 2.1. Structural equality
Compare:

$$
X = [1,2,0]
$$

$$
Y = [1,2,0]
$$

Since all slots match exactly,

$$
X \equiv_s Y
$$

Therefore also:

$$
X \equiv_v Y
$$

---

### Example 2.2. Structural inequality but value equality
Compare:

$$
X = [2,4,0]
$$

$$
Y = [1,2,0]
$$

They are not structurally equal:

$$
X \not\equiv_s Y
$$

But normalization gives:

$$
\mathrm{norm}(X) = [1,2,0]
$$

$$
\mathrm{norm}(Y) = [1,2,0]
$$

So:

$$
X \equiv_v Y
$$

---

### Example 2.3. Child order structural difference
Compare:

$$
X = [1,2,1 + [1,3,0] + [1,5,0]]
$$

$$
Y = [1,2,1 + [1,5,0] + [1,3,0]]
$$

As written:
- child order differs
- so structural equality fails

$$
X \not\equiv_s Y
$$

If normalization sorts children canonically, then they may become
value-equal.

---

## 3. Closed Arithmetic Examples

### Example 3.1. Closed addition
Compute:

$$
[1,2,0] + [1,3,0]
$$

By closed addition rule:

$$
[1\cdot 3 + 1\cdot 2,\; 2\cdot 3,\; 0]
=
[5,6,0]
$$

Projection check:

$$
\frac{1}{2} + \frac{1}{3} = \frac{5}{6}
$$

So:

$$
[1,2,0] + [1,3,0] = [5,6,0]
$$

---

### Example 3.2. Closed subtraction
Compute:

$$
[3,4,0] - [1,2,0]
$$

By closed subtraction rule:

$$
[3\cdot 2 - 1\cdot 4,\; 4\cdot 2,\; 0]
=
[2,8,0]
$$

Normalize:

$$
[2,8,0] \mapsto [1,4,0]
$$

So the exact result is value-equal to:

$$
[1,4,0]
$$

---

### Example 3.3. Closed multiplication
Compute:

$$
[2,3,0] \times [3,5,0]
$$

By closed multiplication rule:

$$
[2\cdot 3,\; 3\cdot 5,\; 0]
=
[6,15,0]
$$

Normalize:

$$
[6,15,0] \mapsto [2,5,0]
$$

---

### Example 3.4. Closed division
Compute:

$$
[2,3,0] \div [4,5,0]
$$

By closed division rule:

$$
[2\cdot 5,\; 3\cdot 4,\; 0]
=
[10,12,0]
$$

Normalize:

$$
[10,12,0] \mapsto [5,6,0]
$$

---

### Example 3.5. Division by closed zero fails
Attempt:

$$
[1,2,0] \div [0,7,0]
$$

Since the divisor is closed zero, division is invalid.

Result:
- explicit failure
- no approximation rescue

---

## 4. Closed Rebasing Examples

### Example 4.1. Successful closed rebase
Rebase:

$$
[1,2,0]
$$

to denominator:

$$
4
$$

Check:

$$
\frac{1\cdot 4}{2} = 2 \in \mathbb{Z}
$$

So rebasing succeeds:

$$
\mathrm{rebase}([1,2,0],4) = [2,4,0]
$$

Normalize if desired:

$$
[2,4,0] \mapsto [1,2,0]
$$

So rebasing changes representation, not value.

---

### Example 4.2. Failed closed rebase
Rebase:

$$
[1,2,0]
$$

to denominator:

$$
3
$$

Check:

$$
\frac{1\cdot 3}{2} = \frac{3}{2} \notin \mathbb{Z}
$$

So closed rebasing fails at v1.

This is exactly the case that motivates active rebasing.

---

## 5. Active Specification Examples

### Example 5.1. Atomic active object
Object:

$$
[3,5,1]
$$

Status:
- raw-valid
- active
- residual is atomic integer \(1\)

Under denominator-sensitive projection:

$$
\Pi([3,5,1]) = \frac{3+1}{5} = \frac{4}{5}
$$

---

### Example 5.2. Active object with closed child
Object:

$$
[1,2,[1,3,0]]
$$

Status:
- raw-valid
- active
- residual contains one child VDR

Projection:

$$
\Pi([1,3,0]) = \frac{1}{3}
$$

Then by parent-sensitive completion:

$$
\Pi([1,2,[1,3,0]]) = \frac{1 + 1/3}{2}
$$

$$
= \frac{4/3}{2}
= \frac{2}{3}
$$

This is a key example:
the child contributes inside the parent denominator frame.

---

### Example 5.3. Composite active object
Object:

$$
[2,5,1 + [1,4,0] + [1,2,0]]
$$

Projection pieces:

$$
\Pi([1,4,0]) = \frac{1}{4}
$$

$$
\Pi([1,2,0]) = \frac{1}{2}
$$

So residual completion is:

$$
\rho_5(R) = 1 + \frac{1}{4} + \frac{1}{2}
= \frac{7}{4}
$$

Then:

$$
\Pi([2,5,R]) = \frac{2 + 7/4}{5}
= \frac{15/4}{5}
= \frac{3}{4}
$$

---

## 6. Active Rebase Examples

### Example 6.1. Closed-to-active rebase motivation
Start with:

$$
[1,2,0]
$$

Target denominator:

$$
3
$$

Closed rebase fails.

So use active rebasing.

Compute:

$$
N = VB = 1\cdot 3 = 3
$$

Divide by original denominator \(D=2\):

$$
3 = 1\cdot 2 + 1
$$

So:
- \(Q = 1\)
- \(S = 1\)

Construct active rebased form:

$$
[1,3,[1,2,0]]
$$

Projection check:

$$
\Pi([1,3,[1,2,0]])
=
\frac{1 + 1/2}{3}
=
\frac{3/2}{3}
=
\frac{1}{2}
$$

So the active rebased object projects exactly to the original value.

This is the core example showing why denominator-sensitive completion matters.

---

### Example 6.2. Active rebase with existing residual
Start with:

$$
[2,5,1]
$$

Target denominator:

$$
3
$$

Compute top-level mismatch:

$$
N = 2\cdot 3 = 6
$$

Divide by original denominator \(5\):

$$
6 = 1\cdot 5 + 1
$$

So:
- \(Q = 1\)
- \(S = 1\)

First-pass rebased form:

$$
[1,3,[1,5,0] + 1]
$$

This is still provisional and may later normalize more elegantly.

Projection check:

Residual completion:

$$
\rho_3([1,5,0] + 1) = \frac{1}{5} + 1 = \frac{6}{5}
$$

Then:

$$
\Pi([1,3,[1,5,0] + 1]) = \frac{1 + 6/5}{3}
= \frac{11/5}{3}
= \frac{11}{15}
$$

Original projection:

$$
\Pi([2,5,1]) = \frac{2+1}{5} = \frac{3}{5}
$$

These are not equal.

This example shows that first-pass active residual preservation without a full
transport adjustment can fail to preserve projection.

This is important and should be documented honestly:
- v1 active rebase idea is motivated
- but full correctness for existing residual transport needs the lift /
  denominator-sensitive machinery refined carefully

This is not a defect in the example.
It is exactly the kind of worked case that reveals where the theory still
needs repair.

---

## 7. Lift Examples

### Example 7.1. Atomic lift
Lift residual:

$$
1
$$

by factor:

$$
3
$$

Then:

$$
\mathrm{lift}(1,3) = 3
$$

---

### Example 7.2. Child lift
Lift child:

$$
[1,3,0]
$$

by factor:

$$
2
$$

Then:

$$
\mathrm{lift}([1,3,0],2) = [2,3,0]
$$

Projection of original child:

$$
\frac{1}{3}
$$

Projection of lifted child:

$$
\frac{2}{3}
$$

This matches the intended scaling of child contribution before insertion into a
new parent frame.

---

### Example 7.3. Composite residual lift
Lift:

$$
1 + [1,3,0]
$$

by factor:

$$
2
$$

Then:

$$
\mathrm{lift}(1 + [1,3,0],2)
=
2 + [2,3,0]
$$

This is exact structural transport.

---

## 8. Equality Recovery Examples

### Example 8.1. Return to origin under closed arithmetic
Start with:

$$
X = [1,2,0]
$$

Add:

$$
[1,3,0]
$$

then subtract:

$$
[1,3,0]
$$

By exact closed arithmetic, the final result is value-equal to:

$$
[1,2,0]
$$

No epsilon test is needed.

---

### Example 8.2. Multiply and divide return
Start with:

$$
X = [3,7,0]
$$

Multiply by:

$$
[5,2,0]
$$

then divide by:

$$
[5,2,0]
$$

The final normalized result is value-equal to:

$$
[3,7,0]
$$

This is the kind of exact return scalar pipelines often only approximate.

---

## 9. Inbound Construction Examples

### Example 9.1. Integer inbound
Input:

$$
5
$$

Inbound construction:

$$
\mathrm{in}(5) = [5,1,0]
$$

Projection check:

$$
\Pi([5,1,0]) = 5
$$

---

### Example 9.2. Rational inbound
Input:

$$
-\frac{3}{4}
$$

Inbound construction:

$$
\mathrm{in}\!\left(-\frac{3}{4}\right) = [-3,4,0]
$$

Projection check:

$$
\Pi([-3,4,0]) = -\frac{3}{4}
$$

---

### Example 9.3. Approximate decimal rejected as exact admission
Input:
- decimal approximation of \( \pi \), e.g. `3.14159`

At v1:
- this may be represented as an approximate external decimal
- but it is not admitted as an exact VDR representation of \( \pi \)

So exact inbound construction fails unless the intended object is explicitly
the rational decimal value \(314159/100000\).

This is an important boundary example.

---

## 10. Out-of-Scope Example

### Example 10.1. Malformed infinite decimal artifact
Input:

```text
0.3333...751
```

This mixes:
- infinite continuation
- and a final terminal suffix

It lacks a coherent finite exact constructive meaning.

So:
- it is not admitted exactly into v1 VDR
- exact inbound construction fails

---

## 11. Key Lessons from the Worked Examples

These examples show that v1 already has:
- a correct closed rational core,
- exact normalization-based equality,
- exact closed rebasing,
- meaningful active specification,
- denominator-sensitive active projection,
- and exact boundaries against fake exactness.

They also show that:
- active rebasing with preexisting residual structure is not yet fully solved
- transport and rebasing laws still need refinement in nontrivial active cases

This is exactly what worked examples should reveal.

---

## Summary

Worked Examples v1 demonstrates:

1. what already works exactly
2. what is structurally admissible
3. what projects coherently
4. what fails honestly
5. what still needs repair or refinement

This makes VDR inspectable not just as a philosophy or axiom list, but as a
live formal program with a working exact core and a visible frontier.

---

# VDR
## Active Rebase Repair Notes v1

This document records a semantic issue exposed by the current worked examples
for active rebasing.

Its purpose is not to invalidate the VDR program.
Its purpose is to:
- identify the precise failure,
- explain why it occurs,
- preserve what still appears correct,
- and define the repair direction for later formal refinement.

This is a correctness document, not a retreat from the charter.

---

## 1. The Issue Exposed

The current first-pass active rebasing idea works cleanly in the simplest
case:

- source object closed
- target denominator incompatible with closed rebasing
- active child introduced to preserve mismatch

Example:

$$
[1,2,0] \rightsquigarrow [1,3,[1,2,0]]
$$

Under denominator-sensitive completion:

$$
\Pi([1,3,[1,2,0]])
=
\frac{1 + 1/2}{3}
=
\frac{1}{2}
$$

So the simple closed-to-active motivation works.

However, a problem appears when the source object already has residual
structure.

Example source:

$$
[2,5,1]
$$

Projection:

$$
\Pi([2,5,1]) = \frac{2+1}{5} = \frac{3}{5}
$$

Target denominator:

$$
3
$$

First-pass active rebasing produced:

$$
[1,3,[1,5,0] + 1]
$$

But projection gives:

$$
\Pi([1,3,[1,5,0] + 1])
=
\frac{1 + (1/5 + 1)}{3}
=
\frac{11}{15}
$$

which is not equal to:

$$
\frac{3}{5}
=
\frac{9}{15}
$$

So the first-pass rebasing rule fails in this case.

---

## 2. What Failed

The failure is not in:
- the idea of denominator-sensitive completion itself,
- nor in the simple mismatch-child construction for a closed source.

The failure is specifically in the naive preservation of pre-existing residual
structure during rebasing.

The problematic first-pass rule was effectively:

$$
R' = [S,D,0] + R
$$

That treats the old residual as if it could simply be carried unchanged into
the new parent denominator frame.

But under denominator-sensitive semantics, residual meaning depends on the
parent denominator.

So preserving \(R\) unchanged across a denominator change is not generally
correct.

---

## 3. Why It Failed

For:

$$
[V,D,R]
$$

the active projection rule is:

$$
\Pi([V,D,R]) = \frac{V + \rho_D(R)}{D}
$$

If the parent denominator changes from \(D\) to \(B\), then the residual
contribution must be reinterpreted in the new denominator frame.

That means the rebased object:

$$
[Q,B,R']
$$

must satisfy:

$$
\frac{Q + \rho_B(R')}{B}
=
\frac{V + \rho_D(R)}{D}
$$

The old residual \(R\) does not generally satisfy this if inserted unchanged.

So the repair target is:

- not “preserve old residual literally”
- but “construct a new residual whose contribution in the new parent frame
  matches the old total contribution exactly”

This is a stronger and more precise requirement.

---

## 4. What Still Appears Correct

The following parts still appear sound and should be preserved:

### 4.1. Parent-sensitive completion
Residual meaning depends on the parent denominator frame.

This remains the correct semantic direction.

### 4.2. Closed-to-active mismatch preservation
For a closed source:

$$
[V,D,0]
$$

rebased to \(B\), the mismatch construction:

$$
VB = QD + S
\quad\Rightarrow\quad
[Q,B,[S,D,0]]
$$

still projects correctly.

### 4.3. Active rebasing must remain exact
Approximation is still forbidden.
If exact finite active rebasing cannot be constructed, rebasing must fail.

### 4.4. Structural preservation principle
Residual structure remains exact value-bearing structure.
The repair is not permission to discard residuals.
The repair is to transport them correctly.

---

## 5. Correct Repair Direction

The correct repair direction is:

When rebasing:

$$
[V,D,R] \to [Q,B,R']
$$

the rebased residual \(R'\) must satisfy:

$$
\rho_B(R') = \frac{B(V + \rho_D(R))}{D} - Q
$$

in exact external comparison form.

This is the fundamental rebase condition.

So active rebasing must be redefined as a residual reconstruction problem:

1. compute the exact required new parent-frame residual contribution
2. construct a valid finite VDR residual object \(R'\) whose
   denominator-sensitive completion in frame \(B\) equals that contribution
3. fail if no such finite exact residual can be constructed in the current
   layer

This is more precise than the original child-plus-old-residual heuristic.

---

## 6. Consequence for `lift`

The current `lift` rule may still be structurally useful, but it is not by
itself sufficient to guarantee correct active rebasing.

Why:
- `lift` transports structure under scaling assumptions
- but active rebasing requires parent-frame residual equivalence, not merely
  structural carryover

So `lift` should now be treated as:
- a possible helper operation,
- not the full solution to active rebase transport

This is an important correction.

---

## 7. Recommended Formal Change

The current active rebase rule should be weakened.

Instead of saying, in effect:

$$
R' = [S,D,0] + R
$$

it should say:

For rebasing:

$$
[V,D,R] \to [Q,B,R']
$$

the rebased residual \(R'\) must be any valid finite residual object such
that:

$$
\frac{Q + \rho_B(R')}{B}
=
\frac{V + \rho_D(R)}{D}
$$

and such that the rebased object remains raw-valid.

Then:
- closed-to-active mismatch construction becomes one valid special case
- general active rebasing remains exact but no longer falsely overspecified

This is the correct v1 repair.

---

## 8. Example of the Corrected View

Source:

$$
[2,5,1]
$$

Projection:

$$
\Pi([2,5,1]) = \frac{2+1}{5} = \frac{3}{5}
$$

Target denominator:

$$
3
$$

Need rebased form:

$$
[Q,3,R']
$$

such that:

$$
\frac{Q + \rho_3(R')}{3} = \frac{3}{5}
$$

So:

$$
Q + \rho_3(R') = \frac{9}{5}
$$

If we choose \(Q = 1\), then we need:

$$
\rho_3(R') = \frac{4}{5}
$$

One possible exact residual witness is:

$$
R' = [4,5,0]
$$

because:

$$
\rho_3([4,5,0]) = \Pi([4,5,0]) = \frac{4}{5}
$$

Thus a corrected rebased form is:

$$
[1,3,[4,5,0]]
$$

Projection check:

$$
\Pi([1,3,[4,5,0]]) = \frac{1 + 4/5}{3} = \frac{9/5}{3} = \frac{3}{5}
$$

This works.

So the repair note shows:
- the naive carryover rule was wrong
- but exact active rebasing itself remains viable

---

## 9. Practical Implementation Consequence

Implementation should not hard-code the naive rule:

```text
R' = mismatch_child + old_residual
```

Instead, implementation should:
1. compute required residual target contribution in the new parent frame
2. attempt exact residual construction for that target
3. return rebased result if construction succeeds
4. otherwise fail explicitly

This means active rebase now depends on an exact residual-construction helper,
not just literal transport.

---

## 10. Status of v1 After This Repair

After this repair note, the status is:

### Stable:
- charter
- foundational object model
- residual formation
- structural validity
- normalization core
- value equality layer
- closed arithmetic
- closed rebasing
- denominator-sensitive completion semantics
- active scalar projection semantics

### Provisional but repairable:
- active rebasing with nontrivial pre-existing residuals
- the role of lift in rebase
- fully canonical active arithmetic beyond add/sub

### Still open:
- exact residual-construction algorithm for broader classes
- canonical quotient selection
- full active multiplication/division
- broader exact inbound construction beyond rationals

---

## 11. Recommended Next Formal Action

The next formal refinement should be:

### Residual Construction Rules v1
A rule layer that answers:

Given an exact external scalar comparison target \(T\), can we construct a
finite valid residual object \(R\) such that:

$$
\rho_D(R) = T
$$

for a specified parent denominator \(D\)?

This becomes the missing bridge between:
- denominator-sensitive semantics,
- active rebasing,
- and future active arithmetic.

---

## Summary

Active Rebase Repair Notes v1 establishes:

1. the original naive carryover rule for pre-existing residuals was incorrect
2. the failure is due to parent-denominator-sensitive semantics
3. active rebasing must be defined by exact residual reconstruction in the new
   denominator frame
4. the simple closed-to-active case still works
5. the general active rebase program remains viable, but needs a residual
   construction layer

This is a productive correction, not a collapse of the theory.

---

# VDR
## Semantic Fork Note v1

This note records a major semantic fork discovered during v1 development.

The issue is whether active VDR objects with nonzero residuals should be
interpreted as:
- scalar-additive completions,
or
- exact state-carrying objects that do not collapse to ordinary scalar value
  by default.

This fork is foundational.
Once chosen, it will strongly affect:
- active semantics,
- active equality,
- rebasing,
- scalar projection,
- arithmetic,
- and the long-term role of VDR.

---

## 1. The Trigger for the Fork

Consider the VDR object:

$$
[2,5,1]
$$

One possible reading is:

- additive completion reading:
  “\(2/5\) completed by residual \(1\)”
  which could collapse to something like \(3/5\)

But this creates a problem:

If:

$$
[2,5,1] \equiv [3,5,0]
$$

then the residual slot loses much of its reason to exist, because the object
could be collapsed into an ordinary closed rational form.

This directly conflicts with the motivating idea that the residual is exact
value-bearing structure that must not be discarded.

The intended motivating example is:

$$
11 / 5 \rightsquigarrow [2,5,1]
$$

Under this reading:
- \(2\) is the settled quotient component,
- \(5\) is the denominator frame,
- \(1\) is the exact residual left by the operation.

Then:

$$
[2,5,1] \neq [3,5,0]
$$

because:
- “quotient 2 with residual 1”
is not the same native object as
- “quotient 3 with no residual”

This tension creates the semantic fork.

---

## 2. Path A: Additive Active Semantics

Under Path A, an active VDR object is interpreted as carrying scalar
completion in a way that contributes directly to scalar value.

Example guiding idea:

$$
[V,D,r]
\mapsto
\frac{V+r}{D}
$$

or, more generally, some parent-sensitive additive completion law.

### Advantages
- easier connection to conventional scalar mathematics
- active scalar projection becomes straightforward
- rebasing can be justified by scalar-preserving formulas
- VDR resembles a recursive exact scalar representation system

### Cost
- residual begins to act like delayed scalar addition
- objects such as:

$$
[2,5,1]
$$

risk collapsing toward:

$$
[3,5,0]
$$

- negative residuals become scalar corrections rather than exact state
- the ontological force of triple irreducibility weakens
- VDR risks becoming “fraction-plus-annotation” rather than a genuinely new
  exact native object system

### Consequence
Path A favors interoperability and scalar comparability, but risks losing the
deep reason for preserving residual structure.

---

## 3. Path B: State-Carrying Active Semantics

Under Path B, a nonzero residual is not automatically interpreted as scalar
additive completion.

Instead, an active VDR object is an exact state-carrying object.

Example guiding idea:

$$
[2,5,1]
$$

means:
- quotient/state value \(2\),
- denominator frame \(5\),
- residual state \(1\),

not:
- \(3/5\)

and not:
- \(2/5 + 1/5\)

Likewise:

$$
[2,5,-1]
$$

is not simply \(1/5\),
but a distinct exact signed residual state in the same denominator frame.

### Advantages
- preserves the ontological importance of the residual
- supports the intuition that VDR records exact operation-state, not merely
  scalar output
- makes triple irreducibility meaningful
- keeps active objects genuinely distinct from closed rational objects

### Cost
- active scalar projection can no longer be assumed by default
- rebasing must preserve exact state, not just scalar value
- arithmetic becomes more difficult
- interoperability with conventional scalar systems becomes weaker or more
  conditional
- VDR becomes less like a generalized fraction system and more like a native
  exact state calculus

### Consequence
Path B preserves VDR’s deeper identity, but requires a more careful theory of:
- when active objects project outward,
- which active subclasses have scalar images,
- and how state-preserving operations work.

---

## 4. Why the Example [2,5,-1] Matters

The object:

$$
[2,5,-1]
$$

makes the fork especially clear.

Under additive semantics, this tends to collapse toward:

$$
\frac{2-1}{5} = \frac{1}{5}
$$

But under state-carrying semantics, it is a different exact object:
- same denominator frame,
- same quotient shell,
- opposite signed residual state.

This strongly suggests that residual is not merely a numerator adjustment.

So the sign of the residual supports Path B more naturally than Path A.

---

## 5. Immediate Consequences if Path B Is Chosen

If Path B is chosen, the following v1 layers must be revised:

1. Denominator-sensitive completion semantics
   - active residual must no longer be treated as scalar-additive by default

2. Active scalar projection
   - must be weakened, restricted, or deferred
   - active objects may not always have direct scalar meaning

3. Active rebasing
   - must preserve exact state, not scalar comparison image alone

4. Lift / residual transport
   - must transport state structure, not just value contribution

5. Active arithmetic
   - must be re-grounded as state operations, not scalar arithmetic extension

The closed rational core remains intact.

---

## 6. Immediate Consequences if Path A Is Chosen

If Path A is chosen, the current v1 active semantics can continue in roughly
their current direction, with technical repair.

But this comes with a conceptual concession:

- the residual becomes part of scalar completion
- and active VDR becomes closer to recursive exact scalar representation

This may still be useful, but it is a weaker break from conventional scalar
thinking.

---

## 7. Current Evidence

The current evidence favors Path B if the design goal is to keep residual
ontologically real rather than merely scalar-additive.

The strongest evidence is:

1. the motivating interpretation of

$$
11/5 \rightsquigarrow [2,5,1]
$$

as exact quotient-plus-residual state

2. the non-collapse intuition:

$$
[2,5,1] \neq [3,5,0]
$$

3. the signed residual distinction:

$$
[2,5,1],\quad [2,5,0],\quad [2,5,-1]
$$

appear to be three different exact native states, not merely three scalar
fractions

4. the charter’s insistence that residual is exact value-bearing structure and
must not be discarded

---

## 8. Recommended Decision Framing

The decision should be framed as follows:

Question:
Should active VDR objects have scalar-additive meaning by default?

- If yes, choose Path A.
- If no, and active residual is exact native state rather than scalar
  correction, choose Path B.

This is the real semantic choice.

---

## 9. Recommendation at v1

Current evidence suggests:

- closed objects:
  retain direct exact rational/scalar projection

- active objects:
  should not be assumed to collapse to scalar value by default

So the likely direction for VDR is:

- scalar semantics for the closed subclass
- state-carrying semantics for the active subclass unless and until a later
  interpretation layer provides a justified scalar projection

This is a mixed but coherent position.

---

## 10. Summary

The semantic fork is:

### Path A
Active residuals contribute directly to scalar completion.

### Path B
Active residuals are exact native state and do not collapse to ordinary scalar
meaning by default.

Choosing Path A makes VDR easier to compare to scalar mathematics, but risks
collapsing the reason the residual exists.

Choosing Path B preserves the ontological force of the residual, but requires
a more difficult theory of active operations and active interoperability.

At this stage, the motivating examples strongly suggest that Path B is closer
to the intended identity of VDR.

This fork should be settled before further active semantic expansion.

---

# VDR
## Revised Active Rebase Repair Notes v1
### Path B Commitment

This note replaces the earlier repair note that was still framed by scalar
preservation.

Under Path B, active VDR objects are exact operation-state objects, not
ordinary scalar values by default. Therefore active rebasing cannot be
repaired by asking only whether a rebased form has the same scalar
projection.

Instead, the repair problem is:

How can an active VDR object be reconstructed exactly in a new denominator
frame without collapsing its residual state into scalar semantics?

This note records:
- what was wrong in the earlier account,
- what remains sound,
- and what the correct repair direction is under Path B.

---

## 1. The Earlier Error

Earlier active rebase discussion relied on a scalar-preserving intuition of
the form:

- start with an active object,
- change denominator,
- preserve projected scalar meaning,
- adjust the residual accordingly.

This was already unstable under the previous additive semantics, and it is no
longer acceptable under Path B.

The deeper error was assuming that an active object could be repaired by
finding the “right scalar-equivalent residual.”

That assumes the active object has a scalar value by default.
Under Path B, it does not.

So the old repair target was conceptually wrong.

---

## 2. What the Worked Example Still Taught

The failed example involving:

$$
[2,5,1]
$$

was still valuable, but for a different reason than first stated.

It showed that:
- literal residual carryover across denominator change is not safe
- additive mismatch correction is not safe
- and denominator frame matters to active state

So the example still exposed a real issue:
active rebasing cannot be defined by naive structural reuse of the old
residual.

That conclusion remains correct.

---

## 3. What Remains Sound

The following points still appear correct and should be preserved:

### 3.1. Active rebasing is needed
If VDR is to support denominator-frame manipulation of active objects at all,
an active rebase theory is necessary.

### 3.2. Denominator frame matters
Residual state is held in a denominator frame.
Changing the denominator changes the frame, so state reconstruction is needed.

### 3.3. Literal carryover is unsound
A rule of the form:

$$
R' = [S,D,0] + R
$$

or any direct copy-forward of old residual state is not a valid general
active rebasing law.

### 3.4. Approximation remains forbidden
If exact active reframe cannot be constructed, rebasing must fail.

---

## 4. What Changes Under Path B

Under Path B, the repair target is no longer:

- “find a rebased object with the same scalar value”

The correct target is:

- “find a rebased object that is a valid exact reconstruction of the same
  native operation-state in a new denominator frame”

This is a stronger and more native requirement.

It means active rebasing is not a scalar equivalence problem.
It is a state-reexpression problem.

---

## 5. Correct Repair Direction

The correct Path B repair direction is:

Given an active object:

$$
X = [V,D,R]
$$

and target denominator:

$$
B \neq 0
$$

seek a new object:

$$
X' = [Q,B,R']
$$

such that:

1. \(X'\) is raw-valid
2. \(X'\) is finite
3. \(X'\) is an exact reexpression of the same native operation-state as \(X\)
   in denominator frame \(B\)
4. no approximation is used
5. if no such exact reconstruction rule is known, rebasing fails

This is the proper Path B rebase criterion.

---

## 6. What This Means for Residual Reconstruction

Residual reconstruction is now not:
- scalar residual matching,
- or additive compensation.

Instead, it is:
- state reconstruction under denominator-frame change.

So a future reconstruction rule must answer:

Given source state \( [V,D,R] \), what residual structure \(R'\) in frame
\(B\) exactly preserves the native state-content of the source?

That is a genuinely different problem from scalar equality.

---

## 7. What This Means for Quotient Selection

Under the discarded scalar path, quotient choice was guided by scalar
decomposition.

Under Path B, quotient choice can no longer be justified by “nearest” or
scalar convenience ideas.

Instead, any quotient choice must be justified by native state criteria, such
as:
- exact reconstructibility,
- structural simplicity,
- canonicality,
- frame coherence,
- or later explicitly defined native rules.

So quotient selection remains open, but now on the correct foundation.

---

## 8. What This Means for `lift`

`lift` remains useful as a structural transport helper, but it is not the same
thing as full state reconstruction.

So:
- `lift` may support active rebasing
- but `lift` alone is not the repair

This remains true under Path B.

---

## 9. What a Safe v1 Position Looks Like

A safe v1 position is:

- active rebasing is conceptually required
- denominator-frame sensitivity makes it nontrivial
- naive residual carryover is invalid
- scalar-preserving repair is not the right target
- exact native state reconstruction is the right target
- general active rebase remains provisional until such reconstruction rules
  are defined

This is a strong and honest position.

---

## 10. Example Status Under Path B

The object:

$$
[2,5,1]
$$

should no longer be used as if it had a default scalar value like \(3/5\).

Instead, it should be used as an example of:
- exact active state,
- denominator-frame sensitivity,
- and non-collapse of residual state.

Thus the earlier worked example still reveals a problem, but the problem is
now stated correctly:
not
- “the projected value came out wrong,”
but
- “the attempted rebasing failed to preserve native active state in a justified
  way.”

---

## 11. Recommended Formal Next Step

The next formal step should no longer be “residual construction from scalar
target.”

Instead, it should be something like:

### Active State Reconstruction Rules v1

A future layer should define:
- when two active objects count as the same native state across denominator
  frames
- how a new residual structure is constructed in a target frame
- and which reconstruction rules are exact and finite

This is the real missing bridge for Path B active rebasing.

---

## 12. Status After This Repair

After the Path B repair, the current status is:

### Stable
- charter
- foundational object model
- residual formation
- raw validity
- structural equality
- normalization core
- value equality
- closed arithmetic
- closed rebasing
- active objects as native operation-state objects

### Provisional but correctly framed
- active rebasing
- lift as support for rebasing
- active same-frame addition-like / subtraction-like operations

### Deferred
- general active state reconstruction
- canonical quotient selection
- active multiplication/division
- scalar interpretation of active objects
- broader inbound construction beyond the closed rational core

---

## Summary

The revised repair note establishes:

1. the old scalar-preservation repair target was wrong under Path B
2. active rebasing must preserve native operation-state, not scalar image
3. naive residual carryover remains invalid
4. denominator-frame reconstruction remains the true problem
5. the next missing layer is active state reconstruction, not scalar residual
   construction

This is a cleaner and more faithful foundation for the next stage of VDR.

---

# VDR
## Revised Worked Examples v1
### Path B Commitment

This document revises the worked examples so they match the Path B semantic
decision.

Under Path B:
- closed VDR objects may still admit exact scalar projection
- active VDR objects are exact operation-state objects by default
- active residual is not additive scalar completion
- active examples must no longer be explained by collapsing them into ordinary
  fractions unless a later interpretation layer explicitly does so

These examples illustrate:
- raw validity,
- normalization,
- structural equality,
- normalized value equality,
- closed arithmetic,
- closed rebasing,
- active specification,
- active structural distinction,
- same-frame active combination,
- exact failure,
- and open reconstruction questions.

---

## 1. Closed Object Examples

### Example 1.1. Simple closed rational
Object:

$$
[1,2,0]
$$

Status:
- raw-valid
- closed
- already normalized under standard sign convention

Closed scalar projection:

$$
\Pi([1,2,0]) = \frac{1}{2}
$$

---

### Example 1.2. Non-normal closed rational
Object:

$$
[2,4,0]
$$

Status:
- raw-valid
- closed
- not normalized

Normalization:

$$
[2,4,0] \mapsto [1,2,0]
$$

So:
- structurally distinct from \([1,2,0]\)
- normalized-value equal to \([1,2,0]\)

Write:

$$
[2,4,0] \not\equiv_s [1,2,0]
$$

but:

$$
[2,4,0] \equiv_n [1,2,0]
$$

---

### Example 1.3. Negative denominator
Object:

$$
[1,-2,0]
$$

Status:
- raw-valid
- closed
- not normalized if denominator-positive convention is chosen

Normalization:

$$
[1,-2,0] \mapsto [-1,2,0]
$$

So negative denominators remain valid in raw form.

---

## 2. Structural Equality and Normalized Value Equality

### Example 2.1. Structural equality
Compare:

$$
X = [1,2,0]
\qquad
Y = [1,2,0]
$$

Then:

$$
X \equiv_s Y
$$

Therefore also:

$$
X \equiv_n Y
$$

---

### Example 2.2. Structural inequality but normalized-value equality
Compare:

$$
X = [2,4,0]
\qquad
Y = [1,2,0]
$$

Then:

$$
X \not\equiv_s Y
$$

but after normalization:

$$
\mathrm{norm}(X) = [1,2,0]
=
\mathrm{norm}(Y)
$$

So:

$$
X \equiv_n Y
$$

---

### Example 2.3. Child order difference
Compare:

$$
X = [1,2,1 + [1,3,0] + [1,5,0]]
$$

$$
Y = [1,2,1 + [1,5,0] + [1,3,0]]
$$

As written:
- child order differs
- so structural equality fails

$$
X \not\equiv_s Y
$$

If normalization canonically orders children, then they may satisfy:

$$
X \equiv_n Y
$$

This is a normalization-layer fact, not a scalar one.

---

## 3. Closed Arithmetic Examples

### Example 3.1. Closed addition
Compute:

$$
[1,2,0] + [1,3,0]
$$

By closed addition:

$$
[1\cdot 3 + 1\cdot 2,\; 2\cdot 3,\; 0]
=
[5,6,0]
$$

Closed projection check:

$$
\frac{1}{2} + \frac{1}{3} = \frac{5}{6}
$$

---

### Example 3.2. Closed subtraction
Compute:

$$
[3,4,0] - [1,2,0]
$$

By closed subtraction:

$$
[3\cdot 2 - 1\cdot 4,\; 4\cdot 2,\; 0]
=
[2,8,0]
$$

Normalize:

$$
[2,8,0] \mapsto [1,4,0]
$$

---

### Example 3.3. Closed multiplication
Compute:

$$
[2,3,0] \times [3,5,0]
$$

By closed multiplication:

$$
[6,15,0]
$$

Normalize:

$$
[6,15,0] \mapsto [2,5,0]
$$

---

### Example 3.4. Closed division
Compute:

$$
[2,3,0] \div [4,5,0]
$$

By closed division:

$$
[10,12,0]
$$

Normalize:

$$
[10,12,0] \mapsto [5,6,0]
$$

---

### Example 3.5. Division by closed zero fails
Attempt:

$$
[1,2,0] \div [0,7,0]
$$

This fails explicitly because division by a closed zero object is invalid.

---

## 4. Closed Rebasing Examples

### Example 4.1. Successful closed rebase
Rebase:

$$
[1,2,0]
$$

to denominator:

$$
4
$$

Check:

$$
\frac{1\cdot 4}{2} = 2 \in \mathbb{Z}
$$

So:

$$
\mathrm{rebase}([1,2,0],4) = [2,4,0]
$$

Normalization may then return:

$$
[1,2,0]
$$

---

### Example 4.2. Failed closed rebase
Rebase:

$$
[1,2,0]
$$

to denominator:

$$
3
$$

Check:

$$
\frac{1\cdot 3}{2} \notin \mathbb{Z}
$$

So closed rebasing fails at v1.

---

## 5. Active Specification Examples

### Example 5.1. Atomic active object
Object:

$$
[2,5,1]
$$

Status:
- raw-valid
- active
- residual is atomic integer \(1\)

Native reading under Path B:
- settled value slot \(2\)
- denominator frame \(5\)
- residual state \(1\)

This object is not identified by default with:

$$
[3,5,0]
$$

and it is not assigned a default scalar projection in v1.

---

### Example 5.2. Negative atomic active object
Object:

$$
[2,5,-1]
$$

Status:
- raw-valid
- active

Native reading:
- settled value slot \(2\)
- denominator frame \(5\)
- residual state \(-1\)

This is distinct from both:

$$
[2,5,0]
\qquad\text{and}\qquad
[2,5,1]
$$

So Path B treats residual sign as meaningful native state, not simple scalar
correction.

---

### Example 5.3. Active object with child state
Object:

$$
[1,2,[1,3,0]]
$$

Status:
- raw-valid
- active
- residual contains one child VDR object

Native reading under Path B:
- parent frame \(2\)
- child state \([1,3,0]\) nested in residual
- no default collapse into a scalar such as \(2/3\)

The child is exact nested state, not automatic numeric completion.

---

### Example 5.4. Composite active state
Object:

$$
[2,5,1 + [1,4,0] + [1,2,0]]
$$

Status:
- raw-valid
- active
- composite residual with atomic base and two child states

Native reading:
- exact operation-state object with finite nested residual structure

No default scalar projection is assigned in v1.

---

## 6. Active Equality Boundary Examples

### Example 6.1. Non-collapse of active to closed
Compare:

$$
X = [2,5,1]
\qquad
Y = [3,5,0]
$$

Under Path B:
- \(X\) is active
- \(Y\) is closed

They are structurally unequal:

$$
X \not\equiv_s Y
$$

And they should not be normalized-value equal at v1:

$$
X \not\equiv_n Y
$$

This is a core Path B example.

---

### Example 6.2. Signed active distinction
Compare:

$$
[2,5,1]
\qquad
[2,5,-1]
$$

These are structurally distinct and remain normalized-value distinct unless a
future rule explicitly identifies them, which Path B does not suggest.

So sign of residual state matters natively.

---

### Example 6.3. Raw-distinct active forms with possible normalization
Compare:

$$
X = [1,2,1 + [1,5,0] + [1,3,0]]
$$

$$
Y = [1,2,1 + [1,3,0] + [1,5,0]]
$$

These are structurally distinct due to child order.

If normalization canonically orders children, they may satisfy:

$$
X \equiv_n Y
$$

This is structural normalization, not scalar collapse.

---

## 7. Same-Frame Active Combination Examples

### Example 7.1. Same-frame addition-like combination
Take:

$$
X = [2,5,1]
\qquad
Y = [3,5,-1]
$$

Since both are in denominator frame \(5\), v1 permits same-frame
addition-like combination:

$$
X + Y = [2+3,\;5,\;1 \oplus (-1)]
$$

Residual combination:

$$
1 \oplus (-1) = 0
$$

So the raw result is:

$$
[5,5,0]
$$

Normalize:

$$
[5,5,0] \mapsto [1,1,0]
$$

This example is valid as a native same-frame rule under v1.
It should not be interpreted as evidence that each operand separately had a
default scalar meaning.

---

### Example 7.2. Same-frame subtraction-like combination
Take:

$$
X = [4,7,2]
\qquad
Y = [1,7,1]
$$

Then:

$$
X - Y = [3,7,2 \ominus 1]
= [3,7,1]
$$

This is an exact same-frame state transformation.

No scalar reading is required.

---

### Example 7.3. Same-frame child residual combination
Take:

$$
X = [1,3,[1,5,0]]
\qquad
Y = [2,3,[2,5,0]]
$$

Then same-frame addition-like combination gives:

$$
[3,3,[1,5,0] \oplus [2,5,0]]
$$

At raw structural level this becomes a composite residual containing both
children, subject to later normalization and any same-denominator child
absorption rules once fully defined.

---

## 8. Active Rebase Boundary Examples

### Example 8.1. Trivial same-frame reconstruction
For:

$$
[2,5,1]
$$

rebasing to denominator:

$$
5
$$

the reconstruction may be identity:

$$
[2,5,1] \rightsquigarrow [2,5,1]
$$

This is the trivial active state reconstruction case.

---

### Example 8.2. Nontrivial active rebase remains open
Attempt to rebase:

$$
[2,5,1]
$$

to denominator:

$$
3
$$

Under Path B, this is not solved by assigning a scalar value and matching it.

Instead, this requires exact active state reconstruction in the new frame.

At v1:
- this case is open unless a special reconstruction rule is explicitly
  supplied
- so honest result is currently:
  explicit failure / unresolved case

This is the correct Path B treatment.

---

## 9. Lift Examples

### Example 9.1. Atomic lift
Lift residual:

$$
1
$$

by factor:

$$
3
$$

Result:

$$
\mathrm{lift}(1,3) = 3
$$

This is exact structural/state transport, not scalar multiplication of an
active object as a whole.

---

### Example 9.2. Child lift
Lift child:

$$
[1,3,0]
$$

by factor:

$$
2
$$

Result:

$$
\mathrm{lift}([1,3,0],2) = [2,3,0]
$$

This preserves child denominator frame while scaling the child value slot.

---

### Example 9.3. Composite lift
Lift:

$$
1 + [1,3,0]
$$

by factor:

$$
2
$$

Result:

$$
2 + [2,3,0]
$$

This is exact residual-state transport.

---

## 10. Equality Recovery Examples

### Example 10.1. Closed return to origin
Start:

$$
X = [1,2,0]
$$

Add:

$$
[1,3,0]
$$

then subtract:

$$
[1,3,0]
$$

Final result is normalized-value equal to:

$$
[1,2,0]
$$

No epsilon test is needed.

---

### Example 10.2. Closed multiply/divide return
Start:

$$
X = [3,7,0]
$$

Multiply by:

$$
[5,2,0]
$$

then divide by:

$$
[5,2,0]
$$

Final normalized result is:

$$
[3,7,0]
$$

again exactly.

---

## 11. Inbound Construction Examples

### Example 11.1. Integer inbound
Input:

$$
5
$$

Inbound construction:

$$
\mathrm{in}(5) = [5,1,0]
$$

Closed projection:

$$
\Pi([5,1,0]) = 5
$$

---

### Example 11.2. Rational inbound
Input:

$$
-\frac{3}{4}
$$

Inbound construction:

$$
\mathrm{in}\!\left(-\frac{3}{4}\right) = [-3,4,0]
$$

Closed projection:

$$
\Pi([-3,4,0]) = -\frac{3}{4}
$$

---

### Example 11.3. Approximate decimal not admitted as exact active meaning
Input:
- decimal approximation of \( \pi \), such as `3.14159`

At v1:
- this may be treated externally as an approximate decimal quantity
- but it is not admitted as an exact VDR representation of \( \pi \)
- and it is not turned into an active VDR object merely by syntax

If treated exactly at all, it is only the rational decimal value:

$$
\frac{314159}{100000}
$$

not \( \pi \).

---

## 12. Out-of-Scope Example

### Example 12.1. Malformed infinite decimal artifact
Input:

```text
0.3333...751
```

This has no coherent finite exact constructive meaning.

So:
- exact inbound construction fails
- it is outside v1 scope

---

## 13. Key Lessons from the Revised Examples

These revised examples show that v1 now has:

- a correct closed rational core
- exact normalization-based equality for the current normalization layer
- exact closed rebasing
- exact active specification
- exact active structural distinction
- exact same-frame active combination rules
- honest failure or openness where active reconstruction is not solved

They also show clearly that:

- active objects are not ordinary scalar values by default
- residual sign matters
- nested child structure is nested state, not automatic arithmetic correction
- nontrivial active rebasing remains open
- the Path B fork is real and productive

---

## Summary

Revised Worked Examples v1 demonstrates:

1. what already works exactly
2. what active state looks like without scalar collapse
3. what closed projection still supports
4. what remains open and must fail honestly
5. how Path B makes VDR genuinely different from decorated fraction
   arithmetic

This is the correct example set for the current state of the theory.

---

Good. Here’s a clean vocabulary split.

1. Native equality
Use:
- “is natively equal to”
- symbols: \( \equiv_s \), \( \equiv_n \), later \( \equiv_a \)

Meaning:
- equality inside VDR only

Do not use `=` casually here unless the layer is clear.

2. Structural identity
Use:
- “is structurally equal to”

Meaning:
- same object as written

Example:
- \([1,2,0]\) is structurally equal to \([1,2,0]\)

3. Normalized equality
Use:
- “is normalized-value equal to”

Meaning:
- same after current normalization rules

Example:
- \([2,4,0]\) is normalized-value equal to \([1,2,0]\)

4. Active-state equivalence
Use:
- “is active-state equivalent to”

Meaning:
- future deeper sameness of active state across frames/reconstructions
- not yet fully defined

5. Projection
Use:
- “projects to”

Meaning:
- external map out of VDR

Safe for closed objects now:
- \([1,2,0]\) projects to \(1/2\)

Not safe by default for active objects.

6. Interpretation / correspondence
Use:
- “corresponds to under interpretation”
- “is a witness for”
- “is motivated by”
- “admits the active form”
- “is represented by under a chosen construction rule”

This is the right language for things like \(11/5\) and \([2,5,1]\).

So instead of:
- \(11/5 = [2,5,1]\)

say:
- \(11/5\) admits \([2,5,1]\) as an active VDR witness under a division-state construction
or shorter:
- \(11/5\) motivates the active form \([2,5,1]\)

And for the negative case:
- it is not yet established whether \(9/5\) admits \([2,5,-1]\) under the same kind of interpretation

7. Construction
Use:
- “constructs into”
- “is admitted as”
- “has inbound form”

Example:
- the rational \(1/2\) constructs into \([1,2,0]\)

That is stronger than “motivates,” but still not native equality.

Recommended rule of thumb

Inside VDR:
- use equality words only for VDR-to-VDR relations

Across VDR and scalar:
- use projection, construction, witness, or interpretation words
- avoid bare `=`

That will save a lot of confusion.

---

# VDR
## Terminology and Relation Discipline v1

This document defines the recommended language discipline for discussing VDR.

Its purpose is to prevent confusion between:
- native VDR relations,
- external scalar relations,
- interpretation-layer correspondences,
- and implementation-oriented construction statements.

This is especially important under Path B, where:
- closed VDR objects may admit scalar projection,
- active VDR objects do not collapse to scalar meaning by default,
- and the same symbol `=` can become dangerously ambiguous if used loosely.

This document is not a replacement for the formal axioms.
It is a usage discipline for writing and discussing the system correctly.

---

## 1. General Rule

### 1.1. Equality Discipline Rule
Inside VDR, equality language should be used only for explicitly defined VDR
relations.

Across VDR and external scalar systems, do not use bare equality unless the
relevant interpretation or projection layer is explicitly stated.

So:
- use exact VDR relation names for VDR-to-VDR comparisons
- use projection / construction / interpretation words for VDR-to-scalar or
  scalar-to-VDR discussion

---

## 2. Native VDR Relations

### 2.1. Structural Equality
Use:

- “is structurally equal to”

and the symbol:

$$
\equiv_s
$$

Meaning:
- exact same VDR object as written,
- slot by slot,
- recursively,
- and in order.

Example:

$$
[1,2,0] \equiv_s [1,2,0]
$$

---

### 2.2. Normalized Value Equality
Use:

- “is normalized-value equal to”

and the symbol:

$$
\equiv_n
$$

Meaning:
- same current canonical form after normalization,
- not necessarily structurally identical as written.

Example:

$$
[2,4,0] \equiv_n [1,2,0]
$$

provided normalization maps both to the same normal form.

---

### 2.3. Reserved Active-State Equivalence
Use:

- “is active-state equivalent to”

and the reserved symbol:

$$
\equiv_a
$$

Meaning:
- exact sameness of native active state across possibly different frames or
  reconstructions,
- beyond current normalization.

At v1 this relation is reserved but not generally defined.

So the phrase may be used only when explicitly discussing future or
special-case active-state theory.

---

## 3. External Scalar Relations

### 3.1. Projection Language
Use:

- “projects to”
- “has scalar projection”
- “has exact closed projection”

Meaning:
- a VDR object is mapped outward into a scalar comparison form by a specified
  external rule.

Example:

$$
[1,2,0]
$$

projects to:

$$
\frac{1}{2}
$$

under the closed projection rule.

---

### 3.2. Projection Limitation Rule
Under Path B, projection language should be used by default only for:
- closed VDR objects,
- or active subclasses for which a specific interpretation layer has been
  explicitly defined.

Do not say that a general active object “equals” or “is” a scalar value by
default.

---

## 4. Scalar-to-VDR Language

### 4.1. Construction Language
Use:

- “constructs into”
- “is admitted as”
- “has inbound form”
- “is represented in VDR as”  
  only when the construction rule is explicit

Meaning:
- an external object is brought into VDR by a specified exact construction
  rule.

Example:

$$
\frac{1}{2}
$$

constructs into:

$$
[1,2,0]
$$

under the rational inbound rule.

---

### 4.2. Construction Is Not Equality Rule
Do not use bare equality to identify an external scalar and a VDR object just
because there is an inbound construction.

So prefer:

- “\(1/2\) constructs into \([1,2,0]\)”,

not:

- “\(1/2 = [1,2,0]\)”

unless a specific interpretive identification is formally stated.

---

## 5. Interpretation-Layer Language

### 5.1. Interpretation Language
When discussing a possible or optional relation between an external scalar and
an active VDR object, use:

- “corresponds to under interpretation”
- “is a witness for”
- “is motivated by”
- “admits the active form”
- “arises under a division-state construction”
- “is associated with under a chosen interpretation layer”

These phrases mark that the relation is:
- not native equality,
- not default scalar projection,
- and not yet a foundational theorem unless stated as such.

---

### 5.2. Motivating Example Language
For examples such as:

$$
11/5
$$

and

$$
[2,5,1]
$$

prefer phrases like:

- “\(11/5\) motivates the active form \([2,5,1]\)”
- “\(11/5\) admits \([2,5,1]\) as an active witness under a division-state
  reading”
- “\([2,5,1]\) may arise from a division-style construction on \(11/5\)”

Do not write, at v1:

$$
11/5 = [2,5,1]
$$

because that incorrectly suggests native scalar equality.

---

### 5.3. Unsettled Interpretation Language
For cases not yet justified, use:

- “not established”
- “open”
- “unresolved”
- “not yet admitted”
- “not yet justified by a formal interpretation layer”

Example:
it is not yet established whether:

$$
9/5
$$

admits:

$$
[2,5,-1]
$$

under the same kind of interpretation that motivates:

$$
11/5 \rightsquigarrow [2,5,1]
$$

---

## 6. Disallowed Informal Shortcuts

### 6.1. No Bare Cross-Domain Equality Rule
Do not use bare `=` between:
- a scalar and an active VDR object,
- unless a specific interpretation layer explicitly authorizes it.

So avoid statements like:

- \(11/5 = [2,5,1]\)
- \(9/5 = [2,5,-1]\)

at the foundational v1 level.

---

### 6.2. No Silent Scalar Collapse Rule
Do not use language that silently treats an active residual as:
- numerator adjustment,
- additive correction,
- delayed simplification,
- or fraction completion

unless a later interpretation layer explicitly defines that semantics.

So avoid phrases like:

- “\([2,5,1]\) is just \(3/5\)”

under Path B.

---

### 6.3. No Ambiguous “Value” Rule
The word “value” can be ambiguous in VDR.

At v1, distinguish carefully among:
- value slot \(V\)
- normalized value equality
- native operation-state
- scalar projection value

When necessary, say:
- “value slot”
- “normalized value equality”
- “native state”
- “external scalar value”

rather than just “value.”

---

## 7. Recommended Writing Pattern

### 7.1. Inside VDR
Use:
- structural equality
- normalized-value equality
- active-state equivalence
- validity
- normalization
- reconstruction
- rebasing
- state combination

---

### 7.2. At the VDR Boundary
Use:
- projects to
- constructs into
- is admitted as
- is reported externally as
- has exact closed projection

---

### 7.3. In Open/Interpretive Discussion
Use:
- motivates
- corresponds under interpretation
- is a witness for
- may arise from
- is unresolved
- is not yet established

---

## 8. Canonical Examples

### Example 8.1. Correct closed statement
Correct:

- \(1/2\) constructs into \([1,2,0]\)
- \([1,2,0]\) projects to \(1/2\)

Avoid:
- \(1/2 = [1,2,0]\)  
  unless a specific formal identification is being made in context

---

### Example 8.2. Correct active statement
Correct:

- \(11/5\) motivates the active form \([2,5,1]\)
- \([2,5,1]\) is an active VDR object with value slot \(2\), denominator frame
  \(5\), and residual state \(1\)

Avoid:
- \(11/5 = [2,5,1]\)
- \([2,5,1] = 3/5\)

---

### Example 8.3. Correct unresolved statement
Correct:

- it is not yet established whether \(9/5\) admits \([2,5,-1]\) under a
  corresponding interpretation layer

Avoid:
- \(9/5 = [2,5,-1]\)

---

## 9. Summary

Terminology and Relation Discipline v1 establishes a clean language boundary:

Inside VDR:
- use native equality names and native structural language

Across domains:
- use projection, construction, interpretation, witness, and motivation
  language

Do not let bare equality silently cross between:
- active VDR state
- and scalar mathematics

This discipline is necessary to keep the Path B version of VDR coherent.

---

## Recommended Immediate Use

This discipline should now be applied when revising:
- Supported Domain Examples v1
- Paper Outline v1
- benchmark wording
- implementation docs
- and any future examples involving active objects

It is one of the key safeguards against accidentally drifting back into the
discarded Path A semantics.

---

