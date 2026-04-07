---
nav_title: Rastreamento de cliques do KakaoTalk
article_title: Rastreamento de cliques do KakaoTalk
page_order: 3
description: "Esta página aborda como ativar o rastreamento de cliques nas suas mensagens do KakaoTalk, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais."
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# Rastreamento de cliques do KakaoTalk

> Esta página aborda como ativar o rastreamento de cliques nas suas mensagens do KakaoTalk, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais.

Quando o rastreamento de cliques do KakaoTalk está ativado, a Braze encurta automaticamente suas URLs, adiciona mecanismos de rastreamento e registra cliques em tempo real. Esses dados permitem que você crie estratégias de segmentação e redirecionamento mais direcionadas, como segmentar usuários com base no comportamento de cliques e disparar mensagens em resposta a cliques específicos.

O rastreamento de cliques do KakaoTalk pode ser usado para mensagens de texto, imagem e itens de lista. Ele oferece suporte a links dentro de botões e ações de comportamento ao clicar em imagens. Você também pode personalizar URLs usando Liquid e domínios personalizados.

## Como funciona

Você pode gerenciar as configurações de rastreamento de cliques do KakaoTalk na seção **Opções de link** do criador de mensagens. Quando ativado, as URLs serão encurtadas usando o domínio padrão da Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de inscrições, e personalizadas para o usuário.

Qualquer URL que comece com `http://` ou `https://` será encurtada. Você pode ter até 25 URLs em uma mensagem. URLs encurtadas que contêm personalização com Liquid (como rastreamento em nível de usuário ou parâmetros UTM) serão válidas por dois meses.

## Configurar o rastreamento de cliques

### Mensagens de texto

Para configurar o rastreamento de cliques para uma mensagem de texto:

1. Redija uma mensagem de **Texto** e adicione uma URL ao campo de texto ou botão.
2. Na seção **Opções de link** do criador de mensagens, confirme que **Rastreamento de cliques** está marcado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

![Criador de mensagens de texto do KakaoTalk mostrando a seção Opções de link com Rastreamento de cliques marcado.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### Mensagens de imagem

Para configurar o rastreamento de cliques para uma mensagem de imagem:

1. Redija uma mensagem de **Imagem** e defina o comportamento ao clicar para abrir uma URL.
2. Insira uma URL no campo de URL.
3. Na seção **Opções de link** do criador de mensagens, confirme que **Rastreamento de cliques** está marcado.

### Mensagens de itens de lista

Para configurar o rastreamento de cliques para uma mensagem de itens de lista:

1. Redija uma mensagem de **Itens de lista** e adicione uma URL ao campo **URL do site** para qualquer item.
2. Na seção **Opções de link** do criador de mensagens, confirme que **Rastreamento de cliques** está marcado.

## Domínios personalizados

O rastreamento de cliques do KakaoTalk permite que você use seu próprio domínio para personalizar a aparência das suas URLs encurtadas, ajudando a transmitir uma imagem de marca consistente. Para saber mais, consulte [Domínios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Personalização com Liquid em URLs

Você pode construir sua URL dinamicamente diretamente no criador de mensagens da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).

As URLs podem ser geradas dinamicamente por meio do uso de qualquer tag de personalização Liquid compatível.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Você também pode encurtar variáveis Liquid definidas de forma personalizada, conforme mostrado no exemplo a seguir:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

A Braze encurta URLs que são renderizadas por Liquid, incluindo aquelas presentes em propriedades de disparo via API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar uma URL válida, a Braze encurtará e rastreará essa URL antes de enviar a mensagem do KakaoTalk.

## Testes

Antes de lançar sua campanha ou Canvas, a prática recomendada é visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Teste** para visualizar e enviar uma mensagem do KakaoTalk para grupos de teste de conteúdo ou para um usuário individual.

A prévia será atualizada com a personalização relevante e a URL encurtada.

{% alert important %}
Se um rascunho for criado dentro de um Canvas ativo, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho do Canvas é ativado.
{% endalert %}

## Relatórios

A tabela de performance do KakaoTalk inclui a coluna **Total de cliques** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. Para mais informações sobre métricas do KakaoTalk, consulte [Relatórios do KakaoTalk]({{site.baseurl}}/kakaotalk_reporting/).

Os dados de cliques serão reportados automaticamente no dashboard de análise de dados.

## Redirecionar usuários

Você pode redirecionar usuários que clicaram em uma URL em uma mensagem do KakaoTalk usando os seguintes filtros de segmentação e gatilhos:

- Gatilhos baseados em ação
    - Interagir com Campanha
    - Interagir com etapa

- Filtros de segmentação
    - Clicou/Abriu Campanha
    - Clicou/Abriu Campanha ou Canvas com tag
    - Clicou/Abriu etapa

## Perguntas frequentes

### Os links que recebo ao enviar um teste são URLs reais?

Sim, URLs reais serão geradas ao enviar um teste. No entanto, a URL exata enviada em uma campanha lançada pode ser diferente daquela enviada em um envio de teste.

### Posso adicionar parâmetros UTM a uma URL antes de ela ser encurtada?

Sim, tanto parâmetros estáticos quanto dinâmicos podem ser adicionados.

### Por quanto tempo as URLs encurtadas permanecem válidas?

URLs personalizadas são válidas por dois meses a partir do momento do registro da URL.

### O SDK da Braze precisa estar instalado para encurtar URLs?

Não, o rastreamento de cliques funciona sem nenhuma integração de SDK.

### É possível saber quais usuários individuais estão clicando em uma URL?

Sim. Quando o rastreamento de cliques está ativado, você pode redirecionar usuários que clicaram em URLs usando os [filtros de redirecionamento do KakaoTalk](#retargeting-users).

### O rastreamento de cliques funciona com deep links ou links universais?

O rastreamento de cliques se aplica a URLs da web. Para deep links, você pode definir um deep link diretamente como o tipo de ação ao clicar para botões no KakaoTalk — esses não passam pelo encurtamento de URL ou rastreamento de cliques. Se você preferir usar links universais de provedores como Branch ou Appsflyer, eles podem ser encurtados, mas a Braze não consegue solucionar problemas que possam surgir (como quebra de atribuição ou falha no redirecionamento).