---
brain_note_id: "dest:unknown:1df5b5811b5d48082cfbfbc804a018a5"
canonical_key: "unknown/1df5b5811b5d48082cfbfbc804a018a5"
brand_id: "unknown"
---
# Tarea: OTP BRANDING + AUTOCOPY IN MOBILE

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The title refers to 'OTP BRANDING' and 'AUTOCOPY IN MOBILE', which are generic technical features related to authentication and mobile UI. There is no specific mention of cheese, fitness/discipline, event venues, or Trellis internal core systems to distinguish between the brands.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3cp4bd` · [Abrir en ClickUp](https://app.clickup.com/t/86e3cp4bd)

**Contenido original**

_Sin texto en el mensaje principal._

**Comentarios**

- **2026-09-23 · Cristian Berrío**: Corrección al comentario anterior: el código YA NO va en el asunto. Va en la vista previa de la notificación. Todo lo demás sigue en producción y verificado. Qué cambió desde el comentario de arriba: ese comentario quedó viejo el mismo día. Decía que el código iba en el asunto; se sacó de ahí a propósito unas horas después. Por qué: el asunto viaja más lejos que la notificación — queda en los metadatos del correo, en el historial de notificaciones, en las reglas de reenvío, y en superficies que muestran el asunto pero nunca la vista previa (un reloj, la pantalla del carro, un teléfono con las vistas previas apagadas). DR es passwordless: el código es la credencial completa, no un segundo factor, y detrás está el horario y la ubicación del niño. El preheader lo muestra en la notificación igual, sin dejarlo en todos esos otros lados. Cómo se ve hoy en el celular: Discipline Rift Your Discipline Rift login code 482913 is your Discipline Rift login code. Commits en main, todos publicados: f027d9f (rebranding de los 2 correos OTP) · 3c85c9c (cuerpo en el formato que reconocen los detectores de iOS/Gmail + botón "Paste code" en coach, parent y register) · 4210d37 (el botón se retira solo donde el navegador deniega el portapapeles — in-app de Instagram/Facebook) · b7a6274 (código al asunto) · eb992f5 (revertido: código al preheader, fuera del asunto). Evidencia: 1129 tests en verde, tsc limpio. Tras publicar: sitio 200, rutas del pipeline OTP en 401 (sanas). OTP reales a grouptrellis@gmail.com con los dos templates, pending→sent en 2-3 s sin errores. Lo que NO está verificado, y hay que decirlo: el autocopiado de Gmail se probó en celular con el código en el asunto. Al moverlo al preheader no se ha vuelto a probar. Los detectores de Apple y Google leen el cuerpo, así que en principio sigue funcionando, pero son heurísticas privadas y sin documentar — nadie lo puede garantizar sin probarlo en un teléfono real. Riesgo: usar "Customize auth emails → Re-scaffold" en Lovable borra este branding. Único camino conocido que lo revierte.

_Sincronizado por Brain: 2026-10-01T03:16:38.069Z_
