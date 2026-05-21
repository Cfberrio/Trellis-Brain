---
brand: Orlando-Event-Venue
area: dna
note_type: leaf
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-7037 page 8cqnrff-4837 (STRATEGY / DNA / OEV / 5) Lead DNA)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Lead

## Parent
- [[DNA-Home|OEV DNA Home]]

## Related
- [[Conversion|OEV Conversion]]
- [[../01-Systems/Sales/Sales-Home|OEV Sales Home]]
- [[../01-Systems/Sales/Lead-Definition|OEV Lead Definition]]
- [[../02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]]

## The Narrow Problem (what callers actually want)
Inbound Google / directory calls consistently ask:
> **"Is my date available, what will it cost, and will my event be allowed (rules)?"**

Narrow + meaningful → naturally leads to next step: **lock the date + execute without issues/fees.**

## Lead Magnet Strategy
Use Hormozi's 3 types — rotate two as standard library:

### A. Reveal Problems (Diagnosis)
> "Are you booking a space that can trigger penalties, timeline issues, or surprise fees?"
- Rules + setup/breakdown realities + common "gotchas"

### B. One Step of a Multi-Step Process
> "Step 1: Confirm availability + get an accurate minimum cost + choose a layout plan."

**Optional later — Samples/Trials:** tour / walkthrough as a try-before-you-buy.

## Lead Magnets To Deploy

### Lead Magnet #1 (Primary) — Instant Availability + Quote Pack
**Goal:** turn "availability callers" into engaged leads we can follow up with automatically.

**Includes:**
- Date/time window request
- Auto-calculated minimum economics (hourly min vs day + cleaning + add-ons if selected)
- Quick compliance snapshot (beer/wine allowed; no hard liquor; key rules)
- Layout chooser (90 chairs / 10 tables templates)

**Packaging (same content, multiple formats):**
- SMS link (fastest for callers)
- 1-page PDF (reference)
- 60–90 sec walkthrough video (space + rules + what's included)

**CTA:**
> "To block the date: **50% deposit today** (remaining 50% per policy)."

**Scarcity/urgency placement:**
- Floors 1–2: no urgency. Just speed + clarity.
- Floor 4+: "Why now?" only if real (hold window, competing inquiry, limited tech resource).

### Lead Magnet #2 (Controlled downsell for personal events) — Personal Event Host Kit
> Not main positioning — personal-event conversion tool.

**Narrow problem:** "How do I run a baby shower / personal event here without fees, stress, or timeline issues?"

**Includes:**
- Decoration + cleanup checklist (no glitter/confetti)
- Setup/breakdown timeline template (avoid overtime)
- Personal event layout templates (gift table, photo area, seating flow)

**Promo attached cleanly (no spontaneous discounts):**
$100 credit only after they accept the kit + agree to proof assets (review/testimonial/social).

**Urgency rule:** booking calendar filling over week + next week.

## Automation Blueprint (CRM-first, voice-agent-driven)

### A. Inbound call (always answered by voice agent) → capture opt-in
**Objective:** every caller leaves with:
1. Availability Pack link (via SMS)
2. Event details captured in CRM

**Voice agent flow — capture 4 fields:**
- Date/time window
- Guest count
- Event type (corporate/workshop/personal)
- A/V needs (none/basic/LED/streaming)

**Then send SMS during the call:**
> "Here's the Instant Availability + Quote Pack — complete it and we'll confirm availability + exact minimum cost."

**Floor rule:** If still early (Floors 1–2), agent stays informational — no urgency language.

### B. After opt-in → respond fast + move to decision
**System rule:** speed matters most right after inquiry.

**Automated sequence:**
1. Confirm availability (or offer 2 closest alternatives)
2. Send quote summary + what's included + key rules
3. Ask for deposit to block date ONLY when qualified (Floor 4+)

### C. Follow-up cadence (automated + voice agent/human)
| Day | Touches |
|---|---|
| Day 0 | Availability confirmation + quote + deposit CTA |
| Same day | 2 nudges if no response (text first; voice/human call second) |
| Days 1–2 | 2 touches/day (different times) |
| Days 3–6 | 1 touch/day |
| Then | Long-term nurture |

### D. Scarcity / Urgency Injection (only when real)

**Floor 4 (qualified) — allowed only if real:**
- Real hold window (timestamped expiration)
- Real inventory constraint (one booking per slot)
- Real resource constraint (LED/streaming = reserve tech time)

**Floor 4 example:**
> "Your date is available right now. I can hold it until [time]. To lock it: 50% deposit → [link]."

**Floor 6 urgency (use ONLY when):**
- ✅ `hold_expires_at` within 24h / 6h
- ✅ `competing_inquiry = true` (logged for same slot)
- ✅ `tech_resource_needed = true` + tech availability limited
- ✅ Peak-date inventory objectively tight (weekends/holidays)

**Do NOT use Floor 6 urgency when:**
- ❌ Still educating (pack not opened, quote not reviewed)
- ❌ Unqualified (capacity/rules mismatch)
- ❌ No specific constraint to cite ("just because" urgency)

**Examples:**
- Hold expiring: "Reminder: the hold for [date/time] expires at [time]. To lock it: 50% deposit → [link]."
- Competing inquiry: "Heads-up: another inquiry came in for [date/time]. The date is confirmed with deposit → [link]."
- Tech constraint: "To guarantee LED/streaming on [date], we also need to reserve the tech slot. Confirm here → [link]."
