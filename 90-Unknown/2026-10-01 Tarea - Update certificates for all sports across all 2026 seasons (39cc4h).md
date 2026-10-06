---
brain_note_id: "dest:unknown:53b5830e84ff58f149e376401dc015b0"
canonical_key: "unknown/53b5830e84ff58f149e376401dc015b0"
brand_id: "unknown"
---
# Tarea: Update certificates for all sports across all 2026 seasons

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The task describes operational updates for sports certificates across various seasons (Winter, Spring, Summer, Fall) for the year 2026. While it mentions sports like volleyball, there is no specific mention of Trellis Core, Cheese To Share, Discipline Rift, or Orlando Event Venue. The content appears to be related to a sports league management system which does not clearly map to the provided brand IDs.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e39cc4h` · [Abrir en ClickUp](https://app.clickup.com/t/86e39cc4h)

**Contenido original**

Objective
Update the certificates for all sports across every season in 2026 (Winter, Spring, Summer, Fall). The updated certificate files are ready in Google Drive.
Context
All certificates for the year are ready and need to be updated in the system. Use this Google Drive folder as the source:

Related existing subtask for Fall 2026 specifically:
To Keep in Mind
Cover all sports, not just volleyball
Cover all 2026 seasons: Winter, Spring, Summer, and Fall
Pull the correct certificate files from the Drive folder linked above
Make sure each sport/season combination gets the right certificate applied

**Comentarios**

- **2026-09-16 · Cristian Berrío**: Hecho: certificados 2026 Fall + Winter en producción (4 deportes, 6 tiers, front+back). Qué pasa: los assets ahora viven por season (fall-2026, winter-2026) y el admin elige Season → Sport → Team; el arte cambia con la season. Flag football entra por primera vez. 96 PNG cortados de los masters del Drive y verificados uno a uno. Decidí estructura por season (no reemplazo in-place) porque el arte lleva la season horneada y con un solo set los teams de Fall habrían salido "Winter". Riesgo: soccer sin arte en Drive → 2 teams Fall 2026 no pueden recibir certificado. Falta prueba de descarga real en prod (1 click). Siguiente paso: Luis · subir arte de soccer si aplica; Cristian · probar un ZIP en prod hoy. Spring/Late Spring 2027 se cargan cuando abran (30 min). Commit 64a36a3 · pre-deploy PASS · Codex 1 hallazgo arreglado · 1012 tests.
- **2026-09-16 · Luis Torres**: Procede con los certificados de Q3 y Q4
- **2026-09-18 · Cristian Berrío**: Q3 y Q4 ya estan. Fall 2026 y Winter 2026 quedaron en produccion desde el commit 64a36a3 del 15 sep, asi que no hay nada mas que hacer hasta que abra Spring 2027. Son 4 deportes por 6 tiers, front y back por season, 96 PNG revisados uno por uno. Flag football entro tambien. Me falta probar la descarga real de un ZIP en produccion, es un click. Lo hago hoy 18 y confirmo aqui. De tu lado sigue faltando el arte de soccer en el Drive. Mientras no exista, 2 teams de Fall 2026 se quedan sin certificado. Tiempo: 1h53 segun git (15 sep, 14:20 a 16:13). Paso el task a realizado.
- **2026-09-18 · Luis Torres**: Hoy monto los certificados de soccer @Cristian Berrío

_Sincronizado por Brain: 2026-10-01T03:11:58.469Z_
