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
sequence: season-reminder
channel: [email, sms]
related_notes:
  - "[[../DR-Communication-Engine]]"
  - "[[../Templates/Parent-Communication-Volleyball-Season]]"
---

# DR Season Reminder Sequence

Every message **during** the season — the weekly parent nurture, the light per-session reminder, the attendance note, and the season-close → re-enroll conversion. Runs after [[DR-Registration-Sequence]] hands off at the first practice.

- **Two layers run in parallel:** (A) the **weekly nurture** email (keeps parents bought in, week 1→6) and (B) the **per-session reminder** (light, operational).
- **Fatigue rule:** the heavy 30/7/1-day countdown belongs to the *first* practice only ([[DR-Registration-Sequence]]). In-season, one **light day-before reminder** per session — SMS reserved for **same-day changes only**.
- **Sport note:** the weekly copy below is the **volleyball** set (weeks 1–6). Tennis, pickleball, and flag football need parallel 6-week banks — same structure, sport-specific skills. Build the message bank once per sport (see notes).
- **Peak-End:** Week 4 = the emotional peak; Week 6 = the ending. Engineer both. Merge syntax `{UPPERCASE}`.

---

## A. Weekly parent nurture (email, 1×/week)

| # | Step | Email | SMS | Trigger |
|---|---|---|---|---|
| 0 | Week 1 — welcome to the season | *{STUDENT_FIRST_NAME}'s first session is done — here's how it went* | — | Day of / after first session |
| 1 | Week 2 — building momentum | *Week 2: what {STUDENT_FIRST_NAME} is working on* | — | Start of week 2 |
| 2 | Week 3 — midpoint check-in | *Halfway there — what the coaches are seeing* | — | Start of week 3 |
| 3 | Week 4 — recognition (the peak) | *Something we noticed about {STUDENT_FIRST_NAME}* | — | Start of week 4 |
| 4 | Week 5 — final stretch | *One week left — what to expect for the finale* | — | Start of week 5 |
| 5 | Week 6 — season close + re-enroll | *Season's done — here's what's next for {STUDENT_FIRST_NAME}* | — | Final week |

## B. Operational (recurring / as-needed)

| # | Step | Email | SMS | Trigger |
|---|---|---|---|---|
| P | Per-session reminder (light) | *{STUDENT_FIRST_NAME} has {SPORT} tomorrow* | ✓ *(same-day change only)* | 1 day before each session |
| N | Attendance note | *A note about {STUDENT_FIRST_NAME}'s session* | — | Student marked absent |
| RE | Re-enroll reminder | *{STUDENT_FIRST_NAME}'s next tier is open* | ✓ | 3 days post-close, if not re-enrolled |

---

# Full copy — weekly nurture

*(Volleyball set. Structure is fixed; swap the sport-specific skill lines for other sports.)*

## 0 — Week 1 · Welcome to the season · Email
Closes the loop on the first session; gives the parent a conversation starter; sets the weekly cadence.

**Subject:** {STUDENT_FIRST_NAME}'s first session is done — here's how it went

```
Hi {PARENT_FIRST_NAME},

Week 1 is officially underway. We're glad {STUDENT_FIRST_NAME} is on the court.

This week, coaches focused on:
• Passing & setting — the foundations of ball control and teamwork
• A team warm-up and getting-to-know-you activity
• A first baseline so we can track progress over the season

At home this week: ask {STUDENT_FIRST_NAME}, "What's one thing that felt easier today than before?" It's how kids start noticing their own growth.

See you next week,
The Discipline Rift Team
```

## 1 — Week 2 · Building momentum · Email
Sets a forward milestone so parents feel a progression, not just attendance.

**Subject:** Week 2: what {STUDENT_FIRST_NAME} is working on

```
Hi {PARENT_FIRST_NAME},

Two weeks in and the energy's been great.

This week's focus: serving — control and consistency, so players feel confident starting a rally.

Coaches are tracking early progress on ball control. By Week 4, most players see a noticeable jump here.

Keep it up,
The Discipline Rift Team
```

## 2 — Week 3 · Midpoint check-in · Email
Reassurance ("on track") + what's ahead.

**Subject:** Halfway there — what the coaches are seeing

```
Hi {PARENT_FIRST_NAME},

We're at the midpoint, and here's what coaches are seeing across the group: players are getting to the ball faster and communicating more.

Coming in the second half:
• Attacking — sending the ball over with purpose
• Defending — keeping the ball alive

{STUDENT_FIRST_NAME} is right on track.

The Discipline Rift Team
```

## 3 — Week 4 · Recognition (the peak) · Email
**The emotional anchor of the whole season.** Make the parent feel the investment was worth it. This is also the first testimonial-capture moment.

**Subject:** Something we noticed about {STUDENT_FIRST_NAME}

```
Hi {PARENT_FIRST_NAME},

Week 4 is when players really start to come into their own — and {STUDENT_FIRST_NAME} is showing it. Consistency and confidence are up, and it shows on the court.

This week coaches are working on movement — getting to the ball, stopping with balance, recovering for the next play.

You're investing in something that matters. We see it — and we think you're starting to see it at home too.

Got a photo or a proud moment from this season? Reply and send it — we'd love to see it. 📸

The Discipline Rift Team
```

## 4 — Week 5 · Final stretch · Email
Logistics-forward — parents need to plan for any end-of-season moment.

**Subject:** One week left — what to expect for the finale

```
Hi {PARENT_FIRST_NAME},

Final week is coming up. This week players focus on communication — calling the ball, supporting teammates, playing as a unit.

{END_OF_SEASON_DETAIL}   (e.g., short season celebration at the last practice — date/time/location)

Coaches will also complete end-of-season tier assessments this week, so you'll see where {STUDENT_FIRST_NAME} finished.

{STUDENT_FIRST_NAME} should be proud of this season.

See you at the finish,
The Discipline Rift Team
```

## 5 — Week 6 · Season close + re-enroll (the ending) · Email
**The highest-intent re-enrollment moment on the calendar.** Peak sentiment + progress summary + a real deadline + the review ask. Treat it as a conversion event, not a goodbye.

**Subject:** Season's done — here's what's next for {STUDENT_FIRST_NAME}

```
Hi {PARENT_FIRST_NAME},

The season's officially wrapped — and {STUDENT_FIRST_NAME} put in a great one.

Where they finished:
{TIER_SUMMARY}   (tier reached / skill summary)

What's next: completing this season means {STUDENT_FIRST_NAME} advances to the next tier. The next season's teams are opening now, and they fill fast.

[ Re-enroll {STUDENT_FIRST_NAME} for next season ] → {REGISTER_URL}
Early re-enrollment closes {REENROLL_DEADLINE}. Two kids? Use code SIBLING for 10% off.

One quick favor: if this season was a good one, a short review helps another parent decide.
[ Leave a review ] → {REVIEW_URL}

It's been a pleasure having {STUDENT_FIRST_NAME} on the court. Hope to see them next season.

The Discipline Rift Team
```

---

# Full copy — operational

## P — Per-session reminder (light) · Email + (conditional SMS)
In-season, one light reminder the day before each session. **Do not** run the 30/7/1 stack per session. SMS **only** if the session changed same-day (time/location/cancellation).

**Subject:** {STUDENT_FIRST_NAME} has {SPORT} tomorrow

```
Hi {PARENT_FIRST_NAME},

Reminder — {STUDENT_FIRST_NAME} has {SPORT} practice tomorrow.

📅 {SESSION_DATE}, {SESSION_TIME}
📍 {SCHOOL_NAME}
🧑‍🏫 Coach {COACH_NAME}

See you there,
The Discipline Rift Team
```

**SMS — same-day change ONLY (cancellation / time / location):**
```
Discipline Rift: heads up — today's {SPORT} practice for {STUDENT_FIRST_NAME} is {CHANGE_DETAIL} (e.g., CANCELED due to weather / moved to 3:45).
Questions? Reply here. Reply STOP to opt out.
```

## N — Attendance note · Email
Sent when a student is marked absent. **Tone is supportive, never punitive.** Coach note must pass a QA/format step before it's allowed to merge into a parent email.

**Subject:** A note about {STUDENT_FIRST_NAME}'s session

```
Hi {PARENT_FIRST_NAME},

We missed {STUDENT_FIRST_NAME} at {SPORT} practice today.

We know things come up — schedules change, rides run late, school happens. If there was anything on our end that made it hard to get there, let us know so we can help.

Our goal is to keep every player progressing and feeling part of the team. You can reply here anytime.

See you at the next practice,
The Discipline Rift Team
```

## RE — Re-enroll reminder · Email + SMS
For families who didn't re-enroll at close. Fires ~3 days after season end. One email + one text, then stop (hand to newsletter).

**Subject:** {STUDENT_FIRST_NAME}'s next tier is open

```
Hi {PARENT_FIRST_NAME},

{STUDENT_FIRST_NAME} earned their spot in the next tier — and the next season's teams are filling now.

[ Re-enroll for next season ] → {REGISTER_URL}
Early re-enrollment closes {REENROLL_DEADLINE}.

Same court, same coaches, next level. Hope to see them back.

The Discipline Rift Team
```

**SMS:**
```
Discipline Rift: {STUDENT_FIRST_NAME}'s next {SPORT} season is open & filling. Re-enroll before {REENROLL_DEADLINE}: {REGISTER_URL}
Reply STOP to opt out.
```

---

## Implementation notes
- **Two parallel layers:** the weekly nurture (A) is about *belief and re-enrollment*; the per-session reminder (P) is about *showing up*. Don't merge them.
- **Sport banks:** only volleyball weeks 1–6 exist. Build tennis, pickleball, and flag football banks once, review once, reuse every season (see `/marketing-machine` — a message bank removes weekly writing pressure and keeps voice consistent). Weekly skill lines per sport come from the Programs tier data DR already stores.
- **Pause/resume:** if a session cancels or reschedules, the weekly cadence must pause/resume so Week 3 content doesn't land while parents are still on Week 2.
- **Testimonial capture:** Week 4 ("send us a proud moment") and Week 6 (`{REVIEW_URL}`) are the two capture points — feed replies/photos into the marketing UGC library.
- **Re-enroll deadline** must be a real date to create urgency — don't ship #5/RE without `{REENROLL_DEADLINE}` set.
- Attendance-note coach input needs a QA step — "didn't show up" is not a parent-ready sentence.
