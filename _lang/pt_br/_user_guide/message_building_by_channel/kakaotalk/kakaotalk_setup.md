---
nav_title: Configurar o KakaoTalk
article_title: "Configurar o KakaoTalk"
description: "Este artigo de referência descreve como configurar seu canal KakaoTalk, incluindo como configurar usuários, reconciliar IDs de usuário e criar usuários teste."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# Configurar o KakaoTalk

> Este artigo aborda como configurar o [canal de envio de mensagens KakaoTalk]({{site.baseurl}}/kakaotalk/) na Braze, incluindo como configurar usuários, reconciliar IDs de usuário e criar usuários teste do KakaoTalk.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta com um parceiro KakaoTalk compatível | É necessário ter uma conta com um parceiro KakaoTalk compatível, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) ou Infobip, para usar o canal de envio de mensagens KakaoTalk. |
| Canal Business do KakaoTalk | Sua conta KakaoTalk deve ser um canal Business do KakaoTalk para enviar mensagens KakaoTalk pela Braze. Quando você cria uma conta, o status padrão é básico. Para tornar sua conta um canal Business, você precisará verificar sua empresa e fornecer a documentação relevante. |
| Sender Key do KakaoTalk | Um Sender Key válido do KakaoTalk. |
| Número de telefone de contato | Um número de telefone de contato para o administrador do seu canal KakaoTalk. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tipos de contas KakaoTalk

| Tipo de conta | Descrição |
| --- | --- |
| Canal básico | Um canal KakaoTalk padrão que qualquer organização pode configurar. Ele permite envio de mensagens em massa e chat 1:1 pelo KakaoTalk. |
| [Canal Business](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Um canal KakaoTalk aprimorado e verificado para empresas que requer um processo de solicitação e verificação. Ele oferece recursos avançados, como {::nomarkdown}<ul><li>Selo de verificação</li><li>Aparição como canal recomendado</li><li>Suporte para envio de mensagens comerciais</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Solicitar um canal Business

Antes de iniciar a solicitação, reúna a seguinte documentação empresarial:
- Certificado de Registro Empresarial Coreano
- Documento de identidade do Representante da Empresa
- Certificado de Emprego
- Licenças específicas do setor

{% alert important %}
As informações no seu canal KakaoTalk (como nome do canal, imagem de perfil e outros) devem corresponder exatamente às informações nos seus documentos oficiais enviados.
{% endalert %}

Após reunir sua documentação, siga estas etapas:

1. Faça login no [Centro de Administração de Canais KakaoTalk](https://center-pf.kakao.com/).
2. Selecione o canal KakaoTalk existente que deseja fazer upgrade.
3. Na seção **Management (관리)**, selecione a opção **Business Channel Application (비즈니스 채널 신청)**.
4. Selecione o botão **Apply** ou **Request (신청)** para iniciar o processo.
5. Forneça as informações necessárias.
6. Aguarde uma notificação com os resultados da revisão.

## Integrar o KakaoTalk

### Etapa 1: Conectar o canal KakaoTalk à Braze

1. Acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione seu provedor KakaoTalk.
2. Reúna as credenciais necessárias para seu provedor (veja abaixo), insira-as na página **Parceiros de Tecnologia** e salve.
3. Use as credenciais recém-salvas para envio.

#### CJ OliveNetworks

Acesse seu [dashboard Comm.One](https://ums.cjmplace.com/) e reúna as seguintes informações.

| Campo | Local |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Selecione seu perfil. |
| **Sender Key (발신프로필 키)** | Acesse **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | No seu dashboard Comm.One, acesse **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Acesse <b>Account Management (계정 관리)</b>, selecione o ícone de menu e depois selecione <b>View Details (자세히보기)</b>.</li><li>Acesse <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Acesse o mesmo local do **Sender number (사업자 등록번호)** e depois acesse **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Dashboard Comm.One mostrando um ID de login censurado.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Dashboard Comm.One mostrando um Sender Key censurado.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Dashboard Comm.One mostrando um nome de canal censurado.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Dashboard Comm.One mostrando um ID de credencial e senha censurados.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

![Campos na página Parceiros de Tecnologia para CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Credenciais para um canal KakaoTalk da Braze.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
Somente os canais mapeados para um único ID comum podem ser registrados.
{% endalert %}

#### Infobip

Acesse seu dashboard Infobip e reúna as seguintes informações.

| Campo | Local |
| --- | --- |
| **API Base URL** | Selecione **Developer Tools** > **API Keys**. |
| **Chave de API** | Selecione **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | Selecione **Channels and Numbers** > **Channels** e depois selecione a guia **Senders**. |
| **Sender profile UUID** | Fornecido diretamente pela Infobip. Entre em contato com a Infobip se você não tiver essa informação. |
| **Channel name** | Fornecido diretamente pela Infobip. Entre em contato com a Infobip se você não tiver essa informação. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurar perfis de usuário

Os perfis de usuário devem ter números de telefone para receber mensagens pelo KakaoTalk. Os números de telefone são exibidos no perfil de usuário no formato em que foram fornecidos. Atualmente, diferentemente do SMS ou WhatsApp, o KakaoTalk usa o campo de telefone padrão (e não um número convertido para o formato E.164).

![Perfil de usuário para um usuário teste com um número de telefone em formato não editado.]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### Importar números de telefone

Importe números de telefone [fazendo upload de um CSV ou usando a API]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/) para criar um usuário.