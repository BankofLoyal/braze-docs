---
nav_title: 푸시
article_title: 푸시
page_order: 6
layout: dev_guide
guide_top_header: "푸시"
guide_top_text: "푸시 알림은 모바일 또는 웹을 통해 시간에 민감한 행동 촉구를 전송하고, 한동안 앱에 들어오지 않은 사용자의 재참여를 유도하는 검증된 방법입니다. 푸시 알림은 사용자를 콘텐츠로 직접 안내하고, 애플리케이션의 가치를 보여줍니다. 사용자를 특정 장소로 유도하는 데 유용하지만, 현명하게 사용해야 합니다. <br><br> 푸시를 보낼 수 있는 대상, 푸시 전송 방법, Braze가 제공하는 고급 푸시 기능에 대해 알아보려면 다음 문서를 읽거나 [푸시 Braze 학습 과정](https://learning.braze.com/messaging-channels-push)을 확인하세요. 푸시 알림의 예시는 [고객 사례](https://www.braze.com/customers)를 확인하세요."
description: "이 랜딩 페이지에는 푸시 메시지 관련 내용이 정리되어 있습니다. 여기에서 푸시 유형, 푸시 등록, 푸시 인에이블먼트, 푸시 프라이머, 푸시 보고서 등에 대한 문서를 확인할 수 있습니다."
channel:
  - push

guide_featured_title: "인기 문서"
guide_featured_list:
- name: 푸시 유형
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: 푸시 등록
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: 푸시 활성화 및 구독
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: 푸시 메시지 만들기
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "더 많은 문서"
guide_menu_list:
- name: 고급 옵션
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: 푸시 프라이머
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: 보고서
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Android 옵션
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: iOS 옵션
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: 웹 푸시
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: 모범 사례
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: 메시지의 로캘
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: 일반적인 푸시 오류 메시지
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: 문제 해결
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: 자주 묻는 질문
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}활용 사례

![Apple 제품에서의 푸시 메시지 예시.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![iPhone 홈 화면의 Stopwatch에서 보낸 푸시 메시지 예시: "Hello! This is an iOS Push".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

푸시 알림은 신규 사용자를 유치하고 재참여 캠페인을 진행하기 위한 훌륭한 도구입니다. 다음은 일반적인 푸시 메시지 활용 사례입니다.

| 활용 사례 | 설명 |
| -------- | ----------- |
| 초기 온보딩 | 사용자가 계정 등록 등 앱 사용을 위한 초기 단계를 완료하기 전까지는 앱의 가치가 크게 제한됩니다. 푸시 알림을 사용하여 사용자가 이러한 단계를 완료하도록 유도하면 앱을 완전히 활용할 수 있게 됩니다. |
| 첫 구매 | 사용자가 앱 사용에 익숙해지면 푸시 알림을 사용하여 인앱 구매자로 전환하는 데 도움을 줄 수 있습니다. |
| 새로운 기능 | 푸시 알림은 이탈한 사용자에게 앱으로 다시 돌아올 수 있는 새로운 기능을 알리는 데 효과적일 수 있습니다. |
| 시간 한정 오퍼 | 오퍼에 시간 제한이 있다면, 만료되기 전에 사용자에게 알리는 데 푸시가 좋은 방법이 될 수 있습니다. 이러한 메시지는 일반적으로 긴박감이 높으며, 최근에 이탈한 사용자에게 앱을 상기시키는 데 최적입니다.<br><br> 예를 들어, 앱이 게임이고 사용자가 매일 게임을 플레이하는 연속 기록을 유지하면 인게임 화폐 보너스를 제공한다고 가정해 보겠습니다. 특정 일수를 초과한 사용자에게 연속 기록이 깨질 위험이 있다고 알리는 것은 합리적인 푸시가 될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

휴면 사용자의 재참여에 대한 자세한 내용은 관련 주제의 [빠른 성공]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) 페이지를 참조하세요.

## 푸시 사용을 위한 필수 조건

Braze를 사용하여 푸시 메시지를 생성하고 전송하려면 먼저 개발자와 협력하여 웹사이트 또는 앱에 푸시를 통합해야 합니다. 자세한 단계는 각 플랫폼별 통합 가이드를 참조하세요:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## 푸시 프라이밍

사용자가 메시지를 받으려면 푸시 수신에 옵트인해야 하므로, 인앱 메시지를 사용하여 고객에게 푸시 알림을 보내려는 이유와 푸시를 활성화하면 어떤 이점이 있는지 설명하는 것이 좋습니다. 이 과정을 [푸시 프라이밍]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)이라고 합니다.

## 푸시 메시지 규정

푸시 메시지는 고객의 휴대폰이나 브라우저로 직접 전송되는 침입적인 유형의 메시징이기 때문에, 앱과 사이트를 통해 푸시 메시지를 전송하기 위한 가이드라인이 있습니다.

### 앱에 대한 모바일 푸시 규정

{% alert important %}
푸시 메시지는 광고, 스팸, 프로모션 등으로 푸시 메시지를 사용하는 것과 관련된 Apple App Store 및 Google Play 스토어 정책의 가이드라인을 준수해야 합니다.
{% endalert %}

|Apple App Store 정책|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) 허용되지 않는 행위: (i) App Store와 유사하거나 일반 관심사 컬렉션으로 서드파티 앱, 확장 프로그램 또는 플러그인을 표시하기 위한 인터페이스를 만드는 행위.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) 푸시 알림은 앱이 작동하는 데 필수적이어서는 안 되며, 민감한 개인 정보나 기밀 정보를 전송하는 데 사용해서는 안 됩니다. 고객이 앱 UI에 표시된 동의 문구를 통해 명시적으로 수신에 동의하고, 사용자가 이러한 메시지 수신을 거부할 수 있는 방법을 앱에서 제공하지 않는 한, 푸시 알림을 프로모션이나 직접 마케팅 목적으로 사용해서는 안 됩니다.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) 푸시 알림, 카메라 또는 자이로스코프와 같은 하드웨어 또는 운영체제에서 제공하는 내장 기능이나, Apple Music 액세스, iCloud 저장소 또는 Screen Time API와 같은 Apple 서비스 및 기술을 수익화할 수 없습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Play 스토어 정책|
|---|
|[시스템 기능의 무단 사용 또는 모방](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Google은 알림이나 경고와 같은 시스템 기능을 모방하거나 방해하는 앱이나 광고를 허용하지 않습니다. 시스템 수준 알림은 사용자에게 특가 상품을 알려주는 항공사 앱이나 게임 내 프로모션을 알려주는 게임과 같이 앱의 핵심 기능에만 사용할 수 있습니다.|
{: .reset-td-br-1 role="presentation" }