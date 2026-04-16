---
nav_title: Sémantique de livraison des événements
article_title: Sémantique de livraison des événements
page_order: 3
page_type: reference
description: "Cet article de référence décrit et définit la manière dont Currents gère les données d'événements en fichier plat que nous envoyons aux partenaires de stockage de l'entrepôt de données."
tool: Currents

---

# Sémantique de livraison des événements

> Cette page décrit et définit la manière dont Currents gère les données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de stockage de l'entrepôt de données.

Currents for Data Storage permet un flux continu de données de notre plateforme vers un compartiment de stockage de l'un de nos [partenaires d'entrepôt de données]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/). Currents écrit les fichiers Avro dans votre compartiment de stockage à des seuils réguliers, ce qui vous permet de traiter et d'analyser les données d'événements en utilisant vos propres outils d'aide à la décision.

{% alert important %}
Ce contenu **s'applique uniquement aux données d'événements de fichiers plats que nous envoyons aux partenaires d'entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage)**. <br><br>Pour le contenu qui s'applique aux autres partenaires, reportez-vous à notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et consultez leurs pages respectives.
{% endalert %}

## Événements de test

Lorsque vous configurez une intégration Currents, cliquez sur **Envoyer des événements test** pour vérifier la connexion avec votre compartiment de stockage. Ces événements de test permettent de vérifier que votre intégration est en mesure de recevoir et de traiter correctement les données.

{% alert important %}
**Format des données de l'événement test :** Les événements de test contiennent des valeurs de marque substitutive qui correspondent aux types de données appropriés pour chaque champ, mais ils ne contiennent pas de données réalistes ou précises. Par exemple, un champ `timezone` peut contenir une chaîne de caractères de type UUID au lieu d'un identifiant de fuseau horaire valide (tel que « America/Chicago »), et d'autres champs tels que `campaign_name` et `ip_pool` peuvent également contenir des valeurs de marque substitutive plutôt que des données réelles.<br>

Il s'agit d'un comportement normal. Les événements de test servent principalement à tester la connexion et la configuration de l'intégration, et non à valider l'exactitude des données. Pour visualiser des événements réels avec des données précises, utilisez une intégration Currents de test afin d'envoyer des données d'événements réels via votre pipeline.
{% endalert %}

## Livraison au moins une fois

En tant que système à haut débit, Currents fournit une livraison des événements « au moins une fois », ce qui signifie que des doublons d'événements peuvent parfois être écrits dans votre compartiment de stockage. Cela peut se produire lorsque des événements sont retraités à partir de notre file d'attente pour une raison ou une autre.

Si vos cas d'utilisation nécessitent une livraison « une seule fois exactement », vous pouvez utiliser le champ d'identifiant unique envoyé avec chaque événement (`id`) pour dédupliquer les événements. Étant donné que le fichier échappe à notre contrôle une fois écrit dans votre compartiment de stockage, nous n'avons aucun moyen de garantir la déduplication de notre côté.

## Horodatages

Tous les horodatages exportés par Currents sont envoyés dans le fuseau horaire UTC. Pour certains événements où il est disponible, un champ de fuseau horaire est également inclus, qui fournit le format IANA (Internet Assigned Numbers Authority) du fuseau horaire local de l'utilisateur au moment de l'événement.

### Temps de latence

Les événements envoyés à Braze par l'intermédiaire du SDK ou de l'API peuvent inclure un horodatage du passé. L'exemple le plus courant est celui des données du SDK mises en file d'attente, par exemple en l'absence de connectivité mobile. Dans ce cas, l'horodatage de l'événement reflétera le moment où l'événement a été généré. Cela signifie qu'un certain pourcentage d'événements semblera présenter une latence élevée.

## Format Apache Avro

Les intégrations de stockage de données de Braze Currents produisent des données au format `.avro`. Nous avons choisi [Apache Avro](https://avro.apache.org/) parce qu'il s'agit d'un format de données flexible qui prend nativement en charge l'évolution des schémas et qui est compatible avec une grande variété de produits de données :

- Avro est pris en charge par la grande majorité des principaux entrepôts de données.
- Si vous souhaitez conserver vos données dans S3, Avro compresse mieux que CSV et JSON, ce qui réduit vos coûts de stockage et potentiellement la consommation de CPU pour analyser les données.
- Avro nécessite des schémas lorsque les données sont écrites ou lues. Les schémas peuvent évoluer au fil du temps pour permettre l'ajout de champs sans rien casser.

Currents crée un fichier pour chaque type d'événement en utilisant le format suivant :

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Vous ne voyez pas le code à cause de la barre de défilement ? Apprenez à résoudre ce problème [ici]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/).
{% endalert %}

Par exemple, le chemin d'un événement d'envoi de notification push peut ressembler à ceci :

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

Le segment de chemin `version` est un simple entier correspondant à la version de Currents, par exemple `version=6`.

|Segment du nom de fichier |Définition|
|---|---|
| `<your-bucket-prefix>` | Le préfixe défini pour cette intégration Currents. |
| `<cluster-identifier>` | Pour usage interne par Braze. Sera une chaîne de caractères telle que « prod-01 », « prod-02 », « prod-03 » ou « prod-04 ». Tous les fichiers auront le même identifiant de cluster.|
| `<connection-type-identifier>` | L'identifiant du type de connexion. Les options sont « S3 », « AzureBlob » ou « GCS ». |
| `<integration-id>` | L'ID unique pour cette intégration Currents. |
| `<event-type>` | Le type de l'événement dans le fichier. |
| `<date>` | L'heure pendant laquelle les événements sont mis en file d'attente dans notre système pour traitement, dans le fuseau horaire UTC. Au format YYYY-MM-DD-HH. |
| `version=<currents_version>` | La version de Currents pour le chemin du pipeline. Cette valeur est un simple entier tel que `6`. |
| `<environment>` | Pour usage interne par Braze. |
| `<partition>` | Pour usage interne par Braze. Entier. |
| `<offset>`| Pour usage interne par Braze. Entier. Notez que les différents fichiers envoyés à la même heure auront un paramètre `<offset>` différent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Les conventions de nommage des fichiers peuvent être modifiées. Braze recommande de rechercher toutes les clés de votre compartiment qui ont le préfixe &lt;your-bucket-prefix&gt;.
{% endalert %}

### Seuil d'écriture Avro

Dans des circonstances normales, Braze écrit des fichiers de données dans votre compartiment de stockage toutes les 5 minutes ou tous les 15 000 événements, selon la condition remplie en premier. En cas de forte charge, nous pouvons écrire des fichiers de données plus volumineux pouvant contenir jusqu'à 100 000 événements par fichier.

{% alert important %}
Currents ne génère jamais de fichiers vides.
{% endalert %}

### Modifications du schéma Avro

De temps à autre, Braze peut apporter des modifications au schéma Avro lorsque des champs sont ajoutés, modifiés ou supprimés. Pour ce qui nous concerne ici, il existe deux types de modifications : celles qui cassent la compatibilité et celles qui ne la cassent pas. Dans tous les cas, la version du chemin Currents est incrémentée pour indiquer que le schéma a été mis à jour. Les événements Currents écrits sur Azure Blob Storage, Google Cloud Storage et Amazon S3 inscrivent cette information sous la forme `version=<currents_version>` dans le chemin. Par exemple : `<your-bucket-prefix>/.../event_type=<event-type>/date=<date>/version=6/<environment>/...`.

#### Changements non cassants

Lorsqu'un champ est ajouté au schéma Avro, nous considérons qu'il s'agit d'un changement non cassant. Les champs ajoutés seront toujours des champs Avro « facultatifs » (par exemple avec une valeur par défaut de `null`), de sorte qu'ils « correspondront » aux anciens schémas conformément à la [spécification de résolution des schémas Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Ces ajouts ne devraient pas affecter les processus ETL (extraire, transformer, charger) existants, car le champ sera simplement ignoré jusqu'à ce qu'il soit ajouté à votre processus ETL.

{% alert important %}
Nous recommandons que votre configuration ETL soit explicite sur les champs traités afin d'éviter de rompre le flux si de nouveaux champs sont ajoutés.
{% endalert %}

Même si nous faisons tout notre possible pour vous informer à l'avance de tous les changements, nous pouvons à tout moment introduire des modifications non cassantes au schéma.

#### Changements cassants

Lorsqu'un champ est retiré ou modifié dans le schéma Avro, nous considérons qu'il s'agit d'un changement cassant. Ce type de changement peut nécessiter de modifier les processus ETL existants, car les champs utilisés peuvent ne plus être enregistrés comme prévu.

Tous les changements cassants apportés au schéma seront communiqués avant leur mise en œuvre.