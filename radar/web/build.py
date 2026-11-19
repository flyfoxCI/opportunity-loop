"""Write the v3 site to docs/v3/.

Pages: Today (index), item reports (i/), product database (db/), playbooks (plays/), directions (d/), charts,
track record, archive (day/). Machine twins: *.md, llms.txt, api/*.json, feed.xml. No JS framework; one CSS file,
one small JS file for tabs and search. Everything renders without JS.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .. import appdb, categories, playbook, synth
from ..categories import fusd
from ..detect import SURFACE_NAME, chart_name
from ..feeds import gravity
from ..investigate import CAUSALITY, CAUSES, PLAY_CATEGORIES, VISIBILITY
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
             "web_traffic": "Traffic climb", "shop_reviews": "Review spike", "cws_users": "User spike"}
SOURCE_TEXT = {"ios": "App Store", "play": "Google Play", "github": "GitHub", "trustmrr": "TrustMRR",
               "tranco": "Web", "minigame": "Mini-game", "drama": "TikTok drama", "drama_ad": "Drama ads",
               "chrome": "Chrome Web Store", "shopify": "Shopify App Store"}
SURFACE_ORDER = ["apps", "saas", "minigames", "chrome", "shopify", "opensource", "drama"]


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

NAV_ICON = {
    "today": '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
    "db": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    "plays": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "cats": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    "dirs": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
    "charts": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "record": '<path d="M20 6 9 17l-5-5"/>',
}


def page(title: str, body: str, *, base: str = "", active: str = "", desc: str = "", day: str = "") -> str:
    nav = [("index.html", "Today", "today"), ("db/index.html", "Product DB", "db"), ("cat/index.html", "Categories", "cats"),
           ("plays/index.html", "Playbooks", "plays"),
           ("d/index.html", "Directions", "dirs"), ("charts.html", "Charts", "charts"), ("record.html", "Track record", "record")]
    links = "".join(f'<a href="{base}{h}" class="{"on" if k == active else ""}"><svg width="16" height="16" viewBox="0 0 24 24" '
                    f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
                    f'aria-hidden="true">{NAV_ICON[k]}</svg>{t}</a>' for h, t, k in nav)
    stamp = datetime.strptime(day, "%Y-%m-%d").strftime("data %b %-d, %Y") if day else "daily breakouts"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc or 'Which small products took off yesterday, why, and how a solo builder could follow.')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&family=Newsreader:opsz,wght@6..72,600;6..72,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/site.css">
<link rel="alternate" type="application/rss+xml" title="{SITE}" href="{base}feed.xml">
<script>try{{var t=localStorage.getItem('ol-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<div class="shell">
<aside class="rail">
  <a class="brand" href="{base}index.html"><span class="logo">O</span><span><b>{SITE}</b><i>{e(stamp)}</i></span></a>
  <nav class="nav" aria-label="Sections">{links}</nav>
  <div class="railfoot"><span>Updated daily · 06:30 UTC</span>
    <a href="{base}feed.xml">RSS feed</a><a href="{base}llms.txt">llms.txt</a><a href="{base}api/today.json">Today as JSON</a>
    <button class="theme" type="button" aria-label="Toggle dark mode" onclick="olTheme()">◐ Theme</button></div>
</aside>
<div class="main">
<main class="wrap">{body}</main>
<footer class="foot wrap">
  <div>{SITE} · daily breakout intelligence for solo builders · data {e(day)}</div>
  <div>Every number links to its source and carries a label: verified, estimated, inferred or not found.
  Charts are never padded. Not investment advice.</div>
</footer>
</div>
</div>
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
    name = p.get("name") or ""
    title = (e(rep["lesson_title"]) if name[:12].lower() in rep["lesson_title"].lower()
             else f'<b>{e(short(name, 40))}</b>: {e(rep["lesson_title"])}')
    meta = [SOURCE_TEXT.get(rep["source"], rep["source"])]
    if p.get("developer"):
        meta.append(e(short(p["developer"], 30)))
    if p.get("age_days") is not None:
        meta.append(f"{p['age_days']} days old")
    return f"""<article class="card" data-surface="{e(rep['surface'])}" data-text="{e((p.get('name') or '') + ' ' + rep['direction_name'] + ' ' + rep['lesson_title']).lower()}">
  <div class="card-l">{icon(p, 48)}</div>
  <div class="card-m">
    <a class="ttl" href="{href}">{title}</a>
    {f'<p class="why">{chip(why["label"])} {e(why["text"])}</p>' if why else (f'<p class="why muted">{e(what)}</p>' if what else '')}
    {f'<p class="take"><span class="k">Take</span> {e(take)}</p>' if take else ''}
    <div class="tags">{grade_badge(rep['grade'])}<span>{' · '.join(meta)}</span>
      <a class="tag" href="{base}d/{e(rep['direction'])}.html">{e(rep['direction_name'])}</a>
      <span class="echo" title="Buyer-intent Reddit threads in this direction, last 14 days">demand {echo_dots(echo['threads_14d'])} {echo['threads_14d']}</span></div>
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
                 'the trigger says "not checked" until the agent investigation (LLM + TinyFish) runs in CI.</div>')
    prev = [d for d in all_days if d < day][:6]
    lanes = sorted(((n, d) for d, n in top_dir.items() if d not in ("other",)), reverse=True)[:10]
    dirbox = ("" if not lanes else '<section class="dirbox" aria-label="Directions"><div class="dirhead"><span><b>By direction</b>'
              'where the moves cluster today</span><a href="d/index.html">All directions →</a></div><div class="dirgrid">'
              + "".join(f'<a class="dirt dt{i % 6}" href="d/{e(d)}.html"><b>{e((BY_SLUG.get(d) or {}).get("name", d))}</b>'
                        f'<span>{n:,} crossed a line</span></a>' for i, (n, d) in enumerate(lanes)) + "</div></section>")
    return f"""
<section class="hero">
  <div class="date">{datetime.strptime(day, '%Y-%m-%d').strftime('%A, %B %-d, %Y')}</div>
  <h1>{e(judgment)}</h1>
  {f'<p class="lede">{lede}</p>' if lede else ''}
  <p class="sub">Which small products took off, why, whether demand is behind it, and how one or two people could follow.
  Every move is measured against the product's own recent baseline or the source's own change figure.</p>
  <div class="tiles">{tiles}</div>
</section>
{dirbox}
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
mini-game boards, drama charts and trending repos for {fdate(day)}.</p></section>
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


PLATFORM = {"ios": "iOS", "play": "Android", "github": "GitHub", "trustmrr": "Web", "tranco": "Web",
            "minigame": "Mini-game", "drama": "TikTok", "drama_ad": "Drama ads", "chrome": "Chrome", "shopify": "Shopify"}
DB_TABS = [("apps", "briefs.html"), ("saas", "briefs-saas.html"), ("minigames", "briefs-minigames.html"),
           ("chrome", "briefs-chrome.html"), ("shopify", "briefs-shopify.html"), ("opensource", "briefs-opensource.html"),
           ("drama", "briefs-drama.html")]
LENS_FILES = [("followed", "index.html"), ("unique", "unique.html"), ("m3_10k", "new-3m.html"), ("y_100k", "year-100k.html")]


def linechart(ch: dict) -> str:
    """Multi-series line chart with axes, inline SVG. Rank charts are inverted (#1 on top); lines break at gaps."""
    W, H, L, R, T, B = 640, 190, 46, 64, 12, 24
    series = ch["series"]
    days = sorted({d for _, pts in series for d, _ in pts})
    vals = [v for _, pts in series for _, v in pts]
    d0 = datetime.strptime(days[0], "%Y-%m-%d")
    span = max(1, (datetime.strptime(days[-1], "%Y-%m-%d") - d0).days)
    lo, hi = min(vals), max(vals)
    if hi == lo:
        lo, hi = (lo - 1, hi + 1) if ch["rank"] or abs(lo) < 20 else (lo * 0.9, hi * 1.1)

    def x(d):
        return L + (datetime.strptime(d, "%Y-%m-%d") - d0).days / span * (W - L - R) if len(days) > 1 else (W - R + L) / 2

    def y(v):
        f = (v - lo) / (hi - lo)
        return T + (f if ch["rank"] else 1 - f) * (H - T - B)

    whole = ch["rank"] or (hi - lo) >= 10 or all(float(v).is_integer() for v in vals)
    fmt = (lambda v: "#" + fnum(round(v))) if ch["rank"] else (lambda v: fnum(round(v) if whole else v, ch.get("money")))
    grid = ""
    for v in (lo, (lo + hi) / 2, hi):
        grid += (f'<line x1="{L}" x2="{W - R}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="gl"/>'
                 f'<text x="{L - 6}" y="{y(v) + 4:.1f}" text-anchor="end" class="ax">{fmt(v)}</text>')
    n_ticks = min(5, len(days))
    for i in range(n_ticks):
        d = days[round(i * (len(days) - 1) / max(1, n_ticks - 1))]
        grid += f'<text x="{x(d):.1f}" y="{H - 6}" text-anchor="middle" class="ax">{fdate(d)}</text>'
    lines = ""
    for k, (lbl, pts) in enumerate(series):
        segs, cur = [], []
        for d, v in pts:
            if cur and (datetime.strptime(d, "%Y-%m-%d") - datetime.strptime(cur[-1][0], "%Y-%m-%d")).days > 2:
                segs.append(cur)
                cur = []
            cur.append((d, v))
        segs.append(cur)
        for sg in segs:
            if len(sg) == 1:
                lines += f'<circle cx="{x(sg[0][0]):.1f}" cy="{y(sg[0][1]):.1f}" r="3" class="s{k}"/>'
            else:
                lines += (f'<polyline class="s{k}" fill="none" points="'
                          + " ".join(f"{x(d):.1f},{y(v):.1f}" for d, v in sg) + '"/>')
        ld, lv = pts[-1]
        lines += f'<circle cx="{x(ld):.1f}" cy="{y(lv):.1f}" r="3" class="s{k}"/>'
        if len(series) == 1:  # several series: latest values go in the legend so labels don't collide
            lines += f'<text x="{x(ld) + 6:.1f}" y="{y(lv) + 4:.1f}" class="lb s{k}">{e(fmt(lv))}</text>'
    legend = ("" if len(series) == 1 else '<div class="lg">' + "".join(
        f'<span><i class="s{k}"></i>{e(lbl)} <b>{e(fmt(pts[-1][1]))}</b></span>' for k, (lbl, pts) in enumerate(series)) + "</div>")
    obs = len({d for _, pts in series for d, _ in pts})
    cap = (f"Data {days[0]} → {days[-1]} ({span + 1} days, {obs} observations)" if len(days) > 1
           else f"Data {days[0]}: first observation, the line grows daily")
    return (f'<figure class="lc"><figcaption>{e(ch["title"])}</figcaption>{legend}'
            f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{e(ch["title"])}">{grid}{lines}</svg>'
            f'<div class="muted small">{cap}.{(" " + e(ch["note"])) if ch.get("note") else ""}</div></figure>')


def move_text(b: dict) -> str:
    rank = b.get("rule") in synth.RANK_RULES
    money = b.get("rule") == "revenue"
    f = (lambda v: "#" + fnum(v)) if rank else (lambda v: fnum(v, money))
    return (f"{f(b['before'])} → {f(b['after'])}" if b.get("before") else f(b.get("after"))) if b.get("after") is not None else ""


def vis_pill(v: str) -> str:
    if not v:
        return '<span class="vis vx" title="The agent hasn’t looked yet">visibility not checked</span>'
    return f'<span class="vis v-{e(v)}">{e(VISIBILITY.get(v, v))}</span>'


def cause_tags(rep: dict) -> str:
    return "".join(f'<span class="tg">{e(CAUSES.get(c, c))}</span>' for c in rep.get("causes") or [])


def platforms(rep: dict) -> list:
    out = [rep["source"]] + [s["source"] for s in rep.get("siblings") or []]
    return sorted(set(out), key=lambda s: ("play", "ios").index(s) if s in ("play", "ios") else 9)


def db_item(row: dict, base: str) -> str:
    rep = row["rep"]
    p, g = rep["product"], rep["grade"]
    plats = platforms(rep)
    verdict = rep.get("verdict") or rep.get("what") or (p.get("description") or "").strip().split("\n")[0][:200]
    follow = rep.get("how_to_follow") or (rep.get("follow") or {}).get("wedge") or ""
    text = " ".join([p.get("name") or "", rep["direction_name"], verdict, follow, p.get("developer") or "",
                     " ".join(CAUSES.get(c, c) for c in rep.get("causes") or [])]).lower()
    return f"""<li data-p="{' '.join(plats)}" data-v="{e(rep.get('visibility') or 'x')}" data-g="{g['grade']}" data-text="{e(text)}">
  <span class="lg">{icon(p, 52)}</span>
  <div class="bd">
    <div class="hd"><a class="nm" href="{base}db/p/{slug(row['entity'])}.html">{e(short(p.get('name'), 60))}</a>{''.join(f'<i class="st">{PLATFORM.get(x, x)}</i>' for x in plats)}</div>
    {f'<div class="vd">{e(verdict)}</div>' if verdict else ''}
    {f'<div class="how"><b>How to follow</b> {e(follow)}</div>' if follow else ''}
    <div class="mt">{vis_pill(rep.get('visibility'))}{cause_tags(rep)}<a class="tg ghost" href="{base}d/{e(rep['direction'])}.html">{e(rep['direction_name'])}</a>
      <span class="muted">{e(p.get('developer') or '')}{' · ' if p.get('developer') else ''}{len(row['breakouts'])} breakout{'s' if len(row['breakouts']) > 1 else ''} · last {fdate(rep['day'])}</span></div>
  </div>
  <div class="rc"><span class="grade g-{g['grade']}" title="{e(g['text'])}">{g['grade']} · {g['score']}</span>
    <span class="mv">{move_text(rep['badge'])}</span><small>{e(rep['badge'].get('metric') or '')}</small></div>
</li>"""


def db_nav(active: str, lens_counts: dict, n_briefs: int) -> str:
    tabs = "".join(f'<a class="tab{" on" if k == active else ""}" href="{f}">{e(appdb.LENSES[k][0])} <span>{lens_counts.get(k, 0)}</span></a>'
                   for k, f in LENS_FILES)
    tabs += f'<a class="tab{" on" if active == "briefs" else ""}" href="briefs.html">Investigated by us <span>{n_briefs}</span></a>'
    return f'<div class="tabs dbtabs">{tabs}</div>'


def age_text(days) -> str:
    if days is None:
        return ""
    if days < 31:
        return f"launched {days} days ago"
    if days < 365:
        return f"launched {round(days / 30.4)} months ago"
    return f"launched {days / 365:.1f} years ago"


def lens_row(r: dict, base: str, inv: dict) -> str:
    href = inv.get((r["source"], r["pid"]))
    link = f'{base}db/p/{href}.html' if href else r["url"]
    ext = "" if href else ' target="_blank" rel="noopener"'
    plats = " ".join(r["platforms"])
    fol = ""
    if r.get("followers"):
        chips = "".join(f'<span class="fchip">{icon(f, 18)}{e(short(f["name"], 22))} <b>{fusd(f["usd"])}</b></span>'
                        for f in r["followers"])
        fol = f'<div class="fol"><span class="muted">{r["n_followers"]} similar earn{"s" if r["n_followers"] == 1 else ""}:</span>{chips}</div>'
    money = (f'<span class="mv">{fusd(r["usd"])}<small>/mo</small></span><small>{"verified MRR" if r["label"] == "verified" else "estimated"}'
             f'{"" if r["label"] == "verified" else " · " + fusd(r["usd"] * .4) + "–" + fusd(r["usd"] * 2.5)}</small>'
             if r.get("usd") else f'<span class="mv">{int(r["users"] or 0):,}</span><small>users</small>')
    chg = f'<small class="up">↑{int(r["chg"])} today</small>' if r.get("chg") else ""
    text = " ".join([r["name"], r["developer"] or "", r["direction_name"], r["desc"] or "", r["basis"] or ""]).lower()
    return f"""<li data-p="{e(plats)}" data-v="x" data-g="x" data-text="{e(text)}">
  <span class="lg">{icon(r, 52)}</span>
  <div class="bd">
    <div class="hd"><a class="nm" href="{e(link)}"{ext}>{e(short(r['name'], 60))}</a>{f'<span class="age">{age_text(r["age_days"])}</span>' if r.get('age_days') is not None else ''}{''.join(f'<i class="st">{PLATFORM.get(x, x)}</i>' for x in r['platforms'])}</div>
    <div class="line">{e(r['developer'] or '')}{' · ' if r['developer'] else ''}<a href="{base}d/{e(r['direction'])}.html">{e(r['direction_name'])}</a>{(' · ' + e(r['basis'])) if r.get('basis') else ''}</div>
    {f'<div class="vd">{e(r["desc"])}</div>' if r.get('desc') else ''}
    {fol}
  </div>
  <div class="rc">{money}{chg}</div>
</li>"""


def db_lens_page(key: str, rows: list, lanes: list, inv: dict, lens_counts: dict, n_briefs: int) -> str:
    base = "../"
    title, sub = appdb.LENSES[key]
    plats = sorted({x for r in rows for x in r["platforms"]}, key=lambda x: list(PLATFORM).index(x) if x in PLATFORM else 99)
    pf = '<span class="grp"><button data-g="p" data-x="" class="on">All</button>' + "".join(
        f'<button data-g="p" data-x="{x}">{PLATFORM.get(x, x)}</button>' for x in plats) + "</span>"
    items = "".join(lens_row(r, base, inv) for r in rows[:150])
    lane_html = "".join(
        f'<a class="cat c{i % 6}" href="{base}d/{e(l["slug"])}.html"><span class="ics">{"".join(icon(x, 26) for x in l["examples"][:3])}</span>'
        f'<b>{e(l["name"])}</b><small>{l["new_10k"]} new earning $10k+ · {l["total"]:,} tracked</small></a>'
        for i, l in enumerate([l for l in lanes if l["slug"] != "other" and l["new_10k"]][:12]))
    return f"""<section class="hero slim"><h1>Product DB</h1>
<p class="sub">{e(sub)} Revenue for store apps and Shopify apps is <b>estimated</b> from grossing rank or review count (it can
be off by 2–3× either way); Web &amp; SaaS revenue is payment-verified. Games and big publishers are left out: these lists are
for one or two builders.</p></section>
{db_nav(key, lens_counts, n_briefs)}
<div class="dbf">{pf}<input class="dbq" type="search" placeholder="Search name, lane, developer…" aria-label="Search"><span class="muted small">showing <b class="dbn">{min(150, len(rows))}</b>{f' of {len(rows):,}' if len(rows) > 150 else ''}</span></div>
<div class="dbhead"><span>Product · what it does · who copied it</span><span>Est. per month</span></div>
<ol class="dbl">{items or '<li class="muted">Nothing matches today.</li>'}</ol>
<h2 class="sec">By lane <span class="muted">where products launched in the last year earn $10k+/month</span></h2>
<div class="cats">{lane_html}</div>"""


def db_page(surface: str, rows: list, counts: dict, lens_counts: dict | None = None) -> str:
    base = "../"
    tabs = "".join(f'<a class="{"on" if s == surface else ""}" href="{f}">{SURFACE_NAME[s]} <span>{counts.get(s, 0)}</span></a>'
                   for s, f in DB_TABS if counts.get(s) or s == surface)
    plats = sorted({x for r in rows for x in platforms(r["rep"])})
    pf = ("" if len(plats) < 2 else '<span class="grp">' + '<button data-g="p" data-x="" class="on">All</button>' + "".join(
        f'<button data-g="p" data-x="{x}">{PLATFORM.get(x, x)}</button>' for x in plats) + "</span>")
    vf = ('<span class="grp"><button data-g="v" data-x="" class="on">Any visibility</button>' + "".join(
        f'<button data-g="v" data-x="{k}">{e(v)}</button>' for k, v in VISIBILITY.items()) + "</span>")
    gf = ('<span class="grp"><button data-g="g" data-x="" class="on">All grades</button>' + "".join(
        f'<button data-g="g" data-x="{x}">{x}</button>' for x in "SABCDE" if any(r["rep"]["grade"]["grade"] == x for r in rows))
        + "</span>")
    items = "".join(db_item(r, base) for r in rows)
    return f"""<section class="hero slim"><h1>Product DB</h1>
<p class="sub">Every product that crossed a line and got a brief, kept and re-measured daily. For each one: why it took off, how you
could follow without cloning it, and a grade for the odds that one or two people make money from it within months:
<b>S</b> act now · <b>A</b> worth following, one or two bets · <b>B</b> can try, clear weak spots · <b>C</b> learn from it ·
<b>D</b> just be aware · <b>E</b> don't touch. The coloured label says how many people already know it: the fewer, the better
the opening. Sorted by grade.</p></section>
{db_nav("briefs", lens_counts or {}, sum(counts.values()))}
<div class="tabs static subtabs">{tabs}</div>
<div class="dbf">{pf}{vf}{gf}<input class="dbq" type="search" placeholder="Search name, move, market…" aria-label="Search"><span class="muted small">showing <b class="dbn">{len(rows)}</b></span></div>
<ol class="dbl">{items or '<li class="muted">Nothing here yet: products appear once they get a brief.</li>'}</ol>"""


def product_guidance(rep: dict, base: str, in_plays: dict, money: dict | None, lane: dict | None) -> str:
    plays = {m["category"]: m for m in rep.get("plays") or [] if m.get("category")}
    p = rep["product"]

    def play_card(cat):
        m = plays.get(cat)
        if not m:
            return ""
        pls = in_plays.get((rep["id"], cat), [])
        return (f'<p class="mv1">{e(m.get("move"))}</p>' + (f'<p>{e(m["why"])}</p>' if m.get("why") else "")
                + (f'<p class="muted">{e(m["did"])}</p>' if m.get("did") else "")
                + (f'<p><span class="k2">Result</span> {e(m["result"])} {causality_tag(m.get("causality"))}</p>' if m.get("result") else "")
                + "".join(f'<p><a href="{base}plays/{pid}.html">In the playbook: {e(rc)} →</a></p>' for pid, rc in pls))
    why = rep.get("verdict") or next((c["text"] for c in rep.get("why_grew") or [] if c.get("label") != "not_found"), "")
    why_html = (f'<p class="mv1">{e(why)}</p>' if why else '<p class="muted">The trigger is not explained yet.</p>') + (
        f'<p>{cause_tags(rep)}</p>' if rep.get("causes") else "")
    pos = rep.get("positioning") or {}
    direction = play_card("direction")
    if not direction:
        bits = []
        if pos.get("before_it") or pos.get("wedge"):
            bits.append(f'<p class="mv1">{e(pos.get("wedge") or "")}</p>')
            if pos.get("before_it"):
                bits.append(f'<p><span class="k2">Before it</span> {e(pos["before_it"])}</p>')
        if lane and lane.get("new_10k"):
            bits.append(f'<p>In <a href="{base}d/{e(lane["slug"])}.html">{e(lane["name"])}</a>, {lane["new_10k"]} products '
                        f'launched in the last year earn $10k+/month (estimated): the lane is open to newcomers.</p>')
        elif lane:
            bits.append(f'<p>{e(lane["name"])}: {lane["total"]:,} products tracked, none launched in the last year earns '
                        f'$10k+/month yet.</p>')
        direction = "".join(bits) or '<p class="muted">No direction evidence yet.</p>'
    growth = play_card("growth")
    if not growth:
        b = rep.get("badge") or {}
        de = rep.get("demand_echo") or {}
        growth = (f'<p class="mv1">{e(rep.get("mechanism") or RULE_TEXT.get(b.get("rule"), "Unexplained climb"))}</p>'
                  f'<p>{e(b.get("metric"))} {move_text(b)} {e(b.get("window") or "")}.</p>'
                  + (f'<p>{de["threads_14d"]} buyer-intent Reddit threads in this lane over 14 days.</p>' if de.get("threads_14d") else ""))
    monet = play_card("monetization")
    if not monet:
        model = ("in-app purchases" if p.get("iap") else (f"paid upfront, {p['price']}" if p.get("price") and p["price"] != "Free" else ""))
        bits = [f'<p class="mv1">{e(model.capitalize())}</p>'] if model else []
        if money and money.get("usd"):
            bits.append(f'<p><b>{fusd(money["usd"])}/month</b> {"verified MRR" if money["label"] == "verified" else "estimated from " + e(money["basis"])}.</p>')
        monet = "".join(bits) or '<p class="muted">No money signal in the data.</p>'
    f = rep.get("follow") or {}
    you = rep.get("how_to_follow") or f.get("wedge") or ""
    you_html = ""
    if you or f.get("play") or f.get("avoid"):
        you_html = ('<div class="you"><h3>If it were you</h3>'
                    + (f'<p><span class="k">Do</span>{e(you)}</p>' if you else "")
                    + (f'<p><span class="k">Copy</span>{e(f["play"])}</p>' if f.get("play") else "")
                    + (f'<p><span class="k">Avoid</span>{e(f["avoid"])}</p>' if f.get("avoid") else "") + "</div>")
    cols = "".join(f'<div class="gcol {c}"><h3>{t}</h3>{h}</div>' for t, c, h in (
        ("Why it moved", "c5", why_html), ("Direction", "c0", direction), ("Growth", "c2", growth), ("Money", "c3", monet)))
    return f'<section class="guide prod"><div class="gcols four">{cols}</div>{you_html}</section>'


def product_page(row: dict, charts: list, in_plays: dict | None = None, money: dict | None = None,
                 lane: dict | None = None) -> str:
    rep = row["rep"]
    p, g = rep["product"], rep["grade"]
    base = "../../"
    plats = platforms(rep)
    verdict = rep.get("verdict") or ""
    follow = rep.get("how_to_follow") or (rep.get("follow") or {}).get("wedge") or ""
    what = rep.get("what") or (p.get("description") or "").strip().split("\n")[0][:240]
    m, sm = rep.get("measure") or {}, rep.get("sibling_measure") or {}
    facts = []
    if p.get("released"):
        facts.append(f"launched {p['released']}" + (f" ({p['age_days']} days ago)" if p.get("age_days") is not None else ""))
    inst = m.get("installs") if rep["source"] == "play" else sm.get("installs")
    if inst:
        facts.append(f"Android installs {fnum(inst)}")
    if m.get("ratings"):
        facts.append(f"{PLATFORM.get(rep['source'])} ratings {fnum(m['ratings'])}")
    if m.get("stars"):
        facts.append(f"{fnum(m['stars'])} stars")
    charts_on = rep.get("charts") or []
    if charts_on:
        best = min(charts_on, key=lambda c: c["rank"])
        facts.append(f"best rank today #{best['rank']} on {e(best['chart'])}")
    summ = [("What it is", e(what)), ("Why it took off", e(verdict) or '<span class="muted">Not checked yet: the agent '
                                                                         'investigation fills this in.</span>'),
            (grade_badge(g) + " How you could follow", e(follow) or '<span class="muted">No wedge found in the data.</span>'),
            ("Grade", f"<b>{g['grade']}: {e(g['text'])}</b> <span class='muted'>score {g['score']}/100</span> "
                      f"{vis_pill(rep.get('visibility'))} {cause_tags(rep)}")]
    summ_html = "".join(f'<div class="kv"><span class="k">{k}</span><div>{v}</div></div>' for k, v in summ)
    story = "".join(f'<h3>{e(s["heading"])}</h3>' + "".join(f"<p>{e(par)}</p>" for par in str(s["body"]).split("\n") if par.strip())
                    for s in rep.get("story") or [])
    if not story:
        why = "".join(f'<li>{chip(c.get("label", "inferred"))} {e(c.get("text"))}'
                      + (f' <a href="{e(c["url"])}" target="_blank" rel="noopener">↗</a>' if c.get("url") else "") + "</li>"
                      for c in rep.get("why_grew", []))
        disc = "".join(f"<li>{e(x)}</li>" for x in rep.get("discounts", []))
        story = (f'<p class="muted">The long-form write-up (where users come from, how it makes money, who built it, what it '
                 f'does badly, what you could do) is written by the agent investigation. Until then, what the data says:</p>'
                 f'<h3>Why it moved</h3><ul class="claims">{why}</ul>'
                 + (f'<h3>Discount the numbers</h3><ul>{disc}</ul>' if disc else ""))
    brk = "".join(f'<tr><td>{fdate(r["day"])}</td><td>{e(RULE_TEXT.get(r["badge"].get("rule"), r["badge"].get("rule")))}</td>'
                  f'<td>{e(r["badge"].get("metric"))} <b class="num">{move_text(r["badge"])}</b></td><td>{grade_badge(r["grade"])}</td>'
                  f'<td><a href="{base}i/{slug(r["id"])}.html">{e(r["lesson_title"])} →</a></td></tr>' for r in row["breakouts"])
    comps = "".join(f'<tr><td>{("<a href=" + chr(34) + e(c["url"]) + chr(34) + " target=_blank rel=noopener>" + e(c["name"]) + "</a>") if c.get("url") else e(c["name"])}</td>'
                    f'<td class="muted">{e(c.get("note") or c.get("how_it_differs"))}</td></tr>' for c in rep.get("competitors", []))
    links = [f'<a href="{e(p.get("url"))}" target="_blank" rel="noopener">{PLATFORM.get(rep["source"], "Source")} page ↗</a>']
    links += [f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{PLATFORM.get(s["source"])} page ↗</a>'
              for s in rep.get("siblings") or []]
    if p.get("site"):
        links.append(f'<a href="{e(p["site"])}" target="_blank" rel="noopener">Website ↗</a>')
    chart_html = "".join(linechart(c) for c in charts)
    body = f"""<a class="back" href="{base}db/{dict(DB_TABS).get(rep['surface'], 'briefs.html')}">← Product DB · {e(SURFACE_NAME.get(rep['surface'], ''))}</a>
<div class="crumb">{e(SURFACE_NAME.get(rep['surface'], ''))} · {' + '.join(PLATFORM.get(x, x) for x in plats)} · written {fdate(rep['day'])}</div>
<header class="phead"><div>
<div class="who big">{icon(p, 52)}<span><b>{e(p.get('name'))}</b>{(' · ' + e(p['developer'])) if p.get('developer') else ''}</span></div>
<h1 class="ph1">{e(rep['lesson_title'])}</h1></div>
<div class="gbox">{grade_badge(g, True)}<b>{g['score']} / 100</b><span>{e(g['text'])}</span></div></header>
{product_guidance(rep, base, in_plays or {}, money, lane)}
<section class="kvs">{summ_html}</section>
<section class="blk"><h2>Data <span class="muted">updated daily</span></h2>
  <p class="facts">{' · '.join(facts) or '<span class="muted">No store measurements for this surface.</span>'}</p>
  <div class="lcs">{chart_html or '<p class="muted">No time series for this product yet.</p>'}</div></section>
<section class="blk story">{story}</section>
<section class="blk"><h2>Breakouts we recorded</h2><div class="tblwrap"><table class="tbl prodbrk"><tbody>{brk}</tbody></table></div></section>
{f'<section class="blk"><h2>Peers</h2><table class="tbl"><tbody>{comps}</tbody></table></section>' if comps else ''}
<p class="links">{' · '.join(links)}</p>"""
    return page(f"{p.get('name')} · Product DB · {SITE}", body, base=base, active="db",
                desc=f"{p.get('name')}: {verdict or rep['lesson_title']}", day=rep["day"])


def plays_index(plays: list) -> str:
    base = "../"
    cats = {k: sum(1 for p in plays if p["category"] == k) for k in PLAY_CATEGORIES}
    induced = any(p["induced"] for p in plays)
    tabs = (f'<button class="tab on" data-f="all">All <span>{len(plays)}</span></button>' + "".join(
        f'<button class="tab" data-f="{k}">{e(v)} <span>{cats[k]}</span></button>' for k, v in PLAY_CATEGORIES.items() if cats[k]))
    rows = ""
    for i, pl in enumerate(plays, 1):
        icons = "".join(icon(c["rep"]["product"], 22) for c in pl["cases"][:6])
        head = (f'<a class="rc" href="{pl["id"]}.html">{e(pl["recipe"])}</a>' if pl["induced"] else f'<b class="rc">{e(pl["recipe"])}</b>')
        cases = "" if pl["induced"] else '<ul class="plain small">' + "".join(
            f'<li>{grade_badge(c["rep"]["grade"])} <a href="{base}i/{slug(c["rid"])}.html">{e(short(c["rep"]["product"]["name"]))}</a> '
            f'<span class="muted">{fdate(c["rep"]["day"])} · {e(c["rep"]["badge"].get("metric"))}</span></li>' for c in pl["cases"][:5]) + "</ul>"
        why = f'<div class="why">{e(pl["why"])}</div>' if pl.get("why") else ""
        rows += (f'<li data-surface="{e(pl["category"])}" data-text="{e((pl["recipe"] + " " + pl.get("why", "")).lower())}">'
                 f'<span class="no">{i}</span><div>{head}{why}'
                 f'<div class="mt"><span>{pl["n"]} products{(" · " + str(pl["n_verified"]) + " with a clear cause") if pl["induced"] else (" · " + e(pl.get("status", "")))}'
                 f' · last seen {fdate(pl["last"])}</span><span class="tg">{e(PLAY_CATEGORIES.get(pl["category"], ""))}</span>'
                 f'<span class="ics">{icons}</span></div>{cases}</div></li>')
    note = ("" if induced else '<div class="note">The playbook is induced by the agent from the growth move found in each '
            'investigation, and a move becomes a play once two or more products used it. No agent run has produced one yet, '
            'so below are the growth mechanisms tagged on each brief.</div>')
    return f"""<section class="hero slim"><h1>Playbooks</h1><p class="sub">Concrete moves that more than one product used recently and
that you can copy. Induced from the products we investigated, then checked case by case: what each one did, what happened, how sure we
are it caused the lift, and who tried the same move without a lift. Follow the play, not the category.</p></section>
{note}<div class="bar"><div class="tabs">{tabs}</div><input class="search" type="search" placeholder="Filter plays" aria-label="Filter"></div>
<ol class="playl">{rows or '<li class="muted">Playbooks form as investigations accumulate.</li>'}</ol>"""


def causality_tag(c: str) -> str:
    return f'<span class="cz cz-{e(c)}">{e(CAUSALITY.get(c, c))}</span>' if c in CAUSALITY else ""


def play_page(pl: dict, num: int, day: str) -> str:
    base = "../"
    steps = "".join(f'<li><p class="do">{e(s["do"])}{" <span class=inf>inferred step: no case shows it directly</span>" if s.get("inferred") else ""}</p>'
                    + (f'<blockquote>{e(s["evidence"])}</blockquote>' if s.get("evidence") else "") + "</li>"
                    for s in pl.get("steps") or [])

    def case(c):
        r = c["rep"]
        p = r["product"]
        return (f'<article class="case"><div class="ch">{icon(p, 36)}<div><b>{e(short(p.get("name"), 50))}</b>'
                f'<i>{e(r.get("what") or r["direction_name"])}</i></div><span class="fg">{e(r["badge"].get("metric"))} {move_text(r["badge"])}</span></div>'
                + (f'<p>{e(c.get("did"))}</p>' if c.get("did") else "")
                + (f'<p class="rs"><span class="k">Result</span> {e(c.get("result"))} {causality_tag(c.get("causality"))}</p>'
                   if c.get("result") else "")
                + f'<a href="{base}db/p/{slug(r["entity"])}.html">product page</a> · <a href="{base}i/{slug(r["id"])}.html">full investigation →</a></article>')

    def counter(c):
        r = c.get("rep")
        name = e(short(r["product"].get("name"), 50)) if r else e(c.get("name"))
        link = f' <a href="{base}i/{slug(r["id"])}.html">investigation →</a>' if r else ' <span class="muted small">(not investigated by us)</span>'
        return f'<li><b>{name}</b> {e(c.get("what"))}{link}</li>'
    cases = "".join(case(c) for c in pl["cases"])
    counters = "".join(counter(c) for c in pl["counter"])
    risks = "".join(f"<li>{e(x)}</li>" for x in pl.get("risks") or [])
    suits = ""
    if pl.get("suits") or pl.get("prerequisites") or risks:
        suits = ('<section class="blk"><h2>Who it suits, and when it doesn’t work</h2>'
                 + (f'<p>{e(pl["suits"])}</p>' if pl.get("suits") else "")
                 + (f'<h3>Prerequisites</h3><p>{e(pl["prerequisites"])}</p>' if pl.get("prerequisites") else "")
                 + (f'<h3>Risks</h3><ol>{risks}</ol>' if risks else "") + "</section>")
    notes = "".join(f"<p>{e(x)}</p>" for x in pl.get("notes") or [])
    if pl.get("changed"):
        notes += f'<p class="muted"><b>What checking changed:</b> {e(pl["changed"])}</p>'
    icons = "".join(icon(c["rep"]["product"], 26) for c in pl["cases"][:8])
    body = f"""<a class="back" href="index.html">← Playbooks</a>
<div class="crumb">#{num} · {e(PLAY_CATEGORIES.get(pl['category'], ''))}</div>
<h1 class="ph1">{e(pl['recipe'])}</h1>
{f'<p class="lede">{e(pl["why"])}</p>' if pl.get('why') else ''}
<p class="proof"><span class="ics">{icons}</span>{pl['n']} products used it · {pl['n_verified']} with a clear cause · last verified {fdate(pl['last'])}</p>
{f'<h2 class="sec">How to do it</h2><ol class="steps">{steps}</ol>' if steps else ''}
<h2 class="sec">Who did it</h2><div class="cases">{cases}</div>
{f'<h2 class="sec">Tried it, didn’t work</h2><section class="blk"><ul class="plain cnt">{counters}</ul></section>' if counters else ''}
{suits}
{f'<section class="blk story"><h2>Worth saying more</h2>{notes}</section>' if notes else ''}"""
    return page(f"{pl['recipe'][:70]} · Playbooks · {SITE}", body, base=base, active="plays", desc=pl.get("why") or pl["recipe"],
                day=day)


CAT_FILES = {"apps": "apps.html", "minigames": "minigames.html", "saas": "web.html", "chrome": "chrome.html",
             "shopify": "shopify.html"}


def guidance_html(g: dict) -> str:
    def pts(xs):
        return "".join(f'<li><b>{e(x.get("point"))}</b>' + (f'<span>{e(x.get("evidence"))}</span>' if x.get("evidence") else "")
                       + "</li>" for x in xs or [] if isinstance(x, dict) and x.get("point"))
    cols = ""
    for k, t, cls in (("direction", "Where to look", "c0"), ("growth", "How users arrive", "c2"), ("money", "How they charge", "c3")):
        li = pts(g.get(k))
        cols += f'<div class="gcol {cls}"><h3>{t}</h3><ul>{li or "<li class=muted>Not enough evidence yet.</li>"}</ul></div>'
    solo = g.get("solo") or {}
    steps = "".join(f"<li>{e(x)}</li>" for x in solo.get("first_week") or [])
    you = ""
    if solo.get("build") or solo.get("avoid"):
        you = ('<div class="you"><h3>If you build here</h3>'
               + (f'<p><span class="k">Build</span>{e(solo["build"])}</p>' if solo.get("build") else "")
               + (f'<p><span class="k">Avoid</span>{e(solo["avoid"])}</p>' if solo.get("avoid") else "")
               + (f'<ol>{steps}</ol>' if steps else "") + "</div>")
    by = ('<span class="lbl lbl-inferred">agent analysis</span>' if g.get("by") == "agent"
          else '<span class="lbl lbl-not_found">rules from the data</span>')
    summ = f'<p class="gs">{e(g["summary"])}</p>' if g.get("summary") else ""
    return (f'<section class="guide"><p class="gh">{e(g.get("headline"))}</p>{summ}'
            f'<div class="gcols">{cols}</div>{you}<p class="muted small">{by}</p></section>')


def mini_rows(rows: list, base: str, inv: dict, n: int = 12) -> str:
    return '<ol class="dbl">' + "".join(lens_row(r, base, inv) for r in rows[:n]) + "</ol>"


def lanes_table(lanes: list, base: str) -> str:
    body = "".join(f'<tr><td><a href="{base}d/{e(l["slug"])}.html">{e(l["name"])}</a></td><td class="num"><b>{l["new_10k"]}</b></td>'
                   f'<td class="num">{l["total"]:,}</td><td class="num">{fusd(l["usd"])}</td><td>'
                   + " · ".join(f'{e(short(x["name"], 26))} <span class="muted">{fusd(x["usd"])}</span>' for x in l["examples"][:3])
                   + "</td></tr>" for l in lanes if l["slug"] != "other")
    return (f'<div class="tblwrap"><table class="tbl"><thead><tr><th>Lane</th><th>New, $10k+/mo</th><th>Tracked</th>'
            f'<th>Est. month, all</th><th>Who</th></tr></thead><tbody>{body}</tbody></table></div>')


def bars(items: list) -> str:
    return '<div class="bars">' + "".join(
        f'<div class="hb"><span>{e(k)}</span><i style="width:{max(2, share * 100):.0f}%"></i><b>{v:,}</b></div>'
        for k, v, share in items) + "</div>"


def cat_page(surface: str, st: dict, g: dict, briefs: list, inv: dict) -> str:
    base = "../"
    name, sub = categories.SURFACES[surface]
    tiles = "".join(f'<div class="tile"><b>{e(v)}</b><span>{e(k)}</span>{f"<em>{e(h)}</em>" if h else ""}</div>'
                    for v, k, h in st["kpis"])
    nav = "".join(f'<a class="{"on" if k == surface else ""}" href="{f}">{e(categories.SURFACES[k][0])}</a>' for k, f in CAT_FILES.items())
    body = ""
    if st.get("lanes"):
        body += f'<h2 class="sec">Lanes <span class="muted">sorted by how many products launched in the last year earn $10k+/month</span></h2>{lanes_table(st["lanes"], base)}'
    if st.get("models"):
        body += f'<h2 class="sec">How the earners charge</h2>{bars(st["models"])}'
    if st.get("markets"):
        tot = sum(v for _, v in st["markets"]) or 1
        body += (f'<h2 class="sec">Where newcomers make money <span class="muted">country of the chart that ranks them best</span></h2>'
                 + bars([(k, v, v / tot) for k, v in st["markets"]]))
    if st.get("top_new"):
        what = "users" if surface == "chrome" else "estimated month"
        body += f'<h2 class="sec">Newcomers that already earn <span class="muted">launched recently, sorted by {what}</span></h2>{mini_rows(st["top_new"], base, inv)}'
    if st.get("growers"):
        body += f'<h2 class="sec">Fastest-growing MRR <span class="muted">30-day growth, payment-verified</span></h2>{mini_rows(st["growers"], base, inv)}'
    if st.get("top") and not st.get("top_new"):
        body += f'<h2 class="sec">Biggest earners</h2>{mini_rows(st["top"], base, inv)}'
    if st.get("cats"):
        rows = "".join(f'<tr><td>{e(c)}</td><td class="num">{n}</td><td class="num">{u:,}</td><td class="num"><b>{y}</b></td></tr>'
                       for c, n, u, y in st["cats"])
        body += (f'<h2 class="sec">Store categories</h2><div class="tblwrap"><table class="tbl"><thead><tr><th>Category</th>'
                 f'<th>Tracked</th><th>Users, all</th><th>Published ≤2 years</th></tr></thead><tbody>{rows}</tbody></table></div>')
    if st.get("genres"):
        tot = sum(v for _, v in st["genres"]) or 1
        body += f'<h2 class="sec">What charts on the boards <span class="muted">genre of every chart slot today</span></h2>' + bars(
            [(k, v, v / tot) for k, v in st["genres"]])
    if st.get("fresh"):
        rows = "".join(f'<tr><td>{e(f["name"])}</td><td class="muted">{e(f["category"])}</td><td>{e(f["board"])}</td>'
                       f'<td class="num"><b>#{f["rank"]}</b></td></tr>' for f in st["fresh"])
        body += f'<h2 class="sec">New on the boards</h2><div class="tblwrap"><table class="tbl"><tbody>{rows}</tbody></table></div>'
    if st.get("publishers"):
        tot = sum(v for _, v in st["publishers"]) or 1
        body += '<h2 class="sec">Who publishes them</h2>' + bars([(k, v, v / tot) for k, v in st["publishers"]])
    if briefs:
        body += (f'<h2 class="sec">Investigated here, last 14 days <span class="muted">{len(briefs)} briefs</span></h2>'
                 f'<div class="cards">{"".join(card(r, base) for r in sorted(briefs, key=lambda r: -r["grade"]["score"])[:12])}</div>')
    return f"""<section class="hero slim"><h1>{e(name)}</h1><p class="sub">{e(sub)}. What is working here, for whom, and what one or
two people could build: guidance first, then the numbers behind it.</p></section>
<div class="tabs static subtabs">{nav}</div>
{guidance_html(g)}
<div class="tiles">{tiles}</div>
{body}"""


def cat_index(st: dict, guid: dict) -> str:
    cards = ""
    for i, (k, f) in enumerate(CAT_FILES.items()):
        g = guid.get(k, {}).get("guidance") or {}
        v, lbl, _ = st[k]["kpis"][1]
        cards += (f'<a class="ccard c{i % 6}" href="{f}"><span class="cn">{e(categories.SURFACES[k][0])}</span>'
                  f'<b>{e(g.get("headline") or "")}</b><span class="ck"><em>{e(v)}</em> {e(lbl)}</span></a>')
    return f"""<section class="hero slim"><h1>Categories</h1><p class="sub">One deep page per kind of product: apps, mini-programs,
web &amp; SaaS, Chrome extensions and Shopify apps. Each says where the openings are, how products there get users, how they
charge, and what a solo builder should try first.</p></section><div class="ccards">{cards}</div>"""


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
- [Product DB](db/index.html): money lenses (followed and earning, unique angle, new and earning) over every app, SaaS and
  Shopify app we can price, plus every product we investigated
- [Categories](cat/index.html): one deep page per surface: apps, mini-programs, web & SaaS, Chrome extensions, Shopify apps
- [Playbooks](plays/index.html): copyable moves verified by more than one product
- [Directions](d/index.html), [Charts](charts.html), [Track record](record.html)

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
    for sub in ("i", "d", "day", "api", "assets", "db"):
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
    plays = playbook.assemble(con, day)
    (OUT / "plays").mkdir(exist_ok=True)
    (OUT / "plays" / "index.html").write_text(page(f"Playbooks · {SITE}", plays_index(plays), base="../", active="plays",
                                                   day=day), encoding="utf-8")
    for i, pl in enumerate(plays, 1):
        if pl["induced"]:
            (OUT / "plays" / f"{pl['id']}.html").write_text(play_page(pl, i, day),
                                                            encoding="utf-8")
    rows = synth.products(con)
    db_counts = {s: sum(1 for r in rows if r["rep"]["surface"] == s) for s in SURFACE_ORDER}
    (OUT / "db" / "p").mkdir(parents=True, exist_ok=True)
    # v4: the money lenses over every product we can price, and one deep page per category
    uday = appdb._day(con)
    uni = appdb.universe(con, uday)
    lens = appdb.lenses(uni, uday)
    lens_counts = {k: len(v) for k, v in lens.items()}
    lanes = appdb.by_lane(appdb.solo_fit(uni))
    lane_of = {l["slug"]: l for l in lanes}
    inv, money_of = {}, {}
    by_key = {(r["source"], r["pid"]): r for r in uni}
    for r in rows:
        rep = r["rep"]
        for src, pid in [(rep["source"], rep["pid"])] + [(x["source"], x["pid"]) for x in rep.get("siblings") or []]:
            inv[(src, pid)] = slug(r["entity"])
            if (src, pid) in by_key and r["entity"] not in money_of:
                money_of[r["entity"]] = by_key[(src, pid)]
    for k, fname in LENS_FILES:
        (OUT / "db" / fname).write_text(page(f"{appdb.LENSES[k][0]} · Product DB · {SITE}",
                                             db_lens_page(k, lens[k], lanes, inv, lens_counts, sum(db_counts.values())),
                                             base="../", active="db", day=day), encoding="utf-8")
    for s, fname in DB_TABS:
        (OUT / "db" / fname).write_text(page(f"Product DB · {SURFACE_NAME[s]} · {SITE}",
                                             db_page(s, [r for r in rows if r["rep"]["surface"] == s], db_counts, lens_counts),
                                             base="../", active="db", day=day), encoding="utf-8")
    cat_stats = categories.stats(con, uday, uni)
    guid = categories.load().get("surfaces") or {}
    (OUT / "cat").mkdir(exist_ok=True)
    (OUT / "cat" / "index.html").write_text(page(f"Categories · {SITE}", cat_index(cat_stats, guid), base="../",
                                                 active="cats", day=day), encoding="utf-8")
    recent = [r for r in all_reps if r["day"] >= (datetime.strptime(day, "%Y-%m-%d") - timedelta(days=14)).strftime("%Y-%m-%d")]
    for k, fname in CAT_FILES.items():
        g = (guid.get(k) or {}).get("guidance") or categories._rules(k, cat_stats[k], [r for r in recent if r["surface"] == k])
        (OUT / "cat" / fname).write_text(page(f"{categories.SURFACES[k][0]} · Categories · {SITE}",
                                              cat_page(k, cat_stats[k], g, [r for r in recent if r["surface"] == k], inv),
                                              base="../", active="cats", day=day), encoding="utf-8")
    in_plays = {}
    for pl in plays:
        if pl["induced"]:
            for c in pl["cases"]:
                in_plays.setdefault((c["rid"], pl["category"]), []).append((pl["id"], pl["recipe"]))
    for r in rows:
        (OUT / "db" / "p" / f"{slug(r['entity'])}.html").write_text(product_page(r, synth.history(con, r["rep"]), in_plays,
                                                                                 money_of.get(r["entity"]),
                                                                                 lane_of.get(r["rep"]["direction"])),
                                                                    encoding="utf-8")
    (OUT / "record.html").write_text(page(f"Track record · {SITE}", record_page(synth.followups(con, day)), active="record",
                                          day=day), encoding="utf-8")
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

