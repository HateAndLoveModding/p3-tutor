# Riley knows the loop and stopping conditions, but still believes the model runs tools and remembers by itself

Riley identified the agent loop (q1), chose a step limit as the safeguard against a repeating agent (q3), and knows the model picks tools from descriptions the program supplies (q6).
Two misconceptions are open: M4, that the model runs the tools itself (q2, q4), and M3, that the model remembers earlier sessions automatically (q6). The answer to q5 gave what the program does with a tool result but not why.

**Evidence:** quiz 0001, submission s1, items q1-q6.

**Implications:** Teach that the program runs each tool and makes a separate model call per step, and that memory has to be saved and re-supplied by the program, before building on context and memory. Compare with submission s2 for change.
