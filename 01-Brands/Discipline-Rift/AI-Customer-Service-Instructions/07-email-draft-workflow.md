---
title: 07 — Email Draft Workflow
brand: Discipline-Rift
area: communication
subarea: ai-customer-service
note_type: sop
canonical: true
used_for_ai: true
hub_role: leaf
purpose: The pipeline from incoming email to sent reply. Draft-only until approved.
status: Human-review-only. No auto-send.
up:
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/00-README]]"
related:
  - "[[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home]]"
---

# 07 — Email Draft Workflow

## Parent
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/00-README|AI Customer Service Instructions — Index]]

## Related
- [[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home|DR Brand Home]]

Claude **creates draft replies. It does not send.** Nothing goes out automatically until the system is tested and approved.

## The pipeline

1. **Email arrives** in the inbox (info@disciplinerift.com).
2. **System identifies brand + audience** — brand = Discipline Rift; audience = parent / faculty / coach.
3. **Claude reads** the email (full thread, not just the latest message).
4. **Claude consults the matching instruction files:**
   - [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/01-brand-voice|01-brand-voice.md]] — always
   - Audience file: [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/02-parent-communication|02]] / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/03-faculty-communication|03]] / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/04-coach-communication|04]]
   - [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/05-program-info-scope|05-program-info-scope.md]] — allowed facts + fallback
   - [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules|06-escalation-rules.md]] — escalate or not
   - Matching examples: [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/09-examples-parent-emails|09]] / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/10-examples-faculty-emails|10]] / [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/11-examples-coach-emails|11]]
5. **Claude generates a draft reply** in DR's voice.
6. **Draft is saved for human review** — not sent. If the message hit an escalation trigger ([[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules|06]]), tag it (e.g., `ESCALATE: refund`).
7. **A human reviews, edits, and sends.**

> The email must **not** be sent automatically until the system is tested and approved.

## Audience detection cues

| Signal | Likely audience |
|---|---|
| "my daughter/son," child's name, refund, absence, registration help | **Parent** → [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/02-parent-communication|02]] |
| School/staff signature, "our Principal," Facilitron, facility, agreement, program fit | **Faculty** → [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/03-faculty-communication|03]] |
| "Coach [Name]," availability, blackout dates, time-off, days off | **Coach/Staff** → [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/04-coach-communication|04]] |

When the audience is unclear, treat as **ambiguous → escalate** ([[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules|06]]).

## Draft output — what a human should see

Each saved draft should include:
- **Audience** detected (parent / faculty / coach)
- **Escalation tag** if any (with a one-line reason)
- **The draft reply text**
- **Facts used** — which items from [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/05-program-info-scope|05]] the reply relies on (so the human can verify)
- **Open questions** — anything Claude couldn't confirm and left to the fallback line

## Guardrails

- Never send. Draft only.
- Never state a final refund/price/contract/personnel decision — that's the human's ([[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/06-escalation-rules|06]]).
- Never invent facts — use the confirm-with-team fallback ([[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/05-program-info-scope|05]]).
- Keep the full thread's context; match the ongoing tone.

## Rollout note

Until the draft quality is validated across parents, faculty, and coaches, **every** draft is human-reviewed before sending — including routine ones. Auto-send is a later phase, only after approval.
