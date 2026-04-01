---
nav_title: Criar uma mensagem do KakaoTalk
article_title: "Criar uma mensagem do KakaoTalk"
description: "Este artigo de referência descreve como criar uma mensagem do KakaoTalk."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# Criar uma mensagem do KakaoTalk

> Use o [canal de envio de mensagens do KakaoTalk]({{site.baseurl}}/kakaotalk/) para alcançar usuários diretamente pela plataforma KakaoTalk. Crie uma experiência de usuário personalizada usando Liquid e outros conteúdos dinâmicos para construir um ambiente que promova e aprimore uma experiência rica com a sua marca.<br><br>Para configurar seu canal de envio de mensagens do KakaoTalk, consulte [Configurar o KakaoTalk]({{site.baseurl}}/kakaotalk_setup/).

## Etapa 1: Escolha onde criar sua mensagem

O KakaoTalk é compatível com campanhas e Canvas. Campanhas são mais adequadas para campanhas de mensagens individuais, enquanto canvas permitem orquestrar jornadas de usuário em múltiplas etapas e múltiplos canais.

{% tabs local %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **KakaoTalk** para uma campanha de canal único, ou **Campanha multicanal** para uma campanha com múltiplos canais.

![Painel com opções para selecionar o canal de envio de mensagens.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Você pode adicionar variantes adicionais à sua campanha, permitindo escolher diferentes tipos de mensagem e layouts. Para saber mais, consulte [Testes multivariantes e A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/).

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. Adicione uma etapa de Mensagem no criador de Canvas e selecione **KakaoTalk**.

![Seleções de canal de envio de mensagens no Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## Etapa 2: Redija sua mensagem do KakaoTalk

1. Selecione o menu suspenso **Canal do KakaoTalk**, que exibe uma lista de canais do KakaoTalk que você configurou pela página de Parceiros de Tecnologia, e selecione o canal do KakaoTalk a ser usado para enviar a mensagem.
2. Selecione o tipo de mensagem a enviar:
- Texto
- Imagem
- Item de lista
    - Estreito
    - Largo

![Seção de Variantes do KakaoTalk com três tipos de mensagens para selecionar.]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

{% tabs local %}
{% tab Text %}

Uma mensagem de texto do KakaoTalk é a forma mais simples de comunicação: uma mensagem de texto padrão.

### Especificações

| Área | Especificações |
| --- | --- |
| Conteúdo | Conteúdo de texto, incluindo emojis e personalização com Liquid |
| Capacidade de texto | Até 1.000 caracteres |
| Botões | Até 5 botões opcionais. Atualmente, só podem ser usados para abrir uma URL ao clicar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Uma mensagem de texto do KakaoTalk no criador.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Image %}

Uma imagem é uma mensagem que combina um elemento visual com texto de apoio. A Braze gerencia automaticamente o upload da imagem para os servidores do KakaoTalk.

### Especificações gerais

| Área | Especificações |
| --- | --- |
| Conteúdo | Uma imagem e texto de apoio |
| Formatos de arquivo aceitos | JPEG ou PNG |
| Largura recomendada | 500px |
| Tamanho do arquivo | Até 500kb |
| Proporção | Deve estar entre 2:1 (largo) e 3:4 (alto) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Mensagens de imagem estreita e larga possuem diferentes limites de caracteres e considerações de botões.

{% subtabs %}
{% subtab Narrow image %}

#### Imagem estreita

Uma mensagem de imagem estreita apresenta uma imagem ligeiramente mais alta e estreita, com opções mais extensas de texto e botões.

##### Especificações

| Área | Especificações |
| --- | --- |
| Conteúdo | Uma imagem e texto de apoio |
| Capacidade de texto | Até 500 caracteres |
| Botões | Até 5 botões opcionais |
| Origem da imagem | As imagens podem ser adicionadas usando a biblioteca de mídia da Braze ou uma URL direta |
| Personalização | Você pode especificar o comportamento ao clicar na imagem |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Uma mensagem estreita do KakaoTalk.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Wide image %}

#### Imagem larga

Uma mensagem de imagem larga apresenta uma imagem larga em destaque, adequada para comunicação visual de alto impacto, com texto de apoio mínimo.

##### Especificações

| Área | Especificações |
| --- | --- |
| Conteúdo | Uma imagem e texto de apoio |
| Capacidade de texto | Até 76 caracteres |
| Botões | Até 2 botões opcionais |
| Origem da imagem | As imagens podem ser adicionadas usando a biblioteca de mídia da Braze ou uma URL direta |
| Personalização | Você pode especificar o comportamento ao clicar na imagem |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Uma mensagem larga do KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Adicionar imagens

Você pode adicionar imagens pela Biblioteca de Mídia da Braze ou colando uma URL que hospede um arquivo JPEG ou PNG. Também é possível especificar o comportamento ao clicar na imagem para redirecionar os usuários que clicarem nela para uma URL específica.

A Braze gerencia automaticamente todos os requisitos de upload de imagem do KakaoTalk, o que significa que você **não precisa** fazer upload de imagens para provedores do KakaoTalk antes de enviar mensagens. Basta fazer upload das imagens e enviar a mensagem diretamente pela Braze!

![Seção com ícones selecionados para adicionar imagem estreita.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab List item %}


Uma mensagem de lista de itens do KakaoTalk é projetada para apresentar uma lista de itens de conteúdo em um formato vertical e claro.

Mensagens de item de lista consistem em um cabeçalho, uma seção de lista de itens e uma área opcional de botões.

#### Especificações

| Área | Especificações |
| --- | --- |
| Quantidade de itens | Requer pelo menos 2 ou 3 itens |
| Botões | Até 5 botões opcionais |
| Cabeçalho | Até 250 caracteres |
| Título do item | Até 25 caracteres |
| URL do site (por item) | Até 250 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Uma mensagem de item de lista do KakaoTalk.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## Etapa 3: Configure o rastreamento de cliques

Quando o rastreamento de cliques do KakaoTalk está ativado, a Braze encurta automaticamente suas URLs, adiciona mecanismos de rastreamento e registra cliques em tempo real. Esses dados permitem criar estratégias de segmentação e redirecionamento mais direcionadas, como segmentar usuários com base no comportamento de cliques e disparar mensagens em resposta a cliques específicos.

O rastreamento de cliques é compatível com mensagens de texto, imagem e item de lista. Ele suporta links em botões e ações de clique em imagens. Você também pode personalizar URLs usando Liquid e domínios personalizados.

Para ativar o rastreamento de cliques, marque **Rastreamento de cliques** na seção **Opções de link** do criador. As URLs serão encurtadas usando o domínio padrão da Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de inscrições, e personalizadas para o usuário.

Para detalhes completos sobre rastreamento de cliques, domínios personalizados, personalização com Liquid em URLs, relatórios e redirecionamento, consulte [Rastreamento de cliques do KakaoTalk]({{site.baseurl}}/kakaotalk_click_tracking/).

### Redirecionar usuários

Você pode redirecionar usuários que clicaram em uma URL em uma mensagem do KakaoTalk usando os seguintes filtros de segmentação e gatilhos:

- Gatilhos baseados em ação
    - Interagir com campanha
    - Interagir com etapa

- Filtros de segmentação
    - Clicou/Abriu campanha
    - Clicou/Abriu campanha ou Canvas com tag
    - Clicou/Abriu etapa

## Etapa 4: Visualize e teste sua mensagem do KakaoTalk

A prévia da mensagem é atualizada automaticamente conforme você redige sua mensagem do KakaoTalk. Quando estiver pronto para testar, acesse a guia **Teste** para enviar uma mensagem de teste para grupos de teste de conteúdo ou usuários individuais, ou para visualizar a mensagem como um usuário existente ou personalizado diretamente na Braze.

Após selecionar seus usuários teste, selecione **Enviar teste**. Uma notificação indicará os resultados do seu envio de teste. Para CJ OliveNetworks, você receberá uma resposta "C100". Se aparecer um erro diferente, consulte a [documentação de usuário do CJ KakaoTalk](https://developers.kakao.com/docs/latest/en/index).

![Janela de prévia de uma mensagem do KakaoTalk.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Para visualizar e enviar uma mensagem de teste para um usuário existente, você precisa ter permissões de "Visualizar IPI". Você pode visualizar e enviar uma mensagem de teste para um usuário personalizado sem essas permissões.
{% endalert %}

Para revisar os resultados de um envio ou solucionar problemas, acesse **Configurações** > **Registro de atividade de mensagens**. Para saber mais, consulte [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

## Etapa 5: Construa o restante da sua campanha ou Canvas

Consulte as seções a seguir para detalhes sobre como usar melhor nossas ferramentas para criar mensagens do KakaoTalk.

### Escolha o agendamento de entrega ou gatilho

Mensagens do KakaoTalk podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para saber mais sobre opções de agendamento e gatilho, consulte [Agendar sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) ou [Tipos de agendamento de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types) (para seu Canvas).

Você pode especificar controles de entrega, como permitir que os usuários se tornem elegíveis novamente para receber a campanha, ou ativar regras de limite de frequência. Para entrega baseada em ação, você também pode definir a duração da campanha e o horário de silêncio.

### Escolha os usuários a direcionar

Direcione usuários selecionando segmentos ou filtros para refinar seu público. Por enquanto, o KakaoTalk só pode enviar mensagens para amigos do canal. Recomendamos definir um atributo personalizado para indicar amigos do canal, para que você possa segmentar seus usuários adequadamente e evitar o envio de mensagens do KakaoTalk para usuários que não podem recebê-las.

### Escolha eventos de conversão

A Braze permite rastrear com que frequência os usuários realizam ações específicas, eventos de conversão, após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão é contabilizada se o usuário realizar a ação especificada.

Eventos de conversão ajudam a medir o sucesso da sua campanha. Por exemplo, se você está tentando incentivar os usuários a usar seu app, defina o evento de conversão como **Inicia sessão**.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo e pense em como deseja medir o sucesso da sua campanha.

## Etapa 6: Revise e implante

Depois de terminar de construir a última parte da sua campanha ou Canvas, revise os detalhes, teste e envie!