---
brand: Cheese-To-Share
area: systems
domain: delivery
note_type: canonical
status: active
used_for_ai: true
owner: Luis
last_updated: 2026-04-23
sensitivity: internal
hub_role: system-home
---

# Delivery Process

## Parent
- [[01-Brands/Cheese-To-Share/00-Brand-Core/Brand-Home|CTS Brand Home]]

## Related
- [[Quality-Standards]]
- [[Dependencies]]
- [[01-Brands/Cheese-To-Share/01-Systems/Finance/Pricing-Logic|CTS Pricing Logic]]

## Delivery surfaces
- Third-party delivery apps
- Pickup
- Catering setup / event execution

## Core rule
CTS delivery logic is not one system. It has:
- app-based fulfillment for daily orders
- event-based execution for catering

## Catering delivery / execution basics
- dependent on notice window
- dependent on package type
- dependent on setup complexity
- tied to deposit and final payment rules
