---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3qxu4z"
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

# CLICKUP OUTREACH FEATURE IN STJOSEPH

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 19 🪪

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3qxu4z](https://app.clickup.com/t/86e3qxu4z) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Cristian Berrío |
| Asignados | — |
| Creada | 2026-10-15 10:00 |
| Actualizada | 2026-10-16 12:37 |
| Cerrada | 2026-10-16 12:37 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
La tarea no tiene descripción; el trabajo se documenta en los comentarios. Cristian construyó en el sistema de St. Joseph un tablero Outreach estilo ClickUp (/admin/outreach) para dar seguimiento a quienes escriben o llaman a la parroquia, con columnas arrastrables, fechas de seguimiento, botón Place, formulario público /contact y las 22 personas de la carpeta FOLLOW UP del correo de Luis cargadas en "Replied". Luis aprobó y pidió poder mover a una persona de Sacraments a otro grupo (ejemplo Richelle); Cristian publicó el botón Move ese mismo día. Pendientes al 15 de octubre: publicar en Lovable, enlazar cuentas de staff con su persona, asignar responsable por tema, revisar y enviar los 22 borradores en el Outlook de Luis y poner el link /contact en la web; los avisos por correo quedan en el Outbox sin envío automático.

## Descripción
_Sin descripción en ClickUp._

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| image.png | png | 2026-10-15 12:31 | Luis Torres |

## Comentarios
### 2026-10-15 10:06 · Cristian Berrío
Tablero "Outreach" en St. Joseph: qué es, qué se hizo y qué falta

En corto: el sistema de St. Joseph ya tiene un tablero estilo ClickUp para dar seguimiento a la gente que escribe o llama a la parroquia. Cada persona es una tarjeta, y el staff la mueve por columnas hasta que queda ubicada en un grupo (por ejemplo, OCIA).

El problema que resuelve
Hoy, cuando alguien escribe a la parroquia ("quiero bautizar a mi hijo", "quiero ser católico"), la única forma de seguirle la pista es contestar el correo y acordarse. La gente se pierde. Con el tablero, nadie se queda sin respuesta y se ve en qué paso va cada persona.

Cómo funciona
Dónde está: en el sistema, menú Outreach (/admin/outreach). Lo ven los administradores y el staff de oficina. Catequistas y líderes no lo ven.
Columnas: Pending → Replied → Follow-up → Pending reply follow-up → Placed. Las tarjetas se arrastran de una columna a otra, como en ClickUp. Los administradores pueden renombrar, cambiar el color, reordenar, agregar o borrar columnas.
Cada tarjeta tiene: datos de contacto, el mensaje original, un responsable, notas internas, historial de movimientos, fecha de seguimiento y tema (Baptism, OCIA, Marriage, Adult formation, Youth, Other).
Fechas de seguimiento: si se pasa la fecha, la tarjeta se pone roja y aparece en el filtro "Overdue".
Cuando la persona ya tiene grupo: se usa el botón "Place". La persona queda inscrita en el grupo y su tarjeta pasa sola a "Placed". Después se archiva a mano, y se puede buscar y restaurar.

Cuatro formas de meter a alguien al tablero
Botón "Add to Outreach" en el perfil de cualquier persona.
"Add people" dentro del tablero: buscar y seleccionar varias personas, o crear una persona nueva.
Un formulario público de contacto (formation-foundations.lovable.app/contact), en inglés y español, para poner en la web de la parroquia.
Un interruptor "Send to Outreach" en los formularios de inscripción que ya existen.

Lo que ya está hecho
El tablero está construido, revisado, subido a GitHub y con la base de datos lista en producción.
Se probó completo con la cuenta demo (personas inventadas).
Ya tiene gente: las 22 personas de la carpeta FOLLOW UP del correo de Luis están en la columna "Replied", 8 de ellas creadas nuevas en el sistema. En cada tarjeta hay una nota que dice que la respuesta quedó como borrador en Outlook, no enviada.

Lo que falta para usarlo al 100%
Publicar en Lovable, para que el tablero aparezca en el sitio publicado.
Enlazar las cuentas del staff con su persona, en Settings → Team. Hoy no hay ninguna enlazada, así que no se puede asignar responsable a ninguna tarjeta.
Elegir un responsable por tema, en Settings → Outreach. Por ejemplo, OCIA → quien lleva OCIA. Hoy ningún tema tiene responsable.
Revisar y enviar los 22 borradores en el Outlook de Luis. Siguen sin enviarse.
Poner el link /contact en la web de la parroquia, si se quiere usar el formulario público.

Importante: los correos de aviso al responsable (cuando le llega o le pasan una tarjeta) no se envían solos todavía. Quedan en Communications → Outbox y alguien tiene que mandarlos desde ahí.

Siguientes proyectos (no incluidos aquí)
Área de equipo y roles (líderes, staff, catequistas, voluntarios).
Tableros iguales para sacramentos y candidatos de OCIA, usando el mismo sistema.
Recordatorio diario por correo de tarjetas vencidas.

### 2026-10-15 12:31 · Luis Torres
bien hecho. algunos detalles, revisa las notas, hermano. Necesito que estés pendiente del hecho de que tenemos que mover a esa persona a algún otro lugar. Actualmente, por ejemplo, Richelle está en Adult Sacraments y, si la queremos mover a otro grupo o asignar a otro grupo, deberíamos poderlo hacer.
image.png

(Adjunto en el comentario: image.png)

### 2026-10-15 15:22 · Cristian Berrío
Nuevo en Sacraments: mover a una persona a otro grupo (ya está publicado)

, en corto: además de Archive, ahora cada persona de Sacraments tiene un botón Move para pasarla a otro grupo de la parroquia. Ya está en la página.

¿Dónde está?
En la lista de Sacraments, debajo del nombre de cada persona, hay dos botones pequeños: Move y Archive. Los mismos botones están arriba en el perfil de la persona. No hace falta abrir el perfil.

¿Cuándo usar cada uno?
Move: la persona sigue con nosotros, pero en otro grupo. Ejemplo: Richelle está en Adult Sacraments y la queremos pasar a Adult Faith Formation, a Marriage o a otro grupo.
Archive: la persona confirmó que ya no viene. Faltar a clase o no contestar no cuenta.

Cómo mover a alguien (ejemplo con Richelle)
En Sacraments, busca a Richelle y dale Move.
En "Move to" eliges el grupo: Adult Faith Formation, Estudio Bíblico, Formación de Fe, Marriage, Baptism Preparation, Young Adults, Youth, ministerios o coros.
En "Why" escribes el motivo (es obligatorio) y confirmas.

Qué pasa después:
Sale de la lista de Sacraments y de sus conteos.
Queda inscrita en el grupo nuevo y aparece en esa lista.
En su perfil queda una nota de staff: "Moved from Adult Sacraments to …: motivo", con quién lo hizo y cuándo.
No se borra nada: perfil, notas y asistencia se quedan.

¿Me equivoqué? Botón Restore
Activa el interruptor "Archived or moved" en la lista. Ahí ves a todos los que salieron, con la etiqueta "Moved to X" o "Archived". El botón Restore la devuelve a Sacraments, la saca del grupo nuevo y deja una nota. Vuelve con el mismo estado que tenía: si estaba "por entrevistar", sigue así.

Lo único que no hace Move
Pasar entre OCIA y Adult Sacraments no se hace con Move. Eso depende del bautismo, como acordamos el 8 de octubre: católico bautizado = Adult Sacraments. Si un bautismo estaba mal anotado, se corrige el estado de bautismo en el perfil y la persona cambia de grupo sola.

Quién puede usarlo
Un administrador puede mover a cualquier grupo.
El staff que solo maneja Sacraments ve Archive pero no Move, porque no tiene acceso a los otros grupos. Si hace falta mover a alguien, que se lo pida a un administrador.

Otros arreglos de hoy
El dashboard principal y la página de Documents ya no cuentan a quienes se archivaron o se movieron.
Archive y Move guardan el cambio y la nota juntos, así nunca queda uno sin el otro.
La descarga de Excel también separa a los que se movieron.

Todo se probó antes de publicar con usuarios de prueba del demo, sin tocar gente real.
@Luis Torres

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-13-86e3pxguj-reconcile-ocia-attendance-registrations-withdrawals|Reconcile OCIA attendance, registrations, withdrawals (mismo comentario del botón Move)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-13-86e40ve5a-draft-ocia-follow-up-emails-in-outlook|Draft OCIA follow-up emails in Outlook]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-15-86e3r2c1h-sacramental-challenges-leaders-guide|Sacramental challenges leaders' guide (mismas 22 personas de FOLLOW UP)]]
