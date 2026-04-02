---
nav_title: Glossário de análise de dados de e-mail
article_title: Glossário de análise de dados de e-mail
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glossário inclui os termos que serão encontrados na seção de análise de dados da sua campanha de e-mail ou do Canvas, após o lançamento. Este glossário não inclui as métricas do Currents."
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

### Variação

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envio de e-mail

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### % de público

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (Destinatários únicos)</span>

{% endapi %}

{% api %}

### Destinatários únicos

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Esse número é recebido da Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Essa métrica é fornecida pela Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Essa métrica é fornecida pela Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Para e-mails, *Entregas* é o número total de mensagens (Envios) enviadas e recebidas com sucesso por partes que podem receber e-mails.

<span class="calculation-line">Cálculo: (Envios) - (Bounces) </span>

{% endapi %}

{% api %}

### Entregas %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envios - Bounces) / (Envios) </span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Para e-mail, a % de *bounce* ou a *taxa de bounce* é a porcentagem de mensagens que foram enviadas sem sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados ou não recebidas pelos usuários de e-mail pretendidos.

Um bounce de e-mail para clientes que usam o SendGrid consiste em hard bounces, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Bounces</i>:</b> Contagem</li>
        <li><b><i>Bounce %</i> ou <i>Bounce Rate %</i>:</b> (Bounces) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Soft bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Se um e-mail receber um soft bounce, geralmente tentaremos novamente dentro de 72 horas, mas o número de tentativas varia de acordo com o destinatário. 

Embora os soft bounces não sejam rastreados na análise de dados da sua campanha, é possível monitorar os soft bounces no [Registro de atividades de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) ou excluir esses usuários do seu envio com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). No Registro de atividades de mensagens, você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" das suas campanhas de e-mail.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Spam</i>:</b> Contagem</li>
        <li><b><i>Spam %</i> ou <i>Spam Rate %</i>:</b> (Marcado como Spam) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Aberturas únicas

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Para e-mail, esse rastreamento é feito em um período de sete dias. Isso significa que um único usuário que abrir o mesmo e-mail novamente após sete dias conta como uma nova abertura única. Como resultado, as contagens de aberturas únicas no dashboard podem ser maiores do que uma simples consulta `DISTINCT user_id` nos dados do Currents. Para corresponder às contagens do dashboard a partir do Currents, filtre por eventos em que `is_unique` seja `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Aberturas únicas</i>:</b> Contagem</li>
        <li><b><i>% de aberturas únicas</i> ou <i>Taxa de abertura única</i>:</b> (Aberturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cliques únicos

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Isso é rastreado em um período de sete dias para e-mails e medido por <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Isso inclui cliques em links de cancelamento de inscrição fornecidos pela Braze. Assim como as aberturas únicas, um usuário que clicar no mesmo link novamente após 7 dias conta como um novo clique único. Para corresponder às contagens do dashboard a partir do Currents, filtre por eventos em que `is_unique` seja `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cliques únicos</i>:</b> Contagem</li>
        <li><b><i>% de cliques únicos</i> ou <i>Taxa de cliques</i>:</b> (Cliques únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Cancelamento de inscrição

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cancelamento de inscrição</i> ou <i>Unsub</i>:</b> Contagem</li>
        <li><b><i>% de cancelamentos de inscrição</i> ou <i>Taxa de cancelamento de inscrição</i>:</b> (Cancelamentos de inscrição) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Receita

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Conversões primárias (A) ou evento de conversão primária

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Para e-mails, push e webhooks, começamos a rastrear as conversões após o envio inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversões primárias (A)</i> ou <i>Evento de conversão primária</i>:</b> Contagem</li>
        <li><b><i>Conversões primárias (A) %</i> ou <i>Taxa de evento de conversão primária</i>:</b> (Conversões primárias) / (Destinatários únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiança

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Aberturas por máquina
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para a SendGrid e de 2 de dezembro de 2021 para a SparkPost.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Outras aberturas

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Note que um usuário também pode abrir um e-mail (como as contagens de abertura para <i>Outras aberturas</i>) antes que uma contagem de <i>Aberturas por máquina</i> seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura por máquina de uma caixa de entrada que não seja do Apple Mail, a quantidade de vezes que o usuário abrir o e-mail será calculada para <i>Outras aberturas</i> e apenas uma vez para <i>Aberturas únicas</i>.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Taxa de cliques por abertura

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Cliques únicos) / (Aberturas únicas) (para e-mail)</span>

{% endapi %}