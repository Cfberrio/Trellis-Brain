---
brain_note_id: "dest:meetings:10c6eed4987c576685f9b38a55b95cf0"
canonical_key: "meetings/10c6eed4987c576685f9b38a55b95cf0"
brand_id: "meetings"
---
# Transcript — 2026-06-05 SyncUp Dev (19837)

## Transcript

- Reunión: [[02-Meetings/2026-06-05 SyncUp Dev (19837)]]

**Luis Torres**: Bueno, querido, ¿cómo es todo? ¿Fantas activo o qué?
**Cristian Berrío**: Sí, andó ando modo modo renewable, que es renewable. Sí, la veneza, lo del real estate.
**Luis Torres**: Renewal.
**Cristian Berrío**: Es que me me me me confundí con Reliable Venice y con con el otro.
**Luis Torres**: Ajá, tiene sentido. ¿Que está haciendo el renewal?
**Cristian Berrío**: O sea, le estoy pasando los transcripts que hablamos ayer, estoy diseñando un plan para hacer, por lo menos, lo de los o sea, para
**Luis Torres**: Mapa de usuario.
**Cristian Berrío**: ¿Ah?
**Luis Torres**: Mapa de usuarios.
**Cristian Berrío**: Sí, o sea, y lo de los master policies que estábamos hablando ayer. O sea, quiero ajustar todo eso, ahorita mismo no estaba nada de eso,
**Luis Torres**: Antes de de llevar algo a la lógica, tenemos que creo que tenemos que mapear. Antes de crear lo de que tenemos que hacer mapa con con usuarios y una estructura de usuario y y accesos. Usuario y accesos y propiedades y propiedades que se conectan con esos usuarios.
**Cristian Berrío**: No, sí, claro, pero, o sea, lo que estoy haciendo es o sea, no estoy implementando sino que estoy diciendo como como quien te dice crear una arquitectura.
**Luis Torres**: Yeah.
**Cristian Berrío**: Estoy poniendo como que las bases para cuando ya tengamos qué es lo que se va hacer exactamente, pues ya ejecutar.
**Luis Torres**: Yeah.
**Cristian Berrío**: Estoy es abriendo paso nada más.
**Luis Torres**: Hi, Reg. This is Louis speaking. How can I help you? Hi, Louis. This is Ashley. Sorry to bother you. You're good. I just wanna I just wanted double check with you. When when is the access key when it be sent? Let me check. It should have been sent today, but let me just check what has been sent. That's the Okay. Here you go. Return to create and bump. To Perfect. Okay. Okay. D and D enabled by customer for SMS. So you activated a do not contact via text message on May twenty first. So it looks like we cannot contact you We we I will send you the message with information. That you need manually, but our system is not sending you the automated ones because you activated an automated you basically just activated the automated ones. So I'm gonna just do it manually. Right now. Yeah. It's okay. I think, you know, we get a lot of a lot of messages and emails from people. And our system, if you activate, like, DMD or, like, the do not like, unsubscribe thing from somewhere, We don't want to bother people, so we just, like, basically stop bothering you. Like, for forever. So I'll send you I'll send you a message that I I'm just copying and pasting from another customer. Just follow the same instructions. Only difference is gonna be that your access code will be different than the your reservation number will be different than theirs. So don't don't treat that as, like, biblical, if that makes sense. So I have to ask Lee's three two one. Then I have a three two okay. There's a phone number. Cool. So I'll just contact you on this one since this is just phone number. Cool. Alright. That is from another again, that's for another customer. You can see that's not even your name. But, you know, same you will follow the same instructions as them. Gotcha. So Michael, in there, in your reservation card, and then you'll see the code. No. You can do that you can do it anytime. My pleasure. You take care, Ashley. Take care. Bye. Hermano,
**Cristian Berrío**: Aquí estoy.
**Luis Torres**: Señor, paciencia. Ok, tenemos, ¿qué qué es lo que pasa con la cadena de de...? No entiendo a absolutamente qué está pasando con la cadena de mensajería de de OIB.
**Cristian Berrío**: O sea, que no
**Luis Torres**: Se supone que nosotros arreglamos esto con la mesaría nueva, pero no se está reflejando, ¿cierto?
**Cristian Berrío**: Mira, es como si tú entras al es como si tú hace un mes que hicimos que el calendario de tours y el calendario de de el calendario de bookings y el calendario de tours, modificamos y lo pusimos en uno solo. Porque antes estaba separado, pero tú me dijiste que lo querías poner en uno solo para chequear la availability y todo eso. ¿Verdad?
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Entonces, digamos que tú hiciste el booking cuando pasó eso. Tú ya entraste a una cadena de automatización, que se envía siete días antes de de de de que empiece el tour, y, pues, un día antes de que empiece el tour, unas horas antes, no me acuerdo cómo es la cadena. ¿Qué es lo que pasa? Digamos que tú pusiste hace un mes, que el cuatro de junio vas a tener tu booking. ¿Verdad? Entonces, ¿qué es lo que pasa? Como estamos manejando, los tours y los bookings en un mismo calendario, el sistema no no detectaba qué es un booking, qué es un tour. Él simplemente detectaba es un appointment. Que es algo que estaba en el calendario, se restringía en el calendario. ¿Verdad? Entonces, él, como no puede hacer esa distinción, lógicamente, como tú agendaste el booking para, digamos, mañana o pasado mañana, y lo hiciste en el momento en el que nosotros hicimos ese cambio de poner los dos calendarios juntos, en uno solo, pues, lógicamente, tú entraste en la que era automatización. Él toma ese booking que tú hiciste, no como un tour, o sea, no no toma, perdón, él toma esa reserva que no como un booking, sino como un tour también. Lo toma como si fueran los dos una misma cosa. ¿Sí me entiendes?
**Luis Torres**: Mhmm.
**Cristian Berrío**: Y eso es lo que pasa con Megan. Megan hizo una reserva, digamos, en el trayecto en el que hicimos todo eso,
**Luis Torres**: Hizo ambos, ella hizo una reserva y un tour. ¿Tuviste eso?
**Cristian Berrío**: Yo solo vi que hizo una reserva. No sé si no sé si ha alcanzado a hacer un tup. Pero yo vi que eso fue una reserva. Porque
**Luis Torres**: No sé por qué no me cargan la conversación
**Cristian Berrío**: porque yo estaba chequeando ahorita, cuando tú me dijiste eso, y actualmente yo ya lo dividí otra vez, o sea, lo volví a poner como lo teníamos antes, inicialmente.
**Luis Torres**: ¿No lo teníamos así antes? ¿Ya no lo habíamos puesto así?
**Cristian Berrío**: Inicialmente, recuerda que teníamos dos calendarios, uno para tours, uno para bookings. Hablamos tú y yo, lo pusimos
**Luis Torres**: Juntos.
**Cristian Berrío**: un solo calendario para bookings y tours, y otra vez dijimos, está pasando el tema de la comunicación, que a la gente que hace bookings
**Luis Torres**: ¿Y la devolviste cuándo? ¿Cuándo contestiste esa cuándo la devolviste?
**Cristian Berrío**: se fue hace como dos semanas,
**Luis Torres**: Ok.
**Cristian Berrío**: más o menos, O sea, fue hace rato,
**Luis Torres**: Mhmm.
**Cristian Berrío**: Por eso, cuando tú me dijiste eso, yo me yo pensé, y dije como que será que no lo hice, será que lo hice malo, será que no se actualizó el cambio, porque no no sé qué está pasando, pero tiene sentido que a Megan le haya llegado porque Megan creo que es este viernes, si no estoy mal,
**Luis Torres**: Mhmm.
**Cristian Berrío**: o mañana. No sé. Ah, bueno, hoy es viernes. Ajá, exacto. Creo que el... Ajá, el booking de allá es ahorita, entonces. Tiene sentido que ella haya entrado en ese flujo porque esa esa esa reserva la hizo hace ratico. Y, probablemente, la hizo cuando estaba el cambio de los dos bookings
**Luis Torres**: ¿Qué pasa si un cliente bookea un tour y un booking en el mismo cliente?
**Cristian Berrío**: O sea, ya no entraré en la misma automatización. O sea, sería es que, como te digo, como son dos calendarios distintos, o sea, son dos automatizaciones o dos dos mundos completamente distintos, entonces entra en el tour, en lo las automatizaciones de tours, de reminders y de follow ups, y entra a nuestras automatizaciones nuestras. No sé si me hago entender. O sea, las de que si los treinta días, que si el remaining balance... ¿Sí me entiendes? Porque es que estas automatizaciones de mensajes de tours lo hacen directamente, o sea, los triggers son el calendario, O sea, eso no es un flujo, como como yo hago así, con nodos, es como trabajamos lo de los reminders de de los treinta días, que esos son flujos complejos, no. O sea, lo que nosotros mandamos en tours son automatizaciones que no dependen de nosotros. O sea, yo solo, literalmente, pongo el correo y digo que se envíe treinta días antes. O que se envíe siete días antes, una hora antes. Así es como funciona, la mensajería de los tours. No es una no es un flujo complejo de automatizaciones. ¿Sí me entiendes?
**Luis Torres**: Mhmm.
**Cristian Berrío**: Entonces, para asegurarme de que los tours y los bookings, o sea, no se mezcle la comunicación, si una persona hace un booking, no le debería llevar, obviamente, de tour, porque él no agendó nada de tours, Lo que hice fue, por eso, restaurarlo, a que cada uno es un ambiente totalmente separado. Un calendario para tours, un calendario para bookings, los dos no se cruzan en ninguna manera. Los dos trabajan de manera independiente.
**Luis Torres**: ¿Y si ustedes y si funcionan los mensajes y todo?
**Cristian Berrío**: Sí. O sea, en tour, siguen enviando. O si yo, si tú haces un ¿tuve que un tour? Pues te llega toda la mensajería de siete días antes, hey, recuerda que viene tu tour, un día antes, llega tu tour. Después, creo que habíamos puesto treinta minutos, una hora después, no me acuerdo, un día después. Lo del follow up
**Luis Torres**: ¿Dónde tenemos esas automatizaciones aquí adentro? Go ahead, Debo.
**Cristian Berrío**: Te metes a calendario.
**Luis Torres**: Es en calendario, se se me ha olvidado. Sí, ya me acuerdo.
**Cristian Berrío**: En calendario, calendar settings, De baja a baja. Eso.
**Luis Torres**: Porque tenemos dos.
**Cristian Berrío**: Editar.
**Luis Torres**: Porque tenemos dos tours.
**Cristian Berrío**: No, es el mismo. O sea, el de abajo es de es el el de, si dice tour, en minúscula, es el de bookings. Como no lo habíamos cambiado, no la vuelto a cambiar el nombre. Pero ya le vuelvo a cambiar el nombre. Abajo. Advanced settings. Notification and policies. Ajá, la Lupita. El lápiz, perdón. Y ahí verás lo que se envía. El el lápiz. En, o sea, si haces, si abres contact, ahí te sale el correo. Y en SMS, lo mismo. En cambio, nombre enseguida, al de tours. Y ponle booklets. Dale en save changes, listo. Y ya, los dos se tratan como calendarios independientes. Y lo que pude hacer, como que no te enredes, es que si ellos si ellos adjuntan un tour les va a salir en el calendario de de Google, de el que tienes tú de OIB, donde sale todo. Ahí, pues ya lo
**Luis Torres**: El calendario de sí, eso eso es de salida. No.
**Cristian Berrío**: Exacto. Entonces, lo
**Luis Torres**: Lo que en el que el número ya no sale.
**Cristian Berrío**: ¿Cómo?
**Luis Torres**: Turistas salían en calendario ya no salen.
**Cristian Berrío**: No, sí, sí sale, siguen saliendo.
**Luis Torres**: ¿Y las automations del booking dónde están?
**Cristian Berrío**: Bookings. Eso pues. Esos son lo lo, pues, automations, o sea, sabes los flujos de, o go back, dale a go back, O sea, el calendario el calendario de bookings, de OEB bookings, no es para más nada, enviar las reservas que ellos hagan para que se reflejen en el en el calendario de Google. O sea, realmente las automatizaciones de ahí, de mensajería, nosotros no usamos eso. Nosotros lo tenemos es dale go back, O sea, todas las automatizaciones que tenemos de node, en automation. Ajá.
**Luis Torres**: Está en está en automation, sí. En estatus, ¿no?, algo así.
**Cristian Berrío**: Exacto, o sea, y está, pues, bueno, o sea, son varias. Está el de estatus, está el de el de remaining balance, está el de los treinta días, está el de staff, está el de pop up de SMS, que es lo de los los leads.
**Luis Torres**: Treinta días.
**Cristian Berrío**: Sí, o sea, lo de treinta días, siete días, un día, una hora.
**Luis Torres**: ¿Dese eso?
**Cristian Berrío**: Lo que vemos claro. En guess report, que no le cambié el nombre. Es ahí. Eso es eso es los reminders. De treinta días antes y eso.
**Luis Torres**: Entendido.
**Cristian Berrío**: O sea, el flujo de mensajes se hace a través de automatizaciones más complejas. El de tour
**Luis Torres**: Esto es esto es este post event la el estatus de post event es automático una hora después de que se termine un evento.
**Cristian Berrío**: El deposit event. No.
**Luis Torres**: Este trigger, student.
**Cristian Berrío**: Ah, o sea, bueno, eso ignora lo de post event y eso. Esos son labels porque antes recuerdas que la lógica nuestra era y por eso y por eso hay que estar como, o sea, por eso es que los cambios, cuando ya tú tienes algo implementado, son complicados. O sea, se quedó como post event, porque recuerda que nosotros habíamos cuadrado que él sea, no no íbamos a enviar reminders, que íbamos a enviar lo que es report un día antes de que empezara el evento, una hora inicial del evento y como ciertas horas después de que terminara. Entonces, los labels se quedaron así. Y si los cambio, pues se daña.
**Luis Torres**: No entiendo, pero ¿qué me qué...? ¿Cuál es el trigger de CLEVO actualmente?
**Cristian Berrío**: Actualmente, o sea, esos son jobs. O sea, esos son jobs, O sea, jobs son tú, cuando haces una reserva y la haces para dentro de un mes, genera enseguida el OIB host report step. Es decir, internamente, lo que hacemos es, con funciones de logable, cuadramos o calculamos cuántos días faltan para que ese evento se cumpla. Y ahí es cuando se acuda. Treinta días, el primer step, Siete días es el segundo step. Y creo que un día antes, una hora antes, no me acuerdo cómo está ahí. Yo me por los mensajes de texto. Así es como me O sea, por lo que dice los mensajes de texto. Y una hora antes, o un día antes, si no estoy mal, alguna de las dos, se ejecuta el tercer step. O sea, todo eso está automatizado, por eso es que cuando llega y por eso siempre te lo digo, cuando llega un booking, todo esto, literalmente, remaining balance, reminders, staff report, todo, todo, todo, todo se genera el mismo día. De que llega una reserva. Todo eso se cuadra, todo eso se agenda. Las automatizaciones no no se ejecutan Ay, no, que falta un día antes para el evento, ahí es cuando se va a ejecutar la función. No. O sea, todas esas señales las envía desde el primer día que nos llega una reserva. Independientemente de que solo hayan pagado el depósito, que vayan a pagar el cincuenta por ciento, eso todo se agenda. Obviamente, si no paga el cincuenta por ciento, en la hora estipulada, o si el el balance no está completo, pues no se le va a enviar esa esa comunicación. Pero todo eso se agenda. Esa comunicación, la única manera en que corta eso esos pasos, es cuando no pagan el el cincuenta por ciento restante.
**Luis Torres**: A tiempo.
**Cristian Berrío**: Entonces, Exacto, o sea, exacto, cuando a tiempo. O, digamos, que tú veces mandas el el invoice tú personalmente, hasta que ese sea, cuando tú sabes que que ellos salen deposit paid y sale paid. Cuando ya cambia estado de paid, ahí es cuando ya se puede mandar esa comunicación. Pero, mientras tanto, o sea, es muy estricto. O sea, el sistema lo dice muy estricto para que no pasen eso de que le envíe mensajes y el cliente no se canceló o nunca pagó el cincuenta por ciento restante.
**Luis Torres**: Entendido.
**Cristian Berrío**: O sea, es es demasiado estricto y todo es
**Luis Torres**: Y de parte, si lo paga tarde, si lo paga tarde el cliente y le le voy a mandar el link, igual va a pasar al próximo paso al próximo paso, ¿cierto?
**Cristian Berrío**: O sea, digamos que, exacto, digamos que ya pasa los quince días, ¿verdad? Los quince días el el cincuenta por ciento restante. Digamos que él lo paga yo qué sé, el día dieciocho, diecinueve. Si el día diecinueve lo paga, y aún así faltan siete días, se ejecuta y se le manda el SMS. Si digamos que lo paga el día diecisiete, el día veinte, y ya el veinte ya faltan seis días para que sea el evento, Ahí, obviamente, pues ya no se lo manda, porque ya pasó el tiempo.
**Luis Torres**: Entendido.
**Cristian Berrío**: O sea, ya ya pasó el tiempo de que se le envíe los lo del SMS de los
**Luis Torres**: La perdón es que se siga que se siga ejecutando a pesar de que, ajá,
**Cristian Berrío**: O sea, lo importante exacto no es ejecutarse, a pesar de que ya no faltan siete días, sino que faltan seis, que
**Luis Torres**: la nota para este mensaje como tal es si logra pasar este paso de post event tiene una regla de tiempo, porque todas las reglas que tenemos ahorita son de tiempo,
**Cristian Berrío**: Exacto, satón, son temporales. Los exacto, o sea, sí, son son temporales, básicamente. Entonces, yo lo puse por estados. O sea, la lógica real, real, está nuestras funciones de lobabor. Lo que hacemos con las automatizaciones es verlo de una manera visual, o... Sí, exacto, verlo por una manera visual, porque me he dado cuenta de que cuando si hacemos esto temporal, o si hacemos estos cálculos, en go high level, hacemos un desastre y no tenemos tracking de nada. Entonces todo eso literalmente son funciones que, cuando falla algo, enseguida me muestra el lock de qué fue lo que falló. Y todo eso está en lo hago. Todas esas son funciones ya desplegadas.
**Luis Torres**: Entendido.
**Cristian Berrío**: Entonces, por eso por eso es que ahorita mismo la comunicación o sea, la comunicación que tú me dijiste que estaba fallando, es que realmente estaba fallando, es que hay personas que, como hicieron o agendaron bookings cuando teníamos el arroz con mango, de tener los dos calendarios en uno. Entró en esa entró en esa automatización. Entonces, por eso es que o sea, ahorita mismo la comunicación, para que falle ahorita mismo, debe ser un caso muy particular. Que no se le envíe o sea, que no se la envíe el el del remaining un reminder, tiene que ser un caso muy específico de falla. Pero realmente no o sea, no está fallado. Sea, lo puse tan
**Luis Torres**: Ну, что у нас дела? Heather, do you speak in early November? How can I help you? Your Absolutely. Can you hold for two minutes? Awesome. Thank you. Mi Bruno, lo, mi pregunta es, lo que tenemos en ClickUp, en planificación, a nivel de tiempos, ¿está todo reflejado aquí la cadena que yo te mandé, que actualizamos hace poco.
**Cristian Berrío**: Yes. Abre el SMS del deposit event. ¿Es el que se envía siete días, treinta días? Sí. El, y todos
**Luis Torres**: No veo más mensajes, hermano. ¿Está el último mensaje que se las manda?
**Cristian Berrío**: El de reminder, sí. Ese era el último.
**Luis Torres**: Falta de siete días, falta de un día, ¿no?
**Cristian Berrío**: Siete días, ahí está, mira.
**Luis Torres**: ¿Y el de un día?
**Cristian Berrío**: El de un diez es que es por correo. O sea, por nuestro correo. ¿Por qué? Por lo que te digo. Y es que por eso hay que estar o sea, hay que estar full pilas cuando hagamos esto, para otros avenues. Porque, o sea, tú, inicialmente, lo hemos cambiado muchísimo. Y esto cuesta cada vez que que que buscamos un cambio de esto. Que tú me digas treinta días, siete días y una hora, ok, lo hago, Pero en vez de, digamos, que ya no quieres una hora, sino que sea un día, o que sea un día y una hora, o sea, que ya sean cuatro
**Luis Torres**: Sí, sí, claro, sí, claro. Yo entiendo entiendo la consecuencia de eso.
**Cristian Berrío**: Exacto, o sea, se vuelve muy complejo hacer todos esos cambios, así sean minúsculos de de un un correo más, un
**Luis Torres**: ¿Dónde es que tenemos eso? Aquí en
**Cristian Berrío**: A mí me llegó
**Luis Torres**: ¿Dónde tenemos la...? ¿Ah?
**Cristian Berrío**: No, lo tienes abajo. En OIB. En la, el espacio de OIB. Abajo. No. Eso no. Ahí.
**Luis Torres**: Listo. One reminder. No, no, necesitamos una una hora Falta un mensaje de una hora.
**Cristian Berrío**: El que está el que está ahí es de una hora.
**Luis Torres**: No, perdón, un día, aquí.
**Cristian Berrío**: El de un día.
**Luis Torres**: Falta ese.
**Cristian Berrío**: Por eso, o sea, ese ahorita lo estamos enviando es por Gmail, era como lo teníamos antes. Que tú me
**Luis Torres**: ¿Lo podemos poner en texto?
**Cristian Berrío**: sabría que enviar habría que agregar el extra paso, que es vez de tres, que sean cuatro, poner la lógica nuevamente, para que esa gente cada vez queda en un booking. Sea, todo lo que te he dicho, pero un paso extra. Y cambiar, obviamente, la automatización, poner uno más. Porque recuerda que a través de
**Luis Torres**: Okay. Entonces cambia, entonces cambia el de esta hora, entonces cambia el documento, ¿verdad? Like, no podemos tener un documento que no está funcionando, entonces, o sea, la idea es que lo que el día del documento es lo que está en ClickUp, no podemos tener dos cosas diferentes. Este es de un día, el de una hora, y déjalo para un día. Mejor.
**Cristian Berrío**: Y eso es más fácil. Solo
**Luis Torres**: Dale, pues activo. Dame dame un segundo, voy a atender a este cliente y te continuamos hablando. Mándamelo que vayas avanzando para el reunido, por la estructura de usuario, no sé qué es lo que estás estructurando, pero necesitamos estructurar eso.
**Cristian Berrío**: Te voy a mostrar lo que estoy haciendo, o sea, lo que voy a hacer, no está ejecutado, pero lo lo estoy haciendo ahora. Que lo miren.
**Luis Torres**: Dale, por último, no me lo puedes revisarlo antes de que antes de continuar. Dale, miro.
**Cristian Berrío**: Vale.
**Luis Torres**: Heather, this is Louis speaking from Orlando Avenue. Sorry for the hold. Can you hear me? Hello? Hello?

_Sincronizado por Brain: 2026-10-17T07:06:51.958Z_
