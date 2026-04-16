---
nav_title: Recommandations d'articles
article_title: Recommandations d'articles dans Braze
page_order: 10
search_rank: 1
description: "Découvrez les moteurs de recommandation d'articles dans Braze."
---

# Recommandations d'articles

> Passez au niveau supérieur en matière de recommandations avec Braze en créant un moteur de recommandation capable de suggérer à vos utilisateurs des articles et du contenu qui les intéressent vraiment. De la personnalisation des expériences grâce à l'intelligence artificielle à la création de vos propres moteurs avec Liquid ou le contenu connecté, vous trouverez tout ce qu'il faut pour que chaque recommandation compte.

## Conditions préalables

Avant de pouvoir créer ou utiliser des recommandations d'articles dans Braze, vous devez [créer au moins un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)&#8212;seuls les articles de ce catalogue seront recommandés aux utilisateurs.

## Types et cas d'utilisation

### IA personnalisée {#ai}

Dans le cadre de la fonctionnalité de [recommandations d'articles par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/), les recommandations IA personnalisées exploitent l'apprentissage profond pour prédire ce qui est susceptible d'intéresser vos utilisateurs ensuite, en fonction de ce qui les a intéressés par le passé. Cette méthode fournit un système de recommandation dynamique et sur mesure qui s'adapte au comportement de l'utilisateur.

Les recommandations IA personnalisées utilisent les 6 derniers mois de données d'interaction avec les articles, comme les achats ou les événements personnalisés, pour construire le modèle de recommandation. Pour les utilisateurs ne disposant pas de suffisamment de données pour une liste personnalisée, les articles les plus populaires servent de solution de repli, afin que vos utilisateurs continuent de recevoir des suggestions pertinentes.

Grâce aux recommandations d'articles par IA, vous pouvez également affiner les articles disponibles avec les
[sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/). Cependant, les sélections utilisant Liquid ne peuvent pas être employées dans les recommandations IA — gardez cela à l'esprit lorsque vous créez vos sélections de catalogue.

{% alert tip %}
Les recommandations IA personnalisées fonctionnent au mieux avec des centaines ou des milliers d'articles et généralement au moins 30 000 utilisateurs disposant de données d'achat ou d'interaction. Il s'agit d'une indication approximative qui peut varier. Les autres types de recommandations peuvent fonctionner avec moins de données.
{% endalert %}

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure :

{% tabs local %}
{% tab Most likely to purchase next %}
Prédire et recommander les articles qu'un utilisateur est le plus susceptible d'acheter ensuite, en fonction des événements d'achat ou des événements personnalisés liés aux achats. Par exemple :

- Un site de voyage pourrait suggérer des forfaits vacances, des vols ou des séjours à l'hôtel en fonction de l'historique de navigation de l'utilisateur et de ses réservations précédentes, anticipant ainsi sa prochaine destination et facilitant l'organisation de son séjour.
- Une plateforme de streaming peut analyser les habitudes de visionnage pour recommander des émissions ou des films qu'un utilisateur est le plus susceptible de regarder ensuite, maintenant ainsi son engagement et réduisant le taux d'attrition.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Une méthode de suivi des achats, soit un objet d'achat, soit un événement personnalisé
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **IA personnalisée**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez la manière dont vous suivez actuellement les événements d'achat et la propriété d'événement correspondante.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations/)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Article le plus populaire {#most-popular}

Le modèle de recommandation « Les plus populaires » met en avant les articles avec lesquels les utilisateurs interagissent le plus.

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation de :

{% tabs local %}
{% tab most popular %}
Encouragez les utilisateurs à explorer les articles populaires de votre catalogue en fonction des achats. Pour vous assurer de ne mettre en avant que du contenu pertinent, nous vous recommandons de filtrer à l'aide d'une sélection. Par exemple, un service de livraison de repas pourrait mettre en avant les plats ou les restaurants les mieux notés dans la zone d'un utilisateur, en fonction de la popularité des commandes sur la plateforme, encourageant ainsi l'essai et la découverte.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Un objet d'achat ou tout événement personnalisé
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus populaires**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents. Par exemple, le service de livraison de repas pourrait proposer une sélection pour filtrer par emplacement du restaurant ou type de plat.
5. Choisissez la manière dont vous suivez actuellement les événements et la propriété d'événement correspondante.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab most liked %}
Encouragez les utilisateurs à explorer les articles qu'ils ont récemment aimés ou les articles populaires, sur la base d'un événement personnalisé pour les likes. Par exemple, une application de streaming musical pourrait créer des playlists personnalisées ou suggérer de nouvelles sorties d'albums en fonction des genres ou des artistes qu'un utilisateur a aimés par le passé, améliorant ainsi l'engagement et le temps passé sur l'application.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Événement personnalisé pour les likes
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus récents**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les likes dans la liste.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab most viewed %}
Mettez en avant les articles qui ont attiré l'attention de votre base d'utilisateurs grâce aux vues, afin d'encourager l'engagement ou les achats. Par exemple, un site immobilier pourrait afficher les annonces les plus consultées dans la zone de recherche d'un utilisateur pour mettre en évidence les biens qui attirent beaucoup d'attention, signalant potentiellement de bonnes affaires ou des emplacements recherchés.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Événement personnalisé pour les vues
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus populaires**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les vues dans la liste.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
Mettez en avant les articles ajoutés au panier par de nombreux autres acheteurs, offrant ainsi aux utilisateurs un aperçu des tendances actuelles parmi vos produits.

Par exemple, un détaillant de mode pourrait promouvoir des vêtements et des accessoires tendance en se basant sur les ajouts fréquents au panier par d'autres clients. Il peut ensuite créer une section dynamique « Tendances du moment » sur sa page d'accueil et son application mobile, mise à jour en temps réel pour encourager les acheteurs à passer commande avant que les articles ne soient épuisés.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Événement personnalisé pour l'ajout au panier
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus populaires**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour l'ajout au panier dans la liste.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Article le plus récent {#most-recent}

Le modèle de recommandation « Les plus récents » met en avant les articles avec lesquels les utilisateurs interagissent le plus. Utilisez ce modèle pour réduire l'attrition en encourageant les utilisateurs inactifs à se réengager avec du contenu pertinent.

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation de :

{% tabs local %}
{% tab Recently clicked %}
Encouragez les utilisateurs à revenir sur les articles sur lesquels ils ont récemment cliqué, en vous appuyant sur un événement personnalisé pour les clics. Par exemple, un détaillant de mode en ligne pourrait créer une recommandation pour envoyer des e-mails de suivi ou des notifications push présentant des vêtements pour lesquels un utilisateur a montré de l'intérêt en cliquant dessus, l'encourageant ainsi à revenir sur l'article et à effectuer un achat.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Événement personnalisé pour les clics
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus récents**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les clics dans la liste.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
Encouragez les utilisateurs à explorer les articles qu'ils ont récemment aimés ou les articles populaires, sur la base d'un événement personnalisé pour les likes. Par exemple, une application de streaming musical pourrait créer des playlists personnalisées ou suggérer de nouvelles sorties d'albums en fonction des genres ou des artistes qu'un utilisateur a aimés par le passé, améliorant ainsi l'engagement et le temps passé sur l'application.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Événement personnalisé pour les likes
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus récents**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les likes dans la liste.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
Mettez en avant les articles avec lesquels les utilisateurs ont récemment interagi, qu'il s'agisse de vues, de clics ou d'achats. Cette approche permet de garder vos recommandations à jour et alignées sur les derniers centres d'intérêt de l'utilisateur. Par exemple :

- **Éducation :** Une plateforme d'éducation en ligne pourrait encourager les utilisateurs qui ont récemment regardé une vidéo éducative mais ne se sont pas inscrits à un cours à consulter des cours similaires ou des sujets d'intérêt, afin de maintenir leur engagement et de les motiver à commencer l'apprentissage.
- **Remise en forme :** Une application de fitness peut suggérer des entraînements ou des défis similaires à ceux que l'utilisateur a récemment effectués ou avec lesquels il a interagi, ce qui lui permet de varier son programme d'exercices et de rester motivé.
- **Bricolage et rénovation :** Après l'achat d'un outil électrique par un client, un détaillant de bricolage peut lui recommander des accessoires associés ou des équipements de sécurité en fonction de son achat récent, améliorant ainsi l'expérience et la sécurité de l'utilisateur.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Un objet d'achat ou tout événement personnalisé pour une interaction d'engagement
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus récents**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les clics dans la liste.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab Recently added %}
Rappelez aux utilisateurs leur intérêt pour les articles qu'ils ont récemment ajoutés à leur panier mais qu'ils n'ont pas encore achetés. Par exemple, un détaillant en ligne pourrait envoyer des rappels ou proposer des réductions à durée limitée sur les articles de leur panier, encourageant ainsi les utilisateurs à finaliser leurs achats avant l'expiration des offres.
{% details Requirements %}

- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Événement personnalisé pour l'ajout au panier
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/).
2. Définissez le **Type** sur **Les plus récents**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour l'ajout au panier dans la liste.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Article en vogue {#trending}

Le modèle de recommandation « Tendances » met en avant les articles ayant connu la dynamique positive la plus forte dans les interactions récentes des utilisateurs. Ce calcul repose sur une analyse pondérée d'environ 10 semaines d'historique d'événements, la pondération la plus importante étant appliquée aux 2 dernières semaines environ. Afin d'éviter que de petites fluctuations n'affectent la qualité des recommandations, nous appliquons un seuil d'activité et des techniques de lissage statistique.

Contrairement au modèle « Les plus populaires », qui met en avant des articles avec un taux d'interaction élevé et constant, ce modèle présente des articles ayant connu une hausse des interactions. Vous pouvez l'utiliser pour recommander des produits émergents qui bénéficient actuellement d'un regain de popularité.

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation de :

{% tabs local %}
{% tab Trending purchased %}
Mettez en évidence les articles que vos utilisateurs ont récemment achetés avec une fréquence accrue. Par exemple, une entreprise d'e-commerce pourrait recommander des articles saisonniers que les utilisateurs commencent à stocker en prévision de la prochaine saison. 

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Une méthode de suivi des achats (soit un objet d'achat, soit un événement personnalisé)
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/ai_item_recommendations/).
2. Définissez le **Type** sur **Tendances**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez un événement d'achat ou un événement personnalisé qui suit les achats, ainsi que la propriété correspondante.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
Mettez en évidence les articles que vos utilisateurs ont récemment aimés de manière plus fréquente. Par exemple, une application musicale pourrait mettre en avant des artistes émergents ayant connu une hausse récente du nombre de likes.

{% details Requirements %}
- Recommandations d'articles par IA
- Catalogue d'articles pertinents
- Événement personnalisé pour le suivi des likes
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article par IA]({{site.baseurl}}/ai_item_recommendations/).
2. Définissez le **Type** sur **Tendances**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les articles pertinents.
5. Choisissez votre événement personnalisé pour le suivi des likes, ainsi que la propriété correspondante.
6. Entraînez la recommandation.
7. [Utilisez la recommandation dans vos messages.]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basé sur des sélections {#selections-based}

Les [sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) sont des groupes spécifiques de données du catalogue. Lorsque vous utilisez une sélection, vous configurez essentiellement des filtres personnalisés basés sur des colonnes spécifiques de votre catalogue. Il peut s'agir de filtres pour la marque, la taille, l'emplacement, la date d'ajout, etc. Cela vous donne le contrôle sur ce que vous recommandez en vous permettant de définir les critères auxquels les articles doivent répondre pour être présentés aux utilisateurs.

Les trois types précédents impliquent tous la configuration et l'entraînement d'un modèle de recommandation dans Braze. Bien que vous puissiez également utiliser des sélections dans ces modèles, vous pouvez aussi réaliser certains cas d'utilisation de recommandation avec uniquement des sélections de catalogue et la personnalisation Liquid.

{% alert note %}
Si vous utilisez des sélections, le champ de tri et les limites ne seront pas pris en compte dans les recommandations d'articles par IA. Cela signifie que si vous créez une sélection avec un champ de tri spécifique et limitez le nombre d'articles renvoyés, ces contraintes ne seront pas utilisées lors du traitement des recommandations d'articles par IA.
{% endalert %}

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation de :

{% tabs local %}
{% tab New items %}
Ce scénario ne repose pas directement sur les actions de l'utilisateur mais plutôt sur les données du catalogue. Vous pouvez filtrer les nouveaux articles en fonction de leur date d'ajout au catalogue et les promouvoir par le biais de campagnes ciblées ou de Canvas sans avoir besoin d'entraîner un modèle de recommandation.

Par exemple, une plateforme d'e-commerce technologique pourrait alerter les passionnés de technologie sur les derniers gadgets ou les précommandes à venir, en utilisant des filtres pour cibler les articles récemment ajoutés au catalogue.

{% details Requirements %}
- Catalogue d'articles pertinents avec un champ pour la date d'ajout
{% enddetails %}

{% details Setting it up %}
1. Créez une sélection à partir de votre catalogue. Assurez-vous que votre catalogue dispose d'un champ temporel (champ dont le **type de données** est défini sur **Temps**) correspondant à la date d'ajout de l'article.
2. (Facultatif) Ajoutez des filtres si vous le souhaitez.
3. Assurez-vous que l'option **Randomiser l'ordre de tri** est désactivée.
4. Pour **Champ de tri**, sélectionnez votre champ de date d'ajout.
5. Définissez l'**Ordre de tri** sur décroissant.
6. [Utilisez la sélection dans vos messages.]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Random items %}
Pour une expérience utilisateur diversifiée, recommander des articles aléatoires peut introduire de la variété et potentiellement susciter de l'intérêt pour des parties moins visitées du catalogue. Cette méthode ne nécessite pas de modèles ou d'événements spécifiques, mais utilise plutôt une sélection de catalogue pour s'assurer que les articles sont affichés de manière aléatoire.

Par exemple, une librairie en ligne pourrait proposer une fonctionnalité « Surprenez-moi », recommandant un livre au hasard en fonction des achats antérieurs de l'utilisateur ou de ses habitudes de navigation, encourageant ainsi l'exploration en dehors de ses genres de lecture habituels.

{% details Requirements %}
- Catalogue d'articles pertinents
- Sélection avec l'option **Randomiser l'ordre de tri** activée
{% enddetails %}

{% details Setting it up %}
1. [Créez une sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection) à partir de votre catalogue.
2. (Facultatif) Ajoutez des filtres si vous le souhaitez.
3. Activez l'option **Randomiser l'ordre de tri**.
4. [Utilisez la sélection dans vos messages.]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basé sur des règles {#rules-based}

Un moteur de [recommandation basé sur des règles]({{site.baseurl}}/rules_based_recommendations/) utilise les données des utilisateurs et les informations sur les produits pour suggérer des articles pertinents aux utilisateurs dans les messages. Il utilise Liquid et les catalogues Braze ou le contenu connecté pour personnaliser dynamiquement le contenu en fonction du comportement et des attributs de l'utilisateur.

Les recommandations basées sur des règles reposent sur une logique fixe que vous devez définir manuellement. Cela signifie que vos recommandations ne s'adapteront pas à l'historique d'achat et aux goûts individuels d'un utilisateur, à moins que vous ne mettiez à jour la logique. Cette méthode est donc idéale pour les recommandations qui ne nécessitent pas de mises à jour fréquentes.

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure :

- **Rappels de réapprovisionnement :** Envoi de rappels de réapprovisionnement pour les articles dont le cycle d'utilisation est prévisible, comme les vitamines mensuelles ou les courses hebdomadaires, en fonction de la dernière date d'achat.
- **Premiers acheteurs :** Recommandez des kits de démarrage ou des offres de lancement aux premiers acheteurs afin de les encourager à effectuer un deuxième achat.
- **Programmes de fidélité :** Mettez en avant les produits qui maximiseraient les points de fidélité ou les récompenses d'un client en fonction de son solde de points actuel.
- **Contenu éducatif :** Suggérez de nouveaux cours ou contenus basés sur les thèmes des documents déjà consultés ou achetés.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Foire aux questions {#faq}

### Pourquoi des articles « Les plus populaires » apparaissent-ils dans les recommandations d'autres modèles ?

Lorsque notre moteur de recommandation établit une liste pour vous, il donne d'abord la priorité aux sélections personnalisées en fonction du modèle spécifique que vous avez choisi, comme « Les plus récents » ou « IA personnalisée ». Si, pour une raison quelconque, ce modèle ne peut pas remplir la liste complète de 30 recommandations, certains de vos articles les plus populaires parmi l'ensemble des utilisateurs sont alors ajoutés afin de garantir que chaque utilisateur dispose toujours d'un ensemble complet de recommandations.

Cela se produit dans quelques conditions spécifiques :

- Le modèle trouve moins de 30 articles correspondant à vos critères.
- Les articles concernés ne sont plus disponibles ou en stock.
- Les articles ne répondent pas aux critères de sélection actuels, peut-être en raison d'un changement de stock ou de préférences de l'utilisateur.

Notez que les recommandations fonctionnent de manière indépendante et n'ont aucune connaissance de ce que les autres modèles recommandent. Cela signifie que chaque section peut contenir des articles déjà affichés dans d'autres sections de recommandations IA du même e-mail.

### Comment éviter les doublons entre plusieurs sections de recommandations ?

Chaque recommandation fonctionnant de manière indépendante, un même article peut apparaître dans plusieurs sections d'un même message. Pour supprimer les doublons, utilisez Liquid pour suivre les ID d'articles déjà affichés et les ignorer dans les sections suivantes.

### Les recommandations existantes sont-elles entraînées chaque semaine après la mise à niveau vers Item Recommendations Pro ?

Oui, mais uniquement après leur prochaine mise à jour planifiée. Les recommandations existantes ne passent pas immédiatement à l'entraînement hebdomadaire et aux prédictions quotidiennes lors de la mise à niveau vers Item Recommendations Pro. Toutefois, elles adopteront automatiquement le nouveau calendrier lors de leur prochain cycle de réentraînement. Par exemple, si une recommandation a été entraînée pour la dernière fois le 1er février et qu'elle est configurée pour se réentraîner tous les 30 jours, elle adoptera le nouveau calendrier hebdomadaire après sa prochaine mise à jour le 2 mars.

### Comment faire expirer en même temps toutes les recommandations qui durent plusieurs jours ?

Si vous souhaitez faire expirer toutes les recommandations sur plusieurs jours à une date précise (afin que toutes les recommandations actives reçoivent de nouvelles prédictions en même temps), contactez l'assistance Braze ou votre Customer Success Manager. Les experts en IA de Braze effectuent cette opération manuellement afin de garantir des performances optimales du modèle.