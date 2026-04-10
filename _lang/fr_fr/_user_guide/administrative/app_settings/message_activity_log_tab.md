---
nav_title: Journal des activités du message
article_title: Journal des activités liées aux messages
page_order: 5
page_type: reference
description: "Cet article de référence décrit le journal d'activité des messages qui vous montre les messages associés à vos campagnes et à vos envois. Vous trouverez également ici des informations sur la façon de comprendre les messages du journal."

---

# Journal des activités de message {#dev-console-troubleshooting}

> Le **journal d'activité des messages** vous permet de voir tous les messages (en particulier les messages d'erreur) associés à vos campagnes et à vos envois.

Vous pouvez consulter les transactions de campagne API, résoudre les problèmes liés aux messages en échec et recueillir des informations sur la manière d'améliorer la distribution des notifications ou de résoudre les problèmes techniques existants.

Pour accéder au journal, allez dans **Paramètres** > **Journal d'activité des messages**.

![Journal des activités de message]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Outre cet article, nous vous recommandons également de consulter notre cours d'apprentissage Braze sur l'[assurance qualité et les outils de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), qui explique comment utiliser le journal d'activité des messages pour effectuer vos propres opérations de résolution des problèmes et de débogage.
{% endalert %}

Vous pouvez filtrer en fonction des contenus suivants enregistrés dans le **journal d'activité des messages** :

- Erreurs de notification push
- Erreurs de message annulé
- Erreurs de webhook
- Erreurs d'e-mail
- Enregistrements des messages API
- Erreurs de contenu connecté
- Erreurs d'audience connectée de l'API REST
- Erreurs d'aliasing de l'utilisateur
- Erreurs de test A/B
- Erreurs de SMS/MMS
- Erreurs WhatsApp
- Erreurs de Live Activity
- Erreurs de mauvais déclencheur utilisateur
- Erreurs de [limite quotidienne d'appels]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#monitor-your-agent) des agents Braze
- Erreurs de [modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) indisponible des agents Braze

Ces messages peuvent provenir de notre propre système, de vos apps ou plateformes, ou de nos partenaires tiers. Cela peut entraîner un nombre infini de messages pouvant apparaître dans ce journal.

## Comprendre les messages du journal

Pour déterminer ce que vos messages signifient, prêtez attention au libellé de chaque message et aux colonnes qui lui correspondent, car cela peut vous aider à résoudre les problèmes grâce aux indices contextuels. 

Par exemple, si vous avez une entrée de journal dont le message indique « empty-cart_app » et que vous n'êtes pas certain de sa signification, consultez la colonne **Type** à gauche. Si vous voyez « Erreur de message annulé », vous pouvez en déduire que le message correspondait à ce qui a été écrit comme [message d'annulation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) avec Liquid, et que le message a été annulé parce que le destinataire prévu disposait d'un panier vide dans votre application.

### Messages courants

Plusieurs types de messages courants existent, et certains peuvent même fournir des liens de résolution des problèmes pour vous aider à diagnostiquer et corriger les problèmes.

Les messages suivants sont donnés à titre d'exemple et peuvent ne pas correspondre exactement à ce qui est affiché dans la colonne **Message** de votre journal.

| Type de message | Message potentiel | Description |
|---|---|---|
| Échec provisoire d'envoi | L'adresse e-mail same@example.com a fait l'objet d'un échec provisoire d'envoi. | L'adresse e-mail était valide et le message e-mail a été acheminé jusqu'au serveur de messagerie du destinataire, mais a été rejeté pour un problème « temporaire ». <br><br>Les raisons les plus courantes de l'échec provisoire d'envoi sont les suivantes : {::nomarkdown} <ul> <li> La boîte de réception était pleine (l'utilisateur a dépassé son quota) </li> <li> Le serveur était hors service </li> <li> Le message était trop volumineux pour la boîte de réception du destinataire </li>  </ul> {:/} Si un e-mail a fait l'objet d'un échec provisoire d'envoi, nous effectuons généralement une nouvelle tentative dans les 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre. |
| Échec d'envoi définitif | Le compte e-mail que vous avez essayé de contacter n'existe pas. Essayez de vérifier que l'adresse e-mail du destinataire ne contient pas de fautes de frappe ou d'espaces inutiles. | Votre message n'a jamais atteint la boîte de réception de cette personne, car il n'y avait tout simplement pas de boîte de réception à atteindre. Si vous souhaitez approfondir vos recherches, les messages de ce type peuvent parfois comporter des liens dans la colonne **Afficher les détails** qui vous permettent de consulter le profil du destinataire prévu.|
| Bloc | Le message spam est rejeté en raison de la politique anti-spam. | Votre message a été classé comme spam. Cette erreur d'e-mail est enregistrée pour un utilisateur si nous avons reçu un événement de l'ESP indiquant que l'e-mail a été abandonné. Il se peut que cela ne concerne que le destinataire prévu, mais si vous recevez fréquemment ce message, il serait peut-être judicieux de réévaluer vos habitudes d'envoi ou le contenu de vos messages. Pensez aussi au passé : avez-vous [réchauffé votre IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) ? Si ce n'est pas le cas, contactez Braze pour obtenir des conseils sur la marche à suivre.|
| Erreur de message annulé | empty-cart_web | Si vous avez une application avec un panier ou que vous créez un envoi avec un message d'annulation dans le Liquid, vous pouvez personnaliser le message qui vous est renvoyé si l'envoi est annulé. Dans ce cas, le message renvoyé est empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Pourquoi mon message ne figure-t-il pas dans cette liste ?

Les messages du journal d'activité des messages peuvent provenir de différentes sources : Braze, vos apps ou plateformes, ou nos partenaires tiers. Cela signifie qu'il existe un nombre infini de messages susceptibles d'apparaître dans ce journal — comme vous pouvez l'imaginer, nous ne pouvons pas tous les énumérer !

Par exemple, certains messages de « blocage » potentiels, en plus de celui mentionné dans le tableau précédent, pourraient être les suivants :

- Malheureusement, les messages provenant de [_IP_ADDRESS_] n'ont pas été envoyés. Veuillez contacter votre fournisseur de services Internet car une partie de son réseau figure sur notre liste de blocage.
- Message rejeté en raison de la politique locale.
- Le message a été bloqué par le destinataire comme étant du spam.
- Service indisponible, l'hôte client [_IP_ADDRESS_] a été bloqué par Spamhaus.

## Durée de conservation des données

Les erreurs des 60 dernières heures sont disponibles dans les journaux d'activité des messages. Les journaux datant de plus de 60 heures sont nettoyés et ne sont plus accessibles.

### Nombre de journaux d'erreurs stockés

Le nombre de journaux enregistrés dépend de plusieurs conditions. Par exemple, si une campagne planifiée est envoyée à des milliers d'utilisateurs, seul un échantillon des erreurs pourrait apparaître dans le journal d'activité des messages, plutôt que la totalité. Voici un aperçu des conditions qui influencent le nombre de journaux enregistrés :
- Jusqu'à 20 journaux d'erreurs du même type sont enregistrés pour la même campagne ou étape du canvas au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreurs de contenu connecté
    - Erreurs de message d'annulation
    - Erreurs de webhook
    - Erreurs de rejet de SMS
    - Erreurs d'échec de réception/distribution des SMS
    - Erreurs d'échec WhatsApp
    - Erreurs de test A/B
- Jusqu'à 20 journaux d'erreurs de notification push du même type sont enregistrés pour la même combinaison de campagne ou étape du canvas et d'application pour les types d'erreurs suivants :
    - Informations d'identification push non valides
    - Jeton de notification push non valide
    - Aucune information d'identification push
    - Erreurs de jeton
    - Quota dépassé
    - Délai d'attente pour les nouvelles tentatives dépassé
    - PAYLOAD non valide
    - Erreur inattendue
- Jusqu'à 100 journaux d'erreurs du même type sont enregistrés pour la même application au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreur de Live Activity (aucune information d'identification push)
    - Erreur de Live Activity (informations d'identification push non valides)
    - Autres erreurs de Live Activity
    - Erreurs de jetons supprimés dans les retours APNs
- Jusqu'à 100 journaux d'erreurs du même type sont enregistrés pour la même campagne ou étape du canvas au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreurs d'échec provisoire d'envoi des e-mails
    - Erreurs d'échec d'envoi définitif des e-mails
    - Erreurs de blocage des e-mails
- Jusqu'à 100 journaux d'erreurs d'aliasing de l'utilisateur sont enregistrés pour le même espace de travail au cours d'une heure fixe.

## Envois de test

Le **journal d'activité des messages** affiche les journaux de test pour les canaux de communication suivants :

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Les journaux d'envoi de test ne sont pas disponibles pour les canaux suivants : e-mail, Content Cards, messages in-app et notifications push.

Les journaux d'envoi de test sont précédés du préfixe « [TEST SEND] », mais il n'est pas garanti que tous les journaux d'envoi de test comportent ce préfixe (par exemple, les erreurs de contenu connecté n'ont pas ce préfixe).