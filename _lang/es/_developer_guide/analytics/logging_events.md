---
nav_title: Registrar eventos personalizados
article_title: Registrar eventos personalizados a través del SDK de Braze
page_order: 3.1
description: "Aprende a registrar eventos personalizados a través del SDK de Braze."

---

# Registrar eventos personalizados

> Aprende a registrar eventos personalizados a través del SDK de Braze.

{% alert note %}
Para los SDK envolventes que no aparecen en la lista, utiliza el método nativo de Android o SWIFT correspondiente.
{% endalert %}

## Registro de un evento personalizado

Para registrar un evento personalizado, utiliza el siguiente método de registro de eventos.

{% tabs %}
{% tab web %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Si prefieres utilizar Google Tag Manager, puedes usar el tipo de etiqueta **Evento personalizado** para llamar al [método `logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) y enviar eventos personalizados a Braze, incluyendo opcionalmente propiedades del evento personalizado. Para ello:

1. Introduce el **nombre del evento** utilizando una variable o escribiendo un nombre de evento.
2. Utiliza el botón **Añadir fila** para añadir propiedades del evento.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción de Braze. Las configuraciones incluidas son «tipo de etiqueta» (evento personalizado), «nombre del evento» (clic en el botón) y «propiedades del evento».]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
Para Android nativo, puedes utilizar el siguiente método:

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab cordova %}
Utiliza el método del complemento de Braze para Cordova:

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

La API `logCustomEvent` acepta:
- `eventName` (cadena obligatoria): Utiliza hasta 255 caracteres. No comiences el nombre con `$`. Utiliza caracteres alfanuméricos y signos de puntuación.
- `eventProperties` (objeto opcional): Añade pares clave-valor para los metadatos del evento. Utiliza claves de hasta 255 caracteres y no empieces las claves con `$`.

Para los valores de propiedad, utiliza `string` (hasta 255 caracteres), `numeric`, `boolean`, matrices u objetos JSON anidados.

Para obtener más información sobre la implementación, consulta el código fuente del SDK de Braze para Cordova:
- [Método `logCustomEvent` en `www/BrazePlugin.js` (líneas 138-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [JSDoc en `www/BrazePlugin.js` (líneas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Controlador Android en `src/android/BrazePlugin.kt` (líneas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Controlador iOS en `src/ios/BrazePlugin.m` (líneas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [Declaración del método iOS en `src/ios/BrazePlugin.h` (línea 24)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
Si has integrado [Infillion Beacons](https://infillion.com/software/beacons/) en tu aplicación Android, puedes utilizar opcionalmente `visit.getPlace()` para registrar eventos específicos de ubicación. `requestImmediateDataFlush` verifica que tu evento se registre incluso si tu aplicación está en segundo plano.

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## Añadir propiedades de metadatos

Cuando registras un evento personalizado, tienes la opción de añadir metadatos sobre ese evento personalizado pasando un objeto de propiedades con el evento. Las propiedades se definen como pares clave-valor. Las claves son cadenas y los valores pueden ser `string`, `numeric`, `boolean`, objetos [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp), matrices u objetos JSON anidados.

Para agregar propiedades de metadatos, utiliza el siguiente método de registro de eventos.

{% tabs %}
{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab cordova %}
Registra eventos personalizados con un objeto de propiedades:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

También puedes pasar propiedades en línea:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

La aplicación de muestra oficial de Cordova incluye propiedades de cadena, numéricas, booleanas, de matriz y de objetos anidados:
- [`sample-project/www/js/index.js` (líneas 230-251)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

Extracto del proyecto de ejemplo:

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

Para obtener más información sobre la API y el puente nativo, consulta:
- [JSDoc en `www/BrazePlugin.js` (líneas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Controlador Android en `src/android/BrazePlugin.kt` (líneas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Controlador iOS en `src/ios/BrazePlugin.m` (líneas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
Las claves `time` y `event_name` están reservadas y no pueden utilizarse como propiedades del evento personalizado.
{% endalert %}

## Buenas prácticas

Hay tres comprobaciones importantes que debes realizar para que las propiedades del evento personalizado se registren según lo esperado:

* [Establecer qué eventos se registran](#verify-events)
* [Verificar el registro](#verify-log)
* [Verificar los valores](#verify-values)

Se pueden registrar varias propiedades cada vez que se registra un evento personalizado.

### Verificar eventos

Comprueba con tus desarrolladores qué propiedades del evento están siendo objeto de seguimiento. Ten en cuenta que todas las propiedades del evento distinguen entre mayúsculas y minúsculas. Para obtener información adicional sobre el seguimiento de eventos personalizados, consulta estos artículos según tu plataforma:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### Verificar el registro

Para confirmar que las propiedades del evento se han registrado correctamente, puedes ver todas las propiedades del evento desde la página **Eventos personalizados**.

1. Ve a **Configuración de datos** > **Eventos personalizados**.
2. Localiza tu evento personalizado en la lista.
3. Para tu evento, selecciona **Administrar propiedades** para ver los nombres de las propiedades asociadas a un evento.

### Verificar los valores

Después de [añadir tu usuario como usuario de prueba]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), sigue estos pasos para verificar tus valores: 

1. Realiza el evento personalizado dentro de la aplicación.
2. Espera unos 10 segundos a que se vacíen los datos.
3. Actualiza el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) para ver el evento personalizado y el valor de la propiedad del evento que se pasó con él.

## Solución de problemas de eventos personalizados

Utiliza estos escenarios para solucionar problemas de registro de eventos personalizados en los distintos SDK.

### Verificar el desencadenante del evento personalizado

Si un evento personalizado no aparece, es posible que la acción rastreada en tu aplicación no coincida con la acción que estás probando.

- Confirma con tu equipo de desarrolladores qué acción de la aplicación desencadena el evento personalizado.
- Comprueba si hay rutas de código obsoletas después de actualizaciones del SDK, como referencias a `appboy` en lugar de `braze`.

### Los eventos personalizados se registran en un perfil anónimo

Si no identificas a un usuario antes de registrar un evento personalizado, Braze puede asociar ese evento con un perfil anónimo.

- Llama a `changeUser()` antes de realizar el evento personalizado para que Braze lo registre en un perfil de usuario identificado.
- Prueba con un usuario de prueba identificado y luego revisa el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/).

### Verificar la configuración del registro de eventos personalizados

Si los eventos personalizados no aparecen como se espera, confirma que tu equipo de desarrolladores ha implementado el registro de eventos personalizados para la acción correcta de la aplicación.

- Pide a tu equipo de desarrolladores que verifique que el evento se registra correctamente y se desencadena desde la acción de usuario esperada.
- Cuando tu equipo abra un ticket con soporte de Braze, incluye [registros detallados]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) y fragmentos de código relevantes.
- Si tu aplicación usa SWIFT o Android, tu equipo de desarrolladores puede utilizar los [requisitos previos del depurador del SDK](https://www.braze.com/docs/developer_guide/sdk_integration/debugging/#prerequisites) para ayudar a generar registros detallados.
- Si tu equipo de desarrolladores no puede identificar el problema, abre un [ticket de soporte de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/).