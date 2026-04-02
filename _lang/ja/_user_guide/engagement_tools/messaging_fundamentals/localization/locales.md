---
nav_title: 多言語メッセージ
article_title: 多言語メッセージ
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "この記事では、メッセージでロケールを使用する方法について説明します。"
---

# 多言語メッセージ

> ワークスペースにロケールを追加した後、単一のプッシュ通知、メール、バナー、アプリ内メッセージ、またはコンテンツブロック内で、異なる言語のユーザーをすべてターゲットにできます。

## 前提条件

{% tabs %}
{% tab Multi-language locales %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Message types %}

| 機能 | 必要なユーザー権限 |
| --- | --- |
| メッセージ&nbsp;タイプ | キャンペーンやキャンバスにロケールと翻訳を追加するには、以下の権限が必要です：<br><br> {::nomarkdown}詳細な権限: <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul> レガシー権限: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Templates %}

| 機能 | 必要なユーザー権限 |
| --- | --- |
| テンプレート | ロケールと翻訳を追加するテンプレートタイプに応じて、以下の権限が必要です：<br><br> {::nomarkdown}詳細な権限: <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul> レガシー権限: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## ロケールの使用

### ステップ 1：ロケールを設定する

メッセージに翻訳を追加する前に、まず[サポートするロケールを作成する]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/)必要があります。ロケールは、メッセージングで利用可能な言語（およびオプションで地域）のバリエーションを定義します。

### ステップ 2：コンテンツに翻訳マークを付ける

翻訳するテキストを Liquid 翻訳タグ {% raw %}`{% translation your_id_here %}` と `{% endtranslation %}`{% endraw %} で囲み、タグ ID を割り当てます。翻訳タグ ID はメッセージ内で一意である必要があります。テキストを明確に説明するセマンティックな ID 名の使用を検討してください（例：{% raw %}`{% translation header %}`{% endraw %}）。

翻訳用にマークされたメッセージの例：{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
翻訳するテキストをハイライトし、キーボードショートカット **Cmd + Alt + L**（macOS）または **Ctrl + Alt + L**（Windows）を使用して翻訳タグで囲みます。<br><br>このショートカットは、メールおよびコンテンツブロックのドラッグ＆ドロップエディターを除く、多言語メッセージングをサポートするすべてのチャネルで使用できます。これらのエディターでは、左サイドバーの**「パーソナライゼーションを追加」**ボタンを使用して翻訳タグを追加してください。
{% endalert %}

#### URL のローカライズ

コンテンツを翻訳する際、URL はリンク切れを防ぐために特別な処理が必要です。

##### 標準（静的）URL

静的 URL はエディターで手動入力します（例：`https://example.com`）。以下の推奨事項もご確認ください：

| 推奨事項 | 理由 |
| --- | --- |
| プロトコル（`https://`）は翻訳タグの外に置いてください。ドメインとパスのみを囲みます（例：`example.com/en`）。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れの原因となる可能性があります。 |
| クエリパラメータを翻訳タグ内に含めないでください（例：`?utm_source=promo`）。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れの原因となる可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

両方の推奨事項に従った標準 URL の例：

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz%}{% endtranslation %}">Click Here</a>
```
{% endraw %}

{% alert important %}
[メールリンクトラッキング](#email-link-tracking)（リンクエイリアスまたはリンクテンプレート）を使用している場合、URL を翻訳タグで囲む際に追加の設定が必要です。
{% endalert %}

#### HTML 属性と構造

翻訳タグで囲むのは、人間が読むテキストのみにしてください。HTML 属性（`class`、`style`、`id` など）やその他の構造コードを囲むことは避けてください。HTML 属性はレイアウト、スタイル、機能を制御します。翻訳タグで囲むと、ローカライズされたメッセージのフォーマットやスタイルが崩れる可能性があります。

正しく囲まれたテキスト：

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details 誤って囲まれたテキスト %}

このテキストは**誤って**囲まれています：

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### ステップ 3：メッセージにロケールを追加する

メッセージに翻訳タグを追加した後、エディターで**「言語の管理」**を選択し（メールおよびコンテンツブロックのドラッグ＆ドロップエディターでは**「言語」**）、翻訳を追加するロケールを少なくとも1つ選択します。

![デフォルトロケールまたはカスタム属性を選択するオプションがあるロケール追加ドロップダウン。]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### 翻訳を含むコンテンツブロック

メッセージに翻訳が保存済みのコンテンツブロックが含まれている場合、それらの翻訳を再アップロードする必要はありません。保存された翻訳は、コンテンツブロックがメッセージに追加されると自動的に適用されます。

**「言語の管理」**モーダルでは、翻訳が保存されたコンテンツブロックが、サポートするロケールとともにリストに表示されます。これにより、新しい翻訳を追加する前に、メッセージのどの部分がすでにローカライズされているかを確認できます。

![翻訳が保存されたコンテンツブロックのリストがある「言語の管理」セクション。]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
各コンテンツブロックに、メッセージに追加されたすべてのロケールの翻訳が含まれていることを確認してください。追加したロケールの翻訳がコンテンツブロックに不足している場合、そのロケールのユーザーには元の言語で表示されます。
{% endalert %}

### ステップ 4：翻訳を追加する

ロケールを選択した後、以下のいずれかの方法でメッセージに翻訳を追加します：

![CSV でアップロードするか、翻訳パートナーに接続するオプションがある「翻訳を追加」タブ。]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSV テンプレートをアップロード %}

**「テンプレートをダウンロード」**を選択すると、選択した翻訳 ID とロケールの対応表を含む CSV がダウンロードされます。各ロケールの翻訳を入力してください。完成したファイルをアップロードすると、翻訳がメッセージに適用されます。

{% alert important %}
英語以外の文字の表示問題を防ぐため、翻訳 CSV の編集に Excel を使用しないでください。
{% endalert %}

![タイトル、オファーテキスト、オファー金額、CTA の翻訳タグを含む CSV。]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab 翻訳 API を使用 %}

パートナー翻訳 API を使用して、キャンペーンやキャンバスの翻訳を管理・更新します。外部のローカライゼーションシステムを使用している場合や、翻訳パートナーと直接接続したい場合に便利です。

キャンバスで翻訳エンドポイントを使用するには、以下のパラメータを含めてください：
  - `workflow_id`
  - `step_id`
  - `message_variation_id` 

{% alert note %}
キャンバスの起動後に作成されたキャンバスステップで翻訳 API を使用する場合、API に渡す `message_variation_id` は空または空白になります。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 5：翻訳をプレビューする

メッセージをプレビューするには、**「ユーザーとしてプレビュー」**ドロップダウンから**「多言語ユーザー」**オプションを選択します。これにより、異なるロケール定義を切り替えて、メッセージのすべての翻訳をプレビューできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## 翻訳の管理

### キャンバスステップまたはキャンペーンの複製と翻訳

キャンバスステップ、キャンペーン、またはバリエーションを複製すると、翻訳も含まれます。ワークスペース間でコピーする場合も同様ですが、コピー先のワークスペースでロケールが定義されている必要があります。キャンバスやキャンペーンに変更を加える際には、必ず翻訳を確認し、適宜更新してください。

### コンテンツブロックに翻訳を保存する

コンテンツブロックは、メッセージと同じ方法で多言語をサポートします。コンテンツブロックを作成または編集する際に、コンテンツに翻訳タグを付け、ロケールを追加し、CSV または[翻訳 API]({{site.baseurl}}/api/endpoints/translations/) を使用して翻訳をアップロードできます。

保存された翻訳はコンテンツブロックに関連付けられたままです。ブロックがメッセージに追加されると、その翻訳が自動的に含まれます。

### 右から左に読むメッセージ

右から左へ書く言語（アラビア語など）の翻訳ファイルを入力する際は、翻訳を `span` で囲んで正しくフォーマットされるようにしてください：

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### メールリンクトラッキング

メールキャンペーンでは、Braze は各 URL にトラッキング情報（クエリパラメータ）を追加してリンクを追跡します。この動作は[リンクエイリアス]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/)と[リンクテンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template)の両方をサポートしています。

URL が翻訳タグで囲まれている場合、Braze はトラッキング情報を追加する場所を判断できないことがあります。正しく動作させるには、トラッキングを追加する場所を示す特殊文字を URL の末尾に含める必要があります。

URL では2つの特殊文字を使用してこの動作を制御します：
  - `?` は、まだトラッキングがない URL にトラッキングを追加します。
  - `&` は、URL にすでに `?` が含まれている場合に追加のトラッキングを追加します。URL には `?` を1つだけ含めることができます。

| URL | `?`&nbsp;を含む | 説明 | 例 |
| --- | --- | --- | --- |
| 標準 URL | いいえ | URL にまだ `?` が含まれていない場合、閉じ翻訳タグの後に `?` を追加します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| 標準 URL | はい | URL にすでに `?` が含まれている場合、URL の末尾（閉じ翻訳タグの後）に `&` を使用します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid 生成 | いいえ | 生成された URL にまだ `?` が含まれていない場合、閉じ翻訳タグの後に `?` を使用します。 | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid 生成 | はい | 生成された URL にすでに `?` が含まれている場合、閉じ翻訳タグの後に `&` を使用します。 | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 言語設定とアクセシビリティ

HTML ベースのチャネル（メール、アプリ内メッセージ、バナー、ランディングページ、コンテンツカード）では、Braze はレンダリングされたメッセージにアクセシビリティ言語（`lang`）属性を追加します。この属性は、スクリーンリーダーなどの支援技術がテキストを正しく解釈し、発音するのに役立ちます。

この属性がない場合、スクリーンリーダーはコンテンツがユーザーのデバイスセットアップ時に設定されたデフォルト言語であると想定します。メッセージが異なる言語の場合、スクリーンリーダーがすべてを正しく発音できない可能性があります。

#### アクセシビリティ言語の設定

アクセシビリティ言語は2つのレベルで設定できます：

##### メッセージレベル

メッセージ設定で、**「アクセシビリティ」**セクションに移動し、ドロップダウンから言語を選択するか、Liquid を使用してアクセシビリティ言語を動的に設定します。これはメッセージ内のすべてのコンテンツに適用されます。

##### ロケールレベル

多言語メッセージの場合、**「ローカライゼーション設定」**で各ロケールにアクセシビリティ言語を設定します。新しいメッセージが作成されると、**「アクセシビリティ」**セクションでデフォルトで {% raw %}`{{accessibility_language}}`{% endraw %} が選択されます。これにより、アクセシビリティ言語がロケール設定にマッピングされます。

#### 標準

アクセシビリティ言語は HTML の `lang` 属性にマッピングされます。これは [WCAG 2.1 レベル A の要件](https://dequeuniversity.com/rules/axe/4.2/html-has-lang)（達成基準 3.1.1）です。多言語コンテンツの場合、HTML 内で `lang` 属性を直接使用して、個々のコンテンツブロックに言語を設定することもできます。

## よくある質問

#### 翻訳タグの制限は何ですか？

翻訳タグを使用する際、以下の制限が適用されます：

- 各メッセージには最大200個の翻訳タグを含めることができます。
- 各デフォルトテキスト（翻訳タグ間のコンテンツ）は最大2,000文字です。
- ロケールごとの翻訳は最大409,600バイト（約409.6&nbsp;KB）です。

#### ロケールの翻訳文を変更できますか？

はい。まず CSV で編集を行ってから、ファイルを再度アップロードすることで翻訳文を変更できます。

### Braze は翻訳を提供しますか？

いいえ。CSV のアップロードまたは翻訳 API を使用して、[ご自身で翻訳を提供する](#step-4-add-translations)必要があります。

### 翻訳タグをネストできますか？

いいえ。

#### HTML メッセージ全体を翻訳タグで囲むことはできますか？

いいえ。ベストプラクティスとして、人間が読むテキストやローカライズが必要なコンテンツのみを囲むようにしてください。これにより、フォーマット、リンク、その他の非テキスト要素の破損を防ぐことができます。

また、正確な翻訳を作成し、パフォーマンスやサイズの制限を回避するために、意味的に関連する小さなテキスト単位で囲むことを検討してください。

#### ロケールの翻訳文を変更できますか？

はい。CSV を使用している場合は、まずファイルで編集を行ってから、再度アップロードして翻訳文を変更します。[翻訳 API]({{site.baseurl}}/api/endpoints/translations/) を使用している場合は、更新エンドポイントを使用して変更を行います。

#### Braze はどのような検証や追加チェックを行いますか？

| シナリオ | Braze での検証 |
| --- | --- |
| メッセージに、異なるテキストにマッピングされた2つ以上の一致する翻訳 ID が含まれている。 | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルに1つ以上の翻訳タグ ID が欠落している。 | この翻訳ファイルはアップロードされません。 |
| 翻訳ファイルに、メッセージに存在しないロケールが含まれている。 | この翻訳ファイルはアップロードされません。 |
| 翻訳テンプレートをダウンロードする前に、翻訳タグをメッセージに追加する必要があります。 | この翻訳ファイルはダウンロードされません。 |
| アップロードされたファイルに含まれる翻訳タグがメッセージに存在しない。 | 余分な翻訳はメッセージに保存されません。 |
| {% raw %}メッセージに1つ以上の壊れた Liquid タグが含まれています。開始タグには `{% translation your_id_here %}` を使用し、閉じ翻訳タグには `{% endtranslation %}` を使用してください。{% endraw %} | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルに、メッセージ内のテキストと一致しないデフォルトテキストが含まれている。 | 翻訳は追加されますが、元のメッセージテキストは更新されません。 |
| メッセージ内の1つ以上のロケールが設定で削除され、存在しなくなった。 | すでに追加された翻訳はメッセージ内に引き続き存在します。メッセージから削除すると、翻訳は失われます。 |
| 翻訳タグに完全な URL または Liquid 生成の URL が含まれている。 | リンク切れやリンクトラッキングの問題が発生する可能性があるため、URL を含む翻訳タグが特定されます。 |
| 翻訳タグにクエリパラメータが含まれている。 | リンク切れやリンクトラッキングの問題が発生する可能性があるため、クエリパラメータを含む翻訳タグが特定されます。 |
| 翻訳タグに HTML 属性または構造が含まれている。 | スタイルやフォーマットの問題が発生する可能性があるため、HTML 属性または構造を含む翻訳タグが特定されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }