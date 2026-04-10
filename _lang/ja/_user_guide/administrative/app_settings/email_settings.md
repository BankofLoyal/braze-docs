---
nav_title: メール設定
article_title: メール設定
page_type: reference
page_order: 14
description: "このリファレンス記事では、送信設定、開封追跡ピクセル、サブスクリプションページとフッターなど、Braze ダッシュボードのメール設定について説明します。"
tool: Dashboard
channel: email
toc_headers: h2

---

# メール設定

> [メール設定] では、カスタムフッター、カスタムのオプトインページ、オプトアウトページなど、具体的な送信メール設定を行うことができます。送信メールにこれらのオプションを含めると、一貫して流れるようなエクスペリエンスがユーザーにもたらされます。

[**メール設定**] は、ダッシュボードの [**設定**] の下にあります。

## 送信設定

[**送信設定**] セクションのメール設定により、メールキャンペーンに含まれる詳細が決まります。特にこれらの設定は、主にユーザーが Braze からメールを受信したときに表示される内容に関連します。

### 送信メールの設定

メール設定を行うときに、送信メール設定は、Braze がユーザーにメールを送信するときに使用する名前とメールアドレスを特定します。

{% tabs local %}
{% tab Display Name Address %}

このセクションでは、Braze がユーザーにメールを送信する際に使用できる名前とメールアドレスを追加できます。メールキャンペーンを作成する際、送信者名とメールアドレスは [**送信情報の編集**] オプションで設定できます。送信メール設定を更新しても、過去にさかのぼって既存の送信には影響しないことに注意してください。

![「送信メール設定」セクションには、異なる表示名とドメイン用のフィールドがある。]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Liquid によるパーソナライゼーション

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) は、**送信者名**、**ローカル部分**、および**ドメイン**フィールドで使用でき、カスタム属性に基づいて送信者名とメールアドレスをダイナミックにテンプレート化できます。**ドメイン**フィールドで Liquid を使用するには、メールキャンペーンの [**送信情報**] オプションに移動し、[**送信者名 + アドレスをカスタマイズ**] チェックボックスを選択する必要があります。

![送信者名、アドレス、ドメインをカスタマイズするためのフィールドがある送信設定。]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

例えば、条件分岐を使って異なるブランドや地域から送信できます：

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

このセクションにメールアドレスを追加すると、そのアドレスをメールキャンペーンの返信先アドレスとして選択できます。[**デフォルトにする**] を選択して、あるメールアドレスをデフォルトのメールアドレスにすることもできます。これらのメールアドレスは、メールキャンペーンを作成するときに [**送信情報を編集**] オプションで使用できます。

![「返信先アドレス」セクションには、複数の返信先アドレスを入力するフィールドがある。]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Liquid によるパーソナライゼーション

**返信先アドレス**フィールドでも [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) を使用でき、カスタム属性に基づいて返信先アドレスをダイナミックにテンプレート化できます。例えば、条件付きロジックを使って、返信先の地域や部署を指定できます：

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@company.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@company.com" %}
{% else %}
{% assign address = "global-support@company.com" %}{% endif %}{{address}}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

このセクションでは、Braze から送信される送信メールに追加できる BCC アドレスを管理できます。メールに BCC アドレスを追加すると、ユーザーが受信するメッセージとまったく同じ内容が、BCC の受信トレイにも送信されます。これは、コンプライアンス要件またはカスタマーサポートの問題のためにユーザーに送信したメッセージのコピーを保持するのに便利なツールです。BCC メールはメールレポートや分析には含まれません。

BCC アドレスは、SendGrid および SparkPost でのみ使用できます。BCC アドレスの代わりに、[メッセージアーカイブ]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/)を使用して、アーカイブまたはコンプライアンスの目的でユーザーに送信されるメッセージのコピーを保存することをお勧めします。

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

![メール設定タブの BCC アドレスセクション。]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

アドレスを追加すると、キャンペーンまたはキャンバスステップでメールを作成するときに、アドレスを選択できるようになります。新規のメールキャンペーンまたはキャンバスコンポーネントを開始するときに、このアドレスがデフォルトで選択されるように設定するには、アドレスの横にある [**デフォルトにする**] を選択します。これをメッセージレベルでオーバーライドするには、メッセージの設定時に [**BCC なし**] を選択します。

Braze から送信されるすべてのメールメッセージに BCC アドレスを含める必要がある場合は、[**すべてのメールキャンペーンで BCC アドレスを要求する**] トグルをオンにできます。これには、デフォルトのアドレスを選択する必要があります。このアドレスは、新しいメールキャンペーンまたはキャンバスステップで自動的に選択されます。デフォルトのアドレスは、REST API を通じてトリガーされるすべてのメッセージにも自動的に追加されます。アドレスを含めるために既存の API リクエストを変更する必要はありません。

#### ダイナミック BCC

ダイナミック BCC を使えば、BCC アドレスに Liquid を使用できます。この機能は**メール設定**でのみ利用可能であり、キャンペーン自体では設定できないことに注意してください。メールの受信者ごとに、BCC アドレスは1つだけ許可されます。

例えば、サポートチームからのメールの BCC アドレスとして {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} を追加できます。

![メール設定タブの BCC アドレスセクションに、Liquid を使用した BCC アドレスが入力されている。]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## 開封追跡ピクセル

[![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

メール開封トラッキングピクセルは目に見えない 1 x 1&nbsp;px の画像であり、メールの HTML に自動的に挿入されます。このピクセルは、Braze がユーザーのメール開封を検知するのに役立ちます。ユーザーのメールクライアントが当社のトラッキングピクセルにリクエストを送信すると、そのリクエストには IP アドレス、ユーザーエージェント、タイムスタンプなどの情報が含まれることがあります。メール開封情報は非常に有用であり、対応する開封率を把握することで効果的なマーケティング戦略を決定するのに役立ちます。

### 追跡ピクセルの配置

Braze のデフォルトの動作では、メールの下部に追跡ピクセルが追加されます。ほとんどのユーザーにとって、これはピクセルを配置する最適な場所です。ピクセルのスタイルはすでに、視覚的な変化をできるだけ小さくするように設定されていますが、意図しない視覚的な変化はメールの下部にあるとほぼまったく目立ちません。これは、SendGrid や SparkPost などのメールプロバイダーのデフォルトでもあります。

### 追跡ピクセルの位置の変更

Braze は現在、メールサービスプロバイダー (ESP) のデフォルトの開封追跡ピクセルの位置（メールの `<body>` の最後のタグ）をオーバーライドして `<body>` の最初のタグに移動することをサポートしています。
  
![「オープントラッキングピクセル」セクションには、SendGrid、SparkPost、Amazon SES のいずれかに移動するオプションがある。]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

場所を変更するには、次の手順に従います。

1. Braze で、[**設定**] > [**メール設定**] に移動します。
2. 以下のオプションから選択します：[**SendGrid の移動**]、[**SparkPost の移動**]、または [**Amazon SES の移動**]
3. [**保存**] を選択します。

保存後、Braze はメールサービスプロバイダー (ESP) に特別な指示を送信し、すべての HTML メールの最上部に開封トラッキングピクセルを配置させます。
  
{% alert important %} 
SSL イネーブルメントは、トラッキングピクセルの URL を HTTP ではなく HTTPS でラップします。SSL の設定が間違っていると、トラッキングピクセルの有効性に影響する可能性があります。 
{% endalert %}

## list-unsubscribe ヘッダー {#list-unsubscribe}

{% alert note %}
2024年2月15日以降、新規企業にはデフォルトで配信停止ヘッダー（ワンクリック配信停止機能付き）が有効になっています。
{% endalert %}

list-unsubscribe ヘッダーを使用すると、メッセージ本文ではなくメールボックス UI 内に [**配信停止**] ボタンが表示されるため、受信者はマーケティングメールから簡単に配信停止ができます。

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

受信者が [**配信停止**] を選択すると、メールボックスプロバイダーはメールヘッダーに定義された送信先に配信停止リクエストを送信します。

list-unsubscribe を有効にすることは、配信到達性のベストプラクティスであり、一部の主要なメールボックスプロバイダーでは要件になっています。エンドユーザーが不要なメッセージから安全に自身を解除することを推奨するものであり、メールクライアントのスパムボタンを押す行為とは対照的です。後者は送信者の信頼度およびメールの配信到達性に悪影響を及ぼします。

[Gmail でサブスクリプションを管理する](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC)際、Gmail はメッセージ本文から配信停止リンクを取得することもできますが、ヘッダーに list-unsubscribe が存在する場合はそちらを優先します。

### メールボックスプロバイダーのサポート

次の表に、「mailto:」ヘッダー、list-unsubscribe URL、およびワンクリック配信停止（[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)）に対するメールボックスプロバイダーのサポートをまとめています。

| list-unsubscribe ヘッダー | Mailto: ヘッダー | list-unsubscribe URL | ワンクリック配信停止（RFC 8058） | 
| ----- | --- | --- | --- |
| Gmail | 対応* | 対応 | 対応 |
| Gmail モバイル | 非対応 | 非対応 | 非対応 |
| Apple メール | 対応 | 非対応 | 非対応 |
| Outlook.com | 対応 | 非対応 | 非対応 |
| Yahoo! メール | 対応* | 非対応 | 対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_*Yahoo と Gmail は最終的に「mailto:」ヘッダーを廃止し、ワンクリックのみをサポートするようになります。_

ヘッダーの表示は、最終的にメールボックスプロバイダーによって決定されます。Gmail で受信者宛ての未加工（テキスト）メールに list-unsubscribe ヘッダーが含まれているかどうかを確認するには、次の手順に従います。

1. メールの [**メッセージのソースを表示**] を選択します。これにより、メールの未加工バージョンとそのヘッダーを含む新しいタブが開きます。
2. 「List-Unsubscribe」を検索します。

このヘッダーが未加工バージョンのメールに含まれているにもかかわらず表示されない場合、メールボックスプロバイダーが配信停止オプションを表示しないと判断しています。つまり、メールボックスプロバイダーがヘッダーを表示しない理由についてはこれ以上のインサイトは得られません。list-unsubscribe ヘッダーの表示は、最終的にレピュテーション（信頼度）に基づいて行われます。大抵の場合、メールボックスプロバイダーにおける送信者の評判が良ければ良いほど、list-unsubscribe ヘッダーが表示される可能性が高くなります。

### ワークスペースのメール配信停止ヘッダー

![送信先として「購読中またはオプトインしているユーザー」を選択する。]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

メール配信停止ヘッダー機能がオンになっている場合、この設定は会社レベルではなく、ワークスペース全体に適用されます。キャンペーンおよびキャンバスビルダーの [**ターゲットオーディエンス**] ステップで、購読中またはオプトインのユーザー、またはオプトインのユーザーに送信するように設定されたキャンペーンおよびキャンバスに追加されます。

「ワークスペースのデフォルト」を使用する場合、Braze はトランザクションと見なされるキャンペーン（「配信停止済みのユーザーを含むすべてのユーザーに送信」に設定されているキャンペーン）にはワンクリック配信停止ヘッダーを追加しません。これをオーバーライドし、配信停止済みのユーザーに送信するときにワンクリック配信停止ヘッダーを追加するには、メッセージレベルのワンクリックリスト配信停止設定で [**すべてのメールからグローバルに配信停止**] を選択できます。

### デフォルトの list-unsubscribe ヘッダー

{% alert important %}
Gmail は、2024年6月1日以降、送信するすべての商用およびプロモーションメッセージについて、ワンクリック配信停止を実装するよう送信者に要求する予定です。詳細については、Gmail の「[メール送信者のガイドライン](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe)」と「[メール送信者のガイドラインに関するよくある質問](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)」を参照してください。Yahoo は、この更新された要件について、2024年初頭のタイムラインを発表しました。詳細については、「[More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/)」を参照してください。
{% endalert %}

Braze の配信停止機能を使用して配信停止を直接処理するには、[**購読中またはオプトイン済みのユーザーに送信されるメールに One-Click List-Unsubscribe（mailto および HTTP）ヘッダーを含める**] を選択し、標準の Braze URL および mail-to として [**Braze のデフォルト**] を選択します。 

![購読中またはオプトインしたユーザーに送信するメールに、配信停止ヘッダーを自動的に含めるオプション。]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze は、次のバージョンの list-unsubscribe ヘッダーをサポートしています。

| リスト配信停止バージョン | 説明 | 
| ----- | --- |
| ワンクリック（RFC 8058） | 受信者がワンクリックでメールからオプトアウトする簡単な方法を提供します。これは、Yahoo と Gmail から一括送信者に課される要件です。 |
| リスト配信停止 URL または HTTPS | 受信者に、配信停止できるウェブページに誘導するリンクを提供します。 |
| mailto | 受信者からブランドに送信される配信停止リクエストメッセージの送信先としてメールアドレスを指定します。<br><br> _mailto list-unsubscribe リクエストを処理するには、そのような配信停止リクエストに、配信を停止するエンドユーザーについて Braze に保存されているメールアドレスが含まれている必要があります。これは、エンドユーザーが配信を停止するメールの「差出人アドレス」、配信を停止するエンドユーザーが受信したメールのエンコードされた件名またはエンコードされた本文で提供される場合があります。ごく限られたケースでは、一部の受信トレイプロバイダーが [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368) プロトコルに準拠していないため、メールアドレスが正しく渡されないことがあります。このため、配信停止リクエストが Braze で処理できない場合があります。_ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze が上記の方法のいずれかでユーザーから list-unsubscribe リクエストを受信すると、このユーザーのグローバルメールサブスクリプション状態が配信停止に設定されます。一致するものがなければ、Braze はこのリクエストを処理しません。

### ワンクリック配信停止

list-unsubscribe ヘッダー（[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)）に対してワンクリック配信停止を使用すると、受信者がメールからオプトアウトするための簡単な方法を提供することに重点が置かれます。

### メッセージレベルのワンクリックリスト配信停止

メッセージレベルでのワンクリック配信停止設定は、ワークスペース向けに設定されたメール配信停止ヘッダー機能をオーバーライドします。次の用途では、キャンペーンまたはキャンバスステップごとにワンクリック配信停止動作を適用します。

- 1つのワークスペース内で複数のブランド/リストをサポートするために、特定のサブスクリプショングループに対して Braze のワンクリック配信停止機能を追加する
- デフォルトの Braze 配信停止 URL かカスタム URL かを切り替える
- カスタムのワンクリック配信停止 URL を追加する
- このメッセージのワンクリック配信停止を省略する

{% alert note %}
メッセージレベルのワンクリックリスト配信停止設定は、ドラッグアンドドロップエディターと更新された HTML エディターを使用する場合にのみ使用できます。以前の HTML エディターを使用している場合は、更新された HTML エディターに切り替えてこの機能を使用してください。
{% endalert %}

メールエディターで、[**送信設定**] > [**送信情報**] と進みます。以下のオプションから選択します：

- **ワークスペースのデフォルトを使用**：[**メール設定**] で設定された [**メール配信停止ヘッダー**] 設定を使用します。この設定への変更は、すべてのメッセージに適用されます。
- **すべてのメールからグローバルに配信停止**：Braze デフォルトのワンクリック配信停止ヘッダーを使用します。配信停止ボタンをクリックしたユーザーは、グローバルなメールサブスクリプション状態が「配信停止」に設定されます。
- **特定のサブスクリプショングループから配信停止**：指定されたサブスクリプショングループを使用します。Braze は、選択されたサブスクリプショングループから配信停止ボタンをクリックしたユーザーを配信停止します。
    - サブスクリプショングループを選択する際、この特定グループを購読しているユーザーのみをターゲットにするには、[**ターゲットオーディエンス**] で [**サブスクリプショングループ**] フィルターを追加します。ワンクリック配信停止用に選択したサブスクリプショングループは、ターゲットにしているサブスクリプショングループと一致していなければなりません。サブスクリプショングループに不一致がある場合、すでに配信停止済みのサブスクリプショングループから配信停止しようとしているユーザーに送信するリスクがあります。

{% alert important %}
[**特定のサブスクリプショングループから配信停止**] 設定は、ワンクリックリスト配信停止ヘッダーにのみ適用されます。このオプションを選択しても、mailto の配信停止ヘッダーは影響を受けません。この方法を使って配信停止した受信者は、特定のサブスクリプショングループからの配信停止ではなく、グローバルな配信停止として記録されます。この設定を選択する際に、mailto リスト配信停止ヘッダーによるグローバル配信停止を除外したい場合は、[サポート]({{site.baseurl}}/support_contact/)に連絡してください。
{% endalert %}

- **カスタム**：配信停止を直接処理するためのカスタムのワンクリック配信停止 URL を追加します。
- **配信停止を除外**

{% alert important %}
ワンクリック配信停止や任意の配信停止メカニズムを除外するのは、パスワードのリセット、領収書、確認メールなど、トランザクションメッセージングに対してのみ行ってください。
{% endalert %}

この設定を変更すると、このメールにおけるワンクリックリスト配信停止のデフォルト動作がオーバーライドされます。

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 要件

独自のカスタム配信停止機能を使用してメールを送信する場合は、設定したワンクリック配信停止 URL を RFC 8058 に確実に適合させるために、次の要件を満たす必要があります。

* URL は配信停止 POST リクエストを処理できる必要があります。
* URL は `https://` で始まる必要があります。
* URL は HTTPS リダイレクトやボディを返してはなりません。ランディングページや他のタイプのウェブページに移動するワンクリック配信停止リンクは、RFC 8058 に準拠していません。
* POST リクエストが Cookie を設定してはなりません。

[**カスタムの list-unsubscribe ヘッダー**] を選択して、独自に構成したワンクリック配信停止エンドポイントと、オプションの「mailto:」を追加します。ワンクリック配信停止 HTTP が Yahoo および Gmail の一括送信者に対する要件であるため、Braze では、カスタムの list-unsubscribe ヘッダーをサポートするために URL を入力する必要があります。

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## メールの件名行の追加

テストメールとシードメールの件名行に「[TEST]」と「[SEED]」を含めるには、トグルを使用します。これは、テストとして送信されたメールキャンペーンの識別に役立ちます。

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 新規メールで CSS をデフォルトでインライン化

CSS インライン化は、メールと新規メールの CSS スタイルを自動的にインライン化する手法です。一部のメールクライアントでは、これによりメールのレンダリング方法が改善される可能性があります。

この設定を変更しても、既存のメールメッセージやテンプレートには一切影響しません。メッセージまたはテンプレートの作成中に、いつでもこのデフォルトをオーバーライドできます。詳細については、[CSS インライン化]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)を参照してください。

## メールアドレスを変更したユーザーの再購読

ユーザーがメールアドレスを変更したときに、そのユーザーを自動的に再購読させることができます。例えば、以前配信停止されていたワークスペースユーザーが、メールアドレスを Braze の配信停止リストにないものに変更した場合、自動的に再購読されます。

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## サブスクリプションのページおよびフッター

{% tabs local %}
{% tab Custom Footer %}

商用メールの場合、[CAN-SPAM 法](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)では、すべての商用メールに配信停止オプションを含めることを義務付けています。カスタムフッター設定を使用すると、CAN-SPAM を遵守したうえで、メールのオプトアウトフッターをカスタマイズできます。遵守状態を維持するために、このワークスペースのキャンペーンの一部として送信されるすべてのメールにカスタムフッターを追加する必要があります。

メールメッセージングのカスタムフッターを作成するときには、次の要件に注意してください。
- 配信停止 URL と物理的な郵送先住所を含める必要があります。
- 100 KB 未満でなければなりません。

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

カスタムフッターの Liquid テンプレートの詳細については、[カスタムフッター]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)に関するドキュメントを参照してください。

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze を使用すると、独自の HTML を使用して**カスタム配信停止ページ**を設定できます。このページは、ユーザーがメールの下部から配信停止を選択した後に表示されます。このページは 750 KB 未満でなければならないことに注意してください。 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% tab Custom Opt-In Page %}

独自の HTML を使用してカスタムのオプトインページを作成できます。これをメールに含めると、特にユーザーのライフサイクル全体を通じてブランディングとメッセージの一貫性を維持する場合にメリットがあります。このページは 750 KB 未満でなければならないことに注意してください。 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% endtabs %}

{% alert tip %}
サブスクリプションページやフッターの [**プレビュー**] セクションで、[**プレビューリンクをコピー**] を選択すると、ランダムなユーザーがメールフッター、配信停止ページ、またはオプトインページをどのように見るかを示す共有可能なプレビューリンクが生成され、コピーされます。リンクは7日間有効です。その後は再生成する必要があります。
{% endalert %}

## よくある質問

### ワンクリック配信停止

{% details ワンクリック配信停止 URL（list-unsubscribe ヘッダー経由）をユーザー設定センターにリンクできますか？ %}
いいえ、これは RFC 8058 に準拠していないため、Yahoo と Gmail のワンクリック配信停止要件に適合しません。
{% enddetails %}

{% details ユーザー設定センターを作成する際に「メール本文に配信停止リンクが含まれていません」というエラーメッセージが表示されるのはなぜですか？ %}
ユーザー設定センターは、配信停止リンクとはみなされません。CAN-SPAM に準拠するためには、メール受信者が商用メールの配信を停止できるようにしなければなりません。
{% enddetails %}

{% details ワンクリック配信停止設定を有効にした後、過去のメールキャンペーンやキャンバスを編集する必要がありますか？ %}
メッセージレベルのワンクリックリスト配信停止設定のユースケースに該当しない場合は、[**メール設定**] でこの設定がオンになっている限り、必要なアクションはありません。Braze は、すべての送信されるマーケティングおよびプロモーションメッセージに、ワンクリック配信停止ヘッダーを自動的に追加します。ただし、ワンクリック配信停止の動作をメッセージごとに設定する必要がある場合は、それに応じてメールで以前のキャンペーンとキャンバスステップを更新する必要があります。
{% enddetails %}

{% details 元のメッセージや生データで list-unsubscribe ヘッダーとワンクリック配信停止ヘッダーが確認できるのに、Gmail や Yahoo で配信停止ボタンが表示されないのはなぜですか？ %}
最終的に、Gmail と Yahoo が list-unsubscribe ヘッダーまたはワンクリック配信停止ヘッダーを表示するかどうかを決定します。新しい送信者または送信者のレピュテーションが低い場合、配信停止ボタンが表示されないことがあります。
{% enddetails %}

{% details カスタムのワンクリック配信停止ヘッダーは Liquid をサポートしていますか？ %}
はい、Liquid および条件付きロジックがサポートされており、ヘッダーのダイナミックなワンクリック配信停止 URL を使用できます。
{% enddetails %}

{% alert tip %}
条件付きロジックを追加する場合、Braze は空白を削除しないため、URL に空白を追加する出力値を含めないようにしてください。
{% endalert %}

### メッセージレベルのワンクリックリスト配信停止

{% details ワンクリック用のメールヘッダーを手動で追加し、メール配信停止ヘッダーがオンになっている場合、どのような動作になりますか？ %}
ワンクリック配信停止用に追加されたメールヘッダーは、このキャンペーンの今後のすべての送信に適用されます。
{% enddetails %}

{% details キャンペーンを開始するために、メッセージバリアント間でサブスクリプショングループが一致している必要があるのはなぜですか？ %}
AB テストを実施するキャンペーンでは、Braze はユーザーにランダムにいずれかのバリアントを送信します。同一キャンペーンに異なるサブスクリプショングループが2つ設定されている場合（バリアント A がサブスクリプショングループ A に、バリアント B がサブスクリプショングループ B に設定されている）、サブスクリプショングループ B のみに登録しているユーザーがバリアント B を受け取ることを保証できません。ユーザーが既にオプトアウト済みのサブスクリプショングループから再度配信停止するケースが考えられます。
{% enddetails %}

{% details メール設定でメール配信停止ヘッダー設定がオフになっていますが、キャンペーンの送信情報ではワンクリックリスト配信停止設定が「ワークスペースのデフォルトを使用」に設定されています。これはバグですか？ %}
いいえ。ワークスペース設定がオフで、メッセージ設定が [**ワークスペースのデフォルトを使用**] に設定されている場合、Braze は [**メール設定**] で構成された内容に従います。これは、キャンペーンに対してワンクリック配信停止ヘッダーを追加しないことを意味します。
{% enddetails %}

{% details サブスクリプショングループがアーカイブされた場合はどうなりますか？送信済みメールのワンクリック配信停止は機能しなくなりますか？ %}
ワンクリックの [**送信情報**] で参照されているサブスクリプショングループがアーカイブされても、Braze はワンクリックからの配信停止を処理し続けます。サブスクリプショングループは、ダッシュボード（Segment フィルター、ユーザープロファイル、および類似の領域）に表示されなくなります。
{% enddetails %}

{% details ワンクリック配信停止設定はメールテンプレートで利用できますか？ %}
メールテンプレートは送信ドメインに割り当てられていないため、現在この機能を追加する予定はありません。メールテンプレートのこの機能に興味がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)を送信してください。
{% enddetails %}

{% details この機能は、カスタムオプションに追加されたワンクリック配信停止 URL が有効かどうかをチェックしますか？ %}
Braze ダッシュボードでは、リンクのチェックや検証は行っていません。ローンチする前に、URL を十分にテストしてください。
{% enddetails %}