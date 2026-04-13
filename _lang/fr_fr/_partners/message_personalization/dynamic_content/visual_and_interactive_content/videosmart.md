---
nav_title: VideoSmart
article_title: VideoSmart
description: "Cet article de référence décrit le partenariat entre Braze et VideoSmart, une technologie de vidéo personnalisée et interactive qui permet aux marques de diffuser du contenu non linéaire basé sur les données, à grande échelle."
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/) fournit une technologie de vidéo personnalisée et interactive qui vous permet de diffuser du contenu non linéaire basé sur les données, à grande échelle. Chaque vidéo est générée dynamiquement à partir de données au niveau du client, ce qui permet d'adapter les messages et les parcours utilisateur au sein d'une seule expérience vidéo.
>
> L'intégration VideoSmart vous permet d'intégrer du contenu vidéo personnalisé dans vos campagnes e-mail en utilisant le contenu connecté de Braze et le templating Liquid pour demander des ressources vidéo à VideoSmart. Cette intégration est généralement mise en œuvre via un modèle de bloc de contenu Braze réutilisable, ce qui permet un déploiement cohérent entre les campagnes tout en offrant de la flexibilité dans la sélection des campagnes et la logique de personnalisation.

_Cette intégration est développée et maintenue par VideoSmart._

## À propos de cette intégration

VideoSmart s'intègre à Braze pour générer dynamiquement des ressources vidéo personnalisées au moment de l'envoi, qui sont ensuite intégrées directement dans le contenu e-mail de vos campagnes et Canvas Braze.

Dans Braze, vous sélectionnez la campagne VideoSmart correspondante et transmettez les attributs client (via le templating Liquid) à VideoSmart lors de l'envoi. Ces attributs sont utilisés pour produire une expérience vidéo unique et personnalisée pour chaque destinataire. Vous pouvez ensuite utiliser le contenu connecté de Braze pour demander des URL ou des ressources vidéo à l'API de VideoSmart en temps réel, ce qui permet une personnalisation à grande échelle.

Cette intégration est conçue pour les messages e-mail Braze prenant en charge le templating Liquid et le contenu connecté. Elle peut être configurée pour fonctionner avec les attributs standard du profil utilisateur Braze ou avec des champs de données personnalisés.

## Cas d'utilisation

Les cas d'utilisation courants incluent les suivants :

- Onboarding client et parcours de bienvenue
- Éducation financière (comme les retraites et les polices d'assurance)
- Relevés annuels et communications réglementaires
- Campagnes de notoriété produit et de vente croisée
- Campagnes de rétention client et de réengagement
- Rappels de panier abandonné : lorsqu'un client ajoute des produits à son panier sans finaliser l'achat, vous envoyez un e-mail avec une vidéo personnalisée mettant en avant les articles laissés de côté
- Suivi post-achat : après un achat, envoyez une vidéo de remerciement personnalisée et recommandez des produits associés

## Conditions préalables

Avant de commencer, vérifiez que vous disposez des éléments suivants :

| Condition                          | Description                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Identifiants de contenu connecté Braze | Un identifiant d'authentification basique de contenu connecté nommé **basic_credentials**, configuré avec les valeurs fournies par VideoSmart |
| Modèle de **bloc de contenu VideoSmart**   | Le modèle de **bloc de contenu VideoSmart** ajouté à votre tableau de bord de Braze (fourni par VideoSmart)                                |
| Un message e-mail Braze               | Un e-mail de campagne Braze ou une étape e-mail Canvas dans lequel vous insérerez le **bloc de contenu VideoSmart**                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Suivez ces étapes pour activer le **bloc de contenu VideoSmart** et l'utiliser dans un e-mail.

### Étape 1 : Configurer le modèle de bloc de contenu VideoSmart dans Braze

Demandez le modèle de **bloc de contenu VideoSmart** à votre conseiller VideoSmart et ajoutez-le à votre tableau de bord de Braze.

VideoSmart fournira les identifiants pour l'authentification du contenu connecté utilisée par le bloc de contenu.

### Étape 2 : Configurer l'authentification du contenu connecté

Créez un identifiant d'authentification basique de contenu connecté dans Braze nommé « basic_credentials ».

- Suivez les instructions de la section [Utiliser l'authentification basique]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#using-basic-authentication).
- Utilisez le nom d'utilisateur et le mot de passe fournis par VideoSmart.

### Étape 3 : Ajouter le bloc de contenu à votre e-mail

Insérez le **bloc de contenu VideoSmart** dans votre e-mail à l'endroit où vous souhaitez que le contenu vidéo apparaisse.

Dans la plupart des configurations Braze, les blocs de contenu sont référencés selon le schéma suivant (remplacez « VideoSmart_Campaign » par le nom du bloc de contenu dans votre compte) :

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
Le nom du bloc de contenu est sensible à la casse et doit correspondre exactement à ce que vous avez configuré dans Braze.
{% endalert %}

### Étape 4 : Remplacer la campagne et les données d'enregistrement (facultatif)

Si votre bloc de contenu prend en charge des valeurs par défaut, vous pouvez l'utiliser sans définir de variables.

Si vous devez choisir une campagne VideoSmart spécifique, transmettre des champs de personnalisation personnalisés, ou les deux, définissez les variables Liquid suivantes avant le rendu du bloc de contenu :

- `vs_campaign_id` : identifiant de la campagne VideoSmart
- `vs_record_data` : une chaîne de caractères JSON contenant les valeurs que vous souhaitez transmettre au modèle VideoSmart

#### Exemple

Cet exemple utilise les attributs utilisateur Braze pour le prénom et le nom de famille :

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'John' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Fournissez toujours des valeurs par défaut pour les données utilisées dans `vs_record_data` afin que la prévisualisation de votre e-mail Braze s'affiche correctement.
- `vs_record_data` doit être un JSON valide, encodé sous forme d'une seule chaîne de caractères (l'exemple utilise `strip_newlines`).
{% endalert %}

### Étape 5 : Utiliser les variables générées par le modèle de bloc de contenu VideoSmart

Après l'exécution du bloc de contenu, celui-ci génère des variables que vous pouvez référencer ailleurs dans votre e-mail.

Les variables courantes incluent :

{% raw %}
| Variable                          | Description                                           |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}`                 | URL de la vidéo personnalisée                         |
| `{{ poster_url }}`                | URL de l'image d'aperçu de la vidéo                   |
| `{{ output_data.VARIABLE_NAME }}` | Champs de sortie supplémentaires exposés par le bloc de contenu |
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limites de débit

L'API de VideoSmart a une limite de débit de 10 000 requêtes par minute. Si vous dépassez cette limite, vous pourriez recevoir des erreurs ou constater des retards dans la génération des vidéos.

Pour réduire ce risque, configurez la limitation de débit de votre campagne Braze afin que le rythme d'envoi des messages reste en dessous de la capacité de l'API VideoSmart.

Pour en savoir plus sur la vitesse de distribution et la limitation de débit dans Braze, consultez [Vitesse de distribution et limitation de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting).

## Points à prendre en compte

- Le contenu connecté est exécuté au moment du rendu du message. Les valeurs peuvent donc différer entre la prévisualisation et l'envoi si vos valeurs par défaut ou vos attributs sont différents.
- Vérifiez que votre e-mail inclut le bloc de contenu avant de référencer des variables comme `video_url`.
- Si vous utilisez des champs personnalisés dans `vs_record_data`, confirmez les noms de champs attendus auprès de VideoSmart.

## Résolution des problèmes

### La prévisualisation ne fonctionne pas

Si la prévisualisation Braze échoue (par exemple, tentatives répétées ou erreurs d'authentification), vérifiez que :

- L'identifiant de contenu connecté « basic_credentials » existe et est correctement configuré.
- Le modèle de **bloc de contenu VideoSmart** est présent dans votre compte Braze.
- Toutes les variables requises (par exemple, `vs_campaign_id` ou les champs requis dans `vs_record_data`) ont des valeurs par défaut définies pour la prévisualisation.

### Les variables du modèle de bloc de contenu VideoSmart ne produisent pas le résultat attendu

Si les variables générées par le modèle de bloc de contenu VideoSmart ne produisent pas le résultat attendu, vérifiez les points suivants :

- Le modèle de **bloc de contenu VideoSmart** est correctement configuré dans Braze.
- L'authentification du contenu connecté est correctement configurée avec les identifiants appropriés.
- Affichez les variables dans votre e-mail pour confirmer qu'elles sont bien définies. Par exemple : `{% raw %}{{ video_url }}{% endraw %}`

Si vous utilisez une campagne personnalisée, vérifiez également que :

- `vs_campaign_id` est défini avec un identifiant de campagne valide.
- `vs_record_data` est un JSON valide et contient les champs attendus.