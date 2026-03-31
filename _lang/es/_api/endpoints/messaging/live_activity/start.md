---
nav_title: "POST: Iniciar actividad en vivo"
article_title: "POST: Iniciar actividad en vivo"
search_tag: Punto de conexión
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Iniciar actividad en vivo."

---
{% api %}
# Iniciar actividad en vivo
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Utiliza este punto de conexión para iniciar remotamente [actividades en vivo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) mostradas en tu aplicación iOS. Este punto de conexión requiere una configuración adicional.

Después de crear una actividad en vivo, puedes hacer una solicitud POST para iniciar remotamente tu actividad para cualquier segmento dado. Para más información sobre las actividades en vivo de Apple, consulta [Iniciar y actualizar actividades en vivo con notificaciones push de ActivityKit](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

Si `content-available` no se configura, la prioridad predeterminada del servicio de notificaciones push de Apple (APN) es 10. Si `content-available` se establece, esta prioridad es 5. Consulta [el objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object) para obtener más detalles.

{% alert tip %}
Para finalizar una actividad en vivo, utiliza el punto de conexión [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) con `end_activity` establecido en `true`.
{% endalert %}

## Programar el descarte automático

Para programar el descarte automático después de que se inicie una actividad en vivo, programa una solicitud de seguimiento al punto de conexión de actualización desde tu backend.

1. Envía una solicitud `/messages/live_activity/start` con un `activity_id` que puedas reutilizar más adelante.
2. Almacena ese `activity_id` y la hora de finalización objetivo en el programador de tu backend.
3. En la hora de finalización objetivo, envía una solicitud `/messages/live_activity/update` con `end_activity` establecido en `true`.
4. Configura el comportamiento de descarte en la misma solicitud de actualización. Para más detalles, consulta el punto de conexión [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/).
5. Verifica los eventos de envío y resultado en el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Requisitos previos

Para utilizar este punto de conexión, tendrás que completar lo siguiente:

- Genera una clave de API con el permiso `messages.live_activity.start`.
- [Crea una actividad en vivo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift#swift_create-an-activity) utilizando el SDK de Braze para Swift.

{% multi_lang_include api/payload_size_alert.md %}

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`",
  // One of the following:
  "external_user_ids": "(optional, array of strings) see external user identifier, maximum 50",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Parámetros de la solicitud

| Parámetro | Obligatorio | Tipo de datos| Descripción  |
|-----------|----------|----------|--------------|
| `app_id` | Obligatorio | Cadena | [Identificador de API]({{site.baseurl}}/api/identifier_types/#the-app-identifier) de la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).  |
| `activity_id` | Obligatorio | Cadena  | Define una cadena personalizada como tu `activity_id`. Utilizarás este ID cuando desees enviar eventos de actualización o finalización a tu actividad en vivo.  |
| `activity_attributes_type`  | Obligatorio | Cadena | El tipo de atributos de actividad que defines en `liveActivities.registerPushToStart` en tu aplicación.  |
| `activity_attributes` | Obligatorio | Objeto  | Los valores estáticos de los atributos del tipo de actividad (como los nombres de los equipos deportivos, que no cambian). |
| `content_state` | Obligatorio | Objeto  | Los parámetros de `ContentState` se definen al crear la actividad en vivo. Pasa los valores actualizados para tu `ContentState` utilizando este objeto.<br><br>El formato de esta solicitud debe coincidir con la forma que definiste inicialmente. |
| `stale_date` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parámetro indica al sistema cuándo el contenido de la actividad en vivo se marca como obsoleto en la interfaz del usuario. |
| `notification` | Obligatorio | Objeto | Incluye un objeto [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) para definir una notificación push. El comportamiento de esta notificación push depende de si el usuario está activo o si está utilizando un dispositivo proxy. {::nomarkdown}<ul><li>Si se incluye un <code>notification</code> y el usuario está activo en su iPhone cuando se entrega la actualización, la interfaz de usuario actualizada de la actividad en vivo se deslizará hacia abajo y se mostrará como una notificación push.</li><li>Si se incluye un <code>notification</code> y el usuario no está activo en su iPhone, su pantalla se iluminará para mostrar la interfaz de usuario de la actividad en vivo actualizada en su pantalla de bloqueo.</li><li>La <code>notification alert</code> no se mostrará como una notificación push estándar. Además, si un usuario tiene un dispositivo proxy, como un Apple Watch, la <code>alert</code> se mostrará allí.</li></ul>{:/} |
| `external_user_ids` | Opcional si se proporciona `segment_id` o `audience` | Matriz de cadenas | Ver [ID de usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). Máximo 50 ID de usuario externos.  |
| `segment_id `  | Opcional si se proporciona `external_user_ids` o `audience` | Cadena    | Ver [identificador de segmento]({{site.baseurl}}/api/identifier_types/). |
| `custom_audience` | Opcional si se proporciona `external_user_ids` o `segment_id` | Objeto de audiencia conectada  | Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "football-chiefs-bills-2024-01-21",
    "content_state": {
        "teamOneScore": 0,
        "teamTwoScore": 0
    },
    "activity_attributes_type": "FootballActivity",
    "activity_attributes": {
        "team1Name": "Chiefs",
        "team2Name": "Bills"
    },
    "stale_date": "2024-01-22T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "The game is starting! Tune in soon!",
            "title": "Chiefs v. Bills"
        }
    },
    // One of the following required:
    "segment_id": "{YOUR-SEGMENT-API-IDENTIFIER}", // Optional
    "custom_audience": {...}, // Optional
    "external_user_ids": ["user-id1", "user-id2"], // Optional
}'
```

## Respuesta

Hay dos respuestas de código de estado para este punto de conexión: `201` y `4XX`.

### Ejemplo de respuesta correcta

Se devuelve un código de estado `201` si la solicitud se formateó correctamente y la recibimos. El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error

La clase de código de estado `4XX` indica un error del cliente. Consulta el [artículo de errores y respuestas de la API]({{site.baseurl}}/api/errors/) para obtener más información sobre los errores que puedes encontrar.

El código de estado `400` podría devolver el siguiente cuerpo de respuesta.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}