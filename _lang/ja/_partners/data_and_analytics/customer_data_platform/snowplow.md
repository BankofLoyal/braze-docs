---
nav_title: Snowplow
article_title: Snowplow
description: "この参考記事では、BrazeとデータインフラプラットフォームであるSnowplowのパートナーシップについて概説しています。SnowplowのEvent Forwardingを使用して、SnowplowのイベントをリアルタイムでBrazeに転送できます。"
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplow.io)は、リッチで高品質な低遅延データ収集のためのスケーラブルなオープンソースプラットフォームです。Snowplowは、企業向けに高品質で完全な行動データを収集するように設計されています。

_この統合は Snowplow によって管理されています。_

## 統合について

BrazeとSnowplowの統合により、Snowplowのイベント転送ソリューションを使って、SnowplowのイベントをリアルタイムでBrazeに転送できます。この統合により、柔軟性とコントロールを提供しながら、Brazeにイベントを送信できます。具体的には、以下のことが可能です：
- Brazeに送信する前に、イベントのフィルタリングと変換を行います。
- SnowplowのイベントデータをBrazeのユーザー属性、カスタムイベント、購入にマッピングします。
- 転送を選択するまで、すべてのデータをプライベートクラウドに保持します。
- 既存のSnowplowクラウドアカウント内にソリューションを自分でデプロイします。 

Snowplowの[Event Forwarding](https://docs.snowplow.io/docs/destinations/forwarding-events/)は、Snowplowの顧客が利用できる有料のアドオン機能です。このアドオンなしでBrazeにイベントを転送するには、Snowplowの[Google Tag Manager Server-Side](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/)統合を使用してください。

Snowplowの豊富な行動データを活用して、Brazeで強力な顧客中心のインタラクションを促進し、パーソナライズ済みメッセージをリアルタイムで配信しましょう。

## 前提条件

| 必要条件             | 説明                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snowplow パイプライン       | Snowplowのパイプラインを稼働させる必要があります。                                                                                                                                                                                                                                          |
| Snowplow Console へのアクセス | イベントフォワーダーを設定するには、Snowplow Consoleにアクセスする必要があります。                                                                                                                                                                                                                                |
| Braze REST APIキー      | 以下の権限を持つBraze REST APIキー：`users.track`、`users.alias.new`、`users.identify`、`users.export.ids`、`users.merge`、`users.external_ids.rename`、および`users.alias.update`。<br><br> Brazeダッシュボードの**「設定」**>**「APIキー」**から作成できます。 |
| Braze REST エンドポイント     | [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

### パーソナライズされたアクションベースの配信
Snowplowがデフォルトで収集する多数のリッチなイベントのいずれかを使用するか、カスタムイベントを定義して、ビジネスに適したより細かなカスタマージャーニーを形成できます。Snowplowの豊富な行動データを活用して顧客ファネルを設計し、マーケティングおよび製品チームの価値を引き出し、Brazeを通じてコンバージョンと製品使用を最大化するのに役立てましょう。

### ダイナミックなセグメンテーション
Snowplowの高品質な行動データに基づいてBrazeでダイナミックなオーディエンスを作成できます。ユーザーが製品、アプリ、またはWeb サイトでアクションを実行すると、Snowplowが収集するリアルタイムの行動データを活用して、Brazeの関連セグメントにユーザーを自動的に追加または削除できます。

## 統合

### ステップ 1: Snowplow Consoleで送信先を設定する

イベントフォワーダーを作成するには：

1. Snowplow Consoleで、**Destinations**に移動し、**Create new destination**を選択します。
2. 接続を設定する際、接続タイプに**Braze**を選択します。
3. Braze APIキーとREST APIエンドポイントを入力します。
4. 接続を保存します。

### ステップ 2: イベントフォワーダーを設定する

フォワーダーを設定する際、転送するSnowplowイベントを選択し、Brazeオブジェクトタイプにマッピングできます：

1. **[ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object)**：ユーザープロファイルデータとカスタムユーザープロパティを更新します。
2. **[カスタムイベント]({{site.baseurl}}/api/objects_filters/event_object)**：ユーザーのアクションや行動を送信します。
3. **[購入]({{site.baseurl}}/api/objects_filters/purchase_object)**：商品詳細を含む取引データを送信します。

オブジェクトタイプごとに、フィールドマッピングを設定して、SnowplowイベントデータをBrazeフィールドにマッピングする方法を指定できます。詳細なセットアップ手順とフィールドマッピングの設定については、Snowplowの[Creating forwardersドキュメント](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/)を参照してください。

### ステップ 3: 統合を検証する

Brazeアカウントで以下のページを確認し、イベントがBrazeに届いていることを検証します：

1. **クエリビルダー**：Brazeで、**「分析」**>**「Query Builder」**に移動します。Snowplowから転送されたデータをプレビューするために、以下のテーブルに対してクエリを記述できます：`USER_BEHAVIORS_CUSTOMEVENT_SHARED`と`USERS_BEHAVIORS_PURCHASE_SHARED`。
2. **API利用ダッシュボード**：Brazeで、**「設定」**>**「APIと識別子」**に移動すると、API使用量の時系列チャートを確認できます。Snowplowが使用しているAPIキーでフィルタリングし、成功と失敗の両方を確認できます。

## カスタムプロパティの送信

標準フィールド以外にもカスタムプロパティを送信できます。その構造は、使用しているBrazeオブジェクトタイプによって異なります：

- **ユーザー属性**：トップレベルフィールドとして追加します（例：`subscription_tier`、`loyalty_points`）
- **イベントプロパティ**：`properties`オブジェクトの下にネストします（例：`properties.plan_type`、`properties.feature_flag`）
- **購入プロパティ**：`properties`オブジェクトの下にネストします（例：`properties.color`、`properties.size`）

スペースを含むプロパティ名には、ブラケット表記を使用します（例：`["account type"]`や`properties["campaign source"]`）。

サポートされるデータタイプ、プロパティ命名要件、ペイロードサイズ制限の詳細については、[イベントオブジェクトのドキュメント]({{site.baseurl}}/api/objects_filters/event_object)を参照してください。

## 制限事項

**レート制限：** Brazeは、Track Users APIに対して3秒ごとに3,000 APIコールのレート制限を適用しています。Snowplowはイベントフォワーダーのバッチ処理をサポートしていないため、このAPIレート制限はイベントレート制限としても機能します。入力スループットが3秒間に3,000イベントを超えると、レイテンシーが増大する可能性があります。