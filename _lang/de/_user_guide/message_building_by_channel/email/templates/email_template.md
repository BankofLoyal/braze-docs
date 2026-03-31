---
nav_title: Eine E-Mail-Vorlage erstellen
article_title: Eine E-Mail-Vorlage erstellen
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Sie E-Mail-Templates erstellen, anpassen und verwalten."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Eine E-Mail-Vorlage erstellen

> Das Braze-Dashboard verfügt über einen E-Mail-Template-Editor, mit dem Sie maßgeschneiderte, aufmerksamkeitsstarke E-Mails erstellen und zur späteren Verwendung in Kampagnen speichern können. Sie können auch Ihr eigenes [HTML-E-Mail-Template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) hochladen.

## 1. Schritt: Navigieren Sie zum E-Mail-Template-Editor

Gehen Sie zu **Templates** > **E-Mail-Templates**.

## 2. Schritt: Wählen Sie Ihre Bearbeitungsoption

Wählen Sie zwischen dem **Drag-and-Drop-Editor** oder dem **HTML-Editor** für Ihre Bearbeitung. 

Als Nächstes können Sie aus vorgefertigten Braze-Templates wählen, ein neues Template erstellen oder ein bestehendes Template (einfach oder [mobil responsiv]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)) bearbeiten.

![Ein E-Mail-Template für den Frühjahrsverkauf eines Unternehmens mit der Möglichkeit, den Drag-and-Drop-Editor oder den HTML-Editor auszuwählen oder aus Braze-Templates auszuwählen.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Vorhandene angepasste HTML-Templates müssen mit dem Drag-and-Drop-Editor neu erstellt werden.
{% endalert %}

## 3. Schritt: Passen Sie Ihr Template an

Nachdem Sie Ihre Bearbeitungsoption ausgewählt haben, haben Sie nun die Möglichkeit, Ihr E-Mail-Template kreativ anzupassen. Sie können HTML verwenden, um Ihr Branding im HTML-Editor zu erstellen und umzusetzen, oder eine Vielzahl von [kreativen Details]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) im Drag-and-Drop-Editor einfügen.

### Einfügen eines Abmeldelinks

Wenn Sie bei der Gestaltung Ihres E-Mail-Templates keinen Abmeldelink einfügen, wird Braze Sie auffordern, diesen in Ihre E-Mail einzufügen, da er in allen Marketing-E-Mails gesetzlich vorgeschrieben ist. Sie können diesen Abmeldelink als Fußzeile am Ende Ihrer E-Mails einfügen, indem Sie den Liquid-Tag {% raw %}``${email_footer}``{% endraw %} verwenden oder in Ihrem Template [die Fußzeile anpassen]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer).

## 4. Schritt: Prüfen Sie auf E-Mail-Fehler

E-Mail-Fehler werden auf dem Tab **Verfassen** des Nachrichten-Workflows angezeigt. Fehler hindern Sie am Fortfahren. „Warnungen" sind Hinweise, die Ihnen helfen sollen, Best Practices zu befolgen. Je nach Ihrem Unternehmen können Sie diese auch ignorieren.

![Liste der Fehler und Warnungen aus einer Beispiel-E-Mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Hier finden Sie eine Liste der Fehler, die in unserem Editor berücksichtigt werden:

- Falsche Liquid-Syntax
- [E-Mail-Textkörper größer als 400 KB; es wird dringend empfohlen, dass sie weniger als 102 KB groß sind]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- Templates ohne Abmeldelink
- E-Mails mit leerem **Text** oder **Betreff**
- E-Mails ohne Abmeldelink

## 5. Schritt: Vorschau und Test Ihrer Nachricht

Nachdem Sie Ihr Template erstellt haben, können Sie es testen, bevor Sie es versenden.

Wählen Sie unten auf dem Übersichtsbildschirm **Vorschau und Test** aus. Hier können Sie eine Vorschau darauf sehen, wie Ihre E-Mail im Posteingang Ihrer Kund:innen erscheinen wird. Wenn Sie **Vorschau als Nutzer:in** ausgewählt haben, können Sie Ihre E-Mail als zufällige:r Nutzer:in anzeigen lassen, eine:n bestimmte:n Nutzer:in auswählen oder eine:n angepasste:n Nutzer:in erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie gewünscht funktionieren. 

Dann können Sie **Vorschau-Link kopieren**, um einen teilbaren Vorschau-Link zu erzeugen und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Der Link bleibt sieben Tage lang gültig, bevor er neu generiert werden muss.

Sie können auch zwischen der Desktop-, der Mobil- und der Klartextansicht wechseln, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheinen wird.

{% alert tip %}
Sind Sie neugierig, wie Ihre E-Mail für Nutzer:innen im Dark Mode aussieht? Wählen Sie den Schalter **Dark-Mode-Vorschau** im Bereich **Vorschau und Test** (nur im Drag-and-Drop-Editor).
{% endalert %}

Wenn Sie für eine abschließende Prüfung bereit sind, wählen Sie **Testsendung** und senden Sie eine Testnachricht an sich selbst oder an eine Gruppe von Inhaltstester:innen, um sicherzustellen, dass Ihre E-Mail auf einer Vielzahl von Geräten und E-Mail-Clients korrekt angezeigt wird.

![Beispiel für eine E-Mail-Vorschau, die zu Testzwecken versendet wird.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Sie Probleme mit Ihrem Template sehen oder Änderungen vornehmen möchten, wählen Sie **E-Mail bearbeiten**, um zum Editor zurückzukehren.

## 6. Schritt: Template speichern

Speichern Sie Ihr Template, indem Sie **Template speichern** auswählen. Jetzt können Sie dieses Template in jeder beliebigen Kampagne oder Canvas-Komponente verwenden. Um auf Ihr Template zuzugreifen, wählen Sie die Bearbeitungsoption, mit der Sie es erstellt haben, und wählen Sie es dann aus der Liste der verfügbaren Templates aus.

{% alert note %}
Wenn Sie Änderungen an einem bestehenden Template vornehmen, werden diese Änderungen nicht in Kampagnen übernommen, die mit früheren Versionen dieses Templates erstellt wurden.
{% endalert %}

### Verwaltung Ihrer Templates

Sie können E-Mail-Templates unter **Templates** > **E-Mail-Templates** einsehen und nach Status, Typ oder Tags filtern oder nach Name suchen. Sie benötigen die Berechtigung **Zugriff auf Kampagnen, Canvase, Cards, Content-Blöcke, Feature-Flags, Segmente, Medienbibliothek, Standorte, Aktionscodes und Präferenzzentren** (oder die entsprechende granulare Berechtigung, z. B. **E-Mail-Templates anzeigen**), um diese Templates einzusehen. Weitere Details finden Sie unter [Nutzer:innen-Berechtigungen]({{site.baseurl}}/user_guide/administrative/access_braze/user_permissions/).

Wenn Sie weitere E-Mail-Templates erstellen, können Sie diese [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) und [archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Mehr erfahren Sie unter [Templates und Medien]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Verwendung Ihrer Templates in API-Kampagnen

Um Ihre E-Mail für eine API-Kampagne zu verwenden, benötigen Sie eine `email_template_id`, die Sie am Ende jedes in Braze erstellten E-Mail-Templates finden.

![API-Bezeichner am unteren Rand eines E-Mail-Templates.]({% image_buster /assets/img/email_templates/template5.png %})

### Kommentare zu E-Mail-Templates

Sie können E-Mail-Templates im Drag-and-Drop-Editor gemeinsam bearbeiten und kommentieren. 

1. Wählen Sie den Content-Block oder die Zeile im E-Mail-Text aus, zu der Sie einen Kommentar abgeben möchten.
2. Wählen Sie das <i class="fas fa-comment"></i> Kommentar-Symbol.
3. Geben Sie Ihren Kommentar in der Seitenleiste ein und wählen Sie dann **Senden**.
4. Nachdem Sie Ihre Kommentare eingegeben haben, wählen Sie **Fertig**.
5. Wählen Sie **Template speichern**, um Ihre Kommentare zu speichern.

Nachdem Ihr Template gespeichert wurde, sehen Nutzer:innen Symbole über nicht beantworteten Kommentaren. Wählen Sie **Auflösen**, um diese Kommentare aufzulösen.

![Ein Kommentar in einem E-Mail-Template, der lautet „Sieht gut aus".]({% image_buster /assets/img/email_templates/template_comment.png %})

Antworten auf häufig gestellte Fragen zu E-Mail-Templates finden Sie in unseren [FAQ zu Templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).