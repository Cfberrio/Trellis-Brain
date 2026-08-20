---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: index
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: index
tags:
  - meta-ads
  - meta-ads/research-run
  - meta-ads/index
  - discipline-rift
aliases:
  - "Research runs — índice"
  - "Research Runs Index"
  - "Bitácora de investigación Meta Ads"
---

# Research runs — la bitácora de cómo se investigó

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación]] — lo que cada corrida intentaba cerrar
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks]] — el entregable de cada ola
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]

---

> [!abstract] Qué es esto
> Una corrida de investigación registra **qué se buscó, qué se descartó, qué se ingirió, cuánto se gastó y qué quedó sin cerrar**. Es lo que hace auditable el resto de la carpeta: si una afirmación te parece dudosa, aquí está de dónde salió y qué se rechazó en el camino.
> El costo total de retrieval pagado en todo el proyecto es de centavos — la mayoría de las corridas gastó **$0.00**.

## Olas de investigación

| Corrida | Preguntas | Entregable | Nota |
|---|---|---|---|
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-13-A1-A2-A3\|2026-08-13 · A1/A2/A3]] | objetivo · evento · calidad vs cantidad | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1A-Objective-and-Optimization-Event\|Wave 1A]] | **Corregida el mismo día**: la auditoría encontró seis errores materiales de interpretación. Donde el log de la corrida choca con las correcciones, **mandan las correcciones** |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-13-B1-B2-B3\|2026-08-13 · B1/B2/B3]] | volumen · presupuesto · aprendizaje a bajo volumen | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget\|Wave 1B]] | Incluye el chequeo read-only del sistema real de DR (Supabase, Stripe, sin CRM). **$0.00 gastados** |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-13-C1-C2-C3-C4\|2026-08-13/14 · C1–C4]] | arquitectura de campaña | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2A-Campaign-Architecture\|Wave 2A]] | **Parchada tras auditoría externa**: la arquitectura sobrevivió, pero se aplicaron siete correcciones de alcance y epistémicas. No se re-corrió investigación |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-14-D1-D2-D3-D4\|2026-08-14 · D1–D4]] | método creativo | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method\|Wave 2B]] | Parche final de evidencia externa: la capa de practicantes era **una sola voz** y cuatro reglas estaban más fuertes que su evidencia. 4 candidatos evaluados, 3 ingeridos, 1 diferido. **$0.00** |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-14-E1-E2-E3-G1-G2\|2026-08-14 · E1–E3, G1–G2]] | audiencia · geo · atribución · medición | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-3-Audience-and-Measurement\|Wave 3]] | **Cinco preguntas cerradas con cero fuentes nuevas ingeridas** — la documentación de Meta ya las resolvía. **$0.00** |

## Adquisición de fuentes

| Corrida | Qué hizo |
|---|---|
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-14-YouTube-Apify\|2026-08-14 · extracción YouTube (Apify)]] | Adquisición dirigida de **como máximo dos** fuentes de YouTube de alto valor. No es una ola nueva y no reabrió ninguna pregunta. Gasto: **~$0.13** |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Audit-2026-08-14-YouTube-Sources\|2026-08-14 · auditoría pre-ingesta]] | Auditoría de esas dos fuentes **antes** de ingerirlas |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-19-Phase2-Run-Report\|2026-08-19 · Phase 2, reporte de ejecución]] | Recuperación masiva del material público del panel a un corpus fechado y trazable. **Sin extracción de claims** — eso es otra fase |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-19-Phase2-Ingestion-Report\|2026-08-19 · Phase 2, reporte de ingesta]] | Extracción de claims a `knowledge/experts/`. Perfiles completos, 8–12 claims por experto, etiquetando honestamente cuando un claim no mapea a ninguna pregunta abierta |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-19-Phase3-Jon-Loomer-Notes\|2026-08-19 · Phase 3, notas Jon Loomer]] | Notas de trabajo de la revisión de video completa, único archivo `per-video` que quedó en el repo |

## Evidencia por video (el par corregido)

Estas cuatro notas son el ejemplo trabajado de cómo se revisa un video: transcripción cruda + mapa de evidencia contra los claims que se le habían atribuido.

| Fuente | Transcripción | Mapa de evidencia |
|---|---|---|
| Ben Heath — *The NEW WAY To Test Facebook Ads (Post Andromeda)* | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Transcript-Ben-Heath-Post-Andromeda\|abrir]] | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Evidence-Ben-Heath-Post-Andromeda\|abrir]] |
| Dara Denney — *How to Test Facebook Ads Creatives at Every Budget* | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Transcript-Dara-Denney-Creative-Testing\|abrir]] | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Evidence-Dara-Denney-Creative-Testing\|abrir]] |

Esa revisión correctiva es la que demostró que el muestreo de pasajes producía errores de atribución — y por eso Phase 3 exigió leer los 463 videos **de principio a fin**.

---

## Lo que estas corridas enseñan como método

1. **Auditar la propia salida encuentra errores reales.** Wave 1A tenía seis; Wave 2A recibió siete correcciones. Ninguna se descubrió sola.
2. **Cerrar preguntas sin gastar es un buen resultado**, no un atajo: cinco preguntas de Wave 3 cerraron con documentación de Meta ya capturada.
3. **Una sola voz no es capa de evidencia.** Wave 2B tuvo que ampliarse porque su capa de practicantes era Loomer y nadie más.
4. **La ausencia de código no prueba la ausencia del sistema.** El grep de Pixel/CAPI se corrigió después: no encontrar implementación en los repos inspeccionados no prueba que no exista una integración viva o de partner.
