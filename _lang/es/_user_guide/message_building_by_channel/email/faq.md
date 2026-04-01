---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre el correo electrónico
page_order: 15
description: "Esta página ofrece respuestas a las preguntas más frecuentes sobre los mensajes de correo electrónico."
channel: email

---

# Preguntas más frecuentes

> Este artículo da respuesta a algunas preguntas frecuentes sobre el correo electrónico.

### ¿Qué ocurre cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico?

Si varios usuarios con direcciones de correo electrónico coincidentes están en un segmento para recibir una campaña, se elige un perfil de usuario aleatorio con esa dirección de correo electrónico en el momento del envío. De este modo, el correo electrónico solo se envía una vez y se deduplica, lo que garantiza que no llegue varias veces a la misma dirección de correo electrónico.

Los siguientes escenarios pueden hacer que parezca que un usuario recibió un correo electrónico dos veces:

- **Se produjo un error durante la creación de la campaña o Canvas:** Es posible que el usuario no reciba literalmente el mismo envío dos veces, pero puede recibir dos correos electrónicos distintos con la misma línea del asunto. Cuando se duplica una campaña o Canvas, comprueba los detalles de configuración del correo electrónico, como las imágenes o las líneas del asunto. También puedes consultar los registros de cambios para ver si la campaña o Canvas se modificó después del lanzamiento: un duplicado puede compartir la misma línea del asunto que el original cuando el usuario lo recibió.
- **Varios perfiles de usuario tienen reenvío de correo electrónico:** Si un usuario tiene varias cuentas en una aplicación determinada pero una cuenta reenvía el correo, el usuario recibe la campaña una vez por buzón de entrada; el correo puede aparecer dos veces en el buzón de entrada donde se reenvían los mensajes. Solo algunos proveedores indican cuándo un correo electrónico fue reenviado desde otra cuenta.
- **Configuración de correo electrónico del destinatario:** Algunos clientes fusionan buzones de entrada ("buzón universal"). Si la misma campaña se dirige a varias cuentas que comparten un buzón de entrada, puede parecer que una persona recibió la campaña dos veces cuando en realidad se enviaron mensajes a dos perfiles distintos. El destinatario puede confirmar si varias cuentas están combinadas en un solo buzón de entrada.

Ten en cuenta que esta deduplicación se produce cuando los usuarios objetivo están incluidos en el mismo envío. Las campañas desencadenadas pueden dar lugar a múltiples envíos a la misma dirección de correo electrónico (incluso dentro de un período en el que los usuarios podrían ser excluidos debido a la reelegibilidad) si diferentes usuarios con direcciones de correo electrónico coincidentes registran el evento desencadenante en diferentes momentos. Los usuarios no son deduplicados por correo electrónico al entrar en Canvas, por lo que es posible que no sean deduplicados más allá del primer paso de un Canvas si progresan en tiempos ligeramente diferentes debido a la entrada con tasa limitada. Cuando un usuario vinculado a una dirección de correo electrónico determinada abre o hace clic en un correo electrónico, todos los perfiles de usuario que comparten esa dirección de correo electrónico se marcan como que han abierto o hecho clic en la campaña.

#### Excepción: campañas desencadenadas por API

Las campañas desencadenadas por API deduplicarán o enviarán duplicados en función de dónde esté definida la audiencia. Los correos electrónicos duplicados deben dirigirse por separado en la llamada a la API usando `user_ids` distintos para recibir múltiples detalles. A continuación se presentan tres posibles escenarios para campañas desencadenadas por API:

- **Escenario 1: Correos electrónicos duplicados en el segmento de destino:** Si el mismo correo electrónico aparece en varios perfiles de usuario agrupados en los filtros de audiencia del dashboard para una campaña desencadenada por API, solo uno de los perfiles recibirá el correo electrónico.
- **Escenario 2: Correos duplicados en diferentes `user_ids` dentro del objeto destinatarios:** Si el mismo correo electrónico aparece en varios valores `external_user_id` referenciados por el objeto `recipients`, el correo electrónico se enviará dos veces.
- **Escenario 3: Correos electrónicos duplicados debido a `user_ids` duplicados dentro del objeto destinatarios:** Si intentas añadir el mismo perfil de usuario dos veces, solo uno de los perfiles recibirá el correo electrónico.

### ¿Se aplicarán retroactivamente las actualizaciones de mi configuración de correo electrónico saliente?

No. Las actualizaciones realizadas en la configuración del correo electrónico saliente no afectan retroactivamente a los envíos existentes. Por ejemplo, cambiar el nombre de visualización predeterminado en la configuración de correo electrónico no sustituirá automáticamente el nombre de visualización predeterminado existente en tus campañas activas o Canvas. 

### ¿Qué es una "buena" tasa de entrega de correo electrónico?

Normalmente, el "número mágico" se sitúa en torno al 98% de mensajes entregados con una tasa de rebote no superior al 3%. Si la entrega cae por debajo de esa cifra, suele ser motivo de preocupación.

Sin embargo, una tasa superior al 98% puede seguir teniendo problemas de capacidad de entrega. Por ejemplo, si todos los rebotes proceden de un dominio concreto, es una señal clara de que hay un problema de reputación con ese proveedor.

Además, es posible que los mensajes se entreguen y acaben en correo no deseado, lo que indica problemas de reputación potencialmente graves. Es importante controlar no solo el número de mensajes que se entregan, sino también las tasas de apertura y clics para determinar si los usuarios ven realmente los mensajes en sus buzones de entrada. Dado que los proveedores no suelen informar de todos los casos de correo no deseado, una tasa de correo no deseado de incluso el 1% podría ser motivo de preocupación y análisis más detallado.

Por último, tu negocio y los tipos de correos electrónicos que envías también pueden afectar a la entrega. Por ejemplo, alguien que envíe principalmente [correos electrónicos transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) debería esperar obtener una tasa mejor que alguien que envíe muchos mensajes de marketing.

### ¿Por qué mis métricas de entrega de correo electrónico no suman el 100%?

Las métricas de entrega de correo electrónico (entregas, rebotes y tasa de correo no deseado) pueden no sumar el 100% debido a los correos electrónicos que sufren un rebote blando y luego no se entregan después del período de reintento de hasta 72 horas.

Los rebotes blandos son correos electrónicos que rebotan debido a un problema temporal o transitorio, como "buzón lleno", "servidor temporalmente no disponible", etc. Si un correo electrónico con rebote blando sigue sin entregarse después de 72 horas, no se tendrá en cuenta en las métricas de entrega de la campaña.

### ¿Qué es un bucle de retroalimentación de correo electrónico?

Un bucle de retroalimentación de correo electrónico (FBL) permite a los remitentes supervisar su reputación identificando campañas que reciben un alto volumen de quejas. Para conocer los pasos para implementar un bucle de retroalimentación de Gmail, consulta el artículo [Bucle de retroalimentación de Google](https://support.google.com/a/answer/6254652).

### ¿Qué son los píxeles de seguimiento de apertura?

[Los píxeles de seguimiento de apertura]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) aprovechan el dominio de seguimiento de clics de correo electrónico de un remitente para realizar un seguimiento de los eventos de apertura de correo electrónico. El píxel es una etiqueta de imagen que se añade al HTML del correo electrónico. Suele ser el último elemento HTML dentro de la etiqueta body. Cuando un usuario carga su correo electrónico, se realiza una solicitud para rellenar la imagen desde el dominio de seguimiento de marca, que registra un evento de apertura.

### ¿Qué ocurre cuando se detiene una campaña de correo electrónico o Canvas?

Se impedirá a los usuarios entrar en Canvas y no se enviarán más mensajes. 

Para las campañas de correo electrónico y Canvas, el botón de detener no significa que el envío se detenga inmediatamente. Cuando se envían las solicitudes de envío, no se puede impedir que se entreguen al usuario, lo que puede ocurrir después de cierto retraso. 

Aunque Braze no enviará más solicitudes una vez que la campaña o Canvas se haya detenido, los análisis pueden seguir aumentando mientras el ESP termina de procesar las solicitudes que ya están en curso.

### ¿Por qué veo más clics en los correos electrónicos que aperturas?

Puede que veas más clics que aperturas por alguna de las siguientes razones:
- Los usuarios hacen varios clics en el cuerpo del correo electrónico con una sola apertura.
- Los usuarios hacen clic en algunos enlaces de correo electrónico dentro del panel de vista previa de sus teléfonos. En este caso, Braze registra este correo electrónico como clicado pero no abierto.
- Los usuarios vuelven a abrir un correo electrónico que habían previsualizado anteriormente.

### ¿Por qué no veo ninguna apertura ni ningún clic en los correos electrónicos?

Es posible que no veas ninguna apertura ni ningún clic en tus correos electrónicos si hay un error de configuración en tu dominio de seguimiento. Esto puede deberse a cualquiera de las siguientes razones:
- Hay un problema con SSL en el que las URL de seguimiento son `http` en lugar de `https`.
- Hay un problema con tu CDN por el que la cadena del agente de usuario en los eventos de apertura, los eventos de clic o ambos no se rellenan.

### ¿Cuáles son los riesgos potenciales de provocar clics en el servidor?

Ciertos elementos de un mensaje de correo electrónico, como los mensajes demasiado largos o con demasiados signos de exclamación, pueden desencadenar respuestas de seguridad del correo electrónico. Estas respuestas pueden afectar a los informes, a la reputación de la IP y pueden hacer que los usuarios cancelen su suscripción.

Para conocer las mejores prácticas sobre cómo gestionar estas respuestas, consulta [Cómo gestionar el aumento del porcentaje de clics]({{site.baseurl}}/help/help_articles/email/open_rates/).

### ¿Puede Braze hacer un seguimiento de los enlaces para cancelar suscripción contabilizados en la métrica "Cancelar suscripción"?

Braze rastrea los enlaces de cancelación de suscripción si se utiliza el siguiente Liquid en los correos electrónicos: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### ¿Por qué veo un número diferente de cancelaciones de suscripción que de clics en mi enlace para cancelar suscripción?

Si hay más _cancelaciones de suscripción_ que usuarios que hicieron clic en el enlace para cancelar suscripción en el cuerpo del correo electrónico, las acciones del encabezado list-unsubscribe suelen explicar la diferencia: un clic en el encabezado list-unsubscribe cuenta como una _cancelación de suscripción_ pero no como un _clic_ en el enlace del cuerpo.

Si el número total de clics en el enlace para cancelar suscripción del cuerpo es mayor que el número de _cancelaciones de suscripción_, es posible que los usuarios hayan hecho clic en el enlace más de una vez.

### ¿Puedo añadir un enlace "ver este correo en un navegador" a mis correos electrónicos?

No, Braze no ofrece esta funcionalidad. Esto se debe a que una mayoría cada vez mayor del correo electrónico se abre en dispositivos móviles y clientes de correo modernos, que renderizan imágenes y contenidos sin problemas.

**Solución:** Para lograr este mismo resultado, puedes alojar el contenido de tu correo electrónico en una página de destino externa (como tu sitio web), a la que se puede enlazar desde la campaña de correo electrónico que estás creando utilizando la herramienta **Enlace** al editar el cuerpo del correo electrónico.

### ¿Por qué el software de seguridad del correo electrónico cancela automáticamente la suscripción de mis usuarios?

Algunas herramientas de seguridad para el correo electrónico corporativo (como Barracuda, Proofpoint y servicios similares) descargan previamente o escanean todas las URL de los correos electrónicos entrantes, incluidos los enlaces para cancelar la suscripción. Esto puede provocar cancelaciones de suscripción involuntarias cuando la herramienta de seguridad sigue el enlace de cancelación de suscripción con un solo clic (list-unsubscribe).

Para mitigar esto:

- **Recomienda a los destinatarios que incluyan tu dominio de envío en la lista de permitidos:** Trabaja con los equipos de TI de los destinatarios afectados para añadir tu dominio de envío y los dominios de seguimiento de Braze a su lista de permitidos de seguridad de correo electrónico.
- **Utiliza un centro de preferencias:** En lugar de un enlace directo para cancelar la suscripción, utiliza un [centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) que requiera la interacción del usuario para confirmar la acción de cancelación. Los escáneres de seguridad normalmente no completan formularios de varios pasos.
- **Revisa los registros de cancelación de suscripción:** Comprueba el encabezado `User-Agent` y la dirección IP en los datos de eventos de cancelación de suscripción de Currents para identificar patrones coherentes con el escaneo automatizado (como encabezados `User-Agent` consistentes en múltiples cancelaciones de suscripción).

Para obtener más información sobre cómo el escaneo del lado del servidor puede afectar las métricas del correo electrónico, consulta [Cómo manejar los aumentos en las tasas de clics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#handling-increases-in-click-rates).

### ¿Por qué ha cambiado inesperadamente mi tasa de aperturas automáticas?

[Las aperturas automáticas]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens) se desencadenan mediante características de seguridad del correo electrónico, como la protección de la privacidad en los correos electrónicos de Apple Mail (MPP), que precarga el contenido del correo electrónico (incluido el píxel de seguimiento) sin que el usuario abra físicamente el correo electrónico. Las tasas de aperturas automáticas pueden variar en función de:

- Cambios en la proporción de tu audiencia que utiliza Apple Mail u otros clientes de correo electrónico con funciones de privacidad habilitadas.
- Actualizaciones de las características de privacidad del proveedor de correo electrónico o de los comportamientos de detección de bots.
- Cambios en la segmentación o la orientación de tu audiencia.

Los porcentajes de aperturas automáticas no son una medida fiable de la interacción real. Para obtener una visión más precisa del rendimiento del correo electrónico, céntrate en *Otras aperturas* (aperturas no automáticas) y *Clics únicos*. También puedes comparar estas métricas a lo largo del tiempo utilizando el [panel de rendimiento del correo electrónico]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard/).

### ¿La métrica *Aperturas únicas* incluye las *aperturas automáticas*?

Sí. *Aperturas únicas* incluye las *aperturas automáticas*. En la página **Análisis de campañas** y en el **generador de informes**, puedes ver ambas métricas.

### ¿Por qué mi volumen de entrega de correo electrónico no coincide con mi volumen de envío?

Después de que se envía un correo electrónico, el buzón de entrada del destinatario decide cuándo se entrega. Los mensajes pueden diferirse durante horas o días debido a un buzón lleno, limitación de velocidad del ESP desde una IP determinada y razones similares.

Cuando los mensajes diferidos se entregan en un día calendario diferente al día de envío, las _entregas_ pueden superar los _envíos_ para el mismo rango de fechas. Cuando muchos aplazamientos se acumulan en un solo día, los _envíos_ pueden superar las _entregas_ para ese rango.

### ¿Por qué veo una advertencia para incluir un enlace para cancelar suscripción cuando mi correo electrónico ya tiene uno?

Esta advertencia puede persistir en campañas duplicadas a partir de una campaña que no tenía un enlace para cancelar suscripción. Para eliminarla:

- Para correos electrónicos HTML, ve a la pestaña **Texto sin formato** y selecciona **Regenerar desde HTML**.
- Después de duplicar, duplica la variante y luego elimina la variante original. **No** selecciones la variante original, o la advertencia puede trasladarse.

### ¿Cuáles son las razones por las que mi usuario no ha recibido una campaña de correo electrónico?


Las razones por las que un usuario no ha recibido una campaña de correo electrónico incluyen:

- No era elegible para recibir el correo electrónico.
- Su dirección de correo electrónico no es válida o no existe.
- Es posible que haya perdido o eliminado el mensaje.
- El mensaje puede estar en su carpeta de correo no deseado.

### ¿Cómo puedo optimizar las imágenes en Outlook?

Outlook a menudo utiliza un renderizado al estilo de Microsoft Word, que puede añadir un borde alrededor de las imágenes. Puedes envolver el contenido para que se oculte en los clientes de Office usando comentarios condicionales estándar, por ejemplo:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### ¿Puedo usar imágenes SVG o WEBP en mis mensajes de correo electrónico?

Las imágenes SVG no se renderizan en Gmail web ni en Gmail iOS. WEBP no es compatible de forma consistente en todos los clientes. En su lugar, utiliza formatos ampliamente compatibles como PNG o JPEG para que las imágenes se rendericen de forma fiable.

### ¿Se pueden usar variables Liquid asignadas en una parte del creador de mensajes en otra?

No. Cada parte del correo electrónico (asunto, cuerpo, encabezados, botones, etc.) se genera por separado, por lo que las variables Liquid asignadas en un campo no están disponibles en otro. Asigna las variables en cada campo que las necesite.

### Mi plantilla de correo electrónico no aparece. ¿Dónde está?

Ve a **Plantillas** > **Plantillas de correo electrónico**. Puedes filtrar por tipo (HTML o arrastrar y soltar).

Confirma que tienes permiso para ver plantillas; consulta [Permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).