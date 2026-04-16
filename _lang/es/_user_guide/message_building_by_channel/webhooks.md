---
nav_title: Webhooks
article_title: Webhooks
page_order: 8
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Los webhooks son una forma habitual de comunicación entre aplicaciones para compartir datos en tiempo real. Hoy en día, rara vez tenemos una aplicación independiente que pueda hacerlo todo. La mayoría de las veces, trabajas con muchas aplicaciones o sistemas diferentes que están especializados en realizar determinadas tareas, y todas estas aplicaciones tienen que poder comunicarse entre sí. Ahí es donde entran en juego los webhooks. <br><br> Un webhook es un mensaje automatizado de un sistema a otro cuando se cumplen determinados criterios. En Braze, este criterio suele ser la activación de un evento personalizado. <br><br>En esencia, un webhook es un método basado en eventos para que dos sistemas distintos tomen medidas eficaces basadas en datos transmitidos en tiempo real. Ese mensaje contiene instrucciones que indican al sistema receptor cuándo y cómo realizar una tarea específica. Por este motivo, los webhooks pueden proporcionarte un acceso más dinámico y flexible a los datos y a la funcionalidad programática, y permitirte configurar recorridos del cliente que agilicen los procesos. <br><br>**La disponibilidad de los webhooks depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar.**"
description: "Esta página de inicio alberga los webhooks. Aquí encontrarás artículos sobre la creación de webhooks, la creación de plantillas de webhooks y los webhooks de Braze a Braze."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Artículos de sección"
guide_featured_list:
- name: Creación de un webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Creación de una plantilla de webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Webhooks de Braze a Braze
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Informe
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Solución de problemas de las solicitudes de webhook
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Casos de uso

Los webhooks son una forma excelente de conectar tus sistemas entre sí; al fin y al cabo, los webhooks son la forma en que se comunican las aplicaciones. Estos son algunos escenarios generales en los que los webhooks pueden resultar especialmente útiles:

- Envío de datos a y desde Braze
- Envío de mensajes a tus clientes a través de canales no compatibles directamente con Braze
- Publicar en las API de Braze

Algunos casos de uso más específicos son los siguientes:

- Si un usuario cancela su suscripción al correo electrónico, puedes hacer que un webhook actualice tu base de datos de análisis o CRM con esa misma información, garantizando una visión holística del comportamiento de ese usuario.
- Envía [mensajes transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) a los usuarios dentro de Facebook Messenger o Line.
- Envía correo directo a los clientes en respuesta a su actividad dentro de la aplicación y en la web utilizando webhooks para comunicarse con servicios de terceros como [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Si un jugador alcanza un determinado nivel o acumula un cierto número de puntos, utiliza webhooks y tu configuración de API existente para enviar una mejora de personaje o monedas directamente a su cuenta. Si envías el webhook como parte de una campaña de mensajería multicanal, puedes enviar un mensaje push o de otro tipo para informar al jugador de la recompensa al mismo tiempo.
- Si eres una aerolínea, puedes utilizar webhooks y tu configuración de API existente para acreditar un descuento en la cuenta de un cliente después de que haya reservado un determinado número de vuelos.
- Un sinfín de recetas "If This Then That" ([IFTTT](https://ifttt.com/about)): por ejemplo, si un cliente inicia sesión en la aplicación a través del correo electrónico, esa dirección puede configurarse automáticamente en Salesforce.

## Anatomía de un webhook

Un webhook consta de las siguientes partes.

| Parte del webhook | Descripción |
| --- | --- |
| [Método HTTP](#methods) | Al igual que las API, los webhooks necesitan métodos de solicitud. Se proporcionan a la URL a la que accede el webhook e indican al punto de conexión qué hacer con la información facilitada. Hay cuatro métodos HTTP que puedes especificar: POST, GET, PUT y DELETE. |
| HTTP URL | La dirección URL del punto de conexión de tu webhook. El punto de conexión es el lugar donde enviarás la información que estás capturando en el webhook. |
| Cuerpo de la solicitud | Esta parte del webhook contiene la información que estás comunicando al punto de conexión. El cuerpo de la solicitud puede ser pares clave-valor JSON o texto sin formato. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Ejemplo de webhook con un método HTTP, una URL HTTP y un cuerpo de solicitud.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Métodos HTTP {#methods}

La siguiente tabla describe los cuatro métodos HTTP diferentes que puedes especificar en tu webhook.

| Método HTTP | Descripción |
| ----------- | ----------- |
| POST | Este método escribe nueva información en el servidor receptor. Un ejemplo común del método POST en una aplicación del mundo real es un [formulario de contacto](https://www.braze.com/company/contact) en un sitio web. Cualquier información que introduzcas en el formulario pasa a formar parte de un cuerpo de solicitud y se envía a un receptor. Es el método más utilizado para enviar datos.
| GET | Este método recupera información existente, en lugar de escribir información nueva. Por definición, una solicitud GET no admite un cuerpo de solicitud. Es el método más utilizado para pedir datos a un servidor. Por ejemplo, considera el [punto de conexión `/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si hicieras una solicitud GET, te devolvería una lista de tus segmentos.
| PUT | Este método actualiza la información en el punto de conexión, reemplazando cualquier información existente con lo que hay en el cuerpo de la solicitud. 
| DELETE | Este método elimina el recurso de la URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhooks en Braze

En Braze, puedes crear un webhook como campaña de webhook, campaña de API o componente de Canvas.

{% tabs %}
{% tab Webhook Campaign %}

1. En el dashboard de Braze, ve a **Campañas**.
2. Haz clic en **Crear campaña** y selecciona **Webhook**.

Consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para más información.

{% endtab %}
{% tab API Campaign %}

1. En el dashboard de Braze, ve a **Campañas**.
2. Haz clic en **Crear campaña** y selecciona **Campaña de API**.
3. Haz clic en **Añadir mensajes** y selecciona **Webhook**.
4. Formatea tu llamada a la API para incluir un [objeto webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para más información.

{% endtab %}
{% tab Canvas Component %}

1. En tu Canvas, crea un nuevo componente.
2. En la sección **Mensaje** de tu componente, selecciona **Webhook**.

Consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para más información.

{% endtab %}
{% endtabs %}

## Gestión de errores de webhook y límite de velocidad

Cuando Braze recibe una respuesta de error de una llamada de webhook, ajustamos automáticamente el comportamiento de envío de ese webhook basándonos en estas cabeceras de respuesta:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Estas cabeceras nos ayudan a interpretar los límites de velocidad y a ajustar la velocidad de envío en consecuencia para evitar más errores. También aplicamos una estrategia de retirada exponencial para los reintentos, que ayuda a reducir el riesgo de saturar tus servidores espaciando los intentos de reintento en el tiempo.

Si detectamos que la mayoría de las solicitudes de webhook a un host específico están fallando, aplazaremos temporalmente todos los intentos de envío a ese host. Después, reanudaremos el envío tras un periodo de enfriamiento definido, permitiendo que tu sistema se recupere.