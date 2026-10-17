---
brain_note_id: "dest:meetings:0d28ad69d7724e4873af150835617647"
canonical_key: "meetings/0d28ad69d7724e4873af150835617647"
brand_id: "meetings"
---
# Transcript — 2026-06-18 SyncUp Dev (21317)

## Transcript

- Reunión: [[02-Meetings/2026-06-18 SyncUp Dev (21317)]]
- Parte 1 de 2
- Siguiente: [[02-Meetings/Transcripts/2026-06-18 SyncUp Dev (21317) - Transcript (Parte 2)]]

**Luis Torres**: Hermano,
**Cristian Berrío**: Amo amo, amo.
**Luis Torres**: tú.
**Cristian Berrío**: Excelente. Excelente.
**Luis Torres**: Ve que tenemos un veo que tenemos un veredicto
**Cristian Berrío**: Veredicto literalmente dijo, vuélvelo a hacer. Literalmente, es inviable migrarlo.
**Luis Torres**: Okay.
**Cristian Berrío**: Y ya de por sí es inviable directamente no se puede.
**Luis Torres**: Correcto.
**Cristian Berrío**: Tendríamos arroz con mango, ¿Que Cloud podría resolver? Sí. Pero a ese punto, y con la complejidad que Doctor es literalmente mejor hacerlo de cero.
**Luis Torres**: Mhmm. Esto es un proyecto más o menos de de de que que de que Calabrio cuánto estamos hablando.
**Cristian Berrío**: No, es que el día el día es más fácil que hoy vi. Sinceramente.
**Luis Torres**: ¿Sí?
**Cristian Berrío**: Sí, cien por ciento. O sea, el website front end, no, me demoró me demoraría como un día. Dos días. Bueno, un día, si ya tengo todo, y que tú me des masticadito, literalmente, o, bueno, dejarlo como ya lo tenemos, con las las mismas secciones, los mismos todos, obviamente, mejorar toda la parte visual, Pero con los mismos assets, mismo todo, yo diría que un día, dos días. Un, perdón, un día solo la parte del fraude.
**Luis Torres**: Pregunto, ¿sería posible que me dejes en documentos lo que tenemos actualmente en diferentes espacios? Para repensar y replantear algunas cosas. Por ejemplo, el dashboard de papás, dashboard de de coaches, como funciona, etcétera.
**Cristian Berrío**: Esa esa esa sería lo único, lo único sospechoso raro, es que, bueno, nosotros tenemos tres tres tres proyectos uno para el dashboard, otro para el programa y otro para coaches.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Y tienen tres rutas distintas, o sea, no es como un slash ruta, padre, sino que tienen literalmente todo el dominio distinto.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Entonces, bueno, no sé si por temas de practicidad, podríamos ponerlo todo en una ruta. O sea, todo el mismo discipline brief punto com, y le ponemos slash staff, slash admin,
**Luis Torres**: Mhmm.
**Cristian Berrío**: slash admin para
**Luis Torres**: Creo que podemos comenzar por ahí. Estoy de acuerdo.
**Cristian Berrío**: Sí, o sea, como que unificamos los tres los tres proyectos en
**Luis Torres**: Correcto.
**Cristian Berrío**: Bueno, realmente, diría que demorar son los dashboards. Bueno, el de padre, sobre todo.
**Luis Torres**: ¿Cómo así?
**Cristian Berrío**: O sea, el dashboard de padres demoraría.
**Luis Torres**: Ok.
**Cristian Berrío**: El de de perdón, el dashboard de administrador. Es el que más demoraría porque es el que tiene más más cosas. Y más funciones y más Bueno, mentira, en verdad, es un proyecto bastante... O sea, flooring no demoraría, pero siento que lo que más demoraría serían las funciones internas. Que tenemos.
**Luis Torres**: Como los correos electrónicos,
**Cristian Berrío**: Son bastantes. Y lo de mirar la base de datos también sería No, mentira, estamos hablando de un proyecto bastante grande. Nada más mirando la base de datos y las funciones que tenemos. Sí demora su tiempito. Migrarlo todo, Y, sobre todo, mirarlo todo que no se nos escape nada. Porque esa es otra. Porque hay cosas que no no hay cosas que Cloud no me va a decir, que están en su país. Sí. O sea, hay cosas que el cloud no va decir que están en su entonces, cosas que yo tengo que darme cuenta mirando. O buscando. Bueno, y también hay que pasar todos los los logos, ahí, crear una carpeta.
**Luis Torres**: Agriequicos.
**Cristian Berrío**: Sí, abrir los... Ey, hablando de eso, no hemos no hemos tenido la reunión de abrir los equipos nuevos. Equipos que aún no están.
**Luis Torres**: Imagínate, ¿para qué vamos a hacer eso si vamos a mover el proyecto? Por eso es que estoy pensando mover el el proyecto de ahora hacia adelante, porque si vamos a hacerlo nuevo, cambiarlo todo ahorita antes de que las registraciones empiecen a llegar, Las registraciones se supone que empiezan a llegar ahorita cerca del primero de julio.
**Cristian Berrío**: No, yo yo creo que me demora que te quede todo y probemos y nos dé tiempo de por de probar que todo está bien, como a sus cuatro días. Tres días. Imagínate que
**Luis Torres**: Mira, esto, fíjate de esta estructura, Mira, aquí estoy poniendo la planificación de el website, tenemos front end, coaches, parents, admin, emails, messages. ¿Qué más necesitamos?
**Cristian Berrío**: Yeah.
**Luis Torres**: Estos serían los dashboards. Coaches, parents, admin, email messages. Y ya. Dentro de emails tenemos tenemos diferentes tipos de correos, tenemos correos de Tenemos correos de de semanas, weekly, Tenemos unos correos de
**Cristian Berrío**: Reminders, the de temporada. De que inicia la sisa. Tenemos el de assistance. Coach assistance reminders.
**Luis Torres**: ¿Cómo así?
**Cristian Berrío**: Cuando el coach no llena cuando el coach no llena el el assistance.
**Luis Torres**: Bueno, entonces podríamos poner estos correos aquí poner estos subdocumentos dentro de su espacio. ¿Qué te aparece esa estructura? Dentro de metemos aquí emails, y en este correo aquí ponemos
**Cristian Berrío**: Pero, o sea, eso eso es de en ocho n. Lo podemos lo podemos categorizar aún más. Porque, realmente, todos los correos de reminders de season weekly, cuando el el estudiante no asista al parent reminders, el coach reminders, todo eso es en HM.
**Luis Torres**: ¿Podemos quitar eso de una, Chavane?
**Cristian Berrío**: ¿Dónde lo quieres poner? En
**Luis Torres**: ¿Que se encojan algo así?
**Cristian Berrío**: Sí.
**Luis Torres**: Ya que están llamando de Edgar. Hi there. This is Lou speaking. How can I help you? This is Ben Reft. Ah, Hi. This is Shaunei Daniels calling for me. I called and spoke with someone last week, and I wanted to try to schedule a time, to have you all come out to meet with myself. The principal, and the head of schools at Hope. To talk about the program and bringing it to us. School. Absolutely. Absolutely. Let me let me go ahead and pull up your the our conversations. You said we're you're calling from Hope Preparatory. Correct? Hope Preparatory Academy. Yes, sir. Perfect. Sounds good. One second. And you are bum bum bum. Are you we sent that email to Totem at go hope academy. Is that correct? I'm I'm Charnay. Nice to meet you, Charnay. I'm Luis Torres. Perfect. So I will go ahead and send you an email with a time that works. At what time do you want to meet next week? Any any Tuesday, Wednesday, or Thursday next week, maybe after ten o'clock. Perfect. So let's Tuesday, Wednesday, Thursday, you said? Either of those days. Yes, sir. Perfect. So I think Thursday works best for for us I can probably bring my director of operations. My name is Luis Torres. I'm the founder. Of Disciplined Rift. He's probably the one that reached out. Mhmm. So let me just go ahead and add you here. So okay. I see you're here. Let me just create a an appointment here with you guys. Perfect. So let's do Thursday. You said after ten? Yes. After ten o'clock would be great. Perfect. Sounds good. Let's go ahead and make sure I can put that here. Maybe eleven AM works I think eleven AM will work best. So I'll go ahead and put you guys here for eleven AM. Would you like us to meet in person there with your team? That'll be great. Perfect. Let's do it. I I like in person anyways, I think. Online remote meetings are are overrated at this point. Mhmm. For sure. Perfect. So I'll go ahead and, put you guys here. I'll also send an email kinda follow-up, and we'll see you guys next Thursday at eleven AM. Luis, let me give you my updated email. It's changed. It's s as in Sam, l as in love, Daniel at Go Hope Academy dot o r g. Perfect. I think I have you here. So s l Daniels with an s at the end, Yeah. And then the domain for the school. Perfect. Sounds good. Mhmm. Yeah. I'll go ahead and do you want me to reply to both emails or just that new one? The new one would be great. Perfect. I'll reply to that new one. And, hopefully, you can get that info from me. Sounds good. Thank you, Louise. Anytime. Thank you, miss Shirley. Take care. Uh-huh. Bye bye. Everyone. Bye. Amazing.
**Cristian Berrío**: Yep.
**Luis Torres**: Amazing. Ese trabajo que ahorita estamos ya sin ¿Te acuerdas de las escuelas que todavía ha sido el scraper que le metí? Esta escuela está fire. Go home preparatory academy. Tampa,
**Cristian Berrío**: Está en pasta leídos.
**Luis Torres**: ¿Qué locura es esto, Cris? Ver, Bueno, pero llámeme para allá, pues. Ok, ok, no se está mal.
**Cristian Berrío**: No está Leo, está ahí mismo.
**Luis Torres**: Sí, vale, no está, nosotros tenemos otra
**Cristian Berrío**: Te sale se sale un poquitico, Orlando.
**Luis Torres**: Sí, se sale un poquito de verdad, no está tan mal. No, tampa es, tampa es esto aquí. Tampas acá. No, los toman, los toman, los toman. Porque creo que es el el esto que está mal, school en Tampa. Eso no es verdad.
**Cristian Berrío**: Se ve se ve privada. Se ve privada la la la academia esa.
**Luis Torres**: Sí, sí, privado. A ver, a ver, a ver. They called in Hey, brother. They called in to schedule an appointment to meet with them in person next Thursday at eleven AM. I will be meeting with them Hopefully, you can join as well depending on how busy we are with everything else. Can you please send them a follow-up email telling them that thank you for appreciate talking to you earlier, whatever. We'll go ahead and see you guys next Thursday at eleven AM Also, please mark the appointment on our calendar on on our Google Calendar, so I can untag my self in it so I can put it in my calendar right away. Ya estamos aquí de vuelta.
**Cristian Berrío**: Okay.
**Luis Torres**: Ok. Ok, volvamos a nuestro tema de conversación. Front end coaches, parents, admin. Dentro de emails, reminders weekly, Ok, emails, aquí tenemos reminders, tenemos weekly emails y también tenemos... Ya, eso es todo, ¿cierto? O, bueno,
**Cristian Berrío**: Le coach reminders. Parent reminders, para cuando no vayan a la práctica los niños. O sea, ¿y reminders de de season? Reminders, Ajá. De de parents, cuando no van los niños. Y ya. Bueno, y lo el correo que mandamos, de cuando llenan el pop up lead, el de confirmación, y ya.
**Luis Torres**: His reminders.
**Cristian Berrío**: Compare reminders. Okay. Exact. Popublitz. Los correos que se le envían. ¿Qué otro?
**Luis Torres**: No está
**Cristian Berrío**: Con la confirmación de pago. Ya. Sí, ya, eso sería todo. Eso sería todo.
**Luis Torres**: Excelente. Y esto le vamos a poner, messages. ¿Qué te parece?
**Cristian Berrío**: Organizado, organizado, Ok, está en Doctor. Website. Okay. Perfecto, me parece. Y ahí meto la información, digamos, features, que tiene cada cosa.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Cada apartado.
**Luis Torres**: Así es.
**Cristian Berrío**: Ok. Sí.
**Luis Torres**: Toda la todo el toda la información absolutamente completa. Lo de los emails y eso, creo que lo tenemos dentro de algún folder de acá adentro. Ah, mira, sí,
**Cristian Berrío**: Bueno, falta falta otro. Crea otro otro documento que se llame
**Luis Torres**: Base de datos. O, bueno. Mejor así. Tal?
**Cristian Berrío**: Ok, aquí habla de messages.
**Luis Torres**: Tipo mensajes de así como van así como hay, y cadena de emails, hay cadena mensajes. O la la el orden que tenemos en OV me gusta más, revisemos eso rapidito. Software, notifications. ¿Qué te parece esta esta cadena mejor? Booking,
**Cristian Berrío**: A mí me a mí me gusta la tabla. La tabla me da me da bastante perspectiva, no, totalmente.
**Luis Torres**: Sí, me gusta más esta tabla también. Ok, entonces,
**Cristian Berrío**: Si no scroll down, scroll up. Para ver qué se manda.
**Luis Torres**: Exacto. Vámonos a website. Tenemos demasiado, tengo que organizar muy desorganizado. Ok, entonces hagamos esto. Notifications. Notifications. Vamos a ponerle a este registration. Error iteration. Season, Registration es todo lo que ellos tienen más,
**Cristian Berrío**: ¿Cuándo cuándo crees tú que Ah, bueno, mentira, tú me dijiste que ahorita está frenado.
**Luis Torres**: qué?
**Cristian Berrío**: El lo del space.
**Luis Torres**: ¿Qué
**Cristian Berrío**: Porque es que siento que siento que, o sea, siento que necesito resolver as soon as possible, lo de pago.
**Luis Torres**: ¿Por qué lo dices?
**Cristian Berrío**: O sea, literalmente estaba haciendo lo que me dijiste de que falta dependientes.
**Luis Torres**: Ajá.
**Cristian Berrío**: Y listo. Literalmente, el output que me dio cloud es, literalmente, primero resuelve el arroz con mango que tienes en lo de los pagos. Porque no no tengo ni idea si funciona. Entonces, literalmente, Cloud está está funcionando y no puede hacer test, y está funcionando a ciega, está funcionando literalmente, no sabe no tiene conocimiento de las otras cuentas, entonces, como que yo le digo, que, ajá, como que yo yo le voy a poner después la las y las credenciales de de lo otro, pero o sea, es como si estuviera trabajando a ciegas, no no puede ver, no puede testear. Conexiones ni nada, simplemente está haciendo lo que pues, ya hicimos en ODB,
**Luis Torres**: Mhmm.
**Cristian Berrío**: lo que tenemos hecho. Lo está adaptando a a lo a los tres enrutamientos que vamos a hacer.
**Luis Torres**: Mhmm. Bueno, si no, si quieres te si quieres hacerlo en un sandbox, de Stripe y luego como que cambiar, o sea, eso tiene que ser específico en la cuenta de Stripe. Digamos que si utilizamos una cuenta de Stripe que creemos hoy, y luego la cambiamos, vamos a tener que hacerlo desde cero, ¿cierto?
**Cristian Berrío**: Exacto. O sea, no nos sirve hacerlo desde troberos o desde lo que sea. Porque igual,
**Luis Torres**: De la de la cuenta como tal.
**Cristian Berrío**: Exacto, porque recuerda que hay que hacer una configuración
**Luis Torres**: Correcto.
**Cristian Berrío**: como yo hice en ODB. Que tengo que ponerlo en Strip Connect y y conectar las cuentas.
**Luis Torres**: Correcto. Bueno,
**Cristian Berrío**: Entonces, Entre más rápido nos movamos con con Stripe, más rápido podemos ver con lo otro. Sea, yo puedo seguir haciendo lo otro, siempre va a quedar hueco. Y, por ejemplo, lo que falta ahorita son, tipo, invoices, y uno que otro feature, así como pendejo de analítica, sea, cosas así muy chiquitas, lo que si es reports, que si cosas así. Que, por cierto, o sea, reports, también necesitaría Stripe porque, me imagino, como vamos a enrutar varias cosas, no sé si quieres que lo divida, tipo, mira, un porcentaje de la ganancia se fue a esto. En reports, o simplemente hago reports globales de cuánta plata nos entró y qué nos entró de cada cosa.
**Luis Torres**: Mhmm.
**Cristian Berrío**: No sé no sé si quieras específico así, tipo, nos entraron mil dólares el el ocho por ciento de cleaning fee si fue a esta cuenta, el veinte por ciento del depósitos, fue a esta cuenta? O sea, como que sí.
**Luis Torres**: No, no, Tú, en la parte de reportes de de Dispatch, ¿es esto? Fíjate que
**Cristian Berrío**: Ajá. O sea, la parte de reports es de de toda la plata que una compra.
**Luis Torres**: fíjate que tú puedes hacer esto en desde ese desde ese lado. Yo te puedo meter aquí en Stripe, meterte en transferencias, en transacciones, La transfers y tú puedes buscar cualquier transferencia te vas a la a la transferencia madre, al pago madre, digo, al source, da la transacción del source, calculas en vez de esto. Digamos que si por si por esto estamos cobrando veinte por ciento, lo puedes calcular todo a mano. Pero tú dices que tú puedes incorporar en la área de reportes un área donde le pueda decir cuáles fueron las transferencias y cómo se calculó.
**Cristian Berrío**: Sí, o sea, sí, o sea, realmente, eso se puede porque, como te digo, realmente son las extraites, eso lo hacemos nosotros. Stripe solo sirve de cartera. Y ya. Pero realmente todo eso lo hacemos nosotros. Entonces, el área de reportes tenemos ahorita en OIB, que es lo que entra, ¿qué nosotros, en AIB, tenemos ahorita tipo, información de cuándo se hizo el pago, y lo tenemos dividido en baseline cleaning production, si es por adicional, bar fees, etcétera.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Lo tenemos así segmentado. Pero no tenemos el ochenta veinte, o sea, es como si el cien por ciento de toda esa transacción hubiera ido hoy día. Entonces, yo lo que te digo es, segmentarlo por sea, para llevar un reporte más detallado, de este porcentaje se fue a tal cuenta. Este porcentaje se fue a a tal cuenta. O sea, como que tener o dividir eso,
**Luis Torres**: Sí.
**Cristian Berrío**: para que quede como detallado. De qué es lo que va acá con
**Luis Torres**: Sí, podemos hacer un apartado que se llame payouts para eso.
**Cristian Berrío**: Ok.
**Luis Torres**: Deberíamos tenerlo en el dashboard. Un un apartado de payouts, que muestre transacción y los payouts que se mandan a a a
**Cristian Berrío**: Correcto.
**Luis Torres**: que que vendría siendo toberos, como cuenta Strike.
**Cristian Berrío**: Exacto. Entonces, para hacer todo eso, necesito que el apartado de de dinero esté terminado. Porque ahorita mismo, o sea, literalmente lo que falta es eso. Bueno, puedo ir haciendo lo de inventario, lo del descuento, si usan descuento. No sé si aplican descuentos aquí. Puedo hacer analítica, de de cuando la gente llena el pop up lead, ¿de cuántas de cuántas gente bookea de esos pop up leads que llena?
**Luis Torres**: Mhmm.
**Cristian Berrío**: Mismo nosotros, de cada ciento sesenta, personas que llenan el coso ese, cuatro están Entonces, me parece un buen un buen conversion rate, no, solamente. Dos punto cinco por ciento.
**Luis Torres**: ¿Y cuántas personas lo llenan al mes?
**Cristian Berrío**: Bastante. Bueno, tú no sé si tú tú miras el apartado analíticas, pero ese apartado analíticas es bastante jugoso, no te voy a mentir. Bastante detallado.
**Luis Torres**: A ver.
**Cristian Berrío**: Mira analítica. Y, mira, abajo salen los correos que se le envían.
**Luis Torres**: Los mensajes de texto?
**Cristian Berrío**: Eso es, recuerda que nosotros mandamos eso. Eso lo manda
**Luis Torres**: Go ahead, though.
**Cristian Berrío**: Sí.
**Luis Torres**: Nosotros sí mandamos los correos de los pop ups.
**Cristian Berrío**: Correcto.
**Luis Torres**: ¿Por qué decidiste hacerlo así?
**Cristian Berrío**: Recuerda que nosotros no tenemos SMS, SMS no podemos mandar. Solo vos high level. Entonces, cada vez que captura, cada vez que llenan un lead, una persona nueva, se van a, o sea, se, primero se crea el contacto en Goji Level, si ya está creado. Si no está creado, pues pues lo crea. Y enseguida entra la automatización. De que se le envía el SMS espera x tiempo, no me acuerdo cuánto es que era,
**Luis Torres**: Y se manda el correo.
**Cristian Berrío**: y se le envía el otro Pero eso no lo puedo manejar, no lo puedo Lo que puedo es eso. Los correos. Mira, ese, le mandamos un correo a
**Luis Torres**: Mhmm.
**Cristian Berrío**: Entonces, analítica, poco se habla de de que está está interesante, no te voy mentir.
**Luis Torres**: Superinteresante. Lead overtime, aquí están todos los leads. Ah, mira, esto es un all time. De todo esto es un all time de los leads.
**Cristian Berrío**: Ciento sesenta.
**Luis Torres**: Sí. ¿Has revisado los ads de Google Ads?
**Cristian Berrío**: Eso estaba ahora. También.
**Luis Torres**: ¿Qué tal?
**Cristian Berrío**: Subimos subimos el ¿Cómo que se llama eso? El ¿Cómo se llama eso?, como el puntaje, el A ver cómo se llama exactamente. Como el puntaje de los ads. Como bien lo subimos. Y las y las keywords, los search terms, están siendo bastante acorde nuestro venue. Ejemplo, los más buscados, ya no hay tantas locuras. Ayer, por lo menos, me di la tarea de mirarlo por encimita, porque siguen siendo bastantes. Siguen siendo dos mil dos mil setecientos setenta y cuatro palabras.
**Luis Torres**: Demasiado.
**Cristian Berrío**: Pero las que se están cliqueando por la más importante, sí están acorde.
**Luis Torres**: Aquí estoy viendo, sí. Porque tenemos impresiones aquí. En
**Cristian Berrío**: ¿Y dónde está?
**Luis Torres**: Interesante.
**Cristian Berrío**: Insights? Ah, bueno, me saltó una alerta de limited budget, pero
**Luis Torres**: ¿Cómo así?
**Cristian Berrío**: Aquí le subamos. Dije lo el budget a a los ads.
**Luis Torres**: ¿Quiere que gastemos más dinero?
**Cristian Berrío**: Literalmente, ya que ya tenemos más dinero. Y el más recomendado,
**Luis Torres**: ¿Verdad? Venerable a los budgets.
**Cristian Berrío**: A mí me recomiendas cincuenta y siete por cincuenta y siete.
**Luis Torres**: No, no, no, no, era era diciéndolo como que en teoría. ¿Cuánto hemos gastado? So far? En esta campaña que acabamos de lanzar?
**Cristian Berrío**: There you go.
**Luis Torres**: ¿Cómo sacó ese cómo sacó ese reporte aquí? En mi pantalla?
**Cristian Berrío**: Ya te digo, Bueno, ya se nos acabó. En mayo, sí, estamos a mayo. No, ¿tú cuándo lo lanzamos?
**Luis Torres**: Acuérdate que el parto lo nosotros pagamos como un buen dinero cash, tenemos la promoción. Creo.
**Cristian Berrío**: Spend doscientos treinta y nueve. Y del crédito nos quedan dos dólares.
**Luis Torres**: Del crédito nos queda en dólares.
**Cristian Berrío**: Sí. En
**Luis Torres**: ¿Dónde veo eso, hermano?
**Cristian Berrío**: en billing summary.
**Luis Torres**: Locura es esa.
**Cristian Berrío**: Ya nos gastamos los doscientos treinta y nueve dólares.
**Luis Torres**: Nosotros teníamos
**Cristian Berrío**: Bueno, doscientos cuarenta en campaña.
**Luis Torres**: nosotros teníamos quinientos dólares en en créditos.
**Cristian Berrío**: Ahí se le quedan doscientos doscientos cuarenta y uno con treinta y cuatro centavos en crédito. Con el promotion code. Ah, no, mentira. No, mentira, sí, fueron quinientos. Me salen dizque ¿Qué?
**Luis Torres**: No entiendo esto.
**Cristian Berrío**: Me sale.
**Luis Torres**: Spend, como no han estado doscientos cuarenta, ¿desde cuándo?
**Cristian Berrío**: Desde junio.
**Luis Torres**: Ya nos hemos gastado doscientos cuarenta dólares y lanzamos la campaña en una, la semana pasada. Estamos gastando diecisiete dólares por el día. Esos números no dan.
**Cristian Berrío**: Bueno. Sí,
**Luis Torres**: Hermano, diecisiete dólares por dos semanas son doscientos dólares. Dos, ¿cuándo cuándo le hacemos la campaña? Mira, aquí sale. Doscientos cincuenta y ocho remaining,
**Cristian Berrío**: ¿Dónde sales?
**Luis Torres**: Okay. En June current month.
**Cristian Berrío**: Porque sale que
**Luis Torres**: Sí, que nos faltan
**Cristian Berrío**: porque sale current credit balance dos dólares con cincuenta.
**Luis Torres**: Current credit balance
**Cristian Berrío**: Abajito. Dólares con cincuenta.
**Luis Torres**: Porque un overpayment fíjate que la promoción aplicó doscientos cuarenta y uno y teníamos un adjustment de uno sesenta y nueve.
**Cristian Berrío**: Mhmm.
**Luis Torres**: Over delivery. Entonces, el costo total fueron como doscientos treinta y ocho, algo algo así. Y pagamos más. De lo necesario. Crédito de dos punto cincuenta, pero nos faltan doscientos cincuenta y ocho de la promoción.
**Cristian Berrío**: Okay.
**Luis Torres**: De esta promoción. Tenemos un crédito de dos punto cincuenta. ¿Qué te parece?
**Cristian Berrío**: Parece curioso, estoy aprendiendo Pero ¿por qué sale?
**Luis Torres**: ¿Qué cosa? Promotions, view promotions, aquí está. Cuando me voy a promociones, get a five hundred credit, pum, pum, pum, pum, aquí te aparece. Credit spent, hemos gastado cuarenta y ocho por ciento del crédito. Ahora, mi pregunta es, ¿cómo yo veo el breakdown de por qué nos están cobrando esto este mes? Porque en mayo tuvimos nuestros ads Ahorita en junio, esto es
**Cristian Berrío**: I mean, again, le suba en el... Ajá, ya, mira, mira. Mira, mira. ¿Ves ya a overview?
**Luis Torres**: Donde
**Cristian Berrío**: En campaigns. Campaigns, izquierda. No, Campaigns. Overview, edita el la fecha. Derecha, custom. Custom, a la derecha, derecha, ahí. No. Custom abajo. Bajito. Ahí. Pon junio. O sea, selecciona solo junio. Dale,
**Luis Torres**: Creo que tenemos que hacer esto para para para visualizar la campaña, creo que
**Cristian Berrío**: ya ya lo acabo de ver, mira. Y ahora vete al al chart que sale abajito.
**Luis Torres**: ¿Al qué?
**Cristian Berrío**: Ahí al al de la las líneas esas.
**Luis Torres**: Es el?
**Cristian Berrío**: El chart que ves arriba o arribita. El gráfico ese que ves ahí, de líneas.
**Luis Torres**: Ok, ok, ok.
**Cristian Berrío**: Ah, pero que no te sale. Ah, pon cost. Mira, veintitrés con ochenta y ocho. Pasa a la derecha. Diecisiete y diecinueve, treinta y cuatro,
**Luis Torres**: No, no, estamos gastando más dinero diario.
**Cristian Berrío**: Sí, mirá que el costo.
**Luis Torres**: Y nuestros budgets, ¿cuál es? ¿De siete dólares todavía?
**Cristian Berrío**: Sí, nuestro budget está está ahorita en diecisiete.
**Luis Torres**: Pero a esta gente no le importa nuestro budget, Lo que lo que podemos decirle después, mira,
**Cristian Berrío**: Mira, literalmente, mira cómo, o sea, mira cómo se gasta. Que preguntar,
**Luis Torres**: Mira, lo lo podemos pedir es un refund. Mira, te gastaste todo el buyer, sin autorización. Un refund. Con razón, ¿qué le quedaste, mamá? Quieren que quieren darle más dinero a nuestro ad.
**Cristian Berrío**: No, porque es que ideas ideas con un flujo específico, y eso y eso hace parte de lo que días que digamos, hay gente que que que que ingresa más al website. No sé cómo lo tratan ellos, pero hay hay días de flujo mayor de de clientes, una cosa así. Entonces, esos días, ellos le suben al budget para que nuestro website tenga mayor visibilidad, si te das cuenta, los días que han subido, el budget, esos días hemos tenido muchísima más impresión.
**Luis Torres**: Claro. Ellos lo hacen automático.
**Cristian Berrío**: Exacto, eso
**Luis Torres**: Pero igual podemos pedirle un refund por Khan Nosotros no les pedimos.
**Cristian Berrío**: o sea, eso eso como que lo hace automático,
**Luis Torres**: Sí.
**Cristian Berrío**: la plataforma, pero pero está sospechoso eso, totalmente.
**Luis Torres**: Mhmm. Mira, aquí estoy bajando, el Excel de las locaciones del ad. Fíjate que el ad actualmente, está subiendo hasta Eusty's, Orange City, Deltona, y acá lo que que no queremos donde que salga el ad ¿Me entiendes?
**Cristian Berrío**: Sì, eso lo podemos cambiar, ¿sabes?
**Luis Torres**: Sí, aquí dice, exclude locations. Aquí vamos a vamos a meterle locaciones vamos a excluir locaciones, y las targeted van a ser algunas de estas. Entonces, lo que vamos a hacer es yo aquí descargué el el un Excel, ¿Dónde está mi Excel?
**Cristian Berrío**: Sí, porque el la, cuando yo tuve la reunión, con la persona, yo lo había seleccionado, pequeñas partes de Orlando, pero la la la la la que me la que me ayudó me dijo que es mejor si es por radio, no por
**Luis Torres**: ¿Cómo por radio?
**Cristian Berrío**: O sea, en vez de coger uno por uno, tipo partes de Orlando, o secciones de Orlando, hacerlo por radio. Y, digamos, el un radio no sé, de no sé cuántos kilómetros va, les va a salir a esas personas.
**Luis Torres**: Oh, ¿me va dar hacerlo por live, entonces?
**Cristian Berrío**: O sea, me dijo que me van a hacerlo por radio, que poner exclusivamente uno por uno las lo que la localización. Obviamente, si tú consideras como como porque tú tienes más experiencia, obviamente ella no sabe, pero si tú consideras que es más factible, que en ciertas zonas le aparezca mucha más, o sea, le aparezcan los ads a más personas de esa zona específico, pues lo podemos hacer. Pero eso ya es como lógica negocio. So,
**Luis Torres**: Sí. El, sí, eso, sí, estoy de acuerdo, esa gente no, ya en ese ese tema ahí se poncharon. Mira lo que vamos a hacer,
**Cristian Berrío**: So
**Luis Torres**: perplexity, nos ayuda con esto. O tenemos también al pendiente del de lo que está sucediendo con GoHad Debo. Por alguna razón, Sebastián, no le llegan las llamadas, hermano. No sé qué pasa con eso.
**Cristian Berrío**: Creo que es porque no tiene o sea, no está asociado al teléfono. Por ejemplo, a ti la llamaste, Jean, a ti nada más. El tiempo usuario,
**Luis Torres**: No.
**Cristian Berrío**: ¿Cuál usuario cuál usuario está usando él? El toy.
**Luis Torres**: El del OEB, el mismo usuario de, bueno, sí, el mismo usuario que usamos todos de OEB,
**Cristian Berrío**: Ok, entonces, que esa es configuración del del teléfono de él.
**Luis Torres**: ser, hay que hay que
**Cristian Berrío**: Porque recuerda que a ti no te a ti no te llegaba. Pero es porque no la tienes configurado. Entonces,
**Luis Torres**: ¿Y cuál es la configuración?
**Cristian Berrío**: creo que, o sea, es como ¿Tú qué revisas? Porque no me acuerdo. Pero, o sea, es literalmente intuitivo, te das como a settings, y te dices como qué te aparece.
**Luis Torres**: I care.
**Cristian Berrío**: O sea, como que te aparecen notificaciones. Porque, o sea, sí le llegan las llamadas a él, pero solo le llegan si tiene el Google abierto. Pero no no le la notificación o le la llamada. Porque a ti también te pasaba lo mismo. Yo me acuerdo. Tiene que configurarlo. Pero si le llega a él, Y lo de que me dijiste que cuando sale como un mensajito de de oprime un botón para conectarte con alguien, Eso yo lo vi. Y según lo que dice perplexity, o sea, la la la configuración, un no está orientada a que aparezca eso. O sea, la opción es para que salga lo de, oprime el teléfono, y que, o sea, no no están configuradas para que sea de esa manera, entonces, o sé. Qué es lo que puede estar pasando ahí. Solo es con Doctor, Esa
**Luis Torres**: Solo es con D VAR. Sea, Gohan Level dentro de Doctor tiene tiene algún tipo de, no sé si es fíjate que yo a veces estoy metido en diferentes sub accounts en el teléfono. Sea, si tú abres la cuenta de en, o sea, yo tengo la cuenta de Trellis abierta,
**Cristian Berrío**: Mhmm.
**Luis Torres**: este, analyze the location report and rank locations. No. No. Nope. These are impressions based on Google Ads. Now I want you to launch your research tool and and, list the wealthiest ZIP codes out of the entire Excel sheet. Do not worry about the impressions. Column. Extra esa información. Yo voy a meter la cuenta de Trellis, y en la cuenta de Trellis yo tengo acceso a las tres sub accounts. Cuando yo voy a las configuraciones para activar las inbound calls, yo activo todos los overcounts que me lleguen las llamadas. Para Doctor, yo estoy, por ejemplo, en orden de venue y me llaman de Doctor, yo tengo que tocar un número de la tecla No, esto Tú, tengo tengo que meterme en Doctor, toclar una tecla, como que un número, darle un número para que me llegue la llamada. ¿Me entiendes?
**Cristian Berrío**: Qué raro. Per quanto ti chiamano a ti?
**Luis Torres**: Correcto.
**Cristian Berrío**: Y estás metido en otra sopa, Caro.
**Luis Torres**: Correcto.
**Cristian Berrío**: Qué raro.
**Luis Torres**: Cuando me llaman a, cuando cuando cuando llaman a cuando estoy, por ejemplo, en OID y llaman a Doctor, tengo que meter, tengo que atiendo la llamada y Guajaleón me dice la llamada, press any key to connect. Ahí le doy un número, ahí se y ahí se como que responde. Por ejemplo, si tú te metes ahorita, en es la manera en que yo hago pruebas. Yo me meto aquí en el en el voice de Doctor, llamo al número, ¿verdad?, llama al número de coja el logo de Doctor, y hice la prueba y sucedió lo mismo. Presione click to connect, presiono el key, y ahí sí se conecta, sin problema.
**Cristian Berrío**: Por eso, pero ese ese mensaje llega a ti o le llega al cliente. O sea,
**Luis Torres**: Ese mensaje
**Cristian Berrío**: Ajá.
**Luis Torres**: ese mensaje me llega a mí, a mí, a mí, a mí. Cuando cuando el cliente esté llamando.
**Cristian Berrío**: Y solo con
**Luis Torres**: ¿Solo con Doctor? Sí, no, porque sí, casi siempre estoy metido en el ojalá y hoy yo lo uso mucho para el teléfono para OID, porque llamo mucha gente.
**Cristian Berrío**: Claro.
**Luis Torres**: Que usted metió en el sofá acá donde goja, le voy. ¿Entiendes?
**Cristian Berrío**: Sí. Ok. Bueno, lo de lo de que Sebastián no no puede atender la llamada, ya sé que es es que no está conectado, porque nosotros tenemos la cuenta la cuenta de Luis Torres, es la de Trellis.
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Es la de admin que tiene acceso a todo.
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Pero la cuenta de creo que no tiene o sea, no está configurado para que le llegue el teléfono.
**Luis Torres**: Hay que, tienes que configurarlo.
**Cristian Berrío**: Ajá, OIB es una es como si fuera una persona. Entonces, a esa persona no tiene es que no es que tenga acceso, es que no le no le imputa la llamada hoy vi. Solo te en ruta la llamada a ti. A Trevis.
**Luis Torres**: ¿Qué pensarías que es mejor? ¿Crear una crear una cuenta de empleado a Sebastián? Porque nos
**Cristian Berrío**: No, o sea, o sea, realmente podemos usar, podemos decir que hoy vi le llegue sea, le llegue le le enrute las llamadas también. Le te route las
**Luis Torres**: El tema es que yo quiero trackear las llamadas que Sebastián responde él. ¿Me entiendes lo que te digo?
**Cristian Berrío**: And then
**Luis Torres**: Sea, porque yo necesito trackear, porque él él es, su income es como que él ayuda como asistente para llamadas que yo no puedo atender. ¿Cierto? Entonces, como que él él gana por comisión. Entonces, la idea es, que las llamadas que entren a OIB al número de OIB, se distribuyan entre el número de OIB, que yo lo uso, o sea, que a mí me llegan las llamadas de OIB directamente a mí, Oh, no, mentira, me llegan a mí de, a mí me llegan las llamadas porque yo estoy en la en la cuenta de del Torres, ¿cierto? Entonces, la idea sería que cuando... Ajá, porque ahorita se va a estar metido en la cuenta de OVB, podemos sacar a Sebastián fuera de la cuenta de como empleado de la sobaca donde OIB para que le lleguen las llamadas de OIB y poder la actividad que él tiene dentro de esa dentro de ese perfil
**Cristian Berrío**: Okay. Could I watch that?
**Luis Torres**: ¿Qué opinas tú?
**Cristian Berrío**: Sí, sí, sí posible, pero igual, o sea, la misma llamada, va a quedar a los dos.
**Luis Torres**: Eso es lo, esa eso sería ideal, tiene que caernos a todas al mismo tiempo, porque si él no responde, yo respondo, si él no responde, él responde. Y eso es algo eso es algo impredecible.
**Cristian Berrío**: Es que pensé que estabas diciendo que le caigan más llamadas a él que a ti, Ah, ok, ok.
**Luis Torres**: No, no, no, no, La idea es que nosotros nos apoyemos de una manera intercambiante. Cuando él no atiende, yo atiendo, cuando él atiende, yo atiendo, así.
**Cristian Berrío**: Okay. No, sí, eso se puede Y lo lo mejor sería así, que él me pase su correo, yo mandarle la la invitación, y que tenga acceso a la llamada, ahí traquee.
**Luis Torres**: Sí.
**Cristian Berrío**: Tú tienes el correo, por ahí.
**Luis Torres**: Fíjate que lo que voy a hacer es aquí voy a agarrar esta aquí,
**Cristian Berrío**: Corazón.
**Luis Torres**: Drive. Coaches, En este correo, este en este roster de coaches, voy a crear otro view para para los empleados, aquí mantengamos a en este sheet de roster, Cris, vamos a mantener a los empleados de OIB. A todo el staff, a, bueno, todos los empleados que tengan acceso a legal, sobre county y eso. Ahora vamos a tener a Jazmín y Sebastián.
**Cristian Berrío**: Okay.
**Luis Torres**: Que serían estos dos. ¿Lo ves?
**Cristian Berrío**: Pero ¿ha tenido ni modo acceso? Accesor
**Luis Torres**: Sí. Sí. Acceso a
**Cristian Berrío**: Okay. Pero
**Luis Torres**: a OEB y créame, otro para a ponerle esto aquí, voy a cambiarle el nombre a esto. Rename, Rochez, email, coaches, email para los coaches, aquí este sheet es mío interno, no le preste atención a eso. OIB para OIB, y Doctor es para el soba que ande Doctor. Para el equipo de de administración de Doctor. Ese sentido, Listo, hoy vi cosa el agua. Y esto es Doctor.
**Cristian Berrío**: Pásame el link aquí por el chat. Mandárselo enseguida.
**Luis Torres**: Excelente. Entonces, creémosle cuentas. El mismo empleado puede tener acceso a diferentes, o sea, dentro de cada super account tú lo que haces es crear una cuenta de de empleado. ¿Cómo funciona eso?
**Cristian Berrío**: O sea, no. Desde desde la agency, se crea el empleado.
**Luis Torres**: Desde Trellis,
**Cristian Berrío**: Sí, desde O de
**Luis Torres**: Ok. ¿Y qué sucede después de ahí?
**Cristian Berrío**: O mentira, espérate. Ah, no, es de caso account. Pero podemos crear una creo que lo puedo crear desde la agency view, de surgir la duda.
**Luis Torres**: O, bueno, porque Jacinto, bueno, está ayudando pero una posibilidad de que él ayude, pero en tal caso, Jacinto estaría dentro de Doctor y dentro de OIB.
**Cristian Berrío**: Ah, sí, mira, Ting, aquí está.
**Luis Torres**: Ver, muéstrame lo que está, muéstrame lo que estás haciendo.
**Cristian Berrío**: O sea, se puede crear Este es el agency view. Aquí no estoy metiendo ningún account. Se puede crear aquí cada usuario, o podemos ir a un soft account específico.
**Luis Torres**: Y esos usuarios del agency view les das, ellos tienen su propio login,
**Cristian Berrío**: Correcto, o sea, ajá, ellos ellos se lo veían con su con su propio correo. Sí, y aquí uno le puede poner los permisos de
**Luis Torres**: nosotros ahí tenemos a Pablo, el equipo de, el staff, por ejemplo, María Luisa, que le asignamos como custodio, ella puede escalarse la aplicación y ver su horario de la aplicación?
**Cristian Berrío**: Y mira, aquí tienen los permisos que tiene cada
**Luis Torres**: ¿El calendario de de custodia está conectado a esto?
**Cristian Berrío**: El calendario de custodia le está conectado a esto, sí. Pero mentira, creo que en su calendario creo que no lo puede ver. Porque el calendario donde salen todos los bookings es el tuyo.
**Luis Torres**: Correcto, pero digamos que le asignamos a un booking a través de nuestro dashboard interno.
**Cristian Berrío**: Eso, exacto, eso te iba a decir, lo que podemos hacer es que, automáticamente, bueno, no sé si se puede automáticamente, pero los bookings se le, si se le asignan a ella, en el calendario, Mira, te vamos a Si se la asigna a ella, ya lo puede ver en su calendario. La verdad es cómo hacer automáticamente eso, porque no no sé si se pueda. Pero, mira,
**Luis Torres**: ¿Cómo así? Si se le asigna a ella, ya puede hablar en su calendario de coger la Google, ¿cierto?
**Cristian Berrío**: Correcto, mira.
**Luis Torres**: Bueno, exacto, podríamos ahí ver, porque ahí ahí Google te muestra los diferentes calendarios que existen.
**Cristian Berrío**: Exacto. Por ejemplo, aquí, este que es nuestro. Si se le asigna a ella que sale eso. No me acuerdo cómo se hacía eso.
**Luis Torres**: ¿Aquí aquí quieres ir? ¿Qué qué es lo que estás haciendo, sir?
**Cristian Berrío**: Intentando asignar un staff o una persona a este bookie. Y así, si, por ejemplo, tú eres la partner owner, pero si si esta, María Elisa está, también podría ver el mismo calendario. Ahorita el calendario de María Elisa es este.
**Luis Torres**: Qué tal si dentro del nuevo venue system que montemos cada staff tiene su propio, como que tiene tiene tenemos su dashboard, ¿no?, donde yo pueden aceptar los bookings y eso. Que les salga dentro de go ahead level. ¿Me entiendes lo que te digo? Que el backend que nosotros creemos dashboards, esté conectado al go ahead level, de tal manera que descarguen la aplicación de GoHad level, y lo y la y la trabajen desde ahí, ¿me entiendes?
**Cristian Berrío**: O sea, ¿qué te refieres con que esté conectado?
**Luis Torres**: Cioè tenemos, nosotros tenemos un front end donde tenemos el website general, tenemos un back end donde tenemos el administrador, ¿cierto? Entre el front end backend en el entre el front end and end, una conexión donde yo puedo asignar staff, Entre ese back end de de administrador hay una conexión con staff. ¿Cierto?, para que el staff le le salga los cambios que haga que haya que con admin, todo está conectado.
**Cristian Berrío**: Correcto.
**Luis Torres**: Ahora, ¿cómo conectamos nuestros back ends a boja level? Como yo como administrador y lo el el propio staff. Digamos que el mismo staff tenga la aplicación de go ahead level, y que entre, que esté como asignado como staff dentro de el account de ese venue, y cuando sea asignado por el administrador, que no solo pueda ver la actividad y la información dentro de este, dentro del dentro del backend, dentro del dentro del dashboard,
**Cristian Berrío**: Mhmm.
**Luis Torres**: está sino puedan verlo a través de Goja Level. ¿Cuáles serían los beneficios de eso? Porque al final del día nosotros tenemos tenemos views de calendario y todo eso en el backend, ¿cierto?
**Cristian Berrío**: Correcto.
**Luis Torres**: Creo que el único beneficio sería que tengamos como que una tengan una aplicación donde puedan ver las cosas.
**Cristian Berrío**: Realmente, tú lo que dices es, por ejemplo, yo en mi dashboard de staff veo estos bookings. No. Veo este booking específico. Este. Que en vez de yo entrar desde un website, entre desde mi cuenta de Google como staff, y
**Luis Torres**: Mhmm.
**Cristian Berrío**: en mi calendario vea esto. O sea, vea el booking ese.
**Luis Torres**: Exacto. Exacto.
**Cristian Berrío**: Pues, hay
**Luis Torres**: Da la información Por ejemplo, vete de María Luisa, vete de María Luisa. ¿A qué tendrían acceso ellos dentro del dentro de ella? ¿Tendrían acceso a bueno, es que ahorita no le sale nada, porque ahorita no está su conexión, ¿cierto?
**Cristian Berrío**: O sea, sí está, pero no sale como, no no está asignada al booking. Al appointment. No les
**Luis Torres**: Esta semana a
**Cristian Berrío**: Al al appointment. O sea, por ejemplo, tú estás asignado a este, tú fuiste que creaste esto, tú estás asignado a esto. Sin embargo, ella no está asignada. O sea, ella no
**Luis Torres**: Habría que asignarla como estafa a ese booking.
**Cristian Berrío**: Exacto. La cuestión es, no sé si es viable es posible. Yo creería que sí, la verdad, Me gustaría pensar que sí se puede, con la conexión que ya tenemos. Porque esto, literalmente, nosotros a través de una API, interna nuestra, es como, o sea, ellos crean el booking de cero.
**Luis Torres**: Sí.
**Cristian Berrío**: Que que parece a ver el website. Entonces, creería que sí se puede, Creería que sí se puede. Tipo asignar varios staff. La cuestión es La cuestión, vamos a hacer a intentar
**Luis Torres**: Bro, creo que dentro de GojaLog podemos crear aplicaciones también. Para las subaccounts, ¿no?
**Cristian Berrío**: Ahí, mira, si se puede. No.
**Luis Torres**: Yeah.
**Cristian Berrío**: No, mentira, no. ¿Aplicaciones qué? Progreso, dejan agregar a uno. Intentando agregar varios. Team members.
**Luis Torres**: ¿No te dañan a a varios?
**Cristian Berrío**: Que no. Pero voy a intentar. Espérate, ponerlo hoy. Dieciocho. No, Parece que no.
**Luis Torres**: Relajado.
**Cristian Berrío**: No, me aparece que no.
**Luis Torres**: En una comodidad, Igual nuestro, igual dentro del backend que nosotros tenemos de staff podemos meterle todo eso.
**Cristian Berrío**: Claro. Pero no, como como que solo deja añadir un
**Luis Torres**: Lo que sí sería bueno, entonces, esto sería bueno para, es que si igual no es bueno para para lógicas de operacionalidad, o sea, los aledores, más que todo, para lógicas de ventas. ¿Cierto? Ejemplo, en tal caso de que Sebastián atiendo una llamada y él mismo gojador puede entregarle a él como que pueda apuntear como puede crear ese cuando la persona cree el el appointment, como tal, lo que sea, creo que, Goja, luego tiene una opción de añadir ese cliente, como que que ese cliente, que ese que ese perfil de cliente se asigne a mi perfil como empleado. Esa asociación siempre se puede hacer, ¿cierto?
**Cristian Berrío**: Correcto. Sí.
**Luis Torres**: Entonces, en tal caso de que Sebastián esté atendiendo las llamadas o cualquier persona esté atendiendo las llamadas, que ese cliente se asigna a ese staff member. Apenas se apenas se contacte.
**Cristian Berrío**: O sea, eso se puede hacer
**Luis Torres**: Y aquí se ha hecho el ser leve. Mejorar esto. Vamos a darle aquí. Vamos a poner el borde ese de la tarima, como dijimos. Avísese bien, si está alguien cerca por aquí, brode, le agradezco si no puede entrar al refrigerio, que estamos aquí secos. Gracias.
**Cristian Berrío**: Yep.
**Luis Torres**: ¿Qué tal?
**Cristian Berrío**: Sí se puede, está lo que comenta. Y para eso está diseñado. Y, como tú dices, lo del calendario, realmente, ellos lo pueden ver en en su dashboard. Pero hubiese estado acá no poder poner el calendario a ellos también. No te va mentir. Por temas de practicidad, practicidad, que no tengan que acceder al al link, sino un aplicativo, hubiese estado chévere.
**Luis Torres**: Mhmm. Sì, però no, eso no... No, no. Ok. Es una comodidad. No es una necesidad. Porque, vos, al lado de crear calendario es por cada staff member. ¿Por cuál es la necesidad de eso?
**Cristian Berrío**: Porque cada esta tiene su, o sea, no sé cómo explicártelo. Nosotros, como somos el admin,
**Luis Torres**: Para que se mande los responders, porque o se lo va mandar los responders, ¿cierto?
**Cristian Berrío**: Exacto. Pero no tanto eso, o sea, ay, acabo de tener una una idea. Pero no sé qué tan loca sea. O sea, es más que todo, nosotros, como tenemos la la vista de Admi, vemos el poco de calendario de esto.
**Luis Torres**: Okay.
**Cristian Berrío**: Pero, realmente, si un usuario como María Elisa, cuando ella entra, ella solo va a ver su calendario. O sea, ella va a omitir todos estos usuarios, todo esto, ella solo va a ver su calendario propio.
**Luis Torres**: Correcto.
**Cristian Berrío**: Entonces, por eso es que por cada persona que entra nueva, por cada usuario nuevo, se crea un calendario. De esa de esa manera, pues, cada persona, pues, puede tener su vista calendario, porque imagínate, si tú creas un usuario y no tiene calendario, y le quieres asignar algo. O él quiere hacer un appointment, si no tiene calendario, no puede hacer nada.
**Luis Torres**: ¿Y por qué tenemos a María Luisa dentro de? Ojalá, una pregunta.
**Cristian Berrío**: Porque como estamos haciendo lo de los staff, lo de enviar el la información del calendario de go high level al calendario de de Google, tú sabes que habían ciertos errores y ciertos inconvenientes, por ejemplo, para Por ejemplo, para que salga así como asignado. Espérate. Aquí. Para que salga asignado. A ver, ¿dónde hay uno tuyo? Esto. Esto, mira. No, Bueno, para que tú me has dicho que salga como que salían como guest Entonces,
**Luis Torres**: El staff,
**Cristian Berrío**: yo estaba aceptando las
**Luis Torres**: ¿es tú? ¿Con
**Cristian Berrío**: Yo estaba yo estaba intentaba intentaba hacer como un workaround para que saliera lo de los guests, saliera al staff también. Pero no, no funciona.
**Luis Torres**: Porque eso no funciona, no no termina funcionando.
**Cristian Berrío**: No. Pero, ajá. Hacer un work around creando el perfil de los staff en Google y luego, para cuando mandara de Google Pay a Google Calendar, salieran como usuarios asignados. A a ese booking.
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Pero no, no fue. Y por eso es que ahí está.
**Luis Torres**: Kijk. Krak, krak, krak. Bueno, Este, pendientes, entonces. Hagamos, ejecutemos el nuevo el nuevo flow de nuestro querido Doctor. Antes de que antes de que se nos inunde la casa, Sé que quieres terminar el tema de Stripe con dejarle bulto sobre this space, Démosle pausa al proyecto. No sea, no le va a pasar nada, no sé, no sé, nos va a desaparecer.
**Cristian Berrío**: Igual, ya está ya está prácticamente o sea, ya lo más complicado o lo más tedioso, ya está. Falta Stripe, y una que otra que tú dices como que no es cien por ciento necesario, pero es útil. Por ejemplo, lo de los pricing, que puedas cambiar los precios, los invoices, todo eso, o sea, como que es útil, es necesario, pero es como que cien por ciento prioridad.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Pero, ajá. Realmente, en this page ya estamos prácticamente hechos. Prácticamente. Y lo del Deloft, bueno, eso sí me tiene como un poquito
**Luis Torres**: Hermano, BLOOP es sencillo, ellos seleccionan katering y ya. Y que salga como una alerta, como servicios de add ons y ya. Sencillo.
**Cristian Berrío**: Entonces, ¿qué me pusiste lo lo de que en routeemos el pago también?
**Luis Torres**: ¿Cómo que anotemos el pago?
**Cristian Berrío**: Tú dices que esa en la tabla que tú me mandaste sale el ocho por ciento para Dilo.
**Luis Torres**: Ajá.
**Cristian Berrío**: Pero si nada, no van a pagar eso.
**Luis Torres**: Como que no van a pagar eso.
**Cristian Berrío**: O sea, seleccionan dealer, sale la alerta, pero realmente dealer no tiene ningún precio.
**Luis Torres**: Ah, eso es para futuro, eso es para futuro.
**Cristian Berrío**: Ah, por eso cuando tú gustes de dilos, yo me quedé en yo pero ¿cuánto se les va a cobrar?
**Luis Torres**: Ah, no, claro.
**Cristian Berrío**: O sea, si sale que tenemos que transferir el ocho por ciento, ¿cuánto se le va a cobrar a él?
**Luis Torres**: No tenemos ningún servicio que que meterle. Olvídate.
**Cristian Berrío**: Ok, ok, a futuro, ya entendí. Perfecto. Bueno, estamos así, estamos claros.
**Luis Torres**: Dale, Miró, vamos a darle play.
**Cristian Berrío**: Te iba a decir, al final el tema del contrato, ¿qué?
**Luis Torres**: Qué de qué?
**Cristian Berrío**: O sea, yo lo que yo entiendo
**Luis Torres**: Adelante.
**Cristian Berrío**: cuál es la lógica de eso.
**Luis Torres**: Ok.
**Cristian Berrío**: Pero, o sea, lo que lo que no me cuadra a mí es el porcentaje, el ocho por ciento ese, que se refleje de aquí a cuatro años, y que vaya subiendo año por año, porcentaje, uno uno uno y pico, dos dos y pico. Entonces, mi pregunta es, mi pregunta no, O sea, yo yo yo miré un poquito, conté un poquito en ese tema. Pero siento que está como muy lejos, llegar al ocho por ciento en cuatro años. O sea, cuatro años es poquito, pero no es tan poquito, o sea, cuatro años son cuatro años. Entonces, quería ver cuáles son las opciones ahí. Pero siento que cuatro años es bastante,
**Luis Torres**: Sí, el va a estar de cool y también es bastante. Los dos son inclusivos, o sea, normalmente, ¿Qué le diste al respecto? O sea, ¿qué qué qué fue lo que viste? ¿Pudiste hacer un poquito, pudiste indagar un poquito sobre eso?
**Cristian Berrío**: Sí, o sea, indagué un poquito. Con el tema del porcentaje, y, obviamente, el porcentaje, el ocho por ciento, pues está bien. O sea, el valor está bien, el ocho por ciento estoy estoy totalmente de acuerdo.
**Luis Torres**: Okay.
**Cristian Berrío**: La cuestión es que se demora cuatro años en reflejarse el ocho por siete, y cuatro años es bastante.
**Luis Torres**: Completo. Cuatro años completo.
**Cristian Berrío**: Cuatro años, o sea, por
**Luis Torres**: Ok. ¿Y cuál es tu cuál es tu problema con los cuatro años? O sea, digamos, que ok, ajá. Digamos que ¿Cómo se llama? Quieres un, en el tal caso. ¿No? De que queramos que sea menos tiempo,
**Cristian Berrío**: Uh-huh.
**Luis Torres**: Bueno, realmente el equity el equity se se lleva a su, a la mitad de su totalidad, a los dos años. O sea, realmente, si lo si lo vas a short jump, igual tienes algún tipo de de de salida. ¿Me entiendes?
**Cristian Berrío**: Espérate, no te escuché, o sea, no te escuché los últimos que me estaban llamando.
**Luis Torres**: Ok, si lo ves a largo, a corto plazo, igual tienes un algún tipo de de de salida. No sé si tiene sentido.
**Cristian Berrío**: ¿Cómo hace algún tipo?
**Luis Torres**: O sea, en el tal caso de que en el tal caso de que no completes por x y z razón, tengas algún tipo de certidumbre de que, bueno, a los dos años y medio, yo no sé, me quiero ir a Europa y viajar por todo el país, no quiero trabajar más por un año. No sé. Qué es lo que tú quieras hacer. Digamos que ese es el caso. A los dos años, igual, ¿tienes algún tipo de de este,
**Cristian Berrío**: De equity.
**Luis Torres**: algún tipo de salida, ¿cierto? Tienes una salida, creo que es la mitad, creo que es del cuatro por ciento, a los dos años, lo cual, desde un punto de vista convencional, es lo normal que una persona, bueno, es lo lo sí, lo más normal que una persona puede puede tener en este tipo de estructura. Digamos, si tú trabajas en un startup, a los dos años se espera que el startup esté en una ronda, por lo menos, por lo menos, a, de de inversión.
**Cristian Berrío**: No.
**Luis Torres**: Cuando se ronda a sucede, las personas se se sacan su cualquier tipo de porcentaje que tengan y y y terminan, ¿no?
**Cristian Berrío**: Sí, o sea, por eso te digo, el porcentaje me parece que está perfecto. Corte, está totalmente justo.
**Luis Torres**: Okay.
**Cristian Berrío**: A mí, lo que me lo que me concierna, de pronto, sí, es un poquito el el tiempo en el que demora reflejándose eso,
**Luis Torres**: Mhmm.
**Cristian Berrío**: Sabemos que fuera un poquito menos de tiempo, o que se pueda no sé, negociar de alguna manera un poquito menos de tiempo. O que por lo menos empiece con algo desde ya.
**Luis Torres**: Claro. Ok.
**Cristian Berrío**: Exacto, o sea, esa sería otra, que de pronto, bueno, tú tengas los cuatro años, pero que por lo menos empiece algo desde ya, porque yo leí y era en un año de aquí a un año, vas a tener el uno por ciento, no lo tengo desde ya, sino que en un año voy a tener ya un porcentaje.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Entonces, en un año está está está lejos. De pronto, se puede negociar que que que tenga algo de ya, o de pronto quitar el tiempo de cuatro años tan largo y cortarlo un poquito. Pero el porcentaje, yo estoy claro en eso. O sea, ahí está perfecto, me parece.
**Luis Torres**: Sí.
**Cristian Berrío**: No sé qué opinen.
**Luis Torres**: Me parece bien, me parece bien. ¿Qué te gustaría más? Sea, ¿cuál es tu cuál es tu interés, cuál es tu prioridad más? Más
**Cristian Berrío**: No sé. Yo diría que que tenga desde ya.
**Luis Torres**: Ok.
**Cristian Berrío**: Por eso es que siento que esperar un año tener o sea, siento que esperar un año tener, por ejemplo, un porcentaje un poquito más, ponte tú, un dos por ciento, lo que sea, en un año, No sé. No, prefiero tener, la la verdad, prefiero tener las de ya. Tengo fe que vamos a vender un millón de dólares en un año. De allí a un año.
**Luis Torres**: Crac, crac. Necesitamos un buen una buena entrada en en un una estrategia bien agresiva.
**Cristian Berrío**: No, con lo que estamos haciendo ahorita de space, y con lo que estamos haciendo de yo prefería tener porcentaje ya. La verdad.
**Luis Torres**: Bien, está bueno, está bueno. Me gusta.
**Cristian Berrío**: O sea, podemos manejar
**Luis Torres**: Bueno, también quisiera que tú te
**Cristian Berrío**: cuatro años, creo que empieza desde ya.
**Luis Torres**: tú ya tienes un año y pico adentro, o sea, también es claramente no desde, no no sin formalidad, pero en teoría ya tú tienes un año y pico adentro.
**Cristian Berrío**: Eso es verdad.
**Luis Torres**: Me parece justo que parece justo que ya tengas algún tipo de de de galardía por por esa por ese camino ya recorrido.
**Cristian Berrío**: Que me tienen preocupados el dólar. La madre de dólar.
**Luis Torres**: El dólar está bajando mucho, eso sí es verdad.
**Cristian Berrío**: Estás demasiado bajo. Nunca nunca había estado así de bajo.
**Luis Torres**: Sí.
**Cristian Berrío**: Literalmente, en la el aumento que me hiciste, fue literalmente lo que ya estaba ganando, pues. O sea, literalmente fue lo mismo, yo me puse, yo miré la taza y yo dije, mierda, sigue bajando, no entiendo por qué.
**Luis Torres**: Sí.
**Cristian Berrío**: Estamos en elección, normalmente, elecciones suele subir bastante, pero
**Luis Torres**: Sí. ¿Qué te parece si te subimos el sueldo a dos por cuatro ocho? Doscientos semanal, serían casi sus casi tres millones,
**Cristian Berrío**: Me sirve.
**Luis Torres**: ¿Tres mil?
**Cristian Berrío**: Serviria naturalmente.
**Luis Torres**: Trescientos un por ciento de de equity. ¿Qué te parece eso?
**Cristian Berrío**: Serviría. Motivación. Me sirve, me sirve. Sí, porque el dólar me está dando
**Luis Torres**: Excelente. Eso, escuchas? Cris,
**Cristian Berrío**: The work my payment fee.
**Luis Torres**: ¿Me escuchas?
**Cristian Berrío**: Sí. Que te iba a decir,
**Luis Torres**: ¿Conseguiste entrenado personal?
**Cristian Berrío**: No, está muy caro, los averigüé, pero está muy caro.
**Luis Torres**: ¿Cuánto cuánto cobran?
**Cristian Berrío**: Y la al gimnasio cobran como trescientos al mes, pero te hacen un plan alimenticio, te hacen todo.
**Luis Torres**: Pero has buscado tipo otro ordenador de la calle que te lo lleva a gimnasio.
**Cristian Berrío**: Se puede. Obviamente, los gimnasios les conviene más que el mismo entrenador o sea, no puedes salir de la
**Luis Torres**: Como que no se puede ir, también para encima tuyo te van a te van a supervisar todo el tiempo, tú vas con un, entrando con un amigo y ya,
**Cristian Berrío**: Esa esa es la cuestión. O sea, realmente, si te pilla, no se puede. Pero, o sea, en papel no se puede, pero ahí como uno puede hacer como o sea, le puedo decir con un entrenador como que no, que Exacto.
**Luis Torres**: Me está ayudando Jack, o cómo saben ellos que él está
**Cristian Berrío**: Que que medio revise, me me supervise, que no sé qué, pero no puede estar encima mío.
**Luis Torres**: Bueno, búscate, yo te, te estoy cobrando que trescientos dólares mensuales, ¿Cuánto? ¿Trescientos qué?
**Cristian Berrío**: No, mensual, trescientos mil, trescientos mil. Pesos, pesos, nomás dólares.
**Luis Torres**: ¿Cuántos dólares son esos? ¿Son como cien dólares? Al mes, sí, más o menos como cien dólares al al mes, ¿no?
**Cristian Berrío**: Sí, ochenta y siete dólares al mes.
**Luis Torres**: Eso es cierto. Búscate un entrenador que te cobre como unos sesenta al mes, Trailers te paga los primeros no sé, dos, tres meses de gimnasio.
**Cristian Berrío**: Me patrocinan los primeros. Es que yo siento que, con dos meses, que yo le le coja la rutina y le coja el plan alimenticio, pues ya es replicarlo, Siento que más de eso no importa.
**Luis Torres**: Métele.
**Cristian Berrío**: Pero me

_Sincronizado por Brain: 2026-10-17T18:46:21.680Z_
