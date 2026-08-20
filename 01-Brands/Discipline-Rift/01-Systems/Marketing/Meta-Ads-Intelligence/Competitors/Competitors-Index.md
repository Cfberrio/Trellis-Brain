---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: index
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/competitors/ (6 anunciantes, 99 anuncios, barrido 2026-08-13)"
repo_path: domains/ads/meta/intelligence/competitors
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: index
tags:
  - meta-ads
  - meta-ads/competitor
  - meta-ads/index
  - discipline-rift
aliases:
  - "Competidores — índice"
  - "Meta Ad Library sweep"
  - "Competitors Index"
---

# Competidores — índice del barrido de Ad Library

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Patterns|Patrones entre anunciantes]] — la salida agregada
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Ad-Scripting-Playbook|DR Ad Scripting Playbook]]
- [[01-Brands/Discipline-Rift/02-Communication/Marketing-Language-Library|DR Marketing Language Library]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia — §10 reglas de Ad Library]]

---

> [!danger] Lo que Ad Library **no** publica, y por tanto no está en ninguna de estas notas
> Gasto, CPA, ROAS, conversiones, ingresos, rentabilidad, geografía de targeting, composición de audiencia, presupuesto, estructura de campaña, estructura de ad set.
> **A ningún anuncio se le llama ganador.** La longevidad es un proxy de "el anunciante siguió eligiendo correrlo" y de nada más.

## Snapshot del dataset (2026-08-13)

| | |
|---|---|
| Anunciantes barridos | 6 |
| Familias de marca independientes | **5** — `i9-sports`, `super-soccer-stars`, `kidstrong`, `skyhawks`, `soccer-shots` |
| Anunciantes locales (Orlando metro) | 2 — KidStrong Windermere, Soccer Shots Orlando |
| Anunciantes nacionales | 4 |
| Anuncios únicos analizados | **99** |
| Registros crudos capturados | 103 en 7 capturas (4 duplicados deduplicados por `<page_id>:<ad_id>`) |
| `sample_status` | **`unknown` para los 6** |

> [!warning] Dos límites que aplican a todo lo de abajo
> **1. La completitud no está establecida para ningún anunciante.** El Actor no emite señal de completitud en modo extracción completa. Ningún anunciante llegó a su tope configurado, pero recuperar menos que el tope no prueba haberlos recuperado todos. Lee cada conteo como **"al menos esta cantidad"** y cada "el único anuncio que…" como "el único anuncio de lo que se recuperó".
> Esto **no** debilita los patrones observados —un anuncio no recuperado solo puede añadir mensajes, no quitar los que se vieron— pero **sí** debilita cualquier afirmación de ausencia ("Skyhawks no corre incentivos").
>
> **2. La muestra está sesgada a nacional.** 79 de 99 anuncios son nacionales. La evidencia local de Orlando son 16 anuncios de 2 familias, y 11 de esos 16 son el lanzamiento de un programa de bebés fuera de la banda de edad de DR. **La lectura local es delgada por construcción.**

## Los 6 anunciantes

| Anunciante | Alcance | Familia | Anuncios | Nota |
|---|---|---|---|---|
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-i9-Sports-National\|i9 Sports]] | nacional | `i9-sports` | 39 | Aporta 39 de 99 anuncios y pesa exactamente **una** familia |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Super-Soccer-Stars-National\|Super Soccer Stars]] | nacional | `super-soccer-stars` | 24 | El más agresivo en incentivo explícito (código de $45, clase de prueba gratis) |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-KidStrong-Windermere\|KidStrong Windermere]] | **local Orlando** | `kidstrong` | 12 | Misma familia que HQ — **no es una segunda voz** |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-KidStrong-HQ\|KidStrong HQ]] | nacional | `kidstrong` | 11 | Encuadra como "programa de entrenamiento basado en ciencia", no como deporte |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Skyhawks-National\|Skyhawks Sports Academy]] | nacional | `skyhawks` | 9 | El único sin incentivo observable en la muestra |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Soccer-Shots-Orlando\|Soccer Shots Orlando]] | **local Orlando** | `soccer-shots` | 4 | El competidor más cercano al mercado real de DR, y solo 4 anuncios capturados |

## Los patrones que se repiten entre familias independientes

Dos anuncios con la misma frase dentro de un anunciante es **repetición**. Dos familias independientes haciendo lo mismo es lo único que aquí se llama **patrón**.

| Patrón | Familias | Confianza |
|---|---|---|
| **Confianza / crecimiento de carácter** como el resultado titular para el niño | **5 de 5** | alta |
| **Aceptación explícita de principiantes** ("no experience needed") | 4 de 5 | alta |
| **Credencial del coach** como elemento de prueba | 4 de 5 | alta |
| **Un incentivo explícito** corriendo como su propia línea creativa | 4 de 5 | alta para la presencia — **nada observable sobre si funcionó** |
| **La banda de edad escrita en el copy** | 3 de 5 | media |
| **Disparador de calendario** (temporada / vuelta al cole) | 3 de 5 | media-alta |

Detalle completo con los IDs de anuncio y las citas literales: [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Patterns|Patrones entre anunciantes]].

## Qué hacer con esto en DR

Esto es **COMPETITOR OBSERVATION**: dice qué mensajes están en el mercado, no qué convierte. Sirve para tres cosas concretas:

1. **Detectar lo que es tabla de apuesta.** Confianza/carácter aparece en las 5 familias — decirlo no diferencia a DR, callarlo probablemente sí resta.
2. **Detectar el hueco.** Lo que ninguna familia dice bien es donde DR puede diferenciarse — pasa por [[01-Brands/Discipline-Rift/00-Brand-Core/Positioning|Positioning]] y [[01-Brands/Discipline-Rift/06-DNA/Message|Message DNA]] antes de convertirse en guion.
3. **Alimentar ángulos de prueba**, no copiarlos. La transferibilidad a DR se evalúa igual que con cualquier otra fuente externa.

> [!info] Cuándo volver a barrer
> Cadencia prevista: mensual, no diario. Los conteos de arriba son **puntuales de 2026-08-13** y no deben presentarse después como valores vivos. Antes de cualquier barrido nuevo hay que revalidar la actividad de cada anunciante.
