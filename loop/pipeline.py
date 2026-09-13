#!/usr/bin/env python3
"""
TrustMRR Opportunity Loop — automated stage (Steps 1–2 partial).

Fetches TrustMRR public AI API, applies coarse filters, clusters, writes
machine + human reports under loop/runs/YYYY-MM-DD_HHMMSS/.

Deeper X verification (Steps 3–5) is driven by AGENT_PROMPT.md via Claude
or another agent with search tools. This script is safe for cron.

Exit codes:
  0  success
  1  fetch/parse failure
  2  config/path failure
"""

from __future__ import annotations

import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        print(f"Missing config: {CONFIG_PATH}", file=sys.stderr)
        sys.exit(2)
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def fetch_json(url: str, timeout: int, retries: int = 4) -> dict[str, Any]:
    """Fetch with retry+backoff. TrustMRR API intermittently drops TLS
    handshakes (EOF during SSL); 4 retries with 1.5x exponential backoff."""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "opportunity-loop/1.0 (+local; TrustMRR research)",
            "Accept": "application/json",
        },
    )
    # macOS Python ships an outdated default cert chain — use a fresh context.
    ctx = ssl.create_default_context()
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
            break
        except (urllib.error.URLError, ssl.SSLError) as e:
            last_err = e
            if attempt < retries - 1:
                wait = 1.5 ** attempt
                print(
                    f"[fetch] retry {attempt + 1}/{retries} after {wait:.1f}s: {e}",
                    file=sys.stderr,
                )
                time.sleep(wait)
    else:
        # All retries exhausted
        raise last_err if last_err else RuntimeError("fetch failed")
    # TrustMRR may return JSON with odd escapes; try strict then fix
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        cleaned = raw.replace("\\_", "_")
        cleaned = re.sub(r'\\(?!["\\/bfnrtu])', r"\\\\", cleaned)
        return json.loads(cleaned)


def cents_to_usd(v: Any) -> float:
    try:
        return float(v or 0) / 100.0
    except (TypeError, ValueError):
        return 0.0


def normalize(item: dict[str, Any]) -> dict[str, Any]:
    rev = item.get("revenue") or {}
    return {
        "name": item.get("name") or "",
        "slug": item.get("slug") or "",
        "category": item.get("category") or "",
        "description": (item.get("description") or "")[:300],
        "website": item.get("website"),
        "x_handle": item.get("xHandle"),
        "target": item.get("targetAudience"),
        "provider": item.get("paymentProvider"),
        "mrr": cents_to_usd(rev.get("mrr")),
        "last30": cents_to_usd(rev.get("last30Days")),
        "total": cents_to_usd(rev.get("total")),
        "subs": int(item.get("activeSubscriptions") or 0),
        "customers": int(item.get("customers") or 0),
        "on_sale": bool(item.get("onSale")),
        "asking_price": cents_to_usd(item.get("askingPrice")),
        "growth30d": item.get("growth30d"),
        "growth_mrr_30d": item.get("growthMRR30d"),
        "margin": item.get("profitMarginLast30Days"),
        "url": item.get("url") or f"https://trustmrr.com/startup/{item.get('slug')}",
        "markdown_url": item.get("markdownUrl")
        or f"https://trustmrr.com/startup/{item.get('slug')}.md",
    }


def passes_coarse(r: dict[str, Any], cfg: dict[str, Any]) -> bool:
    t = cfg["trustmrr"]
    return (
        r["last30"] >= t["min_last30_usd"]
        or r["mrr"] >= t["min_mrr_usd"]
        or r["subs"] >= t["min_active_subs"]
    )


def cluster_of(r: dict[str, Any], keywords: dict[str, list[str]]) -> list[str]:
    text = f"{r['name']} {r['description']} {r['category']}".lower()
    hits = []
    for name, kws in keywords.items():
        if any(k in text for k in kws):
            hits.append(name)
    return hits or ["other"]


def heuristic_flags(r: dict[str, Any]) -> dict[str, Any]:
    """Cheap auto scores before human/X stage. Not final GO."""
    text = f"{r['name']} {r['description']} {r['category']}".lower()
    demand = 1
    if r["mrr"] >= 100 or r["last30"] >= 200:
        demand += 1
    if r["subs"] >= 20:
        demand += 1
    if r["mrr"] >= 500 or r["subs"] >= 100:
        demand += 1
    if r.get("growth_mrr_30d") and float(r["growth_mrr_30d"] or 0) > 0:
        demand += 1
    demand = min(5, demand)

    # Competition heuristic: popular keywords = higher competition
    hot = [
        "seo",
        "aeo",
        "chatgpt",
        "ugc",
        "video",
        "linkedin",
        "cold email",
        "churn",
        "cancel",
        "resume",
        "headshot",
        "photo",
        "reddit",
    ]
    competition = 2
    if any(h in text for h in hot):
        competition = 4
    if "security" in text or "scan" in text or "vulnerab" in text:
        competition = 3
    if r["mrr"] > 10000:
        competition = max(competition, 4)

    # Mode fit
    mvp_fit = True
    if any(x in text for x in ["hardware", "clinic", "bank", "license", "casino", "sweep"]):
        mvp_fit = False

    verdict = "WATCH"
    if not mvp_fit:
        verdict = "KILL"
    elif demand >= 3 and competition <= 3:
        verdict = "GO_CANDIDATE"  # needs X verify
    elif demand >= 3 and competition >= 4:
        verdict = "KILL_OR_UNBUNDLE"
    elif demand < 3:
        verdict = "WATCH"

    return {
        "demand_heuristic": demand,
        "competition_heuristic": competition,
        "mvp_fit_14d": mvp_fit,
        "auto_verdict": verdict,
    }


def build_report(
    run_id: str,
    cfg: dict[str, Any],
    passed: list[dict[str, Any]],
    clusters: dict[str, list[dict[str, Any]]],
    all_items: list[dict[str, Any]],
) -> str:
    lines = [
        f"# Opportunity Loop Run — {run_id}",
        "",
        f"**Generated (UTC):** {datetime.now(timezone.utc).isoformat()}",
        f"**Source:** `{cfg['trustmrr']['api_url']}`",
        f"**Goal:** ${cfg['goal']['target_mrr_usd']} MRR · {cfg['goal']['mvp_days']}d MVP · ≤${cfg['goal']['marketing_budget_usd']}/30d",
        "",
        "---",
        "",
        "## Auto stage complete (Steps 1–2 partial)",
        "",
        "This run **did not** finish X verification (Steps 3–5). Next:",
        "1. Open `AGENT_PROMPT.md`",
        "2. Feed it this run folder",
        "3. Or: `claude` / agent with search tools on GO_CANDIDATE rows only",
        "",
        f"- Total unique listings: **{len(all_items)}**",
        f"- Passed coarse filter: **{len(passed)}**",
        "",
        "---",
        "",
        "## Clusters (by keyword)",
        "",
    ]
    for cname, items in sorted(clusters.items(), key=lambda x: -len(x[1])):
        sm = sum(i["mrr"] for i in items)
        sl = sum(i["last30"] for i in items)
        lines.append(f"### {cname} — n={len(items)} · ΣMRR≈${sm:.0f} · Σlast30≈${sl:.0f}")
        lines.append("")
        lines.append("| Name | MRR | last30 | subs | auto | slug |")
        lines.append("|---|---:|---:|---:|---|---|")
        for i in sorted(items, key=lambda x: -x["mrr"])[:12]:
            f = i.get("_flags", {})
            lines.append(
                f"| {i['name'][:40]} | ${i['mrr']:.0f} | ${i['last30']:.0f} | {i['subs']} | {f.get('auto_verdict','')} | `{i['slug']}` |"
            )
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## GO_CANDIDATE (needs X verify before PRD)",
            "",
            "| Name | MRR | last30 | demand_h | comp_h | website | x |",
            "|---|---:|---:|---:|---:|---|---|",
        ]
    )
    go = [p for p in passed if p.get("_flags", {}).get("auto_verdict") == "GO_CANDIDATE"]
    if not go:
        lines.append("| — | | | | | | |")
    for p in sorted(go, key=lambda x: -x["mrr"]):
        f = p["_flags"]
        lines.append(
            f"| {p['name'][:36]} | ${p['mrr']:.0f} | ${p['last30']:.0f} | {f['demand_heuristic']} | {f['competition_heuristic']} | {p.get('website') or ''} | @{p.get('x_handle') or '-'} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## KILL_OR_UNBUNDLE / KILL (auto)",
            "",
        ]
    )
    kill = [
        p
        for p in passed
        if p.get("_flags", {}).get("auto_verdict") in ("KILL", "KILL_OR_UNBUNDLE")
    ]
    for p in sorted(kill, key=lambda x: -x["mrr"])[:30]:
        f = p["_flags"]
        lines.append(
            f"- **{p['name']}** ({f['auto_verdict']}) MRR=${p['mrr']:.0f} — {p['description'][:100]}"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## Next agent actions (checklist)",
            "",
            "- [ ] For each GO_CANDIDATE: Google `{category} alternatives 2026`",
            "- [ ] X queries A/B/C/D from config.json `x_queries`",
            "- [ ] Final demand/competition scores (human)",
            "- [ ] Append handles to `handles.csv`",
            "- [ ] If dual gate pass: write `directions/{slug}-prd.md` + 14d + 30d plan",
            "- [ ] Update `state/last_run.json` notes field after agent stage",
            "",
            "## Hard gates (never skip)",
            "",
            f"- demand ≥ {cfg['scoring']['go_min_demand']} AND competition ≤ {cfg['scoring']['go_max_competition']}",
            f"- MVP ≤ {cfg['goal']['mvp_days']} days solo",
            f"- marketing ≤ ${cfg['goal']['marketing_budget_usd']}/30d organic-first",
            "",
        ]
    )
    return "\n".join(lines)


def prune_runs(runs_dir: Path, keep: int) -> None:
    if not runs_dir.exists():
        return
    dirs = sorted([d for d in runs_dir.iterdir() if d.is_dir()], reverse=True)
    for old in dirs[keep:]:
        for f in old.rglob("*"):
            if f.is_file():
                f.unlink()
        for f in sorted(old.rglob("*"), reverse=True):
            if f.is_dir():
                f.rmdir()
        try:
            old.rmdir()
        except OSError:
            pass


def main() -> None:
    cfg = load_config()
    run_id = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    runs_dir = ROOT / cfg["outputs"]["runs_dir"]
    run_dir = runs_dir / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    api_url = cfg["trustmrr"]["api_url"]
    timeout = int(cfg["trustmrr"]["timeout_sec"])

    try:
        payload = fetch_json(api_url, timeout)
    except Exception as e:
        err = {"error": str(e), "run_id": run_id, "url": api_url}
        (run_dir / "error.json").write_text(json.dumps(err, indent=2), encoding="utf-8")
        print(json.dumps(err), file=sys.stderr)
        sys.exit(1)

    # Persist raw
    (run_dir / "trustmrr_raw.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    recent = payload.get("recentlyListedStartups") or []
    deals = payload.get("bestDeals") or []
    by_slug: dict[str, dict[str, Any]] = {}
    for src, label in ((recent, "recent"), (deals, "best_deal")):
        for item in src:
            n = normalize(item)
            if not n["slug"]:
                continue
            if n["slug"] in by_slug:
                by_slug[n["slug"]]["sources"] = list(
                    set(by_slug[n["slug"]].get("sources", []) + [label])
                )
            else:
                n["sources"] = [label]
                by_slug[n["slug"]] = n

    all_items = list(by_slug.values())
    passed = []
    for r in all_items:
        if passes_coarse(r, cfg):
            r["_flags"] = heuristic_flags(r)
            r["clusters"] = cluster_of(r, cfg["cluster_keywords"])
            passed.append(r)

    clusters: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in all_items:
        for c in cluster_of(r, cfg["cluster_keywords"]):
            clusters[c].append(r)

    # Machine-readable filtered
    out_passed = []
    for r in passed:
        row = {k: v for k, v in r.items() if k != "_flags"}
        row.update(r["_flags"])
        out_passed.append(row)

    (run_dir / "filtered.json").write_text(
        json.dumps(out_passed, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # handles template
    handles_header = "handle,type,pain_quote,source_url,status,notes,run_id\n"
    (run_dir / "handles.csv").write_text(handles_header, encoding="utf-8")

    # go candidates csv
    go_lines = ["slug,name,mrr,last30,subs,demand_h,comp_h,verdict,website,x_handle\n"]
    for p in sorted(passed, key=lambda x: -x["mrr"]):
        f = p["_flags"]
        go_lines.append(
            f"{p['slug']},{p['name'].replace(',', ' ')},{p['mrr']:.2f},{p['last30']:.2f},{p['subs']},{f['demand_heuristic']},{f['competition_heuristic']},{f['auto_verdict']},{p.get('website') or ''},@{p.get('x_handle') or ''}\n"
        )
    (run_dir / "candidates.csv").write_text("".join(go_lines), encoding="utf-8")

    report = build_report(run_id, cfg, passed, clusters, all_items)
    (run_dir / "REPORT.md").write_text(report, encoding="utf-8")

    # state
    state = {
        "last_run_id": run_id,
        "last_run_utc": datetime.now(timezone.utc).isoformat(),
        "api_url": api_url,
        "counts": {
            "unique": len(all_items),
            "passed": len(passed),
            "go_candidate": sum(
                1 for p in passed if p["_flags"]["auto_verdict"] == "GO_CANDIDATE"
            ),
        },
        "run_dir": str(run_dir.relative_to(ROOT)),
        "agent_stage": "pending",
        "notes": "",
    }
    state_path = ROOT / cfg["outputs"]["state_file"]
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    (run_dir / "state_snapshot.json").write_text(
        json.dumps(state, indent=2), encoding="utf-8"
    )

    prune_runs(runs_dir, int(cfg["outputs"].get("keep_runs", 30)))

    print(f"OK run_id={run_id}")
    print(f"report={run_dir / 'REPORT.md'}")
    print(json.dumps(state["counts"]))


if __name__ == "__main__":
    main()
