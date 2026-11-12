---
brain_note_id: "note:c2bbc051-8854-4caf-900a-6388fa7907a1"
canonical_key: "platform-technical-audit"
brand_id: "orlando_event_venue"
---
# Platform Technical Audit and Findings

## Canonical Statement

- **fact**: The OEV platform has significant security vulnerabilities, including public access to sensitive payroll and revenue functions, and lack of authentication for invoice creation and testing triggers.
- **fact**: Financial reporting and payroll systems contain critical errors, such as double-counting revenue, incorrect payroll calculations, and lack of support for recording payments made outside of Stripe.
- **fact**: Booking and status management systems are currently unreliable, with issues in reschedule pricing, cancellation logic, and automated status transitions.

## Evidence Log

- 2026-11-12T03:53:55.927Z — `clickup_doc_page:8cqnrff-27337/8cqnrff-40637`
  - `e1` (source_body): Severity: H = money, security or blocks the office now; M = wrong numbers or office friction; L = cosmetic or latent. ... S-1: Anonymous users (public website key) can run populate_staff_payroll_items... S-5: Paid add-on invoices never reach revenue... M-1: Reschedule never reprices... M-7: No way to record a balance paid outside Stripe

## Provenance

- Source: `clickup_doc_page` `8cqnrff-27337/8cqnrff-40637`
- Source hash: `560c1998e9d69e9a3101f101232443bb26ffdf639b64498b1f42f2d90de4a78c`
- Observed at: 2026-11-12T03:53:55.927Z
- Agent run: `9572bcc7-f9ad-45e6-b8eb-9fea51e21160`
- Validation run: `6b464c33-5057-4e66-b37b-129358276efa`
