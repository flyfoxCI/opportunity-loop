"""Render the analyze() model to a static site under docs/radar/ (plain HTML, no Jekyll)."""

from __future__ import annotations

import json
import os
import shutil
from datetime import datetime, timezone
from html import escape
from pathlib import Path

from .store import ROOT

OUT = ROOT / "docs" / "radar"
SITE_URL = os.environ.get("RADAR_SITE_URL", "https://flyfoxci.github.io/opportunity-loop/radar/")
STATIC = Path(__file__).parent / "static"
SRC_NAMES = {"trustmrr": "TrustMRR", "appstore": "App Store", "github": "GitHub", "reddit": "Reddit"}
SRC_GLYPH = {"trustmrr": "MRR", "appstore": "iOS", "github": "GH"}
COMP_LABEL = {"money": "Money", "momentum": "Mom.", "demand": "Dem.", "gap": "Gap", "fit": "Fit"}
VERDICT_TXT = {"ENTER": "Evidence clears the bar. Worth a 72-hour test.",
               "NARROW": "Real but crowded or thin. Pick one buyer and one angle.",
               "WATCH": "Not enough evidence yet."}
E = lambda s: escape(str(s if s is not None else ""), quote=True)  # noqa: E731

LOGO = ('<svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.5" fill="none" '
        'stroke="currentColor" stroke-width="1.5"/><circle cx="10" cy="10" r="4.5" fill="none" stroke="currentColor" '
        'stroke-width="1" opacity=".5"/><path d="M10 10 L16 4.5" stroke="currentColor" stroke-width="1.5"/>'
        '<circle cx="14.2" cy="12.6" r="1.8" fill="var(--signal)"/></svg>')


def money(v) -> str:
    if v is None or v == 0:
        return "–"
    v = float(v)
    if v >= 1_000_000:
        return f"${v / 1_000_000:.1f}M"
    if v >= 10_000:
        return f"${v / 1000:.0f}K"
    if v >= 1000:
        return f"${v / 1000:.1f}K"
    return f"${v:,.0f}"


def num(v) -> str:
    if v is None:
        return "–"
    return f"{v:,.0f}" if abs(v) >= 10 else f"{v:,.1f}".rstrip("0").rstrip(".")


def plural(n, word: str) -> str:
    return f"{n:g} {word}{'' if n == 1 else 's'}"


# ------------------------------------------------------------------ chrome

def page(title: str, body: str, base: str, active: str, description: str = "") -> str:
    def link(href, label, key):
        return f'<a class="link{" on" if key == active else ""}" href="{base}{href}">{label}</a>'
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title><meta name="description" content="{E(description or 'What is moving in indie software, why, and what to build next.')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{base}radar.css">
<link rel="alternate" type="application/rss+xml" title="Opportunity Radar daily" href="{base}feed.xml">
<script>try{{var t=localStorage.getItem("radar-theme");if(t)document.documentElement.setAttribute("data-theme",JSON.parse(t))}}catch(e){{}}</script>
</head><body>
<nav class="nav"><div class="wrap">
<a class="brand" href="{base}index.html">{LOGO}Opportunity Radar</a>
{link("index.html", "Today", "today")}{link("directions/index.html", "Directions", "directions")}
{link("check.html", "Check an idea", "check")}{link("method.html", "Method", "method")}
<a class="link" href="{base}../archive/">Build packages</a>
<span class="spacer"></span><button class="theme-btn" data-theme-toggle aria-label="Switch light or dark theme">◐</button>
</div></nav>
<main class="wrap">{body}</main>
<footer><div class="wrap">Opportunity Loop v2. Every figure carries a label: <span class="badge b-verified">verified</span>
<span class="badge b-estimated">estimated</span> or <span class="badge b-inferred">inferred</span>.
Sources: TrustMRR, Apple charts, GitHub Trending, Reddit via Arctic Shift, TinyFish.
Updated daily. <a href="{base}feed.xml">Follow by RSS</a></div></footer>
<script src="{base}radar.js"></script></body></html>"""


def label_badge(label: str) -> str:
    return f'<span class="badge b-{E(label)}">{E(label)}</span>'


def verdict_pill(v: str) -> str:
    return f'<span class="badge v-{E(v)}" title="{E(VERDICT_TXT.get(v, ""))}">{E(v)}</span>'


def meter(d: dict, compact: bool = False) -> str:
    c = d["components"]
    top = max(c, key=c.get)
    return f'<div class="meter{" compact" if compact else ""}">' + "".join(
        f'<div class="{"hi" if k == top else ""}" title="{k} {c[k]:.2f}"><span>{COMP_LABEL[k]}<b>{c[k]:.2f}</b></span>'
        f'<i><u style="width:{int(c[k] * 100)}%"></u></i></div>' for k in ("money", "momentum", "demand", "gap", "fit")) + "</div>"


def signal_vals(s: dict) -> tuple[str, str]:
    """(headline readout, sub readout)."""
    if s.get("rank"):
        if s.get("before") is None:
            return f'#{int(s["after"])}', "grossing rank"
        return f'#{int(s["after"])}', f'from #{int(s["before"])}'
    fmt = money if s["metric"] == "MRR" else num
    if s.get("mult"):
        return f'×{s["mult"]:.1f}', f'{fmt(s["before"])} → {fmt(s["after"])}'
    return fmt(s["after"]), "today"


def signal_row(s: dict, base: str) -> str:
    icon = (f'<img class="ico" src="{E(s["icon"])}" alt="" loading="lazy">' if s.get("icon")
            else f'<span class="ico">{SRC_GLYPH.get(s["source"], "")}</span>')
    head, sub = signal_vals(s)
    trace = ""
    if s.get("trace"):
        trace = ('<div class="tr">' + label_badge("inferred") + " possible trigger"
                 + "".join(f'<a href="{E(t["url"])}" target="_blank" rel="noopener">{E(t["title"] or t["url"])}</a>' for t in s["trace"][:2])
                 + "</div>")
    return f"""<article class="sig" data-f="{E(s['source'])}">{icon}
<div style="min-width:0"><a class="name" href="{E(s['url'])}" target="_blank" rel="noopener">{E(s['name'])}</a>
<div class="meta"><span>{SRC_NAMES.get(s['source'], s['source'])} · {E(s['metric'])} · {E(s['window'])}</span>{label_badge(s['label'])}
<a href="{base}directions/{E(s['direction'])}.html">{E(s['direction_name'])}</a></div>
<p class="d">{E(s.get('desc', ''))}</p></div>
<div class="read"><div class="x">{E(head)}</div><div class="v">{E(sub)}</div></div>{trace}</article>"""


def rank_row(i: int, d: dict, base: str, m: dict | None = None) -> str:
    delta = rank_delta(d, i, m) if m else ""
    return f"""<li data-slug="{E(d['slug'])}" data-f="{E(d['verdict'])} {E(d['group'])}"><span class="n">{i:02d}</span>
<div class="t"><a href="{base}directions/{E(d['slug'])}.html">{E(d['name'])}</a>{delta}<p>{E(d['why'])}</p></div>
<span class="vp">{verdict_pill(d['verdict'])}</span><span class="s">{d['score']:.2f}</span>{meter(d, compact=True)}</li>"""


def thread_row(t: dict, show_dir: bool, base: str) -> str:
    d = (f' · <a href="{base}directions/{E(t["direction"])}.html">{E(t.get("direction_name", ""))}</a>' if show_dir else "")
    when = datetime.fromtimestamp(t["created_utc"], timezone.utc).strftime("%b %d") if t.get("created_utc") else ""
    n = int(t.get("num_comments") or 0)
    return (f'<div class="thread"><div class="c">{n} repl{"y" if n == 1 else "ies"}</div><div class="t">'
            f'<a href="https://www.reddit.com/r/{E(t["subreddit"])}/comments/{E(t["id"])}/" target="_blank" rel="noopener">{E(t["title"])}</a>'
            f'<div>r/{E(t["subreddit"])} · {when}{" · u/" + E(t["author"]) if t.get("author") else ""}{d}</div></div></div>')


def health_line(m: dict) -> str:
    seen = {h["source"]: h for h in m["health"]}
    out = []
    for key in ("trustmrr", "appstore", "github", "reddit"):
        h = seen.get(key)
        cls = "off" if not h else ("" if h["ok"] else "bad")
        note = f'{h["rows"]:,} rows' if h else "not collected"
        out.append(f'<span title="{E(h["note"] if h else "")}"><span class="dot {cls}"></span>{SRC_NAMES[key]} {E(note)}</span>')
    out.append('<span><span class="dot off"></span>TinyFish trace runs in CI</span>')
    return '<div class="health">' + "".join(out) + "</div>"


def lead_block(d: dict, m: dict | None = None) -> str:
    st = d["stats"]
    delta = rank_delta(d, 1, m) if m else ""
    facts = [("Verified products (TrustMRR)", st["tm_players"]), ("At $1K+ MRR", st["tm_earners_1k"]),
             ("Top verified MRR", money(st["tm_top_mrr"])), ("Apps in US top-grossing", st["app_grossing"]),
             ("Buyer-intent Reddit posts / week", f'{st["reddit_posts"]:g}')]
    return f"""<div class="panel lead"><div>
<div class="row">{verdict_pill(d['verdict'])}<span class="eyebrow">{E(d['group'])} · ranked #1 today</span>{delta}</div>
<h2><a href="directions/{E(d['slug'])}.html">{E(d['name'])}</a></h2>
<p class="why">{E(d['why'])}. {E(VERDICT_TXT[d['verdict']])}</p>
<div class="actions"><a class="btn" href="directions/{E(d['slug'])}.html#kit">Get the 72-hour kit</a>
<a class="btn ghost" href="directions/{E(d['slug'])}.html">Open the landscape</a></div></div>
<div><div class="scorebig"><b>{d['score']:.2f}</b><span class="tiny muted">score · confidence {d['confidence']:.1f}</span></div>
{meter(d)}<ul class="facts">{''.join(f'<li><span>{k}</span><b>{v}</b></li>' for k, v in facts)}</ul></div></div>"""


# ------------------------------------------------------------------ daily briefing + history

def briefing(m: dict) -> dict:
    """The day's finding in words, shared by the page, the RSS item and the history file."""
    dirs = m["directions"]
    lead = dirs[0]
    n_enter = sum(1 for d in dirs if d["verdict"] == "ENTER")
    n_narrow = sum(1 for d in dirs if d["verdict"] == "NARROW")
    top_mult = max((s for s in m["signals"] if s.get("mult") and s["source"] == "trustmrr"),
                   key=lambda s: s["mult"], default=None)
    if n_enter:
        head_txt = f'{lead["name"]} clears the evidence bar today'
        head_html = f'<em>{E(lead["name"])}</em> clears the evidence bar today'
    else:
        head_txt = f'No niche clears the bar today, {lead["name"]} comes closest'
        head_html = f'No niche clears the bar today, <em>{E(lead["name"])}</em> comes closest'
    lede = (f'{lead["why"]}. {plural(n_narrow, "more direction")} {"is" if n_narrow == 1 else "are"} real but need a narrow wedge.'
            + (f' Fastest verified mover: {top_mult["name"]}, MRR ×{top_mult["mult"]:.1f} in {top_mult["window"]}.' if top_mult else ""))
    changes = []
    prev = m.get("prev") or {}
    if prev:
        before = prev["ranks"]
        new_enter = [d["name"] for d in dirs if d["verdict"] == "ENTER" and before.get(d["slug"], [0, ""])[1] != "ENTER"]
        dropped = [d["name"] for d in dirs if d["verdict"] != "ENTER" and before.get(d["slug"], [0, ""])[1] == "ENTER"]
        if new_enter:
            changes.append(f'New to ENTER: {", ".join(new_enter)}.')
        if dropped:
            changes.append(f'Dropped out of ENTER: {", ".join(dropped)}.')
        if not changes:
            changes.append("No change in the ENTER list.")
    return {"day": m["generated"][:10], "headline": head_txt, "headline_html": head_html, "lede": lede,
            "changes": " ".join(changes), "n_enter": n_enter, "n_narrow": n_narrow,
            "enter": [d["name"] for d in dirs if d["verdict"] == "ENTER"]}


def load_prev(day: str) -> dict | None:
    """The most recent history file from before `day`."""
    hist = OUT / "history"
    older = sorted(f for f in hist.glob("*.json") if f.stem < day) if hist.exists() else []
    return json.loads(older[-1].read_text()) if older else None


def rank_delta(d: dict, rank: int, m: dict) -> str:
    prev = m.get("prev")
    if not prev:
        return ""
    was = prev["ranks"].get(d["slug"])
    if not was:
        return '<span class="delta">new</span>'
    old_rank, old_verdict = was[0], was[1]
    bits = []
    if old_verdict != d["verdict"]:
        bits.append(f'was {old_verdict}')
    if old_rank != rank:
        bits.append(("▲" if old_rank > rank else "▼") + str(abs(old_rank - rank)))
    if not bits:
        return ""
    cls = "up" if (old_rank > rank or (d["verdict"] == "ENTER" and old_verdict != "ENTER")) else "down"
    return f'<span class="delta {cls}" title="vs {E(prev["day"])}">{" · ".join(bits)}</span>'


def feed_xml(history: list[dict]) -> str:
    items = []
    for h in sorted(history, key=lambda h: h["day"], reverse=True)[:30]:
        pub = datetime.strptime(h["day"], "%Y-%m-%d").strftime("%a, %d %b %Y 07:00:00 +0000")
        desc = " ".join(x for x in (h.get("changes", ""), h["lede"], "ENTER today: " + (", ".join(h["enter"]) or "none") + ".") if x)
        items.append(f"<item><title>{E(h['day'])}: {E(h['headline'])}</title><link>{E(SITE_URL)}</link>"
                     f"<guid isPermaLink=\"false\">radar-{E(h['day'])}</guid><pubDate>{pub}</pubDate>"
                     f"<description>{E(desc)}</description></item>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Opportunity Radar</title>'
            f'<link>{E(SITE_URL)}</link><description>Daily briefing: which indie niches have paying customers and buyers asking now</description>'
            + "".join(items) + "</channel></rss>\n")


# ------------------------------------------------------------------ pages

def index_page(m: dict) -> str:
    dirs = m["directions"]
    lead = dirs[0]
    rest = dirs[1:9]
    caps = {"trustmrr": 8, "appstore": 8, "github": 4}
    taken = {k: 0 for k in caps}
    sigs = []
    for s_ in m["signals"]:
        if taken.get(s_["source"], 99) < caps.get(s_["source"], 0):
            taken[s_["source"]] += 1
            sigs.append(s_)
    counts = {k: v for k, v in taken.items() if v}
    chips = '<button class="on" data-v="all">All</button>' + "".join(
        f'<button data-v="{k}">{SRC_NAMES[k]}</button>' for k in counts)
    b = briefing(m)
    n_enter, n_narrow = b["n_enter"], b["n_narrow"]
    intent = sum(d["stats"]["reddit_posts"] for d in dirs)
    weekday = datetime.strptime(b["day"], "%Y-%m-%d").strftime("%A %d %B %Y")
    headline = b["headline_html"]
    lede = E(b["lede"])
    since = (f'<p class="since"><span>Since {E(datetime.strptime(m["prev"]["day"], "%Y-%m-%d").strftime("%a %d %b"))}</span> {E(b["changes"])}</p>'
             if m.get("prev") else "")
    body = f"""
<header class="mast"><div class="eyebrow"><span>Daily briefing</span><span>{E(weekday)}</span><span>updated {E(m['generated'][11:])}</span></div>
<h1>{headline}</h1><p class="lede">{lede}</p>{since}
<div class="ledger"><div><b>{n_enter}</b><span>enter</span></div><div><b>{n_narrow}</b><span>narrow</span></div>
<div><b>{len(m['signals'])}</b><span>products moving</span></div><div><b>{intent:,.0f}</b><span>buyer asks on Reddit / week</span></div>
<div><b>{m['snapshot_days']}</b><span>days of MRR history</span></div></div>
{health_line(m)}</header>

<section id="watching" hidden><div class="sec-head"><div><h2>Directions you watch</h2><p>Saved in this browser</p></div></div>
<div class="panel"><ol class="rank"></ol></div></section>

<section><div class="sec-head"><h2>Lead direction</h2></div>{lead_block(lead, m)}</section>

<section><div class="sec-head"><div><h2>Also ranked</h2>
<p>Score = money, momentum, demand, gap and fit, discounted when few sources agree. The dark bar marks each direction's strongest part.</p></div>
<a href="directions/index.html">All {len(dirs)} directions →</a></div>
<div class="panel"><ol class="rank">{''.join(rank_row(i + 2, d, '', m) for i, d in enumerate(rest))}</ol></div></section>

<section><div class="sec-head"><div><h2>Moving now</h2><p>MRR growth between our own snapshots, young apps already in the top-grossing charts, and GitHub repos gaining stars fast</p></div>
<div class="filters" data-filter-for="#sig-grid">{chips}</div></div>
<div class="sigs" id="sig-grid">{''.join(signal_row(s, '') for s in sigs) or '<p class="empty">Signals appear after two collection days.</p>'}</div></section>

<section><div class="sec-head"><div><h2>Buyers asking on Reddit</h2><p>Posts asking for a tool, an alternative or a fix, most-discussed first. Each one is a person to talk to.</p></div></div>
<div class="panel threads">{''.join(thread_row(t, True, '') for t in m['hot_threads']) or '<p class="empty">No Reddit data yet.</p>'}</div></section>

<ol id="all-dir-rows" hidden>{''.join(rank_row(i + 1, d, '', m) for i, d in enumerate(dirs))}</ol>
"""
    return page("Opportunity Radar", body, "", "today")


def directions_index(m: dict) -> str:
    dirs = m["directions"]
    groups = sorted({d["group"] for d in dirs})
    chips = ('<button class="on" data-v="all">All</button><button data-v="ENTER">Enter</button><button data-v="NARROW">Narrow</button>'
             + "".join(f'<button data-v="{E(g)}">{E(g)}</button>' for g in groups))
    order = {"ENTER": 3, "NARROW": 2, "WATCH": 1}
    rows = "".join(f"""<tr data-f="{E(d['verdict'])} {E(d['group'])}">
<td><a href="{E(d['slug'])}.html"><b>{E(d['name'])}</b></a><span class="sub">{E(d['why'])}</span></td>
<td data-s="{order[d['verdict']]}">{verdict_pill(d['verdict'])}</td>
<td class="num" data-s="{d['score']}"><b>{d['score']:.2f}</b></td>
<td class="num" data-s="{d['components']['money']}">{d['components']['money']:.2f}</td>
<td class="num" data-s="{d['components']['momentum']}">{d['components']['momentum']:.2f}</td>
<td class="num" data-s="{d['components']['demand']}">{d['components']['demand']:.2f}</td>
<td class="num" data-s="{d['components']['gap']}">{d['components']['gap']:.2f}</td>
<td class="num" data-s="{d['stats']['tm_players']}">{d['stats']['tm_players']}</td>
<td class="num" data-s="{d['stats']['tm_earners_1k']}">{d['stats']['tm_earners_1k']}</td>
<td class="num" data-s="{d['stats']['tm_top_mrr'] or 0}">{money(d['stats']['tm_top_mrr'])}</td>
<td class="num" data-s="{d['stats']['app_grossing']}">{d['stats']['app_grossing']}</td>
<td class="num" data-s="{d['stats']['reddit_posts']}">{d['stats']['reddit_posts']:g}</td></tr>""" for d in dirs)
    body = f"""<header class="mast"><div class="eyebrow"><span>{len(dirs)} directions</span><span>updated {E(m['generated'])}</span></div>
<h1>Every niche we track, ranked by evidence</h1><p class="lede">Each has its own page with the landscape, who earns, where buyers ask, and a 72-hour test.
Click a column to sort. Components run 0–1: money is log-scaled verified MRR, the rest are percentiles across directions.</p></header>
<section><div class="sec-head"><div class="filters" data-filter-for="#dir-table">{chips}</div></div>
<div class="tbl-wrap"><table data-sortable id="dir-table"><thead><tr>
<th class="sortable">Direction</th><th class="sortable">Verdict</th><th class="sortable num">Score</th><th class="sortable num">Money</th>
<th class="sortable num">Mom.</th><th class="sortable num">Demand</th><th class="sortable num">Gap</th>
<th class="sortable num">Verified</th><th class="sortable num">$1K+</th><th class="sortable num">Top MRR</th>
<th class="sortable num">Grossing apps</th><th class="sortable num">Asks / wk</th></tr></thead><tbody>{rows}</tbody></table></div></section>"""
    return page("Directions · Opportunity Radar", body, "../", "directions")


def direction_page(d: dict, m: dict) -> str:
    st = d["stats"]
    base = "../"
    sigs = [s for s in m["signals"] if s["direction"] == d["slug"]]
    tiles = "".join(f'<div class="tile"><div class="v">{v}</div><div class="k">{k}</div></div>' for v, k in [
        (st["tm_players"], "verified products, last 60 days"),
        (st["tm_earners_1k"], "at $1K+ MRR"),
        (money(st["tm_top_mrr"]), "top verified MRR"),
        (st["tm_growers"], "growing 30%+ a month"),
        (st["app_grossing"], "in US top-grossing charts"),
        (st["app_new"], "charting apps under 12 months old"),
        (f'{st["reddit_posts"]:g}', "buyer asks on Reddit / week"),
        (st["gh_trending"], "GitHub repos trending today"),
    ])
    tm_rows = "".join(
        f"""<tr><td><a href="{E(x['url'])}" target="_blank" rel="noopener">{E(x['name'])}</a><span class="sub">{E(x['desc'][:90] + ('…' if len(x['desc']) > 90 else ''))}</span></td>
<td class="num" data-s="{x['mrr'] or 0}">{money(x['mrr'])}</td>
<td class="num" data-s="{x['growth'] or 0}">{(f"{x['growth']:+.0f}%" if x['growth'] is not None else "–")}</td>
<td class="num">{E(x['founded'][:7] or '–')}</td><td class="num">{money(x['asking']) if x['on_sale'] else '–'}</td></tr>"""
        for x in d["trustmrr"][:25])
    ap_rows = "".join(
        f"""<tr><td><a href="{E(x['url'])}" target="_blank" rel="noopener">{E(x['name'])}</a><span class="sub">{E(x['seller'] or '')}</span></td>
<td class="num" data-s="{x['grossing'] or 999}">{('#' + str(int(x['grossing']))) if x['grossing'] else '–'}</td>
<td class="num" data-s="{x['free'] or 999}">{('#' + str(int(x['free']))) if x['free'] else '–'}</td>
<td class="num">{E(x['release'][:7] or '–')}</td></tr>""" for x in d["apps"][:20])
    cad = d["cadence"]
    if cad:
        mx = max(v for _, v in cad) or 1
        bars = "".join('<div title="%s: %d new" style="height:%d%%"></div>' % (k, v, max(3, int(v / mx * 100))) for k, v in cad)
        labels = "".join("<span>%s</span>" % datetime.strptime(k, "%Y-%m").strftime("%b")[:1] for k, _ in cad)
        cad_html = (f'<div class="cad">{bars}</div><div class="cad-l">{labels}</div>'
                    f'<p class="tiny faint" style="margin-top:8px">New products per launch month, last 12 months '
                    f'({cad[0][0]} to {cad[-1][0]}). TrustMRR founded date plus App Store release date.</p>')
    else:
        cad_html = '<p class="empty">No launch dates in this direction yet.</p>'
    kit = d["kit"]
    handles = "".join(f'<a class="chip" href="{E(h["url"])}" target="_blank" rel="noopener" title="{E(h["title"])}">u/{E(h["handle"])}</a>' for h in kit["handles"])
    pains = "".join(f"<blockquote>{E(p)}</blockquote>" for p in kit["pains"][:3])
    pkgs = "".join(f'<tr><td><a href="{base}{E(p["url"])}">{E(p["title"])}</a><span class="sub">{E(p["excerpt"])}</span></td><td>{E(p["tier"])}</td><td class="num">{E(p["date"])}</td></tr>' for p in d["packages"])
    first_comp = (kit["competitors"] or ["the current option"])[0]
    body = f"""
<header class="dhead"><div><div class="crumbs"><a href="index.html">Directions</a> / {E(d['group'])}</div>
<h1>{E(d['name'])}</h1><p class="why">{E(d['why'])}.</p>
<div class="floor">{verdict_pill(d['verdict'])}<span>{E(VERDICT_TXT[d['verdict']])}
{'' if d['floor'] else ' Evidence floor not met: no verified $500+ MRR and fewer than 2 sources.'}</span></div></div>
<div class="panel pad"><div class="scorebig"><b>{d['score']:.2f}</b><span class="tiny muted">score · confidence {d['confidence']:.1f} ({plural(d['sources'], 'source')})</span></div>
{meter(d)}<button class="star" data-watch="{E(d['slug'])}">Watch this direction</button></div></header>

<section><div class="sec-head"><h2>Landscape</h2></div><div class="tiles">{tiles}</div></section>

<section class="grid g2">
<div style="min-width:0"><div class="sec-head"><div><h2>Who's earning</h2><p>{label_badge('verified')} MRR from TrustMRR, read from the payment provider</p></div></div>
{('<div class="tbl-wrap"><table data-sortable><thead><tr><th>Product</th><th class="sortable num">MRR</th><th class="sortable num">30d</th><th class="num">Founded</th><th class="num">Asking</th></tr></thead><tbody>' + tm_rows + '</tbody></table></div>') if tm_rows else '<p class="empty">No verified products here yet.</p>'}</div>
<div style="min-width:0"><div class="sec-head"><div><h2>In the App Store charts</h2><p>{label_badge('verified')} US rank in its genre today</p></div></div>
{('<div class="tbl-wrap"><table data-sortable><thead><tr><th>App</th><th class="sortable num">Grossing</th><th class="sortable num">Free</th><th class="num">Released</th></tr></thead><tbody>' + ap_rows + '</tbody></table></div>') if ap_rows else '<p class="empty">No charting apps matched this direction.</p>'}</div>
</section>

<section class="grid g2">
<div style="min-width:0"><div class="sec-head"><h2>Entry cadence</h2></div><div class="panel pad">{cad_html}</div></div>
<div style="min-width:0"><div class="sec-head"><h2>Moving in this direction</h2></div>
<div class="sigs" style="grid-template-columns:1fr">{''.join(signal_row(s, base) for s in sigs[:5]) or '<p class="empty">Nothing moved here in the latest snapshots.</p>'}</div></div>
</section>

<section><div class="sec-head"><div><h2>Buyers asking on Reddit</h2>
<p>From {", ".join("r/" + E(s) for s in d['subreddits'])}: posts asking for a tool, an alternative or a fix. Use them as wedge evidence and as your first interviews.</p></div></div>
<div class="panel threads">{''.join(thread_row(t, False, base) for t in d['threads'][:12]) or '<p class="empty">No buyer-intent posts in the last two weeks.</p>'}</div></section>

<section class="kit" id="kit"><div class="sec-head"><div><h2>Your 72-hour validation kit</h2><p>Built from this page's evidence. Run it before writing a line of product code.</p></div></div>
<div class="panel pad"><ol>
<li><span>Hour 0</span><div><b>Pick one pain.</b> The most-discussed asks right now:{pains or ' none found yet; use the threads above as they arrive.'}</div></li>
<li><span>Hour 1</span><div><b>Write the wedge in one line:</b> For <span class="slot">one buyer</span> who <span class="slot">has the pain above</span>, unlike <span class="slot">{E(first_comp)}</span>, we <span class="slot">do one thing</span></div></li>
<li><span>Hour 4</span><div><b>Ship a landing page</b> with that line, one mock-up and an email or pre-order button.</div></li>
<li><span>Day 1</span><div><b>Show up where buyers are:</b> {", ".join(f'<a href="https://www.reddit.com/{E(c)}/" target="_blank" rel="noopener">{E(c)}</a>' for c in kit['channels'])}. Answer threads with help first; link only when asked.</div></li>
<li><span>Day 2</span><div>{('<b>Talk to the ' + str(len(kit['handles'])) + ' people who already asked.</b><div class="handles">' + handles + '</div>') if handles else '<b>Find 10 people with the problem</b> in those subreddits and ask how they handle it today.'}</div></li>
<li><span>Day 3</span><div><b>Decide.</b> <span class="pass">Pass:</span> {E(kit['pass_bar'])}. <span class="kill">Kill:</span> {E(kit['kill_bar'])}.</div></li>
</ol></div></section>

{('<section><div class="sec-head"><div><h2>Build packages</h2><p>Full PRD, 14-day build plan and 30-day marketing from earlier weekly loop runs (archive)</p></div></div><div class="tbl-wrap"><table><thead><tr><th>Package</th><th>Tier</th><th class="num">Date</th></tr></thead><tbody>' + pkgs + '</tbody></table></div></section>') if pkgs else ''}
"""
    return page(f"{d['name']} · Opportunity Radar", body, base, "directions", d["why"])


def check_page() -> str:
    body = """<header class="mast"><div class="eyebrow"><span>Idea check</span><span>runs in your browser</span></div>
<h1>Is anyone paying for this, and is anyone asking?</h1>
<p class="lede">Describe what you want to build and for whom. We match it against verified products and our directions, then read Reddit live for people asking for it.</p></header>
<section><form id="check-form" data-src="data.json" class="panel pad">
<label for="idea" class="eyebrow" style="display:block;margin-bottom:8px">Your idea in one sentence</label>
<textarea id="idea" name="idea" placeholder="e.g. invoice reminders for freelance designers that chase late payments by email"></textarea>
<div class="row" style="margin-top:12px;justify-content:space-between"><button class="btn" type="submit" disabled>Check the evidence</button>
<div class="row"><span class="tiny faint">Try</span>
<button type="button" class="chip" data-example="calorie tracker that logs meals from a photo for people on GLP-1">GLP-1 meal tracker</button>
<button type="button" class="chip" data-example="quote and invoice app for roofing contractors that turns a site photo into an estimate">Roofing estimates</button>
<button type="button" class="chip" data-example="tool that finds reddit threads where people ask for a product like mine">Reddit lead finder</button></div></div></form></section>
<div id="check-out"></div>"""
    return page("Check an idea · Opportunity Radar", body, "", "check")


def method_page(m: dict) -> str:
    body = f"""<header class="mast"><div class="eyebrow"><span>Method</span></div><h1>How the radar decides, and how sure it is</h1>
<p class="lede">Every figure says where it came from and whether it is verified, estimated or inferred. Paid data is deliberately left out until the free sources prove useful.</p></header>
<div class="prose">
<h2>Sources (tier 1, free)</h2>
<div class="tbl-wrap"><table><thead><tr><th>Source</th><th>What we take</th><th>Label</th></tr></thead><tbody>
<tr><td>TrustMRR public API</td><td>MRR, last-30 revenue, subscriptions and 30-day growth for newly listed and best-deal startups. Our own snapshots give before and after.</td><td>{label_badge('verified')}</td></tr>
<tr><td>Apple RSS charts + iTunes Lookup</td><td>US top-grossing and top-free rank per genre, rating counts, release dates</td><td>{label_badge('verified')} rank<br>{label_badge('estimated')} rating momentum</td></tr>
<tr><td>GitHub Trending</td><td>Stars today and total stars</td><td>{label_badge('verified')}</td></tr>
<tr><td>Reddit via Arctic Shift</td><td>Newest posts of each direction's subreddits (up to 14 days). A post counts as a buyer ask when it asks for something (“looking for”, “alternative to”, “would pay”) and names a product (app, tool, software, service). Reported as posts per week.</td><td>{label_badge('verified')} counts</td></tr>
<tr><td>TinyFish search</td><td>Possible triggers for the day's top movers</td><td>{label_badge('inferred')}</td></tr>
</tbody></table></div>
<p class="small muted">Tier 2 (keyword volume, X API, app revenue estimates, web traffic) needs paid APIs and is deferred.</p>
<h2>Score v2</h2>
<p class="mono">score = (0.30 money + 0.25 momentum + 0.20 demand + 0.15 gap + 0.10 fit) × confidence</p>
<ul>
<li><b>Money</b>: 70% log-scaled median MRR of the top 5 verified products ($300 → 0, $30K → 1), 30% percentile of top-grossing chart apps.</li>
<li><b>Momentum</b>: percentile of products growing 30%+, moving products, young charting apps and trending repos.</li>
<li><b>Demand</b>: percentile of buyer asks on Reddit per week and the replies they draw.</li>
<li><b>Gap</b>: half “fewer players than other directions”, half “more asks per player”.</li>
<li><b>Fit</b>: a fixed prior for a 14-day, $300 solo build.</li>
<li><b>Confidence</b>: 1 source 0.5, 2 sources 0.8, 3 or more 1.0.</li>
</ul>
<p><b>ENTER</b> needs all four: score 0.60 or more, at least 2 verified products at $1K+ MRR (people already pay), demand 0.5 or more (people are asking now) and gap 0.3 or more (room left).
<b>NARROW</b> is score 0.45 or more with the evidence floor met: a verified product at $500+ MRR, or activity in 2+ sources. Everything else is <b>WATCH</b>. A day with no ENTER is a valid result.</p>
<h2>What counts as moving</h2>
<ul><li>TrustMRR: MRR up at least 1.3× and $100 between our snapshots within 45 days, or TrustMRR's own 30-day growth of 40–2000%.</li>
<li>App Store: a climb of 15+ places in 8 days, or an indie app under 6 months old already in the top 40 grossing of its genre. Launches by large publishers are skipped.</li>
<li>App Store ratings: daily new ratings at 3× or more their 7-day average.</li>
<li>GitHub: 150+ stars in a day.</li></ul>
<p class="small muted">History so far: {m['snapshot_days']} days of TrustMRR snapshots. Products tracked: {", ".join(f"{SRC_NAMES.get(k, k)} {v:,}" for k, v in m['counts'].items())}.</p>
</div>"""
    return page("Method · Opportunity Radar", body, "", "method")


def data_json(m: dict) -> dict:
    prods = []
    for d in m["directions"]:
        for x in d["trustmrr"]:
            prods.append({"name": x["name"], "desc": x["desc"][:200], "mrr": round(x["mrr"] or 0), "url": x["url"],
                          "source": "trustmrr", "direction": d["slug"]})
        for x in d["apps"]:
            prods.append({"name": x["name"], "desc": x["category"], "mrr": None, "rank": x["grossing"], "url": x["url"],
                          "source": "appstore", "direction": d["slug"]})
    return {"generated": m["generated"], "products": prods, "directions": [
        dict({k: d[k] for k in ("slug", "name", "group", "keywords", "subreddits", "queries", "score", "verdict", "why", "components")},
             stats=d["stats"]) for d in m["directions"]]}


def write(m: dict) -> None:
    (OUT / "directions").mkdir(parents=True, exist_ok=True)
    (OUT / "history").mkdir(parents=True, exist_ok=True)
    day = m["generated"][:10]
    m["prev"] = load_prev(day)
    b = briefing(m)
    snap = {k: b[k] for k in ("day", "headline", "lede", "changes", "enter", "n_enter", "n_narrow")}
    snap["ranks"] = {d["slug"]: [i + 1, d["verdict"], d["score"]] for i, d in enumerate(m["directions"])}
    (OUT / "history" / f"{day}.json").write_text(json.dumps(snap, ensure_ascii=False, indent=0), encoding="utf-8")
    history = [json.loads(f.read_text()) for f in sorted((OUT / "history").glob("*.json"))]
    (OUT / "feed.xml").write_text(feed_xml(history), encoding="utf-8")
    for f in ("radar.css", "radar.js"):
        shutil.copy(STATIC / f, OUT / f)
    (OUT / "index.html").write_text(index_page(m), encoding="utf-8")
    (OUT / "check.html").write_text(check_page(), encoding="utf-8")
    (OUT / "method.html").write_text(method_page(m), encoding="utf-8")
    (OUT / "directions" / "index.html").write_text(directions_index(m), encoding="utf-8")
    for d in m["directions"]:
        (OUT / "directions" / f"{d['slug']}.html").write_text(direction_page(d, m), encoding="utf-8")
    (OUT / "data.json").write_text(json.dumps(data_json(m), ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"[radar] site: {len(m['directions'])} directions, {len(m['signals'])} signals → {OUT}")
