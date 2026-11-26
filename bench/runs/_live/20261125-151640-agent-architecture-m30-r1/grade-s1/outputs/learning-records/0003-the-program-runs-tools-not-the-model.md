# The model requests a tool; the program runs it

Riley still slips into picturing the model as the thing that directly runs a tool (opening the booking system, running all three tools inside one call) rather than emitting one request at a time for the program to carry out. This showed up on quiz 0001, missing both items built to test it.

**Evidence:** quiz 0001, submission s1, q2 (picked "it read the calendar by opening the booking system on its own") and q4 (answered 1 model call for a run with three tool requests, as if the model ran all three itself).

**Implications:** This is misconception M4, and it's the main thing to clear up before going further — it will also trip up any explanation of memory or retrieval if left unfixed, since those are also things the program manages around the model, not things the model does itself. A related but separate belief, M3 (the system remembers past choices across sessions automatically), showed up in the same submission (q6) and is worth flagging again once context and memory is taught.
