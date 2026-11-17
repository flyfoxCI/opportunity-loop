---
layout: post
title: "Chart Scanner AI — Explainable Technical-Chart Extraction"
date: 2026-11-17T10:32:16+00:00
week: "2026-11-17_103216"
week_date: "2026-11-17T10:32:16+00:00"
slug: "chart-scanner-ai"
permalink: /directions/chart-scanner-ai.html
tags:
  - "AI"
  - "photo"
  - "language"
  - "mobile"
excerpt: "Upload a chart image and extract structured, explainable technical-analysis data with evidence."
---

**Tier:** GO  
**Demand:** 4/5  
**Competition:** 3/5  
**Target:** $10,000 MRR  
**MVP:** 14 days, solo  
**Marketing budget:** ≤ $300 for 30 days  

## 1. Why this direction

### TrustMRR evidence

- Chart Scanner AI reports approximately **$31.50 MRR**, **$37.64 in last-30-day revenue**, and **120 subscribers**.
- Last-30 revenue exceeding MRR is a positive short-term signal, but may reflect annual-plan timing, refunds, or reporting artifacts; it should not be treated as proof of net retention.
- The product’s apparent workflow—scanning a chart and producing a structured analysis—addresses a frequent, understandable task.
- The 120-subscriber base indicates more top-of-funnel interest than the low MRR alone suggests.
- The opportunity is strongest for traders and analysts who currently save screenshots and manually record chart data.

### X/web evidence

- No identified X handle was supplied for this listing.
- The supplied search run returned 12-result counts, but its stdout contained TinyFish CLI help rather than the actual result bodies. No social quote or engagement metric is therefore claimed.
- Demand is supported primarily by TrustMRR subscriber/revenue evidence and by the ubiquity of chart screenshots in trading communities.
- This direction should be marketed to end users, not treated as a trading signal service.

### Thesis

Create a **chart-image-to-structured-data and plain-language explanation** tool. A user uploads a static chart image, selects the chart type and intended question, and receives:

- extracted price levels, dates, labels, and trend structure where legible;
- a plain-English explanation;
- visible uncertainty and image-quality warnings;
- a CSV/JSON export;
- optional follow-up questions.

The differentiator should be **explainability and structured export**, not proprietary trade recommendations.

### Initial ICP

- Technical-analysis learners who screenshot charts and manually maintain levels.
- Independent chart analysts and trading educators who need a repeatable extraction workflow.
- Start with one market type—daily stock candlesticks—because the chart grammar is well defined and testable.
- Exclude leveraged CFDs, signals, portfolio execution, and personalized financial advice from the MVP.

### Validation questions

1. Does the user need extraction, explanation, or a trade signal? The product must optimize for the first two.
2. How often does the user work from screenshots rather than exchange data?
3. Which fields cause the most manual work?
4. Are users willing to pay for OCR plus structured export?
5. What accuracy threshold makes the output useful without pretending to be infallible?

## 2. Competitor table

### L1 — direct alternatives

| competitor | likely offer/pricing | strength | weakness / opening | evidence confidence |
|---|---|---|---|---|
| Chart Scanner AI | Chart scan/analysis product with approximately $31 MRR | Existing paid validation and task focus | Opportunity for stronger evidence display, vertical templates, and export | High for revenue; medium for exact workflow |
| TradingView Chart Image Recognition | Extracts structured data from chart screenshots when available in supported ecosystems | Deep integration with a major charting platform | Not a standalone cross-chart archive or explanation-first workflow | Medium |
| ChartReader / chart-to-table utilities | Converts chart images into spreadsheet or structured values | Direct task alignment | Often narrow, technical, or inconsistent across visual styles | Medium |
| Vision/OCR SaaS tools | General image transcription and extraction | Flexible and inexpensive | Requires prompt construction and produces inconsistent financial fields | Medium |
| Broker chart tools | Readable charts and drawing tools | Trusted market-data integration | Do not reliably extract a previously captured image into structured records | Medium |

### L2 — adjacent substitutes

| substitute | why buyers use it | opportunity |
|---|---|---|
| Spreadsheet/manual notes | Record levels and observations | Slow, repetitive, and prone to formatting errors |
| General AI vision chat | Ask questions about a chart image | Variable prompts, hallucination risk, poor exports |
| Screenshot album folders | Archive chart evidence | No extraction or explanation |
| Human analyst | Validate ambiguous charts | Expensive and slow |

### L3 — low-end alternatives

| alternative | weakness |
|---|---|
| Free OCR | Text extraction without chart-aware structure |
| Phone gallery + notes | Manual and hard to search |
| Hand-drawn support/resistance maps | No scalable processing |

### Competition conclusion

**Score: 3/5.** Several products can either extract charts or explain images, but the combined workflow is not trivial. The product must avoid generic “ask an AI about this image” positioning and demonstrate measurable extraction accuracy on a small chart corpus.

## 3. PRD MVP

### Target outcome

A user can upload a supported chart screenshot and receive a structured chart record plus a cautious explanation in under a minute.

### P0 — required for launch

- Supported chart types:
  - daily stock candlestick;
  - line chart;
  - basic bar chart.
- Upload via drag-and-drop and mobile camera.
- Image preprocessing:
  - resize;
  - deskew;
  - contrast normalization;
  - axis and plot-region detection.
- Chart-type auto-detection with user override.
- OCR for:
  - ticker or title;
  - date labels;
  - price labels;
  - axis values;
  - visible annotations.
- Structured extraction:
  - open/high/low/close or plotted values;
  - visible support/resistance annotations;
  - detected trend and chart pattern names;
  - source image dimensions and confidence.
- Evidence overlay showing where each field came from.
- Plain-language summary with uncertainty warnings.
- CSV and JSON export.
- Usage limits and Stripe billing.
- Disclaimer: educational extraction only, not financial advice.
- Privacy controls: auto-delete uploads after a configurable period.
- Analytics for upload, processing, report viewed, export, and upgrade.

### P1 — after validation

- Broker/platform adapters for live chart URLs.
- Template recognition for common chart styles.
- Watchlist with saved extracted levels.
- User correction and re-run loop.
- Side-by-side before/after extraction.
- Daily/weekly chart journal.

### P2 — later expansion

- More asset classes and chart styles.
- Team folders and shared research.
- Annotation export back into supported platforms.
- Plugin for education platforms.

### Non-goals

- No buy/sell/sell signals.
- No guaranteed forecasts or price targets.
- No brokerage connection, order routing, or portfolio management in the MVP.
- No claims that extracted values are exchange-authoritative.
- No support for every chart annotation style on day one.
- No autonomous trading automation.

### MVP user story

> As a technical trader or learner, I can upload a chart screenshot and get a structured, inspectable record with uncertainty so that I can save research time without mistaking OCR for authoritative market data.

### Technical approach

- Web app with server-side image processing.
- OCR: a general vision model for initial chart parsing, plus deterministic post-processing.
- Geometry: OpenCV-style preprocessing and line/candle detection.
- Data model:
  - chart;
  - image asset;
  - extraction result;
  - field-level evidence;
  - user correction;
  - export.
- Privacy: encrypted object storage, signed URLs, 24-hour default retention.
- Reliability: every extracted number carries a confidence score and evidence crop.
- Billing: Stripe metered plans with daily usage caps.

### Pricing hypothesis

- **Free:** 3 charts/month, basic extraction.
- **Trader:** $19/month, 60 charts/month, CSV/JSON export and saved records.
- **Analyst:** $49/month, 250 charts/month, templates, corrections, and journal.
- **Education/team:** $99/month, 1,000 charts/month, shared folders and branded exports.

The pricing test should distinguish willingness to pay for extraction from willingness to pay for signals.

## 4. 14-day day-by-day build plan

| Day | objective | deliverables | acceptance test |
|---:|---|---|---|
| 1 | Define scope | Select daily stock charts; create 50-image labeled test corpus; define supported fields and error policy | Corpus covers labels, axes, candles, overlays, and poor quality |
| 2 | Validate task | Interview 10 traders/analysts; show static mock output | At least 5 use screenshots repeatedly and 3 identify a painful manual step |
| 3 | Extraction spike | Test OCR and vision models on the corpus | Establish per-field accuracy and cost; reject poor approaches |
| 4 | Preprocessing | Implement resize, crop, deskew, contrast, plot detection | 90% of corpus images produce a usable plot region |
| 5 | OCR pipeline | Extract titles, dates, prices, and labels | 95% readable-axis transcription on labeled test cases |
| 6 | Geometry | Detect candles, lines, bars, and visible levels | At least 80% of supported chart types parse without manual intervention |
| 7 | Evidence model | Store field values, confidence, and evidence crops | Every value can be inspected against the source image |
| 8 | Report UX | Upload flow, result cards, overlay, warnings, copy/export | User can understand a field and its uncertainty in 60 seconds |
| 9 | Account and persistence | Authentication, chart history, saved records, usage limits | User can retrieve and delete prior uploads |
| 10 | Billing | Stripe plans, webhooks, metering, quota errors | Payment state and quotas are reliable |
| 11 | Safety and privacy | Disclaimers, auto-deletion, retention controls, prompt-injection resistance | Untrusted image text cannot alter system behavior |
| 12 | Pilot | Invite 10 target users; manually review outputs | At least 5 exports and 2 paid conversions |
| 13 | Accuracy iteration | Fix top field failures and improve warning copy | Top three fields exceed agreed test thresholds |
| 14 | Release | Deploy, publish sample gallery, record demo, start outreach | 99% job completion, no P0 defects, paid flow tested |

### Solo-build controls

- Support one primary chart type first.
- Use a fixed evaluation corpus to prevent regression.
- Keep explanations deterministic from structured fields.
- Do not build brokerage integrations in the MVP.
- Limit concurrency and cap image dimensions.

## 5. 30-day marketing calendar

### Budget

| channel | 30-day spend |
|---|---:|
| Small creator/newsletter sponsorships | $120 |
| Search-intent content and one boosted post | $60 |
| Paid chart corpus/test tooling | $40 |
| Interview/demo incentives | $80 |
| **Total** | **$300** |

### Calendar

| day | activity | organic action | paid action | KPI |
|---:|---|---|---:|---|
| 1 | Launch | Publish homepage and interactive sample | None | 150 qualified visits |
| 2 | Founder post | “I tested 50 chart screenshots” on LinkedIn/X | None | 10 qualified comments |
| 3 | Accuracy page | Publish field-by-field benchmark methodology | None | 30 sample uploads |
| 4 | Outreach | Contact 15 technical analysts | None | 5 interviews |
| 5 | Demo video | Publish 60-second extraction demo | None | 20% upload rate |
| 6 | Free tool | Offer 10 free chart extractions | None | 10 uploads |
| 7 | Review | Fix largest OCR/geometry failure | None | 70% successful first parse |
| 8 | Content | Publish “chart screenshot to CSV” guide | None | 50 organic visits |
| 9 | Creator outreach | Send free credits to 10 trading educators | None | 3 creator trials |
| 10 | Newsletter pitch | Pitch chart-productivity newsletters | None | 1 featured mention |
| 11 | Founder analysis | Post a transparent extraction-error review | None | 3 paid conversions |
| 12 | User calls | Interview trial users | None | 5 completed calls |
| 13 | Product iteration | Add user correction and re-run flow | None | 25% correction completion |
| 14 | Pricing test | Show $19/$39/$59 plans | None | 8% checkout start |
| 15 | SEO page | Publish chart OCR/export comparison | None | 20 search visits |
| 16 | Paid creator test | Promote demo to chart-analysis audience | $60 | CAC below $25 |
| 17 | Live session | Run public chart-extraction clinic | None | 10 registrants |
| 18 | Template launch | Add support/resistance annotation template | None | 20 template uses |
| 19 | Review | Segment conversion by source and chart type | None | Identify best ICP |
| 20 | Partnership | Reach out to trading educators | $20 | 2 pilot discussions |
| 21 | Referral | Ask users to refer a chart-analysis peer | $20 | 4 referrals |
| 22 | Content | Publish “5 chart OCR mistakes” | None | 15 shares |
| 23 | Founder post | Explain trust and uncertainty design | None | 8 sales conversations |
| 24 | Paid retarget | Retarget sample visitors | $20 | 3 paid trials |
| 25 | Retention | Review repeat usage among first users | None | 40% second chart within 14 days |
| 26 | Upgrade test | Trigger context upgrade after fifth free use | None | 3 plan conversions |
| 27 | Customer proof | Publish anonymized time-saved result | None | 5 checkout starts |
| 28 | Channel review | Pause low-quality sources | None | CAC below $30 |
| 29 | Automation | Add upload-summary email and weekly usage digest | None | 35% open rate |
| 30 | Monthly review | Reconcile paid users, MRR, churn, and inference cost | $0 | 15+ paid accounts or explicit pivot |

### Organic-first content pillars

- Public benchmark results.
- Chart OCR error analysis.
- Time-saving workflows for analysts.
- Screenshots transformed into CSV.
- Uncertainty and trust design.
- Comparisons with general AI vision and manual notes.

## 6. Unit economics to $10K MRR

### Target mix

| plan | price | customers | MRR |
|---|---:|---:|---:|
| Trader | $19 | 150 | $2,850 |
| Analyst | $49 | 100 | $4,900 |
| Education/team | $99 | 23 | $2,277 |
| **Total** |  | **273** | **$10,027** |

### Cost model

Assumptions:

- Average processed chart cost: **$0.45**.
- Average charts per account per month: **15**.
- Payment/infrastructure cost: **3% of revenue**.
- Support allowance: **$4/account/month**.
- Fixed solo operating cost: **$1,200/month**.

At 273 accounts:

- Revenue: approximately **$10,027/month**.
- Inference/storage cost: approximately **$1,843/month**.
- Payment/infrastructure: approximately **$301/month**.
- Support allowance: approximately **$1,092/month**.
- Contribution before fixed cost: approximately **$6,791/month**.
- After fixed cost: approximately **$5,591/month** before taxes and founder compensation.

### CAC and payback assumptions

- Target blended CAC: **≤ $30**.
- At a $19 plan, one-month gross profit must remain positive:
  - approximately $19 revenue;
  - roughly $6.75 inference cost;
  - roughly $0.57 payment/infrastructure;
  - roughly $4 support allowance;
  - approximately $7.68 contribution before fixed cost.
- The $19 plan may require annual payment or a lower support promise to improve payback.
- At $49 and $99, one-month payback is easier.
- Partnerships with educators are likely necessary to reach 273 accounts without exceeding the $300 budget.

### Sensitivity

- 150 customers at $49 produces $7,350 MRR.
- 204 customers at $49 produces approximately $10K MRR.
- If average charts per account rise to 30, inference costs rise materially; usage limits and efficient model routing are required.
- If churn is above 10% monthly, acquisition must be replaced continuously and the economics weaken.

## 7. Kill criteria

Pause or kill if:

1. Fewer than 4 of 10 interviewed users perform a recurring chart-screenshot workflow.
2. Users primarily want trade signals rather than extraction, and those users reject the non-advisory positioning.
3. The evaluation corpus fails to achieve 90% readable-label accuracy and 80% structured extraction on supported charts.
4. More than 30% of charts require manual correction to be useful.
5. Fewer than 5 users pay after 30 days.
6. Blended CAC exceeds $30 for the $19 plan or $75 for the $49 plan without sufficient monthly gross profit.
7. Inference plus support cost exceeds 60% of revenue on the average customer.
8. Users treat low-confidence values as authoritative, creating unacceptable support or trust risk.
9. The business requires regulated financial-advice claims to convert.
10. Monthly churn exceeds 10%.
