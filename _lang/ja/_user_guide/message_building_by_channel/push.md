---
nav_title: プッシュ
article_title: プッシュ
page_order: 6
layout: dev_guide
guide_top_header: "プッシュ"
guide_top_text: "プッシュ通知は、モバイルや Web を通じて時間制限のあるアクション喚起を送る確実な方法であり、しばらくアプリを利用していないユーザーを再びエンゲージメントする手段でもあります。ユーザーを直接コンテンツに誘導し、アプリケーションの価値を示します。プッシュ通知はユーザーを特定の場所へ誘導するのに便利ですが、賢く使うことが大切です。<br><br> 以下の記事を読んだり、[プッシュ Brazeラーニングコース](https://learning.braze.com/messaging-channels-push)をチェックしたりして、誰にプッシュを送信できるのか、どのように送信するのか、そして Braze が提供する高度なプッシュ機能について学びましょう。プッシュ通知の例については、[顧客ストーリー](https://www.braze.com/customers)をご覧ください。"
description: "このランディングページは、プッシュメッセージのホームです。ここには、プッシュタイプ、プッシュ登録、プッシュイネーブルメント、プッシュプライマー、プッシュレポートなどに関する記事があります。"
channel:
  - push

guide_featured_title: "よく読まれている記事"
guide_featured_list:
- name: プッシュタイプ
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: プッシュ登録
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: プッシュ有効化とサブスクリプション
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: プッシュメッセージを作成する
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "その他の記事"
guide_menu_list:
- name: 詳細オプション
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: プッシュプライマー
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: レポート
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Android オプション
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: iOS オプション
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Web プッシュ
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: ベストプラクティス
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: メッセージのロケール
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: 一般的なプッシュエラーメッセージ
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: トラブルシューティング
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: よくある質問
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}ユースケース

![複数の Apple 製品にわたるプッシュメッセージの例。]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![iPhone のホーム画面に表示される Stopwatch のプッシュメッセージの例:「こんにちは！これは iOS プッシュ通知です。」]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

プッシュ通知は、新しいユーザーを引き付け、再エンゲージメントキャンペーンを行うための非常に優れたツールです。一般的なプッシュメッセージのユースケースの例を以下に示します。

| ユースケース | 説明 |
| -------- | ----------- |
| 初期オンボーディング | ユーザーがアプリの使用に向けた最初のステップ（アカウントの登録など）を完了するまで、アプリの価値は大幅に制限されます。プッシュ通知を使用して、これらのステップを完了し、アプリをフルに活用し始めるようユーザーを促しましょう。 |
| 初回購入 | ユーザーがアプリを快適に使用できるようになったら、プッシュ通知を使用してユーザーをアプリ内購入者にコンバートできます。 |
| 新機能 | プッシュ通知は、離脱したユーザーに新機能を通知し、アプリに呼び戻すのに効果的です。 |
| 時間制限のあるオファー | オファーに期限がある場合、プッシュは期限切れになる前にユーザーに知らせる優れた方法です。通常、これらのメッセージは高い緊迫感を伝え、最近離脱したユーザーにアプリを思い出してもらうのに最適です。<br><br> 例えば、アプリがゲームであり、毎日プレイし続けているユーザーにゲーム内通貨ボーナスを提供しているとします。連続記録が途切れそうだとユーザーに警告するのは、一定日数を超えた場合に合理的なプッシュ通知と言えます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

離脱ユーザーの再エンゲージメントの詳細については、このトピックに関する[クイックウィン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users)ページをご覧ください。

## プッシュを使用するための前提条件

Braze を使用してプッシュメッセージを作成・送信するには、開発者と協力してプッシュを Web サイトまたはアプリに統合する必要があります。詳細なステップについては、各プラットフォームの統合ガイドを参照してください。

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## プッシュプライミング

ユーザーがメッセージを受信するにはプッシュ通知にオプトインする必要があることに留意してください。つまり、アプリ内メッセージを使用して、プッシュ通知を送信する理由やプッシュを有効にすることで得られるメリットを顧客に説明することをお勧めします。このプロセスは[プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)と呼ばれます。

## プッシュメッセージ規定

プッシュ通知は顧客の携帯電話やブラウザに直接届く干渉的なメッセージングの一種であるため、アプリやサイトを通じてプッシュメッセージを送信する際のガイドラインが存在します。

### アプリのモバイルプッシュ規定

{% alert important %}
プッシュメッセージは、Apple App Store および Google の Play Store ポリシーのガイドラインに準拠する必要があります。特に、プッシュメッセージを広告、スパム、プロモーションなどとして使用する場合に注意が必要です。
{% endalert %}

|Apple App Store ポリシー|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) 許容されません：(i) App Store に類似した、または一般的な関心のコレクションとして、サードパーティ製のアプリ、拡張機能、またはプラグインを表示するためのインターフェイスを作成すること。| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) プッシュ通知はアプリの機能に必須であってはならず、機密性の高い個人情報や秘密情報の送信に使用してはなりません。プッシュ通知をプロモーションやダイレクトマーケティングの目的で使用することはできません。ただし、アプリの UI に表示される同意文言を通じて顧客が明示的にオプトインし、かつアプリ内でそのようなメッセージの受信をオプトアウトする方法を提供している場合を除きます。|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) ハードウェアやオペレーティングシステムに内蔵されている機能（プッシュ通知、カメラ、ジャイロスコープなど）、または Apple のサービスやテクノロジー（Apple Music へのアクセス、iCloud ストレージ、Screen Time API など）を収益化することは認められません。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Play ストアポリシー|
|---|
|[不正な使用またはシステム機能の模倣](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) 通知や警告などのシステム機能を模倣したり妨害したりするアプリや広告は許可されていません。システムレベルの通知は、ユーザーに特別価格を通知する航空会社のアプリや、ユーザーにゲーム内プロモーションを通知するゲームなど、アプリの重要な機能にのみ使用できます。|
{: .reset-td-br-1 role="presentation" }