# Direction: magicslides-app — Deck-Only for Indie Consultants

**Tier:** GO_NARROW
**Slug:** magicslides-app
**TrustMRR evidence:** MagicSlides.app, $114 MRR, $103 last30, 827 subs, @indianappguy, https://www.magicslides.app
**Demand / Competition (heuristic, not X-verified):** 4 / 2

## 1. Why this direction

**TrustMRR evidence:**
- $114 MRR with 827 subs = ~$1.38 ARPU = heavily monthly-plan mix, or freemium with small % paid
- Wait — 827 subs × $114/827 = $0.14 ARPU means most subs are free tier → $114 MRR comes from a small converting slice → real paying users likely <100
- BUT: 827 total users is a real audience signal → product-market-fit hypothesis worth testing
- Founder @indianappguy known for shipping, audience leverage is real

**Prior validated evidence:**
- From `vibecheck/` and prior research: deck-generation tools (Gamma, Beautiful.ai, Pitch, Canva) are crowded
- But "deck for client deliverables" specifically is underserved — consultants complain about spending hours on decks, not pitch decks

**Wedge rationale (GO_NARROW justification):**
Full slide-deck market has Gamma at $96M C-round valuation, Beautiful.ai, Canva, Pitch, SlidesAI, etc. Pure GO would be suicide. The narrow wedge:
- **One use case:** client-deliverable decks (status updates, audit reports, strategy recaps)
- **One ICP:** indie management/IT/marketing consultants billing $100-300/hr
- **One input:** project notes + previous deck template
- **Refuse:** pitch decks (Gamma), sales decks (Pitch), educational decks (Canva)

## 2. Competitor table

| Tier | Competitor | What they do | Pricing | Why we don't collide |
|---|---|---|---|---|
| L1 direct | Gamma | One-prompt → full deck | $8-16/mo | Pitch-deck focus, not client deliverables |
| L1 direct | Beautiful.ai | AI design assistant | $12-25/mo | General, expensive for solo consultants |
| L1 direct | Pitch | Modern PowerPoint | Free-$16/mo | Generic, requires user to design |
| L1 direct | SlidesAI | Google Slides AI add-on | $4-20/mo | Text-to-slides only, ugly defaults |
| L2 adjacent | Canva | General design | $0-15/mo | Too broad, learning curve |
| L2 adjacent | PowerPoint Designer | Microsoft AI | Free with M365 | Default for corporates, weak AI |
| L2 adjacent | Tome | AI storytelling decks | $16/mo | Pitch-deck focus, low traction |
| L3 distant | ChatGPT + slides DIY | DIY workflow | $20/mo | Time = money for consultants |

**Competition score: 2 in our narrow wedge.** No one targets "consultant client deliverable" specifically. Gamma and Tome are pitch-deck focused. Consultants are an underserved ICP.

## 3. PRD MVP

### User story
As an indie management consultant, I want to paste my meeting notes + select a previous client template → get a 10-slide client deliverable deck with my branding, ready to send, in 5 minutes.

### Epic E1: Note-to-outline (P0)
- Paste meeting notes / project status doc
- AI extracts: 5-7 key points, 3 data callouts, recommended structure
- User confirms/edits outline

### Epic E2: Template picker (P0)
- 3 starter templates: "Project Status Update", "Audit Findings", "Strategy Recap"
- Each template has slide-by-slide blueprint

### Epic E3: Deck generation (P0)
- 10-slide deck: Title, Context, Findings (3), Analysis (2), Recommendations (2), Next Steps
- Each slide: title, 3 bullets, optional chart/table placeholder

### Epic E4: Brand kit (P0)
- Upload logo + 1 brand color + 1 accent color
- Apply to deck automatically

### Epic E5: Export (P0)
- PPTX export (consultants live in PPTX, not Google Slides)
- PDF export

### Epic E6: Project history (P1)
- Save decks per client
- Re-use templates from past decks

### Non-goals (P2 / OUT)
- ❌ Pitch decks — different audience, defer
- ❌ Sales decks — defer
- ❌ Educational decks — defer
- ❌ Real-time collaboration — defer
- ❌ Speaker notes generation — P2
- ❌ AI image generation for slides — defer, use stock
- ❌ Video / animation — defer
- ❌ Google Slides export — P2 (PPTX first)

### Tech stack
- Frontend: Next.js + Tailwind
- Backend: Supabase
- PPTX gen: python-pptx via Next.js API route (or dedicated Python service on Railway)
- AI: OpenAI gpt-4o for outline reasoning
- Payments: Stripe
- File storage: Supabase storage

### Data model
