---
nav_title: Erstellung von Nachrichten nach Kanal
article_title: Nachrichtenerstellung nach Kanal
page_order: 5
layout: dev_guide

guide_top_header: "Nachrichtenerstellung nach Kanal"
guide_top_text: "Messaging-Kanäle bieten Ihnen die Möglichkeit, virtuell mit Ihren Kund:innen zu kommunizieren – über Push-Benachrichtigungen auf dem Telefon oder im Webbrowser, E-Mails, In-App-Nachrichten und vieles mehr! Wenn Sie mehr über diese Kanäle erfahren möchten und wie Sie sie mit Braze nutzen können, lesen Sie die folgenden Abschnitte. Oder sehen Sie sich unsere Braze-Lernkurse zu <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>Messaging-Kanälen</a> an!<br><br>Mit Braze können Sie für jeden Kanal barrierefreie Messaging-Kampagnen erstellen. Arbeiten Sie mit Ihren Entwickler:innen zusammen, um sicherzustellen, dass Sie bei Ihrer Implementierung die Standards für Barrierefreiheit einhalten."
description: "Diese Landing-Page behandelt die Messaging-Kanäle von Braze. Messaging-Kanäle bieten Ihnen die Möglichkeit, virtuell mit Ihren Kund:innen zu kommunizieren – über Push-Benachrichtigungen auf dem Telefon oder im Webbrowser, E-Mails, In-App-Nachrichten und vieles mehr!"

guide_featured_title: "Verfügbare Kanäle"
guide_featured_list:
- name: Banner
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Content-Cards
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: E-Mail-Messaging
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "In-App-Messaging"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: "KakaoTalk"
  link: /docs/user_guide/message_building_by_channel/kakaotalk/
  image: /assets/img/braze_icons/phone-01.svg
- name: "LINE"
  link: /docs/user_guide/message_building_by_channel/line/
  image: /assets/img/braze_icons/phone-01.svg
- name: Push-Messaging
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: SMS, MMS und RCS
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Ressourcen zur Barrierefreiheit

Mit Braze können Sie für jeden Kanal barrierefreie Messaging-Kampagnen erstellen. Arbeiten Sie mit Ihren Entwickler:innen zusammen, um sicherzustellen, dass Sie bei Ihrer Implementierung die Standards für Barrierefreiheit einhalten. Wenn Sie zusätzliche Orientierung wünschen, empfehlen wir Ihnen:

- [Grundlagen für barrierefreies Messaging](https://learning.braze.com/accessible-messaging-foundations): In diesem Braze-Lernkurs lernen Sie die grundlegenden Prinzipien der Barrierefreiheit kennen, die für die Markenkommunikation gelten.
- [Barrierefreie Nachrichten erstellen]({{site.baseurl}}/help/accessibility/): Erfahren Sie, wie Sie direkt in Braze Alt-Text hinzufügen und Ihre Inhalte für unterstützende Technologien strukturieren können.

{% multi_lang_include accessibility/feedback.md %}

## Auswahl eines Messaging-Kanals

Wenn Sie entscheiden, welcher Messaging-Kanal für Ihre Kampagnen und Canvase am besten geeignet ist, denken Sie immer an den Inhalt und die Dringlichkeit Ihrer Nachricht:

- **Inhalt** beschreibt, wie visuell ansprechend Ihre Nachricht ist. Sie können Ihren Texten Multimedia- und andere Elemente hinzufügen, um Ihren Inhalt reichhaltiger zu gestalten.
- Die **Dringlichkeit** ist ein Maß dafür, wie schnell eine Nachricht Ihre Nutzer:innen erreichen und deren Aufmerksamkeit erregen kann. Benachrichtigungen, die sofort sichtbar sind, haben eine hohe Dringlichkeit, während Nachrichten, für die sich Nutzer:innen erst bei Ihrer App anmelden müssen, eine geringe Dringlichkeit haben.

Die Braze Messaging-Matrix vereinfacht die Kanalauswahl, indem sie die **Inhaltskomplexität** der **Zustellungsdringlichkeit** gegenüberstellt. Indem Sie diese beiden Faktoren ausbalancieren, sorgen Sie dafür, dass Ihre Nachricht ankommt, statt zu stören.

![Mobile/Web-Push sind einfache Inhalte, hohe Dringlichkeit; E-Mails sind reichhaltige Inhalte, hohe Dringlichkeit; In-App-/Browser-Nachrichten sind einfache Inhalte, niedrige Dringlichkeit; Content-Cards sind niedrige Dringlichkeit, reichhaltige Inhalte]({% image_buster /assets/img_archive/messaging_matrix.png %})

Die Matrix hebt zwar die wichtigsten Kanäle hervor, ist aber flexibel einsetzbar: SMS und WhatsApp zum Beispiel sind Tools mit hoher Dringlichkeit, die durch die Verwendung von Multimedia-Formaten auch reichhaltige Inhalte unterstützen. Wenn Sie mehr darüber erfahren möchten, wie Sie diese Matrix nutzen können, sehen Sie sich unseren Braze-Lernkurs zu [kanalübergreifendem Messaging](https://learning.braze.com/cross-channel-messaging) an.

<br><br>