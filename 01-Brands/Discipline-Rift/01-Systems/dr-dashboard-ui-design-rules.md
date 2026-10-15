---
brain_note_id: "note:8eeb20ee-ade3-4c3a-a71a-84f5f4dc4857"
canonical_key: "dashboard-ui-design-rules"
brand_id: "discipline_rift"
---
# DR Dashboard UI Design Rules

## Canonical Statement

- **preference**: Dashboard headers must not repeat the 'DR' text next to the logo; the logo itself is sufficient branding. Headers should display the logo followed only by the role name (e.g., 'Admin', 'Coach').
- **rule**: The 'Admin' login card and sidebar must use the simplified 'Admin' label instead of 'DR Admin'. This applies to both desktop and mobile views.

## Evidence Log

- 2026-10-15T00:40:13.930Z — `clickup:86e3pc5g2`
  - `e1` (source_body): The sidebar header on the dashboard shows the DR logo and the text "DR Admin" right next to it. The logo already says DR, so repeating it makes no sense. Change the header text to just "Admin" (logo + "Admin"), and apply the same fix on every dashboard that has this pattern.
  - `e2` (source_child): Changed it to "Admin" in the admin sidebar (desktop + mobile use the same component) and on the admin login card. Commit 2da5f29, published and checked on prod (/login serves "Admin", "DR Admin" no longer appears anywhere in the site code).

## Provenance

- Source: `clickup` `86e3pc5g2`
- Source hash: `d0e5ac1b4c5ac4806a6ed9325e8cda5c22f969ad01a5fc1965dc958f46a30ca7`
- Observed at: 2026-10-15T00:40:13.930Z
- Agent run: `666c4e70-fb21-47f4-a15e-4de13c239839`
- Validation run: `caa4979c-f12f-482a-8b1e-586c4ec2bbe2`
