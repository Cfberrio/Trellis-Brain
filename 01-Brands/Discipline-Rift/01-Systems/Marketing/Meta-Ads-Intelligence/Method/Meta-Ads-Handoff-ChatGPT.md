---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/HANDOFF-CHATGPT.md"
repo_path: domains/ads/meta/intelligence/HANDOFF-CHATGPT.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/method
  - discipline-rift
aliases:
  - "Meta Ads Handoff"
  - "Briefing de ejecución Meta Ads"
---

# Meta Ads Intelligence — Briefing de ejecución

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Operating-Rules|Reglas de operación del dominio]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-How-To-Use|Cómo usar el sistema]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/HANDOFF-CHATGPT.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

> **Para quien lea esto (ChatGPT u otro modelo):** este documento es autocontenido. No tienes acceso al repositorio. Todo lo que necesitas saber del entorno está aquí abajo, ya verificado. **No propongas construir nada que aparezca en la sección 2 como "ya existe".** Si tu recomendación incluye crear un repo nuevo, escribir un pipeline de TypeScript, o pedir una API key de Anthropic, está fuera de alcance — lee la sección 3 antes de responder.

**Fecha del inventario:** 13 de agosto de 2026
**Marca activa:** Discipline Rift (DR) — única por ahora
**Ubicación de trabajo:** `domains/ads/meta/intelligence/` dentro de un repo Git local ya existente

---

## 1. Objetivo en una frase

Construir un sistema que extraiga **los anuncios que corren otras marcas en Meta Ad Library**, los cruce con documentación oficial de Meta y con conocimiento público de expertos, y produzca un playbook accionable + experimentos concretos para las campañas de Discipline Rift.

No es un content scraper. Si el sistema solo produce material de lectura, falló.

---

## 2. Inventario del entorno — verificado, no asumido

### 2.1 Motor de IA

| Componente | Estado |
|---|---|
| Claude Code (Opus 5, contexto 1M) | Activo. **Es el LLM del sistema.** Orquesta, razona, escribe archivos, llama herramientas. |
| Anthropic API key | **No existe y no se necesita.** El razonamiento ocurre dentro de la sesión de Claude Code. |
| OpenAI API key | No se usa. |

**Implicación:** las tres "instancias de Claude" del plan original (extractor, validator, DR adapter) no son llamadas HTTP. Son **skills** — archivos markdown con instrucciones que Claude Code ejecuta. Cero código, cero SDK, cero factura de tokens aparte.

### 2.2 Scraping — Apify

| Componente | Estado |
|---|---|
| Apify MCP Server | **Ya conectado.** `.mcp.json` → `https://mcp.apify.com`, tipo HTTP, autenticado por OAuth. |
| `APIFY_TOKEN` en `.env` | No hace falta. El MCP maneja la autenticación. |
| `apify-client` (npm) | No instalado y no se necesita. |
| Plan Apify | Free tier ($5/mes de crédito). Suficiente para el MVP completo. |

**Herramientas Apify disponibles desde la sesión:**
`search-actors`, `fetch-actor-details`, `call-actor`, `get-dataset-items`, `get-actor-run`, `abort-actor-run`, `get-key-value-store-record`, `apify--rag-web-browser`, `search-apify-docs`, `fetch-apify-docs`.

Es decir: se puede buscar un actor, leer su input schema, ejecutarlo y leer su dataset **sin escribir una línea de código**.

### 2.3 Herramientas nativas (gratis, sin Apify)

| Herramienta | Uso |
|---|---|
| `WebSearch` | Discovery por keyword. Reemplaza al Apify Google Search Scraper. |
| `WebFetch` | Leer artículos, blogs, landing pages, documentación de Meta. Reemplaza al Apify Website Content Crawler. |
| `Read` / `Write` / `Edit` / `Bash` / `Grep` | Sistema de archivos completo. |

**Regla de costo:** Apify solo para lo que las herramientas nativas no pueden hacer — Meta Ad Library, transcripts de Instagram Reels, subtítulos de YouTube. Todo lo demás va nativo y gratis.

### 2.4 Otros MCPs conectados

ClickUp (capa de ejecución/tareas), Lovable, Playwright, Figma, Composio, claude-mem. Vía conectores de claude.ai: Gmail, Google Drive, Canva, QuickBooks, Higgsfield. **Notion requiere autorización, actualmente no disponible.**

Relevante para este proyecto: **ClickUp** — los experimentos aprobados se convierten en tareas ahí. ClickUp es la capa de ejecución; este sistema es la capa de inteligencia.

### 2.5 Credenciales que ya existen en `.env`

```
META_AD_ACCOUNT_ID
META_APP_ID
META_APP_SECRET
META_GRAPH_VERSION
META_SYSTEM_USER_TOKEN        ← token de sistema de Meta, ya funcional
GOOGLE_ADS_*                  (6 variables)
GHL_PRIVATE_KEY_DR / _CTS / _OEV
LOCATION_ID_DR / _CTS / _OEV
SOCIAL_METRICS_*              (tokens de página e IG por marca)
```

**Nota sobre la API oficial de Ad Library:** existe token de Meta, pero la Ad Library API oficial está limitada a anuncios de temas sociales, elecciones y política. **No cubre anuncios comerciales normales**, que es exactamente lo que necesitamos. Por eso Ad Library va por Apify, no por la Graph API. No propongas usar el token de Meta para esto.

### 2.6 Pipeline de Meta Ads que ya corre

`domains/ads/meta/discipline-rift/` — activo desde marzo 2026:

```
data/raw/          38 CSVs de la cuenta real de DR
                   (campaign/adset/ad insights, by-placement, objects snapshots)
output/fase-2/     3 diagnósticos generados
output/fase-3/     2 SOPs de rehab generados
scripts/           run_meta_insights.py, run_meta_objects.py,
                   run_meta_phase1_extract.sh
CLAUDE.md          contexto de marca de DR (227 líneas) ← ver 2.7
```

Tres skills lo operan: `ads-meta-dr-phase1-extract`, `ads-meta-dr-phase2-diagnostic`, `ads-meta-dr-phase3-campaign-rehab`.

**Esto mira hacia adentro** (nuestra cuenta). **Lo que vamos a construir mira hacia afuera** (los demás). Son dominios separados a propósito.

### 2.7 Contexto de marca de DR — ya escrito, no reescribir

`domains/ads/meta/discipline-rift/CLAUDE.md` ya define, en 227 líneas:

- **Modelo en una línea:** DR ayuda a padres de kids 6-12 a mantener a su hijo activo con temporadas deportivas after-school, on-campus, fun-first, beginner-friendly, lideradas por coaches entrenados.
- **No negociables:** marca local de Orlando FL (no nacional, no multi-estado). Padre paga, niño participa. Edad 6-12. Beginner-friendly. Fun-first. Coach-led. No elite-first. No high-performance.
- **Los 3 deliverables que realmente venden:**
  1. On-campus convenience
  2. Beginner-friendly, safe-to-learn structure
  3. Trained coaches + clear season structure / Tier System
- **Claim rules:** "confidence", "friends", "sportsmanship", "discipline" solo como byproducts, nunca como promesa principal — DR no los mide. No inventar métricas que el negocio no trackea. Si la garantía no está finalizada, no mencionarla.
- **Lenguaje prohibido por defecto:** "next level", "elite", "serious athlete", "high performance", "future champion", "tryouts" (si el offer real no es tryout), "transform your child".
- **Regla final:** si una recomendación no mejora setup quality, tracking/signal quality, learning conditions, geo accuracy, placement control, creative clarity, u offer-message fit — se deja fuera.

Además existe un vault de Obsidian (`Trellis-Brain/01-Brands/Discipline-Rift/00-Brand-Core/`) con Avatar, Positioning, Offers, Objections, Constraints, Value-Proposition — accesible bajo demanda, no por defecto.

**Implicación:** el `config/dr-context.md` que pedía el plan original **no se escribe**. Se referencia el archivo existente. Dos contextos de la misma marca se desincronizan garantizadamente.

### 2.8 Skills ya instaladas y reutilizables

Hay ~90 skills instaladas. Relevantes aquí:

| Skill | Para qué sirve en este proyecto |
|---|---|
| `competitor-profiling` | Perfilar competidores desde sus URLs. Reutilizable para la ficha de cada marca vigilada. |
| `competitive-analysis` | Análisis competitivo estructurado. |
| `paid-ads` | Estrategia de campaña, targeting, bidding. |
| `ad-creative` | Generación de variaciones de copy a escala. |
| `hooks` | Trabajo de hooks. |
| `marketing-psychology` | Marcos de por qué la gente compra. |

**No reescribir lo que estas skills ya hacen.** Las skills nuevas de este proyecto deben delegar en ellas cuando aplique.

### 2.9 Convenciones del repo

- Skills viven en `.claude/skills/<nombre>/SKILL.md`, con frontmatter `name` + `description` + `disable-model-invocation: true` para las de pipeline.
- Convención de nombres ya establecida: `ads-meta-dr-phase1-extract`, `ads-meta-dr-phase2-diagnostic`, `ads-meta-dr-phase3-campaign-rehab`.
- Cada skill de pipeline arranca con un "Paso 0 — Cargar contexto de dominio" que lee el `CLAUDE.md` del dominio antes de hacer nada.
- Reglas modulares en `.claude/rules/` con frontmatter `paths:` — se cargan según en qué carpeta se trabaja.
- Cada dominio bajo `domains/` tiene su propio `CLAUDE.md`, `README.md`, y rutas de data/output aisladas.
- Sin base de datos. Markdown + JSON + Git. El historial se audita con `git log`.

---

## 3. Restricciones duras — qué NO proponer

| No proponer | Por qué |
|---|---|
| Repo nuevo separado (`dr-ads-intelligence`) | Pierde el loop con la data real de la cuenta y con las skills de rehab que ya corren. Vive dentro del repo actual. |
| `src/ingest.ts`, `normalize.ts`, `analyze.ts`, `validate.ts`, `compare.ts`, `publish.ts` | Claude Code ya orquesta. Escribir TypeScript que llame a la API de Claude es construir un segundo sistema para hacer lo que este ya hace. |
| `ANTHROPIC_API_KEY` | Factura nueva, cero capacidad nueva. |
| `npm install apify-client @anthropic-ai/sdk dotenv yaml zod` | Sin código, sin dependencias, sin `package.json`. |
| Apify Google Search Scraper | `WebSearch` nativo hace lo mismo gratis. |
| Apify Website Content Crawler | `WebFetch` nativo hace lo mismo gratis. |
| Base de datos (Postgres, Supabase, vector store) | Markdown + JSON + Git es suficiente para el volumen del MVP. |
| Schedules y webhooks de Apify en el MVP | Automatizar antes de saber si el output sirve es gastar en repetir algo que quizá no queremos repetir. |
| Usar `META_SYSTEM_USER_TOKEN` para Ad Library | La API oficial no cubre anuncios comerciales. Ver 2.5. |
| Dos sistemas de scoring | Uno solo, de 14 puntos. Ver sección 7. |
| Tocar `domains/ads/meta/discipline-rift/` o las skills `google-ads-phase*` / `ads-meta-dr-phase*` | Pipelines en producción. Compatibilidad primero. |

---

## 4. Arquitectura acordada

```
domains/ads/meta/
├── discipline-rift/          YA EXISTE — mira NUESTRA cuenta (fases 1-2-3)
└── intelligence/             NUEVO     — mira HACIA AFUERA
```

Punto de unión, y donde está el valor real:

```
intelligence/output/dr-playbook.md
        ↓
   se lee como input opcional en ads-meta-dr-phase3-campaign-rehab
        ↓
   los cambios propuestos dejan de ser "lo que dice el diagnóstico"
   y pasan a ser "lo que dice el diagnóstico + lo que ya funciona afuera"
```

### Estructura de carpetas a crear

```
domains/ads/meta/intelligence/
│
├── CLAUDE.md                       # contexto y reglas de operación del dominio
├── README.md
├── PLAN.md                         # plan interno
├── HANDOFF-CHATGPT.md              # este archivo
│
├── config/
│   ├── competitors.yaml            # marcas a vigilar en Ad Library
│   ├── experts.yaml                # 4-6 expertos, no más
│   └── keywords.yaml               # queries de discovery
│
├── inbox/
│   └── urls.json                   # cualquiera del equipo pega una URL aquí
│
├── data/
│   ├── raw/                        # dumps crudos de Apify (fecha + fuente en el nombre)
│   └── index.json                  # URLs ya procesadas → dedup
│
├── competitors/
│   ├── ads/                        # un .md por marca vigilada
│   └── patterns.md                 # patrones repetidos entre marcas
│
├── knowledge/
│   ├── official-meta/              # documentación oficial resumida
│   ├── experts/                    # un .md por experto
│   └── topics/                     # un .md por tema (consenso + conflictos)
│
└── output/
    ├── dr-playbook.md              # ← el archivo maestro
    ├── experiments.md              # ← lo que hay que probar
    └── briefs/
        └── YYYY-MM-DD-brief.md
```

---

## 5. Los dos pilares

### Pilar 1 — Competitor Ad Extraction (**prioridad**)

Extraer de Meta Ad Library los anuncios que corren competidores y marcas análogas, y detectar patrones:

- oferta visible
- hook (primera línea / primeros 3 segundos)
- ángulo: conveniencia, precio, seguridad, resultado, identidad
- CTA
- formato: video / imagen / carousel
- **días que lleva corriendo el anuncio** ← la señal más importante
- cuántas variaciones activas corre la misma marca
- landing page destino

**Por qué "días corriendo" es la señal:** Ad Library no publica gasto ni conversiones de anuncios comerciales normales. Pero un anuncio activo 90 días casi seguro funciona — nadie quema presupuesto tres meses en un creative muerto. Longevidad es el único proxy público de performance.

**Lo que NO se afirma:** cuánto venden, cuánto gastan, cuál es su CPA. Ad Library no lo da. Inventarlo destruye la credibilidad del sistema entero.

### Pilar 2 — Public Knowledge (soporte)

Expertos públicos + documentación oficial de Meta, para distinguir si un patrón observado es táctica válida o vicio heredado.

Sin este pilar, el pilar 1 degenera en "copiemos al competidor" — que es exactamente cómo se propagan las malas prácticas en paid social.

---

## 6. Las 3 skills a construir

Nombres siguiendo la convención existente.

### 6.1 `ads-meta-intel-adlib` — Competitor sweep

**Input:** `config/competitors.yaml`
**Proceso:** Apify Ad Library actor vía MCP → dump crudo a `data/raw/` → extracción de patrones
**Output:** `competitors/ads/<marca>.md` + `competitors/patterns.md`

Schema por anuncio:

```yaml
advertiser:
ad_id:
first_seen:
days_running:
format:              # video | image | carousel
hook:                # primera línea / primeros 3s
offer:
angle:               # convenience | price | safety | outcome | identity
cta:
landing_page:
active_variations:   # cuántas versiones corre la misma marca
captured_at:
```

El output agregado debe responder: qué ángulos sobreviven más tiempo, qué ofertas se repiten entre marcas independientes entre sí, qué formato domina, qué hooks se repiten.

### 6.2 `ads-meta-intel-ingest` — Conocimiento público

**Input:** `inbox/urls.json` o una URL suelta
**Proceso:** detecta el tipo de fuente y enruta

```
instagram.com/reel        → Apify (caption + transcript)
youtube.com/watch         → Apify (metadata + subtítulos)
facebook.com/ads/library  → deriva a ads-meta-intel-adlib
cualquier otra            → WebFetch nativo
```

**Output:** claims estructurados en `data/raw/` + actualiza `knowledge/experts/<nombre>.md`

**Dedup obligatorio:** antes de procesar, chequear `data/index.json`. Si la URL canónica ya está, detenerse. Nada se procesa dos veces.

Schema normalizado, idéntico sin importar la fuente:

```json
{
  "id": "unique-id",
  "source_type": "instagram | youtube | website | meta_official | meta_ad_library",
  "source_url": "...",
  "author": "...",
  "title": "...",
  "published_at": "YYYY-MM-DD",
  "captured_at": "YYYY-MM-DD",
  "content": "...",
  "metadata": { "views": null, "likes": null, "comments": null }
}
```

Schema de claim extraído:

```json
{
  "topic": "campaign_structure",
  "claim": "...",
  "recommended_action": "...",
  "structure": { "campaign_type": null, "ad_sets": null, "ads": null },
  "context": { "business_type": "ecommerce", "spend_level": null },
  "evidence": { "quote_or_summary": "...", "timestamp": "08:42" },
  "published_at": "...",
  "captured_at": "...",
  "last_verified_at": "...",
  "confidence": 0.91
}
```

Regla: **si algo no está dicho explícitamente, devolver `null`.** No inventar.

### 6.3 `ads-meta-intel-playbook` — Validación + adaptación a DR

**Input:** todo lo anterior + `domains/ads/meta/discipline-rift/CLAUDE.md` + últimos outputs de `output/fase-2/`

**Proceso:**

1. Agrupar claims por tema
2. Contrastar cada claim contra `knowledge/official-meta/` → veredicto: `SUPPORTED` / `PARTIALLY_SUPPORTED` / `CONFLICTING` / `OUTDATED` / `INSUFFICIENT_EVIDENCE`
3. Comparar entre expertos → consenso y desacuerdos explícitos
4. Cruzar con `competitors/patterns.md` → ¿lo que los expertos dicen coincide con lo que las marcas realmente corren?
5. Traducir a DR: local, on-campus, padres de kids 6-12, KPI real = **costo por registro completado**
6. Puntuar (sección 7)

**Output:** `output/dr-playbook.md` + `output/experiments.md`

`dr-playbook.md` debe responder en una pantalla:

> Si hoy tuviéramos que reconstruir las campañas de DR, ¿qué haríamos y por qué?

Formato de experimento:

```markdown
# Experimento DR-001

## Hipótesis
## Evidencia (Meta oficial / expertos / competidores)
## Setup actual de DR
## Control
## Variante
## KPI primario        (costo por registro completado)
## KPIs secundarios    (CTR, CPC, landing page CVR)
## Observación mínima
## Regla de decisión
```

---

## 7. Scoring — una sola escala de 14 puntos

```
Meta oficial lo respalda        0-3
Varios expertos coinciden       0-3
Publicación reciente            0-2
Relevante para DR               0-3
Calidad de evidencia            0-3
                        TOTAL: 14
```

```
12-14 → HIGH PRIORITY   (adoptar)
 8-11 → TEST            (experimento con control)
 5-7  → WATCH           (registrar, no actuar)
 0-4  → IGNORE
```

Todo claim guarda `published_at`, `captured_at`, `last_verified_at`. **Sin fecha, no entra.**

Toda estrategia de ecommerce se etiqueta antes de tocar DR:

```yaml
applicability_to_DR: high | medium | low
modification_required: yes | no
```

---

## 8. Actors de Apify — verificados en Store el 13 ago 2026

### Meta Ad Library

| Actor | Precio | Nota |
|---|---|---|
| `apify/facebook-ads-scraper` | $0.0058 / anuncio | **Oficial de Apify.** 31.8k usuarios, rating 4.19. Default seguro. Input: `startUrls`, `resultsLimit`, `activeStatus`, `onlyAdsNewerThan`, `isDetailsPerAd`. |
| `brilliant_gum/facebook-ads-library-scraper` | $0.015 / anuncio | Único que reporta explícitamente **días corriendo**. Más caro, pero da la señal que más importa. Input: `searchTerms`, `countries`, `adType`, `maxAds`, `startDate`. |
| `memo23/facebook-ads-library-scraper-ppe` | $0.0005 / result + $0.05 start | Schema más rico (incluye reach EU). Barato a volumen. 24 campos de input. |
| `azzouzana/meta-facebook-instagram-ads-library` | $0.0005 / result | El más barato. Demografía de audiencia. Menos usuarios (266). |

**Decisión:** arrancar con `apify/facebook-ads-scraper` (oficial, estable, mejor soportado). Si el campo de duración no viene utilizable, probar `brilliant_gum`.

**Regla de arquitectura obligatoria:** la skill nunca depende del formato exacto de un actor de terceros. Siempre hay un adapter que normaliza al schema de 6.1 antes de que nada más lo toque. Si mañana cambiamos de actor, el sistema no se rompe.

### Instagram y YouTube

`apify/instagram-scraper` para Reels (caption, autor, fecha, engagement, media). Para transcripts hablados hace falta un actor que devuelva audio/transcript — el caption solo no alcanza cuando el conocimiento está hablado. Para YouTube, un actor con subtítulos. Mismo adapter obligatorio en ambos casos.

### Costo estimado

15 competidores × 40 anuncios = 600 anuncios ≈ **$3.50 por sweep** con el actor oficial.
Sweep mensual → el free tier de Apify ($5/mes) cubre el MVP entero.

---

## 9. Lista inicial de competidores — a validar

Punto de partida propuesto. Discipline Rift es local de Orlando FL, después de la escuela, on-campus, kids 6-12, beginner-first.

**Nacionales / franquicias que compiten por el mismo presupuesto de padre:**

- Soccer Shots
- Skyhawks Sports Academy
- i9 Sports
- TGA Premier Sports
- Amazing Athletes
- Challenger Sports
- Super Soccer Stars
- KidStrong

**Locales de Orlando / Central Florida:** a levantar buscando en Ad Library por keyword + geo `US`, términos tipo `after school sports`, `youth soccer Orlando`, `kids sports program`, `after school program Orlando`.

**Adyacentes que compiten por el mismo slot horario y el mismo presupuesto:** academias de artes marciales, programas de STEM after-school, clases de danza, tutoring.

**Tarea 0 del Sprint 1:** validar esta lista contra la realidad — buscar en Ad Library por keyword + geo antes de fijar `competitors.yaml`. Marca que no corre anuncios activos no entra a la lista.

---

## 10. Orden de construcción

### Sprint 1 — Competitor sweep (el que da valor primero)

0. Validar lista de competidores en Ad Library por keyword + geo
1. Escribir `config/competitors.yaml`
2. Crear skill `ads-meta-intel-adlib`
3. Correr sweep contra 5 competidores
4. Revisar el output

**Criterio de corte:** si el sweep no cambia ninguna decisión de creative, el sistema no se construye más. Se para ahí.

### Sprint 2 — Conocimiento público

5. `config/experts.yaml` — 4-6 personas máximo
6. Crear skill `ads-meta-intel-ingest`
7. Procesar 15 fuentes: 5 Reels + 5 YouTube + 5 artículos
8. Poblar `knowledge/official-meta/` con documentación oficial de Meta:
   account simplification, ad set consolidation, learning phase, Advantage+, creative diversification, Andromeda, budget, targeting, measurement

### Sprint 3 — Playbook

9. Crear skill `ads-meta-intel-playbook`
10. Generar el primer `dr-playbook.md` y `experiments.md`
11. Correr el primer experimento en la cuenta real de DR

### Sprint 4 — Cierre del loop

12. Conectar `dr-playbook.md` como input opcional de `ads-meta-dr-phase3-campaign-rehab`
13. Registrar resultados reales de experimentos en `output/`
14. Crear tareas de ClickUp para los experimentos aprobados

### Sprint 5 — Solo si 1-4 demostraron valor

15. Discovery recurrente con `WebSearch`
16. Cadencia programada

---

## 11. Cadencia

| Ritmo | Qué |
|---|---|
| Cuando aparece algo | Alguien pega una URL en `inbox/urls.json` |
| Mensual | Competitor sweep + regenerar playbook. Se engancha al ciclo mensual que ya corre en `domains/ops/social-metrics/` |
| Trimestral | Revisar documentación oficial de Meta por cambios |

**Nada diario.** El conocimiento de plataforma no cambia todos los días; procesarlo a diario solo produce ruido y quema crédito de Apify.

---

## 12. Prueba de aceptación

15 fuentes de conocimiento + 5 competidores. Después responder:

1. ¿Los patrones de competidores sirven para decidir un creative concreto?
2. ¿Puedo rastrear cada afirmación hasta su fuente original?
3. ¿El sistema distingue opinión de experto vs. regla oficial de Meta?
4. ¿Detecta cuando un experto contradice a Meta?
5. ¿Traduce correctamente ecommerce → programa local after-school?
6. ¿Los experimentos que propone son experimentos que realmente queremos correr?

**Si 1 y 6 son "no", no se sigue construyendo.**

---

## 13. Límites éticos y de veracidad

- Solo información pública. Nada de cursos pirateados, contenido privado, paywalls, ni evasión de logins.
- Ad Library no publica gasto ni conversiones de anuncios comerciales. No se infiere ninguno de los dos.
- Longevidad de un anuncio es un **proxy**, no una métrica. Se etiqueta como proxy en todo output.
- Una estrategia de ecommerce no se copia a DR sin etiquetar `applicability_to_DR` y `modification_required`.
- No inventar claims medibles que el negocio no está trackeando.
- No guardar transcripts que nadie va a convertir en decisión.
- Si el sistema solo produce material de lectura, falló.

---

## 14. Qué se le pide exactamente a quien lea esto

Dado todo lo anterior, produce:

1. El contenido de `config/competitors.yaml` — estructura + lista validable
2. El `SKILL.md` completo de `ads-meta-intel-adlib`, siguiendo la convención descrita en 2.9 (frontmatter `name`/`description`/`disable-model-invocation: true`, "Paso 0 — Cargar contexto de dominio")
3. El `CLAUDE.md` del dominio `intelligence/` — reglas de operación
4. La secuencia exacta de llamadas al MCP de Apify para el primer sweep: qué actor, qué input JSON, qué se hace con el dataset

**No** propongas infraestructura. **No** propongas código. **No** propongas servicios nuevos. Todo el entorno ya existe y está descrito arriba.

---

## Bottom line

El plan original construye una máquina de investigación desde cero. Este entorno ya tiene la mitad: el LLM, el scraper autenticado, el contexto de marca, la data real de la cuenta, y las skills que convierten diagnóstico en SOP de implementación.

Lo que falta es la mirada hacia afuera y el archivo que responde qué hacer.

Eso son **tres skills y una carpeta**. No un repo, no un pipeline de TypeScript, no una API key nueva.
