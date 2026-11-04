# Misconception raised: language models remember past conversations on their own

Riley assumed a language model automatically remembers earlier conversations, so the makerspace assistant would recall what each student said last week. This was corrected in chat: the model only sees the text sent in the current request, so anything remembered between sessions has to be saved by the assistant's code and put back into the context.
Whether the correction landed is not yet confirmed; revisit it when teaching context and memory.

**Evidence:** chat message at the start of the session on context and memory.
**Implications:** Teach the context window, and saving and reloading per-student notes, before any talk of retrieval.
