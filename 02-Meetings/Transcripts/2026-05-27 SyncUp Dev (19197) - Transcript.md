---
brain_note_id: "dest:meetings:553b5bbe6728467436c76141f9b7330b"
canonical_key: "meetings/553b5bbe6728467436c76141f9b7330b"
brand_id: "meetings"
---
# Transcript — 2026-05-27 SyncUp Dev (19197)

## Transcript

- Reunión: [[02-Meetings/2026-05-27 SyncUp Dev (19197)]]

**Luis Torres**: Hermanito,
**Cristian Berrío**: ¿Cómo estamos?
**Luis Torres**: Bien, tú consulta, tengo una consulta. ¿Estás listo?
**Cristian Berrío**: Dime.
**Luis Torres**: Quiero que el guest report de OIB se haga en el mismo website donde obtienen obtienen el el access code al principio. ¿Es posible? Lo nuevo que
**Cristian Berrío**: Vamos ver.
**Luis Torres**: lo único que ha lo único que veo que va a afectar es la automatización para que cuando se terminó el guess report cambié, estaba la broma, pero la realidad actual es que nadie llena el guest report.
**Cristian Berrío**: Mover la ruta de lo del guest report a lo del access code.
**Luis Torres**: Uh-huh. Que pongan ahí su su reservación y llenen el guest report.
**Cristian Berrío**: ¿Y cómo serías hasta que no vienen O sea, sería O sea, obviamente, debería en ver el nombre de la ruta. ¿No?
**Luis Torres**: Habría que cambiar de nombre la ruta.
**Cristian Berrío**: O sea, lo
**Luis Torres**: ¿Cómo así?
**Cristian Berrío**: access code. Slash access code. Primero que todo.
**Luis Torres**: No sé cuál es el número de ruta virtual,
**Cristian Berrío**: Se llama
**Luis Torres**: La tengo aquí...
**Cristian Berrío**: No, o sea, lo del que, o sea, que nombre le pondrías a la ruta. Para que incluya?
**Luis Torres**: La misma misma que está, o sea, no no hay problema. La misma que actualmente está. ¿La misma ruta?
**Cristian Berrío**: Okay.
**Luis Torres**: Yo la acabo de
**Cristian Berrío**: O sea, solo sería solo sería moverlo para que llene sea, el mismo, va ser el mismo reporte, solo que ahora va a estar la ruta de access con
**Luis Torres**: Correcto. Get access sort of guest, o o o guest report, algo así. O sea, tendríamos que ver el ya que me salga en un cliente. Hi there, this is Lou speaking. How can help you? Hi, this is Britney. How are you doing today? Hi, Britney, doing well. How about you? Good. Good. I was calling because I had booked and confirmed a event for June. I was calling because I was trying I'm putting all my records together and coming up with my calculations. For what I have left. By chance, are you able to send out an invoice Sure. For the book so booking that you currently have? Yes, please. Yes, sir. And I do have my reservation number too. Perfect. Let me look you up real quick. Thank you. One second. I just messed up my thing. Take your time. Alright. Cool. I see you here, Britney Jones. I see you. Yes. Perfect. We have your regalia booked up. We have your package ready. Alright. I just sent you the balance link. For what you will have to pay left. Yes. I just sent it to you. And would that also show, like, the beginning rate that we got as well? Yeah. So it's essentially basically, whatever you're now is what you paid at first. So it's divided by exactly. Yeah. I know that. Okay. Thank you so much. I appreciate you. Anytime. Anytime you take care, my friend. You too. Bye bye. Bro, fíjate que los invoices que llegan de OAB mira esto, Pero los invoices no muestran qué paga el cliente. Nada más muestran tipo, lo, cuando yo hablo del balance, nada más muestra el total. Muestra un breakdown. Y aquí tampoco puedo ver qué pagó, como que aquí puedo ver que tiene, que pagó algo, que pagó algo adicional, que claramente pagó el basic package, por cuántas horas, No, por cinco horas. Sí, eso es lo que le sube el precio. La terminó, sí, nada más pagó el basic package. Necesita pagarlo al beer and wine. Pero bueno, varios punticos aquí. Cuando estemos trabajando el nuevo flujo de los de los de la información de los de OEB, Es importante, cuando le mandemos estas cosas, lo de balance due, cuando paguen o cuando le mandamos lo de balance due, tengo aquí un invoice aquí abajo, un invoice de de lo que tienen que pagar, o en el payment confirmation se lo mandamos ahí el invoice, como con PDF, con el con el detallado de qué es lo que pagaron, con el processing fee, todo eso. Me mandaste ahorita un PDF, pero no tenía processing fee. Necesitamos que tenga el processing fee ahí reflejado. Actualmente, este invoice lo tiene, lo que no tiene es un breakdown de lo que está pagando, del de lo que escogió cliente, porque la gente se le olvida.
**Cristian Berrío**: se manda una vez. Tipo, depósito o los dos. Depósito,
**Luis Torres**: ¿Cómo así?
**Cristian Berrío**: O sea, eso se manda para el y para el balance, o solo un invoice para los dos?
**Luis Torres**: Depósito, un no es para el depósito, otro para el balance. Cada vez que hago un pago, la idea es que se les manda un invoice.
**Cristian Berrío**: Ok.
**Luis Torres**: Y fíjate que aquí,
**Cristian Berrío**: O sea, y va a ser, eso va a ser complicado. Cien por ciento, es para el remaining balance que se manda a través de level. Y eso es un correo estático. Que tiene city campus, pero es un, sigue siendo un correo estático.
**Luis Torres**: ¿Y no hay una manera de darles un recibo para cuando cuando terminen de pagar, algo así?
**Cristian Berrío**: Claro, lo puedes meter al recibo, pero, ¿cuál es? Punto? El punto es que la vas a tener que meter en recibo siempre cada vez que les va mandar O sea, ¿sí me entiendes? Es un manual. Para mandar el el el de remaining balance.
**Luis Torres**: Recomendaste, entonces?
**Cristian Berrío**: Ah, mentira, espérate, Ok, ah, no me dieron la confirmación. Entonces el invoice. O sea, se envía en la en la en la si se se envía es en la, cuando ya hacen el pago, o sea, no en el recordatorio de ingresa al link y paga. ¿No?
**Luis Torres**: Correcto.
**Cristian Berrío**: Ok. Bueno, entonces ahí ahí sí, entonces, sí, sí podríamos meter el el email. Porque el el la confirmación de pago del depósito del se envía a través de nuestro website.
**Luis Torres**: Ok, entonces mete ahí en la confirmación de pago metes el metes el invoice. Creo que actualmente está así. Actualmente estoy trabajando, sí. Este es el flujo que ahorita estoy trabajando, remaining balance due, fully paid access versus... Ok. Aquí están los access instructions. Y aquí le da TF, ¿Sí ves? El deposit received, PDF, PDF. Aquí te lo estoy especificando. Así tienen, así va ser, ¿no?
**Cristian Berrío**: Sí.
**Luis Torres**: Excelente. Ok, entonces, volviendo al al tema principal, en este link, puedo poner a guest report,
**Cristian Berrío**: Sea, que accedan y apenas accedas, le salga tipo el access code, y abajo el access code, lo del guest report.
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Sí, sí, sí se puede. Hay que modificar ciertas cositas, pero sí se puede.
**Luis Torres**: Ok. Voy, entonces, a mover la la mensajería de esto y la lógica de de Obsidian para para eso. Para hacerle push y pull Obsidian, hay que hacer algún tipo de push y pull, lo obscene se actualiza solo. En nuestra computadora.
**Cristian Berrío**: Este, repositorio. Es lo que yo les digo cuando escribo no sé, un mensaje en el chat de de si hicieron cambio, se actualiza. Todo eso manual. Se actualiza manual, esos son archivos que tú tienes solo tú en tu computadora. Nadie más lo tiene. Claro que estás haciendo solo tienes tú ahorita mismo, si estás cambiando algo de pues.
**Luis Torres**: Claro. Claro.
**Cristian Berrío**: Que mantener actualizado así con el repositorio.
**Luis Torres**: Excelente. Voy a hacerle push, entonces, para que ustedes le pongan de pull. Dale, hermano, buenísimo. Vamos a darle play. Sí, más adelante.
**Cristian Berrío**: Ya estoy sea, voy a corregir enseguida. Que no se me olvide lo de los invoices en los PDF. Y
**Luis Torres**: Si vas a corregir enseguida, vas a cambiar los correos, aplícate esto de una vez. Tenemos nuevos correos para
**Cristian Berrío**: Ah, no, entonces lo aplico después.
**Luis Torres**: Pero
**Cristian Berrío**: O sea, por lo que te digo es porque estoy en corto el flujo, ¿qué estoy haciendo? Y hago dos cosas en un tiempo y no termino ninguna, y dejar dos cosas incompletas prefiero terminar uno.
**Luis Torres**: Activo. Activo, activo. Igual aquí esto se guarda. Esto esta información se guarda aquí en el la en la conversación.
**Cristian Berrío**: Bueno, ahí te paso los PDF con los processing fee.
**Luis Torres**: Dale, habló activo. Ya se las mandó a la clienta.
**Cristian Berrío**: Revísalos igualmente. Yo cogí los tres, pero yo creo que son esos, sea, lo único que no cogí era el que estaba cancelado.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Pero hay dos que ya lo pagaron completo y hay otros que solo van el depósito y falta el otro. Pago. Ok? El último, falta que solo pago el depósito. No pago
**Luis Torres**: Sí, se lo pago el depósito, pero esto ya lo esto se lo cubre aparte, ¿oyó? ¿Te acuerdas que no se lo podía mandar? Se lo cubre. Balanceado, le mandé un invoice, básicamente. Porque como, ¿te acuerdas que tenemos el programa que que no
**Cristian Berrío**: Pero ella tiene ella tiene tres reservas, ¿sabes?
**Luis Torres**: Ajá, correcto.
**Cristian Berrío**: Ella tiene cuatro, perdón. Una de esas está cancelada y la otra sí. Activa.
**Luis Torres**: La otra la cancelé y luego la volví a poner. La la he cancelado por accidente. Eso fue lo que
**Cristian Berrío**: No, pero mira, mete, metete al
**Luis Torres**: Ajá.
**Cristian Berrío**: Al... No, no, no, a al
**Luis Torres**: Venue.
**Cristian Berrío**: Sí. Mírate,
**Luis Torres**: Cuéntamelo.
**Cristian Berrío**: en bookings, mire que hay uno en prevent ready.
**Luis Torres**: Sí, hermano, este no la mandé. Este balance no se quiere mandar. Porque lo había cancelado. Y luego lo tuve que quitar de nuevo de cancelado, porque lo cancelé por accidente.
**Cristian Berrío**: Okay.
**Luis Torres**: Ese es el que habíamos tenido problemas.
**Cristian Berrío**: Ya.
**Luis Torres**: Eso es lo que te estoy tratando de decir.
**Cristian Berrío**: Okay. Es que bueno, sales arriba y abajo. Persona
**Luis Torres**: Yes. Yes.
**Cristian Berrío**: le digo que asumo que ya está pagado.
**Luis Torres**: Sí, por
**Cristian Berrío**: ¿Cuándo lo pagó ahí?
**Luis Torres**: Y mándame ese invoice. ¿Lo pago ayer? Lo pagó ayer. Pero dale, mira, vamos a darle play, ¿me dices otra cosa? Voy a continuar aquí.
**Cristian Berrío**: ¿Mister, bueno?
**Luis Torres**: Dale, mira. Guest report flow. We're gonna be putting the guest report

_Sincronizado por Brain: 2026-10-17T00:40:34.265Z_
