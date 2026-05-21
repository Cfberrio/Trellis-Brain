---
brand: Reliable-Venues
area: dna
note_type: log
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-5317 page 8cqnrff-5777 (ACTIONABLES) — Meeting Luis/Remo 2025-12-30"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: child
---

# RV Actionables Log

## Parent
- [[01-Brands/Reliable-Venues/06-DNA/DNA-Home|RV DNA Home]]

## Related
- [[01-Brands/Reliable-Venues/06-DNA/Offer|RV Offer]]
- [[01-Brands/Reliable-Venues/06-DNA/Sales|RV Sales]]
- [[01-Brands/Reliable-Venues/06-DNA/Scale|RV Scale]]
- [[01-Brands/Reliable-Venues/06-DNA/Money-Model|RV Money Model]]

## Source

Meeting Luis / Remo — 2025-12-30. Captured directly from the STRATEGY/RV/DNA ACTIONABLES page.

## 1. Decisions locked

- **Positioning:** Sell the "future state" (desired outcome) + "current state gap" → make next step easy to close the gap.
- **Content strategy:** Every obstacle becomes a **video** (or small set of videos).
- **Ascension path:** **Directory Listing → Website → Voice Agent** (upsell chain).
- **Main offer exists, but must have downsells:** If they reject full solution, need a **downsell funnel** (one-time offers + stepwise upsells).
- **Trial structure:** Replace "free month" with **$1 trial** (card on file, qualify buyer, frictionless roll into paid).
- **Core "must-have" components (modular downsells):** **Optimized Google listing + Website + Voice Agent**.
- **Outbound add-on:** Targeted outbound to planners (DJs, wedding planners, corporate planners) as a paid service.
- **Referral / Affiliate engine:** Build a system to quantify and access referral partners per city "at the click of a button."
- **Messaging angle:** Don't lead with "more ads"; lead with **"keep your booking calendar full"** (because owners are overwhelmed).

## 2. Actionables by stage

### A) Traffic / Awareness
- Turn each obstacle into a **video topic map** (Director) — Topic list + hooks — Notion / Docs — Due: ASAP — Metric: 10+ topics ready.
- Create "website walkthrough" ad concept (Director) — Script outline + shot list — Loom / Docs — Due: ASAP — Metric: 1 ad concept approved.
- Build baseline branding package for outreach assets (Director / Design) — Basic brand kit — Figma / Canva — Due: 2026-01-12 — Metric: brand kit ready for campaigns.

### B) Lead Capture
- Define CTAs by channel: Meta ad → Book call; Cold call → "Watch 90-sec video then call"; Outbound email TBD (Director) — CTA matrix — Doc — Due: ASAP — Metric: 3 channel CTAs defined.
- Ensure booking flow triggers "video autoplay" immediately after scheduling (Ops / Dev) — Booking confirmation page experience — GHL / Web — Due: ASAP — Metric: >60% watch rate on thank-you page (target).

### C) Pre-Call Nurture (Video + Email / SMS)
- Produce "What to expect on the call" video (90s) (Editor) — Final video — Loom / CapCut — Due: ASAP — Metric: published + linked in booking flow.
- Build post-booking automation sequence (Ops) — Email / SMS confirmations + reminders + links — GHL — Due: ASAP — Metric: open rate / click rate.
- Add "watch video before call" compliance prompt for cold calls (Sales / Ops) — Script snippet + auto-email template — GHL — Due: ASAP — Metric: % leads who watch before call.

### D) Sales Call / Close
- Create **pre-recorded walkthrough "sales call"** (Director / Editor) — 10–20 min walkthrough: front website → admin dashboard → staff dashboard → marketing / Google listing — Loom — Due: ASAP — Metric: used in every booked call.
- Shift pitch language: "We keep your calendar full" vs "we run more ads" (Sales) — Updated talk track — Doc — Due: ASAP — Metric: improved show-up / close rate.

### E) Downsell Funnel (if full package rejected)
- Define Downsell #1: **$1 / 30-day "Pre-implementation" access** (Director / Ops) — Offer page + checkout — GHL / Stripe — Due: ASAP — Metric: trial conversion rate.
- Define Downsells #2–#4 (easy-to-fulfill modules) (Director) — Productized offers:
  - Optimized Google Listing
  - Website
  - Voice Agent
  Due: ASAP — Metric: at least 3 clear one-time offers.
- Create rejection-path logic: "Reject full → offer $1 trial → reject → offer single module" (Ops) — Workflow diagram + GHL automation — Due: ASAP — Metric: >X% salvaged deals (set baseline).

### F) Upsell / Ascension Path
- Build upsell automation: **Directory claim → Website → Voice agent** (Ops) — Stage tags + offers + triggers — GHL — Due: ASAP — Metric: upsell conversion per step.
- Implement "trial with penalty" / auto-roll into paid (Ops) — Subscription / billing logic — Stripe / GHL — Due: ASAP — Metric: trial → paid conversion.

### G) Referral / Affiliate Engine
- Build city-based referral partner database structure (Ops / Dev) — Categories: DJs, wedding planners, corporate planners, etc. — Airtable / DB — Due: ASAP — Metric: can query "how many exist in a city."
- Build "click of a button" report per city for prospects (Ops / Dev) — Output: "We can put you in front of X partners" — Dashboard / PDF — Due: ASAP — Metric: generated in <60 sec.
- Define pricing: **flat fee + %** for outbound / referral partner distribution (Director) — Pricing sheet — Doc — Due: ASAP — Metric: pricing locked.

### H) Tracking / Attribution
- Confirm sub-account tracking plan (Ops) — Multi-subaccounts + reporting — GHL — Due: ASAP — Metric: can see lead → sale by account.
- Design revenue-share collection method (Ops / Dev) — Approach options: track invoicing via GHL, script calculates payout cadence (weekly / per sale), explore payment splitting (Stripe) — Due: ASAP — Metric: defined "how we get paid" flow.

## 3. Assets to produce (minimum list)

| Asset | Purpose | Use | Length | Must include |
|---|---|---|---|---|
| Obstacle Video Set | Convert problems to content | Ads + nurture | 30–90s each | Problem named + solution preview + CTA |
| 90-sec Pre-Call Video | Force clarity before call | Thank-you page + cold call follow-up | 90 sec | What this is + what to prep + what happens next |
| Full Walkthrough Video | Pre-sell the system | Used before call | 10–20 min | Front site + dashboards + booking / ops flow |
| Offer Ladder One-Pager | Explain ascension + downsells | Sales + email | 1 page | Full solution + downsell modules + $1 trial |
| "See our reviews" link asset | Trust proof | Website CTA | — | Direct to reviews section, 1 click |

## 4. Automations to build (GHL / Stripe / CRM)

| Trigger | Actions | Data needed | Error handling |
|---|---|---|---|
| Appointment booked | Redirect to thank-you with autoplay video + SMS / email confirmation + reminders + tag "Booked-Call" | Name, email, phone, time | If email unopened, SMS follow-up with same link |
| Cold call ends + lead qualified | Send "watch 90-sec video before call" email / SMS + scheduler link | — | If not watched within X hrs, auto reminder |
| Full offer declined | Present $1 trial → if declined → offer single module (listing / website / voice agent) | Reason code for decline (optional) | — |
| Trial ends | Auto-roll into paid plan + notify + upsell next step | — | — |
| New customer onboarded | Generate referral partner count for their city + present outbound / referral add-on (flat fee + %) | — | — |

## 5. Content queue (video-first)

| Topic | Angle | Hook | CTA tier |
|---|---|---|---|
| Inquiries everywhere | Stops chaos of inbound | "Leads are coming from 5 places…" | Top / Mid |
| Response lag kills bookings | Speed-to-lead | "If you reply late, you lose…" | Mid |
| No follow-up = lost revenue | Automation | "Most venues leak money here…" | Mid |
| Walkthrough: venue website that closes | Product demo | "Watch how this converts…" | Top / Mid |
| $1 trial: see it running in 30 days | Risk reversal | "Don't buy the whole package…" | Bottom |

## 6. Risks / blockers

- **"More advertising" triggers fear** (overwhelmed owners) → fix: position as "calendar full + operational relief."
- **Free trial attracts non-buyers** → fix: **$1 trial** (card + authority check).
- **Revenue-share billing complexity** → fix: choose 1 mechanism now (GHL invoicing tracking + scripted billing cadence) and ship.
