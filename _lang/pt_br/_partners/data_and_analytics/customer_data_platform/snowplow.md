---
nav_title: Snowplow
article_title: Snowplow
description: "Este artigo de referência descreve a parceria entre a Braze e a Snowplow, uma plataforma de infraestrutura de dados, que permite que você encaminhe eventos da Snowplow para a Braze em tempo real usando o Event Forwarding da Snowplow."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> A [Snowplow](https://snowplow.io) é uma plataforma dimensionável e de código aberto para coleta de dados avançados, de alta qualidade e de baixa latência. A Snowplow foi projetada para coletar dados comportamentais completos e de alta qualidade para empresas.

_Essa integração é mantida pela Snowplow._

## Sobre a integração

A integração entre a Braze e a Snowplow permite que você encaminhe eventos da Snowplow para a Braze em tempo real usando a solução Event Forwarding da Snowplow. Essa integração permite que você envie eventos para a Braze, oferecendo flexibilidade e controle. Especificamente, você pode:
- Filtrar e transformar eventos antes de enviá-los à Braze.
- Mapear os dados de eventos da Snowplow para atributos de usuários da Braze, eventos personalizados e compras.
- Manter todos os dados em sua nuvem privada até que você decida encaminhá-los.
- Implantar você mesmo a solução em sua conta de nuvem Snowplow existente. 

O [Event Forwarding](https://docs.snowplow.io/docs/destinations/forwarding-events/) da Snowplow é um recurso complementar pago disponível para os clientes da Snowplow. Para encaminhar eventos para a Braze sem esse complemento, use a integração [Google Tag Manager Server-Side](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) da Snowplow.

Aproveite os ricos dados de comportamento da Snowplow para promover interações poderosas centradas no cliente na Braze e enviar mensagens personalizadas em tempo real.

## Pré-requisitos

| Requisito             | Descrição                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pipeline da Snowplow       | Você precisa de um pipeline da Snowplow em funcionamento.                                                                                                                                                                                                                                          |
| Acesso ao Console da Snowplow | Você deve ter acesso ao Console da Snowplow para configurar os encaminhadores de eventos.                                                                                                                                                                                                                                |
| Chave da API REST da Braze      | Uma chave da API REST da Braze com as seguintes permissões: `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename` e `users.alias.update`. <br><br> Você pode criar isso no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze     | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint depende da URL da Braze para sua instância.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

### Entrega personalizada baseada em ação
Use qualquer um dos inúmeros eventos avançados que a Snowplow coleta por padrão ou defina seus eventos personalizados para moldar jornadas de clientes ainda mais granulares que façam sentido para sua empresa. Aproveite os ricos dados de comportamento da Snowplow para projetar funis de clientes e gerar valor para suas equipes de marketing e de produtos, ajudando-as a maximizar a conversão e o uso do produto por meio da Braze.

### Segmentação dinâmica
Crie públicos dinâmicos na Braze com base nos dados comportamentais de alta qualidade da Snowplow: à medida que os usuários realizam ações em seu produto, app ou site, é possível aproveitar os dados de comportamento em tempo real coletados pela Snowplow para adicionar ou remover automaticamente usuários de segmentos relevantes na Braze.

## Integração

### Etapa 1: Configure o destino no Console da Snowplow

Para criar o encaminhador de eventos:

1. No Console da Snowplow, navegue até **Destinos** e selecione **Criar novo destino**.
2. Ao configurar a conexão, selecione **Braze** para o tipo de conexão.
3. Digite sua chave de API da Braze e o endpoint da API REST.
4. Salve a conexão.

### Etapa 2: Configurar o encaminhador de eventos

Ao configurar o encaminhador, você pode escolher quais eventos da Snowplow serão encaminhados e mapeá-los para os tipos de objetos da Braze:

1. **[Atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object)**: Atualize os dados do perfil do usuário e as propriedades personalizadas do usuário.
2. **[Eventos personalizados]({{site.baseurl}}/api/objects_filters/event_object)**: Envie ações e comportamentos do usuário.
3. **[Compras]({{site.baseurl}}/api/objects_filters/purchase_object)**: Envie dados de transação com detalhes do produto.

Para cada tipo de objeto, você pode configurar mapeamentos de campo para especificar como os dados de eventos da Snowplow são mapeados para os campos da Braze. Consulte a documentação [Creating forwarders](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/) da Snowplow para obter instruções detalhadas de configuração e mapeamento de campos.

### Etapa 3: Validar a integração

Confirme se os eventos estão chegando à Braze verificando as seguintes páginas em sua conta da Braze:

1. **Query Builder**: Na Braze, navegue até **Análise de dados** > **Query Builder**. Você pode escrever consultas nas tabelas a seguir para ter uma prévia dos dados encaminhados pela Snowplow: `USER_BEHAVIORS_CUSTOMEVENT_SHARED` e `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **Dashboard de uso da API**: Na Braze, navegue até **Configurações** > **APIs e Identificadores** para ver um gráfico do uso da API ao longo do tempo. Você pode filtrar especificamente pela chave de API que a Snowplow usa e ver os sucessos e as falhas.

## Envio de propriedades personalizadas

Você pode enviar propriedades personalizadas além dos campos padrão. A estrutura depende do tipo de objeto da Braze que você está usando:

- **Atributos do usuário**: Adicione como campos de nível superior (por exemplo, `subscription_tier`, `loyalty_points`)
- **Propriedades do evento**: Aninhe dentro do objeto `properties` (por exemplo, `properties.plan_type`, `properties.feature_flag`)
- **Propriedades de compra**: Aninhe dentro do objeto `properties` (por exemplo, `properties.color`, `properties.size`)

Para nomes de propriedades que contenham espaços, use a notação de colchetes (por exemplo, `["account type"]` ou `properties["campaign source"]`).

Consulte a [documentação do Event Object]({{site.baseurl}}/api/objects_filters/event_object) para obter detalhes sobre os tipos de dados compatíveis, os requisitos de nomenclatura de propriedades e os limites de tamanho da carga útil.

## Limitações

**Limites de taxa:** A Braze impõe um limite de taxa de 3.000 chamadas de API a cada três segundos para a API Track Users. Como a Snowplow não oferece suporte a lotes para encaminhadores de eventos, esse limite de taxa da API também funciona como o limite de taxa de eventos. Se a taxa de transferência de entrada exceder 3.000 eventos a cada três segundos, a latência poderá aumentar.