---
brain_note_id: "dest:meetings:b56b83a925f9ca3417a8448717fc5f20"
canonical_key: "meetings/b56b83a925f9ca3417a8448717fc5f20"
brand_id: "meetings"
---
# SyncUp — 2026-09-22 — DR | Executives 🏐

## Reunión

- Fecha: 2026-09-22
- Horario: 10:31:11 AM - 11:05:26 AM -05
- Canal: DR | Executives 🏐
- Asistentes: Cristian Berrío, Luis Torres
- ClickUp: https://app.clickup.com/9017418223/v/dc/8cqnrff-24737/8cqnrff-37417
- Transcripción: [[02-Meetings/Transcripts/2026-09-22 SyncUp DR Executives (24737) - Transcript]]

**Notetaker**

_This note is shared with all participants for this meeting._
AI notetaker took notes for this meeting from **10:31:11 AM - 11:05:26 AM -05**
**Meeting Channel:** DR | Executives 🏐 ([https://app.clickup.com/9017418223/chat/r/8cqnrff-9037](https://app.clickup.com/9017418223/chat/r/8cqnrff-9037))
**Attendees:** Cristian Berrío, Luis Torres
[https://t9017418223.p.clickup-attachments.com/t9017418223/5edba656-98d6-42ba-8baa-04dfea29dabd/5edba656-98d6-42ba-8baa-04dfea29dabd.mp3](https://t9017418223.p.clickup-attachments.com/t9017418223/5edba656-98d6-42ba-8baa-04dfea29dabd/5edba656-98d6-42ba-8baa-04dfea29dabd.mp3)

**Panorama general**

Reunión de sincronización para alinear la construcción y publicación de la aplicación móvil "Doctor", aclarando arquitectura (Capacitor, APNs/FCM, SQLite) y costos de cuentas de desarrollador (Apple/Google). También se revisó el estado del OTP y branding, el consumo de tokens/créditos para pruebas/builds y tareas de documentación y comunicaciones con padres/coaches.

**Conclusiones clave**

*   Enfoque confirmado: encapsular el código existente con Capacitor para iOS/Android; no será un simple navegador embebido.
*   Notificaciones push: usar APNs para iOS y FCM (Firebase) para Android; Firebase se usará solo para notificaciones, no como base de datos.
*   Modo offline: usar SQLite para guardar cambios críticos (p. ej., check-in) y sincronizar luego.
*   Costos: Google Play Console pago único de $25; Apple Developer anual (~$129 el primer año mencionado); no se cobra por app individual sino por licencia/cuenta.
*   Cambios de OTP y branding ya implementados en un commit pero pendientes de revisión por "Codex" antes de desplegar.
*   Pruebas: se priorizó ejecutar pruebas manuales por terminal para ahorrar tokens; las pruebas en la plataforma consumen demasiado.
*   Créditos/tokens: quedan ~38 y se renuevan en 8 días; si faltan, se comprarán más para no frenar avances.
*   Feedback de usuarios: los coaches prefieren una app nativa sobre el dashboard web por conveniencia, lo que refuerzó la prioridad del release móvil.
*   Documentación: la extracción del libro de voleibol ya está en Obsidian (MDs) y se compartieron rutas; el contenido relacionado se moverá de voleibol a flag football cuando aplique.

**Próximos pasos**

- [ ] **Cristian Berrío**: Someter a revisión los cambios de OTP/branding a Codex y, tras aprobación, desplegarlos. _(Vence: 09/22)_
- [ ] **Cristian Berrío**: Explicar a Luis, por escrito, los cambios realizados en OTP/branding para mantener el contexto.
- [ ] **Cristian Berrío**: Reintentar y estabilizar las pruebas manuales por terminal, buscando workaround para la ejecución y reduciendo consumo de tokens.
- [ ] **Cristian Berrío**: Mantener apagados servicios/bases de datos no necesarios y monitorear créditos/tokens restantes; escalar a Luis si se requiere compra adicional.
- [ ] **Cristian Berrío**: Continuar configuración de notificaciones (APNs/FCM) y SQLite para modo offline en la app Doctor.
- [ ] **Cristian Berrío**: Compartir/actualizar rutas en Obsidian y realizar pull/update del repo; mover materiales pertinentes de voleibol a flag football.
- [ ] **Cristian Berrío**: Enviar correos a los dos padres indicados y notificar a Luis al completar. \*(Vence: 09/22)
- [ ] **Luis Torres**: Confirmar el costo anual de Apple para años siguientes y validar límites/licencias para múltiples apps.
- [ ] **Por asignar**: Probar en dispositivos iOS/Android que el renderizado, botones y configuraciones específicas funcionen correctamente antes del release.

**Key Topics**

*   **Optimización de prompts para reducir consumo de tokens** Idea
    *   Cristian indicó que vio un repositorio que "empaqueta" y optimiza prompts extrayendo keywords y eliminando basura para reducir consumo del modelo.
    *   Confirmó que el repositorio era famoso y con buenos likes, pero los comentarios del video no aclararon si funcionaba bien; dijo que lo probaría ahora (apenas lo estaba descargando).
    *   Luis preguntó si ya lo había probado; Cristian respondió que aún no.

*   **Agenda: evaluación de la construcción de la aplicación de Doctor** Actualización
    *   Luis afirmó que la agenda era evaluar la construcción de la aplicación de Doctor y que leyó el plan completo.
    *   Mencionó un costo anual de "ciento veintinueve, el primer año" y que no vio los años siguientes; asumió que solo se paga el de Apple.
    *   Cristian aclaró costos de tiendas: Google es un solo pago de 25; Apple es anual y no se limita a una sola aplicación.
    *   Cristian señaló que, según ChatGPT, Apple cobra por la licencia y se puede tener múltiples apps; dijo que validaría en la práctica cuando lo pruebe.
    *   Ambos acordaron que para Google sería similar en cuanto a no cobrar por aplicación individual, con el beneficio adicional de ser pago único.

*   **Arquitectura móvil: Capacitor, notificaciones push y empaquetado** Actualización
    *   Cristian explicó que no usarían una app tipo navegador sino que encapsularían el código existente con Capacitor para renderizarlo como app móvil independiente.
    *   Detalló uso de notificaciones push: en iOS via APN (application push notification) y en Android via Firebase (FCM).
    *   Aclaró que lo de Firebase visto por Luis no correspondía a base de datos sino al sistema de notificaciones para Google.
    *   Luis comentó que recordaba la cadena de funcionamiento del trigger de notificaciones en el teléfono.
    *   Cristian indicó que la complejidad estaría en asegurar que todo funcione y se renderice bien (botones, configuración distinta para iPhone).

*   **Almacenamiento offline para flight attendants con SQLite** Actualización
    *   Cristian indicó que "lo de los flight attendants" se haría con SQLite, sin costo (gratis).
    *   Explicó que permitiría guardar cambios de check in offline y luego hacer upload.
    *   Luis recalcó que guardarían cambios específicos/importantes, no todo.
    *   Cristian señaló que al ser sencillo y gratuito, mientras menos complejo, menos falla.

*   **Estado y cambios en OTP (autenticación) y branding** Problema
    *   Luis preguntó si Cristian podía tocar el OTP y mencionó que había un task sobre eso (no estaba seguro si estaba en el board de la semana).
    *   Cristian dijo que tenía un commit con cambios listos pero esperaría a que Codex los revisara antes de hacer el cambio; indicó que Codex se reiniciaba el Tuesday a las 12 Colombia.
    *   Cambios realizados por Cristian: "DLTP, el branding" y el tema de que el código OTP se copie al portapapeles ("lo que se copia en bandeja").
    *   Cristian comentó que pidió a Claude que lo probara, pero como no está en producción, aún no se ha verificado; espera la revisión de Codex para confirmar si sirve.
    *   Explicó que previamente el OTP fue inestable: "se arreglaba y se dañaba"; atribuyó dificultades a que es nativo de "loba, bol"/"low a ball" y que no es tan user friendly como Supabase para renderizar correos.
    *   Luis pidió que Cristian documentara/explicara lo hecho para mantener el contexto; Cristian creó el subtask en el momento.

*   **Estrategia de pruebas y consumo de tokens/créditos** Problema
    *   Se discutió que hacer pruebas en "lobaball" consumía demasiados tokens; Cristian migró pruebas a terminal para ahorrar, pero no se estaban ejecutando bien y buscaba un workaround.
    *   Estado de créditos: Luis indicó que se renovaban en ocho días y quedaban treinta y ocho créditos; mencionó "daily build cuatro punto siete créditos".
    *   Cristian expresó duda de que alcanzaran hasta la renovación; indicó que el mes pasado también duró y que ayer gastó "cuatro" haciendo pruebas.
    *   Luis autorizó comprar más tokens si hiciera falta (por ejemplo, pagar cinco dólares) para que Cristian pudiera trabajar tranquilo.
    *   Cristian informó que tenía apagados prácticamente todos los servicios no utilizados; dijo que lo que consumía tokens eran las bases de datos; las únicas prendidas: discipline brief, OIB, y posiblemente cheese to share.

*   **Preferencias de usuarios (coaches) por app vs dashboard** Actualización
    *   Luis comentó que todos los coaches preferían una aplicación en lugar del dashboard online por conveniencia.
    *   Se afirmó que la aplicación web actual (Azure) estaba "super nice" y era una maravilla comparada con el año pasado.

*   **Documentación y contenidos en Obsidian/Notion** Actualización
    *   Luis informó que los libros de la extracción de bodywork/"Bollywood" en MDs ya estaban en Obsidian.
    *   Cristian confirmó que la última extracción del libro de voleibol (hecha manualmente con alemán) estaba en MDs en Obsidian y compartió la ruta con Luis.
    *   Luis pidió dar update al hub de coaches de Notion dentro de Obsidian; preguntó qué usaba Cristian para extraer y actualizar Notion->Obsidian.
    *   Cristian dijo que usaba "El MCB and Ocean"; describió que en Obsidian hay carpetas "home" que rutean al resto de la información por marca (Doctor) y que el flujo ubica la información nueva de Notion en la ruta/tags correspondientes.
    *   Se acordó mover contenido etiquetado de voleibol a flag football para lo que viene.

*   **Progreso del deliverable "clic/bro" al 95% y pendientes de pruebas** Actualización
    *   Luis preguntó por "clic, con bro" y cuánto faltaba.
    *   Cristian indicó que estaban al "noventa y cinco por ciento. Casi ocho" y que lo faltante eran pruebas.
    *   Indicó que estaba intentando correr pruebas en terminal para evitar el alto consumo de tokens de lobaball, pero no se estaban ejecutando correctamente.

*   **Acciones operativas con padres y flag football** Decisión
    *   Luis indicó que enviaría un mensaje con tareas sobre un niño de flag football y pidió que Cristian ejecutara esas acciones.
    *   Cristian respondió que enviaría correos a los padres ("a los dos") y que avisaría cuando lo hiciera.
    *   Al final, Cristian dijo: "Ya, ya estoy cambiando a los padres esos y les voy a mandar el correo a los dos"; Luis pidió confirmación cuando lo hiciera.

_Sincronizado por Brain: 2026-10-21T18:21:44.516Z_
