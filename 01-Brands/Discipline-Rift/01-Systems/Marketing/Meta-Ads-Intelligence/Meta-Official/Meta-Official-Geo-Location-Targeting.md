---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/geo-location-targeting.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/geo-location-targeting.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Geo targeting"
  - "location_types"
meta_topic: Geographic targeting — geo_locations and location_types
gate_mapping: geo accuracy
meta_publisher: Meta
meta_source_urls:
  - https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/basic-targeting
retrieval_method: webfetch_full_body
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: partial
---

# Geographic targeting — `geo_locations` and `location_types`

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/geo-location-targeting.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

## What Meta states

**The `location_types` enum.** Meta's Basic Targeting reference documents two values:

| Value | Meta's definition (quoted) |
|---|---|
| `home` | "People whose stated location in their Facebook profile 'current city' is in an area." |
| `recent` | "People whose recent location is in a selected area, as determined from mobile device data." |

**The default is both.** Quoted: *"If no `location_types` array is provided, it will default to `['home', 'recent']`."*

**Geographic granularities documented**, with Meta's stated limits:

| Granularity | Limit / range Meta documents |
|---|---|
| `countries` | array of country codes |
| `regions` | 200 |
| `cities` | 250 — radius "10 to 50 miles or 17 to 80 kilometers" |
| `zips` | 50,000 |
| `custom_locations` | 200 — radius "from 0.63 to 50 miles, or 1 to 80 kilometers" |
| `places` | 200 |
| `geo_markets` | 2,500 (Comscore Markets) |
| `electoral_district` | documented, no limit captured |
| `country_groups` | broader regions such as Europe or North America |

Note the radius floors differ: a **city** radius cannot go below 10 miles, while a **custom location** (lat/long or address) goes down to 0.63 miles. Tighter-than-10-mile targeting therefore requires `custom_locations`, not `cities`.

## What Meta does not state

- **This page does not document `travel_in`.** Meta's Business Help Centre prose describes a third "people traveling in this location" option, but that page is not fetchable (JS shell, see `README.md`) and was not retrieved first-hand. Whether `travel_in` remains a live API value, and whether the Ads Manager UI and the Marketing API expose the same set, is **unresolved** and must not be asserted either way from this file.
- No statement was captured on how `recent` location is refreshed, how long a person remains "recent" in an area, or what device-data sources feed it beyond "mobile device data".
- No statement on precedence when a person matches both `home` and `recent` in different areas.
- Nothing about delivery volume, cost, or performance consequences of any location type. Meta documents mechanics here, not outcomes.

## Why it matters for DR

Gate item: **geo accuracy**.

The default is `['home', 'recent']`. On a local Orlando account that default is not neutral — it means an ad set that never touched the location-type setting is, by Meta's own documentation, also reaching *"people whose recent location is in a selected area, as determined from mobile device data."*

Orlando is one of the highest tourist-volume metros in the United States. A parent visiting Walt Disney World from Ohio with their phone in their pocket satisfies `recent` for the Orlando area. They cannot enrol a child in an on-campus after-school season at an Orange County school.

DR's product is delivered at a specific child's specific school, across a season. Residency is not a nice-to-have qualifier for that offer — it is the whole qualification. Anyone matched on `recent` alone is structurally unable to buy.

Two checkable implications for the DR account, both inside the gate:

1. **`location_types` should be verified explicitly**, not assumed. The absence of a setting is a setting — it is `['home','recent']`.
2. **Radius floor matters.** If DR targets by city, Meta's documented minimum radius is 10 miles. Tighter school-catchment targeting requires `custom_locations`, where the floor is 0.63 miles.

Neither of these is a recommendation yet. Both are conditions to check against DR's actual ad sets in phase 2 diagnostic output before anything is proposed.

## Open questions

- Does `travel_in` still exist in the current API version, and does Ads Manager expose location types identically to the Marketing API? Needs the Help Centre page rendered, or a versioned API reference.
- What is DR's account actually set to? Not answerable from this domain — belongs to `domains/ads/meta/discipline-rift/` phase 2 output.
- Does Meta document any minimum audience size interaction with tight radius targeting? Not captured.
