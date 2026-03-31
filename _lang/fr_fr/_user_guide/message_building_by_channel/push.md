---
nav_title: Notification push
article_title: Notification push
page_order: 6
layout: dev_guide
guide_top_header: "Notification push"
guide_top_text: "Les notifications push constituent un moyen éprouvé d'envoyer des appels à l'action urgents via mobile ou web, ainsi que de favoriser le réengagement des utilisateurs qui n'ont pas utilisé l'application depuis un certain temps. Elles dirigent l'utilisateur directement vers le contenu et démontrent la valeur de votre application. Les notifications push sont utiles pour diriger les utilisateurs vers un endroit spécifique, mais il est important de les utiliser avec discernement. <br><br> Lisez l'un des articles suivants ou consultez notre [cours d'apprentissage Braze sur les notifications push](https://learning.braze.com/messaging-channels-push) pour savoir à qui vous pouvez envoyer une notification push, comment l'envoyer et quelles sont les fonctionnalités avancées offertes par Braze pour les notifications push. Pour des exemples de notifications push, consultez nos [témoignages clients](https://www.braze.com/customers)."
description: "Cette page d'accueil regroupe tout ce qui concerne les notifications push. Vous y trouverez des articles sur les types de notification push, l'inscription aux notifications push, l'activation des notifications push, les amorces de notification push, le reporting des notifications push, et bien plus encore."
channel:
  - push

guide_featured_title: "Articles populaires"
guide_featured_list:
- name: Types de notifications push
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: Enregistrement d'une notification push
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Activation et abonnement aux notifications push
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: Créer un message push
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "Autres articles"
guide_menu_list:
- name: Options avancées
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: Amorces de notifications push
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Reporting
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Options Android
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: Options iOS
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Notification push web
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Bonnes pratiques
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Locales dans les messages
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: Messages d'erreur push courants
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: Résolution des problèmes
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: Foire aux questions
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}Cas d'utilisation

![Exemple de notification push sur des produits Apple.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![Exemple de notification push de Stopwatch sur un écran d'accueil iPhone affichant : « Bonjour ! Ceci est une notification push iOS ».]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

Les notifications push constituent un excellent outil pour attirer de nouveaux utilisateurs et mener des campagnes de réengagement. Voici quelques exemples de cas d'utilisation courants.

| Cas d'utilisation | Explication |
| -------- | ----------- |
| Onboarding initial | Tant que les utilisateurs n'ont pas franchi les premières étapes d'utilisation de votre application (comme la création d'un compte), leur valeur reste très limitée. Utilisez les notifications push pour les inciter à effectuer ces étapes afin qu'ils puissent profiter pleinement de votre application. |
| Premiers achats | Une fois que les utilisateurs sont à l'aise avec votre application, vous pouvez utiliser les notifications push pour les convertir en acheteurs in-app. |
| Nouvelles fonctionnalités | Les notifications push peuvent être un moyen efficace d'informer les utilisateurs désengagés de nouvelles fonctionnalités susceptibles de les ramener vers votre application. |
| Offres limitées dans le temps | Si vous avez une offre à durée limitée, une notification push peut être un excellent moyen d'en informer vos utilisateurs avant son expiration. Ces messages transmettent généralement un fort sentiment d'urgence et sont particulièrement adaptés pour rappeler votre application aux utilisateurs récemment inactifs.<br><br> Par exemple, supposons que votre application soit un jeu et que vous offriez à vos utilisateurs un bonus de monnaie virtuelle s'ils maintiennent une série de jeu quotidienne. Alerter un utilisateur que sa série risque d'être interrompue peut être pertinent s'il a dépassé un certain nombre de jours sans jouer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour en savoir plus sur le réengagement des utilisateurs inactifs, consultez notre page [Quick Wins]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) sur le sujet.

## Conditions préalables à l'utilisation des notifications push

Avant de pouvoir créer et envoyer des notifications push avec Braze, vous devez collaborer avec vos développeurs pour intégrer les notifications push à votre site web ou à votre application. Pour des instructions détaillées, consultez nos guides d'intégration pour chaque plateforme :

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Amorçage des notifications push

N'oubliez pas que les utilisateurs doivent s'abonner aux notifications push pour recevoir vos messages. Il est donc judicieux d'utiliser des messages in-app pour expliquer à vos clients pourquoi vous souhaitez leur envoyer des notifications push et en quoi leur activation leur sera bénéfique. Ce processus est appelé [amorçage de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Réglementations relatives aux notifications push

Les notifications push étant un type d'envoi de messages intrusif qui s'affiche directement sur le téléphone ou le navigateur de vos clients, il existe des directives encadrant leur envoi via des applications et des sites.

### Réglementations des notifications push mobiles pour les applications

{% alert important %}
Vos notifications push doivent être conformes aux directives de l'App Store d'Apple et aux politiques du Google Play Store, notamment en ce qui concerne l'utilisation des notifications push à des fins publicitaires, de spam, de promotions, etc.
{% endalert %}

|Politiques de l'App Store d'Apple|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inacceptable : (i) Créer une interface pour afficher des applications, des extensions ou des plug-ins tiers de manière similaire à l'App Store ou en tant que collection d'intérêt général.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Les notifications push ne doivent pas être nécessaires au fonctionnement de l'app et ne doivent pas être utilisées pour envoyer des informations personnelles ou confidentielles sensibles. Les notifications push ne doivent pas être utilisées à des fins de promotion ou de marketing direct, sauf si les clients ont explicitement choisi de les recevoir via un texte de consentement affiché dans l'interface utilisateur de votre application, et si vous fournissez dans votre application un moyen pour l'utilisateur de refuser de recevoir de tels messages.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Vous ne pouvez pas monétiser les capacités intégrées fournies par le matériel ou le système d'exploitation, telles que les notifications push, l'appareil photo ou le gyroscope, ni les services et technologies Apple, tels que l'accès à Apple Music, le stockage iCloud ou les API Screen Time.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Politique du Google Play Store|
|---|
|[Utilisation non autorisée ou imitation des fonctionnalités système](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Nous n'autorisons pas les applications ou les publicités qui imitent ou interfèrent avec les fonctionnalités système, comme les notifications ou les avertissements. Les notifications système ne peuvent être utilisées que pour les fonctionnalités essentielles d'une application, comme l'application d'une compagnie aérienne qui informe les utilisateurs d'offres spéciales, ou un jeu qui informe les utilisateurs de promotions en cours de jeu.|
{: .reset-td-br-1 role="presentation" }