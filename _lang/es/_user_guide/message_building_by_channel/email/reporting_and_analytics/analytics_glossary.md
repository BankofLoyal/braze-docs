---
nav_title: Glosario de Email Analytics
article_title: Glosario de Email Analytics
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glosario incluye los términos que encontrarás en la sección de análisis de tu campaña de correo electrónico o Canvas, tras el lanzamiento. Este glosario no incluye las métricas de Currents."
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

### Variación

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envío por correo electrónico

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### % de audiencia

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatarios en la variante) / (Destinatarios únicos)</span>

{% endapi %}

{% api %}

### Destinatarios únicos

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Este número se recibe de Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envíos

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Mensajes enviados

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} En el caso de los correos electrónicos, las *entregas* son el número total de mensajes (envíos) enviados y recibidos correctamente por las partes que pueden recibir correos electrónicos.

<span class="calculation-line">Cálculo: (Envíos) - (Rebotes) </span>

{% endapi %}

{% api %}

### % de entregas

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envíos - Rebotes) / (Envíos) </span>

{% endapi %}

{% api %}

### Rebotes

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Para el correo electrónico, el *% de rebote* o *tasa de rebote* es el porcentaje de mensajes que se enviaron sin éxito o se designaron como "devueltos" o "no recibidos" de los servicios de envío utilizados o no recibidos por los usuarios destinatarios del correo electrónico.

Un rebote de correo electrónico para clientes que utilizan SendGrid consiste en rebotes duros, correo no deseado (`spam_report_drops`) y correos enviados a direcciones no válidas (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Rebotes</i>:</b> Recuento</li>
        <li><b><i>% de rebote</i> o <i>tasa de rebote %</i>:</b> (Rebotes) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rebote duro

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Rebote blando

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un correo electrónico recibe un rebote blando, normalmente lo reintentaremos en un plazo de 72 horas, pero el número de intentos de reintento varía de un destinatario a otro. 

Aunque los rebotes blandos no se rastrean en los análisis de tu campaña, puedes monitorear los rebotes blandos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) o excluir a estos usuarios de tus envíos con el [filtro de segmento de rebotes blandos]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). En el Registro de actividad de mensajes, también puedes ver el motivo de los rebotes blandos y comprender las posibles discrepancias entre los "envíos" y las "entregas" de tus campañas de correo electrónico.

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}
  
### Correo no deseado

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Correo no deseado</i>:</b> Recuento</li>
        <li><b><i>% de correo no deseado</i> o <i>% de tasa de correo no deseado</i>:</b> (Marcado como correo no deseado) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Aperturas únicas

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} En el caso del correo electrónico, el seguimiento se realiza durante un periodo de siete días. Esto significa que un mismo usuario que abra el mismo correo electrónico de nuevo después de siete días cuenta como una nueva apertura única. Como resultado, los recuentos de aperturas únicas en el dashboard pueden ser mayores que una simple consulta `DISTINCT user_id` sobre los datos de Currents. Para que coincidan con los recuentos del dashboard desde Currents, filtra por eventos donde `is_unique` sea `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Aperturas únicas</i>:</b> Recuento</li>
        <li><b><i>% de aperturas únicas</i> o <i>tasa de aperturas únicas</i>:</b> (Aperturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics únicos

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Esto se rastrea durante un periodo de siete días para el correo electrónico y se mide mediante <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Esto incluye los clics en los enlaces para cancelar suscripción proporcionados por Braze. De forma similar a las aperturas únicas, un usuario que hace clic en el mismo enlace de nuevo después de 7 días cuenta como un nuevo clic único. Para que coincidan con los recuentos del dashboard desde Currents, filtra por eventos donde `is_unique` sea `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Clics únicos</i>:</b> Recuento</li>
        <li><b><i>% de clics únicos</i> o <i>tasa de clics</i>:</b> (Clics únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Cancelaciones de suscripción

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cancelaciones de suscripción</i> o <i>Bajas</i>:</b> Recuento</li>
        <li><b><i>% de cancelaciones de suscripción</i> o <i>tasa de cancelación de suscripciones</i>:</b> (Cancelaciones de suscripción) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ingresos

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Conversiones primarias (A) o evento de conversión primaria

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Para el correo electrónico, push y webhooks, empezamos a hacer el seguimiento de las conversiones después del envío inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversiones primarias (A)</i> o <i>evento de conversión primaria</i>:</b> Recuento</li>
        <li><b><i>Conversiones primarias (A) %</i> o <i>tasa del evento de conversión primaria</i>:</b> (Conversiones primarias) / (Destinatarios únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confianza

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Aperturas automáticas
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Esta métrica se rastrea a partir del 11 de noviembre de 2021 para SendGrid y del 2 de diciembre de 2021 para SparkPost.

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Otras aperturas

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Ten en cuenta que un usuario también puede abrir un correo electrónico (contando como apertura para <i>Otras aperturas</i>) antes de que se registre un recuento de <i>Aperturas automáticas</i>. Si un usuario abre un correo electrónico una vez (o más) después de un evento de apertura automática desde un buzón de entrada que no sea de Apple Mail, entonces la cantidad de veces que el usuario abre el correo electrónico se calcula para <i>Otras aperturas</i> y solo una vez para <i>Aperturas únicas</i>.

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Tasa de clics sobre aperturas

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Clics únicos) / (Aperturas únicas) (para correo electrónico)</span>

{% endapi %}