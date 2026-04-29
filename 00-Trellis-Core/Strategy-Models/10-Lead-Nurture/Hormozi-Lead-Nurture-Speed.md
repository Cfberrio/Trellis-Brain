---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Lead Nurture — 'Pillar II: Speed' (pp. 13–18); 'Lead Nurture Checklist' (pp. 39–40)"
sensitivity: internal
hub_role: leaf
book: Lead-Nurture
---

# Hormozi — Pillar II: Speed

## Parent
- [[00-Book-Home|Lead Nurture — Book Home]]

## Purpose
Second-highest-leverage of the four lead-nurture pillars. Decomposes "speed" into three operationally distinct sub-types and provides the call-decision tree, pull-forward script, and hot-handoff script that operationalize them. Speed is what turns the calendar gaps created by [[Hormozi-Lead-Nurture-Availability|Availability]] into closed throughput.

## Core Idea
> "Money loves speed. Wealth loves time. Poverty loves indecision."
>
> Three independent statistics frame the leverage:
> - **391% increase in conversions** when leads are contacted within 60 seconds (Velocify).
> - **7× more likely to qualify** when contacted within an hour vs. an hour later; **60× more** vs. 24-hour-later (HBR).
> - **78% of customers buy from whoever responds first** (Lead Connect).

A speed-fast operation does not just convert more leads — it converts them with **fewer touches**. The slower the first contact, the more total touches required before a sale. The faster the first contact, the fewer. This is one of the rare cases where "work less to make more" is empirically true.

## Framework / Structure

Speed splits into three operationally distinct types. Operators must score and fix each independently.

### 1. Speed to First Contact
Time between opt-in and first call/text/message. Gold standard: **under 5 minutes**. Extra credit: **under 60 seconds**.

Implementation: the calendar gaps from slot-density expansion (see [[Hormozi-Lead-Nurture-Availability|Availability]]) become the time during which reps execute the under-5-minute response. The book's litmus test:
> *"If you aren't getting 'man that was fast! You guys are on top of it!' at least once a day, you're not calling your leads fast enough."*

### 2. Speed to First Appointment
Time between scheduling and the appointment itself. Rule: **cap booking window at 3 days out** (5 days max if necessary). Closer-in appointments show at materially higher rates than far-out ones.

The mechanism in operator language: same-day = ~100% show; next-day high; day-after high; >72h drops sharply; >5 days = ghost territory.

**Pull-forward as a default.** When confirming a self-scheduled appointment, attempt to **pull the appointment earlier in the week** — ideally to today.

The 5-outcome decision tree for confirmation calls:

| # | Outcome | Action |
|---|---|---|
| 1 | Doesn't respond | Remove from calendar (or double-book if in-person). |
| 2 | Contacted but unqualified | Remove from calendar. Provide free useful resource or appropriate downsell. |
| 3 | Contacted, qualified, free right now | **Best case.** Either go straight to close (same setter+closer) or **hot handoff** to active closer (3-way text intro). |
| 4 | Contacted, qualified, pulled appointment forward | Reschedule earlier — preferably today. |
| 5 | Contacted, qualified, appointment confirmed | Re-confirm time; send text confirmation. |

**Pull-forward script (verbatim shape from the book):**
> "Hey, this is [Name] calling from [Co] on a recorded line. I saw you booked a time for our X on Monday. Just calling to confirm some details before your appointment. Is now a terrible time?
>
> (WHO) Great. So I see you are a [qualification 1], is that right? Awesome.
> (WHAT THEY WANT) And you're looking to [qualification 2], is that correct?
> (WHAT THEY'RE STRUGGLING WITH) And what are the things you've tried so far? Got it. What else? So this is a priority for you to fix or [bad thing] happens. Is that fair to say?
>
> Okay great. Two things. First, good news: I think we can help you out. Second, better news: I have an opening that canceled later today at 4pm to get you all squared away — unless now is a good time?"

If they decline pull-forward but stay confirmed:
> "No worries at all. We always like to offer more times to make it convenient. We want to cost you as little time as possible. So we're all good for two days from now at 4pm. Is there any reason you think you won't be able to make that appointment?"

**Hot handoff script (when setter ≠ closer):**
> "You're in luck. You're going to speak with one of our top experts on X. He's been in this game for a while and helped Y [match-to-lead] achieve [outcome]. We're fortunate to have him.
>
> Let me check his calendar quickly. [pause] Yep — I'm sliding you in so you can get this taken care of ASAP / Yep — you're confirmed and good to go.
>
> The moment we get off the call, I'm going to introduce you to him via text message. Does the [number] work? Great. Have an amazing day, and enjoy your time with [Closer]."

### 3. Speed of Response
Responsiveness during the window between scheduling and the appointment — i.e., what happens when a confirmed lead messages with a question.

The book's two-scenario contrast: same-day responses to mid-window questions = "they're on top of it" perception → show. Next-business-day responses = "scattered and disorganized" perception → no-show.

Operational rule: every messaging system has timestamps. **Use them as a rep-level metric.** If show rates drop for a particular rep, look at their response-lag distribution first.

## Strategic Implications

- **Speed-to-First-Contact is a capacity problem disguised as a behavior problem.** Reps cannot respond in <5 min if their calendar is packed solid. Availability slot-density (see [[Hormozi-Lead-Nurture-Availability|Availability]]) is the prerequisite — gaps fund speed.
- **The 3-day booking cap is a constraint that maximizes throughput.** Operators objection: "we'll get fewer schedules if we limit the calendar window." True — and the dropoff is more than offset by the show-rate gain. The math favors fewer-but-shower bookings.
- **Pull-forward is the highest-leverage call type a setter can run.** Each successful pull-forward converts a future-uncertain show into a near-guaranteed show. The script is short, repeatable, and trains in days.
- **Hot handoff > cold handoff.** The 3-way text intro converts setter→closer at materially higher rates than "the closer will reach out." Eliminate the gap between setter call and closer first contact.
- **Response-lag is a leading indicator of show rate by rep.** Don't wait for show rate to drop. Track response-lag weekly per rep and intervene when it slips.
- **The competitor is not the other vendor — it's distraction.** Leads contacted slowly don't usually defect to a competitor; they disengage. Boredom is the enemy. Speed is the antidote.

## Practical Use

Operator speed checklist:

1. **Staff for sub-5-minute first contact** during open hours. Sub-60-second is the gold standard.
2. **Outbound dial every fresh opt-in** the moment it lands. Do not wait for the lead to "warm up."
3. **Cap self-scheduling at 3 days out** (5 max). Same day, next day, day after — those are the only acceptable windows.
4. **Default every confirmation call to a pull-forward attempt** — script above.
5. **Use the 5-outcome decision tree** as the rep's mental model on every confirmation call.
6. **Standardize hot handoff** when setter ≠ closer. 3-way text intro, not "they'll call you."
7. **Track response-lag per rep** weekly. Intervene when median lag rises.
8. **Use calendar gaps** (created by Availability slot-density) to execute fast contact and pull-forwards. Not dead time — funded time.

## Notes / Limits

- **Compliance.** Rapid double-dial, immediate text after voicemail, multi-channel outreach within minutes — all subject to TCPA / regional telecom and privacy law. The book repeatedly notes "obey the laws of your area." This is a real constraint, especially for B2C and cross-jurisdictional flows.
- **Rep burnout.** Sub-5-minute response standards require either rotation (always-on coverage with shifts) or autodialer/queue tooling. Asking one rep to maintain that standard solo for a full day breaks them.
- **Speed without qualification floods the calendar.** Speed must be paired with [[Hormozi-Lead-Nurture-Personalization|Personalization]] qualification to avoid filling the calendar with bad-fit appointments. Speed is a delivery channel, not a filter.
- **Same-setter-and-closer caveat.** When the same rep sets and closes, the 5-outcome decision tree collapses to "go for the close" on outcome 3. The hot handoff script is only relevant when functions are split — typically a high-ticket pattern.

## Source Basis
- *$100M Playbook: Lead Nurture*, "Pillar II: Speed" (pp. 13–14) — three statistics; cost-of-slow-response framing; capacity-vs-speed tradeoff.
- *Lead Nurture*, "Speed To First Contact" (pp. 13–14) — 5-min/60-sec gold standards; speed litmus test pro-tip; calendar-gap funding mechanism.
- *Lead Nurture*, "Speed To First Appointment" (pp. 14–16) — 3-day booking cap; pull-forward rationale; 5-outcome decision tree; pull-forward script; hot-handoff script.
- *Lead Nurture*, "Speed of Response" (pp. 16–17) — two-scenario contrast; per-rep response-lag tracking.
- *Lead Nurture*, "Speed Summary" (p. 18) — synthesis: contact fast, set inside 72h, respond fast.
- *Lead Nurture*, "Lead Nurture Checklist — Speed block" (p. 39).
- Indexed in [[Hormozi-Lead-Nurture-Source-Map|Lead Nurture — Source Map]].

## Related
- [[Hormozi-Lead-Nurture-Four-Pillars|Hormozi — Lead Nurture: Four Pillars]]
- [[Hormozi-Lead-Nurture-Availability|Hormozi — Pillar I: Availability]]
- [[Hormozi-Lead-Nurture-Personalization|Hormozi — Pillar III: Personalization]]
- [[Hormozi-Lead-Nurture-Volume|Hormozi — Pillar IV: Volume]]
- [[Hormozi-BAMFAM|Hormozi — BAMFAM]]
- [[Hormozi-Lead-Nurture-Execution-Culture|Hormozi — Lead Nurture Execution Culture]]
- [[00-Book-Home|Lead Nurture — Book Home]]
- [[Hormozi-Lead-Nurture-Source-Map|Lead Nurture — Source Map]]
