---
brain_note_id: "note:c9d71bcb-1ea3-4700-8f6c-94b4d087cf1e"
canonical_key: "composio-mcp-email-config"
brand_id: "trellis_core"
---
# Composio-MCP-Email-Configuration

## Canonical Statement

- **rule**: Claude's email access via Composio MCP must be configured for each in-scope Google account individually to prevent 404 errors when performing actions against specific addresses.
- **fact**: The in-scope accounts for Trellis AI email integration include Trellis (grouptrellis@gmail.com), Cheese (Work), Cheese to (cheesetoshare.us), Discipline, and Empanada (Work).
- **process**: When connecting accounts to Composio, the specific email address behind each Chrome profile name must be recorded, as profile names like 'Luis' or 'Discipline' do not inherently show the address.

## Evidence Log

- 2026-10-06T16:10:13.174Z — `clickup:86e3jt0h9`
  - `e1` (source_body): Connect every in-scope Google account... to the Composio MCP so Claude has email access... current Composio connection is only logged into info@disciplinerift.com... actions against other accounts fail with a 404. Record the email address behind each Chrome profile name.

## Provenance

- Source: `clickup` `86e3jt0h9`
- Source hash: `3d9ce11ca4e1328dea8314e9d52f9fc0a901f7fe4274def82e2dc7f69b2b4a1d`
- Observed at: 2026-10-06T16:10:13.174Z
- Agent run: `d57631ac-6b31-46a0-83ab-4bb7cdc2b0fd`
- Validation run: `ec0a8456-f588-4ab2-891b-38a592d6659e`
