---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "Este artículo de referencia cubre la integración de Wunderkind Signals con Braze, incluyendo señales de comportamiento que desencadenan recorridos Canvas, la configuración con la API de entrada a Canvas, la carga útil de contexto de Canvas en la entrega activada por API y los informes."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) es una plataforma de rendimiento de comercio electrónico que utiliza tecnología de identidad propietaria para reconocer visitantes anónimos de sitios web y resolverlos a direcciones de correo electrónico procesables. En promedio, Wunderkind escala la identificación del 3 al 5 % del tráfico del sitio web al 40 al 60 %, lo que permite a las marcas desencadenar mensajes personalizados uno a uno a escala a través de su ESP existente.

*Esta integración está mantenida por Wunderkind. Para soporte, visita [support.wunderkind.co](https://support.wunderkind.co).*

## Sobre la integración

La integración de Wunderkind Signals permite que señales de comportamiento de alta intención —como abandono del carrito de compras, abandono de producto y bajadas de precio— desencadenen recorridos Canvas en tiempo real en Braze. Wunderkind identifica usuarios anónimos en tu sitio web, resuelve su identidad a una dirección de correo electrónico entregable y envía una carga útil de señal estructurada a Braze a través de la API de entrada a Canvas, iniciando automáticamente tus flujos de correo electrónico preconfigurados.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Wunderkind | Se requiere una cuenta de Wunderkind con Signals habilitado. Ponte en contacto con tu representante de Wunderkind para confirmar la elegibilidad. |
| Cuenta de Braze | Se requiere una cuenta de Braze con acceso a Canvas. El equipo de Wunderkind debe tener un puesto asignado en tu cuenta. Para más detalles, consulta [Conceder acceso a Wunderkind a tu cuenta de Braze](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account). |
| Clave de API REST de Braze | Creas una clave de API dedicada con permisos específicos durante la configuración (consulta el [Paso 1](#step-1-create-a-braze-api-key-for-wunderkind)). |
| Identificación de usuario | Wunderkind normalmente resuelve un consumidor en Braze usando `user_alias` con `alias_label: "wknd_email_id"` (a menudo con el correo electrónico como `alias_name`). Cada destinatario de [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) debe incluir exactamente uno de `external_user_id`, `user_alias`, `braze_id` o `email` ([objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object/)); si usas `email`, incluye [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email). Cuando usas `user_alias`, el perfil ya debe existir en Braze antes del desencadenador. Crea o actualiza usuarios y alias primero con [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) o [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). Para más información, consulta [Limitaciones](#limitations). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cómo funciona

Cuando Wunderkind identifica a un usuario anónimo de alta intención y resuelve su identidad, envía una carga útil de señal a Braze usando el punto de conexión `/canvas/trigger/send`, desencadenando el recorrido Canvas correspondiente para ese usuario en tiempo real.

Para un resumen técnico completo, consulta el [Portal de desarrolladores de Wunderkind](https://developer.wunderkind.co/docs/integration-overview).

## Integración

### Paso 1: Crear una clave de API de Braze para Wunderkind

En tu dashboard de Braze:

1. Ve a **Configuración** > **Claves de API** y haz clic en **Crear nueva clave de API**.
2. Dale a la clave un nombre descriptivo (por ejemplo, `Wunderkind Signals`).
3. Concede los permisos listados en [Conceder acceso a Wunderkind a tu cuenta de Braze](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account).
4. Copia la clave de API para ingresarla en la plataforma Wunderkind en la siguiente sección.

{% alert note %}
Para Wunderkind Signals, las solicitudes de la [API REST]({{site.baseurl}}/api/basics/) de Braze se autentican con una clave de API REST, no con tokens OAuth. Crea una clave de API dedicada en el dashboard y proporciona esa clave a Wunderkind.
{% endalert %}

### Paso 2: Conectar Braze a la plataforma Wunderkind

1. Inicia sesión en la plataforma Wunderkind y ve a **Integrations Hub**.
2. Selecciona el mosaico de **Braze** y luego selecciona **Conectar**.
3. Ingresa tu clave de API REST de Braze y selecciona tu clúster.
4. Selecciona **Guardar**.

### Paso 3: Revisar los nuevos activos de Braze

Tras la activación, Wunderkind aprovisiona nuevos activos de implementación en tu espacio de trabajo de Braze según la estrategia alineada con tu representante de Wunderkind:

| Tipo de activo | Método de creación de Wunderkind |
| ---------- | -------------------------- |
| Content Blocks | Automático |
| Canvas activados por API | Servicio gestionado |
| Etiquetas, atributos personalizados, plantillas de enlaces | Servicio gestionado |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 4: Completar la configuración de Canvas

Para cada Canvas de Signals, construye tus plantillas de correo electrónico usando el editor de arrastrar y soltar de Braze o HTML.

- Wunderkind rellena los datos de producto y sesión en el objeto `context` de cada destinatario en `/canvas/trigger/send` en el momento del envío.
- Para instrucciones detalladas sobre cómo usar Liquid con esa carga útil en tus plantillas, consulta [Completar la configuración de Canvas](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) en el Centro de ayuda de Wunderkind.

### Paso 5: Revisar la elegibilidad de Canvas

Para cada Canvas de Signals, ve a la configuración de **Audiencia objetivo** para revisar la audiencia de entrada predeterminada y los criterios de salida de Wunderkind.

- Para asegurarte de que no estás enviando mensajes a tus usuarios con demasiada frecuencia, consulta [Límite de velocidad centrado en el usuario]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).
- Ajusta la configuración para evitar que los usuarios sigan recibiendo mensajes de Canvas después de realizar una compra. Por ejemplo, agrega la excepción **Realizar compra**.
- Ciertos Canvas de Signals están preconfigurados con filtros de atributos personalizados para que los usuarios reciban el mensaje de mayor intención posible.
- Consulta [Revisar la elegibilidad de Canvas](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) en el Centro de ayuda de Wunderkind para detalles sobre la elegibilidad y prioridad de Canvas.

### Paso 6: Probar y lanzar

Wunderkind realiza un control de calidad de extremo a extremo antes del lanzamiento:

- Confirma que las señales se entregan a los Canvas ID correctos sin errores de API.
- Verifica que los campos de `context` (nombre del producto, imagen, URL) se rellenan correctamente en las plantillas de correo electrónico renderizadas.
- Consulta [Probar y lanzar Signals para Braze](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) en el Centro de ayuda de Wunderkind para instrucciones sobre cómo previsualizar plantillas con productos simulados de Wunderkind.

Cuando el control de calidad se aprueba, tu administrador de implementación de Wunderkind coordina el lanzamiento a producción con tu equipo.

## Carga útil de contexto de Canvas

Wunderkind admite seis tipos de señales. Cada una entrega un conjunto distinto de claves y valores dentro del objeto [`context`]({{site.baseurl}}/api/objects_filters/context_object/) para ese destinatario en `/canvas/trigger/send` (consulta [Enviar mensajes Canvas usando entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). El campo `WkPurpose` identifica el tipo de señal dentro de esa carga útil.

### Campos comunes (todos los tipos de Canvas) {#canvas-types-table}

| Propiedad | Tipo | Descripción |
| -------- | ---- | ----------- |
| `Origin` | String | Siempre `"wunderkind"` |
| `DataOnly` | String | Siempre `"Y"` — indica que Wunderkind actúa solo como capa de datos; Braze ejecuta el envío |
| `UserType` | String | `"prospect"` o `"customer"` |
| `WkChannel` | String | Siempre `"email"` para esta integración |
| `WkPurpose` | String | Identificador del tipo de señal (consulta los valores por Canvas a continuación) |
| `WKCouponCode` | String | Código de cupón, si aplica (cadena vacía si no se usa) |
| `WKCouponPurpose` | String | Descripción de la oferta del cupón (cadena vacía si no se usa) |
| `Items` | Array | Array de objetos de producto (consulta los campos de producto a continuación) |
| `WkOpen` | String | Píxel de seguimiento disponible para fines de informes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Campos de artículo de producto

| Propiedad | Tipo | Descripción |
| -------- | ---- | ----------- |
| `WkCopy` | String | Nombre del producto |
| `WkId` | String | ID del producto |
| `WkImageUrl` | String | URL de la imagen del producto |
| `WkUrl` | String | URL de la página de detalle del producto |
| `WkPrice` | String | Precio original (solo Canvas de bajada de precio) |
| `WKSalePrice` | String | Precio de oferta (solo Canvas de bajada de precio) |
| `WkQuantity` | String | Unidades restantes (solo Canvas de stock bajo) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Campos específicos de Canvas y valores de `WkPurpose`

| Tipo de Canvas | Valor de `WkPurpose` | Campos adicionales |
| ----------- | ----------------- | ------------------- |
| Abandono del carrito de compras | `"cart abandonment"` | `WkCartReplenUrl` — URL para reponer el carrito |
| Abandono de producto | `"product abandonment"` | — |
| Resumen de categoría | `"category recap"` | `WkCategoryUrl` — URL de la categoría navegada |
| De vuelta en stock | `"back in stock"` | — |
| Bajada de precio | `"price drop"` | `WkPrice`, `WKSalePrice` en cada artículo |
| Stock bajo | `"low stock"` | `WkQuantity` en cada artículo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Cargas útiles de ejemplo

Cada objeto en `recipients` debe incluir exactamente uno de `external_user_id`, `user_alias`, `braze_id` o `email`. Para más información, consulta el [Objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object/).

{% alert note %}
Cada ejemplo usa **un** identificador de destinatario de Braze. Los primeros seis usan solo `user_alias`; el último usa solo `email` con [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email). El JSON de ejemplo omite la clave `WkChannel` dentro de `context` para que las herramientas de revisión no confundan su valor (`"email"`) con el campo `email` del destinatario de Braze. En producción, incluye `"WkChannel": "email"` en `context` como se documenta en la [tabla de campos comunes (todos los tipos de Canvas)](#canvas-types-table).
{% endalert %}

Los siguientes ejemplos usan `user_alias` con `wknd_email_id`, coincidiendo con la forma en que Wunderkind resuelve identidades.

{% details Carga útil de ejemplo de abandono del carrito de compras %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Carga útil de ejemplo de abandono de producto %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Carga útil de ejemplo de resumen de categoría %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Carga útil de ejemplo de vuelta en stock %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Carga útil de ejemplo de bajada de precio %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Carga útil de ejemplo de stock bajo %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Ejemplo con identificador de correo electrónico (alternativo) %}
Si desencadenas el Canvas con el campo `email` de Braze en lugar de `user_alias`, el destinatario debe incluir solo `email` y `prioritization` (consulta [Enviar mensajes Canvas usando entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). El objeto `context` coincide con los otros ejemplos.

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Ejemplo de uso de Liquid

Cuando Wunderkind llama a `/canvas/trigger/send`, las claves y valores que pasas en el objeto `context` de cada destinatario se convierten en datos de entrada de Canvas. En los pasos de mensaje, haz referencia a ellos con el espacio de nombres Liquid `context`. Un ejemplo es {% raw %}`{{context.${WkPurpose}}}`{% endraw %} como se describe en [Objeto de contexto de Canvas]({{site.baseurl}}/api/objects_filters/context_object/) y [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/). No se requiere configuración adicional más allá de usar la sintaxis Liquid correcta.

No anides etiquetas de salida de Braze dentro de la condición de la etiqueta `for`. Asigna primero el array `Items` de `context` a una variable y luego itera, como se describe en [Uso de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#use-a-filter-result-in-a-for-loop). La línea `assign` usa el formato de entrada de Canvas de Braze {% raw %}`{{context.${Items}}}`{% endraw %} (consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#summary-of-supported-tags)).

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## Informes

Wunderkind ingiere datos de rendimiento de Braze usando **Braze Currents**, que transmite eventos sin procesar a Google Cloud Storage. Wunderkind luego normaliza y agrega estos eventos contra la señal de origen para informes de atribución 1:1.

Las siguientes métricas estarán disponibles próximamente en el dashboard de informes de Wunderkind:

| Métrica | Fuente |
| ------ | ------ |
| Envíos entregados | Braze Currents |
| Aperturas de correo electrónico | Braze Currents |
| Clics | Braze Currents |
| Conversiones | Braze Currents (evento definido en la configuración) |
| Cancelaciones de suscripción | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitaciones

- **Sin sincronización de supresión/exclusión.** La supresión debe gestionarse de forma nativa en Braze. Nota: Para clientes existentes de Wunderkind que migran a Braze Signals, Wunderkind trabaja con tu equipo para preservar tu configuración actual.
- **Solo canal de correo electrónico.** SMS no está soportado actualmente a través de esta integración.
- **El perfil de usuario debe existir antes del desencadenador de Canvas.** [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) con un destinatario `user_alias` resuelve solo perfiles de Braze **existentes** que ya tienen ese alias. No puedes usar `send_to_existing_only` con alias, y el desencadenador de Canvas no crea un perfil completamente nuevo solo a partir del alias. El usuario debe ser creado o actualizado y el alias `wknd_email_id` debe establecerse primero (por ejemplo, usando [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) o [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)). Wunderkind puede esperar brevemente después de esa actualización para que Braze termine de procesar antes de disparar el desencadenador.
- **Correo electrónico como identificador.** Si el desencadenador de Canvas identifica al destinatario con `email` en lugar de `user_alias`, incluye [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) en ese objeto de destinatario, como lo requiere Braze.


## Recursos adicionales

- [Centro de ayuda de Wunderkind — Resumen de Signals para Braze](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Portal de desarrolladores de Wunderkind — Resumen de integración](https://developer.wunderkind.co/docs/integration-overview)
- [Enviar mensajes Canvas usando entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [Objeto de contexto de Canvas]({{site.baseurl}}/api/objects_filters/context_object/)
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)