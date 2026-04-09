---
nav_title: Registro de actividad de mensajes
article_title: Registro de actividad de mensajes
page_order: 5
page_type: reference
description: "Este artículo de referencia describe el registro de actividad de mensajes, que te muestra los mensajes asociados a tus campañas y envíos. Aquí también encontrarás información sobre cómo entender los mensajes de registro."

---

# Registro de actividad de mensajes {#dev-console-troubleshooting}

> El **registro de actividad de mensajes** te ofrece la oportunidad de ver todos los mensajes (especialmente los mensajes de error) asociados a tus campañas y envíos.

Puedes ver las transacciones de campaña de la API, solucionar problemas de mensajes fallidos y obtener información sobre cómo mejorar la entrega de notificaciones o resolver problemas técnicos existentes.

Para acceder al registro, ve a **Configuración** > **Registro de actividad de mensajes**.

![Registro de actividad de mensajes]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Además de este artículo, también recomendamos consultar nuestro curso de Braze Learning sobre [herramientas de control de calidad y depuración](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que trata sobre cómo utilizar el registro de actividad de mensajes para llevar a cabo tu propia solución de problemas y depuración.
{% endalert %}

Puedes filtrar por el siguiente contenido registrado en el **registro de actividad de mensajes**:

- Errores en las notificaciones push
- Errores de mensaje anulado
- Errores de webhook
- Errores de correo
- Registros de mensajes API
- Errores en el contenido conectado
- Errores de audiencia de la API REST conectada
- Errores de asignación de alias de usuario
- Errores en las pruebas A/B
- Errores SMS/MMS
- Errores de WhatsApp
- Errores de actividad en vivo
- Errores de desencadenamiento de usuario incorrecto
- Errores de [límite diario de invocaciones]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#monitor-your-agent) de Braze Agents
- Errores de [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) no disponible de Braze Agents

Estos mensajes pueden proceder de nuestro propio sistema, de tus aplicaciones o plataformas, o de nuestros socios externos. Esto puede dar lugar a un número infinito de mensajes que pueden aparecer en este registro.

## Comprender los mensajes de registro

Para determinar el significado de tus mensajes, presta atención a la redacción de cada mensaje y a las columnas que se corresponden con él, ya que puede ayudarte a solucionar problemas utilizando pistas contextuales. 

Por ejemplo, si tienes una entrada de registro cuyo mensaje indica "empty-cart_app" y no estás seguro de lo que significa, mira a la izquierda, en la columna **Tipo**. Si ves "Error de mensaje anulado", puedes suponer con seguridad que el mensaje era lo que se escribió como [mensaje anulado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) utilizando Liquid, y que el mensaje se anuló porque el destinatario del mensaje tenía un carrito vacío en tu aplicación.

### Mensajes comunes

Hay algunos tipos de mensajes comunes que puedes ver, y algunos incluso pueden proporcionar enlaces de solución de problemas para ayudarte a diagnosticar y solucionar problemas.

Los siguientes mensajes se incluyen a modo de ejemplo y pueden no coincidir exactamente con lo que aparece en la columna **Mensaje** de tu registro.

| Tipo de mensaje | Mensaje potencial | Descripción |
|---|---|---|
| Rebote blando | La dirección de correo electrónico same@example.com arrojó un rebote blando. | La dirección de correo electrónico era válida y el mensaje llegó al servidor de correo del destinatario, pero fue rechazado por un problema "temporal". <br><br>Entre las razones más comunes del rebote blando se incluyen: {::nomarkdown} <ul> <li> El buzón de entrada estaba lleno (el usuario ha superado su cuota) </li> <li> El servidor no funcionaba </li> <li> El mensaje era demasiado grande para el buzón de entrada del destinatario </li>  </ul> {:/} Si un correo electrónico ha recibido un rebote blando, normalmente lo reintentamos en un plazo de 72 horas, pero el número de intentos varía según el destinatario. |
| Rebote duro | La cuenta de correo electrónico a la que intentaste acceder no existe. Comprueba que la dirección de correo electrónico del destinatario no contenga erratas ni espacios innecesarios. | Tu mensaje nunca llegó al buzón de entrada de esta persona porque no había buzón de entrada al que llegar. Si deseas profundizar más, los mensajes como este a veces pueden tener enlaces en la columna **Ver detalles** que te permiten ver el perfil del destinatario previsto.|
| Bloqueo | El mensaje de correo no deseado es rechazado debido a la política anti-spam. | Tu mensaje ha sido clasificado como correo no deseado. Este error de correo se registra para un usuario si hemos recibido un evento del ESP indicando que el correo electrónico ha sido descartado. Puede que solo sea para ese destinatario en concreto, pero si ves este mensaje con frecuencia, tal vez debas replantearte tus hábitos de envío o el contenido de tus mensajes. Además, piensa: ¿realizaste [el calentamiento de tu IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Si no es así, ponte en contacto con Braze para que te asesoren sobre cómo ponerlo en marcha.|
| Error de mensaje anulado | empty-cart_web | Si tienes una aplicación con un carrito o creas un envío con un mensaje de cancelación en Liquid, puedes personalizar qué mensaje se te devuelve si se cancela el envío. En este caso, el mensaje devuelto es empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ¿Por qué mi mensaje no aparece aquí?

Los mensajes del registro de actividad de mensajes pueden proceder de diversas fuentes: Braze, tus aplicaciones o plataformas, o nuestros socios externos. Esto significa que hay un número infinito de mensajes que podrían aparecer en este registro: como puedes imaginar, ¡no podemos enumerarlos todos!

Por ejemplo, algunos posibles mensajes de "Bloqueo", además del enumerado en la tabla anterior, podrían ser:

- Lamentablemente, los mensajes de [_IP_ADDRESS_] no se enviaron. Ponte en contacto con tu proveedor de servicios de Internet, ya que parte de su red está en nuestra lista de bloqueados.
- Mensaje rechazado debido a la política local.
- El mensaje fue bloqueado por el receptor como correo no deseado.
- Servicio no disponible, host del cliente [_IP_ADDRESS_] bloqueado mediante Spamhaus.

## Periodo de retención del almacenamiento

Los errores de las últimas 60 horas están disponibles en los registros de actividad de mensajes. Los registros con más de 60 horas de antigüedad se eliminan y ya no son accesibles.

### Número de registros de errores almacenados

El número de registros guardados depende de varias condiciones. Por ejemplo, si se envía una campaña planificada a miles de usuarios, podríamos ver una muestra de los errores en el registro de actividad de mensajes en lugar de todos los errores. A continuación se ofrece un resumen de las condiciones que afectan al número de registros que se guardan:
- Se guardan hasta 20 registros de errores del mismo tipo para la misma campaña o paso en Canvas en el plazo de una hora fija para los siguientes tipos de errores:
    - Errores en el contenido conectado
    - Errores de mensaje anulado
    - Errores de webhook
    - Errores de rechazo de SMS
    - Errores de fallo en la entrega de SMS
    - Errores de WhatsApp
    - Errores en las pruebas A/B
- Se guardan hasta 20 registros de errores de notificaciones push del mismo tipo de error para la misma campaña o combinación de paso en Canvas y aplicación para los siguientes tipos de error:
    - Credencial push no válida
    - Token de notificaciones push no válido
    - Sin credencial push
    - Errores de token
    - Cuota excedida
    - Se agotó el tiempo de espera para los reintentos
    - Carga útil no válida
    - Error inesperado
- Se guardan hasta 100 registros de errores del mismo tipo para la misma aplicación en el plazo de una hora fija para los siguientes tipos de errores:
    - Error de actividad en vivo (sin credencial push)
    - Error de actividad en vivo (credencial push no válida)
    - Otros errores de actividad en vivo
    - Errores de token eliminados de APNs Feedback
- Se guardan hasta 100 registros de errores del mismo tipo para la misma campaña o paso en Canvas en el plazo de una hora fija para los siguientes tipos de errores:
    - Errores de rebote blando de correo electrónico
    - Errores de rebote duro de correo electrónico
    - Errores de bloqueo de correo electrónico
- Se guardan hasta 100 registros de errores de asignación de alias de usuario para el mismo espacio de trabajo en una hora fija.

## Envíos de prueba

El **registro de actividad de mensajes** muestra los registros de prueba de estos canales de mensajería:

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Los registros de envío de prueba no están disponibles para los siguientes canales: correo electrónico, tarjetas de contenido, mensajes dentro de la aplicación y push.

Los registros de envíos de prueba llevan el prefijo "[TEST SEND]", pero no se garantiza que todos los registros de envíos de prueba tengan ese prefijo (por ejemplo, los errores de contenido conectado no lo tienen).