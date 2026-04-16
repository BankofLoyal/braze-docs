---
nav_title: Semantik der Zustellung von Events
article_title: Semantik der Zustellung von Events
page_order: 3
page_type: reference
description: "In diesem Referenzartikel wird erläutert und definiert, wie Currents die von uns an Data Warehouse-Speicherpartner gesendeten Flat-File-Event-Daten verwaltet."
tool: Currents

---

# Semantik der Zustellung von Events

> Auf dieser Seite wird beschrieben und definiert, wie Currents die Flat-File-Event-Daten verwaltet, die wir an Data Warehouse-Speicherpartner senden.

„Currents für Datenspeicher" ist ein kontinuierlicher Datenstrom von unserer Plattform zu einem Speicher-Bucket auf einer unserer Data Warehouse-[Partnerverbindungen]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/). Currents schreibt Avro-Dateien in regelmäßigen Abständen in Ihren Speicher-Bucket, sodass Sie die Event-Daten mit Ihrem eigenen Business-Intelligence-Toolset (BI) verarbeiten und analysieren können.

{% alert important %}
Dieser Inhalt **gilt nur für die Flat-File-Event-Daten, die wir an Data Warehouse-Speicherpartner (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden**. <br><br>Inhalte, die für andere Partner gelten, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) und auf den jeweiligen Seiten.
{% endalert %}

## Test-Events

Wenn Sie eine Currents-Integration einrichten, klicken Sie auf **Test-Events senden**, um die Verbindung mit Ihrem Speicher-Bucket zu überprüfen. Diese Test-Events bestätigen, dass Ihre Integration Daten korrekt empfangen und verarbeiten kann.

{% alert important %}
**Datenformat von Test-Events:** Test-Events enthalten Platzhalterwerte, die den korrekten Datentypen für jedes Feld entsprechen, jedoch keine realistischen oder genauen Daten enthalten. Beispielsweise kann ein `timezone`-Feld einen UUID-ähnlichen String anstelle eines gültigen Zeitzonen-Bezeichners (wie „America/Chicago") enthalten, und andere Felder wie `campaign_name` und `ip_pool` können ebenfalls Platzhalterwerte anstelle von tatsächlichen Daten enthalten.<br>

Dies ist das erwartete Verhalten. Test-Events dienen in erster Linie dazu, die Verbindung und die Integration zu testen, nicht jedoch dazu, die Richtigkeit der Daten zu validieren. Um reale Events mit genauen Daten zu sehen, verwenden Sie eine Test-Currents-Integration, um tatsächliche Event-Daten über Ihre Pipeline zu senden.
{% endalert %}

## Mindestens-einmal-Zustellung

Als System mit hohem Durchsatz bietet Currents eine „Mindestens-einmal"-Zustellung von Events, was bedeutet, dass gelegentlich doppelte Events in Ihren Speicher-Bucket geschrieben werden können. Dies kann passieren, wenn Events aus unserer Warteschlange aus irgendeinem Grund erneut verarbeitet werden.

Wenn Ihre Anwendungsfälle eine „Exakt-einmal"-Zustellung erfordern, können Sie das Feld für den eindeutigen Bezeichner verwenden, das mit jedem Event gesendet wird (`id`), um Events zu deduplizieren. Da die Datei unsere Kontrolle verlässt, sobald sie in Ihren Speicher-Bucket geschrieben wird, können wir die Deduplizierung von unserer Seite aus nicht garantieren.

## Zeitstempel

Alle von Currents exportierten Zeitstempel werden in der UTC-Zeitzone gesendet. Bei einigen Events, bei denen dies verfügbar ist, wird auch ein Feld für die Zeitzone mitgeliefert, das das IANA-Format (Internet Assigned Numbers Authority) der Ortszeit der Nutzer:innen zum Zeitpunkt des Events angibt.

### Latenz

Events, die über das SDK oder die API an Braze gesendet werden, können einen Zeitstempel aus der Vergangenheit enthalten. Das auffälligste Beispiel ist, wenn SDK-Daten in die Warteschlange gestellt werden, z. B. wenn keine mobile Verbindung besteht. In diesem Fall gibt der Zeitstempel des Events an, wann das Event erzeugt wurde. Das bedeutet, dass ein bestimmter Prozentsatz der Events eine hohe Latenz aufzuweisen scheint.

## Apache Avro-Format

Die Braze-Currents-Integrationen zur Datenspeicherung geben Daten im Format `.avro` aus. Wir haben uns für [Apache Avro](https://avro.apache.org/) entschieden, weil es ein flexibles Datenformat ist, das von Haus aus die Schema-Evolution unterstützt und von einer Vielzahl von Datenprodukten unterstützt wird: 

- Avro wird von nahezu allen großen Data Warehouses unterstützt.
- Falls Sie Ihre Daten in S3 belassen möchten, komprimiert Avro besser als CSV und JSON, sodass Sie weniger für die Speicherung bezahlen und möglicherweise weniger CPU zum Parsen der Daten benötigen.
- Avro erfordert Schemata, wenn Daten geschrieben oder gelesen werden. Schemata können im Laufe der Zeit weiterentwickelt werden, um das Hinzufügen von Feldern zu ermöglichen, ohne dass es zu Brüchen kommt.

Currents erstellt für jeden Event-Typ eine Datei in folgendem Format:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Sie können den Code wegen der Bildlaufleiste nicht sehen? Erfahren Sie [hier]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/), wie Sie das beheben können.
{% endalert %}

Ein Pfad für ein Push-Sende-Event kann beispielsweise so aussehen:

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

Das Pfadsegment `version` ist ein einfacher ganzzahliger Currents-Versionswert, z. B. `version=6`.

|Dateiname-Segment |Definition|
|---|---|
| `<your-bucket-prefix>` | Das Präfix, das für diese Currents-Integration festgelegt wurde. |
| `<cluster-identifier>` | Zur internen Verwendung durch Braze. Ist ein String wie „prod-01", „prod-02", „prod-03" oder „prod-04". Alle Dateien haben denselben Cluster-Bezeichner.|
| `<connection-type-identifier>` | Der Bezeichner für die Art der Verbindung. Optionen sind „S3", „AzureBlob" oder „GCS". |
| `<integration-id>` | Die eindeutige ID für diese Currents-Integration. |
| `<event-type>` | Der Typ des Events in der Datei. |
| `<date>` | Die Stunde, in der Events in unserem System zur Verarbeitung in der UTC-Zeitzone in die Warteschlange gestellt werden. Im Format JJJJ-MM-TT-HH. |
| `version=<currents_version>` | Die Currents-Version für den Pipeline-Pfad. Dieser Wert ist eine einfache Ganzzahl wie `6`. |
| `<environment>` | Zur internen Verwendung durch Braze. |
| `<partition>` | Zur internen Verwendung durch Braze. Ganzzahl. |
| `<offset>`| Zur internen Verwendung durch Braze. Ganzzahl. Beachten Sie, dass verschiedene Dateien, die innerhalb derselben Stunde gesendet werden, einen unterschiedlichen `<offset>`-Parameter haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Die Konventionen für die Dateibenennung können sich ändern. Braze empfiehlt, alle Schlüssel in Ihrem Bucket zu durchsuchen, die das Präfix &lt;your-bucket-prefix&gt; haben.
{% endalert %}

### Avro-Schreibschwelle

Unter normalen Umständen schreibt Braze alle 5 Minuten oder alle 15.000 Events Datendateien in Ihren Speicher-Bucket – je nachdem, was zuerst eintritt. Bei starker Belastung können größere Datendateien mit bis zu 100.000 Events pro Datei geschrieben werden.

{% alert important %}
Currents schreibt niemals leere Dateien.
{% endalert %}

### Änderungen am Avro-Schema

Von Zeit zu Zeit kann Braze Änderungen am Avro-Schema vornehmen, wenn Felder hinzugefügt, geändert oder entfernt werden. Für unsere Zwecke gibt es hier zwei Arten von Änderungen: wesentliche und unwesentliche. In allen Fällen wird die Currents-Pfadversion hochgesetzt, um anzuzeigen, dass das Schema aktualisiert wurde. Bei Currents-Events, die in Azure Blob Storage, Google Cloud Storage und Amazon S3 geschrieben werden, wird dies als `version=<currents_version>` im Pfad angegeben. Zum Beispiel: `<your-bucket-prefix>/.../event_type=<event-type>/date=<date>/version=6/<environment>/...`.

#### Unwesentliche Änderungen

Wenn ein Feld zum Avro-Schema hinzugefügt wird, betrachten wir dies als eine unwesentliche Änderung. Hinzugefügte Felder sind immer „optionale" Avro-Felder (z. B. mit einem Standardwert von `null`), sodass sie gemäß der [Avro-Schemaauflösungsspezifikation](http://avro.apache.org/docs/current/spec.html#schema+resolution) mit älteren Schemata „übereinstimmen". Diese Ergänzungen sollten sich nicht auf bestehende ETL-Prozesse (Extract, Transform, Load) auswirken, da das Feld einfach ignoriert wird, bis es Ihrem ETL-Prozess hinzugefügt wird. 

{% alert important %}
Um zu vermeiden, dass der Ablauf unterbrochen wird, wenn neue Felder hinzugefügt werden, empfehlen wir, dass Sie in Ihrem ETL-Setup explizit angeben, welche Felder verarbeitet werden.
{% endalert %}

Wir bemühen uns, Sie im Voraus über alle Änderungen zu informieren, können jedoch jederzeit unwesentliche Änderungen am Schema vornehmen.

#### Wesentliche Änderungen

Wenn ein Feld aus dem Avro-Schema entfernt oder geändert wird, betrachten wir dies als eine wesentliche Änderung. Wesentliche Änderungen können Anpassungen an bestehenden ETL-Prozessen erfordern, da Felder, die zuvor verwendet wurden, möglicherweise nicht mehr wie erwartet aufgezeichnet werden.

Alle wesentlichen Änderungen am Schema werden im Voraus kommuniziert.