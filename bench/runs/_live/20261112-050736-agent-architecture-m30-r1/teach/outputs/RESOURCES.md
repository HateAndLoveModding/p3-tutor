# Agent Architecture Resources

## Knowledge

- [Effective context engineering for AI agents (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, attention budget, just-in-time retrieval, compaction, structured note-taking, sub-agents. Use for: any decision about what the assistant keeps in context.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, accumulation across turns, overflow behavior. Use for: how big a request is and what limits apply.
- [Claude docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side file-based memory across sessions, handler duties and security. Use for: saving notes between visits.
- [Contextual Retrieval (Anthropic)](https://anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, BM25, contextual chunks, reranking, with reported failure rates (vendor measurements). Use for: finding the right page in a long manual.

## Wisdom (Communities)

No community verified yet; see Gaps.

## Gaps

- A moderated, high-signal community for people building tool-using agents. Find and verify one before recommending it.
