---
page_order: 2
nav_title: セグメンテーションフィルター
article_title: セグメンテーションフィルター
layout: glossary_page
glossary_top_header: "セグメンテーションフィルター"
glossary_top_text: "Braze SDK には、特定の機能と属性に基づいてユーザーをセグメント化し、ターゲットにするための強力なフィルターが備わっています。フィルターカテゴリごとに、これらのフィルターを検索または絞り込むことができます。<br><br>ユーザーをセグメント化するために使用できる各種カスタム属性データタイプについては、<a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">カスタム属性データタイプ</a>を参照してください。"

page_type: glossary
tool: Segments
description: "この用語集には、ユーザーをセグメント化およびターゲット化するための使用可能なフィルターが一覧表示されています。"
search_rank: 2
glossary_tag_name: フィルターカテゴリ
glossary_filter_text: "カテゴリを選択して用語集を絞り込みます:"

# channel to icon/fa or image mapping
# NOTE: glossary_tags names must match the "tags" under each glossary entry exactly (filter/checkbox logic). Do not translate.
glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    display_name: "セグメントメンバーシップ"
    description: フィルターが使用されている任意の場所 (セグメント、キャンペーンなど) でセグメントメンバーシップに基づいてフィルタリングし、1 つのキャンペーン内で複数の異なるセグメントをターゲットにすることができます。<br><br>すでにこのフィルターを使用しているセグメントをさらに追加したり、他のセグメントにネストしたりすることはできません。これは、セグメント A にセグメント B が含まれ、セグメント B に再びセグメント A が含まれるというサイクルが発生する可能性があるためです。もしそうなれば、セグメントは自分自身を参照し続けることになり、誰が実際にそのセグメントに属しているのかを計算することができなくなります。また、このようにセグメントをネストすると、複雑さが増し、動作が遅くなる可能性があります。代わりに、同じフィルターを使用して、含めようとしているセグメントを再作成してください。
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    display_name: "Braze セグメントエクステンション"
    description: セグメントエクステンションを Braze ダッシュボードで作成した後、それらのエクステンションをセグメントに含めたり除外したりできます。
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    display_name: "CSVからの更新/インポート"
    description: CSV アップロードの一部であるかどうかに基づいてユーザーをセグメント化します。
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    display_name: "カスタム属性"
    description: "ユーザーが、記録されたカスタム属性値と一致するかどうかを判定します。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom attribute
  - name: Created At
    display_name: "作成日時"
    description: ユーザープロファイルが作成された時期でユーザーをセグメント化します。ユーザーが CSV または API によって追加された場合、このフィルターは追加された日付を反映します。ユーザーが CSV または API によって追加されておらず、SDK によって最初のセッションが追跡されている場合、このフィルターはその最初のセッションの日付を反映します。
    tags:
      - Other Filters
  - name: Created From
    display_name: "作成元"
    description: "ユーザープロファイルが作成された場所によってユーザーをセグメント化します。<br><br>以下の値がサポートされています:<br>- SDK (<code>sdk</code>): Braze SDK を通じて作成されたユーザープロファイル。<br>- REST API (<code>rest</code>): Braze REST API を通じて作成されたユーザープロファイル。<br>- プッシュトークンインポート (<code>pti</code>): プッシュトークンインポートを通じて作成されたユーザープロファイル。<br>- CSV (<code>csv</code>): CSV インポートを通じて作成されたユーザープロファイル。<br>- デモ (<code>demo</code>): デモデータを通じて作成されたユーザープロファイル。<br>- SMS (<code>sms</code>): SMS を通じて作成されたユーザープロファイル。<br>- Shopify (<code>shopify</code>): Shopify を通じて作成されたユーザープロファイル。<br>- WhatsApp (<code>whats_app</code>): WhatsApp を通じて作成されたユーザープロファイル。<br>- プロバイダーイベント (<code>provider_event</code>): プロバイダーイベントを通じて作成されたユーザープロファイル。<br>- プロバイダー同期 (<code>provider_sync</code>): プロバイダー同期を通じて作成されたユーザープロファイル。<br>- ランディングページ (<code>landing_page</code>): ランディングページを通じて作成されたユーザープロファイル。"
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    display_name: "ネストされたカスタム属性"
    description: "カスタム属性のプロパティである属性です。<br><br>階層化された時間のカスタム属性にフィルターを適用する場合、基準として「年間通算日」または「時刻」を選択できます。「年間通算日」は比較対象として月と日のみを確認します。「時刻」は、年を含む完全なタイムスタンプを比較します。"
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    display_name: "繰り返しイベントの日"
    description: "このフィルターでは、データタイプが「date」のカスタム属性の月と日を調べますが、年は調べません。このフィルターは毎年発生するイベントに役立ちます。<br><br>タイムゾーン&#58;<br>このフィルターは、メッセージがローカル時間のスケジュールオプションで送信される限り、ユーザーのタイムゾーンに合わせて調整します。そうでない場合、このフィルターは会社のタイムゾーンを使用します。"
    tags:
      - Custom attribute
  - name: Custom Event
    display_name: "カスタムイベント"
    description: "ユーザーが特別に記録されたイベントを実行したかどうかを判定します。<br><br>例:<br>プロパティ activity_name によるアクティビティが完了した。<br><br>タイムゾーン:<br>UTC - カレンダー日 = 1 カレンダー日は、ユーザーの過去 24～48 時間の履歴を参照します"
    tags:
      - Custom events
  - name: First Did Custom Event
    display_name: "初回カスタムイベント実行"
    description: "ユーザーが特別に記録されたイベントを実行した最も早い時刻を判定します。(24 時間) <br><br>例:<br>初回のカート放棄が過去 1 日未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: Last Did Custom Event
    display_name: "最終カスタムイベント実行"
    description: "ユーザーが特別に記録されたイベントを最後に実行した時刻を判定します。このフィルターでは、0.25 時間のような小数値がサポートされています。(24 時間) <br><br>例:<br>最後のカート放棄が過去 1 日未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    display_name: "Y日間にカスタムイベントX回"
    description: "ユーザーが、最後に指定された暦日数 (1～30 日) の間に、特別に記録されたイベントを 0～50 回実行したかどうかを判定します。(カレンダー日 = 1 カレンダー日は、ユーザーの過去 24～48 時間の履歴を参照します)<br> <a href=\"/docs/x-in-y-behavior/\">X-in-Y の動作について詳しくはこちらをご覧ください。</a> <br><br>例:<br>過去 1 暦日内にカートをちょうど 0 回放棄した<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンを考慮するため、1 暦日ではセグメント評価時刻に応じて 24～48 時間のユーザー履歴を分析します。2 暦日では 48～72 時間のユーザー履歴を分析し、以下同様です。"
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    display_name: "Y日間にカスタムイベントプロパティX回"
    description: "ユーザーが、最後に指定された暦日数 (1～30 日) の間に、特別に記録されたイベントを特定のプロパティについて 0～50 回実行したかどうかを判定します。(カレンダー日 = 1 カレンダー日は、ユーザーの過去 24～48 時間の履歴を参照します)<br><a href=\"/docs/x-in-y-behavior/\">X-in-Y の動作について詳しくはこちらをご覧ください。</a> <br><br>例:<br>過去 1 暦日内にプロパティ「event_name」でお気に入りに追加をちょうど 0 回行った<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンを考慮するため、1 暦日ではセグメント評価時刻に応じて 24～48 時間のユーザー履歴を分析します。2 暦日では 48～72 時間のユーザー履歴を分析し、以下同様です。"
    tags:
      - Custom events
  - name: Email Address
    display_name: "メールアドレス"
    description: "テスト用に個々のメールアドレスによってキャンペーン受信者を指定できます。これは、フィルターで「メールアドレスが空白でない」指定子を使用して、トランザクションメールをすべてのユーザー (配信停止済みユーザーを含む) に送信するためにも使用できます。このため、オプトインのステータスに関わらずメール配信を最大限に高めることができます。<br><br>このフィルターではユーザープロファイルにメールアドレスがあるかどうかだけがチェックされますが、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">利用可能なメール</a>フィルターでは追加の条件がチェックされます。"
    tags:
      - Other Filters
  - name: External User ID
    display_name: "外部ユーザーID"
    description: テストのために、キャンペーン受信者を個々のユーザー ID で指定することができます。
    tags:
      - Other Filters
  - name: "Random Bucket #"
    display_name: "ランダムバケット番号"
    description: ユーザーをランダムに割り当てられた番号 (0～9999 を含む) でセグメント化します。これにより、A/B テストと多変量テストに対する真のランダムユーザーの一様分布セグメントを作成できるようになります。
    tags:
      - Other Filters
  - name: Session Count
    display_name: "セッション数"
    description: ユーザーをワークスペース内のいずれかのアプリでこれまでに行ったセッション数でセグメント化します。
    tags:
      - Sessions
  - name: Session Count For App
    display_name: "アプリ別セッション数"
    description: 指定されたアプリ内でこれまでに行ったセッション数によってユーザーをセグメント化します。
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    display_name: "過去Y日間にセッションX回"
    description: "最後に指定された暦日数 (1～30 日) の間に、アプリで行ったセッション数 (0～50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">X-in-Y の動作について詳しくはこちらをご覧ください。</a>"
    tags:
      - Sessions
  - name: First Used App
    display_name: "アプリ初回使用"
    description: "アプリを開いた記録の最も早い時刻によってユーザーをセグメント化します。<em>これは、Braze SDK が統合されたバージョンのアプリを初めて使用したセッションを記録するものです。</em>(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: First Used Specific App
    display_name: "特定アプリ初回使用"
    description: "ワークスペース内の任意のアプリを開いた記録の最も早い時刻によってユーザーをセグメント化します。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: Last Used App
    display_name: "アプリ最終使用"
    description: "アプリを最後に開いた時刻によってユーザーをセグメント化します。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: Last Used Specific App
    display_name: "特定アプリ最終使用"
    description: "指定されたアプリを最後に開いた時刻によってユーザーをセグメント化します。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: Median Session Duration
    display_name: "セッション時間の中央値"
    description: アプリ内のセッションの長さの中央値によってユーザーをセグメント化します。
    tags:
      - Sessions
  - name: Received Message from Campaign
    display_name: "キャンペーンからメッセージ受信"
    description: "指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉します。同じメールアドレスや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外です。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用してください。<br><br>コンテンツカード、バナー、アプリ内メッセージについては、カードやアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録したときです。<br><br>プッシュおよび Webhook の場合、これはメッセージがユーザーに送信されたときです。<br><br>WhatsApp の場合、これは、メッセージがユーザーのデバイスに配信されたときではなく、最後のメッセージ API リクエストが WhatsApp に送信されたときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されたときです。<br><br>SMS および RCS の場合、これは最後のメッセージが SMS または RCS プロバイダーに配信されたときです。これは、メッセージがユーザーのデバイスに配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: Received Campaign Variant
    display_name: "キャンペーンバリアント受信"
    description: "受信した多変量キャンペーンのバリアントによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉します。同じメールアドレスや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外です。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用してください。<br><br>コンテンツカード、バナー、アプリ内メッセージについては、カードやアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録したときです。<br><br>プッシュおよび Webhook の場合、これはメッセージがユーザーに送信されたときです。<br><br>WhatsApp の場合、これは、メッセージがユーザーのデバイスに配信されたときではなく、最後のメッセージ API リクエストが WhatsApp に送信されたときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されたときです。<br><br>SMS および RCS の場合、これは最後のメッセージが SMS または RCS プロバイダーに配信されたときです。これは、メッセージがユーザーのデバイスに配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    display_name: "キャンバスステップからメッセージ受信"
    description: "特定のキャンバスコンポーネントを受信したかどうかによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉します。同じメールアドレスや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外です。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用してください。<br><br>コンテンツカードおよびアプリ内メッセージの場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録したときです。<br><br>プッシュおよび Webhook の場合、これはメッセージがユーザーに送信されたときです。<br><br>WhatsApp の場合、これは、メッセージがユーザーのデバイスに配信されたときではなく、最後のメッセージ API リクエストが WhatsApp に送信されたときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されたときです。<br><br>SMS および RCS の場合、これは最後のメッセージが SMS または RCS プロバイダーに配信されたときです。これは、メッセージがユーザーのデバイスに配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    display_name: "特定キャンバスステップからの最終メッセージ受信"
    description: "特定のキャンバスコンポーネントを受信した日時によってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉します。同じメールアドレスや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外です。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用してください。このフィルターでは、ユーザーが他のキャンバスコンポーネントをいつ受信したかは考慮されません。"
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    display_name: "特定キャンペーンからの最終メッセージ受信"
    description: "指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉します。同じメールアドレスや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外です。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用してください。このフィルターは、ユーザーがいつ他のキャンペーンを受信したかは考慮しません。"
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    display_name: "タグ付きキャンペーンまたはキャンバスからメッセージ受信"
    description: "指定したキャンペーンまたは指定したタグのキャンバスを受信したかどうかによって、ユーザーをセグメント化します。「キャンペーンからのメッセージを受信」や「キャンバスステップからのメッセージを受信」とは異なり、このフィルターは重複メッセージを受信した同一のメールアドレスまたは電話番号を持つすべてのユーザーを捕捉します。<br><br>コンテンツカード、バナー (キャンペーンのみ)、アプリ内メッセージについては、カードやアプリ内メッセージが送信された時点ではなく、ユーザーがインプレッションを記録した時点です。<br><br>プッシュおよび Webhook の場合、これはメッセージがユーザーに送信されたときです。<br><br>WhatsApp の場合、これは、メッセージがユーザーのデバイスに配信されたときではなく、最後のメッセージ API リクエストが WhatsApp に送信されたときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されたときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信された時、あるいはユーザーがそのメールやメール内のリンクを開封した時、そのメールアドレスを共有しているすべてのユーザーがメッセージを受信したように見えます。<br><br>SMS および RCS の場合、これは最後のメッセージが SMS または RCS プロバイダーに配信されたときです。これは、メッセージがユーザーのデバイスに配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    display_name: "タグ付きキャンペーンまたはキャンバスからの最終メッセージ受信"
    description: 特定のタグを持つ特定のキャンペーンまたはキャンバスを受信した日時によってユーザーをセグメント化します。このフィルターは、ユーザーが他のキャンペーンやキャンバスを受信した場合は考慮しません。(24 時間)
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    display_name: "キャンペーンまたはキャンバスステップからメッセージ未受信"
    description: キャンペーンまたはキャンバスコンポーネントを受信したことがあるかどうかによって、ユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Last Received Email
    display_name: "最終メール受信"
    description: "最後にメールを受信した時刻によって、ユーザーをセグメント化します。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Last Received Push
    display_name: "最終プッシュ受信"
    description: "ユーザーを最後にプッシュ通知のいずれかを受信した時刻でセグメント化します。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Last In App Message Impression
    display_name: "最終アプリ内メッセージインプレッション"
    description: ユーザーを最後にアプリ内メッセージを表示した時刻でセグメント化します。
    tags:
      - Retargeting
  - name: Last Received SMS
    display_name: "最終SMS受信"
    description: "最後の SMS、MMS、または RCS メッセージが SMS または RCS プロバイダーに配信された時刻によってユーザーをセグメント化します。これは、メッセージがユーザーのデバイスに配信されたことを保証するものではありません。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Last Received Webhook
    display_name: "最終Webhook受信"
    description: "Braze がそのユーザーの Webhook を最後に送信した時刻によってユーザーをセグメント化します。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    display_name: "最終WhatsApp受信"
    description: "最後に WhatsApp メッセージを受信した時刻によってユーザーをセグメント化します。これは、メッセージがユーザーのデバイスに配信されたときではなく、最後のメッセージ API リクエストが WhatsApp に送信されたときです。(24 時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    display_name: "アプリのライブアクティビティプッシュ開始登録"
    description: 特定のアプリ向けに iOS プッシュ通知を通じてライブアクティビティを開始するために登録しているかどうかでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    display_name: "キャンペーンをクリック/開封"
    description: "特定のキャンペーンとのインタラクションでフィルタリングします。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。<br><br>メールについては、「開封済みメール (機械開封)」と「開封済みメール (その他の開封)」でフィルタリングするオプションもあります。配信停止リンクやユーザー設定センターでのクリックは、このフィルターの対象外です。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後、開封/クリックの前にメールアドレスを変更した場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。<br><br>SMS および RCS の場合、インタラクションは次のように定義されます:<br>- ユーザーが、指定されたキーワードカテゴリに一致するリプライ SMS または RCS を最後に送信した。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンにアトリビューションされます。キャンペーンは、過去 4 時間以内に受信されている必要があります。<br>- ユーザーが、指定のキャンペーンから、ユーザーのクリック追跡が有効になっている SMS または RCS メッセージ内の短縮リンクを最後に選択した。"
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    display_name: "タグ付きキャンペーンまたはキャンバスをクリック/開封"
    description: "特定のタグを持つ特定のキャンペーンとのインタラクションでフィルタリングします。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。<br><br>メールについては、「開封済みメール (機械開封)」と「開封済みメール (その他の開封)」でフィルタリングするオプションがあります。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後、開封/クリックの前にメールアドレスを変更した場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。<br><br>SMS および RCS の場合、インタラクションは次のように定義されます:<br>- ユーザーが、指定されたキーワードカテゴリに一致するリプライ SMS または RCS を最後に送信した。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンにアトリビューションされます。キャンペーンは、過去 4 時間以内に受信されている必要があります。<br>- ユーザーがタグを持つ指定のキャンペーンまたはキャンバスステップから、ユーザーのクリック追跡が有効になっている SMS または RCS メッセージ内の短縮リンクを最後に選択した日時。"
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    display_name: "ステップをクリック/開封"
    description: "特定のキャンバスコンポーネントとのインタラクションでフィルタリングします。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。<br><br>メールについては、「開封済みメール (機械開封)」と「開封済みメール (その他の開封)」でフィルタリングするオプションがあります。<br><br>SMS および RCS の場合、インタラクションは次のように定義されます:<br>- ユーザーが、指定されたキーワードカテゴリに一致するリプライ SMS または RCS を最後に送信した。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンにアトリビューションされます。キャンペーンは、過去 4 時間以内に受信されている必要があります。<br>- ユーザーが、指定のキャンバスステップから、ユーザーのクリック追跡が有効になっている SMS または RCS メッセージ内の短縮リンクを最後に選択した。"
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    display_name: "キャンペーンでエイリアスをクリック"
    description: "指定したキャンペーンの特定のエイリアスをクリックしたかどうかによって、ユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後、開封/クリックの前にメールアドレスを変更した場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    display_name: "キャンバスステップでエイリアスをクリック"
    description: "特定のキャンバスで特定のエイリアスをクリックしたかどうかによって、ユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後、開封/クリックの前にメールアドレスを変更した場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    display_name: "任意のキャンペーンまたはキャンバスステップでエイリアスをクリック"
    description: "任意のキャンペーンまたはキャンバス内で特定のエイリアスをクリックしたかどうかによってユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後、開封/クリックの前にメールアドレスを変更した場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: Hard Bounced
    display_name: "ハードバウンス"
    description: ユーザーを、メールアドレスがハードバウンスされたかどうか (メールアドレスが不正な場合など) によってセグメント化します。
    tags:
      - Retargeting
  - name: Soft Bounced
    display_name: "ソフトバウンス"
    description: Y 日間に X 回ソフトバウンスしたかどうかでユーザーをセグメント化します。セグメントフィルターでは 30 日間しか遡ることができませんが、セグメントエクステンションを使えばさらに遡ることができます。<br><br>このフィルターは、Currents のソフトバウンスイベントとは異なる動作をします。ソフトバウンスセグメントフィルターは、72 時間のリトライ期間中に配信が成功しなかった場合にソフトバウンスをカウントします。Currents では、失敗した再試行はすべてソフトバウンスイベントとして送信されます。
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    display_name: "スパムとしてマーク済み"
    description: メッセージをスパムとしてマークしたかどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Invalid Phone Number
    display_name: "無効な電話番号"
    description: 電話番号が不正かどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    display_name: "特定SMS受信キーワードカテゴリの最終送信"
    description: 特定のキーワードカテゴリ内の特定のサブスクリプショングループに SMS、MMS、または RCS を最後に送信した時刻によって、ユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Converted From Campaign
    display_name: "キャンペーンからのコンバージョン"
    description: 特定のキャンペーンでコンバージョンしたかどうかによってユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
    tags:
      - Retargeting
  - name: Converted From Canvas
    display_name: "キャンバスからのコンバージョン"
    description: 特定のキャンバスでコンバージョンしたかどうかによってユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
    tags:
      - Retargeting
  - name: In Campaign Control Group
    display_name: "キャンペーンコントロールグループ内"
    description: ユーザーを、指定した多変量キャンペーンのコントロールグループに属しているかどうかによってセグメント化します。
    tags:
      - Retargeting
  - name: In Canvas Control Group
    display_name: "キャンバスコントロールグループ内"
    description: ユーザーを、指定したキャンバスのコントロールグループに属しているかどうかによってセグメント化します。このフィルターはキャンバスに入ったユーザーのみを評価するため、一度も入らなかったユーザーは結果から完全に除外されます。<br><br>例えば、キャンバスのコントロールグループに属さないユーザーをフィルタリングすると、キャンバスに入り非コントロールバリアントに割り当てられたユーザーのみが対象となります。キャンバスに一度も入らなかったユーザーは含まれません。キャンバスへのエントリに関わらずすべてのユーザーを含めるには、代わりに <code>Entered Canvas Variation</code> フィルターを使用してください。
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    display_name: "任意のコントロールグループへの最終登録"
    description: "キャンペーンで最後にコントロールグループに割り当てられた時刻によってユーザーをセグメント化します。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    display_name: "キャンバスバリエーションに参加"
    description: 特定のキャンバスのバリエーションパスに入ったかどうかによって、ユーザーをセグメント化します。このフィルターはすべてのユーザーを評価します。<br><br>例えば、キャンバスのバリエーションコントロールグループに入っていないユーザーをフィルタリングすると、キャンバスに入ったかどうかに関係なく、コントロールグループに属していないすべてのユーザーが対象となります。
    tags:
      - Retargeting
  - name: Last Received Any Message
    display_name: "最終メッセージ受信"
    description: "最後に受信したメッセージを判別して、ユーザーをセグメント化します。(24 時間)<br><br>コンテンツカード、バナー、アプリ内メッセージについては、カードやアプリ内メッセージが最後に送信されたときではなく、ユーザーが最後にインプレッションを記録したときです。<br><br>プッシュおよび Webhook の場合、これは任意のメッセージがユーザーに送信されたときです。<br><br>WhatsApp の場合、これは、メッセージがユーザーのデバイスに配信されたときではなく、最後のメッセージ API リクエストが WhatsApp に送信されたときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されたときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信された時、あるいはユーザーがそのメールやメール内のリンクを開封した時、そのメールアドレスを共有しているすべてのユーザーがメッセージを受信したように見えます。<br><br>SMS および RCS の場合、これは最後のメッセージが SMS または RCS プロバイダーに配信されたときです。これは、メッセージがユーザーのデバイスに配信されたことを保証するものではありません。<br><br>例:<br>前回受信メッセージ 1 日未満 = 24 時間未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Last Engaged With Message
    display_name: "最終メッセージエンゲージメント"
    description: "メッセージングチャネル (バナー、コンテンツカード、メール、アプリ内メッセージ、SMS、RCS、プッシュ、WhatsApp) のいずれかを最後にクリックまたは開封した時刻でユーザーをセグメント化します。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。(24 時間)<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されたときです。これには、「開封済みメール (機械開封)」と「開封済みメール (その他の開封)」でフィルタリングするオプションも含まれています。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信された時、あるいはユーザーがそのメールやメール内のリンクを開封した時、そのメールアドレスを共有しているすべてのユーザーがメッセージを受信したように見えます。<br><br>SMS および RCS の場合、ユーザーのクリック追跡が有効になっているメッセージ内の短縮リンクを最後に選択したときです。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: Clicked card
    display_name: "カードをクリック"
    description: 特定のコンテンツカードをクリックしたかどうかによってユーザーをセグメント化します。このフィルターは、「キャンペーンをクリック/開封」、「タグ付きのキャンペーンまたはキャンバスをクリック/開封」、および「ステップをクリック/開封」のサブフィルターとして使用できます。
    tags:
      - Retargeting
  - name: Feature Flags
    display_name: "フィーチャーフラグ"
    description: "現在有効になっている特定の<a href=\"/docs/developer_guide/feature_flags/\">フィーチャーフラグ</a>を持つユーザーのセグメントです。"
    tags:
      - Retargeting
  - name: Subscription Group
    display_name: "サブスクリプショングループ"
    description: メール、SMS、MMS、RCS、または WhatsApp のサブスクリプショングループでユーザーをセグメント化します。アーカイブされたグループは表示されず、使用できません。
    tags:
      - Channel subscription behavior
  - name: Email Available
    display_name: "メール利用可能"
    description: "ユーザーを、有効なメールアドレスを持っているかどうか、およびメール配信の購読またはオプトインの有無によってセグメント化します。このフィルターは、ユーザーがメールの配信停止をしているか、Braze がハードバウンスを受け取っているか、メールがスパムとしてマークされているかの 3 つの条件をチェックします。これらの条件のいずれかが満たされる場合、またはユーザーにメールが存在しない場合、そのユーザーは含まれません。<br><br>「利用可能なメール」が <code>false</code> のユーザーは、キャンペーンのオーディエンスから除外され、メールを受け取りません。たとえ送信設定がすべてのユーザー (配信停止ユーザーを含む) に送信するよう設定されていても同様です。<br><br>オプトインステータスが重要なメールについては、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">メールアドレス</a>の代わりに「利用可能なメール」を使用してください。追加の条件は、メールを受け取る資格があるユーザーをターゲットにするのに役立ちます。"
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    display_name: "メールオプトイン日"
    description: メールをオプトインした日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    display_name: "メールサブスクリプションステータス"
    description: メールのサブスクリプションステータスによってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    display_name: "メール配信停止日"
    description: 今後のメールを配信停止した日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    display_name: "フォアグラウンドプッシュ有効"
    description: "暫定的なプッシュ認証があるか、フォアグラウンドプッシュが有効になっているユーザーをセグメント化します。具体的には、このカウントには以下が含まれます:<br>1. 暫定的にプッシュが承認されている iOS ユーザー。<br>2. フォアグラウンドプッシュが有効で、プッシュサブスクリプションのステータスが配信停止になっていないユーザー (いずれかのアプリについて)。これらのユーザーの場合、この数にはフォアグラウンドプッシュのみが含まれます。<br><br>フォアグラウンドプッシュ有効には、配信停止を行ったユーザーは含まれません。<br><br>このフィルターでセグメント化した後、下部の<em>リーチ可能なユーザー</em>パネルで、Android、iOS、Web の各プラットフォームごとにそのセグメントに含まれるユーザーの内訳を確認できます。"
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    display_name: "アプリのフォアグラウンドプッシュ有効"
    description: デバイス上のアプリでプッシュ通知を有効にしているかどうかによってユーザーをセグメント化します。アプリに対してフォアグラウンドプッシュが有効になっているユーザーです。これはプッシュサブスクリプションのステータスを考慮していません。この数には、暫定的にフォアグラウンドおよびバックグラウンドのプッシュトークンを承認されたユーザーが含まれます。
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    display_name: "バックグラウンドまたはフォアグラウンドプッシュ有効"
    description: ユーザーがプッシュトークンを持っており配信停止していないかどうかに基づいてセグメント化します。いずれかのアプリでバックグラウンドまたはフォアグラウンドプッシュが有効になっているユーザーです。
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    display_name: "プッシュオプトイン日"
    description: プッシュ通知をオプトインした日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    display_name: "プッシュサブスクリプションステータス"
    description: "ユーザーをプッシュの<a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">サブスクリプションステータス</a>でセグメント化します。"
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    display_name: "プッシュ配信停止日"
    description: 今後のプッシュ通知を配信停止した日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    display_name: "購入済み商品"
    description: アプリで購入した商品ごとにユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    display_name: "購入総数"
    description: アプリでの購入数によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    display_name: "Y日間に商品X回購入"
    description: 指定の商品を購入した回数でユーザーをフィルタリングします。
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    display_name: "過去Y日間に購入X回"
    description: "最後に指定された暦日数 (1～30 日) の間に、購入を行った回数 (0～50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">X-in-Y の動作について詳しくはこちらをご覧ください。</a>"
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    display_name: "Y日間に購入プロパティX回"
    description: "最後に指定された暦日数 (1～30 日) の間に、特定の購入プロパティに関連して購入を行った回数によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">X-in-Y の動作について詳しくはこちらをご覧ください。</a>"
    tags:
      - Purchase behavior
  - name: First Made Purchase
    display_name: "初回購入"
    description: アプリ内で購入を行った最も早い時刻によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: First Purchase For App
    display_name: "アプリ初回購入"
    description: アプリから購入を行った最も早い時刻によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    display_name: "最終購入"
    description: 前回購入した時刻でユーザーをフィルタリングします。
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    display_name: "最終購入商品"
    description: 特定の商品を最後に購入した時刻でユーザーをフィルタリングします。
    tags:
      - Purchase behavior
  - name: Money Spent
    display_name: "支出金額"
    description: アプリで費やした金額によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    display_name: "Y日間の支出金額X"
    description: "最後に指定された暦日数 (1～30 日) の間に、アプリで費やした金額によってユーザーをセグメント化します。この金額は直近 50 回の購入の合計のみを含みます。<br> <a href=\"/docs/x-in-y-behavior/\">X-in-Y の動作について詳しくはこちらをご覧ください。</a>"
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    display_name: "最終注文日（過去730日）"
    description: "ユーザーを、最後に注文した時期でセグメント化します。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文完了」に基づきます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しません)。ユーザーはこのフィルターに対して 1 日 1 回評価され、最大遡及期間は過去 2 年間です。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    display_name: "注文総数（過去730日）"
    description: "ユーザーを、過去 2 年間における注文総数でセグメント化します。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文完了」に基づきます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しません)。この集計にはキャンセルされた注文は含まれません。キャンセルされた注文は、<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文キャンセル」を使用してトラッキングする必要があります。ユーザーはこのフィルターの評価を 1 日 1 回受けます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Total orders count
    display_name: "注文総数"
    description: "ユーザーの生涯における注文総数に基づいてユーザーをセグメント化します。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文完了」に基づきます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しません)。この集計にはキャンセルされた注文は含まれません。キャンセルされた注文は、<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文キャンセル」を使用してトラッキングする必要があります。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    display_name: "キャンセル注文総数（過去730日）"
    description: "ユーザーを、過去 2 年間にキャンセルした注文の総数でセグメント化します。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文完了」に基づきます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しません)。ユーザーはこのフィルターの評価を 1 日 1 回受けます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    display_name: "顧客生涯価値（過去730日）"
    description: "ユーザーを、そのユーザーが貴社ブランドとの購入履歴を通じて生み出すと予想される総収益によってセグメント化します。計算では過去 730 日間を対象とし、平均注文金額 (AOV) を注文総数で乗算します。その後、ユーザーのアクティブな購入期間 (初回注文から直近の注文までの期間) を考慮に入れます。このフィルターは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>で追跡されたデータを使用します (e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しません)。ユーザーはこのフィルターの評価を 1 日 1 回受けます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    display_name: "返金総額（過去730日）"
    description: "ユーザーを、過去 2 年間に付与された返金額に基づいてセグメント化します。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文返金」に基づきます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しません)。ユーザーはこのフィルターの評価を 1 日 1 回受けます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Total refund value
    display_name: "返金総額"
    description: "ユーザーを、その生涯にわたって付与された返金総額に基づいてセグメント化します。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文返金」に基づきます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しません)。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    display_name: "総収益（過去730日）"
    description: "ユーザーを、過去 2 年間の注文から生じた総収益額でセグメント化します。この収益額は、注文完了時の e コマースイベントに関連する収益から、注文返金時の<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>に関連する収益を差し引いて算出されます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しません)。ユーザーはこのフィルターの評価を 1 日 1 回受けます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Total revenue
    display_name: "総収益"
    description: "ユーザーの生涯にわたる注文から生じた総収益に基づいてユーザーをセグメント化します。この収益は、注文完了時の e コマースイベントに関連する収益から、注文返金時の<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>に関連する収益を差し引いて算出されます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しません)。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    display_name: "平均注文額（過去730日）"
    description: "ユーザーの過去 2 年間の注文平均額 (平均値) に基づいてユーザーをセグメント化します。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文完了」に基づきます (e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しません)。ユーザーはこのフィルターの評価を 1 日 1 回受けます。<br><br>このフィルターはベータ版です。このフィルターを利用したい場合は、Braze のアカウントマネージャーにお問い合わせください。"
    tags:
      - eCommerce
  - name: Country
    display_name: "国"
    description: ユーザーを最後に示された国のロケーションでセグメント化します。
    tags:
      - Demographic attributes
  - name: City
    display_name: "市区町村"
    description: 最後に示された市区町村のロケーションによってユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Language
    display_name: "言語"
    description: ユーザーを好みの言語でセグメント化します。
    tags:
      - Demographic attributes
  - name: Age
    display_name: "年齢"
    description: ユーザーをアプリ内で示した年齢によってセグメント化します。
    tags:
      - Demographic attributes
  - name: Birthday
    display_name: "誕生日"
    description: ユーザーをアプリ内で示した誕生日によってセグメント化します。<br>2 月 29 日が誕生日のユーザーは、3 月 1 日を含むセグメントに含まれます。<br><br>12 月または 1 月の誕生日をターゲットにするには、ターゲットとする年の 12 か月の期間内のフィルターロジックのみを挿入してください。言い換えれば、前の暦年の 12 月を振り返るロジックや、翌年の 1 月までのフォワードロジックを挿入しないでください。たとえば、12 月の誕生日をターゲットにするには、「12 月 31 日」、「12 月 31 日の前」、または「11 月 30 日の後」でフィルタリングすることができます。
    tags:
      - Demographic attributes
  - name: Gender
    display_name: "性別"
    description: アプリ内から示されたとおり、ユーザーを性別でセグメント化します。
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    display_name: "未フォーマット電話番号"
    description: フォーマットされていない電話番号でユーザーをセグメント化します。括弧、ダッシュ、その他の記号は含みません。
    tags:
      - Demographic attributes
  - name: First Name
    display_name: "名"
    description: ユーザーをアプリ内で示した名によってセグメント化します。
    tags:
      - Demographic attributes
  - name: Last Name
    display_name: "姓"
    description: ユーザーをアプリ内で示した姓でセグメント化します。
    tags:
      - Demographic attributes
  - name: Has App
    display_name: "アプリ保有"
    description: ユーザーがアプリをインストールしたことがあるかどうかによってセグメント化します。これには、現在アプリをインストールしているユーザーと、過去にアンインストールしたユーザーが含まれます。通常、このフィルターに一致するには、ユーザーがアプリを開く (セッションを開始する) 必要があります。ただし、ユーザーが Braze にインポートされ、アプリに手動で関連付けられた場合など、いくつかの例外があります。
    tags:
      - App
  - name: Most Recent App Version Name
    display_name: "最新アプリバージョン名"
    description: "ユーザーのアプリの最新の名前によってセグメント化します。<br><br>「より小さい」または「以下」を使用する場合、メインアプリのバージョンが存在しないと、このフィルターは `true` を返します。ユーザーがアプリバージョンより古いためです。これは、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致することを意味します。"
    tags:
      - App
  - name: Most Recent App Version Number
    display_name: "最新アプリバージョン番号"
    description: "ユーザーのアプリの最新バージョン番号によってセグメント化します。<br><br>「より小さい」または「以下」を使用する場合、メインアプリのバージョンが存在しないと、このフィルターは `true` を返します。ユーザーがアプリバージョンより古いためです。これは、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致することを意味します。<br><br>現在のアプリバージョンが表示されるまで時間がかかる場合があります。ユーザープロファイル上のアプリバージョンは、SDK が情報を取得した時点で更新されます。これはユーザーがアプリを開いたタイミングに依存します。ユーザーがアプリを開かない場合、現在のバージョンは更新されません。これらのフィルターは遡って適用されることもありません。現在版や将来版に対しては「より大きい」や「等しい」を使うのが良いですが、過去版のフィルターを使うと予期せぬ動作を引き起こす可能性があります。"
    tags:
      - App
  - name: Uninstalled
    display_name: "アンインストール済み"
    description: アプリをアンインストールした後、再インストールしていないかどうかによって、ユーザーをセグメント化します。
    tags:
      - Uninstall
  - name: Device Carrier
    display_name: "デバイスキャリア"
    description: デバイスの通信事業者によってユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device Count
    display_name: "デバイス数"
    description: アプリを使用したデバイスの数でユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device Model
    display_name: "デバイスモデル"
    description: 携帯電話の機種別にユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device OS
    display_name: "デバイスOS"
    description: "指定のオペレーティングシステムを持つ 1 台以上のデバイスを持つユーザーをセグメント化します。ユーザーをオペレーティングシステムの範囲でセグメント化するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">デバイス OS バージョン番号</a>フィルターを使用してください。"
    tags:
      - Devices
  - name: Device OS Version Number
    display_name: "デバイスOSバージョン番号"
    description: 指定された範囲内のオペレーティングシステムバージョンを持つデバイスを 1 台以上所有するユーザーをセグメント化します。例えば、iOS のオペレーティングシステムバージョンが 26.0 以上であるユーザーをターゲットにできます。
    tags:
      - Devices
  - name: Most Recent Device Locale
    display_name: "最新デバイスロケール"
    description: "最後に使用したデバイスの<a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">ロケール情報</a>でユーザーをセグメント化します。"
    tags:
      - Devices
  - name: Most Recent Watch Model
    display_name: "最新ウォッチモデル"
    description: ユーザーを最新のスマートウォッチモデルでセグメント化します。
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    display_name: "iOSでの暫定承認"
    description: iOS 12 で特定のアプリに対して暫定的に許可されているユーザーを検索できます。
    tags:
      - Devices
  - name: Web Browser
    display_name: "Webブラウザ"
    description: Web サイトにアクセスするために使用するウェブブラウザによって、ユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device IDFA
    display_name: "デバイスIDFA"
    description: テスト用のキャンペーン受信者を IDFA で指定できます。
    tags:
      - Advertising use cases
  - name: Device IDFV
    display_name: "デバイスIDFV"
    description: テスト用に IDFV でキャンペーン受信者を指定できます。
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    display_name: "デバイスGoogle広告ID"
    description: ユーザーを Google 広告 ID でセグメント化します。
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    display_name: "デバイスRoku広告ID"
    description: ユーザーを Roku 広告 ID でセグメント化します。
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    display_name: "デバイスWindows広告ID"
    description: ユーザーを Windows 広告 ID でセグメント化します。
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    display_name: "広告トラッキング有効"
    description: ユーザーが広告の追跡をオプトインしているかどうかに基づいてフィルタリングできます。広告の追跡は IDFA または Apple によってすべての iOS デバイスに割り当てられている「広告主用の識別子」に関連します。これは SDK によって設定できます。この識別子により、広告主はユーザーを追跡し、ターゲット広告を提供することができます。
    tags:
      - Advertising use cases
  - name: Most Recent Location
    display_name: "最新位置情報"
    description: ユーザーを、アプリを使用した最後に記録されたロケーションでセグメント化します。
    tags:
      - Location
  - name: Location Available
    display_name: "位置情報利用可能"
    description: "ユーザーのロケーションがレポートされているかどうかによって、セグメント化します。このフィルターを使用するには、アプリに<a href=\"/docs/search/?query=location%20tracking\">位置情報の追跡が統合</a>されている必要があります。"
    tags:
      - Location
  - name: Amplitude Cohorts
    display_name: "Amplitudeコホート"
    description: Amplitude を使用するクライアントは、Amplitude でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Census Cohorts
    display_name: "Censusコホート"
    description: Census を使用するクライアントは、Census でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Heap Cohorts
    display_name: "Heapコホート"
    description: Heap を使用するクライアントは、Heap 内のコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    display_name: "Hightouchコホート"
    description: Hightouch を使用するクライアントは、Hightouch でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    display_name: "Kubitコホート"
    description: Kubit を使用するクライアントは、Kubit でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    display_name: "Mixpanelコホート"
    description: Mixpanel を使用するクライアントは、Mixpanel でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Segment Cohorts
    display_name: "Segmentコホート"
    description: Segment を使用するクライアントは、Segment でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    display_name: "Tinycluesコホート"
    description: Tinyclues を使用するクライアントは、Tinyclues でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    display_name: "インストールアトリビューション広告"
    description: インストールアトリビューションとなった広告によってユーザーをセグメント化します。
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    display_name: "インストールアトリビューション広告グループ"
    description: インストールアトリビューションとなった広告グループによってユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    display_name: "インストールアトリビューションキャンペーン"
    description: インストールアトリビューションとなった広告キャンペーンによって、ユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Install Attribution Source
    display_name: "インストールアトリビューションソース"
    description: インストールアトリビューションとなったソースによってユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Churn Risk Category
    display_name: "解約リスクカテゴリ"
    description: ユーザーを、特定の予測に応じて解約リスクカテゴリ別にセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    display_name: "解約リスクスコア"
    description: ユーザーを、特定の予測に応じて解約リスクスコア別にセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    display_name: "イベント可能性カテゴリ"
    description: ユーザーを、特定の予測に従ってイベントを実行する可能性によってセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    display_name: "イベント可能性スコア"
    description: ユーザーを、特定の予測に従ってイベントを実行する可能性によってセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    display_name: "インテリジェントチャネル"
    description: 過去 3 か月間で最もアクティブなチャネルごとにユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    display_name: "メッセージ開封可能性"
    description: "<a href=\"/docs/user_guide/brazeai/intelligence/intelligent_channel/#individual-channels\">指定したチャネルでメッセージを開封する可能性</a>を 0～100% の尺度で評価し、それに基づいてユーザーをフィルタリングします。チャネルの可能性を測定するのに十分なデータがないユーザーは、「空白である」を使用して選択できます。<br><br>メールの場合、機械による開封は可能性の計算から除外されます。"
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    display_name: "アプリを使用しているFacebook友達の数"
    description: 同じアプリを使用している Facebook の友達の人数でユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Connected Facebook
    display_name: "Facebook連携済み"
    description: アプリを Facebook に接続したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Connected Twitter
    display_name: "Twitter連携済み"
    description: アプリを X (旧 Twitter) に接続したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Number of Twitter Followers
    display_name: "Twitterフォロワー数"
    description: ユーザーを X (旧 Twitter) フォロワーの数でセグメント化します。
    tags:
      - Social activity
  - name: Phone Number
    display_name: "電話番号"
    description: "E.164 形式の電話番号フィールドでユーザーをセグメント化します。<br><br>電話番号が Braze に送信されると、Braze はそれを SMS、RCS、および WhatsApp チャネルで使用される <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">e.164 形式</a>に変換しようとします。番号が適切にフォーマットされていない場合、変換処理は失敗する可能性があります。その結果、ユーザープロファイルはフォーマットされていない電話番号を持ちますが、送信用電話番号は持たないことになります。このセグメントフィルターは、e.164 形式の電話番号 (利用可能な場合) でユーザーを返します。<br><br>ユースケース:<br>- SMS、RCS、または WhatsApp メッセージを送信する際、このフィルターを使って最も正確なターゲットオーディエンスのサイズを把握できます。<br>- このフィルターで正規表現 (regex) を使って、特定の国コードを持つ電話番号をセグメント化できます。<br>- このフィルターを使用して、e.164 変換処理に失敗した電話番号でユーザーをセグメント化できます。"
    tags:
      - Other Filters
---