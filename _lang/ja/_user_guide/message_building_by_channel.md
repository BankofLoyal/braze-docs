---
nav_title: チャネル別のメッセージ構築
article_title: チャネル別メッセージ構築
page_order: 5
layout: dev_guide

guide_top_header: "チャネル別メッセージ構築"
guide_top_text: "メッセージングチャネルは、スマートフォンや Web ブラウザでのプッシュ通知、メール、アプリ内メッセージなどを通じて、顧客とコミュニケーションを図ることができる手段です。これらのチャネルと Braze での活用方法に関する詳細については、以下のセクションを参照してください。または、<a href='https://learning.braze.com/series/messaging-channels' target='_blank'>Messaging Channels</a> の Brazeラーニングコースをご確認ください。<br><br>Braze を使えば、各チャネルでアクセシブルなメッセージングキャンペーンを作成できます。エンジニアと協力して、実装においてアクセシビリティ基準を満たすようにしてください。"
description: "このランディングページは、Braze メッセージングチャネルを対象としています。メッセージングチャネルは、スマートフォンや Web ブラウザでのプッシュ通知、メール、アプリ内メッセージなどを通じて、顧客とコミュニケーションを図ることができる手段です。"

guide_featured_title: "使用可能なチャネル"
guide_featured_list:
- name: バナー
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: コンテンツカード
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: メールメッセージング
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "アプリ内メッセージング"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: "KakaoTalk"
  link: /docs/user_guide/message_building_by_channel/kakaotalk/
  image: /assets/img/braze_icons/phone-01.svg
- name: "LINE"
  link: /docs/user_guide/message_building_by_channel/line/
  image: /assets/img/braze_icons/phone-01.svg
- name: プッシュメッセージング
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: SMS、MMS、RCS
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## アクセシビリティに関するリソース

Braze を使えば、各チャネルでアクセシブルなメッセージングキャンペーンを作成できます。エンジニアと協力して、実装においてアクセシビリティ基準を満たすようにしてください。追加のガイダンスが必要な場合は、以下をお勧めします。

- [Accessible Messaging Foundations](https://learning.braze.com/accessible-messaging-foundations):この Brazeラーニングコースでは、ブランドコミュニケーションに適用される基本的なアクセシビリティの原則を学びます。
- [アクセシブルなメッセージの作成]({{site.baseurl}}/help/accessibility/):代替テキストの追加方法や、Braze 内で支援技術向けにコンテンツを構造化する方法について説明します。

{% multi_lang_include accessibility/feedback.md %}

## メッセージチャネルの選択

キャンペーンやキャンバスに最適なメッセージチャネルを決定する際には、メッセージのコンテンツと緊急性を常に考慮してください。

- **コンテンツ**は、メッセージの視覚的な訴求力の度合いです。マルチメディアやその他のアセットをコピーに追加して、コンテンツをより充実させることができます。
- **緊急性**は、メッセージがユーザーに届いて注意を引くまでの速さの尺度です。ユーザーがすぐに確認できる通知は緊急性が高く、アプリへのログインが必要なメッセージは緊急性が低くなります。

Braze のメッセージングマトリックスは、**コンテンツの複雑さ**と**配信の緊急度**を対応させることで、チャネル選択を効率化します。この2つの要素のバランスを取ることで、メッセージを邪魔にならず響くものにすることができます。

![モバイル／Web プッシュはシンプルなコンテンツで緊急性が高い、メールはリッチコンテンツで緊急性が高い、アプリ内／ブラウザメッセージはシンプルなコンテンツで緊急性が低い、コンテンツカードは緊急性が低くリッチコンテンツ]({% image_buster /assets/img_archive/messaging_matrix.png %})

マトリックスはコアチャネルを強調していますが、柔軟に適応できます。例えば、SMS や WhatsApp は緊急性の高いツールであり、マルチメディア形式を活用することでリッチコンテンツへとスケールアップします。このマトリックスの活用方法については、[Cross-Channel Messaging](https://learning.braze.com/cross-channel-messaging) に関する Brazeラーニングコースをご覧ください。

<br><br>