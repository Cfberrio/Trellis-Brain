---
brand: Discipline-Rift
area: communication
subarea: email
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
sensitivity: internal
hub_role: leaf
last_updated: 2026-09-14
up:
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Messages-Reminders-Home]]"
related:
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Parent-Email-Template]]"
---

# Parent New Messages — Email 1

**Workflow:** `DR | Webhook - Parent New Messages` · branch `stage = 1`
**When:** the first hourly run after a coach message the parent has not opened.
**Template file:** `brand-kit/email/transactional/message-notification-parent-1.html`
Back: [[Messages-Reminders-Home]]

**Subject:** Coach {{inboundWebhookRequest.coach_first_name}} sent you a message about {{inboundWebhookRequest.team_name}}

**Preheader:** Coach {{inboundWebhookRequest.coach_first_name}} sent you a message about {{inboundWebhookRequest.team_name}}.

---

**DISCIPLINE RIFT**

NEW MESSAGE

Hi {{inboundWebhookRequest.parent_first_name}},

## Coach {{inboundWebhookRequest.coach_first_name}} sent you a message about {{inboundWebhookRequest.team_name}}.

You have {{inboundWebhookRequest.unread_count}} unread {{inboundWebhookRequest.messages_word}} waiting in your Parent Dashboard. Coaches use it for the things that matter: schedule changes, what to bring, how {{inboundWebhookRequest.children_names}} {{inboundWebhookRequest.children_verb}} doing.

It only takes a minute to read and reply.

> **WAITING FOR YOU**
>
> | Team | Coach | Unread |
> |---|---|---|
> | *(one row per team — `teams_html`)* | | |
>
> LATEST MESSAGE · {{inboundWebhookRequest.latest_message_at}}
> *"{{inboundWebhookRequest.latest_message_preview}}"*

Open your Parent Dashboard to read the full message and reply:

**[ READ MESSAGE ]** → https://www.disciplinerift.com/parent/messages

**See you at practice!**
Discipline Rift

---
DISCIPLINE RIFT · Developing young players in volleyball, tennis, pickleball, and flag football
CONTACT · info@disciplinerift.com · (407) 614-7454
713 W. Yale Street, Orlando, FL 32804
