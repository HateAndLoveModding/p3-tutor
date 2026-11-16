# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines context, context rot, just-in-time retrieval, compaction, note-taking and sub-agents. Use for: context and memory design (O3), sub-agent decisions later.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md)
  How a client-side memory tool works, its commands and security duties. Use for: implementing notes as memory.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al., TACL 2024)](https://Huggingface.co/papers/2307.03172)
  Shows accuracy falls when relevant information is in the middle of a long input. Use for: arguing against stuffing whole manuals into context.

## Wisdom (Communities)

- Local: makerspace staff and student users
  Use for: the real questions students ask, to test retrieval against.

## Gaps

- No source yet on retrieval quality (chunking and embedding choices); find one before the retrieval design review.
