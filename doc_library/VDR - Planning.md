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

