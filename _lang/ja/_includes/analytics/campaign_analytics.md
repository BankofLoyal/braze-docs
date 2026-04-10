## 分析を表示する

キャンペーンを開始したら、そのキャンペーンの詳細ページに戻って主要な指標を確認できます。**キャンペーン**ページに移動し、キャンペーンを選択して詳細ページを開きます。{% if include.channel != "banner" %}{% if include.channel == "Content Card" %}コンテンツカード{% elsif include.channel == "banner" %}バナー{% elsif include.channel == "email" %}メール{% elsif include.channel == "in-app message" %}アプリ内メッセージ{% elsif include.channel == "KakaoTalk" %}KakaoTalk メッセージ{% elsif include.channel == "push" %}プッシュメッセージ{% elsif include.channel == "SMS" %}SMS メッセージ{% elsif include.channel == "whatsapp" %}WhatsApp メッセージ{% elsif include.channel == "webhook" %}webhook {% endif %}をキャンバスで送信した場合は、[キャンバス分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)を参照してください。{% endif %}

{% alert tip %}
レポートに記載されている用語や指標の定義をお探しですか？以下を参照してください。
  {% if include.channel == "email" %}[メール分析用語集]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "banner" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)でバナーによるフィルタリングを行ってください。
  {% elsif include.channel == "Content Card" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)でコンテンツカードによるフィルタリングを行ってください。
  {% elsif include.channel == "in-app message" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)でアプリ内メッセージによるフィルタリングを行ってください。
  {% elsif include.channel == "push" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)でプッシュによるフィルタリングを行ってください。
  {% elsif include.channel == "SMS" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)で SMS/MMS および RCS によるフィルタリングを行ってください。
  {% elsif include.channel == "whatsapp" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)で WhatsApp によるフィルタリングを行ってください。
  {% elsif include.channel == "webhook" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)で Webhook によるフィルタリングを行ってください。{% endif %}
{% endalert %}

**キャンペーン分析**タブから、一連のパネルでレポートを確認できます。以下のセクションに記載されているものより多い場合も少ない場合もありますが、それぞれに有用な目的があります。

### 期間

**キャンペーン分析**の期間設定は、デフォルトで現在時刻から過去90日間を表示します。これは、キャンペーンが90日以上前に開始された場合、指定した期間の分析データが「0」と表示されることを意味します。古いキャンペーンの全分析データを表示するには、レポートの時間範囲を調整してください。

### キャンペーンの詳細

**キャンペーンの詳細**パネルには、
  {% if include.channel == "banner" %}バナー
  {% elsif include.channel == "Content Card" %}コンテンツカード
  {% elsif include.channel == "email" %}メール
  {% elsif include.channel == "in-app message" %}アプリ内メッセージ
  {% elsif include.channel == "KakaoTalk" %}KakaoTalk メッセージ
  {% elsif include.channel == "push" %}プッシュメッセージ
  {% elsif include.channel == "SMS" %}SMS、MMS、RCS
  {% elsif include.channel == "whatsapp" %}WhatsApp メッセージ
  {% elsif include.channel == "webhook" %}Webhook
  {% endif %}の全体的なパフォーマンスのハイレベルな概要が表示されます。

このパネルでは、受信者に送信されたメッセージの数、1次コンバージョン率、このメッセージによって生み出された総収益などの全体的な指標を確認できます。このページから、配信、オーディエンス、コンバージョン設定を確認することもできます。

{% if include.channel == "whatsapp" %}
{% alert note %}
WhatsApp チャネルには既読率が含まれます。この指標は既読通知をオンにしているユーザーにのみ配信されるため、値は異なる場合があります。
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_iam.png %})

キャンバスでは、作成したキャンバスにアプリ内メッセージのパフォーマンスがマッピングされます。ページ上部のコントロールパネルを使用して、他のメッセージングタイプ（チャネル）をクリアし、キャンバス内のアプリ内メッセージのみを表示できます。

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![キャンペーンの詳細セクション。]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### コントロールグループ {#cc-control-group}

個々のコンテンツカードの影響を測定するには、A/B テストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントの指標は含まれません。

{% elsif include.channel == "SMS" %}

#### コントロールグループ {#sms-control-group}

個々の SMS、MMS、または RCS メッセージの影響を測定するには、A/B テストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントの指標は含まれません。

{% elsif include.channel == "whatsapp" %}

#### コントロールグループ {#whatsapp-control-group}

個々の WhatsApp メッセージの影響を測定するには、A/B テストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントの指標は含まれません。

{% elsif include.channel == "webhook" %}

#### コントロールグループ {#webhook-control-group}

個々の Webhook メッセージの影響を測定するには、A/B テストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントの指標は含まれません。

{% endif %}

#### 最後に表示してからの変更

チームの他のメンバーによるキャンペーンへの更新数は、キャンペーン概要ページの*最後に表示してからの変更*指標で追跡されます。**最後に表示してからの変更**を選択すると、キャンペーンの名前、スケジュール、タグ、メッセージ、オーディエンス、承認ステータス、またはチームアクセス設定の更新に関する変更ログを表示できます。各更新について、誰がいつ更新を行ったかを確認できます。この変更ログを使用してキャンペーンの変更を監査できます。

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### コンテンツカードのパフォーマンス

**コンテンツカードパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コンテンツカードのメッセージパフォーマンス分析]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### メールのパフォーマンス

**メールパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![メールメッセージのパフォーマンス分析]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### アプリ内メッセージのパフォーマンス

**アプリ内メッセージパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![アプリ内メッセージのパフォーマンス分析]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### プッシュのパフォーマンス

**プッシュパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![プッシュメッセージのパフォーマンス分析]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCS のパフォーマンス

**SMS/MMS/RCS パフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コントロールグループ、バリアント1、バリアント2の指標テーブルを含む SMS/MMS/RCS パフォーマンスパネル。]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### バナーのパフォーマンス

**バナーパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。これらの指標は、メッセージングチャネルや多変量テストを実施しているかどうかによって異なります。

![コントロールグループ、バリアント1、バリアント2の指標テーブルを含む SMS/MMS パフォーマンスパネル。]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### KakaoTalk のパフォーマンス

**KakaoTalk パフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

{% elsif include.channel == "webhook" %}
### Webhook のパフォーマンス

**Webhook パフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コントロールグループとバリアント1の指標テーブルを含む Webhook パフォーマンスパネル。]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp のパフォーマンス

**WhatsApp パフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![バリアント1の指標テーブルを含む WhatsApp パフォーマンスパネル。]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

表示を簡素化する場合は、<i class="fas fa-plus"></i>**列を追加/削除**をクリックし、必要に応じて指標をクリアします。デフォルトでは、すべての指標が表示されます。

{% if include.channel == "email" %}

#### ヒートマップ

ヒートマップを使用すると、1つのメールキャンペーン内の異なるリンクがどの程度成功したかを確認できます。**メッセージ分析**セクションから、**メールパフォーマンス**パネルに移動します。**プレビューとヒートマップ**を選択して、メールキャンペーンとヒートマップのプレビューを表示します。または、バリアント名のハイパーリンクを選択してヒートマップを表示することもできます。

このビューでは、**ヒートマップ表示**トグルを使用して、キャンペーンの存続期間中のクリックの全体的な頻度と場所を示すメールのビジュアルビューを表示できます。**合計クリック数によるリンクテーブル**パネルでは、メールキャンペーン内のすべてのリンクを表示し、合計クリック数で並べ替えることができます。これにより、ユーザーがどこに移動しているかについて追加のインサイトが得られます。参照用にヒートマップのコピーを保存するには、ダウンロードボタンを選択します。

![メールキャンペーンと、リンクエイリアスの例とその合計クリック数を示すパネルを含むプレビューとヒートマップページの例。]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### 画像

ヒートマップのプレビューやエクスポートで画像が壊れるのを防ぐために、画像 URL の CORS を有効にすることをお勧めします。

エクスポートで画像が欠落している場合は、開発者と協力して画像アセットがクロスオリジンアクセスを許可するようにしてください。サーバーは `Access-Control-Allow-Origin` ヘッダーに `*` または Braze ダッシュボードのドメインを返す必要があります。

{% endif %}

{% if include.channel == "Content Card" %}

#### コンテンツカードの指標

以下は、メッセージのパフォーマンスを確認する際に表示される主な指標の内訳です。すべてのコンテンツカード指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照し、コンテンツカードでフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">送信済みメッセージ</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                この計算方法は、
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">カード作成</a>で選択した内容によって異なります：<br><br>
                <ul>
                    <li><b>開始時またはステップエントリ時：</b>作成され、閲覧可能なカードの数です。ユーザーがカードを閲覧したかどうかはカウントされません。</li>
                    <li><b>最初のインプレッション発生時：</b>ユーザーに表示されたカードの数です。</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 同じユーザーに対して複数回増加する可能性があります。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">このカウントは、</span>ユーザーがコンテンツカードを2回目に閲覧しても増加しません。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">ユニーク受信者数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> ユーザーは毎日ユニーク受信者になり得るため、<i>ユニークインプレッション数</i>よりもこの数値が高くなることが想定されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">ユニーククリック数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これには Braze が提供する配信停止リンクのクリックも含まれます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">ユニーク却下数</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
インプレッションの記録方法については、Web、Android、iOS で若干のニュアンスの違いがあります。一般的に Braze は、ユーザーがフィード内の特定のコンテンツカードまでスクロールした後、カードが表示されたときにインプレッションを記録します。
{% endalert %}

#### ユニーク受信者数とユニークインプレッション数

メッセージの可視性をカバーする指標がいくつかあります。これには_ユニーク受信者数_と_ユニークインプレッション数_が含まれます。これらの指標をよりよく理解するために、いくつかのシナリオ例を見てみましょう。

例えば、今日コンテンツカードを閲覧し、翌日に同じキャンペーンから新しいカードを受け取り、さらにその翌日にも受け取った場合、_ユニーク受信者_として3回カウントされます。ただし、_ユニークインプレッション_は1回のみカウントされます。また、カードがデバイスで利用可能であったため、_送信済みメッセージ_の数にもカウントされます。

別の例として、15万件の_送信済みメッセージ_を示すコンテンツカードキャンペーンで5件の_ユニークインプレッション_があるとします。これは、カードが（バックエンドで）15万人のオーディエンスに利用可能になったものの、その送信後に以下のステップをすべて実行したのはわずか5人のユーザーのデバイスだけだったことを意味します：

1. セッションを開始した、またはアプリが明示的にコンテンツカードの同期を要求した（またはその両方）
2. コンテンツカードビューに移動した
3. SDK がインプレッションを記録し、サーバーにログを送信した

_送信済みメッセージ_は閲覧可能なコンテンツカードを指し、_ユニーク受信者_は実際に閲覧されたコンテンツカードを指します。

{% elsif include.channel == "banner" %}

### バナー指標

これらは、バナーキャンペーンのパフォーマンスを確認する際に追跡すべき重要な指標です。バナーのクリック数とインプレッション数は SDK で自動的に追跡されます。

すべてのバナー指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照し、バナーでフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} バナーの場合、インプレッションはユーザーセッションごとに1回記録されます。同じセッション内で同じバナーが複数回表示された場合、インプレッションは1回のみ記録されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">各ユーザーは1回のみカウントされます。</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">クリック数の合計</a></td>
            <td class="no-split"><i>クリック数の合計</i>は、同じユーザーが複数回クリックしたかどうかにかかわらず、配信されたメッセージ内でクリックしたユーザーの総数（および割合）です。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">ユニーククリック数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} 各ユーザーは1回のみカウントされます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">1次コンバージョン数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">ユニーク受信者数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> 閲覧者は毎日ユニーク受信者になり得るため、<i>ユニークインプレッション数</i>よりもこの数値が高くなることが想定されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">収益</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">信頼度</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### バナー指標の計算例

メッセージの可視性をカバーする指標がいくつかあります。これには_ユニーク受信者数_と_ユニークインプレッション数_が含まれます。これらの指標をよりよく理解するために、いくつかのシナリオ例を見てみましょう。

例えば、今日バナーを閲覧し、翌日に同じバナーを閲覧し、さらにその翌日にも閲覧した場合、_ユニーク受信者_として3回カウントされます。ただし、_ユニークインプレッション_は1回のみカウントされます。

別の例として、バナーキャンペーンで5件の_ユニークインプレッション_があるとします。これは、以下のすべてのステップを実行したユーザーのデバイスがわずか5台だったことを意味します：

1. セッションを開始した、またはアプリが明示的にバナーの同期を要求した（またはその両方）
2. バナービューに移動した
3. SDK がインプレッションを記録し、サーバーにログを送信した

_ユニーク受信者_は、実際に閲覧されたバナーを指します。

{% elsif include.channel == "email" %}

#### メール指標

他のチャネルでは見られない、メール固有の主な指標をいくつか紹介します。Braze で使用されるすべてのメール指標の完全な定義については、[メール分析用語集]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)を参照してください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">ユニーククリック数</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これはメールについて7日間の期間で追跡され、<a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> によって測定されます。これには Braze が提供する配信停止リンクのクリックも含まれます。この数値は5〜10%の範囲が目安です。10%を超える場合は非常に優秀です！
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">ユニーク開封数</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} メールについては、7日間の期間で追跡されます。この数値は30〜40%の範囲が目安です。40%を超える場合は非常に優秀です！
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">クリック開封率</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">スパム率</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} この指標が0.08を超える場合、メッセージの文面が売り込み色が強すぎるか、メールアドレスの収集方法を見直す必要がある（メッセージの受信を希望しているユーザーに送信しているか確認する）兆候かもしれません。
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">配信停止数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">その他の開封数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">推定実質開封数</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} 詳細は次のセクションを参照してください。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">マシン開封数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">バウンス数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">ハードバウンス</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">ソフトバウンス</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">延期</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### 配信とバウンス

ダッシュボードでは_ハードバウンス_が強調表示されます。一部の_バウンス_はソフトバウンスの場合があり、その数だけでは一致しません。ソフトバウンスは以下の計算式で概算できます：

_送信数 −（配信数 + ハードバウンス数）≈ ソフトバウンス数_

_配信数_は再試行が成功するにつれて最初の72時間で増加する可能性がありますが、1回限りの送信の場合、_送信数_とハードバウンス数は送信完了後に固定されます。

##### 開封イベントなしのクリック

開封トラッキングピクセルが読み込まれない場合、開封なしでクリックが記録されることがあります。例えば、Gmail でメッセージがクリップされた場合や、ユーザーが画像を無効にしている場合（開封ピクセルは通常フッターにあります）です。一部のクライアントは画像をプロキシ経由で取得するため（Apple Mail など）、ユーザーがメールを読んだときではなく、サーバーが最初にピクセルを取得したときに開封が記録される場合があります。企業ドメインではデフォルトで画像がブロックされていることが多いです。

クリックと開封が異なる日に記録されることもあります。ユーザーが5月16日に画像オフの状態でクリックし（開封なし）、5月17日にウェブメールで開封する（その時点で開封が記録される）場合があります。

##### 延期

延期（Deferred/Deferral）とは、メールがすぐに配信されなかったものの、Braze がこの一時的な配信エラーの後、配信成功の可能性を最大化するために最大72時間再試行を行い、その特定のキャンペーンの試行が停止されることを指します。延期の一般的な理由には、受信トレイプロバイダーからのレピュテーションに基づくメールボリュームのレート制限、一時的な接続の問題、DNS エラーなどがあります。

_延期_は_ソフトバウンス_とは異なります。この再試行期間中にメールが正常に配信されなかった場合、Braze は送信されたキャンペーンごとに1つのソフトバウンスイベントを送信します。2025年2月25日以前は、これらの再試行は1回のキャンペーン送信に対して複数のソフトバウンスとしてカウントされていました。

_延期_は現在、Currents または Braze Snowflake 機能（Query Builder、SQL Segment、Snowflake Data Sharing など）を使用した場合のみ利用可能です。キャンペーンやキャンバスの分析にこれを含めたい場合は、[製品フィードバックを送信]({{site.baseurl}}/user_guide/administrative/access_braze/portal)してください。

##### 推定実質開封率 {#estimated-real-open-rate}

この統計は、Braze が独自に作成した分析モデルを使用して、マシン開封が存在しないかのようにキャンペーンのユニーク開封率の推定値を再構築するものです。一部の開封イベントについてメール送信者から*マシン開封*というラベルを受け取る場合がありますが（上記参照）、これらのラベルは実際の開封をマシン開封と誤って分類することが多いです。つまり、*その他の開封数*は（実際のユーザーによる）実際の開封を過小評価している可能性が高いです。代わりに、Braze は各キャンペーンのクリックデータを使用して、実際の人間がメッセージを開封した率を推測します。これにより、Apple の MPP を含むさまざまなマシン開封メカニズムが補われます。

_推定実質開封率_はメール送信開始から36時間後に算出され、その後24時間ごとに再計算されます。キャンペーンが繰り返される場合、推定は別の送信が発生してから36時間後に再計算されます。

この指標は継続的に再計算されるため、_推定実質開封率_の値は時間の経過とともに変化する可能性があります。新しいエンゲージメントシグナル（開封やクリックなど）が受信され、モデルに組み込まれるにつれて値は変動します。実際には、_推定実質開封率_はキャンペーンがアクティブな間、毎日更新され続けることがあります。

通常、統計を正常に計算するには配信済みメールが約10,000通必要ですが、この数はクリック率によって異なります。統計が計算できない場合、その列には「--」と表示されます。

###### 制限事項

推定実質開封率はキャンペーンでのみ利用可能で、Currents のイベントではレポートされません。この指標は、2023年11月14日以前に開始されたアクティブキャンペーンにのみ遡及して算出されます。

##### クリック率の増加に対応する

開封率は、メールキャンペーンを追跡するための有益な指標です。ただし、これらの開封率は、メールキャンペーンに対する人間のエンゲージメントを必ずしも正確に示す指標ではありません。定義上、開封イベントはユーザーがメールを開封したときに発生し、透明な開封トラッキングピクセルが正常にダウンロードされたことを意味します。

さらに、セキュリティスキャンツールの使用により開封率が膨張する可能性があります。これらのツールの中には、リンクをクリックしてその正当性を確認することで、受信メールに悪意のあるコンテンツが含まれていないかスキャンしてユーザーを保護するものがあります。これらのクリックは「ボットクリック」または「非人間的インタラクション」（NHI）と呼ばれることがあります。

結局のところ、メールが当社のサーバーを離れた後は、その後何が起きるかについて把握できる範囲は限られていますが、結果に影響する NHI を管理するための推奨事項は以下の通りです：

1. この事象はすべての送信者とほぼすべての受信者に発生する可能性があることに注意してください。クリック数は開封数と同様に、メッセージに対する人間のインタラクションを示す完全に信頼できる指標ではないため、NHI を防ぐことはできません。
2. より高いポジティブなエンゲージメントは、より低い NHI と相関する傾向があるため、メールメッセージングの[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)に従うことが重要です。これには、ユーザーからメール送信の明示的な許可を得ることや、エンゲージメントのないサブスクライバーを定期的に Sunsetting (配信停止) することが含まれます。
3. 可能な限り、メールに HTTPS リンクを使用してください。NHI は安全なリンクを使用する送信者に対してはそれほど一般的に発生しません。
4. ワンクリックで配信停止できる仕組みを使用している場合は、ユーザーが通知設定を編集・管理できるページに誘導する[ユーザー設定センター]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview)の作成を検討してください。NHI によって誤ってユーザーの登録が解除される可能性があるため、これは有用です。
5. コンバージョン数、アプリセッション数、サイト訪問数など、メールマーケティングの成功を測定するために[他の指標]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance)の使用も検討してください。
6. メールキャンペーンに隠しリンクを追加します。このリンクは、白地に白のテキストや句読点など、人間が気づかないようなものにします。ボットはすべてのリンクをクリックする傾向があるため、見えないリンクでクリックイベントを生成しているユーザーは実際には NHI の結果であると結論付けることができます。つまり、その開封やクリックは必ずしもポジティブなエンゲージメントを示しているわけではありません。

{% elsif include.channel == "in-app message" %}

#### アプリ内メッセージ指標

分析に表示される主なアプリ内メッセージの指標をいくつか紹介します。Braze で使用されるすべてのアプリ内メッセージ指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照してください。

{% alert note %}
_ボタン1のクリック数_と_ボタン2のクリック数_のレポートは、アプリ内メッセージで**レポート用の識別子**をそれぞれ「0」と「1」に指定した場合にのみ機能します。

![「レポート用識別子」フィールドの値が「0」。]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">本文クリック数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">ボタン1のクリック数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">ボタン2のクリック数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">コンバージョン (B、C、D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">コンバージョン数合計</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">コンバージョン率</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">メッセージを閉じる</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "KakaoTalk" %}

### KakaoTalk 指標

分析に表示される主な KakaoTalk 指標をいくつか紹介します。詳細については、[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)を参照してください。

| 用語 | 定義 |
| --- | --- |
| オーディエンス | _オーディエンス_は、特定のメッセージを受信したユーザーの割合です。<br><br>_（バリアント内の受信者数）/（ユニーク受信者数）_ |
| ユニーク受信者数 | _ユニーク受信者数_は、1日あたりのユニーク受信者数、つまり1日に新しいメッセージを受信したユーザー数です。このカウントがユーザーに対して複数回増加するには、ユーザーが別の日に新しいメッセージを受信する必要があります。この数値は `user_id` に基づいています。詳細については、[レポート指標用語集のユニーク受信者数]({{site.baseurl}}/user_guide/data/report_metrics/#unique-recipients)を参照してください。 |
| 送信数 | キャンペーンで送信されたメッセージの総数です。これはメッセージがデバイスに受信または配信されたことを意味するものではなく、メッセージが送信されたことのみを示します。 |
| クリック数の合計 | 送信された KakaoTalk メッセージがユーザーによってクリックされた合計回数です。 |
| エラー数 | _エラー数_は、KakaoTalk プロバイダーから返されたエラーの数です（送信プロセス中に増加します）。 |
| 収益 | _収益_は、設定された1次コンバージョン期間内のキャンペーン受信者からのドル建て収益です。 |
| 1次コンバージョン数 | _1次コンバージョン数_は、Braze キャンペーンから受信したメッセージを操作または閲覧した後に、定義されたイベントが発生した回数です。この定義されたイベントは、キャンペーン構築時に設定します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% elsif include.channel == "push" %}

#### プッシュ指標

以下は、メッセージのパフォーマンスを確認する際に表示される主な指標の内訳です。すべてのプッシュ指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照し、プッシュでフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>説明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">バウンス数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} <a href="#bounced-push">バウンスしたプッシュ通知</a>を参照してください。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">直接開封数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">開封数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> 通知の配信は、Apple プッシュ通知サービス（APNs）による「ベストエフォート」です。アプリにデータを配信することを目的としておらず、新しいデータが利用可能であることをユーザーに通知することのみを目的としています。重要な違いは、APNs がデバイスに正常に配信した数ではなく、APNs に正常に配信されたメッセージの数が表示されることです。

##### 配信停止の追跡

プッシュ通知の配信停止はキャンペーン分析の指標に含まれておらず、Apple や Google などのプロバイダーによるユーザーのプッシュステータスの更新に依存します。これらの更新は頻度が低く、予測不可能な場合があります。そのため、プッシュの配信停止はプッシュキャンペーン分析の指標として含まれていません。

ただし、手動でプッシュの配信停止を追跡することで、通知の頻度やコンテンツの関連性に対するユーザーの反応について貴重なインサイトを得ることができます。プッシュの配信停止を追跡する方法は2つあります：セグメントフィルターまたはカスタムフィルターを使用する方法です。

{% tabs local %}
{% tab Segment filters %}

プッシュが有効になっていないユーザー、つまりサブスクライブまたはオプトインしておらず、[フォアグラウンドプッシュトークン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)を持っていないユーザーを識別するセグメントを作成できます。例えば、アプリ内の配信停止数を確認するには、以下のセグメントを「OR」条件で組み合わせます：

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![アプリに対する「バックグラウンドまたはフォアグラウンドプッシュ有効」フィルターが false であり、「アンインストール済み」フィルターが選択されているセグメントビルダーセクション。]({% image_buster /assets/img/push_unsub_segment_example.png %})

セグメンテーションフィルターはおおよその目安であり、特定の日付やキャンペーンに結びつけることはできません。

{% endtab %}
{% tab Custom filters %}

{% alert important %}
サブスクリプション変更のカスタムイベントをログに記録すると、[データポイント]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count)が消費されます。または、セグメントフィルターを使用して、プッシュが有効になっていないユーザーを識別し、ターゲットにしてください。
{% endalert %}

別の回避策として、この指標を追跡するために、ユーザーのプッシュ有効ステータスが `true` か `false` かに基づいて、プッシュの配信停止のカスタムイベントを作成することもお勧めします。

{% endtab %}
{% endtabs %}

##### 開封を把握する

_直接開封数_と_誘発された開封数_には「開封」という言葉が含まれていますが、実際には異なる指標です。_直接開封数_は、上の表に記載されているように、プッシュ通知を直接開封することを指します。_誘発された開封数_は、プッシュ通知を受け取った後、特定の時間内にプッシュ通知を開かずにアプリを開封することを指します。つまり、_誘発された開封数_はアプリの開封を指し、プッシュ通知の開封ではありません。

##### プッシュ通知の送信数がユニーク受信者数を超える可能性がある理由

以下の理由により、_送信数_が_ユニーク受信者数_を上回る場合があります：

- **再適格性がオンになっている：**キャンペーンまたはキャンバスの設定で再適格性が有効になっている場合、セグメントと配信条件を満たすユーザーは同じプッシュ通知を複数回受け取ることができます。その結果、総送信数が多くなります。
- **ユーザーが複数のデバイスを持っている：**再適格性が有効になっていない場合、ユーザーが複数のデバイスをプロファイルに関連付けていることで差異が説明される場合があります。例えば、ユーザーがスマートフォンとタブレットの両方を持っていて、プッシュ通知が登録されたすべてのデバイスに送信される場合です。各配信は送信としてカウントされますが、ユニーク受信者は1人のみ記録されます。
- **ユーザーが複数のアプリに割り当てられている：**ユーザーが複数のアプリに関連付けられている場合（新しいアプリのテスト時など）、それぞれのアプリで同じプッシュ通知を受け取ることがあります。これが送信数の増加につながります。

##### バウンスが発生する理由 {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

バウンスは、Apple プッシュ通知サービス（APNs）において、プッシュ通知が対象のアプリがインストールされていないデバイスに配信されようとするときに発生します。APNs はまた、デバイスのトークンを任意に変更する権利を持っています。以前にトークンを登録した時点（各セッション開始時にユーザーのプッシュトークンを登録する場合など）から送信時刻までの間にプッシュトークンが変更されたユーザーのデバイスに送信しようとすると、バウンスが発生します。

ユーザーが次回のアプリ開封時にデバイス設定でプッシュを無効にした場合、SDK はプッシュが無効にされたことを検知し、Braze に通知します。この時点で、プッシュ有効状態を無効に更新します。無効化されたユーザーが新しいセッションを持つ前にプッシュキャンペーンを受信すると、キャンペーンは正常に送信され、配信されたように表示されます。このユーザーに対してプッシュがバウンスすることはありません。その後のセッションで、ユーザーにプッシュを送信しようとすると、Braze はフォアグラウンドトークンがあるかどうかを既に認識しているため、通知は送信されません。

配信前に期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されることもありません。

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging（FCM）のバウンスは3つのケースで発生する可能性があります：

| シナリオ | 説明 |
| -- | -- |
| アンインストールされたアプリケーション | メッセージがデバイスに配信されようとして、そのデバイスで対象のアプリがアンインストールされている場合、メッセージは破棄され、デバイスの登録 ID は無効になります。今後そのデバイスにメッセージを送信しようとすると、NotRegistered エラーが返されます。 |
| バックアップされたアプリケーション | アプリケーションがバックアップされると、アプリケーションが復元される前に登録 ID が無効になる可能性があります。この場合、FCM はアプリケーションの登録 ID を保存しなくなり、アプリケーションはメッセージを受信しなくなります。そのため、アプリケーションのバックアップ時に登録 ID を保存すべきでは**ありません**。 |
| 更新されたアプリケーション | アプリケーションが更新されると、以前のバージョンの登録 ID が使えなくなることがあります。そのため、更新されたアプリケーションは既存の登録 ID を置き換える必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS、MMS、RCS 指標

以下は、メッセージのパフォーマンスを確認する際に表示される主な指標の内訳です。すべての SMS、MMS、RCS 指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照し、SMS/MMS および RCS でフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">送信済み</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">配信失敗数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">確認済み配信</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">拒否数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">オプトアウト</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">ヘルプ</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">クリック数の合計</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Webhook 指標

分析に表示される主な Webhook 指標をいくつか紹介します。Braze で使用されるすべての Webhook 指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照してください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">ユニーク受信者数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">送信数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">エラー数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp 指標

分析に表示される主な WhatsApp 指標をいくつか紹介します。Braze で使用されるすべての WhatsApp 指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照してください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">送信数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">配信数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">既読数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">失敗数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### エンドユーザーのブロックとレポートの指標

追加の指標には [WhatsApp マネージャーダッシュボード](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx)からアクセスできますが、利用可能なすべてのインサイトにアクセスするには[アクセス権の確認](https://www.facebook.com/business/help/218116047387456)が必要です。

{% endif %}

### 過去のパフォーマンス

**過去のパフォーマンス**パネルでは、**メッセージパフォーマンス**パネルの指標を時系列のグラフとして表示できます。パネル上部のフィルターを使用して、グラフに表示される統計やチャネルを変更します。このグラフの時間範囲は、常にページ上部で指定された時間範囲を反映します。

日ごとの内訳を取得するには、<i class="fas fa-bars"></i> ハンバーガーメニューをクリックし、**CSV ダウンロード**を選択してレポートの CSV エクスポートを受け取ります。

![2021年2月から2022年5月までのメールに関する統計例を示す過去のパフォーマンスパネルのグラフ。]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
最新バージョンの Braze のアプリ内メッセージ（第3世代）を表示できるユーザーにのみ送信することを選択した場合、**ターゲットオーディエンス**は選択内容を反映するようには調整されません。
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### キーワード応答

**キーワード応答**パネルには、メッセージ受信後にユーザーが返信した受信キーワードのタイムラインが表示されます。

![キャンペーンレベルの SMS/MMS/RCS キーワード応答パネル。時間経過に伴うキーワード分布の折れ線グラフと、キーワードカテゴリセクション（オプトイン、オプトアウト、ヘルプ、その他、詳細、コーチングのチェックボックスが選択されている）が含まれます。]({% image_buster /assets/img/sms/keyword_responses.png %})

ここでは、[リターゲティング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns)の次のステップを決定し、便利に[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)するために、各キーワードカテゴリの応答分布を確認することもできます。

![折れ線グラフの下にあるテーブル。キーワードカテゴリ、応答分布、リターゲティングの列があり、キーワードカテゴリでセグメントを作成するオプションが提供されています。]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### コンバージョンイベントの詳細

**コンバージョンイベントの詳細**パネルには、キャンペーンのコンバージョンイベントのパフォーマンスが表示されます。詳細については、[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results)を参照してください。

![コンバージョンイベントの詳細パネル。]({% image_buster /assets/img/cc-conversion.png %})

### コンバージョンの相関

**コンバージョンの相関**パネルでは、どのようなユーザー属性と行動がキャンペーンに設定した結果に役立つか、または悪影響を与えるかを把握できます。詳細については、[コンバージョンの相関]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/)を参照してください。

![1次コンバージョンイベント A からのユーザー属性と行動に関する分析を含むコンバージョンの相関パネル。]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## レポートビルダー

[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)を使用して、KakaoTalk キャンペーンのカスタムレポートを作成することもできます。レポートを作成する際、**チャネル**で **KakaoTalk** を選択するか、KakaoTalk キャンペーンに適用したタグでフィルタリングすることで、KakaoTalk キャンペーンのみを含めるようにフィルタリングできます。

{% endif %}

{% if include.channel == "whatsapp" %}

### Meta 分析

Braze の分析に加えて、WhatsApp ビジネスマネージャーでテンプレートレベルの分析にもアクセスできます。詳細については、[Meta のドキュメント](https://www.facebook.com/business/help/218116047387456)を参照してください。

{% endif %}

{% if include.channel == "SMS" %}

### SMS Currents イベント

メールと同様に、Braze は SMS メッセージがユーザーに届く過程で、メッセージに関連するユーザーレベルのイベントを受信します。受信 SMS イベントはすべて、[SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) イベントを通じて Currents イベントとしても送信されます。これにより、ユーザーが Braze プラットフォーム外でテキスト入力したメッセージに対して、追加のアクションやレポートを実行できます。

{% alert note %}
受信メッセージは1,600文字を超えると切り捨てられます。
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## リテンションレポート

リテンションレポートには、特定のキャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}において、指定した期間にユーザーが選択したリテンションイベントを実行した割合が表示されます。詳細については、[リテンションレポート]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)を参照してください。

## 目標到達プロセスレポート

目標到達プロセスレポートは、キャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}を受け取った後の顧客のジャーニーを分析できるビジュアルレポートを提供します。キャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}でコントロールグループや複数のバリアントを使用している場合、異なるバリアントがコンバージョンファネルにどのような影響を与えたかをより細かいレベルで理解し、このデータに基づいて最適化できます。

詳細については、[目標到達プロセスレポート]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)を参照してください。

{% endif %}