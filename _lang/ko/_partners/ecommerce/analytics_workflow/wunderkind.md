---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "이 참조 문서에서는 Wunderkind Signals와 Braze의 통합에 대해 다루며, 캔버스 여정을 트리거하는 행동 신호, Canvas Entry API를 사용한 설정, API 트리거 전달의 캔버스 컨텍스트 페이로드, 보고서 등을 포함합니다."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co)는 독자적인 Identity 기술을 사용하여 익명 웹사이트 방문자를 인식하고 실행 가능한 이메일 주소로 확인하는 이커머스 성과 플랫폼입니다. Wunderkind는 평균적으로 웹사이트 트래픽의 3~5%에 불과한 식별률을 40~60%까지 확장하여, 브랜드가 기존 이메일 서비스 공급자를 통해 개인화된 1:1 메시지를 대규모로 트리거할 수 있도록 합니다.

*이 통합은 Wunderkind에서 유지 관리합니다. 고객지원이 필요한 경우 [support.wunderkind.co](https://support.wunderkind.co)를 방문하세요.*

## 통합 소개

Wunderkind Signals 통합을 사용하면 장바구니 유기, 제품 유기, 가격 하락 등 높은 구매 의도를 나타내는 행동 신호가 Braze에서 실시간 캔버스 여정을 트리거할 수 있습니다. Wunderkind는 웹사이트의 익명 사용자를 식별하고, 해당 사용자의 신원을 전달 가능한 이메일 주소로 확인한 후, Canvas Entry API를 통해 구조화된 신호 페이로드를 Braze에 전달하여 사전 구성된 이메일 플로우를 자동으로 시작합니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Wunderkind 계정 | Signals가 활성화된 Wunderkind 계정이 필요합니다. 자격 여부를 확인하려면 Wunderkind 담당자에게 문의하세요. |
| Braze 계정 | 캔버스 접근 권한이 있는 Braze 계정이 필요합니다. Wunderkind 팀에 계정 내 시트를 부여해야 합니다. 자세한 내용은 [Braze 계정에 Wunderkind 접근 권한 부여](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account)를 참조하세요. |
| Braze REST API 키 | 설정 중에 특정 권한이 있는 전용 API 키를 생성합니다([1단계](#step-1-create-a-braze-api-key-for-wunderkind) 참조). |
| 사용자 식별 | Wunderkind는 일반적으로 `user_alias`와 `alias_label: "wknd_email_id"`를 사용하여 소비자를 Braze에서 확인합니다(이메일을 `alias_name`으로 사용하는 경우가 많습니다). 각 [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 수신자는 `external_user_id`, `user_alias`, `braze_id`, `email` 중 정확히 하나를 포함해야 합니다([수신자 오브젝트]({{site.baseurl}}/api/objects_filters/recipient_object/)). `email`을 사용하는 경우 [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)을 포함하세요. `user_alias`를 사용하는 경우 트리거 전에 프로필이 이미 Braze에 존재해야 합니다. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)를 사용하여 먼저 사용자와 별칭을 생성하거나 업데이트하세요. 자세한 내용은 [제한 사항](#limitations)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 작동 방식

Wunderkind가 높은 구매 의도를 가진 익명 사용자를 식별하고 신원을 확인하면, `/canvas/trigger/send` 엔드포인트를 사용하여 Braze에 신호 페이로드를 전송하고, 해당 사용자에 대한 관련 캔버스 여정을 실시간으로 트리거합니다.

전체 기술 개요는 [Wunderkind 개발자 포털](https://developer.wunderkind.co/docs/integration-overview)을 참조하세요.

## 통합

### 1단계: Wunderkind용 Braze API 키 생성

Braze 대시보드에서:

1. **설정** > **API 키**로 이동하여 **새 API 키 생성**을 클릭합니다.
2. 키에 설명이 포함된 이름을 지정합니다(예: `Wunderkind Signals`).
3. [Braze 계정에 Wunderkind 접근 권한 부여](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account)에 나열된 권한을 부여합니다.
4. API 키를 복사하여 다음 섹션에서 Wunderkind 플랫폼에 입력합니다.

{% alert note %}
Wunderkind Signals의 경우, Braze [REST API]({{site.baseurl}}/api/basics/) 요청은 OAuth 토큰이 아닌 REST API 키로 인증됩니다. 대시보드에서 전용 API 키를 생성하고 해당 키를 Wunderkind에 제공하세요.
{% endalert %}

### 2단계: Wunderkind 플랫폼에 Braze 연결

1. Wunderkind 플랫폼에 로그인하고 **Integrations Hub**로 이동합니다.
2. **Braze** 타일을 선택한 다음 **Connect**를 선택합니다.
3. Braze REST API 키를 입력하고 클러스터를 선택합니다.
4. **Save**를 선택합니다.

### 3단계: 새 Braze 자산 검토

활성화 시 Wunderkind는 Wunderkind 담당자와 합의한 전략에 따라 Braze 워크스페이스에 새로운 구현 자산을 프로비저닝합니다:

| 자산 유형 | Wunderkind 생성 방법 |
| ---------- | -------------------------- |
| Content Blocks | 자동 |
| API 트리거 캔버스 | 매니지드 서비스 |
| 태그, 커스텀 속성, 링크 템플릿 | 매니지드 서비스 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 4단계: 캔버스 설정 완료

각 Signals 캔버스에 대해 Braze의 드래그 앤 드롭 에디터 또는 HTML을 사용하여 이메일 템플릿을 구축합니다.

- Wunderkind는 전송 시 `/canvas/trigger/send`에서 각 수신자의 `context` 오브젝트에 제품 및 세션 데이터를 채웁니다.
- 템플릿에서 해당 페이로드와 함께 Liquid를 사용하는 방법에 대한 자세한 지침은 Wunderkind 도움말 센터의 [캔버스 설정 완료](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup)를 참조하세요.

### 5단계: 캔버스 자격 검토

각 Signals 캔버스에서 **타겟 오디언스** 설정으로 이동하여 Wunderkind의 기본 진입 오디언스 및 종료 기준을 검토합니다.

- 사용자에게 너무 자주 메시지를 보내지 않도록 하려면 [사용자 중심 사용량 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)을 참조하세요.
- 사용자가 구매 후에도 계속 캔버스 메시지를 받지 않도록 설정을 조정합니다. 예를 들어, **구매 완료** 예외를 추가합니다.
- 특정 Signals 캔버스는 사용자가 가장 높은 의도의 메시지를 받을 수 있도록 커스텀 속성 필터가 사전 구성되어 있습니다.
- 캔버스 자격 및 우선순위에 대한 자세한 내용은 Wunderkind 도움말 센터의 [캔버스 자격 검토](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility)를 참조하세요.

### 6단계: 테스트 및 시작

Wunderkind는 라이브 전에 엔드투엔드 QA를 수행합니다:

- 신호가 API 오류 없이 올바른 캔버스 ID로 전달되는지 확인합니다.
- `context` 필드(제품명, 이미지, URL)가 렌더링된 이메일 템플릿에 올바르게 채워지는지 확인합니다.
- 모의 Wunderkind 제품으로 템플릿을 미리보기하는 방법은 Wunderkind 도움말 센터의 [Braze용 Signals 테스트 및 시작](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze)을 참조하세요.

QA가 통과되면 Wunderkind 구현 매니저가 팀과 함께 프로덕션 출시를 조율합니다.

## 캔버스 컨텍스트 페이로드

Wunderkind는 6가지 신호 유형을 지원합니다. 각 유형은 `/canvas/trigger/send`에서 해당 수신자의 [`context`]({{site.baseurl}}/api/objects_filters/context_object/) 오브젝트 내에 고유한 키와 값 세트를 전달합니다([API 트리거 전달을 사용하여 캔버스 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 참조). `WkPurpose` 필드는 해당 페이로드 내에서 신호 유형을 식별합니다.

### 공통 필드(모든 캔버스 유형) {#canvas-types-table}

| 등록정보 | 유형 | 설명 |
| -------- | ---- | ----------- |
| `Origin` | String | 항상 `"wunderkind"` |
| `DataOnly` | String | 항상 `"Y"` — Wunderkind가 데이터 레이어로만 작동하며, Braze가 전송을 실행함을 나타냅니다 |
| `UserType` | String | `"prospect"` 또는 `"customer"` |
| `WkChannel` | String | 이 통합에서는 항상 `"email"` |
| `WkPurpose` | String | 신호 유형 식별자(아래 캔버스별 값 참조) |
| `WKCouponCode` | String | 쿠폰 코드(해당하는 경우, 사용하지 않으면 빈 문자열) |
| `WKCouponPurpose` | String | 쿠폰 제안 설명(사용하지 않으면 빈 문자열) |
| `Items` | Array | 제품 오브젝트 배열(아래 제품 필드 참조) |
| `WkOpen` | String | 보고서 목적으로 사용 가능한 추적 픽셀 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 제품 항목 필드

| 등록정보 | 유형 | 설명 |
| -------- | ---- | ----------- |
| `WkCopy` | String | 제품명 |
| `WkId` | String | 제품 ID |
| `WkImageUrl` | String | 제품 이미지 URL |
| `WkUrl` | String | 제품 상세 페이지 URL |
| `WkPrice` | String | 원래 가격(가격 하락 캔버스에만 해당) |
| `WKSalePrice` | String | 할인 가격(가격 하락 캔버스에만 해당) |
| `WkQuantity` | String | 남은 수량(재고 부족 캔버스에만 해당) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 캔버스별 필드 및 `WkPurpose` 값

| 캔버스 유형 | `WkPurpose` 값 | 추가 필드 |
| ----------- | ----------------- | ------------------- |
| 장바구니 유기 | `"cart abandonment"` | `WkCartReplenUrl` — 장바구니 복원 URL |
| 제품 유기 | `"product abandonment"` | — |
| 카테고리 요약 | `"category recap"` | `WkCategoryUrl` — 탐색한 카테고리 URL |
| 재입고 | `"back in stock"` | — |
| 가격 하락 | `"price drop"` | 각 항목의 `WkPrice`, `WKSalePrice` |
| 재고 부족 | `"low stock"` | 각 항목의 `WkQuantity` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 예시 페이로드

`recipients`의 각 오브젝트는 `external_user_id`, `user_alias`, `braze_id`, `email` 중 정확히 하나를 포함해야 합니다. 자세한 내용은 [수신자 오브젝트]({{site.baseurl}}/api/objects_filters/recipient_object/)를 참조하세요.

{% alert note %}
각 예시는 **하나의** Braze 수신자 식별자를 사용합니다. 처음 6개는 `user_alias`만 사용하고, 마지막 하나는 [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)과 함께 `email`만 사용합니다. 예시 JSON에서는 검토 도구가 해당 값(`"email"`)을 Braze의 수신자 `email` 필드와 혼동하지 않도록 `context` 내의 `WkChannel` 키를 생략합니다. 프로덕션에서는 [공통 필드(모든 캔버스 유형) 테이블](#canvas-types-table)에 문서화된 대로 `context`에 `"WkChannel": "email"`을 포함하세요.
{% endalert %}

다음 예시는 Wunderkind가 신원을 확인하는 방식에 맞춰 `wknd_email_id`와 함께 `user_alias`를 사용합니다.

{% details 장바구니 유기 예시 페이로드 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 제품 유기 예시 페이로드 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 카테고리 요약 예시 페이로드 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 재입고 예시 페이로드 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 가격 하락 예시 페이로드 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 재고 부족 예시 페이로드 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 이메일 식별자 예시(대안) %}
`user_alias` 대신 Braze의 `email` 필드로 캔버스를 트리거하는 경우, 수신자에는 `email`과 `prioritization`만 포함해야 합니다([API 트리거 전달을 사용하여 캔버스 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 참조). `context` 오브젝트는 다른 예시와 동일합니다.

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Liquid 사용 예시

Wunderkind가 `/canvas/trigger/send`를 호출하면, 각 수신자의 `context` 오브젝트에 전달한 키와 값이 캔버스 진입 데이터가 됩니다. 메시지 단계에서는 `context` Liquid 네임스페이스로 참조합니다. 예를 들어 {% raw %}`{{context.${WkPurpose}}}`{% endraw %}와 같이 사용하며, 이는 [캔버스 컨텍스트 오브젝트]({{site.baseurl}}/api/objects_filters/context_object/) 및 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)에 설명되어 있습니다. 올바른 Liquid 구문을 사용하는 것 외에 추가 구성은 필요하지 않습니다.

Braze 출력 태그를 `for` 태그 조건 내에 중첩하지 마세요. [Liquid 사용하기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#use-a-filter-result-in-a-for-loop)에 설명된 대로 먼저 `context`의 `Items` 배열을 변수에 할당한 다음 루프를 실행하세요. `assign` 줄은 Braze의 캔버스 진입 형식 {% raw %}`{{context.${Items}}}`{% endraw %}를 사용합니다([지원되는 개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#summary-of-supported-tags) 참조).

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## 보고서

Wunderkind는 **Braze 커런츠**를 사용하여 Braze에서 성과 데이터를 수집하며, 커런츠는 원시 이벤트를 Google Cloud Storage로 스트리밍합니다. 그런 다음 Wunderkind는 이러한 이벤트를 원래 신호와 대조하여 정규화하고 집계하여 1:1 기여도 보고서를 제공합니다.

다음 측정기준은 곧 Wunderkind 보고서 대시보드에서 사용할 수 있습니다:

| 측정기준 | 소스 |
| ------ | ------ |
| 전달된 발송 수 | Braze 커런츠 |
| 이메일 열기 | Braze 커런츠 |
| 클릭 수 | Braze 커런츠 |
| 전환 | Braze 커런츠(설정 시 정의된 이벤트) |
| 가입 취소 | Braze 커런츠 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 제한 사항

- **수신 거부/옵트아웃 동기화 없음.** 수신 거부는 Braze에서 기본적으로 관리해야 합니다. 참고: Braze Signals로 마이그레이션하는 기존 Wunderkind 고객의 경우, Wunderkind가 팀과 협력하여 현재 설정을 유지합니다.
- **이메일 채널만 지원.** SMS는 현재 이 통합을 통해 지원되지 않습니다.
- **캔버스 트리거 전에 고객 프로필이 존재해야 합니다.** `user_alias` 수신자를 사용하는 [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)는 해당 별칭이 이미 있는 **기존** Braze 프로필만 확인합니다. 별칭에 `send_to_existing_only`를 사용할 수 없으며, 캔버스 트리거는 별칭만으로 새 프로필을 생성하지 않습니다. 먼저 사용자를 생성하거나 업데이트하고 `wknd_email_id` 별칭을 설정해야 합니다(예: [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 사용). Wunderkind는 Braze가 처리를 완료할 수 있도록 해당 업서트 후 잠시 대기한 다음 트리거를 실행할 수 있습니다.
- **이메일을 식별자로 사용하는 경우.** 캔버스 트리거가 `user_alias` 대신 `email`로 수신자를 식별하는 경우, Braze에서 요구하는 대로 해당 수신자 오브젝트에 [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)을 포함하세요.


## 추가 리소스

- [Wunderkind 도움말 센터 — Braze용 Signals 개요](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Wunderkind 개발자 포털 — 통합 개요](https://developer.wunderkind.co/docs/integration-overview)
- [API 트리거 전달을 사용하여 캔버스 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [캔버스 컨텍스트 오브젝트]({{site.baseurl}}/api/objects_filters/context_object/)
- [Braze 커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)