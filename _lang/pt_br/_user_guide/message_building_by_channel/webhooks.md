---
nav_title: Webhooks
article_title: Webhooks
page_order: 8
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Webhooks são uma maneira comum para aplicativos se comunicarem — compartilhando dados em tempo real. Hoje em dia, raramente temos um aplicativo autônomo que consiga fazer tudo. Na maioria das vezes, você trabalha com vários aplicativos ou sistemas diferentes, cada um especializado em realizar determinadas tarefas, e todos eles precisam ser capazes de se comunicar entre si. É aí que os webhooks entram. <br><br> Um webhook é uma mensagem automatizada de um sistema para outro quando determinados critérios são atendidos. Na Braze, esse critério geralmente é o disparo de um evento personalizado. <br><br>Essencialmente, um webhook é um método baseado em eventos que permite que dois sistemas separados tomem ações eficazes com base nos dados transmitidos em tempo real. Essa mensagem contém instruções que informam ao sistema receptor quando e como realizar uma tarefa específica. Por isso, os webhooks podem oferecer um acesso mais dinâmico e flexível aos dados e à funcionalidade programática, além de permitir que você configure jornadas de clientes que otimizam processos. <br><br>**A disponibilidade dos webhooks depende do seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.**"
description: "Esta landing page reúne tudo sobre webhooks. Aqui, você encontra artigos sobre como criar webhooks, criar modelos de webhooks e webhooks Braze-to-Braze."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Artigos da seção"
guide_featured_list:
- name: Criação de um webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Criação de um modelo de webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Webhooks Braze-to-Braze
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Relatórios
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Solução de problemas de solicitações de webhook
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Casos de uso

Webhooks são uma excelente maneira de conectar seus sistemas — afinal, é assim que os aplicativos se comunicam. Veja alguns cenários gerais em que webhooks podem ser particularmente úteis:

- Enviar dados para a Braze e receber dados da Braze
- Enviar mensagens para seus clientes por canais não suportados diretamente pela Braze
- Fazer chamadas para as APIs da Braze

Alguns casos de uso mais específicos incluem:

- Se um usuário cancelar a inscrição de e-mail, você pode usar um webhook para atualizar seu banco de dados de análise de dados ou CRM com essa mesma informação, garantindo uma visão completa do comportamento desse usuário.
- Envie [mensagens transacionais]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) para usuários no Facebook Messenger ou LINE.
- Envie mala direta para os clientes em resposta à atividade deles no app e na web, usando webhooks para se comunicar com serviços de terceiros como o [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Se um jogador atingir um determinado nível ou acumular certa quantidade de pontos, use webhooks e sua configuração de API existente para enviar um upgrade de personagem ou moedas diretamente para a conta dele. Se você enviar o webhook como parte de uma campanha de mensagens em vários canais, pode enviar um push ou outra mensagem para informar o jogador sobre a recompensa ao mesmo tempo.
- Se você é uma companhia aérea, pode usar webhooks e sua configuração de API existente para creditar a conta de um cliente com um desconto após ele ter reservado um determinado número de voos.
- Receitas infinitas do tipo "If This Then That" ([IFTTT](https://ifttt.com/about)) — por exemplo, se um cliente entrar no app via e-mail, esse endereço pode ser configurado automaticamente no Salesforce.

## Anatomia de um webhook

Um webhook é composto pelas seguintes partes:

| Parte do webhook | Descrição |
| --- | --- |
| [Método HTTP](#methods) | Assim como as APIs, webhooks precisam de métodos de solicitação. Eles são atribuídos à URL que o webhook aciona e informam ao endpoint o que fazer com as informações fornecidas. Existem quatro métodos HTTP que você pode especificar: POST, GET, PUT e DELETE. |
| URL HTTP | O endereço URL do seu endpoint de webhook. O endpoint é o local para onde você enviará as informações capturadas no webhook. |
| Corpo da solicitação | Essa parte do webhook contém as informações que você está comunicando ao endpoint. O corpo da solicitação pode ser pares de chave-valor JSON ou texto bruto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Exemplo de webhook com um método HTTP, URL HTTP e corpo da solicitação.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Métodos HTTP {#methods}

A tabela a seguir descreve os quatro métodos HTTP diferentes que você pode especificar no seu webhook.

| Método HTTP | Descrição |
| ----------- | ----------- |
| POST | Este método grava novas informações no servidor receptor. Um exemplo comum do método POST em uma aplicação do mundo real é um [formulário de contato](https://www.braze.com/company/contact) em um site. Qualquer informação que você inserir no formulário se torna parte do corpo da solicitação e é enviada a um receptor. Este é o método mais comum para enviar dados.
| GET | Este método recupera informações existentes, em vez de gravar novas. Por definição, uma solicitação GET não suporta corpo de solicitação. Este é o método mais comum para solicitar dados de um servidor. Por exemplo, considere o [endpoint `/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Se você fizesse uma solicitação GET, ela retornaria uma lista dos seus segmentos.
| PUT | Este método atualiza as informações no endpoint, substituindo qualquer informação existente pelo conteúdo do corpo da solicitação. 
| DELETE | Este método exclui o recurso na URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhooks na Braze

Na Braze, você pode criar um webhook como uma campanha de webhook, campanha de API ou componente do Canvas.

{% tabs %}
{% tab Webhook Campaign %}

1. No dashboard da Braze, acesse **Campanhas**.
2. Clique em **Criar campanha** e selecione **Webhook**.

Consulte [Criar um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para saber mais.

{% endtab %}
{% tab API Campaign %}

1. No dashboard da Braze, acesse **Campanhas**.
2. Clique em **Criar campanha** e selecione **Campanha de API**.
3. Clique em **Adicionar mensagens** e selecione **Webhook**.
4. Formate sua chamada de API para incluir um [objeto webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Consulte [Criar um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para saber mais.

{% endtab %}
{% tab Canvas Component %}

1. No seu Canvas, crie um novo componente.
2. Na seção **Mensagem** do seu componente, selecione **Webhook**.

Consulte [Criar um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para saber mais.

{% endtab %}
{% endtabs %}

## Tratamento de erros e limite de taxa de webhooks

Quando a Braze recebe uma resposta de erro de uma chamada de webhook, o comportamento de envio desse webhook é ajustado automaticamente com base nestes cabeçalhos de resposta:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Esses cabeçalhos nos ajudam a interpretar os limites de taxa e ajustar a velocidade de envio para evitar mais erros. Também implementamos uma estratégia de backoff exponencial para novas tentativas, o que ajuda a reduzir o risco de sobrecarregar seus servidores ao espaçar as tentativas ao longo do tempo.

Se detectarmos que a maioria das solicitações de webhook para um host específico está falhando, adiaremos temporariamente todas as tentativas de envio para esse host. Em seguida, retomaremos o envio após um período de espera definido, permitindo que seu sistema se recupere.