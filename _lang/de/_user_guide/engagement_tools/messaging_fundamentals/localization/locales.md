---
nav_title: Mehrsprachige Nachrichten
article_title: Mehrsprachige Nachrichten
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Locales in Ihren Nachrichten verwenden können."
---

# Mehrsprachige Nachrichten

> Nachdem Sie Ihrem Workspace Locales hinzugefügt haben, können Sie Nutzer:innen in verschiedenen Sprachen mit einem einzigen Push, einer E-Mail, einem Banner, einer In-App-Nachricht oder einem Content-Block ansprechen.

## Voraussetzungen

{% tabs %}
{% tab Multi-language locales %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Message types %}

| Feature | Erforderliche Berechtigungen |
| --- | --- |
| Nachrichtentypen | Sie benötigen diese Berechtigungen, um Locales und Übersetzungen zu Kampagnen und Canvasen hinzuzufügen:<br><br> {::nomarkdown}Granulare Berechtigungen: <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul> Legacy-Berechtigungen: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Templates %}

| Feature | Erforderliche Berechtigungen |
| --- | --- |
| Templates | Sie benötigen diese Berechtigungen für den Template-Typ, dem Sie Locales und Übersetzungen hinzufügen möchten:<br><br> {::nomarkdown}Granulare Berechtigungen: <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul> Legacy-Berechtigungen: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Verwendung von Locales

### 1. Schritt: Locales einrichten

Bevor Sie Übersetzungen zu einer Nachricht hinzufügen können, müssen Sie zunächst [die Locales erstellen, die Sie unterstützen möchten]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/). Locales definieren die verfügbaren Sprach- (und optional Regions-)Varianten für das Messaging.

### 2. Schritt: Inhalte für die Übersetzung markieren

Umschließen Sie den Text, den Sie übersetzen möchten, mit den Liquid-Übersetzungs-Tags {% raw %}`{% translation your_id_here %}` und `{% endtranslation %}`{% endraw %} und weisen Sie eine Tag-ID zu. Übersetzungs-Tag-IDs müssen innerhalb einer Nachricht eindeutig sein. Verwenden Sie am besten semantische ID-Namen, die den Text klar beschreiben, wie z. B. {% raw %}`{% translation header %}`{% endraw %}.

Hier ist ein Beispiel für eine zur Übersetzung markierte Nachricht: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Markieren Sie den Text, den Sie übersetzen möchten, und verwenden Sie die Tastenkombination **Cmd + Alt + L** (macOS) oder **Strg + Alt + L** (Windows), um ihn in Übersetzungs-Tags einzuschließen.<br><br> Diese Tastenkombination funktioniert in allen Kanälen, die mehrsprachiges Messaging unterstützen, mit Ausnahme der Drag-and-Drop-Editoren für E-Mail und Content-Blöcke. Verwenden Sie dort den Button **Add personalization** in der linken Seitenleiste, um Übersetzungs-Tags hinzuzufügen.
{% endalert %}

#### URLs lokalisieren

Beim Übersetzen von Inhalten erfordern URLs eine besondere Behandlung, um fehlerhafte Links zu vermeiden.

##### Standard-URLs (statisch)

Statische URLs werden manuell im Editor eingegeben (z. B. `https://example.com`). Wir empfehlen außerdem Folgendes:

| Empfehlung | Begründung |
| --- | --- |
| Belassen Sie das Protokoll (`https://`) außerhalb der Übersetzungs-Tags. Umschließen Sie nur die Domain und den Pfad (z. B. `example.com/en`). | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu fehlerhaften Links führt. |
| Fügen Sie keine Query-Parameter in Übersetzungs-Tags ein (z. B. `?utm_source=promo`). | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu fehlerhaften Links führt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine Standard-URL, die beide Empfehlungen befolgt, sieht so aus:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz%}{% endtranslation %}">Click Here</a>
```
{% endraw %}

{% alert important %}
Wenn Sie [E-Mail-Link-Tracking](#email-link-tracking) (Link Aliasing oder Link-Templates) verwenden, ist eine zusätzliche Konfiguration erforderlich, wenn URLs in Übersetzungs-Tags eingeschlossen sind.
{% endalert %}

#### HTML-Attribute und -Struktur

Umschließen Sie nur für Menschen lesbaren Text mit Übersetzungs-Tags. Vermeiden Sie es, HTML-Attribute (wie `class`, `style` oder `id`) oder anderen strukturellen Code einzuschließen. HTML-Attribute steuern Layout, Styling und Funktionalität. Wenn Sie sie in Übersetzungs-Tags einschließen, kann dies die Formatierung oder Styles in lokalisierten Versionen Ihrer Nachricht beschädigen.

Dieser Text ist korrekt eingeschlossen:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Falsch eingeschlossener Text %}

Dieser Text ist **falsch** eingeschlossen:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### 3. Schritt: Locales zu Ihrer Nachricht hinzufügen

Nachdem Sie Übersetzungs-Tags zu Ihrer Nachricht hinzugefügt haben, wählen Sie im Editor **Manage languages** (in den Drag-and-Drop-Editoren für E-Mail und Content-Blöcke: **Languages**) und wählen Sie mindestens ein Locale aus, für das Sie Übersetzungen hinzufügen möchten.

![Das Dropdown-Menü „Add locale" mit Optionen zur Auswahl des Standard-Locales oder angepasster Attribute.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content-Blöcke mit Übersetzungen

Wenn Ihre Nachricht Content-Blöcke enthält, für die bereits Übersetzungen gespeichert sind, müssen Sie diese Übersetzungen nicht erneut hochladen. Gespeicherte Übersetzungen werden automatisch angewendet, wenn der Content-Block zu Ihrer Nachricht hinzugefügt wird.

Im Modal **Manage languages** werden Content-Blöcke mit gespeicherten Übersetzungen zusammen mit den unterstützten Locales in der Liste angezeigt. So können Sie sehen, welche Teile Ihrer Nachricht bereits lokalisiert sind, bevor Sie neue Übersetzungen hinzufügen.

![Der Bereich „Manage languages" mit einer Liste von Content-Blöcken, die gespeicherte Übersetzungen enthalten.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Stellen Sie sicher, dass jeder Content-Block Übersetzungen für jedes Locale enthält, das Ihrer Nachricht hinzugefügt wurde. Wenn einem Content-Block Übersetzungen für eines der hinzugefügten Locales fehlen, wird er für Nutzer:innen in diesem Locale in der Originalsprache angezeigt.
{% endalert %}

### 4. Schritt: Übersetzungen hinzufügen

Nachdem Sie Locales ausgewählt haben, fügen Sie Übersetzungen zu Ihrer Nachricht mit einer der folgenden Methoden hinzu:

![Der Tab „Add translations" mit Optionen zum Hochladen von Übersetzungen per CSV oder zur Verbindung mit Übersetzungspartnern.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSV-Template hochladen %}

Wählen Sie **Download template**, um eine CSV-Datei herunterzuladen, die eine Matrix Ihrer ausgewählten Übersetzungs-IDs und Locales enthält. Geben Sie die Übersetzungen für jedes Locale ein. Laden Sie die ausgefüllte Datei hoch, und die Übersetzungen werden auf Ihre Nachricht angewendet.

{% alert important %}
Um Darstellungsprobleme mit nicht-englischen Zeichen zu vermeiden, verwenden Sie für Ihre Übersetzungs-CSV nicht Excel.
{% endalert %}

![CSV mit Übersetzungs-Tags für einen Titel, Angebotstext, Angebotsbetrag und CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Übersetzungs-API verwenden %}

Verwenden Sie eine Partner-Übersetzungs-API, um Übersetzungen in Ihren Kampagnen und Canvasen zu verwalten und zu aktualisieren. Dies ist nützlich, wenn Sie ein externes System für die Lokalisierung verwenden oder eine direkte Verbindung mit einem Übersetzungspartner herstellen möchten.

Um die Übersetzungs-Endpunkte mit Canvasen zu verwenden, geben Sie die folgenden Parameter an:
  - `workflow_id`
  - `step_id`
  - `message_variation_id` 

{% alert note %}
Bei der Verwendung der Übersetzungs-API mit Canvas-Schritten, die nach dem Start des Canvas erstellt wurden, ist die `message_variation_id`, die Sie an die API übergeben, leer.
{% endalert %}

{% endtab %}
{% endtabs %}

### 5. Schritt: Übersetzungen in der Vorschau anzeigen

Um eine Vorschau Ihrer Nachricht anzuzeigen, wählen Sie die Option **Multi-Language User** aus dem Dropdown-Menü **Preview as User**. So können Sie zwischen verschiedenen Locale-Definitionen wechseln, um alle Übersetzungen Ihrer Nachricht in der Vorschau anzuzeigen.

![Vorschau der Locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Übersetzungen verwalten

### Duplizieren von Canvas-Schritten oder Kampagnen und Übersetzungen

Wenn Sie einen Canvas-Schritt, eine Kampagne oder eine Variante duplizieren, werden die Übersetzungen mit übernommen. Dies gilt auch beim Kopieren zwischen Workspaces, sofern die Locales im Ziel-Workspace definiert sind. Überprüfen und aktualisieren Sie die Übersetzungen entsprechend, wenn Sie Änderungen an Ihrem Canvas oder Ihrer Kampagne vornehmen.

### Übersetzungen in Content-Blöcken speichern

Content-Blöcke unterstützen Mehrsprachigkeit auf die gleiche Weise wie Nachrichten. Beim Erstellen oder Bearbeiten von Content-Blöcken können Sie Inhalte für die Übersetzung markieren, Locales hinzufügen und Übersetzungen per CSV oder über die [Übersetzungs-API]({{site.baseurl}}/api/endpoints/translations/) hochladen.

Gespeicherte Übersetzungen bleiben mit dem Content-Block verknüpft. Wenn der Block zu einer Nachricht hinzugefügt wird, werden seine Übersetzungen automatisch einbezogen.

### Nachrichten von rechts nach links

Beim Ausfüllen der Übersetzungsdatei für Sprachen, die von rechts nach links geschrieben werden (wie Arabisch), umschließen Sie die Übersetzung mit `span`, damit sie korrekt formatiert wird:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### E-Mail-Link-Tracking

In E-Mail-Kampagnen verfolgt Braze Links, indem Tracking-Informationen (Query-Parameter) zu jeder URL hinzugefügt werden. Dieses Verhalten unterstützt sowohl [Link Aliasing]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) als auch [Link-Templating]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template).

Wenn eine URL in Übersetzungs-Tags eingeschlossen ist, kann Braze möglicherweise nicht bestimmen, wo diese Tracking-Informationen hinzugefügt werden sollen. Um sicherzustellen, dass dies korrekt funktioniert, müssen Sie ein Sonderzeichen am Ende der URL einfügen, das angibt, wo das Tracking hinzugefügt werden soll.

URLs verwenden zwei Sonderzeichen, um dies zu steuern:
  - `?` fügt Tracking zu einer URL hinzu, die noch keines hat.
  - `&` fügt zusätzliches Tracking hinzu, wenn bereits ein `?` in der URL vorhanden ist. Eine URL kann nur ein `?` enthalten.

| URL | Enthält&nbsp;`?` | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| Standard-URL | Nein | Fügen Sie `?` nach dem schließenden Übersetzungs-Tag hinzu, wenn die URL noch keines enthält. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| Standard-URL | Ja | Verwenden Sie `&` am Ende der URL (nach dem schließenden Übersetzungs-Tag), wenn sie bereits `?` enthält. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid-generiert | Nein | Verwenden Sie `?` nach den schließenden Übersetzungs-Tags, wenn die generierte URL noch keines enthält. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid-generiert | Ja | Verwenden Sie `&` nach dem schließenden Übersetzungs-Tag, wenn die generierte URL bereits ein `?` enthält. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Spracheinstellungen und Barrierefreiheit

Für HTML-basierte Kanäle (E-Mail, In-App-Nachricht, Banner, Landing-Pages und Content-Cards) fügt Braze ein Barrierefreiheits-Sprachattribut (`lang`) zur gerenderten Nachricht hinzu. Dieses Attribut hilft assistiven Technologien wie Screenreadern, Text korrekt zu interpretieren und auszusprechen.

Ohne dieses Attribut geht ein Screenreader davon aus, dass der Inhalt in der Standardsprache verfasst ist, die die Nutzer:innen bei der Einrichtung auf ihrem Gerät festgelegt haben. Wenn die Nachricht in einer anderen Sprache verfasst ist, kann der Screenreader möglicherweise nicht alles korrekt aussprechen.

#### Barrierefreiheitssprache konfigurieren

Sie können die Barrierefreiheitssprache auf zwei Ebenen festlegen:

##### Nachrichtenebene

Gehen Sie in Ihren Nachrichteneinstellungen zum Abschnitt **Accessibility** und wählen Sie eine Sprache aus dem Dropdown-Menü oder verwenden Sie Liquid, um die Barrierefreiheitssprache dynamisch festzulegen. Dies gilt für alle Inhalte in der Nachricht.

##### Locale-Ebene

Für mehrsprachige Nachrichten legen Sie die Barrierefreiheitssprache für jedes Locale in den **Localization Settings** fest. Wenn neue Nachrichten erstellt werden, ist {% raw %}`{{accessibility_language}}`{% endraw %} standardmäßig im Abschnitt **Accessibility** ausgewählt. Dies ordnet die Barrierefreiheitssprache Ihren Locale-Einstellungen zu.

#### Standards

Die Barrierefreiheitssprache wird dem HTML-Attribut `lang` zugeordnet, einer [WCAG 2.1 Level A-Anforderung](https://dequeuniversity.com/rules/axe/4.2/html-has-lang) (Erfolgskriterium 3.1.1). Für mehrsprachige Inhalte können Sie die Sprache auch für einzelne Content-Blöcke festlegen, indem Sie das `lang`-Attribut direkt in Ihrem HTML verwenden.

## Häufig gestellte Fragen

#### Welche Limits gelten für Übersetzungs-Tags?

Bei der Verwendung von Übersetzungs-Tags gelten die folgenden Limits:

- Jede Nachricht kann bis zu 200 Übersetzungs-Tags enthalten.
- Jeder Standardtext (der Inhalt zwischen Übersetzungs-Tags) kann bis zu 2.000 Zeichen umfassen.
- Die Übersetzungen pro Locale können bis zu 409.600 Bytes (ca. 409,6&nbsp;KB) umfassen.

#### Kann ich eine Änderung am übersetzten Text in einem meiner Locales vornehmen?

Ja. Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um die Änderung zu übernehmen.

### Bietet Braze Übersetzungen an?

Nein. Sie müssen [Ihre eigenen Übersetzungen bereitstellen](#step-4-add-translations), entweder durch Hochladen einer CSV-Datei oder über die Übersetzungs-API.

### Lassen sich Übersetzungs-Tags verschachteln?

Nein.

#### Kann ich vollständige HTML-Nachrichten in einen Übersetzungs-Tag einschließen?

Nein. Als Best Practice sollten Sie nur für Menschen lesbaren Text oder Inhalte einschließen, die lokalisiert werden müssen. Dies hilft, fehlerhafte Formatierungen, Links oder andere Nicht-Text-Elemente zu vermeiden.

Erwägen Sie außerdem, kleinere, semantisch zusammenhängende Textabschnitte einzuschließen, um genaue Übersetzungen zu erstellen und Performance- oder Größenbeschränkungen zu vermeiden.

#### Kann ich eine Änderung am übersetzten Text in einem meiner Locales vornehmen?

Ja. Wenn Sie eine CSV-Datei verwenden, nehmen Sie zunächst die Bearbeitung in der Datei vor und laden Sie sie dann erneut hoch, um die Änderung zu übernehmen. Wenn Sie die [Übersetzungs-API]({{site.baseurl}}/api/endpoints/translations/) verwenden, nutzen Sie die Update-Endpunkte, um Änderungen vorzunehmen.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch?

| Szenario | Validierung in Braze |
| --- | --- |
| Eine Nachricht enthält zwei oder mehr übereinstimmende Übersetzungs-IDs, die auf unterschiedlichen Text verweisen. | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| In einer Übersetzungsdatei fehlen eine oder mehrere Übersetzungs-Tag-IDs. | Diese Übersetzungsdatei wird nicht hochgeladen. |
| Eine Übersetzungsdatei enthält Locales, die in der Nachricht fehlen. | Diese Übersetzungsdatei wird nicht hochgeladen. |
| Übersetzungs-Tags müssen einer Nachricht hinzugefügt werden, bevor das Übersetzungs-Template heruntergeladen wird. | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| Übersetzungs-Tags in Ihrer hochgeladenen Datei fehlen in Ihrer Nachricht. | Zusätzliche Übersetzungen werden nicht in der Nachricht gespeichert. |
| {% raw %}Eine Nachricht enthält einen oder mehrere fehlerhafte Liquid-Tags. Verwenden Sie zum Öffnen `{% translation your_id_here %}` und zum Schließen `{% endtranslation %}`.{% endraw %} | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| Eine Übersetzungsdatei enthält Standardtext, der nicht mit dem Text in der Nachricht übereinstimmt. | Übersetzungen werden hinzugefügt, aber der ursprüngliche Nachrichtentext wird nicht aktualisiert. |
| Ein oder mehrere Locales in einer Nachricht wurden in den Einstellungen gelöscht und existieren nicht mehr. | Bereits hinzugefügte Übersetzungen bleiben in der Nachricht bestehen. Wenn sie aus der Nachricht entfernt werden, gehen die Übersetzungen verloren. |
| Übersetzungs-Tags enthalten vollständige URLs oder Liquid-generierte URLs. | Übersetzungs-Tags mit URLs werden identifiziert, falls Probleme mit fehlerhaften Links oder Link-Tracking auftreten. |
| Übersetzungs-Tags enthalten Query-Parameter. | Übersetzungs-Tags mit Query-Parametern werden identifiziert, falls Probleme mit fehlerhaften Links oder Link-Tracking auftreten. |
| Übersetzungs-Tags enthalten HTML-Attribute oder -Strukturen. | Übersetzungs-Tags mit HTML-Attributen oder -Strukturen werden identifiziert, falls Probleme mit Styles und Formatierung auftreten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }