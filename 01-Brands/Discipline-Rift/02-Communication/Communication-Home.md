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
last_updated: 2026-05-21
---

# Discipline Rift — Communication Home

## Parent
- [[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home|DR Brand Home]]

## Communication Engine (go-forward — n8n retired)
> [!todo] Planned, not yet authored (verified 2026-08-20)
> These four notes are referenced across DR planning but do not exist in the vault. Listed as plain names on purpose so the graph stays clean until they are written.
> - **DR Communication Engine** — master rules, merge syntax, channel philosophy, marketing improvements
> - **DR Registration Sequence** — payment → first practice + cart recovery. Live behaviour today lives in [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]] and [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library|Operational Email Library]].
> - **DR Lead Magnet Sequence** — opt-in → registration
> - **DR Season Reminder Sequence** — in-season nurture + re-enroll. See [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season|Parent Communication — Volleyball Season]] for the closest existing artifact.

## Children
- [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] *(legacy — n8n-era reference; superseded by the Engine for syntax + channel rules)*
- [[01-Brands/Discipline-Rift/02-Communication/DR-Script-Evaluation-Context|DR Script Evaluation Context]]
- [[01-Brands/Discipline-Rift/02-Communication/Marketing-Language-Library|DR Marketing Language Library]]
- [[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec|DR Email Design Spec]] — website design system translated for email build (color, type, components, dark mode) — now carries Luis's 2026-08 production rulings (§5.2, §9, §10.1, §11)
- [[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Email-Template|DR Parent Email Template]] — binding drafting contract for house-list marketing emails: ten slots, Luis's five rules, word caps, production chain
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|DR GoHighLevel Marketing + Registration Automations]]
- [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library|DR Operational Email Library]]
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

The active source of truth for this layer is DR Communication Rules, which documents:
- all parent email sequences (registration confirmation, 30-day, 7-day, and 1-day reminders, 6-week volleyball nurture sequence)
- coach-facing email and WhatsApp patterns
- n8n variable syntax and merge field reference
- known template bugs requiring fix before production
- improvement recommendations for the full communication system
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|DR GoHighLevel Marketing and Registration Automations]]