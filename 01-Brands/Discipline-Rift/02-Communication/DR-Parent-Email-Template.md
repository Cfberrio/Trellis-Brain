---
brand: Discipline-Rift
area: communication
subarea: campaigns
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Trellis repo domains/content/discipline-rift/parent-email-template.md — binding drafting contract derived from Luis's approved first-week email + his five rules (2026-08-09/10)"
owner: Luis
last_updated: 2026-08-10
sensitivity: internal
hub_role: leaf
audience: parent
channel: [email]
---

## Parent
- [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|DR Communication Home]]

## Related
- [[DR-Email-Design-Spec|DR Email Design Spec]] — how the slots render
- [[Campaigns/DR-First-Week-Of-School-Campaign-2026-08|First Week of School Campaign]] — the canonical worked example
- [[Campaigns/DR-Email-Rewrite-Retrospective-2026-08|Email Rewrite Retrospective]] — why each rule exists

# DR — Parent Email Template (House List)

**What this is:** The binding drafting contract for DR marketing emails to the parent house list. Derived from Luis's finalized first-week email (2026-08-09) — the canonical example of correct length, density, and register. Every house-list draft is written INTO this structure, then rendered to GHL-ready HTML per [email-design-spec.md](email-design-spec.md).

**What this is NOT for:** cold pop-up nurture. That runs on `popup-funnel-v2` conversion DNA (objection coverage, proof stacking, deadline anchors). **Those rules must never leak into house-list emails.** The 2026-08 first-draft failure was exactly that leak: cold-lead persuasion architecture sent to a warm list.

---

## 1. The sender model

Write as **Coach Luis talking to a parent who already knows the school** — not as a marketer persuading a skeptic. The house list is warm: non-converted leads and past parents. They don't need to be argued into anything; they need one clear, warm, useful message from a coach.

Voice calibration sources, loaded before drafting:
- Luis's finalized first-week email — campaign §2 in [campaigns/2026-08-first-week-of-school-email.md](campaigns/2026-08-first-week-of-school-email.md)
- His real sent parent emails — Trellis-Brain `03-Evidence/Founder-Voice/bot-training/01-PARENTS.md` (verbatim threads)
- The five rules — campaign §0 (binding)

## 2. The structure (from the approved email — slots, in order)

| # | Slot | Size | Notes |
|---|---|---|---|
| 1 | Greeting | 1 line | `Hi {{contact.first_name}},` |
| 2 | Hook — meet them where they are | 2–3 short lines | Plain, situational, positive. A question is fine. No fear framing (fear-as-question allowed in subject/preview only). |
| 3 | **REGISTER button #1** | — | Early, right after the hook lands. |
| 4 | 2–3 points for parents | 1 bold line + 1–2 sentences each | Universal to the age, DR carries the burden. Never a diagnosis of their child. |
| 5 | Method, not mood | 3–4 sentences | Teach → drill → play. The luck line. **No method names.** |
| 6 | Easy for you | 2 lines | Convenience line verbatim: "No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school." |
| 7 | Visibility | 2–3 lines | Per-practice coach update + dashboard (progress, photos). Frame: more to go on when you ask — never "you won't have to ask." |
| 8 | Guarantee | 1–2 lines | "Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season." |
| 9 | **REGISTER button #2** | — | |
| 10 | Warm close | 1 line + signature | e.g. "Wishing your child a valuable, enriched school year." Coach Luis, Founder. Never a deadline squeeze. |

Not every email uses every slot — cut slots before shrinking them. **Never add slots.** (The HTML builds also carry three spec-owned chrome slots outside this copy contract — SLOT 0 header, SLOT H giant-word hero, SLOT F footer, per email-design-spec §5.1/§5.2/§5.9. "Never add slots" refers to copy slots 1–10.)

## 3. Hard caps

- **Target 150–200 words; 230 is the ceiling, not the target.** Luis cut below the approved 230 again at the design stage (bedtime line changed, further content removed post-transcript). Compression is unbounded — every line must survive halving, and every slot must be deletable without breaking the email.
- **One idea per slot.** A slot arguing two things loses one.
- **One unique CTA**, rendered exactly twice (slots 3 and 9). Label `REGISTER`. **Destination is an open ruling:** Luis explicitly shipped the 2026-08 send to the homepage (`disciplinerift.com/`); the funnel's designed entry is `/register` school search. Build with whatever Luis states per send; do not silently "correct" his stated URL.
- **Subject:** calendar-anchored, plain, direct question where possible (`Back to school this Tuesday. Are you ready?`). Preview extends, never repeats; the gap frame is allowed here as an open question.
- Zero: dollar figures, method names, proof stacks (55 schools / Level 2 live on the site, not in house-list emails unless the email's job is trust), urgency mechanics, age-range lines, beginner-only positioning, banned vocabulary.

## 4. The production chain (rerouted 2026-08-10)

```
insight → template-constrained draft → five-rules check (campaign §0)
→ Claude builds GHL-ready HTML (email-design-spec + its §5.2/§10.1 rulings)
→ Luis reacts to the RENDER → QA pass on the final artifact → GHL
```

- The deliverable Luis receives is always the **rendered HTML**, never a document. Each render ships with **one proposed 3–6 word hero phrase** for him to keep or kill (he accepted an AI-proposed hero — "Movement belongs on the list" — when it was short and on-frame).
- Build from `email-html/dr-boilerplate-ghl.html` — every slot is an independently deletable block, because Luis iterates one visual element at a time ("invert it," "remove that") and always cuts.
- QA runs on the final artifact: spelling, CTA URL as Luis stated it, merge-tag fallbacks, dark mode, 600px/375px, the §11 pre-send checklist in the design spec.
- Luis's edits on the render are rulings — reverse-engineer the lesson, update this template, don't argue it back.
- **Archive the shipped HTML per send** (into `email-html/sent/`). Post-approval edits happen off-record (2026-08: bedtime line + further cuts after the transcript ended); the shipped file is the only ground truth.

## 5. Asset blockers (resolve once, unblocks every future build)

| Asset | Status | Where it goes |
|---|---|---|
| DR mark, blue on transparent PNG | **Not hosted** — build falls back to text-wordmark hero | Header on white |
| DR mark, white on transparent PNG | **Not hosted** | Black footer + dark mode |
| White tick, 20px PNG | **Not hosted** | Promo-band checklist |

Source: `Brand Assets/01 Logos/Main Logos` (Drive). Host once at a stable public URL — GHL's media library is the natural home — and record the URLs here and in the design spec. Until then, the giant blue text-wordmark (nothing under it) is the approved fallback per the §5.2 ruling.

**RESOLVED 2026-08-25 — all three assets are hosted** (served by the website, stable URLs; kit derived from the hi-res Drive master):

| Asset | URL |
|---|---|
| DR mark, blue on transparent | `https://disciplinerift.com/brand/dr-mark-blue-52h.png` (header, @2x for 26px) |
| DR mark, white on transparent | `https://disciplinerift.com/brand/dr-mark-white-52h.png` |
| White tick 20px | `https://disciplinerift.com/brand/dr-tick-white-20.png` |

The §4 boilerplate now exists: `~/Documents/DISCIPLINERIFT/brand-kit/email/dr-boilerplate-ghl.html` (all slots as independently deletable blocks, assets wired). The text-wordmark fallback is no longer needed — builds use the real mark.