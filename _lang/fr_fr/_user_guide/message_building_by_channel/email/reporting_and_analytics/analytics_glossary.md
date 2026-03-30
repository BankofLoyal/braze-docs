---
nav_title: Glossaire analytique pour l'e-mail
article_title: Glossaire analytique pour l'e-mail
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire inclut les termes que vous trouverez dans la section d'analyse de votre campagne par e-mail ou de votre Canvas, après son lancement. Ce glossaire n'inclut pas les indicateurs Currents."
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

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Joignable par e-mail

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### % d'audience

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Calcul : (Nombre de destinataires dans la variante) / (Destinataires uniques)</span>

{% endapi %}

{% api %}

### Destinataires uniques

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Ce nombre est fourni par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Envois

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Cet indicateur est fourni par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Messages envoyés

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Cet indicateur est fourni par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Réceptions

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Pour les e-mails, les *réceptions* correspondent au nombre total de messages (envois) envoyés et reçus avec succès par les destinataires joignables par e-mail.

<span class="calculation-line">Calcul : (Envois) - (Rebonds) </span>

{% endapi %}

{% api %}

### % de réceptions

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Calcul : (Envois - Rebonds) / (Envois) </span>

{% endapi %}

{% api %}

### Rebonds

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Pour l'e-mail, le *% de rebonds* ou *taux de rebond* est le pourcentage de messages qui ont été envoyés sans succès ou désignés comme « renvoyés » ou « non reçus » par les services d'envoi utilisés, ou qui n'ont pas été reçus par les destinataires visés.

Pour les clients utilisant SendGrid, un rebond d'e-mail se compose des échecs d'envoi définitifs, du spam (`spam_report_drops`) et des e-mails envoyés à des adresses non valides (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Rebonds</i> :</b> Total</li>
        <li><b><i>% de rebonds</i> ou <i>taux de rebond %</i> :</b> (Rebonds) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Échec d'envoi définitif

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Échec provisoire d'envoi

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un e-mail reçoit un échec provisoire d'envoi, une nouvelle tentative est généralement effectuée dans les 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre. 

Bien que les échecs provisoires d'envoi ne soient pas suivis dans l'analyse de votre campagne, vous pouvez les surveiller dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) ou exclure ces utilisateurs de vos envois à l'aide du [filtre de segmentation des échecs provisoires]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). Dans le journal d'activité des messages, vous pouvez également voir la raison des échecs provisoires et comprendre les écarts éventuels entre les « envois » et les « réceptions » de vos campagnes par e-mail.

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Spam</i> :</b> Total</li>
        <li><b><i>% de spam</i> ou <i>taux de spam %</i> :</b> (Marqué comme spam) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Ouvertures uniques

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Pour les e-mails, le suivi se fait sur une période de sept jours. Cela signifie qu'un même utilisateur qui ouvre à nouveau le même e-mail après sept jours est comptabilisé comme une nouvelle ouverture unique. Par conséquent, le nombre d'ouvertures uniques affiché dans le tableau de bord peut être supérieur à celui obtenu par une simple requête `DISTINCT user_id` sur les données Currents. Pour faire correspondre les totaux du tableau de bord à partir de Currents, filtrez les événements où `is_unique` est `true`.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Ouvertures uniques</i> :</b> Total</li>
        <li><b><i>% d'ouvertures uniques</i> ou <i>taux d'ouvertures uniques</i> :</b> (Ouvertures uniques) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics uniques

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Ce suivi est effectué sur une période de sept jours pour les e-mails et mesuré par <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Cela inclut les clics sur les liens de désinscription fournis par Braze. Comme pour les ouvertures uniques, un utilisateur qui clique à nouveau sur le même lien après 7 jours est comptabilisé comme un nouveau clic unique. Pour faire correspondre les totaux du tableau de bord à partir de Currents, filtrez les événements où `is_unique` est `true`.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Clics uniques</i> :</b> Total</li>
        <li><b><i>% de clics uniques</i> ou <i>taux de clics</i> :</b> (Clics uniques) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Désabonnements

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Désabonnements</i> :</b> Total</li>
        <li><b><i>% de désabonnements</i> ou <i>taux de désabonnement</i> :</b> (Désabonnements) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Chiffre d'affaires

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Conversions principales (A) ou événement de conversion principal

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Pour les e-mails, les notifications push et les webhooks, le suivi des conversions commence après l'envoi initial.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Conversions principales (A)</i> ou <i>événement de conversion principal</i> :</b> Total</li>
        <li><b><i>% de conversions principales (A)</i> ou <i>taux d'événement de conversion principal</i> :</b> (Conversions principales) / (Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiance

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Ouvertures automatiques
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Cet indicateur est suivi à partir du 11 novembre 2021 pour SendGrid et du 2 décembre 2021 pour SparkPost.

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Autres ouvertures

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Notez qu'un utilisateur peut également ouvrir un e-mail (comptabilisé dans les <i>Autres ouvertures</i>) avant qu'une <i>ouverture automatique</i> ne soit enregistrée. Si un utilisateur ouvre un e-mail une ou plusieurs fois après un événement d'ouverture automatique depuis une boîte de réception autre qu'Apple Mail, le nombre de fois où l'utilisateur ouvre l'e-mail est comptabilisé dans les <i>Autres ouvertures</i> et une seule fois dans les <i>Ouvertures uniques</i>.

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Taux de clic par ouverture

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour l'e-mail)</span>

{% endapi %}