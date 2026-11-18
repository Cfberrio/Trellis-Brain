---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3uf6kw"
owner: Cristian
last_updated: 2026-11-17
sensitivity: internal
related_systems:
  - clickup
  - st-joseph-connect
related_notes:
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home]]"
hub_role: leaf
tags:
  - st-joseph
  - clickup-task
  - week-oct-19
---

# Agregar subgrupos de matrimonio al Excel de Sacramentos

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 19 🪪

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3uf6kw](https://app.clickup.com/t/86e3uf6kw) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | — |
| Creada | 2026-10-21 13:04 |
| Actualizada | 2026-10-26 09:54 |
| Cerrada | 2026-10-26 09:54 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis pidió agregar al Excel exportado de Sacramentos (adults-receiving-sacraments) los subgrupos de estatus de matrimonio que ya muestra el dashboard: una tabla "People by marriage case" con leyenda en Summary y una columna "Marriage case" con badges de color junto al nombre en cada tab. Cristian lo entregó el 21/10 (commit edff10b en main), con conteos verificados contra la base de datos para los 150 activos: 22 / 5 / 0 / 6, iguales al dashboard. Al momento del comentario quedaba pendiente publicar en Lovable para que el botón de descarga usara esta versión. Luis respondió "fire" y la tarea se cerró como aprobada el 26/10.

## Descripción
## Objective
Agregar al export de Excel (`adults-receiving-sacraments`) la visualización de los **subgrupos de estatus de matrimonio**, igual que ya se ve en el dashboard, y mostrar ese estatus por persona en la columna de la izquierda junto a su nombre, con el mismo estilo de badge que "Registered & attending".
## Context
El Excel ya funciona y el layout/user-friendliness está muchísimo mejor (feedback de Luis en [la tarea padre OCT 19](https://t9017418223.p.clickup-attachments.com/t9017418223/c87954dc-4cc1-4df9-b4a3-679d29de6032/Screenshot%202026-10-21%20at%2012.57.36%E2%80%AFPM.png)). Lo único que falta son los subgrupos de matrimonio.

En el dashboard (Sacraments, St. Joseph Formation) ya existen estos subgrupos:
*   **Married outside the Catholic Church** (22): siguen juntos, no se necesitan documentos
*   **Divorced** (5): casados antes, requiere annulment decree
*   **Cohabiting** (0): viven juntos sin casarse, conversación pastoral
*   **Engaged** (6): planean casarse

![](https://t9017418223.p.clickup-attachments.com/t9017418223/c87954dc-4cc1-4df9-b4a3-679d29de6032/Screenshot%202026-10-21%20at%2012.57.36%E2%80%AFPM.png)

Hoja Summary actual del Excel: tiene "People by tab" con participation status, pero no hay nada de matrimonio:

![](https://t9017418223.p.clickup-attachments.com/t9017418223/0ff18efd-01e6-4e7e-91ac-56f5f01dce58/image.png)

Tab por grupo (ej. Adult Sacraments - Catholic): la columna A muestra "Participation status" con color. Aquí es donde también debe verse el estatus de matrimonio:

![](https://t9017418223.p.clickup-attachments.com/t9017418223/2c2cfe3a-4ab5-415b-b3ba-8deba9cbf34f/Screenshot%202026-10-21%20at%201.00.26%E2%80%AFPM.png)
## To Keep in Mind
*   **Opción preferida:** arreglar este mismo Excel en lugar de crear otro archivo, a menos que no quepa limpio.
*   **Summary:** agregar una tabla "People by marriage case" (subgrupo × tab, con totales) y una leyenda de qué significa cada subgrupo, igual que la de Participation status.
*   **Tabs por grupo:** agregar columna "Marriage case" a la izquierda, al lado del nombre, con badges de color (mismo estilo visual que Registered & attending). Personas sin caso de matrimonio: mostrar "—".
*   Los conteos deben cuadrar con el dashboard (22 / 5 / 0 / 6) para los 150 activos.
*   Mantener filtros en los headers y que también funcione en "All details".
*   No romper el layout actual que ya está aprobado.

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| Screenshot 2026-10-21 at 1.00.26 PM.png | png | 2026-10-21 13:04 | — |
| Screenshot 2026-10-21 at 12.57.36 PM.png | png | 2026-10-21 13:04 | — |
| image.png | png | 2026-10-21 13:04 | — |

## Comentarios
### 2026-10-21 13:42 · Luis Torres
@Cristian Berrío hermano ataca esto bro

### 2026-10-21 13:42 · Cristian Berrío
Listo. El código ya está en main (commit edff10b, pusheado). Falta publicar en Lovable para que el botón de descarga use esta versión.

Tabs por grupo, Special cases y All details
Nueva columna Marriage case justo después del nombre, con badge de color: Married outside the Catholic Church (azul), Divorced (rosado), Cohabiting (violeta), Engaged (verde agua). Sin caso: "—" en gris.
Usa exactamente la misma regla que las tarjetas "Subgroups · by marriage" del dashboard.
Tiene flecha de filtro en el header, como las demás columnas.
El caso detallado del formulario (ej. "Annulment in process", "Marriage to review") sigue en Special cases y All details, ahora con el nombre Marriage case detail.

Summary
Tabla nueva People by marriage case (tab × subgrupo + "No marriage case" + Total), debajo de la de Participation status.
Leyenda "What 'Marriage case' means" con el mismo estilo de la de Participation status.

Conteos verificados contra la base de datos (150 activos): Married outside 22 · Divorced 5 · Cohabiting 0 · Engaged 6. Igual que el dashboard.

Lo que ya estaba aprobado no cambia: columnas fijas (status + nombre), orden por bloques, colores y filtros.

### 2026-10-21 13:47 · Luis Torres
fire

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-15-86e3r1g9k-fix-sacraments-excel-export|Fix Sacraments Excel export]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-15-86e3r2c1h-sacramental-challenges-leaders-guide|Sacramental challenges leaders' guide]]
