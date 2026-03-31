{% if include.section == "Plan-specific features" %}

## Fonctionnalités d'intelligence artificielle spécifiques au plan

Le tableau suivant décrit les différences entre la version gratuite et la version pro des types de recommandation Personnalisé par l'IA, Plus populaire, Plus récent et Tendance :

| Domaine                   | Version gratuite                          | Version Pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Fréquence de mise à jour utilisateur<sup>1</sup>   | Hebdomadaire                                | Quotidienne                                    |
| Fréquence de réentraînement du modèle  | Mensuelle                               | Hebdomadaire                                   |
| Nombre maximum de modèles de recommandation | 1 modèle par type<sup>2</sup> | 100 modèles par type<sup>2</sup> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<sup>1. Il s'agit de la fréquence à laquelle les recommandations d'articles spécifiques à l'utilisateur sont mises à jour (Personnalisé par l'IA et Plus récent uniquement). Plus populaire et Tendance sont des recommandations globales qui se mettent à jour lors du réentraînement du modèle. Par exemple, si un utilisateur achète un article recommandé sur la base de recommandations d'articles par l'IA, ses articles recommandés seront mis à jour selon cette fréquence.</sup><br>
<sup>2. Les types de recommandation disponibles sont : Personnalisé par l'IA, Plus récent, Plus populaire et Tendance.</sup>

{% endif %}