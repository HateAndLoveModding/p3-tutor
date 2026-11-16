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

**Run:** work/p3-tutor/bench/runs/_live/20261111-010848-agent-architecture-m30-r1

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

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: Quizzes were still written by /teach under a guide that allowed mostly mcq with three to five options; a quiz skill of its own makes most items free-response scenarios that need the topic, gives mcq items five to eight plausible options, puts two or three items on each learning goal from different angles, and has the key explain every distractor and common wrong answer, as these thoughts ask.

### Round 2

**Run:** work/p3-tutor/bench/runs/_live/20261112-050736-agent-architecture-m30-r1

**My thoughts:**

I currently have no complaints about the quiz after adding the quiz skill. I feel like it addressed my main issues using the quiz and there is nothing that I would change at this time. 

Write a grade skill.

Thoughts about the grade skill:

- Each option in a multiple choice question should be explained and why the option is right or wrong.
- When an answer is wrong, explain the reason and don't just assert it. 
- Explain every multiple choice answer option even if the student is right. 
- Walk through what would actually happen in each case.
- Address misconceptions that a student may have by assuming them to be true in a hypothetical sense and then showing why that is still wrong.
- Address multiple misconceptions that the student may have across multiple questions and answers.
- The grading of the free response questions is good but ensure the grder states the right, wrong, and why.
- Answer directly.
- Use analogies or real-world scenarios to explain answers.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md
- Why: Grading still ran inside /teach under a guide that asked for two to four sentences per item and only explained the chosen option; a grade skill of its own explains every mcq option by id even on a correct pick, gives right, wrong and why for free response, walks each wrong answer through what would actually happen, follows each misconception as if it were true until it breaks, uses a scenario or analogy where it helps, and ties a misconception shared by several items together, as these thoughts ask.

### Round 3

**Run:** work/p3-tutor/bench/runs/_live/20261116-133541-agent-architecture-m30-r1

**My thoughts:**

I thought that the grader skill did great. It clearly explained each answer option and directly said whether it was right or wrong. I feel like the grader does not always fully explain why the hypothetical assumptions are wrong. The sections about the hypothetical assumptions should be just as structured as the rest of the response, clearly stating the right, wrong, and why.

I do not want to worry about that yet though.

Write a tutor skill.

Thoughts about the tutor skill:

- Things should be explained with headers and bullet points.
- When evaluating a plan, code, or similar, things that I did well, things that need work, and why should all be clearly stated. Point to the next reachable step.
- If evaluating a claim or my understanding, the right, wrong, and why should be clearly stated.
- Analogies of everyday actions or situations should be used when explaining things and be simple.
- The questions you ask should not hint at the right answer in a multiple choice question.
- Ask for the student's reasoning.
- Have the student identify where the problem actually lives.
- Do not give quiz answers before grading. Ever.
- Identify where the student's misconception is and lead them back to the lesson. Tell them what is wrong but not then what the correction is. The student should figure that out on their own.
- Tie answers back to the project.
- Decline out of scope requests.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: Chat replies still came from /teach under a tutoring guide that asked for short paragraphs with no headings and for stating the correction of a misconception; a tutor skill of its own answers with headers and bullets, states right, wrong and why for claims and done well, needs work and why with a next reachable step for plans and code, uses simple everyday analogies, ties each reply to the project, asks for the learner's reasoning and where the problem lives, never gives or hints at a quiz answer before grading, points out a misconception and sends the learner back to the lesson without giving the correction, and declines out-of-scope requests, as these thoughts ask.

### Round 4

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
