"""Write the v3 site to docs/v3/.

Pages: Today (index), item reports (i/), directions (d/), charts, playbooks, track record, method,
archive (day/). Machine twins: *.md, llms.txt, api/*.json, feed.xml. No JS framework; one CSS file,
one small JS file for tabs and search. Everything renders without JS.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from .. import synth
from ..detect import CFG, SURFACE_NAME, chart_name
from ..feeds import appark, gravity, stores
from ..taxonomy import BY_SLUG

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "v3"
STATIC = Path(__file__).parent / "static"
SITE = "Opportunity Loop"
LABEL_TEXT = {"fact": "fact", "inferred": "inferred", "not_found": "not found", "estimated": "estimated",
              "verified": "verified"}
RULE_TEXT = {"chart_jump": "Chart jump", "chart_new": "New on chart", "gp_installs": "Install spike",
             "ios_ratings": "Ratings spike", "gh_stars": "Star spike", "minigame_rank": "Mini-game climb",
             "drama_ads": "Ad surge", "drama_chart": "Drama chart", "revenue": "Revenue climb",
             "web_traffic": "Traffic climb"}
SOURCE_TEXT = {"ios": "App Store", "play": "Google Play", "github": "GitHub", "trustmrr": "TrustMRR",
               "tranco": "Web", "minigame": "Mini-game", "drama": "TikTok drama", "drama_ad": "Drama ads"}
SURFACE_ORDER = ["apps", "saas", "opensource", "minigames", "drama"]


def e(s) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def short(name: str, n: int = 34) -> str:
    """'CodeHype.ai - Product Hunt Alternative to …' -> 'CodeHype.ai'"""
    name = (name or "").strip()
    if len(name) <= n:
        return name
    head = re.split(r"\s[-–—|]\s|: ", name)[0]
    return head if len(head) <= n else head[: n - 1] + "…"


def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "_", s)[:110]


def fnum(v, money: bool = False) -> str:
    if v is None:
        return "–"
    try:
        v = float(v)
    except (TypeError, ValueError):
        return e(v)
    pre = "$" if money else ""
    a = abs(v)
    if a >= 1_000_000:
        return f"{pre}{v / 1_000_000:.1f}M"
    if a >= 10_000:
        return f"{pre}{v / 1000:.0f}K"
    if a >= 1000:
        return f"{pre}{v / 1000:.1f}K"
    if a >= 100 or v == int(v):
        return f"{pre}{v:,.0f}"
    return f"{pre}{v:,.1f}"


def fdate(d: str) -> str:
    try:
        return datetime.strptime(d[:10], "%Y-%m-%d").strftime("%b %-d")
    except ValueError:
        return d


# ---------------------------------------------------------------- components

def page(title: str, body: str, *, base: str = "", active: str = "", desc: str = "", day: str = "") -> str:
    nav = [("index.html", "Today", "today"), ("d/index.html", "Directions", "dirs"), ("plays.html", "Playbooks", "plays"),
           ("charts.html", "Charts", "charts"), ("record.html", "Track record", "record"),
           ("method.html", "Method", "method")]
    links = "".join(f'<a href="{base}{h}" class="{"on" if k == active else ""}">{t}</a>' for h, t, k in nav)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc or 'Which small products took off yesterday, why, and how a solo builder could follow.')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/site.css">
<link rel="alternate" type="application/rss+xml" title="{SITE}" href="{base}feed.xml">
<script>try{{var t=localStorage.getItem('ol-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<header class="top"><div class="wrap top-in">
  <a class="brand" href="{base}index.html"><span class="mark">◎</span> {SITE}<span class="ver">v3</span></a>
  <nav class="nav">{links}</nav>
  <button class="theme" type="button" aria-label="Toggle dark mode" onclick="olTheme()">◐</button>
</div></header>
<main class="wrap">{body}</main>
<footer class="foot wrap">
  <div>{SITE} · daily breakout intelligence · data {e(day)} · <a href="{base}method.html">how this is made</a> ·
  <a href="{base}llms.txt">llms.txt</a> · <a href="{base}api/today.json">JSON</a> · <a href="{base}feed.xml">RSS</a></div>
  <div class="muted">Every number links to its source and carries a label: verified, estimated, inferred or not found.
  Charts are never padded. Not investment advice.</div>
</footer>
<script src="{base}assets/site.js"></script>
</body>
</html>"""


def chip(label: str) -> str:
    k = label if label in LABEL_TEXT else "inferred"
    return f'<span class="lbl lbl-{k}">{LABEL_TEXT[k]}</span>'


def grade_badge(g: dict, big: bool = False) -> str:
    return (f'<span class="grade g-{g["grade"]}{" big" if big else ""}" title="{e(g["text"])} · score {g["score"]}">'
            f'{g["grade"]}</span>')


def spark(points: list, *, rank: bool = False, w: int = 120, h: int = 34) -> str:
    vals = [v for _, v in points if v is not None]
    if len(vals) < 2:
        return '<span class="spark-empty">day 1</span>'
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1
    n = len(vals)
    pts = []
    for i, v in enumerate(vals):
        x = 2 + i * (w - 4) / (n - 1)
        y = (v - lo) / span
        y = 2 + (y if rank else 1 - y) * (h - 4)
        pts.append(f"{x:.1f},{y:.1f}")
    last = pts[-1].split(",")
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true">'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linejoin="round" stroke-linecap="round"/><circle cx="{last[0]}" cy="{last[1]}" r="2.6" '
            f'fill="currentColor"/></svg>')


def metric_badge(b: dict, big: bool = False) -> str:
    rank = b.get("rule") in synth.RANK_RULES
    money = b.get("rule") == "revenue"
    after = f"#{fnum(b['after'])}" if rank else fnum(b.get("after"), money)
    before = (f"#{fnum(b['before'])}" if rank else fnum(b["before"], money)) if b.get("before") else ""
    mult = ""
    if b.get("mult") and not rank:
        mult = f'<span class="mult">×{b["mult"]:.1f}</span>'
    elif b.get("before") and rank:
        mult = f'<span class="mult">↑{fnum(b["before"] - b["after"])}</span>'
    flow = f'<span class="b4">{before}</span><span class="arr">→</span>' if before else ""
    return (f'<div class="badge{" big" if big else ""}"><span class="mname">{e(b.get("metric"))}</span>{mult}'
            f'<span class="flow">{flow}<b>{after}</b></span>'
            f'<span class="basis basis-{e(b.get("basis"))}" title="{e(b.get("window"))}">{e(b.get("basis", "").replace("-", " "))}</span></div>')


def icon(p: dict, size: int = 44) -> str:
    src = p.get("icon")
    if src:
        return (f'<img class="ico" src="{e(src)}" alt="" width="{size}" height="{size}" loading="lazy" '
                f'referrerpolicy="no-referrer">')
    letter = (p.get("name") or "?").strip()[:1].upper()
    return f'<span class="ico ico-l" style="width:{size}px;height:{size}px">{e(letter)}</span>'


def item_meta(rep: dict) -> str:
    p = rep["product"]
    bits = [SOURCE_TEXT.get(rep["source"], rep["source"])]
    if p.get("developer"):
        bits.append(e(p["developer"]))
    if p.get("age_days") is not None:
        bits.append(f"launched {fdate(p['released'])} ({p['age_days']} days)")
    if p.get("price") and p["price"] not in ("Free",):
        bits.append(e(p["price"]))
    return " · ".join(bits)


def card(rep: dict, base: str) -> str:
    p, b = rep["product"], rep["badge"]
    why = rep["why_grew"][0] if rep.get("why_grew") else None
    if why and why.get("label") == "not_found":
        why = None
    what = rep.get("what") or (p.get("description") or "").strip().split("\n")[0][:180]
    href = f"{base}i/{slug(rep['id'])}.html"
    echo = rep["demand_echo"]
    rank = b.get("rule") in synth.RANK_RULES
    take = rep.get("takeaway") or rep.get("follow", {}).get("wedge") or ""
    return f"""<article class="card" data-surface="{e(rep['surface'])}" data-text="{e((p.get('name') or '') + ' ' + rep['direction_name'] + ' ' + rep['lesson_title']).lower()}">
  <div class="card-l">{grade_badge(rep['grade'])}</div>
  <div class="card-m">
    <a class="ttl" href="{href}">{e(rep['lesson_title'])}</a>
    <div class="who">{icon(p, 28)}<span><b>{e(short(p.get('name')))}</b> <span class="muted">· {item_meta(rep)}</span></span></div>
    {f'<p class="why">{chip(why["label"])} {e(why["text"])}</p>' if why else (f'<p class="why muted">{e(what)}</p>' if what else '')}
    {f'<p class="take"><span class="k">Take</span> {e(take)}</p>' if take else ''}
    <div class="tags"><a class="tag" href="{base}d/{e(rep['direction'])}.html">{e(rep['direction_name'])}</a>
      <span class="tag ghost">{e(RULE_TEXT.get(b.get('rule'), b.get('rule')))}</span>
      <span class="echo" title="Buyer-intent Reddit threads in this direction, last 14 days">demand {echo_dots(echo['threads_14d'])} {echo['threads_14d']} threads</span>
      {'<span class="tag agent">agent-checked</span>' if rep['mode'] == 'agent' else ''}</div>
  </div>
  <div class="card-r">{metric_badge(b)}<div class="sp {'rank' if rank else ''}">{spark(rep.get('curve') or [], rank=rank)}</div></div>
</article>"""


def echo_dots(n: int) -> str:
    k = 0 if not n else (1 if n < 5 else (2 if n < 15 else 3))
    return '<span class="dots">' + "".join(f'<i class="{"on" if i < k else ""}"></i>' for i in range(3)) + "</span>"


def cand_row(c: dict, base: str, inv_ids: set) -> str:
    rank = c["rule"] in synth.RANK_RULES
    money = c["rule"] == "revenue"
    after = f"#{fnum(c['after'])}" if rank else fnum(c.get("after"), money)
    before = (f"#{fnum(c['before'])}" if rank else fnum(c['before'], money)) if c.get("before") else "new"
    where = chart_name(c["chart"]) if c.get("chart", "").startswith("rank:") and c["source"] in ("ios", "play") else (
        c.get("chart", "")[5:].replace(":", " · ") if c.get("chart") else c.get("window", ""))
    name = e(c.get("name"))
    link = (f'<a href="{base}i/{slug(c["id"])}.html">{name}</a>' if c["id"] in inv_ids else name)
    return (f'<tr data-surface="{e(c["surface"])}" data-text="{e((c.get("name") or "").lower())}">'
            f'<td class="nm">{link}</td><td><span class="src src-{e(c["source"])}">{SOURCE_TEXT.get(c["source"], c["source"])}</span></td>'
            f'<td>{e(RULE_TEXT.get(c["rule"], c["rule"]))}</td><td class="num">{before} → <b>{after}</b></td>'
            f'<td class="muted">{e(where)}</td><td><a class="tag ghost" href="{base}d/{e(c["direction"])}.html">'
            f'{e((BY_SLUG.get(c["direction"]) or {}).get("name", c["direction"]))}</a></td></tr>')


# ---------------------------------------------------------------- pages

def today_page(day: str, reps: list, cands: list, all_days: list) -> str:
    counts = {s: sum(1 for c in cands if c["surface"] == s) for s in SURFACE_ORDER}
    total = len(cands)
    inv_ids = {r["id"] for r in reps}
    reps = sorted(reps, key=lambda r: (-r["grade"]["score"]))
    top_dir = {}
    for c in cands:
        top_dir[c["direction"]] = top_dir.get(c["direction"], 0) + 1
    hot = sorted(((n, d) for d, n in top_dir.items() if d not in ("other",)), reverse=True)[:3]
    judgment = f"{total:,} products crossed a line today" if total else "No product crossed a line today yet"
    lede = ""
    if reps:
        best = reps[0]
        lede = (f"Strongest brief: <a href=\"i/{slug(best['id'])}.html\">{e(short(best['product']['name']))}</a> "
                f"(grade {best['grade']['grade']}, {e(best['direction_name'])}). Busiest directions: "
                + ", ".join(f"<a href=\"d/{d}.html\">{e((BY_SLUG.get(d) or {}).get('name', d))}</a> ({n})" for n, d in hot) + ".")
    tabs = '<button class="tab on" data-f="all">All <span>' + f"{total:,}" + "</span></button>" + "".join(
        f'<button class="tab" data-f="{s}">{SURFACE_NAME[s]} <span>{counts[s]:,}</span></button>' for s in SURFACE_ORDER)
    tiles = "".join(f'<div class="tile"><b>{counts[s]:,}</b><span>{SURFACE_NAME[s]}</span></div>' for s in SURFACE_ORDER)
    rest = [c for c in cands if c["id"] not in inv_ids]
    rows = "".join(cand_row(c, "", inv_ids) for c in rest[:400])
    agent_n = sum(1 for r in reps if r["mode"] == "agent")
    mode_note = ("" if agent_n else '<div class="note">These briefs are <b>data-only</b>: every number is measured, '
                 'the trigger says "not checked" until the agent investigation (LLM + TinyFish) runs in CI. '
                 '<a href="method.html#modes">What changes in agent mode</a></div>')
    prev = [d for d in all_days if d < day][:6]
    return f"""
<section class="hero">
  <div class="date">{datetime.strptime(day, '%Y-%m-%d').strftime('%A, %B %-d, %Y')}</div>
  <h1>{e(judgment)}</h1>
  {f'<p class="lede">{lede}</p>' if lede else ''}
  <p class="sub">Which small products took off, why, whether demand is behind it, and how one or two people could follow.
  Every move is measured against the product's own recent baseline or the source's own change figure.</p>
  <div class="tiles">{tiles}</div>
</section>
{mode_note}
<div class="bar"><div class="tabs" role="tablist">{tabs}</div>
<input class="search" type="search" placeholder="Filter by name or direction" aria-label="Filter"></div>
<h2 class="sec">Investigated today <span class="muted">{len(reps)} briefs · ranked by grade</span></h2>
<div class="cards">{''.join(card(r, '') for r in reps) or '<p class="muted">No briefs yet.</p>'}</div>
<h2 class="sec">Also crossed the line <span class="muted">{len(rest):,} more · candidates, not conclusions</span></h2>
<div class="tblwrap"><table class="tbl filt"><thead><tr><th>Product</th><th>Source</th><th>Line crossed</th><th>Move</th><th>Where</th><th>Direction</th></tr></thead><tbody>{rows}</tbody></table></div>
{'<p class="muted">Showing 400 of ' + f"{len(rest):,}" + '. The full list is in <a href="api/today.json">api/today.json</a>.</p>' if len(rest) > 400 else ''}
{('<p class="muted">Earlier days: ' + ' · '.join(f'<a href="day/{d}.html">{fdate(d)}</a>' for d in prev) + ' · <a href="archive.html">archive</a></p>') if prev else ''}
"""


def item_page(rep: dict) -> str:
    p, b, g = rep["product"], rep["badge"], rep["grade"]
    rank = b.get("rule") in synth.RANK_RULES
    base = "../"
    why = "".join(f'<li>{chip(c.get("label", "inferred"))} {e(c.get("text"))}'
                  + (f' <a href="{e(c["url"])}" rel="nofollow noopener" target="_blank">↗</a>' if c.get("url") else "")
                  + "</li>" for c in rep.get("why_grew", []))
    summary = [("What it is", rep.get("what") or (p.get("description") or "")[:220]),
               ("Why it moved", (rep.get("why_grew") or [{}])[0].get("text", "")),
               ("What to take", rep.get("takeaway") or rep.get("follow", {}).get("wedge", "")),
               ("Who · model", " · ".join(x for x in (p.get("developer"), "in-app purchases" if p.get("iap") else
                                                      (p.get("price") or ""), rep.get("staying_power") if rep.get("staying_power") not in (None, "unclear") else "") if x))]
    summ = "".join(f'<div><span class="k">{k}</span><p>{e(v) or "<span class=muted>–</span>"}</p></div>' for k, v in summary)
    pos = rep.get("positioning") or {}
    pos_html = "".join(f'<div><span class="k">{k}</span><p>{e(pos.get(f))}</p></div>' for k, f in
                       (("For whom", "for_whom"), ("Job it does", "job"), ("Before it", "before_it"),
                        ("Where it wedges in", "wedge")) if pos.get(f))
    diffs = "".join(f'<li><b>{e(d.get("claim"))}</b> {chip(d.get("label", "inferred"))}<br><span class="muted">'
                    f'{e(d.get("evidence"))}</span></li>' for d in rep.get("differentiators", []))
    comps = "".join(f'<tr><td>{"<a href=" + chr(34) + e(c["url"]) + chr(34) + " target=_blank rel=noopener>" + e(c["name"]) + "</a>" if c.get("url") else e(c["name"])}</td>'
                    f'<td class="muted">{e(c.get("note") or c.get("how_it_differs"))}</td></tr>' for c in rep.get("competitors", []))
    charts = "".join(f'<tr><td>{e(c["chart"])}</td><td class="num"><b>#{c["rank"]}</b></td><td class="num">'
                     f'{("↑" + str(int(c["change"]))) if c.get("change") and c["change"] > 0 else (("↓" + str(int(-c["change"]))) if c.get("change") else "")}</td></tr>'
                     for c in rep.get("charts", []))
    m = rep.get("measure") or {}
    meas = []
    if m.get("installs") is not None:
        meas.append(("Google Play installs", fnum(m["installs"]), "verified, exact"))
    if m.get("installs_per_day") is not None:
        meas.append(("Installs / day", fnum(m["installs_per_day"]), "verified"))
    if m.get("ratings") is not None:
        meas.append(("Ratings", fnum(m["ratings"]), "verified count"))
    if m.get("ratings_per_day") is not None:
        meas.append(("New ratings / day", fnum(m["ratings_per_day"]), "estimated proxy"))
    if m.get("stars") is not None:
        meas.append(("GitHub stars (total)", fnum(m["stars"]), "verified"))
    if m.get("rating"):
        meas.append(("Average rating", f"{m['rating']:.2f}", "verified"))
    meas.append(("Days in our data", str(m.get("days_tracked", 1)), ""))
    sm = rep.get("sibling_measure") or {}
    if sm.get("installs") is not None:
        meas.append(("Android installs (sibling)", fnum(sm["installs"]), "verified, exact"))
    if sm.get("ratings") is not None and rep["source"] == "play":
        meas.append(("iOS ratings (sibling)", fnum(sm["ratings"]), "verified count"))
    meas_html = "".join(f'<div class="tile sm"><b>{v}</b><span>{k}</span><em>{x}</em></div>' for k, v, x in meas)
    events = "".join(f'<li><span class="dt">{fdate(ev["date"])}</span> {e(ev["text"])}'
                     + (f' <a href="{e(ev["url"])}" target="_blank" rel="noopener">↗</a>' if ev.get("url") else "")
                     + (f'<div class="muted small">“{e(ev["notes"])}”</div>' if ev.get("notes") else "") + "</li>"
                     for ev in rep.get("events", []))
    disc = "".join(f"<li>{e(x)}</li>" for x in rep.get("discounts", []))
    de = rep["demand_echo"]
    threads = "".join(f'<li><a href="{e(t["url"])}" target="_blank" rel="noopener">{e(t["title"])}</a> '
                      f'<span class="muted">r/{e(t["subreddit"])} · {t["comments"]} comments</span></li>' for t in de["threads"])
    xhs = "".join(f'<li><a href="{e(t["url"])}" target="_blank" rel="noopener">{e(t["title"])}</a> {chip("inferred")}</li>'
                  for t in de.get("xhs", []))
    trend = ""
    if de["threads_prev_14d"]:
        r = de["threads_14d"] / de["threads_prev_14d"]
        trend = f" ({'+' if r >= 1 else ''}{(r - 1) * 100:.0f}% vs the 14 days before)"
    factors = "".join(f'<tr><td>{k.title()}</td><td class="num">{v["score"]}</td><td><div class="meter"><i style="width:{v["score"]}%"></i></div></td>'
                      f'<td class="muted">{e(v["why"])}</td></tr>' for k, v in g["factors"].items())
    f = rep.get("follow") or {}
    follow = "".join(f'<div><span class="k">{k}</span><p>{e(f.get(x))}</p></div>' for k, x in
                     (("Play to copy", "play"), ("Wedge", "wedge"), ("Avoid", "avoid")) if f.get(x))
    kit = rep.get("build_kit")
    kit_html = ""
    if kit:
        cols = "".join(f'<div class="kitcol"><h4>{t}</h4><ol>' + "".join(f"<li>{e(x)}</li>" for x in kit.get(k, []))
                       + "</ol></div>" for t, k in (("Validate in 72 hours", "validate_72h"), ("14-day MVP", "mvp_14d"),
                                                     ("First 30 users", "first_30_users")))
        kit_html = f'<section class="blk kit"><h2>Build Kit</h2><div class="kitgrid">{cols}</div><p class="muted small">{e(kit.get("note"))}</p></section>'
    also = "".join(f'<li>{e(SOURCE_TEXT.get(a["source"], a["source"]))}: {e(RULE_TEXT.get(a["rule"], a["rule"]))} '
                   f'{("#" + fnum(a["before"]) + " → #" + fnum(a["after"])) if a["rule"] in synth.RANK_RULES and a.get("before") else fnum(a.get("after"))}'
                   f'{(" on " + e(chart_name(a["chart"]))) if (a.get("chart") or "").startswith("rank:") and a["source"] in ("ios", "play") else ""}</li>'
                   for a in rep.get("also", []))
    sib = "".join(f' · <a href="{e(s["url"])}" target="_blank" rel="noopener">{SOURCE_TEXT.get(s["source"])} version ↗</a>'
                  for s in rep.get("siblings", []))
    shot = p.get("screenshot")
    body = f"""
<a class="back" href="../index.html">← Today</a>
<header class="ihead">
  <div class="ihl">{grade_badge(g, True)}<div class="gt">{e(g['text'])}<br><span class="muted">score {g['score']} / 100</span></div></div>
  <div>
    <h1>{e(rep['lesson_title'])}</h1>
    <div class="who big">{icon(p, 40)}<span><b>{e(p.get('name'))}</b><br><span class="muted">{item_meta(rep)} ·
      <a href="{e(p.get('url'))}" target="_blank" rel="noopener">source ↗</a>{sib}
      {(' · <a href="' + e(p['site']) + '" target="_blank" rel="noopener">website ↗</a>') if p.get('site') else ''}</span></span></div>
    <div class="tags"><a class="tag" href="../d/{e(rep['direction'])}.html">{e(rep['direction_name'])}</a>
      <span class="tag ghost">{e(rep['surface_name'])}</span><span class="tag ghost">{fdate(rep['day'])}</span>
      <span class="tag {'agent' if rep['mode'] == 'agent' else 'ghost'}">{'agent-checked' if rep['mode'] == 'agent' else 'data-only brief'}</span></div>
  </div>
</header>
<section class="ibadge">{metric_badge(b, True)}<div class="sp big {'rank' if rank else ''}">{spark(rep.get('curve') or [], rank=rank, w=320, h=80)}
  <div class="muted small">{e(b.get('window'))} · {len(rep.get('curve') or [])} data points{' · lower is better' if rank else ''}</div></div></section>
<section class="summ">{summ}</section>
<div class="cols">
  <div>
    <section class="blk"><h2>Why it moved</h2><ul class="claims">{why}</ul></section>
    {f'<section class="blk"><h2>Positioning</h2><div class="summ two">{pos_html}</div></section>' if pos_html else ''}
    {f'<section class="blk"><h2>How it differs</h2><ul class="claims">{diffs}</ul></section>' if diffs else ''}
    <section class="blk"><h2>Timeline</h2><ul class="timeline">{events or '<li class="muted">No dated events yet.</li>'}</ul></section>
    <section class="blk warn"><h2>Discount the numbers</h2><ul>{disc}</ul></section>
    {f'<section class="blk"><h2>Moat</h2><p>{e(rep["moat"])}</p></section>' if rep.get('moat') else ''}
  </div>
  <aside>
    <section class="blk"><h2>Measured</h2><div class="tiles sm">{meas_html}</div></section>
    {f'<section class="blk"><h2>On charts today</h2><table class="tbl"><tbody>{charts}</tbody></table></section>' if charts else ''}
    {f'<section class="blk"><h2>Also crossed</h2><ul class="plain">{also}</ul></section>' if also else ''}
    {f'<section class="blk"><h2>Peers</h2><table class="tbl"><tbody>{comps}</tbody></table></section>' if comps else ''}
    {f'<section class="blk"><img class="shot" src="{e(shot)}" alt="Store screenshot" loading="lazy" referrerpolicy="no-referrer" onerror="this.parentNode.remove()"></section>' if shot else ''}
  </aside>
</div>
<section class="blk echo-blk"><h2>Demand Echo <span class="muted">is anyone asking for this?</span></h2>
  <p><b>{de['threads_14d']}</b> buyer-intent threads in <a href="../d/{e(rep['direction'])}.html">{e(rep['direction_name'])}</a> subreddits over 14 days{trend}.</p>
  <ul class="plain">{threads or '<li class="muted">No buyer-intent threads matched this direction.</li>'}{xhs}</ul></section>
<section class="blk"><h2>Grade {g['grade']} · how it was computed</h2>
  <table class="tbl factors"><thead><tr><th>Factor</th><th>Score</th><th></th><th>Evidence</th></tr></thead><tbody>{factors}</tbody></table>
  <p class="muted small">Weights: money 25 · demand 20 · replicable 20 · room 15 · window 10 · durability 10. S ≥ 80 · A ≥ 65 · B ≥ 50 · C ≥ 35 · D ≥ 20. Computed by code, so grades are reproducible.</p></section>
<section class="blk follow"><h2>How to follow</h2><div class="summ" style="--n:{max(1, follow.count('class="k"'))}">{follow or '<p class="muted">No wedge found in the data.</p>'}</div></section>
{kit_html}
<p class="muted small">Labels: {chip('fact')} linked source · {chip('inferred')} our reading · {chip('not_found')} looked, didn't find · {chip('estimated')} third-party estimate. <a href="{slug(rep['id'])}.md">Markdown</a></p>
"""
    return page(f"{rep['lesson_title']} · {SITE}", body, base=base, active="today",
                desc=f"{p.get('name')}: {b.get('metric')} {fnum(b.get('before'))} → {fnum(b.get('after'))}", day=rep["day"])


def directions_index(dirs: list) -> str:
    groups = {}
    for d in dirs:
        groups.setdefault(d["group"], []).append(d)
    hot = [d for d in dirs if d["breakouts_7d"]][:8]
    hot_html = "".join(f'<a class="dcard hot" href="{d["slug"]}.html"><b>{e(d["name"])}</b><span class="n">{d["breakouts_7d"]}</span>'
                       f'<span class="muted small">crossed a line in 7 days</span></a>' for d in hot)
    sections = ""
    for gname, ds in sorted(groups.items(), key=lambda kv: -sum(x["breakouts_7d"] for x in kv[1])):
        cards = "".join(
            f'<a class="dcard" href="{d["slug"]}.html"><b>{e(d["name"])}</b>'
            f'<div class="dstats"><span><em>{d["breakouts_7d"]}</em> breakouts 7d</span><span><em>{d["charting"]}</em> charting apps</span>'
            f'<span><em>{d["saas"]}</em> SaaS earning</span><span><em>{d["threads_14d"]}</em> demand threads</span></div></a>'
            for d in ds)
        sections += f'<h2 class="sec">{e(gname)}</h2><div class="dgrid">{cards}</div>'
    body = f"""<section class="hero slim"><h1>Directions</h1><p class="sub">{len(dirs)} niches. Each shows who crossed a line this week,
how crowded it is, who earns verified revenue, and whether buyers are asking.</p></section>
<h2 class="sec">Busiest this week</h2><div class="dgrid">{hot_html or '<p class="muted">Nothing yet.</p>'}</div>{sections}"""
    return body


def direction_page(d: dict, base: str) -> str:
    meta = synth.direction_meta(d["slug"])
    tiles = "".join(f'<div class="tile"><b>{v}</b><span>{k}</span></div>' for k, v in (
        ("crossed a line, 7 days", d["breakouts_7d"]), ("apps on today's charts", d["charting"]),
        ("of them launched in 12 months", d["new_12m"]), ("SaaS with verified revenue", d["saas"]),
        ("SaaS over $10K MRR", d["saas_10k"]), ("buyer-intent threads, 14 days", d["threads_14d"])))
    items = "".join(card(r, base) for r in d["items"])
    rows = "".join(cand_row(c, base, {r["id"] for r in d["items"]}) for c in d["cands"])
    saas = "".join(f'<tr><td><a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["name"])}</a></td>'
                   f'<td class="num"><b>{fnum(s["mrr"], True)}</b></td><td>{chip("verified")}</td></tr>' for s in d["top_saas"])
    subs = ", ".join(f'<a href="https://www.reddit.com/r/{s}/" target="_blank" rel="noopener">r/{s}</a>' for s in meta.get("subreddits", []))
    takeaways = []
    if d["charting"]:
        share = d["new_12m"] / d["charting"]
        takeaways.append(f"{d['new_12m']} of {d['charting']} charting apps launched in the last 12 months"
                         + (": newcomers can still get in." if share >= 0.3 else ": the charts belong to older apps."))
    if d["saas"]:
        takeaways.append(f"{d['saas']} indie SaaS publish verified revenue here; {d['saas_10k']} earn over $10K a month.")
    if d["threads_14d"]:
        takeaways.append(f"{d['threads_14d']} buyer-intent threads in two weeks: people are asking.")
    tk = "".join(f"<li>{e(t)}</li>" for t in takeaways)
    return f"""<a class="back" href="index.html">← Directions</a>
<section class="hero slim"><div class="date">{e(d['group'])}</div><h1>{e(d['name'])}</h1>
<p class="sub">Solo-builder fit prior {d['fit']:.2f}{(' · buyers talk in ' + subs) if subs else ''}</p>
<div class="tiles six">{tiles}</div>{f'<ul class="takeaways">{tk}</ul>' if tk else ''}</section>
{f'<h2 class="sec">Investigated this week</h2><div class="cards">{items}</div>' if items else ''}
<h2 class="sec">Crossed a line this week <span class="muted">{len(d['cands'])}</span></h2>
{f'<div class="tblwrap"><table class="tbl"><thead><tr><th>Product</th><th>Source</th><th>Line</th><th>Move</th><th>Where</th><th>Direction</th></tr></thead><tbody>{rows}</tbody></table></div>' if rows else '<p class="muted">Quiet week.</p>'}
{f'<h2 class="sec">Who earns here <span class="muted">TrustMRR, payment-verified</span></h2><div class="tblwrap"><table class="tbl"><tbody>{saas}</tbody></table></div>' if saas else ''}"""


def charts_page(con, day: str) -> str:
    def movers(src: str) -> str:
        rows = con.execute(
            "SELECT m.pid, m.metric, m.value chg, r.value rank, p.name, p.url, p.meta FROM metrics m "
            "JOIN metrics r ON r.source=m.source AND r.pid=m.pid AND r.day=m.day AND r.metric='rank:'||substr(m.metric,5) "
            "JOIN products p ON p.source=m.source AND p.pid=m.pid "
            "WHERE m.source=? AND m.day=? AND m.metric LIKE 'chg:%' AND m.value>0 AND r.value<=100 "
            "ORDER BY m.value*1.0/r.value * CASE WHEN m.metric LIKE 'chg:grossing:%' THEN 1.4 "
            "WHEN m.metric LIKE 'chg:paid:%' THEN 0.45 ELSE 1.0 END DESC LIMIT 40", (src, day)).fetchall()
        return "".join(f'<tr><td class="nm">{icon({"icon": json.loads(r["meta"] or "{}").get("icon"), "name": r["name"]}, 22)} '
                       f'<a href="{e(r["url"])}" target="_blank" rel="noopener">{e(r["name"])}</a></td>'
                       f'<td class="muted">{e(chart_name(r["metric"].replace("chg:", "rank:")))}</td>'
                       f'<td class="num">#{int(r["rank"] + r["chg"])} → <b>#{int(r["rank"])}</b></td></tr>' for r in rows)
    def board(plat: str, btype: str) -> str:
        rows = con.execute("SELECT m.pid, m.value rank, p.name, p.category, p.meta, "
                           "(SELECT value FROM metrics c WHERE c.source='minigame' AND c.pid=m.pid AND c.day=m.day "
                           "AND c.metric='chg:'||substr(m.metric,6)) chg FROM metrics m JOIN products p ON p.source=m.source "
                           "AND p.pid=m.pid WHERE m.source='minigame' AND m.day=? AND m.metric=? ORDER BY m.value LIMIT 20",
                           (day, f"rank:{plat}:{btype}")).fetchall()
        return "".join(f'<tr><td class="num">{int(r["rank"])}</td><td>{e(r["name"])} <span class="muted small">{e(r["category"])}</span></td>'
                       f'<td class="num">{("↑" + str(int(r["chg"]))) if r["chg"] and r["chg"] > 0 else (("↓" + str(int(-r["chg"]))) if r["chg"] else "")}</td></tr>'
                       for r in rows)
    drama = con.execute("SELECT m.pid, m.value, p.name, p.meta FROM metrics m JOIN products p ON p.source=m.source "
                        "AND p.pid=m.pid WHERE m.source='drama' AND m.metric='rank:tiktok' AND m.day=? ORDER BY m.value "
                        "LIMIT 20", (day,)).fetchall()
    drama_html = "".join(f'<tr><td class="num">{int(r["value"])}</td><td>{e(r["name"])}</td><td class="muted small">'
                         f'{e(", ".join((json.loads(r["meta"] or "{}").get("labels") or [])[:2]))}</td></tr>' for r in drama)
    ads = con.execute("SELECT p.name, p.meta, m.value creatives, (SELECT value FROM metrics x WHERE x.source='drama_ad' "
                      "AND x.pid=m.pid AND x.day=m.day AND x.metric='impressions') imp FROM metrics m JOIN products p ON "
                      "p.source=m.source AND p.pid=m.pid WHERE m.source='drama_ad' AND m.metric='creatives' AND m.day=? "
                      "ORDER BY m.value DESC LIMIT 15", (day,)).fetchall()
    ads_html = "".join(f'<tr><td>{e(r["name"])}</td><td class="num">{fnum(r["creatives"])}</td><td class="num">{fnum(r["imp"])}</td>'
                       f'<td class="muted small">{e(", ".join((json.loads(r["meta"] or "{}").get("countries") or [])[:3]))}</td></tr>' for r in ads)
    gh = con.execute("SELECT m.pid, m.value, p.description FROM metrics m JOIN products p ON p.source=m.source AND "
                     "p.pid=m.pid WHERE m.source='github' AND m.metric='stars_today' AND m.day=? ORDER BY m.value DESC "
                     "LIMIT 20", (day,)).fetchall()
    gh_html = "".join(f'<tr><td><a href="https://github.com/{e(r["pid"])}" target="_blank" rel="noopener">{e(r["pid"])}</a>'
                      f'<div class="muted small">{e((r["description"] or "")[:110])}</div></td><td class="num"><b>+{fnum(r["value"])}</b></td></tr>' for r in gh)
    boards = ""
    for plat in ("wechat", "douyin"):
        for btype, bname in gravity.BOARD_NAME.items():
            rows = board(plat, btype)
            if rows:
                boards += (f'<div class="panel"><h3>{gravity.PLATFORM_NAME[plat]} · {bname}</h3><table class="tbl">'
                           f'<tbody>{rows}</tbody></table></div>')
    return f"""<section class="hero slim"><h1>Charts today</h1><p class="sub">The raw movement behind the briefs: biggest rank jumps,
mini-game boards, drama charts and trending repos for {fdate(day)}. Derived from the sources on the <a href="method.html">Method</a> page.</p></section>
<div class="tabs static"><a href="#apps">App Store</a><a href="#play">Google Play</a><a href="#mini">Mini-games</a><a href="#drama">Drama</a><a href="#gh">GitHub</a></div>
<div class="grid2">
<div class="panel" id="apps"><h3>App Store · biggest jumps into a top 100</h3><table class="tbl"><tbody>{movers('ios') or '<tr><td class=muted>No data today.</td></tr>'}</tbody></table></div>
<div class="panel" id="play"><h3>Google Play · biggest jumps into a top 100</h3><table class="tbl"><tbody>{movers('play') or '<tr><td class=muted>No data today.</td></tr>'}</tbody></table></div>
</div>
<h2 class="sec" id="mini">Mini-games <span class="muted">Gravity Engine, public top 20</span></h2><div class="grid3">{boards or '<p class="muted">No data today.</p>'}</div>
<div class="grid2" id="drama">
<div class="panel"><h3>TikTok drama chart</h3><table class="tbl"><tbody>{drama_html or '<tr><td class=muted>No data today.</td></tr>'}</tbody></table></div>
<div class="panel"><h3>Drama ads · most creatives today {chip('estimated')}</h3><table class="tbl"><thead><tr><th>Drama</th><th>Creatives</th><th>Impressions</th><th>Top markets</th></tr></thead><tbody>{ads_html or '<tr><td class=muted>No data today.</td></tr>'}</tbody></table></div>
</div>
<div class="panel" id="gh"><h3>GitHub · most stars today</h3><table class="tbl"><tbody>{gh_html or '<tr><td class=muted>No data today.</td></tr>'}</tbody></table></div>"""


def plays_page(plays: list) -> str:
    cards = ""
    for pl in plays:
        cases = "".join(f'<li>{grade_badge(r["grade"])} <a href="i/{slug(r["id"])}.html">{e(r["product"]["name"])}</a> '
                        f'<span class="muted small">{fdate(r["day"])} · {e(r["badge"].get("metric"))}</span></li>' for r in pl["cases"])
        cards += (f'<article class="play"><div class="pst {"ok" if pl["status"] == "verified play" else ""}">{e(pl["status"])}</div>'
                  f'<h3>{e(pl["mechanism"].capitalize())}</h3><p class="muted">{pl["n"]} products · {pl["agent"]} agent-checked · '
                  f'last seen {fdate(pl["last"])}</p><ul class="plain">{cases}</ul></article>')
    return f"""<section class="hero slim"><h1>Playbooks</h1><p class="sub">Growth moves that more than one product has used.
Every investigation is tagged with its mechanism; a mechanism becomes a <b>verified play</b> once three products share it and
the agent has checked at least one. Counter-examples (same move, no lift) are added as the follow-up audit runs.</p></section>
<div class="plays">{cards or '<p class="muted">Playbooks form as investigations accumulate.</p>'}</div>"""


def record_page(fu: dict) -> str:
    stats = fu["stats"]
    head = "".join(f"<th>D+{h}</th>" for h in synth.HORIZONS)
    body_rows = ""
    for g in ("all", "S", "A", "B", "C", "D", "E"):
        cells = ""
        for h in synth.HORIZONS:
            s = stats.get(h, {}).get(g)
            pct = f'{s["held"] / s["n"] * 100:.0f}% <span class="muted">({s["n"]})</span>' if s and s["n"] else "–"
            cells += f'<td class="num">{pct}</td>'
        body_rows += f"<tr><td>{'All grades' if g == 'all' else grade_badge({'grade': g, 'text': '', 'score': ''})}</td>{cells}</tr>"
    recent = "".join(f'<tr><td><a href="i/{slug(r["id"])}.html">{e(r["name"])}</a></td><td>{fdate(r["day"])}</td>'
                     + "".join(f'<td class="o-{r["outcomes"].get(h, "")}">{r["outcomes"].get(h, "…")}</td>' for h in synth.HORIZONS)
                     + "</tr>" for r in fu["rows"][:60])
    pending = (f'<div class="note">The first audit runs on <b>{fdate(fu["next_audit"])}</b>, seven days after the first published '
               f'brief. Until then every outcome reads “…”. We publish misses as well as hits.</div>' if fu["next_audit"] and not any(
                   stats.get(7, {}).values()) else "")
    return f"""<section class="hero slim"><h1>Track record</h1><p class="sub">Did the breakouts hold? Each published brief is re-measured
7, 14 and 30 days later. <b>Held</b> = still within 1.5× of the rank it reached, or still ≥ 2× its old baseline.
Off the chart or back to baseline = <b>faded</b>.</p></section>{pending}
<div class="tblwrap"><table class="tbl"><thead><tr><th>Grade</th>{head}</tr></thead><tbody>{body_rows}</tbody></table></div>
<h2 class="sec">Every brief</h2><div class="tblwrap"><table class="tbl"><thead><tr><th>Product</th><th>Published</th>{head}</tr></thead><tbody>{recent}</tbody></table></div>"""


def method_page(con, day: str) -> str:
    specs = [appark.SPEC, stores.GP_SPEC, stores.IT_SPEC, gravity.SPEC, appark.DRAMA_SPEC,
             {"name": "TrustMRR", "surface": "saas", "label": "verified", "endpoint": "trustmrr.com/api/ai",
              "history": "API + our snapshots", "role": "measurement: payment-verified revenue"},
             {"name": "GitHub Trending", "surface": "opensource", "label": "verified", "endpoint": "github.com/trending",
              "history": "our daily snapshots", "role": "discovery: stars today, 8 languages"},
             {"name": "Tranco", "surface": "saas", "label": "verified", "endpoint": "tranco-list.eu",
              "history": "daily lists by date", "role": "measurement: web traffic rank"},
             {"name": "Reddit (Arctic Shift)", "surface": "demand", "label": "verified counts",
              "endpoint": "arctic-shift.photon-reddit.com", "history": "API", "role": "Demand Echo: buyer-intent threads"},
             {"name": "Xiaohongshu via TinyFish", "surface": "demand", "label": "inferred", "endpoint": "TinyFish search",
              "history": "CI only, when TinyFish is configured", "role": "Demand Echo (CN): public 小工具 posts"}]
    key = {"Appark charts": "appark", "Google Play detail": "gplay", "iTunes Lookup": "itunes",
           "Gravity Engine mini-games": "gravity", "Appark drama": "drama", "TrustMRR": "trustmrr",
           "GitHub Trending": "github", "Tranco": "tranco", "Reddit (Arctic Shift)": "reddit",
           "Xiaohongshu via TinyFish": "xhs_web"}
    rows = ""
    for s in specs:
        k = key[s["name"]]
        last = con.execute("SELECT day, ok, rows, note FROM source_runs WHERE source=? ORDER BY day DESC LIMIT 1", (k,)).fetchone()
        first = con.execute("SELECT MIN(day) FROM source_runs WHERE source=?", (k,)).fetchone()[0]
        status = ("<span class='ok'>●</span> " + fdate(last["day"]) + f" · {last['rows']:,} rows") if last and last["ok"] else (
            ("<span class='bad'>●</span> " + fdate(last["day"]) + " failed") if last else "<span class='muted'>○ not run here</span>")
        rows += (f'<tr><td><b>{e(s["name"])}</b><div class="muted small">{e(s["endpoint"])}</div></td><td>{e(s["role"])}</td>'
                 f'<td>{chip("verified" if s["label"].startswith("verified") else ("inferred" if s["label"] == "inferred" else "estimated"))} '
                 f'<span class="muted small">{e(s["label"])}</span></td><td class="small">{e(s["history"])}'
                 f'{("<br><span class=muted>since " + fdate(first) + "</span>") if first else ""}</td><td class="small">{status}</td></tr>')
    R = CFG["rules"]
    rules = "".join(f'<tr><td><b>{e(RULE_TEXT.get(k, k))}</b></td><td class="small">{e(v.get("label"))}</td><td class="small">{e(_rule_text(k, v))}</td></tr>'
                    for k, v in R.items() if isinstance(v, dict))
    return f"""<section class="hero slim"><h1>Method</h1><p class="sub">Where every number comes from, how a product “crosses a line”,
how briefs are written and graded, and what we refuse to do.</p></section>
<h2 class="sec">Sources</h2><div class="tblwrap"><table class="tbl"><thead><tr><th>Source</th><th>Role</th><th>Label</th><th>History</th><th>Last run</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="muted small">Appark and Gravity Engine endpoints are public but undocumented. We pace requests, publish derived ranks and links,
and never re-host raw chart dumps. Appark gives guests today's charts only, so history starts the day we start collecting.</p>
<h2 class="sec">The line a product must cross</h2>
<p>A product qualifies when today is at least <b>{R['gp_installs']['mult']:.0f}×</b> its own average over the previous {R['baseline_days']} days, above an absolute floor.
New sources have no history yet: until a product has {R['min_baseline_points']} days in our data, we use the change figure the source itself reports and label the card
<span class="basis basis-source-delta">source delta</span> or <span class="basis basis-cold-start">cold start</span> instead of <span class="basis basis-own-baseline">own baseline</span>.</p>
<div class="tblwrap"><table class="tbl"><thead><tr><th>Rule</th><th>Metric</th><th>Threshold</th></tr></thead><tbody>{rules}</tbody></table></div>
<h2 class="sec">Picking what to brief</h2>
<p>score = strength × publisher penalty × freshness × (0.5 + direction fit) × (1 + demand echo) × novelty.
Grossing-chart moves weigh 1.4×, paid-chart moves 0.45× (a few sales move a thin paid chart); products launched in the last year weigh 1.3×,
older than three years 0.55×. Big platforms are penalised, products briefed in the last 14 days are skipped,
each surface gets at least {CFG['pick']['min_per_surface']} briefs and at most {int(CFG['pick']['max_share_per_surface'] * 100)}% of the {CFG['pick']['budget']} daily slots.</p>
<h2 class="sec" id="modes">Two modes of brief</h2>
<div class="grid2"><div class="panel"><h3>Data-only (always)</h3><p>Every field is computed from collected data: badge, curve, charts, measurements,
dated events, peers, Demand Echo, discounts, grade, market-gap wedge. The headline describes the move; the trigger reads “not checked” unless evidence exists.</p></div>
<div class="panel"><h3>Agent-checked (CI with keys)</h3><p>TinyFish searches the web for the trigger; an LLM writes the lesson headline, positioning,
differentiators, moat, wedge and Build Kit <b>from the gathered evidence only</b>. A verify step downgrades any “fact” whose link we didn't gather to “inferred”.
Badges and grades stay computed by code.</p></div></div>
<h2 class="sec">Labels</h2><p>{chip('fact')} linked to a source · {chip('verified')} measured by us or payment-verified · {chip('estimated')} a third party's estimate or a proxy ·
{chip('inferred')} our reading of the evidence · {chip('not_found')} we looked and didn't find it.</p>"""


def _rule_text(k: str, v: dict) -> str:
    if "mult" in v:
        return f"≥ {v['mult']}× own baseline and ≥ {v.get('floor', 0):,}/day" + (
            f"; cold start ≥ {v['cold_floor']:,}" if v.get("cold_floor") else "") + (
            f"; or ≥ {int(v['fresh_share'] * 100)}% of creatives new today" if v.get("fresh_share") else "")
    if "min_jump" in v:
        return f"up ≥ {v['min_jump']} places into the top {v['max_rank']}"
    if "max_rank" in v:
        return f"new or improved inside the top {v['max_rank']}"
    return "v2 logic: MRR ×1.3 in 30 days (≥ $100 gain) / Tranco rank ×1.3 in 7 days"


def archive_page(days: list, counts: dict) -> str:
    rows = "".join(f'<tr><td><a href="day/{d}.html">{datetime.strptime(d, "%Y-%m-%d").strftime("%a %b %-d, %Y")}</a></td>'
                   f'<td class="num">{counts[d][0]:,}</td><td class="num">{counts[d][1]}</td></tr>' for d in days)
    return f"""<section class="hero slim"><h1>Archive</h1></section><div class="tblwrap"><table class="tbl"><thead><tr><th>Day</th>
<th>Crossed a line</th><th>Briefs</th></tr></thead><tbody>{rows}</tbody></table></div>"""


# ---------------------------------------------------------------- machine twins

def item_md(rep: dict) -> str:
    p, b, g = rep["product"], rep["badge"], rep["grade"]
    lines = [f"# {rep['lesson_title']}", "", f"> {p.get('name')} · {item_meta(rep)} · {p.get('url')}",
             f"> {b.get('metric')}: {fnum(b.get('before'))} → {fnum(b.get('after'))} ({b.get('window')}, {b.get('basis')})",
             f"> Grade {g['grade']} ({g['score']}/100, {g['text']}) · direction: {rep['direction_name']} · mode: {rep['mode']}", "",
             "## Why it moved"]
    lines += [f"- [{c.get('label')}] {c.get('text')}" + (f" ({c['url']})" if c.get("url") else "") for c in rep["why_grew"]]
    lines += ["", "## Discount the numbers"] + [f"- {x}" for x in rep["discounts"]]
    lines += ["", "## Demand Echo", f"- {rep['demand_echo']['threads_14d']} buyer-intent threads in 14 days"]
    lines += [f"- {t['title']} ({t['url']})" for t in rep["demand_echo"]["threads"]]
    f = rep.get("follow") or {}
    lines += ["", "## How to follow"] + [f"- {k}: {f[k]}" for k in ("play", "wedge", "avoid") if f.get(k)]
    if rep.get("build_kit"):
        for t, k in (("Validate in 72 hours", "validate_72h"), ("14-day MVP", "mvp_14d"), ("First 30 users", "first_30_users")):
            lines += ["", f"### {t}"] + [f"1. {x}" for x in rep["build_kit"].get(k, [])]
    return "\n".join(lines) + "\n"


def today_md(day: str, reps: list) -> str:
    out = [f"# {SITE} · {day}", "", "Which small products crossed a measurable line today, why, and how to follow.", ""]
    for r in sorted(reps, key=lambda r: -r["grade"]["score"]):
        b = r["badge"]
        out.append(f"- [{r['grade']['grade']}] [{r['lesson_title']}](i/{slug(r['id'])}.md) — {r['product'].get('name')} · "
                   f"{b.get('metric')} {fnum(b.get('before'))} → {fnum(b.get('after'))} · {r['direction_name']}")
    return "\n".join(out) + "\n"


def llms_txt(day: str) -> str:
    return f"""# {SITE} v3

> Daily breakout intelligence for solo builders: which small products (apps, SaaS, open source, mini-games, short drama)
> crossed a measurable line today, why, whether buyers are asking for it, and how one or two people could follow.

Every page has a Markdown twin. Data date: {day}.

## Pages
- [Today]({'index.md'}): today's briefs, ranked by grade
- [Today as JSON](api/today.json): briefs + every candidate that crossed a line
- [Directions](d/index.html), [Playbooks](plays.html), [Charts](charts.html), [Track record](record.html), [Method](method.html)

## Labels
fact (linked) · verified (measured / payment-verified) · estimated (third-party or proxy) · inferred · not_found
"""


def feed_xml(reps: list, day: str) -> str:
    items = "".join(f"""<item><title>{e(r['lesson_title'])}</title><link>i/{slug(r['id'])}.html</link>
<guid isPermaLink="false">{e(r['id'])}</guid><pubDate>{datetime.strptime(r['day'], '%Y-%m-%d').strftime('%a, %d %b %Y 06:00:00 +0000')}</pubDate>
<description>{e(r['product'].get('name'))} · {e(r['badge'].get('metric'))} {fnum(r['badge'].get('before'))} → {fnum(r['badge'].get('after'))} · grade {r['grade']['grade']}</description></item>"""
                    for r in sorted(reps, key=lambda r: r["day"], reverse=True)[:80])
    return f"""<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{SITE}</title><link>index.html</link>
<description>Daily breakout intelligence</description><lastBuildDate>{datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>{items}</channel></rss>"""


# ---------------------------------------------------------------- write

def write(con) -> None:
    days = synth.days_with_candidates(con)
    if not days:
        print("[radar] v3 build: no candidates yet — run `python -m radar detect` first", flush=True)
        return
    day = days[0]
    if OUT.exists():
        shutil.rmtree(OUT)
    for sub in ("i", "d", "day", "api", "assets"):
        (OUT / sub).mkdir(parents=True, exist_ok=True)
    for f in STATIC.iterdir():
        shutil.copy(f, OUT / "assets" / f.name)
    all_reps = synth.investigations(con)
    reps_today = [r for r in all_reps if r["day"] == day]
    cands = synth.candidates(con, day)

    (OUT / "index.html").write_text(page(f"{SITE} · {fdate(day)}", today_page(day, reps_today, cands, days),
                                         active="today", day=day), encoding="utf-8")
    (OUT / "index.md").write_text(today_md(day, reps_today), encoding="utf-8")
    for r in all_reps:
        (OUT / "i" / f"{slug(r['id'])}.html").write_text(item_page(r), encoding="utf-8")
        (OUT / "i" / f"{slug(r['id'])}.md").write_text(item_md(r), encoding="utf-8")
    dirs = synth.directions(con, day)
    (OUT / "d" / "index.html").write_text(page(f"Directions · {SITE}", directions_index(dirs), base="../", active="dirs",
                                               day=day), encoding="utf-8")
    for d in dirs:
        (OUT / "d" / f"{d['slug']}.html").write_text(page(f"{d['name']} · {SITE}", direction_page(d, "../"), base="../",
                                                          active="dirs", day=day), encoding="utf-8")
    (OUT / "charts.html").write_text(page(f"Charts · {SITE}", charts_page(con, day), active="charts", day=day), encoding="utf-8")
    (OUT / "plays.html").write_text(page(f"Playbooks · {SITE}", plays_page(synth.plays(con)), active="plays", day=day),
                                    encoding="utf-8")
    (OUT / "record.html").write_text(page(f"Track record · {SITE}", record_page(synth.followups(con, day)), active="record",
                                          day=day), encoding="utf-8")
    (OUT / "method.html").write_text(page(f"Method · {SITE}", method_page(con, day), active="method", day=day), encoding="utf-8")
    counts = {}
    for d in days:
        cs = synth.candidates(con, d)
        rs = [r for r in all_reps if r["day"] == d]
        counts[d] = (len(cs), len(rs))
        if d != day:
            inv_ids = {r["id"] for r in rs}
            body = (f'<a class="back" href="../archive.html">← Archive</a><section class="hero slim"><h1>{fdate(d)}</h1>'
                    f'<p class="sub">{len(cs):,} crossed a line · {len(rs)} briefs</p></section>'
                    f'<div class="cards">{"".join(card(r, "../") for r in sorted(rs, key=lambda r: -r["grade"]["score"]))}</div>'
                    f'<div class="tblwrap"><table class="tbl"><tbody>{"".join(cand_row(c, "../", inv_ids) for c in cs[:300])}</tbody></table></div>')
            (OUT / "day" / f"{d}.html").write_text(page(f"{fdate(d)} · {SITE}", body, base="../", day=d), encoding="utf-8")
    (OUT / "archive.html").write_text(page(f"Archive · {SITE}", archive_page(days, counts), day=day), encoding="utf-8")
    (OUT / "llms.txt").write_text(llms_txt(day), encoding="utf-8")
    (OUT / "feed.xml").write_text(feed_xml(all_reps, day), encoding="utf-8")
    (OUT / "api" / "today.json").write_text(json.dumps({"day": day, "briefs": reps_today, "candidates": cands},
                                                       ensure_ascii=False, default=str), encoding="utf-8")
    print(f"[radar] v3 site: {day} · {len(reps_today)} briefs · {len(cands)} candidates · {len(dirs)} directions → {OUT}",
          flush=True)

