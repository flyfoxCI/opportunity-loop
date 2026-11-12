---
layout: post
title: "Chart Scanner AI — Direction Package"
date: 2026-11-12T22:35:11+00:00
week: "2026-11-12_223511"
week_date: "2026-11-12T22:35:11+00:00"
slug: "chart-scanner-ai"
permalink: /directions/chart-scanner-ai.html
tags:
  - "AI"
  - "SaaS"
  - "education"
  - "language"
  - "mobile"
excerpt: "Scan chart screenshots into structured, explainable technical-analysis reports."
---

## Why this direction

### TrustMRR evidence

- Chart Scanner AI was classified `GO_CANDIDATE` with **$25.69 MRR**, **$31.10 in last-30-day revenue**, and **99 subscribers**.
- Its demand heuristic was **3**, while its competition heuristic was **3**.
- The last-30-day revenue exceeded current MRR, which is consistent with recent growth or subscriber mix changes.
- The product appears to address a frequent analysis workflow: a trader uploads or captures a chart and receives a structured assessment rather than manually combining visual inspection, indicators, and note-taking.

### X/web evidence

- Stage A did not provide a public X handle for Chart Scanner AI.
- The supplied TinyFish output returned CLI installation instructions rather than usable result excerpts, so no individual X post is claimed as independently verified.
- Recurrent demand signals in trading communities include:
  1. fast second-opinion analysis during market hours;
  2. difficulty keeping a consistent process when reviewing many instruments;
  3. requests for plain-language explanations of chart structure and risk;
  4. desire to capture and annotate charts for later review;
  5. concerns about AI-generated financial advice and false precision.
- Competitive interpretation: general chart platforms, indicator dashboards, AI trading bots, and technical-analysis education are broad substitutes. A focused product can own **post-capture chart review for discretionary swing traders**, not automated trade execution or portfolio management.
- **Final score: demand 3, competition 3 → GO.**

## Competitor table

> Pricing is directional and must be verified before launch.

| Level | Competitor | Pricing found or typical positioning | Strength | Opening for Chart Scanner AI |
|---|---|---:|---|---|
| L1 direct | TradingView | Free tier; paid advanced plans | Largest charting and social ecosystem | Faster screenshot-to-structured report and cross-platform portability. |
| L1 direct | TradingView AI Chart Analysis | Included in some TradingView plans/features | Native chart access and recognized interface | Image-based analysis without requiring live chart login or paid indicator stack. |
| L1 direct | CoinGlass / AI chart tools | Varies; often freemium or paid | Crypto-specific data and analysis | Explainable setup review independent of exchange and token selection. |
| L1 direct | Komo / AI chart analysis tools | Freemium/paid | Rapid technical summaries | Less generic language, explicit uncertainty, and trader-controlled risk checks. |
| L2 | TrendSpider / Trading Central / StockCharts | Subscription | Professional charting and signals | Low-friction capture, structured report, and lower setup burden. |
| L2 | Digrin | Freemium/paid | AI chart recognition and pattern explanations | Trade-journal context and disciplined post-capture review. |
| L2 | ChatGPT / general multimodal AI | Paid subscription | Flexible explanations and cheap availability | Structured technical-analysis schema, chart-specific checks, and consistent reports. |
| L3 | Broker and exchange chart tools | Often free | Native price data and execution | Analysis layer for users who keep charts elsewhere. |
| L3 | Trading journals | $20–$100+/month | Habit tracking, performance review | Turn a captured setup into a testable, evidence-backed review. |

### Competition score rationale

**3/5.** TradingView and general AI tools are strong substitutes, and native AI chart features improve. However, a narrowly designed screenshot-analysis workflow can differentiate through portability, structured outputs, explicit uncertainty, and journal integration. The MVP must avoid competing on real-time data, signals, or execution.

## PRD MVP

### Target customer

- Discretionary swing traders who use screenshots from another charting platform.
- Crypto traders reviewing exchange or TradingView charts.
- Trading educators and community managers producing repeatable chart breakdowns.
- Later: active traders journaling setups.

### Core job

> “Give me a consistent second-opinion review of this chart in under a minute, with observations, possible scenarios, invalidation levels, and clear uncertainty.”

### P0 — required for launch

1. **Chart ingestion**
   - Upload PNG, JPG, WEBP, and PDF.
   - Optional symbol, timeframe, and context fields.
   - Clear quality warnings for unreadable or cropped charts.
2. **Chart structure extraction**
   - Approximate price range and displayed timeframe.
   - Trend, support/resistance zones, visible patterns, and volume behavior.
   - Never imply exact values that cannot be read reliably.
3. **Setup classification**
   - User-selected strategy labels such as breakout, pullback, reversal, or range.
   - Rule-based checklist based on the user's selected methodology.
   - Neutral output when evidence is insufficient.
4. **Structured report**
   - Observation, supporting evidence, possible scenarios, invalidation risks, and missing information.
   - “No signal” is an acceptable result.
   - Confidence expressed as evidence strength, not a probability of profit.
5. **Annotations**
   - Overlay trend lines, zones, and labels.
   - Export annotated chart plus report.
6. **History**
   - Saved analyses and lightweight trade-journal fields.
   - Tag setup, outcome, and lesson after the user records it.
7. **Account, billing, and quota**
   - Email authentication.
   - Usage limits by plan.
   - Private chart storage and deletion controls.

### P1 — after validation

- Multi-chart comparison.
- Custom strategy checklists.
- TradingView/Trading Central style guide packs.
- Custom alert rules based on a saved analysis.
- Journal performance views.
- CSV/PDF journal export.
- API access for paid research users.
- Education-community branded reports.

### P2 — later

- Broker integrations.
- Live data overlays.
- Replay and backtesting.
- Automated trade execution.
- Predictive price targets.
- Social portfolio sharing.
- Mobile native app.

### Explicit non-goals for the first 14 days

- No brokerage or exchange integration.
- No automated order placement.
- No buy, sell, hold, or target-price recommendation.
- No claim that analysis predicts future returns.
- No live market-data feed.
- No model portfolio or copy-trading marketplace.
- No casino, sports-betting, or binary-options product.
- No auto-generated social posts as the core feature.
- No black-box “AI oracle.”

### Technical approach

- Frontend: Next.js/TypeScript.
- Backend: serverless functions or Python workers for image analysis.
- Database: PostgreSQL.
- Storage: private object storage with signed URLs.
- Vision model: multimodal API with a strict structured-output schema.
- Deterministic layer: chart OCR, image preprocessing, indicator/rule checks, and validation.
- PDF export: server-side browser rendering.
- Safety layer: prohibited financial-advice language checks, uncertainty requirements, and refusal to output guaranteed outcomes.
- Security: per-user storage isolation, rate limits, expiring links, and prompt/data retention controls.

### Pricing hypothesis

- **Free:** three analyses/month and watermarked report.
- **Trader — $15/month:** 60 analyses, history, annotations, journal.
- **Pro — $39/month:** 250 analyses, custom checklists, PDF export.
- **Creator — $79/month:** branded reports, higher limits, team use.
- No outcome-based pricing and no upsell based on predicted performance.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|
| 1 | Scope lock and compliance copy | One trader segment, supported chart types, prohibited claims, and output schema defined. |
| 2 | Data model and ingestion | Upload, symbol/timeframe metadata, analysis, report, annotation, and usage models work. |
| 3 | Image preprocessing | Crop, resize, enhance, and detect unreadable charts with actionable warnings. |
| 4 | Structured extraction | Chart structure is returned in validated JSON with confidence and evidence fields. |
| 5 | Scenario and invalidation engine | Reports include observations, scenarios, risks, and missing information without trading directives. |
| 6 | Report UI | Users can review, edit, rerun, and export structured reports. |
| 7 | Annotations | Trend lines and zones can be drawn and included in the export. |
| 8 | History and journal | Saved analyses can be tagged, reviewed, and linked to a later outcome. |
| 9 | Auth, billing, and quotas | Subscription state, limits, cancellation, and generation history work. |
| 10 | Safety and quality suite | Financial-advice language, unsupported precision, hallucination, and adversarial charts are tested. |
| 11 | UX polish | Upload-to-report works on mobile and desktop; errors are clear. |
| 12 | Privacy and deletion | Users can delete charts, reports, and account data; retention settings are visible. |
| 13 | Dogfooding | Ten experienced discretionary traders test known charts and review output quality. |
| 14 | Launch | Production deploy, sample reports, support flow, disclaimers, demo video, and launch posts. |

### Launch-readiness checklist

- A supported chart produces a useful structured report in under 90 seconds.
- Unsupported or illegible charts receive a clear refusal rather than fabricated analysis.
- No output promises certainty, profit, or a trade recommendation.
- Every stated observation points to visible chart evidence.
- Users can delete all uploaded chart data.
- Ten target traders have reviewed outputs during dogfooding.

## 30-day marketing calendar

### Budget

| Channel | 30-day budget |
|---|---:|
| Analyst/creator collaborations and sample reports | $120 |
| Selective paid tests for proven report pages | $100 |
| Demo data, production, and storage | $80 |
| **Total** | **$300 maximum** |

### Weekly calendar

#### Days 1–7: establish category and trust

| Day | Action |
|---:|---|
| 1 | Publish an explainer: what a chart-analysis report can and cannot tell a trader. |
| 2 | Recruit 10 discretionary swing traders for interviews and sample-chart reviews. |
| 3 | Publish a transparent side-by-side chart, evidence, report, and human correction. |
| 4 | Share a no-signal example showing the system declining to force a conclusion. |
| 5 | Post a founder diary about building a financial-analysis tool without financial advice. |
| 6 | Reach out to 15 trading educators or community managers with a branded sample report. |
| 7 | Launch the landing page and founder-led product announcement. |

#### Days 8–14: use cases and proof

| Day | Action |
|---:|---|
| 8 | Publish a TradingView-to-report workflow tutorial. |
| 9 | Publish a crypto-chart workflow tutorial. |
| 10 | Add a saved-analysis journal walkthrough. |
| 11 | Offer 20 assisted pilots to active traders and educators. |
| 12 | Release an “invalidation checklist” lead magnet. |
| 13 | Host a live chart-review clinic without presenting outcomes as guaranteed. |
| 14 | Email qualified leads with a personalized sample report. |

#### Days 15–21: improve and convert

| Day | Action |
|---:|---|
| 15 | Publish a case study on report review time and user corrections. |
| 16 | Reach out to 20 trading educators with a branded-report offer. |
| 17 | Improve the most common extraction and terminology failure modes. |
| 18 | Add a “second opinion, not signals” landing-page section. |
| 19 | Publish a journal-retention workflow for discretionary traders. |
| 20 | Re-engage users who uploaded but did not save an analysis. |
| 21 | Ask satisfied users for a review and referral. |

#### Days 22–30: retention and selective scale

| Day | Action |
|---:|---|
| 22 | Add custom strategy checklists if manually requested by five users. |
| 23 | Interview retained and churned users. |
| 24 | Publish a model/accuracy limitations update. |
| 25 | Test a $50 paid report-page campaign only after organic signup validation. |
| 26 | Add a data-deletion walkthrough and privacy FAQ. |
| 27 | Publish an educator/community case study. |
| 28 | Test annual pricing only if monthly churn is under 10%. |
| 29 | Introduce a referral benefit after a saved report. |
| 30 | Review MRR, activation, report acceptance, corrections, churn, CAC, and safety incidents. |

### KPIs

- Upload-to-report: target 90% within one day.
- Successful analysis without a hard error: target 90%.
- Users who save, annotate, or export: target 35%.
- Free-to-paid conversion after five analyses: target 6%.
- Month-one paid retention: target 90%.
- Serious safety incidents: zero.
- Paid CAC target: under $70.
- Day-30 MRR validation target: **$1,000–$2,500**.

## Unit economics to $10K MRR

### Base case

Assume blended ARPU of **$25/month** and gross margin of **78%** after multimodal inference and storage.

- Customers required: `$10,000 / $25 = 400`.
- Monthly gross profit: `$10,000 × 78% = $7,800`.
- Variable model, storage, and processing costs should remain below **$2,200/month** at 400 users.

### Customer mix

| Customers | Blended ARPU | MRR | Use |
|---:|---:|---:|---|
| 250 | $15 | $3,750 | Trader |
| 115 | $39 | $4,485 | Pro |
| 35 | $79 | $2,765 | Creator |
| **400** | **$27.50** | **$11,000** | Target threshold exceeded |

### CAC and LTV

- Target CAC ceiling: **$65**.
- Gross profit per customer per month at $25 ARPU and 78% margin: **$19.50**.
- Target gross-margin LTV/CAC: **3x**, requiring **$195 LTV**.
- At a 12-month revenue horizon and an average retained life of about 10 months, contribution LTV is approximately **$195**.
- The model clears the threshold only narrowly. ARPU, retention, or referral CAC must improve for attractive economics.
- Initial scaling acquisition: 400 × $65 = **$26,000** over the growth period, funded through revenue.

### Cost controls

- Use cheaper OCR/vision tiers for low-value free requests.
- Reject unsupported images before model invocation.
- Compress client images before upload.
- Store thumbnails instead of full-resolution originals after processing.
- Cache repeated structured analyses where privacy policy permits.
- Cap free usage and paid generation quotas.
- Use deterministic checks to reduce retries and hallucinations.

## Kill criteria

Kill or pause if any of the following occurs:

1. **Use-case failure:** fewer than 8 of 15 interviewed traders regularly review charts outside their native platform.
2. **Activation failure:** fewer than 30% of signups upload a supported chart within seven days.
3. **Quality failure:** more than 25% of reviewed outputs contain a material unsupported observation.
4. **Value failure:** fewer than 25% of users save or export a report after analysis.
5. **Paid conversion failure:** fewer than 5 paid users from 100 activated accounts after two iterations.
6. **Retention failure:** paid churn exceeds 10% in the first billing month.
7. **Safety failure:** any output gives an explicit buy/sell instruction, predicts returns with false precision, or conceals material uncertainty.
8. **Economics failure:** CAC exceeds $65 without creator/referral distribution, or gross margin falls below 70%.
9. **Platform risk:** chart providers block automated capture in a way that makes the intended workflow unreliable.
10. **Scope trap:** the business depends on live data, signals, brokerage, or execution rather than second-opinion review.

Decision rule: if material unsupported observations remain above 15% after two focused iterations, restrict supported charts and categories. If the safety layer cannot reliably prevent prescriptive financial advice, kill the product.

## Research caveats

- The supplied TinyFish output did not contain usable social or web excerpts.
- Chart-analysis feature availability and pricing change rapidly and must be checked before launch.
- This direction is deliberately not a trading bot, signal service, or gambling-adjacent product.
- The GO relies on screenshot review for discretionary traders; live-data and brokerage expansion is excluded.
