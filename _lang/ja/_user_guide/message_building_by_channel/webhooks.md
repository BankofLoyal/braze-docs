---
nav_title: Webhook
article_title: Webhook
page_order: 8
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhook"
guide_top_text: "Webhook は、アプリケーションがリアルタイムでデータを共有するための一般的な通信方法です。今日、1つのスタンドアローンアプリケーションですべてをこなせることはほとんどありません。ほとんどの場合、特定のタスクを実行するために特化した多くの異なるアプリやシステムで作業しており、これらのアプリはすべて互いに通信できる必要があります。そこで webhook の出番です。<br><br> Webhook とは、ある基準が満たされた後に、あるシステムから別のシステムへ自動送信されるメッセージのことです。Braze では、この基準は通常、カスタムイベントのトリガーとなります。<br><br>根本的に、webhook は2つの個別システムがリアルタイムで送信されるデータに基づいて効果的なアクションを実行するための、イベントベースの方法です。そのメッセージには、特定のタスクをいつ、どのように実行するかを受信側システムに伝える指示が含まれています。そのため、webhook を使用すると、データおよびプログラム機能へのよりダイナミックで柔軟なアクセスが可能になり、プロセスを合理化するカスタマージャーニーを設定できます。<br><br>**Webhook の利用可否は Braze パッケージによって異なります。まずはアカウントマネージャーまたはカスタマーサクセスマネージャーにご連絡ください。**"
description: "このランディングページは webhook のホームページです。ここでは、webhook の作成、Webhook テンプレートの作成、Braze-to-Braze webhook に関する記事をご覧いただけます。"
channel:
  - webhooks
search_rank: 3
guide_featured_title: "セクションの記事"
guide_featured_list:
- name: Webhook を作成する
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Webhook テンプレートを作成する
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Braze-to-Braze Webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: レポート
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Webhook リクエストのトラブルシューティング 
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}ユースケース

Webhook は、複数のシステムを接続するための優れた方法です。結局、webhook はアプリの通信方法です。webhook が特に役立つ一般的なシナリオをいくつかご紹介します。

- Braze とデータを送受信する
- Braze が直接サポートしていないチャネル経由で顧客にメッセージを送信する
- Braze API に投稿する

より具体的なユースケースとしては、以下のようなものがあります。

- ユーザーがメール配信を停止した場合、webhook で分析データベースや CRM に同じ情報を更新させることができ、ユーザーの動作を全体的に把握できます。
- Facebook Messenger や LINE 内でユーザーに[トランザクションメッセージ]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)を送信する。
- webhook を使用して [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/) などのサードパーティサービスと通信し、アプリ内および Web のアクティビティに応じて顧客にダイレクトメールを送信する。
- ゲーマーのレベルが一定に達したり、ポイントが一定数に達したら、webhook と既存の API セットアップを使って、キャラクターのアップグレードやコインを直接アカウントに送ります。マルチチャネルメッセージングキャンペーンの一環として webhook を送信する場合は、プッシュ通知やその他のメッセージを送信して、同時にゲーマーに報酬を通知できます。
- 航空会社の場合、webhook と既存の API セットアップを利用して、顧客が一定数のフライトを予約した後、顧客のアカウントに割引をクレジットできます。
- 無限の「If This Then That」（[IFTTT](https://ifttt.com/about)）レシピ — 例えば、顧客がメールでアプリにサインインすると、そのアドレスが自動的に Salesforce に設定されます。

## Webhook の構造

Webhook を構成する要素を以下に示します。

| Webhook の要素 | 説明 |
| --- | --- |
| [HTTP メソッド](#methods) | API と同様に、webhook にはリクエストメソッドが必要です。これらは webhook がヒットする URL に与えられ、与えられた情報で何をすべきかをエンドポイントに伝えます。指定できる HTTP メソッドは4つあります：POST、GET、PUT、および DELETE。 |
| HTTP URL | Webhook エンドポイントの URL アドレスです。エンドポイントは、webhook でキャプチャしている情報の送信先となる場所です。 |
| リクエストボディ | Webhook のこの部分には、エンドポイントに伝える情報が含まれています。リクエストボディには、JSON キーと値のペア、または生のテキストを使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![HTTP メソッド、HTTP URL、リクエストボディを持つ Webhook の例。]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### HTTP メソッド {#methods}

次の表は、webhook で指定できる4つの異なる HTTP メソッドについて説明しています。

| HTTP メソッド | 説明 |
| ----------- | ----------- |
| POST | このメソッドは、受信サーバーに新しい情報を書き込みます。実際のアプリケーションで POST メソッドを使う一般的な例としては、Web サイトの[問い合わせフォーム](https://www.braze.com/company/contact)があります。フォームに入力した情報はすべてリクエストボディの一部となり、レシーバーに送信されます。これはデータを送信する際に最もよく使われるメソッドです。
| GET | このメソッドは、新しい情報を書き込むのではなく、既存の情報を取得します。定義上、GET リクエストはリクエストボディをサポートしません。これは、サーバーにデータを要求するときに使われる最も一般的なメソッドです。例えば、[`/segments/list` エンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)があるとします。GET リクエストをすると、セグメントのリストが返されます。
| PUT | このメソッドはエンドポイントの情報を更新し、既存の情報をリクエストボディの内容に置き換えます。 
| DELETE | このメソッドは HTTP URL のリソースを削除します。 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze の Webhook

Braze では、webhook を Webhook キャンペーン、API キャンペーン、またはキャンバスコンポーネントとして作成できます。

{% tabs %}
{% tab Webhook Campaign %}

1. Braze ダッシュボードで [**キャンペーン**] に移動します。
2. [**キャンペーンを作成**] をクリックし、[**Webhook**] を選択します。

詳しくは [Webhook を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。

{% endtab %}
{% tab API Campaign %}

1. Braze ダッシュボードで [**キャンペーン**] に移動します。
2. [**キャンペーンを作成**] をクリックし、[**API キャンペーン**] を選択します。
3. [**メッセージを追加**] をクリックし、[**Webhook**] を選択します。
4. [Webhook オブジェクト]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/)を含むように API 呼び出しをフォーマットします。

詳しくは [Webhook を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。

{% endtab %}
{% tab Canvas Component %}

1. キャンバスで、新しいコンポーネントを作成します。
2. コンポーネントの [**メッセージ**] セクションで、[**Webhook**] を選択します。

詳しくは [Webhook を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。

{% endtab %}
{% endtabs %}

## Webhook のエラー処理とレート制限

Braze は、Webhook コールからエラー応答を受信すると、以下の応答ヘッダーに基づいて webhook の送信動作を自動的に調整します。

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

これらのヘッダーは、レート制限を解釈し、それに応じて送信速度を調整し、今後のエラーを回避するうえで役立ちます。また、再試行にはエクスポネンシャルバックオフ戦略を採用しており、再試行の間隔を広げることでサーバーに負荷がかかるリスクを軽減します。

特定のホストへの webhook リクエストの大部分が失敗していることが検出された場合には、そのホストへのすべての送信試行を一時的に延期します。その後、定義されているクールダウン期間を経過したら送信を再開し、システムを回復させます。