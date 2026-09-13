# Scheduling the Opportunity Loop

You only need to attach a timer. The loop itself is fixed under `loop/`.

## What runs automatically vs agent

| Stage | Command | Needs network | Needs LLM/agent |
|---|---|---|---|
| **A — Auto** | `./loop/run.sh` | Yes (TrustMRR API) | No |
| **B — Agent** | Claude with `loop/AGENT_PROMPT.md` | Yes (search/X) | Yes |

Cron should run **Stage A** every week.  
Stage B: same day manually, or second cron that opens Claude, or a CI job with an agent.

---

## 1) macOS / Linux — cron (recommended)

```bash
# Edit crontab
crontab -e

# Monday 09:17 local time — weekly TrustMRR pull + filter
17 9 * * 1 /Users/jerry/code/10k-in-month/loop/run.sh >> /Users/jerry/code/10k-in-month/loop/runs/cron.log 2>&1
```

Make executable once:

```bash
chmod +x /Users/jerry/code/10k-in-month/loop/run.sh
```

Test:

```bash
/Users/jerry/code/10k-in-month/loop/run.sh
cat /Users/jerry/code/10k-in-month/loop/state/last_run.json
```

---

## 2) macOS launchd (if you prefer GUI-less always-on)

Create `~/Library/LaunchAgents/com.10k.opportunity-loop.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.10k.opportunity-loop</string>
  <key>ProgramArguments</key>
  <array>
    <string>/Users/jerry/code/10k-in-month/loop/run.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key>
    <integer>1</integer>
    <key>Hour</key>
    <integer>9</integer>
    <key>Minute</key>
    <integer>17</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>/Users/jerry/code/10k-in-month/loop/runs/launchd.out.log</string>
  <key>StandardErrorPath</key>
  <string>/Users/jerry/code/10k-in-month/loop/runs/launchd.err.log</string>
  <key>WorkingDirectory</key>
  <string>/Users/jerry/code/10k-in-month/loop</string>
</dict>
</plist>
```

```bash
launchctl load ~/Library/LaunchAgents/com.10k.opportunity-loop.plist
launchctl start com.10k.opportunity-loop
```

---

## 3) Claude Code `/loop` (agent stage on a schedule)

After Stage A has produced a run:

```text
/loop 7d Read loop/state/last_run.json and execute loop/AGENT_PROMPT.md fully. Write VERDICT.md and GO direction packages into the latest run folder. Do not rebuild methodology.
```

Or one-shot without wait:

```text
Run loop/AGENT_PROMPT.md against the latest loop/runs/* folder.
```

---

## 4) GitHub Actions (optional remote)

`.github/workflows/opportunity-loop.yml`:

```yaml
name: opportunity-loop
on:
  schedule:
    - cron: "17 1 * * 1"   # Monday 01:17 UTC ≈ adjust to taste
  workflow_dispatch:
jobs:
  stage-a:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run TrustMRR pipeline
        run: |
          chmod +x loop/run.sh
          ./loop/run.sh
      - name: Upload run artifact
        uses: actions/upload-artifact@v4
        with:
          name: opportunity-run
          path: loop/runs/
```

Agent stage still needs a model provider job or local Claude.

---

## 5) After each scheduled run (human 15 min)

1. Open `loop/state/last_run.json` → `run_dir`  
2. Open `REPORT.md`  
3. Either:
   - paste AGENT_PROMPT into Claude, or  
   - skip if no GO_CANDIDATE  
4. If GO: open `directions/{slug}.md` and decide build / not  

---

## 6) Files the scheduler must not touch

- `loop/config.json` — thresholds (edit only when changing strategy)
- `loop/AGENT_PROMPT.md` — agent contract
- `loop/pipeline.py` — auto stage
- Historical `loop/runs/*` — append-only audit trail

---

## 7) Failure modes

| Symptom | Fix |
|---|---|
| `error.json` in run folder | TrustMRR down / network; retry later |
| empty GO_CANDIDATE | Normal; market week may be quiet |
| stale scores | Run agent stage; heuristics are not final |
| disk growth | `keep_runs` in config.json (default 30) |
