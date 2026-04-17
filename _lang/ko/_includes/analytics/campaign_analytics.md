## 분석 보기

캠페인을 시작한 후, 해당 캠페인의 세부 정보 페이지로 돌아가 주요 측정기준을 확인할 수 있습니다. **캠페인** 페이지로 이동하여 캠페인을 선택하면 세부 정보 페이지가 열립니다.{% if include.channel != "banner" %} {% if include.channel == "Content Card" %}콘텐츠 카드{% elsif include.channel == "banner" %}배너{% elsif include.channel == "email" %}이메일{% elsif include.channel == "in-app message" %}인앱 메시지{% elsif include.channel == "KakaoTalk" %}KakaoTalk 메시지{% elsif include.channel == "push" %}푸시 메시지{% elsif include.channel == "SMS" %}SMS 메시지{% elsif include.channel == "whatsapp" %}WhatsApp 메시지{% elsif include.channel == "webhook" %}웹훅{% endif %}을 캔버스에서 전송한 경우, [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)을 참조하세요.{% endif %}

{% alert tip %}
보고서에 나열된 용어와 측정기준의 정의를 찾고 계신가요? 
  {% if include.channel == "email" %}[이메일 분석 용어집]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)을 참조하세요.
  {% elsif include.channel == "banner" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)에서 배너로 필터링하세요.
  {% elsif include.channel == "Content Card" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)에서 콘텐츠 카드로 필터링하세요.
  {% elsif include.channel == "in-app message" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)에서 인앱 메시지로 필터링하세요.
  {% elsif include.channel == "push" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)에서 푸시로 필터링하세요.
  {% elsif include.channel == "SMS" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)에서 SMS/MMS 및 RCS로 필터링하세요.
  {% elsif include.channel == "whatsapp" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)에서 WhatsApp으로 필터링하세요.
  {% elsif include.channel == "webhook" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)에서 웹훅으로 필터링하세요.{% endif %}
{% endalert %}

**캠페인 분석** 탭에서 일련의 패널을 통해 보고서를 확인할 수 있습니다. 아래 섹션에 나열된 것보다 더 많거나 적은 항목이 표시될 수 있지만, 각각 유용한 목적이 있습니다.

### 시간 범위

기본적으로 **캠페인 분석**의 시간 범위는 현재 시간으로부터 지난 90일을 표시합니다. 즉, 캠페인이 90일 이상 전에 시작된 경우 해당 시간 범위에 대해 분석이 "0"으로 표시됩니다. 이전 캠페인의 모든 분석을 보려면 보고서 시간 범위를 조정하세요.

### 캠페인 세부 정보

**캠페인 세부 정보** 패널은
  {% if include.channel == "banner" %}배너의
  {% elsif include.channel == "Content Card" %}콘텐츠 카드의
  {% elsif include.channel == "email" %}이메일의
  {% elsif include.channel == "in-app message" %}인앱 메시지의
  {% elsif include.channel == "KakaoTalk" %}KakaoTalk 메시지의
  {% elsif include.channel == "push" %}푸시 메시지의
  {% elsif include.channel == "SMS" %}SMS, MMS 및 RCS의
  {% elsif include.channel == "whatsapp" %}WhatsApp 메시지의
  {% elsif include.channel == "webhook" %}웹훅의
  {% endif %}전체 성과에 대한 상위 수준 개요를 보여줍니다.

이 패널에서 수신자에게 전송된 메시지 수, 주요 전환율, 이 메시지로 발생한 총 매출 등 전반적인 측정기준을 확인할 수 있습니다. 이 페이지에서 전달, 오디언스 및 전환 설정도 검토할 수 있습니다.

{% if include.channel == "whatsapp" %}
{% alert note %}
WhatsApp 채널에는 읽기 비율이 포함됩니다. 이 측정기준은 읽음 확인을 켜놓은 사용자에게만 제공되며, 사용자마다 다를 수 있습니다.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![캠페인 성과를 판단하는 데 사용되는 측정기준 개요가 포함된 캠페인 세부 정보 패널.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![캠페인 성과를 판단하는 데 사용되는 측정기준 개요가 포함된 캠페인 세부 정보 패널.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![캠페인 성과를 판단하는 데 사용되는 측정기준 개요가 포함된 캠페인 세부 정보 패널.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![캠페인 성과를 판단하는 데 사용되는 측정기준 개요가 포함된 캠페인 세부 정보 패널.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![캠페인 성과를 판단하는 데 사용되는 측정기준 개요가 포함된 캠페인 세부 정보 패널.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![캠페인 성과를 판단하는 데 사용되는 측정기준 개요가 포함된 캠페인 세부 정보 패널.]({% image_buster /assets/img/campaign_details_iam.png %})

캔버스에서는 생성한 캔버스에 매핑된 인앱 메시지 성과를 확인할 수 있습니다. 페이지 상단의 제어판을 사용하여 다른 메시징 유형(채널)을 지우고 캔버스의 인앱 메시지만 볼 수 있습니다.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![캠페인 세부 정보 섹션.]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![캠페인 성과를 판단하는 데 사용되는 측정기준 개요가 포함된 캠페인 세부 정보 패널.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### 대조군 {#cc-control-group}

개별 콘텐츠 카드의 영향을 측정하려면 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부 정보** 패널에는 대조군 배리언트의 측정기준이 포함되지 않습니다.

{% elsif include.channel == "SMS" %}

#### 대조군 {#sms-control-group}

개별 SMS, MMS 또는 RCS 메시지의 영향을 측정하려면 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부 정보** 패널에는 대조군 배리언트의 측정기준이 포함되지 않습니다.

{% elsif include.channel == "whatsapp" %}

#### 대조군 {#whatsapp-control-group}

개별 WhatsApp 메시지의 영향을 측정하려면 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부 정보** 패널에는 대조군 배리언트의 측정기준이 포함되지 않습니다.

{% elsif include.channel == "webhook" %}

#### 대조군 {#webhook-control-group}

개별 웹훅 메시지의 영향을 측정하려면 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부 정보** 패널에는 대조군 배리언트의 측정기준이 포함되지 않습니다.

{% endif %}

#### 마지막 확인 이후 변경 사항

팀의 다른 구성원이 캠페인에 적용한 업데이트 수는 캠페인 개요 페이지의 *마지막 확인 이후 변경 사항* 측정기준으로 추적됩니다. **마지막 확인 이후 변경 사항**을 선택하면 캠페인의 이름, 스케줄, 태그, 메시지, 오디언스, 승인 상태 또는 팀 접근 구성에 대한 체인지로그를 확인할 수 있습니다. 각 업데이트에 대해 누가 언제 수행했는지 확인할 수 있습니다. 이 체인지로그를 사용하여 캠페인 변경 사항을 감사할 수 있습니다.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### 콘텐츠 카드 성과

**콘텐츠 카드 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![콘텐츠 카드 메시지 성과 분석]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### 이메일 성과

**이메일 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![이메일 메시지 성과 분석]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### 인앱 메시지 성과

**인앱 메시지 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![인앱 메시지 성과 분석]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### 푸시 성과

**푸시 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![푸시 메시지 성과 분석]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCS 성과

**SMS/MMS/RCS 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![대조군, 배리언트 1 및 배리언트 2에 대한 측정기준 표가 포함된 SMS/MMS/RCS 성과 패널.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### 배너 성과

**배너 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이러한 측정기준은 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다.

![대조군, 배리언트 1 및 배리언트 2에 대한 측정기준 표가 포함된 SMS/MMS 성과 패널.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### KakaoTalk 성과

**KakaoTalk 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

{% elsif include.channel == "webhook" %}
### 웹훅 성과

**웹훅 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![대조군 및 배리언트 1에 대한 측정기준 표가 포함된 웹훅 성과 패널.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp 성과

**WhatsApp 성과** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지 보여줍니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![배리언트 1에 대한 측정기준 표가 포함된 WhatsApp 성과 패널.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

보기를 간소화하려면 <i class="fas fa-plus"></i> **열 추가/제거**를 클릭하고 원하는 측정기준을 선택 해제하세요. 기본적으로 모든 측정기준이 표시됩니다.

{% if include.channel == "email" %}

#### 히트맵

히트맵을 사용하면 단일 이메일 캠페인에서 각 링크가 얼마나 성공적인지 확인할 수 있습니다. **메시지 분석** 섹션에서 **이메일 성과** 패널로 이동하세요. **미리보기 & 히트맵**을 선택하여 이메일 캠페인의 미리보기와 히트맵을 확인할 수 있습니다. 또는 배리언트 이름의 하이퍼링크를 선택하여 히트맵을 볼 수도 있습니다.

이 보기에서 **히트맵 표시** 토글을 사용하면 캠페인 기간 동안의 전체 클릭 빈도와 위치를 시각적으로 확인할 수 있습니다. **총 클릭 수별 링크 테이블** 패널에서는 이메일 캠페인의 모든 링크를 확인하고 총 클릭 수로 정렬할 수 있습니다. 이를 통해 사용자가 어디로 이동하는지에 대한 추가 인사이트를 얻을 수 있습니다. 히트맵 사본을 저장하려면 다운로드 버튼을 선택하세요.

![이메일 캠페인과 총 클릭 수가 포함된 링크 별칭 예시 패널이 있는 미리보기 및 히트맵 페이지 예시.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### 이미지

이미지 URL에 CORS를 활성화하여 히트맵 미리보기 및 내보내기에서 이미지가 깨지는 것을 방지하는 것이 좋습니다.

내보내기에서 이미지가 누락된 경우, 개발자와 협력하여 이미지 자산이 교차 출처 접근을 허용하도록 설정하세요. 서버에서 `Access-Control-Allow-Origin` 헤더를 `*` 또는 Braze 대시보드 도메인으로 반환해야 합니다.

{% endif %}

{% if include.channel == "Content Card" %}

#### 콘텐츠 카드 측정기준

메시지 성과를 검토할 때 볼 수 있는 주요 측정기준을 정리했습니다. 모든 콘텐츠 카드 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)에서 콘텐츠 카드로 필터링하여 확인하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Messages Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                이 값은 <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">카드 생성</a> 시 선택한 항목에 따라 다르게 계산됩니다:<br><br>
                <ul>
                    <li><b>시작 또는 단계 진입 시:</b> 생성되어 볼 수 있는 카드의 수입니다. 사용자가 카드를 실제로 조회했는지 여부는 포함되지 않습니다.</li>
                    <li><b>첫 노출 시:</b> 사용자에게 표시된 카드 수입니다.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">총 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 동일한 사용자에 대해 여러 번 증가할 수 있습니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">고유 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">이 카운트는</span> 사용자가 콘텐츠 카드를 두 번째로 볼 때 증가하지 않습니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">고유 수신자</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> 사용자가 매일 고유 수신자로 카운트될 수 있으므로, 이 값은 <i>고유 노출 수</i>보다 높을 수 있습니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">고유 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Braze에서 제공하는 탈퇴 링크 클릭도 포함됩니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">고유 무시 수</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
노출 횟수 기록 방식에는 웹, Android, iOS 간에 약간의 차이가 있습니다. 일반적으로 Braze는 사용자가 피드에서 특정 콘텐츠 카드까지 스크롤하여 카드를 볼 때 노출 횟수를 기록합니다.
{% endalert %}

#### 고유 수신자 대 고유 노출 수

메시지의 가시성을 다루는 몇 가지 측정기준이 있습니다. 여기에는 _고유 수신자_와 _고유 노출 수_가 포함됩니다. 몇 가지 예시 시나리오를 통해 이 측정기준을 더 잘 이해해 보겠습니다.

오늘 콘텐츠 카드를 보고, 내일 같은 캠페인에서 새 카드를 받고, 모레 다시 받는다면 _고유 수신자_로 세 번 카운트됩니다. 하지만 _고유 노출 수_로는 한 번만 카운트됩니다. 카드가 기기에서 사용 가능했으므로 _전송된 메시지 수_에도 포함됩니다.

또 다른 예로, 콘텐츠 카드 캠페인에서 _전송된 메시지 수_가 150,000이고 _고유 노출 수_가 5인 경우를 가정해 보겠습니다. 이는 카드가 150,000명의 오디언스에게(백엔드에서) 제공되었지만, 발송 이후 다음 단계를 모두 수행한 기기는 5대뿐이었음을 의미합니다:

1. 세션을 시작했거나 앱이 명시적으로 콘텐츠 카드 동기화를 요청했습니다(또는 둘 다)
2. 콘텐츠 카드 보기로 이동했습니다
3. SDK가 노출 횟수를 기록하고 서버에 전송했습니다

_전송된 메시지 수_는 볼 수 있도록 제공된 콘텐츠 카드를 의미하고, _고유 수신자_는 실제로 본 콘텐츠 카드를 의미합니다.

{% elsif include.channel == "banner" %}

### 배너 측정기준

배너 캠페인 성과를 검토할 때 추적해야 할 주요 측정기준입니다. 배너의 클릭 수와 노출 수는 SDK를 통해 자동으로 추적됩니다. 

모든 배너 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)에서 배너로 필터링하여 확인하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">총 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 배너의 경우 노출은 사용자 세션당 한 번 기록됩니다. 같은 배너가 같은 세션 내에서 여러 번 조회되더라도 한 번의 노출만 기록됩니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">고유 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">각 사용자는 한 번만 카운트됩니다.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">총 클릭 수</a></td>
            <td class="no-split"><i>총 클릭 수</i>는 동일한 사용자가 여러 번 클릭했는지 여부와 관계없이 전달된 메시지 내에서 클릭한 사용자의 총 수(및 백분율)입니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">고유 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} 각 사용자는 한 번만 카운트됩니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">주요 전환</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">고유 수신자</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> 시청자가 매일 고유 수신자로 카운트될 수 있으므로, 이 값은 <i>고유 노출 수</i>보다 높을 수 있습니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">매출</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">신뢰도</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### 배너 측정기준 계산 예시

메시지의 가시성을 다루는 몇 가지 측정기준이 있습니다. 여기에는 _고유 수신자_와 _고유 노출 수_가 포함됩니다. 몇 가지 예시 시나리오를 통해 이 측정기준을 더 잘 이해해 보겠습니다.

오늘 배너를 보고, 내일 같은 배너를 보고, 모레 다시 본다면 _고유 수신자_로 세 번 카운트됩니다. 하지만 _고유 노출 수_로는 한 번만 카운트됩니다.

또 다른 예로, 배너 캠페인에서 _고유 노출 수_가 5인 경우를 가정해 보겠습니다. 이는 다음 단계를 모두 수행한 기기가 5대뿐이었음을 의미합니다:

1. 세션을 시작했거나 앱이 명시적으로 배너 동기화를 요청했습니다(또는 둘 다)
2. 배너 보기로 이동했습니다
3. SDK가 노출 횟수를 기록하고 서버에 전송했습니다

_고유 수신자_는 실제로 본 배너를 의미합니다.

{% elsif include.channel == "email" %}

#### 이메일 측정기준

다른 채널에서는 볼 수 없는 몇 가지 주요 이메일 전용 측정기준을 소개합니다. Braze에서 사용되는 모든 이메일 측정기준의 전체 정의는 [이메일 분석 용어집]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)을 참조하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">고유 클릭 수</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} 이메일의 경우 7일 동안 추적되며 <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>로 측정됩니다. Braze에서 제공하는 탈퇴 링크 클릭도 포함됩니다. 이 수치는 5~10% 사이가 일반적이며, 10%를 초과하면 매우 우수한 수준입니다!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">고유 열람</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} 이메일의 경우 7일 동안 추적됩니다. 이 수치는 30~40% 사이가 일반적이며, 40%를 초과하면 매우 우수한 수준입니다!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">클릭 후 열람률</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">스팸율</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} 이 측정기준이 0.08을 초과하면 메시지 내용이 너무 판매 지향적이거나, 이메일 주소 수집 방법을 재검토해야 할 수 있습니다(관심 있는 수신자에게 메시지를 보내고 있는지 확인하기 위해).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">구독 취소자 또는 구독 취소</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">기타 열람 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">추정 실제 열람</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} 자세한 내용은 다음 섹션을 참조하세요.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">기계 열람</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">반송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">하드바운스</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">소프트바운스</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">연기</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### 전달 및 반송

대시보드에서는 _하드바운스_가 강조 표시됩니다. 일부 _반송_은 소프트바운스일 수 있으므로 해당 수치만으로는 일치하지 않을 수 있습니다. 다음 공식으로 소프트바운스를 대략적으로 계산할 수 있습니다:

_발송 − (전달 + 하드바운스) ≈ 소프트바운스_

재시도가 성공함에 따라 _전달_은 처음 72시간 동안 증가할 수 있으며, 일회성 발송의 _발송_ 수와 하드바운스는 발송이 완료되면 고정됩니다.

##### 열람 이벤트 없는 클릭

열람 추적 픽셀이 로드되지 않으면 열람 없이 클릭이 기록될 수 있습니다. 예를 들어, Gmail에서 메시지가 잘리거나 사용자가 이미지를 비활성화한 경우(열람 추적 픽셀은 보통 푸터에 위치)가 이에 해당합니다. 일부 클라이언트는 이미지를 프록시 처리하므로(예: Apple Mail), 사용자가 메일을 읽을 때가 아니라 서버가 처음 픽셀을 가져올 때 열람이 기록될 수 있습니다. 기업 도메인은 기본적으로 이미지를 차단하는 경우가 많습니다.

클릭과 열람이 서로 다른 날에 발생할 수도 있습니다. 사용자가 5월 16일에 이미지가 꺼진 상태에서 클릭하고(열람 없음), 5월 17일에 웹메일에서 열람할 수 있습니다(그때 열람이 기록됨).

##### 연기

연기(Deferral)는 이메일이 즉시 전달되지 않았지만, Braze가 이 임시 전달 실패 후 최대 72시간 동안 이메일 재전송을 시도하여 해당 캠페인에 대한 시도가 중단되기 전에 성공적인 전달 가능성을 극대화하는 것을 의미합니다. 일반적인 연기 사유에는 받은편지함 제공자의 평판 기반 이메일 볼륨 속도 제한, 일시적인 연결 문제 또는 DNS 오류가 포함됩니다.

_연기_는 _소프트바운스_와 다릅니다. 이 재시도 기간 동안 이메일이 성공적으로 전달되지 않으면, Braze는 시도된 캠페인 발송당 하나의 소프트바운스 이벤트를 전송합니다. 2025년 2월 25일 이전에는 이러한 재시도가 1개의 캠페인 발송에 대해 여러 번의 소프트바운스로 카운트되었습니다.

_연기_는 현재 커런츠 또는 Braze Snowflake 기능(예: Query Builder, SQL Segment, Snowflake Data Sharing)을 통해서만 확인할 수 있습니다. 캠페인 또는 캔버스 분석에 포함하고 싶으시다면 [제품 피드백을 제출]({{site.baseurl}}/user_guide/administrative/access_braze/portal)해 주세요.

##### 추정 실제 열람율 {#estimated-real-open-rate}

이 통계는 Braze가 개발한 독점 분석 모델을 사용하여 기계 열람이 존재하지 않는 것처럼 캠페인의 고유 열람율 추정치를 재구성합니다. 이메일 발신자로부터 일부 열람 이벤트에 대한 *기계 열람* 레이블을 받지만(위 참조), 이러한 레이블은 실제 열람을 기계 열람으로 잘못 분류하는 경우가 많습니다. 즉, *기타 열람*은 실제 사용자에 의한 열람 수를 과소 추정할 가능성이 높습니다. 대신 Braze는 각 캠페인의 클릭 데이터를 사용하여 실제 사용자가 메시지를 열어본 비율을 추론합니다. 이를 통해 Apple의 MPP를 비롯한 다양한 기계 열람 메커니즘을 보완합니다.

_추정 실제 열람율_은 이메일 발송이 시작된 후 36시간이 지나면 계산되며, 이후 매 24시간마다 재계산됩니다. 캠페인이 반복되면 다른 발송이 발생한 후 36시간 후에 추정치가 재계산됩니다.

이 측정기준은 지속적으로 재계산되므로, _추정 실제 열람율_ 값은 새로운 참여 신호(예: 열람 및 클릭)가 수신되어 모델에 반영됨에 따라 시간이 지나면서 변경될 수 있습니다. 실제로 _추정 실제 열람율_은 캠페인이 활성 상태인 동안 매일 업데이트될 수 있습니다.

일반적으로 통계가 성공적으로 계산되려면 약 10,000개의 전달된 이메일이 필요하지만, 이 수치는 클릭률에 따라 달라질 수 있습니다. 통계를 계산할 수 없는 경우 열에 "--"가 표시됩니다.

###### 제한 사항

추정 실제 열람율은 캠페인에서만 사용할 수 있으며, 커런츠 이벤트에서는 보고되지 않습니다. 이 측정기준은 2023년 11월 14일 이전에 시작된 활성 캠페인에 대해서만 소급하여 계산됩니다.

##### 클릭률 증가 처리

열람율은 이메일 캠페인에서 추적할 수 있는 유용한 측정기준입니다. 하지만 이러한 열람율이 반드시 이메일 캠페인에 대한 사람의 참여를 정확하게 나타내는 지표는 아닙니다. 열람 이벤트는 정의상 사용자가 이메일을 열었을 때, 즉 투명한 열람 추적 픽셀이 성공적으로 다운로드되었을 때 발생합니다. 

또한 보안 스캐닝 도구를 사용하면 열람율이 부풀려질 수 있습니다. 이러한 도구 중 일부는 수신 이메일에서 악성 콘텐츠를 스캔하면서 링크를 클릭하여 합법성을 확인합니다. 이러한 클릭을 흔히 "봇 클릭" 또는 "비인간 상호작용(NHI)"이라고 합니다. 

궁극적으로 이메일이 서버를 떠난 후에는 가시성이 제한되지만, 결과에 영향을 미치는 NHI를 관리하기 위한 권장 사항은 다음과 같습니다:

1. 이는 모든 발신자와 거의 모든 수신자에게 발생할 수 있다는 점을 인지하세요. 열람과 마찬가지로 클릭도 메시지와의 인간 상호작용을 완전히 신뢰할 수 있는 지표가 아니므로 NHI를 방지할 수는 없습니다.
2. 높은 긍정적 참여는 낮은 NHI와 상관관계가 있는 경향이 있으므로, 이메일 메시징 [모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)를 따르는 것이 중요합니다. 여기에는 사용자로부터 이메일 전송에 대한 명시적인 동의를 받고, 참여하지 않는 가입자를 정기적으로 서비스 종료하는 것이 포함됩니다. 
3. 가능하면 이메일에 HTTPS 링크를 사용하세요. 보안 링크를 사용하는 발신자에게는 NHI가 덜 발생합니다.
4. 단일 클릭 탈퇴 프로세스를 사용하는 경우, 사용자가 알림 기본 설정을 편집하고 관리할 수 있는 페이지로 이동하는 [선호 센터]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview)를 만드는 것을 고려하세요. NHI가 실수로 사용자의 구독을 취소할 수 있으므로 이 방법이 유용합니다.
5. 전환, 앱 세션 또는 사이트 방문과 같은 [다른 측정기준]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance)을 사용하여 이메일 마케팅 성과를 측정하는 것도 고려해 보세요.
6. 이메일 캠페인에 숨겨진 링크를 추가하세요. 흰색 배경에 흰색 텍스트나 구두점처럼 사람이 알아차리지 못할 링크입니다. 봇은 모든 링크를 클릭하는 경향이 있으므로, 보이지 않는 링크에서 클릭 이벤트를 생성하는 사용자는 실제로 NHI의 결과라고 판단할 수 있습니다. 따라서 해당 열람이나 클릭이 반드시 긍정적인 참여를 나타내는 것은 아닙니다.

{% elsif include.channel == "in-app message" %}

#### 인앱 메시지 측정기준

분석에서 볼 수 있는 몇 가지 주요 인앱 메시지 측정기준을 소개합니다. Braze에서 사용되는 모든 인앱 메시지 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하세요.

{% alert note %}
_버튼 1 클릭_ 및 _버튼 2 클릭_에 대한 보고는 인앱 메시지에서 **보고용 식별자**를 각각 "0"과 "1"로 지정한 경우에만 작동합니다.

!["보고용 식별자" 필드의 값이 "0"입니다.]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">본문 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">버튼 1 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">버튼 2 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">고유 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">총 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">전환 (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">총 전환 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">전환율</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">메시지 닫기</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "KakaoTalk" %}

### KakaoTalk 측정기준

분석에서 볼 수 있는 몇 가지 주요 KakaoTalk 측정기준을 소개합니다. 자세한 내용은 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)을 참조하세요.

| 용어 | 정의 |
| --- | --- |
| 오디언스 | _오디언스_는 특정 메시지를 수신한 사용자의 비율입니다. <br><br>_(배리언트의 수신자 수) / (고유 수신자)_ |
| 고유 수신자 | _고유 수신자_는 하루에 새 메시지를 수신한 고유 일일 수신자 또는 사용자의 수입니다. 이 카운트가 사용자에 대해 두 번 이상 증가하려면 사용자가 다른 날에 새 메시지를 수신해야 합니다. 이 수치는 `user_id`를 기반으로 합니다. 자세한 내용은 [보고서 측정기준 용어집의 고유 수신자]({{site.baseurl}}/user_guide/data/report_metrics/#unique-recipients)를 참조하세요. |
| 발송 수 | 캠페인에서 발송된 총 메시지 수입니다. 메시지가 기기에 수신되거나 전달되었음을 의미하지 않으며, 메시지가 발송되었다는 것만을 의미합니다. |
| 총 클릭 수 | 발송된 KakaoTalk 메시지가 사용자에 의해 클릭된 총 횟수입니다. |
| 오류 수 | _오류 수_는 KakaoTalk 제공자가 반환한 오류의 수입니다(발송 과정에서 증가). |
| 매출 | _매출_은 설정된 주요 전환 기간 내 캠페인 수신자로부터의 달러 매출입니다. |
| 주요 전환 | _주요 전환_은 Braze 캠페인에서 수신한 메시지를 보거나 상호작용한 후 정의된 이벤트가 발생한 횟수입니다. 이 정의된 이벤트는 캠페인을 구축할 때 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% elsif include.channel == "push" %}

#### 푸시 측정기준

메시지 성과를 검토할 때 볼 수 있는 주요 측정기준을 정리했습니다. 모든 푸시 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)에서 푸시로 필터링하여 확인하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>설명</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">반송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} <a href="#bounced-push">반송된 푸시 알림</a>을 참조하세요.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">직접 열람 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">열람 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> 알림 전달은 Apple Push Notification 서비스(APNs)의 "최선의 노력"으로 이루어집니다. 앱에 데이터를 전달하기 위한 것이 아니라, 사용자에게 새로운 데이터가 있음을 알리기 위한 것입니다. 중요한 점은 APNs에 성공적으로 전달한 메시지 수를 표시하며, APNs가 기기에 성공적으로 전달한 수와는 다를 수 있다는 것입니다.

##### 구독 취소 추적

푸시 구독 취소는 캠페인 분석의 측정기준에 포함되지 않으며, Apple이나 Google 같은 제공업체의 사용자 푸시 상태 업데이트에 따라 달라집니다. 이러한 업데이트는 드물고 예측하기 어려울 수 있습니다. 따라서 푸시 구독 취소는 푸시 캠페인 분석의 측정기준으로 포함되지 않습니다. 

하지만 수동으로 푸시 구독 취소를 추적하면 알림 빈도와 콘텐츠 관련성에 대한 사용자 반응에 관한 귀중한 인사이트를 얻을 수 있습니다. 푸시 구독 취소를 추적하는 두 가지 방법은 세그먼트 필터 또는 커스텀 필터를 사용하는 것입니다.

{% tabs local %}
{% tab Segment filters %}

푸시가 활성화되지 않은 사용자, 즉 구독하지 않았거나 옵트인하지 않았으며 [포그라운드 푸시 토큰]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)이 없는 사용자를 식별하기 위해 세그먼트를 생성할 수 있습니다. 예를 들어, 앱에서 구독 취소 수를 확인하려면 다음 세그먼트의 "OR" 조합을 사용합니다: 

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![앱에 대해 "백그라운드 또는 포그라운드 푸시 활성화" 필터가 false로 설정되고 "제거됨" 필터가 선택된 세그먼트 빌더 섹션.]({% image_buster /assets/img/push_unsub_segment_example.png %})

세분화 필터는 대략적이며 특정 날짜나 캠페인에 정확히 연결할 수 없습니다.

{% endtab %}
{% tab Custom filters %}

{% alert important %}
구독 변경에 대한 커스텀 이벤트를 기록하면 [데이터 포인트]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count)가 소비됩니다. 또는 세그먼트 필터를 사용하여 푸시가 활성화되지 않은 사용자를 식별하고 타겟팅할 수 있습니다.
{% endalert %}

다른 방법으로, 사용자의 푸시 활성화 상태가 `true`인지 `false`인지에 따라 푸시 구독 취소에 대한 커스텀 이벤트를 생성하여 이 측정기준을 추적하는 것도 좋습니다.

{% endtab %}
{% endtabs %}

##### 열람 이해하기

_직접 열람_과 _영향을 받은 열람_은 모두 "열람"이라는 단어를 포함하지만, 실제로는 서로 다른 측정기준입니다. _직접 열람_은 위의 표에 명시된 대로 푸시 알림을 직접 여는 것을 의미합니다. _영향을 받은 열람_은 푸시 알림을 받은 후 특정 시간 내에 푸시 알림을 열지 않고 앱을 여는 것을 의미합니다. 따라서 _영향을 받은 열람_은 푸시 알림 열람이 아닌 앱 열람을 나타냅니다.

##### 푸시 발송이 고유 수신자를 초과할 수 있는 이유

_발송_ 수가 _고유 수신자_ 수를 초과할 수 있는 이유는 다음과 같습니다:

- **재자격이 활성화된 경우:** 캠페인 또는 캔버스 설정에서 재자격이 활성화되면, 세그먼트 및 전달 기준을 충족하는 사용자가 동일한 푸시 알림을 여러 번 받을 수 있습니다. 이로 인해 총 발송 수가 증가합니다.
- **사용자가 여러 기기를 가진 경우:** 재자격이 활성화되지 않은 경우, 사용자가 프로필에 연결된 여러 기기를 가지고 있기 때문일 수 있습니다. 예를 들어, 사용자가 스마트폰과 태블릿을 모두 가지고 있으면 푸시 알림이 등록된 모든 기기로 전송됩니다. 각 전달은 발송으로 카운트되지만, 고유 수신자는 한 명만 기록됩니다.
- **사용자가 여러 앱에 할당된 경우:** 사용자가 여러 앱(예: 새 앱 테스트 시)에 연결되어 있으면 각 앱에서 동일한 푸시 알림을 받을 수 있습니다. 이로 인해 발송 수가 증가합니다.

##### 반송이 발생하는 이유 {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

반송은 Apple Push Notification 서비스(APNs)에서 푸시 알림이 의도된 앱이 설치되지 않은 기기로 전달을 시도할 때 발생합니다. APNs는 기기의 토큰을 임의로 변경할 수도 있습니다. 이전에 토큰을 등록한 시점(예: 각 세션 시작 시 사용자의 푸시 토큰을 등록할 때)과 실제 발송 시점 사이에 푸시 토큰이 변경된 사용자의 기기로 발송을 시도하면 반송이 발생합니다.

사용자가 기기 설정에서 푸시를 비활성화하면, 이후 앱을 열 때 SDK가 푸시 비활성화를 감지하고 Braze에 알립니다. 이 시점에서 푸시 활성화 상태가 비활성화로 업데이트됩니다. 비활성화된 사용자가 새 세션을 시작하기 전에 푸시 캠페인을 받으면, 캠페인은 성공적으로 전송되어 전달된 것으로 표시됩니다. 이 사용자에 대해 푸시가 반송되지는 않습니다. 이후 세션에서 사용자에게 푸시를 보내려고 할 때, Braze는 이미 포그라운드 토큰 유무를 알고 있으므로 알림이 전송되지 않습니다.

전달 전에 만료되는 푸시 알림은 실패로 간주되지 않으며 반송으로 기록되지 않습니다.

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging(FCM) 반송은 세 가지 경우에 발생할 수 있습니다:

| 시나리오 | 설명 |
| -- | -- |
| 제거된 애플리케이션 | 메시지가 기기로 전달을 시도할 때 해당 기기에 의도된 앱이 제거되어 있으면, 메시지는 폐기되고 기기의 등록 ID가 무효화됩니다. 이후 해당 기기에 메시지를 보내려는 모든 시도는 NotRegistered 오류를 반환합니다. |
| 백업된 애플리케이션 | 애플리케이션이 백업될 때 등록 ID가 애플리케이션 복원 전에 유효하지 않게 될 수 있습니다. 이 경우 FCM은 더 이상 애플리케이션의 등록 ID를 저장하지 않으며 애플리케이션은 더 이상 메시지를 수신하지 않습니다. 따라서 등록 ID는 애플리케이션이 백업될 때 **저장하지 않아야** 합니다. |
| 업데이트된 애플리케이션 | 애플리케이션이 업데이트되면 이전 버전의 등록 ID가 더 이상 작동하지 않을 수 있습니다. 따라서 업데이트된 애플리케이션은 기존 등록 ID를 교체해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS, MMS 및 RCS 측정기준

메시지 성과를 검토할 때 볼 수 있는 주요 측정기준을 정리했습니다. 모든 SMS, MMS 및 RCS 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)에서 SMS/MMS 및 RCS로 필터링하여 확인하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">발송됨</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">전달 실패 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">확인된 전달</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">거부 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">옵트아웃</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">도움말</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">총 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### 웹훅 측정기준

분석에서 볼 수 있는 몇 가지 주요 웹훅 측정기준을 소개합니다. Braze에서 사용되는 모든 웹훅 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">고유 수신자</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">발송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">오류 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp 측정기준

분석에서 볼 수 있는 몇 가지 주요 WhatsApp 측정기준을 소개합니다. Braze에서 사용되는 모든 WhatsApp 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">발송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">전달 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">읽기 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">실패 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### 최종 사용자 차단 및 보고 측정기준

추가 측정기준은 [WhatsApp 매니저 대시보드](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx)를 통해 확인할 수 있지만, 모든 인사이트에 접근하려면 [접근 권한 확인](https://www.facebook.com/business/help/218116047387456)이 필요합니다. 

{% endif %}

### 과거 성과

**과거 성과** 패널에서는 **메시지 성과** 패널의 측정기준을 시간 경과에 따른 그래프로 확인할 수 있습니다. 패널 상단의 필터를 사용하여 그래프에 표시되는 통계와 채널을 수정할 수 있습니다. 이 그래프의 시간 범위는 항상 페이지 상단에 지정된 시간 범위를 반영합니다. 

일별 세부 정보를 확인하려면 <i class="fas fa-bars"></i> 햄버거 메뉴를 클릭하고 **CSV 다운로드**를 선택하여 보고서의 CSV 내보내기를 받으세요.

![2021년 2월부터 2022년 5월까지 이메일에 대한 예시 통계가 포함된 과거 성과 패널 그래프.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
최신 Braze 버전의 인앱 메시지(3세대)를 볼 수 있는 사용자에게만 전송하도록 선택한 경우, **타겟 오디언스**는 해당 선택을 반영하도록 조정되지 않습니다.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### 키워드 응답

**키워드 응답** 패널은 사용자가 메시지를 받은 후 회신한 인바운드 키워드의 타임라인을 보여줍니다.  

![옵트인, 옵트아웃, 도움말, 기타, 더보기 및 코칭에 대한 체크박스가 선택된 키워드 카테고리 섹션과 시간에 따른 키워드 분포 선 그래프가 포함된 캠페인 수준 SMS/MMS/RCS 키워드 응답 패널.]({% image_buster /assets/img/sms/keyword_responses.png %})

여기에서 각 키워드 카테고리의 응답 분포를 확인하여 [리타겟팅]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns)의 다음 단계를 결정하고 편리하게 [세그먼트를 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)할 수 있습니다.

![키워드 카테고리, 응답 분포 및 리타겟팅 열이 있는 선 그래프 아래의 테이블로, 키워드 카테고리로 세그먼트를 생성할 수 있는 옵션이 제공됩니다.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### 전환 이벤트 세부 정보

**전환 이벤트 세부 정보** 패널에는 캠페인의 전환 이벤트 성과가 표시됩니다. 자세한 내용은 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results)를 참조하세요.

![전환 이벤트 세부 정보 패널.]({% image_buster /assets/img/cc-conversion.png %})

### 전환 상관관계

**전환 상관관계** 패널은 캠페인에 설정한 결과에 도움이 되거나 해가 되는 사용자 속성과 동작에 대한 인사이트를 제공합니다. 자세한 내용은 [전환 상관관계]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/)를 참조하세요.

![주요 전환 이벤트 - A의 사용자 속성과 동작에 대한 분석이 포함된 전환 상관관계 패널.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## 보고서 빌더

[보고서 빌더]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)를 사용하여 KakaoTalk 캠페인에 대한 커스텀 보고서를 작성할 수도 있습니다. 보고서를 생성할 때 **채널**에서 **KakaoTalk**을 선택하여 KakaoTalk 캠페인만 포함하도록 필터링하거나, KakaoTalk 캠페인에 적용한 태그로 필터링할 수 있습니다.

{% endif %}

{% if include.channel == "whatsapp" %}

### 메타 분석

Braze 분석 외에도 템플릿 수준의 분석은 WhatsApp 비즈니스 매니저에서 확인할 수 있습니다. 자세한 내용은 [메타의 설명서](https://www.facebook.com/business/help/218116047387456)를 참조하세요.

{% endif %}

{% if include.channel == "SMS" %}

### SMS 커런츠 이벤트

이메일과 마찬가지로, Braze는 SMS 메시지가 사용자에게 전달되는 과정에서 사용자 수준의 이벤트를 수신합니다. 모든 인바운드 SMS 이벤트는 [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) 이벤트를 통해 커런츠 이벤트로도 전송됩니다. 이를 통해 Braze 플랫폼 외부에서 사용자가 보내는 메시지에 대해 추가 작업이나 보고를 수행할 수 있습니다. 

{% alert note %}
인바운드 메시지는 1,600자를 초과하면 잘립니다.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## 리텐션 보고서

리텐션 보고서는 특정 캠페인{% if include.channel != "banner" %} 또는 캔버스{% endif %}에서 시간에 따라 사용자가 선택한 리텐션 이벤트를 수행한 비율을 보여줍니다. 자세한 내용은 [리텐션 보고서]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)를 참조하세요.

## 퍼널 보고서

퍼널 보고서는 캠페인{% if include.channel != "banner" %} 또는 캔버스{% endif %}를 받은 후 고객이 취하는 여정을 분석할 수 있는 시각적 보고서를 제공합니다. 캠페인{% if include.channel != "banner" %} 또는 캔버스{% endif %}에서 대조군이나 여러 배리언트를 사용하는 경우, 다양한 배리언트가 전환 퍼널에 미친 영향을 더 세부적으로 이해하고 이 데이터를 기반으로 최적화할 수 있습니다.

자세한 내용은 [퍼널 보고서]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)를 참조하세요.

{% endif %}