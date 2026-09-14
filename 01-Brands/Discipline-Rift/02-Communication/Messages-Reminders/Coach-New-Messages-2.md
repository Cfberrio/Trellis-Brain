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

# Coach New Messages — Email 2 (last reminder)

**Workflow:** `DR | Webhook - Coach New Messages` · branch `else` (stage = 2)
**When:** 6 business hours after Email 1, only if the coach still has not opened the chat. Nothing after this until a parent writes again.
**Template file:** `brand-kit/email/transactional/message-notification-coach-2.html`
Back: [[Messages-Reminders-Home]]

**Subject:** Reminder: parents are waiting for your reply

**Preheader:** Still unread: {{inboundWebhookRequest.unread_count}} parent {{inboundWebhookRequest.messages_word}} on {{inboundWebhookRequest.team_names}}.

---

**DISCIPLINE RIFT**

REMINDER

Hey Coach {{inboundWebhookRequest.coach_first_name}},

## Parents are still waiting on you: {{inboundWebhookRequest.unread_count}} unread {{inboundWebhookRequest.messages_word}}.

Second and last reminder. A parent who does not hear back assumes nobody is reading, and that is the story they tell other parents.

Reply today, even if it is just to say you will follow up. If a parent writes again, we will let you know.

> **STILL UNREAD**
>
> | Parent | Team | Unread |
> |---|---|---|
> | *(one row per parent · team — `parents_html`)* | | |
>
> LATEST MESSAGE · {{inboundWebhookRequest.latest_message_at}}
> *"{{inboundWebhookRequest.latest_message_preview}}"*

Open your Coach Dashboard now:

**[ REPLY NOW ]** → https://www.disciplinerift.com/coach/messages

**Your team is counting on you!**
Discipline Rift

---
DISCIPLINE RIFT · Developing young players in volleyball, tennis, pickleball, and flag football
CONTACT · info@disciplinerift.com · (407) 614-7454
713 W. Yale Street, Orlando, FL 32804
