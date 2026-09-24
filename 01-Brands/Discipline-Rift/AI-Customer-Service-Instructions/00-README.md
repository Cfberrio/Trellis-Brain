---
title: AI Customer Service Instructions — Discipline Rift (Index)
brand: Discipline-Rift
area: communication
subarea: ai-customer-service
note_type: home
canonical: true
used_for_ai: true
hub_role: system-hub
purpose: Master index for the instruction set that trains/guides Claude to draft email replies for DR.
created: 2026-07-01
owner: Chris / Luis Torres (Founder)
status: Draft — human-review-only mode (no auto-send)
up:
  - "[[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home]]"
down:
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/01-brand-voice]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/02-parent-communication]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/03-faculty-communication]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/04-coach-communication]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/05-program-info-scope]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/07-email-draft-workflow]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/09-examples-parent-emails]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/10-examples-faculty-emails]]"
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/11-examples-coach-emails]]"
related:
  - "[[01-Brands/Discipline-Rift/03-Evidence/Evidence-Home]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Communication-Home]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/01-PARENTS]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/02-FACULTY-SCHOOLS]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/03-COACHES-STAFF]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Communication-Philosophy]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Conversation-Style]]"
  - "[[01-Brands/Discipline-Rift/05-Operations/Training/Method/DR-Coach-Feedback-Standard]]"
---

# AI Customer Service Instructions — Discipline Rift

## Parent
- [[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home|DR Brand Home]]

## Children
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/01-brand-voice|01 — Brand Voice]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/02-parent-communication|02 — Parent Communication]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/03-faculty-communication|03 — Faculty/School Communication]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/04-coach-communication|04 — Coach/Staff Communication]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/05-program-info-scope|05 — Program Info & Scope]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules|06 — Escalation Rules]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/07-email-draft-workflow|07 — Email Draft Workflow]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/09-examples-parent-emails|09 — Example Parent Emails]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/10-examples-faculty-emails|10 — Example Faculty Emails]]
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/11-examples-coach-emails|11 — Example Coach Emails]]

## Related
- [[01-Brands/Discipline-Rift/03-Evidence/Evidence-Home|DR Evidence Home]]
- [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|DR Communication Home]]

This folder holds the instruction files that tell Claude **how to draft email replies** for Discipline Rift (DR).
Everything here is derived from real DR reply threads captured in the founder-voice bot-training set:

- [[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/01-PARENTS|01-PARENTS.md]] — 20 parent reply examples
- [[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/02-FACULTY-SCHOOLS|02-FACULTY-SCHOOLS.md]] — 10 faculty/school reply examples
- [[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/03-COACHES-STAFF|03-COACHES-STAFF.md]] — 10 coach/staff reply examples

## Core rule

**Claude drafts. Humans send.** Nothing goes out automatically until the system is tested and approved.
See [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/07-email-draft-workflow|07-email-draft-workflow.md]].

## Read order

Claude should load, per incoming email:
1. [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/01-brand-voice|01-brand-voice.md]] — always (how DR sounds)
2. The audience file — [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/02-parent-communication|02]] parents / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/03-faculty-communication|03]] faculty / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/04-coach-communication|04]] coaches
3. [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/05-program-info-scope|05-program-info-scope.md]] — what facts Claude may state
4. [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules|06-escalation-rules.md]] — when to flag for a human instead of answering
5. The matching examples file — [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/09-examples-parent-emails|09]] / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/10-examples-faculty-emails|10]] / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/11-examples-coach-emails|11]]

## Philosophy references (added 2026-09-17)
Load when the email is about *what the child is learning*, *why another season*, *practice quality*, or a coach's practice performance — not for pure logistics:
- [[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Communication-Philosophy|DR Parent Communication Philosophy]] — development language for parents (depth within skills, bridges, multi-sport, pathway without promises)
- [[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Conversation-Style|DR Parent Conversation Style]] — the call/text flow; its quotes are tone examples, not policy
- [[01-Brands/Discipline-Rift/05-Operations/Training/Method/DR-Coach-Feedback-Standard|DR Coach Feedback Standard]] — the practice-correction register for coach messages (draft-and-flag; see [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/04-coach-communication|04]])

## File map

| File | Purpose |
|---|---|
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/01-brand-voice|01-brand-voice.md]] | How DR talks — tone, do/don't, register per audience |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/02-parent-communication|02-parent-communication.md]] | Replying to parents — what Claude may answer vs must escalate |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/03-faculty-communication|03-faculty-communication.md]] | Replying to schools/faculty/admins — **highest priority** |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/04-coach-communication|04-coach-communication.md]] | Replying to coaches/internal staff |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/05-program-info-scope|05-program-info-scope.md]] | The facts Claude is allowed to state (and the "let me confirm" fallback) |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules|06-escalation-rules.md]] | Triggers that force human review |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/07-email-draft-workflow|07-email-draft-workflow.md]] | Inbox → draft → human review → send pipeline |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/09-examples-parent-emails|09-examples-parent-emails.md]] | Annotated parent reply examples |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/10-examples-faculty-emails|10-examples-faculty-emails.md]] | Annotated faculty reply examples |
| [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/11-examples-coach-emails|11-examples-coach-emails.md]] | Annotated coach reply examples |

## Intentionally not included

- **`08-sms-ghl-workflow.md`** — skipped for now. No source data exists on DR's SMS / GoHighLevel (GHL) setup in the bot-training files. Add it once the real GHL flow is documented.
- **Faculty examples count** — the plan asked for 10–20 (ideally 20) faculty examples; the current source has **10**. See the note in [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/10-examples-faculty-emails|10-examples-faculty-emails.md]] on how to expand.
