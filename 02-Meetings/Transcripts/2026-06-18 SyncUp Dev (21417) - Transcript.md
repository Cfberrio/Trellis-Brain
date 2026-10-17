---
brain_note_id: "dest:meetings:148536f35ebc3dfad4c95080ae415136"
canonical_key: "meetings/148536f35ebc3dfad4c95080ae415136"
brand_id: "meetings"
---
# Transcript — 2026-06-18 SyncUp Dev (21417)

## Transcript

- Reunión: [[02-Meetings/2026-06-18 SyncUp Dev (21417)]]

**Luis Torres**: Aló.
**Cristian Berrío**: Aló, aló, ¿cómo estamos?
**Luis Torres**: Escucha, se escucha?
**Cristian Berrío**: Te escucho un poquito mal.
**Luis Torres**: Brote, con hueco, con el hueco interminable.
**Cristian Berrío**: ¿Cómo?
**Luis Torres**: ¿Cómo? Ahora sí. Se escuchaba un error terrible.
**Cristian Berrío**: Sí, sí.
**Luis Torres**: Sí, sí.
**Cristian Berrío**: Hay un poquito de coco.
**Luis Torres**: Bueno, ahí Mi hermano, ¿qué pasó con con con las comunicaciones de OVB? Ni siquiera están llegando al inbox. Los correos de Go ahead level no están llegando al inbox, están llegando spam de todos los recipientes. Puse el correo escrito en del email y no llegó bueno, llegó el correo de for confirm, de tour,
**Cristian Berrío**: Tú dices,
**Luis Torres**: tú dices, espérate, es que hay una
**Cristian Berrío**: Espérate, que es que hay una Creo que ya. O sea, ¿tú estás diciendo que los correos están llegando a spam?
**Luis Torres**: No, ya llegaron bien, ya los revisé. ¿Tú lo sacaste de spam?
**Cristian Berrío**: No, no, no, es que o sea, tú pros tengo el discipline brief, ITG o spam.
**Luis Torres**: Habían llegado sí, pero ya está en inbox.
**Cristian Berrío**: Okay. No, sí, o sea, yo sé que los correos están llegando normal. ¿Qué es lo que qué es lo que encontré? Total, exactamente, lo que encontré.
**Luis Torres**: Muéstrame eso, por favor.
**Cristian Berrío**: Te va a pasar lo que me lo que trajo. O sea, en pocas palabras, el problema está que él no distingue el, o sea, los filtros, de cuándo es un appointment y cuándo es un tour. Él lo único que sabe es hay un nuevo slot en mi calendario, no sé si es un book no sé si es un tour. El punto es que hay un nuevo slot, que es un appointment, en mi calendario. Independientemente de lo que sea, de dónde vino, de API, o si vino de de de los tours. O sea, sí, o sea, si es a través de API o si es a través de del embed calendar que tenemos nosotros de tours, que nos distingue eso. Entonces, eso es que está entrando. Ahí planteé dos soluciones. La más rápida no es esa realmente. La más rápida es la b. Que es usar dos calendarios nuevamente y apagar todas las comunicaciones del calendario de los bookings. Referente a Turcia. De esa manera, cuando nosotros mandemos a través del API, un booking cualquiera, no va a entrar a la automatización de los tours.
**Luis Torres**: ¿Y le mandaría más correos electrónicos o nada más mensajes de texto?
**Cristian Berrío**: No, ¿cómo así?
**Luis Torres**: Seguimos mandándole correos a la gente, sepamos los los tours, ¿no entiendo?
**Cristian Berrío**: O sea, mira, ahorita mismo, Hay que volver a hacer las cosas como estábamos haciendo antes.
**Luis Torres**: Por eso yo pensaba que eso lo habíamos hecho ya,
**Cristian Berrío**: No, Ya sé, ya ya entendí. Qué es lo que pudo haber estado pasando todo este tiempo. Nosotros tenemos varios calendarios. ¿Verdad? Entonces, nosotros habíamos creado uno dizque hoy b tours, y otro dizque hoy b bookings. Entonces, hoy vi bookings, ahorita mismo, Es este mismo calendario. O sea, está está funcionando tanto de calendario para para pues los bookings, todos los bookings están llegando allá. Y está funcionando para este mismo calendario de tour. O sea, está cumpliendo la función, el mismo calendario de hacer dos cosas al mismo tiempo.
**Luis Torres**: ¿Por qué? No la hemos separado.
**Cristian Berrío**: No lo habíamos separado, sí, pero no sé por qué lo íbamos a juntar, no me acuerdo.
**Luis Torres**: Por, ¿cómo así? ¿Cómo que lo volvimos a juntar? Nosotros lo hemos separado. ¿Te acuerdas que teníamos que hablarnos con eso? Y volvimos a cambiar la cadena de de comunicación. En compramos
**Cristian Berrío**: Separamos o lo juntamos?
**Luis Torres**: lo juntamos y luego lo separamos, porque no, se estaban confundiendo. Se mezclando.
**Cristian Berrío**: Me hiciste duda. Yo no sé.
**Luis Torres**: Pues le hemos arreglado ya, hermano.
**Cristian Berrío**: Ya entendí qué está pasando. Olvídelo.
**Luis Torres**: No, hola, Cristian, ¿el mes pasado?
**Cristian Berrío**: Ya sé qué está pasando. Okay, ya lo arreglé. Había que apagarlo todo.
**Luis Torres**: ¿Cómo así?
**Cristian Berrío**: Están prendidas las comunicaciones.
**Luis Torres**: ¿De qué?
**Cristian Berrío**: De de OVB bookings. Mirá,
**Luis Torres**: Ajá. ¿Y estamos a suponer que están prendidas?
**Cristian Berrío**: Estas no. Porque estas son las, estas son comunicaciones de tours nada más. O sea, cuando ellos llenan esto,
**Luis Torres**: Calla, es lo mismo.
**Cristian Berrío**: esto. Como te digo, el calendario no.
**Luis Torres**: Y juntos, porque estamos ¿no? Porque Booking está en las notificaciones que de tours.
**Cristian Berrío**: No, no, no, porque es que antes antes lo teníamos antes lo teníamos juntos, como tú dijiste. Yo me confundí. Lo teníamos juntos y después nos separamos, ¿verdad? Cuando nos
**Luis Torres**: Es que no le ha dejado nombre.
**Cristian Berrío**: No, no tanto eso. Cuando lo separamos, no las apagué. Porque no sabía que cuando tú cuando nosotros mandábamos, por medio de API, los bookings, no sabía que lo interpretaban. No no no voy a hacer la distinción de si es un appointment, de tours o si es un appointment de
**Luis Torres**: Puedes poner los nombres correctos, entonces eso es tours o es bookings.
**Cristian Berrío**: Este es bookings. Ya, o sea, ya tiene el nombre correcto en los dos mil. De ahí guardo eso que nos vuelva a mandar. Listo. Este es el de este es el de tours. Y este es el de bookings.
**Luis Torres**: Ok. ¿Ya funciona, entonces?
**Cristian Berrío**: Sí, pero quiero verificar eso que dijiste, tú sabes. Porque la última vez que me acuerdo, No metiera así. Entonces, o sea, ya están ya están divididos. Dos calendarios. Y ya pagué las comunicaciones de b b bookings. El problema había sido que no había pagado las comunicaciones de OVB Booking. Entonces, como te digo, no hacía la distinción de cuándo era un tour, cuándo era un booking, y lo único que hacía era que identificaba un slot que estaba tomando el calendario,
**Luis Torres**: Mhmm.
**Cristian Berrío**: y mandaba la comunicación que ya estaba planteada aquí.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Te mostré.
**Luis Torres**: Abrir la cadena de comunicaciones en bookings, please? Y de tools?
**Cristian Berrío**: ¿De booking sigue?
**Luis Torres**: Voy a abrir la cadena de comunicaciones de bookings y de tour, please. Tipo, las que tienes implementadas, no no la cadena.
**Cristian Berrío**: Ok. Buenas tardes, comparla enseguida.
**Luis Torres**: Bookings. ¿Qué tienes para bookings incorporado? A ver. Sacar. ¿O tienes la de tours? La de tu encuesta?
**Cristian Berrío**: Ajá, está lá tu.
**Luis Torres**: Ok, a ver. And tours? Primero, ¿ok? I wrap up the venue, pull the door.
**Cristian Berrío**: Es más, yo creo que está esto en viejo, mira que tenemos esto aquí.
**Luis Torres**: Sí, esta comunicación no está a
**Cristian Berrío**: Por eso te decía, nosotros lo habíamos juntado.
**Luis Torres**: Sí, lo hemos juntado, o sea, habíamos juntado el calendario, era para que el no lo hemos juntado para preguntarlo, era porque calendario no quería que tú desees overlap, tipo que la gente no pudiera buscar un tour mientras hay un booking, pero eso casi nunca pasa. Porque nosotros no tenemos casi booking los días de semana, así que no importa. Pero, claramente, si hubiese sabido que iba a causar ese problemón, me hubiese dicho nada al principio.
**Cristian Berrío**: No, yo tampoco sabía. Yo me acabo de enterar ahora que me puse
**Luis Torres**: Sí.
**Cristian Berrío**: a investigar.
**Luis Torres**: Sí. La comunicación de tools hay que hay que actualizarla. Todo eso está en mano. Porque eso está bien, eso es viejo. Ahora, la de bookings sí es la que está correcta. Muéstrame lo que tenemos implementado de eso. ¿Todo lo de bookings está implementado de esa manera?
**Cristian Berrío**: Yes. La booking sí está cien por ciento actualizada. Pues, la primera es esta. Esta la enviamos detrás de nuestro website.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Esta remaining No, nada más nada. Este.
**Luis Torres**: Todo está bien. A ver, muésteme. Yo tengo la cadena abierta, si quieres nada más tú sacas la Ok, primero es un correo fifty percent received. ¿Sí? Okay. Luego, y un mensaje, ¿sí?
**Cristian Berrío**: El primer
**Luis Torres**: No, nada más un correo, fifty percent received. Done. Luego, ¿qué tienes? Ese mensaje
**Cristian Berrío**: Remaining. Remaining balance.
**Luis Torres**: el mensaje de animales
**Cristian Berrío**: Mhmm.
**Luis Torres**: Ok. ¿Por correo o mensaje?
**Cristian Berrío**: La dos.
**Luis Torres**: ¿Cómo sabes ahí que están las dos?
**Cristian Berrío**: Y la la que va.
**Luis Torres**: Luego, exit fully paid instructions.
**Cristian Berrío**: Website. ¿Que se le envía?
**Luis Torres**: Se mandaron
**Cristian Berrío**: Porque, ¿cómo iba a saber qué pagó? Eso tenemos que hacerlo a través de tenemos que chequear Stripe, todo lo que sea confirmación de pago. Es por nuestro website, porque tenemos que chequear de alguna manera si paga un Stripe o no. O sea, no hay manera de meterlo aquí.
**Luis Torres**: Ok, ese está en el en nuestro website. ¿Dónde está esa comunicación? ¿Dónde se manda?
**Cristian Berrío**: De de website. O sea, a través de SMTP. Uno que esté por aquí.
**Luis Torres**: ¿Y cómo logras que se haga automático eso? O sea, ¿dónde está la configuración de eso?
**Cristian Berrío**: O sea, es interna, ya. So, te puedo mostrar la función.
**Luis Torres**: Oh, interno es de OIB.
**Cristian Berrío**: Ajá. O sea, interno, literalmente, función. Sí.
**Luis Torres**: Sería mejor montar todas las funciones en un solo lugar? Los perfiles como lo tienen montado ahorita, sí.
**Cristian Berrío**: O sea, realmente, se puede mandar desde a través de de estoy buscándolo. O sea, se puede, realmente, puede enviar otra vez, de Aquí está. Esta función. Eso eso lo invoca cuando usted la avisa, de que ya hizo el pago del cincuenta por ciento. Cuando esto da un ok, enseguida enviamos, a través de nuestro propio correo,
**Luis Torres**: Holy payment.
**Cristian Berrío**: Exacto, está por allí.
**Luis Torres**: Luego, terminate checking. Luego tenemos un check in, que se hace para el correo. Treinta días antes.
**Cristian Berrío**: Sí, ya te muestro. Bueno, lo que te estaba diciendo, o realmente lo podemos enviar a través de o sea, podemos crear una automatización para eso, pero o sea, en verdad es bastante
**Luis Torres**: There we go.
**Cristian Berrío**: No, o sea, es trabajo extra, no es tetris.
**Luis Torres**: ¿Dónde
**Cristian Berrío**: Porque ya le
**Luis Torres**: ¿Hablo desde directo desde el website? ¿Se lo dices tú?
**Cristian Berrío**: Enviarlo, o sea, crear una automatización, que el el email de confirmación de pago sea a través de aquí.
**Luis Torres**: Ah, ya. Dale dale status workflow, a ver qué es más lo que tienes Tienes, entonces, tienes otra treinta días antes y lo demás, un mensaje de texto, ¿cierto? A ver,
**Cristian Berrío**: Estate workflow es para o sea, no manda correos. Solo es
**Luis Torres**: Solo cambia el estatus, ¿cierto? ¿Cierto?
**Cristian Berrío**: Exacto.
**Luis Torres**: ¿Cuál es el que estás, Olino?
**Cristian Berrío**: Ahorita estaba en remaining balance.
**Luis Torres**: Exacto, vámonos a la cadena de comunicación que estamos revisando.
**Cristian Berrío**: Treinta días. Creo que era, ¿no? ¿Volvamos ahora? Treinta días.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Sí.
**Luis Torres**: Cuatro.
**Cristian Berrío**: Email de SMS y SMS.
**Luis Torres**: Eso es treinta días antes.
**Cristian Berrío**: Sí. Treinta días.
**Luis Torres**: Email y el y el resto son puros correos mensaje de texto.
**Cristian Berrío**: Mhmm.
**Luis Torres**: ¿Qué son las instrucciones como tal?
**Cristian Berrío**: Correcto. Bueno, aquí tú puedes ver, la última vez que se ejecutó fue hoy. Las dos.
**Luis Torres**: A ver, métete en en la cadena de mensajes, métete en el último mensaje que les mandas de guest report, No, no, no, no, no, en la cadena, cadena de de de mensajería. Automatización. Ok. Necesito el último mensaje, ajá. ¿Qué dice ese? Echamos todo. ¿Qué? Echamos todo en qué? Locura es eso?
**Cristian Berrío**: Eso es lo que está aquí.
**Luis Torres**: Time, no done. Oh, dice time, sí. Time, door plus door code plus Wi Fi, Ok, falta ahí el mander, ¿o no? Falta el último.
**Cristian Berrío**: Eso se envía a través de nuestro website.
**Luis Torres**: Eso es un mensaje de texto, loco.
**Cristian Berrío**: Yo lo envío como como email.
**Luis Torres**: ¿Por qué?
**Cristian Berrío**: Porque tenemos que cambiar toda la lógica de esto, entonces. Tendríamos que modificar esto. Agregarlo un paso extra.
**Luis Torres**: Eso así, déjame saber, porque hubiésemos, quitamos el quitamos reemplazas, prefiero yo prefiero que quede siete, que quede ocho, o sea, que quede ocho en vez de siete. Métele ahí al ocho.
**Cristian Berrío**: O sea, ¿prefieres que, o sea, que esto lo metan al que ya está el siete?
**Luis Torres**: Claro, claro. Claro, porque lo el último es la retención de de del review, todo,
**Cristian Berrío**: ¿Qué es?
**Luis Torres**: O, bueno, si si querés, ponte. Eso se le manda una hora antes del del evento.
**Cristian Berrío**: Este se le manda
**Luis Torres**: ¿Cuánto se le manda?
**Cristian Berrío**: Y todos hemos una hora antes, sí.
**Luis Torres**: Como se tu como tu vai acionar tu me desejo?
**Cristian Berrío**: No se ve aquí, se ve aquí. Sabes que todo esto es interno, es que eso eso es lo que te quiero decir. O sea, todas esas funciones son literalmente internas, que se hace a través de esto.
**Luis Torres**: La función de mensaje de texto.
**Cristian Berrío**: No, O sea, ponte a pensar, ¿cómo cómo hace?
**Luis Torres**: Ok, mi pregunta es,
**Cristian Berrío**: Cómo hace Gohigh Level para saber cuándo faltan siete días para un evento, si él no tiene la base de datos? Toda esa información la mandamos desde aquí.
**Luis Torres**: Okay.
**Cristian Berrío**: Por eso,
**Luis Torres**: Con tiempo.
**Cristian Berrío**: cuando hay que hacer algo así como, bueno, quiero que mandes en vez de un día, mandes una hora, hay que cambiar todo esto.
**Luis Torres**: Okay.
**Cristian Berrío**: Eso es lo
**Luis Torres**: Entonces, déjame meterme en la cadena de comunicación ¿Y cuándo yo le digo a ellos que llenen el guest report? ¿Dónde va tener esa información?
**Cristian Berrío**: le dices tú?
**Luis Torres**: I just wanna get your point.
**Cristian Berrío**: Se lo hice creo que en treinta.
**Luis Torres**: En los treinta días,
**Cristian Berrío**: No.
**Luis Torres**: Ok, aquí está.
**Cristian Berrío**: Creo que ya no lo estás diciendo.
**Luis Torres**: Sí, un día antes, one day, Ice Remainder. Same link becomes your guest report, pero es no queda claro. Tengo que cambiar esa cadena. Entonces, tú me dices, que el que sale una hora antes por SMS ya ese es el tu mensaje que se pueda enviar por la cadena que tenemos ahorita, ¿cierto?
**Cristian Berrío**: Sí, pero deja y te confirmo. Ese siempre me confunde si es siete un día.
**Luis Torres**: Así?
**Cristian Berrío**: O sea, no no me no me acuerdo siete siete días o un, de un día o una hora, perdón. Se me confunde. Pero ya te digo. Ya estoy preguntando. No una hora. Sí. Es una una hora antes del evento.
**Luis Torres**: Ok, ve tal link rapidito. Vete al link del ya support rapidito, donde dejan aquí a support, El link de WhatsApp, dejan el guest report. Axis code. Creo.
**Cristian Berrío**: No. Ah, mentira, sí, ¿verdad?, que lo habías puesto en access code.
**Luis Torres**: Ok, podríamos cambiar la el el wording de esto para que no sea solo como que access code. Como que sería Orlando access, que ponga reservation number, email, y le le y le botón que diga enter, porque todo esto está como que a que es como que met get the access code. Debería ser debería ser información general ¿cierto?, información general, no solo el access code, por ahí OIB Okay. Okay. They Date.
**Cristian Berrío**: Date,
**Luis Torres**: Como que day, de día. Day of event, day of event. Okay. Excelente. Aquí. Cambiaré la palabra que dicen ahí, es get access to. Dale enter. Ah, no, botón azul. Cambia las palabras que dicen ponle gate code. Digo, enter, Ok. Ok, excelente. Ahora cuando entras a esa página, ¿qué te aparece? Muéstrame ese muéstrame ese. Yo quiero ver el apartado donde ellos mandan el get report acá adentro, Bueno.
**Cristian Berrío**: Sí. No, estamos.
**Luis Torres**: ¿Los viejos pueden entrar todavía? Dale, mete ese correo.
**Cristian Berrío**: Sí, o sea, eso no se bloquea.
**Luis Torres**: ¿Podríamos bloquearlo? Dice,
**Cristian Berrío**: Se lo podemos poner inactivo, sí.
**Luis Torres**: Yo pensaba que esto se bloqueaba para la ¿Y el código dónde sale?
**Cristian Berrío**: ¿El código de qué? Acceso. Abajito.
**Luis Torres**: El código de para entrar, para entrar al admin. Ah, no le sale porque ya pasó el tiempo, ¿cierto?
**Cristian Berrío**: Mhmm.
**Luis Torres**: Una vez que te salga el código una vez, ya no te sale más.
**Cristian Berrío**: Oh,
**Luis Torres**: ¿Cómo funciona eso?
**Cristian Berrío**: cuando ya se acabó el booking, ya no te va a salir el código de acceso. El report siempre va a salir.
**Luis Torres**: Entendido.
**Cristian Berrío**: Pero, por ejemplo, para esta, Nos probamos con esta mejor. Debería salirla. No, esto no
**Luis Torres**: Yeah. ¿Y esto no es una manera de de bloquear quién puede ver el código y quién no?
**Cristian Berrío**: ¿Cómo?
**Luis Torres**: ¿Manera de bloquear quién puede abrir el código y quién no?
**Cristian Berrío**: Pero aquí en, o sea, ¿en qué sentido? Dame lo que
**Luis Torres**: Me refiero. Eres un guest, ya pasó tu, ya tu evento que no nos puedes dar el código al día de tu evento, ¿no? Sí.
**Cristian Berrío**: O sea, se puede bloquear el día del evento. Por ejemplo, el que probamos ahorita, está porque aún no ha pasado. Está apenas Pero el que miramos ahorita, que era esta,
**Luis Torres**: ¿No puedes ver el código más?
**Cristian Berrío**: Exacto, porque ya pasó el día de su evento.
**Luis Torres**: Ok, bloquéalo hasta el día de, el día sí, hasta el día de verano, por
**Cristian Berrío**: Ok. O d. Bueno, hay que modificar, entonces, la comunicación de esto. By the way, ¿puede conectar por MCP? Supavase, y fue mucho más fácil de lo que pensé tomar el toda la información. Sí.
**Luis Torres**: tal?
**Cristian Berrío**: Pues no tuve que mirar manualmente, gracias a dios. Que no tuve que mirar manualmente información que está en su sino que directamente conecté al MCP a cloud y Claude revisó todo por mí. Eso me cerró un poco de tiempo, no tengo mentir.
**Luis Torres**: Sí. Bueno, hermano, este, guárdale dos semanas al día, Asegúrate de que todo esté funcionando para que, una vez que regrese el mensaje del siete y el ocho, el mensaje de canal siete y ocho, mandamos un mensaje nuevo ya. Este, ¿ya lo arreglaste?
**Cristian Berrío**: Sure.
**Luis Torres**: ¿Nada más puedes darle acceso por el día de evento?
**Cristian Berrío**: El día de evento. Pero hay que poner como un mensaje más family friendly.
**Luis Torres**: Eso. De
**Cristian Berrío**: ¿Qué le pondrías tú?
**Luis Torres**: your event is not algo como que your event is not it is not a day of your event yet. Please try again later.
**Cristian Berrío**: No, como please try again, como que el día de hoy entry.
**Luis Torres**: On on your on the day of your event. Eso. Try again on the day of your event. Bueno, hermano, este, tengo que tengo una reunión ahorita a las cinco cuarenta y cinco, y no es aquí en la casa. Así que me voy a retirar. Ahí se me, cuando termines lo de tirar, por favor, para ver si puedo montar las notificaciones esta noche,
**Cristian Berrío**: No, sí, ya. Ya me falta es Me falta es, bueno, la mensajería, A ver, ¿qué?, yo te iba a preguntar. Esto, realmente, solo es poner la mensajería que ya mandamos, ¿no?
**Luis Torres**: ¿Cómo así?
**Cristian Berrío**: O sea, porque tú ya lo tienes guardado aquí. Tú todo eso lo tienes guardado aquí. Aquí.
**Luis Torres**: O la mensajería es la misma, sí.
**Cristian Berrío**: Exacto, o sea, solo es moverlo. O duplicarlo.
**Luis Torres**: Exacto, exacto, exacto.
**Cristian Berrío**: Ok. Bueno, entonces, acabé. Me faltaba duplicarlo ya.
**Luis Torres**: Duplicar qué?
**Cristian Berrío**: La mensajería, o sea, notifications. Porque ya, no,
**Luis Torres**: Meterlo ahí, meterlo ahí.
**Cristian Berrío**: Ajá. ¿O qué quieres que haga aquí exactamente?
**Luis Torres**: Sí, sí, sí, sí, sí, organízalo, organízalo, organízalo, información que ya tenemos adentro.
**Cristian Berrío**: Ok.
**Luis Torres**: Please. Mayoría bastante eso.
**Cristian Berrío**: Pero ya ya terminé todo esto, te lo dejé mastigadito. Con los dioramas que te gustan.
**Luis Torres**: Amazing.
**Cristian Berrío**: Sí.
**Luis Torres**: Así me gusta. Dios mío. Ya ya vamos a poderte acá, tengan creado una, más eficiente, ¿ah?
**Cristian Berrío**: Así es. Bendito sea Claude. Y ya realicé los cambios de de d space, de la nueva, bueno, nuevo documento que montaste. Falta pero ya ya ya hice los cambios que me dijiste. ¿Te lo cambié?
**Luis Torres**: И листайп, de displays.
**Cristian Berrío**: Ajá. O lo cambié y encontré. Las discrepancias que encontré, pues.
**Luis Torres**: ¿Y qué pasa a esa hora?
**Cristian Berrío**: Información, más que todo precios, información.
**Luis Torres**: Activo.
**Cristian Berrío**: Y cleaning fee y todo eso.
**Luis Torres**: Vamos a ver.
**Cristian Berrío**: Ok, pues. Bueno,
**Luis Torres**: Listo, depende de qué te dan, necesito que grajes un también.
**Cristian Berrío**: ¿el qué?
**Luis Torres**: Lista de pendientes de de space.
**Cristian Berrío**: Ah, ya la tengo. Pero no sé no sé dónde va montarla.
**Luis Torres**: ¿Qué es?
**Cristian Berrío**: Ya la tengo. Pero no sé dónde montarla.
**Luis Torres**: En un documento de en el en un documento dentro de Dispace, dentro de la verificación de Dispace.
**Cristian Berrío**: ¿Tipo pendientes? O lo que ya tenemos.
**Luis Torres**: Un nuevo documento, un nuevo documento.
**Cristian Berrío**: Creo que es esto.
**Luis Torres**: O la fecha de hoy, lo que quieras.
**Cristian Berrío**: Okay.
**Luis Torres**: Sí, pon la fecha de hoy. Nos damos cuenta que eso no te falta. Como que hasta ahí quedamos hoy.
**Cristian Berrío**: Okay.
**Luis Torres**: Alómero, me dices algo,
**Cristian Berrío**: Listo, hermano. Dale, ya que el monto puede hacer.

_Sincronizado por Brain: 2026-10-17T18:48:59.193Z_
