---
brand: Discipline-Rift
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift PRODUCT.md + DESIGN.md (source: ClickUp task 86e27puq5 'Plan de Proyecto: Rediseño del Sitio Web de Discipline Rift', Jul 7 2026, approved by Trellis)"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - platform
  - website
  - brand
---

# Website Product Standard

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|DR Platform Home]]

## Related
- [[01-Brands/Discipline-Rift/00-Brand-Core/Voice-and-Tone|DR Voice and Tone]]
- [[01-Brands/Discipline-Rift/02-Communication/Marketing-Language-Library|DR Marketing Language Library]]
- [[01-Brands/Discipline-Rift/00-Brand-Core/Avatar|DR Avatar]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Website-One-Page-Redesign-2026-07|OEV One-Page Redesign]] — borrows this visual system

## Product purpose
A parent-oriented registration site for after-school youth sports (volleyball, tennis, pickleball, flag football) taught **at the child's own school, right after dismissal**. The whole site funnels to one action: **REGISTER**, which always opens with "Find Your School".

## Users
- **Primary:** parents of elementary kids, K through 5th grade, in Central Florida. Busy, mobile-heavy, sceptical of "supervised playtime" programs. They want real teaching, zero logistics, low commitment.
- **Secondary:** school partners ("bring DR to your school") and coach applicants.

## Copy rules — hard
- **Never** em dashes or en dashes.
- **Never** a dollar figure anywhere except the payment step. Before that: "low cost, everything included".
- The Value Guarantee is repeated at every decision point: **"100% refund anytime during the season."**
- Audience line: "Elementary · K through 5th · Beginner to advanced · No transportation needed."
- Brand sentence: "Sports at your child's school where coaches actually teach. Right after school."
- **REGISTER** is always uppercase and always routes to Find Your School.
- Short sentences. Parent to parent. Confident, warm. No hype adjectives.

## Visual system
- Layout model borrowed from the Verizon.com homepage structure and interaction rhythm — giant-word hero, pill sub-nav, full-bleed promo band, thin-outline card rows, tilted tiles, category grid — rendered in DR's minimalist brand. **Shape transfers, colours do not.**
- One accent colour carries the brand: **DR blue `#0497F7`**. Whitespace does the work.
- Sport colours are **restricted** to the hero sports line, sport-tile dots, and the program tier/skill module. Never global UI.
- Mobile mirrors desktop: card rows become horizontal snap-scroll, never vertical stacks.
- Motion via GSAP, with `prefers-reduced-motion` fully honoured.

## Business proof used on the site
Running at **55 schools across Central Florida**.

## Anti-references
- The previous DR site look: Ethnocentric display type in UI, full-bleed photo backgrounds, halftone/grain/aurora effects, neon orbs, cinematic GSAP preloaders. All replaced.
- Generic youth-sports-club templates: badge crests, grungy textures, action-photo heroes with dark overlays.
- Anything that shows a price before the payment step.

## Scope note
This standard governs the **public marketing + registration site**. The parent, coach and admin dashboards live in the same repo but are product surfaces and keep their own chrome.

## Why it is in the vault
This is the approved answer to "what may we say and how may it look" for DR. Any ad creative, landing page or campaign email should be checked against the copy rules above before it ships.
