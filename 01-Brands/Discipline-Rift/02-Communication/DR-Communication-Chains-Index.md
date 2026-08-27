---
brand: Discipline-Rift
area: communication
note_type: index
status: active
canonical: true
used_for_ai: true
owner: Luis
last_updated: 2026-08-04
sensitivity: internal
hub_role: hub
supersedes: "Template index in communication-rules.md §4"
related_notes:
  - "[[DR-Communication-Engine]]"
  - "[[DR-Communication-Audit-2026-08-04]]"
---

# DR Communication Chains — Index

Every chain DR runs, in one table. [[DR-Communication-Engine]] is the rulebook (voice, channel, merge syntax, compliance); this is the map of what exists, what ships, and what's blocked.

---

## The five chains

| # | Chain | Audience | Messages | Status | Document |
|---|---|---|---|---|---|
| 1 | **Lead Magnet** | Prospective parent | 6 email + 2 SMS | Written, unshipped | [[Sequences/DR-Lead-Magnet-Sequence]] |
| 2 | **Registration** | Registering parent | 6 email + 3 SMS + 3 recovery | Written, unshipped | [[Sequences/DR-Registration-Sequence]] |
| 3 | **Season** | Enrolled parent | 6 weekly + 3 operational | Volleyball written; **banks new** | [[Sequences/DR-Season-Reminder-Sequence]] |
| 4 | **Coach lifecycle** | Coach | 11 | **New — built 2026-08-04** | [[Sequences/DR-Coach-Communication-Chain]] |
| 5 | **Sport week banks** | Enrolled parent | 12 written, 6 blocked | **New — built 2026-08-04** | [[Sequences/DR-Sport-Week-Banks]] |

**Total designed:** ~55 messages. **Total live today:** 14, none of which carry the guarantee, the tier, the school pairing, or the "55 schools" proof.

---

## Full journey map

```
PROSPECT
  opts in (popup / guide / QR)      → Chain 1 · Lead Magnet (6 emails, guide-per-email)
  goes quiet after #5                → monthly newsletter

REGISTERING
  starts, doesn't pay                → Chain 2 · Recovery R1 (+1h) → R2 (+24h) → R3 (+72h) → stop
  pays                               → Chain 2 · Confirmation (seconds) → get-ready → 30d → 7d → 1d

IN SEASON
  weekly, weeks 1–6                  → Chain 3 structure × Chain 5 sport bank
  day before each session            → Chain 3 · light reminder
  player absent                      → Chain 3 · attendance note
  session changes same-day           → Chain 3 · SMS (the only same-day text)

SEASON CLOSE
  final session                      → Chain 3/5 · Week 6 — tier result + re-enroll + review
  didn't re-enroll                   → Chain 3 · RE reminder (+3 days), then newsletter

COACH (parallel, all season)
  applies                            → Chain 4 · C0 → C1 accept / C2 decline (human)
  hired                              → C3 onboarding → C4 assignment → C5 week-before
  each week                          → C6 session plan (same row as the parent's Week N)
  forgets to log                     → C7 reminder
  schedule changes                   → C8
  week 3                             → C9 check-in (two-way)
  season ends                        → C10 close + next-season availability
```

---

## What is new in this build

**Chain 4 — Coach lifecycle.** Did not exist. Coaches previously received exactly one automated message: a reminder that they had failed to log a session. Eleven messages now cover application through season close, including the two that were most conspicuously missing — a decision on their application, and a weekly session plan.

**Chain 5 — Sport week banks.** Flag football and tennis weekly parent emails, 12 total, grounded in the actual curriculum in `Training/By-Sport/`. Before this, only volleyball parents heard from DR in-season.

**The C6 ↔ Week N link.** The coach's weekly plan and the parent's weekly email now draw from the same week row. When a parent asks their kid about "eyes on hips" at dinner, the coach said those exact words at practice that afternoon. That link is the thing that makes a weekly email feel like a program rather than a mail merge.

---

## Blocked

| Item | Blocker | Unblock |
|---|---|---|
| **Pickleball week bank** | No curriculum exists. `Pickleball-Home.md`: *"no pickleball PDFs were present in the imported archive."* | Supply the 6-week skill progression the coach already runs. ~1 hour to write once provided. Until then, pickleball parents get the **generic fallback** in [[Sequences/DR-Sport-Week-Banks]] — not silence. |
| **Tennis week ordering** | Source docs are unnumbered PDF extracts; sequence inferred from cumulative titles | Tennis lead confirms the order. 5 minutes. |
| **Tennis cues** | Source material carries no "cue of the week" | Tennis lead supplies one line per week. Optional but it is the strongest at-home device in the flag football set. |
| **Coach dashboard URL** | Live template sends a raw Vercel preview hostname | Move to a DR subdomain, set `{COACH_DASHBOARD_URL}` |
| **Roster / director data on coach record** | Unconfirmed whether it exists | Dev confirm — C4 cannot fire without it |
| **A2P 10DLC registration** | Unconfirmed | Required before any SMS in chains 1–3 ships at scale |

---

## Ship order

Sequenced by revenue impact and dependency, not by chain number.

| Phase | Ship | Why first |
|---|---|---|
| **1 — Copy only, no engineering** | Guarantee line into registration confirmation + 7-day + season close. Fix `Hi name,` and the internal note in the 1-day reminder. | Zero dependencies. The guarantee is DR's strongest asset and appears nowhere. |
| **2 — Merge fields** | `{STUDENT_FIRST_NAME}` into all weekly and countdown emails | Highest impact-to-effort in the audit. No new messages, no new triggers. |
| **3 — The measurement fix** | Chain 3/5 Week 6 — tier result, re-enroll link, real deadline, review ask | Until this ships, re-enrollment rate is uninterpretable and DR cannot tell a virtuous cycle from a vicious one. This is the brand's primary instrument. |
| **4 — The revenue leak** | Chain 2 recovery — R1 / R2 / R3 | Only item with directly recoverable dollars. Currently a parent who starts and doesn't pay hears nothing, ever. |
| **5 — The coach gap** | Chain 4, starting with C6 (weekly plan) and C0/C1/C2 (application outcomes) | C6 is load-bearing: without it the parent weekly email may describe a skill the coach didn't teach. |
| **6 — Sport coverage** | Chain 5 flag football, then tennis | Ends volleyball-only in-season communication. |
| **7 — The unbuilt system** | Chain 1 lead magnet — capture form, delivery, 6 emails | Largest unbuilt system; content cost already sunk (the 5 guides are written). |

Phases 1–3 are the ones that change what a paying parent experiences this season. Everything after compounds.

---

## Standing rules

Carried from [[DR-Communication-Engine]] — repeated here because they are the rules most likely to be broken during a build.

- **Merge syntax is `{UPPERCASE}`.** Four syntaxes are currently live (`{{ .Token }}`, `${VAR}`, `{{ $json.x }}`, `[Bracket]`). Every new message uses one. Normalize the old ones on contact.
- **Never render a raw variable to a parent.** QA every merge field with a test send. Set fallbacks — `{PARENT_FIRST_NAME}` → "there".
- **The 30/7/1 countdown fires once**, for the first practice only. In-season, one light day-before reminder per session.
- **SMS is a scalpel.** ~3 texts across the whole registration journey. Never for weekly nurture, recognition, or general updates.
- **Every parent email names the school.** It is DR's strongest pairing and it is free to use.
- **Every weekly email names one skill and asks one at-home question.** If the coach's session log is empty, do not send.
- **Week 4 and Week 6 are engineered moments.** Photo capture and review/re-enroll. Do not trim them for length.
