---
nav_title: Artikel-Empfehlungen
article_title: Artikel-Empfehlungen in Braze
page_order: 10
search_rank: 1
description: "Erfahren Sie alles über Empfehlungssysteme für Artikel in Braze."
---

# Artikel-Empfehlungen

> Verbessern Sie Ihr Empfehlungssystem mit Braze, indem Sie ein Empfehlungssystem erstellen, das Ihren Nutzer:innen Artikel und Inhalte vorschlägt, die sie tatsächlich interessieren. Von der Anpassung von Erlebnissen mit KI bis zum Aufbau eigener Engines mit Liquid oder Connected-Content finden Sie alles, was Sie brauchen, damit jede Empfehlung zählt.

## Voraussetzungen

Bevor Sie Artikel-Empfehlungen in Braze erstellen oder verwenden können, müssen Sie [mindestens einen Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)&#8212;nur Artikel aus diesem Katalog werden den Nutzer:innen empfohlen.

## Typen und Anwendungsfälle

### KI-personalisiert {#ai}

Als Teil des Features [KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/) nutzen KI-personalisierte Empfehlungen Deep Learning, um auf der Grundlage der bisherigen Interessen Ihrer Nutzer:innen vorherzusagen, woran diese als Nächstes am ehesten interessiert sein könnten. Diese Methode bietet ein dynamisches und maßgeschneidertes Empfehlungssystem, das sich dem Nutzerverhalten anpasst.

KI-personalisierte Empfehlungen verwenden die Daten der letzten 6 Monate zu Artikelinteraktionen, wie Käufe oder angepasste Events, um das Empfehlungsmodell zu erstellen. Für Nutzer:innen, die nicht über ausreichende Daten für eine personalisierte Liste verfügen, dienen die beliebtesten Artikel als Fallback, sodass Ihre Nutzer:innen weiterhin relevante Vorschläge erhalten.

Mit den KI-Artikelempfehlungen können Sie die verfügbaren Artikel auch weiter mit 
[Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) filtern. Allerdings können Auswahlen mit Liquid nicht in KI-Empfehlungen verwendet werden. Beachten Sie dies also, wenn Sie Ihre Katalogauswahlen erstellen.

{% alert tip %}
KI-personalisierte Empfehlungen funktionieren am besten bei Hunderten oder Tausenden von Artikeln und typischerweise mindestens 30.000 Nutzer:innen mit Kauf- oder Interaktionsdaten. Dies ist nur ein grober Richtwert und kann variieren. Die anderen Empfehlungstypen können mit weniger Daten arbeiten.
{% endalert %}

#### Anwendungsfälle

Auf der Grundlage der getrackten Interaktionsdaten könnten die Anwendungsfälle für dieses Modell folgende sein:

{% tabs local %}
{% tab Most likely to purchase next %}
Sagen Sie voraus und empfehlen Sie die Artikel, die Nutzer:innen wahrscheinlich als Nächstes kaufen werden, basierend auf Kauf-Events oder angepassten Events im Zusammenhang mit Käufen. Zum Beispiel:

- Eine Reiseseite könnte auf der Grundlage des Browserverlaufs und früherer Buchungen Urlaubspakete, Flüge oder Hotelaufenthalte vorschlagen und so das nächste Reiseziel vorhersehen und die Reiseplanung erleichtern.
- Eine Streaming-Plattform kann die Sehgewohnheiten analysieren, um Sendungen oder Filme zu empfehlen, die Nutzer:innen sich als Nächstes am ehesten ansehen möchten, um sie bei der Stange zu halten und die Abwanderungsrate zu senken.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Ein Verfahren zum Tracking von Käufen, entweder ein Kauf-Objekt oder ein angepasstes Event
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **KI-personalisiert**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie, wie Sie derzeit Kauf-Events tracken, und die entsprechende Event-Eigenschaft.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations/).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Beliebtester Artikel {#most-popular}

Das Empfehlungsmodell „Beliebteste Artikel" enthält Artikel, mit denen Nutzer:innen am meisten interagieren.

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab most popular %}
Animieren Sie Nutzer:innen dazu, beliebte Artikel in Ihrem Katalog basierend auf Käufen zu erkunden. Um sicherzustellen, dass Sie nur relevante Inhalte anzeigen, empfehlen wir, diese mit einer Auswahl zu filtern. Ein Essenslieferdienst könnte zum Beispiel Gerichte oder Restaurants in der Umgebung hervorheben, die am besten bewertet wurden, basierend auf der Beliebtheit der Bestellungen auf der Plattform, und so zum Probieren und Entdecken anregen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Ein Kauf-Objekt oder ein beliebiges angepasstes Event
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Beliebteste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken. Der Essenslieferdienst könnte zum Beispiel eine Auswahl haben, um nach dem Standort des Restaurants oder der Art des Gerichts zu filtern.
5. Wählen Sie Ihre derzeitige Methode zum Tracking von Events und die entsprechende Event-Eigenschaft aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab most liked %}
Ermuntern Sie die Nutzer:innen, Artikel zu entdecken, die ihnen kürzlich gefallen haben, oder Artikel, die sehr beliebt sind, basierend auf einem angepassten Event für Likes. Eine Musik-Streaming-App könnte zum Beispiel personalisierte Wiedergabelisten erstellen oder neue Alben vorschlagen, die auf den Genres oder Künstlern basieren, die Nutzer:innen in der Vergangenheit mochten, und so das Engagement und die Verweildauer in der App erhöhen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Likes
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Angepasstes Event** und wählen Sie Ihr angepasstes Event für Likes aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab most viewed %}
Heben Sie Artikel hervor, die in Ihrer Nutzerbasis durch Aufrufe Aufmerksamkeit erregt haben, um Engagement oder Käufe anzuregen. Eine Immobilien-Website könnte zum Beispiel die am meisten angesehenen Angebote im Suchbereich anzeigen, um Objekte hervorzuheben, die viel Aufmerksamkeit auf sich ziehen und möglicherweise auf gute Angebote oder begehrte Standorte hinweisen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Aufrufe
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Beliebteste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Angepasstes Event** und wählen Sie Ihr angepasstes Event für Aufrufe aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
Präsentieren Sie Artikel, die von vielen anderen Käufer:innen in den Warenkorb gelegt wurden, und geben Sie den Nutzer:innen einen Einblick in die aktuellen Trends in Ihrem Angebot.

Ein Modehändler könnte z. B. Kleidung und Accessoires bewerben, die gerade im Trend liegen, basierend auf den beliebten Zugängen zu den Warenkörben anderer Kund:innen. Sie können dann einen dynamischen „Jetzt im Trend"-Bereich auf ihrer Startseite und in ihrer mobilen App erstellen, der in Realtime aktualisiert wird, um Käufer:innen zum Kauf zu animieren, bevor die Artikel ausverkauft sind.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für „In den Warenkorb gelegt"
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Beliebteste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Angepasstes Event** und wählen Sie aus der Liste Ihr angepasstes Event für „In den Warenkorb gelegt" aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Neuester Artikel {#most-recent}

Das Empfehlungsmodell „Neueste Artikel" enthält Artikel, mit denen Nutzer:innen zuletzt interagiert haben. Nutzen Sie dieses Modell, um die Abwanderung zu verringern, indem Sie passive Nutzer:innen ermutigen, sich erneut mit relevanten Inhalten zu beschäftigen.

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab Recently clicked %}
Ermuntern Sie Nutzer:innen dazu, Artikel, auf die sie kürzlich geklickt haben, erneut aufzurufen, basierend auf einem angepassten Event für Klicks. Ein Online-Modehändler könnte zum Beispiel eine Empfehlung erstellen, um Folge-E-Mails oder Push-Benachrichtigungen mit Kleidungsstücken zu versenden, für die sich Nutzer:innen durch Anklicken interessiert haben, und sie so zu einem erneuten Besuch des Artikels und einem Kauf zu ermutigen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Klicks
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Angepasstes Event** und wählen Sie Ihr angepasstes Event für Klicks aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
Ermuntern Sie die Nutzer:innen, Artikel zu entdecken, die ihnen kürzlich gefallen haben, oder Artikel, die sehr beliebt sind, basierend auf einem angepassten Event für Likes. Eine Musik-Streaming-App könnte zum Beispiel personalisierte Wiedergabelisten erstellen oder neue Alben vorschlagen, die auf den Genres oder Künstlern basieren, die Nutzer:innen in der Vergangenheit mochten, und so das Engagement und die Verweildauer in der App erhöhen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Likes
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Angepasstes Event** und wählen Sie Ihr angepasstes Event für Likes aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
Bewerben Sie Artikel, mit denen Nutzer:innen kürzlich interagiert haben, z. B. durch Aufrufe, Klicks oder Käufe. Auf diese Weise bleiben Ihre Empfehlungen frisch und auf die aktuellen Interessen abgestimmt. Zum Beispiel:

- **Bildung:** Eine Online-Bildungsplattform könnte Nutzer:innen, die sich kürzlich ein Lernvideo angesehen, sich aber noch nicht für einen Kurs angemeldet haben, dazu ermutigen, sich ähnliche Kurse oder Themen anzusehen, um sie bei der Stange zu halten und zum Lernen zu motivieren.
- **Fitness:** Eine Fitness-App kann Workouts oder Herausforderungen vorschlagen, die denen ähneln, die Nutzer:innen kürzlich absolviert oder mit denen sie interagiert haben. So bleibt die Trainingsroutine abwechslungsreich und motivierend.
- **Einzelhändler für Heimwerkerbedarf:** Nachdem Kund:innen ein Elektrowerkzeug gekauft haben, kann ein Baumarkt auf der Grundlage des letzten Kaufs entsprechendes Zubehör oder Sicherheitsausrüstung empfehlen, um das Erlebnis und die Sicherheit zu verbessern.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Ein Kauf-Objekt oder ein beliebiges angepasstes Event für eine Interaktion
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Angepasstes Event** und wählen Sie Ihr angepasstes Event für Klicks aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Recently added %}
Erinnern Sie Nutzer:innen an ihr Interesse an Artikeln, die sie kürzlich in ihren Warenkorb gelegt, aber noch nicht gekauft haben. Ein Online-Händler könnte zum Beispiel Erinnerungen versenden oder zeitlich begrenzte Rabatte auf die Artikel im Warenkorb anbieten, um Nutzer:innen zu ermutigen, ihre Einkäufe abzuschließen, bevor die Angebote ablaufen.
{% details Requirements %}

- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für „In den Warenkorb gelegt"
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Angepasstes Event** und wählen Sie aus der Liste Ihr angepasstes Event für „In den Warenkorb gelegt" aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Trending-Artikel {#trending}

Das Empfehlungsmodell „Trending" präsentiert Artikel, die in den letzten Nutzerinteraktionen die positivste Dynamik gezeigt haben. Wir berechnen dies anhand einer gewichteten Analyse des Verlaufs der letzten etwa 10 Wochen, wobei die letzten etwa 2 Wochen am stärksten gewichtet werden. Um zu verhindern, dass kleine Schwankungen die Qualität der Empfehlungen beeinträchtigen, wenden wir einen Aktivitätsschwellenwert und statistische Glättungsverfahren an.

Im Gegensatz zum Modell „Beliebteste Artikel", das Artikel mit konstant hoher Interaktion enthält, enthält dieses Modell Artikel, die einen Anstieg der Interaktionen verzeichnet haben. Sie können es verwenden, um Produkte zu empfehlen, die im Kommen sind und derzeit verstärkt Aufmerksamkeit erhalten.

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab Trending purchased %}
Heben Sie Artikel hervor, die Ihre Nutzer:innen in letzter Zeit besonders häufig gekauft haben. Ein E-Commerce-Unternehmen könnte zum Beispiel saisonale Artikel empfehlen, die Nutzer:innen bei ihren Vorbereitungen für die nächste Saison auf Vorrat kaufen. 

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Ein Verfahren zum Tracking von Käufen (entweder ein Kauf-Objekt oder ein angepasstes Event)
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/ai_item_recommendations/).
2. Setzen Sie den **Typ** auf **Trending**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie entweder ein Kauf-Event oder ein angepasstes Event, das Käufe trackt, zusammen mit der entsprechenden Eigenschaft.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
Heben Sie Artikel hervor, die Ihren Nutzer:innen in letzter Zeit besonders häufig gefallen haben. Eine Musik-App könnte zum Beispiel aufstrebende Künstler vorstellen, die in letzter Zeit einen starken Anstieg der Nutzer-Likes verzeichnet haben.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event zum Tracking von Likes
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/ai_item_recommendations/).
2. Setzen Sie den **Typ** auf **Trending**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie Ihr angepasstes Event zum Tracking von Likes zusammen mit der entsprechenden Eigenschaft.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung im Messaging.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Auf Auswahlen basierend {#selections-based}

[Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) sind bestimmte Gruppen von Katalogdaten. Wenn Sie eine Auswahl verwenden, richten Sie im Wesentlichen angepasste Filter ein, die auf bestimmten Spalten in Ihrem Katalog basieren. Dies könnte Filter für Marke, Größe, Standort, Hinzufügedatum und mehr beinhalten. Damit haben Sie die Kontrolle über Ihre Empfehlungen, da Sie Kriterien definieren können, die Artikel erfüllen müssen, um Nutzer:innen angezeigt zu werden.

Bei den drei vorangegangenen Typen geht es darum, ein Empfehlungsmodell in Braze einzurichten und zu trainieren. Sie können zwar auch in diesen Modellen Auswahlen verwenden, aber Sie können einige Empfehlungsanwendungen auch nur mit Katalogauswahlen und Liquid-Personalisierung umsetzen.

{% alert note %}
Bei Verwendung von Auswahlen werden das Sortierfeld und etwaige Einschränkungen nicht für die KI-Artikelempfehlungen berücksichtigt. Das bedeutet: Wenn Sie eine Auswahl mit einem bestimmten Sortierfeld erstellen und die Anzahl der zurückgegebenen Artikel begrenzen, werden diese Einschränkungen bei der Verarbeitung der KI-Artikelempfehlungen nicht angewendet.
{% endalert %}

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab New items %}
Dieses Szenario basiert nicht direkt auf Nutzeraktionen, sondern vielmehr auf Katalogdaten. Sie können nach neuen Artikeln auf der Grundlage des Datums ihrer Aufnahme in den Katalog filtern und diese durch gezielte Kampagnen oder Canvase bewerben, ohne dass Sie ein Empfehlungsmodell trainieren müssen.

Eine E-Commerce-Plattform für Technik könnte zum Beispiel Technikbegeisterte über die neuesten Gadgets oder anstehende Vorbestellungen informieren und dabei Filter verwenden, um Artikel zu finden, die kürzlich in den Katalog aufgenommen wurden.

{% details Requirements %}
- Katalog der relevanten Artikel mit einem Feld für das Hinzufügedatum
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine Auswahl auf der Grundlage Ihres Katalogs. Vergewissern Sie sich, dass Ihr Katalog ein Zeitfeld enthält (ein Feld, dessen **Datentyp** auf **Zeit** eingestellt ist), das dem Datum entspricht, an dem der Artikel hinzugefügt wurde.
2. (Optional) Fügen Sie ggf. Filter hinzu.
3. Stellen Sie sicher, dass **Zufällige Sortierung** ausgeschaltet ist.
4. Wählen Sie unter **Sortierfeld** Ihr Feld für das Hinzufügedatum aus.
5. Setzen Sie die **Sortierreihenfolge** auf absteigend.
6. [Verwenden Sie die Auswahl im Messaging]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Random items %}
Für ein vielfältiges Nutzererlebnis kann die Empfehlung von Zufallsartikeln für Abwechslung sorgen und möglicherweise das Interesse an weniger besuchten Katalogbereichen wecken. Diese Methode erfordert keine bestimmten Modelle oder Events, sondern verwendet eine Katalogauswahl, um sicherzustellen, dass die Artikel zufällig angezeigt werden.

Eine Online-Buchhandlung könnte zum Beispiel eine „Überrasch mich"-Funktion anbieten, die auf der Grundlage früherer Einkäufe oder Surfgewohnheiten ein zufällig ausgewähltes Buch empfiehlt und so dazu anregt, auch außerhalb des gewohnten Lesegenres zu stöbern.

{% details Requirements %}
- Katalog der relevanten Artikel
- Auswahl mit aktivierter **Zufälliger Sortierreihenfolge**
{% enddetails %}

{% details Setting it up %}
1. [Erstellen Sie eine Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection) auf der Grundlage Ihres Katalogs.
2. (Optional) Fügen Sie ggf. Filter hinzu.
3. Aktivieren Sie **Zufällige Sortierung**.
4. [Verwenden Sie die Auswahl im Messaging]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Regelbasiert {#rules-based}

Ein [regelbasiertes Empfehlungssystem]({{site.baseurl}}/rules_based_recommendations/) verwendet Nutzerdaten und Produktinformationen, um relevante Artikel in Nachrichten vorzuschlagen. Es verwendet Liquid und entweder Braze-Kataloge oder Connected-Content, um Inhalte auf der Grundlage von Nutzerverhalten und Attributen dynamisch zu personalisieren.

Regelbasierte Empfehlungen basieren auf einer festen Logik, die Sie manuell einstellen müssen. Das bedeutet, dass sich Ihre Empfehlungen nicht an den individuellen Kaufverlauf und die Vorlieben von Nutzer:innen anpassen, es sei denn, Sie aktualisieren die Logik. Daher eignet sich diese Methode am besten für Empfehlungen, die keine häufigen Updates erfordern.

#### Anwendungsfälle

Auf der Grundlage der getrackten Interaktionsdaten könnten die Anwendungsfälle für dieses Modell folgende sein:

- **Erinnerungen zur Nachbestellung:** Erinnerungen zur Nachbestellung von Artikeln mit einem vorhersehbaren Nutzungszyklus, wie z. B. monatliche Vitamine oder wöchentliche Lebensmittel, basierend auf dem letzten Kaufdatum.
- **Erstkäufer:innen:** Empfehlen Sie Erstkäufer:innen Starterkits oder Einführungsangebote, um sie zu einem zweiten Kauf zu bewegen.
Kundenbindungs-Programme: Heben Sie Produkte hervor, mit denen Kund:innen ihre Treuepunkte oder Rewards auf der Grundlage ihres aktuellen Punktestandes maximieren können.
- **Bildungsinhalte:** Schlagen Sie neue Kurse oder Inhalte vor, die auf den Themen der bereits konsumierten oder gekauften Materialien basieren.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Häufig gestellte Fragen {#faq}

### Wie kommt es dazu, dass „Beliebteste" Artikel mit den Empfehlungen anderer Modelle vermischt werden?

Wenn das Empfehlungssystem eine Liste für Sie zusammenstellt, priorisiert es zunächst die personalisierte Auswahl auf der Grundlage des von Ihnen gewählten Modells, also z. B. „Neueste" oder „KI-personalisiert". Wenn dieses Modell aus irgendeinem Grund nicht die komplette Liste mit 30 Empfehlungen füllen kann, werden einige Ihrer bei allen Nutzer:innen beliebtesten Artikel hinzugefügt, um sicherzustellen, dass jede:r Nutzer:in immer einen vollständigen Satz an Empfehlungen hat.

Dies geschieht unter einigen besonderen Bedingungen:

- Das Modell findet weniger als 30 Artikel, die Ihren Kriterien entsprechen.
- Die entsprechenden Artikel sind nicht mehr verfügbar oder auf Lager.
- Die Artikel entsprechen nicht den aktuellen Auswahlkriterien, z. B. weil sich der Bestand oder die Präferenzen geändert haben.

Bitte beachten Sie, dass Empfehlungen unabhängig voneinander funktionieren und keine Kenntnis darüber haben, was die anderen Modelle empfehlen. Das bedeutet, dass jeder Abschnitt doppelte Artikel enthalten kann, die bereits in anderen KI-Empfehlungsabschnitten derselben E-Mail angezeigt werden.

### Wie verhindere ich doppelte Artikel in mehreren Empfehlungsabschnitten?

Da jede Empfehlung unabhängig funktioniert, kann derselbe Artikel in mehr als einem Abschnitt derselben Nachricht erscheinen. Um Duplikate zu entfernen, verwenden Sie Liquid, um zu verfolgen, welche Artikel-IDs Sie bereits angezeigt haben, und überspringen Sie diese in nachfolgenden Abschnitten.

### Werden bestehende Empfehlungen nach dem Upgrade auf Item Recommendations Pro wöchentlich trainiert?

Ja, aber erst nach ihrem nächsten geplanten Update. Bestehende Empfehlungen schalten beim Upgrade auf Item Recommendations Pro nicht sofort auf wöchentliches Training und tägliche Prognosen um. Sie übernehmen den neuen Zeitplan jedoch automatisch bei ihrem nächsten Trainingszyklus. Wenn eine Empfehlung zum Beispiel zuletzt am 1. Februar trainiert wurde und so eingestellt ist, dass sie alle 30 Tage neu trainiert wird, übernimmt sie den neuen wöchentlichen Zeitplan nach dem nächsten Update am 2. März.

### Wie kann ich alle Empfehlungen, die mehrere Tage gültig sind, gleichzeitig ablaufen lassen?

Wenn Sie alle mehrtägigen Empfehlungen zu einem bestimmten Datum ablaufen lassen möchten (sodass alle aktiven Empfehlungen gleichzeitig neue Prognosen erhalten), wenden Sie sich bitte an den Braze-Support oder Ihren Customer-Success-Manager. Die BrazeAI-Expert:innen führen diesen Vorgang manuell durch, um eine optimale Performance des Modells zu gewährleisten.