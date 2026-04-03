---
nav_title: Documentation de conformité
article_title: Documentation de conformité
page_order: 1
permalink: /compliance_documentation/
toc_headers: h2
noindex: true
---

# Documentation de conformité

_Date de révision : 30 mars 2026_

## Qu'est-ce qui est inclus dans la documentation de conformité ?

La documentation de conformité ci-dessous énonce les conditions spécifiques applicables à votre produit, canal, fonctionnalité ou service acheté :

- Pour les fonctionnalités des services Braze qui permettent aux clients d'interagir avec, d'intégrer ou d'accéder au produit, au site Web, à l'application ou au service d'un fournisseur tiers, la documentation de conformité contient les conditions du fournisseur tiers applicables à votre utilisation de cette fonctionnalité ; et
- Toutes les pratiques et normes industrielles générales auxquelles les clients de Braze sont tenus de se conformer pour l'utilisation de ce produit, canal, fonctionnalité, fonction ou service de Braze.

## Mises à jour de la documentation de conformité

Vous pouvez vous abonner pour recevoir les mises à jour de notre documentation (y compris la documentation de conformité) via le [dépôt GitHub de Braze](https://github.com/braze-inc/braze-docs).

## Documentation de conformité pour des canaux, intégrations et fonctionnalités spécifiques

Vous trouverez ci-dessous la liste de nos produits, canaux, fonctionnalités et services disposant d'une documentation de conformité applicable. Si vous utilisez plusieurs produits, toute la documentation de conformité pertinente s'applique.

### Conditions générales

Sans limiter les obligations du client au titre du contrat, et pour éviter toute ambiguïté, le client est seul responsable de l'obtention de tous les droits, consentements et autorisations nécessaires, de la fourniture d'avis de confidentialité juridiquement adéquats dans le cadre de son utilisation, et de l'obtention de tous les consentements et autorisations légalement requis pour l'utilisation des canaux et fonctionnalités énumérés ci-dessous.

## Canaux et fonctionnalités

1. [Canal des messages mobiles](#mobile-messages-channel)
2. [Canal webhooks](#webhooks-channel)
3. [Documentation de conformité du canal WhatsApp](#hatsapp-channel-compliance-documentation)
4. [Documentation de conformité du canal LINE](#line-channel-compliance-documentation)
5. [Documentation de conformité de l'intégration Shopify](#shopify-integration-compliance-documentation)
6. [Documentation de conformité de la synchronisation d'audience](#audience-sync-compliance-documentation)
7. [Documentation de conformité de l'archivage des messages et du chiffrement au niveau du champ](#message-archiving-and-field-level-encryption-compliance-documentation)
8. [Documentation de conformité de la console agent](#agent-console-compliance-documentation)
9. [Documentation de conformité du canal KakaoTalk](#kakaotalk-channel-compliance-documentation)

## 1. Canal des messages mobiles {#mobile-messages-channel}

Les conditions supplémentaires suivantes s'appliquent dans le cadre de l'utilisation du canal des messages mobiles par le client :

### Définitions

**« Agrégateurs »**, **« Opérateurs »** ou **« Intermédiaires de messages mobiles »** désignent les intermédiaires tiers (i) qui transmettent des messages mobiles entre les fournisseurs de messages mobiles et les opérateurs ; (ii) qui sont des fournisseurs de services sans fil (par exemple, T-Mobile, AT\&T, etc.) ; et/ou (iii) qui participent à la transmission de messages RCS des fournisseurs de messages mobiles aux utilisateurs finaux.

**« Fournisseurs SMS/MMS » ou « Fournisseurs de messages mobiles »** désignent les sous-traitants de Braze utilisés pour la transmission de messages SMS, MMS et/ou RCS, tels qu'identifiés sur [www.braze.com/subprocessors](http://www.braze.com/subprocessors).

**« Messages SMS/MMS » ou « Messages mobiles »** désignent les messages SMS, MMS et/ou RCS.

### Normes et bonnes pratiques industrielles applicables

Lors de l'envoi de messages mobiles, les clients doivent se conformer aux politiques d'utilisation acceptable et d'envoi de messages des fournisseurs de messages mobiles, aux normes et directives industrielles applicables, et, le cas échéant, aux codes industriels et aux directives des intermédiaires de messages mobiles applicables pour tout pays dans lequel le client a l'intention d'envoyer des messages mobiles, comme décrit plus en détail dans la [Politique d'utilisation acceptable](https://www.braze.com/company/legal/aup/) de Braze.

Les tiers impliqués dans l'envoi de messages mobiles, y compris les intermédiaires de messages mobiles, peuvent imposer des frais ou des pénalités en cas d'envoi de messages mobiles en violation de leurs conditions ou des lois applicables. Le client est responsable du paiement des frais et pénalités résultant de la violation par le client de ces conditions de tiers, que ces frais ou pénalités soient imposés au client ou à Braze.

### Sous-traitants

Braze peut utiliser tout fournisseur de messages mobiles figurant sur sa liste de sous-traitants à l'adresse [www.braze.com/subprocessors](https://www.braze.com/subprocessors/).

Nonobstant ce qui précède, dans le cas où le client envoie des messages mobiles en utilisant le modèle « Bring Your Own (BYO) SMS Connector », les fournisseurs de messages mobiles impliqués dans l'envoi seront considérés comme des fournisseurs tiers (tels que définis dans le contrat) et non comme des sous-traitants de Braze, et les clauses de non-responsabilité ci-dessous s'appliqueront à ces fournisseurs tiers.

### Conditions d'exception pour l'utilisation des webhooks

Applicable aux clients ayant souscrit à des crédits de messages à compter du 9 décembre 2024 (selon la date d'entrée en vigueur du bon de commande) : les restrictions décrites dans la documentation de conformité du canal webhooks ne s'appliquent pas à l'utilisation de webhooks pour l'envoi de messages mobiles via une plateforme de fournisseur tiers.

### Bring Your Own (BYO) SMS Connector

Les clients peuvent envoyer des messages mobiles depuis Braze en utilisant des fournisseurs tiers via le modèle « BYO SMS Connector ». Nonobstant ce qui précède, les clients ne doivent pas utiliser le modèle BYO SMS Connector pour envoyer des messages mobiles aux États-Unis et au Canada.

### Clauses de non-responsabilité

Braze décline toute déclaration, garantie, responsabilité et obligation d'indemnisation en ce qui concerne tout fournisseur tiers ou intermédiaire de messages mobiles impliqué dans l'envoi ou le traitement de messages mobiles, y compris la responsabilité liée à la capacité du système, au débit des messages ou à la réception effective sur l'appareil d'un utilisateur final.

## 2. Canal webhooks {#webhooks-channel}

Les conditions supplémentaires suivantes s'appliquent dans le cadre de l'utilisation du canal webhooks par le client :

### Conditions d'utilisation du canal webhooks

Sauf autorisation contraire dans la documentation de conformité du canal applicable, (a) le client ne doit pas utiliser de webhooks lorsque Braze offre des fonctionnalités natives permettant d'obtenir le même résultat, et (b) le client ne doit pas utiliser un webhook pour déclencher l'envoi d'un message via une plateforme de fournisseur tiers dans la mesure où Braze fournit un mécanisme natif pour envoyer ces messages via les services Braze.

Si Braze met à disposition un mécanisme nouveau ou mis à jour de manière générale dans les services Braze pendant la durée d'abonnement en cours du client, le client ne pourra plus utiliser de webhooks pour déclencher l'envoi de messages via la plateforme de fournisseur tiers spécifiée à compter de six (6) mois après la date de mise à disposition générale du nouveau mécanisme ou à la fin de l'année en cours de la durée d'abonnement du client, selon la date la plus tardive.

### Exceptions aux conditions d'utilisation du canal webhooks

Voir [Canal des messages mobiles](#mobile-messages-channel) et [Canal WhatsApp](#whatsapp-channel-compliance-documentation)

### Clause de non-responsabilité

Braze décline toute responsabilité en ce qui concerne l'utilisation par le client de webhooks pour déclencher l'envoi de tout message ou toute autre action en dehors des services Braze.

## 3. Documentation de conformité du canal WhatsApp {#whatsapp-channel-compliance-documentation}

Les conditions supplémentaires suivantes s'appliquent dans le cadre de l'utilisation du canal WhatsApp par le client :

### Conditions applicables du fournisseur tiers

Le client doit se conformer à toutes les conditions préalables, conditions et politiques applicables au canal WhatsApp, y compris toute condition requise par WhatsApp, LLC et ses sociétés affiliées, comme décrit sur la page de [configuration WhatsApp](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/overview/) de Braze.

### Conditions d'exception pour l'utilisation des webhooks

Le client ne peut pas utiliser de webhooks pour déclencher l'envoi de messages via le canal WhatsApp, sauf à des fins d'assistance client, telles que les cas d'utilisation de chat assisté par un agent humain et/ou les cas d'utilisation de chatbot.

### Bring Your Own (BYO) Whatsapp Connector

Les clients peuvent connecter leurs comptes Whatsapp directs avec Braze en utilisant le « BYO Whatsapp Connector ».

## 4. Documentation de conformité du canal LINE {#line-channel-compliance-documentation}

Les conditions supplémentaires suivantes s'appliquent dans le cadre de l'utilisation du canal LINE par le client :

### Conditions préalables

Pour envoyer des messages via le canal LINE, les clients doivent obtenir un compte officiel LINE vérifié, qui est approuvé et accordé par LINE à sa seule discrétion. Les clients doivent s'assurer d'obtenir un compte officiel vérifié auprès de LINE avant d'acheter des crédits de messages Braze pour l'utilisation du canal LINE.

### Conditions applicables du fournisseur tiers

En utilisant le canal LINE, le client accepte de se conformer et d'être lié par, le cas échéant, toutes les conditions et politiques requises par LY Corporation et ses sociétés affiliées (collectivement « LINE »), y compris, sans s'y limiter, les conditions d'utilisation du compte officiel LINE, les conditions d'utilisation de l'API du compte officiel, les directives du compte officiel LINE, la politique de données utilisateur LINE, et toutes les politiques, conditions, directives et documentations incorporées par référence (collectivement, les « Conditions LINE »). Pour plus de clarté, le client est responsable de : (i) s'assurer que toute donnée traitée en lien avec LINE est traitée conformément aux conditions LINE applicables ; et (ii) tous les frais ou paiements dus à LINE pour l'utilisation des services LINE en lien avec le canal LINE.

Nonobstant toute disposition contraire dans les conditions LINE, le client reste principalement responsable de son utilisation des services LINE.


## 5. Documentation de conformité de l'intégration Shopify {#shopify-integration-compliance-documentation}

Les conditions supplémentaires suivantes s'appliquent dans le cadre de l'utilisation par le client de l'intégration Shopify en lien avec les services Braze (« **Intégration Shopify** ») :

Le client accepte de se conformer et d'être lié par toutes les conditions, politiques, directives et documentations applicables de Shopify Inc. ou de l'une de ses sociétés affiliées (« **Shopify** ») applicables à l'utilisation de l'intégration Shopify.

Le client reconnaît que Shopify peut à tout moment et à sa seule discrétion : (i) exiger que Braze désactive ou bloque l'accès du client à l'intégration Shopify ; ou (ii) cesser de fournir, suspendre ou résilier l'accès du client à l'intégration Shopify. Braze n'assume aucune responsabilité en ce qui concerne la cessation par Shopify de l'accès à l'intégration Shopify pour le client ou via les services Braze de manière générale.

## 6. Documentation de conformité de la synchronisation d'audience {audience-sync-compliance-documentation}

Les conditions supplémentaires suivantes s'appliquent dans le cadre de l'utilisation de la synchronisation d'audience par le client.

### Conditions applicables du fournisseur tiers

Le client accepte de se conformer et d'être lié par toutes les conditions, politiques, directives et documentations applicables des fournisseurs tiers que le client utilise en lien avec les intégrations de synchronisation d'audience.

Le client reconnaît que les fournisseurs tiers peuvent examiner, filtrer et/ou supprimer toute donnée, publicité ou contenu utilisé en lien avec leurs services.

## 7. Documentation de conformité de l'archivage des messages et du chiffrement au niveau du champ {#message-archiving-and-field-level-encryption-compliance-documentation}

### Clause de non-responsabilité
Le client reconnaît que l'utilisation de l'archivage des messages et/ou du chiffrement au niveau du champ (chacun, la « **Fonctionnalité** ») peut avoir un impact sur la vitesse d'envoi des messages envoyés via les services Braze. Braze ne saurait être tenu responsable d'un tel impact, et tout engagement relatif à la vitesse d'envoi ne s'appliquera pas lorsque le client utilise la fonctionnalité. La fonctionnalité peut être utilisée pour soutenir les efforts de conformité du client, cependant le client reconnaît que Braze ne fait aucune déclaration ni garantie quant à savoir si l'utilisation de la fonctionnalité elle-même satisfait les obligations de conformité du client, et décline toute responsabilité à cet égard.

## 8. Documentation de conformité de la console agent {#agent-console-compliance-documentation}

### Fournisseurs de LLM en tant que sous-traitants ou fournisseurs tiers

Lorsque le client utilise une intégration avec un grand modèle de langage fourni par Braze via l'option Braze Auto dans les services Braze (« LLM fourni par Braze »), le fournisseur de ce LLM fourni par Braze agira en tant que sous-traitant de Braze, sous réserve des conditions de l'addendum relatif au traitement des données (DPA) entre le client et Braze.

Si le client choisit d'utiliser sa propre clé API pour s'intégrer aux fonctionnalités d'intelligence artificielle de Braze, le fournisseur de l'abonnement LLM propre au client sera considéré comme un fournisseur tiers, tel que défini dans le contrat entre le client et Braze.

## 9. Documentation de conformité du canal KakaoTalk {#kakaotalk-channel-compliance-documentation}

Les conditions supplémentaires suivantes s'appliquent dans le cadre de l'utilisation du canal KakaoTalk par le client :

### Conditions préalables

Pour envoyer des messages via le canal KakaoTalk, les clients doivent d'abord obtenir un compte KakaoTalk et souscrire un contrat pour les services KakaoTalk auprès des fournisseurs tiers impliqués dans la fourniture de la fonctionnalité KakaoTalk au client (« Fournisseurs tiers KakaoTalk »). Les comptes KakaoTalk sont approuvés et accordés par ces fournisseurs tiers KakaoTalk à leur seule discrétion.

### Conditions applicables du fournisseur tiers

En utilisant le canal KakaoTalk, le client accepte de se conformer et d'être lié par toutes les conditions et politiques applicables de KakaoTalk et des fournisseurs tiers KakaoTalk (collectivement, les « Conditions KakaoTalk ») et d'être responsable de son utilisation des services KakaoTalk. Pour plus de clarté, le client est responsable de tous les frais ou paiements dus à KakaoTalk et/ou aux fournisseurs tiers KakaoTalk pour l'utilisation de ces services de fournisseurs tiers KakaoTalk en lien avec le canal KakaoTalk.

{% multi_lang_include braze_legal/english_language_governance.md %}