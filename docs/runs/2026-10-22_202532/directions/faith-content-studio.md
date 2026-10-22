# Faith Content Studio — Sermon and Devotional Workflows for Small Congregations

## 1. Why this direction

### TrustMRR evidence

The prior validated research identifies **Sermon Scribe at approximately $14K MRR with 2,362 paid users**. This is unusually strong proof that small religious organizations will pay for narrow AI-assisted content workflows.

The implied customer economics are attractive: approximately $14,000 / 2,362 = **$5.93 per customer per month**. That means the model should not depend on high ARPU. Instead, it should prioritize:

- self-serve distribution;
- very low support burden;
- denomination-neutral positioning;
- a specific weekly workflow;
- low inference cost;
- conversion from seasonal or occasional use into an annual plan if needed.

The MVP focuses on sermon preparation and devotional repurposing. It does not claim theological authority or replace pastoral judgment.

### X and web evidence

The supplied Stage A search output contains no valid social results; TinyFish returned installation text only.

Before launch, collect real evidence using:

- `("sermon AI" OR "AI sermon tool") pastor`
- `("sermon preparation" pastor) (struggling OR hate OR "looking for")`
- `(church OR pastor) ChatGPT sermon`
- `("devotional content" church AI)`
- `"just shipped" sermon AI`

Archive URL, date, handle, exact quote, and engagement. Supplement this with interviews with pastors, worship leaders, and small-church administrators. Prior local-church communities may be more useful than broad consumer social feeds.

### Customer and promise

**ICP:** pastors or worship leaders at independent congregations of roughly 20–300 weekly attendees who prepare weekly messages and related devotionals.

**Promise:** Turn a pastor’s notes, scripture references, and sermon constraints into editable drafts and derivative content while preserving the pastor’s voice and final approval.

## 2. Competitor table

Pricing and denomination availability require live verification.

| Level | Competitor or substitute | Typical pricing | Strength | Opening for this product |
|---|---|---:|---|---|
| L1 direct | AI sermon-note generators | Often free or $10–$50/month | Fast structured sermon drafting | Denomination-neutral voice controls, audit trail, editable theology boundaries |
| L1 direct | Sermon Scribe and similar transcription tools | Roughly consumer-scale monthly plans proven at $14K MRR | Category recognition and repeat use | Better collaborative review and weekly content system |
| L1 direct | Church communication platforms with AI | $20–$100+/month plus broader suite | Existing church distribution | Sermon-specific workflow usable outside an ecosystem |
| L2 adjacent | ChatGPT, Claude, Gemini | $0–$200+/month | Strong general reasoning and long context | Purpose-built workflow, privacy controls, repeatable structure |
| L2 adjacent | Presentation tools | Subscription | Familiar congregation workflow | Integrated speaker notes and content output |
| L2 adjacent | Church management software | Often bundled or paid | Membership and scheduling data | Standalone content product with minimal setup |
| L3 substitute | Sermon templates and outlines | Mostly free | Human control and theological grounding | Faster personalization while keeping approval mandatory |
| L3 substitute | Human ghostwriter or intern | Project-based | High quality and contextual nuance | Lower cost and faster repeatable first drafts |

**Competitive score:** 3/5 for a narrow, denomination-neutral workflow, subject to live recheck. This is **GO**.

## 3. PRD MVP

### P0 — required for launch

1. **Organization profile**
   - name, language, denomination/tradition;
   - tone;
   - scripture translation preferences;
   - content restrictions.
2. **Weekly briefing**
   - sermon theme;
   - scripture references;
   - audience;
   - service type;
   - desired length;
   - key points.
3. **Structured generation**
   - hook;
   - thesis;
   - outline;
   - speaker notes;
   - transitions;
   - application questions;
   - Scripture references clearly separated from generated text.
4. **Voice and controls**
   - editable tone presets;
   - regenerate section;
   - accept/reject suggestions;
   - source/user-note distinction.
5. **Derivative outputs**
   - devotional;
   - bulletin summary;
   - social captions;
   - discussion questions.
6. **Review and export**
   - human approval checkpoint;
   - copy to Markdown/Docs/PDF;
   - revision history.
7. **Safety and IP**
   - no fabricated quotations;
   - explicit Scripture verification state;
   - pastor approval before publishing;
   - no impersonation;
   - copyrighted lyrics and sermon-manuscript controls;
   - delete uploaded source material.
8. **Billing**
   - Stripe;
   - monthly/annual plan;
   - trial and cancellation.

### P1 — after validation

- recurring service series;
- shared pastoral-team workspace;
- presentation export;
- calendar;
- translation;
- custom templates;
- integrations with common church tools.

### P2 — later

- congregation collaboration;
- curriculum library;
- children’s ministry variants;
- audio sermon transcription;
- messaging distribution;
- denomination-specific approved templates;
- team review analytics.

### Non-goals

- automated church publishing;
- authoritative theology or pastoral counseling;
- generated quotations presented as verified;
- unlicensed copyrighted lyrics;
- denomination control by the founder;
- faith-matching or mental-health advice;
- church-management-system replacement;
- fully autonomous preaching.

## 4. 14-day day-by-day build plan

| Day | Solo deliverable |
|---:|---|
| 1 | Interview 5 pastors or worship leaders about weekly preparation and existing tools. |
| 2 | Interview 5 more; choose one universal workflow and collect five real briefs with permission. |
| 3 | Manually produce three complete outputs; test clarity, theology boundaries, and voice. |
| 4 | Build auth, organizations, profiles, billing skeleton, and document storage. |
| 5 | Implement structured weekly briefing and deterministic output sections. |
| 6 | Add voice presets, section-level regeneration, user-note grounding, and Scripture labels. |
| 7 | Add devotional, bulletin, caption, and discussion derivative outputs. |
| 8 | Build editor, review state, version history, export, and deletion. |
| 9 | Add Stripe monthly/annual plans, trial, limits, cancellation, and cost controls. |
| 10 | Add copyright, quotation, sensitive-content, and theological caution rules. |
| 11 | Conduct five usability sessions with pastors; revise terminology and workflow. |
| 12 | Complete privacy/security review, backups, logging, and error recovery. |
| 13 | Close 15 beta accounts and deliver weekly support manually. |
| 14 | Fix launch blockers, publish, charge users, and measure first-week activation. |

## 5. 30-day marketing calendar

**Budget cap:** $150, heavily favoring ministry communities and content-led organic distribution.

| Day/channel | Action | Budget |
|---|---|---:|
| 1–3 | Publish landing page with an annotated example sermon brief | $0 |
| 4 | Share a free “sermon preparation workflow” template in ministry groups | $0 |
| 5 | Personally deliver three sample sermon outlines | $0 |
| 6 | Publish a transparent AI-use and Scripture-verification guide | $0 |
| 7 | Ask beta pastors for one outcome quote | $0 |
| 8 | Run a live sermon-brief teardown | $0 |
| 9 | Contact five church-service or ministry newsletter writers | $0 |
| 10 | Publish a comparison with generic ChatGPT prompts | $0 |
| 11 | Run a $75 ministry newsletter sponsorship | $75 |
| 12 | Onboard every trial with a real upcoming service | $0 |
| 13 | Publish derivative-content examples | $0 |
| 14 | Review activation and editing behavior | $0 |
| 15 | Contact worship leaders and volunteer administrators | $0 |
| 16 | Add recurring-series templates | $0 |
| 17 | Publish a theology-neutral review checklist | $0 |
| 18 | Ask users to invite one pastoral-team collaborator | $0 |
| 19 | Publish a before/after time-saving case study | $0 |
| 20 | Review language, cultural, and theological complaints | $0 |
| 21 | Add preferred scripture-translation handling | $0 |
| 22 | Approach ten small churches through their public ministry contacts | $0 |
| 23 | Host a second live session | $0 |
| 24 | Request an annual-plan conversion conversation | $0 |
| 25 | Publish a printable sermon workflow | $0 |
| 26 | Test pricing between $15 and $29 monthly without permanent discounting | $0 |
| 27 | Onboard warm prospects and close objections | $0 |
| 28 | Review retention, usage cadence, support burden, and gross margin | $0 |
| 29 | Ship one recurring-use feature | $0 |
| 30 | Continue, narrow, or kill based on paid weekly use | $0 |

## 6. Unit economics to $10K MRR

### Pricing

Primary options:

- Solo: **$19/month**
- Pro: **$39/month**
- Team: **$79/month for 5 collaborators**
- Annual: two months free

Assume average realized ARPU of **$22/month**.

| Metric | Assumption |
|---|---:|
| Model/API cost per active user | $2–4/month |
| Infrastructure allocation | $1 |
| Support allocation | $1 |
| Payment/overhead allocation | $1 |
| Contribution/user/month | about $15–17 |

- Customers needed: $10,000 / $22 = approximately **455 paid accounts**.
- At 80% gross margin, monthly variable cost at target is about $2,500.
- At 6% monthly churn, approximately 27 new subscribers per month are required merely to replace churn at 455 accounts, before growth.
- Organic distribution and pastoral referrals are therefore essential; paid media cannot be the primary acquisition strategy.

### Retention requirement

Because church budgets are sensitive, target:

- monthly logo churn below 6%;
- at least 45% active users generating a weekly brief;
- annual conversion above 20%;
- median support time below five minutes per account monthly.

## 7. Kill criteria

Kill or re-niche if any occur by Day 30:

- fewer than 25 pastor or worship-leader interviews;
- fewer than 15 users create a real brief;
- fewer than 8 pay;
- fewer than 6 return for a second service/week cycle;
- fewer than 4 use derivative outputs;
- users require denomination-specific theological judgment the product cannot safely provide;
- Scripture or quotation accuracy repeatedly undermines trust;
- users only want a one-off free generation and refuse recurring workflow software;
- monthly churn exceeds 10% after onboarding fixes;
- contribution margin falls below 70%;
- copyright complaints or misuse cannot be mitigated technically and contractually.

## Wedge (required for GO_NARROW)

This direction is marked **GO**, not GO_NARROW, so no additional narrowing section is required. The product remains intentionally scoped to sermon preparation and derivative devotional content rather than general-purpose religious AI.
