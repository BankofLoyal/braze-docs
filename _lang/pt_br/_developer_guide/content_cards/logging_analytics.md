---
nav_title: Registro de análise de dados
article_title: Registro de análise de dados 
page_order: 1
description: "Este artigo aborda como registrar manualmente impressões, cliques, dispensas e lidar com o comportamento ao clicar para seus Cartões de conteúdo personalizados."
toc_headers: "h2"

---

# Registro de análise de dados

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Análise de dados ausente nos Cartões de conteúdo

Se os Cartões de conteúdo aparecem corretamente no seu app, mas você não recebe nenhuma análise de dados de forma consistente (destinatários únicos, impressões, cliques etc.), provavelmente trata-se de um problema de integração de SDK.

- **Visualizações personalizadas de Cartões de conteúdo (Android, iOS, Web):** A interface padrão da Braze registra impressões e cliques automaticamente em todas as plataformas. Se você está usando uma visualização ou implementação personalizada de Cartões de conteúdo, é necessário chamar os métodos de registro apropriados explicitamente dentro do seu aplicativo. Consulte [Registro de análise de dados]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) para a sua plataforma. Para implementações Web personalizadas especificamente, verifique se o SDK Web da Braze está carregado, confira o console do navegador em busca de erros e confirme que os dados dos cartões estão sendo recebidos.
- **Inicialização do SDK e identificação do usuário:** Certifique-se de que o SDK esteja totalmente inicializado antes de exibir os cartões. Os eventos são descartados silenciosamente (não enfileirados) se o SDK não estiver inicializado, estiver em modo de inicialização com postergação ou desabilitado por GDPR. O SDK registra análise de dados para usuários anônimos, mas métricas do dashboard como "destinatários únicos" exigem uma identidade de usuário resolvida, então chame `changeUser` antes de exibir os cartões sempre que possível.