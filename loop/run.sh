#!/usr/bin/env bash
# Opportunity Loop entrypoint — safe for cron / launchd / GitHub Actions
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

export PYTHONUNBUFFERED=1
LOG_DIR="$ROOT/runs"
mkdir -p "$LOG_DIR"

TS="$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$LOG_DIR/cron_${TS}.log"

{
  echo "=== opportunity loop start $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  python3 "$ROOT/pipeline.py"
  echo "=== opportunity loop end $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  echo "Next: run agent stage with AGENT_PROMPT.md on latest runs/*"
} 2>&1 | tee "$LOG_FILE"

# Print latest run path for schedulers
if [[ -f "$ROOT/state/last_run.json" ]]; then
  python3 -c "import json;print(json.load(open('state/last_run.json'))['run_dir'])"
fi
