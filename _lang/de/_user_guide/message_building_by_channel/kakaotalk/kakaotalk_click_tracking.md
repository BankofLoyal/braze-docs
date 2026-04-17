---
nav_title: KakaoTalk-Klick-Tracking
article_title: KakaoTalk-Klick-Tracking
page_order: 3
description: "Diese Seite beschreibt, wie Sie das Klick-Tracking in Ihren KakaoTalk-Nachrichten aktivieren, gekürzte Links testen, Ihre eigene Domain in getrackten Links verwenden und mehr."
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# KakaoTalk-Klick-Tracking

> Diese Seite beschreibt, wie Sie das Klick-Tracking in Ihren KakaoTalk-Nachrichten aktivieren, gekürzte Links testen, Ihre eigene Domain in getrackten Links verwenden und mehr.

Wenn das KakaoTalk-Klick-Tracking aktiviert ist, kürzt Braze Ihre URLs automatisch, fügt Tracking-Mechanismen hinzu und erfasst Klicks in Echtzeit. Diese Daten ermöglichen es Ihnen, gezieltere Segmentierungs- und Retargeting-Strategien zu entwickeln – zum Beispiel Nutzer:innen anhand ihres Klickverhaltens zu segmentieren oder Nachrichten als Reaktion auf bestimmte Klicks zu triggern.

KakaoTalk-Klick-Tracking kann für Text-, Bild- und Listeneintrags-Nachrichten verwendet werden. Es unterstützt Links innerhalb von Buttons und Bild-Klick-Aktionen. Sie können URLs auch mit Liquid und eigenen Domains personalisieren.

## Funktionsweise

Sie können die Einstellungen für das KakaoTalk-Klick-Tracking im Abschnitt **Link options** des Nachrichten-Editors verwalten. Wenn es aktiviert ist, werden URLs mit der Standard-Braze-Domain (`https://brz.ai`) oder der für die Abo-Gruppe festgelegten eigenen Domain gekürzt und für die jeweiligen Nutzer:innen personalisiert.

Alle URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Sie können bis zu 25 URLs in einer Nachricht verwenden. Gekürzte URLs, die Liquid-Personalisierung enthalten (z. B. nutzerspezifisches Tracking oder UTM-Parameter), sind zwei Monate lang gültig.

## Klick-Tracking einrichten

### Textnachrichten

So richten Sie das Klick-Tracking für eine Textnachricht ein:

1. Verfassen Sie eine **Text**-Nachricht und fügen Sie eine URL in das Textfeld oder den Button ein.
2. Bestätigen Sie im Abschnitt **Link options** des Nachrichten-Editors, dass **Click Tracking** aktiviert ist. Das Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

![KakaoTalk-Textnachrichten-Editor mit dem Abschnitt „Link options", in dem „Click Tracking" aktiviert ist.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### Bildnachrichten

So richten Sie das Klick-Tracking für eine Bildnachricht ein:

1. Verfassen Sie eine **Image**-Nachricht und legen Sie als Klick-Verhalten das Öffnen einer URL fest.
2. Geben Sie eine URL in das URL-Feld ein.
3. Bestätigen Sie im Abschnitt **Link options** des Nachrichten-Editors, dass **Click Tracking** aktiviert ist.

### Listeneintrags-Nachrichten

So richten Sie das Klick-Tracking für eine Listeneintrags-Nachricht ein:

1. Verfassen Sie eine **List item**-Nachricht und fügen Sie eine URL in das Feld **Website URL** für einen beliebigen Eintrag ein.
2. Bestätigen Sie im Abschnitt **Link options** des Nachrichten-Editors, dass **Click Tracking** aktiviert ist.

## Eigene Domains

Das KakaoTalk-Klick-Tracking ermöglicht es Ihnen, Ihre eigene Domain zu verwenden, um das Erscheinungsbild Ihrer gekürzten URLs anzupassen und so ein einheitliches Markenbild zu vermitteln. Weitere Informationen finden Sie unter [Eigene Domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Liquid-Personalisierung in URLs

Sie können Ihre URL direkt im Braze-Nachrichten-Editor dynamisch zusammenstellen, um dynamische UTM-Parameter hinzuzufügen oder Nutzer:innen individuelle Links zu senden (z. B. um sie zu ihrem Warenkorb-Abbruch oder zu einem bestimmten Produkt weiterzuleiten, das wieder auf Lager ist).

URLs können mithilfe aller unterstützten Liquid-Personalisierungs-Tags dynamisch generiert werden.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Sie können auch benutzerdefinierte Liquid-Variablen kürzen, wie im folgenden Beispiel gezeigt:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

Braze kürzt URLs, die von Liquid gerendert werden – auch solche, die in API-Trigger-Eigenschaften enthalten sind. Wenn beispielsweise {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, wird Braze diese URL vor dem Senden der KakaoTalk-Nachricht kürzen und tracken.

## Testen

Bevor Sie Ihre Kampagne oder Ihr Canvas starten, empfiehlt es sich, Ihre Nachricht zunächst in der Vorschau anzuzeigen und zu testen. Gehen Sie dazu zum Tab **Test**, um eine KakaoTalk-Nachricht an Inhalts-Testgruppen oder einzelne Nutzer:innen in der Vorschau anzuzeigen und zu senden.

Die Vorschau wird mit der entsprechenden Personalisierung und der gekürzten URL aktualisiert.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird erst generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

## Reporting

Die KakaoTalk-Performance-Tabelle enthält die Spalte **Total Clicks**, die die Anzahl der Klick-Ereignisse pro Variante und die zugehörige Klickrate anzeigt. Weitere Details zu KakaoTalk-Metriken finden Sie unter [KakaoTalk-Reporting]({{site.baseurl}}/kakaotalk_reporting/).

Klick-Daten werden automatisch im Analytics-Dashboard angezeigt.

## Nutzer:innen retargeten

Sie können Nutzer:innen, die auf eine URL in einer KakaoTalk-Nachricht geklickt haben, mithilfe der folgenden Segmentierungs-Filter und Trigger retargeten:

- Aktionsbasierte Trigger
    - Interact with Campaign
    - Interact with Step

- Segmentierungs-Filter
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Häufig gestellte Fragen

### Sind die Links, die ich beim Testsenden erhalte, echte URLs?

Ja, beim Testsenden werden echte URLs generiert. Die genaue URL, die in einer gestarteten Kampagne gesendet wird, kann sich jedoch von der im Testversand gesendeten URL unterscheiden.

### Kann ich UTM-Parameter zu einer URL hinzufügen, bevor sie gekürzt wird?

Ja, es können sowohl statische als auch dynamische Parameter hinzugefügt werden.

### Wie lange bleiben gekürzte URLs gültig?

Personalisierte URLs sind ab dem Zeitpunkt der URL-Registrierung zwei Monate lang gültig.

### Muss das Braze SDK installiert sein, um URLs zu kürzen?

Nein, das Klick-Tracking funktioniert ohne jegliche SDK-Integration.

### Kann ich sehen, welche einzelnen Nutzer:innen auf eine URL klicken?

Ja. Wenn das Klick-Tracking aktiviert ist, können Sie Nutzer:innen, die auf URLs geklickt haben, mithilfe der [KakaoTalk-Retargeting-Filter](#retargeting-users) retargeten.

### Funktioniert das Klick-Tracking mit Deeplinks oder Universal Links?

Das Klick-Tracking gilt für Web-URLs. Für Deeplinks können Sie einen Deeplink direkt als Klick-Aktionstyp für Buttons in KakaoTalk festlegen – diese durchlaufen keine URL-Kürzung und kein Klick-Tracking. Wenn Sie Universal Links von Anbietern wie Branch oder Appsflyer verwenden möchten, können diese gekürzt werden, aber Braze kann keine Probleme beheben, die dabei auftreten können (z. B. fehlerhafte Attribution oder fehlgeschlagene Weiterleitungen).