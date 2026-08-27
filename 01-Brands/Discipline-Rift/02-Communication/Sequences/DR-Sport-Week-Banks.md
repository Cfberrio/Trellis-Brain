---
brand: Discipline-Rift
area: communication
subarea: sequences
note_type: sequence
status: ready
used_for_ai: true
sensitivity: internal
owner: Luis
last_updated: 2026-08-04
sequence: sport-week-banks
audience: parent
channel: [email]
related_notes:
  - "[[DR-Season-Reminder-Sequence]]"
  - "[[DR-Coach-Communication-Chain]]"
  - "[[../DR-Communication-Engine]]"
---

# DR Sport Week Banks

The weekly parent email, built once per sport. [[DR-Season-Reminder-Sequence]] defines the **structure** (weeks 1–6, week 4 = the emotional peak, week 6 = close and re-enroll) and carries the volleyball copy. This note carries the banks for the other sports.

**Why this exists:** before it, volleyball parents got six in-season touchpoints and tennis, pickleball, and flag-football parents got none. Same price, same season, same promise — one third of the families heard from us weekly and the rest went dark after the countdown.

- **One row per week feeds two emails.** The coach's Week {N} plan ([[DR-Coach-Communication-Chain]] C6) and the parent's Week {N} update pull from the same row. The parent hears about the skill the coach actually taught that week.
- **Merge syntax:** `{UPPERCASE}`. Every email uses `{STUDENT_FIRST_NAME}` in the subject.
- **Fixed elements in every week:** the school named, the coach named, one skill, one at-home question.

---

## Week-row master table

| Sport | W1 | W2 | W3 | W4 (peak) | W5 | W6 (close) |
|---|---|---|---|---|---|---|
| **Volleyball** | Passing & Setting | Serving | Attacking | Defending | Moving | Communicating |
| **Flag Football** | Throwing & Catching | Catching & Communication | Ball Carrying & Flag Pulling | Ball Carrying & QB Handoff | Handoffs & Running Lanes | Play Action & 4th Down |
| **Tennis** | Forehands | Backhands | Volleys | Serves | Full-stroke review | Assessment |
| **Pickleball** | — | — | — | — | — | — |

> **Volleyball copy** lives in [[DR-Season-Reminder-Sequence]]. Not duplicated here.
>
> **Pickleball is blocked.** `Training/By-Sport/Pickleball/` contains a home note stating no curriculum was ever imported: *"no pickleball PDFs were present in the imported archive."* A pickleball bank cannot be written without inventing a curriculum DR does not teach. **Unblock:** supply the 6-week pickleball skill progression (the coach running it already has one in practice), then this bank takes about an hour. Until then pickleball parents should receive the **generic fallback** at the bottom of this note — not silence.

---

# Flag Football — Weeks 1–6

Cues and themes below are taken verbatim from `Training/By-Sport/Flag-Football/Source-Docs/Week-1` through `Week-6`. The coach is already saying these words at practice. Putting the same words in the parent's inbox is what makes a parent's question at dinner land.

| Week | Focus | Cue of the week | Theme |
|---|---|---|---|
| 1 | Throwing & Catching | "STEP to your target" | Discipline creates freedom. Scrimmage is earned. |
| 2 | Catching & Communication | "Diamond hands at chest" | If you're out, you're on a job. |
| 3 | Ball Carrying & Flag Pulling | "Eyes on hips" | Defense drives confidence. |
| 4 | Ball Carrying & QB Handoff | "Tuck and lock it away" | Reset fast. |
| 5 | Handoffs & Running Lanes | "Inside elbow up" | Play fast, stay organized. |
| 6 | Play Action & 4th Down | "Sell the fake" | Strategy makes us hard to guard. |

---

## FF Week 1 · Welcome to the season

**Subject:** {STUDENT_FIRST_NAME}'s first flag football session is done

```
Hi {PARENT_FIRST_NAME},

Week 1 is underway. {STUDENT_FIRST_NAME} is on the field at {SCHOOL_NAME} with
Coach {COACH_NAME}.

This week: throwing and catching.
The cue coaches repeated all practice was "STEP to your target" — the throw starts with
the opposite foot, not the arm. On the catching side, diamond hands for anything at chest
height or above.

Coaches also spent the first few minutes on what discipline actually means here. Most kids
assume it means punishment. We tell them it's the power to commit to a decision and follow
through. That framing runs the whole season.

At home this week: ask {STUDENT_FIRST_NAME}, "What does STEP to your target mean?"
If they can show you, they had a good first practice.

One thing worth knowing: practice is 60 minutes and every minute is planned. Scrimmage is
earned by working — that's the deal the coaches make with them on day one, and the kids
buy in fast.

See you next week,
The Discipline Rift Team
```

## FF Week 2 · Building momentum

**Subject:** Week 2: what {STUDENT_FIRST_NAME} is working on

```
Hi {PARENT_FIRST_NAME},

Two weeks in at {SCHOOL_NAME}.

This week: catching and communication.
Cue: "diamond hands at chest." Lots of reps — the goal is that catching stops being a
thing they think about.

The communication half matters more than it sounds. Every rep this week has a callout
built into it, because a player who can't talk on the field can't play with anyone else.
Quiet players get found fast in flag football, and they grow fast.

At home: ask what their "job" is when they're out of a rep. There's an answer — coaches
run it as "if you're out, you're on a job," so nobody stands around.

Keep it up,
The Discipline Rift Team
```

## FF Week 3 · Midpoint

**Subject:** Halfway there — what the coaches are seeing

```
Hi {PARENT_FIRST_NAME},

Midpoint at {SCHOOL_NAME}.

This week: ball carrying and flag pulling.
Cue: "eyes on hips." Not the ball, not the face — hips, because hips can't lie about which
way someone's going.

Coaches teach defense here for a specific reason: at this age, defense is what builds
confidence. A kid who can stop somebody stops being afraid of the game. The season mantra
is three steps — slow down, stay between, pull the flag.

{STUDENT_FIRST_NAME} is right on track.

Coming in the second half: handoffs, running lanes, and the strategy that ties it together.

The Discipline Rift Team
```

## FF Week 4 · Recognition — the peak

**Subject:** Something we noticed about {STUDENT_FIRST_NAME}

```
Hi {PARENT_FIRST_NAME},

Week 4 is when players come into their own, and it's showing at {SCHOOL_NAME}.

This week: ball carrying and the QB handoff.
Cue: "tuck and lock it away." Secure the ball first, then run. The effort norm coaches are
holding them to is "reset fast" — jog back, eyes up, ready before the whistle.

Four weeks ago most of this group had never run a play. This week they're taking a handoff
after a whistle and protecting the ball while somebody chases them. That's a real jump,
and it's worth saying out loud at home.

You're investing in something that matters. We see it — and we think you're starting to
see it at home too.

Got a photo or a proud moment from this season? Reply and send it. We'd love to see it. 📸

The Discipline Rift Team
```

## FF Week 5 · Final stretch

**Subject:** One week left — what to expect for the finale

```
Hi {PARENT_FIRST_NAME},

Final week is coming up at {SCHOOL_NAME}.

This week: handoffs and running lanes.
Cue: "inside elbow up" — the runner makes a pocket, the QB places the ball in it. Theme is
play fast, stay organized, which is harder than it sounds when eleven kids are excited.

{END_OF_SEASON_DETAIL}

Coach {COACH_NAME} will also complete end-of-season tier assessments this week, so you'll
see where {STUDENT_FIRST_NAME} finished.

{STUDENT_FIRST_NAME} should be proud of this season.

See you at the finish,
The Discipline Rift Team
```

## FF Week 6 · Season close + re-enroll

**Subject:** Season's done — here's what's next for {STUDENT_FIRST_NAME}

```
Hi {PARENT_FIRST_NAME},

The season's wrapped, and {STUDENT_FIRST_NAME} put in a good one.

Last week: play action and 4th down.
Cue: "sell the fake." Theme: strategy makes us hard to guard. It's the week where the game
stops being about who's fastest and starts being about who's thinking.

Where they finished:
{TIER_SUMMARY}

What's next: finishing this season means {STUDENT_FIRST_NAME} advances to the next tier.
Next season's teams at {SCHOOL_NAME} are opening now, and they fill fast.

[ Re-enroll {STUDENT_FIRST_NAME} for next season ] → {REGISTER_URL}
Early re-enrollment closes {REENROLL_DEADLINE}. Two kids? Use code SIBLING for 10% off.

One quick favor: if this season was a good one, a short review helps another parent decide.
[ Leave a review ] → {REVIEW_URL}

It's been a pleasure having {STUDENT_FIRST_NAME} on the field. Hope to see them next season.

The Discipline Rift Team
```

---

# Tennis — Weeks 1–6

**Ordering note:** the tennis source docs are unnumbered PDF extracts. The sequence below is inferred from their titles, which are cumulative — each adds one stroke and reviews the prior ones, ending in an assessment week. `[CONFIRM WITH TENNIS LEAD before first send.]`

**Cue note:** unlike flag football, the tennis source material carries no "cue of the week." Rather than invent cues, these emails run on the skill focus. If the tennis lead supplies a one-line cue per week, add it — it is the strongest at-home device in the flag football set.

| Week | Focus | Source doc |
|---|---|---|
| 1 | Forehands | `Week-Forehands` |
| 2 | Backhands (forehand review) | `Week-Backhands-and-Forehands-Review` |
| 3 | Volleys (forehand + backhand review) | `Week-Volleys-Forehands-and-Backhands-Review` |
| 4 | Serves (forehand + backhand review) | `Week-Serves-Forehands-and-Backhands-Review` |
| 5 | Full-stroke review | `Week-Forehands-Backhands-Volleys-and-Serves-Review` |
| 6 | Assessment | `Week-Forehands-Backhands-Volleys-and-Serves-Assessment` |

---

## TN Week 1 · Welcome to the season

**Subject:** {STUDENT_FIRST_NAME}'s first tennis session is done

```
Hi {PARENT_FIRST_NAME},

Week 1 is underway. {STUDENT_FIRST_NAME} is on the court at {SCHOOL_NAME} with
Coach {COACH_NAME}.

This week: forehands. It's the first stroke we teach because it's the one they'll hit most,
and getting it repeatable early makes everything after it easier.

Coaches opened by asking the group what discipline means. Most kids guess it means
punishment. We tell them it's the power to commit to a decision and follow through — and
then we spend six weeks proving it with a racket.

At home this week: ask {STUDENT_FIRST_NAME} to show you a forehand. No court needed. The
shape of the swing is the whole thing at this stage.

A note on how the season runs: same day, same court, same structure every week. Predictable
is the point — it's what lets a beginner relax enough to actually learn.

See you next week,
The Discipline Rift Team
```

## TN Week 2 · Building momentum

**Subject:** Week 2: what {STUDENT_FIRST_NAME} is working on

```
Hi {PARENT_FIRST_NAME},

Two weeks in at {SCHOOL_NAME}.

This week: backhands — plus continued forehand reps, because nothing gets dropped once
it's introduced. Every week from here adds one stroke and reviews everything before it.

The backhand is the one that frustrates beginners. It feels wrong for about two practices
and then it clicks. If {STUDENT_FIRST_NAME} comes home saying it's hard, that's the
expected week to hear it.

At home: ask what felt easier this week than last week. Something usually did.

Keep it up,
The Discipline Rift Team
```

## TN Week 3 · Midpoint

**Subject:** Halfway there — what the coaches are seeing

```
Hi {PARENT_FIRST_NAME},

Midpoint at {SCHOOL_NAME}.

This week: volleys, with forehands and backhands still in rotation.

Volleys are where the game gets fast. Players move forward instead of waiting, and they
have to make a decision in about half a second. It's the week where kids who were hanging
back start committing.

{STUDENT_FIRST_NAME} is right on track.

Coming in the second half: serves, then a full review of every stroke, then assessment week.

The Discipline Rift Team
```

## TN Week 4 · Recognition — the peak

**Subject:** Something we noticed about {STUDENT_FIRST_NAME}

```
Hi {PARENT_FIRST_NAME},

Week 4 is when players come into their own, and it's showing at {SCHOOL_NAME}.

This week: serves. It's the only shot in tennis nobody else can affect — no opponent, no
excuse, just the player and the toss. That makes it the most nerve-testing thing we ask
of them all season, and also the most satisfying when it lands.

Four weeks ago, most of this group had never held a racket properly. This week they're
serving. Worth saying out loud at home.

You're investing in something that matters. We see it — and we think you're starting to
see it at home too.

Got a photo or a proud moment from this season? Reply and send it. We'd love to see it. 📸

The Discipline Rift Team
```

## TN Week 5 · Final stretch

**Subject:** One week left — what to expect for the finale

```
Hi {PARENT_FIRST_NAME},

Final week is coming up at {SCHOOL_NAME}.

This week: everything together — forehands, backhands, volleys, and serves in live rally
play. It's the first week the sport looks like tennis rather than drills, and it's usually
the week the kids enjoy most.

{END_OF_SEASON_DETAIL}

Coach {COACH_NAME} will also complete end-of-season tier assessments this week, so you'll
see where {STUDENT_FIRST_NAME} finished.

{STUDENT_FIRST_NAME} should be proud of this season.

See you at the finish,
The Discipline Rift Team
```

## TN Week 6 · Season close + re-enroll

**Subject:** Season's done — here's what's next for {STUDENT_FIRST_NAME}

```
Hi {PARENT_FIRST_NAME},

The season's wrapped, and {STUDENT_FIRST_NAME} put in a good one.

Final week was assessment — every stroke, measured against where they started. Not a test
they can fail. A record of what changed in six weeks.

Where they finished:
{TIER_SUMMARY}

What's next: finishing this season means {STUDENT_FIRST_NAME} advances to the next tier.
Next season's teams at {SCHOOL_NAME} are opening now, and they fill fast.

[ Re-enroll {STUDENT_FIRST_NAME} for next season ] → {REGISTER_URL}
Early re-enrollment closes {REENROLL_DEADLINE}. Two kids? Use code SIBLING for 10% off.

One quick favor: if this season was a good one, a short review helps another parent decide.
[ Leave a review ] → {REVIEW_URL}

It's been a pleasure having {STUDENT_FIRST_NAME} on the court. Hope to see them next season.

The Discipline Rift Team
```

---

# Generic fallback — any sport without a bank

Use for pickleball until its curriculum exists, and for any new sport in its first season. Sport-agnostic, so it never claims a skill DR didn't teach. It is thinner than a real bank — treat it as a stopgap, not a solution.

**Subject:** Week {WEEK_NUMBER}: how {STUDENT_FIRST_NAME}'s season is going

```
Hi {PARENT_FIRST_NAME},

Week {WEEK_NUMBER} at {SCHOOL_NAME} with Coach {COACH_NAME}.

This week coaches focused on {WEEK_FOCUS_FREETEXT}.

At home: ask {STUDENT_FIRST_NAME}, "What's one thing that felt easier today than last week?"
It's specific enough that they can't answer "fine," and it teaches them to notice their own
progress instead of waiting to be told.

{STUDENT_FIRST_NAME} is right on track.

See you next week,
The Discipline Rift Team
```

`{WEEK_FOCUS_FREETEXT}` comes from the coach's session log for that week. If the log is empty, **do not send** — a weekly update that says nothing specific is worse than no weekly update.

---

## Implementation notes

- **Build order:** flag football first (curriculum is complete and cue-based, so the emails are strongest), tennis second (confirm ordering first), pickleball when curriculum lands.
- **One row, two audiences.** Any edit to a week row updates both the coach plan and the parent email. Do not let them drift — a parent asking about a cue the coach never said is worse than a generic email.
- **Week 4 and Week 6 are the engineered moments** per [[../DR-Communication-Engine]] §7. Week 4 captures the photo, Week 6 captures the review and the re-enrollment. Do not ship a bank with those two weeks trimmed for length.
- **`{REENROLL_DEADLINE}` must be a real date.** Do not ship Week 6 without it — an urgency line with no date reads as a template.
- **Tennis ordering needs a human confirm** before the first send. Everything else here is source-grounded.
