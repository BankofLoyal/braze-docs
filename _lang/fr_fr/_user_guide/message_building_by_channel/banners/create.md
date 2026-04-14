---
nav_title: Créer une bannière
article_title: Créer une bannière
page_order: 1
description: "Cet article de référence explique comment créer, composer, configurer et envoyer des bannières à l'aide des campagnes Braze et des Canvas."
tool:
  - Campaigns
channel:
  - banners
---

# Créer une bannière

> Découvrez comment créer des bannières lorsque vous créez des campagnes et des Canvas dans Braze. Pour plus d'informations générales, reportez-vous à la section [À propos des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Conditions préalables

Avant de pouvoir lancer votre bannière, votre équipe de développement doit [configurer des emplacements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/creating_placements/). Vous pouvez tout de même rédiger votre campagne de bannière en attendant, mais vous ne pourrez pas la lancer tant que les emplacements n'auront pas été configurés.

## Créer un message bannière

{% multi_lang_include banners/creating_placements.md section="user" %}

### Étape 2 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux campagnes de communication uniques et ciblées, tandis que les Canvas conviennent mieux aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Bannière**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire. Les étiquettes facilitent la recherche et l'identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le générateur de rapports, vous pouvez filtrer par les étiquettes pertinentes.
5. Sélectionnez l'emplacement que vous avez précédemment créé pour l'associer à votre campagne.
6. Ajoutez des variantes si nécessaire. Vous pouvez choisir un type de message et une disposition différents pour chacune d'entre elles. Pour plus d'informations sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Choisissez une date et une heure de début pour votre campagne de bannières. Par défaut, les bannières durent indéfiniment. Vous pouvez modifier cela en sélectionnant **Heure de fin** et en spécifiant une date et une heure de fin.

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite sélectionner **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape Message dans le générateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Sélectionnez **Bannière** comme canal de communication.
4. Sélectionnez un emplacement pour la bannière.
5. Définissez la priorité de la bannière. La [priorité des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) détermine l'ordre dans lequel les bannières sont affichées si elles partagent le même emplacement.
6. Définissez une date d'expiration pour la bannière. Celle-ci peut correspondre à un délai après la mise à disposition de l'étape, ou à une date et une heure spécifiques.

{% endtab %}
{% endtabs %}

### Étape 3 : Composer une bannière {#compose-a-banner}

Pour créer votre bannière, vous avez la possibilité de :

- Commencer par un modèle vide
- Utiliser un modèle de bannière Braze
- Sélectionner un modèle de bannière enregistré

![Possibilité de choisir une bannière vierge ou un modèle.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Étape 3.1 : Styliser la bannière

Vous pouvez glisser-déposer des blocs et des lignes dans la zone de travail pour commencer à créer votre message.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Pour personnaliser les propriétés de l'arrière-plan de votre message, les paramètres de bordure, etc., sélectionnez **Styles**. Si vous souhaitez uniquement personnaliser le style d'un bloc ou d'une ligne spécifique, sélectionnez-le pour apporter des modifications.

![Panneau de style du compositeur de bannières.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Étape 3.2 : Définir le comportement au clic (facultatif)

Lorsqu'un utilisateur clique sur un lien dans la bannière, vous pouvez choisir de le diriger plus en profondeur dans votre application ou de le rediriger vers une autre page web. Vous pouvez également choisir d'[enregistrer un attribut personnalisé ou un événement]({{site.baseurl}}/developer_guide/analytics/), ce qui met à jour le profil de l'utilisateur avec des données personnalisées lorsqu'il clique sur la bannière.

{% alert important %}
{::nomarkdown}
Le comportement au clic peut être remplacé si un élément spécifique (tel qu'un bouton, un lien ou une image de la bannière) possède son propre comportement au clic. Par exemple, avec les comportements au clic suivants :<br><ul><li>Une bannière a un comportement au clic qui redirige vers la page d'accueil d'un site web.</li><li>Une image dans la bannière a un comportement au clic qui redirige vers la page produit d'un site web.</li></ul>Si un utilisateur clique sur l'image, il est redirigé vers la page du produit. En revanche, cliquer sur la zone environnante de la bannière le redirige vers la page d'accueil.
{:/}
{% endalert %}

#### Étape 3.3 : Ajouter des propriétés personnalisées (facultatif) {#custom-properties}

Vous pouvez ajouter des propriétés personnalisées à une bannière afin d'y associer des métadonnées structurées, telles que des chaînes de caractères ou des objets JSON. Ces propriétés n'affectent pas l'affichage de la bannière, mais sont [accessibles via le SDK Braze]({{site.baseurl}}/developer_guide/banners/placements/) pour modifier le comportement ou l'apparence de votre application. Par exemple, vous pourriez :

- Envoyer des métadonnées pour vos analyses tierces ou intégrations.
- Utiliser des métadonnées telles qu'un `timestamp` ou un objet JSON pour déclencher une logique conditionnelle.
- Contrôler le comportement d'une bannière en fonction des métadonnées incluses comme `ratio` ou `format`.

Pour ajouter une propriété personnalisée, sélectionnez **Paramètres** > **Propriétés** > **Ajouter une propriété**.

![La page des propriétés présentant l'option permettant d'ajouter la première propriété personnalisée à une campagne de bannière.]({% image_buster /assets/img/banners/add_property.png %})

Pour chaque propriété que vous souhaitez ajouter, remplissez les champs suivants :

| Champ | Description | Exemple |
|-------|-------------|---------|
| Type de propriété | Le type de données de la propriété. Les types pris en charge comprennent les chaînes de caractères, les valeurs booléennes, les nombres, les horodatages, les URL d'images et les objets JSON. | Chaîne de caractères |
| Clé de propriété | L'identifiant unique de la propriété. Cette clé est utilisée dans le SDK pour accéder à la propriété. | `color` |
| Valeur | La valeur attribuée à la propriété. Elle doit correspondre au type de propriété sélectionné. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Lorsque vous avez terminé, sélectionnez **Terminé**.

![La page des propriétés avec une propriété de type chaîne de caractères dont la clé est « color » et la valeur #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Étape 4 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campaign %}

#### Définir la priorité de la bannière (facultatif)

La [priorité des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) détermine l'ordre dans lequel les bannières sont affichées si elles partagent le même emplacement. Pour définir manuellement la priorité :

1. Sélectionnez **Définir la priorité exacte**.
2. Glissez-déposez les campagnes pour les ordonner avec la bonne priorité.
3. Sélectionnez **Appliquer le tri**.

{% alert tip %}
Si vous avez plusieurs campagnes de bannières utilisant le même ID d'emplacement, nous vous recommandons d'utiliser la fonction de tri des priorités par glisser-déposer pour définir la priorité exacte.
{% endalert %}

#### Choisir votre audience

1. Dans **Audiences cibles**, sélectionnez des segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative du segment. L'appartenance exacte au segment est calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. Dans **Affecter les conversions**, suivez la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne en définissant des événements de conversion avec une fenêtre maximale de 30 jours pour comptabiliser l'action comme une conversion.

{% multi_lang_include target_audiences.md %}

#### Choisir des événements de conversion

Braze vous permet de suivre les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), c'est-à-dire la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne. Vous avez la possibilité d'autoriser une période maximale de 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les [tests multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) et la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), etc., reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

### Étape 5 : Tester votre message (facultatif)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Étape 6 : Vérifier et déployer

Une fois que vous avez terminé la création de votre campagne ou de votre Canvas, vérifiez ses détails, [testez-la]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), puis envoyez-la lorsque vous êtes prêt.