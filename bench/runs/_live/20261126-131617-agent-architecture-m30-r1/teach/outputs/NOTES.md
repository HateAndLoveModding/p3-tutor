# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- 2026-11-26: Taught `lessons/0001-context-and-memory.html`, objective O3 (context window, what persists within a run vs. across sessions, retrieval and notes), 30 minutes. Builds on the agent loop (learning record 0002) and reuses M3 (automatic memory of past conversations) from quiz 0001.
  New misconceptions introduced for future quizzes on O3: M7 (a short new message means a cheap call, ignoring resent history), M8 (important facts save themselves between sessions without an explicit write), M9 (retrieval searches the open internet rather than an indexed local corpus), M10 (retrieval makes notes unnecessary, since search can find any fact once it's true).
  Cheat sheet at `cheatsheets/context-and-memory.html` compares context window, within-session memory, between-session memory, retrieval and notes.
- Next in the mission: deciding when a part of the assistant should be a fixed workflow rather than an agent (O4), and when splitting work across several agents pays off (O5).
