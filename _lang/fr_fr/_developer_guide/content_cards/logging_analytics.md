---
nav_title: Enregistrer les analyses
article_title: Enregistrer les analyses 
page_order: 1
description: "Cet article explique comment enregistrer manuellement les impressions, les clics, les fermetures et gérer le comportement au clic pour vos cartes de contenu personnalisées."
toc_headers: "h2"

---

# Enregistrer les analyses

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Analyses manquantes pour les Cartes de contenu

Si les Cartes de contenu s'affichent correctement dans votre application mais que vous ne recevez systématiquement aucune donnée analytique (destinataires uniques, impressions, clics, etc.), il s'agit probablement d'un problème d'intégration SDK.

- **Vues personnalisées de Cartes de contenu (Android, iOS, Web) :** L'interface par défaut de Braze enregistre automatiquement les impressions et les clics sur toutes les plateformes. Si vous utilisez une vue ou une implémentation personnalisée de Cartes de contenu, vous devez appeler explicitement les méthodes d'enregistrement appropriées dans votre application. Consultez [Enregistrer les analyses]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) pour votre plateforme. Pour les implémentations Web personnalisées en particulier, vérifiez que le SDK Web de Braze est chargé, consultez la console du navigateur pour détecter d'éventuelles erreurs et assurez-vous que les données des cartes sont bien reçues.
- **Initialisation du SDK et identification de l'utilisateur :** Assurez-vous que le SDK est entièrement initialisé avant d'afficher les cartes. Les événements sont silencieusement ignorés (et non mis en file d'attente) si le SDK n'est pas initialisé, s'il est en mode d'initialisation différée ou s'il est désactivé pour le RGPD. Le SDK enregistre bien les analyses pour les utilisateurs anonymes, mais les indicateurs du tableau de bord comme « destinataires uniques » nécessitent une identité utilisateur résolue. Appelez donc `changeUser` avant l'affichage des cartes dans la mesure du possible.