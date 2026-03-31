---
nav_title: Messages multilingues
article_title: Messages multilingues
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Cet article fournit des instructions sur la manière d'utiliser les paramètres régionaux dans vos messages."
---

# Messages multilingues

> Après avoir ajouté des paramètres régionaux à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues à l'aide d'une seule notification push, d'un e-mail, d'une bannière, d'un message in-app ou d'un bloc de contenu.

## Conditions préalables

{% tabs %}
{% tab Paramètres régionaux multilingues %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Types de messages %}

| Fonctionnalité | Autorisations utilisateur requises |
| --- | --- |
| Types&nbsp;de&nbsp;messages | Vous avez besoin de ces autorisations pour ajouter des paramètres régionaux et des traductions aux campagnes et aux Canvas :<br><br> {::nomarkdown}Autorisations granulaires : <ul><li>Modifier les campagnes</li><li>Modifier les Canvas</li></ul> Autorisations héritées : <ul><li>Accéder aux campagnes, Canvas, cartes, blocs de contenu, indicateurs de fonctionnalité, segments, bibliothèque multimédia, emplacements, codes de promotion et centres de préférences</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modèles %}

| Fonctionnalité | Autorisations utilisateur requises |
| --- | --- |
| Modèles | Vous avez besoin de ces autorisations pour le type de modèle auquel vous souhaitez ajouter des paramètres régionaux et des traductions :<br><br> {::nomarkdown}Autorisations granulaires : <ul><li>Modifier les modèles d'e-mail</li><li>Modifier les modèles de messages in-app</li><li>Modifier les modèles de blocs de contenu</li></ul> Autorisations héritées : <ul><li>Accéder aux campagnes, Canvas, cartes, blocs de contenu, indicateurs de fonctionnalité, segments, bibliothèque multimédia, emplacements, codes de promotion et centres de préférences</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Utilisation des paramètres régionaux

### Étape 1 : Configurer les paramètres régionaux

Avant de pouvoir ajouter des traductions à un message, vous devez d'abord [créer les paramètres régionaux que vous souhaitez prendre en charge]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/). Les paramètres régionaux définissent les variantes de langue (et éventuellement de région) disponibles pour l'envoi de messages.

### Étape 2 : Identifier le contenu à traduire

Encadrez le texte que vous souhaitez traduire avec les étiquettes Liquid de traduction {% raw %}`{% translation your_id_here %}` et `{% endtranslation %}`{% endraw %} et attribuez un ID d'étiquette. Les ID des étiquettes de traduction doivent être uniques au sein d'un message. Pensez à utiliser des noms d'ID sémantiques qui décrivent clairement le texte, comme {% raw %}`{% translation header %}`{% endraw %}.

Voici un exemple de message identifié pour la traduction : {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Sélectionnez le texte que vous souhaitez traduire et utilisez le raccourci clavier **Cmd + Alt + L** (macOS) ou **Ctrl + Alt + L** (Windows) pour l'encadrer avec des étiquettes de traduction.<br><br> Ce raccourci fonctionne dans tous les canaux prenant en charge l'envoi de messages multilingues, à l'exception des éditeurs par glisser-déposer pour les e-mails et les blocs de contenu. Pour ceux-ci, utilisez le bouton **Ajouter une personnalisation** dans la barre latérale gauche pour ajouter des étiquettes de traduction.
{% endalert %}

#### Localisation des URL

Lors de la traduction du contenu, les URL nécessitent un traitement particulier pour éviter les liens cassés.

##### URL standard (statiques)

Les URL statiques sont saisies manuellement dans l'éditeur (par exemple, `https://example.com`). Nous recommandons également ce qui suit :

| Recommandation | Raison |
| --- | --- |
| Conservez le protocole (`https://`) en dehors des étiquettes de traduction. N'encadrez que le domaine et le chemin (par exemple, `example.com/en`). | Les traducteurs pourraient accidentellement modifier ou supprimer des caractères spéciaux, ce qui casserait les liens. |
| N'incluez pas les paramètres de requête dans les étiquettes de traduction (par exemple, `?utm_source=promo`). | Les traducteurs pourraient accidentellement modifier ou supprimer des caractères spéciaux, ce qui casserait les liens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Une URL standard qui suit ces deux recommandations se présente ainsi :

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz%}{% endtranslation %}">Click Here</a>
```
{% endraw %}

{% alert important %}
Si vous utilisez le [suivi des liens e-mail](#email-link-tracking) (aliasage de lien ou modèles de liens), une configuration supplémentaire est nécessaire lorsque les URL sont encadrées par des étiquettes de traduction.
{% endalert %}

#### Attributs et structure HTML

N'encadrez que le texte lisible par l'utilisateur dans les étiquettes de traduction. Évitez d'encadrer les attributs HTML (tels que `class`, `style` ou `id`) ou tout autre code structurel. Les attributs HTML contrôlent la mise en page, le style et les fonctionnalités. Les encadrer dans des étiquettes de traduction peut casser le formatage ou les styles dans les versions localisées de votre message.

Ce texte est correctement encadré :

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Texte incorrectement encadré %}

Ce texte est **incorrectement** encadré :

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### Étape 3 : Ajouter des paramètres régionaux à votre message

Après avoir ajouté des étiquettes de traduction à votre message, sélectionnez **Gérer les langues** dans l'éditeur (**Langues** dans les éditeurs par glisser-déposer pour les e-mails et les blocs de contenu) et sélectionnez au moins un paramètre régional pour lequel vous souhaitez ajouter des traductions.

![Le menu déroulant Ajouter un paramètre régional avec des options pour sélectionner le paramètre régional par défaut ou les attributs personnalisés.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Blocs de contenu contenant des traductions

Si votre message contient des blocs de contenu qui ont déjà des traductions enregistrées, vous n'avez pas besoin de les importer à nouveau. Les traductions enregistrées sont automatiquement appliquées lorsque le bloc de contenu est ajouté à votre message.

Dans la fenêtre modale **Gérer les langues**, les blocs de contenu avec des traductions enregistrées apparaissent dans la liste, accompagnés des paramètres régionaux qu'ils prennent en charge. Cela vous permet de voir quelles parties de votre message sont déjà localisées avant d'ajouter de nouvelles traductions.

![La section Gérer les langues avec une liste de blocs de contenu ayant des traductions enregistrées.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Assurez-vous que chaque bloc de contenu inclut des traductions pour chaque paramètre régional ajouté à votre message. Si un bloc de contenu ne dispose pas de traductions pour l'un des paramètres régionaux que vous avez ajoutés, il s'affichera dans sa langue d'origine pour les utilisateurs de ce paramètre régional.
{% endalert %}

### Étape 4 : Ajouter les traductions

Après avoir sélectionné les paramètres régionaux, ajoutez les traductions à votre message en utilisant l'une des méthodes suivantes :

![L'onglet Ajouter des traductions avec des options pour importer les traductions par CSV ou en se connectant à des partenaires de traduction.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Importer un modèle CSV %}

Sélectionnez **Télécharger le modèle** pour télécharger un fichier CSV contenant une matrice de vos ID de traduction et paramètres régionaux sélectionnés. Saisissez les traductions pour chaque paramètre régional. Importez le fichier complété et les traductions seront appliquées à votre message.

{% alert important %}
Pour éviter les problèmes d'affichage avec les caractères non anglais, n'utilisez pas Excel pour votre fichier CSV de traduction.
{% endalert %}

![CSV avec des étiquettes de traduction pour un titre, un texte d'offre, un montant d'offre et un CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Utiliser l'API de traduction %}

Utilisez l'API de traduction d'un partenaire pour gérer et mettre à jour les traductions dans vos campagnes et Canvas. C'est utile si vous utilisez un système externe pour la localisation ou si vous souhaitez vous connecter directement à un partenaire de traduction.

Pour utiliser les endpoints de traduction avec les Canvas, incluez les paramètres suivants :
  - `workflow_id`
  - `step_id`
  - `message_variation_id` 

{% alert note %}
Lorsque vous utilisez l'API de traduction avec des étapes du canvas créées après le lancement du canvas, le `message_variation_id` que vous transmettez à l'API sera vide ou vierge.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Prévisualiser les traductions

Pour prévisualiser votre message, sélectionnez l'option **Utilisateur multilingue** dans le menu déroulant **Prévisualiser en tant qu'utilisateur**. Vous pourrez ainsi basculer entre les différentes définitions de paramètres régionaux pour prévisualiser toutes les traductions de votre message.

![Aperçus des paramètres régionaux]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Gestion des traductions

### Duplication des étapes du canvas ou des campagnes, et traductions

Lorsque vous dupliquez une étape du canvas, une campagne ou une variante, les traductions sont incluses. Cela vaut également lors de la copie entre espaces de travail, à condition que les paramètres régionaux soient définis dans l'espace de travail de destination. Pensez à vérifier et à mettre à jour les traductions en conséquence lorsque vous apportez des modifications à votre canvas ou à votre campagne.

### Enregistrement des traductions dans les blocs de contenu

Les blocs de contenu prennent en charge le multilingue de la même manière que les messages. Lors de la création ou de la modification de blocs de contenu, vous pouvez identifier le contenu à traduire, ajouter des paramètres régionaux et importer des traductions à l'aide d'un CSV ou de l'[API de traduction]({{site.baseurl}}/api/endpoints/translations/).

Les traductions enregistrées restent associées au bloc de contenu. Lorsque le bloc est ajouté à un message, ses traductions sont automatiquement incluses.

### Messages de droite à gauche

Lorsque vous remplissez le fichier de traduction pour les langues qui s'écrivent de droite à gauche (comme l'arabe), encadrez la traduction avec `span` afin qu'elle soit correctement formatée :

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Suivi des liens e-mail

Dans les campagnes e-mail, Braze suit les liens en ajoutant des informations de suivi (paramètres de requête) à chaque URL. Ce comportement prend en charge à la fois l'[aliasage de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) et les [modèles de liens]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template).

Lorsqu'une URL est encadrée par des étiquettes de traduction, Braze peut ne pas être en mesure de déterminer où ajouter ces informations de suivi. Pour garantir le bon fonctionnement, vous devez inclure un caractère spécial à la fin de l'URL pour indiquer où le suivi doit être ajouté.

Les URL utilisent deux caractères spéciaux pour contrôler ce fonctionnement :
  - `?` ajoute le suivi à une URL qui n'en possède pas encore.
  - `&` ajoute un suivi supplémentaire si un `?` est déjà présent dans l'URL. Une URL ne peut contenir qu'un seul `?`.

| URL | Contient&nbsp;`?` | Description | Exemple |
| --- | --- | --- | --- |
| URL standard | Non | Ajoutez `?` après l'étiquette de traduction fermante si l'URL n'en contient pas déjà un. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL standard | Oui | Utilisez `&` à la fin de l'URL (après l'étiquette de traduction fermante) si elle contient déjà `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Générée par Liquid | Non | Utilisez `?` après les étiquettes de traduction fermantes si l'URL générée n'en contient pas déjà un. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Générée par Liquid | Oui | Utilisez `&` après l'étiquette de traduction fermante si l'URL générée contient déjà un `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Paramètres de langue et accessibilité

Pour les canaux basés sur HTML (e-mail, message in-app, bannières, pages d'accueil et cartes de contenu), Braze ajoute un attribut de langue d'accessibilité (`lang`) au message rendu. Cet attribut aide les technologies d'assistance comme les lecteurs d'écran à interpréter et prononcer correctement le texte.

Sans cet attribut, un lecteur d'écran suppose que le contenu est dans la langue par défaut définie par l'utilisateur sur son appareil lors de la configuration. Si le message est dans une autre langue, le lecteur d'écran risque de ne pas tout prononcer correctement.

#### Configuration de la langue d'accessibilité

Vous pouvez définir la langue d'accessibilité à deux niveaux :

##### Au niveau du message

Dans les paramètres de votre message, accédez à la section **Accessibilité** et sélectionnez une langue dans le menu déroulant ou utilisez Liquid pour définir dynamiquement la langue d'accessibilité. Cela s'applique à l'ensemble du contenu du message.

##### Au niveau du paramètre régional

Pour les messages multilingues, définissez la langue d'accessibilité sur chaque paramètre régional dans les **Paramètres de localisation**. Lors de la création de nouveaux messages, {% raw %}`{{accessibility_language}}`{% endraw %} est sélectionné par défaut dans la section **Accessibilité**. Cela associe la langue d'accessibilité à vos paramètres régionaux.

#### Normes

La langue d'accessibilité correspond à l'attribut HTML `lang`, une [exigence WCAG 2.1 de niveau A](https://dequeuniversity.com/rules/axe/4.2/html-has-lang) (critère de succès 3.1.1). Pour le contenu multilingue, vous pouvez également définir la langue sur des blocs de contenu individuels en utilisant l'attribut `lang` directement dans votre HTML.

## Foire aux questions

#### Quelles sont les limites des étiquettes de traduction ?

Lors de l'utilisation des étiquettes de traduction, les limites suivantes s'appliquent :

- Chaque message peut contenir jusqu'à 200 étiquettes de traduction.
- Chaque texte par défaut (le contenu entre les étiquettes de traduction) peut contenir jusqu'à 2 000 caractères.
- Les traductions par paramètre régional peuvent contenir jusqu'à 409 600 octets (environ 409,6&nbsp;Ko).

#### Puis-je modifier la version traduite dans l'un de mes paramètres régionaux ?

Oui. Modifiez d'abord le fichier CSV, puis importez-le à nouveau pour appliquer la modification.

### Braze fournit-il des traductions ?

Non. Vous devez [fournir vos propres traductions](#step-4-add-translations) soit en important un CSV, soit en utilisant l'API de traduction.

### Puis-je imbriquer des étiquettes de traduction ?

Non.

#### Puis-je encadrer des messages HTML complets dans une étiquette de traduction ?

Non. En bonne pratique, vous ne devez encadrer que le texte lisible par l'utilisateur ou le contenu qui doit être localisé. Cela permet d'éviter les problèmes de formatage, de liens ou d'autres éléments non textuels.

De plus, pensez à encadrer des portions de texte plus petites et sémantiquement liées pour obtenir des traductions précises et éviter les limitations de performances ou de taille.

#### Puis-je modifier la version traduite dans l'un de mes paramètres régionaux ?

Oui. Si vous utilisez un CSV, modifiez d'abord le fichier, puis importez-le à nouveau pour appliquer la modification. Si vous utilisez l'[API de traduction]({{site.baseurl}}/api/endpoints/translations/), utilisez les endpoints de mise à jour pour effectuer les modifications.

#### Quelles validations ou vérifications supplémentaires Braze effectue-t-il ?

| Scénario | Validation dans Braze |
| --- | --- |
| Un message contient deux ou plusieurs ID de traduction identiques associés à des textes différents. | Ce fichier de traduction ne sera pas téléchargé. |
| Il manque un ou plusieurs ID d'étiquettes de traduction dans le fichier de traduction. | Ce fichier de traduction ne sera pas importé. |
| Un fichier de traduction contient des paramètres régionaux absents du message. | Ce fichier de traduction ne sera pas importé. |
| Les étiquettes de traduction doivent être ajoutées à un message avant de télécharger le modèle de traduction. | Ce fichier de traduction ne sera pas téléchargé. |
| Des étiquettes de traduction présentes dans votre fichier importé sont absentes de votre message. | Les traductions supplémentaires ne seront pas enregistrées dans le message. |
| {% raw %}Un message contient une ou plusieurs étiquettes Liquid incorrectes. Pour les étiquettes ouvrantes, utilisez `{% translation your_id_here %}`, et fermez les étiquettes de traduction avec `{% endtranslation %}`.{% endraw %} | Ce fichier de traduction ne sera pas téléchargé. |
| Un fichier de traduction contient un texte par défaut qui ne correspond pas à celui du message. | Les traductions sont ajoutées, mais le texte original du message n'est pas mis à jour. |
| Un ou plusieurs paramètres régionaux d'un message ont été supprimés dans les paramètres et n'existent plus. | Les traductions déjà ajoutées continuent d'exister dans le message. Si elles sont supprimées du message, les traductions sont perdues. |
| Les étiquettes de traduction contiennent des URL complètes ou des URL générées par Liquid. | Les étiquettes de traduction contenant des URL sont identifiées en cas de problèmes de liens cassés ou de suivi des liens. |
| Les étiquettes de traduction incluent des paramètres de requête. | Les étiquettes de traduction contenant des paramètres de requête sont identifiées en cas de problèmes de liens cassés ou de suivi des liens. |
| Les étiquettes de traduction contiennent des attributs ou des structures HTML. | Les étiquettes de traduction contenant des attributs ou des structures HTML sont identifiées en cas de problèmes de styles et de formatage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }