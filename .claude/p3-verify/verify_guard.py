"""The verifier's guard: a PreToolUse hook that keeps p3-verify (claude --agent p3-verify) read-only,
except for its one file of facts, VERIFIED-FACTS.md at the repo root.

.claude/agents/p3-verify.md registers it, through verify_guard.sh, which finds a Python to run it.
Claude Code sends the hook's input as JSON on stdin. Exit 0 lets the tool call run; exit 2 blocks it,
and the agent reads the one line printed on stderr. The rules are:

- Write, Edit, MultiEdit and NotebookEdit: only VERIFIED-FACTS.md at the repo root.
- Read, Grep and Glob: anything except a blind comparison's key, bench/compare/*.key.json.
- PowerShell: nothing (the verifier uses Bash).
- Bash: the Guide's read-only commands, checked by the course's own guard
  (.claude/hooks/guide_guard.py, imported, never changed), plus `git ls-remote`, so the verifier can
  compare the local commit with GitHub's without a fetch. `gh ... --web` is refused, because it opens
  a browser.

tests/test_verify_guard.py covers these rules.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent  # .claude/p3-verify/ -> repo root
sys.path.insert(0, str(ROOT / ".claude" / "hooks"))

import guide_guard as gg  # noqa: E402  (the course's guard; its parser and command checks)

AGENT = "p3-verify"
FACTS = "VERIFIED-FACTS.md"
WRITERS = ("Write", "Edit", "MultiEdit", "NotebookEdit")


def check_segment(words: list[str]) -> None:
    name, args = gg.name_of(words[0]), words[1:]
    if name == "git":
        rest = args
        while rest and rest[0] in ("-C", "--no-pager"):
            rest = rest[2:] if rest[0] == "-C" else rest[1:]
        if rest[:1] == ["ls-remote"]:
            if any(a.startswith("--upload-pack") or a.startswith("-u") for a in rest[1:]):
                raise gg.Blocked("git ls-remote with --upload-pack, which runs a program")
            return
    if name == "gh" and any(a in ("--web", "-w") for a in args):
        raise gg.Blocked("gh --web, which opens a browser")
    gg.check_segment(words)


def check_bash(command: str) -> None:
    """The course guard's check_bash, with this guard's check_segment."""
    low = command.replace("\\", "/").lower()
    if gg.KEY in low:
        raise gg.Blocked("it never opens a blind comparison's key")
    if "bench/compare" in low:
        raise gg.Blocked("it never reads the blind comparison folder (bench/compare/); the picks stay blind until the student runs p3 compare --reveal")
    segments = gg.split(command)
    if not segments:
        raise gg.Blocked("an empty command")
    for words in segments:
        for word in words:
            if gg.KEY in word.lower():
                raise gg.Blocked("it never opens a blind comparison's key")
        check_segment(words)


def is_facts_file(path_text: str, cwd: str | None) -> bool:
    if not path_text:
        return False
    path = Path(path_text)
    if not path.is_absolute():
        path = Path(cwd or os.getcwd()) / path
    try:
        return path.resolve() == (ROOT / FACTS).resolve()
    except OSError:
        return False


def decide(data: dict) -> str | None:
    """None to allow the call, or the reason to block it."""
    agent = data.get("agent_type")
    if agent is not None and agent != AGENT:
        return None
    tool = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}
    if tool in ("Read", "Grep", "Glob"):
        named = " ".join(str(tool_input.get(k) or "") for k in ("file_path", "path", "pattern", "glob")).lower()
        if gg.KEY in named or (tool == "Grep" and "bench/compare" in named.replace("\\", "/")):
            return "the verifier never opens a blind comparison's key (bench/compare/*.key.json)"
        return None
    if tool == "PowerShell":
        return "the verifier uses Bash, not PowerShell"
    if tool == "Bash":
        try:
            check_bash(str(tool_input.get("command") or ""))
        except gg.Blocked as exc:
            return (f"the verifier only reads, so it cannot run this: {exc}. "
                    "Tell the student who runs it instead: the Builder (give the exact sentence to say) or the student in a plain terminal (give the exact command).")
        return None
    if tool in WRITERS:
        target = str(tool_input.get("file_path") or tool_input.get("notebook_path") or "")
        if is_facts_file(target, data.get("cwd")):
            return None
        return f"the verifier writes only {FACTS} at the repo root; every other file is the student's or the Builder's"
    return None


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        print("p3-verify guard: could not read the hook input, so the call is blocked", file=sys.stderr)
        return 2
    reason = decide(data if isinstance(data, dict) else {})
    if reason is None:
        return 0
    print(f"p3-verify guard: {reason}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
