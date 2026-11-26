# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic)](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  Primary source on the context window as a limited "attention budget," what counts as context during an agent run, and memory techniques (compaction, structured note-taking, just-in-time retrieval). Use for: context window, what persists within a run vs. across sessions, notes as memory.
- [Docs: "Token counting" (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
  Defines a token and explains why providers count and bill by tokens, not words or messages. Use for: what a token is, why context size drives cost.
- [Article: "What is Retrieval-Augmented Generation (RAG)?" (AWS)](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
  Plain explanation of indexing documents, matching a query against them, and injecting only the relevant results into the prompt. Use for: retrieval as a way to answer from documents too large to fit in context.

## Gaps

- No source yet on multi-agent architectures or the workflow-vs-agent decision (needed for later objectives O4 and O5).
