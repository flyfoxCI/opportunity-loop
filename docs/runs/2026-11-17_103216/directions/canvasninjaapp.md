# CanvasNinja — Course Canvas Production Copilot

**Tier:** GO  
**Demand:** 4/5  
**Competition:** 2/5  
**Target:** $10,000 MRR  
**MVP:** 14 days, solo  
**Marketing budget:** ≤ $300 for 30 days  

## 1. Why this direction

### TrustMRR evidence

- CanvasNinja reports approximately **$18.80 MRR**, **$20.84 in last-30-day revenue**, and **123 subscribers**.
- The subscriber count is large relative to paid MRR, suggesting a meaningful top-of-funnel audience but an unresolved conversion problem.
- The apparent workflow addresses creation of course or training canvases, a recurring production task for small course creators and agencies.
- The low MRR means the evidence supports exploration, not a confident forecast.
- The opportunity is to make one deliverable exceptionally fast: transform a rough outline or source document into a polished, editable course canvas.

### X/web evidence

- No X handle was supplied.
- The TinyFish result bodies were unavailable, so there is no defensible quote or engagement count to report.
- Public demand is inferred from the 123 subscribers, the recurring production workflow, and the availability of adjacent design tools.
- The central validation assumption is that course creators and small education agencies repeatedly create promotional, lesson, or module canvases and value speed more than unlimited layout control.

### Thesis

Build a **course-canvas production copilot** for one workflow:

> Give the tool an outline, lesson text, PDF, or brief; receive a polished visual canvas with editable text, images, structure, and export options.

The first release should not compete with Canva, Figma, or a full course-platform authoring system. It should win on one repeatable output: **course-ready promotional or lesson canvases from source content**.

### Initial ICP

- Solo course creators producing weekly social or lesson assets.
- Small course-production agencies that need fast first drafts for clients.
- Start with **solo course creators in one niche**, such as software education or creator education.
- Exclude enterprise instructional-design teams in the MVP.

### Validation questions

1. Is the painful output a promotional canvas, lesson summary, lead magnet, or course thumbnail?
2. Which source material do creators already have?
3. How much editing is required before publication?
4. Do creators buy templates, outsource, or accept AI design?
5. Which deliverable can be produced in 14 days without becoming a general design suite?

## 2. Competitor table

### L1 — direct alternatives

| competitor | likely offer/pricing | strength | weakness / opening | evidence confidence |
|---|---|---|---|---|
| CanvasNinja | Course/canvas-focused creation product; approximately $19 MRR and 123 subscribers | Existing audience and category focus | Opportunity to specialize by output and guarantee rapid editable drafts | High for metrics; medium for exact feature set |
| Canva | General design platform with free and paid tiers | Massive template library, brand controls, broad familiarity | General-purpose workflow; users must design the course asset themselves | High |
| Adobe Express | General content creation suite | Brand ecosystem and polished templates | General-purpose and heavier for rapid course asset production | High |
| Figma | Collaborative design canvas | Flexible, powerful, reusable components | Requires design skill and manual layout; not optimized for source-to-course output | High |
| Beautiful.ai | Presentation and design automation | Smart layout assistance | Presentation-centric rather than course-workflow-specific | High |
| Gamma | Presentations and documents from prompts | Fast generation and attractive layouts | Presentation/document output rather than editable course-canvas production | High |

### L2 — adjacent substitutes

| substitute | why buyers use it | opportunity |
|---|---|---|
| Canva templates | Start from a familiar layout | Templates do not transform source content into a finished canvas |
| AI presentation tools | Generate slides quickly | Often unsuitable for isolated course/social assets |
| Freelance designer | Produce polished custom creative | Higher cost and turnaround time |
| Figma plugin/template workflow | Reuse a creator’s design system | Setup and operational overhead |

### L3 — low-end alternatives

| alternative | weakness |
|---|---|
| PowerPoint / Google Slides | Familiar but slow for repeated branded course assets |
| Prompting a general image model | Inconsistent typography, editability, and dimensions |
| Copy-pasting into a blank Canva project | Manual assembly and no content transformation |

### Competition conclusion

**Score: 2/5.** General design platforms are major incumbents, but the direct niche of **source content → editable course canvas → creator export** can be specialized. The MVP must produce a finished artifact quickly and avoid pretending to replace a full design suite.

## 3. PRD MVP

### Target outcome

A course creator uploads or pastes structured content and receives a polished, editable course canvas generated from a chosen template.

### P0 — required for launch

### Inputs

- Course title and audience.
- Content type:
  - lesson summary;
  - promotional carousel;
  - module overview;
  - course thumbnail.
- Source:
  - pasted text;
  - markdown;
  - PDF text extraction.
- Brand inputs:
  - one logo;
  - two brand colors;
  - one optional font pairing.
- Optional target channel:
  - Instagram carousel;
  - LinkedIn document;
  - presentation;
  - generic course module.

### Outputs

- Editable canvas with text blocks, image placeholders, and consistent spacing.
- One-click text regeneration for selected blocks.
- Three template families appropriate to course creators.
- Brand-kit application.
- Export:
  - PNG for generic canvases;
  - PDF for print;
  - PNG slides/PDF for presentation mode.
- Autosave versions with undo.
- Source content linked to each generated text block.
- Account, usage limits, and Stripe billing.
- Downloadable source file where technically practical, but not a blocking requirement.
- Analytics for project start, generation, edit, export, repeat project, and upgrade.

### P1 — after validation

- Brand-kit save and reuse.
- Bulk generation for a lesson series.
- Canva-compatible import/export workflow.
- Team templates and approval status.
- Image-generation integration for decorative visuals.
- Reuse characters across a course series.

### P2 — later expansion

- Full course-builder integration.
- Interactive course blocks and quizzes.
- Marketplace of creator templates.
- White-label output for agencies.
- Automated brand compliance checks.

### Non-goals

- No pixel-perfect clone of Canva or Figma.
- No general graphic editor in the MVP.
- No marketplace, comments, or collaborative infrastructure at launch.
- No AI-generated video.
- No full LMS/course hosting.
- No promise of print-perfect exports.
- No agency workflow features until individual creators validate retention.

### MVP user story

> As a solo course creator, I can turn a lesson outline into an editable, branded course canvas in minutes so that I can publish consistent assets without manually rebuilding every layout.

### Technical approach

- Front end: React/Next.js canvas editor with a restricted, template-driven node model.
- Rendering: HTML/SVG or canvas rendering with deterministic layout templates.
- Generation: structured content transformation with a language model.
- Source ingestion: plain text, Markdown, and PDF text extraction only.
- Storage: PostgreSQL plus object storage for exports.
- Editor: allow text editing, image replacement, reorder within predefined sections, color/font application, and undo.
- Export service: server-side rendering to PNG/PDF.
- Billing: Stripe with project quotas.
- Safety: sanitize uploaded PDFs and images; do not execute embedded instructions from source files.

### Pricing hypothesis

- **Free:** 2 projects/month.
- **Creator:** $19/month, 30 projects, brands, exports.
- **Pro:** $49/month, 150 projects, bulk series generation, priority rendering.
- **Agency pilot:** $99/month, five client brand kits and reusable templates.

## 4. 14-day day-by-day build plan

| Day | objective | deliverables | acceptance test |
|---:|---|---|---|
| 1 | Choose output | Select course lesson-summary canvas; interview 10 creators | 5 confirm weekly use and 3 will supply source material |
| 2 | Prototype | Build one static template and clickable editing flow | A creator can generate and edit a complete example in 10 minutes |
| 3 | Competitor samples | Create Canva/Gamma comparison samples | Output is materially faster while remaining editable |
| 4 | Template engine | Build one responsive template with tokenized text/image blocks | Template renders correctly at three aspect ratios |
| 5 | Content model | Normalize title, audience, sections, bullets, CTA, and image needs | 20 varied source samples produce valid structures |
| 6 | Generation | Structured source-to-canvas-content generation | 90% of blocks pass simple quality checks |
| 7 | Brand kit | Upload logo, pick colors, set typography | Brand application survives regeneration |
| 8 | Editor | Edit text, replace image, undo, autosave, versions | User can make common corrections without support |
| 9 | Export | Render PNG and PDF; add download state | Export dimensions and typography are correct |
| 10 | Account and billing | Authentication, quotas, Stripe checkout, webhooks | Payment unlocks limits and cancellation is handled |
| 11 | Reliability | Queue rendering, retries, sanitization, error states | Failed jobs recover and source content cannot inject commands |
| 12 | Pilot | Give 10 creators free projects and observe | 7 generate, 5 export, 3 request paid access |
| 13 | Improve UX | Fix top three abandonment points and add templates | 70% complete without help |
| 14 | Release | Deploy, publish gallery, record demo, onboard pilots | 99% export success and 3 paid conversions available |

### Solo-build controls

- Build only two output types: lesson summary and promotional carousel.
- Use fixed templates rather than a freeform editor.
- Do not support PDF upload until day 6.
- Do not build image generation; use image placeholders and uploads.
- Use manual export rendering if a full editor becomes too costly.

## 5. 30-day marketing calendar

### Budget

| channel | 30-day spend |
|---|---:|
| Creator micro-sponsorships | $120 |
| Search-intent content and one boost | $60 |
| Demo/production tools | $20 |
| User incentives | $100 |
| **Total** | **$300** |

### Calendar

| day | activity | organic action | paid action | KPI |
|---:|---|---|---:|---|
| 1 | Launch | Publish homepage and 20-sample gallery | None | 200 qualified visits |
| 2 | Founder post | “I made 10 course canvases in 20 minutes” | None | 15 comments |
| 3 | User outreach | Contact 20 solo course creators | None | 6 interviews |
| 4 | Template post | Publish one niche-specific lesson template | None | 30 template opens |
| 5 | Demo video | Publish source-to-canvas workflow | None | 20% project-start rate |
| 6 | Free project | Offer free lesson-summary canvas | None | 15 projects |
| 7 | Review | Fix first-generation quality issues | None | 60% export rate |
| 8 | SEO page | Publish “Canva alternative for course creators” | None | 30 visits |
| 9 | Creator outreach | Seed tool with 10 micro-creators | None | 3 posts |
| 10 | Agency outreach | Pitch 10 course-production agencies | None | 2 calls |
| 11 | Before/after | Publish time-saved case study | None | 4 trials |
| 12 | User calls | Interview five active creators | None | 5 completed interviews |
| 13 | Iteration | Improve text blocks and image replacement | None | 70% satisfaction |
| 14 | Pricing | Add $19/$49 plans and annual option | None | 8% checkout start |
| 15 | Weekly asset | Publish 7-day course-content workflow | None | 20 saves |
| 16 | Paid creator | Promote demo to course-creator audience | $60 | CAC below $30 |
| 17 | Live build | Build a course canvas live | None | 15 registrants |
| 18 | Series feature | Release consistent-series template | None | 20 repeat projects |
| 19 | Review | Analyze conversion by output type | None | Identify best template |
| 20 | Partnership | Reach newsletter authors and educators | $20 | 1 collaboration |
| 21 | Referral | Ask creators to refer one peer | $25 | 5 referrals |
| 22 | Brand content | Publish brand-kit consistency guide | None | 10 brand-kit setups |
| 23 | Founder post | Explain why the tool is not another Canva | None | 8 sales conversations |
| 24 | Paid retarget | Retarget sample-page visitors | $15 | 3 trials |
| 25 | Retention | Review second-project rate | None | 40% repeat within 14 days |
| 26 | Upgrade prompt | Offer series generation upgrade | None | 3 conversions |
| 27 | Customer proof | Publish creator testimonial and result | None | 5 checkout starts |
| 28 | Channel review | Stop weak paid sources | None | CAC below $30 |
| 29 | Automation | Send project reminder and series prompt | None | 30% open rate |
| 30 | Monthly review | Reconcile MRR, churn, export failures, and CAC | $0 | 15 paid accounts or pivot |

### Organic-first content pillars

- Course-creator speed workflows.
- Before/after canvas examples.
- Brand-consistency education.
- Template galleries by niche.
- Founder build-in-public posts.
- Comparisons with Canva, Gamma, and Figma for one specific output.

## 6. Unit economics to $10K MRR

### Target mix

| plan | price | customers | MRR |
|---|---:|---:|---:|
| Creator | $19 | 180 | $3,420 |
| Pro | $49 | 100 | $4,900 |
| Agency | $99 | 17 | $1,683 |
| **Total** |  | **297** | **$10,003** |

### Cost model

Assumptions:

- Generation and rendering cost: **$0.55/project**.
- Average projects per account per month: **12**.
- Storage, export, payment, and infrastructure: **4% of revenue**.
- Support allowance: **$3/account/month**.
- Fixed solo operating cost: **$1,300/month**.

At 297 accounts:

- Revenue: approximately **$10,003/month**.
- Generation/rendering: approximately **$1,960/month**.
- Storage/payment/infrastructure: approximately **$400/month**.
- Support: approximately **$891/month**.
- Contribution before fixed cost: approximately **$6,752/month**.
- After fixed cost: approximately **$5,452/month** before taxes and founder compensation.

### CAC and payback assumptions

- Blended CAC target: **≤ $30**.
- At $19/month and 12 projects, estimated direct variable cost is:
  - $6.60 generation/rendering;
  - roughly $0.76 infrastructure;
  - $3 support;
  - approximately $8.64 contribution before fixed cost.
- The $19 tier therefore has limited room for paid acquisition; creators may need to be acquired through templates, search, referrals, or annual plans.
- Higher-value Pro and Agency users should support the blended target.

### Sensitivity

- 204 customers at $49 produce approximately $10K MRR.
- 180 Creator accounts alone produce only $3,420 MRR, so the mix must not over-rely on the lowest tier.
- If average projects rise to 25 per account, rendering costs can exceed $4,000/month; caching, model routing, and quotas are mandatory.

## 7. Kill criteria

Pause or kill if:

1. Fewer than 4 of 10 interviewed creators perform this workflow at least weekly.
2. No one completes a paid pilot after receiving a customized canvas.
3. More than 40% of users consider the output too close to a generic template.
4. Median generation-plus-edit time exceeds 15 minutes without human help.
5. Export failure exceeds 2%.
6. After 30 days, fewer than 5 paid accounts or fewer than 15 completed exports from activated users.
7. Blended CAC exceeds $30 for Creator or $80 for Pro without sufficient gross profit.
8. Users demand full Canva/Figma parity before paying.
9. Monthly churn exceeds 12%.
10. The product requires broad template or editing scope that exceeds a two-week solo build.
