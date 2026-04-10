---
nav_title: Sobre o Audience Sync
article_title: Sobre o Audience Sync
alias: /partners/about_audience_sync/
description: "Este artigo de referência abordará como usar a sincronização de público da Braze para o Facebook, para veicular anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 0
Tool:
  - Canvas

---

# Sobre o Audience Sync

> O recurso de Audience Sync da Braze ajuda você a expandir o alcance de suas campanhas para muitas das principais tecnologias sociais e de publicidade. Por meio do [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas), as marcas podem sincronizar dinamicamente e com segurança os dados de usuários de primeira parte no ecossistema de publicidade para impulsionar a eficiência de marketing e operacional.

## Disponibilidade de recursos

Todos os clientes da Braze têm acesso imediato ao Audience Sync para Google e Facebook, mas os clientes que utilizam créditos de mensagem podem acessar todos os parceiros do Audience Sync. Para desbloquear destinos adicionais do Audience Sync, adquira o Audience Sync Pro. Entre em contato com o gerente de conta da Braze para mais detalhes.

## Casos de uso

- Direcionamento de usuários de alto valor usando canais proprietários e pagos para gerar compras ou engajamento incrementais.
- Criação de públicos semelhantes dos seus usuários de alto valor para otimizar os custos de aquisição de novos usuários e conversões.
- Redirecionamento de usuários com anúncios que são menos responsivos a outros canais de marketing.
- Criação de públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.

## Visão geral

<style>
table td {
    word-break: break-word;
}
</style>

| Destino | Tempo para o destino corresponder aos membros do público | Limite de taxa | Semelhante ou actalike | Dicas |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | Até 24 horas | 250.000 solicitações por minuto. Em lote a cada 5 segundos com uma nova tentativa automática com base no feedback do Google. | Sim | {::nomarkdown}<ul><li>A Criteo suporta até 1.000 públicos de anúncios.</li><li>O tamanho mínimo do público é 500, e o recomendado é acima de 20.000.</li></ul>{:/} |
| [Facebook ou Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | Até 24 horas | 190.000 contas de anúncios por hora | Sim | {::nomarkdown}<ul><li>O Facebook suporta até 500 públicos de anúncios.</li><li>O Facebook exige que o público tenha pelo menos 1.000 usuários.</li></ul>{:/} |
| [Google Ads ou YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | Entre 6 e 12 horas | Em lote a cada 5 segundos com uma nova tentativa automática baseada no feedback do Google | Não | {::nomarkdown}<ul><li><b>Correspondência com o cliente:</b> Use o anúncio no celular, o endereço de e-mail ou o número de telefone.</li><li>O público do Google exige pelo menos 5.000 usuários para começar a veicular anúncios.</li><li>O tamanho do público será mostrado como zero até que haja pelo menos 1.000 usuários.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48 horas | O LinkedIn processa 10 consultas por segundo e 100.000 usuários por solicitação. A Braze agrupa usuários em lote a cada 5 segundos. | Públicos preditivos de IA | {::nomarkdown}<ul><li>O tamanho mínimo do público é de 300 membros, levando em consideração o direcionamento por local.</li><li>O LinkedIn mostra a taxa de correspondência no dashboard da Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | Entre 24 e 48 horas | O Pinterest processa 7 consultas por segundo e 1.900 usuários por solicitação. A Braze agrupa usuários em lote a cada 5 segundos. | Sim | Os públicos do Pinterest exigem pelo menos 100 usuários. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | N/D | O Snapchat processa 10 consultas por segundo e 100.000 usuários por solicitação. A Braze agrupa usuários em lote a cada 5 segundos. | Sim | O Snapchat suporta até 1.000 públicos de anúncios. |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | Entre 24 e 48 horas | O TikTok processa 50 consultas por segundo e 10.000 usuários por solicitação. A Braze agrupa usuários em lote a cada 5 segundos. | Sim | {::nomarkdown}<ul><li>O TikTok suporta até 400 públicos de anúncios.</li><li>O público do TikTok precisa de pelo menos 1.000 usuários para começar a veicular anúncios.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>Quando o limite de taxa for atingido, a Braze tentará novamente as sincronizações por 13 horas.</sup>

## Como funciona

Para usar o Audience Sync com o Google ou o Facebook, conecte sua conta de anúncio procurando pelo parceiro na página de **Parceiros de Tecnologia**.

![Parceiro de tecnologia do Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Parceiro de tecnologia do Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Depois de conectar sua conta de anúncios, você pode criar um Canvas com uma etapa do Audience Sync.

![Menu de componentes do Canvas para adicionar a etapa do Audience Sync à jornada do usuário.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Em seguida, selecione o parceiro para sincronizar os públicos.

![Opção para selecionar seu parceiro de sincronização de público na etapa Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Para cada parceiro, você precisará configurar o seguinte como parte da sua etapa do Audience Sync: 

- Conta de anúncio
- Público 
- Ação para adicionar ou remover usuários 
- Campos para correspondência 

Lembre-se de que a Braze sincronizará os usuários assim que eles entrarem na etapa do Audience Sync dentro do seu Canvas. 

Para cada destino do Audience Sync, o parceiro pode ter requisitos diferentes para os campos que podemos enviar. Consulte a documentação específica do parceiro para mais detalhes. 

### Audience Sync Pro

Para usar um parceiro do Audience Sync Pro, como TikTok, Pinterest, Snapchat ou Criteo, você poderá selecionar seus parceiros com base nas suas cotas de compra do Audience Sync Pro na seção **Audience Sync Pro** na página **Parceiros de Tecnologia**.

![Audience Sync Pro sem parceiros selecionados ainda.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Primeiro, selecione os parceiros que você pretende usar clicando em Selecionar Parceiros. Cada compra do Audience Sync Pro fornecerá 3 destinos alocados do Audience Sync Pro, que estarão disponíveis em cada um dos seus espaços de trabalho no dashboard.

![Opção para selecionar até três parceiros para se conectar à Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Depois de selecionar seus destinos do Audience Sync Pro, conecte a conta de anúncio do parceiro selecionado clicando no bloco do parceiro.

![Um exemplo do Snapchat e do TikTok selecionados como parceiros para o Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Configurações do Snapchat Audience Sync com a mensagem: "Você conectou com sucesso 1 conta do Snapchat".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Por fim, crie sua etapa do Audience Sync no Canvas usando esse destino do Audience Sync Pro.

### E-mails de erro do Audience Sync

Se o erro estiver relacionado à integração geral com o parceiro (como um problema de autorização), um e-mail será enviado ao usuário que conectou a integração. Se esse usuário não existir mais, os administradores receberão os e-mails. 

Se o erro estiver relacionado a problemas com o componente Audience Sync (como "O público não existe") no Canvas, um e-mail será enviado ao usuário que configurou o Canvas. Se esse usuário não existir mais, a responsabilidade recairá sobre o administrador da empresa.

Para configurar quem receberá esses e-mails, entre em contato com o gerente de sucesso do cliente para adicionar destinatários em **Preferências de Notificação**. Como esse recurso mudará o comportamento atual, você precisará adicionar imediatamente os destinatários a essa nova preferência de notificação, já que a Braze não faz a aceitação de ninguém por padrão, garantindo assim que nenhum e-mail de erro seja perdido.

## Considerações sobre privacidade de dados

{% alert important %}
Esta documentação não se destina a fornecer, nem pode ser considerada como fornecendo aconselhamento jurídico. O uso do Audience Sync está sujeito a requisitos legais específicos. Busque orientação jurídica para ter certeza de que você está utilizando o serviço conforme a legislação aplicável.
{% endalert %}

Ao criar públicos para rastreamento de anúncios, você pode desejar incluir ou excluir certos usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não Vender ou Compartilhar" sob o [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canvas. Abaixo, listamos algumas opções.

Se você coletou o [IDFA do iOS pelo SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), poderá usar o filtro "Rastreamento de anúncios ativado". Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync nos quais eles deram aceitação.

![Um Canvas com um público de entrada de "Rastreamento de anúncios ativado é verdadeiro".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluí-los dentro dos seus critérios de entrada do Canvas como um filtro:

![Um Canvas com um público de entrada de "opted_in_marketing é igual a true".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma Braze, consulte a [Assistência Técnica de Proteção de Dados]({{site.baseurl}}/dp-technical-assistance/).

## Gerenciamento do consentimento para direcionamento de anúncios

Como anunciante, é sua responsabilidade gerenciar o consentimento para rastreamento ou direcionamento de anúncios dos seus usuários.

Para enviar anúncios aos seus usuários, é necessário cumprir todas as leis e regulamentos aplicáveis, bem como as políticas e os requisitos da plataforma de anúncios. Use a Braze para direcionamento e sincronização de usuários somente quando tiver obtido o consentimento deles. 

Para manter suas listas de público nessas plataformas de anúncios atualizadas e remover usuários que revogaram seu consentimento, configure um Canvas para remover usuários dessas listas de público existentes usando uma etapa do Audience Sync.