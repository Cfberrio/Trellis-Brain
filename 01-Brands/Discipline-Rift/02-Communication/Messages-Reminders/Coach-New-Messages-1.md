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
  - "[[01-Brands/Discipline-Rift/02-Communication/Sequences/DR-Coach-Communication-Chain]]"
---

# Coach New Messages — Email 1

**Workflow:** `DR | Webhook - Coach New Messages` · branch `stage = 1`
**When:** the first hourly run after a parent message on any team the coach (head or assistant) belongs to, that this coach has not opened.
**Template file:** `brand-kit/email/transactional/message-notification-coach-1.html`
Back: [[Messages-Reminders-Home]]

**Subject:** {{inboundWebhookRequest.parent_count}} {{inboundWebhookRequest.parents_word}} wrote to you — {{inboundWebhookRequest.team_names}}

**Preheader:** {{inboundWebhookRequest.parent_count}} {{inboundWebhookRequest.parents_word}} wrote to you on {{inboundWebhookRequest.team_names}}.

---

**DISCIPLINE RIFT**

COACH INBOX

Hey Coach {{inboundWebhookRequest.coach_first_name}},

## {{inboundWebhookRequest.parent_count}} {{inboundWebhookRequest.parents_word}} wrote to you on {{inboundWebhookRequest.team_names}}.

You have {{inboundWebhookRequest.unread_count}} unread {{inboundWebhookRequest.messages_word}} in your Coach Dashboard. Parents notice when a coach replies the same day, and it is the single biggest thing that keeps a family coming back next season.

A one-line reply is enough. Open the dashboard and clear the list.

> **WAITING FOR YOU**
>
> | Parent | Team | Unread |
> |---|---|---|
> | *(one row per parent · team — `parents_html`)* | | |
>
> LATEST MESSAGE · {{inboundWebhookRequest.latest_message_at}}
> *"{{inboundWebhookRequest.latest_message_preview}}"*

Open your Coach Dashboard to read and reply:

**[ REPLY NOW ]** → https://www.disciplinerift.com/coach/messages

**Thanks for looking after your team!**
Discipline Rift

---
DISCIPLINE RIFT · Developing young players in volleyball, tennis, pickleball, and flag football
CONTACT · info@disciplinerift.com · (407) 614-7454
713 W. Yale Street, Orlando, FL 32804
