---
brand: Orlando-Event-Venue
area: dna
note_type: leaf
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-7037 page 8cqnrff-4857 (STRATEGY / DNA / OEV / 6) Conversion DNA)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Conversion

## Parent
- [[DNA-Home|OEV DNA Home]]

## Related
- [[Lead|OEV Lead]]
- [[../01-Systems/Sales/Sales-Process|OEV Sales Process]]
- [[../01-Systems/Sales/Closing-Logic|OEV Closing Logic]]
- [[../01-Systems/Sales/Follow-Up-Rules|OEV Follow-Up Rules]]
- [[../01-Systems/Sales/Objection-Handling|OEV Objection Handling]]
- [[../02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]]

## A. Entry Points
- **Primary:** inbound phone call (Google / venue directories)
- **Secondary:** website form / DM / directory inquiry

**System rule:** every lead moves into a **text thread** immediately after capture (continue in the medium they respond to).

## B. Decision Path (Lead → Cash → Ops → Proof)
```
Inbound lead
    → Contact captured
        → Availability + fit confirmed
            → Booking link sent
                → 50% deposit paid (date held)
                    → Add-ons selected (online)
                        → Pre-event reminders
                            → Event
                                → Post-event proof capture
```

**Scarcity rule (truthful):** dates are fixed supply; "held only when paid." No fake urgency.

## C. Call SOP (Voice Agent) — MUST follow this order

### Step 0 — Capture info FIRST (30 sec)
1. "What's your **name**?"
2. "Perfect [name], is **(XXX) XXX-XXXX** the best number to reach you?"
3. "What's the best **email** for your receipt + agreement?"

> Reason: collect as much info as possible so you can personalize medium, messaging, follow-up.

### Step 1 — Confirm availability inputs (60–90 sec)
- Date + start time + end time
- Guest count (≤90)
- Event type
- Alcohol (beer & wine only fit)

### Step 2 — Present the next step (binary + simple)
> "Great — if it's available, the next step to **hold the date** is the **50% deposit** through the website checkout."

### Step 3 — Convert call → SMS thread (while still on phone)
- "I'm texting you the booking link + key details now."
- Send **SMS #0** immediately.
- "Do you have a minute right now? I can stay with you while you complete the checkout."

### Step 4 — If they stall (one default close)
> "Totally understand — **what's your main concern?**"

Aligned with Closing: give them power to decide (yes or no), not let them linger in avoidance.

## D. Tour Handoff (Admin-run)
**When they ask for a tour:**
- Capture name + best mobile number (confirm + repeat-back)
- Set expectation: "Our admin runs tours and will text/call you to confirm a time."

**Internal policy (non-negotiable):** admin offers tour times **within 72 hours** because closer appointments show higher.

## E. AI SMS System — Rules of Engagement

### Bot rules (always on)
1. **Thread-first:** keep conversation in SMS (preferred medium)
2. **Stop-on-reply:** any inbound question = answered thread (no blasting scheduled texts over active conversation)
3. **Decision power:** when unclear, ask "what's your main concern?"
4. **Truthful scarcity only:** "date held once deposit paid" (no fake "others booking")
5. **Transparent automation:** people don't mind reminders; they mind being lied to

### Bot triggers (simple)
- If they ask **price / availability / rules** → answer + send booking link
- If they say **tour** → collect phone, confirm, admin follows up
- If they show intent but hesitate → "what's your main concern?" → resolve
- If unqualified (liquor / >90 / won't follow rules) → exit cleanly

## F. SMS Sequence (AI-friendly, deposit-forward, address near end)

### SMS #0 — Decision Packet (T+0, immediately after call)
```
Hey [NAME] — confirmed [DATE] [TIME WINDOW] is currently available.

Rates:
• Hourly: $140/hr (4-hr min) + $199 cleaning
• Daily: $899/day (24-hr access) + $199 cleaning

Fit: up to 90 guests • beer & wine only (no liquor)

To hold the date, checkout requires a 50% deposit (date is held once paid).

Book/pay: orlandoeventvenue.org

You can also add production packages + optional services during checkout.

Address: 3847 E Colonial Dr, Orlando, FL 32803

Reply with any question (or say "book" / "tour") and I'll guide you.

Reply STOP to opt out. HELP for help.
```

### SMS #1 — Day 1 (24 hours)
```
Quick check-in — still interested in [DATE]?

Reminder: the date is held once the 50% deposit is paid via orlandoeventvenue.org.

Address: 3847 E Colonial Dr, Orlando, FL 32803

If you want a tour, reply "tour" and confirm the best number for the admin to reach you.
```

### SMS #2 — Day 3 (proof)
```
Here are photos/video so you can visualize it fast:

Photos: [PHOTOS]
Video: [VIDEO]

If you want [DATE], book/pay here to hold it: orlandoeventvenue.org

Address: 3847 E Colonial Dr, Orlando, FL 32803

What's your main concern right now? (price, rules, timing, tour)
```

### SMS #3 — Day 5 (close-the-loop)
```
Last check-in — do you want [DATE]?

If yes, the next step to hold it is the 50% deposit at orlandoeventvenue.org.

Address: 3847 E Colonial Dr, Orlando, FL 32803

If you want a tour, reply "tour" and confirm the best number.
```

## G. Missed Call / Form Lead Workflow (Speed + Volume)
If they opt in and don't answer:
- Call within **5 minutes**
- **Double-dial** if no answer → leave VM → text immediately
- Continue attempts same day + next days per cadence
- Front-load attempts; don't stop after one
