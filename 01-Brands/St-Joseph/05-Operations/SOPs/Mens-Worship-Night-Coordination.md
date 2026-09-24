---
brand: St-Joseph
domain: operations
area: sops
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: curated
owner: Luis
last_updated: 2026-09-18
sensitivity: internal
up:
  - "[[01-Brands/St-Joseph/00-Brand-Core/Brand-Home]]"
tags:
  - sop
  - worship-night
  - fraternity-of-st-joseph
---

# SOP: Men's Worship Night coordination (Fraternity of St. Joseph)

**Purpose:** Secure priest, sacristan, and church coverage for the monthly Men's Worship Night, and notify the parish liturgy team ahead of time.
**Trigger:** ~2 to 3 weeks before the next Worship Night. Also after any change of date.
**Owner:** Luis Torres (Worship Pillar Coordinator).
**Tools:** Claude Code + Composio (Gmail account `LUIS TORRES`, id `ca_FrHkyHl9OdYp`), the Fraternity schedule sheet in the `fratstjoes@gmail.com` account.

## Context you need
- Men's ministry meets every Tuesday, 7:00 to 8:30 PM.
- 4 pillars, one per month: Fellowship, Formation, Service, Worship.
- Worship Night = Mass, Confessions, Adoration in the church.
- Sacristan: Tom Reich. Needs the sacristy open by 6:30 PM.
- Parish contacts:
  - Oriana Paez, Liturgical Coordinator, opaez@stjosephorlando.org, (407) 275-0841. Primary contact for priests and sacristans.
  - Hunter Spyckaboer, hspyckaboer@gmail.com. Ministry lead, always Cc.
  - Johanna Cedeno (jcedeno@stjosephorlando.org) is leaving; do not include.
- Priest request: whoever is available. Ask for someone other than the last priest when possible so the men meet more priests.
- No meetings: Sep 29 and Dec 29, 2026.

## Steps
1. **Get the date.** Open the schedule sheet in the fratstjoes account. If unavailable, fallback rule used so far: Worship = first Tuesday of the month (only one confirmed data point, Sep 1 2026). Confirm before sending.
2. **Check history.** In Claude: search Gmail for `"worship night"` on the Luis account to see who served last time and any open threads.
   ```
   composio execute GMAIL_FETCH_EMAILS --account ca_FrHkyHl9OdYp -d '{"query":"\"worship night\"","max_results":20,"include_payload":false}'
   ```
3. **Draft the email.** To Oriana, Cc Hunter. Subject: `Men's Worship Night - Tuesday, <Month D>`. Use the template below. Create as a draft first, never send directly.
   ```
   composio execute GMAIL_CREATE_EMAIL_DRAFT --account ca_FrHkyHl9OdYp -d @draft.json
   ```
4. **Review the body in chat**, fix wording, then send the draft only on an explicit "send".
   ```
   composio execute GMAIL_SEND_DRAFT --account ca_FrHkyHl9OdYp -d '{"draft_id":"<id>"}'
   ```
5. **Follow up.** If no reply in 5 business days, reply in the same thread. When Oriana confirms the priest, reply thanks and note the priest's name in the schedule sheet.
6. **Marketing.** Once confirmed, submit the bulletin and communications requests:
   - https://stjosephorlando.org/sjcc-ministry-event-requests/
   - https://stjosephorlando.org/ministry-communications-request/
   - Flyer template (Canva): https://www.canva.com/design/DAHID1TdYzI/Q17PzABSAzrx2izc6s60Cw/edit

## Email template
```
Subject: Men's Worship Night - Tuesday, <Month D>

Hi Oriana and Hunter,

I hope you're both doing well. I'm coordinating the Worship Nights for the Fraternity of St. Joseph, so I wanted to reach out ahead of our next one.

Our next Men's Worship Night is Tuesday, <Month D>, from 7:00 to 8:30 PM in the church (Mass, Confessions, and Adoration), same format as our <last date> night.

Oriana, could you please help us schedule a priest for that evening and confirm we are covered for Mass, Confessions, and Adoration? Whoever is available works for us. Father <last priest> served last time, so if another priest is available this time, we would love to give the men a chance to meet more of our priests, but we are grateful for whoever can serve.

Tom Reich has been serving as our sacristan and asks that the sacristy be opened by 6:30 PM so he can prepare. If Tom is not available, please let me know and we can coordinate a sacristan together.

Thank you both for your help. Please let me know if there's anything else you need from me.

In Christ,
Luis Torres
Worship Pillar Coordinator, Fraternity of St. Joseph
luistorresportillo123@gmail.com
```

## QA before sending
- Date is a Tuesday and not on the no-meeting list.
- Oriana in To, Hunter in Cc, nobody else.
- Last priest name and last date are correct.
- Draft reviewed in chat, explicit "send" given.

## Done when
Oriana has confirmed a priest by name, Tom (or a substitute) is confirmed, and the bulletin request is submitted.

## Log
| Worship Night | Priest | Sent | Notes |
|---|---|---|---|
| 2026-09-01 | Fr. Benjamin | Hunter, Aug 26 | Handoff to Luis |
| 2026-10-06 | pending | Luis, Sep 18 | Asked for a priest other than Fr. Benjamin |
