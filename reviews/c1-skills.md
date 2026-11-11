# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261111-010848-agent-architecture-m30-r1

**My thoughts:**

#### Lesson

- I liked the check-yourself boxes (5 answers each), common mix-up boxes, learning goals per section, and the bulleted summary of main points.
- I would like an opening quiz to determine prior knowledge.
- I would like a bulleted list of must know points at the beginning of each section.
- I read it faster (~15 minutes) but I wouldn't change the length. 
- I like the visualizations in the original less more but I don't these were bad or not helpful. It might just be Claude's randomness.

#### Quiz

- Overall I loved the quiz. It made me think even though I have probably seen this content 10 times.
- I liked the broader topic range.
- I like that there was only one mcq with 6 options.

#### Grader

- Claude still answered correctly with the correct misconceptions but overall the responses were clearer because the content was more structured.
- I still wasn't satisified with Q2. Maybe Claude should walk through what actually happens. It could also assume that the assistant could read the booking system, explaining why that would still be wrong, and then explaining why it isn’t realistic because my natural instinct is that it is possible for the assistant to read the booking system (I know that answer is wrong for other reasons though).

#### Tutor

- I liked the structure responses.
- I still feel like p01 hints at the right answer (but I kinda blame it on the question).
- I thought p02 was good and didn't hint at the right answer. I feel like the question pushed the student to think about what actually happens.

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

### Round 2

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

## Major review

**Run:** bench/runs/c1-skills/TODO

**Live tries:**

TODO

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Tutor

#### Guardrails

Rating: TODO

TODO

#### Personalization

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
