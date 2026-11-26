# Agent architecture Resources

## Knowledge

- [Anthropic: "Effective context engineering for AI agents"](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  Ties together context rot, compaction, structured note-taking, and just-in-time retrieval in one place. Use for: deciding what belongs in context versus what should be retrieved or noted instead.
- [Claude Docs: "Context windows"](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official reference for exactly what counts toward a call's context window (system prompt, messages, tool results, tool definitions), token ceilings by model, and overflow behavior. Use for: precise mechanics of context and cost.
- [Anthropic: "Contextual retrieval in AI systems"](https://www.anthropic.com/engineering/contextual-retrieval)
  How retrieval over a chunked document works, why naive chunking loses context, and how adding context to chunks improves search. Use for: designing a tool that searches long manuals.
- [Anthropic: "The components of agent memory"](https://www.anthropic.com/research/components-of-agent-memory)
  Deeper framework for persistent memory beyond one note: transcripts, notes, representations, and injected context. Use for: once basic notes and retrieval feel solid and the assistant's memory needs grow.

## Gaps

- No community or forum identified yet for this mission; Riley's constraints (three hours a week, a five-week deadline) point toward official docs over discussion, so this has not been pursued.
