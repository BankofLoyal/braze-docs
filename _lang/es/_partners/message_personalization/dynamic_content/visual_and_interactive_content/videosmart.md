---
nav_title: VideoSmart
article_title: VideoSmart
description: "Este artículo de referencia describe la integración entre Braze y VideoSmart, una tecnología de video personalizado e interactivo que permite a las marcas entregar contenido basado en datos y no lineal a escala."
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/) ofrece tecnología de video personalizado e interactivo que te permite entregar contenido basado en datos y no lineal a escala. Cada video se genera dinámicamente utilizando datos a nivel de cliente, lo que permite mensajería personalizada y recorridos de usuario dentro de una única experiencia de video.
>
> La integración de VideoSmart te permite incrustar contenido de video personalizado en campañas de correo electrónico utilizando contenido conectado de Braze y plantillas Liquid para solicitar activos de video de VideoSmart. Esta integración se implementa normalmente a través de una plantilla reutilizable de bloque de contenido de Braze, lo que permite un despliegue consistente entre campañas y al mismo tiempo ofrece flexibilidad en la selección de campañas y la lógica de personalización.

_Esta integración es desarrollada y mantenida por VideoSmart._

## Acerca de esta integración

VideoSmart se integra con Braze para generar dinámicamente activos de video personalizados en el momento del envío, que luego se incrustan directamente en el contenido de correo electrónico de tus campañas y Canvas de Braze.

En Braze, seleccionas la campaña de VideoSmart correspondiente y pasas atributos de cliente (a través de plantillas Liquid) a VideoSmart cuando realizas el envío. Estos atributos se utilizan para renderizar una experiencia de video única y personalizada para cada destinatario. Luego puedes usar contenido conectado de Braze para solicitar URLs de video o activos de la API de VideoSmart en tiempo real, lo que permite personalización a escala.

Esta integración está diseñada para mensajes de correo electrónico de Braze que admiten plantillas Liquid y contenido conectado, y se puede configurar para funcionar con atributos estándar del perfil de usuario de Braze o campos de datos personalizados.

## Casos de uso


Los casos de uso más comunes incluyen los siguientes:

- Incorporación de clientes y recorridos de bienvenida
- Educación financiera (como pensiones y pólizas de seguros)
- Estados de cuenta anuales y comunicaciones regulatorias
- Campañas de conocimiento de producto y venta cruzada
- Campañas de retención de clientes y reactivación de la interacción
- Recordatorios de carrito abandonado: cuando un cliente agrega productos a su carrito pero no compra, envías un correo electrónico con un video personalizado que destaca los artículos que dejó atrás
- Seguimientos post-compra: después de una compra, envía un video de agradecimiento personalizado y recomienda productos relacionados

## Requisitos previos

Antes de comenzar, confirma que tienes lo siguiente:

| Requisito                        | Descripción                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Credenciales de contenido conectado de Braze | Una credencial de autenticación básica de contenido conectado llamada **basic_credentials**, configurada con los valores proporcionados por VideoSmart |
| Plantilla de **bloque de contenido de VideoSmart**   | La plantilla de **bloque de contenido de VideoSmart** agregada a tu dashboard de Braze (proporcionada por VideoSmart)                                |
| Un mensaje de correo electrónico de Braze               | Un correo electrónico de campaña de Braze o un paso de correo electrónico de Canvas donde insertarás el **bloque de contenido de VideoSmart**                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Sigue estos pasos para habilitar el **bloque de contenido de VideoSmart** y usarlo en un correo electrónico.

### Paso 1: Configura la plantilla del bloque de contenido de VideoSmart en Braze

Solicita la plantilla del **bloque de contenido de VideoSmart** a tu representante de VideoSmart y agrégala a tu dashboard de Braze.

VideoSmart proporcionará las credenciales para la autenticación de contenido conectado utilizada por el bloque de contenido.

### Paso 2: Configura la autenticación de contenido conectado

Crea una credencial de autenticación básica de contenido conectado en Braze llamada "basic_credentials".

- Sigue las instrucciones en [Uso de autenticación básica]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#using-basic-authentication).
- Usa el nombre de usuario y la contraseña proporcionados por VideoSmart.

### Paso 3: Agrega el bloque de contenido a tu correo electrónico

Inserta el **bloque de contenido de VideoSmart** en tu correo electrónico donde quieras que aparezca el contenido de video.

En la mayoría de las configuraciones de Braze, los bloques de contenido se referencian usando el siguiente patrón (reemplaza "VideoSmart_Campaign" con el nombre del bloque de contenido en tu cuenta):

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
El nombre del bloque de contenido distingue entre mayúsculas y minúsculas y debe coincidir exactamente con lo que has configurado en Braze.
{% endalert %}

### Paso 4: Sobrescribe la campaña y los datos de registro (opcional)

Si tu bloque de contenido admite valores predeterminados, puedes usarlo sin establecer ninguna variable.

Si necesitas elegir una campaña específica de VideoSmart, pasar campos de personalización personalizados, o ambas cosas, establece las siguientes variables Liquid antes de renderizar el bloque de contenido:

- `vs_campaign_id`: identificador de campaña de VideoSmart
- `vs_record_data`: una cadena JSON que contiene los valores que deseas pasar a la plantilla de VideoSmart

#### Ejemplo

Este ejemplo usa atributos de usuario de Braze para el nombre y el apellido:

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'John' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Siempre proporciona valores predeterminados para los valores utilizados en `vs_record_data` para que la vista previa de tu correo electrónico de Braze se muestre correctamente.
- `vs_record_data` debe ser JSON válido, codificado como una sola cadena (el ejemplo usa `strip_newlines`).
{% endalert %}

### Paso 5: Usa las variables generadas por la plantilla del bloque de contenido de VideoSmart

Después de que el bloque de contenido se ejecuta, genera variables que puedes referenciar en otras partes de tu correo electrónico.

Las variables comunes incluyen:

{% raw %}
| Variable                          | Descripción                                           |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}`                 | URL del video personalizado                         |
| `{{ poster_url }}`                | URL de la imagen de póster del video                 |
| `{{ output_data.VARIABLE_NAME }}` | Campos de salida adicionales expuestos por el bloque de contenido |
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Límites de velocidad

La API de VideoSmart tiene un límite de velocidad de 10,000 solicitudes por minuto. Si superas este límite, puedes recibir errores o experimentar retrasos en la generación de videos.

Para reducir este riesgo, configura el límite de velocidad de la campaña de Braze para que la tasa de envío de mensajes se mantenga por debajo de la capacidad de la API de VideoSmart.

Para obtener orientación de Braze sobre velocidad de entrega y límites de velocidad, consulta [Velocidad de entrega y límites de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting).

## Consideraciones

- El contenido conectado se ejecuta cuando el mensaje se renderiza, por lo que los valores pueden diferir entre la vista previa y el envío si tus valores predeterminados o atributos difieren.
- Confirma que tu correo electrónico incluye el bloque de contenido antes de referenciar variables como `video_url`.
- Si usas campos personalizados en `vs_record_data`, confirma los nombres de campo esperados con VideoSmart.

## Solución de problemas

### La vista previa no funciona

Si la vista previa de Braze falla (por ejemplo, reintentos repetidos o errores de autenticación), verifica que:

- La credencial de contenido conectado "basic_credentials" existe y está configurada correctamente.
- La plantilla del **bloque de contenido de VideoSmart** está presente en tu cuenta de Braze.
- Cualquier variable requerida (por ejemplo, `vs_campaign_id` o campos obligatorios en `vs_record_data`) tiene valores predeterminados establecidos para la vista previa.

### Las variables de la plantilla del bloque de contenido de VideoSmart no generan la salida esperada

Si las variables generadas por la plantilla del bloque de contenido de VideoSmart no generan la salida esperada, verifica lo siguiente:

- La plantilla del **bloque de contenido de VideoSmart** está configurada correctamente en Braze.
- La autenticación de contenido conectado está configurada correctamente con las credenciales apropiadas.
- Imprime las variables en tu correo electrónico para confirmar que se están estableciendo. Por ejemplo: `{% raw %}{{ video_url }}{% endraw %}`

Si estás usando una campaña personalizada, también verifica:

- `vs_campaign_id` está establecido con un identificador de campaña válido.
- `vs_record_data` es JSON válido y contiene los campos esperados.