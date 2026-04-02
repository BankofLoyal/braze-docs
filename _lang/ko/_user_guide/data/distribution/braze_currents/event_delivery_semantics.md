---
nav_title: 이벤트 전달 의미론
article_title: 이벤트 전달 의미론
page_order: 3
page_type: reference
description: "이 참조 문서에서는 커런츠가 데이터 웨어하우스 스토리지 파트너에게 보내는 플랫 파일 이벤트 데이터를 관리하는 방법을 간략하게 설명하고 정의합니다."
tool: Currents

---

# 이벤트 전달 의미론

> 이 페이지에서는 커런츠가 데이터 웨어하우스 스토리지 파트너에게 보내는 플랫 파일 이벤트 데이터를 관리하는 방법을 간략하게 설명하고 정의합니다.

데이터 스토리지용 커런츠는 플랫폼에서 데이터 웨어하우스 [파트너 연결]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 중 하나에 있는 스토리지 버킷으로 데이터를 지속적으로 스트리밍하는 것입니다. 커런츠는 일정한 임계값에 따라 Avro 파일을 스토리지 버킷에 기록하여 자체 비즈니스 인텔리전스(BI) 도구 세트로 이벤트 데이터를 처리하고 분석할 수 있도록 합니다.

{% alert important %}
이 콘텐츠는 **데이터 웨어하우스 스토리지 파트너(Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage)로 전송하는 플랫 파일 이벤트 데이터에만 적용됩니다**. <br><br>다른 파트너에게 적용되는 콘텐츠는 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 목록을 참조하여 해당 페이지를 확인하세요.
{% endalert %}

## 테스트 이벤트

커런츠 통합을 설정할 때, **테스트 이벤트 전송**을 클릭하여 스토리지 버킷과의 연결을 확인하세요. 이 테스트 이벤트는 통합이 데이터를 올바르게 수신하고 처리할 수 있는지 검증합니다.

{% alert important %}
**테스트 이벤트 데이터 형식:** 테스트 이벤트는 각 필드에 대해 올바른 데이터 유형과 일치하는 입력 안내 값을 포함하지만, 현실적이거나 정확한 데이터는 포함하지 않습니다. 예를 들어, `timezone` 필드는 유효한 시간대 식별자(예: "America/Chicago") 대신 UUID와 유사한 문자열을 포함할 수 있으며, `campaign_name` 및 `ip_pool`과 같은 다른 필드도 실제 데이터 대신 입력 안내 값을 포함할 수 있습니다.<br>

이는 예상되는 동작입니다. 테스트 이벤트는 주로 연결 및 통합 설정을 테스트하기 위한 것이지, 데이터 정확성을 검증하기 위한 것이 아닙니다. 정확한 데이터가 포함된 실제 이벤트를 보려면, 테스트 커런츠 통합을 사용하여 파이프라인을 통해 실제 이벤트 데이터를 전송하세요.
{% endalert %}

## 최소 한 번 이상 전달

처리량이 많은 시스템인 커런츠는 이벤트를 "최소 한 번" 전달하므로, 중복된 이벤트가 스토리지 버킷에 기록될 수 있습니다. 이는 어떤 이유로든 이벤트가 대기줄에서 재처리될 때 발생할 수 있습니다.

사용 사례에 "정확히 한 번" 전달이 필요한 경우, 모든 이벤트와 함께 전송되는 고유 식별자 필드(`id`)를 사용하여 이벤트 중복을 제거할 수 있습니다. 파일이 스토리지 버킷에 기록되는 순간 당사의 제어를 벗어나기 때문에, 당사 측에서 중복 제거를 보장할 수 있는 방법이 없습니다.

## 타임스탬프

커런츠에서 내보내는 모든 타임스탬프는 UTC 시간대로 전송됩니다. 사용 가능한 일부 이벤트의 경우 시간대 필드도 포함되어 있어, 이벤트 발생 시점의 사용자 현지 시간대를 IANA(인터넷 할당 번호 기관) 형식으로 전달합니다.

### 지연 시간

SDK 또는 API를 통해 Braze로 전송된 이벤트에는 과거의 타임스탬프가 포함될 수 있습니다. 가장 대표적인 예는 모바일 연결이 되지 않는 경우와 같이 SDK 데이터가 대기줄에 쌓이는 경우입니다. 이 경우 이벤트 타임스탬프는 이벤트가 생성된 시점을 반영합니다. 즉, 일부 이벤트가 지연 시간이 높은 것처럼 보일 수 있습니다.

## Apache Avro 형식

Braze 커런츠 데이터 스토리지 통합은 `.avro` 형식으로 데이터를 출력합니다. 기본적으로 스키마 진화를 지원하고 다양한 데이터 제품에서 지원되는 유연한 데이터 형식이기 때문에 [Apache Avro](https://avro.apache.org/)를 선택했습니다.

- Avro는 거의 모든 주요 데이터 웨어하우스에서 지원됩니다.
- 데이터를 S3에 그대로 보관하고자 하는 경우, Avro는 CSV 및 JSON보다 압축률이 높으므로 스토리지 비용이 적게 들고 데이터 구문 분석에 필요한 CPU도 줄일 수 있습니다.
- Avro는 데이터를 쓰거나 읽을 때 스키마를 요구합니다. 스키마는 시간이 지남에 따라 진화하여 기존 기능을 중단하지 않고 필드를 추가할 수 있습니다.

커런츠는 다음 형식을 사용하여 각 이벤트 유형에 대한 파일을 생성합니다:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
스크롤 막대 때문에 코드가 보이지 않나요? [여기에서]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/) 해결 방법을 알아보세요.
{% endalert %}

예를 들어, 푸시 전송 이벤트 경로는 다음과 같을 수 있습니다:

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

`version` 경로 세그먼트는 `version=6`과 같은 단순 정수 커런츠 버전 값입니다.

|파일 이름 세그먼트 |정의|
|---|---|
| `<your-bucket-prefix>` | 이 커런츠 통합을 위해 설정된 접두사입니다. |
| `<cluster-identifier>` | Braze에서 내부용으로 사용합니다. "prod-01", "prod-02", "prod-03" 또는 "prod-04"와 같은 문자열입니다. 모든 파일은 동일한 클러스터 식별자를 갖습니다.|
| `<connection-type-identifier>` | 연결 유형의 식별자입니다. 옵션은 "S3", "AzureBlob" 또는 "GCS"입니다. |
| `<integration-id>` | 이 커런츠 통합의 고유 ID입니다. |
| `<event-type>` | 파일에 포함된 이벤트의 유형입니다. |
| `<date>` | UTC 시간대 기준으로 이벤트가 시스템에서 처리 대기줄에 오른 시간입니다. 형식은 YYYY-MM-DD-HH입니다. |
| `version=<currents_version>` | 파이프라인 경로의 커런츠 버전입니다. 이 값은 `6`과 같은 단순 정수입니다. |
| `<environment>` | Braze에서 내부용으로 사용합니다. |
| `<partition>` | Braze에서 내부용으로 사용합니다. 정수입니다. |
| `<offset>`| Braze에서 내부용으로 사용합니다. 정수입니다. 같은 시간 내에 전송된 파일마다 `<offset>` 매개변수가 다르다는 점에 유의하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
파일 명명 규칙은 변경될 수 있습니다. Braze는 &lt;your-bucket-prefix&gt; 접두사가 있는 버킷의 모든 키를 검색할 것을 권장합니다.
{% endalert %}

### Avro 쓰기 임계값

일반적인 상황에서 Braze는 5분마다 또는 15,000개의 이벤트가 쌓일 때 중 더 빠른 시점에 데이터 파일을 스토리지 버킷에 기록합니다. 부하가 많을 때는 파일당 최대 100,000개의 이벤트가 포함된 대용량 데이터 파일을 기록할 수도 있습니다.

{% alert important %}
커런츠는 빈 파일을 절대 기록하지 않습니다.
{% endalert %}

### Avro 스키마 변경 사항

Braze는 필드가 추가, 변경 또는 제거될 때 Avro 스키마를 변경할 수 있습니다. 여기서는 호환성을 깨는 변경과 호환성을 깨지 않는 변경, 두 가지 유형이 있습니다. 모든 경우에 스키마가 업데이트되었음을 나타내기 위해 커런츠 경로 버전이 올라갑니다. Azure Blob Storage, Google Cloud Storage 및 Amazon S3에 기록되는 커런츠 이벤트는 경로에 `version=<currents_version>`으로 기록됩니다. 예: `<your-bucket-prefix>/.../event_type=<event-type>/date=<date>/version=6/<environment>/...`.

#### 호환성을 깨지 않는 변경 사항

필드가 Avro 스키마에 추가되면 이를 호환성을 깨지 않는 변경으로 간주합니다. 추가된 필드는 항상 "선택 사항"인 Avro 필드(예: 기본값이 `null`)이므로, [Avro 스키마 해석 사양](http://avro.apache.org/docs/current/spec.html#schema+resolution)에 따라 이전 스키마와 "일치"하게 됩니다. 이러한 추가 사항은 필드가 ETL 프로세스에 추가될 때까지 단순히 무시되므로 기존 추출, 변환 및 로드(ETL) 프로세스에 영향을 미치지 않습니다.

{% alert important %}
새 필드가 추가될 때 흐름이 중단되지 않도록, ETL 설정에서 처리할 필드를 명시적으로 지정하는 것이 좋습니다.
{% endalert %}

모든 변경 사항에 대해 사전 경고를 제공하기 위해 노력하지만, 호환성을 깨지 않는 변경 사항은 언제든지 스키마에 포함될 수 있습니다.

#### 호환성을 깨는 변경 사항

Avro 스키마에서 필드가 제거되거나 변경되면 이를 호환성을 깨는 변경으로 간주합니다. 호환성을 깨는 변경이 발생하면 사용 중이던 필드가 더 이상 예상대로 기록되지 않을 수 있으므로 기존 ETL 프로세스를 수정해야 할 수 있습니다.

스키마에 대한 모든 호환성을 깨는 변경 사항은 변경 전에 미리 알려드립니다.