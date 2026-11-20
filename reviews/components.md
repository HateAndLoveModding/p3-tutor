# Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: To make sure the quizzes challenge the student and ensure that they actually understand everything. It should be a skill because it requires a repeatable procedure inside the active conversation.
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: The quizzes now encourage critical thinking and actually test understanding with more free response questions or mcq with more options. Example with: c1-skills q3. Example without: 20261111-010848-agent-architecture-m30-r1 q1.
- Kept in final: TODO

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: To ensure that each multiple choice option is explained fully and clearly. It should be a skill because it requires a repeatable procedure inside the active conversation.
- With and without: reviews/c1-skills.md, Round 2 (without) and Round 3 (with)
- Review: The multiple choice options are now all explained thouroughly. Example with: c1-skills grade-s1 q1. Example without: 20261112-050736-agent-architecture-m30-r1 grade-s1 q1.
- Kept in final: TODO

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: Attempt to help give the tutor more guidance on how to respond without giving away the answer. It should be a skill because it requires a repeatable procedure inside the active conversation.
- With and without: reviews/c1-skills.md, Round 3 (without) and Round 4 (with)
- Review: I feel like it did better not just stating the correction to the student's misconception and instead telling them where to find that information and encouraging them to find it themself. Example with: c1-skills p03. Example without: c0-baseline 20261104-000731-agent-architecture-m30-r3 p03.
- Kept in final: TODO

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: To add more structure to the lessons and help me actually learn the content. It should be a skill because it requires a repeatable procedure inside the active conversation.
- With and without: reviews/c1-skills.md, Round 4 (without) and the c1-skills full run (with)
- Review: The structure is great now and it is much more condusive to my learning style. I love the quiz at the beginning of the lesson. Example with: "Pre-quiz 1
Covers Section 1: The context window
The makerspace assistant is answering a question. Which of these counts toward the context window of that model call?
Only the student's latest message and the reply the model writes
The model's training data plus everything sent in the request
The system prompt, tool definitions, all messages, tool results and the new output
The system prompt and every file stored on the assistant's server"
Example without: "Warm-up 3 min
Last time you traced a request through the agent loop. Before we add memory, pull that loop back out of your head.
Recall
A student asks, "Is the laser cutter free tomorrow at 3 pm?" The assistant has a calendar tool. Without looking back: who actually runs the tool, the model or the program around it? And after it runs, what happens to the result?
Check your answer"
- Kept in final: TODO
