---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/business-tools-data-restrictions.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/business-tools-data-restrictions.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Business Tools Terms"
meta_topic: Business Tools Terms — what advertisers may not send to Meta, incl. under-13 data and event-naming rules
gate_mapping: tracking / signal quality, setup quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/legal/terms/businesstools
retrieval_method: rendered_browser
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: partial
research_questions: [A3]
---

# Business Tools Terms — data restrictions

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/business-tools-data-restrictions.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved first-hand because Wave 1A proposed an optimization event gated on a **child's age and school**, and DR's entire audience is children aged 6–12. That proposal cannot be evaluated without the terms that govern what may be sent to Meta through Pixel or the Conversions API.

## What Meta states

The restriction, verbatim and complete:

> *"You represent and warrant that you will not share Business Tool Data with us that (i) you know or reasonably should know is from or about children under the age of 13, (ii) includes Contact Information not hashed in accordance with Section 1.a.i, (iii) includes identifiers we do not permit, such as social security or credit card numbers, or (iv) includes or is based on, directly or otherwise, health information, financial information, consumer report information, or other categories of sensitive information (including any information defined as sensitive under applicable laws, regulations and applicable industry guidelines)."*

And immediately following it — the sentence that governs event design, verbatim:

> *"The names you choose and criteria you establish for your events, conversions, and any custom audiences you create must not reflect, imply or be based on any category of information described in this Section 1.h."*

Two features of this text are load-bearing and easy to skim past:

1. **"or is based on, directly or otherwise"** (clause iv) reaches derived data, not only raw fields. A signal computed *from* restricted information is still covered.
2. **The second sentence extends the restriction from the payload to the design** — the event's *name* and its *criteria* must not reflect, imply, or be based on any listed category. It is therefore not sufficient to strip child data out of the transmitted payload if the event's trigger condition is itself defined by that data.

Meta also states elsewhere in the same terms that the advertiser *"represent[s] and warrant[s] that you (and any data provider that you may use) have all of the necessary rights and permissions and a lawful basis … for the disclosure and use of Business Tool Data."*

## What Meta does not state

- **No safe-harbour construction is described.** The terms prohibit; they do not offer an approved pattern for advertisers whose customers are parents purchasing on behalf of under-13 children. Nothing found says "a generic signal derived internally is acceptable."
- **No definition of how far "based on … indirectly" reaches.** Whether an event meaning "this visitor met our internal eligibility rules" is "based on" child age when eligibility is defined by child age is **not resolved by this text**, and reasonable readings differ.
- No guidance specific to youth-activity, school, or child-program advertisers.
- These are contractual terms, not a technical control. Nothing here describes a system that blocks such data — compliance is the advertiser's warranty.

## Why it matters for DR

Gate items: **tracking / signal quality**, **setup quality**.

DR's participants are aged **6–12 — entirely under 13.** Its natural qualifiers (child's age band, the child's school) are exactly the fields clause (i) covers, and the second sentence means DR cannot simply launder them into an event whose *criteria* are those fields.

Concretely, this constrains the R2 "qualified custom event" rung proposed in `output/wave-1a-event-framework.md`:

- **Must not be sent to Meta:** child age or age band, child's school, or any other child-identifying or child-derived qualifying field, via Pixel or CAPI.
- **Must not be encoded in the design either:** an event named or triggered in a way that reflects or implies those categories.
- **May stay internal:** DR evaluating eligibility inside its own systems, for its own operations, is not Business Tool Data at all. The restriction governs what is *shared with Meta*.

**The privacy-minimising architecture — evaluate eligibility internally, send only a generic outcome signal — is a hypothesis, not a cleared design.** The blocking question is the second sentence: if the criteria establishing the event are DR's child-eligibility rules, a plain reading may still treat the event as "based on" a prohibited category. Nothing retrieved settles it.

**Standing rule for this domain:** no future implementation of R2, or of any DR optimization event, may place under-13 data or other prohibited information into Meta Business Tools — in the payload, in the event name, or in the criteria that fire it. Any R2 implementation requires a compliance review against these terms before build, and the review must reach the "criteria" sentence, not just the payload.

## Open questions

- Does Meta publish any guidance for advertisers whose end participant is a minor but whose purchaser is an adult? None was located.
- Is an internally-evaluated, generically-named eligibility event acceptable under the "criteria … must not … be based on" sentence? Unresolved and material — it decides whether R2 is buildable at all.
- Do applicable US laws (e.g. COPPA) impose constraints beyond Meta's terms for a business advertising children's programmes? Out of scope for this domain and not researched; flagged because it bears on the same decision.
