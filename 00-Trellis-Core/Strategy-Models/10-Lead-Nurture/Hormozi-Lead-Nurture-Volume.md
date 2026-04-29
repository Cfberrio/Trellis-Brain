---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Lead Nurture — 'Pillar IV: Volume' (pp. 27–31); 'Lead Nurture Checklist' (pp. 39–40)"
sensitivity: internal
hub_role: leaf
book: Lead-Nurture
---

# Hormozi — Pillar IV: Volume

## Parent
- [[00-Book-Home|Lead Nurture — Book Home]]

## Purpose
Fourth lead-nurture pillar. Defines the **outreach cadence** (how many touches before giving up), the **automated reminder schedule**, the **manual reminder schedule**, and the **conversation-keeper protocol** (Acknowledge → Compliment → Ask). Counters the empirical default — **~44% of salespeople stop after the first attempt; average is 1.3 attempts** (InsideSales.com / RAIN Group) — with a structured 7+ touch sequence.

## Core Idea
> "Volume negates luck."
>
> Most communication attempts fail for benign reasons (bad timing, distraction, missed signal, "didn't need it then but do now"). The lead opted in — they asked to be contacted. Repeated outreach is therefore both commercially correct and ethically appropriate. Quitting after one or two attempts leaves most of the addressable shows on the table.

## Framework / Structure

Volume splits into three operationally distinct components.

### 1. Scheduling Appointments — 7-day front-loaded outreach cadence
Default cadence per fresh opt-in. Front-loaded because schedule-rate decays with elapsed time.

| Day | Action |
|---|---|
| Day 0, t=0–5 min | **Call within 5 min of opt-in.** Sub-60-second is gold standard. |
| Day 0, on no-answer | **Double-dial** (call again immediately). Two reasons: (a) act like permission to contact actually means contact; (b) many phones block first unrecognized call but allow the second. |
| Day 0, on no-answer #2 | Leave **voicemail**. |
| Day 0, immediately after VM | Send **text** (compliance-permitting). |
| Day 0, later | **2 more double-dial + text** attempts, hours apart. |
| Day 1 | **2 calls** (one early, one late) + text after second call. |
| Day 2 | Same pattern: 2 calls + text. |
| Days 3–6 | **1 call + 1 text per day.** Vary AM/PM to catch different responder windows. |
| Day 7+ | Transition to **long-term nurture** (out of scope of this playbook — value-providing rhythm with soft CTAs to re-engage). When they re-engage, the 7-day sequence restarts. |

Total touches in the 7-day window: typically **15–20+ across all channels**. Compare to industry default of ~1.3 attempts.

Rationale for front-loading: the schedule probability decays roughly with the log of elapsed time. Days 0–2 carry most of the addressable schedule volume.

### 2. Reminding Them to Show

Once scheduled, the goal shifts from *get them to schedule* to *get them to show*. Two reminder layers run in parallel.

**Automated reminders** (use software defaults; transparently labeled as automated):

| When | Content |
|---|---|
| Immediately on schedule | Confirmation: time, date, calling number, person they'll meet |
| 24 hours before | Reminder |
| 12 hours before | Reminder |
| 3 hours before | Reminder |

Tips: include the **area code you'll be calling from** (2× pickup rate). Use the **lead's local time zone** in the reminder text.

**Manual reminders** (from a real cell phone, not the platform):

| When | Form |
|---|---|
| Night before | Personal text |
| Morning of | Personal text |
| ~60 min prior | Personal text or call |

**Manual-reminder rules:**
- **Multiple short messages** beat one big block message — reads as more human.
- **Conversation-keeper protocol** when they reply: **Acknowledge → Compliment → Ask the next question.** Use "the next question" to qualify and to attempt pull-forward (see [[Hormozi-Lead-Nurture-Speed|Speed]] pull-forward script).
- Once they respond — keep nurturing. Keep responding quickly. Don't fall silent post-reply.

### 3. Book Their Next Appointment at the Current Appointment
Standalone tactic with its own canonical: **BAMFAM (Book-A-Meeting-From-A-Meeting)** — see [[Hormozi-BAMFAM|Hormozi — BAMFAM]]. Summary: never end any appointment without the next appointment booked **on the calendar in real time**, not "I'll follow up with times." Multi-step sales (qualify → close, close → onboarding) are where this lever is largest.

## Strategic Implications

- **The default human pattern is to under-contact.** ~44% of salespeople give up after attempt 1; ~average is 1.3 attempts. The 7+ touch cadence is not aggressive — it is **catching up to opted-in permission** that the operator already received.
- **Front-loading exploits the decay curve.** Touches on day 0–2 carry most of the addressable schedules. Spreading the same touch count evenly across two weeks underperforms front-loading materially.
- **Automated + manual reminders are not redundant — they signal different things.** Automated says "logistics are handled." Manual says "a real person values this appointment." Both lift show; both are needed.
- **Conversation-keeper (Acknowledge → Compliment → Ask) is a simple, trainable script.** It prevents the common rep failure of responding to a lead's reply and then going silent — converting a live conversation into a dead thread.
- **Volume is ethically defensible *because* of the opt-in.** Without opt-in, this cadence is harassment. With opt-in, it is service delivery. Get the opt-in right and the volume is justified.
- **BAMFAM compounds with multi-step funnels.** Any business with a setter→closer or close→onboarding split eats huge no-show losses on the second meeting unless BAMFAM is enforced. Single-call-close businesses are unaffected.

## Practical Use

Operator volume checklist (synthesizing pp. 39–40):

1. **Day 0:** call within 5 min → double-dial → VM → text → 2 more double-dial + text rounds.
2. **Day 1–2:** 2 calls + 1 text per day, AM/PM split.
3. **Days 3–6:** 1 call + 1 text per day.
4. **Day 7+:** transition to long-term nurture; restart sequence on re-engagement.
5. **Automated reminders** at: scheduled, 24h, 12h, 3h. Include calling area code + local time zone.
6. **Manual reminders** at: night before, morning of, 60 min prior — from a real cell phone.
7. **Multiple short messages**, not blocky paragraphs.
8. **Conversation-keeper:** Acknowledge → Compliment → Ask the next question. Use "ask" to attempt pull-forward.
9. **BAMFAM on every multi-step appointment** — book the next meeting before this one ends.
10. **Get an autodialer.** 2–3× rep efficiency. Removes the "live in spreadsheets" overhead.

## Notes / Limits

- **Compliance is the binding constraint.** TCPA, GDPR, CASL, regional telecom and consumer-protection law constrain frequency, channel, time-of-day, and consent scope. The book repeatedly notes "obey the laws of your area." Build the cadence template once, then validate per jurisdiction.
- **Channel mix matters more than channel count.** 7 SMS in one day + 0 calls is not a 7-touch cadence — it's spam. Balance call / text / email / DM per the lead's preferred channel (see [[Hormozi-Lead-Nurture-Personalization|Personalization]] tactic 1).
- **Volume without [[Hormozi-Lead-Nurture-Personalization|personalization]] degrades fast.** Identical templated outreach 7×=spam. Segment-relevant outreach 7× = nurture. Same touch count, opposite outcomes.
- **Long-term nurture is a separate playbook.** Day 7+ off-ramp is real — do not treat the 7-day cadence as a standing pattern for cold lists.
- **Autodialer compliance.** Autodialers carry their own regulatory exposure (TCPA "ATDS" definitions, jurisdiction-specific rules). Tool choice must match jurisdiction.

## Source Basis
- *$100M Playbook: Lead Nurture*, "Pillar IV: Volume — Description" (p. 27) — definition; ~44% give-up-after-one stat; ethical/permission framing.
- *Lead Nurture*, "1) Scheduling Appointments" (pp. 27–28) — 8-step front-loaded outreach cadence.
- *Lead Nurture*, "Pro Tip: Get An Automatic Dialer" (p. 28).
- *Lead Nurture*, "2) Reminding Them To Show — Automated + Manual" (pp. 29–31) — automated reminder schedule, area-code/time-zone tips, manual reminder schedule, multiple-short-messages rule, Acknowledge-Compliment-Ask protocol.
- *Lead Nurture*, "3) Book Their Next Appointment At The Current Appointment" (p. 31) — BAMFAM (cross-linked to dedicated canonical).
- *Lead Nurture*, "Volume Summary" (p. 31).
- *Lead Nurture*, "Lead Nurture Checklist — Volume block" (pp. 39–40).
- Indexed in [[Hormozi-Lead-Nurture-Source-Map|Lead Nurture — Source Map]].

## Related
- [[Hormozi-Lead-Nurture-Four-Pillars|Hormozi — Lead Nurture: Four Pillars]]
- [[Hormozi-Lead-Nurture-Availability|Hormozi — Pillar I: Availability]]
- [[Hormozi-Lead-Nurture-Speed|Hormozi — Pillar II: Speed]]
- [[Hormozi-Lead-Nurture-Personalization|Hormozi — Pillar III: Personalization]]
- [[Hormozi-BAMFAM|Hormozi — BAMFAM]]
- [[Hormozi-Lead-Nurture-Execution-Culture|Hormozi — Lead Nurture Execution Culture]]
- [[00-Book-Home|Lead Nurture — Book Home]]
- [[Hormozi-Lead-Nurture-Source-Map|Lead Nurture — Source Map]]
