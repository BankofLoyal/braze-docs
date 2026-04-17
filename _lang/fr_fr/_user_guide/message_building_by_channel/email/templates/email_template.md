---
nav_title: "Créer un modèle d'e-mail"
article_title: Créer un modèle d'e-mail
page_order: 0
description: "Le présent article de référence explique comment créer, personnaliser et gérer des modèles d'e-mail."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Créer un modèle d'e-mail

> Le tableau de bord de Braze intègre un éditeur de modèles d'e-mails qui vous permet de créer des e-mails personnalisés et attrayants, puis de les enregistrer pour les réutiliser dans vos campagnes. Vous pouvez également télécharger votre propre [modèle d'e-mail HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/).

## Étape 1 : Accéder à l'éditeur de modèles d'e-mail

Allez dans **Modèles** > **Modèles d'e-mail**.

## Étape 2 : Sélectionner votre expérience d'édition 

Choisissez entre l'**éditeur par glisser-déposer** et l'**éditeur HTML** pour votre expérience d'édition. 

Ensuite, vous pouvez choisir parmi les modèles prédéfinis de Braze, créer un nouveau modèle ou modifier un modèle existant (simple ou [mobile responsive]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)).

![Un modèle d'e-mail pour les soldes de printemps d'une entreprise avec des options permettant de sélectionner l'éditeur par glisser-déposer ou l'éditeur HTML, ou de choisir parmi les modèles de Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Tous les modèles HTML personnalisés existants devront être recréés à l'aide de l'éditeur par glisser-déposer.
{% endalert %}

## Étape 3 : Personnaliser votre modèle

Après avoir sélectionné votre expérience d'édition, c'est le moment de laisser libre cours à votre créativité pour personnaliser votre modèle d'e-mail. Vous pouvez utiliser le HTML pour créer et reproduire votre image de marque dans l'éditeur HTML, ou intégrer une variété de [détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) dans l'éditeur par glisser-déposer.

### Inclure un lien de désabonnement

Lors de la conception de votre modèle d'e-mail, si vous n'incluez pas de lien de désabonnement, Braze vous invitera à l'ajouter, car la loi l'exige pour tous les e-mails marketing. Vous pouvez ajouter ce lien de désabonnement en pied de page au bas de vos e-mails à l'aide de l'étiquette Liquid {% raw %}``${email_footer}``{% endraw %}, ou en [personnalisant le pied de page]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) dans votre modèle.

## Étape 4 : Vérifier les erreurs d'e-mail

Les erreurs d'e-mail sont affichées dans l'onglet **Rédiger** du flux de travail du message. Les erreurs vous empêchent de passer à l'étape suivante. Les « Avertissements » sont des rappels pour vous aider à suivre les bonnes pratiques. Selon votre activité, vous pouvez choisir de les ignorer.

![Liste des erreurs et des avertissements d'un exemple d'e-mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Voici la liste des erreurs prises en compte dans notre éditeur :

- Syntaxe Liquid incorrecte
- [Corps d'e-mail supérieurs à 400 ko ; il est fortement recommandé que les corps soient inférieurs à 102 ko]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- Modèles sans lien de désabonnement
- E-mails dont le **corps** ou l'**objet** est vide
- E-mails sans lien de désabonnement

## Étape 5 : Prévisualiser et tester votre message

Une fois votre modèle finalisé, vous pouvez le tester avant de l'envoyer.

En bas de l'écran d'aperçu, sélectionnez **Prévisualiser et tester**. Vous pouvez y visualiser la façon dont votre e-mail apparaîtra dans la boîte de réception d'un client. Si l'option **Prévisualiser en tant qu'utilisateur** est sélectionnée, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de vérifier que vos appels de contenu connecté et de personnalisation fonctionnent correctement. 

Ensuite, vous pouvez **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Ce lien reste valide pendant sept jours, après quoi il devra être régénéré.

Vous pouvez également basculer entre les vues bureau, mobile et texte brut pour avoir un aperçu de votre message dans différents contextes.

{% alert tip %}
Vous aimeriez savoir à quoi ressemblent vos e-mails pour les utilisateurs en mode sombre ? Sélectionnez le bouton **Aperçu en mode sombre** situé dans la section **Prévisualiser et tester** (éditeur par glisser-déposer uniquement).
{% endalert %}

Lorsque vous êtes prêt pour une dernière vérification, sélectionnez **Tester l'envoi** et envoyez un message test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s'affiche correctement sur différents appareils et clients de messagerie.

![Exemple d'aperçu d'e-mail à envoyer pour test.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si vous rencontrez des problèmes avec votre modèle ou si vous souhaitez y apporter des modifications, sélectionnez **Modifier l'e-mail** pour revenir à l'éditeur.

## Étape 6 : Enregistrer votre modèle

Veillez à enregistrer votre modèle en sélectionnant **Enregistrer le modèle**. Vous êtes maintenant prêt à utiliser ce modèle dans toute campagne ou tout composant Canvas de votre choix. Pour accéder à votre modèle, sélectionnez l'expérience d'édition avec laquelle vous l'avez créé, puis sélectionnez-le dans la liste des modèles disponibles.

{% alert note %}
Si vous apportez des modifications à un modèle existant, ces modifications ne seront pas reflétées dans les campagnes créées avec les versions précédentes de ce modèle.
{% endalert %}

### Gérer vos modèles

Vous pouvez consulter vos modèles d'e-mail dans **Modèles** > **Modèles d'e-mail**, en filtrant par état, type ou étiquettes, ou en effectuant une recherche par nom. Vous devez disposer de l'autorisation **Accéder aux campagnes, Canvas, cartes, blocs de contenu, indicateurs de fonctionnalité, segments, bibliothèque multimédia, emplacements, codes de promotion et centres de préférences** (ou de l'autorisation granulaire équivalente, comme **Afficher les modèles d'e-mail**) pour consulter ces modèles. Pour plus de détails, consultez [Autorisations des utilisateurs]({{site.baseurl}}/user_guide/administrative/access_braze/user_permissions/).

Au fur et à mesure que vous créez des modèles d'e-mail, vous pouvez les [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) et les [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Pour en savoir plus, consultez la rubrique [Modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Utiliser vos modèles dans des campagnes API

Pour utiliser votre e-mail dans une campagne API, vous avez besoin d'un `email_template_id`, qui se trouve au bas de tout modèle d'e-mail créé dans Braze.

![Identifiant API situé au bas d'un modèle d'e-mail.]({% image_buster /assets/img/email_templates/template5.png %})

### Commenter les modèles d'e-mail

Vous pouvez collaborer et commenter les modèles d'e-mail dans l'éditeur par glisser-déposer. 

1. Sélectionnez le bloc de contenu ou la ligne dans le corps de l'e-mail que vous souhaitez commenter.
2. Sélectionnez l'icône de commentaire <i class="fas fa-comment"></i>.
3. Saisissez votre commentaire dans la barre latérale, puis sélectionnez **Envoyer**.
4. Après avoir saisi vos commentaires, sélectionnez **Terminé**.
5. Sélectionnez **Enregistrer le modèle** pour enregistrer vos commentaires.

Une fois votre modèle enregistré, les utilisateurs peuvent voir des icônes sur les commentaires non traités. Sélectionnez **Résoudre** pour résoudre ces commentaires.

![Un commentaire sur un modèle d'e-mail qui dit « Ça me paraît bien ».]({% image_buster /assets/img/email_templates/template_comment.png %})

Pour obtenir des réponses aux questions fréquemment posées sur les modèles d'e-mail, consultez notre [FAQ sur les modèles]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).