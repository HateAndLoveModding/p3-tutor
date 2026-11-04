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
- Lesson 0001 (context-and-memory, O3, 30 min) written with quiz 0002 and a cheat sheet; not yet taken. Worked example uses token arithmetic; the learner's first practice on "re-sent every call" is the numeric item q3.
- Misconception ids in use: M3 (the model remembers earlier chats by itself), M4 (the model runs tools itself), M6 (an agent needs no stopping condition), M7 (a big window means context needs no curation or persists between calls).
- Communities: none proposed yet; no verified source found.
- Context and memory was next in the mission, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
