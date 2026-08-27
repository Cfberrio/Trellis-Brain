---
brand: Discipline-Rift
area: communication
subarea: sequences
note_type: sequence
status: draft
used_for_ai: true
sensitivity: internal
owner: Luis
last_updated: 2026-07-23
sequence: registration
channel: [email, sms]
related_notes:
  - "[[../DR-Communication-Engine]]"
---

# DR Registration Sequence

Every message from **the moment a parent registers a child** through **the first practice** — plus the branch that recovers a registration someone started but didn't pay for. One document, one table, full copy below.

- **Voice:** warm, organized, mobile-readable. Short sentences. Uses `{STUDENT_FIRST_NAME}` and `{PARENT_FIRST_NAME}`.
- **Channel rule:** email carries it; SMS only where time-sensitive + high-value (see [[../DR-Communication-Engine]]). Total texts in this whole journey: **3**.
- **Merge syntax:** `{UPPERCASE}` canonical. Times in America/New_York.
- **Fatigue rule:** the 30/7/1-day countdown fires **once, for the first practice / season start only** — never per session.

---

## A. Main spine — confirmed registration → first practice

| # | Step | Email | SMS | Trigger |
|---|---|---|---|---|
| 0 | Verification code (OTP) | *Your Discipline Rift verification code* | — | Parent requests access code during registration |
| 1 | Booking confirmation — "you're good to go" | *{STUDENT_FIRST_NAME} is in! Here's what's next* | ✓ | Payment succeeds (fires within seconds) |
| 2 | Get ready — what to expect | *What to expect before {STUDENT_FIRST_NAME}'s first practice* | — | +1 day after payment (skip if season starts in <10 days) |
| 3 | 30-day countdown | *30 days until {STUDENT_FIRST_NAME}'s season 🗓️* | — | 30 days before season start (first session only) |
| 4 | 7-day countdown + what to bring | *One week away — what {STUDENT_FIRST_NAME} needs* | — | 7 days before season start (first session only) |
| 5 | Day before first practice | *Tomorrow's the day, {STUDENT_FIRST_NAME}! 🏐* | ✓ | 1 day before first session |

## B. Branch — registration started, not paid (cart recovery)

| # | Step | Email | SMS | Trigger |
|---|---|---|---|---|
| R1 | Recovery #1 — "your spot is held" | *You're almost done — {STUDENT_FIRST_NAME}'s spot is held* | — | Registration started, no payment, +1 hour |
| R2 | Recovery #2 — "filling up" | — | ✓ | Still unpaid, +24 hours |
| R3 | Recovery #3 — final | *Last call for {STUDENT_FIRST_NAME}'s spot* | — | Still unpaid, +72 hours (then stop) |

---

# Full copy

## 0 — Verification code (OTP) · Email · transactional

**Subject:** Your Discipline Rift verification code

```
Hi {PARENT_FIRST_NAME},

Your one-time code is:

{OTP_CODE}

Enter it to finish signing in. It expires in 10 minutes.
If you didn't request this, you can ignore this email.

— The Discipline Rift Team
```
*Keep it bare. No marketing in an OTP.*

---

## 1 — Booking confirmation · Email + SMS · transactional
**The most important message in the sequence.** Fires within seconds of payment. Closes the doubt, reverses the risk, plants the next step and the sibling cross-sell.

**Subject:** {STUDENT_FIRST_NAME} is in! Here's what's next
**Preview:** Spot confirmed for {SPORT} at {SCHOOL_NAME}.

```
Hi {PARENT_FIRST_NAME},

{STUDENT_FIRST_NAME} is officially registered for {SPORT} at {SCHOOL_NAME}. Their spot is locked. 🎉

Here's what you confirmed:
• Sport: {SPORT}
• School: {SCHOOL_NAME}
• Season: {SEASON_START_DATE} – {SEASON_END_DATE}
• Schedule:
{PRACTICE_SCHEDULE}
• Coach: {COACH_NAME}
• Paid: {AMOUNT} on {PAYMENT_DATE}

[ Add first practice to your calendar ]  → {ADD_TO_CALENDAR_URL}
[ View your registration ]  → {DASHBOARD_URL}

What happens next:
1. We'll send a get-ready note with what to bring.
2. You'll get a reminder as the first practice gets close.
3. Everything is handled by our coaches from dismissal, on campus — no transportation needed.

This season is Tier 1 of {STUDENT_FIRST_NAME}'s journey. Finish it and they advance to the next tier — with progress you can actually see.

Have another child? Use code SIBLING at checkout for 10% off their registration.

Our promise: we actually teach the sport. If we don't deliver that during the season, you get a 100% refund, any time. No windows, no fine print.

Questions? Just reply to this email.

See you on the court,
The Discipline Rift Team
info@disciplinerift.com · (407) 614-7454 · disciplinerift.com
```

**SMS (fires same moment — reassurance, expected):**
```
Discipline Rift: {STUDENT_FIRST_NAME} is confirmed for {SPORT} at {SCHOOL_NAME} 🎉
First practice: {FIRST_PRACTICE_DATE}, {FIRST_PRACTICE_TIME}.
Details + add to calendar: {DASHBOARD_URL}
Reply STOP to opt out.
```

---

## 2 — Get ready / what to expect · Email
Sent the day after payment. Skip if the season is already <10 days out (the 7-day email covers it). Front-loads the useful stuff so parents aren't guessing.

**Subject:** What to expect before {STUDENT_FIRST_NAME}'s first practice
**Preview:** A quick guide so day one goes smoothly.

```
Hi {PARENT_FIRST_NAME},

Now that {STUDENT_FIRST_NAME} is registered, here's everything you need so the first practice is easy.

What to bring:
• Water bottle
• Athletic shoes
• Comfortable clothes
• {SPORT_SPECIFIC_ITEM}   (e.g., knee pads optional for volleyball)

How it works:
• Practices are on campus at {SCHOOL_NAME}, right after dismissal.
• Coaches meet the students at the designated spot — you don't need to drop off or drive anywhere new.
• Pickup is at {FIRST_PRACTICE_TIME_END} at {SCHOOL_LOCATION}.

One thing that helps at home:
After the first practice, ask {STUDENT_FIRST_NAME} one question — "What's one thing that felt easier today than before?" It's how kids start noticing their own progress.

You can see the full schedule and your coach anytime in your dashboard:
[ View dashboard ] → {DASHBOARD_URL}

See you soon,
The Discipline Rift Team
```

---

## 3 — 30-day countdown · Email
Fires 30 days before the **first** session only. Short — this is a "start planning" signal, not onboarding.

**Subject:** 30 days until {STUDENT_FIRST_NAME}'s season 🗓️
**Preview:** Still on track — here's the schedule again.

```
Hi {PARENT_FIRST_NAME},

Quick heads-up — {STUDENT_FIRST_NAME}'s {SPORT} season starts in 30 days.

Here's the schedule so you can plan ahead:
{PRACTICE_SCHEDULE}

Nothing to do yet. We'll send everything you need as it gets closer.

See you on the court,
The Discipline Rift Team
```
> **Bug to fix:** current template banner reads "1-Day Reminder." Change to "30-Day Reminder."

---

## 4 — 7-day countdown + what to bring · Email
Fires 7 days before the first session. Logistics-forward — parents are planning their week now. Introduce the coach to lower first-day nerves.

**Subject:** One week away — what {STUDENT_FIRST_NAME} needs
**Preview:** First practice details + what to bring.

```
Hi {PARENT_FIRST_NAME},

{STUDENT_FIRST_NAME}'s {SPORT} season starts in one week.

First practice:
📅 {FIRST_PRACTICE_DATE}, {FIRST_PRACTICE_TIME}
📍 {SCHOOL_NAME} — {SCHOOL_LOCATION}
🧑‍🏫 Coach: {COACH_NAME}

Before day one:
• Bring: water bottle, athletic shoes, comfortable clothes{SPORT_SPECIFIC_ITEM_LINE}
• Coaches meet students right after dismissal — no new drop-off routine.
• Pickup at {FIRST_PRACTICE_TIME_END}.

Coach {COACH_NAME} is ready for a great first session.

See you there,
The Discipline Rift Team
```
> **Bug to fix:** banner still reads "1-Day Reminder." Change to "7-Day Reminder."

---

## 5 — Day before first practice · Email + SMS
The show-up nudge. Short, scannable — parents read this on their phone mid-day. SMS is the human, time-sensitive layer.

**Subject:** Tomorrow's the day, {STUDENT_FIRST_NAME}! 🏐
**Preview:** First {SPORT} practice is tomorrow.

```
Hi {PARENT_FIRST_NAME},

{STUDENT_FIRST_NAME}'s first {SPORT} practice is tomorrow.

📅 {FIRST_PRACTICE_DATE}, {FIRST_PRACTICE_TIME}
📍 {SCHOOL_NAME}
👕 Bring: water, athletic shoes, comfortable clothes
🧑‍🏫 Coach {COACH_NAME} will meet students right after dismissal.

That's it — see you tomorrow.
The Discipline Rift Team
```

**SMS (afternoon before):**
```
Discipline Rift: {STUDENT_FIRST_NAME}'s first {SPORT} practice is tomorrow, {FIRST_PRACTICE_TIME}, at {SCHOOL_NAME}.
Bring water + athletic shoes. Coach {COACH_NAME} meets them after dismissal.
See you there! Reply STOP to opt out.
```

---

# Branch B — cart recovery (started, not paid)

Front-loaded per Lead Nurture: hour 1 → day 1 → day 3, then stop. Loss-aversion framing ("spot held / filling"), not "come back." One text total.

## R1 — Recovery #1 · Email · +1 hour

**Subject:** You're almost done — {STUDENT_FIRST_NAME}'s spot is held
**Preview:** Finish in under a minute.

```
Hi {PARENT_FIRST_NAME},

You started registering {STUDENT_FIRST_NAME} for {SPORT} at {SCHOOL_NAME} — you're one step from done. We're holding the spot for you.

[ Finish registration ] → {REGISTER_URL}

If something came up or you have a question, just reply — happy to help.

The Discipline Rift Team
```

## R2 — Recovery #2 · SMS · +24 hours
```
Discipline Rift: {STUDENT_FIRST_NAME}'s spot for {SPORT} at {SCHOOL_NAME} is still open, but teams are filling for the season.
Finish here (takes <1 min): {REGISTER_URL}
Reply STOP to opt out.
```

## R3 — Recovery #3 (final) · Email · +72 hours

**Subject:** Last call for {STUDENT_FIRST_NAME}'s spot
**Preview:** We'll release the hold soon.

```
Hi {PARENT_FIRST_NAME},

We've been holding {STUDENT_FIRST_NAME}'s spot for {SPORT} at {SCHOOL_NAME}, but the season is filling and we'll need to release it soon.

If you still want in:
[ Complete registration ] → {REGISTER_URL}

A reminder of why parents choose us: it's on campus, right after school, beginner-friendly, and we actually teach the sport. If we don't deliver, you get a 100% refund, any time during the season.

If now isn't the right time, no problem — we'll be here next season.

The Discipline Rift Team
```
*After R3, stop the branch. Drop the contact into the long-term newsletter (see [[DR-Lead-Magnet-Sequence]]).*

---

## Implementation notes
- **#1 fires within seconds of payment** — not batched. This is the highest-leverage timing in the sequence.
- Countdown emails (#3–4) fire **only for the first session / season start.** Recurring per-session reminders live in [[DR-Season-Reminder-Sequence]].
- `{SPORT_SPECIFIC_ITEM}` pulls per sport (volleyball: knee pads optional; tennis/pickleball: none required; flag football: none required) — DR already stores sport data.
- QA every merge field with a test send before activation. Confirm `{ADD_TO_CALENDAR_URL}` and `{DASHBOARD_URL}` resolve.
- Cart-recovery SMS (R2) requires SMS opt-in captured during the started registration — if no consent, replace R2 with a second email.
