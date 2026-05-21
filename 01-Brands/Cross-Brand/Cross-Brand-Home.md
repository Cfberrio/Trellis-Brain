---
brand: Cross-Brand
area: brand-core
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
owner: Trellis
last_updated: 2026-05-21
sensitivity: internal
hub_role: brand-hub
---

# Cross-Brand — Home

## Parent
- [[00-Trellis-Core/Trellis-Home|Trellis Home]]

## Children
- [[Meetings/Meetings-Home|Meetings Home]]
- [[Real-Estate/Real-Estate-Home|Real Estate Home]]
- [[AI-Systems/AI-Systems-Home|AI Systems Home]]
- [[Founder-Admin/Founder-Admin-Home|Founder Admin Home]]
- [[Reference/Reference-Home|Reference Home]]
- [[Systems/Systems-Home|Cross-Brand Systems Home]]
- [[Synthesis/Synthesis-Home|Synthesis Home]]

## Related
- [[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home|DR Brand Home]]
- [[01-Brands/Trellis-Fields/00-Brand-Core/Brand-Home|TF Brand Home]]
- [[01-Brands/Cheese-To-Share/00-Brand-Core/Brand-Home|CTS Brand Home]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|OEV Brand Home]]
- [[01-Brands/Reliable-Venues/00-Brand-Core/Brand-Home|RV Brand Home]]

## Purpose
This folder holds content that **does not belong to a single brand**. It exists because the Trellis workspace generates many cross-cutting artifacts:
- Meeting notes (founder sessions, ad-hoc calls, AI note-taker output)
- Real-estate / venue partnership notes
- AI / Claude / MCP / Skills setup docs
- Founder admin (accounting, taxes, legal)
- Cross-team references (editor specs, naming guides)
- Cross-brand systems (framework definitions, sales reference)
- Pattern synthesis across brands

> [!warning] Brand isolation still applies
> Even though Cross-Brand content can REFERENCE multiple brands, the content here must not become a dumping ground for brand-specific material. If a doc is primarily about one brand, route it to that brand's folder instead.

## Routing Rule (when to land here vs in a brand folder)
A doc goes in `Cross-Brand/` only if:
1. It explicitly addresses multiple brands together (e.g., "Trellis decision affecting DR + CTS + OEV")
2. It has no brand context at all (Claude setup, MCP config, generic editor guides)
3. It is a meeting note where actions span multiple brands
4. It is a personal venue/partnership note that does not yet attach to a brand's project pipeline

Otherwise → route to the brand's folder.

## Sensitivity Rules (locked per operator decision 2026-05-21)
- **Credentials → hard exclude** (never extract; never reference values)
- **COMP doc → hard exclude** (compensation values never written to vault)
- **LLC / Adding Limited Members → `sensitivity: restricted`, `used_for_ai: false`**

## Source
This folder was created as part of [PLAN-v2.md](../../../../CLAUDE%20CODE/domains/ops/clickup/extraction-plan/PLAN-v2.md) execution. ClickUp source content lives in orphan docs (no space) + cross-brand spaces (Claude / Founder / Director / Mystery / STRATEGY).
