Good. Let’s test the active rebase algorithm on simple rational cases.

I’ll use the rule just defined:

For source
$$
[V,D,R]
$$
rebased to target denominator \(B\),

1. compute
$$
N = VB
$$

2. divide
$$
N = QD + S
$$

3. construct
$$
\mathrm{rebase}([V,D,R],B)
=
[Q,B,\; [S,D,0] + \mathrm{lift}(R,B)]
$$

For these first examples, I’ll use only closed sources:
$$
[V,D,0]
$$
so `lift(R,B)=0`.

Thus:
$$
\mathrm{rebase}([V,D,0],B)
=
[Q,B,[S,D,0]]
$$
when closed rebasing does not land cleanly.

# Simple Rational Cases

## Case 1: Exact closed rebase
Source:
$$
[1,2,0]
$$
Target denominator:
$$
B=4
$$

Step 1:
$$
N = V B = 1 \cdot 4 = 4
$$

Step 2:
$$
4 = Q\cdot 2 + S
$$
So:
- \(Q=2\)
- \(S=0\)

Result:
$$
[2,4,0]
$$

Normalize:
$$
[2,4,0] \mapsto [1,2,0]
$$

This is a clean closed rebase.

---

## Case 2: Another exact closed rebase
Source:
$$
[3,4,0]
$$
Target:
$$
B=8
$$

Step 1:
$$
N = 3\cdot 8 = 24
$$

Step 2:
$$
24 = Q\cdot 4 + S
$$
So:
- \(Q=6\)
- \(S=0\)

Result:
$$
[6,8,0]
$$

Normalize:
$$
[6,8,0] \mapsto [3,4,0]
$$

Again, exact closed rebase.

---

## Case 3: Non-clean rebase, active residual appears
Source:
$$
[1,2,0]
$$
Target:
$$
B=3
$$

Step 1:
$$
N = 1\cdot 3 = 3
$$

Step 2:
$$
3 = Q\cdot 2 + S
$$
So:
- \(Q=1\)
- \(S=1\)

Result:
$$
\mathrm{rebase}([1,2,0],3) = [1,3,[1,2,0]]
$$

Interpretation:
- top-level quotient gives \(1/3\)
- remainder child carries the unresolved exact part \(1/2\)

So this is the first active rebased form.

Important note:
This is structurally exact under the proposed rule,
but whether this object evaluates correctly under your eventual semantics depends on the full evaluation law for nested remainder.

Still, as a formal active rebase output, this is the right simple test case.

---

## Case 4: Another non-clean rebase
Source:
$$
[1,3,0]
$$
Target:
$$
B=2
$$

Step 1:
$$
N = 1\cdot 2 = 2
$$

Step 2:
$$
2 = Q\cdot 3 + S
$$
Using integer division:
- \(Q=0\)
- \(S=2\)

Result:
$$
\mathrm{rebase}([1,3,0],2) = [0,2,[2,3,0]]
$$

So the rebased object becomes:
- top-level \(0/2\)
- active residual child \([2,3,0]\)

Again, exact residual preserved rather than approximated.

---

## Case 5: Whole number rebased awkwardly
Source:
$$
[2,1,0]
$$
Target:
$$
B=3
$$

Step 1:
$$
N = 2\cdot 3 = 6
$$

Step 2:
$$
6 = Q\cdot 1 + S
$$
So:
- \(Q=6\)
- \(S=0\)

Result:
$$
[6,3,0]
$$

Normalize:
$$
[6,3,0] \mapsto [2,1,0]
$$

Whole numbers rebase cleanly to any denominator, as expected.

---

## Case 6: Negative denominator allowed
Source:
$$
[1,-2,0]
$$
Target:
$$
B=3
$$

Step 1:
$$
N = 1\cdot 3 = 3
$$

Step 2:
$$
3 = Q\cdot (-2) + S
$$

One valid integer-division choice is:
- \(Q=-1\)
- \(S=1\)

since:
$$
3 = (-1)(-2) + 1 = 2 + 1
$$

Result:
$$
\mathrm{rebase}([1,-2,0],3) = [-1,3,[1,-2,0]]
$$

This is a good example of why allowing negative denominators complicates division conventions. You’ll eventually need one fixed signed division rule.

But structurally, the form still works.

---

## Case 7: Negative numerator
Source:
$$
[-1,2,0]
$$
Target:
$$
B=3
$$

Step 1:
$$
N = -1\cdot 3 = -3
$$

Step 2:
$$
-3 = Q\cdot 2 + S
$$

Using standard quotient/remainder with bounded remainder:
- \(Q=-1\)
- \(S=-1\)

since:
$$
-3 = (-1)\cdot 2 + (-1)
$$

Result:
$$
[-1,3,[-1,2,0]]
$$

Again, active rebasing preserves sign exactly.

---

## Case 8: Larger exact rational
Source:
$$
[5,6,0]
$$
Target:
$$
B=4
$$

Step 1:
$$
N = 5\cdot 4 = 20
$$

Step 2:
$$
20 = Q\cdot 6 + S
$$

So:
- \(Q=3\)
- \(S=2\)

Result:
$$
[3,4,[2,6,0]]
$$

This is a nice example:
- top-level quotient \(3/4\)
- residual child \(2/6\), which itself normalizes to \(1/3\)

So after child normalization:
$$
[3,4,[1,3,0]]
$$

That seems like a strong candidate for normalized active rebased form.

---

# Observations from these simple cases

## 1. Exact closed rebases behave as expected
When \(D\) divides \(VB\), you get ordinary denominator change.

## 2. Non-clean rebases generate residual child VDRs naturally
This is the key behavior.

## 3. Whole numbers are easy
They close under any target denominator.

## 4. Signed values need a fixed division convention
Especially negative denominators and numerators.

## 5. Residual children often simplify
For example:
- \([2,6,0] \mapsto [1,3,0]\)

This suggests normalization of residual children is going to be very important.

---

# Key next problem
The biggest unresolved question is this:

What is the exact evaluation meaning of:

$$
[Q,B,[S,D,0]]
$$

Is it:
- \(Q/B\) plus something?
- \(Q/B\) with residual child as exact completion?
- some more native non-additive interpretation?

Because until that is defined precisely, the active rebase form is structurally clear but semantically incomplete.

That is the next major step.

If you want, next I can:
- define the exact semantic evaluation law for `[Q,B,[S,D,0]]`,
- propose a signed integer division convention for VDR,
- or work more examples and look for patterns in when rebasing terminates.

---

Good. Under completion semantics, the examples should be read natively as:

- top-level ratio
- completed by exact residual child
- not flattened additively unless we explicitly switch to legacy conversion

So I’ll rewrite the earlier simple cases that way.

# Arithmetic / Rebase Examples
## Under Completion Semantics

---

## Case 1: Exact closed rebase
Source:
$$
[1,2,0]
$$
Target denominator:
$$
3
$$

This does not close cleanly at denominator 3.

Compute:
$$
N = 1 \cdot 3 = 3
$$

Integer division by source denominator 2:
$$
3 = 1\cdot 2 + 1
$$

So:
- \(Q=1\)
- \(S=1\)

Rebased form:
$$
[1,3,[1,2,0]]
$$

Native reading:
- “one third with exact completion one-half”

Not:
- “one third plus one half”

Legacy conversion only:
$$
\mathrm{legacy}([1,3,[1,2,0]]) = \frac13 + \frac12 = \frac56
$$

So if this exact active rebase is meant to preserve the original value \(1/2\), then this construction is wrong as written.

This means the original active rebase rule needs correction.

That’s the first major consequence of the new semantics: the earlier quotient/residual placement was not value-preserving.

---

## Important correction
If completion is not additive in native semantics, but additive only in legacy flattening, then the rebasing rule must still flatten correctly when checked in legacy mode.

So a valid rebased object must satisfy:

$$
\mathrm{legacy}(\mathrm{rebase}(X,B)) = \mathrm{legacy}(X)
$$

That means the previous simple quotient rule was not correct.

---

# Corrected rebase intuition

If:
$$
[V,D,0]
$$
is to be rebased to denominator \(B\),

then the top-level frame should reflect the largest exact amount expressible in denominator \(B\), and the child should complete the remainder left after that amount.

So the correct equation in legacy terms must be:

$$
\frac{V}{D} = \frac{Q}{B} + \mathrm{legacy}(\text{child})
$$

where child is the exact leftover after removing \(Q/B\).

That means:

$$
\frac{V}{D} - \frac{Q}{B} = \frac{VB-QD}{DB}
$$

So the child must represent:

$$
\frac{VB-QD}{DB}
$$

not simply \([S,D,0]\).

That’s the corrected basis.

---

## Case 1 corrected
Source:
$$
[1,2,0]
$$
Target:
$$
3
$$

Choose:
$$
Q = 1
$$

Then leftover is:
$$
\frac12 - \frac13 = \frac{1}{6}
$$

So correct rebased form is:

$$
[1,3,[1,6,0]]
$$

Native reading:
- “one third with exact completion one sixth”

Legacy conversion:
$$
\frac13 + \frac16 = \frac12
$$

Now it works.

---

## Case 2 corrected
Source:
$$
[1,3,0]
$$
Target:
$$
2
$$

Choose:
$$
Q=0
$$

Then leftover:
$$
\frac13 - 0 = \frac13
$$

So rebased form:
$$
[0,2,[1,3,0]]
$$

Native reading:
- “zero halves with exact completion one third”

Legacy conversion:
$$
0 + \frac13 = \frac13
$$

This is valid.

But maybe not minimal.

Alternative choice:
If we allow \(Q=1\), then leftover is:
$$
\frac13 - \frac12 = -\frac16
$$

So another valid rebased form is:
$$
[1,2,[-1,6,0]]
$$

Native reading:
- “one half with exact completion negative one sixth”

Legacy:
$$
\frac12 - \frac16 = \frac13
$$

This is probably more informative because it keeps the target denominator visible in a more “filled” top-level frame.

So rebasing is not unique unless you define a quotient-selection rule.

That’s another important consequence.

---

## Case 3: exact closed rebase still works
Source:
$$
[1,2,0]
$$
Target:
$$
4
$$

Since:
$$
\frac12 = \frac24
$$

result:
$$
[2,4,0]
$$

Native reading:
- “two fourths, fully closed”

Legacy:
$$
\frac24 = \frac12
$$

No completion child needed.

---

## Case 4: another exact closed rebase
Source:
$$
[3,4,0]
$$
Target:
$$
8
$$

Result:
$$
[6,8,0]
$$

Native:
- “six eighths, fully closed”

Legacy:
$$
\frac68 = \frac34
$$

---

## Case 5: larger rational
Source:
$$
[5,6,0]
$$
Target:
$$
4
$$

We need:
$$
\frac56 = \frac{Q}{4} + \text{completion}
$$

Choose:
$$
Q = 3
$$

Then leftover:
$$
\frac56 - \frac34 = \frac{10-9}{12} = \frac1{12}
$$

So corrected rebased form:
$$
[3,4,[1,12,0]]
$$

Native reading:
- “three fourths with exact completion one twelfth”

Legacy:
$$
\frac34 + \frac1{12} = \frac{9+1}{12} = \frac{10}{12} = \frac56
$$

This works perfectly.

---

## Case 6: negative numerator
Source:
$$
[-1,2,0]
$$
Target:
$$
3
$$

We need:
$$
-\frac12 = \frac{Q}{3} + \text{completion}
$$

Choose:
$$
Q=-1
$$

Then leftover:
$$
-\frac12 - \left(-\frac13\right)
= -\frac12 + \frac13
= -\frac16
$$

So:
$$
[-1,3,[-1,6,0]]
$$

Native reading:
- “negative one third with exact completion negative one sixth”

Legacy:
$$
-\frac13 - \frac16 = -\frac12
$$

Correct.

---

## Case 7: negative denominator
Source:
$$
[1,-2,0]
$$

This is legacy-equal to:
$$
[-1,2,0]
$$

Target:
$$
3
$$

So one rebased form is:
$$
[-1,3,[-1,6,0]]
$$

Or if you refuse sign normalization first, you’d still need a rule that gives the same legacy result.

This again shows:
negative denominators are fine in raw ontology, but operational arithmetic really wants a signed quotient convention or normalization pass.

---

# What changed under completion semantics

The major correction is:

Previously, I treated the residual child too naively as:
$$
[S,D,0]
$$

But under completion semantics, the child must be the exact leftover after the top-level fraction has been chosen.

So the correct rebasing law is:

Choose \(Q\) in the target denominator \(B\), then define the child as the exact completion of:

$$
\frac{V}{D} - \frac{Q}{B}
$$

Thus the child is not “the residual numerator from integer division.”
It is:
- the exact leftover value.

That’s the right semantics.

---

# Better corrected generic rule

For closed source:
$$
[V,D,0]
$$
rebased to denominator \(B\),

pick an integer \(Q\), then define child \(C\) so that:

$$
\mathrm{legacy}(C) = \frac{V}{D} - \frac{Q}{B}
$$

and:
$$
\mathrm{rebase}([V,D,0],B) = [Q,B,C]
$$

If the leftover is zero, then:
$$
C = 0
$$

If nonzero, \(C\) must be represented as a finite exact VDR.

That is the semantically correct rebasing form.

---

# Immediate insight
This means rebasing depends on a quotient-choice rule.

For example, should \(Q\) be:
- floor?
- truncation toward zero?
- nearest?
- chosen to minimize child complexity?

That now matters a lot.

And it suggests the next axioms should define:
- quotient selection
- minimal completion
- or canonical rebasing choice

If you want, next I can:
- write the corrected rebase axioms formally with quotient-choice,
- define a canonical quotient rule,
- or keep working examples and compare different quotient-selection strategies.

---

