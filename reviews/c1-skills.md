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

Write a quiz skill.

Thoughts about the quiz skill:

- Most of the questions should be free response
- When a multiple choice question is used, there should be at least 5 answer options and a maximum of 8.
- On a multiple choice question, none of the answers should be obviously nonsense.
- Do not generate questions that don’t need the topic to answer.
- Most of the problems should focus on problem-solving and real-world scenarios about the learning goal.
- Each quiz question should address one learning goal.
- There should be 2-3 questions per learning goal.
- The stem should not contain the answer.
- Each question should have exactly one best answer.
- Questions on the same learning goal must test different angles, such as recall, apply and diagnose, and that knowing one fact should not answer them all.
- The answer keys in your notes should explain each distractor and common wrong answers. 

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
