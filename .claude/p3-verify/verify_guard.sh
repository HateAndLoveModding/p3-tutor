# The verifier's guard hook (see verify_guard.py): find a working Python and hand it the hook's input.
# Modeled on .claude/hooks/guide_guard.sh. With no Python, the verifier's tool call is blocked.
input=$(cat)
if [ -n "$CLAUDE_PROJECT_DIR" ]; then
  guard="$CLAUDE_PROJECT_DIR/.claude/p3-verify/verify_guard.py"
else
  guard="$(dirname "$0")/verify_guard.py"
fi
for py in python3 python py; do
  if "$py" -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)" </dev/null >/dev/null 2>&1; then
    printf '%s' "$input" | "$py" "$guard"
    exit $?
  fi
done
echo "p3-verify guard: no Python found on this machine, so the verifier's tools are off" >&2
exit 2
