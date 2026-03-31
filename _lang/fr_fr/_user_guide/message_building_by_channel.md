---
nav_title: Créer des messages par canal
article_title: Création de message par canal
page_order: 5
layout: dev_guide

guide_top_header: "Création de message par canal"
guide_top_text: "Les canaux de communication vous permettent de communiquer virtuellement avec vos clients via des notifications push sur leur téléphone ou navigateur web, par e-mail, par messages in-app et bien plus encore ! Si vous souhaitez en savoir plus sur ces canaux et comment les utiliser avec Braze, consultez les sections ci-dessous. Ou découvrez nos cours d'apprentissage Braze sur les <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>canaux de communication</a> !<br><br>Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Vérifiez avec vos ingénieurs que vous répondez aux normes d'accessibilité lors de la mise en place."
description: "Cette page d'accueil couvre les canaux de communication Braze. Les canaux de communication vous permettent de communiquer virtuellement avec vos clients via des notifications push sur leur téléphone ou navigateur web, par e-mail, par messages in-app et bien plus encore !"

guide_featured_title: "Canaux disponibles"
guide_featured_list:
- name: Bannières
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Cartes de contenu
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: E-mail
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "Messages in-app"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: "KakaoTalk"
  link: /docs/user_guide/message_building_by_channel/kakaotalk/
  image: /assets/img/braze_icons/phone-01.svg
- name: "LINE"
  link: /docs/user_guide/message_building_by_channel/line/
  image: /assets/img/braze_icons/phone-01.svg
- name: Notifications push
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: SMS, MMS et RCS
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Ressources en matière d'accessibilité

Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Vérifiez avec vos ingénieurs que vous répondez aux normes d'accessibilité lors de la mise en place. Si vous souhaitez obtenir des conseils supplémentaires, nous vous recommandons :

- [Fondements de l'envoi de messages accessibles](https://learning.braze.com/accessible-messaging-foundations) : apprenez les principes fondamentaux de l'accessibilité qui s'appliquent aux communications de marque dans ce cours d'apprentissage Braze.
- [Créer des messages accessibles]({{site.baseurl}}/help/accessibility/) : apprenez à ajouter du texte alt et à structurer votre contenu pour les technologies d'assistance directement dans Braze.

{% multi_lang_include accessibility/feedback.md %}

## Choisir un canal de communication

Lorsque vous déterminez quel canal de communication est le mieux adapté à vos campagnes et Canvas, pensez toujours au contenu et à l'urgence de votre message :

- Le **contenu** désigne le degré d'attrait visuel de votre message. Vous pouvez ajouter du multimédia et d'autres ressources à votre texte pour enrichir votre contenu.
- L'**urgence** mesure la rapidité avec laquelle un message est capable de notifier votre utilisateur et d'attirer son attention. Les notifications directement visibles par l'utilisateur ont un caractère urgent ; à l'inverse, les messages nécessitant une connexion de l'utilisateur à votre application n'ont pas de caractère d'urgence.

La matrice de messages de Braze simplifie la sélection des canaux en croisant la **complexité du contenu** avec l'**urgence de la distribution**. En équilibrant ces deux facteurs, vous pouvez faire en sorte que votre message résonne plutôt qu'il n'interrompe.

![Les notifications push web ou mobile ont un contenu simple avec une urgence élevée ; les e-mails ont un contenu riche avec une urgence élevée ; les messages in-app/navigateur ont un contenu simple avec une faible urgence ; les cartes de contenu ont une faible urgence avec un contenu riche]({% image_buster /assets/img_archive/messaging_matrix.png %})

Bien que la matrice mette l'accent sur les canaux essentiels, elle est adaptable : les SMS et WhatsApp, par exemple, sont des outils à forte urgence qui se prêtent aussi au contenu riche lorsqu'ils utilisent des formats multimédias. Pour en savoir plus sur la manière de tirer parti de cette matrice, consultez notre cours d'apprentissage Braze sur la [communication cross-canal](https://learning.braze.com/cross-channel-messaging).

<br><br>