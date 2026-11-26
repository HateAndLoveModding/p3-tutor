# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).
- Can recognize the agent loop's structure and the need for a stopping condition in multiple choice (quiz 0001, s1: q1, q3 correct).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Open misconceptions
- M4: thinks the model carries out tool calls itself, rather than only requesting them and getting the result back from the program (quiz 0001, s1: q2, q4 wrong). See learning record 0003.
- M3: thinks the model automatically remembers things across sessions on its own; correctly rejected as an MCQ option in q1 but volunteered unprompted in free response in q6. See learning record 0003.
- q5 (why the program sends a tool result back to the model) was partial: has the "what" but not yet the "why" (so the model can decide its next step).

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `s1` is graded (`grades/0001-s1.json`); `s2` is not yet graded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
  When teaching it, explicitly contrast "the program saves and re-feeds something" with "the model remembers on its own," since that is the default assumption M3 shows.
