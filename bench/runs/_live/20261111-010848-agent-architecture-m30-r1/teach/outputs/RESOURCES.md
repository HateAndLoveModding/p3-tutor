# Agent Architecture Resources

## Knowledge

- [Effective context engineering for AI agents (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, context rot, compaction, notes, just-in-time retrieval, sub-agents. Use for: what to keep in context and how agents manage long tasks.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, accumulation across turns, overflow, compaction and context editing. Use for: exact behavior of the window and token counting.
- [Contextual Retrieval (Anthropic)](https://anthropic.com/news/contextual-retrieval)
  RAG, chunking, embeddings, BM25, and when a knowledge base is small enough to skip retrieval. Use for: designing manual search.
- [Claude docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Notes persisted across sessions (listed from the context-windows page; not read in full). Use for: a concrete cross-session memory pattern.

## Wisdom (Communities)

- Local: the makerspace staff and the senior design team's design reviews
  Use for: which questions students really ask and whether the memory plan fits real use.

## Gaps

- No verified community for agent builders found yet.
