---
nav_title: Configurer KakaoTalk
article_title: "Configurer KakaoTalk"
description: "Cet article de référence explique comment configurer votre canal KakaoTalk, notamment comment configurer les utilisateurs, réconcilier les ID utilisateur et créer des utilisateurs test."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# Configurer KakaoTalk

> Cet article explique comment configurer le [canal de communication KakaoTalk]({{site.baseurl}}/kakaotalk/) dans Braze, notamment comment configurer les utilisateurs, réconcilier les ID utilisateur et créer des utilisateurs test KakaoTalk.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte auprès d'un partenaire KakaoTalk pris en charge | Un compte auprès d'un partenaire KakaoTalk pris en charge, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) ou Infobip, est requis pour utiliser le canal de communication KakaoTalk. |
| Canal Business KakaoTalk | Votre compte KakaoTalk doit être un canal Business KakaoTalk pour envoyer des messages KakaoTalk via Braze. Lorsque vous créez un compte, son statut par défaut est basique. Pour transformer votre compte en canal Business, vous devrez vérifier votre entreprise et fournir la documentation correspondante. |
| Clé d'expéditeur KakaoTalk | Une clé d'expéditeur KakaoTalk valide. |
| Numéro de téléphone de contact | Un numéro de téléphone de contact pour l'administrateur de votre canal KakaoTalk. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Types de comptes KakaoTalk

| Type de compte | Description |
| --- | --- |
| Canal basique | Un canal KakaoTalk standard que toute organisation peut configurer. Il permet l'envoi de messages diffusés et le chat 1:1 via KakaoTalk. |
| [Canal Business](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Un canal KakaoTalk amélioré et vérifié pour les entreprises, qui nécessite un processus de candidature et de vérification. Il offre des fonctionnalités avancées, telles que {::nomarkdown}<ul><li>Badge vérifié</li><li>Apparition en tant que canal recommandé</li><li>Prise en charge de l'envoi de messages professionnels</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Demander un canal Business

Avant de commencer la candidature, rassemblez les documents professionnels suivants :
- Certificat d'enregistrement d'entreprise coréen
- Pièce d'identité du représentant de l'entreprise
- Certificat d'emploi
- Licences spécifiques au secteur d'activité

{% alert important %}
Les informations de votre canal KakaoTalk (telles que le nom du canal, l'image de profil, etc.) doivent correspondre exactement aux informations figurant sur vos documents officiels soumis.
{% endalert %}

Après avoir rassemblé vos documents, suivez ces étapes :

1. Connectez-vous au [Centre d'administration des canaux KakaoTalk](https://center-pf.kakao.com/).
2. Sélectionnez le canal KakaoTalk existant que vous souhaitez mettre à niveau.
3. Dans la section **Management (관리)**, sélectionnez l'option **Business Channel Application (비즈니스 채널 신청)**.
4. Sélectionnez le bouton **Apply** ou **Request (신청)** pour lancer le processus.
5. Fournissez les informations requises.
6. Attendez une notification avec les résultats de la vérification.

## Intégrer KakaoTalk

### Étape 1 : Connecter le canal KakaoTalk à Braze

1. Accédez à **Intégration partenaires** > **Partenaires technologiques** et sélectionnez votre fournisseur KakaoTalk.
2. Rassemblez les identifiants requis pour votre fournisseur (voir ci-dessous), puis saisissez-les sur la page **Partenaires technologiques** et enregistrez.
3. Utilisez les identifiants nouvellement enregistrés pour l'envoi.

#### CJ OliveNetworks

Accédez à votre [tableau de bord Comm.One](https://ums.cjmplace.com/) et rassemblez les informations suivantes.

| Champ | Emplacement |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Sélectionnez votre profil. |
| **Sender Key (발신프로필 키)** | Accédez à **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | Dans votre tableau de bord Comm.One, accédez à **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Accédez à <b>Account Management (계정 관리)</b>, sélectionnez l'icône de menu, puis sélectionnez <b>View Details (자세히보기)</b>.</li><li>Accédez à <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Accédez au même emplacement que pour le **Sender number (사업자 등록번호)**, puis accédez à **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Tableau de bord Comm.One affichant un identifiant de connexion masqué.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Tableau de bord Comm.One affichant une clé d'expéditeur masquée.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Tableau de bord Comm.One affichant un nom de canal masqué.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Tableau de bord Comm.One affichant un identifiant et un mot de passe masqués.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

![Champs sur la page Partenaires technologiques pour CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Identifiants pour un canal KakaoTalk dans Braze.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
Seuls les canaux associés à un même identifiant commun peuvent être enregistrés.
{% endalert %}

#### Infobip

Accédez à votre tableau de bord Infobip et rassemblez les informations suivantes.

| Champ | Emplacement |
| --- | --- |
| **API Base URL** | Sélectionnez **Developer Tools** > **API Keys**. |
| **Clé API** | Sélectionnez **Developer Tools** > **API Keys**. |
| **Nom de l'expéditeur / Clé d'expéditeur** | Sélectionnez **Channels and Numbers** > **Channels**, puis sélectionnez l'onglet **Senders**. |
| **UUID du profil d'expéditeur** | Fourni directement par Infobip. Contactez Infobip si vous ne disposez pas de cette information. |
| **Nom du canal** | Fourni directement par Infobip. Contactez Infobip si vous ne disposez pas de cette information. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurer les profils utilisateur

Les profils utilisateur doivent contenir des numéros de téléphone pour pouvoir leur envoyer des messages via KakaoTalk. Les numéros de téléphone sont affichés sur le profil utilisateur dans le format dans lequel ils ont été fournis. Actuellement, contrairement au SMS ou à WhatsApp, KakaoTalk utilise le champ de téléphone standard (et non un numéro converti au format E.164).

![Profil utilisateur d'un utilisateur test avec un numéro de téléphone dans un format non modifié.]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### Importer des numéros de téléphone

Importez des numéros de téléphone en [chargeant un fichier CSV ou en utilisant l'API]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/) pour créer un utilisateur.