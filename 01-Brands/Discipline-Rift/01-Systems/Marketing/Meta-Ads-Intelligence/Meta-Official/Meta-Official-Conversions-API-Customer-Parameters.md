---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/conversions-api-customer-parameters.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/conversions-api-customer-parameters.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "CAPI parameters"
meta_topic: Conversions API — customer information parameters and hashing rules
gate_mapping: tracking / signal quality
meta_publisher: Meta
meta_source_urls:
  - https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters/
retrieval_method: webfetch_full_body
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: full_page
---

# Conversions API — customer information parameters

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/conversions-api-customer-parameters.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

## What Meta states

Meta documents no single required `user_data` parameter. Quoted constraint: you must provide **"at least one"** user_data parameter.

### Parameters requiring hashing

| Parameter | Field | Meta's normalization rule (quoted) |
|---|---|---|
| `em` | Email | "Hashing required. Trim any leading and trailing spaces. Convert all characters to lowercase." |
| `ph` | Phone | "Hashing required. Remove symbols, letters, and any leading zeros." |
| `fn` | First name | "Hashing required. Lowercase only with no punctuation." |
| `ln` | Last name | "Hashing required. Lowercase only with no punctuation." |
| `db` | Date of birth | "Hashing required. We accept the YYYYMMDD format." |
| `ge` | Gender | "Hashing required. We accept gender in the form of an initial in lowercase." |
| `ct` | City | "Hashing required. Lowercase only with no punctuation, no special characters, and no spaces." |
| `st` | State | "Hashing required. Use the 2-character ANSI abbreviation code in lowercase." |
| `zp` | Zip | "Hashing required. Use lowercase with no spaces and no dash." |
| `country` | Country | "Hashing required. Use the lowercase, 2-letter country codes in ISO 3166-1 alpha-2." |
| `external_id` | External ID | "Hashing recommended." |

### Parameters that must not be hashed

`client_ip_address` ("must be a valid IPV4 or IPV6 address"), `client_user_agent`, `fbc` (click ID), `fbp` (browser ID), `subscription_id`, `fb_login_id`, `lead_id`, `anon_id`, `page_id`, `page_scoped_user_id`, `ctwa_clid`, `ig_account_id`, `ig_sid`. Each carries "Do not hash."

`madid` is listed without an explicit hashing statement on the captured page.

Normalization is not cosmetic: an unhashed-but-should-be-hashed value, or a correctly hashed value that was not normalized first, produces a different digest and therefore fails to match.

## What Meta does not state

- **This page does not document Event Match Quality scoring.** EMQ (a score out of 10) lives on a Business Help Centre page that is not fetchable. It is **not verified first-hand here** — see `event-match-quality.md` (pending).
- No statement on how many parameters are needed for good matching, only that more coverage helps. The "more parameters is better" framing came from a Help Centre page, not this one.
- No statement about server-side event deduplication mechanics on the captured page.
- Nothing about retention, or how long Meta stores hashed identifiers.

## Why it matters for DR

Gate item: **tracking / signal quality**.

DR's conversion is a completed season registration by a parent — a form submission with a real name, email, phone and almost always a home address, since the child attends a specific school. That is an unusually rich identity payload compared with an anonymous ecommerce checkout.

The consequence: the parameter coverage available to DR is high, so any gap between what the registration form collects and what actually reaches Meta is a self-inflicted signal loss. `em`, `ph`, `fn`, `ln`, `ct`, `st`, `zp` are all plausibly present at registration.

Normalization is where this quietly fails. Meta's rules are specific and easy to violate: a phone number sent with a `+1` and dashes intact, or a state sent as "Florida" rather than `fl`, hashes to something that will never match — and it fails silently. Nothing errors. The event is accepted. It just does not match.

On a small local account, match rate is not a reporting nicety. It is the input to the optimization the account depends on, and low-volume accounts have the least tolerance for signal loss.

This is a check, not yet a recommendation: verify what DR's registration flow actually sends and whether each field is normalized to Meta's stated rule before hashing.

## Open questions

- Verify EMQ scoring first-hand (needs rendered browser — Help Centre).
- Does DR currently run CAPI at all, or pixel only? Belongs to the DR domain, not here.
- Deduplication requirements when the same event is sent by both pixel and CAPI — needs the best-practices page fetched.
