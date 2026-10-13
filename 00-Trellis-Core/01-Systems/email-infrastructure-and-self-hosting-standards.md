---
brain_note_id: "note:81773f66-ced1-41c2-8681-a53ae2c76f8a"
canonical_key: "email-infrastructure-self-hosting"
brand_id: "trellis_core"
---
# Email Infrastructure and Self-Hosting Standards

## Canonical Statement

- **decision**: Self-hosting brand email requires a VPS with a static public IP, basic Linux administration skills, and the ability to manage SPF, DKIM, and DMARC records.
- **fact**: Typical challenges of self-hosting email include managing IP reputation, blacklists, 24/7 maintenance, TLS/DMARC compliance, and spam filtering.
- **rule**: New IPs often have poor reputation; it is recommended to use an SMTP relay (e.g., Mailgun, SendGrid, SMTP2GO) for outgoing mail initially.
- **process**: Operational maintenance for self-hosted email includes OS patching, Postfix/Dovecot/Rspamd/ClamAV management, log rotation, and backup restoration tests.

## Evidence Log

- 2026-10-13T20:50:41.299Z — `clickup:86dzp1m9h`
  - `e1` (source_child): Retos típicos de self‑hosting de email: reputación de IP, listas negras, mantenimiento 24/7, cumplimiento TLS/DMARC, y filtrado de spam. ... IPs nuevas suelen tener mala reputación; es común usar relay (Mailgun/SendGrid/SMTP2GO) para saliente al principio.

## Provenance

- Source: `clickup` `86dzp1m9h`
- Source hash: `3bb031b8f6630b3e5b0afbbdee2b790dc8f47aa7c7884c3775cec3362e062600`
- Observed at: 2026-10-13T20:50:41.299Z
- Agent run: `6bba23a5-57e1-4ed9-ba6f-511bf7db1b69`
- Validation run: `f0635f8d-07b4-40f9-90bb-0f46a85fd315`
