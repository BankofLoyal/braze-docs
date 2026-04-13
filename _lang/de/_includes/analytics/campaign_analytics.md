## Analytik anzeigen

Sobald Sie Ihre Kampagne gestartet haben, können Sie zur Detailseite dieser Kampagne zurückkehren, um die wichtigsten Kennzahlen einzusehen. Navigieren Sie zur Seite **Kampagnen** und wählen Sie Ihre Kampagne aus, um die Detailseite zu öffnen.{% if include.channel != "banner" %} Für {% if include.channel == "Content Card" %}Content-Cards {% elsif include.channel == "banner" %}Banner {% elsif include.channel == "email" %}E-Mails {% elsif include.channel == "in-app message" %}In-App-Nachrichten {% elsif include.channel == "KakaoTalk" %}KakaoTalk-Nachrichten {% elsif include.channel == "push" %}Push-Nachrichten {% elsif include.channel == "SMS" %}SMS-Nachrichten {% elsif include.channel == "whatsapp" %}WhatsApp-Nachrichten {% elsif include.channel == "webhook" %}Webhooks {% endif %}, die in Canvas gesendet werden, lesen Sie den Abschnitt [Canvas-Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).{% endif %}

{% alert tip %}
Suchen Sie nach Definitionen für die in Ihrem Bericht aufgeführten Begriffe und Metriken? Sehen Sie sich unser
  {% if include.channel == "email" %}[E-Mail-Analytics-Glossar]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/) an.
  {% elsif include.channel == "banner" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) an und filtern Sie nach Bannern.
  {% elsif include.channel == "Content Card" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) an und filtern Sie nach Content-Cards.
  {% elsif include.channel == "in-app message" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) an und filtern Sie nach In-App-Nachricht.
  {% elsif include.channel == "push" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) an und filtern Sie nach Push.
  {% elsif include.channel == "SMS" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) an und filtern Sie nach SMS/MMS und RCS.
  {% elsif include.channel == "whatsapp" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) an und filtern Sie nach WhatsApp.
  {% elsif include.channel == "webhook" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) an und filtern Sie nach Webhook.{% endif %}
{% endalert %}

Auf dem Tab **Kampagnen-Analytics** können Sie Ihre Berichte in einer Reihe von Panels einsehen. Möglicherweise sehen Sie mehr oder weniger als die in den folgenden Abschnitten aufgelisteten, aber jedes hat seinen eigenen nützlichen Zweck.

### Zeitraum

Standardmäßig zeigt **Kampagnen-Analytics** die letzten 90 Tage ab dem aktuellen Zeitpunkt an. Das bedeutet: Wenn die Kampagne vor mehr als 90 Tagen gestartet wurde, werden die Analytics für den angegebenen Zeitraum als „0" angezeigt. Um alle Analytics für ältere Kampagnen anzuzeigen, passen Sie den Berichtszeitraum an.

### Kampagnendetails

Das Panel **Kampagnendetails** zeigt einen Überblick über die gesamte Performance Ihrer
  {% if include.channel == "banner" %}Banner.
  {% elsif include.channel == "Content Card" %}Content-Card.
  {% elsif include.channel == "email" %}E-Mail.
  {% elsif include.channel == "in-app message" %}In-App-Nachricht.
  {% elsif include.channel == "KakaoTalk" %}KakaoTalk-Nachricht.
  {% elsif include.channel == "push" %}Push-Nachricht.
  {% elsif include.channel == "SMS" %}SMS, MMS und RCS.
  {% elsif include.channel == "whatsapp" %}WhatsApp-Nachrichten.
  {% elsif include.channel == "webhook" %}Webhook.
  {% endif %}

In diesem Panel sehen Sie Gesamtmetriken wie die Anzahl der gesendeten Nachrichten, die Anzahl der Empfänger:innen, die primäre Konversionsrate und den Gesamtumsatz, der mit dieser Nachricht erzielt wurde. Auf dieser Seite können Sie auch die Einstellungen für Zustellung, Zielgruppe und Konversion überprüfen.

{% if include.channel == "whatsapp" %}
{% alert note %}
Der WhatsApp-Kanal enthält die Leserate. Diese Metrik wird nur für Nutzer:innen mit aktivierten Lesebestätigungen geliefert, was variieren kann.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken, die zur Bestimmung der Kampagnen-Performance verwendet werden.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken, die zur Bestimmung der Kampagnen-Performance verwendet werden.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken, die zur Bestimmung der Kampagnen-Performance verwendet werden.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken, die zur Bestimmung der Kampagnen-Performance verwendet werden.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken, die zur Bestimmung der Kampagnen-Performance verwendet werden.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken, die zur Bestimmung der Kampagnen-Performance verwendet werden.]({% image_buster /assets/img/campaign_details_iam.png %})

In Canvas sehen Sie die Performance von In-App-Nachrichten, die dem von Ihnen erstellten Canvas zugeordnet sind. Sie können das Bedienfeld oben auf der Seite verwenden, um andere Nachrichtentypen (Kanäle) auszublenden und nur die In-App-Nachrichten in Ihrem Canvas anzuzeigen.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![Der Abschnitt „Kampagnendetails".]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken, die zur Bestimmung der Kampagnen-Performance verwendet werden.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Kontrollgruppen {#cc-control-group}

Um die Wirkung einer einzelnen Content-Card zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Kampagnendetails** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% elsif include.channel == "SMS" %}

#### Kontrollgruppen {#sms-control-group}

Um die Wirkung einer einzelnen SMS-, MMS- oder RCS-Nachricht zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Kampagnendetails** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% elsif include.channel == "whatsapp" %}

#### Kontrollgruppen {#whatsapp-control-group}

Um die Wirkung einer einzelnen WhatsApp-Nachricht zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Kampagnendetails** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% elsif include.channel == "webhook" %}

#### Kontrollgruppen {#webhook-control-group}

Um die Wirkung einer einzelnen Webhook-Nachricht zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Kampagnendetails** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% endif %}

#### Änderungen seit letztem Aufruf

Die Anzahl der Aktualisierungen der Kampagne durch andere Mitglieder Ihres Teams wird durch die Metrik *Änderungen seit letztem Aufruf* auf der Kampagnenübersichtsseite erfasst. Wählen Sie **Änderungen seit letztem Aufruf**, um ein Changelog der Aktualisierungen an Name, Zeitplan, Tags, Nachricht, Zielgruppe, Genehmigungsstatus oder Teamzugriffskonfiguration der Kampagne anzuzeigen. Bei jeder Aktualisierung können Sie sehen, wer die Änderung vorgenommen hat und wann. Sie können dieses Changelog verwenden, um Änderungen an Ihrer Kampagne nachzuvollziehen.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Content-Card-Performance

Das Panel **Content-Card-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![Content-Card-Nachrichten-Performance-Analytics]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### E-Mail-Performance

Das Panel **E-Mail-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![E-Mail-Nachrichten-Performance-Analytics]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### In-App-Nachrichten-Performance

Das Panel **In-App-Nachrichten-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![In-App-Nachrichten-Performance-Analytics]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Push-Performance

Das Panel **Push-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![Push-Nachrichten-Performance-Analytics]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCS-Performance

Das Panel **SMS/MMS/RCS-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![SMS/MMS/RCS-Performance-Panel mit einer Tabelle mit Metriken für eine Kontrollgruppe, Variante 1 und Variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Banner-Performance

Das Panel **Banner-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Diese Metriken variieren je nach Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen.

![SMS/MMS-Performance-Panel mit einer Tabelle mit Metriken für eine Kontrollgruppe, Variante 1 und Variante 2.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### KakaoTalk-Performance

Das Panel **KakaoTalk-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

{% elsif include.channel == "webhook" %}
### Webhook-Performance

Das Panel **Webhook-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![Webhook-Performance-Panel mit einer Tabelle mit Metriken für eine Kontrollgruppe und Variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp-Performance

Das Panel **WhatsApp-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![WhatsApp-Performance-Panel mit einer Tabelle mit Metriken für Variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Wenn Sie Ihre Ansicht vereinfachen möchten, klicken Sie auf <i class="fas fa-plus"></i> **Spalten hinzufügen/entfernen** und deaktivieren Sie die gewünschten Metriken. Standardmäßig werden alle Metriken angezeigt.

{% if include.channel == "email" %}

#### Heatmaps

Mit Heatmaps können Sie sehen, wie erfolgreich verschiedene Links in einer einzelnen E-Mail-Kampagne sind. Gehen Sie im Abschnitt **Nachrichtenanalyse** zum Panel **E-Mail-Performance**. Wählen Sie **Vorschau & Heatmap**, um eine Vorschau Ihrer E-Mail-Kampagne und der Heatmap anzuzeigen. Alternativ können Sie den Hyperlink im Variantennamen auswählen, um die Heatmap aufzurufen.

In dieser Ansicht können Sie mit dem Schalter **Heatmap anzeigen** eine visuelle Darstellung Ihrer E-Mail aufrufen, die die Gesamthäufigkeit und den Ort der Klicks innerhalb der Laufzeit der Kampagne anzeigt. Im Panel **Link-Tabelle nach Gesamtklicks** können Sie alle Links in Ihrer E-Mail-Kampagne anzeigen und nach Gesamtklicks sortieren. Dies kann zusätzliche Insights darüber liefern, wohin Ihre Nutzer:innen navigieren. Um eine Kopie der Heatmap als Referenz zu speichern, klicken Sie auf den Download-Button.

![Beispiel für die Vorschau- und Heatmap-Seite mit einer E-Mail-Kampagne und einem Panel mit Beispielen für Link-Aliase und deren Gesamtklicks.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Bilder

Wir empfehlen, CORS für Ihre Bild-URLs zu aktivieren, damit Bilder in Heatmap-Vorschauen und -Exporten nicht fehlen.

Wenn Bilder in einem Export fehlen, arbeiten Sie mit Ihren Entwickler:innen zusammen, damit Bild-Assets den Cross-Origin-Zugriff erlauben: Der Server sollte den Header `Access-Control-Allow-Origin` mit entweder `*` oder Ihrer Braze-Dashboard-Domain zurückgeben.

{% endif %}

{% if include.channel == "Content Card" %}

#### Content-Card-Metriken

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller Content-Cards-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/). Filtern Sie dort nach Content-Cards.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Gesendete Nachrichten</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                Die Berechnung hängt davon ab, was Sie für die
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Kartenerstellung</a> ausgewählt haben:<br><br>
                <ul>
                    <li><b>Beim Start oder beim Einstieg in den Schritt:</b> Die Anzahl der erstellten und verfügbaren Karten. Dabei wird nicht berücksichtigt, ob die Nutzer:innen die Karte angesehen haben.</li>
                    <li><b>Bei der ersten Impression:</b> Die Anzahl der Karten, die den Nutzer:innen angezeigt wurden.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Impressionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Dieser Wert kann für dieselbe Nutzer:in mehrfach gezählt werden.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Eindeutige Impressionen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Dieser Zähler</span> wird nicht erhöht, wenn eine Nutzer:in eine Content-Card zum zweiten Mal aufruft.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">Eindeutige Empfänger:innen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> Da eine Nutzer:in jeden Tag als eindeutige Empfänger:in gezählt werden kann, sollten Sie davon ausgehen, dass dieser Wert höher ist als die <i>eindeutigen Impressionen</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Eindeutige Klicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dies umfasst auch Klicks auf die von Braze bereitgestellten Abmeldelinks.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Eindeutige Ausblendungen</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
Bei der Protokollierung von Impressionen gibt es einige Unterschiede zwischen Web, Android und iOS. Generell protokolliert Braze eine Impression, wenn eine Karte gesehen wird – also nachdem eine Nutzer:in zur entsprechenden Content-Card in ihrem Feed gescrollt hat.
{% endalert %}

#### Eindeutige Empfänger:innen versus eindeutige Impressionen

Es gibt mehrere Metriken, die die Sichtbarkeit Ihrer Nachricht erfassen, darunter _eindeutige Empfänger:innen_ und _eindeutige Impressionen_. Anhand einiger Beispielszenarien lassen sich diese Metriken besser verstehen.

Angenommen, Sie sehen sich heute eine Content-Card an, erhalten morgen eine neue Karte aus derselben Kampagne und übermorgen wieder eine – dann werden Sie dreimal als _eindeutige Empfänger:in_ gezählt. Sie werden jedoch nur für eine _eindeutige Impression_ gezählt. Außerdem werden Sie in der Anzahl der _gesendeten Nachrichten_ berücksichtigt, da die Karte auf Ihrem Gerät verfügbar war.

Ein weiteres Beispiel: Angenommen, Sie sehen fünf _eindeutige Impressionen_ für eine Content-Card-Kampagne mit 150.000 _gesendeten Nachrichten_. Das bedeutet, dass die Karte (im Backend) einer Zielgruppe von 150.000 Nutzer:innen zur Verfügung gestellt wurde, aber nur die Geräte von fünf Nutzer:innen alle folgenden Schritte nach dem Senden ausgeführt haben:

1. Eine Sitzung gestartet oder die App hat explizit eine Content-Cards-Synchronisierung angefordert (oder beides)
2. Zur Content-Cards-Ansicht navigiert
3. Das SDK hat eine Impression aufgezeichnet und an den Server gesendet

_Gesendete Nachrichten_ bezieht sich auf Content-Cards, die zum Ansehen verfügbar sind, während _eindeutige Empfänger:innen_ die Content-Cards bezeichnet, die tatsächlich angesehen wurden.

{% elsif include.channel == "banner" %}

### Banner-Metriken

Dies sind die wichtigsten Metriken, die Sie bei der Überprüfung der Performance Ihrer Banner-Kampagne im Blick behalten sollten. Klicks und Impressionen für Banner werden automatisch über das SDK getrackt.

Die vollständigen Definitionen aller Banner-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/). Filtern Sie dort nach Bannern.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impressionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Bei Bannern werden Impressionen einmal pro Nutzersitzung protokolliert. Wenn dasselbe Banner innerhalb derselben Sitzung mehrfach angezeigt wird, wird nur eine Impression protokolliert.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Eindeutige Impressionen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Jede Nutzer:in wird nur einmal gezählt.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Klicks gesamt</a></td>
            <td class="no-split"><i>Klicks gesamt</i> ist die Gesamtzahl (und der Prozentsatz) der Nutzer:innen, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob dieselbe Nutzer:in mehrmals geklickt hat.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Eindeutige Klicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} Jede Nutzer:in wird nur einmal gezählt.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Primäre Konversionen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Eindeutige Empfänger:innen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> Da eine Betrachterin oder ein Betrachter jeden Tag als eindeutige Empfänger:in gezählt werden kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>eindeutigen Impressionen</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Umsatz</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Konfidenz</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Berechnungsbeispiele für Banner-Metriken

Es gibt mehrere Metriken, die die Sichtbarkeit Ihrer Nachricht erfassen, darunter _eindeutige Empfänger:innen_ und _eindeutige Impressionen_. Anhand einiger Beispielszenarien lassen sich diese Metriken besser verstehen.

Angenommen, Sie sehen sich heute ein Banner an, morgen dasselbe Banner und übermorgen erneut – dann werden Sie dreimal als _eindeutige Empfänger:in_ gezählt. Sie werden jedoch nur für eine _eindeutige Impression_ gezählt.

Nehmen wir als weiteres Beispiel an, Sie sehen fünf _eindeutige Impressionen_ in einer Banner-Kampagne. Das bedeutet, dass nur die Geräte von fünf Nutzer:innen alle folgenden Schritte ausgeführt haben:

1. Eine Sitzung gestartet oder die App hat explizit eine Banner-Synchronisierung angefordert (oder beides)
2. Zur Banner-Ansicht navigiert
3. Das SDK hat eine Impression aufgezeichnet und an den Server gesendet

_Eindeutige Empfänger:innen_ bezieht sich auf die Banner, die tatsächlich angesehen wurden.

{% elsif include.channel == "email" %}

#### E-Mail-Metriken

Im Folgenden finden Sie einige wichtige E-Mail-spezifische Metriken, die in anderen Kanälen nicht verfügbar sind. Die vollständigen Definitionen aller in Braze verwendeten E-Mail-Metriken finden Sie in unserem [E-Mail-Analytics-Glossar]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Eindeutige Klicks</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dieser Wert wird über einen Zeitraum von sieben Tagen für E-Mails getrackt und anhand der <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> gemessen. Dazu gehören auch Klicks auf die von Braze bereitgestellten Abmeldelinks. Dieser Wert sollte zwischen 5–10 % liegen. Alles über 10 % ist außergewöhnlich!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Eindeutige Öffnungen</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Bei E-Mails erfolgt das Tracking über einen Zeitraum von 7 Tagen. Dieser Wert sollte zwischen 30–40 % liegen. Alles über 40 % ist außergewöhnlich!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Effektive Klickrate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Spam-Rate</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} Wenn diese Metrik größer als 0,08 ist, könnte dies ein Hinweis darauf sein, dass entweder Ihr Nachrichtentext zu verkaufsorientiert ist oder Sie Ihre Methoden zur Erfassung von E-Mail-Adressen überdenken sollten (um sicherzustellen, dass Sie nur Personen anschreiben, die an Ihrer Korrespondenz interessiert sind).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Abmeldungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Sonstige Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Geschätzte reale Öffnungen</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Weitere Informationen finden Sie im folgenden Abschnitt.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Automatische Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Aufschub</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Zustellungen und Bounces

Das Dashboard hebt _Hard Bounces_ hervor. Einige _Bounces_ können Soft Bounces sein und stimmen allein nicht mit dieser Zahl überein. Sie können Soft Bounces mit dieser Formel annähern:

_Sendungen − (Zustellungen + Hard Bounces) ≈ Soft Bounces_

_Zustellungen_ können in den ersten 72 Stunden steigen, wenn Wiederholungsversuche erfolgreich sind, während _Sendungen_ und Hard Bounces bei einem einmaligen Versand nach Abschluss des Versands feststehen.

##### Klicks ohne Öffnungs-Event

Ein Klick kann ohne eine Öffnung protokolliert werden, wenn das Öffnungs-Pixel nie geladen wird. Zum Beispiel wird die Nachricht in Gmail abgeschnitten, oder die Nutzer:in hat Bilder deaktiviert (das Öffnungs-Pixel befindet sich normalerweise in der Fußzeile). Einige Clients leiten Bilder über Proxys weiter (wie Apple Mail), sodass die Öffnung protokolliert werden kann, wenn der Server das Pixel zum ersten Mal abruft – nicht wenn die Nutzer:in die E-Mail liest. Unternehmensdomains blockieren Bilder oft standardmäßig.

Ein Klick und eine Öffnung können auch an verschiedenen Tagen stattfinden: Eine Nutzer:in könnte am 16. Mai mit deaktivierten Bildern klicken (keine Öffnung) und dann am 17. Mai im Webmail öffnen (Öffnung wird dann protokolliert).

##### Aufschübe

Ein Aufschub (Deferral) bedeutet, dass eine E-Mail nicht sofort zugestellt werden konnte. Braze versucht jedoch, die E-Mail bis zu 72 Stunden nach diesem vorübergehenden Zustellungsfehler erneut zuzustellen, um die Chancen auf eine erfolgreiche Zustellung zu maximieren, bevor die Versuche für diese spezielle Kampagne eingestellt werden. Typische Gründe für Aufschübe sind reputationsbasiertes Rate-Limiting des Posteingangs-Anbieters für das E-Mail-Volumen, vorübergehende Verbindungsprobleme oder DNS-Fehler.

_Aufschübe_ unterscheiden sich von _Soft Bounces_. Wenn während dieses Wiederholungszeitraums keine E-Mail erfolgreich zugestellt wurde, sendet Braze ein Soft-Bounce-Event pro versuchtem Kampagnenversand. Vor dem 25. Februar 2025 wurden diese Wiederholungsversuche als mehrere Soft Bounces für einen Kampagnenversand gezählt.

Beachten Sie, dass _Aufschübe_ derzeit nur über Currents oder Braze-Snowflake-Features (wie Query Builder, SQL-Segmente, Snowflake Data Sharing) verfügbar sind. Wenn Sie dies in Kampagnen- oder Canvas-Analytics einbeziehen möchten, [senden Sie uns bitte Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Geschätzte reale Öffnungsrate {#estimated-real-open-rate}

Diese Statistik verwendet ein proprietäres, von Braze entwickeltes Analysemodell, um eine Schätzung der individuellen Öffnungsrate der Kampagne zu rekonstruieren – so, als ob es keine automatischen Öffnungen gäbe. Obwohl wir bei einigen Öffnungs-Events von E-Mail-Absendern die Kennzeichnung *Automatische Öffnungen* erhalten (siehe oben), können diese Kennzeichnungen häufig tatsächliche Öffnungen fälschlicherweise als automatische Öffnungen markieren. Mit anderen Worten: Die *sonstigen Öffnungen* sind wahrscheinlich eine Unterschätzung der tatsächlichen Öffnungen (durch echte Nutzer:innen). Stattdessen verwendet Braze die Klickdaten der einzelnen Kampagnen, um auf die Rate zu schließen, mit der Menschen die Nachricht tatsächlich geöffnet haben. Dies kompensiert verschiedene Mechanismen zum automatischen Öffnen, einschließlich Apples MPP.

Die _geschätzte reale Öffnungsrate_ wird 36 Stunden nach Beginn des E-Mail-Versands berechnet und danach alle 24 Stunden neu berechnet. Bei wiederkehrenden Kampagnen wird die Schätzung 36 Stunden nach einem weiteren Versand neu berechnet.

Da diese Metrik kontinuierlich neu berechnet wird, kann sich der Wert der _geschätzten realen Öffnungsrate_ im Laufe der Zeit ändern, wenn neue Engagement-Signale (wie Öffnungen und Klicks) empfangen und in das Modell integriert werden. In der Praxis kann die _geschätzte reale Öffnungsrate_ täglich aktualisiert werden, solange eine Kampagne aktiv ist.

Normalerweise sind etwa 10.000 zugestellte E-Mails erforderlich, damit die Statistik erfolgreich berechnet werden kann, wobei diese Zahl je nach Klickrate variieren kann. Wenn die Statistik nicht berechnet werden kann, wird in der Spalte „--" angezeigt.

###### Einschränkungen

Die geschätzte reale Öffnungsrate ist nur in Kampagnen verfügbar und wird nicht in Currents-Events gemeldet. Diese Metrik wird nur für aktive Kampagnen, die vor dem 14. November 2023 gestartet wurden, rückwirkend berechnet.

##### Umgang mit steigenden Klickraten

Öffnungsraten können eine aufschlussreiche Metrik für das Tracking Ihrer E-Mail-Kampagnen sein. Allerdings sind diese Öffnungsraten nicht unbedingt ein genauer Indikator für das menschliche Engagement bei E-Mail-Kampagnen. Ein Öffnungs-Event tritt definitionsgemäß ein, wenn eine Nutzer:in eine E-Mail öffnet, was bedeutet, dass ein transparentes Tracking-Pixel für die Öffnung erfolgreich heruntergeladen wurde.

Darüber hinaus kann die Verwendung von Sicherheitsscannern die Öffnungsraten in die Höhe treiben. Einige dieser Tools schützen ihre Nutzer:innen, indem sie eingehende E-Mails auf bösartige Inhalte überprüfen und auf Links klicken, um deren Legitimität zu verifizieren. Diese Klicks werden oft als „Bot-Klicks" oder „nicht-menschliche Interaktion" (NHI) bezeichnet.

Nachdem eine E-Mail unsere Server verlassen hat, haben wir nur begrenzte Einblicke in den weiteren Verlauf. Hier sind einige Empfehlungen zum Umgang mit NHI, die sich auf Ihre Ergebnisse auswirken können:

1. Seien Sie sich bewusst, dass dies bei jedem Absender und fast jeder Empfänger:in passieren kann. Klicks sind ebenso wie Öffnungen kein vollständig zuverlässiger Indikator für die menschliche Interaktion mit Ihren Nachrichten – NHI lässt sich nicht verhindern.
2. Ein höheres positives Engagement korreliert in der Regel mit niedrigerer NHI. Daher ist es wichtig, die [Best Practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) für E-Mail-Messaging zu befolgen. Dazu gehört, die ausdrückliche Erlaubnis Ihrer Nutzer:innen für den E-Mail-Versand einzuholen und nicht engagierte Abonnent:innen regelmäßig per Sunsetting zu entfernen.
3. Verwenden Sie wenn möglich HTTPS-Links in Ihren E-Mails. NHI ist bei Absendern, die sichere Links verwenden, weniger verbreitet.
4. Wenn Sie einen Ein-Klick-Abmeldeprozess verwenden, sollten Sie die Einrichtung eines [Präferenzzentrums]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview) in Betracht ziehen, das die Nutzer:innen zu einer Seite weiterleitet, auf der sie ihre Benachrichtigungseinstellungen bearbeiten und verwalten können. Dies kann hilfreich sein, da NHI Nutzer:innen versehentlich abmelden kann.
5. Ziehen Sie [andere Metriken]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) in Betracht, um den Erfolg Ihres E-Mail-Marketings zu messen, z. B. Konversionen, App-Sitzungen oder Website-Besuche.
6. Fügen Sie einen versteckten Link in Ihre E-Mail-Kampagnen ein. Dieser Link sollte für Menschen nicht sichtbar sein, z. B. weißer Text auf weißem Hintergrund oder ein Interpunktionszeichen. Bots neigen dazu, alle Links anzuklicken. Daher können Sie davon ausgehen, dass Nutzer:innen, die Klick-Events auf dem unsichtbaren Link generieren, tatsächlich das Ergebnis von NHI sind – die Öffnung oder der Klick deutet also nicht unbedingt auf positives Engagement hin.

{% elsif include.channel == "in-app message" %}

#### Metriken für In-App-Nachrichten

Im Folgenden finden Sie einige wichtige Metriken für In-App-Nachrichten, die Sie in Ihren Analytics sehen können. Die vollständigen Definitionen aller in Braze verwendeten Metriken für In-App-Nachrichten finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

{% alert note %}
Die Berichterstattung für _Button-1-Klicks_ und _Button-2-Klicks_ funktioniert nur, wenn Sie in der In-App-Nachricht den **Bezeichner für Reporting** auf „0" bzw. „1" setzen.

![Das Feld „Bezeichner für Reporting" mit dem Wert „0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Klicks auf Text</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Klicks auf Button 1</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Klicks auf Button 2</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Eindeutige Impressionen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impressionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Konversionen (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Konversionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Konversionsrate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Nachricht schließen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "KakaoTalk" %}

### KakaoTalk-Metriken

Im Folgenden finden Sie einige wichtige KakaoTalk-Metriken, die Sie in Ihren Analytics sehen können. Weitere Details finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/).

| Begriff | Definition |
| --- | --- |
| Zielgruppe | _Zielgruppe_ ist der Prozentsatz der Nutzer:innen, die eine bestimmte Nachricht erhalten haben. <br><br>_(Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)_ |
| Eindeutige Empfänger:innen | _Eindeutige Empfänger:innen_ ist die Anzahl der eindeutigen täglichen Empfänger:innen, also Nutzer:innen, die an einem Tag eine neue Nachricht erhalten haben. Damit dieser Zähler für eine Nutzer:in mehr als einmal erhöht wird, muss die Nutzer:in an einem anderen Tag eine neue Nachricht erhalten. Diese Zahl basiert auf der `user_id`. Weitere Details finden Sie unter [Eindeutige Empfänger:innen im Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/#unique-recipients). |
| Sendungen | Die Gesamtzahl der in einer Kampagne gesendeten Nachrichten. Dies bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde. |
| Klicks gesamt | Die Gesamtzahl der Male, die die gesendeten KakaoTalk-Nachrichten von Nutzer:innen angeklickt wurden. |
| Fehler | _Fehler_ ist die Anzahl der vom KakaoTalk-Anbieter zurückgegebenen Fehler (wird während des Sendevorgangs erhöht). |
| Umsatz | _Umsatz_ ist der Umsatz in Dollar von Kampagnenempfänger:innen innerhalb des festgelegten primären Konversionsfensters. |
| Primäre Konversionen | _Primäre Konversionen_ ist die Anzahl der Male, die ein definiertes Event nach der Interaktion mit oder dem Anzeigen einer empfangenen Nachricht aus einer Braze-Kampagne aufgetreten ist. Dieses definierte Event wird von Ihnen beim Erstellen der Kampagne festgelegt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% elsif include.channel == "push" %}

#### Push-Metriken

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller Push-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/). Filtern Sie dort nach Push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} Siehe <a href="#bounced-push">Zurückgewiesene Push-Benachrichtigungen</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direkte Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> Die Zustellung von Benachrichtigungen erfolgt nach dem „Best-Effort"-Prinzip durch die Apple Push Notification Services (APNs). Sie ist nicht dazu gedacht, Daten an Ihre App zu liefern, sondern nur die Nutzer:in darüber zu informieren, dass neue Daten verfügbar sind. Der wichtige Unterschied ist, dass wir anzeigen, wie viele Nachrichten wir erfolgreich an APNs zugestellt haben – nicht unbedingt, wie viele APNs erfolgreich an Geräte zugestellt hat.

##### Tracking von Abmeldungen

Push-Abmeldungen werden nicht als Metrik in die Kampagnen-Analytics einbezogen und hängen von Updates des Push-Status einer Nutzer:in durch Anbieter wie Apple oder Google ab. Diese Updates können unregelmäßig und unvorhersehbar sein. Daher werden Push-Abmeldungen nicht als Metrik in den Push-Kampagnen-Analytics berücksichtigt.

Dennoch kann das manuelle Tracking von Push-Abmeldungen wertvolle Insights über die Reaktionen der Nutzer:innen auf Ihre Benachrichtigungshäufigkeit und die Relevanz der Inhalte liefern. Es gibt zwei Möglichkeiten für das Tracking von Push-Abmeldungen: Segmentfilter oder angepasste Filter.

{% tabs local %}
{% tab Segment filters %}

Sie können ein Segment erstellen, um Nutzer:innen zu identifizieren, die keine Push-Benachrichtigungen aktiviert haben – also nicht abonniert oder per Opt-in registriert sind und kein [Vordergrund-Push-Token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) besitzen. Um beispielsweise die Anzahl der Abmeldungen in Ihrer App anzuzeigen, verwenden Sie eine „ODER"-Kombination der folgenden Segmente:

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![Der Abschnitt „Segment Builder" mit dem Filter „Hintergrund- oder Vordergrund-Push für App aktiviert" für eine App ist deaktiviert, und der Filter „Hat deinstalliert" ist ausgewählt.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Bitte beachten Sie, dass die Segmentierungsfilter nur Näherungswerte liefern und nicht konkret mit einem Datum und einer Kampagne verknüpft werden können.

{% endtab %}
{% tab Custom filters %}

{% alert important %}
Das Protokollieren eines angepassten Events für Abo-Änderungen verbraucht [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Verwenden Sie alternativ Segmentfilter, um Nutzer:innen zu identifizieren und zu targetieren, die nicht Push-aktiviert sind.
{% endalert %}

Als weitere Möglichkeit empfehlen wir, ein angepasstes Event für Push-Abmeldungen zu erstellen, das darauf basiert, ob der Push-Aktivierungsstatus einer Nutzer:in `true` oder `false` ist, um diese Metrik zu verfolgen.

{% endtab %}
{% endtabs %}

##### Öffnungen verstehen

Auch wenn _direkte Öffnungen_ und _beeinflusste Öffnungen_ das Wort „Öffnungen" enthalten, handelt es sich um unterschiedliche Metriken. _Direkte Öffnungen_ bezieht sich auf das direkte Öffnen einer Push-Benachrichtigung, wie in der Tabelle oben beschrieben. _Beeinflusste Öffnungen_ bezieht sich auf das Öffnen einer App, ohne dass eine Push-Benachrichtigung innerhalb eines bestimmten Zeitraums nach Erhalt geöffnet wurde. _Beeinflusste Öffnungen_ bezieht sich also auf App-Öffnungen, nicht auf das Öffnen von Push-Benachrichtigungen.

##### Warum Push-Sendungen die Zahl der eindeutigen Empfänger:innen übersteigen können

Die Anzahl der _Sendungen_ kann die Anzahl der _eindeutigen Empfänger:innen_ aus folgenden Gründen übersteigen:

- **Wiederzulassung ist aktiviert:** Wenn die Wiederzulassung in Ihren Kampagnen- oder Canvas-Einstellungen aktiviert ist, können Nutzer:innen, die das Segment und die Zustellungskriterien erfüllen, dieselbe Push-Benachrichtigung mehrmals erhalten. Dies führt zu einer höheren Gesamtzahl an Sendungen.
- **Nutzer:innen haben mehrere Geräte:** Wenn die Wiederzulassung nicht aktiviert ist, kann der Unterschied dadurch erklärt werden, dass Nutzer:innen mehrere Geräte mit ihrem Profil verknüpft haben. Eine Nutzer:in könnte zum Beispiel sowohl ein Smartphone als auch ein Tablet besitzen, und die Push-Benachrichtigung wird an alle registrierten Geräte gesendet. Jede Zustellung zählt als eine Sendung, aber es wird nur eine eindeutige Empfänger:in erfasst.
- **Nutzer:innen sind mehreren Apps zugewiesen:** Wenn Nutzer:innen mit mehr als einer App verbunden sind (z. B. beim Testen einer neuen App), erhalten sie möglicherweise dieselbe Push-Benachrichtigung in jeder App. Dies trägt zu einer höheren Anzahl von Sendungen bei.

##### Warum Bounces auftreten {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

Bounces treten bei Apple Push Notification Services (APNs) auf, wenn eine Push-Benachrichtigung versucht, an ein Gerät zugestellt zu werden, auf dem die gewünschte App nicht installiert ist. APNs hat außerdem das Recht, Token für Geräte beliebig zu ändern. Wenn Sie versuchen, an das Gerät einer Nutzer:in zu senden, deren Push-Token sich zwischen der Registrierung (z. B. zu Beginn jeder Sitzung, wenn wir eine Nutzer:in für ein Push-Token registrieren) und dem Zeitpunkt des Sendens geändert hat, führt dies zu einem Bounce.

Wenn eine Nutzer:in Push in den Geräteeinstellungen deaktiviert, erkennt das SDK beim nächsten Öffnen der App, dass Push deaktiviert wurde, und benachrichtigt Braze. An diesem Punkt aktualisieren wir den Push-Aktivierungsstatus auf „deaktiviert". Wenn eine deaktivierte Nutzer:in eine Push-Kampagne erhält, bevor sie eine neue Sitzung hat, wird die Kampagne erfolgreich gesendet und erscheint als zugestellt. Der Push wird für diese Nutzer:in nicht bouncen. Bei einer nachfolgenden Sitzung weiß Braze bereits, ob ein Vordergrund-Token vorhanden ist, sodass keine Benachrichtigung gesendet wird.

Push-Benachrichtigungen, die vor der Zustellung ablaufen, gelten nicht als fehlgeschlagen und werden nicht als Bounce registriert.

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging (FCM) Bounces können in drei Fällen auftreten:

| Szenario | Beschreibung |
| -- | -- |
| Deinstallierte Anwendungen | Wenn eine Nachricht versucht, an ein Gerät zugestellt zu werden, und die vorgesehene App auf diesem Gerät deinstalliert ist, wird die Nachricht verworfen und die Registrierungs-ID des Geräts wird ungültig. Alle weiteren Versuche, das Gerät zu benachrichtigen, geben den Fehler NotRegistered zurück. |
| Gesicherte Anwendung | Wenn eine Anwendung gesichert wird, kann ihre Registrierungs-ID ungültig werden, bevor die Anwendung wiederhergestellt wird. In diesem Fall speichert FCM die Registrierungs-ID der Anwendung nicht mehr und die Anwendung empfängt keine Nachrichten mehr. Registrierungs-IDs sollten daher **nicht** gespeichert werden, wenn eine Anwendung gesichert wird. |
| Aktualisierte Anwendung | Wenn eine Anwendung aktualisiert wird, funktioniert die Registrierungs-ID der vorherigen Version möglicherweise nicht mehr. Daher sollte eine aktualisierte Anwendung ihre bestehende Registrierungs-ID ersetzen. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS-, MMS- und RCS-Metriken

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller SMS-, MMS- und RCS-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/). Filtern Sie dort nach SMS/MMS und RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Gesendet</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Zustellfehler</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Bestätigte Zustellung</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Zurückweisungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Opt-out</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Hilfe</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Klicks gesamt</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Webhook-Metriken

Hier sind einige wichtige Webhook-Metriken, die Sie in Ihren Analytics sehen können. Die vollständigen Definitionen aller in Braze verwendeten Webhook-Metriken finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Eindeutige Empfänger:innen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sendungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Fehler</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp-Metriken

Hier sind einige wichtige WhatsApp-Metriken, die Sie in Ihren Analytics sehen können. Die vollständigen Definitionen aller in Braze verwendeten WhatsApp-Metriken finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sendungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Zustellungen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Gelesen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Fehlschläge</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Metriken zu Endnutzer-Sperrung und -Meldung

Über das [Dashboard des WhatsApp Managers](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx) können Sie auf weitere Metriken zugreifen. Allerdings ist eine [Bestätigung Ihres Zugriffs](https://www.facebook.com/business/help/218116047387456) erforderlich, um alle verfügbaren Insights einzusehen.

{% endif %}

### Historische Performance

Im Panel **Historische Performance** können Sie die Metriken aus dem Panel **Nachrichtenleistung** als Diagramm im Zeitverlauf betrachten. Verwenden Sie die Filter am oberen Rand des Panels, um die angezeigten Statistiken und Kanäle zu ändern. Der Zeitraum dieses Diagramms entspricht immer dem oben auf der Seite angegebenen Zeitraum.

Um eine tagesgenaue Aufschlüsselung zu erhalten, klicken Sie auf das Hamburger-Menü <i class="fas fa-bars"></i> und wählen Sie **CSV herunterladen**, um einen CSV-Export des Berichts zu erhalten.

![Ein Diagramm des Panels „Historische Performance" mit Beispielstatistiken für eine E-Mail von Februar 2021 bis Mai 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Wenn Sie sich dafür entscheiden, nur an Nutzer:innen zu senden, die die neueste Braze-Version der In-App-Nachrichten (Generation 3) sehen können, wird Ihre **Zielgruppe** nicht entsprechend Ihrer Auswahl angepasst.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Schlüsselwort-Antworten

Das Panel **Schlüsselwort-Antworten** zeigt Ihnen eine Zeitleiste der eingehenden Schlüsselwörter, mit denen Nutzer:innen nach Erhalt Ihrer Nachricht geantwortet haben.

![Das Panel „Kampagnenebene – SMS/MMS/RCS-Schlüsselwort-Antworten" mit einem Liniendiagramm zur Verteilung der Schlüsselwörter im Zeitverlauf und einem Abschnitt „Schlüsselwort-Kategorien" mit ausgewählten Kontrollkästchen für „Opt-in", „Opt-out", „Hilfe", „Sonstiges", „Mehr" und „Coaching".]({% image_buster /assets/img/sms/keyword_responses.png %})

Hier können Sie auch die Antwortverteilung für jede Schlüsselwort-Kategorie einsehen, um die nächsten Schritte für das [Retargeting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) festzulegen und bequem [ein Segment zu erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).

![Die Tabelle unterhalb des Liniendiagramms mit Spalten für Schlüsselwort-Kategorie, Antwortverteilung und Retargeting, wobei Sie die Möglichkeit haben, ein Segment mit der Schlüsselwort-Kategorie zu erstellen.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Details zum Konversions-Event

Das Panel **Details zum Konversions-Event** zeigt Ihnen die Performance Ihrer Konversions-Events für Ihre Kampagne. Weitere Informationen finden Sie unter [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results).

![Das Panel „Details zum Konversions-Event".]({% image_buster /assets/img/cc-conversion.png %})

### Konversionskorrelation

Das Panel **Konversionskorrelation** gibt Ihnen Aufschluss darüber, welche Nutzerattribute und Verhaltensweisen die von Ihnen für Kampagnen festgelegten Ergebnisse fördern oder beeinträchtigen. Weitere Informationen finden Sie unter [Konversionskorrelation]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/).

![Das Panel „Konversionskorrelation" mit einer Analyse der Nutzerattribute und des Verhaltens aus dem primären Konversions-Event – A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## Berichts-Builder

Sie können auch den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, um benutzerdefinierte Berichte für Ihre KakaoTalk-Kampagnen zu erstellen. Beim Erstellen eines Berichts können Sie filtern, um nur KakaoTalk-Kampagnen einzubeziehen, indem Sie unter **Kanäle** die Option **KakaoTalk** auswählen oder nach Tags filtern, die Sie Ihren KakaoTalk-Kampagnen zugewiesen haben.

{% endif %}

{% if include.channel == "whatsapp" %}

### Meta-Analytics

Zusätzlich zu den Braze-Analytics können Sie im WhatsApp Business Manager auf Analytics auf Vorlagenebene zugreifen. Weitere Informationen finden Sie in der [Dokumentation von Meta](https://www.facebook.com/business/help/218116047387456).

{% endif %}

{% if include.channel == "SMS" %}

### SMS-Currents-Events

Wie bei E-Mails empfängt Braze Events auf Nutzerebene im Zusammenhang mit einer SMS-Nachricht auf ihrem Weg zur Nutzer:in. Alle eingehenden SMS-Events werden auch als Currents-Event über das Event [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) gesendet. So können Sie zusätzliche Aktionen durchführen oder Berichte zu den Nachrichten erstellen, die Ihre Nutzer:innen außerhalb der Braze-Plattform senden.

{% alert note %}
Eingehende Nachrichten werden nach 1.600 Zeichen abgeschnitten.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Bindungsbericht

Bindungsberichte zeigen Ihnen die Raten, mit denen Ihre Nutzer:innen ein ausgewähltes Bindungs-Event über Zeiträume in einer bestimmten Kampagne{% if include.channel != "banner" %} oder Canvas{% endif %} durchgeführt haben. Weitere Informationen finden Sie unter [Bindungsberichte]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

## Funnel-Bericht

Funnel-Berichte bieten einen visuellen Bericht, mit dem Sie die Wege Ihrer Kund:innen nach dem Erhalt einer Kampagne{% if include.channel != "banner" %} oder Canvas{% endif %} analysieren können. Wenn Ihre Kampagne {% if include.channel != "banner" %}oder Canvas {% endif %}eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie nachvollziehen, wie sich die verschiedenen Varianten auf den Konversionstrichter ausgewirkt haben, und auf Grundlage dieser Daten optimieren.

Weitere Informationen finden Sie unter [Funnel-Berichte]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

{% endif %}