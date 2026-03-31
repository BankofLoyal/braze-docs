---
nav_title: 이메일 템플릿 만들기
article_title: 이메일 템플릿 만들기
page_order: 0
description: "이 참조 문서에서는 이메일 템플릿을 만들고, 커스텀하고, 관리하는 방법에 대해 설명합니다."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# 이메일 템플릿 만들기

> Braze 대시보드에는 눈길을 사로잡는 맞춤형 이메일을 작성하고 나중에 캠페인에서 사용할 수 있도록 저장할 수 있는 이메일 템플릿 편집기가 있습니다. 나만의 [HTML 이메일 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/)을 업로드할 수도 있습니다.

## 1단계: 이메일 템플릿 편집기로 이동하기

**템플릿** > **이메일 템플릿**으로 이동합니다.

## 2단계: 편집 환경 선택 

편집 환경에 맞게 **드래그 앤 드롭 편집기** 또는 **HTML 편집기** 중에서 선택합니다. 

그런 다음 미리 디자인된 Braze 템플릿에서 선택하거나, 새 템플릿을 만들거나, 기존 템플릿(일반 또는 [모바일 반응형]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates))을 편집할 수 있습니다.

![드래그 앤 드롭 편집기 또는 HTML 편집기를 선택하거나 Braze 템플릿에서 선택할 수 있는 옵션이 포함된 회사의 봄 세일용 이메일 템플릿입니다.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
기존 커스텀 HTML 템플릿은 드래그 앤 드롭 편집기를 사용하여 다시 만들어야 합니다.
{% endalert %}

## 3단계: 템플릿 커스텀하기

편집기 환경을 선택한 후에는 이메일 템플릿을 창의적으로 커스텀할 수 있습니다. HTML 편집기에서 HTML을 사용하여 브랜딩을 만들고 에뮬레이션하거나 드래그 앤 드롭 편집기에서 다양한 [크리에이티브 세부 정보]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details)를 포함할 수 있습니다.

### 탈퇴 링크 포함

이메일 템플릿을 디자인할 때 탈퇴 링크를 포함하지 않으면 모든 마케팅 이메일에 법적으로 요구되는 탈퇴 링크를 이메일에 추가하라는 메시지가 Braze에서 표시됩니다. Liquid 태그 {% raw %}``${email_footer}``{% endraw %}를 사용하거나 템플릿에서 [바닥글을 커스텀]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer)하여 이메일 하단에 이 탈퇴 링크를 바닥글로 추가할 수 있습니다.

## 4단계: 이메일 오류 확인

이메일 오류는 메시지 워크플로의 **작성** 탭에 표시됩니다. 오류가 있으면 다음 단계로 진행할 수 없습니다. "경고"는 모범 사례를 따르는 데 도움이 되는 알림을 표시합니다. 비즈니스에 따라 이를 무시할 수도 있습니다.

![예시 이메일의 오류 및 경고 목록입니다.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

다음은 편집기에서 확인하는 오류 목록입니다:

- 잘못된 Liquid 구문
- [400kb를 초과하는 이메일 본문; 본문은 102kb 미만으로 유지하는 것을 강력히 권장합니다]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- 탈퇴 링크가 없는 템플릿
- **본문** 또는 **제목**이 비어 있는 이메일
- 탈퇴 링크가 없는 이메일

## 5단계: 메시지 미리보기 및 테스트

템플릿 작성을 완료한 후에는 발송하기 전에 테스트할 수 있습니다.

개요 화면 하단에서 **미리보기 및 테스트**를 선택합니다. 여기에서 이메일이 고객의 받은편지함에 어떻게 표시되는지 미리 볼 수 있습니다. **사용자로 미리보기**를 선택하면 임의의 사용자로 이메일을 미리 보거나 특정 사용자를 선택하거나 커스텀 사용자를 만들 수 있습니다. 이를 통해 연결된 콘텐츠 및 개인화 호출이 정상적으로 작동하는지 테스트할 수 있습니다. 

그런 다음 **미리보기 링크 복사**를 선택하여 임의의 사용자에게 이메일이 어떻게 보이는지 확인할 수 있는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 이 링크는 7일 후에 다시 생성해야 합니다.

또한 데스크톱, 모바일 및 일반 텍스트 보기 간에 전환하여 메시지가 다양한 컨텍스트에서 어떻게 표시되는지 확인할 수 있습니다.

{% alert tip %}
다크 모드 사용자에게 이메일이 어떻게 보이는지 궁금하신가요? **미리보기 및 테스트** 섹션에 있는 **다크 모드 미리보기** 토글을 선택하세요(드래그 앤 드롭 편집기에서만 사용 가능).
{% endalert %}

최종 확인이 준비되면 **테스트 전송**을 선택하고 본인 또는 콘텐츠 테스터 그룹에게 테스트 메시지를 전송하여 다양한 기기와 이메일 클라이언트에서 이메일이 제대로 표시되는지 확인합니다.

![테스트를 위해 전송할 이메일 미리보기 예시입니다.]({% image_buster /assets/img_archive/newEmailTest.png %})

템플릿에 문제가 있거나 변경하고 싶은 사항이 있으면 **이메일 편집**을 선택하여 편집기로 돌아갑니다.

## 6단계: 템플릿 저장

**템플릿 저장**을 선택하여 템플릿을 저장하세요. 이제 이 템플릿을 원하는 캠페인이나 캔버스 구성요소에 사용할 준비가 되었습니다. 템플릿에 액세스하려면 템플릿을 만든 편집 환경을 선택한 다음 사용 가능한 템플릿 목록에서 해당 템플릿을 선택합니다.

{% alert note %}
기존 템플릿을 편집하는 경우 해당 변경 사항은 해당 템플릿의 이전 버전을 사용하여 만든 캠페인에 반영되지 않습니다.
{% endalert %}

### 템플릿 관리하기

**템플릿** > **이메일 템플릿**에서 이메일 템플릿을 확인할 수 있으며, 상태, 유형 또는 태그별로 필터링하거나 이름으로 검색할 수 있습니다. 이러한 템플릿을 보려면 **캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리, 위치, 프로모션 코드 및 환경설정 센터 액세스** 권한(또는 **이메일 템플릿 보기**와 같은 세분화된 권한)이 필요합니다. 자세한 내용은 [사용자 권한]({{site.baseurl}}/user_guide/administrative/access_braze/user_permissions/)을 참조하세요.

이메일 템플릿을 더 많이 만들면 이메일 템플릿을 [복제]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates)하고 [아카이브]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates)할 수 있습니다. [템플릿 및 미디어]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)에서 자세히 알아보세요.

### API 캠페인에서 템플릿 사용

API 캠페인에 이메일을 사용하려면 Braze에서 생성한 이메일 템플릿 하단에 있는 `email_template_id`가 필요합니다.

![이메일 템플릿 하단에 있는 API 식별자입니다.]({% image_buster /assets/img/email_templates/template5.png %})

### 이메일 템플릿에 댓글 달기

드래그 앤 드롭 편집기에서 이메일 템플릿에 대해 공동 작업하고 댓글을 달 수 있습니다. 

1. 댓글을 달고 싶은 이메일 본문의 콘텐츠 블록 또는 행을 선택합니다.
2. <i class="fas fa-comment"></i> 댓글 아이콘을 선택합니다.
3. 사이드바에 댓글을 입력한 다음 **제출**을 선택합니다.
4. 댓글을 입력한 후 **완료**를 선택합니다.
5. **템플릿 저장**을 선택하여 댓글을 저장합니다.

템플릿이 저장되면 사용자는 처리되지 않은 댓글 위에 아이콘을 볼 수 있습니다. **해결**을 선택하여 이러한 댓글을 해결합니다.

!["좋아 보인다"라는 이메일 템플릿 댓글.]({% image_buster /assets/img/email_templates/template_comment.png %})

이메일 템플릿에 대해 자주 묻는 질문에 대한 답변은 [템플릿 FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/)를 확인하세요.