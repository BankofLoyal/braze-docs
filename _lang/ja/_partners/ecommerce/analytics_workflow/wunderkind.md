---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "このリファレンス記事では、Wunderkind Signals と Braze の統合について説明します。キャンバスジャーニーをトリガーする行動シグナル、Canvas Entry API を使用したセットアップ、API トリガー配信でのキャンバスコンテキストペイロード、レポートについて取り上げます。"
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) は、独自の識別技術を使用して匿名の Web サイト訪問者を認識し、実用的なメールアドレスに解決する e コマースパフォーマンスプラットフォームです。平均して、Wunderkind は Web サイトトラフィックの3～5%の識別率を40～60%に拡大し、ブランドが既存のメールサービスプロバイダー (ESP) を通じてパーソナライズされた1対1のメッセージを大規模にトリガーできるようにします。

*この統合は Wunderkind によって管理されています。サポートについては、[support.wunderkind.co](https://support.wunderkind.co) をご覧ください。*

## 統合について

Wunderkind Signals の統合により、カート放棄、商品放棄、価格低下などの高インテントな行動シグナルが、Braze でリアルタイムのキャンバスジャーニーをトリガーできます。Wunderkind は Web サイト上の匿名ユーザーを識別し、配信可能なメールアドレスにアイデンティティを解決し、Canvas Entry API を介して構造化されたシグナルペイロードを Braze に配信することで、事前設定されたメールフローを自動的に開始します。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Wunderkind アカウント | Signals が有効になっている Wunderkind アカウントが必要です。資格の確認については、Wunderkind の担当者にお問い合わせください。 |
| Braze アカウント | キャンバスにアクセスできる Braze アカウントが必要です。Wunderkind チームにアカウントのシートを付与する必要があります。詳細については、[Grant Wunderkind Access to Your Braze Account](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account) を参照してください。 |
| Braze REST API キー | セットアップ中に特定の権限を持つ専用の API キーを作成します（[ステップ 1](#step-1-create-a-braze-api-key-for-wunderkind) を参照）。 |
| ユーザー識別 | Wunderkind は通常、`user_alias` と `alias_label: "wknd_email_id"`（多くの場合メールアドレスを `alias_name` として使用）を使用して消費者を Braze に解決します。各 [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) の受信者には、`external_user_id`、`user_alias`、`braze_id`、または `email` のいずれか1つを含める必要があります（[recipients オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)）。`email` を使用する場合は、[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) を含めてください。`user_alias` を使用する場合、トリガーの前にプロファイルが Braze に既に存在している必要があります。[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) または [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) を使用して、ユーザーとエイリアスを先に作成または更新してください。詳細については、[制限事項](#limitations)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 仕組み

Wunderkind が高インテントの匿名ユーザーを識別し、そのアイデンティティを解決すると、`/canvas/trigger/send` エンドポイントを使用してシグナルペイロードを Braze に送信し、そのユーザーに対して関連するキャンバスジャーニーをリアルタイムでトリガーします。

技術的な概要の全体については、[Wunderkind Developer Portal](https://developer.wunderkind.co/docs/integration-overview) を参照してください。

## 統合

### ステップ 1: Wunderkind 用の Braze API キーを作成する

Braze ダッシュボードで以下を行います。

1. **設定** > **API キー**に移動し、**新しい API キーを作成**をクリックします。
2. キーにわかりやすい名前を付けます（例: `Wunderkind Signals`）。
3. [Grant Wunderkind Access to Your Braze Account](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account) に記載されている権限を付与します。
4. API キーをコピーして、次のセクションで Wunderkind プラットフォームに入力します。

{% alert note %}
Wunderkind Signals の場合、Braze [REST API]({{site.baseurl}}/api/basics/) リクエストは OAuth トークンではなく REST API キーで認証されます。ダッシュボードで専用の API キーを作成し、そのキーを Wunderkind に提供してください。
{% endalert %}

### ステップ 2: Braze を Wunderkind プラットフォームに接続する

1. Wunderkind プラットフォームにログインし、**Integrations Hub** に移動します。
2. **Braze** タイルを選択し、**Connect** を選択します。
3. Braze REST API キーを入力し、クラスターを選択します。
4. **Save** を選択します。

### ステップ 3: 新しい Braze アセットを確認する

アクティベーション時に、Wunderkind は Wunderkind の担当者と合意した戦略に基づいて、Braze ワークスペースに新しい実装アセットをプロビジョニングします。

| アセットタイプ | Wunderkind の作成方法 |
| ---------- | -------------------------- |
| コンテンツブロック | 自動 |
| API トリガーキャンバス | マネージドサービス |
| タグ、カスタム属性、リンクテンプレート | マネージドサービス |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ 4: キャンバスのセットアップを完了する

各 Signals キャンバスについて、Braze のドラッグ＆ドロップエディターまたは HTML を使用してメールテンプレートを作成します。

- Wunderkind は、送信時に `/canvas/trigger/send` で各受信者の `context` オブジェクトに商品データとセッションデータを入力します。
- テンプレートでそのペイロードを Liquid で使用する方法の詳細な手順については、Wunderkind ヘルプセンターの [Complete Canvas Setup](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) を参照してください。

### ステップ 5: キャンバスの適格性を確認する

各 Signals キャンバスについて、**ターゲットオーディエンス**設定に移動し、Wunderkind のデフォルトのエントリオーディエンスと終了条件を確認します。

- ユーザーへのメッセージ送信頻度が高くなりすぎないようにするには、[ユーザー中心のレート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)を参照してください。
- ユーザーが購入後もキャンバスメッセージを受信し続けることを防ぐために設定を調整します。例えば、例外として**購入を行う**を追加します。
- 特定の Signals キャンバスは、ユーザーが最もインテントの高いメッセージを受信できるように、カスタム属性フィルターで事前設定されています。
- キャンバスの適格性と優先度の詳細については、Wunderkind ヘルプセンターの [Review Canvas Eligibility](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) を参照してください。

### ステップ 6: テストと起動

Wunderkind は本番稼働前にエンドツーエンドの QA を実施します。

- シグナルが API エラーなしで正しいキャンバス ID に配信されていることを確認します。
- `context` フィールド（商品名、画像、URL）がレンダリングされたメールテンプレートに正しく入力されていることを検証します。
- モック Wunderkind 商品でテンプレートをプレビューする手順については、Wunderkind ヘルプセンターの [Test and Launch Signals for Braze](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) を参照してください。

QA が合格すると、Wunderkind の実装マネージャーがチームと連携して本番環境への起動を調整します。

## キャンバスコンテキストペイロード

Wunderkind は6種類のシグナルタイプをサポートしています。各タイプは、`/canvas/trigger/send` でその受信者の [`context`]({{site.baseurl}}/api/objects_filters/context_object/) オブジェクト内に固有のキーと値のセットを配信します（[API トリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を参照）。`WkPurpose` フィールドは、そのペイロード内のシグナルタイプを識別します。

### 共通フィールド（すべてのキャンバスタイプ） {#canvas-types-table}

| プロパティ | タイプ | 説明 |
| -------- | ---- | ----------- |
| `Origin` | 文字列 | 常に `"wunderkind"` |
| `DataOnly` | 文字列 | 常に `"Y"` — Wunderkind がデータレイヤーとしてのみ機能し、Braze が送信を実行することを示します |
| `UserType` | 文字列 | `"prospect"` または `"customer"` |
| `WkChannel` | 文字列 | この統合では常に `"email"` |
| `WkPurpose` | 文字列 | シグナルタイプ識別子（以下の各キャンバスの値を参照） |
| `WKCouponCode` | 文字列 | クーポンコード（該当する場合。使用しない場合は空文字列） |
| `WKCouponPurpose` | 文字列 | クーポンオファーの説明（使用しない場合は空文字列） |
| `Items` | 配列 | 商品オブジェクトの配列（以下の商品フィールドを参照） |
| `WkOpen` | 文字列 | レポート目的で利用可能なトラッキングピクセル |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 商品アイテムフィールド

| プロパティ | タイプ | 説明 |
| -------- | ---- | ----------- |
| `WkCopy` | 文字列 | 商品名 |
| `WkId` | 文字列 | 商品 ID |
| `WkImageUrl` | 文字列 | 商品画像 URL |
| `WkUrl` | 文字列 | 商品詳細ページ URL |
| `WkPrice` | 文字列 | 元の価格（価格低下キャンバスのみ） |
| `WKSalePrice` | 文字列 | セール価格（価格低下キャンバスのみ） |
| `WkQuantity` | 文字列 | 残り数量（在庫僅少キャンバスのみ） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### キャンバス固有のフィールドと `WkPurpose` の値

| キャンバスタイプ | `WkPurpose` の値 | 追加フィールド |
| ----------- | ----------------- | ------------------- |
| カート放棄 | `"cart abandonment"` | `WkCartReplenUrl` — カートを補充する URL |
| 商品放棄 | `"product abandonment"` | — |
| カテゴリーまとめ | `"category recap"` | `WkCategoryUrl` — 閲覧されたカテゴリーの URL |
| 再入荷 | `"back in stock"` | — |
| 価格低下 | `"price drop"` | 各アイテムの `WkPrice`、`WKSalePrice` |
| 在庫僅少 | `"low stock"` | 各アイテムの `WkQuantity` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ペイロードの例

`recipients` 内の各オブジェクトには、`external_user_id`、`user_alias`、`braze_id`、または `email` のいずれか1つを含める必要があります。詳細については、[Recipients オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。

{% alert note %}
各例では **1つの** Braze 受信者識別子を使用しています。最初の6つは `user_alias` のみを使用し、最後の1つは `email` と [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) のみを使用しています。例の JSON では、レビューツールがその値（`"email"`）を Braze の受信者 `email` フィールドと混同しないように、`context` 内の `WkChannel` キーを省略しています。本番環境では、[共通フィールド（すべてのキャンバスタイプ）テーブル](#canvas-types-table)に記載されているとおり、`context` に `"WkChannel": "email"` を含めてください。
{% endalert %}

以下の例では、Wunderkind がアイデンティティを解決する方法に合わせて、`wknd_email_id` を使用した `user_alias` を使用しています。

{% details カート放棄のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 商品放棄のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details カテゴリーまとめのペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 再入荷のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 価格低下のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 在庫僅少のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details メール識別子の例（代替） %}
`user_alias` の代わりに Braze の `email` フィールドでキャンバスをトリガーする場合、受信者には `email` と `prioritization` のみを含める必要があります（[API トリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を参照）。`context` オブジェクトは他の例と同じです。

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Liquid の使用例

Wunderkind が `/canvas/trigger/send` を呼び出すと、各受信者の `context` オブジェクトに渡されたキーと値がキャンバスエントリデータになります。メッセージステップでは、`context` Liquid 名前空間を使用してそれらを参照します。例えば、[Canvas context オブジェクト]({{site.baseurl}}/api/objects_filters/context_object/)および[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)に記載されているように {% raw %}`{{context.${WkPurpose}}}`{% endraw %} を使用します。正しい Liquid 構文を使用する以外に、追加の設定は不要です。

Braze の出力タグを `for` タグの条件内にネストしないでください。[Liquid の使用]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#use-a-filter-result-in-a-for-loop)に記載されているように、まず `context` から `Items` 配列を変数に割り当ててからループしてください。`assign` 行では Braze のキャンバスエントリ形式 {% raw %}`{{context.${Items}}}`{% endraw %} を使用します（[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#summary-of-supported-tags)を参照）。

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## レポート

Wunderkind は **Braze Currents** を使用して Braze からパフォーマンスデータを取り込みます。Braze Currents は生のイベントを Google Cloud Storage にストリーミングします。Wunderkind はこれらのイベントを正規化し、元のシグナルに対して集計することで、1対1のアトリビューションレポートを作成します。

以下の指標は、Wunderkind レポートダッシュボードで近日中に利用可能になります。

| 指標 | ソース |
| ------ | ------ |
| 配信済み送信数 | Braze Currents |
| メール開封数 | Braze Currents |
| クリック数 | Braze Currents |
| コンバージョン | Braze Currents（セットアップ時に定義されたイベント） |
| 配信停止 | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 制限事項

- **抑制/オプトアウトの同期なし。** 抑制は Braze 内でネイティブに管理する必要があります。注: Braze Signals に移行する既存の Wunderkind 顧客の場合、Wunderkind はチームと連携して現在のセットアップを維持します。
- **メールチャネルのみ。** SMS はこの統合では現在サポートされていません。
- **キャンバストリガーの前にユーザープロファイルが存在している必要があります。** `user_alias` 受信者を使用した [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) は、そのエイリアスを既に持つ**既存の** Braze プロファイルのみを解決します。エイリアスで `send_to_existing_only` を使用することはできず、キャンバストリガーはエイリアスのみから新しいプロファイルを作成しません。ユーザーを先に作成または更新し、`wknd_email_id` エイリアスを設定する必要があります（例えば、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) または [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) を使用）。Wunderkind は、Braze が処理を完了できるように、そのアップサート後にトリガーを発火する前に少し待機する場合があります。
- **識別子としてのメール。** キャンバストリガーが `user_alias` の代わりに `email` で受信者を識別する場合、Braze の要件に従って、その受信者オブジェクトに [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) を含めてください。


## その他のリソース

- [Wunderkind ヘルプセンター — Signals for Braze Overview](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Wunderkind Developer Portal — Integration Overview](https://developer.wunderkind.co/docs/integration-overview)
- [API トリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [Canvas context オブジェクト]({{site.baseurl}}/api/objects_filters/context_object/)
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)