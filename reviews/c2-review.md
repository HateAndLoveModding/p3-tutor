# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** work/p3-tutor/bench/runs/_live/20261125-151640-agent-architecture-m30-r1

**My thoughts:**

I want to add a quiz reviewer subagent. 

I want the subagent to check and make sure the skill criteria was followed and ensure that whether the question is correct and the student has to identify that, or the question is wrong and the student has to correct it, is random.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: These thoughts ask for a reviewer that checks the quiz skill's own criteria and, specifically, that scenario items asking the learner to judge or fix something do not all land on the same side (always flawed, or always sound) in a guessable pattern; quiz-reviewer's checklist covers the skill's stem, goal-coverage, mcq and key-rationale rules and adds a check that lists each such item's side so a one-sided or ordered pattern shows up, and the quiz skill now drafts into drafts/, sends the draft to quiz-reviewer, revises for up to two passes, and writes the final quiz and key once the loop ends.

### Round 2

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

### Round 3

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

## Major review

**Run:** bench/runs/c2-review/TODO

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

### Compared with the previous step

TODO

### What the next step should fix

TODO
