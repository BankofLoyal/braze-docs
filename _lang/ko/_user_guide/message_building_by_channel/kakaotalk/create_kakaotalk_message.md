---
nav_title: KakaoTalk 메시지 만들기
article_title: "KakaoTalk 메시지 만들기"
description: "이 참조 문서에서는 KakaoTalk 메시지를 만드는 방법을 설명합니다."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# KakaoTalk 메시지 만들기

> [KakaoTalk 메시징 채널]({{site.baseurl}}/kakaotalk/)을 사용하여 KakaoTalk 플랫폼을 통해 사용자에게 직접 도달하세요. Liquid 및 기타 동적 콘텐츠를 사용하여 개인화된 사용자 경험을 만들고, 브랜드와 함께 풍부한 사용자 경험을 촉진하고 향상시키는 환경을 구축하세요.<br><br>KakaoTalk 메시징 채널을 설정하려면 [KakaoTalk 설정]({{site.baseurl}}/kakaotalk_setup/)을 참조하세요.

## 1단계: 메시지를 작성할 위치 선택

KakaoTalk은 캠페인과 캔버스 모두에서 지원됩니다. 캠페인은 단일 메시징 캠페인에 가장 적합하며, 캔버스는 다단계, 다채널 사용자 여정을 오케스트레이션할 수 있습니다.

{% tabs local %}
{% tab Campaign %}

1. **메시징** > **캠페인**으로 이동하여 **캠페인 생성**을 선택합니다.
2. 단일 채널 캠페인의 경우 **KakaoTalk**을, 다중 채널 캠페인의 경우 **멀티채널 캠페인**을 선택합니다.

![메시징 채널을 선택하는 옵션이 있는 패널.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. 캠페인에 추가 배리언트를 추가하여 다양한 메시지 유형과 레이아웃을 선택할 수 있습니다. 자세한 내용은 [다변량 및 A/B 테스트](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.

{% endtab %}
{% tab Canvas %}

1. [캔버스를 생성](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)합니다.
2. 캔버스 빌더에서 메시지 단계를 추가하고 **KakaoTalk**을 선택합니다.

![캔버스 메시징 채널 선택.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## 2단계: KakaoTalk 메시지 작성

1. **KakaoTalk 채널** 드롭다운을 선택하면 기술 파트너 페이지를 통해 설정한 KakaoTalk 채널 목록이 표시됩니다. 메시지를 보내는 데 사용할 KakaoTalk 채널을 선택합니다.
2. 보낼 메시지 유형을 선택합니다:
- 텍스트
- 이미지
- 리스트 아이템
    - 좁은 형태
    - 넓은 형태

![세 가지 메시지 유형을 선택할 수 있는 KakaoTalk 배리언트 섹션.]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

{% tabs local %}
{% tab Text %}

KakaoTalk 텍스트 메시지는 가장 간단한 커뮤니케이션 형태인 표준 텍스트 메시지입니다.

### 사양

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 이모지 및 Liquid 개인화를 포함한 텍스트 콘텐츠 |
| 텍스트 용량 | 최대 1,000자 |
| 버튼 | 최대 5개의 선택 사항 버튼. 현재 클릭 시 URL을 여는 용도로만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![작성기에서의 KakaoTalk 텍스트 메시지.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Image %}

이미지는 시각적 요소와 보조 텍스트를 결합한 메시지입니다. Braze는 KakaoTalk 서버로의 이미지 업로드를 자동으로 처리합니다.

### 일반 사양

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 하나의 이미지와 보조 텍스트 |
| 허용 파일 형식 | JPEG 또는 PNG |
| 권장 너비 | 500px |
| 파일 크기 | 최대 500kb |
| 종횡비 | 2:1(넓은 형태)에서 3:4(세로 형태) 사이여야 합니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

좁은 형태와 넓은 형태의 이미지 메시지는 각각 다른 글자 수 및 버튼 고려 사항이 있습니다.

{% subtabs %}
{% subtab Narrow image %}

#### 좁은 이미지

좁은 이미지 메시지는 약간 더 길고 좁은 이미지와 더 많은 텍스트 및 버튼 옵션을 제공합니다.

##### 사양

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 하나의 이미지와 보조 텍스트 |
| 텍스트 용량 | 최대 500자 |
| 버튼 | 최대 5개의 선택 사항 버튼 |
| 이미지 소스 | Braze 미디어 라이브러리 또는 직접 URL을 사용하여 이미지를 추가할 수 있습니다 |
| 커스터마이징 | 이미지의 클릭 시 동작을 지정할 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![KakaoTalk 좁은 형태 메시지.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Wide image %}

#### 넓은 이미지

넓은 이미지 메시지는 시각적 임팩트가 큰 커뮤니케이션에 적합한 눈에 띄는 넓은 이미지와 최소한의 보조 텍스트를 제공합니다.

##### 사양

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 하나의 이미지와 보조 텍스트 |
| 텍스트 용량 | 최대 76자 |
| 버튼 | 최대 2개의 선택 사항 버튼 |
| 이미지 소스 | Braze 미디어 라이브러리 또는 직접 URL을 사용하여 이미지를 추가할 수 있습니다 |
| 커스터마이징 | 이미지의 클릭 시 동작을 지정할 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![KakaoTalk 넓은 형태 메시지.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### 이미지 추가

Braze 미디어 라이브러리를 통해 또는 JPEG 또는 PNG 파일을 호스팅하는 URL을 붙여넣어 이미지를 추가할 수 있습니다. 이미지의 클릭 시 동작을 지정하여 이미지를 클릭한 사용자를 특정 URL로 리디렉션할 수도 있습니다.

Braze는 KakaoTalk의 모든 이미지 업로드 요구 사항을 자동으로 처리하므로, 메시지를 보내기 전에 KakaoTalk 제공업체에 이미지를 업로드할 **필요가 없습니다**. 이미지를 업로드하고 Braze에서 직접 메시지를 보내기만 하면 됩니다!

![좁은 이미지를 추가하기 위한 아이콘이 선택된 섹션.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab List item %}


KakaoTalk 아이템 리스트 메시지는 콘텐츠 항목 목록을 명확한 세로 형식으로 표시하도록 설계되었습니다.

리스트 아이템 메시지는 헤더, 아이템 리스트 섹션, 선택 사항 버튼 영역으로 구성됩니다.

#### 사양

| 영역 | 사양 |
| --- | --- |
| 아이템 수 | 최소 2개 또는 3개의 아이템 필요 |
| 버튼 | 최대 5개의 선택 사항 버튼 |
| 헤더 | 최대 250자 |
| 아이템 제목 | 최대 25자 |
| 웹사이트 URL(아이템당) | 최대 250자 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![KakaoTalk 리스트 아이템 메시지.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## 3단계: 클릭 추적 설정

KakaoTalk 클릭 추적이 켜져 있으면 Braze가 자동으로 URL을 단축하고, 추적 메커니즘을 추가하며, 실시간으로 클릭을 기록합니다. 이 데이터를 통해 클릭 동작을 기반으로 사용자를 세분화하고 특정 클릭에 대한 응답으로 메시지를 트리거하는 등 더 타겟팅된 세분화 및 리타겟팅 전략을 만들 수 있습니다.

클릭 추적은 텍스트, 이미지, 리스트 아이템 메시지에서 지원됩니다. 버튼 내 링크와 이미지 클릭 시 동작을 지원합니다. Liquid 및 커스텀 도메인을 사용하여 URL을 개인화할 수도 있습니다.

클릭 추적을 활성화하려면 작성기의 **링크 옵션** 섹션에서 **클릭 추적**을 체크합니다. URL은 기본 Braze 도메인(`https://brz.ai`) 또는 구독 그룹에 지정된 커스텀 도메인을 사용하여 단축되고 사용자별로 개인화됩니다.

클릭 추적, 커스텀 도메인, URL 내 Liquid 개인화, 보고서 및 리타겟팅에 대한 자세한 내용은 [KakaoTalk 클릭 추적]({{site.baseurl}}/kakaotalk_click_tracking/)을 참조하세요.

### 사용자 리타겟팅

다음 세분화 필터 및 트리거를 사용하여 KakaoTalk 메시지에서 URL을 클릭한 사용자를 리타겟할 수 있습니다:

- 실행 기반 트리거
    - 캠페인과 상호작용
    - 단계와 상호작용

- 세분화 필터
    - 캠페인 클릭/열기
    - 태그가 있는 캠페인 또는 캔버스 클릭/열기
    - 단계 클릭/열기

## 4단계: KakaoTalk 메시지 미리보기 및 테스트

KakaoTalk 메시지를 작성하면 메시지 미리보기가 자동으로 업데이트됩니다. 테스트할 준비가 되면 **테스트** 탭으로 이동하여 콘텐츠 테스트 그룹이나 개별 사용자에게 테스트 메시지를 보내거나, Braze에서 직접 기존 사용자 또는 커스텀 사용자로 메시지를 미리 볼 수 있습니다.

테스트 사용자를 선택한 후 **테스트 보내기**를 선택합니다. 테스트 발송 결과를 알려주는 알림이 표시됩니다. CJ OliveNetworks의 경우 "C100" 응답을 받게 됩니다. 다른 오류가 표시되면 [CJ KakaoTalk 사용자 설명서](https://developers.kakao.com/docs/latest/en/index)를 참조하세요.

![KakaoTalk 메시지의 미리보기 창.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
기존 사용자에게 테스트 메시지를 미리 보고 보내려면 "PII 보기" 권한이 필요합니다. 해당 권한 없이도 커스텀 사용자에게 테스트 메시지를 미리 보고 보낼 수 있습니다.
{% endalert %}

발송 결과를 검토하거나 문제를 해결하려면 **설정** > **메시지 활동 로그**로 이동합니다. 자세한 내용은 [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)를 참조하세요.

## 5단계: 캠페인 또는 캔버스의 나머지 부분 구축

KakaoTalk 메시지를 작성하기 위해 도구를 가장 잘 활용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

### 전달 스케줄 또는 트리거 선택

KakaoTalk 메시지는 스케줄된 시간, 동작 또는 API 트리거를 기반으로 전달할 수 있습니다. 스케줄 및 트리거 옵션에 대한 자세한 내용은 [캠페인 스케줄]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) 또는 [진입 스케줄 유형]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types)(캔버스의 경우)을 참조하세요.

사용자가 캠페인을 다시 받을 수 있도록 허용하거나 최대 게재빈도 설정 규칙을 켜는 등 전달 제어를 지정할 수 있습니다. 실행 기반 전달의 경우 캠페인의 기간과 방해금지 시간도 설정할 수 있습니다.

### 타겟 사용자 선택

세그먼트 또는 필터를 선택하여 오디언스를 좁혀 사용자를 타겟팅합니다. 현재 KakaoTalk은 채널의 친구에게만 메시지를 보낼 수 있습니다. 채널 친구를 나타내는 커스텀 속성을 설정하여 사용자를 적절히 세분화하고 메시지를 받을 수 없는 사용자에게 KakaoTalk 메시지를 보내는 것을 방지하는 것을 권장합니다.

### 전환 이벤트 선택

Braze를 사용하면 캠페인을 받은 후 사용자가 특정 행동(전환 이벤트)을 수행하는 빈도를 추적할 수 있습니다. 사용자가 지정된 행동을 취하면 전환으로 집계되는 최대 30일의 기간을 허용하는 옵션이 있습니다.

전환 이벤트는 캠페인의 성공을 측정하는 데 도움이 됩니다. 예를 들어, 사용자가 앱을 사용하도록 유도하려는 경우 전환 이벤트를 **세션 시작**으로 설정합니다.

특정 사용 사례에 따라 커스텀 전환 이벤트를 설정할 수도 있습니다. 창의적으로 생각하여 캠페인의 성공을 어떻게 측정할지 고민해 보세요.

## 6단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 부분을 완성한 후 세부 정보를 검토하고 테스트한 다음 발송하세요!