---
nav_title: Snowplow
article_title: Snowplow
description: "Cet article de référence présente le partenariat entre Braze et Snowplow, une plateforme d'infrastructure de données, qui vous permet de transmettre les événements Snowplow à Braze en temps réel grâce à l'Event Forwarding de Snowplow."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplow.io) est une plateforme open source et évolutive pour la collecte de données riches, de haute qualité et à faible latence. Snowplow est conçu pour collecter des données comportementales complètes et de haute qualité pour les entreprises.

_Cette intégration est maintenue par Snowplow._

## À propos de l'intégration

L'intégration entre Braze et Snowplow vous permet de transmettre les événements Snowplow à Braze en temps réel grâce à la solution Event Forwarding de Snowplow. Cette intégration vous permet d'envoyer des événements à Braze tout en offrant flexibilité et contrôle. Plus précisément, vous pouvez :
- Filtrer et transformer les événements avant de les envoyer à Braze.
- Mapper les données des événements Snowplow aux attributs utilisateur de Braze, aux événements personnalisés et aux achats.
- Conserver toutes les données dans votre cloud privé jusqu'à ce que vous décidiez de les transmettre.
- Déployer vous-même la solution au sein de votre compte Snowplow existant. 

L'[Event Forwarding](https://docs.snowplow.io/docs/destinations/forwarding-events/) de Snowplow est une fonctionnalité supplémentaire payante disponible pour les clients Snowplow. Pour transmettre des événements à Braze sans ce module complémentaire, utilisez l'intégration [Google Tag Manager Server-Side](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) de Snowplow.

Exploitez les riches données comportementales de Snowplow pour favoriser de puissantes interactions centrées sur le client dans Braze et diffuser des messages personnalisés en temps réel.

## Conditions préalables

| Condition             | Description                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pipeline Snowplow       | Vous devez disposer d'un pipeline Snowplow opérationnel.                                                                                                                                                                                                                                          |
| Accès à la console Snowplow | Vous devez avoir accès à la console Snowplow pour configurer les transferts d'événements.                                                                                                                                                                                                                                |
| Clé API REST Braze      | Une clé API REST Braze avec les autorisations suivantes : `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename` et `users.alias.update`. <br><br> Vous pouvez la créer dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze     | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

### Livraison personnalisée par événement
Utilisez l'un des nombreux événements riches que Snowplow collecte par défaut, ou définissez vos propres événements personnalisés pour façonner des parcours clients encore plus précis, adaptés à votre entreprise. Exploitez les données comportementales de Snowplow pour concevoir des entonnoirs clients et créer de la valeur pour vos équipes marketing et produit, en les aidant à maximiser la conversion et l'utilisation des produits via Braze.

### Segmentation dynamique
Créez des audiences dynamiques dans Braze à partir des données comportementales de haute qualité de Snowplow : lorsque les utilisateurs effectuent des actions dans votre produit, application ou site web, vous pouvez exploiter les données comportementales en temps réel collectées par Snowplow pour ajouter ou supprimer automatiquement des utilisateurs des segments pertinents dans Braze.

## Intégration

### Étape 1 : Configurer la destination dans la console Snowplow

Pour créer le transfert d'événements :

1. Dans la console Snowplow, accédez à **Destinations** et sélectionnez **Create new destination**.
2. Lors de la configuration de la connexion, sélectionnez **Braze** comme type de connexion.
3. Saisissez votre clé API Braze et l'endpoint de l'API REST.
4. Enregistrez la connexion.

### Étape 2 : Configurer le transfert d'événements

Lors de la configuration du transfert, vous pouvez choisir les événements Snowplow à transmettre et les mapper à des types d'objets Braze :

1. **[Attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object)** : mettez à jour les données du profil utilisateur et les propriétés personnalisées.
2. **[Événements personnalisés]({{site.baseurl}}/api/objects_filters/event_object)** : envoyez les actions et les comportements des utilisateurs.
3. **[Achats]({{site.baseurl}}/api/objects_filters/purchase_object)** : envoyez les données de transaction avec les détails du produit.

Pour chaque type d'objet, vous pouvez configurer les mappages de champs afin de spécifier comment les données d'événement Snowplow correspondent aux champs Braze. Consultez la [documentation de Snowplow sur la création de transferts](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/) pour obtenir des instructions détaillées sur la configuration et le mappage des champs.

### Étape 3 : Valider l'intégration

Vérifiez que les événements arrivent bien dans Braze en consultant les pages suivantes de votre compte Braze :

1. **Générateur de requêtes** : dans Braze, accédez à **Analytique** > **Générateur de requêtes**. Vous pouvez écrire des requêtes sur les tables suivantes pour prévisualiser les données transmises par Snowplow : `USER_BEHAVIORS_CUSTOMEVENT_SHARED` et `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **Tableau de bord d'utilisation de l'API** : dans Braze, accédez à **Paramètres** > **API et identifiants** pour voir un graphique de l'utilisation de l'API au fil du temps. Vous pouvez filtrer spécifiquement sur la clé API utilisée par Snowplow et consulter les succès comme les échecs.

## Envoi de propriétés personnalisées

Vous pouvez envoyer des propriétés personnalisées en plus des champs standard. La structure dépend du type d'objet Braze que vous utilisez :

- **Attributs utilisateur** : ajoutez-les comme champs de premier niveau (par exemple, `subscription_tier`, `loyalty_points`).
- **Propriétés d'événement** : imbriquez-les sous l'objet `properties` (par exemple, `properties.plan_type`, `properties.feature_flag`).
- **Propriétés d'achat** : imbriquez-les sous l'objet `properties` (par exemple, `properties.color`, `properties.size`).

Pour les noms de propriétés contenant des espaces, utilisez la notation entre crochets (par exemple, `["account type"]` ou `properties["campaign source"]`).

Consultez la [documentation sur l'objet événement]({{site.baseurl}}/api/objects_filters/event_object) pour plus de détails sur les types de données pris en charge, les exigences de nommage des propriétés et les limites de taille du PAYLOAD.

## Limitations

**Limites de débit :** Braze applique une limite de débit de 3 000 appels API toutes les trois secondes pour l'API Track Users. Étant donné que Snowplow ne prend pas en charge le regroupement par lots pour les transferts d'événements, cette limite de débit de l'API s'applique également comme limite de débit des événements. Si votre débit d'entrée dépasse 3 000 événements par trois secondes, vous risquez de constater une augmentation de la latence.