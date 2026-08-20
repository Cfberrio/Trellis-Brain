---
brand: Orlando-Event-Venue
area: systems
subarea: marketing
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT docs/superpowers/specs/2026-07-15-oev-onepage-redesign-design.md (ClickUp 86e2a4e96 §6) + commits 2026-07-15"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - marketing
  - website
---

# Website One-Page Redesign — July 2026

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Marketing-Home|OEV Marketing Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Voice-and-Tone|OEV Voice and Tone]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Website-Product-Standard|DR Website Product Standard]] — the visual system this borrows from

## Decision
Rebuild the public OEV site as a clean, modern **one-page** using the Discipline Rift visual language, while keeping all current content and business logic. Requested by Luis after the 14 July video review.

What transfers from DR: bold typography, motion system, pill buttons, stamps and bubbles, element placement. What does **not** transfer: palette and branding. OEV keeps its own brand.

## Hard requirements
1. **One page.** All marketing lives at `/`, navigated by anchors. The only end-user routes outside it are `/book`, `/schedule-tour`, `/tour`.
2. **Zero functional regressions.** GA4 untouched; the `/book` flow untouched, including `?type=hourly|daily` links; admin and staff dashboards untouched with no global shadcn token values changed; dynamic pricing via `usePricing` preserved (hourly, daily, cleaning fee, setup/breakdown, tablecloth, bar packages); contact form logic unchanged, restyled only; discount popup kept as-is.
3. **SEO.** Semantic h1/h2, and legacy indexed URLs redirect to anchors rather than 404: `/pricing → /#pricing`, `/gallery → /#gallery`, `/contact → /#contact`. Meta tags preserved.
4. **Motion accessibility.** Under `prefers-reduced-motion`, all content is visible without animation — initial states only inside a non-preference `gsap.matchMedia`, always `fromTo`.
5. Existing vitest suites pass unmodified.

## Page order
Sticky nav (white 92% + blur, 1px bottom border, shadow after scroll, anchor links, "Book Now" pill) → hero with oversized headline → pricing → add-ons → gallery carousel → tours card with rotated bubble and parallax → four-step how-it-works with numbered circles → FAQ accordion → final CTA band → black footer.

## What shipped alongside
- Legacy marketing routes redirected and dead components deleted.
- Gallery lightbox scoped and pinned to dialog bounds; mobile arrows kept inside the viewport.
- Brand OG tags and favicon replacing Lovable defaults.
- Sitewide copy pass: 5-star badge, em/en dashes removed, grammar fixes.
- Hero restored to the venue photo background with address link and 5-star badge.
- Admin 4-hour minimum production restriction removed for admins.

## Why it matters
The site is the top of a funnel where half of all leads compete for the same dates. A cleaner one-page shortens the path from landing to `/book` and removes the indexed dead ends that used to drop paid traffic.
