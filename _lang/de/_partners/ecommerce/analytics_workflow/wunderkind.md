---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "Dieser Referenzartikel behandelt die Integration von Wunderkind Signals mit Braze, einschließlich Verhaltenssignale, die Canvas-Journeys triggern, die Einrichtung mit der Canvas Entry API, den Canvas-Kontext-Payload bei API-getriggerter Zustellung und Reporting."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) ist eine E-Commerce-Performance-Plattform, die proprietäre Identifizierungstechnologie nutzt, um anonyme Website-Besucher:innen zu erkennen und sie zu verwertbaren E-Mail-Adressen aufzulösen. Im Durchschnitt skaliert Wunderkind die Identifizierung von 3 bis 5 % des Website-Traffics auf 40 bis 60 %, sodass Marken personalisierte, eins-zu-eins-Nachrichten im großen Maßstab über ihren bestehenden ESP triggern können.

*Diese Integration wird von Wunderkind gepflegt. Für Support besuchen Sie [support.wunderkind.co](https://support.wunderkind.co).*

## Über die Integration

Die Integration von Wunderkind Signals ermöglicht es, Verhaltenssignale mit hoher Absicht – wie abgebrochener Einkauf, Produktabbruch und Preissenkungen – in Realtime Canvas-Journeys in Braze zu triggern. Wunderkind identifiziert anonyme Nutzer:innen auf Ihrer Website, löst deren Identität zu einer zustellbaren E-Mail-Adresse auf und liefert einen strukturierten Signal-Payload über die Canvas Entry API an Braze, wodurch Ihre vorkonfigurierten E-Mail-Flows automatisch gestartet werden.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Wunderkind-Konto | Ein Wunderkind-Konto mit aktivierten Signals ist erforderlich. Kontaktieren Sie Ihre Wunderkind-Vertretung, um die Berechtigung zu bestätigen. |
| Braze-Konto | Ein Braze-Konto mit Canvas-Zugang ist erforderlich. Dem Wunderkind-Team muss ein Platz in Ihrem Konto gewährt werden. Alle Details finden Sie unter [Wunderkind Zugang zu Ihrem Braze-Konto gewähren](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account). |
| Braze REST-API-Schlüssel | Sie erstellen während der Einrichtung einen dedizierten API-Schlüssel mit bestimmten Berechtigungen (siehe [1. Schritt](#step-1-create-a-braze-api-key-for-wunderkind)). |
| Nutzeridentifizierung | Wunderkind löst eine:n Verbraucher:in in Braze typischerweise über `user_alias` mit `alias_label: "wknd_email_id"` auf (häufig mit der E-Mail als `alias_name`). Jede:r [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)-Empfänger:in muss genau eines der folgenden Felder enthalten: `external_user_id`, `user_alias`, `braze_id` oder `email` ([Recipients-Objekt]({{site.baseurl}}/api/objects_filters/recipient_object/)); wenn Sie `email` verwenden, fügen Sie [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) hinzu. Bei Verwendung von `user_alias` muss das Profil bereits in Braze existieren, bevor der Trigger ausgelöst wird. Erstellen oder aktualisieren Sie Nutzer:innen und Aliase zunächst mit [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). Weitere Informationen finden Sie unter [Einschränkungen](#limitations). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## So funktioniert es

Wenn Wunderkind eine:n anonyme:n Nutzer:in mit hoher Absicht identifiziert und deren Identität auflöst, sendet es einen Signal-Payload über den `/canvas/trigger/send`-Endpunkt an Braze und triggert die entsprechende Canvas-Journey für diese:n Nutzer:in in Realtime.

Einen vollständigen technischen Überblick finden Sie im [Wunderkind Developer Portal](https://developer.wunderkind.co/docs/integration-overview).

## Integration

### 1. Schritt: Einen Braze-API-Schlüssel für Wunderkind erstellen

In Ihrem Braze-Dashboard:

1. Gehen Sie zu **Einstellungen** > **API-Schlüssel** und klicken Sie auf **Neuen API-Schlüssel erstellen**.
2. Geben Sie dem Schlüssel einen aussagekräftigen Namen (zum Beispiel `Wunderkind Signals`).
3. Gewähren Sie die Berechtigungen, die unter [Wunderkind Zugang zu Ihrem Braze-Konto gewähren](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account) aufgeführt sind.
4. Kopieren Sie den API-Schlüssel, um ihn im nächsten Abschnitt in der Wunderkind-Plattform einzugeben.

{% alert note %}
Für Wunderkind Signals werden Braze [REST API]({{site.baseurl}}/api/basics/)-Anfragen mit einem REST-API-Schlüssel authentifiziert, nicht mit OAuth-Token. Erstellen Sie einen dedizierten API-Schlüssel im Dashboard und stellen Sie diesen Schlüssel Wunderkind zur Verfügung.
{% endalert %}

### 2. Schritt: Braze mit der Wunderkind-Plattform verbinden

1. Melden Sie sich bei der Wunderkind-Plattform an und gehen Sie zum **Integrations Hub**.
2. Wählen Sie die **Braze**-Kachel und dann **Verbinden** aus.
3. Geben Sie Ihren Braze REST-API-Schlüssel ein und wählen Sie Ihren Cluster aus.
4. Wählen Sie **Speichern** aus.

### 3. Schritt: Neue Braze-Assets überprüfen

Nach der Aktivierung stellt Wunderkind neue Implementierungs-Assets in Ihrem Braze-Workspace bereit, basierend auf der mit Ihrer Wunderkind-Vertretung abgestimmten Strategie:

| Asset-Typ | Erstellungsmethode durch Wunderkind |
| ---------- | -------------------------- |
| Content-Blöcke | Automatisch |
| API-getriggerte Canvase | Managed Service |
| Tags, angepasste Attribute, Link-Templates | Managed Service |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 4. Schritt: Canvas-Einrichtung abschließen

Erstellen Sie für jeden Signals-Canvas Ihre E-Mail-Templates mit dem Drag-and-Drop-Editor oder HTML von Braze.

- Wunderkind befüllt Produkt- und Sitzungsdaten im `context`-Objekt jeder Empfängerin bzw. jedes Empfängers bei `/canvas/trigger/send` zum Sendezeitpunkt.
- Ausführliche Anleitungen zur Verwendung von Liquid mit diesem Payload in Ihren Templates finden Sie unter [Canvas-Einrichtung abschließen](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) im Wunderkind Help Center.

### 5. Schritt: Canvas-Berechtigung überprüfen

Gehen Sie für jeden Signals-Canvas zu den **Zielgruppe**-Einstellungen, um die Standard-Eingangs-Zielgruppe und Ausstiegskriterien von Wunderkind zu überprüfen.

- Um sicherzustellen, dass Sie Ihre Nutzer:innen nicht zu häufig kontaktieren, lesen Sie [Nutzerzentriertes Rate-Limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).
- Passen Sie die Einstellungen an, um zu verhindern, dass Nutzer:innen nach einem Kauf weiterhin Canvas-Nachrichten erhalten. Fügen Sie beispielsweise die Ausnahme **Kauf tätigen** hinzu.
- Bestimmte Signals-Canvase sind mit Filtern für angepasste Attribute vorkonfiguriert, damit Nutzer:innen die Nachricht mit der höchsten Absicht erhalten.
- Details zur Canvas-Berechtigung und Priorisierung finden Sie unter [Canvas-Berechtigung überprüfen](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) im Wunderkind Help Center.

### 6. Schritt: Testen und starten

Wunderkind führt vor dem Go-Live eine End-to-End-Qualitätssicherung durch:

- Bestätigen, dass Signale ohne API-Fehler an die richtigen Canvas-IDs zugestellt werden.
- Überprüfen, dass `context`-Felder (Produktname, Bild, URL) in den gerenderten E-Mail-Templates korrekt befüllt werden.
- Anleitungen zur Vorschau von Templates mit Wunderkind-Testprodukten finden Sie unter [Signals für Braze testen und starten](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) im Wunderkind Help Center.

Wenn die Qualitätssicherung bestanden ist, koordiniert Ihre Wunderkind-Implementierungsmanagerin bzw. Ihr Implementierungsmanager den Produktionsstart mit Ihrem Team.

## Canvas-Kontext-Payload

Wunderkind unterstützt sechs Signaltypen. Jeder liefert einen eigenen Satz von Schlüsseln und Werten innerhalb des [`context`]({{site.baseurl}}/api/objects_filters/context_object/)-Objekts für die jeweilige Empfängerin bzw. den jeweiligen Empfänger bei `/canvas/trigger/send` (siehe [Canvas-Nachrichten mit API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). Das Feld `WkPurpose` identifiziert den Signaltyp innerhalb dieses Payloads.

### Gemeinsame Felder (alle Canvas-Typen) {#canvas-types-table}

| Eigenschaft | Typ | Beschreibung |
| -------- | ---- | ----------- |
| `Origin` | String | Immer `"wunderkind"` |
| `DataOnly` | String | Immer `"Y"` — zeigt an, dass Wunderkind nur als Datenschicht agiert; Braze führt den Versand aus |
| `UserType` | String | `"prospect"` oder `"customer"` |
| `WkChannel` | String | Immer `"email"` für diese Integration |
| `WkPurpose` | String | Signaltyp-Bezeichner (siehe Werte pro Canvas unten) |
| `WKCouponCode` | String | Gutscheincode, falls zutreffend (leerer String, wenn nicht verwendet) |
| `WKCouponPurpose` | String | Beschreibung des Gutscheinangebots (leerer String, wenn nicht verwendet) |
| `Items` | Array | Array von Produktobjekten (siehe Produktfelder unten) |
| `WkOpen` | String | Tracking-Pixel, verfügbar für Reporting-Zwecke |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Produktartikel-Felder

| Eigenschaft | Typ | Beschreibung |
| -------- | ---- | ----------- |
| `WkCopy` | String | Produktname |
| `WkId` | String | Produkt-ID |
| `WkImageUrl` | String | Produktbild-URL |
| `WkUrl` | String | URL der Produktdetailseite |
| `WkPrice` | String | Originalpreis (nur Preissenkung-Canvas) |
| `WKSalePrice` | String | Aktionspreis (nur Preissenkung-Canvas) |
| `WkQuantity` | String | Verbleibende Einheiten (nur Niedriger-Bestand-Canvas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Canvas-spezifische Felder und `WkPurpose`-Werte

| Canvas-Typ | `WkPurpose`-Wert | Zusätzliche Felder |
| ----------- | ----------------- | ------------------- |
| Abgebrochener Einkauf | `"cart abandonment"` | `WkCartReplenUrl` — URL zum Wiederherstellen des Warenkorbs |
| Produktabbruch | `"product abandonment"` | — |
| Kategorie-Zusammenfassung | `"category recap"` | `WkCategoryUrl` — URL zur durchsuchten Kategorie |
| Wieder auf Lager | `"back in stock"` | — |
| Preissenkung | `"price drop"` | `WkPrice`, `WKSalePrice` bei jedem Artikel |
| Niedriger Bestand | `"low stock"` | `WkQuantity` bei jedem Artikel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Beispiel-Payloads

Jedes Objekt in `recipients` muss genau eines der folgenden Felder enthalten: `external_user_id`, `user_alias`, `braze_id` oder `email`. Weitere Informationen finden Sie im [Recipients-Objekt]({{site.baseurl}}/api/objects_filters/recipient_object/).

{% alert note %}
Jedes Beispiel verwendet **einen** Braze-Empfänger-Bezeichner. Die ersten sechs verwenden nur `user_alias`; das letzte verwendet nur `email` mit [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email). Das Beispiel-JSON lässt den `WkChannel`-Schlüssel innerhalb von `context` weg, damit Überprüfungstools dessen Wert (`"email"`) nicht mit dem Braze-Empfängerfeld `email` verwechseln. In der Produktion fügen Sie `"WkChannel": "email"` in `context` ein, wie in der [Tabelle Gemeinsame Felder (alle Canvas-Typen)](#canvas-types-table) dokumentiert.
{% endalert %}

Die folgenden Beispiele verwenden `user_alias` mit `wknd_email_id`, entsprechend der Art, wie Wunderkind Identitäten auflöst.

{% details Beispiel-Payload für abgebrochenen Einkauf %}
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

{% details Beispiel-Payload für Produktabbruch %}
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

{% details Beispiel-Payload für Kategorie-Zusammenfassung %}
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

{% details Beispiel-Payload für Wieder auf Lager %}
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

{% details Beispiel-Payload für Preissenkung %}
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

{% details Beispiel-Payload für Niedriger Bestand %}
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

{% details Beispiel mit E-Mail-Bezeichner (Alternative) %}
Wenn Sie den Canvas mit dem Braze-Feld `email` anstelle von `user_alias` triggern, muss die Empfängerin bzw. der Empfänger nur `email` und `prioritization` enthalten (siehe [Canvas-Nachrichten mit API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). Das `context`-Objekt entspricht den anderen Beispielen.

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

### Beispiel für die Liquid-Verwendung

Wenn Wunderkind `/canvas/trigger/send` aufruft, werden die Schlüssel und Werte, die Sie im `context`-Objekt jeder Empfängerin bzw. jedes Empfängers übergeben, zu Canvas-Eingangsdaten. In Nachrichten-Schritten referenzieren Sie diese mit dem `context`-Liquid-Namespace. Ein Beispiel ist {% raw %}`{{context.${WkPurpose}}}`{% endraw %}, wie unter [Canvas-Kontext-Objekt]({{site.baseurl}}/api/objects_filters/context_object/) und [Nachricht]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) beschrieben. Über die korrekte Liquid-Syntax hinaus ist keine zusätzliche Konfiguration erforderlich.

Verschachteln Sie keine Braze-Ausgabe-Tags innerhalb der `for`-Tag-Bedingung. Weisen Sie das `Items`-Array aus `context` zuerst einer Variablen zu und iterieren Sie dann darüber, wie unter [Liquid verwenden]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#use-a-filter-result-in-a-for-loop) beschrieben. Die `assign`-Zeile verwendet das Braze Canvas-Eingangsformat {% raw %}`{{context.${Items}}}`{% endraw %} (siehe [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#summary-of-supported-tags)).

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

## Reporting

Wunderkind nimmt Performance-Daten aus Braze über **Braze-Currents** auf, die Roh-Events an Google Cloud Storage streamen. Wunderkind normalisiert und aggregiert diese Events dann gegen das auslösende Signal für 1:1-Attribution-Reporting.

Die folgenden Metriken werden in Kürze im Wunderkind-Reporting-Dashboard verfügbar sein:

| Metrik | Quelle |
| ------ | ------ |
| Zugestellte Sendungen | Braze-Currents |
| E-Mail-Öffnungen | Braze-Currents |
| Klicks | Braze-Currents |
| Konversionen | Braze-Currents (Event wird bei der Einrichtung definiert) |
| Abmeldungen | Braze-Currents |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Einschränkungen

- **Keine Unterdrückungs-/Opt-out-Synchronisierung.** Die Unterdrückung muss nativ in Braze verwaltet werden. Hinweis: Für bestehende Wunderkind-Kund:innen, die zu Braze Signals migrieren, arbeitet Wunderkind mit Ihrem Team zusammen, um Ihre aktuelle Einrichtung beizubehalten.
- **Nur E-Mail-Kanal.** SMS wird derzeit über diese Integration nicht unterstützt.
- **Nutzerprofil muss vor dem Canvas-Trigger existieren.** [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) mit einer `user_alias`-Empfängerin bzw. einem `user_alias`-Empfänger löst nur **bestehende** Braze-Profile auf, die diesen Alias bereits haben. Sie können `send_to_existing_only` nicht mit Aliasen verwenden, und der Canvas-Trigger erstellt kein komplett neues Profil allein aus dem Alias. Die Nutzerin bzw. der Nutzer muss zuerst erstellt oder aktualisiert und der `wknd_email_id`-Alias gesetzt werden (zum Beispiel mit [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)). Wunderkind wartet möglicherweise kurz nach diesem Upsert, damit Braze die Verarbeitung abschließen kann, bevor der Trigger ausgelöst wird.
- **E-Mail als Bezeichner.** Wenn der Canvas-Trigger die Empfängerin bzw. den Empfänger mit `email` anstelle von `user_alias` identifiziert, fügen Sie [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) zu diesem Empfängerobjekt hinzu, wie von Braze gefordert.


## Zusätzliche Ressourcen

- [Wunderkind Help Center — Signals für Braze Übersicht](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Wunderkind Developer Portal — Integrationsübersicht](https://developer.wunderkind.co/docs/integration-overview)
- [Canvas-Nachrichten mit API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [Canvas-Kontext-Objekt]({{site.baseurl}}/api/objects_filters/context_object/)
- [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)