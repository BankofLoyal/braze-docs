---
nav_title: Snowplow
article_title: Snowplow
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Snowplow, einer Plattform für Dateninfrastruktur, die es Ihnen ermöglicht, Snowplow-Events in Realtime an Braze weiterzuleiten, indem Sie Snowplows Event Forwarding nutzen."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplow.io) ist eine skalierbare Open-Source-Plattform für eine umfangreiche, qualitativ hochwertige Datenerfassung mit geringer Latenz. Snowplow wurde entwickelt, um hochwertige, vollständige Verhaltensdaten für Unternehmen zu sammeln.

_Diese Integration wird von Snowplow gepflegt._

## Über die Integration

Die Integration von Braze und Snowplow ermöglicht es Ihnen, Snowplow-Events in Realtime an Braze weiterzuleiten – mit Hilfe der Snowplow Event Forwarding Lösung. Diese Integration bietet Ihnen die Möglichkeit, Events an Braze zu senden und dabei volle Flexibilität und Kontrolle zu behalten. Genauer gesagt können Sie:
- Events filtern und transformieren, bevor sie an Braze gesendet werden.
- Snowplow-Event-Daten auf Braze-Attribute, angepasste Events und Käufe abbilden.
- Alle Daten in Ihrer privaten Cloud aufbewahren, bis Sie sich entscheiden, sie weiterzuleiten.
- Die Lösung selbst innerhalb Ihres bestehenden Snowplow-Cloud-Kontos bereitstellen. 

Das [Event Forwarding](https://docs.snowplow.io/docs/destinations/forwarding-events/) von Snowplow ist ein kostenpflichtiges Add-on-Feature, das Snowplow-Kund:innen zur Verfügung steht. Um Events ohne dieses Add-on an Braze weiterzuleiten, verwenden Sie die [Google Tag Manager Server-Side](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/)-Integration von Snowplow.

Nutzen Sie die umfangreichen Verhaltensdaten von Snowplow, um leistungsstarke kundenorientierte Interaktionen in Braze voranzutreiben und personalisierte Nachrichten in Realtime zuzustellen.

## Voraussetzungen

| Anforderung             | Beschreibung                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snowplow-Pipeline       | Sie benötigen eine funktionsfähige Snowplow-Pipeline.                                                                                                                                                                                                                                          |
| Zugang zur Snowplow-Konsole | Sie müssen Zugriff auf die Snowplow-Konsole haben, um Event-Forwarder zu konfigurieren.                                                                                                                                                                                                                                |
| Braze REST-API-Schlüssel      | Ein Braze REST-API-Schlüssel mit den folgenden Berechtigungen: `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename` und `users.alias.update`. <br><br> Sie können diesen im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellen. |
| Braze REST-Endpunkt     | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

### Personalisierte, aktionsbasierte Zustellung
Verwenden Sie eines der zahlreichen Events, die Snowplow standardmäßig erfasst, oder definieren Sie angepasste Events, um noch detailliertere Customer Journeys zu gestalten, die für Ihr Unternehmen sinnvoll sind. Nutzen Sie die reichhaltigen Verhaltensdaten von Snowplow, um Kunden-Funnel zu entwerfen und Ihren Marketing- und Produkt-Teams dabei zu helfen, Konversion und Produktnutzung durch Braze zu maximieren.

### Dynamische Segmentierung
Erstellen Sie dynamische Zielgruppen in Braze auf der Grundlage der hochwertigen Verhaltensdaten von Snowplow: Wenn Nutzer:innen in Ihrem Produkt, Ihrer App oder auf Ihrer Website Aktionen durchführen, können Sie die von Snowplow in Realtime erfassten Verhaltensdaten nutzen, um Nutzer:innen automatisch zu relevanten Segmenten in Braze hinzuzufügen oder daraus zu entfernen.

## Integration

### 1. Schritt: Konfigurieren Sie das Ziel in der Snowplow-Konsole

So erstellen Sie den Event Forwarder:

1. Navigieren Sie in der Snowplow-Konsole zu **Destinations** und wählen Sie **Create new destination**.
2. Wenn Sie die Verbindung konfigurieren, wählen Sie **Braze** als Verbindungstyp aus.
3. Geben Sie Ihren Braze-API-Schlüssel und Ihren REST-API-Endpunkt ein.
4. Speichern Sie die Verbindung.

### 2. Schritt: Konfigurieren Sie den Event Forwarder

Bei der Konfiguration des Forwarders können Sie auswählen, welche Snowplow-Events weitergeleitet werden sollen, und sie auf Braze-Objekttypen abbilden:

1. **[Attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object)**: Aktualisieren Sie die Daten des Nutzerprofils und angepasste Nutzer:innen-Eigenschaften.
2. **[Angepasste Events]({{site.baseurl}}/api/objects_filters/event_object)**: Senden Sie Nutzer:innen-Aktionen und Verhaltensweisen.
3. **[Käufe]({{site.baseurl}}/api/objects_filters/purchase_object)**: Senden Sie Transaktionsdaten mit Produktdetails.

Für jeden Objekttyp können Sie Feldzuordnungen konfigurieren, um festzulegen, wie Snowplow-Event-Daten auf Braze-Felder abgebildet werden. Detaillierte Anweisungen zur Einrichtung und Konfiguration der Feldzuordnungen finden Sie in der Snowplow-Dokumentation zum [Erstellen von Forwardern](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/).

### 3. Schritt: Validieren Sie die Integration

Überprüfen Sie, ob die Events Braze erreichen, indem Sie die folgenden Seiten in Ihrem Braze-Konto aufrufen:

1. **Query Builder**: Navigieren Sie in Braze zu **Analytics** > **Query Builder**. Sie können Abfragen zu den folgenden Tabellen schreiben, um eine Vorschau der von Snowplow weitergeleiteten Daten zu erhalten: `USER_BEHAVIORS_CUSTOMEVENT_SHARED` und `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **API-Nutzungs-Dashboard**: Navigieren Sie in Braze zu **Einstellungen** > **APIs und Bezeichner**, um ein Chart der API-Nutzung im Zeitverlauf anzuzeigen. Sie können speziell nach dem API-Schlüssel filtern, den Snowplow verwendet, und sowohl Erfolge als auch Fehler einsehen.

## Angepasste Eigenschaften senden

Sie können angepasste Eigenschaften über die Standardfelder hinaus senden. Die Struktur hängt davon ab, welchen Braze-Objekttyp Sie verwenden:

- **Attribute**: Fügen Sie sie als Top-Level-Felder hinzu (zum Beispiel `subscription_tier`, `loyalty_points`)
- **Event-Eigenschaften**: Verschachteln Sie sie unter dem `properties`-Objekt (zum Beispiel `properties.plan_type`, `properties.feature_flag`)
- **Kauf-Eigenschaften**: Verschachteln Sie sie unter dem `properties`-Objekt (zum Beispiel `properties.color`, `properties.size`)

Für Eigenschaftsnamen, die Leerzeichen enthalten, verwenden Sie die Klammerschreibweise (zum Beispiel `["account type"]` oder `properties["campaign source"]`).

Einzelheiten zu den unterstützten Datentypen, den Anforderungen an die Benennung der Eigenschaften und den Größenbeschränkungen für die Nutzdaten finden Sie in der [Dokumentation zum Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object).

## Einschränkungen

**Rate-Limits:** Braze erzwingt ein Rate-Limit von 3.000 API-Aufrufen alle drei Sekunden für die Track Users API. Da Snowplow keine Stapelverarbeitung für Event-Forwarder unterstützt, fungiert dieses API-Rate-Limit auch als Rate-Limit für Events. Wenn Ihr Eingabedurchsatz 3.000 Events pro drei Sekunden überschreitet, kann es zu erhöhten Latenzzeiten kommen.