---
nav_title: Uninstall-Tracking
article_title: Uninstall-Tracking
page_order: 6
page_type: reference
description: "Dieser Referenzartikel behandelt die Implementierung von Uninstall-Tracking für Statistiken auf Kampagnen- und App-Ebene."
tool: Reports

---

# Uninstall-Tracking

> Dieser Artikel zeigt Ihnen, wie Sie die Gesamtheit der App-Deinstallationen im Laufe der Zeit betrachten können, um Trends und Anomalien zu erkennen, und wie Sie Deinstallationen auf Kampagnenebene verfolgen können, um festzustellen, ob eine bestimmte Kampagne App-Installationen fördert oder verhindert.

Uninstall-Tracking in Braze liefert die folgenden Details:

1. Tägliche Deinstallationsstatistiken auf App-Ebene in einem Zeitreihendiagramm auf der **Startseite**.
2. Deinstallationsstatistiken auf Kampagnenebene in einem Zeitreihendiagramm auf der Seite **Kampagnendetails** für eine bestimmte Kampagne. Diese Statistik gibt die Anzahl der Kampagnenempfänger:innen an, die jeden Tag deinstallieren.

{% alert note %} 
Sie müssen das Uninstall-Tracking in Ihrem Braze-Dashboard aktivieren. Dieses Feature ist für Apps auf iOS, Android und Fire OS verfügbar. 
{% endalert %}

## Funktionsweise

Braze sammelt automatisch grundlegende Deinstallationsinformationen aus Ihren regulären Push-Kampagnen. Da die Häufigkeit, mit der verschiedene Nutzer:innen Push-Kampagnen erhalten, jedoch variieren kann, bieten wir Uninstall-Tracking an, um eine genauere Momentaufnahme der Deinstallationsaktivitäten Ihrer Nutzer:innen zu erhalten.

Wenn Braze eine Deinstallation erkennt, wird der oder die Nutzer:in als deinstalliert markiert. Wenn Sie den Filter **Hat nicht deinstalliert** in einer Kampagne verwenden, werden diese markierten Nutzer:innen ausgeschlossen. Wenn ein:e Nutzer:in die App erneut installiert, sie aber nicht öffnet, bleibt die Deinstallationsmarkierung im Profil bestehen. Die Markierung wird erst entfernt, wenn der oder die Nutzer:in eine neue Sitzung in der neu installierten App startet. Das bedeutet, dass ein:e Nutzer:in, der oder die die App erneut installiert, aber nie öffnet, weiterhin als deinstalliert angezeigt wird.

Weitere Informationen zur Verwendung des Uninstall-Trackings finden Sie in unserem Blogbeitrag [Uninstall-Tracking: Ein Blick auf die Stärken und Grenzen der Branche](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Uninstall-Tracking aktivieren

Sie können das Uninstall-Tracking auf der Seite **App-Einstellungen** unter **Einstellungen** für jede App aktivieren, die Sie verfolgen möchten.

Wenn Sie das Uninstall-Tracking für eine App aktivieren, sendet Braze jede Nacht eine Push-Nachricht im Hintergrund an Nutzer:innen, die innerhalb der letzten 24 Stunden keine Sitzung aufgezeichnet oder keine Push-Nachricht erhalten haben.

### Konfiguration

Um das Uninstall-Tracking für Ihre iOS-Anwendung zu konfigurieren, verwenden Sie eine [Utility-Methode]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Verwenden Sie für Ihre Android-Anwendung [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Wenn Braze eine Deinstallation feststellt – sei es durch Uninstall-Tracking oder durch die normale Zustellung von Push-Kampagnen – erfassen wir den bestmöglich geschätzten Zeitpunkt der Deinstallation beim Nutzer oder bei der Nutzerin. Dieser Zeitpunkt wird im Nutzerprofil als Standardattribut gespeichert und kann zur Definition eines Segments von Nutzer:innen für Rückgewinnungskampagnen verwendet werden.

## Segmente nach Deinstallationen filtern

Der Filter **Deinstalliert** wählt Nutzer:innen aus, die Ihre App innerhalb eines bestimmten Zeitraums deinstalliert haben. Da es schwierig ist, den genauen Zeitpunkt einer Deinstallation zu bestimmen, empfehlen wir, bei Deinstallationsfiltern breitere Zeitspannen zu verwenden, um sicherzustellen, dass alle Nutzer:innen, die deinstallieren, irgendwann in das Segment fallen.

Tägliche Statistiken über Deinstallationen finden Sie auf der **Startseite**. 

![Deinstallations-Segment.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

Das Diagramm kann nach App und Segment aufgeschlüsselt werden, ähnlich wie andere Statistiken, die Braze bereitstellt. Wählen Sie im Abschnitt **Performance-Übersicht** Ihren Datumsbereich und, falls gewünscht, eine App aus. Scrollen Sie dann zum Diagramm **Performance im Zeitverlauf** und gehen Sie wie folgt vor:

1. Wählen Sie in der Dropdown-Liste **Statistik für** die Option **Deinstallationen** aus.
2. Wählen Sie in der Dropdown-Liste **Aufschlüsselung** die Option **Nach Segment** aus.
3. Wählen Sie in der Dropdown-Liste **Aufschlüsselungswerte** die Segmente aus, die in das Diagramm aufgenommen werden sollen.

{% alert note %}
Apps ohne aktiviertes Uninstall-Tracking melden Deinstallationen nur von einer Teilmenge ihrer Nutzer:innen (denjenigen, die mit Push-Benachrichtigungen angesprochen wurden), sodass die tägliche Gesamtzahl der Deinstallationen höher sein kann als angezeigt.
{% endalert %}

## Uninstall-Tracking für Kampagnen

Das Uninstall-Tracking für Kampagnen zeigt die Anzahl der Nutzer:innen, die eine bestimmte Kampagne erhalten und anschließend Ihre App innerhalb des ausgewählten Zeitraums deinstalliert haben. Dieses Tool gibt Insights darüber, wie Kampagnen unbeabsichtigtes negatives Nutzerverhalten fördern können, und hilft dabei, die Gesamtwirksamkeit von Kampagnen zu messen.

Die Deinstallationsstatistiken für Kampagnen befinden sich auf der Seite **Campaign Analytics** der jeweiligen Kampagne. Bei Multichannel- und multivariaten Kampagnen können die Deinstallationen nach Kanal bzw. Variante aufgeschlüsselt werden.

![Deinstallation auf Kampagnenebene.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Funktionsweise

Braze verfolgt Deinstallationen, indem es beobachtet, wann Push-Nachrichten, die an die Geräte der Nutzer:innen gesendet werden, entweder von Firebase Cloud Messaging (FCM) oder vom Apple Push Notification Service (APNs) ein Signal zurückgeben, dass die App nicht mehr installiert ist. Wenn Sie das globale Uninstall-Tracking für eine App aktivieren, sendet Braze täglich eine stille Push-Nachricht an die Nutzer:innen, um festzustellen, ob sie die App deinstalliert haben. Braze sendet diesen „stillen" Push an alle Nutzer:innen (es sei denn, der oder die Nutzer:in hat stille Pushes in den App-Einstellungen deaktiviert); der Push wird den Nutzer:innen nicht angezeigt. Wenn Braze feststellt, dass ein:e Nutzer:in die App deinstalliert hat, geschieht Folgendes:

* Die Gesamtzahl der Deinstallationen der App wird um eins erhöht.
* Die Deinstallationszahl für jede Kampagne, die der oder die Nutzer:in in den letzten 24 Stunden erfolgreich erhalten hat, wird um eins erhöht.
* Wenn ein:e Nutzer:in in einem Zeitraum von 24 Stunden drei Kampagnen erhält und dann deinstalliert, erhöhen wir die Anzahl der „Deinstallationen" für alle drei Kampagnen.

FCM und APNs unterliegen Einschränkungen hinsichtlich des Uninstall-Trackings. Braze erhöht die Deinstallationszahl nur, wenn FCM oder APNs uns mitteilen, dass ein:e Nutzer:in die App deinstalliert hat. Diese Drittanbietersysteme können uns jedoch jederzeit über Deinstallationen informieren. Verwenden Sie das Uninstall-Tracking, um allgemeine Trends zu erkennen, anstatt präzise Statistiken zu erwarten.

## Fehlerbehebung

### Warum sehe ich plötzlich einen Anstieg bei den Deinstallationen?

Wenn die Deinstallationen von Apps sprunghaft ansteigen, kann das daran liegen, dass Firebase Cloud Messaging (FCM) und der Apple Push Notification Service (APNS) alte Token in unterschiedlicher Häufigkeit widerrufen.

{% alert note %} 
Aus Datenschutzgründen können die Push-Anbieter von Braze Token in unregelmäßigen Abständen widerrufen, was dazu führen kann, dass die Anzahl der Deinstallationen in einem bestimmten Zeitraum gelegentlich stark ansteigt.<br><br>Um diese Änderungen zu validieren, überwachen Sie das Uninstall-Tracking zusammen mit einer Metrik für Nutzeraktionen, wie beispielsweise der direkten Push-Öffnungsrate. Wenn die Deinstallationen stark zunehmen, die direkten Push-Öffnungen jedoch stabil bleiben, spiegelt der Anstieg wahrscheinlich eher die Aufhebung alter Token durch einen Anbieter wider als das tatsächliche Nutzerverhalten.
{% endalert %}

### Warum unterscheidet sich die Anzahl der App-Deinstallationen von den Angaben in den APNs?

Der Unterschied ist zu erwarten. 

Apple verwendet einen zufälligen Zeitplan, um die Meldung zu verzögern, wenn ein Push-Token ungültig wird. Das bedeutet, dass APNs auch nach der Deinstallation einer App noch für eine gewisse Zeit erfolgreiche Antworten auf Push-Benachrichtigungen zurückgeben können. Diese Verzögerung ist beabsichtigt und dient dem Schutz der Privatsphäre der Nutzer:innen. Es wird kein Absprung oder Fehler gemeldet, bis APNs einen `410`-Status für ein ungültiges Token zurückgibt.