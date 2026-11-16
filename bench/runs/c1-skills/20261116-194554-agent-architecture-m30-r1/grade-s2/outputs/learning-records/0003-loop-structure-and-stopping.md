# Riley knows the loop's structure but still needs the stop condition and who runs the tools

On the spaced-practice attempt of quiz 0001, Riley correctly identified the agent loop (q1), that the model outputs a tool request rather than running anything (q2), and that the tool result goes back as the next model input (q5).
Two misconceptions remain open: M6 (an agent left running will eventually succeed, so it needs no stopping condition) and M4 (the model runs the tools itself), which showed in the reasoning for q4 despite the right count of 4.
A third gap: Riley relies on the tool's name alone and not its full description to explain how the model picks a tool (q6).

**Evidence:** quiz 0001, submission s2, items q1, q2, q3, q4, q5, q6.

**Implications:** Before moving to context and memory, revisit stopping conditions (step limits, cost caps) and have Riley trace a request showing what the program does between model calls. Tie tool descriptions to Riley's own makerspace tools.
