---
nav_title: Criar um Banner
article_title: Criar um Banner
page_order: 1
description: "Este artigo de referência cobre como criar, redigir, configurar e enviar Banners usando campanhas e canvas da Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Criar um Banner

> Aprenda como criar Banners ao construir campanhas e canvas na Braze. Para saber mais informações gerais, veja [Sobre Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Pré-requisitos

Antes de lançar seu Banner, sua equipe de desenvolvimento deve [configurar os placements no seu app ou site]({{site.baseurl}}/developer_guide/banners/creating_placements/). Você ainda pode rascunhar sua campanha de Banner enquanto isso, mas não poderá lançar a campanha até que os placements estejam configurados.

## Criar uma mensagem de Banner

{% multi_lang_include banners/creating_placements.md section="user" %}

### Etapa 2: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canvas? Campanhas são melhores para campanhas de mensagens únicas e direcionadas, enquanto canvas são melhores para jornadas de usuários em múltiplas etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário. As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o Construtor de Relatórios, você pode filtrar pelas tags relevantes.
5. Selecione o placement que você criou anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e layout diferentes para cada uma. Para saber mais sobre variantes, consulte [Testes multivariantes e Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Escolha uma data e hora de início para sua campanha de Banner. Por padrão, Banners duram indefinidamente. Você pode mudar isso selecionando **Hora de Término** e especificando uma data e hora de término.

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes adicionais. Você pode então selecionar **Copiar da Variante** no menu suspenso **Adicionar Variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador de Canvas.
2. Após configurar seu Canvas, adicione uma etapa de Mensagem no construtor de Canvas. Dê um nome claro e significativo à sua etapa.
3. Selecione **Banner** como seu canal de envio de mensagens.
4. Selecione um placement para o Banner.
5. Defina a prioridade para o Banner. A [prioridade do Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determina a ordem em que os Banners são exibidos se compartilharem o mesmo placement.
6. Defina uma expiração para o Banner. Isso pode ser após um período de tempo depois que a etapa estiver disponível ou em uma data e hora específicas.

{% endtab %}
{% endtabs %}

### Etapa 3: Redija um Banner {#compose-a-banner}

Para redigir seu Banner, você pode escolher:

- Começar com um modelo em branco
- Usar um modelo de banner da Braze
- Selecionar um modelo de banner salvo

![Opção para escolher um Banner em branco ou um modelo.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Etapa 3.1: Estilize o Banner

Você pode arrastar e soltar blocos e linhas na área da canva para começar a construir sua mensagem.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para personalizar as propriedades de fundo, configurações de borda e mais da sua mensagem, selecione **Estilos**. Se você quiser personalizar o estilo apenas de um bloco ou linha específica, selecione-o para fazer alterações.

![Painel de estilo do criador de Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Etapa 3.2: Defina o comportamento ao clicar (opcional)

Quando um usuário clica em um link no Banner, você pode escolher direcioná-lo para uma área mais profunda do seu app ou redirecioná-lo para outra página da web. Além disso, você pode escolher [registrar um atributo personalizado ou evento]({{site.baseurl}}/developer_guide/analytics/), que atualiza o perfil do usuário com dados personalizados quando ele clica no Banner.

{% alert important %}
{::nomarkdown}
O comportamento ao clicar pode ser substituído se um elemento específico (como um botão, link ou imagem do Banner) tiver seu próprio comportamento ao clicar. Por exemplo, dados os seguintes comportamentos ao clicar:<br><ul><li>Um Banner tem um comportamento ao clicar que redireciona para a página inicial de um site.</li><li>Uma imagem no Banner tem um comportamento ao clicar que redireciona para a página de produto de um site.</li></ul>Se um usuário clicar na imagem, ele será redirecionado para a página do produto. No entanto, clicar na área ao redor do Banner redireciona para a página inicial.
{:/}
{% endalert %}

#### Etapa 3.3: Adicione propriedades personalizadas (opcional) {#custom-properties}

Você pode adicionar propriedades personalizadas a um Banner para anexar metadados estruturados, como strings ou objetos JSON. Essas propriedades não afetam como o Banner é exibido, mas podem ser [acessadas por meio do SDK da Braze]({{site.baseurl}}/developer_guide/banners/placements/) para modificar o comportamento ou a aparência do seu app. Por exemplo, você poderia:

- Enviar metadados para análise de dados de terceiros ou integrações.
- Usar metadados como um `timestamp` ou objeto JSON para disparar lógica condicional.
- Controlar o comportamento de um banner com base em metadados incluídos, como `ratio` ou `format`.

Para adicionar uma propriedade personalizada, selecione **Configurações** > **Propriedades** > **Adicionar propriedade**.

![A página de propriedades mostrando a opção de adicionar a primeira propriedade personalizada a uma campanha de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propriedade que você gostaria de adicionar, preencha o seguinte:

| Campo | Descrição | Exemplo |
|-------|-------------|---------|
| Tipo de propriedade | O tipo de dado da propriedade. Os tipos suportados incluem string, booleano, número, timestamp, URL de imagem e objeto JSON. | String |
| Chave da propriedade | O identificador único da propriedade. Essa chave é usada no SDK para acessar a propriedade. | `color` |
| Valor | O valor atribuído à propriedade. Deve corresponder ao tipo de propriedade selecionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Quando terminar, selecione **Concluir**.

![A página de propriedades com uma propriedade de string com uma chave de cor e valor de #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Etapa 4: Crie o restante da sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

#### Definir prioridade do Banner (opcional)

A [prioridade do Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determina a ordem em que os Banners são exibidos se compartilharem o mesmo placement. Para definir a prioridade manualmente:

1. Selecione **Definir prioridade exata**.
2. Arraste e solte as campanhas para ordená-las com a prioridade correta.
3. Selecione **Aplicar Ordenação**.

{% alert tip %}
Se você tiver várias campanhas de Banner usando o mesmo ID de placement, recomendamos usar o organizador de prioridade por arrastar e soltar para definir a prioridade exata.
{% endalert %}

#### Escolha seu público

1. Em **Públicos-alvo**, escolha segmentos ou filtros para restringir seu público. Você recebe automaticamente uma prévia da população aproximada do segmento. A associação exata ao segmento é calculada antes que a mensagem seja enviada.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. Em **Atribuir Conversões**, acompanhe com que frequência os usuários realizam ações específicas após receber uma campanha, definindo eventos de conversão com um período de até 30 dias para contar a ação como uma conversão.

{% multi_lang_include target_audiences.md %}

#### Selecionar eventos de conversão

A Braze permite que você acompanhe [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), ou seja, com que frequência os usuários realizam ações específicas após receber uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão é contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar [testes multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), e mais, consulte a etapa [Construa seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação de Canvas.

{% endtab %}
{% endtabs %}

### Etapa 5: Teste sua mensagem (opcional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Etapa 6: Revisão e implementação

Depois de terminar de construir sua campanha ou Canvas, revise os detalhes, [teste]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) e envie quando estiver pronto.