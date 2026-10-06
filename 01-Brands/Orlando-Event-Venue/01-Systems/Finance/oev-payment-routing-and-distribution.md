---
brain_note_id: "note:7c7d83e8-a3e5-4e5a-a128-56ea8dcbab82"
canonical_key: "payment-routing-and-distribution"
brand_id: "orlando_event_venue"
---
# OEV Payment Routing and Distribution

## Canonical Statement

- **process**: OEV uses Stripe Connect to automatically route payments by category: Base Rent (20% fee to RV, remainder to D'Space), Cleaning/Services (8% fee to RV, remainder to D'Space), and F&B (8% fee, remainder to D'Loft).
- **rule**: Accounting and transfers utilize category-specific metadata to separate venue income from costs and partner distributions.

## Evidence Log

- 2026-10-04T03:41:20.301Z — `clickup_chat_thread:8cqnrff-2077/80170035389901`
  - `e1` (source_child): Stripe Connect los separa y enruta automáticamente por categoría: base rent (20% fee a RV, resto a D’Space), cleaning/servicios (8% fee a RV, resto a D’Space) y F&B va directo a D’Loft.
  - `e2` (source_child): Connect con transfers/metadata por categoría para separar ingresos del venue vs. cost

## Provenance

- Source: `clickup_chat_thread` `8cqnrff-2077/80170035389901`
- Source hash: `bdb0ba6fbdee09097ec1353c0d8d0f8d13b353bae4419d819ba68a524d3e8fe0`
- Observed at: 2026-10-04T03:41:20.301Z
- Agent run: `0cb98489-437f-4960-a1c6-c0653c9640a2`
- Validation run: `b70c9f50-2e93-4483-91dc-02cb52e80238`
