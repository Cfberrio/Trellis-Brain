---
brand: Trellis-Core
area: strategy-models
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
owner: Trellis
last_updated: 2026-04-28
sensitivity: internal
hub_role: system-hub
---

# Strategy Models Home

## Parent
- [[00-Trellis-Core/Trellis-Home|Trellis Home]]

## Purpose
Shared abstract strategy layer for Trellis. Contains reusable commercial models, frameworks, and decision logic that any brand may reference but no brand owns.

This hub is shared infrastructure under Trellis-Core. It is not a brand, not a voice library, and not a copy source. Brand notes link in via `## Strategy References`. Strategy notes do not link out into brand notes.

## Scope
Strategy-Models contains:
- Hormozi knowledge domain (offers, leads, value, pricing, monetization, sales)
- future abstract frameworks (testing loops, feedback loops, leverage models)

Strategy-Models does not contain:
- brand voice
- brand offers
- brand copy
- brand evidence
- brand-specific funnels

## Children
- [[Hormozi-Home|Hormozi Home]]
- [[Hormozi-Linking-Contract|Hormozi Linking Contract]]

## Related
- [[00-Trellis-Core/Routing-Rules|Routing Rules]]
- [[00-Trellis-Core/Metadata-Standard|Metadata Standard]]

## Routing Rule
Strategy models load only when a task benefits from abstract optimization (offer design, pricing, objection logic, retention, acquisition, leverage, testing). They do not load by default for mechanical or voice-bound tasks.

## Naming Rule
All notes inside this folder must use a domain prefix to avoid collision with brand notes. Hormozi notes use `Hormozi-` prefix. Future framework notes use a prefix that identifies the source or model family.
