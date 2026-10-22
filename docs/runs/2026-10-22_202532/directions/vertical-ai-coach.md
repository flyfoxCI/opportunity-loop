# Vertical AI Coach — Evidence-Grounded Practice Coach for Real-Estate Agents

## 1. Why this direction

### TrustMRR evidence

The prior validated direction pack identifies **Sherpa at approximately $26K MRR** as evidence that AI-assisted professional mentorship can support meaningful recurring revenue. More importantly, it reports that dedicated AI mentor products for individual professions remain sparse even while general-purpose coaching products and human coaching are widely available.

That creates an opening for a narrower product:

- one profession;
- one repeated workflow;
- evidence-grounded responses;
- practice and accountability;
- output that saves time rather than merely producing motivational text.

The initial vertical is **real-estate agents**. They repeatedly prepare listing copy, prospect-call preparation, follow-ups, CMA narratives, and client objections. The product should not attempt to replace brokerage expertise or give legal, tax, lending, or appraisal advice.

### X and web evidence

The supplied Stage A search payloads are unusable because TinyFish returned CLI help text instead of social results. No direct X quote is therefore claimed as verified.

Before building, search and archive actual evidence using:

- `("real estate agent" OR realtor) ("ChatGPT" OR AI) (painful OR hate OR "looking for")`
- `("listing copy" OR "follow-up") realtor AI`
- `("listing appointment" OR "CMA") (template OR ChatGPT OR AI)`
- `("real estate coach" OR "agent coaching") software`

Valid evidence must include a URL, date, exact pain statement, and—where applicable—engagement. The manually supported concierge interviews in Week 1 are the minimum fallback if social evidence remains thin.

### Customer and promise

**ICP:** U.S. or Canadian residential real-estate agents with 3–30 active clients, working primarily in team or brokerage environments, and already paying for at least one productivity or coaching tool.

**Promise:** Produce evidence-grounded listing, prospect, and follow-up work in minutes while preserving a distinct voice and client context.

**Why it is selectable:** professional users have high willingness to pay, the initial workflow can be delivered manually, and the narrow vertical makes messaging and evaluation tractable.

## 2. Competitor table

The following are category-level competitors and substitutes. Prices and current features must be rechecked immediately before launch.

| Level | Competitor or substitute | Typical positioning/pricing | Strength | Opening for this product |
|---|---|---|---|---|
| L1 direct | Sherpa / AI mentor products | Premium professional coaching; price varies | Strong coaching framing | Profession-specific workflows, evidence traceability, email and CRM context |
| L1 direct | Real estate coaching platforms | Often $50–$500+/month for humans or programs | Human accountability and trust | Lower-cost daily workflow practice, not full coaching replacement |
| L1 direct | Real-estate CRM AI assistants | Bundled with established CRM ecosystems; often $20–$100+/seat/month | Data and workflow integration | Vendor-neutral intake and rapid setup |
| L2 adjacent | General ChatGPT, Claude, and Gemini | $0–$200+/user/month | Powerful general generation | Real-estate playbooks, citations, client-memory controls, evaluation |
| L2 adjacent | Listing-copy generators | Free to $30/month | Fast listing descriptions | Broader pre-listing workflow: objections, follow-up, CMA narrative |
| L2 adjacent | Human coaches and brokerages | $100–$2,000+/month | Empathy and accountability | Measurable drills and asynchronous practice |
| L3 substitute | Templates, spreadsheets, and note-taking | Low recurring cost | Flexible and familiar | Faster context capture and evidence-based feedback |
| L3 substitute | Generic CRM automations | Included with brokerage stack | Existing adoption | Portable playbook and better coaching feedback |

**Competitive score:** 4/5. Competition is meaningful, so this is **GO_NARROW**, not full-market GO.

## 3. PRD MVP

### P0 — required for launch

1. **Agent profile**
   - brokerage, market, role, target buyer, and communication style.
2. **Workflow sessions**
   - listing preparation;
   - prospect-call preparation;
   - listing-appointment follow-up;
   - CMA conversation preparation;
   - common-objection practice.
3. **Grounded response**
   - workflow-specific prompt templates;
   - editable assumptions;
   - visible source notes or user-provided materials;
   - “do not invent” behavior.
4. **Practice loop**
   - scenario;
   - user response;
   - rubric-based feedback;
   - one next drill.
5. **History and reuse**
   - save outputs;
   - copy/export;
   - regenerate with edits.
6. **Safety**
   - fair-housing and legal/tax/lending disclaimers;
   - no unsupported claims;
   - sensitive client-data deletion controls;
   - no automated outbound messaging in MVP.
7. **Billing**
   - Stripe subscription;
   - 7-day trial;
   - self-serve cancellation.

### P1 — after launch validation

- CRM paste-in context such as HubSpot or Follow Up Boss;
- voice rehearsal and transcription;
- brokerage-level templates;
- manager scorecards;
- custom playbook upload;
- Zapier or Make export.

### P2 — later

- email and calendar integrations;
- cohort coaching;
- marketplace;
- multilingual support;
- role-based manager analytics.

### Non-goals

- automated lead contacting;
- automated email or SMS;
- CMA valuation or pricing decisions;
- legal, tax, mortgage, or investment advice;
- replacement for a licensed agent, broker, or human coach;
- brokerage operating-system replacement;
- generic life coaching;
- support for every profession at launch.

## 4. 14-day day-by-day build plan

| Day | Solo deliverable |
|---:|---|
| 1 | Interview 3 agents; define the listing-appointment workflow, rubric, and prohibited claims. Interview one brokerage manager or coach. |
| 2 | Interview 3 more agents; choose the narrow promise and manually create five high-quality deliverable examples. |
| 3 | Interview 2 agents and test the examples; record objections and willingness-to-pay signals. |
| 4 | Build authentication, database schema, billing skeleton, and session persistence. |
| 5 | Implement profile and four workflow templates using structured model output. |
| 6 | Add evidence-note upload, citations, safety rules, and output editing. |
| 7 | Implement practice scoring, feedback, history, copy/export, and basic analytics. |
| 8 | Add subscription checkout, trial state, cancellation, and usage limits. |
| 9 | Add admin-configurable playbooks, error handling, logging, and model-cost controls. |
| 10 | Complete privacy policy, terms, DPA language, deletion/export, and disclaimers. |
| 11 | Usability test with 5 agents; fix comprehension and workflow defects. |
| 12 | Load test, security review, prompt-injection tests, and backup restoration test. |
| 13 | Close beta with 10 target users; run live onboarding sessions and collect outcomes. |
| 14 | Fix launch blockers, publish, charge beta customers, and establish support/metrics dashboards. |

**Definition of shipped:** a user can create a profile, run one real workflow, inspect grounded inputs, edit an output, save/export it, receive useful practice feedback, and subscribe.

## 5. 30-day marketing calendar

**Budget cap:** $200, leaving a $100 contingency reserve within the $300 limit.

| Day/channel | Action | Budget |
|---|---|---:|
| 1–3 | Launch landing page with one workflow and transparent price | $0 |
| 4 | Post a before/after listing workflow in three real-estate groups | $0 |
| 5 | Send five personalized audit invitations | $0 |
| 6 | Publish “10 listing objections agents still mishandle” | $0 |
| 7 | Host a 30-minute live workflow teardown | $0 |
| 8 | Ask beta users for one recorded workflow result | $0 |
| 9 | Publish a case study with baseline and measured time saved | $0 |
| 10 | Send a no-pitch follow-up to every engaged prospect | $0 |
| 11 | Partner with one real-estate coach or trainer | $0 |
| 12 | Post a short client-objection drill demo | $0 |
| 13 | Create a searchable comparison against generic ChatGPT | $0 |
| 14 | Review activation and pricing objections; update page | $0 |
| 15 | Run a $75 creator sponsorship test with one niche newsletter | $75 |
| 16 | Personally onboard every trial | $0 |
| 17 | Publish three prompts users can copy today | $0 |
| 18 | Contact five brokerage managers or team leads | $0 |
| 19 | Add the strongest measured outcome to the homepage | $0 |
| 20 | Run a second live teardown using user-submitted material | $0 |
| 21 | Request referrals and testimonials from paid users | $0 |
| 22 | Publish a fair-use and data-safety guide | $0 |
| 23 | Review weekly retention and interview one churned user | $0 |
| 24 | Offer a time-limited 14-day team trial, not a permanent discount | $0 |
| 25 | Publish a manager scorecard demo | $0 |
| 26 | Close five personalized high-value prospects | $0 |
| 27 | Run onboarding and pricing calls for warm leads | $0 |
| 28 | Decide whether to continue, narrow, or kill from cohort data | $0 |
| 29 | Ship one blocker fix based on customer evidence | $0 |
| 30 | Review MRR, retention, usage, support burden, and next bet | $0 |

**Marketing KPIs:** qualified landing-page visits, interviews, activated trials, paid conversions, week-4 retention, minutes saved, and qualified opportunities generated.

## 6. Unit economics to $10K MRR

### Proposed pricing

- Solo: **$49/month**
- Pro: **$99/month**
- small team: **$199/month for 5 seats**

### Base-case model

| Metric | Assumption |
|---|---:|
| Average realized ARPU | $72/month |
| Customers needed for $10K MRR | 139 |
| Gross margin target | 80% |
| Revenue/customer at target | $72 |
| Model/inference cost/customer/month | $10–14 |
| Payment, support, and infrastructure allocation | $4–6 |
| Contribution/customer/month | approximately $52–58 |

At 85% gross margin, **$10K revenue requires about $11.8K in monthly variable cost capacity**. This is plausible only with usage limits, efficient caching, model routing, and low-touch support.

### Acquisition economics

Assume:

- blended CAC: $250;
- monthly gross contribution: $55;
- simple CAC payback: 4.5 months;
- monthly logo churn: 5%;
- average lifetime: 20 months;
- LTV:CAC: 20 × $55 / $250 = **4.4:1**.

At the target, acquire approximately 7–10 net new customers each month once the funnel is proven. Do not assume the $200 marketing test will scale acquisition; founder-led sales, partnerships, and organic workflow content must carry most growth.

## 7. Kill criteria

Kill or materially re-niche if any of the following occurs by Day 30:

- fewer than 15 target agents complete discovery;
- fewer than 10 activate the product;
- fewer than 5 pay;
- fewer than 3 retain through week 4;
- median identified time saving is below two hours per month;
- users mostly ask for a generic chatbot rather than the narrow workflow;
- grounded/source controls are ignored and hallucinations create trust concerns;
- customer acquisition cost exceeds $400 before any credible path to improvement;
- fair-housing, privacy, or brokerage-policy review identifies unresolved high-risk behavior;
- contribution margin falls below 70% at intended usage.

## Wedge (required for GO_NARROW)

**Refuse to build:**

- every real-estate role or jurisdiction;
- brokerage-wide CRM replacement;
- automated prospect outreach;
- lead scoring without verifiable data;
- CMA valuation or pricing recommendations;
- legal, lending, tax, or investment guidance;
- a generic ChatGPT wrapper;
- replacement of human coaching;
- broad vertical expansion before at least three retained paying teams.

The MVP serves **individual residential agents doing listing and prospect preparation**, uses **one profession and one workflow system**, and refuses all general-purpose brokerage automation.
