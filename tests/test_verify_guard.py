"""The verifier's guard (.claude/p3-verify/verify_guard.py).

Each test runs the guard as Claude Code does: a subprocess with the PreToolUse hook input as JSON on
stdin. Exit 0 allows the call; exit 2 blocks it with one line on stderr starting "p3-verify guard:".
"""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUARD = ROOT / ".claude" / "p3-verify" / "verify_guard.py"
AGENT = "p3-verify"


def run_guard(payload=None, *, raw: str | None = None):
    text = raw if raw is not None else json.dumps(payload)
    proc = subprocess.run([sys.executable, str(GUARD)], input=text, capture_output=True, text=True)
    return proc.returncode, proc.stderr


def call(tool: str, agent: str | None = AGENT, cwd: str | None = None, **tool_input) -> dict:
    data = {"tool_name": tool, "tool_input": tool_input}
    if agent is not None:
        data["agent_type"] = agent
    if cwd is not None:
        data["cwd"] = cwd
    return data


def bash(command: str, agent: str | None = AGENT) -> dict:
    return call("Bash", agent, command=command)


class VerifyGuardTest(unittest.TestCase):
    def assertAllow(self, payload):
        code, err = run_guard(payload)
        self.assertEqual(code, 0, f"expected allow for {payload!r}: {err}")
        self.assertEqual(err, "")

    def assertBlock(self, payload, needle: str = ""):
        code, err = run_guard(payload)
        self.assertEqual(code, 2, f"expected block for {payload!r}")
        lines = [ln for ln in err.splitlines() if ln.strip()]
        self.assertEqual(len(lines), 1, err)
        self.assertTrue(lines[0].startswith("p3-verify guard:"), err)
        if needle:
            self.assertIn(needle, err)

    # writes
    def test_writes_only_the_facts_file(self):
        self.assertAllow(call("Write", file_path=str(ROOT / "VERIFIED-FACTS.md"), content="x"))
        self.assertAllow(call("Edit", file_path=str(ROOT / "VERIFIED-FACTS.md"), old_string="a", new_string="b"))
        self.assertAllow(call("Edit", cwd=str(ROOT), file_path="VERIFIED-FACTS.md", old_string="a", new_string="b"))

    def test_blocks_every_other_write(self):
        for path in ("EVAL.md", "tutor/PREFERENCES.md", "reviews/c1-skills.md", "tutor/VERIFIED-FACTS.md",
                     ".claude/agents/p3-verify.md", "../VERIFIED-FACTS.md", "VERIFIED-FACTS.md.bak"):
            self.assertBlock(call("Write", file_path=str(ROOT / path), content="x"), "writes only")
            self.assertBlock(call("Edit", file_path=str(ROOT / path), old_string="a", new_string="b"), "writes only")
        self.assertBlock(call("NotebookEdit", notebook_path=str(ROOT / "x.ipynb")), "writes only")
        self.assertBlock(call("Write", content="x"), "writes only")

    # reads
    def test_reads_except_blind_keys(self):
        self.assertAllow(call("Read", file_path=str(ROOT / "EVAL.md")))
        self.assertAllow(call("Glob", pattern="bench/runs/**/run.json"))
        self.assertBlock(call("Read", file_path=str(ROOT / "bench/compare/abc.key.json")), "key")
        self.assertBlock(call("Grep", pattern="x", path="bench/compare"), "key")

    # bash
    def test_read_only_commands(self):
        for cmd in ("uv run p3 next", "uv run p3 check", "uv run p3 check --final", "uv run p3 report --configs c0-baseline",
                    "git status --short", "git log --oneline -10", "git rev-parse HEAD", "git ls-remote origin HEAD",
                    "git -C . ls-remote origin", "gh run list --limit 5", "gh repo view --json visibility",
                    "ls bench/runs/c0-baseline | wc -l", "git ls-files bench/runs 2>/dev/null"):
            self.assertAllow(bash(cmd))

    def test_blocks_writing_and_model_commands(self):
        for cmd in ("uv run p3 bench --config live --quick", "uv run p3 snapshot c1-skills", "uv run p3 score x",
                    "git commit -m x", "git push", "git fetch", "echo hi > EVAL.md", "rm VERIFIED-FACTS.md",
                    "claude -p hi", "sed -i s/a/b/ EVAL.md", "git ls-remote --upload-pack=evil origin",
                    "gh repo view --web", "gh run view 1 -w", "cat bench/compare/x.key.json"):
            self.assertBlock(bash(cmd))

    def test_powershell_blocked(self):
        self.assertBlock(call("PowerShell", command="Get-ChildItem"), "PowerShell")

    # protocol
    def test_other_agents_untouched(self):
        self.assertAllow(call("Write", agent="p3-guide-something-else", file_path=str(ROOT / "EVAL.md"), content="x"))

    def test_unreadable_input_blocks(self):
        code, err = run_guard(raw="not json")
        self.assertEqual(code, 2)
        self.assertIn("p3-verify guard:", err)


if __name__ == "__main__":
    unittest.main()
