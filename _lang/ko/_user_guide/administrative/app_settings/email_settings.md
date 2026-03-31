---
nav_title: 이메일 기본 설정
article_title: 이메일 환경설정
page_type: reference
page_order: 14
description: "이 참조 문서는 Braze 대시보드에서 이메일 환경설정을 다루며, 발송 구성, 열람 추적 픽셀, 구독 페이지 및 바닥글 등을 포함합니다."
tool: Dashboard
channel: email
toc_headers: h2

---

# 이메일 환경설정

> 이메일 환경설정은 커스텀 바닥글, 커스텀 옵트인 및 옵트아웃 페이지 등 특정 발신 이메일 설정을 할 수 있는 곳입니다. 이러한 옵션을 발신 이메일에 포함하면 사용자에게 매끄럽고 일관된 경험을 제공할 수 있습니다.

**이메일 환경설정**은 대시보드의 **설정**에서 찾을 수 있습니다.

## 발송 구성

**발송 구성** 섹션의 이메일 설정은 이메일 캠페인에 포함되는 세부 정보를 결정합니다. 특히 이러한 설정은 사용자가 Braze로부터 이메일을 받을 때 보게 되는 내용과 주로 관련이 있습니다.

### 아웃바운드 이메일 설정

이메일 설정을 구성할 때, 발신 이메일 설정은 Braze가 사용자에게 이메일을 보낼 때 사용되는 이름과 이메일 주소를 식별합니다.

{% tabs local %}
{% tab Display Name Address %}

이 섹션에서는 Braze가 사용자에게 이메일을 보낼 때 사용할 수 있는 이름과 이메일 주소를 추가할 수 있습니다. 표시 이름과 이메일 주소는 이메일 캠페인을 작성할 때 **발송 정보** 옵션에서 사용할 수 있습니다. 아웃바운드 이메일 설정에 대한 업데이트는 기존 발송에 소급 적용되지 않습니다.

!["발신 이메일 설정" 섹션에는 다양한 표시 이름과 도메인을 위한 필드가 있습니다.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Liquid로 개인화하기

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 **발신 표시 이름**, **로컬 부분** 및 **도메인** 필드에서 사용하여 커스텀 속성에 따라 발신자 이름과 이메일 주소를 동적으로 템플릿화할 수 있습니다. **도메인** 필드에서 Liquid를 사용하려면 이메일 캠페인의 **발송 정보** 옵션으로 이동하여 **발신 표시 이름 + 주소 커스터마이즈** 체크박스를 선택해야 합니다.

![발신 표시 이름, 주소 및 도메인을 커스터마이즈하기 위한 필드가 있는 발송 설정.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

예를 들어, 조건 로직을 사용하여 다른 브랜드나 지역에서 보낼 수 있습니다:

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

이 섹션에 이메일 주소를 추가하면 이메일 캠페인의 회신 주소로 선택할 수 있습니다. 이메일 주소를 기본값으로 설정하려면 **기본값으로 설정**을 선택하세요. 이 이메일 주소는 이메일 캠페인을 작성할 때 **발송 정보** 옵션에서 사용할 수 있습니다.

!["회신 주소" 섹션에는 여러 회신 주소를 입력할 수 있는 필드가 있습니다.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Liquid로 개인화하기

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 **회신 주소** 필드에서 사용하여 커스텀 속성에 따라 회신 주소를 동적으로 템플릿화할 수 있습니다. 예를 들어, 조건 로직을 사용하여 다른 지역이나 부서로 회신을 보낼 수 있습니다:

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

이 섹션에서는 Braze에서 발송하는 아웃바운드 이메일 메시지에 추가할 수 있는 BCC 주소를 관리할 수 있습니다. 이메일 메시지에 BCC 주소를 추가하면 사용자가 받는 메시지의 동일한 복사본이 BCC 받은편지함으로 전송됩니다. 이는 규정 준수 요구 사항이나 고객지원 문제를 위해 사용자에게 보낸 메시지의 사본을 보관하는 데 유용한 도구입니다. BCC 이메일은 이메일 보고 및 분석에 포함되지 않습니다.

BCC 주소는 SendGrid 및 SparkPost에서만 사용할 수 있습니다. BCC 주소의 대안으로, 아카이브 또는 규정 준수 목적으로 사용자에게 보낸 메시지의 사본을 저장하기 위해 [메시지 아카이빙]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/)을 사용하는 것을 권장합니다.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

![이메일 설정 탭의 BCC 주소 섹션.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

주소를 추가하면 캠페인 또는 캔버스 단계에서 이메일을 작성할 때 해당 주소를 선택할 수 있습니다. 주소 옆의 **기본값으로 설정**을 선택하여 새 이메일 캠페인 또는 캔버스 구성요소를 시작할 때 이 주소가 기본적으로 선택되도록 설정합니다. 메시지 수준에서 이를 재정의하려면 메시지를 설정할 때 **BCC 없음**을 선택할 수 있습니다.

Braze에서 보내는 모든 이메일 메시지에 BCC 주소가 포함되도록 하려면 **모든 이메일 캠페인에 BCC 주소 필요** 토글을 선택할 수 있습니다. 이렇게 하면 기본값 주소를 선택해야 하며, 새 이메일 캠페인 또는 캔버스 단계에서 자동으로 선택됩니다. 기본값 주소는 또한 REST API를 통해 트리거된 모든 메시지에 자동으로 추가됩니다. 기존 API 요청에 주소를 포함하도록 변경할 필요가 없습니다.

#### 동적 BCC

동적 BCC를 사용하면 BCC 주소에서 Liquid를 사용할 수 있습니다. 이 기능은 **이메일 환경설정**에서만 사용할 수 있으며 캠페인 자체에서는 설정할 수 없습니다. 이메일 수신자당 하나의 BCC 주소만 허용됩니다.

예를 들어, 지원 팀의 이메일에 대한 BCC 주소로 {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %}을 추가할 수 있습니다.

![Liquid를 사용하는 BCC 주소가 있는 이메일 설정 탭의 BCC 주소 섹션.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## 열람 추적 픽셀

[![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

이메일 열람 추적 픽셀은 보이지 않는 1 x 1&nbsp;px 이미지이며 자동으로 이메일 HTML에 삽입됩니다. 이 픽셀은 Braze가 사용자가 이메일을 열었는지 감지하는 데 도움을 줍니다. 사용자의 이메일 클라이언트가 추적 픽셀에 요청을 할 때, 요청에는 IP 주소, 사용자 에이전트 및 타임스탬프와 같은 정보가 포함될 수 있습니다. 이메일 열람 정보는 매우 유용할 수 있으며, 해당 열람률을 이해함으로써 효과적인 마케팅 전략을 결정하는 데 도움을 줍니다.

### 추적 픽셀 배치

Braze의 기본 동작은 추적 픽셀을 이메일 하단에 추가하는 것입니다. 대부분의 사용자에게 이것은 픽셀을 배치하기에 이상적인 위치입니다. 픽셀은 이미 가능한 한 적은 시각적 변화를 일으키도록 스타일링되어 있지만, 의도하지 않은 시각적 변화는 이메일 하단에서 가장 덜 눈에 띕니다. 이것은 또한 SendGrid 및 SparkPost와 같은 이메일 제공자의 기본값이기도 합니다.

### 추적 픽셀의 위치 변경

Braze는 현재 이메일의 `<body>`의 마지막 태그에 있는 ESP의 기본 열람 추적 픽셀 위치를 `<body>`의 첫 번째 태그로 이동하는 것을 지원합니다.
  
!["열람 추적 픽셀" 섹션에는 SendGrid, SparkPost 또는 Amazon SES로 이동할 수 있는 옵션이 있습니다.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

위치를 변경하려면:

1. Braze에서 **설정** > **이메일 환경설정**으로 이동합니다.
2. 다음 옵션 중에서 선택합니다: **Move for SendGrid**, **Move for SparkPost** 또는 **Move for Amazon SES**
3. **저장**을 선택합니다.

저장한 후, Braze는 ESP에 특별 지침을 보내어 모든 HTML 이메일의 상단에 열람 추적 픽셀을 배치합니다.
  
{% alert important %} 
SSL 활성화는 추적 픽셀의 URL을 HTTP 대신 HTTPS로 감쌉니다. SSL이 잘못 구성된 경우 추적 픽셀의 효과에 영향을 미칠 수 있습니다. 
{% endalert %}

## List-unsubscribe 헤더 {#list-unsubscribe}

{% alert note %}
2024년 2월 15일부터 새로운 회사는 기본적으로 list-unsubscribe 헤더(원클릭 탈퇴 포함)가 활성화되어 있습니다.
{% endalert %}

list-unsubscribe 헤더를 사용하면 수신자가 메시지 본문이 아닌 메일함 UI 내에 표시되는 **탈퇴** 버튼을 통해 마케팅 이메일에서 쉽게 탈퇴할 수 있습니다.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

수신자가 **탈퇴**를 선택하면, 메일박스 제공자는 이메일 헤더에 정의된 대상으로 탈퇴 요청을 보냅니다.

list-unsubscribe를 활성화하는 것은 전달 가능성 모범 사례이며 일부 주요 메일박스 제공자의 요구 사항입니다. 이는 최종 사용자가 원치 않는 메시지에서 안전하게 자신을 제거하도록 장려하며, 이메일 클라이언트에서 스팸 버튼을 누르는 것보다 좋습니다. 후자는 발신자 평판과 이메일 전달 가능성에 해롭습니다.

[Gmail에서 구독 관리](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC) 시, Gmail은 메시지 본문에서 탈퇴 링크를 가져올 수도 있지만, 헤더에 list-unsubscribe가 있는 경우 이를 우선시합니다.

### 메일박스 제공자 지원

다음 표는 "mailto:" 헤더, list-unsubscribe URL 및 원클릭 탈퇴([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))에 대한 메일박스 제공자 지원을 요약한 것입니다.

| List-unsubscribe 헤더 | Mailto: 헤더 | List-unsubscribe URL | 원클릭 탈퇴 (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | 지원됨* | 지원됨 | 지원됨 |
| Gmail 모바일 | 지원되지 않음 | 지원되지 않음 | 지원되지 않음 |
| Apple Mail | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| Outlook.com | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| Yahoo! Mail | 지원됨* | 지원되지 않음 | 지원됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Yahoo와 Gmail은 결국 "mailto:" 헤더를 더 이상 지원하지 않으며 원클릭만 지원할 예정입니다._

헤더 표시 여부는 궁극적으로 메일박스 제공자가 결정합니다. Gmail에서 수신자의 원시(텍스트) 이메일에 list-unsubscribe 헤더가 포함되어 있는지 확인하려면 다음을 수행하세요:

1. 이메일에서 **원본 보기**를 선택합니다. 이메일의 원본 버전과 헤더가 포함된 새 탭이 열립니다.
2. "List-Unsubscribe"를 검색합니다.

헤더가 이메일의 원본 버전에 있지만 표시되지 않는 경우, 메일박스 제공자가 탈퇴 옵션을 표시하지 않기로 결정한 것이며, 메일박스 제공자가 헤더를 표시하지 않는 이유에 대한 추가적인 인사이트는 없습니다. list-unsubscribe 헤더의 표시 여부는 궁극적으로 평판에 기반합니다. 대부분의 경우, 메일박스 제공자와의 발신자 평판이 좋을수록 list-unsubscribe 헤더가 나타날 가능성이 높습니다.

### 워크스페이스의 이메일 탈퇴 헤더

![발송 대상으로 "구독하거나 옵트인한 사용자"를 선택합니다.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

이메일 탈퇴 헤더 기능이 켜져 있으면, 이 설정은 회사 수준이 아닌 전체 워크스페이스에 적용됩니다. 캠페인 및 캔버스 빌더의 **타겟 오디언스** 단계에서 구독하거나 옵트인한 사용자, 또는 옵트인한 사용자에게 보내도록 설정된 캠페인 및 캔버스에 추가됩니다.

"워크스페이스 기본값"을 사용할 때, Braze는 "탈퇴한 사용자를 포함한 모든 사용자에게 보내기"로 구성된 트랜잭션 캠페인에 대해 원클릭 탈퇴 헤더를 추가하지 않습니다. 이를 재정의하고 탈퇴한 사용자에게 보낼 때 원클릭 탈퇴 헤더를 추가하려면 메시지 수준 원클릭 목록 탈퇴 설정에서 **모든 이메일에서 전역적으로 탈퇴**를 선택하면 됩니다.

### 기본 list-unsubscribe 헤더

{% alert important %}
Gmail은 발신자가 2024년 6월 1일부터 모든 발신 상업적, 홍보 메시지에 대해 원클릭 탈퇴를 구현하도록 요구하고 있습니다. 자세한 내용은 [Gmail의 발신자 지침](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) 및 [Gmail의 이메일 발신자 지침 FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)을 참조하세요. Yahoo는 업데이트 요구 사항에 대한 2024년 초 일정을 발표했습니다. 자세한 내용은 [More Secure, Less Spam: 더 나은 경험을 위한 이메일 표준 시행](https://blog.postmaster.yahooinc.com/)을 참조하세요.
{% endalert %}

Braze 탈퇴 기능을 사용하여 탈퇴를 직접 처리하려면 **구독하거나 옵트인한 사용자에게 보내는 이메일에 원클릭 list-unsubscribe(mailto 및 HTTP) 이메일 헤더 포함**을 선택하고 표준 Braze URL 및 mail-to로 **Braze 기본값**을 선택합니다.

![구독하거나 옵트인한 사용자에게 보낸 이메일에 자동으로 list-unsubscribe 헤더를 포함할 수 있는 옵션.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze는 다음 버전의 list-unsubscribe 헤더를 지원합니다:

| List-unsubscribe 버전 | 설명 | 
| ----- | --- |
| 원클릭 (RFC 8058) | 수신자가 한 번의 클릭으로 이메일을 옵트아웃할 수 있는 간단한 방법을 제공합니다. 이것은 대량 발송자를 위한 Yahoo 및 Gmail의 요구 사항입니다. |
| List-unsubscribe URL 또는 HTTPS | 수신자에게 탈퇴할 수 있는 웹 페이지로 안내하는 링크를 제공합니다. |
| Mailto | 수신자가 브랜드에 보내는 탈퇴 요청 메시지의 대상으로 이메일 주소를 지정합니다. <br><br> _mailto list-unsubscribe 요청을 처리하려면, 해당 탈퇴 요청에 탈퇴하는 최종 사용자의 Braze에 저장된 이메일 주소가 포함되어야 합니다. 이는 최종 사용자가 탈퇴하는 이메일의 "발신 주소", 인코딩된 제목, 또는 최종 사용자가 수신한 이메일의 인코딩된 본문에서 제공될 수 있습니다. 매우 제한된 경우에 일부 받은편지함 제공자가 [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368) 프로토콜을 준수하지 않아 이메일 주소가 올바르게 전달되지 않을 수 있습니다. 이로 인해 Braze에서 탈퇴 요청을 처리할 수 없게 될 수 있습니다._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze가 위의 방법 중 하나를 통해 사용자의 list-unsubscribe 요청을 받으면, 해당 사용자의 글로벌 이메일 구독 상태가 탈퇴로 설정됩니다. 일치하는 항목이 없으면, Braze는 이 요청을 처리하지 않습니다.

### 원클릭 탈퇴

list-unsubscribe 헤더에 원클릭 탈퇴([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))를 사용하면 수신자가 이메일을 쉽게 옵트아웃할 수 있는 방법을 제공하는 데 중점을 둡니다.

### 메시지 수준 원클릭 목록 탈퇴

메시지 수준의 원클릭 list-unsubscribe 설정은 워크스페이스에 설정된 이메일 탈퇴 헤더 기능을 재정의합니다. 다음 용도에 대해 캠페인 또는 캔버스 단계별로 원클릭 탈퇴 동작을 적용하세요:

- 특정 구독 그룹에 대해 Braze 원클릭 탈퇴를 추가하여 하나의 워크스페이스 내에서 여러 브랜드/목록을 지원합니다
- 기본 Braze 탈퇴 또는 커스텀 URL 사이에서 토글합니다
- 커스텀 원클릭 탈퇴 URL을 추가합니다
- 이 메시지에서 원클릭 탈퇴를 생략합니다

{% alert note %}
메시지 수준 원클릭 list-unsubscribe 설정은 드래그 앤 드롭 편집기와 업데이트된 HTML 편집기를 사용할 때만 사용할 수 있습니다. 이전 HTML 편집기를 사용 중인 경우 업데이트된 HTML 편집기로 전환하여 이 기능을 사용하세요.
{% endalert %}

이메일 편집기에서 **발송 설정** > **발송 정보**로 이동합니다. 다음 옵션 중에서 선택합니다:

- **워크스페이스 기본값 사용**: **이메일 환경설정**에서 설정된 **이메일 탈퇴 헤더** 설정을 사용합니다. 이 설정에 대한 모든 변경 사항은 모든 메시지에 적용됩니다.
- **모든 이메일에서 전역으로 탈퇴**: Braze 기본 원클릭 탈퇴 헤더를 사용합니다. 탈퇴 버튼을 클릭한 사용자는 글로벌 이메일 구독 상태가 "탈퇴됨"으로 설정됩니다.
- **특정 구독 그룹에서 탈퇴**: 지정된 구독 그룹을 사용합니다. Braze는 탈퇴 버튼을 클릭한 사용자를 선택한 구독 그룹에서 탈퇴시킵니다.
    - 구독 그룹을 선택할 때 **타겟 오디언스**에 **구독 그룹** 필터를 추가하여 이 특정 그룹에 구독한 사용자만 타겟팅합니다. 원클릭 탈퇴를 위해 선택한 구독 그룹은 타겟팅하는 구독 그룹과 일치해야 합니다. 구독 그룹이 일치하지 않으면 이미 탈퇴한 구독 그룹에서 탈퇴하려는 사용자에게 발송할 위험이 있습니다.

{% alert important %}
**특정 구독 그룹에서 탈퇴** 설정은 원클릭 list-unsubscribe 헤더에만 적용됩니다. 이 옵션을 선택할 때 mailto list-unsubscribe 헤더는 영향을 받지 않습니다. 이는 이 방법으로 탈퇴하는 수신자가 특정 구독 그룹에서 탈퇴하는 것이 아니라 글로벌 탈퇴를 기록함을 의미합니다. 이 설정을 선택할 때 mailto list-unsubscribe 헤더가 사용자를 글로벌로 탈퇴시키지 않도록 하려면 [고객지원]({{site.baseurl}}/support_contact/)에 문의하세요.
{% endalert %}

- **커스텀**: 탈퇴를 직접 처리할 수 있도록 커스텀 원클릭 탈퇴 URL을 추가합니다.
- **탈퇴 제외**

{% alert important %}
원클릭 탈퇴 또는 탈퇴 메커니즘을 제외하는 것은 비밀번호 재설정, 영수증 및 확인 이메일과 같은 트랜잭션 메시징에만 해당되어야 합니다.
{% endalert %}

이 설정을 조정하면 이 이메일의 원클릭 목록 탈퇴에 대한 기본 동작이 재정의됩니다.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 요구 사항

자체 커스텀 탈퇴 기능을 사용하여 이메일을 보내는 경우, 설정한 원클릭 탈퇴 URL이 RFC 8058에 부합하도록 다음 요구 사항을 충족해야 합니다:

* URL은 탈퇴 POST 요청을 처리할 수 있어야 합니다.
* URL은 `https://`로 시작해야 합니다.
* URL은 HTTPS 리디렉션이나 본문을 반환해서는 안 됩니다. 원클릭 탈퇴 링크가 랜딩 페이지 또는 다른 유형의 웹 페이지로 이동하는 경우 RFC 8058을 준수하지 않습니다.
* POST 요청은 쿠키를 설정해서는 안 됩니다.

**커스텀 list-unsubscribe 헤더**를 선택하여 직접 구성한 원클릭 탈퇴 엔드포인트 및 선택적 "mailto:"를 추가합니다. Braze는 Yahoo 및 Gmail의 대량 발송자에게 요구되는 원클릭 탈퇴 HTTP를 지원하기 위해 커스텀 list-unsubscribe 헤더에 URL 입력이 필요합니다.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## 이메일 제목란에 접두사 추가

토글을 사용하여 테스트 및 시드 이메일 제목란에 "[TEST]" 및 "[SEED]"를 포함합니다. 이를 통해 테스트로 발송된 이메일 캠페인을 식별하는 데 도움이 됩니다.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 새 이메일에 기본적으로 CSS 인라인 적용

CSS 인라이닝은 이메일과 새 이메일에 대한 CSS 스타일을 자동으로 인라인하는 기술입니다. 일부 이메일 클라이언트의 경우, 이를 통해 이메일이 렌더링되는 방식을 개선할 수 있습니다.

이 설정을 변경해도 기존 이메일 메시지나 템플릿에는 영향을 미치지 않습니다. 메시지 또는 템플릿을 작성하는 동안 언제든지 이 기본값을 재정의할 수 있습니다. 자세한 내용은 [CSS 인라이닝]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)을 참조하세요.

## 사용자의 이메일이 변경될 때 다시 구독시키기

사용자가 이메일 주소를 변경할 때 자동으로 다시 구독시킬 수 있습니다. 예를 들어, 이전에 탈퇴한 워크스페이스 사용자가 Braze의 탈퇴 목록에 없는 이메일 주소로 변경하면 자동으로 재구독됩니다.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## 구독 페이지 및 바닥글

{% tabs local %}
{% tab Custom Footer %}

상업용 이메일의 경우 [CAN-SPAM 법](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)은 모든 상업용 이메일에 탈퇴 옵션을 포함하도록 요구합니다. 커스텀 바닥글 설정을 사용하면 이메일 옵트아웃 바닥글을 커스터마이징하면서 CAN-SPAM 규정을 준수할 수 있습니다. 규정을 준수하려면 이 워크스페이스의 캠페인으로 전송되는 모든 이메일에 커스텀 바닥글을 추가해야 합니다.

이메일 메시징을 위한 커스텀 바닥글을 만들 때 다음 요구 사항을 참고하세요:
- 탈퇴 URL 및 실제 우편 주소를 포함해야 합니다.
- 100KB 미만이어야 합니다.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

커스텀 바닥글 Liquid 템플릿에 대해 자세히 알아보려면 [커스텀 바닥글]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)에 대한 설명서를 확인하세요.

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze를 사용하면 자체 HTML로 **커스텀 탈퇴 페이지**를 설정할 수 있습니다. 이 페이지는 사용자가 이메일 하단에서 탈퇴를 선택한 후 나타납니다. 이 페이지는 750KB 미만이어야 합니다.

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

[이메일 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)에서 이메일 목록 관리에 대한 모범 사례를 자세히 알아보세요.

{% endtab %}
{% tab Custom Opt-In Page %}

자체 HTML을 사용하여 커스텀 옵트인 페이지를 만들 수 있습니다. 이메일에 이를 포함하면 사용자 라이프사이클 전반에 걸쳐 브랜드와 메시지를 일관되게 유지하고자 할 때 특히 유익합니다. 이 페이지는 750KB 미만이어야 합니다.

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

[이메일 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)에서 이메일 목록 관리에 대한 모범 사례를 자세히 알아보세요.

{% endtab %}
{% endtabs %}

{% alert tip %}
구독 페이지 또는 바닥글의 **미리보기** 섹션에서 **미리보기 링크 복사**를 선택하면 이메일 바닥글, 탈퇴 페이지 또는 옵트인 페이지가 무작위 사용자에게 어떻게 보이는지 확인할 수 있는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 링크는 7일 동안 유효하며, 이후 재생성해야 합니다.
{% endalert %}

## 자주 묻는 질문

### 원클릭 탈퇴

{% details 원클릭 탈퇴 URL(list-unsubscribe 헤더를 통한)을 환경설정 센터에 연결할 수 있나요? %}
아니요, 그것은 RFC 8058을 준수하지 않으므로 Yahoo와 Gmail의 원클릭 탈퇴 요구 사항을 충족하지 않습니다.
{% enddetails %}

{% details 환경설정 센터를 작성할 때 "이메일 본문에 탈퇴 링크가 포함되어 있지 않습니다"라는 오류 메시지가 표시되는 이유는 무엇인가요? %}
환경설정 센터는 탈퇴 링크로 간주되지 않습니다. 이메일 수신자는 CAN-SPAM 규정을 준수하기 위해 모든 상업적 이메일에서 탈퇴할 수 있는 옵션이 있어야 합니다.
{% enddetails %}

{% details 원클릭 탈퇴 설정을 활성화한 후 이전 이메일 캠페인과 캔버스를 편집해야 하나요? %}
메시지 수준의 원클릭 목록 탈퇴 설정에 대한 사용 사례가 없는 경우, **이메일 환경설정**에서 설정이 켜져 있는 한 필요한 조치는 없습니다. Braze는 모든 발신 마케팅 및 프로모션 메시지에 원클릭 탈퇴 헤더를 자동으로 추가합니다. 그러나 메시지별로 원클릭 탈퇴 동작을 구성해야 하는 경우, 해당 이메일이 포함된 이전 캠페인과 캔버스 단계를 업데이트해야 합니다.
{% enddetails %}

{% details 원본 메시지나 원시 데이터에서 list-unsubscribe 및 원클릭 탈퇴 헤더를 볼 수 있는데, Gmail이나 Yahoo에서 탈퇴 버튼이 보이지 않는 이유는 무엇인가요? %}
Gmail과 Yahoo는 궁극적으로 list-unsubscribe 또는 원클릭 탈퇴 헤더를 표시할지 여부를 결정합니다. 새로운 발신자이거나 발신자 평판이 낮은 경우, 탈퇴 버튼이 표시되지 않을 수 있습니다.
{% enddetails %}

{% details 커스텀 원클릭 탈퇴 헤더는 Liquid를 지원하나요? %}
네, Liquid 및 조건 로직이 지원되어 헤더에 동적 원클릭 탈퇴 URL을 사용할 수 있습니다.
{% enddetails %}

{% alert tip %}
조건 로직을 추가하는 경우, URL에 공백을 추가하는 출력 값을 피하세요. Braze는 이러한 공백을 제거하지 않습니다.
{% endalert %}

### 메시지 수준 원클릭 목록 탈퇴

{% details 원클릭을 위한 이메일 헤더를 수동으로 추가하고 이메일 탈퇴 헤더가 켜져 있는 경우, 예상되는 동작은 무엇인가요? %}
원클릭 list-unsubscribe를 위해 추가된 이메일 헤더는 이 캠페인의 모든 향후 발송에 적용됩니다.
{% enddetails %}

{% details 시작하려면 메시지 배리언트 간에 구독 그룹이 일치해야 하는 이유는 무엇인가요? %}
A/B 테스트가 있는 캠페인의 경우, Braze는 무작위로 사용자에게 배리언트 중 하나를 보냅니다. 같은 캠페인에 두 개의 서로 다른 구독 그룹이 설정되어 있는 경우(배리언트 A는 구독 그룹 A에 설정되고 배리언트 B는 구독 그룹 B에 설정됨), 구독 그룹 B에만 구독한 사용자가 배리언트 B를 받을 것이라고 보장할 수 없습니다. 사용자가 이미 탈퇴한 구독 그룹에서 탈퇴하는 시나리오가 발생할 수 있습니다.
{% enddetails %}

{% details 이메일 환경설정에서 이메일 탈퇴 헤더 설정이 꺼져 있지만, 캠페인의 발송 정보에서 원클릭 list-unsubscribe 설정이 "워크스페이스 기본값 사용"으로 설정되어 있습니다. 이것은 버그인가요? %}
아니요. 워크스페이스 설정이 꺼져 있고 메시지 설정이 **워크스페이스 기본값 사용**으로 설정된 경우, Braze는 **이메일 환경설정**에 구성된 내용을 따릅니다. 이는 캠페인에 대해 원클릭 탈퇴 헤더를 추가하지 않음을 의미합니다.
{% enddetails %}

{% details 구독 그룹이 아카이브되면 어떻게 되나요? 발송된 이메일의 원클릭 탈퇴가 중단되나요? %}
원클릭을 위한 **발송 정보**에서 참조된 구독 그룹이 아카이브된 경우, Braze는 여전히 원클릭에서 탈퇴를 처리합니다. 구독 그룹은 더 이상 대시보드(세그먼트 필터, 고객 프로필 및 유사한 영역)에 나타나지 않습니다.
{% enddetails %}

{% details 원클릭 탈퇴 설정을 이메일 템플릿에서 사용할 수 있나요? %}
아니요, 이메일 템플릿은 발송 도메인에 할당되지 않으므로 현재 이 기능을 추가할 계획은 없습니다. 이메일 템플릿에 이 기능이 필요하시면 [제품 피드백]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)을 제출하세요.
{% enddetails %}

{% details 이 기능은 커스텀 옵션에 추가된 원클릭 탈퇴 URL이 유효한지 확인하나요? %}
아니요, Braze 대시보드에서 링크를 확인하거나 검증하지 않습니다. 출시 전에 URL을 제대로 테스트하세요.
{% enddetails %}