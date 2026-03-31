---
nav_title: "Messages in-app"
article_title: Messages in-app
page_order: 3
alias: /in-app_messages/
description: "Cette page d'accueil contient tout ce qui concerne les messages in-app. Vous y trouverez des articles sur la création de messages in-app, l'éditeur par glisser-déposer, la personnalisation de vos messages, la création de rapports, et bien plus encore."
channel:
  - in-app messages
search_rank: 5
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Messages in-app

> Les messages in-app vous permettent de transmettre du contenu à vos utilisateurs sans les interrompre avec une notification push, car ces messages ne sont pas diffusés en dehors de l'application et n'apparaissent pas sur leur écran d'accueil. 

Des messages in-app personnalisés et adaptés améliorent l'expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Grâce à un large choix de mises en page et d'outils de personnalisation, les messages in-app favorisent un engagement inédit de vos utilisateurs. Ils s'inscrivent dans un contexte, sont moins urgents et sont envoyés lorsque l'utilisateur est actif dans votre application. Pour des exemples de messages in-app, consultez nos [témoignages clients](https://www.braze.com/customers/).

## Cas d'utilisation

Grâce au contenu riche des messages in-app, vous pouvez exploiter ce canal pour une grande variété de cas d'utilisation :

| Cas d'utilisation | Explication |
| --- | --- |
| Amorçage de notification push | Lancez une campagne d'[amorçage de notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) à l'aide d'un message in-app riche afin de montrer à vos clients l'intérêt de s'abonner aux notifications push pour votre application ou votre site, et présentez-leur une invite pour autoriser les notifications push.
| Soldes et promotions | Utilisez des messages in-app modaux pour accueillir les clients avec des visuels attrayants contenant des codes de promotion ou des offres statiques. Incitez-les à effectuer des achats ou des conversions qu'ils n'auraient pas faits autrement. |
| Encouragement de l'adoption de fonctionnalités | Encouragez les clients à utiliser d'autres parties de votre application ou à profiter d'un service. |
| Campagnes hautement personnalisées | Placez des messages in-app de façon à ce que vos clients les voient dès qu'ils ouvrent votre application ou votre site. Ajoutez des fonctionnalités de personnalisation de Braze, telles que le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), pour inciter les utilisateurs à passer à l'action et ainsi rendre votre communication plus efficace.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Autres cas d'utilisation à considérer :

- Nouvelles fonctionnalités de l'application
- Gestion de l'application
- Avis
- Mises à niveau ou mises à jour de l'application
- Concours et tirages au sort

## Types de messages standard

Les onglets suivants montrent ce que vos utilisateurs voient lorsqu'ils ouvrent l'un de nos types de messages in-app standard : messages contextuels, modaux et plein écran.

{% tabs %}
{% tab Slideup %}

Les messages contextuels apparaissent généralement en haut ou en bas de l'écran de l'application (vous pouvez le définir lors de la création du message). Ils sont parfaits pour avertir vos utilisateurs de nouvelles conditions de service, de cookies et d'autres extraits d'information.

![Message in-app contextuel apparaissant en bas de l'écran de l'application. Le message contextuel comprend une icône et un message succinct.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Les fenêtres modales apparaissent au centre de l'écran de l'appareil avec une incrustation qui les démarque de votre application en arrière-plan. Elles sont parfaites pour suggérer à votre utilisateur de profiter d'une vente ou d'un concours, sans trop de subtilité.

![Message in-app modal apparaissant au centre d'une application et d'un site Web sous forme de boîte de dialogue. La fenêtre modale comprend une image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

Comme leur nom l'indique, les messages plein écran occupent tout l'écran de l'appareil ! Ce type de message est idéal lorsque vous avez vraiment besoin de toute l'attention de votre utilisateur, par exemple pour des mises à jour obligatoires de l'application.

![Message in-app plein écran sur un écran d'application. Le message plein écran comprend une grande image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

En plus de ces modèles de messages par défaut, vous pouvez également personnaliser davantage votre envoi de messages à l'aide de messages in-app HTML personnalisés, de fenêtres modales avec CSS ou de formulaires de capture d'e-mails Web. Pour plus d'informations, reportez-vous à la rubrique [Personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Messages in-app basés sur des modèles

Les messages in-app sont envoyés sous forme de messages in-app basés sur des modèles lorsque l'option **Réévaluer l'éligibilité à la campagne avant l'affichage** est sélectionnée ou si l'une des étiquettes Liquid suivantes est présente dans le message :

- `canvas_entry_properties`
- `connected_content`
- Les variables SMS telles que {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Cela signifie que lors du démarrage de la session, l'appareil recevra le déclencheur de ce message in-app au lieu du message complet. Lorsque l'utilisateur déclenche le message in-app, l'appareil effectue une requête réseau pour récupérer le message réel.

{% alert note %}
Le message ne sera pas transmis si l'appareil n'a pas accès à Internet. Le message pourrait ne pas être transmis si la logique Liquid prend trop de temps à se résoudre.
{% endalert %}

## Comportement d'abandon

Chez Braze, un abandon se produit lorsqu'un utilisateur effectue une action qui le rend éligible à recevoir un message, mais qu'il ne reçoit pas ce message car la logique Liquid le marque comme non éligible. Par exemple :

1. Sam effectue une action qui devrait déclencher une campagne par e-mail.
2. Le corps de l'e-mail contient une logique Liquid qui indique que si le score d'un attribut personnalisé est inférieur à 50, cet e-mail ne doit pas être envoyé.
3. Le score de l'attribut personnalisé de Sam est de 20.
4. Braze identifie que Sam ne devrait pas recevoir cet e-mail, et l'envoi de l'e-mail est abandonné.
5. Un événement d'abandon est enregistré.

Cependant, étant donné que les messages in-app constituent un canal de type « pull », les abandons fonctionnent de manière légèrement différente pour ceux-ci.

### Comportement d'abandon des messages in-app

Les messages in-app sont récupérés par l'appareil au début de la session et mis en cache localement. Ainsi, quelle que soit la qualité de la connexion Internet, le message peut être transmis instantanément à l'utilisateur. Par exemple, si un utilisateur reçoit cinq messages in-app au cours de sa session, il les recevra tous les cinq au début de la session. Les messages seront mis en cache localement et apparaîtront lorsque les événements déclencheurs définis se produiront (début de session, clic de l'utilisateur sur un bouton qui enregistre un événement personnalisé, ou autre).

En d'autres termes, la logique qui détermine si un message in-app doit être abandonné intervient **avant** que le déclencheur ne se produise. Pour illustrer cela, supposons que Sam, dans l'exemple de l'e-mail, soit abonné aux notifications push.

1. Sam commence une session en lançant une application propulsée par Braze sur son téléphone.
2. En fonction des critères d'audience des campagnes actives dans l'espace de travail, Sam pourrait être éligible à cinq campagnes différentes. Les cinq sont récupérées sur son téléphone et mises en cache.
3. Sam **n'a** effectué aucune action susceptible de déclencher ces messages, mais il pourrait les recevoir au cours de la session.
4. La logique Liquid de deux des messages in-app comporte des règles qui empêchent Sam de recevoir le message (par exemple, son attribut personnalisé de score n'est pas suffisamment élevé).
5. Sam ne reçoit pas les deux messages in-app qui l'excluent, mais il reçoit les trois autres.
6. Aucun événement d'abandon n'est enregistré.

Braze n'enregistre aucun événement d'abandon dans le cas de Sam, car cela ne correspond pas à notre définition d'un abandon : Sam **n'a** effectué aucune action susceptible de déclencher ces messages. Pour les messages in-app, les utilisateurs n'effectuent jamais réellement l'action de déclenchement avant que Braze ne détermine qu'ils ne devraient pas voir le message.

#### Comportement d'abandon des messages in-app basés sur des modèles

[Les messages in-app basés sur des modèles](#templated-in-app-messages) forcent le SDK à réévaluer si un message doit s'afficher lorsque l'événement déclencheur se produit. Le comportement d'abandon est donc différent. Pour illustrer cela, examinons l'exemple suivant :

1. Sam commence une session Braze en lançant une application propulsée par Braze sur son téléphone.
2. Les critères d'audience des campagnes actives indiquent que Sam pourrait être éligible pour recevoir un message in-app basé sur un modèle. Les informations de déclencheur sont donc envoyées à son appareil sans le contenu du message.
3. Sam appuie sur un bouton qui enregistre un événement personnalisé, déclenchant ainsi le message in-app basé sur un modèle.
4. L'appareil de Sam effectue une requête réseau pour récupérer le message in-app.
5. La logique Liquid du message entraîne un abandon. Braze enregistre donc cela comme un abandon, car Sam a effectué l'action de déclenchement avant cette évaluation.

##### Comparaison du comportement d'abandon des messages in-app

Ce tableau compare les flux de messages in-app que Sam a rencontrés :

| Message in-app | Comportement d'abandon |
| --- | --- |
| Standard | Aucun événement d'abandon n'a été enregistré, car Sam n'a effectué aucune action susceptible de déclencher un message.<br><br>Les messages in-app standard n'enregistrent pas les abandons, car la définition d'un abandon est « ne pas avoir vu le message malgré l'exécution de l'action de déclenchement ». Étant donné que les messages in-app sont envoyés à l'appareil avant que les actions de déclenchement ne se produisent, il n'est pas pertinent de considérer que les messages in-app sont omis en raison de la logique Liquid. |
| Basé sur un modèle | Un événement d'abandon a été enregistré car Sam a effectué l'action de déclenchement pour déclencher le message in-app basé sur un modèle, mais a reçu un abandon lors de l'évaluation du modèle Liquid. <br><br>Les messages in-app basés sur des modèles enregistrent les abandons car l'évaluation Liquid se produit après l'exécution de l'action de déclenchement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ressources supplémentaires

Avant de vous lancer dans la création de vos propres campagnes de messages in-app — ou dans l'utilisation de messages in-app dans le cadre d'une campagne multicanal — nous vous recommandons vivement de consulter notre [guide de préparation des messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). Ce guide couvre les questions de ciblage, de contenu et de conversion à prendre en compte lors de la création de messages in-app.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}