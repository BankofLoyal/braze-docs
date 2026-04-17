---
nav_title: VideoSmart
article_title: VideoSmart
description: "이 참조 문서에서는 Braze와 VideoSmart 간의 파트너십을 설명합니다. VideoSmart는 브랜드가 데이터 중심의 비선형 콘텐츠를 대규모로 전달할 수 있도록 하는 개인화된 인터랙티브 비디오 기술입니다."
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/)는 데이터 중심의 비선형 콘텐츠를 대규모로 전달할 수 있는 개인화된 인터랙티브 비디오 기술을 제공합니다. 각 비디오는 고객 수준의 데이터를 사용하여 동적으로 생성되므로, 단일 비디오 경험 내에서 맞춤형 메시징과 사용자 여정을 구현할 수 있습니다.
>
> VideoSmart 통합을 사용하면 Braze 연결된 콘텐츠와 Liquid 템플릿을 활용하여 VideoSmart에서 비디오 자산을 요청함으로써 이메일 캠페인에 개인화된 비디오 콘텐츠를 삽입할 수 있습니다. 이 통합은 일반적으로 재사용 가능한 Braze 콘텐츠 블록 템플릿을 통해 구현되며, 캠페인 전반에 걸쳐 일관된 배포를 가능하게 하면서도 캠페인 선택과 개인화 로직에 유연성을 제공합니다.

_이 통합은 VideoSmart에서 개발 및 유지 관리합니다._

## 이 통합에 대하여

VideoSmart는 Braze와 통합되어 발송 시점에 개인화된 비디오 자산을 동적으로 생성하며, 이를 Braze 캠페인 및 캔버스 이메일 콘텐츠에 직접 삽입합니다.

Braze에서 관련 VideoSmart 캠페인을 선택하고 발송 시 고객 속성을 Liquid 템플릿을 통해 VideoSmart에 전달합니다. 이러한 속성은 각 수신자에게 고유하고 개인화된 비디오 경험을 렌더링하는 데 사용됩니다. 그런 다음 Braze 연결된 콘텐츠를 사용하여 VideoSmart의 API에서 실시간으로 비디오 URL 또는 자산을 요청할 수 있어 확장 가능한 개인화가 가능합니다.

이 통합은 Liquid 템플릿과 연결된 콘텐츠를 지원하는 Braze 이메일 메시지용으로 설계되었으며, 표준 Braze 고객 프로필 속성 또는 커스텀 데이터 필드와 함께 작동하도록 구성할 수 있습니다.

## 활용 사례


일반적인 활용 사례는 다음과 같습니다:

- 고객 온보딩 및 환영 여정
- 금융 교육(연금 및 보험 상품 등)
- 연간 명세서 및 규제 커뮤니케이션
- 제품 인지도 및 교차 판매 캠페인
- 고객 유지 및 재참여 캠페인
- 유기한 장바구니 리마인더: 고객이 장바구니에 제품을 추가했지만 구매하지 않은 경우, 남겨둔 항목을 강조하는 개인화된 비디오가 포함된 이메일을 발송합니다
- 구매 후 후속 조치: 구매 후 개인화된 감사 비디오를 보내고 관련 제품을 추천합니다

## 필수 조건

시작하기 전에 다음 사항을 확인하세요:

| 요구 사항                        | 설명                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Braze 연결된 콘텐츠 자격 증명 | VideoSmart에서 제공한 값으로 구성된 **basic_credentials**라는 이름의 연결된 콘텐츠 기본 인증 자격 증명 |
| **VideoSmart 콘텐츠 블록** 템플릿   | Braze 대시보드에 추가된 **VideoSmart 콘텐츠 블록** 템플릿(VideoSmart에서 제공)                                |
| Braze 이메일 메시지               | **VideoSmart 콘텐츠 블록**을 삽입할 Braze 캠페인 이메일 또는 캔버스 이메일 단계                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

다음 단계에 따라 **VideoSmart 콘텐츠 블록**을 활성화하고 이메일에서 사용하세요.

### 1단계: Braze에서 VideoSmart 콘텐츠 블록 템플릿 설정

VideoSmart 담당자에게 **VideoSmart 콘텐츠 블록** 템플릿을 요청하고 Braze 대시보드에 추가하세요.

VideoSmart에서 콘텐츠 블록에서 사용하는 연결된 콘텐츠 인증을 위한 자격 증명을 제공합니다.

### 2단계: 연결된 콘텐츠 인증 설정

Braze에서 "basic_credentials"라는 이름의 연결된 콘텐츠 기본 인증 자격 증명을 생성하세요.

- [기본 인증 사용]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#using-basic-authentication)의 지침을 따르세요.
- VideoSmart에서 제공한 사용자 이름과 비밀번호를 사용하세요.

### 3단계: 이메일에 콘텐츠 블록 추가

비디오 콘텐츠를 표시할 위치에 **VideoSmart 콘텐츠 블록**을 이메일에 삽입하세요.

대부분의 Braze 설정에서 콘텐츠 블록은 다음 패턴을 사용하여 참조됩니다("VideoSmart_Campaign"을 계정의 콘텐츠 블록 이름으로 교체하세요):

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
콘텐츠 블록 이름은 대소문자를 구분하며 Braze에서 구성한 것과 정확히 일치해야 합니다.
{% endalert %}

### 4단계: 캠페인 및 레코드 데이터 재정의(선택 사항)

콘텐츠 블록이 기본값을 지원하는 경우 변수를 설정하지 않고도 사용할 수 있습니다.

특정 VideoSmart 캠페인을 선택하거나, 커스텀 개인화 필드를 전달하거나, 두 가지 모두를 수행해야 하는 경우 콘텐츠 블록을 렌더링하기 전에 다음 Liquid 변수를 설정하세요:

- `vs_campaign_id`: VideoSmart 캠페인 식별자
- `vs_record_data`: VideoSmart 템플릿에 전달할 값이 포함된 JSON 문자열

#### 예시

이 예시에서는 이름과 성에 Braze 사용자 속성을 사용합니다:

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'John' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Braze 이메일 미리보기가 올바르게 표시되도록 `vs_record_data`에 사용되는 값에 항상 기본값을 제공하세요.
- `vs_record_data`는 단일 문자열로 인코딩된 유효한 JSON이어야 합니다(예시에서는 `strip_newlines`를 사용합니다).
{% endalert %}

### 5단계: VideoSmart 콘텐츠 블록 템플릿에서 생성된 변수 사용

콘텐츠 블록이 실행되면 이메일의 다른 곳에서 참조할 수 있는 변수가 생성됩니다.

일반적인 변수는 다음과 같습니다:

{% raw %}
| 변수                          | 설명                                           |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}`                 | 개인화된 비디오의 URL                         |
| `{{ poster_url }}`                | 비디오의 포스터 이미지 URL                 |
| `{{ output_data.VARIABLE_NAME }}` | 콘텐츠 블록에서 노출하는 추가 출력 필드 |
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용량 제한

VideoSmart의 API는 분당 10,000건의 요청으로 사용량이 제한됩니다. 이 제한을 초과하면 오류가 발생하거나 비디오 생성이 지연될 수 있습니다.

이 위험을 줄이려면 메시지 발송 속도가 VideoSmart API 용량 이하로 유지되도록 Braze 캠페인 사용량 제한을 구성하세요.

전달 속도 및 사용량 제한에 대한 Braze 가이드는 [전달 속도 및 사용량 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)을 참조하세요.

## 고려 사항

- 연결된 콘텐츠는 메시지가 렌더링될 때 실행되므로, 기본값이나 속성이 다른 경우 미리보기와 발송 시 값이 다를 수 있습니다.
- `video_url`과 같은 변수를 참조하기 전에 이메일에 콘텐츠 블록이 포함되어 있는지 확인하세요.
- `vs_record_data`에서 커스텀 필드를 사용하는 경우 VideoSmart에 예상 필드 이름을 확인하세요.

## 문제 해결

### 미리보기가 작동하지 않는 경우

Braze 미리보기가 실패하는 경우(예: 반복적인 재시도 또는 인증 오류), 다음을 확인하세요:

- 연결된 콘텐츠 자격 증명 "basic_credentials"가 존재하고 올바르게 구성되어 있는지 확인합니다.
- **VideoSmart 콘텐츠 블록** 템플릿이 Braze 계정에 있는지 확인합니다.
- 필수 변수(예: `vs_campaign_id` 또는 `vs_record_data`의 필수 필드)에 미리보기용 기본값이 설정되어 있는지 확인합니다.

### VideoSmart 콘텐츠 블록 템플릿 변수가 예상 출력을 생성하지 않는 경우

VideoSmart 콘텐츠 블록 템플릿에서 생성된 변수가 예상 출력을 생성하지 않는 경우 다음을 확인하세요:

- **VideoSmart 콘텐츠 블록** 템플릿이 Braze에서 올바르게 설정되어 있는지 확인합니다.
- 연결된 콘텐츠 인증이 적절한 자격 증명으로 올바르게 설정되어 있는지 확인합니다.
- 이메일에서 변수를 출력하여 설정되고 있는지 확인합니다. 예: `{% raw %}{{ video_url }}{% endraw %}`

커스텀 캠페인을 사용하는 경우 다음도 확인하세요:

- `vs_campaign_id`가 유효한 캠페인 식별자로 설정되어 있는지 확인합니다.
- `vs_record_data`가 유효한 JSON이며 예상 필드를 포함하고 있는지 확인합니다.