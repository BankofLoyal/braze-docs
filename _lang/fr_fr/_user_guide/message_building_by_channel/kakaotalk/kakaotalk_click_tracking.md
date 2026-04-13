---
nav_title: Suivi des clics KakaoTalk
article_title: Suivi des clics KakaoTalk
page_order: 3
description: "Cette page explique comment activer le suivi des clics dans vos messages KakaoTalk, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore."
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# Suivi des clics KakaoTalk

> Cette page explique comment activer le suivi des clics dans vos messages KakaoTalk, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore.

Lorsque le suivi des clics KakaoTalk est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, par exemple en segmentant les utilisateurs en fonction de leur comportement de clic ou en déclenchant des messages en réponse à des clics spécifiques.

Le suivi des clics KakaoTalk peut être utilisé pour les messages texte, image et liste d'éléments. Il prend en charge les liens dans les boutons et les actions au clic sur les images. Vous pouvez également personnaliser les URL à l'aide de Liquid et de domaines personnalisés.

## Fonctionnement

Vous pouvez gérer les paramètres de suivi des clics KakaoTalk dans la section **Options de lien** du composeur. Lorsque cette option est activée, les URL sont raccourcies à l'aide du domaine Braze par défaut (`https://brz.ai`) ou du domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisées pour l'utilisateur.

Toutes les URL commençant par `http://` ou `https://` seront raccourcies. Vous pouvez inclure jusqu'à 25 URL dans un message. Les URL raccourcies contenant une personnalisation Liquid (comme le suivi au niveau de l'utilisateur ou les paramètres UTM) restent valides pendant deux mois.

## Configurer le suivi des clics

### Messages texte

Pour configurer le suivi des clics pour un message texte :

1. Rédigez un message **Texte** et ajoutez une URL dans le champ de texte ou le bouton.
2. Dans la section **Options de lien** du composeur, vérifiez que **Suivi des clics** est coché. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

![Composeur de message texte KakaoTalk affichant la section Options de lien avec le Suivi des clics coché.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### Messages image

Pour configurer le suivi des clics pour un message image :

1. Rédigez un message **Image** et définissez le comportement au clic pour ouvrir une URL.
2. Saisissez une URL dans le champ URL.
3. Dans la section **Options de lien** du composeur, vérifiez que **Suivi des clics** est coché.

### Messages liste d'éléments

Pour configurer le suivi des clics pour un message liste d'éléments :

1. Rédigez un message **Liste d'éléments** et ajoutez une URL dans le champ **URL du site web** pour n'importe quel élément.
2. Dans la section **Options de lien** du composeur, vérifiez que **Suivi des clics** est coché.

## Domaines personnalisés

Le suivi des clics KakaoTalk vous permet d'utiliser votre propre domaine pour personnaliser l'apparence de vos URL raccourcies, contribuant ainsi à véhiculer une image de marque cohérente. Pour en savoir plus, consultez [Domaines personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Personnalisation Liquid dans les URL

Vous pouvez construire dynamiquement votre URL directement dans le composeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (par exemple, les diriger vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).

Les URL peuvent être générées dynamiquement grâce à l'utilisation de toutes les balises de personnalisation Liquid prises en charge.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Vous pouvez également raccourcir des variables Liquid personnalisées, comme illustré dans l'exemple suivant :

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

Braze raccourcit les URL rendues par Liquid, y compris celles incluses dans les propriétés de déclenchement API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, Braze raccourcira et suivra cette URL avant d'envoyer le message KakaoTalk.

## Tests

Avant de lancer votre campagne ou Canvas, il est recommandé de prévisualiser et de tester votre message au préalable. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un message KakaoTalk à des groupes de test de contenu ou à un utilisateur individuel.

L'aperçu sera mis à jour avec la personnalisation pertinente et l'URL raccourcie.

{% alert important %}
Si un brouillon est créé au sein d'un Canvas actif, aucune URL raccourcie ne sera générée. L'URL raccourcie réelle est générée lorsque le brouillon du Canvas est activé.
{% endalert %}

## Rapports

Le tableau de performance KakaoTalk inclut la colonne **Total des clics** qui affiche le nombre d'événements de clic par variante ainsi que le taux de clics associé. Pour plus de détails sur les indicateurs KakaoTalk, consultez [Rapports KakaoTalk]({{site.baseurl}}/kakaotalk_reporting/).

Les données de clics sont automatiquement reportées dans le tableau de bord d'analyse.

## Recibler les utilisateurs

Vous pouvez recibler les utilisateurs ayant cliqué sur une URL dans un message KakaoTalk en utilisant les filtres de segmentation et déclencheurs suivants :

- Déclencheurs basés sur l'action
    - Interagir avec une campagne
    - Interagir avec une étape

- Filtres de segmentation
    - A cliqué/ouvert une campagne
    - A cliqué/ouvert une campagne ou un Canvas avec une étiquette
    - A cliqué/ouvert une étape

## Questions fréquentes

### Les liens que je reçois lors d'un envoi test sont-ils de vraies URL ?

Oui, de vraies URL sont générées lors d'un envoi test. Cependant, l'URL exacte envoyée dans une campagne lancée peut différer de celle envoyée lors d'un envoi test.

### Puis-je ajouter des paramètres UTM à une URL avant qu'elle ne soit raccourcie ?

Oui, des paramètres statiques et dynamiques peuvent être ajoutés.

### Combien de temps les URL raccourcies restent-elles valides ?

Les URL personnalisées sont valides pendant deux mois à compter de l'enregistrement de l'URL.

### Le SDK Braze doit-il être installé pour raccourcir les URL ?

Non, le suivi des clics fonctionne sans aucune intégration SDK.

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ?

Oui. Lorsque le suivi des clics est activé, vous pouvez recibler les utilisateurs ayant cliqué sur des URL en utilisant les [filtres de reciblage KakaoTalk](#retargeting-users).

### Le suivi des clics fonctionne-t-il avec les liens profonds ou les liens universels ?

Le suivi des clics s'applique aux URL web. Pour les liens profonds, vous pouvez définir un lien profond directement comme type d'action au clic pour les boutons dans KakaoTalk — ceux-ci ne passent pas par le raccourcissement d'URL ni le suivi des clics. Si vous préférez utiliser des liens universels de fournisseurs tels que Branch ou Appsflyer, ceux-ci peuvent être raccourcis, mais Braze n'est pas en mesure de résoudre les problèmes qui pourraient survenir (comme la rupture de l'attribution ou l'échec de la redirection).