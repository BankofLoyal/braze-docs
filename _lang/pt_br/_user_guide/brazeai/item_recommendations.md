---
nav_title: Recomendações de itens
article_title: Recomendações de itens na Braze
page_order: 10
search_rank: 1
description: "Aprenda tudo sobre motores de recomendação de itens na Braze."
---

# Recomendações de itens

> Aprimore suas recomendações com a Braze criando um motor de recomendação que pode sugerir itens e conteúdos que seus usuários realmente desejam. Desde a personalização de experiências com IA até a criação de seus próprios mecanismos com Liquid ou Conteúdo conectado, você encontrará tudo o que precisa para fazer com que cada recomendação conte.

## Pré-requisitos

Antes de criar ou usar recomendações de itens na Braze, você precisará [criar pelo menos um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)&#8212;apenas itens desse catálogo serão recomendados aos usuários.

## Tipos e casos de uso

### IA Personalizada {#ai}

Como parte do recurso [recomendações de itens de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/), as recomendações personalizadas de IA aproveitam o deep learning para prever quais itens seus usuários têm mais probabilidade de se interessar a seguir, com base no que demonstraram interesse no passado. Esse método fornece um sistema de recomendação dinâmico e personalizado que se adapta ao comportamento do usuário.

As recomendações personalizadas de IA usam os últimos 6 meses de dados de interação com itens, como compras ou eventos personalizados, para criar o modelo de recomendação. Para usuários sem dados suficientes para uma lista personalizada, os itens mais populares servem como fallback, para que seus usuários ainda recebam sugestões relevantes.

Com as recomendações de itens de IA, você também pode filtrar ainda mais os itens disponíveis com
[seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/). No entanto, as seleções com Liquid não podem ser usadas em recomendações de IA, então lembre-se disso ao criar suas seleções de catálogo.

{% alert tip %}
As recomendações personalizadas por IA funcionam melhor com centenas ou milhares de itens e, normalmente, com pelo menos 30.000 usuários com dados de compra ou interação. Esse é apenas um guia aproximado e pode variar. Os outros tipos de recomendação podem funcionar com menos dados.
{% endalert %}

#### Casos de uso

Com base nos dados de interação sendo rastreados, os casos de uso para este modelo podem incluir:

{% tabs local %}
{% tab Most likely to purchase next %}
Preveja e recomende os itens que um usuário provavelmente comprará em seguida, com base em eventos de compra ou eventos personalizados relacionados a compras. Por exemplo:

- Um site de viagens poderia sugerir pacotes de férias, voos ou estadias em hotéis com base no histórico de navegação e nas reservas anteriores de um usuário, antecipando seu próximo destino de viagem e facilitando o planejamento da viagem.
- Uma plataforma de streaming pode analisar os hábitos de visualização para recomendar programas ou filmes que um usuário provavelmente assistirá em seguida, mantendo-o engajado e reduzindo as taxas de churn.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um método para rastrear compras, seja um objeto de compra ou um evento personalizado
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **IA Personalizada**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha como você rastreia atualmente os eventos de compra e a propriedade de evento correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations/).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Item mais popular {#most-popular}

O modelo de recomendação "Mais popular" apresenta itens com os quais os usuários mais interagem.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações de:

{% tabs local %}
{% tab most popular %}
Incentive os usuários a explorar itens populares em seu catálogo com base nas compras. Para garantir que apenas conteúdo relevante seja exibido, recomendamos filtrar com uma seleção. Por exemplo, um serviço de entrega de comida poderia destacar os pratos ou restaurantes mais bem avaliados na área de um usuário, com base na popularidade dos pedidos na plataforma, incentivando a experimentação e a descoberta.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um objeto de compra ou qualquer evento personalizado
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes. Por exemplo, o serviço de entrega de comida pode ter uma seleção para filtrar pelo local do restaurante ou tipo de prato.
5. Escolha como você rastreia eventos atualmente e a propriedade de evento correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab most liked %}
Incentive os usuários a explorar itens que eles curtiram recentemente ou itens que são popularmente apreciados, com base em um evento personalizado para curtidas. Por exemplo, um app de streaming de música poderia criar playlists personalizadas ou sugerir lançamentos de novos álbuns com base nos gêneros ou artistas que um usuário curtiu no passado, aumentando o engajamento do usuário e o tempo gasto no app.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para curtidas
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para curtidas na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab most viewed %}
Destaque os itens que ganharam atenção na sua base de usuários por meio de visualizações para incentivar o engajamento ou as compras. Por exemplo, um site imobiliário poderia exibir os imóveis mais visualizados na área de pesquisa de um usuário para destacar propriedades que estão atraindo muita atenção, indicando potencialmente bons negócios ou localizações desejáveis.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para visualizações
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para visualizações na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
Exiba itens que são adicionados aos carrinhos por muitos outros compradores, dando aos usuários um vislumbre das tendências atuais entre suas ofertas.

Por exemplo, um varejista de moda poderia promover roupas e acessórios que estão em alta com base em adições populares aos carrinhos de outros clientes. Em seguida, eles podem criar uma seção dinâmica "Trending Now" na página inicial e no app para dispositivos móveis, que é atualizada em tempo real para incentivar os compradores a comprar antes que os itens se esgotem.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para adicionar ao carrinho
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha **Custom Event** e selecione na lista o evento personalizado para adicionar ao carrinho.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Item mais recente {#most-recent}

O modelo de recomendação "Mais recente" apresenta itens com os quais os usuários interagiram mais recentemente. Use esse modelo para reduzir o churn, incentivando usuários inativos a se engajarem novamente com conteúdo relevante.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações de:

{% tabs local %}
{% tab Recently clicked %}
Incentive os usuários a revisitar os itens em que clicaram recentemente, com base em um evento personalizado para cliques. Por exemplo, um varejista de moda on-line poderia criar uma recomendação para enviar e-mails de acompanhamento ou notificações por push com roupas pelas quais um usuário demonstrou interesse ao clicar nelas, incentivando-o a revisitar o item e fazer uma compra.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para cliques
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para cliques na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
Incentive os usuários a explorar itens que eles curtiram recentemente ou itens que são popularmente apreciados, com base em um evento personalizado para curtidas. Por exemplo, um app de streaming de música poderia criar playlists personalizadas ou sugerir lançamentos de novos álbuns com base nos gêneros ou artistas que um usuário curtiu no passado, aumentando o engajamento do usuário e o tempo gasto no app.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para curtidas
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para curtidas na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
Promova itens com os quais os usuários interagiram recentemente, incluindo visualizações, cliques ou compras. Essa abordagem mantém suas recomendações atualizadas e alinhadas com os interesses mais recentes do usuário. Por exemplo:

- **Educação:** Uma plataforma de educação on-line pode incentivar os usuários que assistiram recentemente a um vídeo educativo, mas não se inscreveram em um curso, a conferir cursos semelhantes ou assuntos de interesse para manter o usuário engajado e motivado a começar a aprender.
- **Fitness:** Um app de fitness pode sugerir exercícios ou desafios semelhantes aos que o usuário concluiu recentemente ou com os quais interagiu, mantendo sua rotina de exercícios variada e envolvente.
- **Varejista de artigos para casa:** Depois que um cliente adquire uma ferramenta elétrica, um varejista de reforma residencial pode recomendar acessórios relacionados ou equipamentos de segurança com base na compra recente, aprimorando a experiência e a segurança do usuário.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um objeto de compra ou qualquer evento personalizado para uma interação de engajamento
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para cliques na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}

{% tab Recently added %}
Lembre os usuários do interesse deles em itens que adicionaram recentemente ao carrinho, mas que ainda não compraram. Por exemplo, um varejista on-line poderia enviar lembretes ou oferecer descontos por tempo limitado nos itens do carrinho, incentivando os usuários a concluir suas compras antes que as ofertas expirem.
{% details Requirements %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para adicionar ao carrinho
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha **Custom Event** e selecione na lista o evento personalizado para adicionar ao carrinho.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Item em alta {#trending}

O modelo de recomendação "Em alta" apresenta itens que mostraram o maior impulso positivo nas interações recentes dos usuários. Calculamos isso usando uma análise ponderada de aproximadamente 10 semanas de histórico de eventos, com o maior peso aplicado às aproximadamente 2 semanas mais recentes. Para evitar que pequenas flutuações afetem a qualidade da recomendação, aplicamos um limite de atividade e técnicas de suavização estatística.

Ao contrário do modelo "Mais popular", que apresenta itens com interação consistentemente alta, esse modelo apresenta itens que tiveram um aumento nas interações. Você pode usá-lo para recomendar produtos que estão em ascensão e ganhando força no momento.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações de:

{% tabs local %}
{% tab Trending purchased %}
Destaque os itens que seus usuários compraram recentemente com maior frequência. Por exemplo, uma empresa de e-commerce poderia recomendar itens sazonais que os usuários estão começando a estocar durante os preparativos para a próxima estação. 

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um método para rastrear compras (seja um objeto de compra ou um evento personalizado)
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Defina o **Tipo** como **Em alta**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha um evento de compra ou um evento personalizado que rastreia compras, juntamente com a propriedade correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
Destaque itens que seus usuários curtiram recentemente com maior frequência. Por exemplo, um app de música poderia apresentar artistas promissores que tiveram um aumento recente no número de curtidas dos usuários.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para rastreamento de curtidas
{% enddetails %}

{% details Setting it up %}
1. Crie uma [recomendação de item de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Defina o **Tipo** como **Em alta**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação apenas para itens relevantes.
5. Escolha seu evento personalizado para rastreamento de curtidas, juntamente com a propriedade correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Baseado em seleções {#selections-based}

[As seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) são grupos específicos de dados de catálogo. Ao usar uma seleção, você está basicamente configurando filtros personalizados com base em colunas específicas do seu catálogo. Isso pode incluir filtros por marca, tamanho, local, data de adição e muito mais. Isso dá a você controle sobre o que está recomendando, permitindo definir os critérios que os itens devem atender para serem mostrados aos usuários.

Os três tipos anteriores envolvem a configuração e o treinamento de um modelo de recomendação na Braze. Embora também seja possível usar seleções nesses modelos, você também pode realizar alguns casos de uso de recomendação apenas com seleções de catálogo e personalização Liquid.

{% alert note %}
Se você usar seleções, o campo de ordenação e quaisquer limites não serão usados com as recomendações de itens de IA. Isso significa que, se você criar uma seleção com um campo de ordenação específico e limitar o número de itens retornados, essas restrições não serão usadas quando as recomendações de itens de IA forem processadas.
{% endalert %}

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações de:

{% tabs local %}
{% tab New items %}
Esse cenário não depende diretamente das ações do usuário, mas sim dos dados do catálogo. É possível filtrar novos itens com base na data de adição ao catálogo e promovê-los por meio de campanhas direcionadas ou canvas sem a necessidade de treinar um modelo de recomendação.

Por exemplo, uma plataforma de e-commerce de tecnologia poderia alertar os entusiastas da tecnologia sobre os últimos gadgets ou as próximas pré-encomendas, usando filtros para direcionar itens que foram adicionados recentemente ao catálogo.

{% details Requirements %}
- Catálogo de itens relevantes com um campo para data de adição
{% enddetails %}

{% details Setting it up %}
1. Crie uma seleção com base em seu catálogo. Certifique-se de que seu catálogo tenha um campo de tempo (campo com um **Tipo de dados** definido como **Tempo**) que corresponda à data em que o item foi adicionado.
2. (Opcional) Adicione filtros, se desejar.
3. Certifique-se de que a opção **Randomize Sort Order** esteja desativada.
4. Em **Sort Field**, selecione o campo de data de adição.
5. Defina **Sort Order** como descendente.
6. [Use a seleção no envio de mensagens]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Random items %}
Para uma experiência diversificada do usuário, a recomendação de itens aleatórios pode introduzir variedade e potencialmente despertar o interesse em áreas menos visitadas do catálogo. Esse método não requer modelos ou eventos específicos, mas usa uma seleção de catálogo para garantir que os itens sejam exibidos aleatoriamente.

Por exemplo, uma livraria on-line poderia oferecer o recurso "Surpreenda-me", recomendando um livro aleatório com base nas compras anteriores ou nos hábitos de navegação do usuário, incentivando a exploração fora dos gêneros de leitura habituais.

{% details Requirements %}
- Catálogo de itens relevantes
- Seleção com a opção **Randomize Sort Order** ativada
{% enddetails %}

{% details Setting it up %}
1. [Crie uma seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection) com base em seu catálogo.
2. (Opcional) Adicione filtros, se desejar.
3. Ative a opção **Randomize Sort Order**.
4. [Use a seleção no envio de mensagens]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Baseado em regras {#rules-based}

Um mecanismo de [recomendação baseado em regras]({{site.baseurl}}/rules_based_recommendations/) usa dados de usuários e informações de produtos para sugerir itens relevantes aos usuários dentro das mensagens. Ele usa o Liquid e os catálogos da Braze ou o Conteúdo conectado para personalizar dinamicamente o conteúdo com base no comportamento e nos atributos do usuário.

As recomendações baseadas em regras são fundamentadas em uma lógica fixa que você deve definir manualmente. Isso significa que suas recomendações não se ajustarão ao histórico de compras e gostos individuais de um usuário, a menos que você atualize a lógica; portanto, esse método é mais indicado para recomendações que não precisam de atualizações frequentes.

#### Casos de uso

Com base nos dados de interação sendo rastreados, os casos de uso para este modelo podem incluir:

- **Lembretes de reabastecimento:** Enviar lembretes de reabastecimento para itens com um ciclo de uso previsível, como vitaminas mensais ou mantimentos semanais, com base na data da última compra.
- **Compradores de primeira viagem:** Recomendar kits iniciais ou ofertas introdutórias aos compradores de primeira viagem para incentivar uma segunda compra.
Programas de fidelidade: Destaque os produtos que maximizariam os pontos de fidelidade ou as recompensas de um cliente com base em seu saldo de pontos atual.
- **Conteúdo educacional:** Sugerir novos cursos ou conteúdos com base nos tópicos de materiais consumidos ou comprados anteriormente.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Perguntas frequentes {#faq}

### O que faz com que os itens "Mais populares" sejam misturados às recomendações de outros modelos?

Quando nosso mecanismo de recomendação faz a curadoria de uma lista para você, ele primeiro prioriza as seleções personalizadas com base no modelo específico que você escolheu, como "Mais recente" ou "IA Personalizada". Se esse modelo não conseguir preencher a lista completa de 30 recomendações por qualquer motivo, alguns dos itens mais populares entre todos os usuários serão adicionados para garantir que cada usuário sempre tenha um conjunto completo de recomendações.

Isso acontece em algumas condições específicas:

- O modelo encontra menos de 30 itens que correspondem aos seus critérios.
- Os itens relevantes não estão mais disponíveis ou em estoque.
- Os itens não atendem aos critérios de seleção atuais, talvez devido a uma alteração no estoque ou nas preferências do usuário.

Observe que as recomendações operam de forma independente e não têm conhecimento do que os outros modelos estão recomendando. Isso significa que cada seção pode ter itens duplicados já exibidos em outras seções de recomendações de IA no mesmo e-mail.

### Como evitar itens duplicados em várias seções de recomendação?

Como cada recomendação opera de forma independente, o mesmo item pode aparecer em mais de uma seção da mesma mensagem. Para remover duplicatas, use Liquid para rastrear quais IDs de itens você já exibiu e ignorá-los nas seções seguintes.

### As recomendações existentes treinam semanalmente após a atualização para Item Recommendations Pro?

Sim, mas apenas após a próxima atualização programada. As recomendações existentes não mudam para treinamento semanal e previsão diária imediatamente após a atualização para Item Recommendations Pro. No entanto, elas adotarão o novo cronograma automaticamente no próximo ciclo de retreinamento. Por exemplo, se uma recomendação foi treinada pela última vez em 1º de fevereiro e está programada para retreinamento a cada 30 dias, ela adotará o novo cronograma semanal após sua próxima atualização em 2 de março.

### Como posso fazer com que todas as recomendações que duram vários dias expirem de uma vez?

Se você quiser expirar todas as recomendações de vários dias em uma data específica (para que todas essas recomendações ativas recebam novas previsões de uma vez), entre em contato com o suporte da Braze ou seu gerente de sucesso do cliente para obter assistência. Os especialistas em IA da Braze realizam isso manualmente para garantir a máxima performance do modelo.