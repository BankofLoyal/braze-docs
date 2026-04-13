{% alert important %}
Braze introduit [des autorisations granulaires]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), une méthode plus flexible pour gérer l'accès des utilisateurs. Consultez la section [Migration vers des autorisations granulaires]({{site.baseurl}}/granular_permissions_migration/) pour en savoir plus sur le processus de migration, y compris sur la correspondance entre les autorisations héritées et les autorisations granulaires.
{% endalert %}

## Création d'un ensemble d'autorisations

Utilisez les ensembles d'autorisations pour regrouper les autorisations liées à des domaines ou actions spécifiques. Vous pouvez appliquer des ensembles d'autorisations aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un ensemble d'autorisations, accédez à **Paramètres** > **Paramètres des autorisations**, puis sélectionnez **Créer un ensemble d'autorisations**. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nom|Autorisations|
|-----------|----------------|
|Développeurs|« Accéder à la console de développement »|
|Marketeurs|« Accéder aux campagnes, aux Canvas, aux cartes, aux indicateurs de fonctionnalité, aux segments, à la bibliothèque multimédia et aux centres de préférences » <br> « Gérer les ressources de la bibliothèque multimédia »|
|Gestion des utilisateurs|« Gérer les utilisateurs du tableau de bord » <br> « Gérer les équipes »|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Création d'un rôle

Les rôles permettent une meilleure structuration en regroupant vos autorisations personnalisées individuelles avec les contrôles d'accès à l'espace de travail. C'est particulièrement utile si vous avez plusieurs marques ou espaces de travail régionaux dans un seul tableau de bord. Grâce aux rôles, vous pouvez ajouter les utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nom du rôle    | Espace de travail | Autorisations  
----------- | ----------- | ---------
| Marketeur - Marques de mode | {::nomarkdown}[DEV] Marque de mode, [QA] Marque de mode, [PROD] Marque de mode {:/} | « Accéder aux campagnes, aux Canvas, aux cartes, aux indicateurs de fonctionnalité, aux segments, à la bibliothèque multimédia et au centre de préférences »<br>« Gérer les ressources de la bibliothèque multimédia » |
| Marketeur - Marques de soins de la peau | {::nomarkdown}[DEV] Marque de soins de la peau, [QA] Marque de soins de la peau, [PROD] Marque de soins de la peau {:/} | « Accéder aux campagnes, aux Canvas, aux cartes, aux indicateurs de fonctionnalité, aux segments, à la bibliothèque multimédia et aux centres de préférences » <br>« Gérer les ressources de la bibliothèque multimédia » |
| Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Marque de mode, [QA] Marque de mode, [PROD] Marque de mode, [DEV] Marque de soins de la peau, [QA] Marque de soins de la peau, [PROD] Marque de soins de la peau {:/} | « Gérer les utilisateurs du tableau de bord »<br>« Gérer les équipes » |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## En quoi les ensembles d'autorisations et les rôles diffèrent-ils des équipes ?

{% multi_lang_include permissions.md content="Differences" %}

### Points à considérer lors de l'ajout d'autorisations utilisateur aux équipes

Vous pourriez rencontrer des difficultés lorsque vous essayez d'enregistrer les autorisations dans le tableau de bord de Braze, en particulier lorsque vous ajoutez ou supprimez des utilisateurs d'un espace de travail, ou lorsque vous les ajoutez à une équipe. Le bouton **Enregistrer/Mettre à jour les utilisateurs** peut être grisé si les autorisations de l'utilisateur sont identiques à celles dont il dispose déjà au niveau de l'espace de travail. Cette restriction existe car il n'y a aucun avantage à disposer d'une équipe si tous les utilisateurs possèdent les mêmes autorisations que l'ensemble de l'espace de travail.

Pour ajouter un utilisateur à une équipe tout en conservant les mêmes autorisations, n'attribuez aucune autorisation au niveau de l'espace de travail. Attribuez plutôt les autorisations exclusivement au niveau de l'équipe.

## Utilisateurs limités

Les utilisateurs limités disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze, tout en étant soumis à des restrictions par rapport aux administrateurs d'entreprise et aux administrateurs d'espace de travail.

| Autorisations | Les utilisateurs limités peuvent modifier les autorisations d'autres utilisateurs limités s'ils disposent de l'autorisation « Gérer les utilisateurs du tableau de bord ». Ils peuvent également créer de nouveaux utilisateurs limités et modifier leurs ensembles d'autorisations. Cependant, ils ne peuvent pas créer ni gérer de comptes administrateur d'entreprise. |
| Limitations des rôles | Si un utilisateur limité dispose de toutes les autorisations à l'exception de « Administrateur du groupe d'applications », il aura toujours accès à toutes les autres autorisations généralement accordées à un administrateur d'espace de travail. |
| Visibilité des autorisations | Si un utilisateur limité a coché « Gérer les utilisateurs du tableau de bord » pour un groupe d'applications (tel que Dev), mais pas pour un autre (tel que Prod), il ne verra pas les autorisations du groupe d'applications Prod dans son profil « Gérer les utilisateurs ». |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparaison des utilisateurs limités

| Type d'utilisateur limité | Description |
| --- | --- |
| Administrateur du groupe d'applications | Les administrateurs de groupes d'applications disposent d'autorisations spécifiques à la gestion des groupes d'applications, mais n'ont pas les mêmes prérogatives que les administrateurs d'entreprise. Les utilisateurs limités peuvent hériter d'autorisations similaires à celles des administrateurs de groupes d'applications s'ils disposent des autorisations nécessaires. |
| Administrateur d'entreprise | Les administrateurs d'entreprise disposent d'autorisations plus étendues, notamment la possibilité de supprimer des utilisateurs du tableau de bord. Cependant, ils ne peuvent pas supprimer leur propre compte et doivent contacter un autre administrateur d'entreprise pour cette action. |
| Autorisation de lecture seule de base | Pour accéder à certaines parties du tableau de bord, telles que la page Partenaires technologiques, les utilisateurs doivent disposer d'une autorisation de base en lecture seule. Cela implique d'activer l'option « Gérer les intégrations externes » et d'accorder les autorisations d'accès aux campagnes, aux Canvas, aux cartes, aux segments et à la bibliothèque multimédia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erreur d'accès restreint

Les utilisateurs peuvent rencontrer des messages tels que « Accès limité. Vous n'avez pas les autorisations nécessaires pour accéder à cette page. » Dans ce cas, l'administrateur du compte doit vérifier s'il est possible de résoudre le problème en désactivant puis en réactivant les autorisations de l'utilisateur.

{% alert note %}
Il n'est pas possible de fusionner ou d'importer les autorisations d'un utilisateur du tableau de bord vers un autre.
{% endalert %}

## Modifier les autorisations d'un utilisateur

Pour modifier les autorisations actuelles d'un utilisateur (administrateur, entreprise ou espace de travail), accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez son nom.

![La page « Utilisateurs de l'entreprise » dans Braze avec un utilisateur répertorié dans les résultats.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Les administrateurs ont accès à toutes les fonctionnalités et peuvent modifier tous les paramètres de l'entreprise. Ils peuvent :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Ajouter, modifier, supprimer, suspendre ou réactiver d'autres [utilisateurs de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- Exporter les utilisateurs de Braze au format CSV

Pour accorder ou retirer les privilèges d'administrateur, sélectionnez **Cet utilisateur est un administrateur**, puis sélectionnez **Mettre à jour l'utilisateur**.

![Les détails de l'utilisateur sélectionné avec la case à cocher admin mise en évidence.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Si vous retirez les privilèges d'administrateur à un utilisateur, celui-ci ne pourra plus accéder à Braze tant que vous ne lui aurez pas attribué au moins une autorisation [au niveau de l'entreprise ou de l'espace de travail]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions&tab=company#legacypermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Entreprise

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case en regard de l'autorisation concernée. Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

|Nom de l'autorisation|Description|
|----------|-----------|
|Gérer les paramètres de l'entreprise|Permet aux utilisateurs de modifier n'importe quel paramètre de l'entreprise.|
|Créer et supprimer des espaces de travail|Permet aux utilisateurs de créer et de supprimer des espaces de travail.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espace de travail

Vous pouvez attribuer à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer ses autorisations au niveau de l'espace de travail, sélectionnez **Sélectionner les espaces de travail et les autorisations**, puis choisissez manuellement les autorisations ou attribuez un ensemble d'autorisations [que vous avez précédemment créé]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_creating-a-permission-set).

Si vous devez attribuer à un utilisateur des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Autorisations**, choisissez une ou plusieurs autorisations dans la liste déroulante. Braze n'attribue ces autorisations qu'aux espaces de travail que vous avez sélectionnés. Vous pouvez également sélectionner **Activer l'accès administrateur** si vous souhaitez accorder toutes les autorisations pour cet espace de travail.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Les autorisations au niveau de l'espace de travail sont sélectionnées manuellement dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual_legacy.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Ensembles d'autorisations**, choisissez un ensemble d'autorisations. Braze n'attribue ces autorisations qu'aux espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Autorisations au niveau de l'espace de travail attribuées via un ensemble d'autorisations dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set_legacy.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporter les autorisations des utilisateurs

Pour télécharger une liste de vos utilisateurs et de leurs autorisations, accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez **Exporter les utilisateurs**. Un fichier CSV sera envoyé à votre adresse e-mail dans les plus brefs délais.

![La page « Utilisateurs de l'entreprise » dans Braze avec l'option « Exporter les utilisateurs » mise en évidence.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste des autorisations

|Niveau|Nom|Définition|
|---|---|---|
|Admin|Admin|Permet aux utilisateurs d'accéder à toutes les fonctionnalités disponibles. Il s'agit du paramètre par défaut pour tous les nouveaux utilisateurs. Peut mettre à jour les paramètres de l'entreprise (nom de l'entreprise et fuseau horaire), ce que les utilisateurs limités ne peuvent pas faire.|
|Entreprise|Créer et supprimer des espaces de travail|Permet aux utilisateurs de créer et de supprimer des espaces de travail.|
|Entreprise|Gérer les paramètres de l'entreprise|Permet aux utilisateurs de modifier n'importe quel paramètre de l'entreprise.|
|Espace de travail|Accéder aux campagnes, aux Canvas, aux cartes, aux blocs de contenu, aux indicateurs de fonctionnalité, aux segments, à la bibliothèque multimédia, aux emplacements, aux codes de promotion et aux centres de préférences|Permet aux utilisateurs de consulter les indicateurs de performance des campagnes et des Canvas, de créer et de dupliquer des brouillons de campagnes et de Canvas, de modifier des brouillons et des modèles de campagnes et de Canvas, de consulter des brouillons de segments, des modèles et des médias, de créer des modèles, de télécharger des médias, de créer ou de mettre à jour des listes de codes de promotion, de consulter les rapports d'engagement et de consulter les paramètres généraux des messages dans le tableau de bord. Cependant, les utilisateurs disposant de cette autorisation ne peuvent pas suspendre ni modifier le contenu en ligne existant.<br><br> Lorsque cette autorisation est configurée en tant qu'[autorisation d'équipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), si des campagnes ou des Canvas dans le [rapport d'engagement]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) ne font pas partie des équipes attribuées à un utilisateur ou n'ont aucune équipe attribuée, le rapport est masqué pour cet utilisateur.|
|Espace de travail|Accéder à la console de développement|Permet un accès complet aux paramètres et journaux suivants :{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Clés API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Groupes internes</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Journal d'activité des messages</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Journal des événements utilisateurs</a></li></ul>{:/}|
|Espace de travail|Approuver et refuser des campagnes|Permet aux utilisateurs d'approuver ou de refuser des campagnes. Le [processus d'approbation des campagnes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement disponible en accès anticipé. Contactez votre Account Manager si vous souhaitez participer à l'accès anticipé.|
|Espace de travail|Approuver et refuser des Canvas|Permet aux utilisateurs d'approuver ou de refuser des Canvas. Le [processus d'approbation des Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique.|
|Espace de travail|Modifier les intégrations Currents|Permet aux utilisateurs de modifier une connexion Currents, y compris les informations d'identification. Par défaut, les utilisateurs auxquels est attribuée l'autorisation « Intégrations externes » se voient également attribuer cette autorisation.|
|Espace de travail|Modifier les segments|Permet aux utilisateurs de créer et de modifier des segments. Vous pouvez toujours créer des campagnes avec des segments et des filtres existants sans cette autorisation. Vous avez besoin de cette autorisation pour générer un segment à partir d'utilisateurs dans un fichier CSV ou recibler le groupe d'utilisateurs dans le fichier CSV.|
|Espace de travail|Exporter les données utilisateur|Permet aux utilisateurs d'exporter leurs données utilisateur à partir des segments, des campagnes et des Canvas. Cette autorisation inclut des informations sensibles sur les utilisateurs, telles que les noms, les adresses e-mail et d'autres informations personnelles identifiables (IPI) collectées. Pour exporter des fichiers CSV depuis le tableau de bord, vous devez disposer de cette autorisation ainsi que de l'autorisation « Afficher les IPI ».|
|Espace de travail|Importer et mettre à jour les données utilisateur|Permet aux utilisateurs d'importer des fichiers CSV et de mettre à jour les fichiers des utilisateurs d'applications, ainsi que de consulter la page d'importation d'utilisateurs. Cela permet également de modifier le statut d'abonnement d'un utilisateur et les règles d'abonnement/de désabonnement de son groupe d'abonnement.|
|Espace de travail|Lancer et gérer les blocs de contenu|Permet aux utilisateurs de lancer et de gérer des [blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espace de travail|Lancer les centres de préférences|Permet aux utilisateurs de lancer des [centres de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espace de travail|Gérer les applications|Permet aux utilisateurs de modifier les **Paramètres de l'application**.|
|Espace de travail|Gérer les autorisations du tableau de bord des catalogues|Permet aux utilisateurs de créer et de gérer des catalogues.|
|Espace de travail|Gérer les utilisateurs du tableau de bord| Permet aux non-administrateurs de consulter, modifier et gérer la page **Utilisateurs de l'entreprise**, et de gérer les utilisateurs du tableau de bord dans leur espace de travail en modifiant les autorisations de n'importe quel utilisateur, y compris les leurs. Les utilisateurs disposant de cette autorisation ne peuvent pas supprimer des utilisateurs (seuls les administrateurs peuvent supprimer des utilisateurs).<br><br>Ceci correspond à l'autorisation héritée `MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Espace de travail|Gérer les paramètres des e-mails|Permet aux utilisateurs d'enregistrer les modifications apportées à la configuration des e-mails (**Paramètres** > **Préférences e-mail**).|
|Espace de travail|Gérer les événements, attributs et achats|Permet aux utilisateurs de modifier les attributs personnalisés (les utilisateurs qui n'ont pas cette capacité peuvent toujours consulter les attributs personnalisés), de modifier et de consulter les propriétés des événements personnalisés, et de modifier et de consulter les propriétés des produits sous **Paramètres des données**.|
|Espace de travail|Gérer les intégrations externes|Permet d'accéder à tous les onglets sous **Partenaires technologiques**, de synchroniser Braze avec d'autres plateformes et de gérer l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Espace de travail|Gérer les indicateurs de fonctionnalité|Permet aux utilisateurs de créer ou de modifier des [indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/).|
|Espace de travail|Gérer les ressources de la bibliothèque multimédia|Permet aux utilisateurs d'ajouter, de modifier et de supprimer des ressources de la bibliothèque multimédia.|
|Espace de travail|Gérer les groupes d'abonnement|Permet aux utilisateurs de créer et de gérer des groupes d'abonnement.|
|Espace de travail|Gérer les étiquettes|Permet aux utilisateurs de modifier ou de supprimer des étiquettes (sous **Gestion des étiquettes**). Vous n'avez pas besoin de cette autorisation pour ajouter des étiquettes aux campagnes ou segments.|
|Espace de travail|Gérer les équipes|Permet aux utilisateurs de gérer les **équipes internes**. La possibilité de sélectionner cette autorisation dépend de votre contrat avec Braze.<br><br>Ceci correspond à l'autorisation héritée `MANAGE_TERRITORIES`.|
|Espace de travail|Gérer les transformations|Permet aux utilisateurs de créer et de gérer des transformations de données.|
|Espace de travail|Envoyer des campagnes et des Canvas|Permet aux utilisateurs de modifier, d'archiver et d'arrêter des campagnes et des Canvas, de créer des campagnes et de lancer des Canvas.|
|Espace de travail|Afficher les détails de facturation|Permet aux utilisateurs de consulter les abonnements et la facturation.|
|Espace de travail|Voir l'intégration Currents|Permet aux utilisateurs de consulter toutes les informations relatives à une connexion Currents, à l'exception des informations d'identification. Par défaut, cette autorisation est également attribuée aux utilisateurs disposant de l'autorisation « Accéder aux campagnes, aux Canvas, aux cartes, aux blocs de contenu, aux indicateurs de fonctionnalité, aux segments, à la bibliothèque multimédia, aux emplacements, aux codes de promotion et aux centres de préférences ».|
|Espace de travail|Afficher les attributs personnalisés marqués comme IPI|Permet aux utilisateurs non administrateurs de consulter les attributs personnalisés qui contiennent des informations sensibles et sont marqués comme des informations personnelles identifiables (IPI).|
|Espace de travail|Afficher les IPI|Permet aux utilisateurs de consulter les champs d'informations personnelles identifiables (IPI) tels que définis par votre entreprise dans le tableau de bord. Les utilisateurs peuvent également consulter les champs IPI dans l'onglet **Prévisualiser en tant qu'utilisateur** des aperçus de messages.<br><br>Vous avez besoin de cette autorisation pour utiliser le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), car il permet d'accéder directement à certaines données clients. Pour exporter des fichiers CSV depuis le tableau de bord, les utilisateurs doivent disposer à la fois de cette autorisation et de l'autorisation « Exporter les données utilisateur ».|
|Espace de travail|Voir les profils utilisateur conformes aux IPI|Permet aux utilisateurs de consulter des profils utilisateur contenant des champs que votre entreprise a définis comme des informations personnelles identifiables (IPI), tout en masquant les champs IPI.<br><br>Vous avez besoin de cette autorisation pour utiliser l'outil de recherche d'utilisateurs.|
|Espace de travail|Afficher les transformations|Permet aux utilisateurs de consulter les [transformations de données de Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Espace de travail|Afficher les données d'utilisation|Permet aux utilisateurs de consulter l'utilisation de l'application, y compris les tableaux de bord des performances des canaux.|
|Espace de travail|Fusionner les utilisateurs dupliqués|Permet aux utilisateurs de fusionner des profils utilisateur en double.|
|Espace de travail|Prévisualiser les utilisateurs dupliqués|Permet aux utilisateurs de voir quels profils utilisateur sont dupliqués.|
|Espace de travail|Créer et modifier des modèles Canvas|Permet aux utilisateurs de créer et de modifier des modèles Canvas.|
|Espace de travail|Afficher les modèles Canvas|Permet aux utilisateurs de consulter les modèles Canvas.|
|Espace de travail|Archiver les modèles Canvas|Permet aux utilisateurs d'archiver des modèles Canvas.|
|Espace de travail|Gérer la segmentation des propriétés d'événements personnalisés|Permet aux utilisateurs de créer des segments basés sur la récurrence et la fréquence des propriétés d'événement.|
|Espace de travail|Publier des landing pages|Permet aux utilisateurs de publier des [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Espace de travail|Créer des brouillons de landing pages|Permet aux utilisateurs de créer et d'enregistrer des brouillons de landing pages.|
|Espace de travail|Accéder aux landing pages|Permet aux utilisateurs d'accéder à la page **Landing Pages**.|
|Espace de travail|Créer et modifier des modèles de landing pages|Permet aux utilisateurs de créer et de modifier des modèles de landing pages.|
|Espace de travail|Voir les modèles de landing pages|Permet aux utilisateurs de consulter les modèles de landing pages.|
|Espace de travail|Archiver les modèles de landing pages|Permet aux utilisateurs d'archiver des modèles de landing pages.|
|Espace de travail|Voir les agents d'intelligence artificielle personnalisés|Permet aux utilisateurs de consulter les [agents d'intelligence artificielle personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/). Cette fonctionnalité est actuellement en version bêta.|
|Espace de travail|Créer des agents d'intelligence artificielle personnalisés|Permet aux utilisateurs de créer des agents d'intelligence artificielle personnalisés. Cette fonctionnalité est actuellement en version bêta.|
|Espace de travail|Modifier les agents d'intelligence artificielle personnalisés|Permet aux utilisateurs de modifier des agents d'intelligence artificielle personnalisés. Cette fonctionnalité est actuellement en version bêta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }