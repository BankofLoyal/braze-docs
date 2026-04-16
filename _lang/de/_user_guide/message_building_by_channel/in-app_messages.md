---
nav_title: "In-App-Nachrichten"
article_title: In-App-Nachrichten
page_order: 3
alias: /in-app_messages/
description: "Auf dieser Landing-Page finden Sie alles rund um In-App-Nachrichten. Hier finden Sie Artikel über die Erstellung von In-App-Nachrichten, den Drag-and-Drop-Editor, die Anpassung Ihrer Nachrichten, Berichte und vieles mehr."
channel:
  - in-app messages
search_rank: 5
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} In-App-Nachrichten

> In-App-Nachrichten ermöglichen es Ihnen, Ihren Nutzer:innen Inhalte zukommen zu lassen, ohne sie mit Push-Benachrichtigungen zu stören, da diese Nachrichten nicht außerhalb der App zugestellt werden und nicht auf dem Startbildschirm erscheinen. 

Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größten Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungswerkzeugen, aus denen Sie wählen können, binden In-App-Nachrichten Ihre Nutzer:innen mehr als je zuvor. Sie werden im Kontext angezeigt, haben eine geringere Dringlichkeit und werden zugestellt, wenn die Nutzer:innen in Ihrer App aktiv sind. Beispiele für In-App-Nachrichten finden Sie in unseren [Kundenberichten](https://www.braze.com/customers/).

## Anwendungsfälle

Mit dem reichhaltigen Angebot an Inhalt, den In-App-Nachrichten bieten, können Sie diesen Kanal für eine Vielzahl von Anwendungsfällen nutzen:

| Anwendungsfall | Erklärung |
| --- | --- |
| Push-Priming | Führen Sie eine [Push-Priming-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) mit einer reichhaltigen In-App-Nachricht durch, um Ihren Kund:innen die Vorteile einer Push-Erlaubnis für Ihre App oder Website zu verdeutlichen, und fordern Sie sie auf, die Push-Erlaubnis zu erteilen.
| Verkäufe und Aktionen | Verwenden Sie modale In-App-Nachrichten, um Kund:innen mit visuell ansprechenden Medien zu begrüßen, die statische Aktionscodes oder Angebote enthalten. Ermutigen Sie sie zu Käufen oder Konversionen, die sie sonst nicht getätigt hätten. |
| Förderung der Feature-Nutzung | Ermuntern Sie Ihre Kund:innen, andere Teile Ihrer App zu nutzen oder einen Dienst in Anspruch zu nehmen. |
| Hochgradig personalisierte Kampagnen | Platzieren Sie In-App-Nachrichten als das Erste, was Ihre Kund:innen sehen, wenn sie Ihre App oder Website betreten. Fügen Sie einige Braze-Features zur Personalisierung hinzu, wie z. B. [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), um Nutzer:innen zum Handeln zu bewegen und so Ihre Reichweite zu erhöhen.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Anwendungsfälle, die Sie in Betracht ziehen sollten:

- Neue Features in der App
- App-Verwaltung
- Bewertungen
- App-Upgrades oder -Updates
- Werbegeschenke und Verlosungen

## Standard-Nachrichtentypen

Die folgenden Tabs zeigen, wie es aussieht, wenn Ihre Nutzer:innen eine unserer standardmäßigen In-App-Nachrichtenarten öffnen – Slideup-, modale und Vollbild-In-App-Nachrichten.

{% tabs %}
{% tab Slideup %}

Slideup-Nachrichten erscheinen normalerweise am oberen oder unteren Rand des App-Bildschirms (Sie können dies beim Erstellen Ihrer Nachricht einstellen). Diese eignen sich hervorragend, um Ihre Nutzer:innen über neue Nutzungsbedingungen, Cookies und andere Informationen zu informieren.

![Slideup-In-App-Nachricht, die am unteren Rand des App-Bildschirms angezeigt wird. Das Slideup enthält ein Symbolbild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Modale Nachrichten erscheinen in der Mitte des Gerätebildschirms mit einem Overlay, das sie von Ihrer App im Hintergrund abhebt. Sie eignen sich perfekt, um Ihren Nutzer:innen auf deutliche Weise vorzuschlagen, von einem Verkauf oder einer Werbeaktion zu profitieren.

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialogfeld angezeigt wird. Das Modal enthält ein Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

Vollbild-Nachrichten sind genau das, was Sie erwarten – sie nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer:innen wirklich benötigen, z. B. bei obligatorischen App-Updates.

![Vollbild-In-App-Nachricht, die einen App-Bildschirm einnimmt. Die Vollbild-Nachricht umfasst ein großes Bild, eine Kopfzeile, den Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Zusätzlich zu diesen Standard-Nachrichten-Templates können Sie Ihre Nachrichten auch mithilfe von angepassten HTML-In-App-Nachrichten, Internet-Modalen mit CSS oder Internet-E-Mail-Erfassungsformularen weiter anpassen. Weitere Informationen finden Sie unter [Anpassung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Vorlagenbasierte In-App-Nachrichten

In-App-Nachrichten werden als vorlagenbasierte In-App-Nachrichten zugestellt, wenn die Option **Kampagnenberechtigung vor der Anzeige erneut prüfen** ausgewählt ist oder wenn einer der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- SMS-Variablen wie z. B. {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Dies bedeutet, dass das Gerät zu Beginn der Sitzung den Auslöser dieser In-App-Nachricht anstelle der gesamten Nachricht empfängt. Wenn die Nutzer:innen die In-App-Nachricht triggern, sendet das Gerät eine Netzwerkanfrage, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Internetzugang hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Liquid-Logik zu lange für die Auflösung benötigt.
{% endalert %}

## Abbruchverhalten

Bei Braze kommt es zu einem Abbruch, wenn Nutzer:innen eine Aktion ausführen, die sie zum Empfang einer Nachricht berechtigt, sie die Nachricht jedoch nicht erhalten, weil sie aufgrund der Liquid-Logik als nicht berechtigt markiert sind. Zum Beispiel:

1. Sam führt eine Aktion durch, die eine E-Mail-Kampagne triggern sollte.
2. Der Text der E-Mail enthält eine Liquid-Logik, die besagt, dass diese E-Mail nicht versendet werden soll, wenn die Punktzahl eines angepassten Attributs unter 50 liegt.
3. Sams Punktzahl für das angepasste Attribut beträgt 20.
4. Braze erkennt, dass Sam diese E-Mail nicht erhalten sollte, und die E-Mail wird abgebrochen.
5. Ein Abbruchereignis wird protokolliert.

Da In-App-Nachrichten jedoch ein Pull-Kanal sind, funktionieren Abbrüche bei ihnen etwas anders.

### Abbruchverhalten bei In-App-Nachrichten

In-App-Nachrichten werden zu Beginn der Sitzung vom Gerät abgerufen und auf dem Gerät zwischengespeichert, sodass die Nachricht unabhängig von der Qualität der Internetverbindung sofort zugestellt werden kann. Wenn Nutzer:innen beispielsweise fünf In-App-Nachrichten innerhalb einer Sitzung erhalten, werden alle fünf zu Beginn der Sitzung abgerufen. Die Nachrichten werden lokal zwischengespeichert und erscheinen, wenn die definierten Auslöseereignisse eintreten (Sitzungsstart, Nutzer:innen klicken auf einen Button, der ein angepasstes Event protokolliert, oder andere).

Mit anderen Worten: Die Entscheidung, ob eine In-App-Nachricht abgebrochen werden soll, wird getroffen, **bevor** der Auslöser eintritt. Um dies zu veranschaulichen, nehmen wir an, dass Sam aus dem E-Mail-Beispiel Push-Benachrichtigungen abonniert hat.

1. Sam beginnt eine Sitzung, indem er eine von Braze unterstützte App auf seinem Smartphone startet.
2. Basierend auf den Zielgruppenkriterien der aktiven Kampagnen im Workspace könnte Sam für fünf verschiedene Kampagnen in Frage kommen. Alle fünf werden auf das Gerät heruntergeladen und zwischengespeichert.
3. Sam **hat keine** Aktionen durchgeführt, die diese Nachrichten triggern würden, könnte diese Nachrichten jedoch in der Sitzung erhalten.
4. Die Liquid-Logik in zwei der In-App-Nachrichten enthält Regeln, die Sam vom Empfang der Nachricht ausschließen (z. B. weil das angepasste Attribut „Punktzahl" nicht hoch genug ist).
5. Sam erhält die beiden In-App-Nachrichten, die ihn ausschließen, nicht, jedoch werden ihm die anderen drei Nachrichten zugestellt.
6. Es werden keine Abbruchereignisse protokolliert.

Braze protokolliert in Sams Fall keine Abbruchereignisse, da dies nicht unserer Definition eines Abbruchs entspricht; Sam **hat keine** Aktionen durchgeführt, die die Nachrichten ausgelöst hätten. Bei In-App-Nachrichten führen Nutzer:innen den Auslöser nie tatsächlich aus, bevor Braze feststellt, dass sie die Nachricht nicht sehen sollten.

#### Abbruchverhalten bei vorlagenbasierten In-App-Nachrichten

[Vorlagenbasierte In-App-Nachrichten](#templated-in-app-messages) veranlassen das SDK dazu, erneut zu prüfen, ob eine Nachricht angezeigt werden soll, wenn das auslösende Ereignis eintritt. Dies weist ein abweichendes Abbruchverhalten auf. Zur Veranschaulichung betrachten wir das folgende Beispiel:

1. Sam startet eine Braze-Sitzung, indem er eine von Braze unterstützte App auf seinem Smartphone öffnet.
2. Die Zielgruppenkriterien der aktiven Kampagnen zeigen, dass Sam für eine vorlagenbasierte In-App-Nachricht in Frage kommen könnte, sodass die Auslöseinformationen ohne die Nachrichtennutzlast an sein Gerät gesendet werden.
3. Sam wählt einen Button aus, der ein angepasstes Event protokolliert und die vorlagenbasierte In-App-Nachricht triggert.
4. Sams Gerät sendet eine Netzwerkanfrage, um die In-App-Nachricht abzurufen.
5. Die Liquid-Logik der Nachricht führt zu einem Abbruch, daher protokolliert Braze dies als Abbruch; Sam hat die Aktion zum Triggern vor dieser Auswertung durchgeführt.

##### Vergleich des Abbruchverhaltens von In-App-Nachrichten

Diese Tabelle vergleicht die In-App-Nachrichtenflüsse, die Sam erlebt hat:

| In-App-Nachricht | Abbruchverhalten |
| --- | --- |
| Standard | Ein Abbruchereignis wurde nicht protokolliert, da Sam keine Aktionen durchgeführt hat, die eine Nachricht ausgelöst hätten.<br><br>Standardmäßige In-App-Nachrichten protokollieren keine Abbrüche, da ein Abbruch als „die Nachricht wurde trotz Ausführung der Aktion zum Triggern nicht angezeigt" definiert ist. Da In-App-Nachrichten an das Gerät zugestellt werden, bevor die Aktionen zum Triggern stattfinden, ist es nicht sinnvoll, In-App-Nachrichten aufgrund der Liquid-Logik als ausgelassen zu betrachten. |
| Vorlagenbasiert | Ein Abbruchereignis wurde protokolliert, da Sam die Aktion zum Triggern der vorlagenbasierten In-App-Nachricht ausgeführt hat, jedoch einen Abbruch in der Liquid-Vorlage erhalten hat. <br><br>Vorlagenbasierte In-App-Nachrichten protokollieren Abbrüche, da die Liquid-Auswertung erst nach der Aktion erfolgt, die den Trigger auslöst. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Weitere Ressourcen

Bevor Sie mit der Erstellung Ihrer eigenen In-App-Nachrichten-Kampagnen beginnen – oder In-App-Nachrichten in einer Multichannel-Kampagne verwenden – empfehlen wir Ihnen dringend, sich unseren [Leitfaden zur Vorbereitung von In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/) anzusehen. Dieser Leitfaden behandelt Fragen zu Targeting, Inhalt und Konversion, die Sie bei der Erstellung von In-App-Nachrichten berücksichtigen sollten.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}