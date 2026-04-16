---
nav_title: Log-Analytics
article_title: Log Analytics 
page_order: 1
description: "Dieser Artikel beschreibt, wie Sie Impressionen, Klicks und Schließungen manuell protokollieren und das On-Click-Verhalten für Ihre angepassten Content-Cards handhaben."
toc_headers: "h2"

---

# Log Analytics

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Fehlende Content-Cards-Analytics

Wenn Content-Cards in Ihrer App korrekt angezeigt werden, Sie aber durchgehend keine Analytics erhalten (eindeutige Empfänger:innen, Impressionen, Klicks usw.), liegt wahrscheinlich ein Problem mit der SDK-Integration vor.

- **Angepasste Content-Card-Ansichten (Android, iOS, Internet):** Die Standard-Braze-UI protokolliert Impressionen und Klicks auf allen Plattformen automatisch. Wenn Sie eine angepasste Content-Card-Ansicht oder -Implementierung verwenden, müssen Sie die entsprechenden Protokollierungsmethoden explizit in Ihrer Anwendung aufrufen. Weitere Informationen finden Sie unter [Log Analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) für Ihre Plattform. Stellen Sie bei angepassten Internet-Implementierungen insbesondere sicher, dass das Braze Web SDK geladen ist, prüfen Sie die Browser-Konsole auf Fehler und überprüfen Sie, ob Kartendaten empfangen werden.
- **SDK-Initialisierung und Nutzeridentifikation:** Stellen Sie sicher, dass das SDK vollständig initialisiert ist, bevor Karten angezeigt werden. Events werden stillschweigend verworfen (nicht in die Warteschlange gestellt), wenn das SDK nicht initialisiert ist, sich im verzögerten Initialisierungsmodus befindet oder DSGVO-deaktiviert ist. Das SDK protokolliert zwar Analytics für anonyme Nutzer:innen, aber Dashboard-Metriken wie „Eindeutige Empfänger:innen" erfordern eine aufgelöste Nutzeridentität. Rufen Sie daher nach Möglichkeit `changeUser` auf, bevor Karten angezeigt werden.