# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).
- The loop needs a stopping condition (such as a step limit) and why: quiz 0001 s1, q3 correct, with every distractor explained.
- Picks a tool from its name and description, matching it to the request (quiz 0001 s1, q6, right part).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Open misconceptions
- M4 (the model runs a tool's action itself, inside one call, instead of only requesting it): shown in quiz 0001 s1, q2 (picked the option where the model reads the calendar itself) and q4 (counted 1 model call instead of 4). See learning record 0003.
- M3 (the model automatically remembers earlier sessions): correctly rejected as an answer choice in q1, but restated unprompted in q6 ("it also remembers on its own ... from earlier sessions"). See learning record 0004 — good lead-in for the upcoming memory lesson.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, graded in `grades/0001-s1.json` (2 correct, 2 partial, 2 wrong), and `submissions/s2.json` four days later, from memory, as spaced practice — not yet graded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits. M3 above is directly relevant to that lesson.
