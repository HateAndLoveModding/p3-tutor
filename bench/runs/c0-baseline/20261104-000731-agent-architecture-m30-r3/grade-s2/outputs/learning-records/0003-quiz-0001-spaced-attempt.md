# Loop and request/result split are mostly solid; stopping conditions and the model-runs-tools slip (M4) remain

On the spaced quiz 0001 attempt (s2), Riley correctly identified what makes an agent, that the model only outputs a tool request, and that the result returns as the next input. Two things remain open: Riley believes a stuck agent will eventually succeed without a stopping condition (M6, q3), and the explanation for q4 still says the model runs the tools itself (M4), though the count was right.
Riley also relied on the tool's name alone to explain tool choice (q6), so tool descriptions need a lesson.

**Evidence:** quiz 0001, submission s2, items q1-q6; grades/0001-s2.json.

**Implications:** Before building on context and memory, revisit stopping conditions and the model/program split briefly. Link tool descriptions to the tool-description skill in MISSION.md.
