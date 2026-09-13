#!/usr/bin/env bash
# Install the opportunity-loop skill into ~/.claude/skills/
# Re-run to update after pulling the repo.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.claude/skills/opportunity-loop"
mkdir -p "$DEST"
cp "$ROOT/SKILL.md" "$DEST/SKILL.md"
echo "✓ Installed: $DEST/SKILL.md"
echo "  (re-run this script after pulling to update)"
