---
brain_note_id: "dest:meetings:b5e6fddd88f0ac94c04fb5f444c4ba54"
canonical_key: "meetings/b5e6fddd88f0ac94c04fb5f444c4ba54"
brand_id: "meetings"
---
# Transcript — 2026-09-01 SyncUp Dev (23877)

## Transcript

- Reunión: [[02-Meetings/2026-09-01 SyncUp Dev (23877)]]

**Cristian Berrío**: ¿Tesola o Sí. Fanta
**User guest**: Hermano, buenos días.
**Cristian Berrío**: días, buenos días.
**User guest**: ¿Cómo está todo?
**Cristian Berrío**: Excelente.
**User guest**: ¿Estás en oro?
**Cristian Berrío**: Lo de o sea, lo de la automatización, continuando con eso.
**User guest**: ¿Cómo quedamos? ¿Cómo se oye?
**Cristian Berrío**: Bueno, ayer no busqué lo de lo del problema ese. Pero lo que pienso que que va a arrojar en ChatGPT y eso, es tomar un contador para que el padre que tenga dos hijos en el mismo equipo no no reciba dos correos.
**User guest**: Correcto.
**Cristian Berrío**: Hacer una especie de contador por cada padre, de un equipo,
**User guest**: No.
**Cristian Berrío**: y si, pues, el padre llega a más de o sea, dos, pues no no se le envía el el otro correo a ese padre. Y se reinicia. Para cada día. Hay padres que tienen estudiantes en dos escuelas distintos. Bueno, dos equipos, pues. Ya.
**User guest**: ¿Y cómo vas con la con la ejecución de ese de esa parte?
**Cristian Berrío**: Ya estoy ejecutando el cambio. Porque, o sea, lo del coach para que llenen el la asistencia, eso eso es fácil. Y lo del parent, sí, para cuando no vaya el hijo, también es fácil. Y se hace lo mismo de de que no se le el mismo correo, Ah, bueno, ¿Me entiende? Ese sí, pues, they were. Porque puede que un hijo vaya y lo otro no, no sé. Entonces, sí se le envía Por eso sigue igual. Pero es que el problema fue el tema de las de las de las sesiones. Para que se mostrara bien Porque, obviamente, yo podía poner que empezaba tipo, el start date y el el end date, y ahí ya fácil. El problema es que nosotros tomamos las sesiones manualmente, y hacemos el breakdown nosotros manual. Realmente, es el que nosotros guardamos. El inicio y el final. Entonces, guardar eso, desde go ahead level. Está difícil. Bueno, estaba. Que se viera, no no guardarlo, que se viera bien. Ese era el verdadero problema. Entonces, ya.
**User guest**: ¿Cuándo llegaste a la solución? ¿Ayer o hoy?
**Cristian Berrío**: Okay.
**User guest**: ¿Cuándo ya está la solución?, ¿ayer o hoy?
**Cristian Berrío**: El de las sesiones, ayer. El del ¿el qué? El de sea, ¿la que Pare no repita el mismo correo? Pues ya lo estoy haciendo. Estaba haciendo ahorita que estaba dando una llamada. Estoy esperando que termine de ejecutar. Y ya el de coach y el otro es más fácil. No tiene incidencia porque no usamos sesiones. Es un reminder de correo normal. Eso es breve.
**User guest**: Oh, ¿nos montaste todavía?
**Cristian Berrío**: No, te empecé correr más difícil. Los otros sí son más fáciles, otros
**User guest**: ¿O llevas trabajando las secuencias de los correos de las temporadas desde ayer, de temprano?
**Cristian Berrío**: sea, es que vos
**User guest**: Yo pensé que ya tú habías montado la estructura de todos los demás,
**Cristian Berrío**: No, no, no. O sea, está están las funciones hechas. No está el la automatización como tal terminada, no. Está la función edge. Y me me me demoré por por lo que te digo, las sesiones. Que no se estaban viendo bien. Pues, cuando cuando enviabas, cuando intentaba renderizar el correo, se veía horrible lo lo del breakdown de sesión.
**User guest**: Okay.
**Cristian Berrío**: Pero la las funciones de los otros dos ya están creadas. Solo es tipo, literalmente, poner enviar correo. O sea, pones el no de de de que recibo esa función, y el otro no de que mande el correo. Ya. Literalmente, eso.
**User guest**: Entendido.
**Cristian Berrío**: Eso demorar diez minutos. Voy a hacer las pruebas, pues. Veinte minutos.
**User guest**: Sí. Pero yo pensaba que ya nosotros el tema de las sesiones lo hemos arreglado con el correo que que hemos arreglado de de instalación. ¿No?
**Cristian Berrío**: De registración. ¿Cómo así?
**User guest**: Nosotros tenemos un correo de registración de confirmación que ahí se dan las sesiones. Y se supone que están ahí renderizadas correctamente, ¿no?
**Cristian Berrío**: Sí, pero recuerda que esto todo lo estamos haciendo desde vos y Leo.
**User guest**: Correcto.
**Cristian Berrío**: Entonces, si nosotros enviamos un correo desde nuestro website, hacer ese breakdown, no o sea, es sencillo, porque nosotros controlamos absolutamente todo en ese correo.
**User guest**: ¿Verdad que no se me había olvidado?
**Cristian Berrío**: Exacto.
**User guest**: Se me olvidó que era de nuestro website.
**Cristian Berrío**: Exacto. Nosotros solo podemos enviar como que unas sesiones en una, digamos, lista separadas por coma, y después tenemos que revisarlo en el correo. No, yo, como renderizo en el correo, los leo, les literalmente escribo el HTML, el código, Entonces es mucho más manual. Y es menos controlado. Esos correos.
**User guest**: No, por supuesto. Esta es un ambiente totalmente externo,
**Cristian Berrío**: Sí, sí.
**User guest**: tiene tiene mucho menos control customización. Se me ha olvidado que, bueno, exacto, sale el punto se me ha olvidado que los correos de confirmación eran atrás de nuestro website.
**Cristian Berrío**: Exacto.
**User guest**: ¿Nos sería mejor mandar esos correos de WhatsApp al agua para que nos web no nos flaqueen como como spam?
**Cristian Berrío**: Los de confirmación, ¿se puede hacer? Bueno, sí se puede, o sea, realmente, eso
**User guest**: Lánzate lánzate... Aquí tenemos al al notetaker de AI, es que tú con teléfono no puedo ver.
**Cristian Berrío**: Sí, sí lo he aprendido.
**User guest**: Ok. La tatua de, bueno, se lo tenga, esté prendido para que luego una plática sobre eso. Me gustaría ver si podemos nada más, Si podemos asegurarnos de que dentro de la plataforma de Google Level, este, end of this time is open until Friday. Deme un segundo.
**Cristian Berrío**: Ahorita te mando el reporte de
**User guest**: Yeah. It's
**Cristian Berrío**: Sí.
**User guest**: Ayer vi que se han registrado algunos niños de las escuelas que tenemos plagueadas. Que que separamos, que creamos donde creamos el access aparte.
**Cristian Berrío**: Bueno, realmente solo vi a uno,
**User guest**: Sí, yo también hay uno.
**Cristian Berrío**: Sí, vía uno de de esos.
**User guest**: ¿Cuánto gastamos?
**Cristian Berrío**: En total, ¿O solo los
**User guest**: Bueno, en eso en eso, en la en la segmentación de los de las escuelas bajas,
**Cristian Berrío**: Cuarenta y dos dólares.
**User guest**: ¿Y se registra nada más un papá a través de los ads o sin ads?
**Cristian Berrío**: Con ADT se registró un padre. O sea, voy a ver de pronto porque tú sabes que no falta el padre que se mete al ate y no lo hace, sino que lo hace después. Para ver si en alguna de esas escuelas se registraron ya manualmente.
**User guest**: Okay.
**Cristian Berrío**: O sea, ya, pues, a través de Safari y eso. Se metieron después.
**User guest**: Mhmm.
**Cristian Berrío**: Igual, bueno, también hubo registraciones en la otras los otros ad sets también. Y el ROA está en tres diez.
**User guest**: ¿Todas estas en tres días?
**Cristian Berrío**: El está en tres diez. Contando todos. Los
**User guest**: Soleo, soleo. Bueno, cuando me haces reporte, ¿Qué vamos a hacer?
**Cristian Berrío**: Yo termino hasta enseguida. No me demoro, la verdad.
**User guest**: Sí. Ya,
**Cristian Berrío**: Por ahí por ahí
**User guest**: Sí, sí, sí, ya, es que me estoy poniendo los zapatos para salir. Te comento acerca de un tema que estuve viendo esta mañana, Pero pero sí, definitivamente necesitamos reportes de ads para ver qué es lo que vamos a hacer con con eso, porque, a lo mejor, a lo mejor cambiamos la estrategia de ads para esas escuelas que están bajas, y cambiamos cambiamos la estrategia de videos. Con los dos videos que tenemos al mundo. Podría ser. Aunque aunque el vídeo es el que menos convierte, ¿cierto?, entre el flyer y el y el video, hay videos ahí que me los ha ha convertido en general, ¿cierto?
**Cristian Berrío**: Sì. Correcto.
**User guest**: Hay que utilizar
**Cristian Berrío**: Are you guys okay?
**User guest**: La mujer está hablando.
**Cristian Berrío**: Sí.
**User guest**: ¿Qué hacemos con Hicks?
**Cristian Berrío**: Sí, cien por ciento. Okay.
**User guest**: Listo.
**Cristian Berrío**: Ponía
**User guest**: Ok, hermano.
**Cristian Berrío**: terminé el el de los
**User guest**: ¿Terminaste qué?
**Cristian Berrío**: que terminé el de las rima, entonces ahora o sea, ahora que terminemos la llamada, lo lo apruebo.
**User guest**: Don't wake the reminders.
**Cristian Berrío**: Sí. Ay, no, lo otro, el otro, el otro. El de, sí, solo el de estar reminder. ¿Sabes cuál te digo?
**User guest**: Sí, sí, sí. El de seven day, seven day reminder.
**Cristian Berrío**: Ajá. Epa, ya.
**User guest**: Pero ¿terminaste todos los reminders o nada más eso de seven days?
**Cristian Berrío**: Ese, o sea, los otros pueden pueden crear las branches. O sea, los los dos nodos que te dije. Y aprobarlos todos, pues.
**User guest**: Ok, excelente. Bueno, vamos a terminar esta secuencia Un una una nota a considerar, con el tema de los con el tema de los correos que vamos a estar mandando toda la semana, que los estamos mandando, los vamos a mandar un día antes de la práctica. ¿Tú entendiste ese punto? No.
**Cristian Berrío**: O sea, el de los el de, por ejemplo, el de quince días, siete días y un día, es un día antes.
**User guest**: No.
**Cristian Berrío**: O él estaba hablando de los weekly,
**User guest**: No. That weekly.
**Cristian Berrío**: Ah, ok, ok, ah, bueno, entonces no importa. Okay.
**User guest**: Ok, vale, quizás ya lo mandamos un día antes, o sea, que el de los weeklies no lo vamos a mandar al mismo día de práctica. Se mandan un día antes de la práctica, están estructurados a nivel de gramática, y mensaje, y sustancia, para que se manden un día antes, y también es lo más estratégico, para que funcionen más como un reminder de cambiar la práctica, hay que, mira, ya hoy tomemos práctica esto es lo que va a suceder, ¿me entiendes?
**Cristian Berrío**: Sí. Sí, entiendo.
**User guest**: Serían serían ocho días antes de la práctica. Que se tenga que mandar ese mensaje. Y puedes poner literalmente multiplica ocho por veinticuatro, o sea, puedes ponerlo literalmente a la hora que comenzaría la práctica, ocho días antes. Tipo tres de la tarde, ocho días antes.
**Cristian Berrío**: ¿Cómo ha sido ocho días antes?
**User guest**: Sí.
**Cristian Berrío**: O sea, por ejemplo, yo tengo yo tengo práctica mañana martes, envía hoy. O sea, se envía ayer. Lunes.
**User guest**: El de seven day.
**Cristian Berrío**: El
**User guest**: Digo, disculpa, en ocho días antes. Veinticuatro horas, exacto, veinticuatro horas antes en cada práctica.
**Cristian Berrío**: Ah, iba decir, como así, ocho días. Ya ya atendí.
**User guest**: Eso de ocho días, no sé qué estás pensando.
**Cristian Berrío**: Okay.
**User guest**: Creo que me confundí con con el Seven Daily. Le la lógica de un día, pero no, la lógica se supone que aplica para los weekly, se manda un día antes de cada práctica. ¿Sí?
**Cristian Berrío**: Okay. Sí, claro.
**User guest**: Ok, hermano, referente a tasks, no, o sea, ya este punto, este nivel, no hay espacio para no tener las cosas anotadas, organizadas. Qué me refiero con eso? La semana pasada hablamos de el website de OIB, y poner el el botón de tres d, la área de los en el área del hero, y también cambiar la el tour tres d. Con básicamente, montar el prompt de Hicks, las fotos, de Higgs, utilizarlas, básicamente, montar las fotos que se tomaron, profesionales. Eso fue un trabajo que hicimos en el año, para luego montar esas fotos, usarlas con a través de Hicks, convertirlas a las dimensiones necesarias para poder ejecutar el tour tres d, ya que se puede dar dentro de website. Claramente, también mucha gente me pregunta cuando me llaman, quiero ver el website, etcétera, si el botón está ahí mismo, yo le digo a la gente, mira, el botón está ahí mismo, venue. A lo mejor no es un tour en persona o o lo que sea, pero le da como que un entendimiento de cómo se ve el espacio. ¿Sí?
**Cristian Berrío**: Mhmm.
**User guest**: Te te pregunto, ¿qué pasó con eso?
**Cristian Berrío**: Yo lo hice.
**User guest**: ¿Cómo así? No está en el website.
**Cristian Berrío**: Tú te metes al top tres d, ahí están las fotos.
**User guest**: El botón del tour tres d no está en el hero.
**Cristian Berrío**: Eso sí me faltó. Pero las imágenes de ese ajustar ni están ahí. Falta faltó, sí me faltó lo del tour tres d. En
**User guest**: ¿Y tú le dices tú tú hiciste hicks para el tour tres d? Yo ni siquiera
**Cristian Berrío**: No, no, no, no utilices hicks. O sea, y hay que ajustar el tamaño de las imágenes. Y, o sea, no es necesario usar Hicksfield para eso. Porque, realmente, o sea, si tú vas a ajustar el tamaño de una imagen, eso lo puedes hacer hasta en una plataforma gratis. Me entiendes? Entonces, o sea, usar Hicksville no no era necesario. Usarlo. Yo ahí tengo
**User guest**: En teoría, como que sí. Yo pienso que sí. Mira esto. O sea, tú puedes agarrar todas las fotos que hemos tomado en webs del del venue, que son bastantes, y lograr que hits haga la historia completa, porque estas fotos se ven cortadas. Mira,
**Cristian Berrío**: La segunda, pues, ay, pero la segunda ya nada que hacer.
**User guest**: ¿Cómo que no hay que hacer?
**Cristian Berrío**: O sea, la segunda después te la genera O sea, la tomaron mal, desde un principio, O sea, hay fotos que se pueden ajustar y que se ven bien, o se ve natural, el tema de de alargarlas. Pero esa esa es como quien te dice, la tomé vertical, y, o sea, ya tiene un formato muy distinto.
**User guest**: Pero es que el tema, ya nosotros tenemos foto vertical, nosotros tenemos fotos digitales de ese mismo espacio. O sea,
**Cristian Berrío**: Pero es que, o sea, mira mira mira cómo, o sea, yo me yo me entré a la carpeta de Dropbox que tú me pasaste,
**User guest**: Entiendo.
**Cristian Berrío**: y literalmente la segunda foto de el
**User guest**: Sea, mi punto es, yo sé que las carpetas de Dropbox, a lo mejor, tendrán fotos que no estarán bien, pero para tú generar fotos con Hicksfield, ¿verdad?, y generar fotos que sean, que tengan la de que que puedan ser visualizadas de una buena manera a través del tour tres d. Puedas utilizar las fotos que tenemos históricas del venue en general, ¿verdad?, y ya con los con los toques de renovación que tenemos, puedes como que dar instrucciones de, por lo menos, la área principal, la área de recepción, te puedes fijar que en las dos fotos es igual. Así que, Hixion, al tú meterle estas fotos a Hixion como como source, para que te expanda la foto y te cree algo algo que va a funcionar para el tema de los tours, va a ser funcional. ¿Por qué? Ya tú tienes varias fotos de diferentes ángulos, horizontal, vertical, grande, pequeña, etcétera, para que Jisio tenga un entendimiento mejor o un mejor entendimiento del espacio, te genere la foto que tú necesitas. O sea, lo que tenemos en Dropbox no es lo único que tenemos al venue, es lo que me refiero. No sé si pensaste en eso.
**Cristian Berrío**: Ya. Si sí, sí, yo pensé en eso. Solo que, cuando yo pues, por lo menos la de welcome, que intenté alargarlo lo máximo posible. Se generaba una foto completamente distinta. O sea, los elementos que ponía a la derecha izquierda para que se viera así alargada como las demás, O sea, era una
**User guest**: ¿Y qué le está dando
**Cristian Berrío**: una zona
**User guest**: que le estás dando como feed, que foto le está dando como feed,
**Cristian Berrío**: La la de webcomedia y la otra de la que está literalmente al lado. La que es ya como como la zona para entrar. Tiene otro cartel y un televisor.
**User guest**: ¿Y esa foto dónde vienen? De Dropbox, el Dropbox link.
**Cristian Berrío**: Sí.
**User guest**: Del link de Dropbox.
**Cristian Berrío**: Sí, esas esas dos bien de Dropbox.
**User guest**: ¿Y por qué no utilizaste las fotos de source con...? ¿Por qué no le no le metiste tan bien a Hicks para que tenga un mejor entrenamiento de las pasos de la que ya tenemos de de Daniel. Tipo general,
**Cristian Berrío**: Porque, o sea, la la entrada, otra foto distinta.
**User guest**: Sí, de la entrada. Sí. Sí. O sea, la entrada, del espacio, o sea, realmente el venue sigue siendo lo mismo, Lo único que se cambió fue el piso. Cualquier cosa, literalmente, le puedes pedir a Higgs, que utilice el mismo piso en todo el venue. O las fotos viejas, las nuevas. La pintura en la pared. Y como ya tienes un color real del piso, y tienes un color real de la pintura de pared, puedes lograr que se vea igual en dos partes. Y puedes expandir las fotos. O si en el momento, o sea, a lo mejor tú no llegas a esta conclusión tú solo, hermano, pero si en el momento tú llegas a la conclusión de que esto no es posible y las fotos quedan bien y sabes las fotos del tour, yo no las estoy revisando ahorita, pero este, o sea, no las había visto. Pero las estoy revisando ahorita y no no no no se hicieron como tenían que haberse hecho. ¿Me puedes preguntar o me puedes decir, mira, estoy teniendo problemas como que las fotos me hagan esto y podemos idear sobre lo que tenemos, porque claramente yo tengo el contexto de todo lo que tenemos sobre OIB, tú también, pero a lo mejor como que no conectas esos dos puntos.
**Cristian Berrío**: O sea, a ver, las fotos nuevas del piso quedaron como la la las otras fotos que tú habías aprobado, en las primeras del tour, antes de los cambios. Así, o sea, quedaron así, tal cual, como como a ti te gustaron anteriormente. La única que siento yo que si hay que ver cómo ajustarla, es la segunda, La segunda sí es la que está como como medio rara. Se se ve muy vertical. El resto, o sea, está como tú habías aprobado inicialmente, la primera vez que hicimos esto.
**User guest**: Bueno, certamente. O sea, la idea hacerlo una segunda vez es que podamos mejorar lo que ya tenemos.
**Cristian Berrío**: O sea, tú
**User guest**: O sea, lo que veo aquí,
**Cristian Berrío**: tú exactamente qué es lo que quieres que que pase?
**User guest**: Hermano,
**Cristian Berrío**: O sea, tú quieres que pase entre sesenta. Porque eso era intentado.
**User guest**: claro, yo quiero que el venue se pueda apreciar de una mejor manera, por supuesto.
**Cristian Berrío**: Por eso, no, no, si tú quieres que sea un tres yo lo he intentado. La primera vez. Y me demoré bastante, bastante con Hicksville, con todas las herramientas que te puedas imaginar, haciendo un tres sesenta. Y es muy complicado, o sea, slash, no sé si se pueda hacer realmente. No pagamos una plataforma que te haga los tours virtuales.
**User guest**: Bueno,
**Cristian Berrío**: O sea, un tres sesenta yo no lo veo.
**User guest**: yo tampoco lo creo que tampoco veo necesario que sea entre sesenta. No es la no es necesariamente el objetivo. Pero, ciertamente, el menú se puede ver de una mejor manera, o sea, puedes apresar y venir de una mejor manera, si acomodamos las fotos un poco con Ciertamente, con los nuevos modelos de Hicksfield, hace, o sea, hacen magia con las fotos que que generan, o sea, yo he hecho muy buenas cosas con y lo que toma es un prompt. Sea, literalmente no, tomas un un prompt y las fotos correctas, como source.
**Cristian Berrío**: Okay.
**User guest**: ¿Entiendes? Sea, y está bien, está bien que no lo, o sea, a lo mejor si no lo quieres hacer, por por lo que sea, hablar al respecto, cómo se puede hacer, una vuelta, lo que sea, o me meto, yo lo hago. Pero tenemos que hacer algo al respecto, o sea, no podemos como que ni siquiera tener una conversación al respecto, ¿me entiendes?, como que no no debería ser.
**Cristian Berrío**: No, claro. O sea, bueno, o sea, yo puedo puedo intentar hacerlo tres sesenta, por lo menos el área ya de de del espacio como tal. Donde está la gente. Donde está el proyector y todo eso.
**User guest**: ¿Cómo lo haríaste en sesenta? Vas a pedir la hicks que te dé, o sea, yo entiendo cómo cuál es el proceso para hacer eso.
**Cristian Berrío**: Le pasaría todas las imágenes disponibles O sea, porque el varias imágenes. De los cambios que hicieron,
**User guest**: El drive también.
**Cristian Berrío**: Sí, pero la idea es que usemos el Dropbox, porque, vamos a usar un source, de un piso, distinto, o sea, como dos sources distintos, ya, o sea, sea, de por sí, ya ya ya va ser complicado. Le metemos otra complicación, que es el piso está el uno en uno y el otro está distinto. Like,
**User guest**: Bueno.
**Cristian Berrío**: Igual, o sea, por eso el Dropbox tiene toda la, tiene foto de todos los las paredes y eso. O sea, tiene la misma la misma, el mismo espacio, tiene varias fotos. Entonces, o sea, con eso se puede se podría ser suficiente source para para crear algo. El único tres sesenta que se podría hacer es ese, porque, bueno, la la cocina y el otro coso pues, ya no tiene mucho sentido hacer un tres sesenta.
**User guest**: No, no es no es un tres sesenta, o sea, pon nada más expandir la foto o no sé.
**Cristian Berrío**: Sea, pero tú ya viste cómo quedaron las otras fotos.
**User guest**: Sí, sí, sí.
**Cristian Berrío**: Y tú sientes que hay que expandirlas más.
**User guest**: Las fotos generales del venue,
**Cristian Berrío**: La de
**User guest**: ¿Cuáles fotos, a qué fotos están?
**Cristian Berrío**: de adentro, o de la cuatro adelante.
**User guest**: Oh, sí, sí, no, pienso que están bien, o sea, pienso que están pienso que están bien. Podrían ser mejores, como que el no o sea, para un tour tres d como tal, para para una presentación tres d, pienso que podría mejorar. Pero pero, ajá. Es un tema ya de Por eso es que te digo, yo pienso, opinión es, ni siquiera ni siquiera tocando un tema del tres sesenta, porque yo pienso que eso es otro problema aparte. Yo lo que pienso es, agarro las dimensiones que yo te pedí que extraigas de de lo que te pide esa plataforma. O que agarras lo que las dimensiones, los espacios, etcétera. Luego montas luego montas, agarrás esas dimensiones, luego las montas dentro de una dentro de un prompt, donde agarras las fotos que tenemos actuales del venue, y le pides que te que te aterrice esas dimensiones, manteniendo el espacio, manteniendo la integridad y el y la y aspectos ultrarealistas del espacio, o sea, manteniendo la realidad, que no crea algo que sea real o que no pongan elementos que no existen, etcétera. Pero que agarrando todas esas fotos como source, expanda la foto, para que dentro de esa experiencia donde tú vas a ir dándole clic a cada foto, ¿verdad?, se vea precio un poco más al espacio. Yo pienso que, o sea, Hizo debería tener la habilidad de hacer eso. En vez de ponernos a hacer algo de tres sesenta, que ya es como que un paso más allá, no veo la no veo la necesidad de de complicarnos tan allá. Porque ya sea, un tour tres sesenta, hecho, con IA va a ser un flujo muy es posible, no es imposible, pero va a ser un flujo muy técnico. Es decir, hay la probabilidad de que algo se salga del lugar, o que algo esté mal puesto, etcétera, sube. Que son muchas, o sea, va a tener que generar muchos espacios. Que actualmente no sabe como qué qué son y que existen. En cambio, si tú fotos que tienen ya, si tú me dices que ya en el Dropbox hay suficientes fotos para generar esta foto, ya ya está su respuesta. O sea, tú mismo me estás dando la respuesta.
**Cristian Berrío**: Sì, sí, hay bastantes fotos. Bueno, de welcome area solo está esa y está la otra.
**User guest**: Ok, entonces agarremos las fotos de que son las anteriores, es igual. Y le pides a le pides a Eix que te deje el piso igual, a las a las otras fotos. Ya con un punto de referencia es mucho más fácil crear generativo. Ese punto de referencia, ya tú puedes darle con todo. ¿Por qué? Porque ese punto de referencia, te le dice, Alea exactamente cómo es el piso, tienes que describirlo. Por ejemplo, si nosotros antes de comenzar ese proyecto, y renovar ese piso, nosotros ya estamos tratando de generar el piso como se iba a ver con con hits y con chat, etcétera. Y era muy difícil explicarle el color el color, el tono de la pared, piso, que lo cambié aquí, que lo cambié allá, etcétera. Ahorita que ya está hecho, tienes una referencia exacta sobre cómo debería ser. No tenés que inventar nada. Si yo te dijera, mira, ¿creías que es la el mes que viene? Vamos a poner un un piso azul. Piso azul claro, que es como esta foto y te mandó una foto. Ponle ese piso al venue, que ahí el flujo se vuelve un poco muchísimo más complicado.
**Cristian Berrío**: Yeah. Ok, no. Pero o sea, bueno, que quede claro. Entonces. Welcome, María. Y la otra y la otra que está del televisor? Antes de entrar, Ah, bueno, esa esa se cambia, Sí, sí, sí.
**User guest**: Esa es la misma área, esa es el área de recepción, esa área es la misma.
**Cristian Berrío**: No, sí, me refiero a que esas se cambian para alargarlas un poquito más. No hacer las tres sesenta, pero como dices tú, alargarlas más. Y el resto, ya en el salón como tal, también se van a alargar más o te parece que así es también? O se alarga
**User guest**: Alarga todo eso también, alarga todo eso también.
**Cristian Berrío**: Por eso, pero van a seguir siendo fotos. O sea, van a seguir siendo las mismas fotos un poquito más alargadas.
**User guest**: Por supuesto.
**Cristian Berrío**: Pero no tres sesenta.
**User guest**: Por supuesto.
**Cristian Berrío**: Ok. Ok, ok.
**User guest**: Con las dimensiones que te pide que te pide esa plataforma, que yo te dije, mira, ¿cuáles son las dimensiones de esto? Para saberlo para el futuro.
**Cristian Berrío**: No.
**User guest**: ¿Te acuerdas que yo te pedí que sacarte las dimensiones?
**Cristian Berrío**: Sí, y eso están, y yo yo usé esa dimensión, esas fueron las dimensiones que yo usé. Alargarlas un poquito más. La cuestión es que, por ejemplo, las vainas así como del welcome, estaba en una dimensión completa, o sea, le faltaba demasiado a esa dimensión, y cuando intenté generarla, tipo, espacio sobrante, no no, o sea, me inventaba una un espacio distinto. Entonces dije, bueno, ya, lo dejo así. Y fue cuando por eso te etiqueté y dije como que, mira, así. Ver qué qué precio estabas tú.
**User guest**: Claro. Entendido. Entendido. No extraño esto para nada. Ok. Entonces, punto hacia lo que sucedió con esta parte. Entendemos los dos que tenemos que trabajar en comunicación, o sea, este tipo de este tipo de cosas es especialmente cuando estás tomando una decisión sobre algo que realmente no queda claro, y, a lo mejor, no entiendes la importancia de lo que estamos tratando de hacer. ¿Entiendes? Como que, lo mejor, lo que yo te estoy diciendo es como que, mira, esto no tiene sentido, no entiendo por qué, no entiendo por qué, este, estamos haciendo esto, yo te puedo explicar cuál es el sentido, los clientes necesitan ver el venue, porque necesitamos que las fotos se hagan en una experiencia más más, especialmente cuando lancemos ads, porque estamos a punto de lanzar ads, tenemos que alguien llegue al venue y sepa exactamente cómo se ve el venue, y que no me juegan la vida, poniéndome a hacer poniéndome a hacer tours, etcétera, sino que se sientan más, este, más más cómodos con la decisión de bokear un venue online. ¿Me entiendes?
**Cristian Berrío**: Sí.
**User guest**: O sea, el al final del día ese es el objetivo, que que el proceso sea más cómodo, más sencillo para el cliente y que puedan ver espacio de una mejor manera. No solamente con una galería, que tengamos abajo, que sea un botón en el hero, en la página de hero. ¿Sí?
**Cristian Berrío**: Correcto.
**User guest**: Excelente, entonces, ese punto. Otro punto, avances. Necesitamos los avances dentro de Clico. ¿Por qué? Porque yo sé que a veces hablamos por WhatsApp, yo a veces tomé esto en la calle, y a veces hasta se me hace más cómodo hablar por WhatsApp, porque estoy hablando con cinco o seis personas a la vez por WhatsApp, porque estoy manejando, sé, diferentes tipos de de pendientes y y cosas que estoy trabajando, desarrollando. Entonces, al final del día, necesitamos dejar lo que sucedió. Digo, ¿por qué? Porque en la en la mañana, siendo, o esa misma noche, yo me vuelvo a meter en clic y desde un solo lugar, yo trabajo en lo que vamos a hacer al día siguiente. Al yo saber en dónde quedamos y qué es lo que tenemos que hacer todavía, este, dentro de clic o por lo que sea que estemos haciendo, este, me ayuda a mí mejor saber, mira, esto es lo que todavía nos falta, aquí nosotros nos quedamos, cuál es el próximo paso. Este, sabemos en qué dirección nos vamos a mover. ¿Sí?
**Cristian Berrío**: Sí.
**User guest**: Entonces, dentro de cada dentro de cada dentro de cada subtask que trabajemos. Ve dejando los avances a medida que vas trabajando, no esperes al final del día, no esperes verlo dejando a medida que vas trabajando, así no se siente como algo fastidioso. Especialmente cuando tienes un MCP, que es literalmente un comando un avance. Que básicamente es lo que has estado haciendo todo todo este tiempo. Literalmente, no toma mucho.
**Cristian Berrío**: Ayer como como nos pasamos todo media jornada, en llamada. Y no creamos ningún task de click up, sino que solo lo como que las cosas las íbamos hablando y las íbamos haciendo.
**User guest**: Mhmm.
**Cristian Berrío**: Como que ahí sí, como que, bueno, no quedó nada prácticamente en no. Prácticamente, no, no quedó nada documentado ayer.
**User guest**: Sí, no, está bien, o sea,
**Cristian Berrío**: Pero normalmente cuando entren las notas y eso, intento decir como que lo terminé, y si no tiene ningún comentario y no tiene ningún estatus cambiado, pues es porque no lo toqué. Directamente.
**User guest**: Mhmm. Sí, o sea, me refiero a, por ejemplo, entiendo en durante la jornada, claramente estamos trabajando juntos, no sé, falta, a menos que claramente sea algo que necesitamos documentar para futuro, etcétera. Que dejemos mucha planta en algún lugar, Claramente, si estamos juntos, no zapata, Dejar dejar updates. Bueno, aunque a veces estamos juntos, pero tú ves que allá yo estuve con Jacinthe, contigo y con clientes, etcétera, y a veces ni siquiera hablar sobre lo que está sucediendo, porque tú vas avanzando y yo, a veces ni siquiera puedo lograr a tener... O sea, mis avances son en otra en otro sentido, porque estoy manejando cosas al mismo tiempo. Entonces, aun así estemos en una llamada, yo diría que hasta tendría sentido que vayamos dejando que nos hace documentando, cuando yo vuelvo a hablar contigo, ya tenemos algo que Están llamando hoyos a Leo. Este es el tipo de cosas que me refiero, o sea, esto es una locura total. Un segundo, Joao. Aló, hermano.
**Cristian Berrío**: Estoy, estoy.
**User guest**: Me están me están vendiendo websites.
**Cristian Berrío**: Imagínate.
**User guest**: Me estaban in the websites. Te compro cuatro ya mismo.
**Cristian Berrío**: Lo sé en un día tú.
**User guest**: Literalmente. Bueno, ese es el punto, por eso es que me da amor. Crear websites, hoy en día, están me imagino que las personas que se dedican a esto están tan profitable. Están le le están lucrativo.
**Cristian Berrío**: Sí.
**User guest**: Literalmente, es una es un hack, es un hack de de avance. Y creo que Google también sacó un qué?, la gente pone un poco basura dentro de los website para rankear más arriba,
**Cristian Berrío**: Mhmm.
**User guest**: en en el search engine, etcétera. Usa como una herramienta donde están autorizando un poco de día para bañar, webs de que abusan de esto.
**Cristian Berrío**: Ya. Sí, porque antes era complicado como que las personas manualmente estuvieran bien los rankings y todo.
**User guest**: A la gente que hacía eso antes. Ok, Otro punto, conversiones que tenemos y puntos que tenemos pendientes. Dios mío, aquí no hay nada de estacionamiento. Si estamos hablando sobre cosas que tenemos pendientes, activa clic agarras la nota que tenemos de activar Whisper, agarra la nota que tenemos de ClickUp, y mete esas notas en un algún tipo de flujo de de chat o lo que sea, para que te genere accionables. A veces yo te digo direcciones, a veces, trabajamos planificaciones a la marcha. Y yo no tengo el el momento de dejarte todo bonito, bello, hermoso, de troclical, Entonces, por ejemplo, con lo que pasó con la página de tours, no confía en tu memoria para este tipo de cosas. ¿Por qué? Porque yo me voy a tener que devolver yo reviso algo que te dije de manera explícita, y no está, como que no no se hizo. ¿Entiendes? Entonces, está bien que este tipo de cosas funcionen, o sea, a veces se escapan cosas, sí. El hecho de que no tengamos de que no se le hicimos una herramienta que tenemos ahorita para trabajar con organización, que no nos permitan a nosotros tener un proceso más fluido para atacar los los temas pendientes, este punto no debería suceder. ¿Por qué? Porque, literalmente, son dos botones que toman sea, dos teclas que que que que se necesita activar risk Se tienen las dos teclas, y Whisper te toma todas las notas y no se escapa, pero absolutamente nada. O sea, esto era antes, de tener este tipo de herramientas que las cosas se escapaban y había más margen de error. Ahorita no debería, ahorita el margen de error se trata de otro tipo de cosas. Por ejemplo, el margen de error ahorita debería ser temas de comunicación, Ah, mira, el tema de los no se hizo como nosotros queríamos que que se hiciera. Bueno, más, a ver, nos vamos a hablar sobre qué es lo que tenemos que hacer y lo arreglamos. ¿Me entiendes? Como que ahí es donde está el espacio para el margen de error, nosotros deberíamos tener margen de error. ¿Por qué? Porque tenemos todas las herramientas necesarias, tenemos todos los sistemas necesarios para poder trabajarlo el desarrollo de los proyectos que estamos teniendo. ¿Me entiendes?
**Cristian Berrío**: Sí. Sí, entiendo.
**User guest**: Este, literalmente, el hecho de que ese ese tipo de cosas se escarpe, es una, o sea, refleja, yo no sé si utilizaste Whisper en un momento, lo que sea, pero refleja que no estamos utilizando las herramientas de manera adecuada, porque si fuese el caso, no nos hubiese pasado ese tipo de cosas. A menos, que claramente ya se nos haya escapado después de haberlo tenido después haberlo tenido anotado por ahí, etcétera. Por lo que yo vi, no vi ni siquiera un no vi no vi ningún ningún task, ni ningún ningún checklist, nada, Al respecto
**Cristian Berrío**: No, sí, eso es yo yo creo en task.
**User guest**: de de los cambios de la la página de de tours, y los cambios que le hicimos a
**Cristian Berrío**: ¿Cómo que no? Si te metes a
**User guest**: ¿Me entiendes?
**Cristian Berrío**: te metes te metes a agosto veinticuatro, cambiar tres d tours para hoy,
**User guest**: Ah, está todo.
**Cristian Berrío**: y te puse exactamente qué es lo fue lo que Claro.
**User guest**: ¿Y este botón del del hero también?
**Cristian Berrío**: Lo elegí,
**User guest**: O sea, lo que se está tratando de lo que tratando de llegar es porque el botón del hero no se incluyó. Es un tema de documentación, o sea, ¿qué qué sucedió?
**Cristian Berrío**: No, eso sí se lo copió. O sea, eso sí se me se me pasó. En el Whisper. Pero yo utilicé Whisper. Porque yo lo que cogí fue lo que hablamos en esa llamada, lo metí literalmente a y de saqué las imágenes, pero no se me olvidó sacarlo del O sea, el botón no lo cogió. Cuando hablamos del botón, no no cogió eso. Porque, si te fijas, yo hasta cogí el botón de de book now, que me dijiste que incluyera. O sea, que tú me dijiste que
**User guest**: Wat dan de boek nou ik... Nee, nee,
**Cristian Berrío**: o sea, lo lo cambié a imagen. Me dijiste, coge el botón de book now, y mételo también en en out tours. Y ese ese
**User guest**: Correto, corretto, corretto.
**Cristian Berrío**: sí lo cogí, pero el otro el otro sí se
**User guest**: Escapó.
**Cristian Berrío**: o sea, se me se me pasó con Whisper y se me pasó
**User guest**: Entendido. Ok, perfecto. Tiene más sentido.
**Cristian Berrío**: Yes.
**User guest**: Eso tiene más sentido. Ok, listo, entonces. Sí, estamos encaminados por el por el camino derecho. Por el buen camino. Hermano, ¿estás disponible hoy en la tarde? Para conversar el tema del salario, lo que me estás proponiendo? Los cambios que tenemos que trabajar para ya formalizar el tema de tu el los porcentajes que se tienen que dar a tu a tu salud, etcétera, etcétera, etcétera.
**Cristian Berrío**: Sí, sí. Si quieres, hablamos de de de cinco. Cuando acabe.
**User guest**: Listo, activo. Acá cuadramos una reunión, entonces, a las a las cinco, revisamos lo que se hizo hoy y también cuadramos el tema de de te la propuesta de lo que vamos a hacer con tu salario. Y tú y tu paquete de beneficios de empleo.
**Cristian Berrío**: Dale, hermano, me parece, me parece.
**User guest**: Vale, miro buenísimo. Este, te dejé otro task para OIB, Aquí vamos a lanzar ants, at estáticos, vamos a comenzar implementando el tema de de API, etcétera. Básicamente, vamos a copiar y pegar la estructura que aplicamos en Doctor, que esa estructura partiendo desde website es muy sustentable, y, definitivamente, es lo que necesitamos. ¿Por qué es lo que necesitamos? Porque necesitamos extraer toda la data posible nuestras plataformas actuales, es muy sustentable en el sentido de que podemos trackear el el mecanismo que las personas utilizan para la administración, para en caso de Entonces, básicamente, vamos a agarrar todo
**Cristian Berrío**: Mhmm.
**User guest**: todo lo que hemos aprendido a DVR, vamos a implementárselo en a Pienso que para AOIB lo más funcional va ser sacar ads estáticos, Pienso que videos funcionarían, pero primero vamos a hacer unas pruebas con at estáticos, vamos ver cuál es nuestro roas. Y vamos a lanzar otro set de ads luego con videos, y ver si en robas sube o baja.
**Cristian Berrío**: Vieron?
**User guest**: Pero en vez de lanzar videos y fotos juntos, vamos a vamos a primero fotos estáticas. Como antes, y luego esas fotos este, nos vamos a lanzar increíble, esto es increíble. Luego, esas fotos no, lanzamos, este, esas fotos le usamos otro set de ads con, específicamente con videos.
**Cristian Berrío**: Okay. Me parece. Tiene sentido.
**User guest**: Excelente. Hay que abrir cuentas de redes sociales para OEB, conecta todas esas cuentas de sociales con el correo de Gmail, no ministries, sino Orlando Bienvenido. Si necesita un número de teléfono cuando está abriendo las cuentas de Meta, Instagram, Facebook, etcétera, o utilizas mi mi número de teléfono personal, Si necesitas un código, me avisas y te lo mando, Y, por último, este, ¿puedes montar como para que te, para tener algo de, o sea, monta tres publicaciones. Una publicación puede ser con el video que ya está dentro de OIB, Hay un video dentro de hoy vi que se editó con Julián, básicamente, es el como que él venía en diferentes snapshots, las otras dos publicaciones pueden estar utilizando las fotos de la renovación como que hablando de la renovación del dueño, etcétera. Se montan esas esas tres publicaciones para que haya algo en la cuenta de redes sociales o, a lo mejor, dentro de los mismos ants, utiliza la opción de que no se de que no se de que no salgan de que no salgan los los perfiles de Facebook, listo, para que las personas no se puedan meter, a nuestros perfiles y realmente allá a nuestro website. ¿Entiendes eso?
**Cristian Berrío**: Sí. No,
**User guest**: Que no tenga la opción
**Cristian Berrío**: Ajá.
**User guest**: que no haya ningún tipo de opción para que para que ellos se metan a nuestro perfil, simplemente que nada más pueda ser redirigido a nuestro webcam.
**Cristian Berrío**: Okay. Pregunta. Voy ir al final y hiciste lo que te dije del IT.
**User guest**: No, se me olvidó hacerlo. ¿Hasta cuándo tenemos tiempo?
**Cristian Berrío**: No sé. Pero en cualquier momento,
**User guest**: Ya.
**Cristian Berrío**: Sí. O sea, dice que es es requerido para el futuro. No sé si el futuro es mañana o pasado.
**User guest**: Interview.
**Cristian Berrío**: Y después nos va.
**User guest**: Entendido, bueno. Voy a meterme hacer eso hoy. Un mensaje de WhatsApp para que no se me olvide cuando termine ya de de estar, de de salir de esta locura, ¿no?, para esto metido ahorita.
**Cristian Berrío**: Listo, hermano. Listo. Bueno, voy a intentar crear los task así como tú me dices. Yo no sé cómo a ti te cree, o sea, a ti te te crean bacanos los task, eso.
**User guest**: ¿Dentro de ClickUp?
**Cristian Berrío**: Objetivo y todo. Yo cuando los creo cuando Sí. Yo cuando los creo con el brain, salen todos feos. No sé cómo le hace.
**User guest**: Oh, lo que pasa es que yo tengo una te puedes meter en mi click up, y puedes ver que yo tengo yo tengo dentro de click up, tengo una de hay un hay un, algo que se llama ClickUp Memory, algo así,
**Cristian Berrío**: Mhmm.
**User guest**: donde tú tienes donde tú lees instrucciones, y yo le digo, yo tengo una estructura sencilla, que le des el objective, entre otras que el un objective, una descripción y creo que accionables, no me acuerdo cuál era el tercero. Pero sí que sí, tengo, yo lento, le dije que antes de mostrar cualquier task, siempre monte un objective, y que monto el objective y que monto la descripción y como que los asignables de de ese task. Y como que lo agarras la estructura y lo montas, y queda nice.
**Cristian Berrío**: Sì,
**User guest**: Pero pero sí, me enteré, a ver qué que terminas qué terminas aterrizando. Y, bueno, con la estructura que yo tengo que, pues, agarrar de eso, para hacerlo tú también. Pero eso en sí, Brian, en realidad, es muy inteligente. O sea, Brain me impresiona, de verdad que me impresiona el nivel de el nivel de de conocimiento que tiene.
**Cristian Berrío**: Sí. Efectivo.
**User guest**: No, no no hay ningún GPT dos. Para que me meten le meten power a esa a esa gente.
**Cristian Berrío**: Sí.
**User guest**: Pero nada, mira, vamos al play. Este mes, ver cosas, estamos pendientes. Acuérdate que hay que levantar hoy, bien cero, También me metí en la carpeta o b b, no están las fotos de los logos, tampoco están las fotos nuevas de Dropbox, así que necesito que tengan esa carpeta al día de hoy, vi.
**Cristian Berrío**: Aquí todos son bastantes, ¿oíste?
**User guest**: Son bastante que
**Cristian Berrío**: Hay que usar la herramienta que tú la vez pasada.
**User guest**: che cosa?
**Cristian Berrío**: Que son bastantes, bastantes fotos. El
**User guest**: De del drop box que mandó Pablo. De las nuevas fotos.
**Cristian Berrío**: Sí, son bastantes.
**User guest**: Herman, no deberían ser más de cincuenta foto. Imposible.
**Cristian Berrío**: Es que cincuenta fotos es bastante, o sea, imagínate cargar una por una. Es lo que te digo.
**User guest**: Puedes escalar todo eso con un ZIP,
**Cristian Berrío**: Tal no son no son
**User guest**: puedes tú puedes tipear todo eso, ¿no?
**Cristian Berrío**: Pues la idea es que no esté en un ZIP, o sea, la idea es que salgan todas, ¿no?
**User guest**: ¿Cómo así?
**Cristian Berrío**: O sea, la idea es que la foto, cuando tú desde la carpeta baby, te metas y la veas así, en preview, no como un punto así que de Dropbox.
**User guest**: Bueno, tú agarras un, tú te metes en el en el link que yo te mandé, las descargas como un ZIP, abres la carpeta de SIP y le descargas la carpeta de SIP a OVB, ya.
**Cristian Berrío**: O igual, lo que voy a hacer es más fácil aún, y más bacano, es usar la herramienta que ya tenemos, para cuando pasamos el TeraBox a Drive. Que yo vi que esa herramienta tiene de de de Dropbox a Drive también. Entonces, le le pongo la ruta a la carpeta de Dropbox, y se la meto a a la carpeta de Drive.
**User guest**: También,
**Cristian Berrío**: Y ya, esto se ejecuta en background, sin yo tener que hacer nada.
**User guest**: También.
**Cristian Berrío**: Sí, se lo acabo de hacer. Esa esa está en el computador de Charlie's o el de Windows, no me acuerdo. Creo que está el de Windows. O tiene que estar el de Windows, sino porque igual ya no estás en tu casa, ¿verdad?
**User guest**: Correcto. No estoy en mi casa, pero según todo está atendido.
**Cristian Berrío**: Ya te confirmo. Bueno, mira, ahora sí está prendido. O sea, estoy conectando mal de Windows, pero está como lento.
**User guest**: Sí, bueno, está bien, entonces.
**Cristian Berrío**: Si no, cualquier cosa, pues ya lo hago manualmente. Ya, como tú dices, sí, punto SIP, y pongo el punto SIP en la otra carpeta. O sea, en en Drive. Hier.
**User guest**: Excelente.
**Cristian Berrío**: Yeah.
**User guest**: Bueno, buenísimo. Monto también los, por favor. Ese es otro tema que te había dicho también. Este, me dieras las, que montaras las fotos de nuevas en usar otro punto con lo con el tema de OVV. Y que los nuevos logos que los logos están ahí, yo no sé por qué ya no están en Google Drive.
**Cristian Berrío**: No.
**User guest**: Los nuevos logos de hoy vi, en brand assets, esa carpeta está vacía. Entiendo.
**Cristian Berrío**: No sé. Yo no he tocado eso. No no sé qué decirte.
**User guest**: Está bien, raro. Bien raro. Exacto. Busca bien y mándame la rotas.
**Cristian Berrío**: Sea, de pronto hay otra carpeta de branditas. Algún lower day?
**User guest**: De con que diga bebito o no sé. Me parece raro.
**Cristian Berrío**: Sí.
**User guest**: Pero adelante. Guau, esto es increíble. Pero bueno, mero,
**Cristian Berrío**: Pregunta, que está el Dropbox?
**User guest**: Adelante.
**Cristian Berrío**: ¿Al Dropbox de quién es?
**User guest**: El dropbox es la link que yo te mandé.
**Cristian Berrío**: Pero ¿eso es de alguna cuenta de nosotros?
**User guest**: ¿Cómo así?
**Cristian Berrío**: ¿O es de una cuenta de la imagen o comparte un link?
**User guest**: Es una cuenta bien más que nos comparte el link. Pero eso no harías ese flow tan complicado, eso es sencillo. Las fotos que mandaron, o sea, de los Samsung.
**Cristian Berrío**: Oh, ya, la la vamos normalmente, entonces.
**User guest**: Son menos de treinta fotos, descárate todo eso, ZIP abre el ZIP en tu computadora y móntale móntale la carpeta a OSB, eso es sencillo. O sea, hasta yo lo puedo hacer, pero te dije a ti, porque ya la había ya voy a estar manejando esas fotos y Ajá. Que los dos hagamos lo mismo, que uno haga las cosas de cero a cien y y ya, o sea, al final el día de hacer esa foto también fue un trabajo Ya eso tiene un un flujo que se ha estado desarrollando. Increíble. Increíble. Pero bueno, me bro. Ya ese link de él está en nuestro WhatsApp, si no lo consigue, está en WhatsApp, búscamete a nuestra conversación, en links, ahí está.
**Cristian Berrío**: No, sí, ya, ya lo encontré, relajo.
**User guest**: Excelente. Excelente.
**Cristian Berrío**: Okay. Bueno, estoy comentando, Voy a hacerle la foto enseguida.
**User guest**: Excelente, pero más la
**Cristian Berrío**: Dale, bueno. Aviso en todo? Cualquier cosa.
**User guest**: Listo. Vale.

_Sincronizado por Brain: 2026-10-21T01:46:57.626Z_
