---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: playbook
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/dr-playbook.md (commit 3aa367c). Evidencia: 99 anuncios de competidores, 11 documentos oficiales de Meta, 16 claims de expertos validados"
owner: Cristian
last_updated: 2026-08-13
sensitivity: internal
hub_role: leaf
---

# DR Meta Ads Playbook

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Marketing-Home|DR Marketing Home]]
- [[../Systems-Home|DR Systems Home]]

## Relacionado
- [[DR-Meta-Ads-Experiments|DR Meta Ads Experiments]]
- [[Ad-Scripting-Playbook|DR Ad Scripting Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]] — toda la evidencia detrás de estas decisiones
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-Structure-Full-Method|Método completo de estructura DR]] — la versión larga, capa por capa
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks (Waves 1A–3)]] — por qué cada decisión es esa
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas]] — qué hay que verificar antes de tocar la cuenta

> [!info] Qué es esto
> Qué hacer y qué **no** hacer en la cuenta de Meta Ads de DR, con la evidencia detrás de cada decisión.
> Jerarquía de evidencia: datos reales de DR → documentación oficial de Meta → comportamiento observable de competidores → acuerdo entre expertos → opinión de un solo experto.

---

## Decisiones

| # | Decisión | Acción | Confianza |
|---|---|---|---|
| 1 | Re-extraer antes de actuar | **HACER PRIMERO** | ALTA |
| 2 | Verificar geo **y `location_types`** | **AUDITAR PRIMERO** | ALTA |
| 3 | Mantener la estructura 1/1/1 | **DEJAR COMO ESTÁ** | ALTA |
| 4 | Mantener todos los placements | **DEJAR COMO ESTÁ** | MEDIA |
| 5 | Introducir creativos de forma deliberada, en lotes | **ADOPTAR** (regla, no construcción) | ALTA |
| 6 | No usar cambios de spending limit como remedio | **ADOPTAR** (guardrail) | MEDIA |
| 7 | Verificar que el optimization event dispara; pixel/CAPI | **AUDITAR PRIMERO** | ALTA |
| 8 | Capturar el contenido creativo de DR en el extract | **ARREGLAR** | ALTA |

---

## Dónde está DR realmente

Todos los snapshots (2026-03-30 → 2026-05-12) coinciden: **1 campaña** (`DR SPRING 2`, `OUTCOME_TRAFFIC`, **PAUSADA**), **1 ad set** (`New Traffic Ad Set`, `LANDING_PAGE_VIEWS`), **1 anuncio** (`DR SPRING`).

Última ventana medida (2026-03-25 → 04-23): **$82.11 · 1.015 impresiones · 256 reach · 10 clics · CTR 0.99% · CPC $8.21 · CPM $80.90.**

> [!warning] Los datos tienen 3 meses y la campaña está pausada
> Ninguna decisión de abajo debe ejecutarse contra esa foto. Primero re-extraer.

Targeting actual: `advantage_audience: 1` sobre audiencia `DR HISTORIC`, **sin clave `geo_locations`**. Sin `publisher_platforms` → entrega en 11 posiciones. **Ninguna columna de conversión existe en los extracts.**

---

## 1 — Re-extraer antes de actuar

Los datos son del 2026-05-12. Además, cuarentena para `2026-05-11_meta_phase2_diagnostic.md` y su rehab: describen 4 campañas y ~$9.246 de gasto que **no aparecen en ningún snapshot**, incluido el tomado al día siguiente. Etiquetarlos, no citarlos.

## 2 — Verificar geo, y específicamente `location_types`

**Meta oficial:** `location_types` tiene dos valores — `home` y `recent` (*"recent location… as determined from mobile device data"*). **El default es ambos:** *"If no `location_types` array is provided, it will default to `['home', 'recent']`."*

**Por qué importa:** DR vende una temporada en una escuela concreta. La residencia **es** la calificación. Orlando es de los mercados turísticos más grandes de EE. UU., así que el default incluye visitantes que no pueden inscribir a un hijo en un programa de Orange County.

**Acción:** en Ads Manager registrar (a) las ubicaciones listadas, (b) si el selector dice "People living in this location" o "living in or recently in", (c) si la expansión de audiencia está ampliando más allá. **No cambiar nada hasta leer la configuración actual.**

## 3 — Mantener la estructura 1/1/1

> [!tip] Lo más valioso que previno esta investigación
> Sam Piliero usa cuatro campañas. Aplicarlo a DR habría sido un error bien citado.

**Meta oficial (PARTIALLY_SUPPORTED):** tres páginas convergen en consolidación — *"Combining ad sets and campaigns will help you get the results you need faster"*, *"Avoid high ad volumes… By combining similar ad sets, you also combine learnings"*. **Meta apoya la consolidación como dirección; Meta no dice que una campaña sea suficiente.**

**EL PRINCIPIO TRANSFIERE:** al volumen de DR, dividir el presupuesto empeora cuatro de las cinco causas de learning limited a la vez.
**LA IMPLEMENTACIÓN NO:** la arquitectura de Sam asume $1.000/día. A $2.70/día mataría de hambre cada celda.

**Acción: no construir nada.** Sin scale campaign, sin retargeting, sin retention, sin packs.

## 4 — Mantener todos los placements

IG feed se llevó 79% del gasto a $136 CPM vs Facebook feed a $34. Parece grave, pero son **10 clics sobre $82.11**, y la concentración probablemente refleja una semilla de audiencia pequeña, no un defecto de placement.

**Meta oficial (INSUFFICIENT_EVIDENCE):** documenta solo el comportamiento por defecto y **no publica ninguna afirmación de rendimiento por placement**. Efecto neto: el test de placements **baja de prioridad**, detrás de geo, tracking y mensaje.

## 5 — Introducir creativos de forma deliberada

**Meta oficial (PARTIALLY_SUPPORTED — la validación más fuerte del proyecto):** la lista de ediciones siempre significativas incluye *"Any change to ad creative"* y *"Adding a new ad to your ad set"*.

**EL PRINCIPIO TRANSFIERE:** cambiar o añadir creativo en un ad set vivo reinicia su learning phase.
**LA IMPLEMENTACIÓN NO:** los "packs" de Sam son su inferencia, no respaldada por Meta y en tensión con *"avoid high ad volumes"*.

**Acción:** tratar cada cambio de creativo como un reinicio deliberado y programado. **Agrupar cambios en lotes en vez de gotearlos.** Meta también advierte contra el exceso contrario: *"you shouldn't try to avoid the learning phase completely."*

## 6 — No usar cambios de spending limit como remedio

> [!important] El hallazgo que ninguna capa tenía sola
> Ambos expertos recurren a límites de gasto cuando un anuncio no entrega. **Ninguno menciona que hacerlo pueda tener un costo.**

**Meta oficial (SUPPORTED con matiz):** *"Ad set spending limit amount"* está en la lista de ediciones condicionalmente significativas: *"may or may not be significant, **depending on the magnitude of the change**."*

**Leer el matiz con precisión.** Esto **no** es "toda edición de spending limit reinicia el learning". Es: *puede* ser significativa, la magnitud decide, y **Meta no publica ningún umbral**.

DR hoy no tiene spending limits configurados, así que no hay exposición. Es un guardrail a futuro.

## 7 — Verificar el optimization event, pixel y CAPI

El ad set optimiza `LANDING_PAGE_VIEWS`, pero **ningún archivo de insights contiene columna de acciones ni LPV**. Volumen acotado por clics: 10 en 30 días (~2,3/semana). Pixel y CAPI: sin evidencia en ningún sentido.

**Es una auditoría, no un diagnóstico.** Nada indica que el tracking esté roto. Ver [[DR-Meta-Ads-Experiments#Antes de la lista de experimentos|nota sobre UNKNOWN]].

## 8 — Capturar el contenido creativo de DR en el extract

El extract no guarda contenido creativo — el único campo es `ad_name: "DR SPRING"`. **Consecuencia:** los 99 anuncios de competidores no tienen contra qué compararse. Las cuatro mejores observaciones (escuela/on-campus, rango de edad, fecha de temporada, destino específico) son **inevaluables, no ausentes**.

---

## Lo que deliberadamente NO importamos

| Rechazado | Por qué |
|---|---|
| Arquitectura de cuatro campañas | Asume $1.000/día. DR está en $2.70/día |
| Scale campaign dedicada | No hay pool de ganadores; existe un anuncio |
| Retargeting / retention | No hay pool de eventos de compra |
| "Packs" de creativos por ronda | Meta dice evitar alto volumen de ad sets |
| Mínimo de ad set a 1x CPA (~$100/día) | ~37x el gasto diario total de DR |
| Nudge de $5/día como práctica rutinaria | ~185% del gasto diario de DR |
| Ranking por incremental attribution | Requiere muchos anuncios con gasto real |
| "90% de los ads no gastan y está bien" | Cierto solo con suficientes tests |
| Ampliar el hook para desbloquear entrega | Va en contra de la calificación que DR necesita |
| Confianza / crecimiento de carácter como promesa principal | **Las reglas de claims de DR lo prohíben** salvo que se mida |

---

## Evidencia de competidores — solo dirección creativa

De `competitors/patterns.md` (99 anuncios, 5 marcas independientes). **Solo afirmaciones de presencia; Ad Library no publica gasto, CPA ni conversiones, y ningún anuncio se llama ganador.**

- **Ubicación de entrega nombrada en el creativo** — *"Soccer at Your Child's School! ⚽️🏫"* de Soccer Shots Orlando, el único de 99 que pone la ubicación en el título. 1 familia, muestra de 4 — bajo la barra de consenso, pero del análogo local más cercano.
- **Rango de edad explícito** — 3 de 5 familias.
- **Fecha de temporada + ventana de registro abierta** — 3 de 5 familias, incluidas las dos locales.
- **Destino a nivel de programa, no homepage** — 3 de 5 familias.

Informan el mensaje. No establecen rendimiento.

---

## Siguiente acción

Las decisiones 1, 2 y 7 son auditorías y se pueden hacer en una sola sesión en Ads Manager y Events Manager. **Nada en este playbook cambia una campaña.**
