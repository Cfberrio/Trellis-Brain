---
title: DR AI Customer Service — Instruction Set (Index)
brand: Discipline-Rift
note_type: home
area: communication
subarea: ai-customer-service
canonical: true
hub_role: system-hub
purpose: Instruct/train Claude to draft (not send) replies to parents, faculty, and coaches for Discipline Rift
status: active
used_for_ai: true
owner: Luis Torres / Trellis
last_updated: 2026-07-03
grounded_in:
  - STRATEGY-Source-DR.md (canonical DNA, used_for_ai)
  - Extracted real email threads (see 09/10/11)
up:
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Systems-Home]]"
down:
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/01-brand-voice]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/02-parent-communication]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/03-faculty-communication]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/04-coach-communication]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/05-program-info-scope]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/06-escalation-rules]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/07-email-draft-workflow]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/08-sms-ghl-workflow]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/09-examples-parent-emails]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/10-examples-faculty-emails]]"
  - "[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/11-examples-coach-emails]]"
related:
  - "[[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/00-README]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Evidence-Home]]"
---

# DR AI Customer Service — Instruction Set

## Parent
- [[01-Brands/Cross-Brand/AI-Systems/AI-Systems-Home|AI Systems — Home]]

## Children
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/01-brand-voice|01 — Brand Voice]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/02-parent-communication|02 — Parent Communication]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/03-faculty-communication|03 — Faculty/School Communication]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/04-coach-communication|04 — Coach/Staff Communication]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/05-program-info-scope|05 — Program Info & Scope]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/06-escalation-rules|06 — Escalation Rules]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/07-email-draft-workflow|07 — Email Draft Workflow]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/08-sms-ghl-workflow|08 — SMS/GHL Draft Workflow]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/09-examples-parent-emails|09 — Example Parent Emails]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/10-examples-faculty-emails|10 — Example Faculty Emails]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/11-examples-coach-emails|11 — Example Coach Emails]]

## Related
- [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/00-README|DR AI Customer Service Instructions — Index (brand-root canonical copy)]]
- [[01-Brands/Discipline-Rift/03-Evidence/Evidence-Home|DR Evidence Home]]

This folder instructs Claude how to handle inbound customer service for **Discipline Rift** across email and SMS/GHL. **Claude drafts; a human reviews and sends.** Nothing goes out automatically until the system is tested and approved.

> **Note:** This is a parallel/older copy of the instruction set. The brand-root copy at [[01-Brands/Discipline-Rift/AI-Customer-Service-Instructions/00-README|01-Brands/Discipline-Rift/AI-Customer-Service-Instructions]] is the actively maintained canonical version (matches the real DR voice/DNA docs more closely); this Cross-Brand copy additionally documents the SMS/GHL workflow (08) which the canonical copy intentionally omits pending real GHL data.

## Load order (read top → bottom)
1. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/01-brand-voice|01-brand-voice.md]]** — how DR sounds (all audiences)
2. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/02-parent-communication|02-parent-communication.md]]** — replying to parents
3. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/03-faculty-communication|03-faculty-communication.md]]** — replying to schools/faculty/admin (highest priority)
4. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/04-coach-communication|04-coach-communication.md]]** — replying to coaches/staff
5. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/05-program-info-scope|05-program-info-scope.md]]** — what info Claude may state (and what it must not invent)
6. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/06-escalation-rules|06-escalation-rules.md]]** — when to stop and flag for a human
7. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/07-email-draft-workflow|07-email-draft-workflow.md]]** — email draft process
8. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/08-sms-ghl-workflow|08-sms-ghl-workflow.md]]** — SMS/GHL draft process
9. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/09-examples-parent-emails|09-examples-parent-emails.md]]** — real parent reply examples
10. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/10-examples-faculty-emails|10-examples-faculty-emails.md]]** — real faculty reply examples
11. **[[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/11-examples-coach-emails|11-examples-coach-emails.md]]** — real coach reply examples

## The one rule above all
When money, safety, a child's wellbeing, or DR's reputation is involved — **draft it, flag it, do not decide.** See 06.

## Golden pattern (from real DR replies)
Acknowledge → own any mistake plainly → give the concrete action/answer → hand over the exact resource (link, code, name, date) → close with a clear next step. Warm, human, never robotic or corporate.
