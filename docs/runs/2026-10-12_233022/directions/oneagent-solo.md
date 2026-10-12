# Direction — `oneagent-solo` (GO_NARROW unbundle of `agenkit`)

> **UNBUNDLE** of AgenKit ($4 MRR, $48 last30, 120 subs · demand 4 / comp 4).
> **Tier:** **GO_NARROW** (competition 4 — must hold the wedge).
> **MVP 14 days · solo · $300 / 30d marketing**

---

## 1. Why this direction

**TrustMRR evidence**
- AgenKit has unusually high `last30` ($48) vs MRR ($4), meaning real trials convert (or attrition is high); 120 subs at near-zero MRR means **demand exists but the product pricing/monetization is broken**.
- Pattern matched: "builders want AI agents, will sign up, but balk at paying". **The wedge:** shrink the product surface until $29/mo is a no-brainer.

**Web / cultural evidence**
- AI-agent builders exploded 2024–2025: n8n, Lindy, Relevance, Voiceflow, Botpress, CrewAI, AutoGen, Flowise, LangGraph, GPT-tutored chatbots.
- All have grown enterprise / mid-market segments; **small-business / solopreneur segment is underserved.** Lindy is closest but starts at $49/mo and configures 30+ triggers.
- Reddit r/AutoGenAI, r/AI_Agents, r/LangChain — perpetual "what should I use?" threads. The honest answer: for solopreneurs, **the right answer is fewer features, not more**.

**Why the wedge works (must hold!)**
- **One agent per site.** Not five. Not a builder. One.
- **No vector DB.** No retrieval infrastructure. Just instructions + tools.
- **Setup < 30 minutes** start to finish.
- **$29/mo, transparent pricing.** No "usage" surprises.
- **Tool list capped at 8 well-known tools** (Calendly, Stripe, Notion, Email, Slack, HubSpot, Google Calendar, Webflow). Not 80.

If we deviate from this wedge, we lose. We are the opposite of n8n, not its cousin.

---

## 2. Competitor table (L1 / L2 / L3)

| Tier | Competitor | Pricing | Why they lose |
|---|---|---|---|
| L1 direct | **Lindy.ai** | $49+ | Two-three most-popular agent build, but configurable labor. |
| L1 direct | **Voiceflow** | $15–250/mo | Indie but heavily dev-flavored. |
| L1 direct | **n8n Cloud** | $24+/mo | Power-user, requires workflow / JSON. |
| L1 direct | **Relevance AI** | $49+/mo | Teams, $299 recommended. |
| L1 direct | **Botpress** | $65+/mo | Developer-leaning. |
| L1 direct | **AgenKit** | $X/early | In early monetization. |
| L2 adjacent | **ChatGPT custom GPTs** | $20/mo Plus | No external API / tool execution. |
| L2 adjacent | **Tidio AI** | $29+/mo | Ecom-first; overcomplicated. |
| L3 substitute | **Hire a VA** | $400+/mo | Latency, training. |
| L3 substitute | **DIY with LangGraph + Next.js** | $20–200/mo in LLM cost | Dev time cost. |

**Score:** competition = **4**. Comp is high. Hence GO_NARROW — we win only by holding the **solopreneur + one-agent + 30-min-setup** wedge.

---

## 3. PRD MVP (P0 / P1 / P2 + non-goals)

### P0 — must ship day 14
- **One agent per site.** Plan = "Sales qualifier / Support / Lead-form / Booking".
- **Setup wizard (<30 min):** instructions box, tool picker (capped at 8), knowledge-paste (plain text), color, system-prompt tester.
- **Embed:** drop-in script snippet OR popup modal OR full-page takeover.
- **Calendly integration** (native for booking).
- **Stripe integration** (collect $ on the spot).
- **Plain-text knowledge** for retrieval (no vector DB — embed at query time).
- **Email handoff** (forward to a help@ address).
- **Usage:** 1,000 messages/mo on $29 plan, 5,000 on $99 plan.
- **Pricing:**
  - Free: 100 messages/mo, watermark "made with OneAgent".
  - **Solo: $29/mo** — 1,000 messages.
  - **Solo+: $99/mo** — 5,000 messages + custom domain + CSV export.

### P1 — month 2
- **Zapier tool** (replaces 7 of 8 native tools with 1,000+ apps).
- Slack alert on new leads.
- Webhook out (push to a CRM).

### P2 — month 3+
- **Multi-agent** in a 2-flow chain (extraction → outreach). Pro plan only.
- **Voice mode** (Vapi / ElevenLabs) — bump to $149/mo.
- **Slackbot instead of chat-on-website.**

### Non-goals (DO NOT BUILD — wedge!)
- **No vector DB / RAG.** Plain-text retrieval only. (This is the wedge — DO NOT generalize.)
- **No multi-agent orchestration.** One agent.
- **No React Flow drag-drop builder.** Settings form only.
- **No "training" of LLMs.** Just prompt engineering.
- **No phone / voice in MVP.** It's a worse wedge.
- **No agency / white-label tier.** Studio tier reserved for month 6.

### Tech stack
- Next.js 14 + Tailwind.
- Convex (db, real-time updates).
- OpenAI Assistants API (plain-text retrieval, thread mgmt).
- Stripe.
- Cloudflare Workers for embed snippet.

---

## 4. 14-day day-by-day build plan

| Day | Goal | Output |
|---|---|---|
| **D1 Mon** | Repo scaffold + auth + Convex schema (agent, message, plan). | Auth live. |
| **D2 Tue** | Setup wizard: instructions, tool picker (8), knowledge-paste. | Wizard works. |
| **D3 Wed** | Embed snippet (Cloudflare Worker) + chat UI on test domain. | Chat visible. |
| **D4 Thu** | OpenAI Assistants integration (one thread per visitor). | Replies work. |
| **D5 Fri** | Calendly + Stripe integrations (button trigger). | Calendar + payment. |
| **D6 Sat** | Plain-text knowledge (pre-processed retrieval) — **NOT vector DB**. | Knowledge works. |
| **D7 Sun** | Email handoff + watermark logic. | Watermarked free plan. |
| **D8 Mon** | Stripe + quota gates. | Paywall live. |
| **D9 Tue** | Usage dashboard + CSV export for Pro. | Dashboard. |
| **D10 Wed** | Polish, mobile responsive, empty states. | Demo-ready. |
| **D11 Thu** | Beta with 8 indie hackers. | 8 installs. |
| **D12 Fri** | Bug bash + speed pass. | Stable. |
| **D13 Sat** | Landing page v2 + demo GIF. | Public landing. |
| **D14 Sun** | **Launch on X + IndieHackers.** | Live. |

**DoD:** 1 agent, 8 tools, plain-text retrieval only, embed snippet works in < 5 lines, payment verified, < 4 sec reply time at p95.

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Day | Channel | Action | Cost |
|---|---|---|---|
| D1 | X | Build @oneagentsolo handle; first thread on "I want to make AI agents feel small". | $0 |
| D3 | IndieHackers | "What do you wish AI agents did, that they don't?" (lead post). | $0 |
| D5 | Reddit | Lurk + reply in r/AutoGenAI, r/SaaS. | $0 |
| D7 | IndieHackers | Build log #1. | $0 |
| D10 | X | Demo GIF: "Setup to live agent in 25 minutes." | $0 |
| D12 | Reddit | Cross-post in r/SaaS, r/sidehustle. | $0 |
| D14 | X | Thread: "I refused to add a vector DB to my AI agent product. Here's why." — wedge narrative. | $0 |
| D15 | ProductHunt | Launch (Tue). | $0 |
| D18 | IndieHackers | Lead-magnet post: "One-agent template (instructions + 8 tools)." | $0 |
| D21 | SEO | Publish 3 SEO pages: "one page ai agent", "calendly ai assistant", "stripe ai chatbot". | $0 |
| D24 | Reddit | AMA in r/AutoGenAI. | $0 |
| D27 | X | Customer screenshot + mini-interview. | $0 |
| D30 | Lifecycle | Re-engagement email to free users who hit 100-msg cap. | $0 |

**Paid budget:** **Default $0.** If organic stalls, allocate $200 to X ads targeted at IndieHackers audience, $100 to AI-tools newsletter sponsorship.

**KPIs**
- Time-to-live-agent < 30 min.
- Setup completion rate ≥ 60%.
- Free→paid ≥ 4%.
- MRR by D30: ~$300–600.

---

## 6. Unit economics to $10K MRR

| Variable | Value | Source |
|---|---|---|
| ARPU (blend) | $36/mo | 70% Solo $29 + 25% Solo+ $99 + 5% free → $36 blended. |
| Gross margin | 60% | OpenAI ~$0.05/thread, Convex, Stripe 2.9%. Heavy OpenAI costs. |
| Monthly churn | 5% | Solopreneurs churn but volume is high. |
| Paid users needed for $10K MRR | ~278 | $10,000 / $36 ≈ 278. |
| New paid / month needed | ~17 | 278 × 5% ≈ 14/mo. |

**Path to $10K MRR (12 mo)**
| Month | Paid | New | Churn | Paid | MRR |
|---|---:|---:|---:|---:|---:|
| 1 | 20 | 20 | 1 | 39 | $1,404 |
| 3 | 90 | 50 | 5% | 138 | $4,968 |
| 6 | 220 | 60 | 5% | 277 | $9,972 |
| 9 | 360 | 70 | 5% | 427 | $15,372 |

> $10K MRR achievable by **month 6**.

**Break-even:** ~25 paid = $900/mo (OpenAI costs are real).

---

## 7. Kill criteria (hard)

- **Setup completion < 40%** after 100 starts → wizard is broken.
- **Free→paid < 2% by D30** → wedge positioning wrong.
- **Reply latency p95 > 8 sec** → unacceptable; cut to GPT-4o-mini or pre-canned.
- **OpenAI costs > 60% of revenue** by month 2 → shift to pre-canned templates + light GPT.
- **< 30 paying users by D60** despite 1000+ free starts → wedge is not holding; abandon.
- **Any competitor launch** that does exactly "one agent, plain text, $29/mo, 8 tools" within 30 days → wedge is now public, reposition.

---

## 8. Wedge (required for GO_NARROW)

We refuse to build:

- ❌ **Vector DBs.** Plain-text retrieval only. (The biggest wedge.)
- ❌ **React Flow / drag-drop builder.** Settings form. (Easier = higher conversion.)
- ❌ **Multi-agent orchestration.** One agent per site only.
- ❌ **Custom workflow / trigger logic beyond "user sends a message".**
- ❌ **Phone / voice integration.** In-person UX damage too high at this stage.
- ❌ **White-label / agency tier.** It's the right product, just for *next* product.
- ❌ **Open-ended "tools marketplace".** Hard cap at 8 carefully chosen integrations.
- ❌ **Self-serve RAG uploads (PDFs / docs).** That's the trap. Plain text or nothing.
- ❌ **Custom fine-tuning.** Prompt engineering only.
- ❌ **Anything that reverts us to "we're a smaller n8n."**

If a request, customer feedback, or investor pattern suggests any of the above, the right answer is to **add the wedge to a list of future-product ideas** — not to ship them.

The wedge is **one agent, one site, plain text, 8 tools, 30-minute setup, $29/mo.** Hold it for 6 months minimum before extending.
