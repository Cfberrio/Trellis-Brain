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
last_updated: 2026-09-17
up:
  - "[[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home]]"
down:
  - "[[01-Brands/Discipline-Rift/02-Communication/communication-rules]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Script-Evaluation-Context]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Marketing-Language-Library]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Email-Template]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/School-Outreach-Email-Templates]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Guides-Library]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Messages-Reminders-Home]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Communication-Philosophy]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Conversation-Style]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/Coach-After-Practice-Parent-Update]]"
related:
  - "[[01-Brands/Discipline-Rift/06-DNA/Message]]"
  - "[[01-Brands/Discipline-Rift/00-Brand-Core/Avatar]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/School-Outreach-AI-Feedback-Synthesis]]"
  - "[[01-Brands/Discipline-Rift/05-Operations/Training/Method/Method-Home]]"
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


## Parent-facing philosophy and coach-to-parent standard (added 2026-09-17)
- [[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Communication-Philosophy|DR Parent Communication Philosophy]] — what DR says to parents about development: depth within skills, bridges between skills, why season two is not a repeat, multi-sport, pathway without pressure. Luis's own text.
- [[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Conversation-Style|DR Parent Conversation Style]] — how a call or text with a parent runs (welcome → clarify → check → guide → own → respond → recap → close). Quotes are tone examples from one call, **not** standing policy.
- [[01-Brands/Discipline-Rift/02-Communication/Templates/Coach-After-Practice-Parent-Update|Coach After-Practice Parent Update]] — *proposed* standard for the coach's Dashboard "Message All" after every practice: what we worked on → what improved → what comes next. Pairs with the pre-practice weekly email.
- Method these serve: [[01-Brands/Discipline-Rift/05-Operations/Training/Method/Method-Home|DR Method Home]].

## Communication Engine (built 2026-08-04, verified in vault 2026-09-07)
- [[01-Brands/Discipline-Rift/02-Communication/DR-Communication-Engine|DR Communication Engine]] — master rules, merge syntax, channel philosophy, marketing improvements
- [[01-Brands/Discipline-Rift/02-Communication/DR-Communication-Chains-Index|DR Communication Chains Index]] — map of all five chains, ship order, blockers
- [[01-Brands/Discipline-Rift/02-Communication/DR-Communication-Audit-2026-08-04|DR Communication Audit — 2026-08-04]]
- [[01-Brands/Discipline-Rift/02-Communication/Sequences/DR-Registration-Sequence|DR Registration Sequence]] — payment → first practice + cart recovery
- [[01-Brands/Discipline-Rift/02-Communication/Sequences/DR-Lead-Magnet-Sequence|DR Lead Magnet Sequence]] — opt-in → registration
- [[01-Brands/Discipline-Rift/02-Communication/Sequences/DR-Season-Reminder-Sequence|DR Season Reminder Sequence]] — in-season nurture + re-enroll
- [[01-Brands/Discipline-Rift/02-Communication/Sequences/DR-Coach-Communication-Chain|DR Coach Communication Chain]] — coach lifecycle, 11 messages
- [[01-Brands/Discipline-Rift/02-Communication/Sequences/DR-Sport-Week-Banks|DR Sport Week Banks]] — flag football + tennis weekly banks

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
- [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Guides-Library|Parent Guides Library]]
- [[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Messages-Reminders-Home|Messages Reminders]] — unread-dashboard-message emails to parents and coaches (live 2026-09-11): max 2 per cycle, business hours only, all logic in the database, GHL only renders. Four templates + design spec inside.

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
- **What we tell parents about development** → [[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Communication-Philosophy|DR Parent Communication Philosophy]]; the coach's after-practice message follows [[01-Brands/Discipline-Rift/02-Communication/Templates/Coach-After-Practice-Parent-Update|Coach After-Practice Parent Update]] (proposed 2026-09-17)
- **Voice, audience segmentation, merge-field conventions, improvement backlog** → [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] — still useful for these, *not* for template copy
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|DR GoHighLevel Marketing and Registration Automations]]
