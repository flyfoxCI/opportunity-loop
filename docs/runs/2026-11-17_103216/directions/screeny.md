# Screeny — Interactive Product Demos for One Onboarding Workflow

**Tier:** GO_NARROW  
**Demand:** 4/5  
**Competition:** 4/5  
**Target:** $10,000 MRR  
**MVP:** 14 days, solo  
**Marketing budget:** ≤ $300 for 30 days  

## 1. Why this direction

### TrustMRR evidence

- Screeny reports approximately **$4.64 MRR**, **$26.20 in last-30-day revenue**, and **115 subscribers**.
- Last-30 revenue exceeding current MRR may reflect recent conversions, prepaid billing, or reporting timing; the net result needs validation.
- The subscriber base suggests interest in turning product screenshots or walkthroughs into polished demos.
- The apparent opportunity is stronger for user onboarding, support, and sales enablement than for general mockup creation.
- Low MRR means this direction must be validated as a narrow workflow rather than a broad interactive-demo builder.

### X/web evidence

- No X handle was supplied.
- The TinyFish outputs did not include result bodies, so no social quotes or engagement metrics are asserted.
- Demand is inferred from the 115 subscribers and from the recurring need to demonstrate product flows without granting live access.
- User-generated content and creator-tool communities are plausible channels, but direct interviews must establish which workflow has urgency.

### Thesis

Build a tool that turns a sequence of screenshots or a short product walkthrough into a **clickable, shareable onboarding demo**.

The product can:

- import screenshots;
- detect order and group them into steps;
- add clickable hotspots;
- add captions;
- generate a short interactive link;
- provide analytics;
- optionally add a lightweight presenter video.

The wedge should be explicit: **onboarding and product-tour demos for SaaS teams**, excluding open-ended mockup and video creation.

### Initial ICP

- Early-stage SaaS teams that need to onboard users without adding a sales-engineer.
- Customer-success teams that need a reproducible product walkthrough.
- Start with **B2B SaaS onboarding**, not mobile-app games, physical products, or general advertising.

### Validation questions

1. Is the main pain producing a walkthrough, documenting onboarding, or supporting sales?
2. What format do users have today: screenshots, Loom video, or live session?
3. Which step creates the most confusion?
4. Will users share a link, or require custom controls and branding?
5. Why not use a generic video or prototype tool?

## 2. Competitor table

### L1 — direct alternatives

| competitor | likely offer/pricing | strength | weakness / opening | evidence confidence |
|---|---|---|---|---|
| Screeny | Product mockup/demo product with approximately $5 MRR and 115 subscribers | Existing audience and demo focus | Opportunity to specialize in onboarding tours and link-based delivery | High for metrics; medium for exact features |
| StoryboardHero | Video/image messaging and interactive stories | Familiar creator workflow and sharing | More creator-oriented than structured product onboarding | Medium |
| Guidant / Tango | Interactive product tours and process documentation | Strong use-case alignment and established workflows | More complex than a 14-day solo MVP can reproduce broadly | High |
| Navattic | Interactive product tours | Enterprise-ready analytics and design tools | Often too heavy or expensive for a small team | High |
| Storyflow | Guided product tours and onboarding | Polished interactive tours and support workflows | Broad feature set and direct incumbent competition | High |
| Loom / Vimeo | Quick screen recording and video hosting | Extremely easy adoption and recording | Harder to navigate, update, or turn into a clickable product flow | High |

### L2 — adjacent substitutes

| substitute | why buyers use it | opportunity |
|---|---|---|
| Static screenshot carousel | Show steps sequentially | No clickable flow, branching, or update workflow |
| Screen recording | Captures real interaction | Difficult to update, no branch, and no structured hotspots |
| Loom walkthrough | Fast human explanation | Searchability, updates, and self-service interaction are weaker |
| Google Docs/SOP | Document a support workflow | Slower for self-service and less engaging |
| Live demo call | Personal explanation | Expensive and not scalable |

### L3 — low-end alternatives

| alternative | weakness |
|---|---|
| Figma prototype | Requires design and technical skill for each flow |
| Keynote/PowerPoint | Not interactive or embeddable as a product tour |
| Generic no-code prototype | Overpowered for a simple guided walkthrough |

### Competition conclusion

**Score: 4/5.** This is a crowded category with established, well-funded or mature alternatives. It cannot be approved as a full-market GO. A narrow **SaaS onboarding tour generated from screenshots** may work, but only if users prefer it over Loom and existing tour builders and if the MVP avoids general video editing and enterprise controls.

## 3. PRD MVP

### Target outcome

A SaaS product manager uploads a sequence of screenshots and receives a shareable, clickable onboarding tour in one session.

### P0 — required for launch

- Screenshot upload, up to 15 images per tour.
- Automatic chronological ordering.
- Manual reorder.
- Step captions.
- Clickable next/back controls.
- Optional hotspot on the image.
- Intro and end screens.
- Device-width preview.
- Shareable public URL.
- Embed snippet.
- Basic analytics:
  - tour opened;
  - step reached;
  - completion;
  - hotspot clicked.
- Password protection for sensitive flows.
- Authentication, tour limits, Stripe billing.
- Draft and published states.
- Image resizing and compression.
- No need for a general timeline editor in the MVP.

### P1 — after validation

- Screen recording upload and automatic step detection.
- Branching based on user choice.
- Custom branding.
- Lead capture before viewing.
- Text and voiceover additions.
- Reusable product-tour templates.
- Team editing and approvals.

### P2 — later expansion

- Branching logic builder.
- Dynamic data and integrations.
- In-app widget.
- Analytics cohorts and user segmentation.
- Full video editor.
- Enterprise SSO and granular permissions.

### Non-goals

- No full video editor.
- No AI-generated avatars or voice cloning.
- No complex branching in the MVP.
- No native mobile-app prototyping.
- No enterprise integrations.
- No guaranteed conversion lift.
- No broad ad creative or landing-page builder.
- No bidirectional sync with Figma.

### MVP user story

> As a SaaS product manager, I can turn screenshots into a clickable onboarding tour and share it with users so that they can complete setup without booking a live demo.

### Technical approach

- Web app with React front end and lightweight API.
- Image processing: resize, crop, and package assets.
- Ordering: upload timestamp plus manual drag-and-drop.
- Storage: PostgreSQL metadata and object storage for images.
- Tour rendering: server-side HTML or static generated pages for fast sharing.
- Analytics: first-party event endpoint and simple dashboard.
- Billing: Stripe with published-tour limits.
- Security: signed image URLs, optional password, rate limiting, and no script execution from uploaded content.

### Pricing hypothesis

- **Free:** 3 published tours.
- **Starter:** $29/month, 20 tours and analytics.
- **Pro:** $79/month, 100 tours, password protection, branding, and removal of Screeny branding.
- **Team:** $149/month, shared editing, approvals, and 500 tours.

## 4. 14-day day-by-day build plan

| Day | objective | deliverables | acceptance test |
|---:|---|---|---|
| 1 | Validate ICP | Select B2B SaaS onboarding; prepare 15-flow interview script | 10 interviews scheduled |
| 2 | Prototype | Build clickable prototype for one screenshot flow | A target user understands and completes the flow |
| 3 | Competitor test | Compare mockups with Loom, Tango, Guidant, and Navattic | One clear advantage and three non-negotiables identified |
| 4 | Import | Multi-image upload, reorder, metadata, thumbnail generation | 15-image tour imports reliably |
| 5 | Viewer | Public tour page, next/back, captions, hotspots | Tour works on mobile and desktop |
| 6 | Publishing | Public IDs, share link, password protection, embed | Links and embeds load and can be revoked |
| 7 | Editor | Draft/publish, title, intro/end, edit steps | User can update a tour in under 10 minutes |
| 8 | Analytics | Event collection and basic completion dashboard | Funnel counts reconcile with manual spot checks |
| 9 | Account and billing | Authentication, ownership, quotas, Stripe | Paid access and cancellation work correctly |
| 10 | Reliability | Image transforms, caching, retries, monitoring | 99% tour-view success |
| 11 | Security | Password hashing, rate limits, signed URLs, upload validation | Unauthorized tours and malicious uploads are rejected |
| 12 | Pilot | Onboard 10 SaaS teams with real onboarding flows | 6 publish tours and 3 share them with users |
| 13 | Pricing and polish | Add plan comparison, onboarding, demo tour | 2 users click paid plan and checkout works |
| 14 | Release | Deploy, publish sample tours, record demo, start outreach | No P0 defects and first paid conversion available |

### Solo-build controls

- Screenshot imports only.
- Linear tours only.
- One rendering path.
- No custom domains or advanced branching.
- Prioritize share speed and analytics.

## 5. 30-day marketing calendar

### Budget

| channel | 30-day spend |
|---|---:|
| Creator/productivity sponsorships | $100 |
| Search-intent content and small boosts | $60 |
| Demo/design tooling | $40 |
| Interview/referral incentives | $100 |
| **Total** | **$300** |

### Calendar

| day | activity | organic action | paid action | KPI |
|---:|---|---|---:|---|
| 1 | Launch | Publish homepage and 10 interactive samples | None | 200 qualified visits |
| 2 | Founder post | “Turn my onboarding docs into a tour” | None | 15 comments |
| 3 | Outreach | Contact 20 SaaS product managers | None | 6 interviews |
| 4 | Free tour | Generate five tours manually | None | 5 published tours |
| 5 | Demo video | Publish 60-second tour creation clip | None | 20% upload-start rate |
| 6 | Comparison | Publish Screeny vs Loom/Tango/Storyflow page | None | 30 visits |
| 7 | Review | Fix import and mobile-viewing friction | None | 70% publish rate |
| 8 | Template | Publish SaaS onboarding template | None | 20 uses |
| 9 | Creator outreach | Seed with 10 productivity creators | None | 3 posts |
| 10 | Partnership | Pitch onboarding agencies and CS teams | None | 2 calls |
| 11 | Case study | Publish time/support-saved result | None | 4 trials |
| 12 | User calls | Interview five trial teams | None | 5 calls |
| 13 | Product iteration | Add captions, hotspots, password protection | None | 70% satisfaction |
| 14 | Pricing test | Add $29/$79/$149 plans | None | 8% checkout start |
| 15 | Educational post | Publish “When to use a tour instead of a Loom” | None | 25 shares |
| 16 | Paid creator | Promote onboarding-tour workflow | $60 | CAC below $40 |
| 17 | Live session | Build an onboarding tour live | None | 10 registrants |
| 18 | Analytics release | Publish completion funnel feature | None | 20 tours viewed |
| 19 | Review | Segment activation by use case | None | Identify best ICP |
| 20 | Agency pilot | Offer white-label pilot to one onboarding agency | $20 | 1 pilot discussion |
| 21 | Referral | Ask teams to refer one peer | $25 | 5 referrals |
| 22 | SEO | Publish interactive onboarding demo examples | None | 20 organic visits |
| 23 | Founder post | Explain why screenshot tours beat generic video | None | 8 sales calls |
| 24 | Paid retarget | Retarget sample visitors | $15 | 3 trials |
| 25 | Retention | Review repeat tour creation/update rate | None | 35% update within 14 days |
| 26 | Upgrade prompt | Prompt password, branding, and analytics upgrade | None | 3 conversions |
| 27 | Customer proof | Publish onboarding-team testimonial | None | 5 checkout starts |
| 28 | Channel review | Pause weak sources | None | CAC below $40 |
| 29 | Automation | Send update suggestion and engagement summary | None | 30% open rate |
| 30 | Monthly review | Reconcile MRR, churn, views, and hosting cost | $0 | 15+ paid accounts or explicit pivot |

### Organic-first content pillars

- Better onboarding through interactive tours.
- Public reusable product tours.
- Comparisons with Loom, Tango, and static docs.
- Founder build-in-public content.
- Templates for common SaaS onboarding flows.
- Analytics and completion-funnel education.

## 6. Unit economics to $10K MRR

### Target mix

| plan | price | customers | MRR |
|---|---:|---:|---:|
| Starter | $29 | 120 | $3,480 |
| Pro | $79 | 70 | $5,530 |
| Team | $149 | 7 | $1,043 |
| **Total** |  | **197** | **$10,053** |

### Cost model

Assumptions:

- Hosting and image bandwidth: **$0.30/tour/month**.
- Average published tours per account: **5**.
- Payment and infrastructure: **4% of revenue**.
- Support allowance: **$4/account/month**.
- Fixed solo operating cost: **$1,300/month**.

At 197 accounts:

- Revenue: approximately **$10,053/month**.
- Hosting/bandwidth: approximately **$296/month**.
- Payment/infrastructure: approximately **$402/month**.
- Support: approximately **$788/month**.
- Contribution before fixed cost: approximately **$8,567/month**.
- After fixed cost: approximately **$7,267/month** before taxes and founder compensation.

### CAC and payback assumptions

- Target blended CAC: **≤ $40**.
- At $29/month:
  - $29 revenue;
  - approximately $1.50 hosting;
  - roughly $1.16 infrastructure;
  - $4 support;
  - approximately $22.34 contribution before fixed cost.
- One-month payback is possible under the target CAC.
- Agency partnerships may lower CAC and raise average price.

### Sensitivity

- 127 customers at $79 produce approximately $10K MRR.
- If the product remains locked in the $29 tier, 347 customers are required.
- View traffic rather than creation may dominate infrastructure cost; optimize image sizes and hotlink/CDN delivery.
- High churn in one-time documentation use would require annual contracts, templates, or a broader recurring use case.

## 7. Kill criteria

Pause or kill if:

1. Fewer than 4 of 10 interviewed SaaS teams regularly create product walkthroughs.
2. Users rate Loom and Google Docs as “good enough” and show no willingness to switch.
3. No one agrees to a paid pilot after seeing a custom tour.
4. Fewer than 10 teams publish a tour during the first 30 days.
5. More than 50% of users need branching, recording, or deep editing immediately, expanding the 14-day scope.
6. Fewer than 5 paid accounts after 30 days.
7. Blended CAC exceeds $40 for Starter or $90 for Pro without sufficient gross profit.
8. Median tour creation exceeds 15 minutes.
9. Monthly churn exceeds 12%.
10. The wedge remains “general product demo” rather than a validated recurring onboarding workflow.

## Wedge (required for GO_NARROW)

### Narrow wedge

The product serves **B2B SaaS onboarding and customer-success walkthroughs**, beginning with screenshot-based, linear product tours. It does not target general advertising, landing pages, app prototypes, or enterprise sales demonstrations.

### What the product refuses to build

- No general video editor.
- No complex branch-and-condition builder at launch.
- No Figma bidirectional sync.
- No native iOS/Android prototyping.
- No enterprise SSO, SCIM, audit logs, or custom integrations.
- No AI avatars or voice cloning.
- No ad creative generation.
- No promise of product analytics or conversion lift beyond basic tour engagement.
- No expansion to general users until onboarding teams show recurring creation and update behavior.

### Explicit expansion condition

Add branching, recording, branding, and team workflows only after at least 25 paid teams publish or update a tour in two consecutive months and identify the next most common bottleneck.
