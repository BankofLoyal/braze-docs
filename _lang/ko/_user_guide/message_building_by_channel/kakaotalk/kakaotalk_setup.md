---
nav_title: KakaoTalk 설정
article_title: "KakaoTalk 설정"
description: "이 참조 문서에서는 사용자 설정, 사용자 ID 조정, 테스트 사용자 생성 등 KakaoTalk 채널을 설정하는 방법을 설명합니다."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# KakaoTalk 설정

> 이 문서에서는 사용자 설정, 사용자 ID 조정, KakaoTalk 테스트 사용자 생성 등 Braze에서 [KakaoTalk 메시징 채널]({{site.baseurl}}/kakaotalk/)을 설정하는 방법을 다룹니다.

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| 지원되는 KakaoTalk 파트너 계정 | KakaoTalk 메시징 채널을 사용하려면 지원되는 KakaoTalk 파트너인 [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) 또는 Infobip의 계정이 필요합니다. |
| KakaoTalk 비즈니스 채널 | Braze를 통해 KakaoTalk 메시지를 발송하려면 KakaoTalk 계정이 KakaoTalk 비즈니스 채널이어야 합니다. 계정을 생성하면 기본 상태는 일반입니다. 비즈니스 채널로 전환하려면 사업자 인증을 완료하고 관련 서류를 제출해야 합니다. |
| KakaoTalk 발신 키 | 유효한 KakaoTalk 발신 키가 필요합니다. |
| 연락처 전화번호 | KakaoTalk 채널 관리자의 연락처 전화번호가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### KakaoTalk 계정 유형

| 계정 유형 | 설명 |
| --- | --- |
| 일반 채널 | 모든 조직이 설정할 수 있는 표준 KakaoTalk 채널입니다. KakaoTalk을 통한 단체 메시지 발송 및 1:1 채팅이 가능합니다. |
| [비즈니스 채널](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | 신청 및 인증 절차가 필요한 사업자 인증 KakaoTalk 채널입니다. 다음과 같은 향상된 기능을 제공합니다. {::nomarkdown}<ul><li>인증 배지</li><li>추천 채널로 노출</li><li>비즈니스 메시징 지원</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 비즈니스 채널 신청

신청을 시작하기 전에 다음 사업자 서류를 준비하세요:
- 사업자등록증
- 대표자 신분증
- 재직증명서
- 업종별 인허가증

{% alert important %}
KakaoTalk 채널의 정보(채널명, 프로필 이미지 등)는 공식 제출 서류의 정보와 정확히 일치해야 합니다.
{% endalert %}

서류를 준비한 후 다음 단계를 따르세요:

1. [KakaoTalk 채널 관리자센터](https://center-pf.kakao.com/)에 로그인합니다.
2. 업그레이드하려는 기존 KakaoTalk 채널을 선택합니다.
3. **관리(Management)** 섹션에서 **비즈니스 채널 신청(Business Channel Application)** 옵션을 선택합니다.
4. **신청(Apply)** 또는 **신청 버튼(Request button)**을 선택하여 절차를 시작합니다.
5. 필요한 정보를 입력합니다.
6. 검토 결과 알림을 기다립니다.

## KakaoTalk 통합

### 1단계: KakaoTalk 채널을 Braze에 연결

1. **파트너 통합** > **기술 파트너**로 이동하여 KakaoTalk 제공업체를 선택합니다.
2. 제공업체에 필요한 자격 증명을 수집한 후(아래 참조) **기술 파트너** 페이지에 입력하고 저장합니다.
3. 새로 저장한 자격 증명을 사용하여 발송합니다.

#### CJ OliveNetworks

[Comm.One 대시보드](https://ums.cjmplace.com/)로 이동하여 다음 정보를 수집합니다.

| 필드 | 위치 |
| --- | --- |
| **Comm.One 로그인 아이디(Login ID)** | 프로필을 선택합니다. |
| **발신프로필 키(Sender Key)** | **템플릿 관리(Template Management)** > **발신프로필 관리(Sender Profile Management)**로 이동합니다. |
| **카카오톡 채널 프로필명(Channel name)** | Comm.One 대시보드에서 **템플릿 관리(Template Management)** > **발신프로필 관리(Sender Profile Management)**로 이동합니다. |
| **연락처(Sender number)** | {::nomarkdown}<ol><li><b>계정 관리(Account Management)</b>로 이동하여 메뉴 아이콘을 선택한 후 <b>자세히보기(View Details)</b>를 선택합니다.</li><li><b>업체 상세 정보(Business Detailed Information)</b> > <b>기업정보(Company Information)</b>로 이동합니다.</li></ul>{:/} |
| **자격 증명(ID) & 비밀번호(Password)** | **연락처(사업자 등록번호)**와 동일한 위치로 이동한 후 **API** > **브랜드 메시지(Brand Message)**로 이동합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![로그인 ID가 가려진 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![발신 키가 가려진 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![채널명이 가려진 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![자격 증명 ID와 비밀번호가 가려진 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

![CJ OliveNetworks의 기술 파트너 페이지 필드.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Braze KakaoTalk 채널의 자격 증명.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
단일 공통 ID에 매핑된 채널만 등록할 수 있습니다.
{% endalert %}

#### Infobip

Infobip 대시보드로 이동하여 다음 정보를 수집합니다.

| 필드 | 위치 |
| --- | --- |
| **API Base URL** | **Developer Tools** > **API Keys**를 선택합니다. |
| **API 키** | **Developer Tools** > **API Keys**를 선택합니다. |
| **발신자명 / 발신 키** | **Channels and Numbers** > **Channels**를 선택한 후 **Senders** 탭을 선택합니다. |
| **발신 프로필 UUID** | Infobip에서 직접 제공합니다. 이 정보가 없는 경우 Infobip에 문의하세요. |
| **채널명** | Infobip에서 직접 제공합니다. 이 정보가 없는 경우 Infobip에 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 고객 프로필 설정

KakaoTalk을 통해 메시지를 발송하려면 고객 프로필에 전화번호가 있어야 합니다. 전화번호는 고객 프로필에 제공된 형식 그대로 표시됩니다. 현재 SMS나 WhatsApp과 달리 KakaoTalk은 표준 전화번호 필드를 사용합니다(E.164 형식으로 변환된 번호가 아님).

![편집되지 않은 형식의 전화번호가 있는 테스트 사용자의 고객 프로필.]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### 전화번호 가져오기

[CSV 업로드 또는 API를 사용]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/)하여 전화번호를 가져오고 사용자를 생성합니다.