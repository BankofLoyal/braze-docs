---
nav_title: Lokalisierungseinstellungen
article_title: Lokalisierungseinstellungen
alias: "/multi_language_support/"
page_order: 5.5
description: "Dieser Artikel bietet eine Übersicht über die mehrsprachigen Einstellungen im Braze-Dashboard und darüber, wie Sie Lokalisierungen in Ihrem Messaging verwenden können."
---

# Lokalisierungseinstellungen

> Das Mehrsprachen-Feature ermöglicht es Ihnen, [Übersetzungs-Tags]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) zu verwenden, um Nutzer:innen in verschiedenen Sprachen und an verschiedenen Standorten mit einer einzigen Nachricht anzusprechen.

## Voraussetzungen

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## Gebietsschema hinzufügen

1. Gehen Sie zu **Einstellungen** > **Lokalisierungseinstellungen**.
2. Wählen Sie **Gebietsschema hinzufügen** und dann **Standardgebietsschema** oder **Angepasste Attribute**.

![Das Dropdown-Menü „Gebietsschema hinzufügen" mit Optionen zur Auswahl des Standard-Gebietsschemas oder angepasster Attribute.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}

{: start="3"}
3. Geben Sie einen Namen für das Gebietsschema ein.
4. [Wählen Sie eine Sprache für die Barrierefreiheit aus]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/#language-settings-and-accessibility). Diese Einstellung ermöglicht es assistiven Technologien wie Screenreadern, Text korrekt auszusprechen.
5. Wählen Sie die entsprechenden Nutzerattribute für die von Ihnen gewählte Gebietsschema-Option aus. Beim Einrichten eines Gebietsschemas können Sie entweder Sprachen aus den Standard-Nutzerattributen oder aus angepassten Attributen auswählen. Sie können nicht aus beiden wählen.

{% tabs %}
{% tab Default locale %}

Verwenden Sie für **Standardgebietsschema** die Dropdown-Listen, um die hinzuzufügende Sprache und optional das Land, das mit der Sprache verknüpft werden soll, auszuwählen.

![Ein Fenster mit dem Titel „Gebietsschema hinzufügen – Standard-Sprache und Land" zur Angabe der Sprache und des Landes.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

Für **Angepasste Attribute** wählen Sie aus der Dropdown-Liste das entsprechende angepasste Attribut aus und geben in das Textfeld den Wert ein.

![Ein Fenster mit dem Titel „Gebietsschema hinzufügen – Angepasste Attribute", in dem das angepasste Attribut und der Wert angegeben werden können.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Wählen Sie **Gebietsschema hinzufügen**.

Wie Sie diese Gebietsschemata in Ihren Nachrichten verwenden können, erfahren Sie unter [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

## Überlegungen

- Sie können bis zu zwei angepasste Attribute in einem einzigen Gebietsschema oder bis zu zwei Standard-Nutzerattributsprachen auswählen. In beiden Fällen ist das zweite Attribut optional.
- Wenn Sie Änderungen an den übersetzten Werten in der CSV-Datei vornehmen, vermeiden Sie es, die Standardwerte in der Datei zu ändern.
- Der Lokalisierungsschlüssel in Ihrer hochgeladenen Datei muss mit dem Schlüssel in Ihren Mehrspracheneinstellungen übereinstimmen.

### Support und Priorisierung

- Wenn ein:e Nutzer:in sowohl mit einem Gebietsschema auf Basis angepasster Attribute als auch mit einem auf Basis von Standard-Nutzerattributen übereinstimmt, wird das Gebietsschema mit angepassten Attributen priorisiert.
- Angepasste Attribute unterstützen Text-Werte (String) mit exakter Übereinstimmung.
- Wenn ein angepasstes Attribut gelöscht oder sein Typ geändert wird, kann der/die Nutzer:in nicht mehr in dieses Gebietsschema fallen und wird entweder in der Prioritätsliste der Gebietsschemata nach unten rutschen oder Standard-Marketing-Übersetzungen erhalten.
- Wenn ein Gebietsschema ungültig ist (das angepasste Attribut hat sich geändert oder wurde gelöscht), wird der Fehler auf der Seite **Mehrsprachiger Support** angezeigt.

## Häufig gestellte Fragen

#### Wie viele Gebietsschemata kann ich hinzufügen?

Sie können bis zu 200 Gebietsschemata hinzufügen.

#### Wo werden die Übersetzungsdateien in Braze gespeichert?

Die Übersetzungsdateien werden auf Kampagnen-Ebene gespeichert, d. h. für jede Nachrichtenvariante müssen Übersetzungen hochgeladen werden. Übersetzungen können auch in Content-Blöcken gespeichert werden. Wenn der Block einer Nachricht hinzugefügt wird, werden seine Übersetzungen automatisch einbezogen.

#### Muss der Name des Gebietsschemas einem bestimmten Muster oder Format folgen?

Nein. Sie können Ihre bevorzugte Benennungskonvention verwenden. Der Name des Gebietsschemas wird bei der Auswahl des Gebietsschemas im Editor verwendet und erscheint in den Überschriften der Datei, die Sie mit den Übersetzungs-IDs herunterladen.