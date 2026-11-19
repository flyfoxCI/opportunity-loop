---
title: "Stringers Plays · How a Play Is Built"
author: "Opportunity Loop Research"
description: "A close reading of all 25 Stringers playbook pages: what a play is, how each one finds a direction, a growth move or a way to charge, how cases are checked, and what our playbook copies."
---

# Stringers Plays: How a Play Is Built

> [!NOTE]
> **Read on:** 2026-11-19 · **Scope:** all 25 pages under `stringers.io/plays/` (p01–p25), with 124 case cards, plus
> the linked investigation pages. **Purpose:** rebuild our playbook (`radar/playbook.py`, `docs/v3/plays/`) to work the same way.

## 0. Summary

A Stringers play is not a trend or a category. It is **one concrete action a solo builder can take this week**, backed by
products that took it recently, and checked case by case. Five things make it work:

1. **The title is an instruction with numbers in it.** "Add an annual plan at *pay 10 months, use 12*, default the pricing
   toggle to it." Not "annual plans help retention".
2. **One line of mechanism**: why the action works, sometimes with its own caveat ("the thread gathers people who want
   apps, *but only 4 of 53 replies passed 10k views*").
3. **Exactly five steps**, each an instruction followed by an evidence paragraph that cites several cases by name, with
   verbatim copy, prices, dates and numbers, and often a counter-example inline.
4. **Every case is graded for causality**: hard / medium / weak. 27 hard, 77 medium, 20 weak across 124 cases, so most
   cases are openly labelled "probably".
5. **The page argues against itself**: a "tried it, didn't work" section, a "who it suits / when it fails" section, and a
   closing note that says what the first draft got wrong after checking.

## 1. The catalogue

| Category | Plays | What the plays answer |
|---|---|---|
| **Finding a direction** 找方向 | 4 | *Where* to build: demand that someone else creates for you |
| **Growth** 增长 | 17 | *How users arrive*: one repeatable distribution move |
| **Monetization** 商业化 | 4 | *Where and how to charge*: the price structure, not the price level |

Growth dominates because breakouts are, almost by definition, distribution events. Direction and monetization plays are
rarer and more valuable: they come out of reading *why* a niche opened and *how* the money was taken.

### Direction plays: someone else makes the demand

| # | Play | Where the demand comes from |
|---|---|---|
| p14 | Pick an exam or release with an officially fixed date; have the tool, search pages and a time-limited pass ready; let people search their way to you on the day | An official calendar |
| p05 | Ship a replacement with one-click migration before a big company's shutdown or paywall deadline | A shutdown notice |
| p09 | Take money in a chat app, paid community or crowdfunding first; build the app after | People already paying in the crudest form |
| p20 | In the first two weeks of an open-source hit, build its GUI shell, resource directory or counter-tool, and be the most complete one | The hit's own audience |

The common rule: **don't invent demand; stand where a date, a deadline or someone else's launch pushes people.** Every
direction play includes a selection test in step 1 ("only notices with a hard date that leave old users no path", "only if
each delivery has a crowd waiting for it") and an honest ceiling ("one country, one exam: the best month was $2,276").

### Monetization plays: lock the moment of value

| # | Play | The lock |
|---|---|---|
| p07 | Annual plan at "pay 10, use 12", default the toggle to annual | Commitment up front |
| p16 | Free to view everything; charge only at export, copy, or getting the contact | The moment the user takes the result away |
| p18 | Next to the self-serve tier, a done-for-you tier at 4×+ price, limited seats, call before invoice | People who want the outcome, not the tool |
| p11 | A vertical launch site: 5 free slots a day for a backlink badge, sell $12–29 queue skips | Waiting time |

The common rule: **charge where the user has already seen their own result**, and price to the shape of the need (a
24-hour pass for a one-day event, lifetime for one-off jobs).

### Growth plays: one repeatable move, measured

The 17 growth plays fall into four families:

| Family | Plays |
|---|---|
| **Re-say it**: same product, new hook | p08 re-post with a human line, a number, a new image or a hot topic (16 products) · p03 fixed hook format, vary one variable per short video · p25 "which ordinary machine + model size + tokens/s" title |
| **Borrow attention** | p19 post within 24h of a big model/feature launch, with output · p22 reply "this is the open-source version" under a viral demo · p06 quote the "what to install on a new Mac" thread · p01 name the incumbent, put the side-by-side numbers first |
| **Let others carry it** | p17 make it a one-line-install agent skill so roundups list it · p13 be an early vertical plugin on a newly opened platform · p12 recruit suppliers who already have buyers · p21 dozens of ordinary creators shoot the same proven script · p24 Reel + "comment a word to get the link" |
| **Be found / be trusted** | p02 one signed answer page per competitor name and per user question · p04 localize the store page, price and ads for one small country at a time · p10 post each release back to the same subreddit · p15 ask for ratings right after a successful payment · p23 turn the product's own daily output into short videos |

Growth plays always specify **the measurement and the patience**: "post at least 30 before concluding", "watch MRR, not
the daily number", "log views per star; when the ratio drops, change the line".

## 2. Anatomy of one play page

Every page has the same order. Example: p14 (fixed-date exams and releases).

| Block | What it holds | p14 example |
|---|---|---|
| Category tag | One of three | Finding a direction |
| **Recipe** (H1) | Imperative, concrete, no product names | Pick an exam or release with an official date… |
| **Mechanism** | One sentence | The deadline is set by someone else; on the day people search by themselves and only want to pay for this stretch |
| Proof line | Case icons · N products verified · last verified date | 5 products · Nov 10 |
| **How to do it** (5 steps) | Instruction + evidence paragraph + screenshot | 1 choose the date · 2 put the date in the first sentence and first action · 3 prepare search pages and payment while waiting · 4 price to the length of the stretch · 5 on the day: stay up, keep payments working |
| **Who verified it** | One card per product | MisiPNS, VTC Facile, Scalperz, Atanalım, … |
| **Tried it, didn't work** | Named products and what went wrong | CCN: same release day, monthly subscription and a hidden paywall, 45 of 60 reviews one-star |
| **Who it suits / when it fails** | Who · prerequisites · numbered risks | Suits people who took the exam themselves; fails when exams are local or bookable any day; risks: stale question banks, trademark |
| **Worth saying more** | Synthesis | "Three kinds of dates, three businesses"; what matters most; what the draft got wrong |

### The steps follow a fixed arc

Across the 25 pages the five steps almost always run in this order:

1. **Select**: when this play applies and how to pick the target (and when it doesn't: "if not, none of the next steps work").
2. **Shape the offer**: what to put in the first sentence, first screen or first action, quoted from a case.
3. **Prepare to catch the traffic**: link in the post, payment working, docs ready, issues closed same day.
4. **Execute the move**: the copy, price, cadence or channel, with numbers.
5. **Measure and persist**: which number to watch, how long to wait, when to change.

A step that no case shows directly is marked as such: *"this step is inferred from the cases' bad reviews, not
copied from a case."*

### A case card

| Field | Content | Example (Logopack, p16) |
|---|---|---|
| Name + one line | What it is + who built it | Exports a finished SVG logo into the full client package; built by one brand designer |
| Metric flag | The tracked metric, before → after | Daily revenue $37 → $218 |
| **How** | What exactly they did: verbatim copy (original + translation), prices, dates, channels; ad-library check | Week one: export free, 1 paid of 79 sign-ups; A/B: export-free 812 visitors 0 paid vs preview-only 896 visitors 6 paid |
| **Result** | Dated numbers, what the number is *not*, alternative explanations | Day 21: 51 paying, $565 total; "the $218 day is more likely the price change (inferred), not this play" |
| **Causality** | Hard / medium / weak | Hard |
| Screenshot + caption | The evidence itself, dated | The founder's A/B dashboard |

The **result** is where the honesty lives: "the 65k installs in the draft are cumulative, not from this jump",
"the competitor rose the same day: the whole lane rose", "the ratings came from migrating old users, not new ones".

## 3. How a play gets made (the method behind the pages)

The pages show the process:

1. **Investigate each breakout** and write down the move it used: what it did, when, what happened.
2. **Group moves** shared by several products into a draft play with steps.
3. **Check each case against its evidence**: re-date, re-measure, grade causality, and drop what doesn't hold.
4. **Look for counter-examples**: products that made the same move without a lift, or broke one step (CCN hid its paywall;
   budgenie locked before showing anything; Plotta tightened its free tier late).
5. **Rewrite the play from what survived.** The closing note often says so: *"the draft merged two things, gathering
   people and taking money; after checking only the second held"*, *"I found no case that proves the 'post content that
   week' step"*.

A product can appear in several plays (Logopack, NotchOwl, Scalperz), and one product can be both a case and a
counter-example (VTC Facile "did it most by the book and made the least money").

## 4. How the analysis reads one app, by lens

Each investigation feeds all three categories. The same product is read three ways:

| Lens | Question | What is quoted as evidence |
|---|---|---|
| **Direction** | Why did a gap open here, now? Who made the demand? | Shutdown notices, official calendars, competitor reviews ("there's no trial"), a leader that stopped updating |
| **Growth** | Where did the users come from, exactly? | The post (link, likes, views), the ad libraries (Meta / Google / TikTok: found or not), store featuring, chart moves of rivals the same day |
| **Monetization** | How is the money taken, at which moment, at what price shape? | Pricing page copy, plan list, A/B screenshots, payment-verified revenue, refund and one-star reviews about paywalls |

Then **"if it were you"**: verdict, who it suits, how to start, the wedge it left open, a deadline, and what would prove
this wrong.

## 5. What we changed in Opportunity Loop

| Stringers practice | Our implementation |
|---|---|
| Three categories | `direction`, `growth`, `monetization` in `radar/investigate.py` |
| Each investigation read through three lenses | The agent returns up to three `plays` per brief, one per lens, each with move / did / result / causality / evidence URLs |
| Causality hard / medium / weak | `causality: hard | medium | weak` on every case; "N with a clear cause" counts hard + medium |
| Draft → check → rewrite | `radar/playbook.py` runs two passes: *draft* groups moves into plays; *verify* re-reads each play against its cases' full briefs, regrades causality, drops unsupported cases and steps, marks inferred steps, and writes what changed |
| Five steps with evidence | `steps: [{do, evidence, inferred}]`, evidence must name cases and their numbers |
| Counter-examples | From the agent (same move, no lift) **and** from our track record (breakouts that faded by D+7) |
| Who it suits / risks / worth saying more | `suits`, `prerequisites`, `risks`, `notes` sections on each play page |
| Proof line | Case icons · N products · N with a clear cause · last verified |

What we can't copy yet: Stringers' screenshots and verbatim social posts come from manual or browser-agent research. Our
evidence is what TinyFish and the collectors gather, so our cases will quote fewer posts until the trace step gets deeper.
