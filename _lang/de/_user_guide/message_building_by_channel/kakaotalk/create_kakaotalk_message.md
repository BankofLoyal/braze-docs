---
nav_title: KakaoTalk-Nachricht erstellen
article_title: "KakaoTalk-Nachricht erstellen"
description: "Dieser Referenzartikel beschreibt, wie Sie eine KakaoTalk-Nachricht erstellen."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# KakaoTalk-Nachricht erstellen

> Nutzen Sie den [KakaoTalk-Messaging-Kanal]({{site.baseurl}}/kakaotalk/), um Nutzer:innen direkt über die KakaoTalk-Plattform zu erreichen. Erstellen Sie ein personalisiertes Nutzungserlebnis, indem Sie Liquid und anderen dynamischen Content verwenden, um eine Umgebung zu schaffen, die ein reichhaltiges Nutzungserlebnis mit Ihrer Marke fördert und verbessert.<br><br>Informationen zur Einrichtung Ihres KakaoTalk-Messaging-Kanals finden Sie unter [KakaoTalk einrichten]({{site.baseurl}}/kakaotalk_setup/).

## 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten

KakaoTalk wird sowohl in Kampagnen als auch in Canvas unterstützt. Kampagnen eignen sich am besten für einzelne Messaging-Kampagnen, während Canvase es Ihnen ermöglichen, mehrstufige, kanalübergreifende User Journeys zu orchestrieren.

{% tabs local %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **KakaoTalk** für eine Einzelkanal-Kampagne oder **Multichannel-Kampagne** für eine Kampagne mit mehreren Kanälen.

![Panel mit Optionen zur Auswahl des Messaging-Kanals.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Sie können Ihrer Kampagne zusätzliche Varianten hinzufügen, mit denen Sie verschiedene Nachrichtentypen und Layouts auswählen können. Weitere Informationen finden Sie unter [Multivariate und A/B-Tests](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/).

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. Fügen Sie im Canvas-Builder einen Nachrichten-Schritt hinzu und wählen Sie **KakaoTalk**.

![Auswahl des Messaging-Kanals im Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## 2. Schritt: Verfassen Sie Ihre KakaoTalk-Nachricht

1. Wählen Sie das Dropdown-Menü **KakaoTalk-Kanal**, das eine Liste der KakaoTalk-Kanäle anzeigt, die Sie über die Seite „Technology Partners" eingerichtet haben, und wählen Sie den KakaoTalk-Kanal aus, über den die Nachricht gesendet werden soll.
2. Wählen Sie den zu sendenden Nachrichtentyp:
- Text
- Bild
- Listenelement
    - Schmal
    - Breit

![KakaoTalk-Varianten-Bereich mit drei auswählbaren Nachrichtentypen.]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

{% tabs local %}
{% tab Text %}

Eine KakaoTalk-Textnachricht ist die einfachste Form der Kommunikation: eine Standard-Textnachricht.

### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Textinhalt, einschließlich Emojis und Liquid-Personalisierung |
| Textkapazität | Bis zu 1.000 Zeichen |
| Buttons | Bis zu 5 optionale Buttons. Derzeit kann dies nur verwendet werden, um beim Klick eine URL zu öffnen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Eine KakaoTalk-Textnachricht im Composer.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Image %}

Ein Bild ist eine Nachricht, die ein visuelles Element mit unterstützendem Text kombiniert. Braze übernimmt automatisch den Upload des Bildes auf die KakaoTalk-Server.

### Allgemeine Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Ein Bild und unterstützender Text |
| Akzeptierte Dateiformate | JPEG oder PNG |
| Empfohlene Breite | 500px |
| Dateigröße | Bis zu 500kb |
| Seitenverhältnis | Muss zwischen 2:1 (breit) und 3:4 (hoch) liegen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Schmale und breite Bildnachrichten haben jeweils unterschiedliche Zeichenanzahl- und Button-Anforderungen.

{% subtabs %}
{% subtab Narrow image %}

#### Schmales Bild

Eine schmale Bildnachricht zeigt ein etwas höheres, schmales Bild mit umfangreicheren Text- und Button-Optionen.

##### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Ein Bild und unterstützender Text |
| Textkapazität | Bis zu 500 Zeichen |
| Buttons | Bis zu 5 optionale Buttons |
| Bildquelle | Bilder können über die Braze-Medienbibliothek oder eine direkte URL hinzugefügt werden |
| Anpassung | Sie können das Klickverhalten für das Bild festlegen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Eine schmale KakaoTalk-Nachricht.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Wide image %}

#### Breites Bild

Eine breite Bildnachricht zeigt ein prominentes breites Bild, das sich für wirkungsvolle visuelle Kommunikation eignet, mit minimalem unterstützendem Text.

##### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Ein Bild und unterstützender Text |
| Textkapazität | Bis zu 76 Zeichen |
| Buttons | Bis zu 2 optionale Buttons |
| Bildquelle | Bilder können über die Braze-Medienbibliothek oder eine direkte URL hinzugefügt werden |
| Anpassung | Sie können das Klickverhalten des Bildes festlegen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Eine breite KakaoTalk-Nachricht.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Bilder hinzufügen

Sie können Bilder über die Braze-Medienbibliothek hinzufügen oder eine URL einfügen, die eine JPEG- oder PNG-Datei hostet. Sie können auch das Klickverhalten des Bildes festlegen, um Nutzer:innen, die darauf klicken, zu einer bestimmten URL weiterzuleiten.

Braze übernimmt automatisch alle Bild-Upload-Anforderungen von KakaoTalk. Das bedeutet, dass Sie Bilder **nicht** vor dem Senden von Nachrichten bei KakaoTalk-Anbietern hochladen müssen. Laden Sie einfach Bilder hoch und senden Sie die Nachricht direkt über Braze!

![Bereich mit ausgewählten Symbolen zum Hinzufügen eines schmalen Bildes.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab List item %}


Eine KakaoTalk-Artikellisten-Nachricht ist dafür konzipiert, eine Liste von Inhaltselementen in einem übersichtlichen, vertikalen Format darzustellen.

Listenelement-Nachrichten bestehen aus einem Header, einem Artikellisten-Bereich und einem optionalen Button-Bereich.

#### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Artikelanzahl | Erfordert mindestens 2 oder 3 Artikel |
| Buttons | Bis zu 5 optionale Buttons |
| Header | Bis zu 250 Zeichen |
| Artikeltitel | Bis zu 25 Zeichen |
| Website-URL (pro Artikel) | Bis zu 250 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Eine KakaoTalk-Listenelement-Nachricht.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## 3. Schritt: Klick-Tracking einrichten

Wenn das KakaoTalk-Klick-Tracking aktiviert ist, kürzt Braze automatisch Ihre URLs, fügt Tracking-Mechanismen hinzu und erfasst Klicks in Echtzeit. Diese Daten ermöglichen es Ihnen, gezieltere Segmentierungs- und Retargeting-Strategien zu erstellen – z. B. Nutzer:innen basierend auf dem Klickverhalten zu segmentieren und Nachrichten als Reaktion auf bestimmte Klicks zu triggern.

Klick-Tracking wird für Text-, Bild- und Listenelement-Nachrichten unterstützt. Es unterstützt Links innerhalb von Buttons und Bild-Klick-Aktionen. Sie können URLs auch mit Liquid und angepassten Domains personalisieren.

Um das Klick-Tracking zu aktivieren, setzen Sie ein Häkchen bei **Klick-Tracking** im Abschnitt **Link-Optionen** des Composers. URLs werden mit der Standard-Braze-Domain (`https://brz.ai`) oder der für die Abo-Gruppe angegebenen angepassten Domain gekürzt und für die Nutzer:innen personalisiert.

Ausführliche Informationen zu Klick-Tracking, angepassten Domains, Liquid-Personalisierung in URLs, Berichterstattung und Retargeting finden Sie unter [KakaoTalk-Klick-Tracking]({{site.baseurl}}/kakaotalk_click_tracking/).

### Retargeting von Nutzer:innen

Sie können Nutzer:innen, die eine URL in einer KakaoTalk-Nachricht angeklickt haben, mit den folgenden Segmentierungs-Filtern und Triggern retargeten:

- Aktionsbasierte Trigger
    - Mit Kampagne interagiert
    - Mit Schritt interagiert

- Segmentierungs-Filter
    - Kampagne angeklickt/geöffnet
    - Kampagne oder Canvas mit Tag angeklickt/geöffnet
    - Schritt angeklickt/geöffnet

## 4. Schritt: Vorschau und Test Ihrer KakaoTalk-Nachricht

Die Nachrichtenvorschau wird automatisch aktualisiert, während Sie Ihre KakaoTalk-Nachricht verfassen. Wenn Sie bereit zum Testen sind, gehen Sie zum Tab **Test**, um eine Testnachricht an Content-Testgruppen oder einzelne Nutzer:innen zu senden oder um die Nachricht als bestehende:r oder angepasste:r Nutzer:in direkt in Braze in der Vorschau anzuzeigen.

Nachdem Sie Ihre Testnutzer:innen ausgewählt haben, wählen Sie **Test senden**. Eine Benachrichtigung zeigt die Ergebnisse Ihres Testversands an. Für CJ OliveNetworks erhalten Sie eine „C100"-Antwort. Wenn Sie einen anderen Fehler sehen, konsultieren Sie die [CJ KakaoTalk-Nutzerdokumentation](https://developers.kakao.com/docs/latest/en/index).

![Vorschaufenster für eine KakaoTalk-Nachricht.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Um eine Testnachricht an bestehende Nutzer:innen in der Vorschau anzuzeigen und zu senden, benötigen Sie die Berechtigung „PII anzeigen". Sie können eine Testnachricht an angepasste Nutzer:innen ohne diese Berechtigungen in der Vorschau anzeigen und senden.
{% endalert %}

Um die Ergebnisse eines Versands zu überprüfen oder Probleme zu beheben, gehen Sie zu **Einstellungen** > **Nachrichtenaktivitätsprotokoll**. Weitere Informationen finden Sie unter [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

## 5. Schritt: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

In den folgenden Abschnitten finden Sie Details dazu, wie Sie unsere Tools am besten zum Erstellen von KakaoTalk-Nachrichten nutzen können.

### Zustellungszeitplan oder Trigger wählen

KakaoTalk-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen zu Zeitplan- und Trigger-Optionen finden Sie unter [Ihre Kampagne planen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) oder [Eingangs-Zeitplantypen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types) (für Ihren Canvas).

Sie können Zustellungskontrollen festlegen, z. B. Nutzer:innen erlauben, erneut für den Empfang der Kampagne berechtigt zu werden, oder Frequency-Capping-Regeln aktivieren. Bei aktionsbasierter Zustellung können Sie auch die Dauer der Kampagne und Ruhezeiten festlegen.

### Zielgruppe zusammenstellen

Richten Sie Ihre Zielgruppe aus, indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Derzeit kann KakaoTalk nur Freunde des Kanals anschreiben. Wir empfehlen, ein angepasstes Attribut zu setzen, um Kanal-Freunde zu kennzeichnen, damit Sie Ihre Nutzer:innen richtig segmentieren und vermeiden, KakaoTalk-Nachrichten an Nutzer:innen zu senden, die sie nicht empfangen können.

### Konversions-Events wählen

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen (Konversions-Events) nach dem Empfang einer Kampagne ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Kampagne zu messen. Wenn Sie beispielsweise versuchen, Nutzer:innen zur Nutzung Ihrer App zu bewegen, setzen Sie das Konversions-Event auf **Sitzung starten**.

Sie können auch angepasste Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen. Werden Sie kreativ und überlegen Sie, wie Sie den Erfolg Ihrer Kampagne messen möchten.

## 6. Schritt: Überprüfen und bereitstellen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie alles und senden Sie ab!