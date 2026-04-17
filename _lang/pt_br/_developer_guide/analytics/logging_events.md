---
nav_title: Registre eventos personalizados
article_title: Registre eventos personalizados através do SDK da Braze
page_order: 3.1
description: "Aprenda como registrar eventos personalizados através do SDK da Braze."

---

# Registre eventos personalizados

> Aprenda como registrar eventos personalizados através do SDK da Braze.

{% alert note %}
Para wrapper SDKs não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

## Registro de um evento personalizado

Para registrar um evento personalizado, use o seguinte método de registro de eventos.

{% tabs %}
{% tab web %}
Para uma implementação padrão do SDK Web, você pode usar o seguinte método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Se você preferir usar o Google Tag Manager, pode usar o tipo de tag **Evento Personalizado** para chamar o [método `logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) e enviar eventos personalizados para a Braze, incluindo opcionalmente propriedades de eventos personalizados. Para fazer isso:

1. Digite o **Nome do Evento** usando uma variável ou digitando um nome de evento.
2. Use o botão **Adicionar Linha** para adicionar propriedades de eventos.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação da Braze. As configurações incluídas são "tipo de tag" (evento personalizado), "nome do evento" (clique no botão) e "propriedades do evento".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
Para Android nativo, você pode usar o seguinte método:

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
Use o método do plugin Braze Cordova:

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

A API `logCustomEvent` aceita:
- `eventName` (string obrigatória): Use até 255 caracteres. Não comece o nome com `$`. Use caracteres alfanuméricos e pontuação.
- `eventProperties` (objeto opcional): Adicione pares chave-valor para metadados do evento. Use chaves de até 255 caracteres e não comece as chaves com `$`.

Para valores de propriedade, use `string` (até 255 caracteres), `numeric`, `boolean`, arrays ou objetos JSON aninhados.

Para detalhes de implementação, veja o código-fonte do SDK Braze Cordova:
- [Método `logCustomEvent` em `www/BrazePlugin.js` (linhas 138-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [JSDoc em `www/BrazePlugin.js` (linhas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Manipulador Android em `src/android/BrazePlugin.kt` (linhas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Manipulador iOS em `src/ios/BrazePlugin.m` (linhas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [Declaração de método iOS em `src/ios/BrazePlugin.h` (linha 24)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
Se você integrou o [Infillion Beacons](https://infillion.com/software/beacons/) ao seu app Android, pode opcionalmente usar `visit.getPlace()` para registrar eventos específicos de localização. O `requestImmediateDataFlush` garante que seu evento será registrado mesmo que o app esteja em segundo plano.

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

## Adicionando propriedades de metadados

Quando você registra um evento personalizado, tem a opção de adicionar metadados sobre esse evento passando um objeto de propriedades junto com ele. As propriedades são definidas como pares chave-valor. As chaves são strings e os valores podem ser `string`, `numeric`, `boolean`, objetos [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp), arrays ou objetos JSON aninhados.

Para adicionar propriedades de metadados, use o seguinte método de registro de eventos.

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
Registre eventos personalizados com um objeto de propriedades:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

Você também pode passar propriedades inline:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

O app de exemplo oficial do Cordova inclui propriedades de string, numéricas, booleanas, array e objetos aninhados:
- [`sample-project/www/js/index.js` (linhas 230-251)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

Trecho do projeto de exemplo:

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

Para detalhes da API e da ponte nativa, veja:
- [JSDoc em `www/BrazePlugin.js` (linhas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Manipulador Android em `src/android/BrazePlugin.kt` (linhas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Manipulador iOS em `src/ios/BrazePlugin.m` (linhas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
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
As chaves `time` e `event_name` são reservadas e não podem ser usadas como propriedades de eventos personalizados.
{% endalert %}

## Melhores práticas

Existem três verificações importantes a serem realizadas para que as propriedades do seu evento personalizado sejam registradas conforme o esperado:

* [Estabeleça quais eventos são registrados](#verify-events)
* [Verifique o registro](#verify-log)
* [Verifique os valores](#verify-values)

Várias propriedades podem ser registradas cada vez que um evento personalizado é registrado.

### Verificar eventos

Verifique com seus desenvolvedores quais propriedades de eventos estão sendo rastreadas. Lembre-se de que todas as propriedades de eventos diferenciam maiúsculas de minúsculas. Para mais informações sobre rastreamento de eventos personalizados, confira estes artigos com base na sua plataforma:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### Verificar registro

Para confirmar que as propriedades do evento estão sendo rastreadas com sucesso, você pode visualizar todas as propriedades do evento na página de **Eventos personalizados**.

1. Acesse **Configurações de Dados** > **Eventos personalizados**.
2. Localize seu evento personalizado na lista.
3. Para seu evento, selecione **Gerenciar Propriedades** para visualizar os nomes das propriedades associadas a um evento.

### Verificar valores

Após [adicionar seu usuário como um usuário teste]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), siga estas etapas para verificar seus valores: 

1. Execute o evento personalizado dentro do app.
2. Aguarde cerca de 10 segundos para que os dados sejam enviados.
3. Atualize o [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) para ver o evento personalizado e o valor da propriedade do evento que foi passado com ele.

## Solução de problemas de eventos personalizados

Use estes cenários para solucionar problemas de registro de eventos personalizados nos SDKs.

### Verificando o gatilho do evento personalizado

Se um evento personalizado não aparece, a ação rastreada no seu app pode não corresponder à ação que você está testando.

- Confirme com sua equipe de desenvolvimento qual ação do app dispara o evento personalizado.
- Verifique se há caminhos de código obsoletos após upgrades do SDK, como referências a `appboy` em vez de `braze`.

### Eventos personalizados são registrados em um perfil anônimo

Se você não identificar um usuário antes de registrar um evento personalizado, a Braze pode associar esse evento a um perfil anônimo.

- Chame `changeUser()` antes de executar o evento personalizado para que a Braze registre o evento em um perfil de usuário identificado.
- Teste com um usuário teste identificado e depois revise o [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/).

### Verificando a configuração do registro de eventos personalizados

Se os eventos personalizados não estão aparecendo conforme o esperado, confirme que sua equipe de desenvolvimento implementou o registro de eventos personalizados para a ação correta do app.

- Peça à sua equipe de desenvolvimento para verificar se o evento está sendo registrado corretamente e disparado a partir da ação esperada do usuário.
- Quando sua equipe abrir um ticket com o suporte da Braze, inclua [logs detalhados]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) e trechos de código relevantes.
- Se seu app usa Swift ou Android, sua equipe de desenvolvimento pode usar os [pré-requisitos do depurador do SDK](https://www.braze.com/docs/developer_guide/sdk_integration/debugging/#prerequisites) para ajudar a gerar logs detalhados.
- Se sua equipe de desenvolvimento não conseguir identificar o problema, abra um [ticket de suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/).