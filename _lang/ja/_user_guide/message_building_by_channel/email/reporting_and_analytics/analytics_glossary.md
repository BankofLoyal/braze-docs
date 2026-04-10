---
nav_title: メール分析用語集
article_title: メール分析用語集
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "この用語集には、起動後のメールキャンペーンまたはキャンバスの分析セクションに表示される用語が含まれています。この用語集には、Currents の指標は含まれていません。"
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

### バリエーション

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### メール可能

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### オーディエンス (%)

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数) / (ユニーク受信者数)</span>

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} この数値は Braze から提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  この指標は Braze から提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  この指標は Braze から提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信数

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} メールの場合、*配信数*は、メール可能な宛先に正常に送信および受信されたメッセージ（送信数）の合計です。

<span class="calculation-line">計算式: (送信数) - (バウンス数) </span>

{% endapi %}

{% api %}

### 配信率 (%)

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">計算式: (送信数 - バウンス数) / (送信数) </span>

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

メールの場合、*バウンス率 (%)* または*バウンス率*は、使用した送信サービスが送信に失敗した、または「返送された」や「受信されなかった」と指定されたメッセージ、あるいは目的のメール可能なユーザーが受信しなかったメッセージの割合です。

SendGrid を使用している顧客のメールバウンスには、ハードバウンス、スパム (`spam_report_drops`)、および無効なアドレスに送信されたメール (`invalid_emails`) が含まれます。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>バウンス数</i>:</b> カウント</li>
        <li><b><i>バウンス %</i> または <i>バウンス率 %</i>:</b> (バウンス数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ハードバウンス

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### ソフトバウンス

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} メールがソフトバウンスになった場合、通常は72時間以内に再試行されますが、再試行回数は受信側ごとに異なります。 

ソフトバウンスはキャンペーン分析では追跡されませんが、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)で監視できます。また、[ソフトバウンスセグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)を使用して、送信対象からこれらのユーザーを除外することもできます。メッセージアクティビティログでは、ソフトバウンスの理由を確認し、メールキャンペーンの「送信数」と「配信数」の間で生じる可能性のある差異を把握することもできます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}
  
### スパム

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>スパム</i>:</b> カウント</li>
        <li><b><i>スパム %</i> または <i>スパム率 %</i>:</b> (スパムとしてマークされた数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### ユニーク開封数

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} メールの場合、これは7日間にわたって追跡されます。つまり、同じメールを7日後に再度開封した同一ユーザーは、新しいユニーク開封としてカウントされます。そのため、ダッシュボードのユニーク開封数は、Currents データに対する単純な `DISTINCT user_id` クエリよりも高くなる場合があります。ダッシュボードの数値を Currents から一致させるには、`is_unique` が `true` のイベントでフィルタリングしてください。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>ユニーク開封数</i>:</b> カウント</li>
        <li><b><i>ユニーク開封率 (%)</i> または <i>ユニーク開封率</i>:</b> (ユニーク開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーククリック数

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これは、メールの場合7日間にわたって追跡され、<a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> によって測定されます。これには、Braze が提供する配信停止リンクのクリックも含まれます。ユニーク開封と同様に、同じリンクを7日後に再度クリックした同一ユーザーは、新しいユニーククリックとしてカウントされます。ダッシュボードの数値を Currents から一致させるには、`is_unique` が `true` のイベントでフィルタリングしてください。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>ユニーククリック数</i>:</b> カウント</li>
        <li><b><i>ユニーククリック率 (%)</i> または <i>クリック率</i>:</b> (ユニーククリック数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### 配信停止数

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>配信停止数</i> または <i>購読解除</i>:</b> カウント</li>
        <li><b><i>配信停止率 (%)</i> または <i>配信停止率</i>:</b> (配信停止数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 収益

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### 1次コンバージョン (A) または1次コンバージョンイベント

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} メール、プッシュ、webhook では、最初の送信後にコンバージョンの追跡を開始します。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>1次コンバージョン (A)</i> または <i>1次コンバージョンイベント</i>:</b> カウント</li>
        <li><b><i>1次コンバージョン (A) %</i> または <i>1次コンバージョンイベント率</i>:</b> (1次コンバージョン数) / (ユニーク受信者数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 信頼度

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### マシン開封数
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} この指標は、SendGrid の場合は2021年11月11日から、SparkPost の場合は2021年12月2日から追跡されています。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### その他の開封数

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} ユーザーは、<i>マシン開封数</i>が記録される前にメールを開封する（<i>その他の開封数</i>としてカウントされる開封など）こともあります。あるユーザーが、マシン開封イベント後に Apple Mail 以外の受信トレイからメールを1回（またはそれ以上）開封した場合、そのユーザーによるメール開封回数は<i>その他の開封数</i>に加算され、<i>ユニーク開封数</i>には1回のみカウントされます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### クリック開封率

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数) (メールの場合)</span>

{% endapi %}