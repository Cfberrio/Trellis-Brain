---
brain_note_id: "dest:meetings:296b668ac317aaff1c30d3ca8ed28d47"
canonical_key: "meetings/296b668ac317aaff1c30d3ca8ed28d47"
brand_id: "meetings"
---
# Transcript — 2026-06-19 SyncUp Dev (21477)

## Transcript

- Reunión: [[02-Meetings/2026-06-19 SyncUp Dev (21477)]]

**Cristian Berrío**: Aló, aló.
**Luis Torres**: Sí, señor hermano, buenos días.
**Cristian Berrío**: Buenos días, ¿cómo estamos? Aquí una
**Luis Torres**: Aquí lo activo dándole su.
**Cristian Berrío**: Bien, bien. Excelente.
**Luis Torres**: Me alegro, miró. Ahora llamada ejecutiva para Doctor. ¿Estás listo?
**Cristian Berrío**: Listo.
**Luis Torres**: Vamos a darle.
**Cristian Berrío**: Estoy revisando qué fue lo que mandaste por ahí.
**Luis Torres**: Vamos a regresar los puntos. Listo. Okay. Bueno, vamos a compartir específicamente esta pantalla. Reporte completo, sesenta y siete iniciativas, adjusting corporate and proof. Creo que esto ya lo estamos clarificando, uno de los puntos que anoté es que, definitivamente, vamos a considerar vamos a consolidar este, una sola plataforma, ¿cierto?, donde tengamos nuestros accesos de dashboards, etcétera, todo un solo en un solo lugar, no en diferentes repos.
**Cristian Berrío**: Mhmm.
**Luis Torres**: Ahí estamos a ir con eso.
**Cristian Berrío**: Correcto.
**Luis Torres**: F dos. Aquí me, aquí el reporte sacó que los mensajes que no se leen cuentan como que si estuviesen recontadas en cada app. En cada, bueno, me imagino que se referen como en cada software. Lo cual, que la inconsistencia es centralizar las reglas, para que cada rol se comporte de la misma manera. ¿Entiendes más o menos a qué se refiere eso?
**Cristian Berrío**: ¿Esto se refiere a los mensajes de los mensajes que se mandan por los portal.
**Luis Torres**: Creo que sí.
**Cristian Berrío**: Debería. Creería yo. Capacity checks. An error message counts. R twenty
**Luis Torres**: Bueno, si querés, haré tú el mismo file, tú mismo para que puedas organizarlo. No estés como con la pantalla.
**Cristian Berrío**: Bueno, eso sí, habla de lo mismo, como lo tenemos dividido.
**Luis Torres**: Correcto.
**Cristian Berrío**: Son varias, una función para cada software.
**Luis Torres**: Excelente.
**Cristian Berrío**: Entonces, sería unificar también para una función
**Luis Torres**: Okay. F tres, formulas a shared design system, me parece que esto está bueno. Este, es por mobile first, loading empty, oversells, capturing this is result tokens. Que el diseño como que está formalizado en todas las, en todo en todo el sistema.
**Cristian Berrío**: Mhmm.
**Luis Torres**: Que sea un diseño consistente. F cuatro, no lo entiendo muy bien, Pienso que está hablando de go ahead level. No sé por qué está incluyendo información sobre el Doctor o VRV, C2S, vía brand prompts and go ahead of tokens. No entiendo esa parte. Okay. Securing compliance, algo que hay algo sobre f cuatro, f cinco? ¿Entiendes algo de eso? O lo
**Cristian Berrío**: Creo que está hablando de lo que tenemos ahorita, para ¿Cómo se llama eso? Lo que tenemos ahorita que responde los mensajes de voz y luego. Que genera como un draft.
**Luis Torres**: Okay.
**Cristian Berrío**: Creo que está hablando de eso, pero no entiendo por qué metió las otras marcas, la verdad. La verdad, no sé. That's it. F cinco,
**Luis Torres**: Securing compliance. Lockdown, public storage bucket, attachments, So for those can be enumerated by anyone, not just open via a node link. Move secrets out of Eskiba and rotate them. Start Edge Secret and Abrown Record, be Bueno, esto es un tema de seguridad. ¿Hay alguno que no está correcto, alguno que tú claramente entiendes esto, señor? Así que
**Cristian Berrío**: sí, o sea, eso es, básicamente, que o sea, row level security son las personas capaces de modificar las tablas editarlas, verlas. Entonces, como nosotros, al principio, pues estábamos un poquito digamos, en pañales cuando hicimos todo esto. No le metimos rollout en security. A las tablas. Igual, de todas maneras, a menos de que es como quien te dice, a menos de que un hacker nos quiere hacer daño, pues puede mirar la información. Realmente.
**Luis Torres**: Yeah.
**Cristian Berrío**: Pero es como que es a qué qué van a hacer con eso, porque no hay nada en las tablas, o solo va haber información de
**Luis Torres**: Got it. But
**Cristian Berrío**: Pero no no así.
**Luis Torres**: este, tenemos la realidad de nuestro asunto es que sí tenemos enemigos, por más de que pensemos que sí tenemos enemigos que se pueden filtrar lo menos, estamos teniendo una inconveniencia con uno de los, una de nuestras competencias nosotros le estamos dando estamos haciendo significantemente mejor que ellos en muchísimas áreas, y ellos están muy molestos de que nosotros estemos teniendo éxito entonces nos mandan mensajes de de threats que nos van a demandar, blablablá, blablablá. Pero, ciertamente, Maggie, nosotros le deberíamos de mandar a ellos, porque ya este punto es como un como una una invasión a nuestra a nuestra identidad corporativa, por el hecho de que no le hemos hecho nada, o sea, literalmente, lo único que hemos hecho es hacer las cosas bien. Pero claramente, cuando conseguimos resultados, eso ya es molesta, y tenemos problemas con con ellos, por eso. Pero el punto es que no creo que contraten un hacker para que nos hackeen las plataformas, ciertamente no es no lo veo no lo veo no lo veo feasible, no lo veo factible, pero ciertamente es una posibilidad.
**Cristian Berrío**: Correcto. Entonces, básicamente, o sea, es eso, es quién tiene la capacidad de ver las cosas. Entonces, como a one level security es como quien te dice, no tiene el two step authentication,
**Luis Torres**: Mhmm.
**Cristian Berrío**: Entonces, pues, cualquier persona que le sepa el tema, bueno, cualquier persona, pero alguien que le sepa el tema de de hackear, infiltrarse, como cuando un hacker se mete a una base de datos de de una clínica, le roba toda la y les dice, págame no sé cuántos millones para que soltemos la información.
**Luis Torres**: Correcto.
**Cristian Berrío**: O sea, no es nada así superguau, pues a pequeña escala. Pero a grandes escalas tipo corporativas, ya es más Pero, o sea, eso ya lo ya lo sé hacer, o sea, lo hice con que antes, cuando cuando estaba... ¿Cómo se llama?
**Luis Torres**: Arrancando, comenzando.
**Cristian Berrío**: No, ¿cómo se llama? Vercel ¿lo que era en una verse?
**Luis Torres**: Ajá, ajá. Sí, verso.
**Cristian Berrío**: Ah, bueno. Ajá, cuando estamos con no, no. No le sabía no le sabía poner eso. Pero ya con lo olieclode, ya esa vaina se hace sola.
**Luis Torres**: Mhmm. Modelo de data.
**Cristian Berrío**: Pero ajá, se puede bajar.
**Luis Torres**: Revisamos el modelo de data.
**Cristian Berrío**: Data...
**Luis Torres**: Standard conventions. School team session lowercase by newsletter, the art team partners, program is capitalized. Eso sí es muy importante, Cris. O sea, cuando estemos trabajando nombres de plataformas, etcétera, si estás trabajando algo si la escuela es Caperdise, mantén todas las escuelas Caperdise.
**Cristian Berrío**: No, está bien.
**Luis Torres**: ¿Me entiendes?
**Cristian Berrío**: O sea, esto se refiere a el nombre de las columnas.
**Luis Torres**: Exacto. Bueno, hasta hasta eso, mínimo, hagamos algún informe bonito.
**Cristian Berrío**: Ok.
**Luis Torres**: O sea, hasta hasta en el detalle más mínimo, la idea es trabajar de manera consistente, o sea, que no haya como que Si vas a, si vamos a decidir en llamar títulos de tablas, equipo, etcétera, Todo capitalized tiene que ser capitalized across the board, no, que no haya inconsistencia. Aquí dice, build a real skills and tears data model. Skills and levels is described as one of the most valuable parent features. Yet the database only stores student levels. Integer one through six. The actual skills appear hard coded in the UI, so coaches cannot really update them. Making this data driven unlocks the future end to end. ¿Qué piensas tú al respecto? Aquí está como que diciendo que no solo que los coches meter el skill, sino puedan como que añadir, modificar los skills que aprenden dentro de cada dentro de cada tier. Dentro de cada nivel del niño. Que se ha dado como que más tender hacia cada niño, lo que yo entiendo por eso, ¿cierto?
**Cristian Berrío**: Sí, básicamente, los skills que tú mencionaste, del uno al seis, eso está como quien te dice,
**Luis Torres**: Sí, yo sé, yo sé, yo sé, entiendo esa parte.
**Cristian Berrío**: Bueno, entonces, o sea, lo que menciona ahí es que las skills sean como una columna nueva, cosa de que, si el coach la quiere cambiar, en su dashboard, esa información se guarda en la tabla y se refleja en el en el ¿Qué? Se refleja en el dashboard de de padres. Entonces, es cosa de que, si digamos que tú lo quieres cambiar mañana, me tengas que decir a mí, hey, cambia esto. En vez de yo cambiarlo, pues que lo cambien ellos mismos. Cuando quieran cambiar las skills o lo que sea.
**Luis Torres**: Encanta ese me encanta esa me encanta ese feature. Excelente. Explaced statements change for payment enrollment. Canceled abandoned card status inferred from a mixed of inactive, abandoned, notified, payment joint. Is fragile and hard to reason about. Creo que hay que mejor lógica a nivel de cuando los papás dejan de hacer los pagos, etcétera, ¿cierto?
**Cristian Berrío**: Mhmm. Yes.
**Luis Torres**: Eso ya lo tienes que hablar. ¿Cómo lo podemos hacer? Básicamente, que en vez de que tengamos estos estatus locos, creo que lo que dice que es que tengamos un proceso más técnico. Pending payment, paid, abandoned, refunded. And payment as pending, driven by webhooks rather than client signals. ¿Sí o no?
**Cristian Berrío**: Correcto. Pero espérate, dime. Okay.
**Luis Torres**: Ok. ¿Qué qué tal si tú revisas cada uno de los puntos? Estamos en data models, d m uno, dos, tres, cuatro, ciento seis, ¿Me explicas qué es lo que está diciendo? Y y como que qué es lo que hace al respecto, en vez de que yo te explique a ti. Claramente, me parece que es una pérdida de tiempo que yo te explicaron, lo cual no, o sea, yo con lo entiendo, ¿no? O sea, yo entiendo la estructura que tenemos actualmente, lo que está tratando y cada, lo que toma cada uno de los puntos, lo que lo que pienso es que aprovechemos esta conversación para hablar lo que lo que estamos lo que estamos visualizando, y y estará en la en la misma línea, de lo que tenemos que hacer antes de montar el el dashboard completo de todo el ecosistema completo de de nuevo, eso es lo que va a comenzar hoy. Hoy vamos a comenzar a trabajar el el hoy vamos a comenzar literalmente, tratar de avanzar lo más que podamos para, por lo menos, tener la infraestructura lista de DVR.
**Cristian Berrío**: O sea, lo que dice el d m dos es g cuando un padre no paga o deja el carro abandonado o falla el pago. Sea.
**Luis Torres**: Correcto.
**Cristian Berrío**: Que no sea una acción como que de cliente o que el tree no sea el cliente, tipo, no sé, pasaron tres minutos desde que estaba en el checkout, y no pagó. O sea, que sea como que orientada hasta el Webhooks, O sea, que el mismo Stripe maneja los diferentes estados, cuando alguien no paga, cuando alguien abandona, cuando alguien, no se le sale declined la tarjeta. Que no manejemos esos, esa lógica nosotros, sino que lo hagamos por Stripe Webcast,
**Luis Torres**: ¿Qué opinas de esa solución?
**Cristian Berrío**: Pues, o sea, vamos vamos a orientar a algo real que que no tenemos que hacer nosotros. Porque, o sea, lo que se hacía era que, si pasaba x cantidad de tiempo y no había pagado, pues nosotros asumíamos que no o sea, nosotros nosotros tomábamos esa lógica bajo esa lógica, pues mandábamos un mensaje de texto o este, un mensaje de texto, un correo o lo que sea, Entonces, así, pues, nos, o sea, mantemos una organización mejor, porque, o sea, eso lo manejas Drive literalmente, o sea, no es con nosotros ya. O sea, mismo Stripe maneja las señales, el mismo sabe cómo maneja eso internamente. Así como cuando hacen un pago y Stripe manda como que el aprobado de que llegó el pago. Entonces, pues ahí, eso le dejamos la lógica totalmente a Stripe, y no lo hacemos nosotros. Porque pasaba que a veces cuando hacía pruebas, y digamos que ya estaba en checkout, y me demoraba x cantidad de tiempo porque me ponía a hacer otra cosa. A mí me llegaba a veces un correo, que teníamos cuando no paga, de o sea, el, no me acuerdo cómo se se cómo se llama el correo. Pero hay un correo que nosotros mandamos cuando no pagan. Es como que vuelvan a pagar. Sea, que se metan otra vez y paguen. Entonces, digamos que el trigger de ese correo ya no es como que, ay, me demoré cinco minutos. Sino que el mismo Stripe identifica como cuando tú estás pagando algo y dejas ahí eso abierto, que cuando tú vas a querer meter la información, se se reinicia, no te deja, etcétera, etcétera.
**Luis Torres**: Correcto.
**Cristian Berrío**: O sea, ¿te parece? No. Pues a eso lo manejas, pues, en la plataforma de pagos que estés usando.
**Luis Torres**: Correcto.
**Cristian Berrío**: Entonces, eso es lo que te refiero.
**Luis Torres**: ¿Qué vamos hacer al respecto? ¿Piensas que utilizar webhoods de Stripe va ser una mejor solución? O sea, el punto es, yo sé a qué se refiere, O sea, yo más o menos quiero que veas que, si tiene el punto, revisemos todos los puntos rápido, si tiene validez, skipéalo. Si si no tiene disculpa, skipéalo. Y si tiene validez, explica qué es lo que está pasando y qué lo que vamos a hacer. Eso es lo que a mí me importa de de de lo que estemos de lo que estemos en
**Cristian Berrío**: Okay.
**Luis Torres**: de el objetivo de lo que estamos haciendo justamente ahorita en esta reunión. Para Diana.
**Cristian Berrío**: O sea, no es crítico, pero se, o sea, no estaría mal tenerlo. Pero no es crítico, tipo, prioridad cien por ciento.
**Luis Torres**: No,
**Cristian Berrío**: Estaría chévere.
**Luis Torres**: muchas de estas cosas no son críticas, pero la idea es mejorar lo que tenemos actualmente, ¿no?
**Cristian Berrío**: Ah, sí, o sea, sí, para mejorarlo, sí, pues, sí es útil bastante. Que no les llegue el correo a un padre que haciendo el checkout, solo que se está un poquito más porque está buscando la tarjeta o está haciendo x cosa.
**Luis Torres**: Excelente.
**Cristian Berrío**: Entonces, sí sirve.
**Luis Torres**: Excelente.
**Cristian Berrío**: Bueno, el de d m cuatro
**Luis Torres**: Ok.
**Cristian Berrío**: hacerlo un poquito más robusto, en vez de, si viniera no dinero, que, o sea, que tenga más como estados. Que tenga labels, así como dice. Present, absent, late, excused. O sea, como que de de más opciones. Más que un sí o un no. Es útil. Bueno, no sé hasta qué punto, porque no sé qué no sé cómo tomar la asistencia, pero pero, bueno, hay algunos padres que ponen o que mandan correo de que el hijo no fue. Pero eso es como cuando le mandamos la la automatización de que el hijo no fue.
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Pero pues, no sé qué tal sea eso, no sé si sepas tú o qué. No sé a ti cuando te llamen o te digan como que, hey, mi hijo no va ir hoy o lo que sea. No sé si eso es como
**Luis Torres**: Igual les mande la, igual le mandamos el correo y que le dijo va a estar absent, o sea, el correo estuvo absent.
**Cristian Berrío**: Sí, exacto.
**Luis Torres**: Sí. La simplemente la la instrucción de de responder ese correo tiene que ser como que entrenará a cloud, o quien responda a nuestros correos, a través de lo que sea, tener un file de cómo responder correos de de ausencia. Y que ese correo diga, bueno, si van a estar ausentes y no lo dice con anticipación, le respondemos como que no problem, thanks for letting me know, I'm not afraid of coaches, we will still mark him absent, you'll be getting an email later today. Notifying you of of of your child's absence. Ese es el mensaje que debería tener ese correo de respuesta. Claramente, tenemos que activar de nuevo que tenemos tenemos que cambiar el flujo que tenemos para los correos de día que responden los correos de día, ¿cierto? Una vez tengamos toda la información adentro del nuevo ecosistema, creamos instrucciones para responderle a padres que puedo extraerla. O sea, yo ahorita con Cloud conectado al correo a través del MCP, de Claude, y el correo electrónico de Doctor, Bueno, creo que no puedo conectarlo al correo electrónico de Doctor porque no tenemos la suficiente dentro de Claude. ¿Qué has hecho tú para esos casos? Cuando tenés que conectar un MCP a una cuenta que no es Trellis,
**Cristian Berrío**: Mas?
**Luis Torres**: Digamos que tienes que, no sé, por alguna razón, meterte en una cuenta de Google que no es Trellis, de the cloud. A través del MCP. ¿Cómo tú lo haces Porque no tenemos supervisión en otras cuentas de correo.
**Cristian Berrío**: No, eso no tiene nada que ver. No tiene que ser el mismo correo. Por ejemplo, yo ahorita, yo yo ayer conecté SupaBase, a al o sea, su, a ver,
**Luis Torres**: Pero ¿tú has intentado hacerlo con Gmail? Porque a mí a mí no me dejó hacerlo con Gmail porque es como la misma cuenta de Google. ¿Entiendes? Te te fuerza a hacer un log out y un log in de clon.
**Cristian Berrío**: No estoy bien, O sea, raro, porque realmente el MCP y Claude son cosas completamente distintas. Supabase, tú sabes que está con la cuenta de discipline brief, el Gmail de de discipline rift. Lo conecté sin problema. Y he conectado varias cosas así, que no tienen que nada que ver con Trailis. No o sea, no, de pronto, ¿estabas haciendo algo malo o qué? Pero eso sí deja.
**Luis Torres**: Yeah. Ok, continuemos.
**Cristian Berrío**: Bueno, o sea, esto es útil. La verdad. Se puede poner. Sirve tener como como otro lever. Otro nivel de de de que se pueden hacer cuando un padre te envíe un correo de apps en lo que sea. No sé, o sea, para futuro, pues, organización, está chévere. O llevar un reporte. Más detallado más que un sí vino o no vino.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Mire, aquí sale. Pero o sea, se puede poner, habría habría que cambiar cosas. Eso sí. By the way, por cada cosa que está hablando aquí, no es cambiar base de datos, sino cambiar código. Todo lo que menciona aquí. Por ejemplo, estandarizar esto, que esta school salga en minúscula, Yo le voy a poner mayúscula, ahí cambiar todo todo, todo, todo, lo que referencia a la escuela en minúscula, hay que enviarlo todo por mayúscula. O sea, todo esto cuando, si se aprueba, hay que hacer cambios también al código. O sea, no es un copy paste, sino que que modificar también todo eso.
**Luis Torres**: Modificar qué parte dentro de Google, eso no es lo que, no entiendo.
**Cristian Berrío**: No, no, no, código, código, todo esto es código.
**Luis Torres**: Ok.
**Cristian Berrío**: Todo esto es base de datos, y código.
**Luis Torres**: Ok. Pero igual no vamos a pasar esa base de datos por cloud para mejorarla. De todas maneras.
**Cristian Berrío**: O sea,
**Luis Torres**: O sea, ¿tú te sientes cómodo con continuar con el modelo? O sea, ¿a todos que tienes actualmente?
**Cristian Berrío**: No, o sea, yo estoy de acuerdo que hay que mejorar cositas. Lo que te quiero decir es que, al mejorar cositas, pues, hay que cambiar bastantes cosas, bastantes ambientes que que están funcionando actualmente. Entonces, como obviamente vamos a vamos a hacer prácticamente todo esto de cero. No es de cero, porque ya tenemos una lógica pero sí es de cero, porque todo el código se va a hacer de cero. Porque no podemos migrarlo así, a lo caré perro, copiar y pegar. Hay que hacerlo todo de cero. Entonces, al al hacerlo todo de cero, si yo le paso información de de que school sale minúscula, pero ahora queremos estandarizar todo para que sea mayúscula, pues todo eso tiene que ir cambiando. Entonces, es información que no tenía, sino que va a tomar guía de lo que ya tenemos y lo va a mejorar. Tanto la base de datos tanto en código. Entonces, o sea, sí, es como que estemos en la misma página, de que si vamos a hacer cambios, para mejorar, obviamente, pues, obviamente, hay cosas que que, o sea, una cosa afecta a todo, Cuando se trata de base de datos, una cosita afecta a todo. Todo, todo. Por ejemplo, esta cosita de de sí o no, pasarlo a a estados. Pues afecta. Afecta la lógica que ya manejamos. Entonces, esos cambios hay que tenerlos en cuenta y hay que hacerlo. Pero, o sea, si yo sí estoy de acuerdo en en hacer todo, o sea, yo estoy de acuerdo en hacer los cambios, para mejorar, obviamente. Porque todo esto es mejorar. Que no sea un simple nuestro website sirve, aún, o sea, nuestro nuestro website sirve y estar lo más posible. O sea, si ya vamos a mirar todo, pues, aprovechamos y mejoramos todo también.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Pero sí. Bueno, el DM cinco,
**Luis Torres**: Entonces, ¿qué vamos a hacer con la base de datos? ¿Cuál es tu cuál es tu propuesta final?
**Cristian Berrío**: Mejorarla. Modifica.
**Luis Torres**: Ok. Entonces, esos cambios, eso va a requerir cambios que lo van a dar requerir que restructuremos todo eso, ¿no?
**Cristian Berrío**: Yes.
**Luis Torres**: Bueno.
**Cristian Berrío**: So, va requerir bastantes cambios. La cuestión es, lo que estoy viendo, bueno, no sé si me deje, pero la primero, es pasar el esquema. Eso es lo primero que voy a hacer. O sea, pasar el esquema de base de datos, con las mejoras que estamos hablando, La cuestión es, metires, puede. Nada, nada, olvídate. O sea, la primero era mejorarlo y después lo que tenía pensado era exportar la data.
**Luis Torres**: Okay.
**Cristian Berrío**: La ataque que tenemos que no perdamos nada.
**Luis Torres**: Okay.
**Cristian Berrío**: Falta ver cómo va a funcionar eso. Porque hay tablas que ciertamente no tienen muchos datos. Pero hay otras que sí tienen que si mil, dos mil y pico, Entonces, que ver eso. Habría que ver cuánto demora hacer esa migración de datos. Pero, bueno.
**Luis Torres**: Todo es un paseo. Bueno, la mayoría de las cosas, paseo.
**Cristian Berrío**: No, o sea, se demora en el sentido de cargar los datos.
**Luis Torres**: Oh, bueno.
**Cristian Berrío**: O sea, cargar la data que ya tenemos, que no perderla.
**Luis Torres**: Fíjate que pronto vamos a tener las computadoras de Moche, Charlize y Julius, así que prepara tu estación para que tengamos múltiples sesiones de clore y y computer de power corriendo.
**Cristian Berrío**: Más o menos una una infraestructura.
**Luis Torres**: Vamos a vamos a
**Cristian Berrío**: Pues vamos vamos a montar una supercomputadora.
**Luis Torres**: vamos a convertirnos en esa gente que nunca en esa gente que que utilizó... ¿Cómo se llama eso? Que utilizó los Mac minis para para lanzar OpenClow.
**Cristian Berrío**: Literal.
**Luis Torres**: Ese sueño que pudimos alcanzar,
**Cristian Berrío**: Literal. Okay. Este, bueno, el cinco eso es construir backup tables. Okay. O sea, aquí dice que no no construía backups. En la el avance de datos de producción. Que son
**Luis Torres**: ¿Qué opinas al respecto?
**Cristian Berrío**: Pues sí, o sea, eso es más que todo por organización. La verdad. No es como modificar, es como una recomendación.
**Luis Torres**: Okay.
**Cristian Berrío**: Porque ahora yo tenía bases de, yo tenía tablas Cuando iba a tirar como un feature así, bien ácido, creaba un un backup de la tabla. Por si acaso. Uno nunca sabe. Si borraba algo, hacía algo que no había. Entonces, la dejaba ahí y no la borraba. El backup. Cuando ya, digamos, que funcionaba. Ahí me dice,
**Luis Torres**: Bello, sí me acuerdo de esa. Me acuerdo de eso.
**Cristian Berrío**: Entonces, ahorita mismo ahí como bastante establitas duplicadas, entonces dice que no lo guarde ahí, sino que lo guarde, digamos, en mi computador.
**Luis Torres**: Yeah.
**Cristian Berrío**: O que lo guarde en una base de datos completamente instalada en producción. Ok.
**Luis Torres**: Me parece bien, me parece que es una buena buena recomendación. Aquí te aquí te te grillaron, ¿no?
**Cristian Berrío**: Sí. Aquí están, dice, todos
**Luis Torres**: Te dieron duro
**Cristian Berrío**: aquí están diciendo, organiza tu vida.
**Luis Torres**: Te te te dieron dónde más, dónde más? Donde más era necesario.
**Cristian Berrío**: Sí, ese ese clut es un poquito grosero, realmente.
**Luis Torres**: Sí, me gusta hacer cuándo se pone cuándo se pone director o cero.
**Cristian Berrío**: So,
**Luis Torres**: Me
**Cristian Berrío**: admission, access and drop. On index attendance enrollment message page. Ok, aquí dice que no utilice data redundante. Por ejemplo, tengo una de que dice que message, y otra message read status, O sea, tengo como que cosas que o columnas que no estoy utilizando. O tengo las tablas que están no sé, digamos, muy grandes. O sí, que tienen como que columnas innecesarias que no se utiliza, y al momento de hacer consultas o hacer cosas, se demora. Entonces, ¿qué...? Que quite como que esas columnas redundantes que ya no estoy utilizando. Por ejemplo, como las columnas de de is active, is ongoing, antes utilizábamos. Utilizábamos true, false, false true, para saber el estado. Bueno, ahora nosotros, lo que estamos utilizando son las columnas de estatus. En vez de de como que hacer ese esa distinción de true, false, false true. Esas columnas que ya no se están utilizando, borrarlas. O eliminarlas. Porque, ajá, no se están utilizando, ¿y qué van a estar ahí? DM siete upgrade the coupon models. Okay. Aquí dice el de upgrade coupon model es mejorar eso. Para que sea, o sea, que esté más organizado. Por ejemplo, cuando tú crees un cupón que tenga un máximo de usuarios, o máximo de personas que puedan utilizarlo, o tener como duración que empieza, termina tanto. O sea, como no crear un cupón y que el cupón. Pues está útil. La verdad. Vaso extra. Pero sí, o sea, está chévere. Que pueda poner como que cuando un cupón y eso.
**Luis Torres**: Excelente.
**Cristian Berrío**: Public marketing. Esto tiene un montón de puntos. Estoy bajando y
**Luis Torres**: Nunca se acaba.
**Cristian Berrío**: Qué locura. Esto te lo hizo, Claus.
**Luis Torres**: Yes, sir. Le mandé el mega prompt. Le hablé como unos veinte, unos diez, quince minutos dándole todo el contexto.
**Cristian Berrío**: Si. Sí. Está un
**Luis Torres**: Para que me viera eso. ¿Ah?
**Cristian Berrío**: un poquito un poquito loco esto.
**Luis Torres**: ¿Loco por qué?
**Cristian Berrío**: No, aquí está largo.
**Luis Torres**: Oh, sí. Bueno, pero sí, lo que te digo, lo que te parezca nonsense, es lo que te parece que es un buen punto, conversémoslo. Para que tengas claridad. Tú y yo tenga claridad, y le damos ¿te parece?
**Cristian Berrío**: Okay. Bueno, aquí dice, que se puede presentar un problema si dos padres están pagando al mismo tiempo, y solo hay un spot left
**Luis Torres**: Ah, eso eso es muy, hay cero punto cero posibilidades de que eso suceda.
**Cristian Berrío**: literalmente son O es imposible que pase. O sea, hacer una lógica completa para algo que
**Luis Torres**: Imposible.
**Cristian Berrío**: Sí. Bueno, aquí dice, make a store webhook the the source of true payment. Eso es lo que estamos hablando ahorita. Que no manejemos la lógica nosotros, sino que a través de Webhooks de Stripe, pues él mismo analice cuándo una persona abandonó declínio, etcétera, etcétera. Eso me parece importante. Aquí dice algo, Dije a full team, is a lost demand today. Capturing a waitlist convert that demand when spots open. O sea, que era una waitlist, en vez de que el equipo salga full, como que tenga una waitlist. ¿Qué opinas de eso tú? ¿Necesario o innecesario?
**Luis Torres**: Fire, sería fire, sería superfire.
**Cristian Berrío**: Una waitlist.
**Luis Torres**: Sí, una sí.
**Cristian Berrío**: Ok.
**Luis Torres**: Y si decidimos hacer más más una que esos papás del waitlist estén en una, que estén en una tabla de la base de datos de esa temporada. Acuérdate que nosotros al final de Doctor, como que más como que cerca de octubre, noviembre, replanteamos la lógica de temporadas, ¿cierto? La lógica de la lógica del sistema
**Cristian Berrío**: Mhmm.
**Luis Torres**: y establecimos nombre por temporadas. Entonces, tiene que haber una tabla de temporada ese lo tenemos actualmente, así es que se refleja en Google Earth. Tiene que haber una tabla de temporada de equipo, ¿Te acuerdas que en Google tienes que poner el tag? Oh, tan año. Y el equipo, y te salen los los nombres de ese equipo y ese de ese equipo de esa temporada. Entonces, de la misma manera, necesitamos una tabla para el waitlist de ese equipo, donde los papás entren al waitlist y cuando hagamos más más spots, si es que se abren, podamos podamos decirles, porque actualmente ellos como que me dicen, mira, quiero entrar en el well list, y yo tengo que como que anotar eso por ahí, veces se me pierden las notas.
**Cristian Berrío**: Yes.
**Luis Torres**: Entonces, sería superbueno que tengamos eso. ¿Qué tanto dolor de cabeza crees que eso causaría?
**Cristian Berrío**: No, solo una tabla. ¿Y quién cuando vayan al equipo full, le den un botón. Y se guarde la información de ellos. Ah, bueno, espérate, ¿cómo guardaremos la información? Sería como que añadir... Okay. Sería como que entra al equipo, ve que está full, abajito, en vez de registrar, sale el botón de waitlist, le dan ahí, llenan que si su nombre, su email, su número.
**Luis Torres**: Así es.
**Cristian Berrío**: Y cualquier que quieras tú.
**Luis Torres**: Así es.
**Cristian Berrío**: Ok.
**Luis Torres**: Me encanta ese reporte, estaba más Yo lo leí completo y yo dije, bueno, hay algunos puntos que me los porque no los entendía, pero, bro, habían demasiados puntos muy, muy jugosos.
**Cristian Berrío**: No, sí está está está efectivo.
**Luis Torres**: ¿Qué más ves? Lindo?
**Cristian Berrío**: Sí, te la parte de authentication. Mira, un
**Luis Torres**: Veremos crear un, veremos crear un authentication también para los coaches, ¿no? Capa. Por los
**Cristian Berrío**: ¿Puede para qué?
**Luis Torres**: coches tienen un gas application, ¿cierto?
**Cristian Berrío**: Claro, tiene OTP.
**Luis Torres**: Y ellos le hacen log out, la plataforma hace log out, cuando ellos están dentro de la dentro del dashboard,
**Cristian Berrío**: ¿No les hace log out? Sea, si se reinicia, me hiciste dudar. Yo creo que sí les hace logo después de cierto tiempo.
**Luis Torres**: Bueno,
**Cristian Berrío**: Tipo inactivo.
**Luis Torres**: el punto es, hagamos, ya ya tenemos quitemos el log out, porque a veces cuando estás dentro de las escuelas, la conexión es muy mala. Y si tienen que meterse a hacer hacer attendance, va a ser mucho proceso de de de va a ser mucho proceso que ellos hagan. Entonces, la idea es que no, que no lo hagan.
**Cristian Berrío**: Que no se expire la sesión.
**Luis Torres**: Correcto.
**Cristian Berrío**: Ok.
**Luis Torres**: Podemos crear un apartado cuando ellos estén haciendo attendance de una como un survey, un cuestionario que ellos llenen.
**Cristian Berrío**: ¿Cómo hace?
**Luis Torres**: En esa práctica, digamos que digamos, ok, es? Attendance, haz el attendance. Paso uno. Paso dos, responde preguntas. ¿Cómo fue la práctica de hoy? Uno, ¿cómo fue la práctica de hoy? ¿Qué problemas tuviste? Claramente, van a ser otros, ya tengo esas preguntas estructuradas, pero son preguntas ejemplo, que ellos las puedan responder ahí mismo.
**Cristian Berrío**: Ok. Diría que, en cuanto no sea tan largo, pues no se hace tan tan engorroso, los los coches sí hacen eso. Porque siento que, si pones muchos extra pasos, es como cuando tú estás
**Luis Torres**: Correcto, correcto, correcto. Una pregunta, que asistiría que sea una pregunta, algo así. Y
**Cristian Berrío**: Exacto.
**Luis Torres**: que dentro del admin, yo pueda editar esa pregunta.
**Cristian Berrío**: Okay. Sí. Sí se podría. ¿No estás tan loco?
**Luis Torres**: Okay. Vamos a implementar eso también.
**Cristian Berrío**: Qué bendición. Creo que lo va volver tiene. MCP. Para hacer cambios. En
**Luis Torres**: No sé.
**Cristian Berrío**: en la base de datos. Qué rico, gracias a dios. Ok.
**Luis Torres**: ¿No está autorizado la el MCP de la base de datos de logo?
**Cristian Berrío**: No puedo. Sea, es que como te explico, O sea, utiliza superbase. Un es muy
**Luis Torres**: Viejo.
**Cristian Berrío**: muy interno, muy interno de ellos. O sea, es como que le, ellos ellos utilizan lo mismo que pero a le recortaron como que un cuarto de todo lo que puede hacer. Entonces, el supabase que utiliza a ellos es muy o sea, es muy simple. Porque lo hago, en verdad, es para que lo use todo el mundo. Entonces, las funciones principales que tiene SupabC, pero no te deja accederlo no no es muy robusto, no es muy robusto. Entonces, digamos que cuando yo cambié a una función cuando iba a cambiar algo de la base de datos, cuando iba a hacer algo así relacionado a base de datos y funciones, tiene que hacerlo muy manual. Es decir, digamos que hacía todo en cloud, y cloud hizo una una modificación a la base de datos o una función. O un cron job. Entonces, después le daba push, al repositorio, y le le me tocaba escribir un prompt al abogado diciendo, hey, necesito que actualices la función con esta que que te mandé. O necesito que actualices o que la base de datos con los campos nuevos que agregué. O sea, me tocaba hacer literalmente doble proceso, mandar la información a a Lowable y el lowable escribirle como que mira este archivo y ejecuta los cambios. En la base de datos. En cambio, con su pago, y siempre fue hago un cambio y ya. Se se se proyecta el cambio.
**Luis Torres**: Claro, entonces ahora para trabajar en la base de datos de logo va a ser mucho más fácil con el MCP.
**Cristian Berrío**: Cien por cien, la base de datos, las funciones, o sea, todo, todo. Todo lo que antes el el que se mandó,
**Luis Torres**: Eso es lo que te asustaba, ¿no?, de todo este proyecto.
**Cristian Berrío**: ¿Cómo?
**Luis Torres**: Eso es lo que te asustaba, de todo este proyecto.
**Cristian Berrío**: Eso es lo que no te escuché.
**Luis Torres**: Como que una base de datos tan robusta la base de datos de Lobo es lo que te asustaba este proyecto.
**Cristian Berrío**: Cien por ciento. O sea, es lo que más me costaba. Porque me tocaba hacerlo todo muy manual.
**Luis Torres**: Ya se te resolvió la vida, bro.
**Cristian Berrío**: Exacto, y así me resuelve bastante, bastante. Gracias a dios. Pero, bueno, dashboard, esto está bueno. Pero está raro. En parent dashboard, self serve, reenrollment, and registration. Que a través de de ahí con un clic puedan entrar en puedan ¿Cómo se hace eso? O sea, hacer el enrollment de de del niño. Con un solo clic, y que lo redijea como a checkout o no sé, como al overview de qué lo que van a pagar. Después al checking.
**Luis Torres**: Fire. Fire.
**Cristian Berrío**: Eso está bueno. La cuestión es Bueno, hay que ver cómo afectaría eso. O cómo se haría. Por ejemplo, si quieren cambiar algo del
**Luis Torres**: La la porque es posible.
**Cristian Berrío**: No, sí, pero no sé,
**Luis Torres**: No, mentira.
**Cristian Berrío**: si quieren cambiar información del niño o algo así. Yo diría, que leer al botón de reenrollment los redirija automáticamente y autopopulará la información del niño, y creerá next. Ya, pues, le salga lo volvió del pago y ya le den a pagar. Por si por x o y motivo quieren cambiar la información del niño. Que, por ejemplo, o sea, digamos que ya pasó un año o pasó varios años y niño ya, obviamente, no tiene siete años, sino que ya tiene ocho. Como que vayan a cambiar este tipo de información, ¿sí me entiende?
**Luis Torres**: Claro. Otro punto hacia eso, me parece que sería bueno que los papás tengan una manera de poder de registrarse varias temporadas. Dentro del parent dashboard. ¿Me entiendes?, que puedan ver las temporadas siguientes ahí mismo. Y que las tablas de las próximas temporadas ya estén creadas.
**Cristian Berrío**: Fuerte situación.
**Luis Torres**: Cuarta situación, ¿cierto?
**Cristian Berrío**: Claro, porque eso significa que alguien meta eso significa que tú, directamente sepas qué va a pasar la siguiente temporada. Porque hay veces que tú modificas las cosas. Hay veces que tú no modificas la temporada y lo
**Luis Torres**: ¿Y podríamos tener una temporada, podríamos tener una temporada sin fechas? Que nada más sea una base de datos y ya, y luego y luego en en esa temporada meterle la las fechas como tal, cuando la montemos live.
**Cristian Berrío**: So I se pueden duplicar las mismas fechas.
**Luis Torres**: Porque, en teoría, yo puedo montarte la fecha actual temporal, yo completo. De un solo golpe, no no tengo problema con eso. Especialmente ahora que yo trabajo los schedules con Claude, Es mucho más sencillo. Antes tenía que poner cada fecha con mi con mis dedos.
**Cristian Berrío**: O sea, yo creo que sí. La cuestión es, bueno, digamos que yo duplico la yo duplico los equipos, y le pongo como un nuevo estado de coming soon, cosa así. O sea, en teoría, sí se puede como que escribir pues, ahora es temporada. La cuestión es cómo se va a manejar la lógica, o van a pagar las tres temporadas, upfront o qué descuento se le puede hacer? Porque, o sea, si yo voy a pagar tres temporadas adelantado, algún descuento me tienes que hacer. O sea, como que la lógica se vuelve un poquito más me parece a mí. Y sea, no sé, de pronto sería como un feature chévere para futuro.
**Luis Torres**: Sí, o sea, sí, ponte, en el tal escenario que yo te dejé todas las fechas de todos los equipos listos para el año completo, podríamos tenerlo.
**Cristian Berrío**: Sí, o sea, sí, o sea, lo único, no se Bueno, mentira, podría poner como que las fechas. Y lo pongo todo, pero como en estado coming soon, ya.
**Luis Torres**: Exacto. Y que se registren dentro del dashboard.
**Cristian Berrío**: Exacto. O sea, no saldría en el front end, front end, sino en el dashboard de de
**Luis Torres**: Amazing.
**Cristian Berrío**: como que le salga la opción de de de enroll para para, pues, varias Pues ya tú desarrollarías la lógica de qué descuento lo harías dependiendo de cuántas temporadas se inscriba. Por adelantado.
**Luis Torres**: Correcto, correcto, correcto. Sí, que, digamos, que en checkout haya un código de descuento, algo así. Dentro del mismo parent dashboard.
**Cristian Berrío**: Okay. Make skills levels live. Lo mismo, que en el dashboard de padre, los skills toda esa información, no sea que esté en una base de datos, y, pues, tú la puedas modificar. A través del dashboard. De de admin. Upgrade the payment tabs. Payments are read only. History expects receipts. Ah, bueno, esto. También es importante. De cierta manera. Los pagos, ellos solo ven como que, ay, pagaste ciento veintinueve. Pero la idea es que tengan como pueden acceder como un PDF o un recibo.
**Luis Torres**: Invoice, invoice.
**Cristian Berrío**: Invoices.
**Luis Torres**: Un invoice que se les pase por correo. Que tenga la que tenga el nombre de la compañía. Ya te mando el nombre de la compañía y todo eso.
**Cristian Berrío**: Bueno, aquí se refiere más a que puedan acceder a ello a través de el payment tab que está en su dashboard. Exacto.
**Luis Torres**: También, pero sería excelente que le mandemos la información por correo, solo por
**Cristian Berrío**: Que se lo mande por correo y que tengan también acceso directamente desde el dashboard.
**Luis Torres**: Correcto.
**Cristian Berrío**: Dios mío, Claude me dio mucho paro ahí, esta vaina que
**Luis Torres**: Te te desnudo, bro, te dejo desnudo.
**Cristian Berrío**: Cuando uno cree que uno uno está bien, salen con estas vainas.
**Luis Torres**: Cuando piensas que finalmente estás avanzando, viene Claudia te
**Cristian Berrío**: Literal.
**Luis Torres**: y te
**Cristian Berrío**: Y encuentra encuentra catorce mil puntos para No, pero en verdad está tirando tirando insights bastante Como que está tirando ideas que que no se me ocurrirían lo primero. Me da me da otra
**Luis Torres**: Me estoy dejando en la website.
**Cristian Berrío**: Okay. Unified notification centers. ¿Cuánto importa? Consolidate messaging into module. Ah, bueno. Lo que estábamos hablando ahorita. Lo de, ya estoy en mensaje. Consolidar los mensajes en un módulo. Antes lo teníamos pues, dividido entre parents, admin, y coaches. Pues ya cuando, si lo tenemos todo en un mismo dominio, pues es más fácil Replacement seconds with real time. No importa. Coach, quick replies. Slash templates.
**Luis Torres**: No te escucho.
**Cristian Berrío**: Dame un segundo. No, sí está abriendo. Coach app. Offline, Oh, mira lo que te estaba diciendo. Offline, attendance. Gym and courts, often have connectivity. But attendants are safe to the cloud
**Luis Torres**: Amo. Amo cluck.
**Cristian Berrío**: Hello, good. Coach This is missing input at my experience. Per student skill making during So, no sé qué se refiere. Session notes, slash practice plan type to curriculum. Make sure it's in the status. I know, reach your attendance is que pongamos estados en vez de sí o no vino, enforce, data, scope via, security. Y esto es mejorar la seguridad de la base de datos. Admin dashboard, unified communication model, Instead of relay address.
**Luis Torres**: Crees? ¿Que lo del offline es posible? Loquito?
**Cristian Berrío**: Lo de mandar el Yo creo que sí. Pero, bueno, no sé. Será o sea, no entiendo cómo se haría. Si él lo dio es porque lo sabe hacer, eso lo tengo claro. Si lo mencionó, él él verá cómo lo resuelve, pero yo creo que sí. Que lo marquen, en offline, y y cuando tengan conexión eventualmente, se envíe solo. Raro eso, pero yo creo que sí se puede. ¿Y sí no? Y si no, también voy a implementar lo de ¿Lo de qué? Si no, también voy a implementar lo de lo del session, que no que no existe.
**Luis Torres**: ¿A qué te esperas, Juan, no?
**Cristian Berrío**: Que no no se le expire la sesión o no lo saque. Que hace login.
**Luis Torres**: Oh, exacto.
**Cristian Berrío**: Espérate. Great. Consolidate email delivery. Sending is Split across Gmail marketing Ok, bueno, no importa. Business and operational analytics, are traffic only visitors. The business needs revenue, enrollments, I want to touch out. Crearte una parte de analítica, tipo revenue enrollments by seasons, sports, school, para que tengas como que eso. Retention, ¿de cuántos padres se inscriben constantemente, cuáles son nuevos. Cuáles están yendo. Interesante como hacer cositas. Está interesante. Program builder updates. Crear templates. Raro. No entiendo cómo eso mejoraría, pero ahí está. Session templates. Con así, ah, bueno, mentira. Para para evitarnos la locura de de hacerlo uno por uno, aquí dice, clonar una season completa. Pero habría que ver cómo eso mejora. Cambiar la fecha, realmente. Bueno, me parece tan óptimo. Pero ahí está. Polish AI logo and roster tools. They need to be non broken. Automation integration. Bueno, ¿qué había mejorado? Fixed broken and duplicate automation. Se había arreglado. Importante. Y de policía, retries for all web. Que no se ejecuta tres veces. Define go to the level rows. No importa. The call base multibrand SMS drafting Error tracking Were there email integration or help Like, some migration. Okay. Robusto. Ya terminé. Hay bastantes cosas que se pueden mejorar slash cambiar.
**Luis Torres**: ¿Piensa que tiene un punto de de partida?
**Cristian Berrío**: No, tengo un punto de partida en inicio, Tengo un punto de partida, y un punto de de de final. O sea, ya más de ella no necesito.
**Luis Torres**: Excelente. Me alegro por eso, hermano. Me parece que estamos en sintonía, alineamiento, y perfecta preparación. Continuamos con el proyecto. ¿Tienes por dónde cortar? Conectas a MCP. Prepárate para trabajar la la base de datos. Construir infraestructura, Primero saca, o sea, del reporte que te mandé saca los puntos que sí vas a tocar, para que tengas como que pendientes, como que no no esperes que sacarlos de tu cabeza ya, Te recomiendo que crees un plan de trabajo con los puntos que vas a incorporar que son nuevos, en base a lo que acabas de leer, puedes sacar las cosas de este transcript de de ClickUp también, puede ayudarte en identificar qué tipo de cosas necesitas extraer. Con ese transcript, ya puedes aterrizar los pendientes que vas a cambiar. Y nada, también te dejo otro mensaje dentro de ClickUp, que, básicamente, es la primera auditoría que mandé, que no me gustó, y luego mandé un segundo flujo que mandé con mucho más contexto, que me terminó dando la información que te mandé. Así que igual puedes utilizar primer output como como referencia. Creo que bastantes cosas son lo mismo, pero otros puntos a la mesa que no están mal, no están tan detallados como como el como el road map que te mandé ahorita.
**Cristian Berrío**: Correcto. Es el propio.
**Luis Torres**: Yes. ¿Qué más? Listos? ¿Vas a estar listo para hablar con todo?
**Cristian Berrío**: Yes, sir. Yes, sir. Yes, sir.
**Luis Torres**: Te dejé un screenshot de donde te dejé la información para el invoice. La información de la compañía, ¿ok?
**Cristian Berrío**: Invoice. Okay?
**Luis Torres**: Para
**Cristian Berrío**: Ah, yeah. Yeah.
**Luis Torres**: incluyas la información de la compañía dentro del invoice.
**Cristian Berrío**: Okay. Estamos claros, estoy Oh, ya con eso que mandaste al HTML, ya la tengo más clara. Ya es como que solo es mirar Incluso, hasta lo diste en fases y todo. Interesante eso. Pero bueno, ya ahí vamos, vamos viendo, vamos bien. Ya lo tengo más claro. Pero, bueno, hoy es día de migración, pues. Día de migración.
**Luis Torres**: Correcto. Ya, migración, ¿tratemos de tener algo chévere hoy? Para poder revisar el fin de semana y planificar para la semana que viene, ¿te parece? Dale,
**Cristian Berrío**: Me parece. Bueno.
**Luis Torres**: estamos ahora mismo. Hi there, this is Louis speaking. How can I help you? Hello?

_Sincronizado por Brain: 2026-10-17T18:50:32.178Z_
