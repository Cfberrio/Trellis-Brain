---
brand: Trellis-Fields
area: projects
subarea: trellis-esign
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-22317 'Trellis e-Sign — Documentación' (pages 1, 5, 8) + TrellisEsign repo commits 2026-07-21 → 2026-08-13"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: system-hub
tags:
  - trellis-fields
  - product
  - esign
---

# Trellis e-Sign — Home

## Parent
- [[01-Brands/Trellis-Fields/00-Brand-Core/Brand-Home|Trellis Fields Brand Home]]

## Related
- [[01-Brands/Trellis-Fields/01-Systems/Marketing/Lead-Magnet-Strategy|TF Lead Magnet Strategy]]
- [[01-Brands/Cross-Brand/AI-Systems/AI-Systems-Home|AI Systems Home]]

## What it is
An electronic signature platform under the Trellis brand — a lean alternative to DocuSign. Two purposes: **internal Trellis use**, and a **free plan for external users as a lead magnet**.

Live: `easy-sign-express.lovable.app`. Repo `Cfberrio/trellis-e-sign`.

## Status: MVP complete and deployed
| Area | Status |
|---|---|
| Accounts and login (Google for users, email/password for admin) | done |
| Individual / company onboarding | done |
| Upload PDF, place fields, save draft | done |
| Send request + email (Gmail SMTP) | done |
| Signer signs without an account, with IP / UA / consent capture | done |
| Flattened final PDF + completion certificate + hashes | done |
| Signed PDF download (owner and signer) | done |
| Admin dashboard + account suspension | done |
| Free-plan limits | done |
| Void / cancel a request | done |
| Automatic expiry (hourly cron) | done |

## Three areas of the platform
1. **User app** — the owner creates an account, uploads a PDF, adds signers, places fields, sends and tracks.
2. **Signer side** — the recipient opens a secure link and signs, no account required.
3. **Admin dashboard** — internal Trellis oversight: users, documents, audit, usage, suspension.

## Architecture
- **Frontend:** TanStack Start (React 19 SSR) + Tailwind 4 + shadcn/ui, file-based routing.
- **Backend:** Lovable Cloud (Supabase: Postgres, Auth, Storage, Deno Edge Functions).
- **Auth:** Google OAuth for users, email/password for the internal admin.
- **Email:** Gmail SMTP via denomailer.
- **PDF:** `pdf-lib` for flattening and the certificate, `react-pdf` / `pdfjs-dist` for rendering.

Sensitive logic lives only in edge functions: `create-signature-request`, `get-signing-session`, `submit-signature`, `finalize-document` (idempotent), `send-email`, `send-reminder`, `void-document`, `get-signed-document`, `admin-update-account`.

End-to-end flow: upload → place fields → save draft → send → tokens generated and emailed → signer opens link (marked viewed) → signs → on completion `finalize-document` produces the final PDF plus certificate → both parties download.

## Shipped since the doc was written (Jul–Aug 2026)
- Trellis brand kit applied to the e-Sign shells: logo, palette, fonts, favicon (2026-07-28) — this closes the branding item that page 8 listed as the only pending piece.
- Field placement keyboard shortcuts (copy / paste / delete / undo).
- `full_name` field, required-by-default with opt-out, and next-to-unfilled navigation.
- Text fields accept multi-sentence paragraphs, and long text fits its field box on any viewport.
- Fields render at true size so dense stacks no longer overlap; responsive, legible, high-contrast signer theme.
- Mobile signature draw fix (pointer capture order) — the first draw used to be lost.
- Recipient column on the Documents dashboard; **Download All as ZIP** on completed packages.
- Signer values stamped above fillable-PDF form fields, plus repair-mode flags for re-finalizing already-signed requests.
- Email fix: whitespace-only HTML lines stripped so `=20` artifacts stopped appearing.

## Open items
- **Email deliverability.** Still Gmail SMTP without a Trellis domain: roughly 500 emails/day and real spam risk. When the Trellis domain exists, move to a verified domain with SPF/DKIM/DMARC, or to an HTTP email API.
- **Rotate the admin password.**

## Deliberately out of MVP scope
Reusable templates, SMS / strong identity verification, payment collection, advanced scheduled reminders, folders, client portals, team accounts, per-account custom branding, paid subscriptions, CRM integrations, API/webhooks, bulk send, advanced analytics.

## Maintenance lesson worth keeping
The 2026-07-08 end-to-end verification found **five blocking bugs in a product that was already marked "deployed"** — RLS function permissions, a pdf.js version mismatch, React hook ordering, admin detail routing, and an email send that failed on a premature client close. "Deployed" is not "verified". Run the end-to-end path against the published site before calling a build done.

## Next step
Deliverability is the item that limits external use as a lead magnet. Decide the Trellis domain, then migrate the sender.
