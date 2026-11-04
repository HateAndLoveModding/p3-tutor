# Open misconceptions: the model runs the tools (M4) and remembers across sessions (M3)

On quiz 0001, submission s1, Riley understood the loop and that the model picks tools from their descriptions. Riley also believed the model runs the tools itself (M4, items q2 and q4, which gave 1 model call instead of 4). And Riley believed the model remembers earlier sessions on its own (M3, item q6).

**Evidence:** quiz 0001, submission s1, items q2, q4 and q6. Grades are in `grades/0001-s1.json`.

**Implications:** Before building on the loop, re-check that every step is a separate model call and that the program runs each tool. Context and memory lessons should start from the point that the model sees only its current input, and that anything saved between sessions is stored and re-supplied by the program. Submission s2 may show whether this was corrected.
