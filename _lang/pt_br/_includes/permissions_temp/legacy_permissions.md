{% alert important %}
A Braze está introduzindo [permissões granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), uma forma mais flexível de gerenciar o acesso dos usuários. Consulte [Migrando para permissões granulares]({{site.baseurl}}/granular_permissions_migration/) para saber mais sobre o processo de migração, incluindo como as permissões legadas são mapeadas para permissões granulares.
{% endalert %}

## Criando um conjunto de permissões

Use conjuntos de permissões para agrupar permissões relacionadas a áreas ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acesse **Configurações** > **Configurações de Permissão**, depois selecione **Criar conjunto de permissões**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nome|Permissões|
|-----------|----------------|
|Desenvolvedores|"Acessar Console de Desenvolvimento"|
|Profissionais de marketing|"Acessar Campanhas, Canvas, Cartões, Feature Flags, Segmentos, Biblioteca de Mídia e Centrais de Preferências" <br> "Gerenciar ativos da biblioteca de mídia"|
|Gerenciamento de Usuários|"Gerenciar Usuários do Dashboard" <br> "Gerenciar equipes"|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Criando uma função

As funções permitem mais estrutura ao agrupar suas permissões personalizadas individuais com os controles de acesso do espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nome da Função | Espaço de trabalho | Permissões  
----------- | ----------- | ---------
| Profissional de Marketing - Marcas de Moda | {::nomarkdown}[DEV] Marca de Moda, [QA] Marca de Moda, [PROD] Marca de Moda {:/} | "Acessar Campanhas, Canvas, Cartões, Feature Flags, Segmentos, Biblioteca de Mídia e Central de Preferências"<br>"Gerenciar ativos da biblioteca de mídia" |
| Profissional de Marketing - Marcas de Cuidados com a Pele | {::nomarkdown}[DEV] Marca de Cuidados com a Pele, [QA] Marca de Cuidados com a Pele, [PROD] Marca de Cuidados com a Pele {:/} | "Acessar Campanhas, Canvas, Cartões, Feature Flags, Segmentos, Biblioteca de Mídia e Centrais de Preferências" <br>"Gerenciar ativos da biblioteca de mídia" |
| Gerenciamento de Usuários - Todas as Marcas | {::nomarkdown}[DEV] Marca de Moda, [QA] Marca de Moda, [PROD] Marca de Moda, [DEV] Marca de Cuidados com a Pele, [QA] Marca de Cuidados com a Pele, [PROD] Marca de Cuidados com a Pele {:/} | "Gerenciar Usuários do Dashboard"<br>"Gerenciar equipes" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e funções diferem das Equipes?

{% multi_lang_include permissions.md content="Differences" %}

### Considerações para adicionar permissões de usuário às Equipes

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard da Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho, ou adicioná-los a uma Equipe. O botão **Salvar/Atualizar Usuários** pode ficar desativado se as permissões do usuário forem idênticas às que ele já possui no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma Equipe se todos os usuários possuem as mesmas permissões que todo o espaço de trabalho.

Para adicionar um usuário a uma Equipe com sucesso, mantendo as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados

Usuários limitados têm permissões específicas que permitem gerenciar certos aspectos do dashboard da Braze, enquanto têm restrições em comparação com administradores da empresa e administradores de espaço de trabalho.

| Permissões | Usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Gerenciar Usuários do Dashboard" marcada. Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, eles não podem criar ou gerenciar contas de administradores da empresa. |
| Limitações de função | Se um usuário limitado tiver todas as permissões, exceto "Administrador de Grupo de App", ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador de espaço de trabalho. |
| Visibilidade das permissões | Se um usuário limitado tiver "Gerenciar Usuários do Dashboard" marcado para um grupo de app (como Dev), mas não para outro (como Prod), ele não verá as permissões do grupo de app Prod em seu perfil "Gerenciar Usuários". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparando usuários limitados

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do grupo de app | Os Administradores do Grupo de App têm permissões específicas para gerenciar grupos de app, mas não têm a mesma autoridade que os Administradores da Empresa. Usuários limitados podem herdar permissões semelhantes às dos Administradores do Grupo de App se tiverem as permissões necessárias marcadas. |
| Administrador da empresa | Os Administradores da Empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro Administrador da Empresa para essa ação. |
| Permissão básica somente leitura | Para acessar certas partes do dashboard, como a página de Parceiros de Tecnologia, os usuários devem ter uma permissão básica somente leitura. Isso inclui ter "Gerenciar Integrações Externas" ativado, juntamente com permissões para Acessar Campanhas, Canvas, Cartões, Segmentos e Biblioteca de Mídia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erro de acesso limitado

Os usuários podem encontrar mensagens como "Acesso Limitado. Você não tem permissões para acessar esta Página." Nesses casos, o administrador da conta deve verificar se pode resolver o problema desativando e reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Editando as permissões de um usuário

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Usuários da Empresa** e selecione o nome dele.

![A página "Usuários da Empresa" na Braze com um usuário listado nos resultados.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Adicionar, editar, excluir, suspender ou reativar outros [usuários da Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- Exportar usuários da Braze como um CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador** e depois selecione **Atualizar usuário**.

![Os detalhes do usuário selecionado com a caixa de seleção de administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar a Braze até que você atribua a ele pelo menos uma permissão [de nível de empresa ou de nível de espaço de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions&tab=company#legacypermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gerenciar as seguintes permissões de nível de empresa para um usuário, marque ou desmarque a caixa ao lado dessa permissão. Quando terminar, selecione **Atualizar usuário**.

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Criar e excluir espaços de trabalho|Permite que os usuários criem e excluam espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espaço de trabalho

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence na Braze. Para gerenciar as permissões de nível de espaço de trabalho, selecione **Selecionar espaços de trabalho e permissões** e escolha suas permissões manualmente para selecionar ou atribuir um conjunto de permissões [que você criou anteriormente]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_creating-a-permission-set).

Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Depois, em **Permissões**, escolha uma ou mais permissões no menu suspenso. A Braze atribui essas permissões apenas para os espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Ativar Acesso de Administrador** se quiser conceder permissões totais para esse espaço de trabalho.

Quando terminar, selecione **Atualizar usuário**.

![Permissões de nível de espaço de trabalho sendo selecionadas manualmente na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual_legacy.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Conjuntos de permissão**, escolha um conjunto de permissões. A Braze atribui essas permissões apenas para os espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões de nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set_legacy.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário

Para baixar uma lista dos seus usuários e suas permissões, acesse **Configurações** > **Usuários da Empresa** e selecione **Exportar Usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Usuários da Empresa" na Braze com a opção "Exportar Usuários" em foco.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões

|Nível|Nome|Definição|
|---|---|---|
|Administrador|Administrador|Permite que os usuários acessem todos os recursos disponíveis. Esta é a configuração padrão para todos os novos usuários. Pode atualizar as configurações da empresa (nome da empresa e fuso horário), o que os usuários limitados não podem fazer.|
|Empresa|Criar e excluir espaços de trabalho|Permite que os usuários criem e excluam espaços de trabalho.|
|Empresa|Gerenciar configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Espaço de trabalho|Acessar Campanhas, Canvas, Cartões, Blocos de Conteúdo, Feature Flags, Segmentos, Biblioteca de Mídia, Localizações, Códigos de Promoção e Centrais de Preferências|Permite que os usuários visualizem métricas de performance de campanhas e Canvas, criem e dupliquem rascunhos de campanhas e Canvas, editem rascunhos e modelos de campanhas e Canvas, visualizem rascunhos de segmentos, modelos e mídias, criem modelos, façam upload de mídias, criem ou atualizem listas de códigos promocionais, visualizem relatórios de engajamento e visualizem configurações de mensagens globais no dashboard. No entanto, os usuários com essa permissão não podem pausar ou editar conteúdo ativo existente.<br><br> Quando essa permissão é configurada como uma [permissão de Equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), se quaisquer campanhas ou Canvas no [relatório de engajamento]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) estiverem fora das Equipes atribuídas ao usuário ou não tiverem Equipes atribuídas, o relatório ficará oculto para o usuário.|
|Espaço de trabalho|Acessar Console de Desenvolvimento|Permite acesso total às seguintes configurações e registros:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Chaves de API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Grupos internos</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Registro de atividades de envio de mensagem</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Registro de usuários de eventos</a></li></ul>{:/}|
|Espaço de trabalho|Aprovar e rejeitar campanhas|Permite que os usuários aprovem ou rejeitem campanhas. O [fluxo de trabalho de aprovação para campanhas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta se quiser participar do acesso antecipado.|
|Espaço de trabalho|Aprovar e rejeitar Canvas|Permite que os usuários aprovem ou rejeitem Canvas. O [fluxo de trabalho de aprovação para Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique.|
|Espaço de trabalho|Editar integrações com o Currents|Permite que os usuários modifiquem uma conexão Currents, incluindo credenciais. Por padrão, os usuários atribuídos à permissão "Integrações Externas" também recebem essa permissão.|
|Espaço de trabalho|Editar segmentos|Permite que os usuários criem e editem segmentos. Você ainda pode criar campanhas com segmentos e filtros existentes sem essa permissão. Você precisa dessa permissão para gerar um segmento a partir de usuários em um CSV ou redirecionar o grupo de usuários no CSV.|
|Espaço de trabalho|Exportar dados de usuários|Permite que os usuários exportem seus dados de usuários de segmentos, campanhas e Canvas. Essa permissão inclui informações confidenciais do usuário, como nomes, endereços de e-mail e outras informações de identificação pessoal (IPI) coletadas. Para exportar CSVs do dashboard, você deve ter esta permissão e a permissão "Visualizar IPI".|
|Espaço de trabalho|Importar e atualizar dados de usuários|Permite que os usuários importem arquivos CSV e atualizem arquivos de usuários do app, bem como visualizem a página de importação de usuário. Isso também permite que você edite o status de inscrição de um usuário e suas regras de aceitação/recusa de grupo de inscrições.|
|Espaço de trabalho|Lançar e gerenciar blocos de conteúdo|Permite que os usuários lancem e gerenciem [blocos de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espaço de trabalho|Lançar Centrais de Preferências|Permite que os usuários lancem [centrais de preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espaço de trabalho|Gerenciar apps|Permite que os usuários editem **Configurações do app**.|
|Espaço de trabalho|Permissão para gerenciar catálogos do dashboard|Permite que os usuários criem e gerenciem catálogos.|
|Espaço de trabalho|Gerenciar usuários do dashboard| Permite que os não administradores visualizem, editem e gerenciem a página **Usuários da Empresa** e gerenciem os usuários do dashboard em seu espaço de trabalho, modificando as permissões de qualquer usuário, inclusive eles próprios. Os usuários com essa permissão não podem excluir usuários (somente os administradores podem excluir usuários).<br><br>Isso corresponde à permissão legada `MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Espaço de trabalho|Gerenciar configurações de e-mail|Permite que os usuários salvem as alterações de configuração de e-mail (**Configurações** > **Preferências de e-mail**).|
|Espaço de trabalho|Gerenciar eventos, atributos, compras|Permite que os usuários editem atributos personalizados (usuários sem essa capacidade ainda podem visualizar atributos personalizados), editem e visualizem propriedades de eventos personalizados e editem e visualizem propriedades de produtos em **Configurações de Dados**.|
|Espaço de trabalho|Gerenciar integrações externas|Permite acesso a todas as guias em **Parceiros de Tecnologia**, capacidade de sincronizar a Braze com outras plataformas e acesso para gerenciar [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Espaço de trabalho|Gerenciar Feature Flags|Permite que os usuários criem ou editem [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags/).|
|Espaço de trabalho|Gerenciar ativos da biblioteca de mídia|Permite que os usuários adicionem, editem e excluam ativos da biblioteca de mídia.|
|Espaço de trabalho|Gerenciar grupos de inscrições|Permite que os usuários criem e gerenciem grupos de inscrições.|
|Espaço de trabalho|Gerenciar tags|Permite que os usuários editem ou excluam tags (em **Gerenciamento de Tag**). Você não precisa dessa permissão para adicionar tags a campanhas ou segmentos.|
|Espaço de trabalho|Gerenciar equipes|Permite que os usuários gerenciem **Equipes Internas**. A capacidade de selecionar esta permissão depende do seu contrato com a Braze.<br><br>Isso corresponde à permissão legada `MANAGE_TERRITORIES`.|
|Espaço de trabalho|Gerenciar transformações|Permite que os usuários criem e gerenciem Transformações de Dados.|
|Espaço de trabalho|Enviar campanhas, Canvas|Permite que os usuários editem, arquivem e interrompam campanhas e Canvas, criem campanhas e lancem Canvas. |
|Espaço de trabalho|Ver informações de faturamento|Permite que os usuários visualizem inscrições e faturamento.|
|Espaço de trabalho|Ver integração do Currents|Permite que os usuários visualizem todas as informações sobre uma conexão Currents, excluindo credenciais. Por padrão, os usuários atribuídos à permissão "Acessar Campanhas, Canvas, Cartões, Blocos de Conteúdo, Feature Flags, Segmentos, Biblioteca de Mídia, Localizações, Códigos de Promoção e Centrais de Preferências" também recebem essa permissão.|
|Espaço de trabalho|Ver atributos personalizados marcados como IPI|Permite que usuários não administradores visualizem atributos personalizados que contenham informações confidenciais e estejam marcados como informações de identificação pessoal (IPI).|
|Espaço de trabalho|Ver IPI|Permite que os usuários visualizem os campos de informações de identificação pessoal (IPI) conforme definido pela sua empresa no dashboard. Os usuários também podem visualizar os campos de IPI na guia **Pré-visualizar como Usuário** das prévias de mensagens.<br><br>Você precisa desta permissão para usar o [Construtor de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), pois permite acesso direto a alguns dados de clientes. Para exportar CSVs do dashboard, os usuários precisam tanto desta permissão quanto da permissão "Exportar Dados de Usuários".|
|Espaço de trabalho|Ver perfis de usuário em conformidade com IPI|Permite que os usuários visualizem perfis de usuários que contenham campos que sua empresa definiu como informações de identificação pessoal (IPI), mas os campos de IPI são ocultados.<br><br>Você precisa desta permissão para usar a ferramenta de busca de usuários. |
|Espaço de trabalho|Ver transformações|Permite que os usuários visualizem [Transformações de Dados da Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Espaço de trabalho|Ver dados de uso|Permite que os usuários visualizem o uso do app, incluindo os painéis de performance do canal.|
|Espaço de trabalho|Mesclar usuários duplicados|Permite que os usuários mesclem perfis de usuário duplicados.|
|Espaço de trabalho|Pré-visualizar usuários duplicados|Permite que os usuários vejam uma prévia de quais perfis de usuário estão duplicados.|
|Espaço de trabalho|Criar e editar modelos de Canvas|Permite que os usuários criem e editem modelos de Canvas.|
|Espaço de trabalho|Ver modelos de Canvas|Permite que os usuários visualizem os modelos de Canvas.|
|Espaço de trabalho|Arquivar modelos de Canvas|Permite que os usuários arquivem modelos de Canvas.|
|Espaço de trabalho|Gerenciar segmentação de propriedades personalizadas de eventos|Permite que os usuários criem segmentos com base na recência e na frequência da propriedade do evento.|
|Espaço de trabalho|Publicar landing pages|Permite que os usuários publiquem [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Espaço de trabalho|Criar rascunhos de landing pages|Permite que os usuários criem e salvem rascunhos de landing pages.|
|Espaço de trabalho|Acessar landing pages|Permite que os usuários acessem a página **Landing Pages**.|
|Espaço de trabalho|Criar e editar modelos de landing page|Permite que os usuários criem e editem modelos de landing page.|
|Espaço de trabalho|Ver modelos de landing page|Permite que os usuários visualizem modelos de landing page.|
|Espaço de trabalho|Arquivar modelos de landing page|Permite que os usuários arquivem modelos de landing page.|
|Espaço de trabalho|Ver agentes de IA personalizados|Permite que os usuários visualizem [agentes de IA personalizados]({{site.baseurl}}/user_guide/brazeai/agents/). Esse recurso está em beta.|
|Espaço de trabalho|Criar agentes de IA personalizados|Permite que os usuários criem agentes de IA personalizados. Esse recurso está em beta.|
|Espaço de trabalho|Editar agentes de IA personalizados|Permite que os usuários editem agentes de IA personalizados. Esse recurso está em beta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }