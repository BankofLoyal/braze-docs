---
nav_title: Banner erstellen
article_title: Banner erstellen
page_order: 1
description: "Dieser Referenzartikel behandelt die Erstellung, Gestaltung, Konfiguration und den Versand von Bannern mithilfe von Braze-Kampagnen und Canvases."
tool:
  - Campaigns
channel:
  - banners
---

# Banner erstellen

> Erfahren Sie, wie Sie Banner erstellen, wenn Sie Kampagnen und Canvase in Braze erstellen. Weitere allgemeine Informationen finden Sie unter [Über Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Voraussetzungen

Bevor Sie Ihr Banner starten können, muss Ihr Entwicklungsteam [Platzierungen in Ihrer App oder Website einrichten]({{site.baseurl}}/developer_guide/banners/creating_placements/). Sie können Ihre Banner-Kampagne in der Zwischenzeit weiterhin entwerfen, jedoch können Sie die Kampagne erst starten, wenn die Platzierungen konfiguriert sind.

## Banner-Nachricht erstellen

{% multi_lang_include banners/creating_placements.md section="user" %}

### 2. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich besser für einzelne, zielgerichtete Messaging-Kampagnen, während Canvase besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **Banner**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu. Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den Berichts-Builder verwenden, können Sie nach den entsprechenden Tags filtern.
5. Wählen Sie die Platzierung aus, die Sie zuvor erstellt haben, um sie mit Ihrer Kampagne zu verknüpfen.
6. Fügen Sie bei Bedarf Varianten hinzu. Sie können für jede Variante einen anderen Nachrichtentyp und ein anderes Layout wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Wählen Sie ein Startdatum und eine Startzeit für Ihre Banner-Kampagne. Standardmäßig sind Banner unbegrenzt gültig. Sie können dies ändern, indem Sie **Endzeit** auswählen und ein Enddatum und eine Endzeit angeben.

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus dem Dropdown-Menü **Variante hinzufügen** die Option **Aus Variante kopieren** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie einen Nachrichtenschritt im Canvas-Builder hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Banner** als Ihren Messaging-Kanal.
4. Wählen Sie eine Platzierung für das Banner aus.
5. Legen Sie die Priorität für das Banner fest. Die [Bannerpriorität]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dieselbe Platzierung haben.
6. Legen Sie ein Ablaufdatum für das Banner fest. Dies kann nach einer bestimmten Zeitspanne, nachdem der Schritt verfügbar ist, oder zu einem bestimmten Datum und einer bestimmten Uhrzeit erfolgen.

{% endtab %}
{% endtabs %}

### 3. Schritt: Banner gestalten {#compose-a-banner}

Um Ihr Banner zu gestalten, haben Sie folgende Möglichkeiten:

- Mit einem leeren Template beginnen
- Ein Braze-Banner-Template verwenden
- Ein gespeichertes Banner-Template auswählen

![Option zur Auswahl eines leeren Banners oder eines Templates.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Schritt 3.1: Das Banner stylen

Sie können Blöcke und Zeilen per Drag-and-Drop in den Canvas-Bereich ziehen, um mit der Erstellung Ihrer Nachricht zu beginnen.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Um die Hintergrundeigenschaften Ihrer Nachricht, die Rahmeneinstellungen und mehr anzupassen, wählen Sie **Stile**. Wenn Sie nur den Stil für einen bestimmten Block oder eine bestimmte Zeile anpassen möchten, wählen Sie das Element aus, um Änderungen vorzunehmen.

![Stil-Panel des Banner-Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Schritt 3.2: Klickverhalten definieren (optional)

Wenn Nutzer:innen auf einen Link im Banner klicken, können Sie sie tiefer in Ihre App navigieren oder auf eine andere Webseite weiterleiten. Darüber hinaus können Sie [ein angepasstes Attribut oder Event protokollieren]({{site.baseurl}}/developer_guide/analytics/), wodurch das Profil der Nutzer:innen mit angepassten Daten aktualisiert wird, wenn sie auf das Banner klicken.

{% alert important %}
{::nomarkdown}
Das Klickverhalten kann überschrieben werden, wenn ein bestimmtes Element (z. B. ein Button, ein Link oder ein Bild des Banners) ein eigenes Klickverhalten hat. Nehmen wir zum Beispiel folgendes Klickverhalten an:<br><ul><li>Ein Banner hat ein Klickverhalten, das auf die Homepage einer Website weiterleitet.</li><li>Ein Bild im Banner hat ein Klickverhalten, das auf die Produktseite einer Website weiterleitet.</li></ul>Wenn Nutzer:innen auf das Bild klicken, werden sie zur Produktseite weitergeleitet. Ein Klick auf den umgebenden Bereich des Banners leitet sie jedoch zur Homepage weiter.
{:/}
{% endalert %}

#### Schritt 3.3: Angepasste Eigenschaften hinzufügen (optional) {#custom-properties}

Sie können einem Banner angepasste Eigenschaften hinzufügen, um strukturierte Metadaten wie Strings oder JSON-Objekte anzuhängen. Diese Eigenschaften haben keinen Einfluss auf die Darstellung des Banners, können jedoch [über das Braze SDK abgerufen]({{site.baseurl}}/developer_guide/banners/placements/) werden, um das Verhalten oder das Erscheinungsbild Ihrer App anzupassen. Beispielsweise könnten Sie:

- Metadaten für Ihre Analytics oder Integrationen von Drittanbietern senden.
- Metadaten wie einen `timestamp` oder ein JSON-Objekt verwenden, um bedingte Logik zu triggern.
- Das Verhalten eines Banners basierend auf enthaltenen Metadaten wie `ratio` oder `format` steuern.

Um eine angepasste Eigenschaft hinzuzufügen, wählen Sie **Einstellungen** > **Eigenschaften** > **Eigenschaft hinzufügen**.

![Die Eigenschaftenseite mit der Option zum Hinzufügen der ersten angepassten Eigenschaft zu einer Banner-Kampagne.]({% image_buster /assets/img/banners/add_property.png %})

Füllen Sie für jede Eigenschaft, die Sie hinzufügen möchten, die folgenden Angaben aus:

| Feld | Beschreibung | Beispiel |
|-------|-------------|---------|
| Eigenschaftstyp | Der Datentyp für die Eigenschaft. Unterstützte Typen umfassen String, Boolescher Wert, Zahl, Zeitstempel, Bild-URL und JSON-Objekt. | String |
| Eigenschaftsschlüssel | Der eindeutige Bezeichner für die Eigenschaft. Dieser Schlüssel wird im SDK verwendet, um auf die Eigenschaft zuzugreifen. | `color` |
| Wert | Der der Eigenschaft zugewiesene Wert. Muss mit dem ausgewählten Eigenschaftstyp übereinstimmen. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Wenn Sie fertig sind, wählen Sie **Fertig**.

![Die Eigenschaftenseite mit einer String-Eigenschaft mit dem Schlüssel „color" und dem Wert „#FF0000".]({% image_buster /assets/img/banners/example_property.png %})

### 4. Schritt: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

#### Banner-Priorität festlegen (optional)

Die [Bannerpriorität]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) bestimmt die Reihenfolge, in der Banner angezeigt werden, wenn sie dieselbe Platzierung haben. Um die Priorität manuell festzulegen:

1. Wählen Sie **Exakte Priorität festlegen**.
2. Ziehen Sie die Kampagnen per Drag-and-Drop, um sie in der richtigen Prioritätsreihenfolge anzuordnen.
3. Wählen Sie **Sortierung anwenden**.

{% alert tip %}
Wenn Sie mehrere Banner-Kampagnen mit derselben Platzierungs-ID haben, empfehlen wir, den Drag-and-Drop-Prioritätssortierer zu verwenden, um die genaue Priorität festzulegen.
{% endalert %}

#### Zielgruppe auswählen

1. Wählen Sie unter **Zielgruppen** Segmente oder Filter aus, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segmentgröße. Die genaue Segmentzugehörigkeit wird vor dem Versand der Nachricht berechnet.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. Verfolgen Sie unter **Konversionen zuweisen**, wie oft Nutzer:innen bestimmte Aktionen ausführen, nachdem sie eine Kampagne erhalten haben, indem Sie Konversions-Events mit einem Zeitfenster von bis zu 30 Tagen definieren, um die Aktion als Konversion zu zählen.

{% multi_lang_include target_audiences.md %}

#### Konversions-Events auswählen

Mit Braze können Sie [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) nachverfolgen – also wie oft Nutzer:innen bestimmte Aktionen ausführen, nachdem sie eine Kampagne erhalten haben. Sie können einen Zeitraum von bis zu 30 Tagen festlegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte Ihrer Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von [multivariaten Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) und [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) und mehr finden Sie im Schritt [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

### 5. Schritt: Nachricht testen (optional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### 6. Schritt: Überprüfen und bereitstellen

Nachdem Sie Ihre Kampagne oder Ihr Canvas fertiggestellt haben, überprüfen Sie die Details, [testen Sie es]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) und versenden Sie es, sobald Sie bereit sind.