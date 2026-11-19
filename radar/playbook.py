"""Playbooks: induce reusable plays from the moves the agent found in each investigation.

Modelled on Stringers' playbook (research/stringers-plays-analysis.md). A play is one concrete action a solo builder
can take this week, in one of three categories (finding a direction, growth, monetization), backed by two or more
products that took it recently. Each play page carries: recipe, mechanism, five steps (instruction + evidence that names
the cases), the cases (what they did, what happened, causality hard/medium/weak), tried-it-didn't-work, who it suits /
prerequisites / risks, and a closing note that says what checking changed.

Two LLM passes run after `investigate`:
  1. draft  - group the per-brief moves (rep["plays"]) into plays and write every section;
  2. verify - per play, re-read each case's full brief: regrade causality, drop cases and steps the evidence doesn't
              support, mark steps no case shows as inferred, check the counter-examples, record what changed.
The result goes to data/playbook.json (committed, so ids and history survive cache loss). Without LLM keys the file is
left as it is and the site falls back to mechanism groups. Breakouts that faded by D+7 are added as counter-examples
from the track record when the page is built.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

from . import synth
from .investigate import BASE_URL, CAUSALITY, MODEL, PLAY_CATEGORIES, agent_available

PATH = Path(__file__).resolve().parent.parent / "data" / "playbook.json"
WINDOW_DAYS = 60
MAX_ROWS = 240

RULES = """A play is ONE concrete action a solo builder can take this week, not a trend or a category. Categories:
- direction: where to build — demand someone else creates (an official date, a shutdown/price change, an open-source hit,
  people already paying in a chat/community/crowdfunding, a leader that stopped updating);
- growth: one repeatable distribution move, with the channel, the hook format and the cadence;
- monetization: where and how to charge — the moment that is locked, the plan shape, the price structure.
Write every section like this:
- recipe: imperative, max 45 words, no product names, with the specific detail that makes it work (a number, a moment,
  a channel). Good: "Add an annual plan at 'pay 10 months, use 12' and default the pricing toggle to it". Bad: "Use annual plans".
- why: one sentence, the mechanism; add its own caveat if the cases show one.
- steps: exactly 5 when the cases support it (fewer otherwise), in this arc: 1 select (when this play applies, how to pick
  the target, when it doesn't), 2 shape the offer (first sentence / first screen / first action), 3 prepare to catch the
  traffic, 4 execute the move (copy, price, cadence, channel, with numbers), 5 measure and persist (which number, how long,
  when to change). Each step: {do: the instruction, evidence: a paragraph naming 1-3 cases with what they did, their own
  words quoted, prices, dates and numbers, and an inline counter-example when there is one, inferred: true if no case
  shows this step directly}.
- cases: every product that took the move: {rid, did (what exactly it did, dated, its own words), result (dated numbers
  and what the number is NOT), causality: hard|medium|weak}. hard = timing + mechanism + no rival explanation;
  medium = plausible, other causes not excluded; weak = it uses the move and grew, cause unproven.
- counter: products that took the same move without a lift, or broke one step of it: {rid or name, what (what they did
  and what happened)}; a case can also be a counter-example for one step.
- suits: who it suits (team, skills, product type), one paragraph. prerequisites: one paragraph.
- risks: 2-5 short strings (platform rules, legal/trademark, reputation, ceiling).
- notes: 1-3 paragraphs "worth saying more": the typology across cases, what matters most, and the honest discount on
  the numbers.
Write ONLY from the evidence given. Never invent products, quotes, numbers, dates or links. English."""

DRAFT_SYSTEM = f"""You maintain the playbook of a daily breakout-intelligence product for solo builders.
Input: the current playbook and recent investigated products, one row per move a product used (rid, product, category,
move, why, did, result, causality, d7 = did the breakout hold a week later).
Group rows whose moves are the SAME concrete action into plays. A play needs at least 2 different products; a move seen
once stays out. Keep existing play ids and wording while the play still holds; new plays get the next free id
(p01, p02 ...). Drop a play only if none of its cases are in the input.
{RULES}
Return one JSON object {{"plays": [{{id, category, recipe, why, steps, cases, counter, suits, prerequisites, risks,
notes}}]}}, no prose."""

VERIFY_SYSTEM = f"""You are the fact-checker of a playbook for solo builders. You receive one drafted play and the full
investigation of every product cited in it. Check the play against that evidence:
- each case: is the move really what the product did? Is the result dated and measured? Regrade causality strictly.
  Remove cases the evidence doesn't support; correct numbers that don't match.
- each step: if no case shows it directly, set inferred: true or remove it; rewrite evidence paragraphs to match the
  corrected cases.
- counter-examples: keep only those the evidence supports.
- if fewer than 2 products still hold, return {{"drop": true, "reason": "..."}}.
- changed: 1-3 sentences on what checking changed versus the draft (or "Checking confirmed the draft.").
{RULES}
Return the corrected play as one JSON object {{id, category, recipe, why, steps, cases, counter, suits, prerequisites,
risks, notes, changed}}, no prose."""


def load() -> list:
    try:
        return json.loads(PATH.read_text(encoding="utf-8")).get("plays", [])
    except (OSError, ValueError):
        return []


def _moves(rep: dict) -> list:
    """The moves on a brief: agent `plays` (new) or the single `play` (older briefs)."""
    if rep.get("plays"):
        return rep["plays"]
    return [rep["play"]] if isinstance(rep.get("play"), dict) else []


def _inputs(con, today: str) -> tuple:
    lo = (datetime.strptime(today, "%Y-%m-%d") - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%d")
    reps = [r for r in synth.investigations(con) if r["day"] >= lo and _moves(r)]
    d7 = {r["id"]: r["outcomes"].get(7, "") for r in synth.followups(con, today)["rows"]}
    rows = []
    for r in reps:
        for m in _moves(r):
            rows.append({"rid": r["id"], "product": r["product"].get("name"), "day": r["day"],
                         "what": r.get("what") or "", "metric": _metric(r), "d7": d7.get(r["id"], ""),
                         **{k: m.get(k) for k in ("category", "move", "why", "did", "result", "causality")}})
    return rows[:MAX_ROWS], {r["id"]: r for r in reps}


def _metric(r: dict) -> str:
    b = r["badge"]
    return f"{b.get('metric')} {b.get('before')} -> {b.get('after')} ({b.get('window')})"


def _evidence(rep: dict) -> dict:
    """What the verifier sees for one case: the brief minus page furniture, trimmed."""
    keep = ("id", "day", "product", "badge", "measure", "charts", "events", "why_grew", "traces", "discounts",
            "verdict", "story", "plays", "competitors")
    ev = {k: rep.get(k) for k in keep}
    ev["product"] = {k: (rep["product"].get(k) or "") for k in ("name", "url", "description", "developer",
                                                                 "released", "price")}
    ev["product"]["description"] = ev["product"]["description"][:400]
    ev["charts"] = (rep.get("charts") or [])[:5]
    return ev


def _ask(client, system: str, payload: dict, max_tokens: int) -> dict:
    msg = client.messages.create(model=MODEL, max_tokens=max_tokens, system=system,
                                 messages=[{"role": "user", "content": json.dumps(payload, ensure_ascii=False)}])
    text = "".join(getattr(b, "text", "") for b in msg.content)
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError("no JSON in model output")
    return json.loads(m.group(0))


def _strs(x, n: int) -> list:
    return [s.strip() for s in (x or []) if isinstance(s, str) and s.strip()][:n]


def _clean(p: dict, by_id: dict) -> dict | None:
    """Schema-check one play; None if it no longer has two products we actually investigated."""
    if not isinstance(p, dict) or p.get("drop") or p.get("category") not in PLAY_CATEGORIES or not p.get("recipe"):
        return None
    cases = []
    for c in p.get("cases") or []:
        if isinstance(c, dict) and c.get("rid") in by_id and c["rid"] not in {x["rid"] for x in cases}:
            cases.append({"rid": c["rid"], "did": c.get("did", ""), "result": c.get("result", ""),
                          "causality": c.get("causality") if c.get("causality") in CAUSALITY else "weak"})
    if len({by_id[c["rid"]]["entity"] for c in cases}) < 2:
        return None
    steps = [{"do": s["do"].strip(), "evidence": (s.get("evidence") or "").strip(), "inferred": bool(s.get("inferred"))}
             for s in p.get("steps") or [] if isinstance(s, dict) and isinstance(s.get("do"), str) and s["do"].strip()]
    counter = [{"rid": c.get("rid") if c.get("rid") in by_id else None, "name": c.get("name") or "",
                "what": c.get("what") or c.get("why") or ""}
               for c in p.get("counter") or [] if isinstance(c, dict) and (c.get("rid") in by_id or c.get("name"))]
    return {"id": p.get("id"), "category": p["category"], "recipe": p["recipe"].strip(), "why": p.get("why") or "",
            "steps": steps[:5], "cases": cases, "counter": counter, "suits": p.get("suits") or "",
            "prerequisites": p.get("prerequisites") or "", "risks": _strs(p.get("risks"), 5),
            "notes": _strs(p.get("notes") if isinstance(p.get("notes"), list) else [p.get("notes")], 3),
            "changed": p.get("changed") or ""}


def _ids(plays: list, old: list) -> list:
    """Stable ids: keep a valid unused id, otherwise take the next free number."""
    taken = {p["id"] for p in old if p.get("id")}
    n = max([int(m.group(1)) for i in taken if (m := re.match(r"p(\d+)$", i))] + [0])
    used = set()
    for p in plays:
        if not re.match(r"p\d+$", str(p.get("id") or "")) or p["id"] in used:
            n += 1
            p["id"] = f"p{n:02d}"
        used.add(p["id"])
    return plays


def induce(con, today: str) -> int:
    if not agent_available():
        print("[radar] playbook: no LLM key, keeping data/playbook.json as is", flush=True)
        return 0
    rows, by_id = _inputs(con, today)
    if len({by_id[r["rid"]]["entity"] for r in rows}) < 2:
        print("[radar] playbook: fewer than 2 products with agent moves yet", flush=True)
        return 0
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("ANTHROPIC_API_KEY"),
                                 base_url=BASE_URL)
    old = load()
    draft = _ask(client, DRAFT_SYSTEM, {"current_playbook": old, "moves": rows}, 32000).get("plays", [])
    out = []
    for p in draft:
        first = _clean(p, by_id)
        if not first:
            continue
        cited = {c["rid"] for c in first["cases"]} | {c["rid"] for c in first["counter"] if c["rid"]}
        try:
            checked = _ask(client, VERIFY_SYSTEM, {"play": first, "investigations": [_evidence(by_id[r]) for r in cited]},
                           12000)
            checked.setdefault("id", first["id"])
            checked.setdefault("category", first["category"])
            final = _clean(checked, by_id)
        except Exception as e:  # noqa: BLE001  a failed check keeps the draft, flagged
            print(f"[radar] playbook verify failed for {first['recipe'][:40]}: {e}", flush=True)
            final = {**first, "changed": "Not fact-checked: the verification pass failed on this run."}
        if final:
            out.append(final)
    out = _ids(out, old)
    PATH.write_text(json.dumps({"updated": today, "plays": out}, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(out)


def assemble(con, today: str) -> list:
    """Plays ready for the site: cases joined to their briefs, faded cases added as counter-examples.
    Falls back to mechanism groups (synth.plays) while no induced playbook exists."""
    reps = {r["id"]: r for r in synth.investigations(con)}
    fu = {r["id"]: r["outcomes"] for r in synth.followups(con, today)["rows"]}
    out = []
    for p in load():
        cases = [{**c, "rep": reps[c["rid"]]} for c in p.get("cases", []) if c.get("rid") in reps]
        if len({c["rep"]["entity"] for c in cases}) < 2:
            continue
        counter = [{**c, "rep": reps.get(c.get("rid"))} for c in p.get("counter", [])]
        seen = {c.get("rid") for c in counter}
        for c in cases:
            if fu.get(c["rid"], {}).get(7) == "faded" and c["rid"] not in seen:
                counter.append({"rid": c["rid"], "rep": c["rep"], "name": "",
                                "what": "Took the move, but the breakout faded within 7 days (track record)."})
        clear = [c for c in cases if c.get("causality") in ("hard", "medium")]
        out.append({**p, "cases": cases, "counter": counter, "n": len({c["rep"]["entity"] for c in cases}),
                    "n_verified": len({c["rep"]["entity"] for c in clear}),
                    "last": max(c["rep"]["day"] for c in cases), "induced": True})
    if out:
        return sorted(out, key=lambda p: (-p["n"], p["id"]))
    for g in synth.plays(con):  # fallback: growth mechanisms tagged on each brief
        cases = [{"rid": r["id"], "rep": r, "did": r.get("verdict") or "", "result": "", "causality": ""}
                 for r in g["cases"]]
        out.append({"id": "", "category": "growth", "recipe": g["mechanism"].capitalize(), "why": "",
                    "steps": [], "cases": cases, "counter": [], "risks": [], "notes": [], "n": g["n"],
                    "n_verified": g["agent"], "last": g["last"], "induced": False, "status": g["status"]})
    return out
