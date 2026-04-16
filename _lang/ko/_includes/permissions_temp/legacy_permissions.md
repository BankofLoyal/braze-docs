{% alert important %}
Braze는 사용자 액세스를 보다 유연하게 관리할 수 있는 [세분화된 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions)을 도입했습니다. 레거시 권한이 세분화된 권한에 어떻게 매핑되는지를 포함한 마이그레이션 프로세스에 대해 알아보려면 [세분화된 권한으로 마이그레이션]({{site.baseurl}}/granular_permissions_migration/)을 참조하세요.
{% endalert %}

## 권한 세트 생성

권한 세트를 사용하면 특정 주제 영역이나 동작과 관련된 권한을 하나로 묶을 수 있습니다. 여러 워크스페이스에서 동일한 액세스가 필요한 대시보드 사용자에게 권한 세트를 적용할 수 있습니다. 권한 세트를 만들려면 **설정** > **권한 설정**으로 이동한 다음 **권한 세트 만들기**를 선택합니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions)을 참조하세요.

{% tabs local %}
{% tab example permission sets %}
|이름|권한|
|-----------|----------------|
|개발자|"개발자 콘솔에 액세스"|
|마케터|"캠페인, 캔버스, 카드, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경 설정 센터에 액세스" <br> "미디어 라이브러리 자산 관리"|
|사용자 관리|"대시보드 사용자 관리" <br> "Teams 관리"|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## 역할 만들기

역할은 개별 커스텀 권한을 워크스페이스 액세스 제어와 함께 묶어 더 체계적인 구조를 제공합니다. 하나의 대시보드에 여러 브랜드나 지역별 워크스페이스가 있는 경우 특히 유용합니다. 역할을 사용하면 대시보드 사용자를 적절한 워크스페이스에 추가하고 관련 권한을 직접 부여할 수 있습니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions)을 참조하세요.

{% tabs local %}
{% tab example roles %}
| 역할 이름    | 워크스페이스 | 권한  
----------- | ----------- | ---------
| 마케터 - 패션 브랜드 | {::nomarkdown}[DEV] 패션 브랜드, [QA] 패션 브랜드, [PROD] 패션 브랜드 {:/} | "캠페인, 캔버스, 카드, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경 설정 센터에 액세스"<br>"미디어 라이브러리 자산 관리" |
| 마케터 - 스킨케어 브랜드 | {::nomarkdown}[DEV] 스킨케어 브랜드, [QA] 스킨케어 브랜드, [PROD] 스킨케어 브랜드 {:/} | "캠페인, 캔버스, 카드, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경 설정 센터에 액세스" <br>"미디어 라이브러리 자산 관리" |
| 사용자 관리 - 모든 브랜드 | {::nomarkdown}[DEV] 패션 브랜드, [QA] 패션 브랜드, [PROD] 패션 브랜드, [DEV] 스킨케어 브랜드, [QA] 스킨케어 브랜드, [PROD] 스킨케어 브랜드 {:/} | "대시보드 사용자 관리"<br>"Teams 관리" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## 권한 세트와 역할은 Teams와 어떻게 다른가요?

{% multi_lang_include permissions.md content="Differences" %}

### Teams에 사용자 권한을 추가할 때 고려 사항

Braze 대시보드에서 권한을 저장할 때, 특히 워크스페이스에서 사용자를 추가하거나 제거하거나 Teams에 추가할 때 어려움이 발생할 수 있습니다. 사용자의 권한이 워크스페이스 수준에서 이미 보유한 권한과 동일한 경우 **저장/사용자 업데이트** 버튼이 비활성화될 수 있습니다. 이 제한은 모든 사용자가 전체 워크스페이스와 동일한 권한을 가지면 Teams를 사용할 이점이 없기 때문에 존재합니다.

동일한 권한을 유지하면서 사용자를 Teams에 성공적으로 추가하려면 워크스페이스 수준에서 권한을 할당하지 마세요. 대신 팀 수준에서만 권한을 할당하세요.

## 제한된 사용자

제한된 사용자는 Braze 대시보드의 특정 측면을 관리할 수 있는 특정 권한을 가지고 있지만, 회사 관리자 및 워크스페이스 관리자에 비해 제한이 있습니다.

| 권한 | 제한된 사용자는 "대시보드 사용자 관리" 권한이 체크된 경우 다른 제한된 사용자의 권한을 편집할 수 있습니다. 또한 새로운 제한된 사용자를 생성하고 권한 세트를 수정할 수 있습니다. 그러나 회사 관리자 계정을 생성하거나 관리할 수는 없습니다. |
| 역할 제한 | 제한된 사용자가 "앱 그룹 관리자"를 제외한 모든 권한을 가지고 있다면, 워크스페이스 관리자에게 일반적으로 부여되는 다른 모든 권한에 여전히 접근할 수 있습니다. |
| 권한 가시성 | 제한된 사용자가 한 앱 그룹(예: Dev)에 대해 "대시보드 사용자 관리"가 체크되어 있지만 다른 앱 그룹(예: Prod)에 대해서는 체크되어 있지 않다면, "사용자 관리" 프로필에서 Prod 앱 그룹 권한을 볼 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 제한된 사용자 비교

| 제한된 사용자 유형 | 설명 |
| --- | --- |
| 앱 그룹 관리자 | 앱 그룹 관리자는 앱 그룹 관리에 특화된 권한을 가지고 있지만 회사 관리자와 동일한 권한은 없습니다. 제한된 사용자는 필요한 권한이 체크되어 있다면 앱 그룹 관리자와 유사한 권한을 상속받을 수 있습니다. |
| 회사 관리자 | 회사 관리자는 대시보드 사용자를 삭제할 수 있는 등 더 넓은 권한을 가지고 있습니다. 그러나 자신의 계정은 삭제할 수 없으며, 해당 작업을 위해 다른 회사 관리자에게 연락해야 합니다. |
| 기본 읽기 전용 권한 | 기술 파트너 페이지와 같은 대시보드의 특정 부분에 접근하려면 기본 읽기 전용 권한이 필요합니다. 여기에는 "외부 통합 관리"가 활성화되어 있어야 하며, 캠페인, 캔버스, 카드, 세그먼트 및 미디어 라이브러리에 대한 액세스 권한이 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 제한된 접근 오류

사용자에게 "제한된 접근. 이 페이지에 접근할 권한이 없습니다."와 같은 메시지가 표시될 수 있습니다. 이런 경우, 계정 관리자는 사용자의 권한을 비활성화한 후 다시 활성화하여 문제를 해결할 수 있는지 확인해야 합니다.

{% alert note %}
한 대시보드 사용자의 권한을 다른 사용자로 병합하거나 가져오는 것은 불가능합니다.
{% endalert %}

## 사용자 권한 편집

사용자의 현재 관리자, 회사 또는 워크스페이스 권한을 편집하려면 **설정** > **회사 사용자**로 이동한 다음 해당 사용자의 이름을 선택하세요.

![결과에 사용자 한 명이 나열된 Braze의 "회사 사용자" 페이지.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### 관리자

관리자는 모든 기능에 접근할 수 있으며 회사 설정을 수정할 수 있습니다. 관리자는 다음을 수행할 수 있습니다:

- [승인 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval) 변경
- 다른 [Braze 사용자]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)를 추가, 편집, 삭제, 일시 중지 또는 일시 중지 해제
- Braze 사용자를 CSV로 내보내기

관리자 권한을 부여하거나 제거하려면 **이 사용자는 관리자입니다**를 선택한 다음 **사용자 업데이트**를 선택하세요.

![선택된 사용자의 세부 정보와 관리자 체크박스가 포커스된 상태.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
사용자에게서 관리자 권한을 제거하면, 최소한 하나의 [회사 수준 또는 워크스페이스 수준]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions&tab=company#legacypermissions_editing-a-users-permissions) 권한을 할당할 때까지 해당 사용자는 Braze에 접근할 수 없습니다.
{% endalert %}

{% endtab %}
{% tab Company %}

### 회사

사용자의 회사 수준 권한을 관리하려면 해당 권한 옆의 체크박스를 선택하거나 해제하세요. 완료되면 **사용자 업데이트**를 선택하세요.

|권한 이름|설명|
|----------|-----------|
|회사 설정 관리|사용자가 회사 설정을 수정할 수 있습니다.|
|워크스페이스 생성 및 삭제|사용자가 워크스페이스를 생성하고 삭제할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### 워크스페이스

Braze에서 사용자가 속한 각 워크스페이스에 대해 서로 다른 권한을 부여할 수 있습니다. 워크스페이스 수준 권한을 관리하려면 **워크스페이스 및 권한 선택**을 선택한 다음, 수동으로 권한을 선택하거나 [이전에 생성한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_creating-a-permission-set) 권한 세트를 할당하세요.

사용자에게 워크스페이스별로 다른 권한을 부여해야 하는 경우, 필요한 만큼 이 과정을 반복하세요. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions)을 참조하세요.

{% subtabs %}
{% subtab Select manually %}

**워크스페이스**에서 드롭다운을 통해 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **권한**에서 드롭다운을 통해 하나 이상의 권한을 선택합니다. Braze는 선택한 워크스페이스에 대해서만 이러한 권한을 할당합니다. 선택적으로 **관리자 액세스 활성화**를 선택하여 해당 워크스페이스에 대한 전체 권한을 부여할 수도 있습니다.

완료되면 **사용자 업데이트**를 선택하세요.

![Braze에서 수동으로 선택된 워크스페이스 수준 권한.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual_legacy.png %})

{% endsubtab %}
{% subtab Assign permission set %}

**워크스페이스**에서 드롭다운을 통해 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **권한 세트**에서 하나의 권한 세트를 선택합니다. Braze는 선택한 워크스페이스에 대해서만 이러한 권한을 할당합니다.

완료되면 **사용자 업데이트**를 선택하세요.

![Braze에서 권한 세트를 통해 할당된 워크스페이스 수준 권한.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set_legacy.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 사용자 권한 내보내기

사용자 및 권한 목록을 다운로드하려면 **설정** > **회사 사용자**로 이동한 다음 **사용자 내보내기**를 선택하세요. 잠시 후 CSV 파일이 이메일 주소로 전송됩니다.

![Braze의 "회사 사용자" 페이지에서 "사용자 내보내기" 옵션이 포커스된 상태.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## 권한 목록

|레벨|이름|정의|
|---|---|---|
|관리자|관리자|사용자가 사용 가능한 모든 기능에 액세스할 수 있습니다. 모든 신규 사용자의 기본값 설정입니다. 회사 이름 및 시간대를 포함한 회사 설정을 업데이트할 수 있으며, 제한된 사용자는 이를 수행할 수 없습니다.|
|회사|워크스페이스 생성 및 삭제|사용자가 워크스페이스를 생성하고 삭제할 수 있습니다.|
|회사|회사 설정 관리|사용자가 회사 설정을 수정할 수 있습니다.|
|워크스페이스|캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리, 위치, 프로모션 코드 및 환경 설정 센터에 액세스|사용자가 캠페인 및 캔버스 성과 측정기준을 보고, 캠페인 및 캔버스 초안을 생성 및 복제하고, 캠페인 및 캔버스 초안과 템플릿을 편집하고, 세그먼트, 템플릿 및 미디어 초안을 보고, 템플릿을 생성하고, 미디어를 업로드하고, 프로모션 코드 목록을 생성 또는 업데이트하고, 참여 보고서를 보고, 대시보드에서 글로벌 메시지 설정을 볼 수 있습니다. 그러나 이 권한을 가진 사용자는 기존 라이브 콘텐츠를 일시 중지하거나 편집할 수 없습니다.<br><br>이 권한이 [Teams 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)으로 구성된 경우, [참여 보고서]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/)의 캠페인이나 캔버스가 사용자에게 할당된 Teams 외부에 있거나 할당된 Teams가 없으면 해당 보고서가 사용자에게 표시되지 않습니다.|
|워크스페이스|개발자 콘솔 액세스|다음 설정 및 로그에 대한 전체 액세스를 허용합니다:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API 키</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>내부 그룹</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>메시지 활동 로그</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>이벤트 사용자 로그</a></li></ul>{:/}|
|워크스페이스|캠페인 승인 및 거부|사용자가 캠페인을 승인하거나 거부할 수 있습니다. 이 권한이 적용되려면 캠페인에 대한 [승인 워크플로우]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/)가 활성화되어야 합니다. 이 설정은 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 계정 매니저에게 문의하세요.|
|워크스페이스|캔버스 승인 및 거부|사용자가 캔버스를 승인하거나 거부할 수 있습니다. 이 권한이 적용되려면 캔버스에 대한 [승인 워크플로우]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/)가 활성화되어야 합니다.|
|워크스페이스|커런츠 통합 편집|사용자가 자격 증명을 포함하여 커런츠 연결을 수정할 수 있습니다. 기본적으로 "외부 통합" 권한이 할당된 사용자에게도 이 권한이 할당됩니다.|
|워크스페이스|세그먼트 편집|사용자가 세그먼트를 생성하고 편집할 수 있습니다. 이 권한 없이도 기존 세그먼트 및 필터로 캠페인을 생성할 수 있습니다. CSV의 사용자로부터 세그먼트를 생성하거나 CSV의 사용자 그룹을 리타겟하려면 이 권한이 필요합니다.|
|워크스페이스|사용자 데이터 내보내기|사용자가 세그먼트, 캠페인 및 캔버스에서 사용자 데이터를 내보낼 수 있습니다. 이 권한에는 이름, 이메일 주소 및 기타 수집된 개인 식별 정보(PII)와 같은 민감한 사용자 정보가 포함됩니다. 대시보드에서 CSV를 내보내려면 이 권한과 "PII 보기" 권한이 모두 필요합니다.|
|워크스페이스|사용자 데이터 가져오기 및 업데이트|사용자가 앱 사용자의 CSV 파일을 가져오고 업데이트하며 사용자 가져오기 페이지를 볼 수 있습니다. 또한 사용자의 구독 상태와 구독 그룹 옵트인/옵트아웃 규칙을 편집할 수 있습니다.|
|워크스페이스|콘텐츠 블록 시작 및 관리|사용자가 [콘텐츠 블록]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/)을 시작하고 관리할 수 있습니다.|
|워크스페이스|환경 설정 센터 시작|사용자가 [환경 설정 센터]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/)를 시작할 수 있습니다.|
|워크스페이스|앱 관리|사용자가 **앱 설정**을 편집할 수 있습니다.|
|워크스페이스|카탈로그 대시보드 권한 관리|사용자가 카탈로그를 생성하고 관리할 수 있습니다.|
|워크스페이스|대시보드 사용자 관리|관리자가 아닌 사용자가 **회사 사용자** 페이지를 보고, 편집하고, 관리할 수 있으며, 자신을 포함한 모든 사용자의 권한을 수정하여 워크스페이스의 대시보드 사용자를 관리할 수 있습니다. 이 권한을 가진 사용자는 사용자를 삭제할 수 없습니다(관리자만 사용자를 삭제할 수 있습니다).<br><br>이는 레거시 권한 `MANAGE_DEVELOPERS_AND_PERMISSIONS`에 해당합니다.|
|워크스페이스|이메일 설정 관리|사용자가 이메일 구성 변경 사항을 저장할 수 있습니다(**설정** > **이메일 환경설정**).|
|워크스페이스|이벤트, 속성, 구매 관리|사용자가 커스텀 속성을 편집할 수 있습니다(이 기능이 없는 사용자도 커스텀 속성을 볼 수는 있음). 커스텀 이벤트의 등록정보를 편집 및 보고, **데이터 설정**에서 제품의 등록정보를 편집 및 볼 수 있습니다.|
|워크스페이스|외부 통합 관리|**기술 파트너** 아래의 모든 탭에 대한 액세스, Braze를 다른 플랫폼과 동기화하는 기능, [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/cloud_ingestion/)을 관리하는 액세스를 허용합니다.|
|워크스페이스|기능 플래그 관리|사용자가 [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags/)를 생성하거나 편집할 수 있습니다.|
|워크스페이스|미디어 라이브러리 자산 관리|사용자가 미디어 라이브러리 자산을 추가, 편집 및 삭제할 수 있습니다.|
|워크스페이스|구독 그룹 관리|사용자가 구독 그룹을 생성하고 관리할 수 있습니다.|
|워크스페이스|태그 관리|사용자가 태그(**태그 관리**)를 편집하거나 삭제할 수 있습니다. 캠페인이나 세그먼트에 태그를 추가하는 데는 이 권한이 필요하지 않습니다.|
|워크스페이스|Teams 관리|사용자가 **내부 Teams**를 관리할 수 있습니다. 이 권한의 선택 가능 여부는 Braze와의 계약에 따라 다릅니다.<br><br>이는 레거시 권한 `MANAGE_TERRITORIES`에 해당합니다.|
|워크스페이스|변환 관리|사용자가 데이터 변환을 생성하고 관리할 수 있습니다.|
|워크스페이스|캠페인, 캔버스 발송|사용자가 캠페인 및 캔버스를 편집, 아카이브 및 중지하고, 캠페인을 생성하고, 캔버스를 시작할 수 있습니다.|
|워크스페이스|청구 세부 정보 보기|사용자가 구독 및 청구 정보를 볼 수 있습니다.|
|워크스페이스|커런츠 통합 보기|사용자가 자격 증명을 제외한 커런츠 연결에 대한 모든 정보를 볼 수 있습니다. 기본적으로 "캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리, 위치, 프로모션 코드 및 환경 설정 센터 액세스" 권한이 할당된 사용자에게도 이 권한이 할당됩니다.|
|워크스페이스|PII로 표시된 커스텀 속성 보기|관리자가 아닌 사용자가 민감한 정보를 포함하고 개인 식별 정보(PII)로 표시된 커스텀 속성을 볼 수 있습니다.|
|워크스페이스|PII 보기|사용자가 대시보드 내에서 회사가 정의한 개인 식별 정보(PII) 필드를 볼 수 있습니다. 사용자는 메시지 미리보기의 **사용자로 미리보기** 탭에서도 PII 필드를 볼 수 있습니다.<br><br>일부 고객 데이터에 직접 액세스할 수 있으므로 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/)를 사용하려면 이 권한이 필요합니다. 대시보드에서 CSV를 내보내려면 이 권한과 "사용자 데이터 내보내기" 권한이 모두 필요합니다.|
|워크스페이스|PII 준수 고객 프로필 보기|사용자가 회사에서 개인 식별 정보(PII)로 정의한 필드를 포함하는 고객 프로필을 볼 수 있지만, PII 필드는 마스킹 처리됩니다.<br><br>사용자 검색 도구를 사용하려면 이 권한이 필요합니다.|
|워크스페이스|변환 보기|사용자가 [Braze 데이터 변환]({{site.baseurl}}/user_guide/data/data_transformation/overview/)을 볼 수 있습니다.|
|워크스페이스|사용 데이터 보기|사용자가 채널 성과 대시보드를 포함한 앱 사용량을 볼 수 있습니다.|
|워크스페이스|중복 사용자 병합|사용자가 중복된 고객 프로필을 병합할 수 있습니다.|
|워크스페이스|중복 사용자 미리보기|사용자가 중복된 고객 프로필을 미리 볼 수 있습니다.|
|워크스페이스|캔버스 템플릿 생성 및 편집|사용자가 캔버스 템플릿을 생성하고 편집할 수 있습니다.|
|워크스페이스|캔버스 템플릿 보기|사용자가 캔버스 템플릿을 볼 수 있습니다.|
|워크스페이스|캔버스 템플릿 아카이브|사용자가 캔버스 템플릿을 아카이브할 수 있습니다.|
|워크스페이스|커스텀 이벤트 속성정보 세분화 관리|사용자가 이벤트 속성정보의 최근성 및 빈도를 기반으로 세그먼트를 생성할 수 있습니다.|
|워크스페이스|랜딩 페이지 게시|사용자가 [랜딩 페이지]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/)를 게시할 수 있습니다.|
|워크스페이스|랜딩 페이지 초안 생성|사용자가 랜딩 페이지 초안을 생성하고 저장할 수 있습니다.|
|워크스페이스|랜딩 페이지 액세스|사용자가 **랜딩 페이지** 페이지에 액세스할 수 있습니다.|
|워크스페이스|랜딩 페이지 템플릿 생성 및 편집|사용자가 랜딩 페이지 템플릿을 생성하고 편집할 수 있습니다.|
|워크스페이스|랜딩 페이지 템플릿 보기|사용자가 랜딩 페이지 템플릿을 볼 수 있습니다.|
|워크스페이스|랜딩 페이지 템플릿 아카이브|사용자가 랜딩 페이지 템플릿을 아카이브할 수 있습니다.|
|워크스페이스|커스텀 AI 에이전트 보기|사용자가 [커스텀 AI 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/)를 볼 수 있습니다. 이 기능은 현재 베타 버전입니다.|
|워크스페이스|커스텀 AI 에이전트 생성|사용자가 커스텀 AI 에이전트를 생성할 수 있습니다. 이 기능은 현재 베타 버전입니다.|
|워크스페이스|커스텀 AI 에이전트 편집|사용자가 커스텀 AI 에이전트를 편집할 수 있습니다. 이 기능은 현재 베타 버전입니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }