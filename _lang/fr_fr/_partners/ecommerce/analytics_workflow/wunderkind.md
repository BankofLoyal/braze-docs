---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "Cet article de référence couvre l'intégration Wunderkind Signals avec Braze, notamment les signaux comportementaux qui déclenchent des parcours Canvas, la configuration avec l'API Canvas Entry, le payload de contexte Canvas lors de la distribution déclenchée par API, et le reporting."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) est une plateforme de performance e-commerce qui utilise une technologie d'identification propriétaire pour reconnaître les visiteurs anonymes d'un site web et les associer à des adresses e-mail exploitables. En moyenne, Wunderkind fait passer l'identification de 3 à 5 % du trafic d'un site web à 40 à 60 %, permettant aux marques de déclencher des messages personnalisés et individuels à grande échelle via leur ESP existant.

*Cette intégration est maintenue par Wunderkind. Pour obtenir de l'assistance, rendez-vous sur [support.wunderkind.co](https://support.wunderkind.co).*

## À propos de l'intégration

L'intégration Wunderkind Signals permet à des signaux comportementaux à forte intention — tels que l'abandon de panier, l'abandon de produit et les baisses de prix — de déclencher des parcours Canvas en temps réel dans Braze. Wunderkind identifie les utilisateurs anonymes sur votre site web, résout leur identité vers une adresse e-mail exploitable, et transmet un payload de signal structuré à Braze via l'API Canvas Entry, initiant automatiquement vos flux d'e-mails préconfigurés.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Wunderkind | Un compte Wunderkind avec Signals activé est requis. Contactez votre conseiller Wunderkind pour confirmer votre éligibilité. |
| Compte Braze | Un compte Braze avec accès à Canvas est requis. L'équipe Wunderkind doit disposer d'un accès à votre compte. Pour tous les détails, consultez [Accorder à Wunderkind l'accès à votre compte Braze](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account). |
| Clé API REST Braze | Vous créez une clé API dédiée avec des autorisations spécifiques lors de la configuration (voir [Étape 1](#step-1-create-a-braze-api-key-for-wunderkind)). |
| Identification des utilisateurs | Wunderkind résout généralement un consommateur dans Braze en utilisant `user_alias` avec `alias_label: "wknd_email_id"` (souvent avec l'e-mail comme `alias_name`). Chaque destinataire de [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) doit inclure exactement l'un des éléments suivants : `external_user_id`, `user_alias`, `braze_id` ou `email` ([objet recipients]({{site.baseurl}}/api/objects_filters/recipient_object/)) ; si vous utilisez `email`, incluez [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email). Lorsque vous utilisez `user_alias`, le profil doit déjà exister dans Braze avant le déclencheur. Créez ou mettez à jour les utilisateurs et les alias au préalable avec [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). Pour en savoir plus, consultez [Limitations](#limitations). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fonctionnement

Lorsque Wunderkind identifie un utilisateur anonyme à forte intention et résout son identité, il envoie un payload de signal à Braze via l'endpoint `/canvas/trigger/send`, déclenchant le parcours Canvas correspondant pour cet utilisateur en temps réel.

Pour un aperçu technique complet, consultez le [Portail développeur Wunderkind](https://developer.wunderkind.co/docs/integration-overview).

## Intégration

### Étape 1 : Créer une clé API Braze pour Wunderkind

Dans votre tableau de bord de Braze :

1. Accédez à **Paramètres** > **Clés API** et cliquez sur **Créer une nouvelle clé API**.
2. Donnez à la clé un nom descriptif (par exemple, `Wunderkind Signals`).
3. Accordez les autorisations listées dans [Accorder à Wunderkind l'accès à votre compte Braze](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account).
4. Copiez la clé API pour la saisir dans la plateforme Wunderkind à l'étape suivante.

{% alert note %}
Pour Wunderkind Signals, les requêtes de l'[API REST]({{site.baseurl}}/api/basics/) Braze sont authentifiées avec une clé API REST, et non avec des jetons OAuth. Créez une clé API dédiée dans le tableau de bord et fournissez cette clé à Wunderkind.
{% endalert %}

### Étape 2 : Connecter Braze à la plateforme Wunderkind

1. Connectez-vous à la plateforme Wunderkind et accédez au **Hub d'intégrations**.
2. Sélectionnez la tuile **Braze**, puis sélectionnez **Connect**.
3. Saisissez votre clé API REST Braze et sélectionnez votre cluster.
4. Sélectionnez **Enregistrer**.

### Étape 3 : Vérifier les nouvelles ressources Braze

Lors de l'activation, Wunderkind provisionne de nouvelles ressources d'implémentation dans votre espace de travail Braze en fonction de la stratégie définie avec votre conseiller Wunderkind :

| Type de ressource | Méthode de création Wunderkind |
| ---------- | -------------------------- |
| Content Blocks | Automatique |
| Canvas déclenchés par API | Service géré |
| Étiquettes, attributs personnalisés, modèles de liens | Service géré |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 4 : Finaliser la configuration du Canvas

Pour chaque Canvas Signals, créez vos modèles d'e-mails à l'aide de l'éditeur par glisser-déposer de Braze ou en HTML.

- Wunderkind renseigne les données produit et de session dans l'objet `context` de chaque destinataire sur `/canvas/trigger/send` au moment de l'envoi.
- Pour des instructions détaillées sur l'utilisation de Liquid avec ce payload dans vos modèles, consultez [Finaliser la configuration du Canvas](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) dans le Centre d'aide Wunderkind.

### Étape 5 : Vérifier l'éligibilité du Canvas

Pour chaque Canvas Signals, accédez aux paramètres **Audience cible** pour vérifier l'audience d'entrée par défaut et les critères de sortie définis par Wunderkind.

- Pour vous assurer de ne pas envoyer trop de messages à vos utilisateurs, consultez [Limitation du débit centrée sur l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).
- Ajustez les paramètres pour empêcher les utilisateurs de continuer à recevoir des messages Canvas après un achat. Par exemple, ajoutez l'exception **Effectuer un achat**.
- Certains Canvas Signals sont préconfigurés avec des filtres d'attributs personnalisés pour que les utilisateurs reçoivent le message à la plus forte intention possible.
- Consultez [Vérifier l'éligibilité du Canvas](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) dans le Centre d'aide Wunderkind pour plus de détails sur l'éligibilité et la priorité des Canvas.

### Étape 6 : Tester et lancer

Wunderkind effectue une assurance qualité de bout en bout avant la mise en production :

- Confirmer que les signaux sont transmis aux bons Canvas ID sans erreurs API.
- Vérifier que les champs `context` (nom du produit, image, URL) s'affichent correctement dans les modèles d'e-mails rendus.
- Consultez [Tester et lancer Signals pour Braze](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) dans le Centre d'aide Wunderkind pour les instructions de prévisualisation des modèles avec des produits Wunderkind fictifs.

Une fois l'assurance qualité validée, votre responsable d'implémentation Wunderkind coordonne le lancement en production avec votre équipe.

## Payload de contexte Canvas

Wunderkind prend en charge six types de signaux. Chacun transmet un ensemble distinct de clés et de valeurs dans l'objet [`context`]({{site.baseurl}}/api/objects_filters/context_object/) pour ce destinataire sur `/canvas/trigger/send` (voir [Envoyer des messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). Le champ `WkPurpose` identifie le type de signal dans ce payload.

### Champs communs (tous les types de Canvas) {#canvas-types-table}

| Propriété | Type | Description |
| -------- | ---- | ----------- |
| `Origin` | String | Toujours `"wunderkind"` |
| `DataOnly` | String | Toujours `"Y"` — indique que Wunderkind agit uniquement comme couche de données ; Braze exécute l'envoi |
| `UserType` | String | `"prospect"` ou `"customer"` |
| `WkChannel` | String | Toujours `"email"` pour cette intégration |
| `WkPurpose` | String | Identifiant du type de signal (voir les valeurs par Canvas ci-dessous) |
| `WKCouponCode` | String | Code de coupon, le cas échéant (chaîne vide si non utilisé) |
| `WKCouponPurpose` | String | Description de l'offre de coupon (chaîne vide si non utilisée) |
| `Items` | Array | Tableau d'objets produit (voir les champs produit ci-dessous) |
| `WkOpen` | String | Pixel de suivi disponible à des fins de reporting |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Champs des articles produit

| Propriété | Type | Description |
| -------- | ---- | ----------- |
| `WkCopy` | String | Nom du produit |
| `WkId` | String | ID du produit |
| `WkImageUrl` | String | URL de l'image du produit |
| `WkUrl` | String | URL de la page de détail du produit |
| `WkPrice` | String | Prix d'origine (Canvas baisse de prix uniquement) |
| `WKSalePrice` | String | Prix promotionnel (Canvas baisse de prix uniquement) |
| `WkQuantity` | String | Unités restantes (Canvas stock faible uniquement) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Champs spécifiques au Canvas et valeurs de `WkPurpose`

| Type de Canvas | Valeur de `WkPurpose` | Champs supplémentaires |
| ----------- | ----------------- | ------------------- |
| Abandon de panier | `"cart abandonment"` | `WkCartReplenUrl` — URL pour reconstituer le panier |
| Abandon de produit | `"product abandonment"` | — |
| Récapitulatif de catégorie | `"category recap"` | `WkCategoryUrl` — URL de la catégorie consultée |
| De retour en stock | `"back in stock"` | — |
| Baisse de prix | `"price drop"` | `WkPrice`, `WKSalePrice` sur chaque article |
| Stock faible | `"low stock"` | `WkQuantity` sur chaque article |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Exemples de payloads

Chaque objet dans `recipients` doit inclure exactement l'un des éléments suivants : `external_user_id`, `user_alias`, `braze_id` ou `email`. Pour en savoir plus, consultez l'[objet Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/).

{% alert note %}
Chaque exemple utilise **un seul** identifiant de destinataire Braze. Les six premiers utilisent uniquement `user_alias` ; le dernier utilise uniquement `email` avec [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email). Le JSON d'exemple omet la clé `WkChannel` dans `context` afin que les outils de vérification ne confondent pas sa valeur (`"email"`) avec le champ `email` du destinataire Braze. En production, incluez `"WkChannel": "email"` dans `context` comme documenté dans le [tableau des champs communs (tous les types de Canvas)](#canvas-types-table).
{% endalert %}

Les exemples suivants utilisent `user_alias` avec `wknd_email_id`, conformément à la manière dont Wunderkind résout les identités.

{% details Exemple de payload d'abandon de panier %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemple de payload d'abandon de produit %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemple de payload de récapitulatif de catégorie %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemple de payload de retour en stock %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemple de payload de baisse de prix %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemple de payload de stock faible %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemple avec identifiant e-mail (alternative) %}
Si vous déclenchez le Canvas avec le champ `email` de Braze au lieu de `user_alias`, le destinataire doit inclure uniquement `email` et `prioritization` (voir [Envoyer des messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). L'objet `context` est identique aux autres exemples.

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Exemple d'utilisation de Liquid

Lorsque Wunderkind appelle `/canvas/trigger/send`, les clés et valeurs transmises dans l'objet `context` de chaque destinataire deviennent des données d'entrée Canvas. Dans les étapes Message, référencez-les avec l'espace de noms Liquid `context`. Par exemple {% raw %}`{{context.${WkPurpose}}}`{% endraw %}, comme décrit dans [Objet de contexte Canvas]({{site.baseurl}}/api/objects_filters/context_object/) et [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/). Aucune configuration supplémentaire n'est nécessaire au-delà de l'utilisation de la syntaxe Liquid correcte.

N'imbriquez pas les balises de sortie Braze dans la condition de la balise `for`. Assignez d'abord le tableau `Items` depuis `context` à une variable, puis effectuez la boucle, comme décrit dans [Utiliser Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#use-a-filter-result-in-a-for-loop). La ligne `assign` utilise le format d'entrée Canvas de Braze {% raw %}`{{context.${Items}}}`{% endraw %} (voir [Balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#summary-of-supported-tags)).

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## Reporting

Wunderkind ingère les données de performance depuis Braze à l'aide de **Braze Currents**, qui diffuse les événements bruts vers Google Cloud Storage. Wunderkind normalise et agrège ensuite ces événements par rapport au signal d'origine pour un reporting d'attribution 1:1.

Les indicateurs suivants seront bientôt disponibles dans le tableau de bord de reporting Wunderkind :

| Indicateur | Source |
| ------ | ------ |
| Envois distribués | Braze Currents |
| Ouvertures d'e-mails | Braze Currents |
| Clics | Braze Currents |
| Conversions | Braze Currents (événement défini lors de la configuration) |
| Désabonnements | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

- **Pas de synchronisation des suppressions/désinscriptions.** La suppression doit être gérée nativement dans Braze. Remarque : pour les clients Wunderkind existants migrant vers Braze Signals, Wunderkind collabore avec votre équipe pour préserver votre configuration actuelle.
- **Canal e-mail uniquement.** Le SMS n'est actuellement pas pris en charge par cette intégration.
- **Le profil utilisateur doit exister avant le déclencheur Canvas.** [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) avec un destinataire `user_alias` ne résout que les profils Braze **existants** qui possèdent déjà cet alias. Vous ne pouvez pas utiliser `send_to_existing_only` avec des alias, et le déclencheur Canvas ne crée pas de nouveau profil à partir de l'alias seul. L'utilisateur doit être créé ou mis à jour et l'alias `wknd_email_id` doit être défini au préalable (par exemple, en utilisant [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)). Wunderkind peut attendre brièvement après cette mise à jour afin que Braze termine le traitement avant de déclencher le signal.
- **E-mail comme identifiant.** Si le déclencheur Canvas identifie le destinataire avec `email` au lieu de `user_alias`, incluez [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) dans l'objet destinataire, comme requis par Braze.


## Ressources supplémentaires

- [Centre d'aide Wunderkind — Aperçu de Signals pour Braze](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Portail développeur Wunderkind — Aperçu de l'intégration](https://developer.wunderkind.co/docs/integration-overview)
- [Envoyer des messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [Objet de contexte Canvas]({{site.baseurl}}/api/objects_filters/context_object/)
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)