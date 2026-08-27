---
brand: Discipline-Rift
area: communication
note_type: manual
status: active
canonical: true
used_for_ai: true
source_type: curated
sensitivity: internal
owner: Luis
last_updated: 2026-07-23
supersedes: "n8n automation model in communication-rules.md (§3 variables, §7 channel logic)"
related_notes:
  - "[[Sequences/DR-Registration-Sequence]]"
  - "[[Sequences/DR-Lead-Magnet-Sequence]]"
  - "[[Sequences/DR-Season-Reminder-Sequence]]"
  - "[[communication-rules]]"
---

# DR Communication Engine

**One document format, one merge syntax, one set of rules — for every message DR sends a parent.**

This replaces the scattered n8n model. n8n is retired. Email and SMS now go out from DR's own stack (the same sender that powers the admin campaign tool). Each *sequence* lives in one document: a numbered table at the top, full copy below. Anyone can open one file and see every message, when it fires, and on which channel.

## The three sequences

| Sequence | Covers | Document |
|---|---|---|
| **Registration** | From "just paid" → first practice, plus recover-the-cart | [[Sequences/DR-Registration-Sequence]] |
| **Lead Magnet** | Guide download / newsletter opt-in → registration | [[Sequences/DR-Lead-Magnet-Sequence]] |
| **Season Reminder** | Weekly in-season nurture + per-session reminders + close & re-enroll | [[Sequences/DR-Season-Reminder-Sequence]] |

Every sequence document uses the **same table**:

| # | Step | Email | SMS | Trigger |
|---|---|---|---|---|

- **#** — communication number (0, 1, 2 …). Start at 0.
- **Step** — plain-language name of the message.
- **Email** — the subject line if email is used; `—` if not.
- **SMS** — `✓` if a text is used (the copy is in the detail block); `—` if not.
- **Trigger** — the exact event or timing that fires it.

Full email body + full SMS copy for each row live in numbered detail blocks under the table.

---

## Channel philosophy — email carries the load, SMS is a scalpel

DR's brand rule is warmth through clarity, not volume. **Email is the primary channel.** SMS is reserved for messages that are *time-sensitive AND high-value AND expected* — because a text interrupts, and interruption is a cost.

**Send an SMS only when at least two are true:**
1. It's time-sensitive (happens in <24h, or the window to act is closing).
2. Missing it has a real cost to the parent (missed first practice, lost spot, forgotten pickup change).
3. The parent would thank you for the interrupt, not resent it.

**Never SMS for:** weekly nurture, recognition, general updates, anything that can wait for the inbox.

Across the whole registration journey a parent should receive **~3 texts, not 10**: an instant booking confirmation, a day-before-first-practice nudge, and (only if they stalled) one cart-recovery text. That's the ceiling.

> This supersedes the old rule in `communication-rules.md` §7 ("No DR communication currently uses SMS as a primary channel"). SMS is now a real, sanctioned channel — governed by the scalpel test above, not banned.

---

## Merge-field syntax — pick ONE and standardize

The codebase currently has **two** syntaxes fighting each other:
- n8n emails: `{{ $json.firstname }}`
- Admin campaign tool: `{PARENT_NAME}`, `{STUDENT_NAME}`
- Registration-confirmation server template: `${STUDENT_FIRST_NAME}`

**Go-forward canonical = single-brace UPPERCASE `{FIELD_NAME}`** (matches the admin campaign tool, which is now the sender of record). Normalize the old `{{ $json.x }}` and `${X}` templates to this.

### Canonical variable dictionary

| Variable | Contains | Example |
|---|---|---|
| `{PARENT_FIRST_NAME}` | Parent first name | Maria |
| `{STUDENT_FIRST_NAME}` | Child first name | Sofia |
| `{STUDENT_LAST_NAME}` | Child last name | Gonzalez |
| `{GRADE}` | Child's grade | 3rd |
| `{SPORT}` | Volleyball / Tennis / Pickleball / Flag Football | Volleyball |
| `{TEAM_NAME}` | Team name | Deerwood Volleyball |
| `{SCHOOL_NAME}` | Host school | Deerwood Elementary |
| `{SCHOOL_LOCATION}` | Address / campus | 123 Deerwood Rd |
| `{COACH_NAME}` | Assigned coach | Coach Santiago |
| `{PRACTICE_SCHEDULE}` | Rendered schedule block (replaces `scheduleHtml` / `PRACTICE_OCCURRENCES`) | (table) |
| `{FIRST_PRACTICE_DATE}` | First session date | Fri, Sep 12 |
| `{FIRST_PRACTICE_TIME}` | First session time | 3:15–4:15 PM |
| `{SEASON_START_DATE}` / `{SEASON_END_DATE}` | Season window | Sep 12 / Oct 24 |
| `{AMOUNT}` | Amount paid | $129.00 |
| `{PAYMENT_DATE}` | Payment date | Jul 23, 2026 |
| `{DASHBOARD_URL}` | Parent dashboard login | … |
| `{REGISTER_URL}` | Registration flow | disciplinerift.com/register |
| `{SCHOOL_SEARCH_URL}` | Find-your-school search | … |
| `{ADD_TO_CALENDAR_URL}` | One-tap add first practice to calendar | … |
| `{REVIEW_URL}` | Google review link | … |
| `{OTP_CODE}` | One-time verification code | 482910 |
| `{UNSUBSCRIBE_URL}` | Email opt-out | … |

**Rules:** always set a fallback (`{PARENT_FIRST_NAME}` → "there" when empty). Never render a raw variable to a parent — QA every merge field before a sequence goes live. Times render in **America/New_York**.

---

## Areas of improvement — marketing lens

Grounded in the DR brand and the marketing frameworks (`/lead-nurture`, `/marketing-psychology`, `/money-models`, `/offers`, `/lead-magnets`, `/marketing-machine`). Each item is a change, not a theory.

### 1. Speed & front-loading (Lead Nurture — Volume)
The single most under-used lever. Two fixes:
- **Booking confirmation must fire within seconds of payment**, not on a batch. The moment after paying is when doubt is highest — close the loop instantly.
- **Cart recovery must be front-loaded**: hour 1, day 1, day 3 — not a slow drip. Schedule probability decays with the log of elapsed time; days 0–2 hold most of the recoverable registrations.

### 2. Kill post-purchase doubt with risk reversal (Offers)
The booking confirmation currently just lists what they bought. It should also **restate the Value Guarantee** ("100% refund, any time during the season") right there. That one line converts a nervous first-time parent's *"did I just waste $129?"* into *"I'm covered — good."* Risk reversal works hardest at the moment money leaves the account.

### 3. Plant the continuity seed early (Money Models)
DR's real model is **re-enroll every season → advance a Tier**. That's continuity, and continuity revenue is decided long before the season ends. So:
- Frame the season at confirmation as **"Tier 1 of the journey — finish it and {STUDENT_FIRST_NAME} advances,"** not a one-off purchase.
- Surface the **`SIBLING` 10% code** in the booking confirmation — the cheapest cross-sell DR has is the second kid in the same house, and the buying moment is *now*, not next season.
- The season-close email is the highest-intent re-enroll moment in the whole calendar (peak sentiment). Treat it as a conversion event with a deadline, not a goodbye.

### 4. Turn the season into a testimonial machine (Marketing Machine)
The 6-week season *is* a UGC/lifecycle engine if you build capture into the comms:
- **Before** (nervous first-timer) and **after** (smiling, progressing) is DR's best-proven ad story — the emails should ask for it. Week 1 plants the "what felt easier today?" habit (from the parent guide); Week 4 recognition and season-close ask for a photo/one-line win.
- **Season-close = the review ask** at peak sentiment (`{REVIEW_URL}`). A review requested the day after a proud finish converts far above a cold request.

### 5. Personalization > volume (Lead Nurture — Personalization)
Same touch count, opposite outcome depending on relevance:
- Every subject line uses **`{STUDENT_FIRST_NAME}`** — the parent's primary reference point.
- Reminders name the **specific coach, school, and schedule** — "generic reminder" reads as spam; "Coach Santiago, Friday at Deerwood" reads as a program that has its act together.
- SMS: **multiple short lines beat one block** — reads human, not automated.

### 6. Reciprocity before the ask (Lead Magnets)
The 5 Parent Guides are a reciprocity asset DR isn't fully using. The lead-magnet sequence should **give a usable guide in nearly every email before it ever asks for a registration** — the "one question after practice," the "4 red flags," the age checklist. Each one also *reframes what a good program looks like* — and DR happens to be the answer. Give value, earn the ask.

### 7. Peak-End & loss aversion (Marketing Psychology)
- **Peak-End:** parents remember two moments — the emotional peak and the ending. Engineer them: Week 4 recognition = the peak; season-close = the ending. Both should feel personal and proud, because that memory is what drives re-enrollment and word-of-mouth.
- **Loss aversion:** cart recovery says **"your spot is still held — but the team is filling"** (not "come back"). A held spot about to be lost pulls harder than a discount.
- **Commitment/consistency:** the countdown emails (30/7/1-day) aren't just logistics — each one re-confirms the decision and makes backing out feel like undoing something already true.

### 8. Availability & the reminder-to-show layer (Lead Nurture — Availability + Volume)
Show rate is the cheapest revenue in the business, and DR's version of "show" is **the child actually attends the first practice.** So:
- Booking confirmation includes a **one-tap add-to-calendar** for the first practice.
- The 30/7/1-day countdown is the **automated reminder-to-show layer**; the day-before SMS is the **manual, human-feel layer** ("Coach Santiago's ready — see {STUDENT_FIRST_NAME} tomorrow"). Both lift attendance; both are needed.

### 9. Fatigue discipline (operational)
- **Do NOT fire 30/7/1-day reminders for every session** — only for the **first session / season start**. During the season, one light day-before reminder per session is plenty. Firing three countdowns per session would train parents to ignore DR.
- One SMS per parent per day, hard cap. Quiet hours **9 AM–6 PM ET**.

---

## Compliance (now that SMS is real)

SMS was cosmetic before; now it ships. Non-negotiables:
- **A2P 10DLC** campaign registration on the sending number **before** any texting at scale. `[CONFIRM STATUS — owner: dev]`
- **Explicit SMS opt-in** captured at registration and at popup (separate checkbox, not pre-checked). The registration Step-3 consent line already exists ("Text and email me season updates and my child's weekly progress") — split it into its own SMS checkbox.
- **STOP / HELP** honored automatically; **quiet hours 9 AM–6 PM ET**; **≤1 marketing SMS per parent per day.**
- Every marketing **email** carries `{UNSUBSCRIBE_URL}`.
- Transactional messages (OTP, booking confirmation, day-before-practice safety logistics) are exempt from marketing-consent gating but still respect STOP.

## Bugs to clear before go-live (carried from communication-rules §9)
1. 30-day & 7-day reminder banners still say "1-Day Reminder" — fix labels.
2. Coach reminder renders `json.name` literally — fix to `{COACH_NAME}`.
3. Application confirmation opens "Hi name," — wire `{FIRST_NAME}`.
4. Registration-confirmation template still uses `${X}` — normalize to `{X}`.

---

*Source of truth for how DR talks to parents. Update this file first, then the sequence docs.*
