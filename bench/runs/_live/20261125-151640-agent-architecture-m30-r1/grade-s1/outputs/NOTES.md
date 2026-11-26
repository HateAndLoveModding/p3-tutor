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

## Open misconceptions
- M4 (the model runs a tool itself, rather than emitting a request the program carries out): shown on quiz 0001 s1, q2 and q4 (learning record 0003). Still open.
- M3 (the system remembers past sessions or past choices automatically, with no explicit memory step): shown on quiz 0001 s1, q6's added claim; correctly avoided as a wrong option in q1. Worth retesting once context and memory is taught.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `submissions/s1.json` is now graded (`grades/0001-s1.json`): 2 correct (q1, q3), 2 partial (q5, q6), 2 wrong (q2, q4). `submissions/s2.json` is still ungraded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
