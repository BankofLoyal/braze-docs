---
nav_title: イベント配信のセマンティクス
article_title: イベント配信のセマンティクス
page_order: 3
page_type: reference
description: "このリファレンス記事では、データウェアハウスストレージパートナーに送信するフラットファイルのイベントデータを Currents がどのように管理するかを概説および定義します。"
tool: Currents

---

# イベント配信のセマンティクス

> このページでは、データウェアハウスストレージパートナーに送信するフラットファイルのイベントデータを Currents がどのように管理するかを概説および定義します。

データストレージ用の Currents は、弊社のプラットフォームから、データウェアハウスの[パートナー接続]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)の 1 つにあるストレージバケットに送信されるデータの連続ストリームです。Currents は、通常のしきい値に達するとストレージバケットに Avro ファイルを書き込むので、独自のビジネスインテリジェンス (BI) ツールセットを使用してイベントデータの処理および分析ができます。

{% alert important %}
このコンテンツは、**データウェアハウスストレージパートナー (Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage) に送信するフラットファイルのイベントデータにのみ適用されます**。<br><br>他のパートナーに適用されるコンテンツについては、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。
{% endalert %}

## テストイベント

Currents の統合を設定する際は、ストレージバケットとの接続を確認するために**「テストイベントを送信」**をクリックしてください。これらのテストイベントは、統合がデータを正しく受信し処理できることを検証するものです。

{% alert important %}
**テストイベントデータ形式：**テストイベントには、各フィールドの正しいデータタイプに合致するプレースホルダー値が含まれていますが、現実的または正確なデータは含まれていません。例えば、`timezone` フィールドには有効なタイムゾーン識別子（「America/Chicago」など）ではなく UUID のような文字列が含まれている場合があります。また、`campaign_name` や `ip_pool` といった他のフィールドも、実際のデータではなくプレースホルダー値を含んでいることがあります。<br>

これは想定どおりの動作です。テストイベントは主に接続と統合設定のテストを目的としており、データの正確性を検証するためのものではありません。正確なデータを含む実際のイベントを確認するには、テスト用の Currents 統合を使用し、実際のイベントデータをパイプライン経由で送信してください。
{% endalert %}

## 1 回以上の配信

Currents は高スループットのシステムであるため、「1回以上」のイベント配信を保証します。つまり、ストレージバケットにイベントが重複して書き込まれることがまれにあります。これは、何らかの理由でキューからイベントが再処理された場合に発生します。

ユースケースで「厳密に1回」の配信が必要な場合は、イベントとともに送信されるユニーク識別子フィールド (`id`) を使用して、重複するイベントを除外できます。ファイルはストレージバケットに書き込まれた時点で弊社の管理下から離れるため、弊社側で重複排除を保証する方法はありません。

## タイムスタンプ

Currents がエクスポートするすべてのタイムスタンプは、UTC タイムゾーンで送信されます。一部のイベントでは、タイムゾーンフィールドも含まれます。これは、インターネット番号割当機構 (IANA) のフォーマットで、イベント発生時点でのユーザーのローカルタイムゾーンを提供します。

### レイテンシー

SDK または API を介して Braze に送信されたイベントには、過去のタイムスタンプが含まれていることがあります。最も顕著な例は、モバイル接続がない場合など、SDK データがキューに入れられるケースです。その場合、イベントのタイムスタンプは、そのイベントが生成された時点を反映します。つまり、イベントの一部はレイテンシーが大きいように見えることがあります。

## Apache Avro 形式

Braze Currents のデータストレージ統合では、`.avro` 形式でデータが出力されます。弊社が [Apache Avro](https://avro.apache.org/) を選択した理由は、スキーマの進化をネイティブにサポートし、さまざまなデータ製品でサポートされている柔軟なデータ形式だからです。 

- Avro は、ほぼすべての主要なデータウェアハウスでサポートされています。
- S3 にデータを残す場合、Avro は CSV や JSON より圧縮率が高いため、ストレージコストを削減でき、データ解析に使用する CPU も少なくて済む可能性があります。
- Avro ではデータの書き込みや読み取りにスキーマが必要です。スキーマは時間の経過とともに進化させることができ、既存の構造を壊すことなくフィールドの追加に対応できます。

Currents は、以下の形式で各イベントタイプのファイルを作成します。

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
スクロールバーがあるためにコードが見えない場合は、その解決方法を[こちら]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)で確認してください。
{% endalert %}

例えば、プッシュ送信イベントのパスは以下のようになります。

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

`version` パスセグメントは、`version=6` のようなシンプルな整数の Currents バージョン値です。

|ファイル名セグメント |定義|
|---|---|
| `<your-bucket-prefix>` | この Currents 統合のために設定されたプレフィックス。 |
| `<cluster-identifier>` | Braze 内部で使用されます。「prod-01」、「prod-02」、「prod-03」、「prod-04」などの文字列になります。すべてのファイルは同じクラスタ識別子を持ちます。|
| `<connection-type-identifier>` | 接続タイプの識別子。オプションは「S3」、「AzureBlob」、または「GCS」です。 |
| `<integration-id>` | この Currents 統合のユニーク ID。 |
| `<event-type>` | ファイル内のイベントタイプ。 |
| `<date>` | UTC タイムゾーンでイベントが処理のためにシステムのキューに入れられた時間。形式は YYYY-MM-DD-HH です。 |
| `version=<currents_version>` | パイプラインパスの Currents バージョン。この値は `6` のようなシンプルな整数です。 |
| `<environment>` | Braze 内部で使用されます。 |
| `<partition>` | Braze 内部で使用されます。整数。 |
| `<offset>`| Braze 内部で使用されます。整数。同一時間内に送信された異なるファイルは、異なる `<offset>` パラメーターを持つことに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
ファイルの命名規則は変更される可能性があります。Braze は、バケット内のプレフィックスが &lt;your-bucket-prefix&gt; で始まるすべてのキーを検索することを推奨します。
{% endalert %}

### Avro の書き込みしきい値

通常の場合、Braze は 5 分またはイベント 15,000 件のいずれか早い方に達するたびに、ストレージバケットにデータファイルを書き込みます。高負荷時には、1 ファイルあたり最大 100,000 件のイベントを含む大きなデータファイルを書き込むことがあります。

{% alert important %}
Currents は空のファイルを書き込むことはありません。
{% endalert %}

### Avro スキーマの変更

Braze では、フィールドの追加、変更、または削除に伴って、Avro スキーマを変更することがあります。ここでは、破壊的変更と非破壊的変更の 2 つのタイプがあります。すべての場合において、スキーマが更新されたことを示すために Currents パスのバージョンが増分されます。Azure Blob Storage、Google Cloud Storage、および Amazon S3 に書き込まれる Currents イベントは、パスに `version=<currents_version>` として記録されます。例: `<your-bucket-prefix>/.../event_type=<event-type>/date=<date>/version=6/<environment>/...`

#### 非破壊的な変更

Avro スキーマにフィールドが追加された場合は、非破壊的な変更と見なします。追加されたフィールドは常に Avro の「オプション」フィールド（デフォルト値 `null` を持つものなど）になるため、[Avro スキーマ解決仕様](http://avro.apache.org/docs/current/spec.html#schema+resolution)に従って古いスキーマと「一致」します。このフィールドは ETL プロセスに追加されるまで単に無視されるため、これらの追加は既存の ETL（Extract, Transform, and Load）プロセスに影響を与えないはずです。 

{% alert important %}
新規フィールドが追加されたときにフローが破損しないように、ETL の設定で処理するフィールドを明示的に指定することをお勧めします。
{% endalert %}

弊社はすべての変更について事前に通知するよう努めていますが、非破壊的な変更はいつでもスキーマに含める可能性があります。

#### 破壊的な変更

Avro スキーマからのフィールドの削除や変更は、破壊的な変更と見なされます。破壊的な変更では、使用されていたフィールドが意図どおりに記録されなくなる可能性があるため、既存の ETL プロセスの修正が必要になることがあります。

スキーマに対する破壊的な変更はすべて、変更前に事前通知されます。