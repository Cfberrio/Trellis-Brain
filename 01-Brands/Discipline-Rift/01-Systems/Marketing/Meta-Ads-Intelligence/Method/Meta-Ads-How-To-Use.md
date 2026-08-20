---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/META_ADS_INTELLIGENCE_DR_USAGE.md"
repo_path: domains/ads/meta/intelligence/META_ADS_INTELLIGENCE_DR_USAGE.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/method
  - discipline-rift
aliases:
  - "Meta Ads How To Use"
  - "Cómo usar Meta Ads Intelligence"
---

# Meta Ads Intelligence — Discipline Rift

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Operating-Rules|Reglas de operación del dominio]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Experiments|DR Meta Ads Experiments]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Patterns|Patrones entre anunciantes]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-Structure-Full-Method|Método completo de estructura DR]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/META_ADS_INTELLIGENCE_DR_USAGE.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---
## Cómo utilizarlo

Fecha: 2026-08-13

Este documento no repite la investigación. Explica **cómo usar lo que ya está construido** cuando vamos a trabajar una campaña real de DR.

---

## 1. Qué se construyó

Una capa de inteligencia para Meta Ads que combina cinco fuentes:

- **Anuncios públicos de competidores** — lo que otras marcas están corriendo hoy en Meta.
- **Documentación oficial actual de Meta** — las reglas reales de la plataforma, verificadas de primera mano.
- **Conocimiento público de expertos** — recomendaciones de compradores de medios con experiencia.
- **Contexto y reglas de Discipline Rift** — la oferta real, el público real, el lenguaje permitido y el prohibido.
- **Resultados reales de DR** — cuando existan datos de la cuenta.

El objetivo es usar todo eso junto para tomar mejores decisiones en campañas reales, no para acumular investigación.

---

## 2. Cómo se construyó

1. **Competitor Ad Library intelligence** — se extrajeron y normalizaron 99 anuncios únicos de 6 anunciantes (5 marcas independientes), con evidencia guardada.
2. **Official Meta knowledge base** — 11 documentos de fuentes oficiales de Meta, cada uno con fecha y enlace.
3. **Expert intelligence** — se procesaron fuentes públicas de expertos y se extrajeron afirmaciones concretas con su cita textual.
4. **Validación de claims** — cada afirmación importante se contrastó contra la documentación oficial de Meta.
5. **DR playbook** — las decisiones que sí aplican a DR.
6. **Experimentos para DR** — pruebas concretas que DR puede realmente correr.

Regla clave que se respetó en todo: **una recomendación no entra si no se puede rastrear a una fuente verificable.**

---

## 3. Cuál fue la solución

Los dos archivos que importan:

```
domains/ads/meta/intelligence/output/dr-playbook.md
domains/ads/meta/intelligence/output/experiments.md
```

`dr-playbook.md` = qué hacer y qué **no** hacer en la cuenta de DR, con la evidencia detrás de cada decisión.
`experiments.md` = qué pruebas vale la pena correr, en qué orden, y cómo saber si funcionaron.

Todo lo demás (competidores, Meta oficial, expertos) es material de respaldo que alimenta a esos dos archivos.

---

## 4. Cómo se utiliza cuando vamos a hacer ads

**Esta es la sección importante.**

No hay que volver a investigar todo desde cero cada vez. La investigación ya está hecha y se reutiliza.

### Paso 1 — Definir qué campaña queremos trabajar

Ejemplos: *Fall Volleyball registrations*, *Tennis season*, *campaña de registro para una escuela específica*, *retargeting* (solo si existe una razón real).

Definir antes de pedir nada:

- qué estamos vendiendo;
- para qué escuelas o zona;
- fechas de la temporada y ventana de registro;
- precio u oferta;
- objetivo de negocio.

Si esto no está claro, ninguna recomendación va a servir.

### Paso 2 — Cargar el contexto existente

Claude Code debe leer como mínimo:

```
domains/ads/meta/intelligence/CLAUDE.md
domains/ads/meta/discipline-rift/CLAUDE.md
domains/ads/meta/intelligence/output/dr-playbook.md
domains/ads/meta/intelligence/output/experiments.md
domains/ads/meta/intelligence/competitors/patterns.md
```

No hay que releer todo el histórico salvo que la pregunta realmente lo pida.

### Paso 3 — Ver la campaña/configuración actual de DR

Si ya existe una campaña, **primero análisis READ-ONLY**. Revisar solo lo necesario para la decisión:

- estructura de campaña
- ad sets
- presupuesto
- geo
- placements
- optimization event
- anuncios y creativos actuales

**No hacer cambios automáticamente.** Primero entender, después recomendar, y ejecutar solo con aprobación.

### Paso 4 — Utilizar las skills que ya existen

**Skills de DR** (para datos reales de nuestra cuenta):

| Skill | Cuándo usarla |
|---|---|
| `ads-meta-dr-phase1-extract` | Para obtener datos y configuración actuales de la cuenta de DR |
| `ads-meta-dr-phase2-diagnostic` | Cuando hay que diagnosticar datos y resultados reales |
| `ads-meta-dr-phase3-campaign-rehab` | Solo cuando existe una campaña que realmente necesita recomendaciones de mejora |

**Skills de Intelligence** (para material externo):

| Skill | Cuándo usarla |
|---|---|
| `ads-meta-intel-adlib` | Solo cuando haga falta actualizar u observar anuncios de competidores. **No correrla en cada campaña** si lo que ya tenemos sigue siendo suficientemente reciente |
| `ads-meta-intel-ingest` | Solo para incorporar una fuente pública nueva cuando exista una pregunta importante que la base actual no responde. **No buscar expertos por buscar expertos** |

### Lo más importante de este paso

**Para crear una campaña normal de DR NO hace falta correr todas las skills.**

La mayoría de las veces alcanza con:

```
contexto de DR  +  playbook  +  experiments  +  datos reales de la campaña
```

Y solo se corre una skill adicional cuando realmente necesitamos datos nuevos.

---

## 5. ¿Hay que usar Pixel o CAPI?

Pixel y Conversions API son parte del tracking de DR, pero **este proyecto no requiere reconstruirlos ni configurarlos de nuevo cada vez que se crea una campaña.**

Hoy se consideran **sistemas existentes y protegidos**.

**No tocar** solo porque un documento interno diga `UNKNOWN`:

- Pixel
- Conversions API
- `event_id`
- deduplicación
- configuración de Events Manager

`UNKNOWN` significa que **esa información no estaba visible en ese extracto** — no que esté rota.

Si una campaña real demuestra un problema de tracking: **primero diagnosticarlo y reportarlo.** No modificar Pixel ni CAPI sin una razón demostrada y autorización explícita.

---

## 6. Prompt base para trabajar una campaña

Copiar, pegar y completar el objetivo:

```
TASK — BUILD / IMPROVE A REAL DR META CAMPAIGN

Use the existing Discipline Rift Meta Ads intelligence system.

Read:
- DR CLAUDE.md
- intelligence CLAUDE.md
- dr-playbook.md
- experiments.md
- competitor patterns

Goal:
[DESCRIBE CAMPAIGN]

Before recommending anything:
1. inspect relevant DR campaign/account data read-only;
2. compare the current setup and creative against the DR playbook;
3. use competitor evidence only for observable creative/message patterns;
4. use official Meta guidance for platform rules;
5. use expert advice only when transferable to DR's scale.

Return:
- recommended campaign structure
- budget approach
- geo
- placements
- optimization
- creative/message angles
- ads to create
- experiments worth running
- what should NOT be changed
- evidence behind each major decision

Do not modify Meta campaigns unless explicitly authorized.
Do not touch Pixel/CAPI unless a demonstrated tracking problem exists.
```

---

## 7. Flujo simple

```
CAMPAIGN GOAL
      ↓
DR CURRENT DATA
      ↓
DR PLAYBOOK
      +
META OFFICIAL
      +
COMPETITOR INTELLIGENCE
      +
TRANSFERABLE EXPERT KNOWLEDGE
      ↓
CAMPAIGN RECOMMENDATION
      ↓
USER APPROVAL
      ↓
EXECUTION
      ↓
REAL DR RESULTS
      ↓
BETTER NEXT DECISION
```

---

**La investigación no se repite en cada campaña. Se reutiliza. Solo se actualiza una fuente o se corre una skill nueva cuando existe una pregunta o dato que realmente lo requiere.**
