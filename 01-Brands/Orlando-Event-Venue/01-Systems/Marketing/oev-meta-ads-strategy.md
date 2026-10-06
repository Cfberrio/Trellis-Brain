---
brain_note_id: "note:0f6db02b-08db-4030-a106-e566e9103742"
canonical_key: "meta-ads-strategy"
brand_id: "orlando_event_venue"
---
# OEV Meta Ads Strategy

## Canonical Statement

- **process**: OEV Meta Ads tracking requires a dual Pixel and Conversions API (CAPI) setup with server-side deduplication and mandatory capture of fbclid regardless of cookie consent.
- **rule**: Standard conversion events for the OEV funnel are defined as PageView, ViewContent (pricing/packages), Lead (form/tour request), Schedule (tour booked), InitiateCheckout, and Purchase.
- **process**: Geographic targeting for OEV ads focuses on the Orlando metro area, specifically utilizing a 5-10 mile radius around the venue address (3847 E Colonial Dr).
- **rule**: OEV ad campaigns utilize Ad Set Budgeting (ABO) with a 7-day click, 1-day view attribution window, excluding existing bookers via a 180-day Purchase custom audience.

## Evidence Log

- 2026-09-30T20:29:27.842Z — `clickup:86e327a9a`
  - `e1` (source_body): Set up Conversions API (CAPI) server-side... Define the conversion events for OEV's funnel: PageView, ViewContent, Lead, Schedule, InitiateCheckout, Purchase... Geographic targeting: Orlando metro area. Consider radius targeting around the venue (5-10 mile radius of 3847 E Colonial Dr)

## Provenance

- Source: `clickup` `86e327a9a`
- Source hash: `7700404aa0b307fbad5d79174ebfca581514d2a34c0de8f0a7365381d7fcb524`
- Observed at: 2026-09-30T20:29:27.842Z
- Agent run: `1cc480f1-429d-40d3-b2bc-f2378b555d77`
- Validation run: `1103cfe6-0f48-4409-bf40-275505854855`
