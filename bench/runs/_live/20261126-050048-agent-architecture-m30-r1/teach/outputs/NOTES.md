# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has not met workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Taught Lesson 1 (`lessons/0001-context-and-memory-in-agents.html`, objective O3, 30 minutes): the context window and what counts toward it, what carries forward within one task versus between separate sessions, and retrieval versus notes as the two patterns for agent memory. Cheat sheet at `cheatsheets/0001-context-and-memory-decision-rule.html`.
  Not yet checked: whether Riley can apply the retrieval-vs-note decision rule to a new case unprompted, or still reaches for "store everything" by default. A `/quiz` on this lesson would test it.
- Next in the mission, once O3 is checked: likely workflows versus agents (when a fixed pipeline beats a model choosing its own actions) or multi-agent systems, both named directly in the mission's success criteria.
