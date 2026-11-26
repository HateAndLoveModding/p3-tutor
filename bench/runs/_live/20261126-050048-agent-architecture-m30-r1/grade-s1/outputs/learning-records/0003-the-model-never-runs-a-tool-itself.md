---
status: active
---

# Open misconception: Riley thinks the model carries out tool calls itself

Riley believes the model directly executes tools (reads the calendar, runs the three tools in a row) rather than only ever requesting a tool call and waiting for the program to run it and report back. This is the gap learning record [[0002-the-agent-loop]] flagged as "not yet checked," and quiz 0001 confirms it is open, not a slip: it showed up on two independent items, a multiple-choice question and a numeric one, with the same reasoning both times.

A related but separate belief also surfaced: Riley correctly rejected "automatic memory of every earlier conversation" when it was offered as a multiple-choice option, but volunteered the same belief unprompted in a free-response answer about tool selection, attached specifically to remembering which tool fit a request across sessions. The belief seems to survive recognition but resurface in generation.

**Evidence:** quiz 0001, submission s1, items q2 and q4 (model runs tools itself); item q6 (automatic cross-session memory, stated despite correctly rejecting it in q1).

**Implications:** Before moving on to context and memory, trace one multi-tool request on paper and write out literally what text the model outputs at each step, to make concrete that it is always a request, never an execution. When memory is taught, explicitly contrast "the program saves and re-feeds something" with "the model remembers on its own," since Riley's q6 answer shows the second framing is the default assumption.
