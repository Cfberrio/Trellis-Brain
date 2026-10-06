---
brain_note_id: "dest:unknown:ab7c9848f6e01c668c02b81f3ed13e92"
canonical_key: "unknown/ab7c9848f6e01c668c02b81f3ed13e92"
brand_id: "unknown"
---
# Tarea: Extract Pico book list (PDF + MD) and finish the pending book extractions

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The task involves book extraction for 'Pico' and 'Obsidian Training', which are internal knowledge management processes. While 'Luis' is a known Trellis member, the content does not explicitly reference Cheese To Share, Discipline Rift, Orlando Event Venue, or Trellis Core specific business logic or products.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3addj2` · [Abrir en ClickUp](https://app.clickup.com/t/86e3addj2)

**Contenido original**

Objective
Review the state of the book extraction Luis sent earlier, then extract (1) the new list of books for Pico that Luis will send and (2) every book from the previous list that is still pending. Each book comes out in two formats: PDF and MD.
Context
Luis previously sent a set of books to extract; part of that batch is not finished. He is now adding a second batch for Pico. Both batches use the same extraction, and the resulting MDs feed the Obsidian Training folder (see the sibling subtask for placement).

Requested in the parent task comment thread: comment:90170253014734
To Keep in Mind
Blocked on input: the Pico book list has not been sent yet — start with the pending books from the first batch while waiting.
Audit first: list which books from the first batch are done vs. pending before extracting anything, and post that list in this task so Luis can correct it.
Formats: PDF + MD per book. Luis said "PDF y en DIS" in the comment — the audio transcript reads as "MDs", which matches the Training folder. Confirm with Luis if he meant a third format.
Naming: keep one consistent filename per book across both formats so they pair up in the folder.
Do not place files yet — placement is the separate subtask.

**Comentarios**

- **2026-09-18 · Cristian Berrío**: Ya le di upload al drive con los pdf, y adicional a eso tambien lo puse en obsidian, queda pendiente los libors de pickleball
- **2026-09-22 · Luis Torres**: Ya los libros estan en obsidian?
- **2026-09-22 · Luis Torres**: DR Curriculum Research - Flag Football.htmlpickleball-curriculum-research.html @Cristian Berrío listos para extraccion
- **2026-09-22 · Cristian Berrío**: Pico batch extracted: 27 sources in the vault, 19 of them as paired PDF + MD. What happened: the Pico list never came through, so I decided not to stay blocked and pulled the batch from the Kitchen Library research report instead. Result is 27 sources and 1.6M characters of source text. 19 have matching PDF and MD filenames so they pair up in the folder. The other 8 were web pages with no PDF, because none ever existed. 5 of the 19 had dead source domains and came back through Wayback Machine, including OPEN K-2, Pickleminton 3-5 and OPEN 6-8. Those snapshots are now the only copies left anywhere. Another 22 sources could not be pulled: dead domains, confirmed 403 blocks, password walls or paid products. Each one is logged with its verified reason and URL, nothing assumed. Two deviations I want on record. I placed the files in Obsidian Training/PICKLEBALL even though this task says placement belongs to the sibling subtask. And I have not audited the first batch yet, that one is still open. Risk: 59 MB of PDFs now sit inside the vault, and the 5 Wayback ones deserve a backup outside it before anything else touches them. Next step: Luis to confirm two things. Whether this covers what he wanted for Pico or his list is different, and whether "PDF y en DIS" meant a third format beyond PDF and MD. I pick up the first batch audit once that answer lands.
- **2026-09-23 · Luis Torres**: DR Curriculum Research - Flag Football_1.htmlflag extraction fixed @Cristian Berrío
- **2026-09-23 · Luis Torres**: usar este root 05-Operations/Training
- **2026-09-24 · Luis Torres**: image.png Hermano, no veo los nuevos libros en PDFs organizados aqui Me metí en Obsidian y conseguí PDFs dentro de Obsidian. Pensé que nada más estaba montando PDFs. Bueno, por lo menos esas grandes instrucciones. Los PDFs van dentro de Drive. @Cristian Berrío
- **2026-09-24 · Cristian Berrío**: Los habia puesto solo en obsidian
- **2026-09-24 · Cristian Berrío**: pero ya los pongo en drive
- **2026-09-24 · Cristian Berrío**: Screenshot 2026-09-24 at 9.38.04 AM.png d
- **2026-09-24 · Cristian Berrío**: done
- **2026-09-24 · Luis Torres**: También los de volley que habias sacado?
- **2026-09-24 · Cristian Berrío**: sip todos los que se hicieron

_Sincronizado por Brain: 2026-10-01T03:10:00.297Z_
