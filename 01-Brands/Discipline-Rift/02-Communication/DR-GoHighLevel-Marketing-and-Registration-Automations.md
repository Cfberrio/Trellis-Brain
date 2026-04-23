---
brand: Discipline-Rift
area: communication
note_type: manual
status: active
used_for_ai: true
owner: Luis
last_updated: 2026-04-23
sensitivity: internal
---

# DR GoHighLevel Marketing and Registration Automations

## Parent
- [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|DR Communication Home]]

## Related
- [[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home|DR Brand Home]]
- [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]]

## Purpose
Documents the confirmed GoHighLevel automation workflows active for Discipline Rift, covering newsletter nurture, registration abandonment recovery, and SMS-based marketing sequences. This is the starting reference for GHL's communication role in DR — separate from the n8n-based event reminder system documented in DR Communication Rules.

## Confirmed GoHighLevel Role in DR
GoHighLevel is used in Discipline Rift for:
- SMS communication
- Email marketing
- Communication workflows and automation
- Newsletter subscription follow-up
- Registration abandonment recovery

GHL in DR operates primarily at the top and middle of the funnel — driving conversions from general interest to completed registration, rather than managing post-booking logistics.

## Automation 1 — Newsletter Subscriber Nurture
**Trigger:** Contact subscribes to the Discipline Rift newsletter

**What it does:**
- Subscriber receives a sequence of emails after joining the newsletter
- Goal is to move them from general interest to active registration
- Specific number of emails and timing not yet confirmed — needs later documentation

**Certainty level:** Confirmed from user. Email count and cadence not yet documented.

---

## Automation 2 — Registration Abandonment Recovery
**Trigger:** Contact begins registration but does not complete it

**What it does:**
- Contact receives a sequence combining emails and SMS messages
- Goal is to return them to complete registration
- Exact number of messages, order, and timing not yet confirmed

**Certainty level:** Confirmed from user. Full sequence detail not yet documented.

---

## Automation 3 — Popup Tag SMS Sequence
**Trigger:** Contact is tagged with a tag that includes "popup"

**What it does:**
- Sends an initial SMS
- Waits
- Sends a second SMS
- Waits
- Sends a third SMS

Screenshots confirm the three-SMS pattern with wait steps between messages. Specific message content, wait durations, and the exact tag name are not fully legible from screenshots.

**Certainty level:** Sequence structure (3x SMS with waits between) confirmed from screenshots. Message content, exact tag name, and wait durations need later confirmation.

---

## Notes on Certainty

**Confirmed from user:**
- GHL is used in DR for SMS, email marketing, and communication workflows
- Newsletter subscriber nurture automation exists
- Registration abandonment recovery automation exists — uses both email and SMS
- Additional DR automations exist in GHL beyond what is documented here

**Confirmed from screenshots:**
- Popup tag SMS sequence: three SMS messages with wait steps between them

**Not yet documented in full detail:**
- Email count and cadence for newsletter nurture
- Full sequence structure for abandonment recovery
- Complete DR automation inventory in GHL beyond the three documented here
- Exact tag name, message content, and wait durations for popup SMS sequence
