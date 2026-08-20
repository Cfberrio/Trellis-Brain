---
brand: Orlando-Event-Venue
area: systems
subarea: marketing
note_type: synthesis
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT docs/marketing/POST-MORTEM-CAMPANA-GOOGLE-ADS-JUNIO-2026.md (analysis 2026-07-09) + ClickUp OEV/GOOGLE ADS doc 8cqnrff-22337"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - marketing
  - post-mortem
---

# Google Ads Post-Mortem — June 2026

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Marketing-Home|OEV Marketing Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit|Lead Magnet — Event Planning Kit]]
- [[01-Brands/Orlando-Event-Venue/06-DNA/Conversion|OEV Conversion DNA]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Follow-Up-Rules|OEV Follow-Up Rules]]

Campaign: "Event Venue Orlando" (Performance Max). Analysis date 2026-07-09. Central question: many leads came in during the campaign and did not close — how many, where were they lost, what do we learn.

## Executive findings
1. **The discount popup was 100% broken for the entire campaign.** From 29 May (the HOST100 rebrand), every person who filled the popup got "Something went wrong. Please try again." The lead was not saved, never reached GHL, never received an email. Last captured lead: 28 May. June leads: **zero**. Fixed and verified 9 July.
2. **The campaign ran blind.** The two conversion events configured in Google Ads (`purchase`, `booking_deposit_paid`) **never existed in the site code**. Google Ads received no real conversion in the whole period. Smart Bidding optimized with no signal.
3. **June was the worst booking month of the year** — 2 web bookings, one of them a $15 internal test, against 10–13/month from January to May.
4. **Date availability is a real bottleneck.** Of 149 leads in 2026 that stated a preferred date, **73 (49%) wanted a date that another client ended up booking**. Half the leads compete for the same dates, so follow-up speed decides who closes.
5. **Nothing was attributable** — the site captured no UTM and no `gclid`, and no loss reason was recorded anywhere in the funnel (16 cancellations that year, zero reasons noted).

## Root cause 1 — no conversion signal
- The only tag on the site was the base GA4 snippet sending page views. Zero `gtag()` event calls anywhere in the code.
- `booking_deposit_paid` existed neither on the site nor in the backend, so the Ads conversion action pointing at it could never receive data.
- Stripe breaks attribution: the client leaves to `checkout.stripe.com` and returns; without `stripe.com` in GA4 unwanted referrals, the return session is attributed to Stripe, not the ad.
- The `.lovable.app` domain was not declared in cross-domain configuration ("Needs Attention" in Tag Quality).

> The Google rep's hypothesis on the 9 July call was that the warning came from inactivity or lack of recent conversions. The real cause was that the event was never implemented. Absence, not inactivity.

Fix: `purchase` implemented in `src/lib/analytics.ts` + `BookingConfirmation.tsx`. Value = deposit charged, `transaction_id` = booking number (deduplicates), fires only on the initial checkout, not on balance or add-on payments.

## Root cause 2 — the broken popup (the gravest finding)
The 29 May popup rebrand (SAVE100 → HOST100) inserted an `event_type` column into `popup_leads`. The migration adding that column existed in the repo but **was never applied to the production database** — hand-written migrations do not apply themselves in this project, the same pattern as the recurring-invoice `pg_cron` job that had to be registered manually in June.

Effect: every popup INSERT failed from 29 May to 9 July. Because of the code ordering, the failure also skipped the GHL contact sync and the coupon email. Total silent loss of the channel for the six weeks that contained the entire ad campaign.

Scale: at the March–May rate of 33–58 leads/month, an estimated **40–90 leads were lost** — precisely the visitors the campaign paid to bring.

Prevention, now standing policy:
- After any deploy containing a hand-written migration, apply it in the Supabase SQL editor and verify.
- Test the popup in production, in incognito, after any change that touches it.

## Before spending another dollar on ads
- Conversion tracking deployed and verified with real data.
- Capture path (popup and booking form) tested in production that same week.
- UTM and `gclid` captured and stored on the lead.
- Loss reason recorded at cancellation and at lead death.
- `stripe.com` added to GA4 unwanted referrals; all domains declared cross-domain.

## Commercial reading
The campaign did not fail because of creative or bidding. It failed because the measurement layer and the capture layer were both broken, and neither had a check that would have surfaced it. The 49% date-collision figure is the more durable insight: in this business, **speed of follow-up is the conversion lever**, because half of all demand is fighting for the same dates.
