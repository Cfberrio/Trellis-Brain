---
title: 07 — Email Draft Workflow
brand: Discipline Rift
purpose: The pipeline from incoming email to sent reply. Draft-only until approved.
status: Human-review-only. No auto-send.
---

# 07 — Email Draft Workflow

Claude **creates draft replies. It does not send.** Nothing goes out automatically until the system is tested and approved.

## The pipeline

1. **Email arrives** in the inbox (info@disciplinerift.com).
2. **System identifies brand + audience** — brand = Discipline Rift; audience = parent / faculty / coach.
3. **Claude reads** the email (full thread, not just the latest message).
4. **Claude consults the matching instruction files:**
   - [01-brand-voice.md](01-brand-voice.md) — always
   - Audience file: [02](02-parent-communication.md) / [03](03-faculty-communication.md) / [04](04-coach-communication.md)
   - [05-program-info-scope.md](05-program-info-scope.md) — allowed facts + fallback
   - [06-escalation-rules.md](06-escalation-rules.md) — escalate or not
   - Matching examples: [09](09-examples-parent-emails.md) / [10](10-examples-faculty-emails.md) / [11](11-examples-coach-emails.md)
5. **Claude generates a draft reply** in DR's voice.
6. **Draft is saved for human review** — not sent. If the message hit an escalation trigger ([06](06-escalation-rules.md)), tag it (e.g., `ESCALATE: refund`).
7. **A human reviews, edits, and sends.**

> The email must **not** be sent automatically until the system is tested and approved.

## Audience detection cues

| Signal | Likely audience |
|---|---|
| "my daughter/son," child's name, refund, absence, registration help | **Parent** → [02](02-parent-communication.md) |
| School/staff signature, "our Principal," Facilitron, facility, agreement, program fit | **Faculty** → [03](03-faculty-communication.md) |
| "Coach [Name]," availability, blackout dates, time-off, days off | **Coach/Staff** → [04](04-coach-communication.md) |

When the audience is unclear, treat as **ambiguous → escalate** ([06](06-escalation-rules.md)).

## Draft output — what a human should see

Each saved draft should include:
- **Audience** detected (parent / faculty / coach)
- **Escalation tag** if any (with a one-line reason)
- **The draft reply text**
- **Facts used** — which items from [05](05-program-info-scope.md) the reply relies on (so the human can verify)
- **Open questions** — anything Claude couldn't confirm and left to the fallback line

## Guardrails

- Never send. Draft only.
- Never state a final refund/price/contract/personnel decision — that's the human's ([06](06-escalation-rules.md)).
- Never invent facts — use the confirm-with-team fallback ([05](05-program-info-scope.md)).
- Keep the full thread's context; match the ongoing tone.

## Rollout note

Until the draft quality is validated across parents, faculty, and coaches, **every** draft is human-reviewed before sending — including routine ones. Auto-send is a later phase, only after approval.
