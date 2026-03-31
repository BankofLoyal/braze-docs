---
nav_title: 로그 분석
article_title: 로그 분석 
page_order: 1
description: "이 문서에서는 커스텀 콘텐츠 카드에 대한 노출 횟수, 클릭, 해제를 수동으로 기록하고 클릭 시 동작을 처리하는 방법을 다룹니다."
toc_headers: "h2"

---

# 로그 분석

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## 콘텐츠 카드 분석 누락

콘텐츠 카드가 앱에 올바르게 표시되지만 분석(고유 수신자, 노출 횟수, 클릭 수 등)이 지속적으로 수신되지 않는 경우, SDK 통합 문제일 가능성이 높습니다.

- **커스텀 콘텐츠 카드 뷰(Android, iOS, Web):** 기본 Braze UI는 모든 플랫폼에서 노출 횟수와 클릭을 자동으로 기록합니다. 커스텀 콘텐츠 카드 뷰 또는 구현을 사용하는 경우, 애플리케이션 내에서 적절한 로깅 메서드를 명시적으로 호출해야 합니다. 해당 플랫폼의 [로그 분석]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)을 참조하세요. 특히 커스텀 Web 구현의 경우, Braze Web SDK가 로드되었는지 확인하고, 브라우저 콘솔에서 오류를 확인하며, 카드 데이터가 수신되고 있는지 검증하세요.
- **SDK 초기화 및 사용자 식별:** 카드를 표시하기 전에 SDK가 완전히 초기화되었는지 확인하세요. SDK가 초기화되지 않았거나, 지연 초기화 모드이거나, GDPR이 비활성화된 경우 이벤트는 대기줄에 추가되지 않고 자동으로 삭제됩니다. SDK는 익명 사용자에 대해서도 분석을 기록하지만, "고유 수신자"와 같은 대시보드 측정기준은 확인된 사용자 ID가 필요하므로 가능하면 카드가 표시되기 전에 `changeUser`를 호출하세요.