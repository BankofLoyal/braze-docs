---
nav_title: オーディエンス同期について
article_title: オーディエンス同期について
alias: /partners/about_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to Facebook を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 0
Tool:
  - Canvas

---

# オーディエンス同期について

> Braze のオーディエンス同期機能は、多くのトップソーシャルテクノロジーおよび広告テクノロジーにキャンペーンのリーチを拡大するのに役立ちます。[Braze キャンバス]({{site.baseurl}}/user_guide/engagement_tools/canvas)を通じて、ブランドはファーストパーティのユーザーデータを広告エコシステムにダイナミックかつ安全に同期させ、マーケティングと運用の効率化を推進できます。

## 機能の利用について

Braze をご利用のすべてのお客様は、Audience Sync to Google と Audience Sync to Facebook をすぐに利用できますが、メッセージクレジットを使用するお客様はすべての Audience Sync パートナーにアクセスできます。追加の Audience Sync 送信先をロック解除するには、Audience Sync Pro を購入してください。詳細については、Braze のアカウントマネージャーにお問い合わせください。

## ユースケース

- 所有チャネルと有料チャネルを利用して高価値のユーザーをターゲティングし、購買やエンゲージメントの増加を図ります。
- 新規ユーザーの獲得コストとコンバージョンを最適化するために、価値の高いユーザーの類似オーディエンスを作成します。
- 他のマーケティングチャネルで反応が低いユーザーを広告でリターゲティングします。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成します。

## 概要

<style>
table td {
    word-break: break-word;
}
</style>

| 送信先 | オーディエンスメンバーのマッチにかかる時間 | レート制限 | 類似または類似行動 | ヒント |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | 最長 24 時間 | 1分あたり 250,000 リクエスト。Google のフィードバックに基づく自動リトライで、5 秒ごとにバッチ処理されます。 | はい | {::nomarkdown}<ul><li>Criteo は最大 1,000 件の広告オーディエンスに対応します。</li><li>最小オーディエンスサイズは 500 人、推奨は 20,000 人以上です。</li></ul>{:/} |
| [Facebook または Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | 最長 24 時間 | 毎時 190,000 件の広告アカウント | はい | {::nomarkdown}<ul><li>Facebook は最大 500 の広告オーディエンスに対応します。</li><li>Facebook のオーディエンスは 1,000 ユーザー以上にする必要があります。</li></ul>{:/} |
| [Google 広告または YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | 6 ～ 12 時間 | Google のフィードバックに基づく自動リトライで、5 秒ごとにバッチ処理されます。 | いいえ | {::nomarkdown}<ul><li><b>カスタマーマッチ:</b>モバイル広告、メールアドレス、電話番号のいずれかを使用します。</li><li>Google オーディエンスでの広告配信の開始には、5,000 人以上のユーザーが必要です。</li><li>ユーザー数が 1,000 人以上になるまでは、オーディエンスサイズはゼロと表示されます。</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48 時間 | LinkedIn は毎秒 10 件のクエリを処理し、リクエスト 1 件あたり 100,000 ユーザーを処理します。Braze は 5 秒ごとにユーザーをバッチ処理します。 | AI 予測オーディエンス | {::nomarkdown}<ul><li>ロケーションターゲティングを考慮した場合、オーディエンスの最小サイズは 300 人です。</li><li>LinkedIn は Braze ダッシュボードにマッチ率を表示します。</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | 24 ～ 48 時間 | Pinterest は毎秒 7 件のクエリを処理し、リクエスト 1 件あたり 1,900 ユーザーを処理します。Braze は 5 秒ごとにユーザーをバッチ処理します。 | はい | Pinterest のオーディエンスには 100 人以上のユーザーが必要です。 |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | N/A | Snapchat は毎秒 10 件のクエリを処理し、リクエスト 1 件あたり 100,000 ユーザーを処理します。Braze は 5 秒ごとにユーザーをバッチ処理します。 | はい | Snapchat は最大 1,000 の広告オーディエンスに対応します。 |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | 24 ～ 48 時間 | TikTok は毎秒 50 件のクエリを処理し、リクエスト 1 件あたり 10,000 ユーザーを処理します。Braze は 5 秒ごとにユーザーをバッチ処理します。 | はい | {::nomarkdown}<ul><li>TikTok は最大 400 の広告オーディエンスに対応します。</li><li>TikTok オーディエンスでの広告配信の開始には、1,000 人以上のユーザーが必要です。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>レート制限に達すると、Braze は 13 時間にわたって同期を再試行します。</sup>

## 仕組み

Audience Sync to Google または Audience Sync to Facebook を使用するには、[**テクノロジーパートナー**] ページでパートナーを検索して、広告アカウントを接続します。

![Facebook のテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google 広告のテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

広告アカウントの接続後に、オーディエンス同期ステップを含むキャンバスを作成できます。

![キャンバスコンポーネントメニューを使用して、ユーザージャーニーにオーディエンス同期ステップを追加します。]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![オーディエンス同期ステップでオーディエンス同期パートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

パートナーごとに、オーディエンス同期ステップの一部として次の内容を設定する必要があります。 

- 広告アカウント
- オーディエンス 
- ユーザーを追加または削除するアクション 
- マッチするフィールド 

キャンバス内でユーザーがオーディエンス同期ステップに入るとすぐに、Braze によりユーザーが同期されることに注意してください。 

オーディエンス同期の送信先ごとに、パートナーの送信可能なフィールドに関する要件が異なる場合があります。詳細については、特定のパートナーのドキュメントを参照してください。 

### Audience Sync Pro

TikTok、Pinterest、Snapchat、Criteo などの Audience Sync Pro パートナーを使用するには、[**テクノロジーパートナー**] ページの [**Audience Sync Pro**] セクションで Audience Sync Pro の購入割り当てに基づいてパートナーを選択できます。

![パートナーが未選択の Audience Sync Pro。]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

最初に [パートナーを選択] を選択して、使用するパートナーを選択します。Audience Sync Pro を購入すると、1 回の購入につき 3 つの Audience Sync Pro 送信先が割り当てられます。これは、ダッシュボードの各ワークスペース内で使用可能になります。

![Braze に接続するパートナーを 3 社まで選択できるオプション。]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Audience Sync Pro 送信先を選択したら、パートナータイルをクリックして、選択したパートナーの広告アカウントを接続します。

![オーディエンス同期のパートナーに選ばれた Snapchat と TikTok の例。]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Snapchat オーディエンス同期設定。メッセージ「Snapchat の 1 件のアカウントに正常に接続されました」を表示。]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

最後に、この Audience Sync Pro 送信先を使用して、キャンバスでオーディエンス同期ステップを作成します。

### オーディエンス同期エラーメール

エラーがパートナー連携全体に関連している場合（許可の問題など）、連携を接続したユーザーにメールが届きます。そのユーザーがもう存在しない場合は、管理者がメールを受け取ります。 

エラーがキャンバスのオーディエンス同期コンポーネントの問題（「オーディエンスが存在しない」など）に関連している場合、キャンバスを設定したユーザーにメールが届きます。そのユーザーがもう存在しない場合は、会社の管理者にフォールバックされます。

これらのメールの受信者を設定するには、カスタマーサクセスマネージャーに連絡し、[**通知設定**] で受信者を追加してください。この機能は現在の動作を変更するため、Braze のデフォルトでは誰もオプトインされません。エラーメールを見逃さないよう、すぐにこの新しい通知設定に受信者を追加する必要があります。

## データプライバシーに関する考慮事項

{% alert important %}
本書は、法的助言を提供することを意図したものではなく、また法的助言を提供するものとして依拠することもできません。オーディエンス同期の使用には、特定の法的要件が適用されます。適用されるすべての法律を遵守して使用していることを確認するために、法律顧問の助言を求めてください。
{% endalert %}

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また [CCPA](https://oag.ca.gov/privacy/ccpa) に基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合があります。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げます。

[Braze SDK で iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) を収集した場合、「広告トラッキングが有効」フィルターを使用できます。ユーザーがオプトインしたオーディエンス同期の送信先にのみユーザーを送信するには、値を `true` に選択します。

![エントリオーディエンスが「Ad Tracking Enabled is true」のキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![エントリオーディエンスが「opted_in_marketing equals true」のキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Braze プラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

## 広告ターゲティングの同意の管理

広告主として、ユーザーの広告トラッキングやターゲティングに対する同意を管理する責任を負います。

ユーザーに広告を配信するには、適用されるすべての法律と規制、および広告プラットフォームのポリシーと要件を遵守する必要があります。ユーザーの同意を得た場合にのみ、Braze を使用してユーザーのターゲティングと同期を行ってください。 

これらの広告プラットフォームのオーディエンスリストを最新の状態に保ち、同意を取り消したユーザーを削除するには、オーディエンス同期ステップを使用して、これらの既存のオーディエンスリストからユーザーを削除するキャンバスを設定します。