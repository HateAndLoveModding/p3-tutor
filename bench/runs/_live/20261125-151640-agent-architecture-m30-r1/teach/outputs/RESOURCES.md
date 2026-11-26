# Agent Architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  The primary source for Lesson 1 (O3). Defines the context window as a finite, degrading resource ("context rot"), and lays out just-in-time retrieval and structured note-taking as the two main ways to manage it. Use for: anything on context budgeting, retrieval, or agent memory design.
- [Docs: "Context windows" (Claude Platform Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Exact mechanics: what counts toward the window (system prompt, messages, tool results, tool definitions, output), how tokens accumulate turn over turn, billing, and overflow behavior. Use for: precise token-accounting questions and cost reasoning.
- [Docs: "Memory tool" (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A concrete, file-based implementation of notes-as-memory (a `/memories` directory with view/create/str_replace/delete/rename commands), plus the multisession software-development pattern (progress log, checklist, read-back at session start). Use for: how to actually implement cross-session memory when the mission gets to building the assistant.

## Gaps

- No community or forum source yet for this mission; add one if a need for peer troubleshooting comes up (e.g. a Discord or forum for builders of small, cost-constrained agents).
