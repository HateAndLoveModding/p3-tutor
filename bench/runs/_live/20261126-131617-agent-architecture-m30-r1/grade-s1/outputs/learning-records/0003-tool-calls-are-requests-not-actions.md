# The model only requests a tool; the program runs it

Riley correctly worked out the agent loop's structure (q1, q3 of quiz 0001) but, when asked what the model itself does at the moment it calls a tool, twice fell back on the model carrying out the action itself: picking the option where the model "reads the calendar on its own" (q2), and counting a single model call for three tool uses plus the final answer (q4). Both answers show the same misconception, M4: the model emits a text request naming the tool and its arguments, and it is the program, in a separate step, that runs the real code and feeds the result back as a new input.

**Evidence:** quiz 0001, submission s1, items q2 and q4.

**Implications:** M4 is still open and shows up specifically at the model-call boundary, not in the loop's overall shape. A good check next time: have Riley trace a multi-tool request call-by-call (as in q4) and name, at each step, whether the model or the program is acting.
