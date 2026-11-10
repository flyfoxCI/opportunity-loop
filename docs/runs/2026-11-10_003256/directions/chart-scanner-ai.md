# Chart Scanner AI — Opportunity Direction

## 1. Why this direction

### Opportunity

Create a narrow screenshot-to-investor-brief assistant. A user uploads an existing price-chart screenshot from one supported platform and receives a structured summary: visible trend, support and resistance zones, notable volatility, and a short watchlist note. The product explains what is visible in the supplied chart; it does not provide brokerage, execute trades, promise returns, or give personalized financial advice.

### Target customer

The initial ICP is a non-professional active trader or research-oriented investor who:

- Already receives screenshots from a charting or social platform.
- Wants a faster written interpretation for notes, alerts, or review.
- Uses one platform and one chart style.
- Understands the informational—not advisory—nature of the output.
- Will pay for research organization and time savings.

The initial supported platform should be selected before coding. The recommended first wedge is Discord-based trading communities, where screenshots and interpretation requests are common. However, the product must avoid unsolicited promotion, signal-selling, manipulation, or facilitating market abuse.

### TrustMRR evidence

Stage A reports Chart Scanner AI at:

- MRR: **$25.08**
- Last 30 days: **$27.00**
- Subscribers: **98**
- Stage A demand score: **3**
- Stage A competition score: **3**
- Website: https://chartscannerai.com

The product has paid validation and sustained recent revenue, making it stronger than low-revenue novelty apps. However, the category includes established technical-analysis products, charting platforms with built-in AI, and free indicator ecosystems. The initial implementation should therefore avoid attempting to scan every chart type or make predictions.

### X and web evidence

The supplied automated search output did not return actual search results and cannot substantiate demand. Perform these searches manually:

- `"Chart Scanner AI" (painful OR broken OR hate OR expensive)`
- `"Chart Scanner AI" (looking for OR recommend OR alternative)`
- `"chart scanner AI" trading`
- `"screenshot chart" analysis (AI OR Discord)`
- `"chart analysis" (painful OR "takes forever" OR manual)`
- `site:x.com "Chart Scanner AI"`
- `site:reddit.com screenshot chart analysis AI`

Demand validation requires 10 dated posts, at least five explicit pain statements, at least three mentions of manual or expensive alternatives, and evidence that users would pay $15–$29 per month for interpretation workflows. Collect public evidence without attempting to scrape private groups.

### Why it can win

The product should focus on a narrow, repeatable job:

1. Receive a screenshot.
2. Confirm the platform and timeframe.
3. Extract visible structure and indicators.
4. Return a structured, source-tied chart brief.
5. Save the brief to a personal watchlist or export it.

The value is fast organization and consistent visual explanation, not prediction accuracy.

### Validation gate

Proceed only if:

1. Ten public demand signals or interviews confirm repetitive screenshot analysis is a pain.
2. Five testers provide example charts from the same platform.
3. Three testers agree to use a daily or weekly brief.
4. Two agree to pay $15 or more per month.
5. Compliance review confirms that the interface, marketing, and outputs avoid personalized advice and guaranteed-return language.

## 2. Competitor table

### L1 direct competitors

| Competitor | Positioning | Pricing to verify | Strength | Opening for Chart Scanner AI |
|---|---|---:|---|---|
| Chart Scanner AI | Chart screenshot analysis, to verify | Unknown | Existing paid audience and focused product | Improve explainability, watchlist workflow, and platform-specific UX |
| TradingView | Charting platform with indicators and AI-assisted features | Free tier plus paid plans | Global distribution and rich charting | Analyze existing screenshots without requiring platform migration |
| TrendSpider | Automated chart pattern detection | Paid plans | Pattern recognition and alert workflows | Faster screenshot-to-brief workflow and lower complexity |
| Pattern Daytrader | Chart-pattern scanner and alerts | Paid plans | Established scanner features | Lower setup burden and broader visual explanation |
| Stocks Signals | Technical analysis and signal reports | Paid plans | Ready-made analyses | Focus on the user's own chart and transparent uncertainty |
| Danelfin | AI-driven stock analysis | Free and paid options | Broad investor audience | Chart-image input and concise structured output |
| Tickeron | AI trading pattern and forecast tools | Paid plans | Pattern-focused AI | Avoid forecast positioning; emphasize visual explanation |
| TradingFinder | Pattern and indicator platform | Paid plans | Technical-analysis tooling | Lightweight screenshot workflow |
| LuxAlgo | TradingView indicators and AI tools | Paid plans | Creator ecosystem and indicator depth | Cross-platform screenshot intake and compact briefs |

Pricing, features, and market availability must be checked on official sources immediately before implementation.

### L2 alternatives

| Alternative | Why users choose it | Opening |
|---|---|---|
| Manual analysis | Free and uses full human judgment | Slow and inconsistent for repetitive research |
| TradingView built-in AI | Convenient and bundled | Platform-locked and less useful for screenshots from elsewhere |
| Broker chart tools | Included with brokerage | Limited cross-platform use |
| Community analysts | Contextual and social | Inconsistent, potentially promotional, and not always available |
| Spreadsheet notes | Flexible | Manual, difficult to search, and no structured chart context |
| General vision models | One-off analysis | Inconsistent structure, no chart-specific workflow, no watchlist |
| Screenshot OCR tools | Extracts text/levels | Does not explain structure or record a research brief |

### L3 substitute behavior

- Screenshot the chart and post it to a paid analysis group.
- Ask another trader personally.
- Write notes manually.
- Take a screenshot and upload it to ChatGPT or another general model.
- Use only the charting platform's native AI.
- Avoid the workflow entirely.

### Competition score

**Score: 4/5.** Paid demand exists, but the category includes charting platforms, scanner tools, signal services, and general AI substitutes. This direction is therefore **`GO_NARROW`**, not full-market GO.

### Narrow wedge

The product must be limited to:

- One screenshot source ecosystem in the first release.
- One primary instrument class or visual template.
- Visible technical structure only.
- A structured research brief and personal watchlist.
- No predictions, buy/sell recommendations, automated trading, copy trading, social posting, or brokerage.

If the wedge changes, reassess demand, competition, and compliance.

## 3. PRD — MVP

### Product promise

Turn one supported chart screenshot into a clear, structured research brief in under 30 seconds.

### P0 — launch-critical

1. **Supported screenshot intake**
   - Upload PNG/JPEG.
   - One supported chart platform and viewport.
   - Automatic size and quality checks.
   - User confirms instrument, timeframe, and intended watchlist label.

2. **Vision extraction**
   - Detect candlestick or line-chart structure.
   - Extract visible price range, date/time labels, and major peaks and troughs.
   - Detect a limited indicator set only if visible.
   - Do not infer unavailable values.

3. **Structured brief**
   - Instrument, timeframe, visible range, and source.
   - Trend description.
   - Support and resistance as approximate visual zones.
   - Volatility description.
   - Notable events.
   - Confidence and missing-data warnings.
   - "What the image does not establish" disclaimer.

4. **Watchlist**
   - Save briefs to a personal account.
   - Add a note and tag.
   - Compare two saved observations.
   - Export as Markdown or CSV.

5. **Account and billing**
   - Email magic-link authentication.
   - 7-day trial.
   - Starter: **$19/month**, 40 analyses.
   - Pro: **$49/month**, 200 analyses.
   - Stripe billing.

6. **Trust and safety**
   - Prominent informational-only language.
   - No individualized buy/sell/sell/hold recommendation.
   - No guaranteed-return or performance claims.
   - Upload deletion controls.
   - No image retention in the free trial by default, or a clearly stated short retention policy.
   - No public sharing in the MVP.
   - Block or flag manipulated, altered, or low-resolution images where detectable.

7. **Quality controls**
   - Test suite of screenshots from the supported platform.
   - Confidence thresholds.
   - “Unable to analyze” state rather than fabricated analysis.
   - Manual correction/reporting button.
   - Model and prompt version stored with every brief.

### P1 — first 30 days

- Additional chart screenshot layouts for the same platform.
- Daily watchlist digest by email.
- Alert when a saved brief is manually re-uploaded and compared.
- PDF export.
- Side-by-side screenshot comparison.
- Team watchlist with limited seats.
- More instrument classes only within the same platform.

### P2 — after product-market signal

- Mobile screenshot share extension.
- Multi-platform support.
- User-defined watchlist conditions.
- API access.
- Private team workspace.
- Integration with journaling platforms.
- Additional chart types.

### Non-goals

- Brokerage or exchange integration.
- Order placement.
- Buy, sell, or hold recommendations.
- Price predictions.
- Guaranteed signals.
- Copy trading.
- Social-media auto-posting.
- Signal-selling or paid trade alerts in the MVP.
- Multi-user social feed.
- Full charting platform.
- Indicator marketplace.
- Support for every charting platform in the MVP.
- Backtesting.
- Claims of financial return.
- Copyrighted redistribution of chart images.

### Core user stories

- As an active researcher, I want a screenshot interpreted quickly so that I can spend more time reviewing research.
- As a researcher, I want the output tied to visible chart evidence so that I can judge uncertainty.
- As a researcher, I want saved briefs so that I can revisit observations.
- As a researcher, I want the tool to refuse unsupported images so that I am not misled by fabricated analysis.
- As a privacy-conscious user, I want control over uploaded screenshot retention.

### MVP acceptance criteria

A user can:

1. Sign up.
2. Upload one supported chart screenshot.
3. Select instrument, timeframe, and label.
4. Receive a structured brief with visible evidence and uncertainty.
5. Save the brief to a watchlist.
6. Export it.
7. Delete the image and analysis according to policy.
8. Upgrade through Stripe.

### Technical recommendation

- TypeScript web application.
- PostgreSQL for users, analyses, briefs, and watchlist entries.
- S3-compatible object storage with short-lived signed upload URLs.
- A vision model with structured JSON output.
- Queue long-running analysis jobs.
- Prompt and model version metadata.
- Stripe billing.
- Structured audit log for analysis versions and corrections.
- Encryption in transit and at rest.
- Moderation and privacy review before enabling any sharing.

### Compliance safeguards

- Contract specialist review before launch.
- Use terms such as “chart summary,” “research note,” and “visual observation,” not “signal” or “prediction.”
- Include risk and informational-use disclosures.
- Prohibit marketing claims about profits or accuracy.
- Do not use user images for model training without explicit opt-in.
- Provide takedown and deletion workflows.
- Preserve audit records without retaining unnecessary source images.

## 4. 14-day build plan

| Day | Objective | Deliverables | Exit criterion |
|---:|---|---|---|
| 1 | Validate ICP and compliant wedge | Select one platform; ten interviews/post reviews; define forbidden outputs | Five strong pain confirmations |
| 2 | Validate willingness to pay | Show concierge brief; offer $19/month | Two paid commitments |
| 3 | Compliance and dataset | Risk checklist, 50 consented test charts, labeling guide, test set | Legal/specialist review and test set complete |
| 4 | Foundation | Auth, database, storage, queue, model versioning | End-to-end placeholder analysis works |
| 5 | Image intake | Upload, validation, retention controls, metadata | Supported and unsupported images route correctly |
| 6 | Vision extraction | Structured chart data and confidence scoring | 80% schema success on supported test set |
| 7 | Brief generation | Trend, levels, volatility, uncertainty, disclaimer | Twenty test briefs pass quality rubric |
| 8 | Watchlist | Save, list, detail, tag, compare, export | Full saved-analysis workflow works |
| 9 | Billing | Stripe, trial, quotas, customer portal | Payment and quota paths pass |
| 10 | Trust and safety | Unable-to-analyze state, report correction, deletion, audit log | Safety checklist passes |
| 11 | UX polish | Mobile upload, progress state, examples, onboarding | Five first-time users complete without help |
| 12 | Marketing and legal | Landing page, privacy policy, terms, disclaimer, pricing | Claims and disclosures pass review |
| 13 | Pilot | Ten target users analyze real screenshots | Five retained users and ten briefs |
| 14 | Release | Fix blockers, deploy, invite cohort, instrument funnel | Five users, 20 briefs, and three paying customers, otherwise review |

### Quality rubric for a brief

A supported analysis must:

- Refer only to visible chart content.
- Identify missing or uncertain data.
- Use approximate language for visual levels.
- Avoid directional trading instructions.
- Avoid claims about future performance.
- Remain understandable in under 30 seconds.

## 5. 30-day marketing calendar

### Budget

Total maximum: **$300**

| Activity | Budget |
|---|---:|
| Research and pilot incentives | $75 |
| Sponsorship of narrowly relevant educational content | $75 |
| Demo assets, charts, landing page, and email | $50 |
| Compliance review reserve | $50 |
| Referral or beta credit | $50 |
| **Total** | **$300** |

Paid promotion must be tightly controlled to avoid the appearance of paid trading signals or financial advice.

### Organic-first plan

| Day | Activity | Channel | CTA | Success signal |
|---:|---|---|---|---|
| 1 | Publish a transparent “what chart AI gets wrong” teardown | LinkedIn, X | Submit anonymized chart | 5 test charts |
| 2 | Interview 10 active chart-analysis users | Targeted outreach | Join research | 10 interviews |
| 3 | Show a before/after manual brief | LinkedIn | Request early access | 15 waitlist signups |
| 4 | Publish the supported-platform guide | Blog | Upload screenshot | 10 uploads |
| 5 | Demo uncertainty handling, not predictions | YouTube, LinkedIn | Try beta | 12 beta users |
| 6 | Post a visual-analysis walkthrough | X, Discord where permitted | Analyze a chart | 15 analyses |
| 7 | Publish methodology and limitations | Website, blog | Read methodology | 20 method visits |
| 8 | Recruit one tester community | Partner outreach | Pilot group | 10 users |
| 9 | Share a weekly research-note workflow | LinkedIn | Save a brief | 8 saves |
| 10 | Run a chart-reading office hours session | YouTube live | Bring a chart | 12 attendees |
| 11 | Publish a false-confidence case study | Blog, X | Test tool | 10 tests |
| 12 | Ask pilot users for feedback interview | Email | Book interview | 6 replies |
| 13 | Release saved watchlist update | Email, product | Compare briefs | 20% feature adoption |
| 14 | Open paid beta | Founder account, niche groups | Subscribe | 10 trials |
| 15 | Publish a sample daily research digest | Blog, email | Join digest | 8 digest signups |
| 16 | Contact niche educators and communities for workflow sponsorship | Direct outreach | Propose demo | 5 conversations |
| 17 | Publish “what this tool does not do” guide | Blog, X | Read safeguards | 15 visits |
| 18 | Show manual brief versus product brief | LinkedIn, YouTube | Try comparison | 8 trials |
| 19 | Add one supported screenshot layout | Product, email | Analyze | 10 layout uses |
| 20 | Interview retained users | Email | Continue | 6 responses |
| 21 | Publish corrected-analysis transparency report | Blog | Trust the product | 10 signups |
| 22 | Offer pilot users a monthly plan | Email | Upgrade | 5 upgrades |
| 23 | Partner with one responsible educator | Joint demo | Join session | 20 attendees |
| 24 | Publish API and export teaser | Blog, X | Join waitlist | 8 waitlist signups |
| 25 | Contact chart-journaling communities without posting signals | Direct outreach | Workflow demo | 5 conversations |
| 26 | Improve onboarding based on five failed tests | Product | Start analysis | 30% trial activation |
| 27 | Publish product transparency and deletion controls | Website | Read policy | 12 visits |
| 28 | Release weekly digest automation | Email, product | Enable digest | 15 digest users |
| 29 | Rescue inactive trial users | Email | Complete one brief | 8 rescues |
| 30 | Publish cohort metrics and limitations | Blog, founder account | Join next cohort | Clear keep/kill decision |

### Acquisition targets

By day 30:

- 150 targeted visitors.
- 35 trials.
- 15 activated users.
- 8 paying customers.
- $152 MRR at $19/month.
- Ten documented pain posts and five completed research interviews.

## 6. Unit economics to $10K MRR

### Proposed pricing

- Starter: **$19/month**, 40 analyses.
- Pro: **$49/month**, 200 analyses.
- Optional annual plan after retention evidence.

At $19/month, 527 paying customers are required for $10,013 MRR. At a blended $29/month, 345 customers are needed for $10,005 MRR.

### Model

| Metric | Conservative | Target | Strong |
|---|---:|---:|---:|
| Blended ARPA | $19 | $29 | $39 |
| Customers for $10K | 527 | 345 | 257 |
| Gross margin | 78% | 84% | 90% |
| Gross profit/customer/month | $14.82 | $24.36 | $35.10 |
| CAC allowance | $40 | $65 | $90 |
| Months to $10K at constant CAC | 142.3 | 92.0 | 65.9 |
| Monthly churn | 8% | 5% | 3% |

At $29 ARPA, 84% gross margin, and 5% churn:

- LTV = **$487.20**.
- A $65 CAC gives an LTV:CAC ratio of approximately 7.5:1.
- Payback is about 2.7 months.

### Cost controls

- Use a tiered model: standard analysis first, premium model only when confidence or feature requires it.
- Cache repeated images by content hash.
- Use smaller previews for model input.
- Limit free trials by quota and fair-use rules.
- Track gross margin per analysis, not only per subscription.
- Avoid expensive always-on inference.

### Distribution requirement

The $300 budget cannot acquire 345 customers directly. Required channels include:

1. Trusted educator and community partnerships.
2. Saved research-note workflows.
3. Referral from collaborating analysts.
4. Journaling and watchlist integrations.
5. High-value plan for active professionals.
6. A transparent evidence-based reputation that avoids performance claims.

The $10K MRR objective is a 6–12 month target after retained usage and a compliant acquisition channel are proven.

### Scenario checkpoints

- Month 1: 8 paying users and $152 MRR.
- Month 3: 30 paying users and $870 MRR.
- Month 6: 100 paying users and $2,900 MRR.
- Month 9: 345 paying users and approximately $10K MRR at $29 blended ARPA.

## 7. Kill criteria

Stop or materially reframe if:

1. Fewer than 5 of 20 target users describe screenshot interpretation as a frequent pain.
2. No tester agrees to pay $15 or more per month.
3. The product cannot reliably explain supported screenshots without fabricating visible evidence.
4. Fewer than 60% of test briefs pass the quality rubric.
5. Fewer than 30% of trials produce a saved brief.
6. Weekly retained usage falls below 25% of activated users.
7. Monthly churn exceeds 10% for two cohorts.
8. Users primarily request buy/sell signals and will not pay for informational briefs.
9. Compliance review cannot approve the proposed marketing and outputs.
10. Competitor research shows entrenched direct tools with materially better distribution and bundled pricing.
11. Model costs produce gross margin below 70%.
12. The product expands beyond one screenshot ecosystem and loses its narrow wedge.
13. The founder cannot sustain privacy, deletion, and audit obligations safely.

## Wedge (required for GO_NARROW)

> One supported charting ecosystem, one chart-image workflow, visible technical structure only. Produce a source-tied research brief and personal watchlist; refuse personalized buy/sell/hold advice, predictions, guaranteed signals, automated trading, copy trading, social posting, brokerage, and multi-platform support.
