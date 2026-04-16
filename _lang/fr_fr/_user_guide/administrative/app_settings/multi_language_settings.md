---
nav_title: Paramètres de localisation
article_title: Paramètres de localisation
alias: "/multi_language_support/"
page_order: 5.5
description: "Cet article donne un aperçu des paramètres multilingues du tableau de bord de Braze et explique comment utiliser les paramètres régionaux dans vos messages."
---

# Paramètres de localisation

> La fonctionnalité multilingue vous permet d'utiliser des [étiquettes de traduction]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) pour cibler des utilisateurs de différentes langues et provenant de différents emplacements, le tout dans un seul message.

## Conditions préalables

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## Ajouter un paramètre régional

1. Accédez à **Paramètres** > **Paramètres de localisation**.
2. Sélectionnez **Ajouter des paramètres régionaux**, puis sélectionnez **Paramètres régionaux par défaut** ou **Attributs personnalisés**.

![La liste déroulante « Ajouter des paramètres régionaux » avec des options pour sélectionner les paramètres régionaux par défaut ou des attributs personnalisés.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}

{: start="3"}
3. Saisissez un nom pour le paramètre régional.
4. [Sélectionnez une langue pour l'accessibilité]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/#language-settings-and-accessibility). Ce paramètre permet aux technologies d'assistance, comme les lecteurs d'écran, de prononcer correctement le texte.
5. Sélectionnez les attributs utilisateur correspondant à l'option de paramètre régional que vous avez choisie. Lors de la configuration d'un paramètre régional, vous pouvez sélectionner des langues à partir des attributs utilisateur par défaut ou des attributs personnalisés. Vous ne pouvez pas choisir depuis les deux sources.

{% tabs %}
{% tab Default locale %}

Pour les **Paramètres régionaux par défaut**, utilisez les menus déroulants pour sélectionner la langue à ajouter et, éventuellement, le pays à associer à la langue.

![Une fenêtre intitulée « Ajouter une locale - Langue et pays par défaut » pour définir la langue et le pays.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

Pour les **Attributs personnalisés**, utilisez le menu déroulant pour sélectionner l'attribut personnalisé associé et, dans le champ de texte, saisissez la valeur.

![Une fenêtre intitulée « Ajouter une locale - Attributs personnalisés » permettant de spécifier l'attribut personnalisé et sa valeur.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Sélectionnez **Ajouter des paramètres régionaux**.

Pour connaître les étapes d'utilisation de ces paramètres régionaux dans vos messages, consultez la section [Messages multilingues]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

## Considérations

- Vous pouvez sélectionner jusqu'à deux attributs personnalisés pour un même paramètre régional, ou jusqu'à deux langues d'attribut utilisateur par défaut. Dans les deux cas, le deuxième attribut est facultatif.
- Lorsque vous modifiez les valeurs traduites dans le fichier CSV, évitez de modifier les valeurs par défaut du fichier.
- La clé de paramètre régional de votre fichier importé doit correspondre à celle de vos paramètres multilingues.

### Assistance et hiérarchisation

- Si un utilisateur correspond à la fois à un paramètre régional défini par des attributs personnalisés et à un paramètre régional défini par des attributs utilisateur par défaut, le paramètre régional basé sur les attributs personnalisés est prioritaire.
- Les attributs personnalisés prennent en charge les valeurs textuelles (chaînes de caractères) avec une correspondance exacte.
- Si un attribut personnalisé est supprimé ou si son type est modifié, l'utilisateur ne peut plus appartenir à ce paramètre régional et descendra dans la liste prioritaire des paramètres régionaux dont il relève, ou recevra les traductions marketing par défaut.
- Si un paramètre régional n'est pas valide (l'attribut personnalisé a changé ou a été supprimé), l'erreur apparaîtra sur la page **Assistance multilingue**.

## Foire aux questions

#### Combien de paramètres régionaux puis-je ajouter ?

Vous pouvez ajouter jusqu'à 200 paramètres régionaux.

#### Où sont stockés les fichiers de traduction dans Braze ?

Les fichiers de traduction sont stockés au niveau de la campagne, ce qui signifie que des traductions doivent être importées pour chaque variante de message. Les traductions peuvent également être stockées dans des blocs de contenu. Lorsqu'un bloc est ajouté à un message, ses traductions sont automatiquement incluses.

#### Le nom du paramètre régional doit-il suivre un modèle ou un format spécifique ?

Non. Vous pouvez utiliser la convention de nommage de votre choix. Le nom du paramètre régional est utilisé lors de la sélection du paramètre régional dans l'éditeur et figurera dans les en-têtes du fichier que vous téléchargez avec les ID de traduction.