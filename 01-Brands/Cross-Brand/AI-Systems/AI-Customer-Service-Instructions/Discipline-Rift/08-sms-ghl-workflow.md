---
title: DR SMS / GHL Draft Workflow
brand: Discipline Rift
used_for_ai: true
last_updated: 2026-07-03
related: ghl-ai-draft-bots (multibrand draft-note pattern)
---

# 08 — SMS / GHL Draft Workflow

Same principle as email: **Claude drafts, a human sends.** Mirrors the existing GHL AI-draft-bot pattern (draft posted as an internal note; the team copies, edits, and sends manually).

## Workflow
1. **Message arrives** through Go High Level (SMS / conversation).
2. **System detects brand + contact** (Discipline Rift → Parent / Faculty / Coach).
3. **Claude uses the active DR instructions** ([01](01-brand-voice.md)–[06](06-escalation-rules.md)).
4. **Claude generates a draft** in DR voice, sized for SMS (short, warm, one clear next step).
5. **Draft is posted as an internal note / sticky note** on the GHL contact/conversation — **not sent to the contact.**
6. **The team copies, edits, and sends manually.**

## Internal draft format (post as note)
```
[AI DRAFT — revisar antes de enviar]

Mensaje sugerido:
...
```

If escalation applies, add on the first line:
```
[AI DRAFT — revisar antes de enviar]  ⚠️ HUMAN REVIEW: [reason]
```

## SMS-specific rules
- **Short.** 1–3 sentences. Warm, human, no corporate tone.
- **One next step** (registration link, confirm a time, "we'll follow up").
- Include the registration link when relevant: https://disciplinerift.com/register
- **Never auto-send.** Draft note only, until the system is tested and approved.
- **Escalate** refunds, complaints, injuries, upset contacts, pricing, child-sensitive, legal, ambiguous → [06-escalation-rules.md](06-escalation-rules.md).
- **Don't invent facts** — if unsure, draft: "Let me confirm this with our team and we'll follow up." ([05](05-program-info-scope.md))

## Example draft note (parent, GHL)
```
[AI DRAFT — revisar antes de enviar]

Mensaje sugerido:
Hi [Name]! Yes—registration for the new season is open. You can sign up here: https://disciplinerift.com/register. Happy to help if you get stuck. — Discipline Rift
```
