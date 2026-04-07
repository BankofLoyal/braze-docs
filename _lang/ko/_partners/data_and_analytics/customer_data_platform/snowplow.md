---
nav_title: Snowplow
article_title: Snowplow
description: "이 참조 문서에서는 데이터 인프라 플랫폼인 Snowplow와 Braze의 파트너십에 대해 설명하며, Snowplow의 이벤트 포워딩을 사용하여 Snowplow 이벤트를 실시간으로 Braze에 전달할 수 있습니다."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplow.io)는 풍부한 고품질, 저지연 데이터 수집을 위한 확장 가능한 오픈소스 플랫폼입니다. Snowplow는 기업 비즈니스를 위한 고품질의 완전한 행동 데이터를 수집하도록 설계되었습니다.

_이 통합은 Snowplow에서 유지 관리합니다._

## 통합 정보

Braze와 Snowplow 통합을 통해 Snowplow의 이벤트 포워딩 솔루션을 사용하여 Snowplow 이벤트를 실시간으로 Braze에 전달할 수 있습니다. 이 통합을 통해 유연성과 제어를 유지하면서 이벤트를 Braze로 전송할 수 있습니다. 구체적으로 다음을 수행할 수 있습니다:
- Braze로 전송하기 전에 이벤트를 필터링하고 변환합니다.
- Snowplow 이벤트 데이터를 Braze 사용자 속성, 커스텀 이벤트 및 구매에 매핑합니다.
- 전달을 선택할 때까지 모든 데이터를 프라이빗 클라우드에 보관합니다.
- 기존 Snowplow 클라우드 계정 내에서 솔루션을 직접 배포합니다. 

Snowplow의 [이벤트 포워딩](https://docs.snowplow.io/docs/destinations/forwarding-events/)은 Snowplow 고객에게 제공되는 유료 애드온 기능입니다. 이 애드온 없이 이벤트를 Braze에 전달하려면 Snowplow의 [Google Tag Manager 서버 측](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) 통합을 사용하세요.

Snowplow의 풍부한 행동 데이터를 활용하여 Braze에서 강력한 고객 중심 인터랙션을 유도하고 개인화된 메시지를 실시간으로 전달하세요.

## 필수 조건

| 요구 사항             | 설명                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snowplow 파이프라인       | Snowplow 파이프라인이 가동 및 실행 중이어야 합니다.                                                                                                                                                                                                                                          |
| Snowplow 콘솔 액세스 | 이벤트 전달자를 구성하려면 Snowplow 콘솔에 액세스할 수 있어야 합니다.                                                                                                                                                                                                                                |
| Braze REST API 키      | 다음 권한이 있는 Braze REST API 키: `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename`, `users.alias.update`. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트     | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 활용 사례

### 개인화된 실행 기반 전달
Snowplow가 기본적으로 수집하는 다양한 풍부한 이벤트를 사용하거나, 커스텀 이벤트를 정의하여 비즈니스에 적합한 더욱 세분화된 고객 여정을 설계하세요. Snowplow의 풍부한 행동 데이터를 활용하여 고객 퍼널을 설계하고 마케팅 및 제품 팀의 가치를 극대화하여 Braze를 통해 전환율과 제품 사용량을 높이세요.

### 동적 세분화
Snowplow의 고품질 행동 데이터를 기반으로 Braze에서 동적 오디언스를 생성하세요. 사용자가 제품, 앱 또는 웹사이트에서 행동을 취하면 Snowplow가 수집하는 실시간 행동 데이터를 활용하여 Braze의 관련 세그먼트에 사용자를 자동으로 추가하거나 제거할 수 있습니다.

## 통합

### 1단계: Snowplow 콘솔에서 대상 구성하기

이벤트 전달자를 만들려면 다음과 같이 하세요:

1. Snowplow 콘솔에서 **Destinations**로 이동하여 **Create new destination**을 선택합니다.
2. 연결을 구성할 때 연결 유형으로 **Braze**를 선택합니다.
3. Braze API 키와 REST API 엔드포인트를 입력합니다.
4. 연결을 저장합니다.

### 2단계: 이벤트 전달자 구성

전달자를 구성할 때 전달할 Snowplow 이벤트를 선택하고 이를 Braze 오브젝트 유형에 매핑할 수 있습니다:

1. **[사용자 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object)**: 고객 프로필 데이터 및 커스텀 사용자 속성을 업데이트합니다.
2. **[커스텀 이벤트]({{site.baseurl}}/api/objects_filters/event_object)**: 사용자 행동 및 동작을 전송합니다.
3. **[구매]({{site.baseurl}}/api/objects_filters/purchase_object)**: 제품 세부 정보가 포함된 트랜잭션 데이터를 전송합니다.

각 오브젝트 유형에 대해 필드 매핑을 구성하여 Snowplow 이벤트 데이터가 Braze 필드에 매핑되는 방식을 지정할 수 있습니다. 자세한 설정 지침 및 필드 매핑 구성은 Snowplow의 [전달자 만들기 설명서](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/)를 참조하세요.

### 3단계: 통합 검증하기

Braze 계정에서 다음 페이지를 확인하여 이벤트가 정상적으로 도달하고 있는지 확인하세요:

1. **쿼리 빌더**: Braze에서 **분석** > **쿼리 빌더**로 이동합니다. 다음 테이블에 쿼리를 작성하여 Snowplow에서 전달된 데이터를 미리 볼 수 있습니다: `USER_BEHAVIORS_CUSTOMEVENT_SHARED` 및 `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **API 사용 대시보드**: Braze에서 **설정** > **API 및 식별자**로 이동하여 시간별 API 사용량 차트를 확인합니다. Snowplow가 사용하는 API 키로 필터링하여 성공과 실패를 모두 확인할 수 있습니다.

## 커스텀 등록정보 보내기

표준 필드 외에 커스텀 등록정보를 보낼 수 있습니다. 구조는 사용 중인 Braze 오브젝트 유형에 따라 다릅니다:

- **사용자 속성**: 최상위 필드로 추가합니다(예: `subscription_tier`, `loyalty_points`).
- **이벤트 등록정보**: `properties` 오브젝트 아래에 중첩합니다(예: `properties.plan_type`, `properties.feature_flag`).
- **구매 속성정보**: `properties` 오브젝트 아래에 중첩합니다(예: `properties.color`, `properties.size`).

공백이 포함된 등록정보 이름의 경우 대괄호 표기법을 사용합니다(예: `["account type"]` 또는 `properties["campaign source"]`).

지원되는 데이터 유형, 등록정보 명명 요구 사항 및 페이로드 크기 제한에 대한 자세한 내용은 [이벤트 오브젝트 설명서]({{site.baseurl}}/api/objects_filters/event_object)를 참조하세요.

## 제한 사항

**사용량 제한:** Braze는 사용자 추적 API에 대해 3초당 3,000회의 API 호출 사용량 제한을 적용합니다. Snowplow는 이벤트 전달자에 대한 일괄 처리를 지원하지 않으므로 이 API 사용량 제한은 이벤트 속도 제한으로도 작동합니다. 입력 처리량이 3초당 3,000개의 이벤트를 초과하는 경우 지연 시간이 늘어날 수 있습니다.