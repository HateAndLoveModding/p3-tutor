# Mixes up stage chances with overall chances in Algorithm R (M5, open)

Given that a record is already in the reservoir, the learner answered with the unconditional k/n instead of the survival chance i/n, and computed the chance of a specific slot as the acceptance chance alone.
Their fix for an off-by-one bug also kept an off-by-one (M2), and they believed the max-weight replacement bug depends on arrival order.
Next work: tracing conditional and per-slot probabilities step by step; the same step was done correctly in the weighted case.

**Evidence:** quiz 0001, submission s1, items q1, q2, q4, q8.
