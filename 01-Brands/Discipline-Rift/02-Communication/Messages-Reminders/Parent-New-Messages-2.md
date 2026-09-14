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

# Parent New Messages — Email 2 (last reminder)

**Workflow:** `DR | Webhook - Parent New Messages` · branch `else` (stage = 2)
**When:** 6 business hours after Email 1, only if the parent still has not opened the chat. Nothing after this until the coach writes again.
**Template file:** `brand-kit/email/transactional/message-notification-parent-2.html`
Back: [[Messages-Reminders-Home]]

**Subject:** Still waiting: {{inboundWebhookRequest.unread_count}} unread {{inboundWebhookRequest.messages_word}} from your coach

**Preheader:** Quick reminder: {{inboundWebhookRequest.unread_count}} {{inboundWebhookRequest.messages_word}} from your coach still waiting.

---

**DISCIPLINE RIFT**

REMINDER

Hi {{inboundWebhookRequest.parent_first_name}},

## Still waiting: {{inboundWebhookRequest.unread_count}} {{inboundWebhookRequest.messages_word}} from Coach {{inboundWebhookRequest.coach_first_name}}.

Quick reminder! You still have unread messages in your dashboard. Some may be time sensitive from this week's practice.

This is our last reminder about these messages. If your coach writes again, we will let you know.

> **STILL UNREAD**
>
> | Team | Coach | Unread |
> |---|---|---|
> | *(one row per team — `teams_html`)* | | |
>
> LATEST MESSAGE · {{inboundWebhookRequest.latest_message_at}}
> *"{{inboundWebhookRequest.latest_message_preview}}"*

Open your Parent Dashboard to catch up:

**[ READ MESSAGES ]** → https://www.disciplinerift.com/parent/messages

**Thanks for staying connected!**
Discipline Rift

---
DISCIPLINE RIFT · Developing young players in volleyball, tennis, pickleball, and flag football
CONTACT · info@disciplinerift.com · (407) 614-7454
713 W. Yale Street, Orlando, FL 32804
