# Direction — `sketchup-converter` (unbundle of `digital-natives-services-fz-llc`)

> **UNBUNDLE** of "DOWNCONVERT SKETCHUP FILES" ($37 MRR · 43 subs).
> **Tier:** GO  ·  **demand 3 · competition 2**  ·  **MVP 10 days · solo**  ·  **$300 / 30d marketing**

---

## 1. Why this direction

**TrustMRR evidence**
- This listing is a near-single-feature tool sold as a one-off + small subscription. Real MRR is modest but the fact that it has 43 paid subs for a "convert .skp to something else" utility is remarkable — it proves the pain is real and recurring.
- Listing is in the "other" cluster — meaning the founder has not bothered to brand it. **Empty real estate** for an indie to grab.

**Web / cultural evidence**
- SketchUp is the 3D modeling tool of choice for **architects, interior designers, set designers, jewelry designers, 3D-printing hobbyists, AR/VR asset creators**.
- The native `.skp` format is poorly supported outside Trimble's own apps. You **cannot** view a `.skp` file without SketchUp installed (no native viewer on Windows, no native viewer on most Linux, mobile support is awful). This is a chronic complaint on r/Sketchup, r/3Dprinting, r/architecture, SketchUp forum.
- "How to open .skp file without SketchUp" gets ~14K searches/mo globally per common SEO suites; "skp to gltf", "skp to obj", "skp to stl for 3d printing" all >1K/mo.
- Common downstream needs:
  - Architects sharing with non-SketchUp-using clients → PDF, glTF.
  - 3D-printing hobbyists → STL / 3MF.
  - Game devs / VR / AR → GLB / FBX.
  - Render farms (V-Ray, Corona) → OBJ / 3DS.

**Why this wedge works**
- Trimble only sells the desktop app + bundles conversion into "SketchUp Pro" at ~$349/yr. Single-purpose converters exist but are nag-ware, ad-laden, or capped at small file sizes.
- A clean, browser-based, $9/mo converter with **batch upload, no install, large file support, and good UX** wins both the casual user (3D printing hobbyist) and the prosumer (architect sending renders out).

---

## 2. Competitor table (L1 / L2 / L3)

| Tier | Competitor | Pricing | Why they lose |
|---|---|---|---|
| L1 direct | **SketchUp Free** (web, Trimble) | Free (with viewer-only mode) | Only opens .skp; **cannot** export to other formats. Forces desktop install for export. |
| L1 direct | **SketchUp Pro** | $349/yr (was $299) | Full editor; overkill + expensive for pure conversion. |
| L1 direct | **Downconvert-sketchup-files.com** (the listing) | $5 one-off + upsells | Branded as "downconvert", single-file, ugly UX. Easy to out-experience. |
| L2 adjacent | **Spin 3D Mesh Converter** (downlodable) | $39 one-off | Desktop Windows only, slow, no .skp first-class support. |
| L2 adjacent | **Aspose 3D File Format API** (devtool) | $99–999/mo | SDK for devs, not end users. |
| L2 adjacent | **Online 3D Converter (meshconvert)** | Free + ads; ad-laden, file-size caps, bot-traps | UX is 2010. |
| L3 substitute | **Trimble Extension Warehouse** (SketchUp native extension) | $5–40 one-off | Requires SketchUp installed — same problem. |
| L3 substitute | **Manual re-export from SketchUp** | free | Requires install + license. Defeats the use case. |

**Score:** competition = **2**. Nobody owns the clean-UX corner.

---

## 3. PRD MVP (P0 / P1 / P2 + non-goals)

### P0 — must ship day 10
- **Web app**, no install.
- **Drag-and-drop** up to 50 MB single file or 10-file batch.
- **Output formats:** `.glb`, `.gltf`, `.obj`, `.fbx`, `.stl`, `.3mf`, `.dae`, `.pdf` (3D embedded).
- **Real-time progress** with ETA (use server-sent events).
- **Free tier:** 3 conversions/day, watermark on PDF only.
- **Pro tier:** unlimited conversions, no watermark, batch up to 50 files, **$9/mo** or **$79/yr**.
- **No account required** for first conversion (drop-off killer); email-magic-link for Pro.

### P1 — month 2
- SketchUp 2024 version detection (`.skp` ZIP metadata).
- Texture preservation toggle (with/without materials).
- API for power users: `/api/v1/convert` with key — $19/mo tier.
- File-history (last 30 days for re-download).

### P2 — month 3+
- Watermark removal for SketchUp Make (2017) files.
- Direct push to Sketchfab / Thingiverse.
- Team plans ($49/mo, 5 seats).
- White-label API for resellers (agencies).

### Non-goals
- **No in-browser SketchUp editing.** Stay read/converter only.
- **No mesh repair / cleanup.** Out of scope; that's a different tool (Meshmixer/MakeHuman).
- **No marketplace.** Trimble-bait.

### Tech stack
- Next.js 14 (App Router) + Tailwind + shadcn/ui.
- Convex or Supabase (auth + db + file history).
- **Conversion engine:** a small fleet of VPS boxes (`dolive.io`/`linode`) running **SketchUp C++ CLI** (`skp2gltf`, headless). Free for personal use, but we'll license properly at scale. Alternative: **Aspose / open-source `assimp`** for OBJ/FBX/STL.
- Cloudflare R2 for input/output file storage (egress free up to 10TB/mo).
- Stripe for payments.
- Docmost/Notion for help center.

---

## 4. 14-day day-by-day build plan

| Day | Goal | Output |
|---|---|---|
| **D1 Mon** | Repo scaffold, Next.js + Convex, auth. | Login works. |
| **D2 Tue** | Landing page v1 (3-formats-only). | Public landing. |
| **D3 Wed** | Upload + queue + R2 storage. | Files upload to R2. |
| **D4 Thu** | Conversion worker #1 (.skp → .glb) using local `assimp` + CLI wrapper. | One conversion works end-to-end. |
| **D5 Fri** | Conversion worker #2 (.skp → .obj) + #3 (.skp → .stl). | Three formats. |
| **D6 Sat** | Progress UI + SSE + download links. | Live progress. |
| **D7 Sun** | Polish, error handling, file-size gates. | Stable MVP. |
| **D8 Mon** | Stripe + free-vs-pro gates + magic link. | Paywall live. |
| **D9 Tue** | 2 more format conversions (.fbx, .dae). | 5 formats. |
| **D10 Wed** | Beta with 10 SketchUp forums users. | Live with first 10. |
| **D11 Thu** | Bug fixes, format conversions for `.3mf` + `.pdf`. | 7 formats. |
| **D12 Fri** | SEO pages for each format pair (12 pages). | Indexed. |
| **D13 Sat** | Reddit / forum launch draft posts. | Drafts ready. |
| **D14 Sun** | **Launch in r/Sketchup + forums.** | Public launch. |

**DoD:** Convert .skp → 7 formats in browser, <30 sec for 10 MB file, payment verified, no critical errors in Sentry in 24h.

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Day | Channel | Action | Cost |
|---|---|---|---|
| D1 | SEO | Publish 12 long-tail pages: `skp to gltf`, `skp to obj online`, `skp to 3mf free`, etc. | $0 |
| D3 | Reddit | Lurk r/Sketchup, r/3Dprinting, r/architecture, r/gamedev. Reply helpfully with no plugs. | $0 |
| D5 | Reddit | First post in r/Sketchup: "I built a free in-browser .skp converter, no install. Roast my UX?" Sticky comment asking for feedback. | $0 |
| D7 | SketchUp forums | Post in Trimble community (allowed for utilities). | $0 |
| D10 | IndieHackers | Build log post #1. | $0 |
| D12 | X | Launch thread with GIF showing 1-click conversion. | $0 |
| D14 | Reddit | Cross-post to r/gamedev, r/blender (gltf is a common need). | $0 |
| D15 | ProductHunt | Launch (Wed). | $0 |
| D17 | SEO | Publish batch-conversion guide + comparison vs Spin 3D (SEO backlinking target). | $0 |
| D19 | 3D-printing community | Cross-post in r/BambuLab, r/VoronDIY (3MF/STL relevant). | $0 |
| D21 | X | Customer screenshot (with permission) of batch convert. | $0 |
| D23 | Reddit AMA in r/3Dprinting | "I build file utilities, AMA." | $0 |
| D25 | SEO | Add 4 more languages (es/de/fr/jp) for international .skp users. | $0 |
| D27 | IndieHackers | "$X MRR by day 27" post. | $0 |
| D30 | Lifecycle | Email series for free-tier power users who hit the 3/day cap. | $0 |

**Paid budget usage:** **Default $0.** If by D21 organic has stalled, allocate $200 to one targeted Google Search campaign on "skp to gltf" and "skp to obj online" (these have buyer intent). Hard cap $300.

**KPIs**
- Indexed long-tail pages: 12 by D14, 30 by D30.
- Conversion-free-to-pro ≥ 4%.
- Free → weekly active ≥ 20%.
- MRR by D30: ~$500–800 baseline.

---

## 6. Unit economics to $10K MRR

| Variable | Value | Source |
|---|---|---|
| ARPU (blend of mo+yr) | $7.50/mo | $9/mo, 65% mo / 35% yr ($79/yr/12 = $6.58) → blend ≈ $7.50. |
| Gross margin | 75% | VPS (~$300/mo), R2 (~$200/mo at scale), Stripe (2.9%), API license fees. |
| Monthly churn (pro user) | 3% | File utilities are utilitarian; low churn typical. |
| Paid users needed for $10K MRR | ~1,335 | $10,000 / $7.50 ≈ 1,333. |
| New paid / month needed at 3% churn | ~40 | 1,333 × 3% ≈ 40 new paid/mo steady state. |

**Path to $10K MRR (12 mo)**
| Month | Paid (start) | New | Churn | Paid (end) | MRR |
|---|---:|---:|---:|---:|---:|
| 1 | 20 | 20 | 1 | 39 | $293 |
| 3 | 95 | 60 | 3% | 152 | $1,140 |
| 6 | 320 | 100 | 3% | 425 | $3,188 |
| 9 | 700 | 130 | 3% | 828 | $6,210 |
| 12 | 1,100 | 160 | 3% | 1,253 | $9,398 |
| **13** | 1,253 | 80 | 3% | **1,332** | **$9,990** |

**Break-even:** ~50 paid = ~$375/mo MRR.

**Why the math is realistic:** the long-tail SEO strategy is the multiplier — every format keyword (`.skp to gltf`, `.skp to stl`, `.skp to 3mf`) is its own landing page hitting a different buyer intent. 30 indexed pages × 100 organic click-throughs × 4% conversion × 60 months organic tail = 720 conversions/yr per page = $54K/yr per page at $9/mo.

---

## 7. Kill criteria (hard)

- **Conversion success rate < 85% on first delivery** → engine is broken; pause & fix.
- **Free→pro < 2% by D30** → pricing/limit wrong; test $14/mo or add more free conversions + Pro for batch.
- **< 100 free conversions / day by D30** → SEO not biting; bad keyword choice.
- **Trademark or DMCA complaint from Trimble** → rebrand, remove "SketchUp" from name (rely on generic phrasing "convert your 3D models").
- **Page-1 ranking on no format keyword by D60** → SEO strategy is wrong; revert to Reddit-led growth only.
- **> $300/mo in VPS before 300 paid users** → over-provisioned; scale workers down.

---

## 8. Risks specific to SketchUp utility

- **Trimble cease-and-desist.** They protect the SketchUp brand. Mitigation: use generic phrasing "3D model converter" + footnotes; never use their logo.
- **assimp + skp CLI license terms.** assimp is BSD — fine. SketchUp CLI for headless is free for personal use; at commercial scale we will need Trimble's enterprise license or migrate to a fully open-source skp parser (e.g. `sketchup-rb` community forks — work-in-progress, monitor).
- **Server abuse.** Bad actors uploading malware. Mitigation: 50 MB cap + ClamAV scan + rate limiting + max 50 files/day per IP.
- **Long-tail SEO competition from Autodesk/Adobe branded converters.** Mitigation: target only Trimble-format-specific queries (`.skp`, `.skp to .*`).
