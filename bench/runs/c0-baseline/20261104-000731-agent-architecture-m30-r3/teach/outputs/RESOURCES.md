# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, attention budget, compaction, structured note-taking, up-front vs just-in-time retrieval, sub-agents. Use for: anything on context and memory design.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates, compaction and context editing. Use for: precise facts about how requests fill the window.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A file-based memory design for notes across sessions. Use for: designing the assistant's saved student notes.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al.)](https://ar5iv.labs.arxiv.org/html/2307.03172)
  Accuracy depends on where in a long input the relevant text sits. Use for: evidence that long contexts are not used uniformly (tested on earlier models).

## Wisdom (Communities)

## Gaps

- No community has been vetted yet for agent builders. Until one is, use the team's design reviews and the makerspace staff.
