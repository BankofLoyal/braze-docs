---
nav_title: Webhooks
article_title: Webhooks
page_order: 8
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Les webhooks sont un moyen courant pour les applications de communiquer entre elles et de partager des données en temps réel. Aujourd'hui, il est rare qu'une seule application autonome puisse tout faire. La plupart du temps, vous travaillez avec de nombreuses applications ou systèmes spécialisés dans certaines tâches, et ces applications doivent pouvoir communiquer entre elles. C'est là que les webhooks entrent en jeu. <br><br> Un webhook est un message automatisé envoyé d'un système à un autre lorsque certains critères sont remplis. Dans Braze, ce critère est généralement le déclenchement d'un événement personnalisé. <br><br>Fondamentalement, un webhook est une méthode événementielle permettant à deux systèmes distincts d'agir efficacement sur la base de données transmises en temps réel. Ce message contient des instructions indiquant au système destinataire quand et comment effectuer une tâche donnée. Grâce à cela, les webhooks vous offrent un accès plus dynamique et flexible aux données et aux fonctionnalités programmatiques, tout en vous permettant de mettre en place des parcours clients qui simplifient vos processus. <br><br>**La disponibilité des webhooks dépend de votre offre Braze. Contactez votre Account Manager ou votre Customer Success Manager pour commencer.**"
description: "Cette page d'accueil présente tout ce qui concerne les webhooks. Vous y trouverez des articles sur la création de webhooks, la création de modèles de webhooks et les webhooks Braze à Braze."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Section Articles"
guide_featured_list:
- name: Créer un webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Créer un modèle de webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Webhooks Braze à Braze
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Reporting
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Résolution des problèmes liés aux demandes de webhook
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Cas d'utilisation

Les webhooks sont un excellent moyen de connecter vos systèmes entre eux. Après tout, c'est comme ça que les applications communiquent. Voici quelques scénarios courants dans lesquels les webhooks peuvent s'avérer particulièrement utiles :

- Envoyer des données vers et depuis Braze
- Envoyer des messages à vos clients via des canaux qui ne sont pas directement pris en charge par Braze
- Publier vers les API de Braze

Voici quelques cas d'utilisation plus spécifiques :

- Si un utilisateur se désabonne de vos e-mails, un webhook peut mettre à jour votre base de données analytique ou votre CRM avec cette même information, vous offrant ainsi une vision globale du comportement de cet utilisateur.
- Envoyez des [messages transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) aux utilisateurs via Facebook Messenger ou Line.
- Envoyez du publipostage aux clients en réponse à leur activité in-app et web en utilisant des webhooks pour communiquer avec des services tiers comme [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Si un joueur atteint un certain niveau ou accumule un certain nombre de points, utilisez les webhooks et votre configuration API existante pour envoyer une amélioration de personnage ou des pièces directement sur son compte. Si vous envoyez le webhook dans le cadre d'une campagne de communication multicanale, vous pouvez également envoyer une notification push ou un autre message pour informer le joueur de sa récompense en même temps.
- Si vous êtes une compagnie aérienne, vous pouvez utiliser les webhooks et votre configuration API existante pour créditer le compte d'un client d'une réduction après qu'il a réservé un certain nombre de vols.
- Des recettes « If This Then That » ([IFTTT](https://ifttt.com/about)) à l'infini : par exemple, si un client se connecte à l'application par e-mail, cette adresse peut être automatiquement configurée dans Salesforce.

## Anatomie d'un webhook

Un webhook se compose des éléments suivants.

| Élément du webhook | Description |
| --- | --- |
| [Méthode HTTP](#methods) | Comme pour les API, les webhooks ont besoin de méthodes de requête. Elles sont transmises à l'URL ciblée par le webhook et indiquent à l'endpoint quoi faire avec les informations reçues. Vous pouvez spécifier quatre méthodes HTTP : POST, GET, PUT et DELETE. |
| URL HTTP | L'adresse URL de votre endpoint webhook. L'endpoint est l'endroit où vous enverrez les informations capturées par le webhook. |
| Corps de la requête | Cette partie du webhook contient les informations que vous transmettez à l'endpoint. Le corps de la requête peut contenir des paires clé-valeur JSON ou du texte brut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Exemple de webhook avec une méthode HTTP, une URL HTTP et un corps de requête.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Méthodes HTTP {#methods}

Le tableau suivant décrit les quatre méthodes HTTP que vous pouvez spécifier dans votre webhook.

| Méthode HTTP | Description |
| ----------- | ----------- |
| POST | Cette méthode écrit de nouvelles informations sur le serveur destinataire. Un exemple courant de la méthode POST est un [formulaire de contact](https://www.braze.com/company/contact) sur un site web. Les informations que vous saisissez dans le formulaire font partie du corps de la requête et sont envoyées à un récepteur. C'est la méthode la plus utilisée pour envoyer des données.
| GET | Cette méthode récupère des informations existantes, contrairement à l'écriture de nouvelles informations. Par définition, une requête GET ne comporte pas de corps de requête. C'est la méthode la plus courante pour demander des données à un serveur. Prenons l'exemple de l'[endpoint `/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si vous effectuez une requête GET, elle renvoie la liste de vos segments.
| PUT | Cette méthode met à jour les informations sur l'endpoint en remplaçant les informations existantes par le contenu du corps de la requête. 
| DELETE | Cette méthode supprime la ressource à l'URL HTTP indiquée. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Les webhooks dans Braze

Dans Braze, vous pouvez créer un webhook en tant que campagne webhook, campagne API ou composant Canvas.

{% tabs %}
{% tab Webhook Campaign %}

1. Dans le tableau de bord de Braze, accédez à **Campagnes**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Webhook**.

Pour plus d'informations, consultez [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab API Campaign %}

1. Dans le tableau de bord de Braze, accédez à **Campagnes**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Campagne API**.
3. Cliquez sur **Ajouter des messages** et sélectionnez **Webhook**.
4. Formulez votre appel API de manière à inclure un [objet webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Pour plus d'informations, consultez [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab Canvas Component %}

1. Créez un nouveau composant dans votre Canvas.
2. Dans la section **Message** de votre composant, sélectionnez **Webhook**.

Pour plus d'informations, consultez [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% endtabs %}

## Gestion des erreurs et limite de débit des webhooks

Lorsque Braze reçoit une réponse d'erreur suite à un appel webhook, le comportement d'envoi de ce webhook est automatiquement ajusté en fonction des en-têtes de réponse suivants :

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Ces en-têtes nous permettent d'interpréter les limites de débit et d'adapter la vitesse d'envoi en conséquence pour éviter d'autres erreurs. Nous appliquons également une stratégie de délais exponentiels pour les nouvelles tentatives, ce qui réduit le risque de saturation de vos serveurs en espaçant les tentatives dans le temps.

Si nous constatons que la majorité des demandes de webhook adressées à un hôte spécifique échouent, toutes les tentatives d'envoi vers cet hôte sont temporairement suspendues. L'envoi reprend après une période de pause définie, laissant le temps à votre système de se rétablir.