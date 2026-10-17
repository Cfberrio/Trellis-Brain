---
brain_note_id: "dest:meetings:ccd2a77b9dcf9422ccf551e4556c43e5"
canonical_key: "meetings/ccd2a77b9dcf9422ccf551e4556c43e5"
brand_id: "meetings"
---
# Transcript — 2026-06-18 SyncUp Dev (21277)

## Transcript

- Reunión: [[02-Meetings/2026-06-18 SyncUp Dev (21277)]]

**Luis Torres**: Bueno, querido.
**Cristian Berrío**: Buenos días, mi hermano.
**Luis Torres**: ¿Cómo estás, Vero?
**Cristian Berrío**: Espérate, no te escucho.
**Luis Torres**: ¿Cómo está todo, Miro? ¿Estás en ok?
**Cristian Berrío**: Yes, no cosplay the d. Camisillita,
**Luis Torres**: ¿Por qué? ¿Tienes el meter?
**Cristian Berrío**: Ah, pues, hace culo de calor allí. Haciendo calor.
**Luis Torres**: Fire. O sea, es que eso aquí le dicen, wife beater, ¿Sabes qué es wife beater?
**Cristian Berrío**: No.
**Luis Torres**: Los hombres que le tengan las mujeres, le dicen, o sea, como que wife beater, bidding beating your wife. Entonces, es como como se Como los horarios se ponen esas camisas, le dicen West Better's.
**Cristian Berrío**: Curioso, curioso, el nombre.
**Luis Torres**: Sí, bastante. Los americanos hacen sus cosas, Mi hermano, cuéntame, ¿qué nos falta para Dispace? ¿Quieres presentar algo? ¿Tienes tienes algún más significante?
**Cristian Berrío**: Wow.
**Luis Torres**: ¿O lo mismo?
**Cristian Berrío**: ¿No sabes lo que te dije ayer? Yo ayer te dije, o sea, realmente, ya tengo son tres workflows. El de estatus ya está listo. El de remaining balance está listo, pero no lo he probado porque no tenemos Stripe. El de el último que faltaría son de los reminders. En los reminders ya tengo avances significativos. Pero falta una que otra cosita. O sea, tengo la lógica del código que envía desde nuestro backend,
**Luis Torres**: Mhmm.
**Cristian Berrío**: a Google high level.
**Luis Torres**: Okay.
**Cristian Berrío**: Falta es poner los nodos, que poner los nodos no tiene mucha ciencia. Ya están estas tres cositas.
**Luis Torres**: Okay.
**Cristian Berrío**: O sea, lo que falta son huecos, o sea, hay como huecos así, tipo algunos en la lógica, que me terminaste de pasar ayer, pero es a como estaba con el tema de automatizaciones, no he arreglado. Tanto como de front end y y y esas cosas. Lo que sí alcancé a arreglar ayer, que no se me olvidar, el tema de enrutar lo los pagos.
**Luis Torres**: Okay.
**Cristian Berrío**: Pero, ajá, no lo he probado porque no está strike.
**Luis Torres**: Claro.
**Cristian Berrío**: Lo dejé de de manera que, literalmente, lo único que falte es poner las cuentas de extracto.
**Luis Torres**: Y si es posible hacerlo, de la manera en que en que se en que se está aprendiendo,
**Cristian Berrío**: Sí, sí, cien por ciento es posible, eso no eso no hay problema, pero, ajá. Hay que, pues, probar que todo eso sirva.
**Luis Torres**: Claro.
**Cristian Berrío**: ¿Qué más falta también? El tema de añadir invoices, el tema de de poder mandar manualmente el remaining balance,
**Luis Torres**: Mhmm.
**Cristian Berrío**: Y, pues, ya los a los features esos chiquitillos que tenemos. De high level, que si mandar recurring invoices, o sea, todas esas cositas chiquitas que tenemos. Falta de eso. ¿Qué otra cosa? Bueno, lo de Deloft aún no lo tengo tan claro, si te soy cien por ciento sincero, Ya entendí lo de los pagos, más o menos, pero no lo tengo cien por ciento claro.
**Luis Torres**: We love s nosotros, básicamente, sí, lo, como funcionó, bebé, ellos recogen el pago del cliente, pasan por su cuenta de y la distribución es hacia nosotros. Ocho por ciento. Por Deloft.
**Cristian Berrío**: No, no, no, sí. Pero me refiero, en el momento del booking, digamos que ellos solo lo pueden añadir, no paga, o sea, no lo pagan realmente deal of eso es lo que me tienen enredado.
**Luis Torres**: Oh, es que no tenemos, o sea, como que, ¿te acuerdas que habíamos hablado de que le seleccionen el add on, el add on y no hacen más nada? Porque no tenemos que pegarle. Sí, eso es todo.
**Cristian Berrío**: O sea, por eso, ellos lo añaden y solo como que lo tenemos ahí. Pero como tal no lo pagan.
**Luis Torres**: No. No lo pagan porque no tenemos no tenemos la la opción de que, no tenemos precio, no tenemos nada de eso.
**Cristian Berrío**: Okay. Okay.
**Luis Torres**: Ok. Ok, mira lo que vamos a hacer hoy. Ayer, le mandé la propuesta al agente de Dispace. Porque se pusieron todos poppy con el tema de los se pusieron todos específicos con el tema de los de la del fee transacción, y, este, querían una querían un workaround, Yo pensaba que dentro de Stripe eso iba a ser difícil, como que poder como que direccionar diferentes pagos de o sea, hacer el split, y las transferencias de los pagos que vengan del cliente y va a ser difícil si lo hacemos por servicio, ¿no? Porque me imagino que dentro de la transferencia como hay diferentes montos, unos veinte por ciento, otros ocho por ciento, el mismo sistema internamente hace esas calculaciones y manda la transferencia, ¿cierto?
**Cristian Berrío**: Espérate. Sí. O sea, realmente, no tiene mucha ciencia. Porque o sea, Stripelet, realmente, es una herramienta que utilizamos para guardar la plata. Pero, realmente, o sea, nosotros podemos hacer lo que queramos y podemos distribuir los porcentajes como queramos, superpersonalizados, el tema de de calcular distintos fees y distintas digamos que montos que se van a transferir a diferentes cuentas. O sea, literalmente, solo es una herramienta guardar plata. O sea, no, él no es él no es nada estricto con eso.
**Luis Torres**: Por supuesto.
**Cristian Berrío**: Entonces, sí, o sea, realmente uno puede hacer lo que quiera, pues, lo que quiera, si le quiere sacar un dos por ciento únicamente a el cleaning fee, se puede hacer.
**Luis Torres**: Yeah. Está bueno, no sabía eso. Pero, bueno, el punto es, que yo como que empujé hacia atrás en ese en ese lado, y nada, lo que causó esa conversación fue que le mandáramos una propuesta con todo lo con todo la el replanteamiento de los fees, los servicios que le estamos ofreciendo, etcétera, eso están ellos por aprobarlo. Entonces, lo que vamos a hacer para movernos hacia adelante, antes de seguir, porque así lo construimos para dispatch o no, esto va a ser la maqueta que se la va a llevar a un venue, ¿cierto? Porque todo está como que estructurado. Lo único que habría que cambiar sería información, etcétera. Estoy seguro que vamos a trabajar con Dispace, simplemente no sé cuándo. Tenemos a otro venue que es mucho más sencillo, que tenemos que montar, Te tengo que montar la planificación para ese venue, vamos a trabajarla, El problema que tenemos con este tema es la área de PeerSpace, PeerSpace, ciertamente, es una plataforma que tiene mucho marketing muchas personas terminan y terminan encontrando el venue por PeerSpace. El problema de PeerSpace es que ellos hacen A ver, a ver. Connect with Stripe. No sé si PeerSpace se conecta con Stripe, pero el punto es que a medida que vamos que vamos manejando otros venues, aquí dice que PeerSpace integrates with Stripes to manage all of statement processing, payouts, and identification. I can't if you got it, see peer space se se conecta con Stripe, así podemos con, así podemos pasar ejemplos, si conectamos PeerSpace a Stripe podría redireccionar el dinero que entra a PeerSpace hacia dos cuentas, hacia la cuenta que recibe y la cuenta de management, que sería nosotros.
**Cristian Berrío**: No, ahí sí ahí sí, no creo. Porque
**Luis Torres**: Aún sí, lanzas el dinero Strike.
**Cristian Berrío**: o sea, sí, o sea, puedes realizar la conexión, pero realmente, o sea, es que el tema de integrar esos de pago es muy código. O sea, te estoy diciendo que Stripe no hace nada, Stripe uno lo que hace es como que la única configuración que abre un es conectar una cuenta a otro,
**Luis Torres**: Correct.
**Cristian Berrío**: Tipo, ponerle el el qué, la contraseña. Las de todas las tres cuentas. Pero de ahí adelante, es puro código.
**Luis Torres**: I'll commit I follow her.
**Cristian Berrío**: O sea, no sé qué tan manual De pronto, sí, de pronto sí no ha sido un user.
**Luis Torres**: El lugar eso,
**Cristian Berrío**: En para
**Luis Torres**: evalúa eso porque tenemos que tenemos que implementar eso para para para OEB, Actualmente, los pagos de de peer space no están cayendo dentro del nuestra cuenta Stripe, le caen directamente al AOBB, y necesitamos redireccionar eso, Necesito que averigües eso, punto número uno, para entender cómo vamos a trabajar PeerSpace con los venues hacia adelante, esa es como que la visión para eso. Créame una lista, punto número tres, por crea una lista, con las cosas que nos faltan para Dispace. ¿Cierto? Y así lo vamos a atacar a nivel de prioridad. Como que que nos falten automatización, etcétera. Lo que te falta hoy por hoy para terminar despaces escríbelo en una lista, y si falta información, para tener dispace, mételo en esa lista también. ¿Sí?
**Cristian Berrío**: Cuando tú dices qué es lo que falta terminar, es que lo que falta terminar, tipo, que ya esté funcional o qué es falta terminar que literalmente
**Luis Torres**: Todo.
**Cristian Berrío**: duplique al website?
**Luis Torres**: Que que que esté, lo que esté, lo que falta por montar ¿verdad?, lo que falte por probar, y lo que falte, todos los pasos de de lo que falta por montar y lo que falta por probar para irnos live.
**Cristian Berrío**: Okay.
**Luis Torres**: Así atacamos esa lista En el futuro no la vamos a atacar ahorita, Ahorita lo que vamos a hacer es evaluar el el la la reprogramación de de PeerSpace con Stripe, posiblemente, ver qué podemos hacer con eso. O crear algún tipo de de automatización para que los pagos se se se vayan de una cuenta a la otra y no tengamos que pasar invoices manuales por por lo que se hace por PeerSpace, Esto va a ser clave para el nuevo venue. El nuevo venue que vamos a hacer onboard, principalmente, va tener una presencia muy, muy importante dentro de PeerSpace. Entonces necesito resolver ese tema. Para montarte la planificación del dinero nuevo, Y cuarto punto, vamos a replantear el website y todo el el ecosistema de Doctor. Entonces, necesito que evalúe lo que tenemos actualmente, y des un plan a lo más lo más eficiente un plan, y un plan b, no sería tan eficiente, pero que sería como que lo mejor que deberíamos hacer. ¿Sí?
**Cristian Berrío**: Okay. Sí, está averiguando ese ya lo de strike para ver.
**Luis Torres**: Dale, métela a eso. Con Charlie, hablamos un ratico, pero averiguate esos puntos y hablamos más tarde.
**Cristian Berrío**: Listo, hermano.
**Luis Torres**: Como en media hora, cuarenta y cinco minutos. Hablamos sobre PeerSpace y sobre la Doctor. Parece?
**Cristian Berrío**: Dale, dale.

_Sincronizado por Brain: 2026-10-17T15:51:31.894Z_
