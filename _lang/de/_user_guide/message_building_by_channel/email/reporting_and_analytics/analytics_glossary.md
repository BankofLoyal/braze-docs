---
nav_title: E-Mail-Analyse-Glossar
article_title: E-Mail-Analyse-Glossar
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar enthält die Begriffe, die Sie im Analysebereich Ihrer E-Mail-Kampagne oder Ihres Canvas nach dem Start finden werden. Dieses Glossar enthält keine Currents-Metriken."
channel: 
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variante

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Per E-Mail versendbar

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Zielgruppe %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Berechnung: (Zahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

### Eindeutige Empfänger:innen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Diese Zahl wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Nachrichten gesendet

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Zustellungen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Bei E-Mails ist *Deliveries* die Gesamtzahl der Nachrichten (Sends), die erfolgreich an E-Mail-fähige Empfänger:innen gesendet und von diesen empfangen wurden.

<span class="calculation-line">Berechnung: (Sendungen) - (Bounces) </span>

{% endapi %}

{% api %}

### Zustellungen %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Berechnung: (Sendungen - Bounces) / (Sendungen) </span>

{% endapi %}

{% api %}

### Absprünge

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Bei E-Mails ist *Bounce %* oder *Absprungrate* der prozentuale Anteil der Nachrichten, die von den verwendeten Diensten erfolglos versendet oder als „zurückgeschickt" oder „nicht erhalten" bezeichnet wurden oder von den vorgesehenen Nutzer:innen nicht empfangen wurden.

Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, besteht aus Hard Bounces, Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Absprünge</i>:</b> Anzahl</li>
        <li><b><i>Bounce %</i> oder <i>Absprungrate %</i>:</b> (Bounces) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Wenn eine E-Mail einen Soft Bounce erhält, versuchen wir es normalerweise innerhalb von 72 Stunden erneut, aber die Anzahl der Wiederholungsversuche variiert von Empfänger:in zu Empfänger:in. 

Soft Bounces werden zwar nicht in den Analytics Ihrer Kampagne getrackt, aber Sie können die Soft Bounces im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) überwachen oder diese Nutzer:innen mit dem [Filter für Soft-Bounced-Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced) von Ihrem Versand ausschließen. Im Nachrichten-Aktivitätsprotokoll können Sie auch den Grund für die Soft Bounces sehen und mögliche Diskrepanzen zwischen den „Sendungen" und „Zustellungen" Ihrer E-Mail-Kampagnen nachvollziehen.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Spam</i>:</b> Anzahl</li>
        <li><b><i>Spam %</i> oder <i>Spam-Rate %</i>:</b> (Als Spam markiert) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Eindeutige Öffnungen

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Bei E-Mails wird dies über einen Zeitraum von sieben Tagen getrackt. Das bedeutet, dass ein:e einzelne Nutzer:in, die dieselbe E-Mail nach sieben Tagen erneut öffnet, als neue eindeutige Öffnung gezählt wird. Daher können die Zähler für eindeutige Öffnungen im Dashboard höher sein als eine einfache `DISTINCT user_id`-Abfrage auf Currents-Daten. Um die Dashboard-Zähler mit Currents abzugleichen, filtern Sie nach Events, bei denen `is_unique` den Wert `true` hat.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Eindeutige Öffnungen</i>:</b> Anzahl</li>
        <li><b><i>Eindeutige Öffnungen %</i> oder <i>Eindeutige Öffnungsrate</i>:</b> (Eindeutige Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Klicks

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dies wird über einen Zeitraum von sieben Tagen für E-Mails getrackt und anhand der <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> gemessen. Dazu gehören auch Klicks auf die von Braze bereitgestellten Abmeldelinks. Ähnlich wie bei eindeutigen Öffnungen wird ein:e Nutzer:in, die denselben Link nach 7 Tagen erneut anklickt, als neuer eindeutiger Klick gezählt. Um die Dashboard-Zähler mit Currents abzugleichen, filtern Sie nach Events, bei denen `is_unique` den Wert `true` hat.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Eindeutige Klicks</i>:</b> Anzahl</li>
        <li><b><i>Eindeutige Klicks %</i> oder <i>Klickrate</i>:</b> (Eindeutige Klicks) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Abgemeldete Personen oder Abmeldung

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Abgemeldete Personen</i> oder <i>Abmeldung</i>:</b> Anzahl</li>
        <li><b><i>Abgemeldete Personen %</i> oder <i>Abmelderate</i>:</b> (Abmeldungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Umsatz

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Primäre Konversionen (A) oder primäres Konversions-Event

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Bei E-Mail, Push und Webhooks beginnen wir mit dem Tracking von Konversionen nach dem ersten Versand.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Primäre Konversionen (A)</i> oder <i>primäres Konversions-Event</i>:</b> Anzahl</li>
        <li><b><i>Primäre Konversionen (A) %</i> oder <i>Primäre Konversions-Event-Rate</i>:</b> (Primäre Konversionen) / (Eindeutige Empfänger:innen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Konfidenz

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Automatische Öffnungen
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Diese Metrik wird ab dem 11. November 2021 für SendGrid und ab dem 2. Dezember 2021 für SparkPost getrackt.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Sonstige Öffnungen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Beachten Sie, dass ein:e Nutzer:in eine E-Mail auch öffnen kann (wobei die Öffnung zu den <i>sonstigen Öffnungen</i> zählt), bevor eine <i>automatische Öffnung</i> protokolliert wird. Wenn ein:e Nutzer:in eine E-Mail einmal (oder öfter) nach einem automatischen Öffnungsereignis aus einem Nicht-Apple-Mail-Posteingang öffnet, wird die Anzahl der Öffnungen in die Kategorie <i>Sonstige Öffnungen</i> und nur einmal in die Kategorie <i>Eindeutige Öffnungen</i> eingerechnet.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Effektive Klickrate

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Berechnung: (Eindeutige Klicks) / (Eindeutige Öffnungen) (für E-Mail)</span>

{% endapi %}