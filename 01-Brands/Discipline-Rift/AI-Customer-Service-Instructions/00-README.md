---
title: AI Customer Service Instructions — Discipline Rift (Index)
brand: Discipline Rift
purpose: Master index for the instruction set that trains/guides Claude to draft email replies for DR.
created: 2026-07-01
owner: Chris / Luis Torres (Founder)
status: Draft — human-review-only mode (no auto-send)
---

# AI Customer Service Instructions — Discipline Rift

This folder holds the instruction files that tell Claude **how to draft email replies** for Discipline Rift (DR).
Everything here is derived from real DR reply threads captured in the founder-voice bot-training set:

- [01-PARENTS.md](../03-Evidence/Founder-Voice/bot-training/01-PARENTS.md) — 20 parent reply examples
- [02-FACULTY-SCHOOLS.md](../03-Evidence/Founder-Voice/bot-training/02-FACULTY-SCHOOLS.md) — 10 faculty/school reply examples
- [03-COACHES-STAFF.md](../03-Evidence/Founder-Voice/bot-training/03-COACHES-STAFF.md) — 10 coach/staff reply examples

## Core rule

**Claude drafts. Humans send.** Nothing goes out automatically until the system is tested and approved.
See [07-email-draft-workflow.md](07-email-draft-workflow.md).

## Read order

Claude should load, per incoming email:
1. [01-brand-voice.md](01-brand-voice.md) — always (how DR sounds)
2. The audience file — [02](02-parent-communication.md) parents / [03](03-faculty-communication.md) faculty / [04](04-coach-communication.md) coaches
3. [05-program-info-scope.md](05-program-info-scope.md) — what facts Claude may state
4. [06-escalation-rules.md](06-escalation-rules.md) — when to flag for a human instead of answering
5. The matching examples file — [09](09-examples-parent-emails.md) / [10](10-examples-faculty-emails.md) / [11](11-examples-coach-emails.md)

## File map

| File | Purpose |
|---|---|
| [01-brand-voice.md](01-brand-voice.md) | How DR talks — tone, do/don't, register per audience |
| [02-parent-communication.md](02-parent-communication.md) | Replying to parents — what Claude may answer vs must escalate |
| [03-faculty-communication.md](03-faculty-communication.md) | Replying to schools/faculty/admins — **highest priority** |
| [04-coach-communication.md](04-coach-communication.md) | Replying to coaches/internal staff |
| [05-program-info-scope.md](05-program-info-scope.md) | The facts Claude is allowed to state (and the "let me confirm" fallback) |
| [06-escalation-rules.md](06-escalation-rules.md) | Triggers that force human review |
| [07-email-draft-workflow.md](07-email-draft-workflow.md) | Inbox → draft → human review → send pipeline |
| [09-examples-parent-emails.md](09-examples-parent-emails.md) | Annotated parent reply examples |
| [10-examples-faculty-emails.md](10-examples-faculty-emails.md) | Annotated faculty reply examples |
| [11-examples-coach-emails.md](11-examples-coach-emails.md) | Annotated coach reply examples |

## Intentionally not included

- **`08-sms-ghl-workflow.md`** — skipped for now. No source data exists on DR's SMS / GoHighLevel (GHL) setup in the bot-training files. Add it once the real GHL flow is documented.
- **Faculty examples count** — the plan asked for 10–20 (ideally 20) faculty examples; the current source has **10**. See the note in [10-examples-faculty-emails.md](10-examples-faculty-emails.md) on how to expand.
