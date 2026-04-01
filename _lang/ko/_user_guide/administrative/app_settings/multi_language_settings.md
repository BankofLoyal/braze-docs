---
nav_title: 현지화 설정
article_title: 현지화 설정
alias: "/multi_language_support/"
page_order: 5.5
description: "이 문서에서는 Braze 대시보드의 다국어 설정에 대한 개요와 메시징에서 로캘을 사용하는 방법에 대해 설명합니다."
---

# 현지화 설정

> 다국어 기능을 사용하면 단일 메시지 내에서 [번역 태그]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)를 사용하여 다양한 언어와 위치의 사용자를 타겟팅할 수 있습니다.

## 필수 조건

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## 로캘 추가

1. **설정** > **현지화 설정**으로 이동합니다.
2. **로캘 추가**를 선택한 다음, **기본값 로캘** 또는 **커스텀 속성**을 선택합니다.

!["로캘 추가" 드롭다운에는 기본값 로캘 또는 커스텀 속성을 선택할 수 있는 옵션이 있습니다.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}

{: start="3"}
3. 로캘의 이름을 입력합니다.
4. [접근성을 위한 언어를 선택합니다]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/#language-settings-and-accessibility). 이 설정을 통해 스크린 리더와 같은 보조 기술이 텍스트를 올바르게 읽을 수 있습니다.
5. 선택한 로캘 옵션에 대한 해당 사용자 속성을 선택합니다. 로캘을 설정할 때 기본값 사용자 속성 또는 커스텀 속성에서 언어를 선택할 수 있습니다. 둘 다에서 선택할 수는 없습니다.

{% tabs %}
{% tab Default locale %}

**기본값 로캘**의 경우, 드롭다운을 사용하여 추가할 언어를 선택하고, 선택 사항으로 언어와 연관된 국가를 선택합니다.

![언어 및 국가를 지정하기 위한 "로캘 추가 - 기본값 언어 및 국가"라는 창.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

**커스텀 속성**의 경우, 드롭다운을 사용하여 관련 커스텀 속성을 선택하고 텍스트 필드에 값을 입력합니다.

![커스텀 속성과 값을 지정하기 위한 "로캘 추가 - 커스텀 속성"이라는 창.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. **로캘 추가**를 선택합니다.

메시지에서 이러한 로캘을 사용하는 방법은 [다국어 메시지]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)를 참조하세요.

## 고려 사항

- 단일 로캘에서 최대 두 개의 커스텀 속성을 선택하거나 최대 두 개의 기본값 사용자 속성 언어를 선택할 수 있습니다. 두 경우 모두 두 번째 속성은 선택 사항입니다.
- CSV 파일에서 번역된 값을 편집할 때, 파일의 기본값을 수정하지 않도록 주의하세요.
- 업로드한 파일의 로캘 키는 다국어 설정의 키와 일치해야 합니다.

### 고객지원 및 우선순위

- 사용자가 커스텀 속성으로 정의된 로캘과 기본값 사용자 속성으로 정의된 로캘 모두에 일치하는 경우, 커스텀 속성 로캘이 우선시됩니다.
- 커스텀 속성은 정확히 일치하는 텍스트(문자열) 값을 지원합니다.
- 커스텀 속성이 삭제되거나 유형이 변경되면 사용자는 더 이상 해당 로캘에 속할 수 없으며, 속한 로캘의 우선순위 목록에서 다음 순위로 내려가거나 기본 마케팅 번역을 받게 됩니다.
- 로캘이 유효하지 않은 경우(커스텀 속성이 변경되거나 삭제된 경우) 오류가 **다국어 지원** 페이지에 표시됩니다.

## 자주 묻는 질문

#### 로캘을 몇 개까지 추가할 수 있나요?

로캘을 최대 200개까지 추가할 수 있습니다.

#### Braze에서 번역 파일은 어디에 저장되나요?

번역 파일은 캠페인 수준에서 저장되므로 각 메시지 배리언트에 번역이 업로드되어 있어야 합니다. 번역은 콘텐츠 블록에도 저장할 수 있습니다. 블록이 메시지에 추가되면 해당 번역이 자동으로 포함됩니다.

#### 로캘 이름이 특정 패턴이나 형식을 따라야 하나요?

아니요. 원하는 이름 지정 규칙을 사용할 수 있습니다. 로캘 이름은 편집기에서 로캘을 선택할 때 사용되며, 번역 ID와 함께 다운로드하는 파일의 헤더에 표시됩니다.