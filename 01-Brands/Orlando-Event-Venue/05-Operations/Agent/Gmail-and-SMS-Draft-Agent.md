---
brand: Orlando-Event-Venue
area: operations
subarea: agent
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp doc 8cqnrff-22137 'AI Gmail Draft Agent — OEV (Producción 2026-07-03)' + 8cqnrff-21977 'OEV — SMS + Email AI Drafts (GHL Bot)' + OEV-PROJECT commits 2026-07-03 → 2026-08-20"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - ai-agent
  - operations
---

# Gmail and SMS Draft Agent — OEV

## Parent
- [[01-Brands/Orlando-Event-Venue/05-Operations/Agent/Voice-Agent-Master-Prompt|OEV Voice Agent Master Prompt]]

## Related
- [[01-Brands/Orlando-Event-Venue/03-Evidence/Founder-Voice/bot-training/OEV/05-email-draft-workflow|OEV Email Draft Workflow]]
- [[01-Brands/Orlando-Event-Venue/03-Evidence/Founder-Voice/bot-training/OEV/06-ghl-sms-workflow|OEV GHL SMS Workflow]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Systems-Home|AI Systems Home]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Automation-Jobs-and-Cron|Automation, Jobs and Cron]]

## What it is
Two production draft agents that write replies for OEV but **never send them**. A human reviews and sends. In production since 2026-07-03.

- **Gmail draft agent** — drafts replies to inbound email, including website contact-form submissions.
- **GHL SMS draft agent** — drafts replies to inbound SMS inside GoHighLevel.

The same multi-brand method runs for DR and CTS. The shared architecture and lessons live in the Trellis method doc; this note records what is specific to OEV.

## Operating rules learned in production
- **Draft, never send.** The agent's output is a draft in the human's inbox.
- **Claim before drafting.** The SMS agent claims the inbound message before generating, which is what stopped duplicate AI drafts from two concurrent runs (fix 2026-08-12).
- **The auto-reply must read the submission it is answering.** A contact-form reply that ignores the submitted content reads as a template and destroys trust (fix 2026-08-20).
- **Ground the agent in live data.** As of 2026-08-20 the draft agent is grounded in live pricing and inclusions rather than a static copy, so quotes in drafts cannot drift from the real price table.
- **Strip emoji from staff-response subject lines** — they broke rendering in some clients.
- **Alert on credit exhaustion.** When the model provider quota runs out the agent fails silently unless it alerts; alerting was added with the contact-form drafting.

## Grounding sources
The agent reads from the OEV knowledge surfaces, which must stay current or the drafts go stale:
- pricing and inclusions (live from the platform),
- [[01-Brands/Orlando-Event-Venue/05-Operations/Agent/Voice-Agent-Knowledge-Pack|Voice Agent Knowledge Pack]],
- [[01-Brands/Orlando-Event-Venue/05-Operations/Agent/Voice-Agent-FAQ|Voice Agent FAQ]],
- [[01-Brands/Orlando-Event-Venue/02-Communication/OEV-Communication-Manual|OEV Communication Manual]].

## Next step
Whenever pricing, inclusions or venue rules change, verify the draft agent's grounding the same day. A wrong price in a draft that a human sends without checking is worse than no draft.
