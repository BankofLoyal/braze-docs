---
nav_title: "Préférences en matière d'e-mails"
article_title: Préférences des e-mails
page_type: reference
page_order: 14
description: "Cet article de référence couvre les préférences d'e-mail dans le tableau de bord de Braze, y compris les configurations d'envoi, les pixels de suivi d'ouverture, la page et les pieds de page d'abonnement, et plus encore."
tool: Dashboard
channel: email
toc_headers: h2

---

# Préférences des e-mails

> Les préférences des e-mails vous permettent de définir des paramètres spécifiques pour les e-mails sortants, comme des pieds de page personnalisés, des pages d'abonnement et de désabonnement personnalisées, et plus encore. Inclure ces options dans vos e-mails sortants permet d'offrir une expérience fluide et cohérente à vos utilisateurs.

Les **Préférences des e-mails** se trouvent sous **Paramètres** dans le tableau de bord.

## Configuration de l'envoi

Les paramètres d'e-mail de la section **Configuration d'envoi** déterminent quels détails sont inclus dans vos campagnes par e-mail. Ces paramètres concernent notamment ce que vos utilisateurs voient quand ils reçoivent un e-mail de Braze.

### Paramètres d'e-mail sortant

Lorsque vous configurez vos paramètres d'e-mail, vos paramètres d'e-mails sortants identifient le nom et les adresses e-mail utilisés quand Braze envoie des e-mails à vos utilisateurs.

{% tabs local %}
{% tab Display Name Address %}

Dans cette section, vous pouvez ajouter les noms et adresses e-mail utilisables lorsque Braze envoie des e-mails à vos utilisateurs. Les noms d'affichage et les adresses e-mail sont disponibles dans les options **Informations d'envoi** lorsque vous rédigez votre campagne par e-mail. Notez que les mises à jour apportées aux paramètres des e-mails sortants n'affectent pas rétroactivement les envois existants.

![Section « Paramètres des e-mails sortants » avec des champs pour différents noms d'affichage et domaines.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Personnalisation avec Liquid

Vous pouvez également utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) dans les champs **From Display Name** (Nom d'affichage de l'expéditeur), **Local Part** (Partie locale) et **Domain** (Domaine) pour générer dynamiquement le nom et l'adresse e-mail de l'expéditeur à partir d'attributs personnalisés. Notez que pour utiliser Liquid dans le champ **Domain**, vous devez accéder aux options **Informations d'envoi** d'une campagne par e-mail et cocher la case **Customize from display name + address** (Personnaliser le nom d'affichage et l'adresse de l'expéditeur).

![Paramètres d'envoi avec des champs pour personnaliser le nom d'affichage, l'adresse et le domaine de l'expéditeur.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

Par exemple, vous pouvez utiliser la logique conditionnelle pour envoyer des messages provenant de différentes marques ou régions :

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

L'ajout d'une adresse e-mail dans cette section vous permet de la sélectionner en tant qu'adresse de réponse pour votre campagne par e-mail. Vous pouvez également définir une adresse e-mail par défaut en sélectionnant **Définir par défaut**. Ces adresses e-mail seront disponibles dans les options **Informations d'envoi** lorsque vous rédigerez votre campagne par e-mail.

![Section « Adresse de réponse » avec des champs permettant de saisir plusieurs adresses de réponse.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Personnalisation avec Liquid

Vous pouvez également utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) dans le champ **Adresse de réponse** pour générer dynamiquement l'adresse de réponse à partir d'attributs personnalisés. Par exemple, vous pouvez utiliser la logique conditionnelle pour diriger les réponses vers différentes régions ou différents services :

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@company.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@company.com" %}
{% else %}
{% assign address = "global-support@company.com" %}{% endif %}{{address}}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

Cette section vous permet de gérer les adresses CCI que vous pouvez ajouter aux e-mails sortants envoyés depuis Braze. Ajouter une adresse en CCI à un e-mail envoie une copie identique du message reçu par votre utilisateur vers votre boîte de réception CCI. Cet outil est utile pour conserver des copies des messages envoyés à vos utilisateurs à des fins de conformité ou d'assistance client. Les e-mails en CCI ne sont pas inclus dans les rapports et les analyses des e-mails.

Les adresses CCI ne sont disponibles que pour SendGrid et SparkPost. Comme alternative aux adresses CCI, nous vous recommandons d'utiliser l'[archivage des messages]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) pour enregistrer une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

![Section CCI de l'onglet Paramètres d'e-mail.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Une fois que vous avez ajouté une adresse, celle-ci sera disponible lors de la composition d'un e-mail dans les campagnes ou les étapes du canvas. Sélectionnez **Définir par défaut** à côté d'une adresse pour qu'elle soit sélectionnée par défaut lors du lancement d'une nouvelle campagne par e-mail ou d'un composant Canvas. Pour remplacer ce choix au niveau du message, vous pouvez sélectionner **Pas de CCI** lors de la configuration de votre message.

Si vous exigez que tous les e-mails envoyés depuis Braze incluent une adresse CCI, vous pouvez activer l'option **Exiger une adresse CCI pour toutes vos campagnes par e-mail**. Vous devrez alors sélectionner une adresse par défaut, qui sera automatiquement sélectionnée pour les nouvelles campagnes par e-mail ou étapes du canvas. L'adresse par défaut sera également automatiquement ajoutée à tous les messages déclenchés via notre API REST. Il n'est pas nécessaire de modifier la requête API existante pour inclure l'adresse.

#### CCI dynamique

Avec la fonction CCI dynamique, vous pouvez utiliser Liquid dans votre adresse CCI. Notez que cette fonctionnalité n'est disponible que dans les **Préférences des e-mails** et ne peut pas être configurée au niveau de la campagne. Une seule adresse CCI par destinataire d'e-mail est autorisée.

Par exemple, vous pouvez ajouter {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} comme adresse CCI pour les e-mails provenant de votre équipe d'assistance.

![Section Adresse CCI de l'onglet Paramètres d'e-mail avec une adresse CCI utilisant Liquid.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Pixel de suivi d'ouverture

[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Le pixel de suivi d'ouverture des e-mails est une image invisible de 1 x 1&nbsp;px automatiquement insérée dans le code HTML de votre e-mail. Ce pixel permet à Braze de détecter si vos utilisateurs ont ouvert votre e-mail. Lorsque le client de messagerie d'un utilisateur envoie une requête à notre pixel de suivi, cette requête peut contenir des informations telles que l'adresse IP, l'agent utilisateur et l'horodatage. Les informations relatives à l'ouverture des e-mails sont très utiles : elles vous aident à déterminer des stratégies marketing efficaces en vous permettant d'analyser les taux d'ouverture correspondants.

### Placement du pixel de suivi

Par défaut, Braze ajoute le pixel de suivi en bas de votre e-mail. Pour la grande majorité des utilisateurs, c'est l'endroit idéal. Bien que le pixel soit conçu pour provoquer le moins de différences visuelles possible, tout changement visuel involontaire sera le moins visible au bas de l'e-mail. C'est également le comportement par défaut des fournisseurs d'e-mail tels que SendGrid et SparkPost.

### Modification de l'emplacement du pixel de suivi

Braze permet de remplacer l'emplacement par défaut du pixel de suivi d'ouverture de l'ESP (la dernière balise dans le `<body>` d'un e-mail) pour le déplacer vers la première balise du `<body>`.
  
![Section « Open Tracking Pixel » avec les options de déplacement pour SendGrid, SparkPost ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Pour modifier l'emplacement :

1. Dans Braze, allez dans **Paramètres** > **Préférences des e-mails**.
2. Sélectionnez l'une des options suivantes : **Move for SendGrid**, **Move for SparkPost** ou **Move for Amazon SES**.
3. Sélectionnez **Enregistrer**.

Une fois l'enregistrement effectué, Braze envoie des instructions spécifiques à l'ESP afin de placer le pixel de suivi d'ouverture en haut de tous les e-mails HTML.
  
{% alert important %} 
L'activation SSL remplace le protocole HTTP par le protocole HTTPS dans l'URL du pixel de suivi. Si votre SSL est mal configuré, cela peut affecter l'efficacité du pixel de suivi. 
{% endalert %}

## En-tête list-unsubscribe {#list-unsubscribe}

{% alert note %}
Depuis le 15 février 2024, les nouvelles entreprises disposent par défaut de l'en-tête list-unsubscribe (avec désabonnement en un clic).
{% endalert %}

L'utilisation d'un en-tête list-unsubscribe permet à vos destinataires de se désabonner facilement des e-mails marketing en affichant un bouton **Se désabonner** dans l'interface de la boîte de réception, et non dans le corps du message.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Lorsqu'un destinataire sélectionne **Se désabonner**, le fournisseur de messagerie envoie la demande de désabonnement à l'adresse indiquée dans l'en-tête de l'e-mail.

L'activation du list-unsubscribe est une bonne pratique de livrabilité et une exigence chez certains des principaux fournisseurs de messagerie. Elle encourage les utilisateurs finaux à se retirer en toute sécurité des messages indésirables, plutôt que d'utiliser le bouton « spam » dans un client de messagerie, ce qui nuit à la réputation de l'expéditeur et à la livrabilité des e-mails.

Lorsque [vous gérez vos abonnements dans Gmail](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC), Gmail peut également extraire le lien de désabonnement du corps du message, mais donne la priorité au list-unsubscribe s'il est présent dans l'en-tête.

### Prise en charge par les fournisseurs de messagerie

Le tableau suivant résume la prise en charge par les fournisseurs de messagerie de l'en-tête « mailto: », de l'URL list-unsubscribe et du désabonnement en un clic ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| En-tête list-unsubscribe | En-tête Mailto: | URL list-unsubscribe | Désabonnement en un clic (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Pris en charge* | Pris en charge | Pris en charge |
| Gmail Mobile | Non pris en charge | Non pris en charge | Non pris en charge |
| Apple Mail | Pris en charge | Non pris en charge | Non pris en charge |
| Outlook.com | Pris en charge | Non pris en charge | Non pris en charge |
| Yahoo! Mail | Pris en charge* | Non pris en charge | Pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_*Yahoo et Gmail vont progressivement abandonner l'en-tête « mailto: » et ne prendront plus en charge que le clic unique._

L'affichage de l'en-tête est déterminé par le fournisseur de messagerie. Pour vérifier si l'en-tête list-unsubscribe est inclus dans l'e-mail brut (texte) pour le destinataire dans Gmail, procédez comme suit :

1. Sélectionnez **Afficher l'original** dans l'e-mail. Un nouvel onglet s'ouvre avec la version brute de l'e-mail et ses en-têtes.
2. Recherchez « List-Unsubscribe ».

Si l'en-tête figure dans la version brute de l'e-mail mais n'est pas affiché, le fournisseur de messagerie a décidé de ne pas afficher l'option de désabonnement, et nous n'avons pas d'informations supplémentaires sur la raison de ce choix. L'affichage de l'en-tête list-unsubscribe dépend de la réputation. Dans la plupart des cas, plus votre réputation d'expéditeur auprès du fournisseur de messagerie est bonne, plus l'en-tête list-unsubscribe est susceptible d'apparaître.

### En-tête de désabonnement par e-mail dans les espaces de travail

![Sélectionner les « utilisateurs abonnés ou ayant donné leur accord » auxquels envoyer le message.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Lorsque la fonctionnalité d'en-tête de désabonnement par e-mail est activée, ce paramètre s'applique à l'ensemble de l'espace de travail, et non au niveau de l'entreprise. Il est ajouté aux campagnes et aux Canvas configurés pour envoyer aux utilisateurs abonnés ou ayant donné leur accord, ou aux utilisateurs ayant donné leur accord, dans l'étape **Audience cible** des générateurs de campagnes et de Canvas.

Lorsque vous utilisez le « paramètre par défaut de l'espace de travail », Braze n'ajoute pas l'en-tête de désabonnement en un clic pour les campagnes considérées comme transactionnelles, c'est-à-dire configurées pour « envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés ». Pour passer outre et ajouter l'en-tête de désabonnement en un clic lors de l'envoi aux utilisateurs désabonnés, vous pouvez sélectionner **Se désabonner globalement de tous les e-mails** dans les paramètres de désabonnement en un clic au niveau du message.

### En-tête list-unsubscribe par défaut

{% alert important %}
Gmail souhaite que les expéditeurs mettent en œuvre le désabonnement en un clic pour tous leurs messages commerciaux et promotionnels sortants à compter du 1er juin 2024. Pour plus d'informations, consultez les [directives de Gmail relatives à l'expéditeur](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) et la [FAQ sur les directives de Gmail relatives aux expéditeurs d'e-mails](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo a annoncé un calendrier début 2024 pour la mise à jour de ses exigences. Pour plus d'informations, consultez [Plus de sécurité, moins de spam : Application des normes en matière d'e-mails pour une meilleure expérience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Pour utiliser la fonctionnalité de désabonnement de Braze afin de traiter directement les désabonnements, sélectionnez **Inclure un en-tête list-unsubscribe en un clic (mailto et HTTP) pour les e-mails envoyés aux utilisateurs abonnés ou ayant opté pour l'abonnement** et sélectionnez **Braze par défaut** comme URL et mail-to standard de Braze. 

![Option pour inclure automatiquement un en-tête list-unsubscribe pour les e-mails envoyés aux utilisateurs abonnés ou inscrits.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze prend en charge les versions suivantes de l'en-tête list-unsubscribe :

| Version list-unsubscribe | Description | 
| ----- | --- |
| Un clic (RFC 8058) | Offre aux destinataires un moyen simple de se désabonner des e-mails en un seul clic. Il s'agit d'une exigence de Yahoo et Gmail pour les expéditeurs d'e-mails en masse. |
| URL list-unsubscribe ou HTTPS | Fournit aux destinataires un lien qui les dirige vers une page web où ils peuvent se désabonner. |
| Mailto | Spécifie une adresse e-mail comme destination du message de demande de désabonnement envoyé par le destinataire à la marque. <br><br> _Pour traiter les demandes de désabonnement mailto, ces demandes doivent inclure l'adresse e-mail telle qu'elle est stockée dans Braze pour l'utilisateur final qui se désabonne. Cette information peut être fournie par l'adresse d'expédition (« from-address ») de l'e-mail à partir duquel l'utilisateur final se désabonne, l'objet encodé ou le corps encodé de l'e-mail reçu par l'utilisateur final. Dans des cas très limités, certains fournisseurs de boîtes de réception ne respectent pas le protocole [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), ce qui empêche la transmission correcte de l'adresse e-mail. La demande de désabonnement risque alors de ne pas pouvoir être traitée dans Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsque Braze reçoit une demande de désabonnement de liste de la part d'un utilisateur via l'une des méthodes ci-dessus, l'état d'abonnement global de cet utilisateur est défini sur « Désabonné ». En l'absence de correspondance, Braze ne traite pas cette demande.

### Désabonnement en un clic

Le désabonnement en un clic pour l'en-tête list-unsubscribe ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) vise à offrir aux destinataires un moyen simple de se désabonner des e-mails.

### Désabonnement list-unsubscribe en un clic au niveau du message

Le paramètre de désabonnement en un clic au niveau du message remplace la fonctionnalité d'en-tête de désabonnement par e-mail définie pour les espaces de travail. Appliquez le comportement de désabonnement en un clic par campagne ou par étape du canvas pour les cas suivants :

- Ajouter un désabonnement en un clic de Braze pour un groupe d'abonnement spécifique afin de prendre en charge plusieurs marques/listes au sein d'un même espace de travail
- Basculer entre le désabonnement par défaut de Braze et une URL personnalisée
- Ajouter votre URL de désabonnement en un clic personnalisée
- Omettre le désabonnement en un clic pour ce message

{% alert note %}
Le paramètre de désabonnement list-unsubscribe en un clic au niveau du message n'est disponible qu'avec l'éditeur par glisser-déposer et l'éditeur HTML mis à jour. Si vous utilisez l'ancien éditeur HTML, passez à l'éditeur HTML mis à jour pour utiliser cette fonctionnalité.
{% endalert %}

Dans votre éditeur d'e-mails, allez dans **Paramètres d'envoi** > **Informations d'envoi**. Sélectionnez l'une des options suivantes :

- **Utiliser l'espace de travail par défaut** : Utilise les paramètres de **l'en-tête de désabonnement par e-mail** définis dans les **Préférences des e-mails**. Toute modification apportée à ce paramètre s'applique à tous les messages.
- **Se désabonner globalement de tous les e-mails** : Utilise l'en-tête de désabonnement en un clic par défaut de Braze. Les utilisateurs qui cliquent sur le bouton « Se désabonner » voient leur statut d'abonnement global aux e-mails défini sur « Désabonné ».
- **Se désabonner d'un groupe d'abonnement spécifique** : Utilise le groupe d'abonnement spécifié. Braze désabonne du groupe d'abonnement sélectionné les utilisateurs qui cliquent sur le bouton « Se désabonner ».
    - Lors de la sélection d'un groupe d'abonnement, ajoutez le filtre **Groupe d'abonnement** dans **Audiences cibles** pour ne cibler que les utilisateurs abonnés à ce groupe spécifique. Le groupe d'abonnement sélectionné pour le désabonnement en un clic doit correspondre au groupe d'abonnement que vous ciblez. En cas d'incohérence, vous risquez d'envoyer un message à un utilisateur qui tente de se désabonner d'un groupe d'abonnement dont il s'est déjà désabonné.

{% alert important %}
Le paramètre **Se désabonner d'un groupe d'abonnement spécifique** s'applique uniquement à l'en-tête de désabonnement en un clic. L'en-tête mailto list-unsubscribe n'est pas affecté par cette option. Cela signifie qu'un destinataire qui se désabonne via cette méthode enregistre un désabonnement global, et non un désabonnement du groupe d'abonnement spécifique. Pour empêcher l'en-tête mailto list-unsubscribe de désabonner globalement les utilisateurs lorsque vous sélectionnez ce paramètre, contactez l'[assistance]({{site.baseurl}}/support_contact/).
{% endalert %}

- **Personnalisé** : Ajoute votre URL personnalisée de désabonnement en un clic vous permettant de traiter directement les demandes de désabonnement.
- **Exclure le désabonnement**

{% alert important %}
L'exclusion du désabonnement en un clic ou de tout mécanisme de désabonnement ne devrait s'appliquer qu'aux messages transactionnels, tels que les réinitialisations de mot de passe, les reçus et les e-mails de confirmation.
{% endalert %}

La modification de ce paramètre remplace le comportement par défaut du désabonnement list-unsubscribe en un clic pour cet e-mail.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Conditions requises

Si vous envoyez des e-mails avec votre propre fonctionnalité de désabonnement personnalisée, vous devez respecter les exigences suivantes pour que l'URL de désabonnement en un clic soit conforme à la RFC 8058 :

* L'URL doit être capable de gérer les requêtes POST de désabonnement.
* L'URL doit commencer par `https://`.
* L'URL ne doit pas renvoyer de redirection HTTPS ni de corps de réponse. Les liens de désabonnement en un clic qui mènent à une page de destination ou à un autre type de page web ne sont pas conformes à la RFC 8058.
* Les requêtes POST ne doivent pas définir de cookies.

Sélectionnez **En-tête list-unsubscribe personnalisé** pour ajouter votre propre endpoint de désabonnement en un clic, ainsi qu'un « mailto: » facultatif. Braze nécessite une URL pour prendre en charge un en-tête list-unsubscribe personnalisé, car le désabonnement en un clic via HTTP est une exigence de Yahoo et Gmail pour les expéditeurs d'e-mails en masse.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Ajout aux lignes d'objet des e-mails

Utilisez le bouton pour inclure « [TEST] » et « [SEED] » dans les lignes d'objet de vos e-mails de test et d'initiateur. Cela peut vous aider à identifier les campagnes par e-mail envoyées en tant que tests.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## Insertion CSS activée par défaut pour les nouveaux e-mails

L'insertion CSS est une technique qui intègre automatiquement les styles CSS dans vos e-mails et nouveaux e-mails. Pour certains clients de messagerie, cela peut améliorer le rendu de vos e-mails.

La modification de ce paramètre n'affecte aucun de vos messages e-mail ou modèles existants. Vous pouvez remplacer cette valeur par défaut à tout moment lors de la composition de vos messages ou modèles. Pour plus d'informations, reportez-vous à la section [Insertion CSS]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/).

## Réabonner les utilisateurs lorsque leur adresse e-mail change

Vous pouvez réabonner automatiquement les utilisateurs lorsqu'ils changent leur adresse e-mail. Par exemple, si un utilisateur d'espace de travail précédemment désabonné modifie son adresse e-mail pour une adresse qui ne figure pas sur la liste de désabonnement de Braze, il sera automatiquement réabonné.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Pages et pieds de page d'abonnement

{% tabs local %}
{% tab Custom Footer %}

Pour les e-mails commerciaux, la [loi CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que tous les e-mails commerciaux incluent une option de désabonnement. Grâce aux paramètres de pied de page personnalisés, vous pouvez rester conforme à la loi CAN-SPAM tout en personnalisant votre pied de page de désabonnement. Pour rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre des campagnes de cet espace de travail.

Notez les exigences suivantes lors de la création d'un pied de page personnalisé pour vos e-mails :
- Doit inclure une URL de désabonnement et une adresse postale physique.
- Doit faire moins de 100 Ko.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Pour en savoir plus sur la personnalisation des pieds de page avec Liquid, consultez notre documentation sur les [pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze vous permet de définir une **page de désabonnement personnalisée** avec votre propre HTML. Cette page s'affiche lorsqu'un utilisateur choisit de se désabonner au bas d'un e-mail. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Pour en savoir plus sur les bonnes pratiques de gestion des listes de diffusion, consultez [Gestion des abonnements aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

Vous pouvez créer une page d'abonnement personnalisée avec votre propre HTML. Inclure cette page dans votre e-mail peut être particulièrement utile si vous souhaitez que votre branding et vos messages restent cohérents tout au long du cycle de vie de votre utilisateur. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Pour en savoir plus sur les bonnes pratiques de gestion des listes de diffusion, consultez [Gestion des abonnements aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

{% alert tip %}
Dans la section **Aperçu** d'une page d'abonnement ou d'un pied de page, sélectionnez **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable montrant à quoi ressemble le pied de page de l'e-mail, la page de désabonnement ou la page d'abonnement pour un utilisateur aléatoire. Le lien est valable sept jours avant de devoir être régénéré.
{% endalert %}

## Foire aux questions

### Désabonnement en un clic

{% details L'URL de désabonnement en un clic (via l'en-tête list-unsubscribe) peut-elle renvoyer vers un centre de préférences ? %}
Non, cela ne respecte pas la RFC 8058, ce qui signifie que vous ne serez pas en conformité avec l'exigence de désabonnement en un clic de Yahoo et Gmail.
{% enddetails %}

{% details Pourquoi est-ce que je reçois le message d'erreur « Your email body does not include an unsubscribe link » lors de la composition de mon centre de préférences ? %}
Un centre de préférences n'est pas considéré comme un lien de désabonnement. Vos destinataires doivent avoir la possibilité de se désabonner de tout e-mail commercial pour rester conformes à la loi CAN-SPAM.
{% enddetails %}

{% details Dois-je modifier les campagnes par e-mail et les Canvas passés pour appliquer le paramètre de désabonnement en un clic après l'avoir activé ? %}
Si vous n'avez aucun des cas d'utilisation nécessitant le paramètre de désabonnement en un clic au niveau du message, aucune action n'est requise tant que le paramètre est activé dans les **Préférences des e-mails**. Braze ajoute automatiquement les en-têtes de désabonnement en un clic à tous les messages marketing et promotionnels sortants. Toutefois, si vous devez configurer le comportement de désabonnement en un clic au niveau de chaque message, vous devrez mettre à jour les campagnes précédentes et les étapes du canvas concernées.
{% enddetails %}

{% details Je peux voir l'en-tête list-unsubscribe et de désabonnement en un clic dans le message original ou les données brutes, mais pourquoi le bouton Se désabonner ne s'affiche-t-il pas dans Gmail ou Yahoo ? %}
Ce sont Gmail et Yahoo qui décident d'afficher ou non l'en-tête list-unsubscribe ou de désabonnement en un clic. Pour les nouveaux expéditeurs ou les expéditeurs dont la réputation est faible, il peut arriver que le bouton de désabonnement ne s'affiche pas. 
{% enddetails %}

{% details L'en-tête personnalisé de désabonnement en un clic prend-il en charge Liquid ? %}
Oui, Liquid et la logique conditionnelle sont pris en charge pour permettre des URL de désabonnement dynamiques en un clic dans l'en-tête.
{% enddetails %}

{% alert tip %}
Si vous ajoutez une logique conditionnelle, évitez les valeurs de sortie qui ajoutent des espaces à votre URL, car Braze ne supprime pas ces espaces.
{% endalert %}

### Désabonnement list-unsubscribe en un clic au niveau du message

{% details Si j'ajoute manuellement les en-têtes d'e-mail pour le désabonnement en un clic et que l'en-tête de désabonnement par e-mail est activé, quel est le comportement attendu ? %}
Les en-têtes d'e-mail ajoutés pour le désabonnement en un clic s'appliquent à tous les futurs envois de cette campagne.
{% enddetails %}

{% details Pourquoi les groupes d'abonnement doivent-ils correspondre entre les variantes de message pour pouvoir lancer la campagne ? %}
Dans le cadre d'une campagne avec test A/B, Braze envoie de manière aléatoire l'une des variantes à un utilisateur. Si deux groupes d'abonnement distincts sont définis pour une même campagne (la variante A est associée au groupe d'abonnement A et la variante B au groupe d'abonnement B), nous ne pouvons pas garantir que les utilisateurs abonnés uniquement au groupe d'abonnement B recevront la variante B. Il est possible que des utilisateurs se désabonnent d'un groupe d'abonnement dont ils se sont déjà désinscrits.
{% enddetails %}

{% details Le paramètre d'en-tête de désabonnement par e-mail est désactivé dans les Préférences des e-mails, mais dans les informations d'envoi de ma campagne, le paramètre de désabonnement en un clic est défini sur « Utiliser l'espace de travail par défaut ». Est-ce un bug ? %}
Non. Si le paramètre de l'espace de travail est désactivé et que le paramètre du message est défini sur **Utiliser l'espace de travail par défaut**, Braze suit la configuration définie dans les **Préférences des e-mails**. Cela signifie que l'en-tête de désabonnement en un clic n'est pas ajouté pour la campagne.
{% enddetails %}

{% details Que se passe-t-il si un groupe d'abonnement est archivé ? Cela casse-t-il le désabonnement en un clic sur les e-mails envoyés ? %}
Si un groupe d'abonnement référencé dans les **Informations d'envoi** pour le désabonnement en un clic est archivé, Braze continue de traiter les désabonnements en un clic. Le groupe d'abonnement n'apparaît plus sur le tableau de bord (filtre de segment, profil utilisateur et zones similaires).
{% enddetails %}

{% details Le paramètre de désabonnement en un clic est-il disponible pour les modèles d'e-mail ? %}
Non, nous ne prévoyons pas actuellement d'ajouter cette fonctionnalité pour les modèles d'e-mail, car ces modèles ne sont pas associés à un domaine d'envoi. Si cette fonctionnalité vous intéresse pour les modèles d'e-mail, soumettez vos [commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Cette fonctionnalité vérifie-t-elle que l'URL de désabonnement en un clic ajoutée à l'option personnalisée est valide ? %}
Non, nous ne vérifions ni ne validons aucun lien dans le tableau de bord de Braze. Assurez-vous de bien tester votre URL avant le lancement.
{% enddetails %}