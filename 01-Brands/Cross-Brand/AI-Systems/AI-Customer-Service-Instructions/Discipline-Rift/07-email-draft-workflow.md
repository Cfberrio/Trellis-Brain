---
title: DR Email Draft Workflow
brand: Discipline-Rift
note_type: sop
area: communication
subarea: ai-customer-service
canonical: true
hub_role: leaf
used_for_ai: true
last_updated: 2026-07-03
---

# 07 — Email Draft Workflow

## Parent
- [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/00-README|AI Customer Service Instructions — Index (Cross-Brand copy)]]

**Claude drafts email replies. Claude does not send.** Nothing goes out automatically until the system is tested and approved by the team.

## Workflow
1. **Email arrives** in the inbox (info@disciplinerift.com).
2. **System identifies brand + audience** (Discipline Rift → Parent / Faculty / Coach).
3. **Claude reads** the full email/thread (including quoted history).
4. **Claude consults** the matching instruction files:
   - Voice: [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/01-brand-voice|01-brand-voice.md]]
   - Audience: [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/02-parent-communication|02]] / [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/03-faculty-communication|03]] / [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/04-coach-communication|04]]
   - Scope: [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/05-program-info-scope|05-program-info-scope.md]]
   - Escalation: [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/06-escalation-rules|06-escalation-rules.md]]
5. **Claude generates a draft reply** in DR voice, following the golden pattern (acknowledge → own mistakes → concrete answer → exact resource → next step).
6. **Draft is saved for human review** (e.g., Gmail draft on the thread, or a review queue). It is **not** sent.
7. **Human reviews, edits, and sends.**

## Draft output format
```
TO: [original sender]
RE: [subject]
AUDIENCE: [Parent | Faculty | Coach]
STATUS: DRAFT — review before sending
[⚠️ HUMAN REVIEW — reason]   ← only if escalation applies (see 06)

--- DRAFT REPLY ---
[the email body, in DR voice, with signature]
--- END DRAFT ---

NOTES: [anything the reviewer should know — unconfirmed facts, price left blank, why escalated]
```

## Rules
- **Never auto-send.** Save as draft only, until the system is proven and approved.
- **Escalate per [[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/06-escalation-rules|06]]** — flag refunds, complaints, injuries, upset contacts, pricing, child-sensitive, legal, ambiguous.
- **Don't invent facts** — leave price/date as `$___ (confirm)` or use the confirm-and-follow-up line ([[01-Brands/Cross-Brand/AI-Systems/AI-Customer-Service-Instructions/Discipline-Rift/05-program-info-scope|05]]).
- **Match the audience register** — parents simple/warm; faculty formal/logistics; coaches warm/precise.
- **Preserve real intent** — answer what was actually asked; hand over the exact resource.
- One draft = one clear next step.
