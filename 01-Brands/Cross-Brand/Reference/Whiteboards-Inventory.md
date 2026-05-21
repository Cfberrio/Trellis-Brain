---
brand: Cross-Brand
area: reference
note_type: inventory
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp whiteboards (6 total) — swept 2026-05-21"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# ClickUp Whiteboards — Inventory

## Parent
- [[01-Brands/Cross-Brand/Reference/Reference-Home|Cross-Brand Reference]]

## Related
- [[01-Brands/Cross-Brand/Cross-Brand-Home|Cross-Brand Home]]

## Purpose

Authoritative inventory of all ClickUp whiteboards in the Trellis workspace. Whiteboards are visual artifacts (canvases with sticky notes, shapes, mind maps, org charts). Their content can't be reliably extracted as text — they live as **referenced visual sources**.

## Whiteboards (6 total)

| Name | ID | Location | URL | Relevance |
|---|---|---|---|---|
| The Trellis Plan 2026 | `8cqnrff-6637` | Director 🧠 / Planeacion y Estrategia / Trellis Method | [open](https://app.clickup.com/9017418223/v/wb/8cqnrff-6637) | **High** — strategic plan |
| Trellis Organizational Chart | `8cqnrff-677` | (root) | [open](https://app.clickup.com/9017418223/v/wb/8cqnrff-677) | **Medium** — org chart |
| CTS | `8cqnrff-1697` | (root) | [open](https://app.clickup.com/9017418223/v/wb/8cqnrff-1697) | CTS-specific visual |
| trellis | `8cqnrff-14977` | (root) | [open](https://app.clickup.com/9017418223/v/wb/8cqnrff-14977) | Trellis visual notes |
| Whiteboard | `8cqnrff-15897` | (root) | [open](https://app.clickup.com/9017418223/v/wb/8cqnrff-15897) | Unnamed scratch |
| Whiteboard | `8cqnrff-1717` | (root) | [open](https://app.clickup.com/9017418223/v/wb/8cqnrff-1717) | Unnamed scratch |

## Sweep policy

- Whiteboards are **visual artifacts** — the MCP API does not return canvas content as readable text.
- Treat each whiteboard as a **referenced source link**, not extracted material.
- When the strategic content on a whiteboard graduates into a decision or doc, capture it as a canonical note in the right brand folder and link **back** to the whiteboard URL as the source.

## High-priority whiteboards to translate to notes

1. **The Trellis Plan 2026** — when reviewed, translate to a strategic plan note in `00-Trellis-Core/` or `01-Brands/Cross-Brand/Synthesis/`. Currently deferred.
2. **Trellis Organizational Chart** — when reviewed, translate to `01-Brands/Cross-Brand/Reference/Org-Chart.md`. Currently deferred.

## Dashboards (0 total)

No ClickUp dashboards exist in the workspace as of this sweep. If created later, add a `Dashboards-Inventory.md` sibling note here.
