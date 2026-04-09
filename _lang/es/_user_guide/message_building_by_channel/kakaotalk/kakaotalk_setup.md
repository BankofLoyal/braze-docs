---
nav_title: Configurar KakaoTalk
article_title: "Configurar KakaoTalk"
description: "Este artículo de referencia describe cómo configurar tu canal de KakaoTalk, incluyendo cómo configurar usuarios, conciliar ID de usuario y crear usuarios de prueba."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# Configurar KakaoTalk

> Este artículo cubre cómo configurar el [canal de mensajería KakaoTalk]({{site.baseurl}}/kakaotalk/) en Braze, incluyendo cómo configurar usuarios, conciliar ID de usuario y crear usuarios de prueba de KakaoTalk.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta con un socio de KakaoTalk compatible | Se requiere una cuenta con un socio de KakaoTalk compatible, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) o Infobip, para usar el canal de mensajería KakaoTalk. |
| Canal Business de KakaoTalk | Tu cuenta de KakaoTalk debe ser un canal Business de KakaoTalk para enviar mensajes de KakaoTalk a través de Braze. Cuando creas una cuenta, su estado predeterminado es básico. Para convertir tu cuenta en un canal Business, necesitarás verificar tu empresa y proporcionar la documentación correspondiente. |
| Sender Key de KakaoTalk | Un Sender Key de KakaoTalk válido. |
| Número de teléfono de contacto | Un número de teléfono de contacto para el administrador de tu canal de KakaoTalk. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tipos de cuentas de KakaoTalk

| Tipo de cuenta | Descripción |
| --- | --- |
| Canal básico | Un canal estándar de KakaoTalk que cualquier organización puede configurar. Permite mensajería de difusión y chat 1:1 a través de KakaoTalk. |
| [Canal Business](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Un canal de KakaoTalk mejorado y verificado para empresas que requiere un proceso de solicitud y verificación. Ofrece características mejoradas, como {::nomarkdown}<ul><li>Insignia de verificación</li><li>Aparición como canal recomendado</li><li>Soporte para mensajería empresarial</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Solicitar un canal Business

Antes de iniciar la solicitud, reúne la siguiente documentación empresarial:
- Certificado de registro empresarial coreano
- Identificación del representante de la empresa
- Certificado de empleo
- Licencias específicas del sector

{% alert important %}
La información en tu canal de KakaoTalk (como el nombre del canal, la imagen de perfil y otros) debe coincidir exactamente con la información de tus documentos oficiales presentados.
{% endalert %}

Después de reunir tu documentación, sigue estos pasos:

1. Inicia sesión en el [Centro de administración de canales de KakaoTalk](https://center-pf.kakao.com/).
2. Selecciona el canal de KakaoTalk existente que deseas actualizar.
3. En la sección **Management (관리)**, selecciona la opción **Business Channel Application (비즈니스 채널 신청)**.
4. Selecciona el botón **Apply** o **Request (신청)** para comenzar el proceso.
5. Proporciona la información requerida.
6. Espera una notificación con los resultados de la revisión.

## Integrar KakaoTalk

### Paso 1: Conectar el canal de KakaoTalk a Braze

1. Ve a **Integraciones del socio** > **Socios tecnológicos** y selecciona tu proveedor de KakaoTalk.
2. Reúne las credenciales requeridas para tu proveedor (ver a continuación), luego ingrésalas en la página de **Socios tecnológicos** y guarda.
3. Usa las credenciales recién guardadas para enviar.

#### CJ OliveNetworks

Ve a tu [dashboard de Comm.One](https://ums.cjmplace.com/) y reúne la siguiente información.

| Campo | Ubicación |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Selecciona tu perfil. |
| **Sender Key (발신프로필 키)** | Ve a **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | En tu dashboard de Comm.One, ve a **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Ve a <b>Account Management (계정 관리)</b>, selecciona el icono de menú y luego selecciona <b>View Details (자세히보기)</b>.</li><li>Ve a <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Ve a la misma ubicación del **Sender number (사업자 등록번호)**, luego ve a **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Dashboard de Comm.One mostrando un ID de inicio de sesión censurado.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Dashboard de Comm.One mostrando un Sender Key censurado.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Dashboard de Comm.One mostrando un nombre de canal censurado.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Dashboard de Comm.One mostrando un ID de credencial y contraseña censurados.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

![Campos en la página de socios tecnológicos para CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Credenciales para un canal de KakaoTalk en Braze.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
Solo se pueden registrar los canales mapeados a un único ID común.
{% endalert %}

#### Infobip

Ve a tu dashboard de Infobip y reúne la siguiente información.

| Campo | Ubicación |
| --- | --- |
| **API Base URL** | Selecciona **Developer Tools** > **API Keys**. |
| **Clave de API** | Selecciona **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | Selecciona **Channels and Numbers** > **Channels**, luego selecciona la pestaña **Senders**. |
| **Sender profile UUID** | Proporcionado directamente por Infobip. Ponte en contacto con Infobip si no tienes esta información. |
| **Nombre del canal** | Proporcionado directamente por Infobip. Ponte en contacto con Infobip si no tienes esta información. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurar perfiles de usuario

Los perfiles de usuario deben tener números de teléfono para poder enviarles mensajes a través de KakaoTalk. Los números de teléfono se muestran en el perfil de usuario y en el formato en que se proporcionan. Actualmente, a diferencia de SMS o WhatsApp, KakaoTalk usa el campo de teléfono estándar (y no un número que haya sido convertido al formato E.164).

![Perfil de usuario para un usuario de prueba con un número de teléfono en formato sin editar.]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### Importar números de teléfono

Importa números de teléfono [cargando un CSV o usando la API]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/) para crear un usuario.