# Notes

## Mission

- Taking a computer simulation course (see `learning-records/0001-mission-simulation-course.md`).

## Objectives

- O1: sample a stream of unknown length with reservoir sampling (uniform Algorithm R, and one-item weighted sampling), in the context of computer simulation. Taught in `lessons/0001-reservoir-sampling.html`; quizzed in `quizzes/0001.json`.

## Misconceptions (ids shared across the workspace)

- M1: accepting each new record with a fixed probability (such as 1/2) or with k/n using a length not known during the stream.
- M2: an off-by-one in the random range of Algorithm R (such as drawing 1..i with 0-based indices).
- M3: believing early records are favored because they enter the reservoir with certainty, ignoring later evictions.
- M4: in weighted sampling, letting the heaviest candidate always win (replacing only when the new weight is larger).
- M5: confusing the chance of entering the reservoir at a step with the final chance of being in the sample.
- M6: evicting the oldest stored record instead of a uniformly random slot.

## What the learner knows

- Quiz 0001 (s1, graded in `grades/0001-s1.json`): 5 correct, 1 partial, 3 wrong.
- Knows: the k/n result and its k/i x i/n derivation, choosing Algorithm R over flawed schemes, weighted one-item reservoir probabilities (`learning-records/0002-...`).
- Open: M5 (gave k/n when asked for survival given already in; acceptance chance for a specific slot), M2 (fix to an off-by-one kept an off-by-one), and the max-weight bug's effect: thought order matters, missed that other lights vanish from the image (`learning-records/0003-...`).
- The learner called i/n an "acceptance" probability; push the entry-then-survive wording.
- 2026-11-17: believed Python's `random.randint(a, b)` excludes b (it includes both ends; `randrange` and `range` exclude the stop). Related to M2; sent back to the docs. Same day: now reads `randint(1, i)` as inclusive and maps j = 1..k to R[0..k-1] correctly; still to show that these lines need i counted from 1 (the q2 loop counts from 0).

## Working notes

- 2026-11-16: the learner asked for a "short" lesson on reservoir sampling in computer simulation; it was written as 10 minutes.
- 2026-11-17: quiz 0001 written (9 items: 4 numeric, 3 short answer, 2 multiple choice).
