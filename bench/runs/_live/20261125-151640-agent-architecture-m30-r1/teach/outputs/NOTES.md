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
- Taught Objective O3 (context window, what's kept between steps vs. sessions, retrieval and notes as memory) as a 30-minute lesson: `lessons/0001-context-and-memory-in-an-agent.html`.
  Worked examples used the makerspace assistant's laser-cutter training flow (token growth across turns) and a Monday/Wednesday session split (certification persisted via a booking-system write, not model memory), plus a combined retrieval + notes example (manual search vs. a per-student training note).
  Not yet checked by quiz: whether Riley can himself tell apart a fact that needs retrieval from one that needs a written note, under a new scenario.
- Next in the mission, once O3 is checked: workflows versus agents (when to use a fixed pipeline instead of a loop), which the mission's "argue which parts should be a fixed workflow" success criterion needs.
