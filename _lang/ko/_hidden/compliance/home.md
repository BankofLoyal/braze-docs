---
nav_title: 규정 준수 설명서
article_title: 규정 준수 설명서
page_order: 1
permalink: /compliance_documentation/
toc_headers: h2
noindex: true
---

# 규정 준수 설명서

_개정 날짜: 2026년 3월 30일_

## 규정 준수 설명서에 포함된 내용은 무엇인가요?

아래의 규정 준수 설명서는 귀하가 구매한 제품, 채널, 기능, 기능성 또는 서비스에 적용되는 특정 조건을 명시합니다:

- 고객이 타사 제공자의 제품, 웹사이트, 애플리케이션 또는 서비스와 상호 작용하거나 통합하거나 액세스할 수 있도록 하는 Braze 서비스 기능의 경우, 규정 준수 설명서에는 해당 기능 사용에 적용되는 타사 제공자 조건이 포함되어 있습니다.
- Braze 제품, 채널, 기능, 기능성 또는 서비스 사용을 위해 Braze 고객이 준수해야 하는 일반 산업 관행 및 표준.

## 규정 준수 설명서 업데이트

[Braze의 GitHub 리포지토리](https://github.com/braze-inc/braze-docs)를 통해 설명서(규정 준수 설명서 포함) 업데이트를 구독하여 받아볼 수 있습니다.

## 특정 채널, 통합 및 기능에 대한 규정 준수 설명서

아래는 해당 규정 준수 설명서가 적용되는 제품, 채널, 기능, 기능성 및 서비스 목록입니다. 여러 제품을 사용하는 경우 관련된 모든 규정 준수 설명서가 적용됩니다.

### 일반 조건

계약에 따른 고객의 의무를 제한하지 않으며, 의심의 여지를 없애기 위해, 고객은 아래 나열된 채널 및 기능의 사용과 관련하여 필요한 모든 권리, 동의 및 승인을 획득하고 법적으로 적절한 개인정보 보호 고지를 제공하며, 법적으로 요구되는 모든 동의 및 승인을 획득할 전적인 책임이 있습니다.

## 채널 및 기능

1. [모바일 메시지 채널](#mobile-messages-channel)
2. [웹훅 채널](#webhooks-channel)
3. [WhatsApp 채널 규정 준수 설명서](#hatsapp-channel-compliance-documentation)
4. [LINE 채널 규정 준수 설명서](#line-channel-compliance-documentation)
5. [Shopify 통합 규정 준수 설명서](#shopify-integration-compliance-documentation)
6. [오디언스 동기화 규정 준수 설명서](#audience-sync-compliance-documentation)
7. [메시지 아카이빙 및 필드 수준 암호화 규정 준수 설명서](#message-archiving-and-field-level-encryption-compliance-documentation)
8. [에이전트 콘솔 규정 준수 설명서](#agent-console-compliance-documentation)
9. [KakaoTalk 채널 규정 준수 설명서](#kakaotalk-channel-compliance-documentation)

## 1. 모바일 메시지 채널 {#mobile-messages-channel}

다음 추가 조건은 고객의 모바일 메시지 채널 사용과 관련하여 적용됩니다:

### 정의

**"수집자"**, **"통신사"** 또는 **"모바일 메시지 중개자"**란 (i) 모바일 메시지 제공자와 통신사 간에 모바일 메시지를 전송하거나, (ii) 무선 서비스 제공자(예: T-Mobile, AT\&T 등)이거나, (iii) 모바일 메시지 제공자로부터 최종 사용자에게 RCS 메시지 전송에 관여하는 타사 중개자를 의미합니다.

**"SMS/MMS 제공자" 또는 "모바일 메시지 제공자"**란 [www.braze.com/subprocessors](http://www.braze.com/subprocessors)에 명시된 바와 같이 SMS, MMS 및/또는 RCS 메시지 전송에 사용되는 Braze 하위 처리자를 의미합니다.

**"SMS/MMS 메시지"** 또는 **"모바일 메시지"**란 SMS, MMS 및/또는 RCS 메시지를 의미합니다.

### 적용 가능한 산업 표준 및 모범 사례

모바일 메시지를 발송할 때, 고객은 모바일 메시지 제공자의 해당 허용 사용 및 메시징 정책, 해당 산업 표준 및 가이드라인, 그리고 해당되는 경우 고객이 모바일 메시지를 발송하려는 국가의 산업 코드 및 해당 모바일 메시지 중개자 가이드라인을 준수해야 하며, 이에 대한 자세한 내용은 Braze의 [허용 사용 정책](https://www.braze.com/company/legal/aup/)에 명시되어 있습니다.

모바일 메시지 중개자를 포함하여 모바일 메시지 발송에 관여하는 타사는 해당 조건 또는 관련 법률을 위반하여 발송된 모바일 메시지에 대해 수수료 또는 벌금을 부과할 수 있습니다. 고객은 해당 수수료 및 벌금이 고객 또는 Braze에 부과되는지 여부에 관계없이, 고객의 타사 조건 위반으로 인해 발생하는 수수료 및 벌금을 지불할 책임이 있습니다.

### 하위 처리자

Braze는 [www.braze.com/subprocessors](https://www.braze.com/subprocessors/)의 하위 처리자 목록에 포함된 모든 모바일 메시지 제공자를 사용할 수 있습니다.

위 내용에도 불구하고, 고객이 "자체 SMS 커넥터(BYO SMS Connector)" 모델을 사용하여 모바일 메시지를 발송하는 경우, 발송에 관여하는 모바일 메시지 제공자는 Braze의 하위 처리자가 아닌 타사 제공자(계약에 정의된 바와 같이)로 간주되며, 아래의 면책 조항이 해당 타사 제공자에 적용됩니다.

### 웹훅 사용 예외 조건

2024년 12월 9일 이후에 메시지 크레딧을 구독한 고객(주문서 발효일 기준)에게 적용됩니다: 웹훅 채널 규정 준수 설명서에 명시된 제한 사항은 타사 제공자 플랫폼을 통해 모바일 메시지를 발송하기 위한 웹훅 사용에는 적용되지 않습니다.

### 자체 SMS 커넥터(BYO SMS Connector)

고객은 "BYO SMS Connector" 모델을 통해 타사 제공자를 사용하여 Braze에서 모바일 메시지를 발송할 수 있습니다. 위 내용에도 불구하고, 고객은 BYO SMS Connector 모델을 사용하여 미국 및 캐나다로 모바일 메시지를 발송해서는 안 됩니다.

### 면책 조항

Braze는 모바일 메시지의 발송 또는 처리에 관여하는 타사 제공자 또는 모바일 메시지 중개자와 관련하여, 시스템 용량, 메시지 처리량 또는 최종 사용자 기기로의 실제 전달과 관련된 책임을 포함하여 모든 진술, 보증, 책임 및 배상 의무를 부인합니다.

## 2. 웹훅 채널 {#webhooks-channel}

다음 추가 조건은 고객의 웹훅 채널 사용과 관련하여 적용됩니다:

### 웹훅 채널 사용 조건

해당 채널 규정 준수 설명서에서 달리 허용하지 않는 한, (a) 고객은 Braze가 동일한 결과를 달성하기 위한 네이티브 기능을 제공하는 경우 웹훅을 사용해서는 안 되며, (b) 고객은 Braze가 Braze 서비스를 통해 해당 메시지를 발송하기 위한 네이티브 메커니즘을 제공하는 범위 내에서 타사 제공자 플랫폼을 통한 메시지 발송을 트리거하기 위해 웹훅을 사용해서는 안 됩니다.

Braze가 고객의 현재 구독 기간 중에 Braze 서비스에서 새로운 또는 업데이트된 메커니즘을 일반적으로 제공하는 경우, 고객은 새 메커니즘의 일반 출시일로부터 6개월 후 또는 고객의 현재 구독 기간 연도 말 중 더 늦은 시점부터 지정된 타사 플랫폼을 통한 메시지 발송을 트리거하기 위해 웹훅을 사용하는 것이 금지됩니다.

### 웹훅 채널 사용 조건의 예외

[모바일 메시지 채널](#mobile-messages-channel) 및 [WhatsApp 채널](#whatsapp-channel-compliance-documentation)을 참조하세요.

### 면책 조항

Braze는 Braze 서비스 외부에서 메시지 발송 또는 기타 동작을 트리거하기 위한 고객의 웹훅 사용과 관련된 모든 책임을 부인합니다.

## 3. WhatsApp 채널 규정 준수 설명서 {#whatsapp-channel-compliance-documentation}

다음 추가 조건은 고객의 WhatsApp 채널 사용과 관련하여 적용됩니다:

### 적용 가능한 타사 제공자 조건

고객은 Braze [WhatsApp 설정](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/overview/) 페이지에 설명된 바와 같이, WhatsApp, LLC 및 그 계열사가 요구하는 조건을 포함하여 WhatsApp 채널에 적용되는 모든 필수 조건, 조건 및 정책을 준수해야 합니다.

### 웹훅 사용 예외 조건

고객은 사람이 지원하는 채팅 사용 사례 및/또는 챗봇 사용 사례와 같은 고객 지원 목적이 아닌 한, WhatsApp 채널을 통한 메시지 발송을 트리거하기 위해 웹훅을 사용할 수 없습니다.

### 자체 WhatsApp 커넥터(BYO WhatsApp Connector)

고객은 "BYO WhatsApp Connector"를 사용하여 자신의 직접 WhatsApp 계정을 Braze에 연결할 수 있습니다.

## 4. LINE 채널 규정 준수 설명서 {#line-channel-compliance-documentation}

다음 추가 조건은 고객의 LINE 채널 사용과 관련하여 적용됩니다:

### 필수 조건

LINE 채널을 통해 메시지를 발송하려면, 고객은 LINE의 자체 재량에 따라 승인 및 부여되는 LINE 인증 공식 계정을 획득해야 합니다. 고객은 LINE 채널 사용을 위한 Braze 메시지 크레딧을 구매하기 전에 LINE으로부터 인증 공식 계정을 획득해야 합니다.

### 적용 가능한 타사 제공자 조건

LINE 채널을 사용함으로써, 고객은 LY Corporation 및 그 계열사(통칭 "LINE")가 요구하는 모든 조건 및 정책을 준수하고 이에 구속되는 것에 동의합니다. 여기에는 LINE 공식 계정 이용약관, 공식 계정 API 이용약관, LINE 공식 계정 가이드라인, LINE 사용자 데이터 정책, 그리고 이에 참조로 포함된 모든 정책, 조건, 가이드라인 및 설명서(통칭 "LINE 조건")가 포함되며 이에 국한되지 않습니다. 명확히 하자면, 고객은 다음에 대해 책임이 있습니다: (i) LINE과 관련하여 처리되는 모든 데이터가 해당되는 LINE 조건에 따라 처리되도록 보장하는 것, (ii) LINE 채널과 관련하여 LINE 서비스 사용에 대해 LINE에 지불해야 하는 모든 수수료 또는 비용.

LINE 조건에 상반되는 내용이 있더라도, 고객은 LINE 서비스 사용에 대해 일차적으로 책임을 집니다.


## 5. Shopify 통합 규정 준수 설명서 {#shopify-integration-compliance-documentation}

다음 추가 조건은 Braze 서비스와 관련하여 고객의 Shopify 통합 사용("**Shopify 통합**")에 적용됩니다:

고객은 Shopify 통합 사용에 적용되는 Shopify Inc. 또는 그 계열사("**Shopify**")의 해당 조건, 정책, 가이드라인 및 설명서를 준수하고 이에 구속되는 것에 동의합니다.

고객은 Shopify가 언제든지 자체 재량에 따라 다음을 수행할 수 있음을 인정합니다: (i) Braze가 고객의 Shopify 통합 액세스를 비활성화하거나 차단하도록 요구하는 것, 또는 (ii) 고객의 Shopify 통합 액세스 제공을 중단, 일시 중지 또는 종료하는 것. Braze는 Shopify가 고객 또는 Braze 서비스 전반을 통해 Shopify 통합에 대한 액세스 제공을 중단하는 것과 관련하여 어떠한 책임도 지지 않습니다.

## 6. 오디언스 동기화 규정 준수 설명서 {audience-sync-compliance-documentation}

다음 추가 조건은 고객의 오디언스 동기화 사용에 적용됩니다.

### 적용 가능한 타사 제공자 조건

고객은 오디언스 동기화 통합과 관련하여 고객이 활용하는 타사 제공자의 해당 조건, 정책, 가이드라인 및 설명서를 준수하고 이에 구속되는 것에 동의합니다.

고객은 타사 제공자가 자사 서비스와 관련하여 사용되는 모든 데이터, 광고 또는 콘텐츠를 검토, 심사 및/또는 제거할 수 있음을 인정합니다.

## 7. 메시지 아카이빙 및 필드 수준 암호화 규정 준수 설명서 {#message-archiving-and-field-level-encryption-compliance-documentation}

### 면책 조항
고객은 메시지 아카이빙 및/또는 필드 수준 암호화(각각 "**기능**")의 사용이 Braze 서비스를 통해 발송되는 메시지의 발송 속도에 영향을 미칠 수 있음을 인정합니다. Braze는 이러한 영향에 대해 책임을 지지 않으며, 고객이 해당 기능을 사용하는 경우 발송 속도 약속은 적용되지 않습니다. 해당 기능은 고객의 규정 준수 노력을 지원하기 위해 사용될 수 있지만, 고객은 Braze가 해당 기능의 사용 자체가 고객의 규정 준수 의무를 충족하는지 여부에 대해 어떠한 진술이나 보증도 하지 않으며, 이와 관련된 모든 책임을 부인함을 인정합니다.

## 8. 에이전트 콘솔 규정 준수 설명서 {#agent-console-compliance-documentation}

### 하위 처리자 또는 타사 제공자로서의 LLM 제공자

고객이 Braze 서비스의 Braze Auto 옵션을 통해 Braze가 제공하는 대규모 언어 모델("Braze 제공 LLM")과의 통합을 사용하는 경우, 해당 Braze 제공 LLM의 제공자는 고객과 Braze 간의 데이터 처리 부록(DPA) 조건에 따라 Braze 하위 처리자로서 활동합니다.

고객이 Braze AI 기능과 통합하기 위해 자체 API 키를 가져오는 경우, 고객 자체 LLM 구독의 제공자는 고객과 Braze 간의 계약에 정의된 바와 같이 타사 제공자로 간주됩니다.

## 9. KakaoTalk 채널 규정 준수 설명서 {#kakaotalk-channel-compliance-documentation}

다음 추가 조건은 고객의 KakaoTalk 채널 사용과 관련하여 적용됩니다:

### 필수 조건

KakaoTalk 채널을 통해 메시지를 발송하려면, 고객은 먼저 KakaoTalk 계정을 획득하고 고객에게 KakaoTalk 기능을 제공하는 데 관여하는 타사 제공자("KakaoTalk 타사 제공자")와 KakaoTalk 서비스 계약을 체결해야 합니다. KakaoTalk 계정은 해당 KakaoTalk 타사 제공자의 자체 재량에 따라 승인 및 부여됩니다.

### 적용 가능한 타사 제공자 조건

KakaoTalk 채널을 사용함으로써, 고객은 해당되는 KakaoTalk 및 KakaoTalk 타사 제공자의 조건 및 정책(통칭 "KakaoTalk 조건")을 준수하고 이에 구속되며 KakaoTalk 서비스 사용에 대해 책임을 지는 것에 동의합니다. 명확히 하자면, 고객은 KakaoTalk 채널과 관련하여 해당 KakaoTalk 타사 제공자 서비스 사용에 대해 KakaoTalk 및/또는 KakaoTalk 타사 제공자에게 지불해야 하는 모든 수수료 또는 비용에 대해 책임이 있습니다.

{% multi_lang_include braze_legal/english_language_governance.md %}