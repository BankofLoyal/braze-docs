---
nav_title: Suivi des désinstallations
article_title: Suivi des désinstallations
page_order: 6
page_type: reference
description: "Cet article de référence couvre la mise en œuvre du suivi des désinstallations pour les statistiques au niveau de la campagne et de l'application."
tool: Reports

---

# Suivi des désinstallations

> Cet article montre comment visualiser l'ensemble des désinstallations d'applications au fil du temps pour repérer les tendances et les anomalies, et suivre les désinstallations au niveau des campagnes pour déterminer si une campagne spécifique favorise ou empêche les installations d'applications.

Le suivi des désinstallations dans Braze fournit les détails suivants :

1. Statistiques quotidiennes de désinstallation au niveau de l'application dans un graphique chronologique sur la page **d'accueil**.
2. Statistiques de désinstallation au niveau de la campagne dans un graphique chronologique sur la page **Détails de la campagne** d'une campagne spécifique. Cette statistique indique le nombre de destinataires de la campagne qui désinstallent chaque jour.

{% alert note %} 
Il est nécessaire d'activer le suivi des désinstallations sur votre tableau de bord de Braze. Cette fonctionnalité est disponible pour les applications sur iOS, Android et Fire OS. 
{% endalert %}

## Fonctionnement

Braze collecte automatiquement des informations basiques sur les désinstallations dans le cadre de vos campagnes de notification push habituelles. Cependant, comme la fréquence à laquelle les différents utilisateurs reçoivent des campagnes push peut varier, nous proposons un suivi des désinstallations pour fournir un aperçu plus précis de l'activité de désinstallation parmi vos utilisateurs.

Lorsque Braze détecte une désinstallation, l'utilisateur est marqué comme ayant désinstallé l'application. Si vous utilisez le filtre **N'a pas désinstallé** dans une campagne, ces utilisateurs marqués sont exclus. Si un utilisateur réinstalle l'application sans l'ouvrir, le marqueur de désinstallation reste sur son profil. Ce marqueur n'est supprimé que lorsque l'utilisateur démarre une nouvelle session dans l'application réinstallée. Cela signifie qu'un utilisateur qui réinstalle l'application sans jamais l'ouvrir continue d'apparaître comme ayant désinstallé.

Pour en savoir plus sur l'utilisation du suivi des désinstallations, consultez notre article de blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Activer le suivi des désinstallations

Vous pouvez activer le suivi des désinstallations sur la page **Paramètres des applications**, sous **Paramètres**, pour chaque application que vous souhaitez suivre.

Lorsque vous activez le suivi des désinstallations pour une application, Braze envoie chaque nuit un message push en arrière-plan aux utilisateurs qui n'ont pas enregistré de session ou reçu de push au cours des dernières 24 heures.

### Configuration

Pour configurer le suivi des désinstallations pour votre application iOS, utilisez une [méthode utilitaire]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Pour votre application Android, utilisez [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Lorsque Braze détecte une désinstallation, qu'il s'agisse du suivi des désinstallations ou de la distribution normale d'une campagne push, nous enregistrons la meilleure estimation de l'heure de désinstallation sur le profil de l'utilisateur. Cette information est stockée dans le profil utilisateur en tant qu'attribut standard et peut être utilisée pour définir un segment d'utilisateurs pour les campagnes de reconquête.

## Filtrage des segments en fonction des désinstallations

Le filtre **Désinstallé** sélectionne les utilisateurs qui ont désinstallé votre application dans une période donnée. Comme il est difficile de déterminer l'heure exacte d'une désinstallation, nous recommandons d'utiliser des plages de temps plus larges pour les filtres de désinstallation afin de s'assurer que toutes les personnes ayant désinstallé l'application soient incluses dans le segment à un moment donné.

Les statistiques quotidiennes sur les désinstallations sont disponibles sur la page **d'accueil**. 

![Segmentation de la désinstallation.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

Le graphique peut être décomposé par application et par segment, à l'instar d'autres statistiques fournies par Braze. Dans la section **Aperçu des performances**, sélectionnez votre plage de dates et, si vous le souhaitez, une application. Ensuite, faites défiler la page jusqu'au graphique des **performances dans le temps** et procédez comme suit :

1. Dans le menu déroulant **Statistiques pour**, sélectionnez **Désinstallations**.
2. Dans le menu déroulant **Répartition**, sélectionnez **Par segment**.
3. Dans le menu déroulant **Valeurs de répartition**, sélectionnez les segments à inclure dans le graphique.

{% alert note %}
Les applications sans suivi des désinstallations activé n'affichent les désinstallations que pour un sous-ensemble de leurs utilisateurs (ceux qui ont été ciblés avec des notifications push). Le nombre total de désinstallations quotidiennes peut donc être plus élevé que celui affiché.
{% endalert %}

## Suivi des désinstallations pour les campagnes

Le suivi des désinstallations de campagnes indique le nombre d'utilisateurs qui ont reçu une campagne spécifique et qui ont ensuite désinstallé votre application dans le délai sélectionné. Cet outil permet de comprendre comment les campagnes peuvent encourager des comportements négatifs involontaires de la part des utilisateurs et aide à mesurer l'efficacité globale de la campagne.

Les statistiques de désinstallation des campagnes se trouvent sur la page **Analyse de campagne** d'une campagne spécifique. Pour les campagnes multicanaux et multivariées, les désinstallations peuvent être ventilées respectivement par canal et par variante.

![Désinstallation au niveau de la campagne.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Fonctionnement

Braze suit les désinstallations en observant lorsque les messages push envoyés aux appareils des utilisateurs renvoient un signal provenant de Firebase Cloud Messaging (FCM) ou d'Apple Push Notification Service (APN) indiquant que l'application n'est plus installée. Si vous activez le suivi global des désinstallations pour une application, Braze envoie quotidiennement un message push silencieux aux utilisateurs afin de détecter s'ils ont désinstallé l'application. Braze envoie cette notification « silencieuse » à tous les utilisateurs (à moins que l'utilisateur n'ait désactivé les notifications silencieuses dans les paramètres de son application) ; la notification n'apparaît pas aux utilisateurs. Si Braze détecte qu'un utilisateur a désinstallé l'application, nous :

* Incrémentons d'une unité le nombre total de désinstallations de l'application.
* Incrémentons d'une unité le nombre de désinstallations pour chaque campagne que l'utilisateur a reçue avec succès au cours des dernières 24 heures.
* Si un utilisateur reçoit trois campagnes au cours d'une période de 24 heures puis désinstalle l'application, nous incrémentons le nombre de « désinstallations » pour les trois campagnes.

FCM et APN imposent des restrictions sur le suivi des désinstallations. Braze incrémente uniquement le nombre de désinstallations lorsque FCM ou APN nous informe qu'un utilisateur a désinstallé l'application. Cependant, ces systèmes tiers peuvent nous notifier les désinstallations à tout moment. Utilisez le suivi des désinstallations pour identifier les tendances générales plutôt que pour obtenir des statistiques précises.

## Résolution des problèmes

### Pourquoi le nombre de désinstallations augmente-t-il soudainement ?

Si vous constatez un pic de désinstallations de l'application, cela peut être dû à la révocation des anciens jetons à une fréquence différente par Firebase Cloud Messaging (FCM) et Apple Push Notification Service (APN).

{% alert note %} 
Pour des raisons de confidentialité, les fournisseurs de services push de Braze peuvent révoquer les jetons à intervalles irréguliers, ce qui signifie que le nombre de désinstallations peut parfois augmenter de manière significative au cours d'une période donnée.<br><br>Pour valider ces variations, surveillez le suivi des désinstallations parallèlement à un indicateur d'action utilisateur, tel que le taux d'ouverture directe des notifications push. Si les désinstallations augmentent fortement mais que les ouvertures directes restent stables, le pic reflète probablement la révocation d'anciens jetons par un fournisseur plutôt que le comportement réel des utilisateurs.
{% endalert %}

### Pourquoi le nombre de désinstallations d'applications diffère-t-il de ce qui figure dans les APN ?

Cette différence est normale. 

Apple utilise une planification aléatoire pour retarder le signalement lorsqu'un jeton push devient invalide, ce qui signifie que même après qu'un utilisateur a désinstallé une application, les APN peuvent continuer à renvoyer des réponses positives aux notifications push pendant un certain temps. Ce délai est intentionnel et vise à protéger la vie privée des utilisateurs. Aucun rebond ou échec ne sera signalé tant que les APN ne renvoient pas un statut `410` pour un jeton invalide.