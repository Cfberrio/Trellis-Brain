---
brand: Discipline-Rift
area: communication
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
sensitivity: internal
hub_role: communication-hub
last_updated: 2026-08-27
---

# Discipline Rift — Communication Home

## Parent
- [[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home|DR Brand Home]]

## Sending engines (verified against ClickUp 2026-08-27)

| Engine | What it sends today |
|---|---|
| **n8n** | 30/7/1-day reminders (#3–#5), Coach Session Reminder (#6), Parent Assistance / no-show (#7), and the 6-week weekly volleyball sequence. Source pages are still labelled `(N8N)` in ClickUp Doc `8cqnrff-21297` → NOTIFICATIONS. |
| **Supabase Auth** | OTP / account verification (#1) — merge token `{{ .Token }}` |
| **Code (Supabase edge functions)** | Registration Confirmation (#2), Parent Guide (#9), Waitlist Invite (#10) — `email-templates.ts`, migrated 2026-08-25 |
| **GoHighLevel** | Newsletter nurture, registration abandonment recovery, SMS marketing |

> [!warning] Earlier "n8n retired" claim was too broad
> It applies only to #2/#9/#10. n8n is still live for the reminder + weekly families. Corrected 2026-08-27.

## Communication Engine (planned rewrite — applies to the code-migrated templates)
> [!todo] Planned, not yet authored (verified 2026-08-20)
> These four notes are referenced across DR planning but do not exist in the vault. Listed as plain names on purpose so the graph stays clean until they are written.
> - **DR Communication Engine** — master rules, merge syntax, channel philosophy, marketing improvements
> - **DR Registration Sequence** — payment → first practice + cart recovery. Live behaviour today lives in [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]] and [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library|Operational Email Library]].
> - **DR Lead Magnet Sequence** — opt-in → registration
> - **DR Season Reminder Sequence** — in-season nurture + re-enroll. See [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season|Parent Communication — Volleyball Season]] for the closest existing artifact.

## ClickUp verbatim mirror
- [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/NOTIFICATIONS|ClickUp NOTIFICATIONS (verbatim)]] — literal, unedited transcription of every notification/email page in ClickUp Doc `8cqnrff-21297`, including the `COACHES (N8N)` and `WEEKLY (N8N)` sub-trees. Use it when you need to know exactly what the ClickUp source says; use the curated notes below when you need the cleaned-up, annotated version.

## Children
- [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] *(2026-04 document. Its `Template pattern` blocks are **proposals, not live copy** — see the banner at its top. Bug flags re-checked 2026-08-27: Email 03/04 header leak and Email 06 merge-field are fixed at source; Email 08 `Hi name,` still broken.)*
- [[01-Brands/Discipline-Rift/02-Communication/DR-Script-Evaluation-Context|DR Script Evaluation Context]]
- [[01-Brands/Discipline-Rift/02-Communication/Marketing-Language-Library|DR Marketing Language Library]]
- [[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec|DR Email Design Spec]] — website design system translated for email build (color, type, components, dark mode) — now carries Luis's 2026-08 production rulings (§5.2, §9, §10.1, §11) and the tokens driving the code-rendered transactional shell (see Operational Email Library below)
- [[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Email-Template|DR Parent Email Template]] — binding drafting contract for house-list marketing emails: ten slots, Luis's five rules, word caps, production chain
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|DR GoHighLevel Marketing + Registration Automations]]
- [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library|DR Operational Email Library]] — Registration Confirmation, Parent Guide, and Waitlist Invite migrated off n8n/ClickUp to code and DR-rebranded 2026-08-25 (fixed a `=20` encoding bug in the process); rest of the 10-template index still ClickUp-sourced
- [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season|Parent Communication — Volleyball Season]]
- [[01-Brands/Discipline-Rift/02-Communication/Templates/School-Outreach-Email-Templates|School Outreach Email Templates]]

## Campaigns (dated, one-time — not lifecycle chains)
- [[01-Brands/Discipline-Rift/02-Communication/Campaigns/DR-First-Week-Of-School-Campaign-2026-08|First Week of School Campaign — August 2026]] — 3 emails to the parent house list, fires on the first day of school and retires. Primary approved by Luis 2026-08-09; §0 carries his five binding parent-copy rules; GHL-ready HTML kit in the Trellis repo (`email-html/`).
- [[01-Brands/Discipline-Rift/02-Communication/Campaigns/DR-Email-Rewrite-Retrospective-2026-08|Email Rewrite Retrospective — August 2026]] — full analysis of Luis's breakdown of the first draft: what each correction protects, what survived, what died. The training document behind the template.

## Related
- [[01-Brands/Discipline-Rift/06-DNA/Message|DR Message]]
- [[01-Brands/Discipline-Rift/00-Brand-Core/Avatar|DR Avatar]]
- [[01-Brands/Discipline-Rift/03-Evidence/School-Outreach-AI-Feedback-Synthesis|School Outreach AI Feedback Synthesis]]

## Purpose
Hub for all Discipline Rift communication rules, email templates, and messaging patterns across parent-facing, coach-facing, and internal channels.

Source of truth by layer (corrected 2026-08-27):

- **Live email copy** → [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library|DR Operational Email Library]] (#1–#10) and [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season|Parent Communication — Volleyball Season]] (weekly). Both verified verbatim against ClickUp Doc `8cqnrff-21297` on 2026-08-27.
- **Render contract / design tokens** → [[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec|DR Email Design Spec]]
- **Voice, audience segmentation, merge-field conventions, improvement backlog** → [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] — still useful for these, *not* for template copy
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|DR GoHighLevel Marketing and Registration Automations]]
