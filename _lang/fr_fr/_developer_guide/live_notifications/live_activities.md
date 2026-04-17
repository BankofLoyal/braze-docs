---
nav_title: Activités en direct pour Swift
article_title: Activités en direct pour le SDK Swift de Braze
page_order: 0.2
description: "Découvrez comment configurer les activités en direct pour le SDK Swift de Braze."
platform: 
  - Swift
---

# Activités en direct pour Swift

> Découvrez comment implémenter les activités en direct pour le SDK Swift de Braze. Les activités en direct sont des notifications persistantes et interactives qui s'affichent directement sur l'écran de verrouillage, permettant aux utilisateurs d'obtenir des mises à jour dynamiques en temps réel&#8212;sans déverrouiller leur appareil.

## Fonctionnement

![Un suivi de livraison d'activité en direct sur l'écran de verrouillage d'un iPhone. Une barre d'état avec une voiture est presque à moitié remplie. Le texte indique « 2 min avant le ramassage ».]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

Les activités en direct présentent une combinaison d'informations statiques et dynamiques que vous mettez à jour. Par exemple, vous pouvez créer une activité en direct qui fournit un suivi de statut pour une livraison. Cette activité en direct comporterait le nom de votre entreprise comme information statique, ainsi qu'un « délai de livraison » dynamique qui serait mis à jour à mesure que le livreur approche de sa destination.

En tant que développeur, vous pouvez utiliser Braze pour gérer les cycles de vie de vos activités en direct, effectuer des appels à l'API REST de Braze pour mettre à jour les activités en direct, et faire en sorte que tous les appareils abonnés reçoivent la mise à jour dès que possible. De plus, comme vous gérez les activités en direct via Braze, vous pouvez les utiliser en tandem avec vos autres canaux de communication&mdash;notifications push, messages in-app, cartes de contenu&mdash;pour favoriser l'adoption.

## Diagramme de séquence {#sequence-diagram}

{% tabs %}
{% tab Live Activities Sequence Diagram %}
{% details Afficher le diagramme %}
```mermaid
---
config:
  theme: mc
---
sequenceDiagram
  participant Server as Client Server
  participant Device as User Device
  participant App as iOS App / Braze SDK
  participant BrazeAPI as Braze API
  participant APNS as Apple Push Notification Service
  Note over Server, APNS: Launch Option 1<br/>Locally Start Activities
  App ->> App: Register a Live Activity using <br>`launchActivity(pushTokenTag:activity:)`
  App ->> App: Get push token from iOS
  App ->> BrazeAPI: Activity ID & Push token<br>automatically sent to Braze
  Note over Server, APNS: Launch Option 2<br/>Remotely Start Activities
  Device ->> App: Call `registerPushToStart`<br>to collect push tokens early
  App ->> BrazeAPI: Push-to-start tokens sent to Braze
  Server ->> BrazeAPI: POST /messages/live_activity/start
  Note right of BrazeAPI: Payload includes:<br>- push_token<br>- activity_id<br>- external_id<br>- event_name<br>- content_state (optional)
  BrazeAPI ->> APNS: Live activity start request
  APNS ->> Device: APNS sends activity to device
  App ->> App: Get push token from iOS
  App ->> BrazeAPI: Activity ID & Push token<br>automatically sent to Braze
  Note over Server, APNS: Resuming activities upon app launch
  App ->> App: Call `resumeActivities(ofType:)` on each app launch
  Note over Server, APNS: Updating a Live Activity
  loop update a live activity
  Server ->> BrazeAPI: POST /messages/live_activity/update
  Note right of BrazeAPI: Payload includes changes<br>to ContentState (dynamic variables)
  BrazeAPI ->> APNS: Update sent to APNS
  APNS ->> Device: APNS sends update to device
  end
  Note over Server, APNS: Ending a Live Activity
  Server ->> BrazeAPI: POST /messages/live_activity/update
  Note right of BrazeAPI: Activity can be ended via:<br> - User manually dismisses<br>- Times out after 12 hours<br>- Setting `end_activity: true` on `/messages/live_activity/update`
  APNS ->> Device: Live activity is dismissed
```
{% enddetails %}
{% endtab %}
{% endtabs %}

## Implémenter une activité en direct

#{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également remplir les conditions suivantes :

- Assurez-vous que votre projet cible iOS 16.1 ou une version ultérieure.
- Ajoutez le droit `Push Notification` sous **Signing & Capabilities** dans votre projet Xcode.
- Assurez-vous que les clés `.p8` sont utilisées pour envoyer des notifications. Les fichiers plus anciens tels que `.p12` ou `.pem` ne sont pas pris en charge.
- À partir de la version 8.2.0 du SDK Swift de Braze, vous pouvez [enregistrer à distance une activité en direct](#swift_step-2-start-the-activity). Pour utiliser cette fonctionnalité, iOS 17.2 ou une version ultérieure est requis.

{% alert note %}
Bien que les activités en direct et les notifications push soient similaires, leurs autorisations système sont distinctes. Par défaut, toutes les fonctionnalités des activités en direct sont activées, mais les utilisateurs peuvent désactiver cette fonctionnalité par application.
{% endalert %}

{% sdk_min_versions swift:5.11.0 %}

### Étape 1 : Créer une activité {#create-an-activity}

Tout d'abord, assurez-vous d'avoir suivi [Afficher des données en direct avec les activités en direct](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) dans la documentation d'Apple pour configurer les activités en direct dans votre application iOS. Dans le cadre de cette tâche, assurez-vous d'inclure `NSSupportsLiveActivities` défini sur `YES` dans votre `Info.plist`.

Comme la nature exacte de votre activité en direct sera spécifique à votre cas d'usage, vous devrez configurer et initialiser les objets [Activity](https://developer.apple.com/documentation/activitykit/activityattributes). Vous définirez notamment :
* `ActivityAttributes` : Ce protocole définit le contenu statique (immuable) et dynamique (variable) qui apparaîtra dans votre activité en direct.
* `ActivityAttributes.ContentState` : Ce type définit les données dynamiques qui seront mises à jour au cours de l'activité.

Vous utiliserez également SwiftUI pour créer la présentation de l'interface utilisateur sur l'écran de verrouillage et Dynamic Island sur les appareils pris en charge.

Assurez-vous de bien connaître les [conditions préalables et les limites](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints) d'Apple pour les activités en direct, car ces contraintes sont indépendantes de Braze.

{% alert note %}
Si vous prévoyez d'envoyer des notifications push fréquentes vers la même activité en direct, vous pouvez éviter d'être limité par le budget d'Apple en définissant `NSSupportsLiveActivitiesFrequentUpdates` sur `YES` dans votre fichier `Info.plist`. Pour plus de détails, reportez-vous à la section [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) dans la documentation ActivityKit.
{% endalert %}

#### Exemple

Imaginons que nous voulions créer une activité en direct pour donner à nos utilisateurs des mises à jour sur le spectacle Superb Owl, où deux équipes concurrentes de sauvetage d'animaux sauvages reçoivent des points pour les hiboux dont ils s'occupent. Dans cet exemple, nous avons créé une structure appelée `SportsActivityAttributes`, mais vous pouvez utiliser votre propre implémentation d'`ActivityAttributes`.

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

### Étape 2 : Démarrer l'activité {#start-the-activity}

Tout d'abord, choisissez le mode d'enregistrement de votre activité :

- **À distance :** Utilisez la méthode [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) au début du cycle de vie de l'utilisateur et avant que le jeton push-to-start ne soit nécessaire, puis démarrez une activité à l'aide de l'endpoint [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
- **Localement :** Créez une instance de votre activité en direct, puis utilisez la méthode [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) pour créer des jetons de notification push que Braze pourra gérer.

{% tabs local %}
{% tab remote %}
{% alert important %}
Pour enregistrer à distance une activité en direct, iOS 17.2 ou une version ultérieure est requis.
{% endalert %}

#### Étape 2.1 : Ajouter BrazeKit à votre extension de widget

Dans votre projet Xcode, sélectionnez le nom de votre application, puis **General**. Sous **Frameworks and Libraries**, vérifiez que `BrazeKit` est inclus dans la liste.

![Le framework BrazeKit sous Frameworks and Libraries dans un exemple de projet Xcode.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### Étape 2.2 : Ajouter le protocole BrazeLiveActivityAttributes {#brazeActivityAttributes}

Dans votre implémentation d'`ActivityAttributes`, ajoutez la conformité au protocole `BrazeLiveActivityAttributes`, puis ajoutez la propriété `brazeActivityId` à votre modèle d'attributs.

{% alert important %}
iOS associera la propriété `brazeActivityId` au champ correspondant dans votre PAYLOAD push-to-start de l'activité en direct. Elle ne doit donc pas être renommée ni se voir attribuer une autre valeur.
{% endalert %}

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
// 1. Add the `BrazeLiveActivityAttributes` conformance to your `ActivityAttributes` struct.
struct SportsActivityAttributes: ActivityAttributes, BrazeLiveActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String

  // 2. Add the `String?` property to represent the activity ID.
  var brazeActivityId: String?
}
```

#### Étape 2.3 : S'inscrire au push-to-start

Ensuite, enregistrez le type d'activité en direct afin que Braze puisse suivre tous les jetons push-to-start et les instances d'activité en direct associés à ce type.

{% alert warning %}
Le système d'exploitation iOS ne génère des jetons push-to-start que lors de la première installation de l'application après le redémarrage d'un appareil. Pour vous assurer que vos jetons sont enregistrés de manière fiable, appelez `registerPushToStart` dans votre méthode `didFinishLaunchingWithOptions`.
{% endalert %}

###### Exemple

Dans l'exemple suivant, la classe `LiveActivityManager` gère des objets d'activité en direct. Ensuite, la méthode `registerPushToStart` enregistre `SportsActivityAttributes` :

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {

  @available(iOS 17.2, *)
  func registerActivityType() {
    // This method returns a Swift background task.
    // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
    let pushToStartObserver: Task = Self.braze?.liveActivities.registerPushToStart(
      forType: Activity<SportsActivityAttributes>.self,
      name: "SportsActivityAttributes"
    )
  }

}
```

#### Étape 2.4 : Envoyer une notification push-to-start

Envoyez une notification push-to-start à distance à l'aide de l'endpoint [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
{% endtab %}

{% tab local %}
Vous pouvez utiliser le [framework ActivityKit d'Apple](https://developer.apple.com/documentation/activitykit) pour obtenir un jeton de notification push que le SDK Braze peut gérer pour vous. Cela vous permet de mettre à jour les activités en direct via l'API Braze, car Braze enverra le jeton de notification push au service de notification push d'Apple (APNs) côté serveur.

1. Créez une instance de votre implémentation d'activité en direct à l'aide des API ActivityKit d'Apple.
2. Définissez le paramètre `pushType` sur `.token`.
3. Transmettez les `ActivitiesAttributes` et le `ContentState` des activités en direct que vous avez définis.
4. Enregistrez votre activité auprès de votre instance Braze en la passant dans [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class). Le paramètre `pushTokenTag` est une chaîne de caractères personnalisée que vous définissez. Elle doit être unique pour chaque activité en direct que vous créez.

Une fois l'activité en direct enregistrée, le SDK Braze extrait et observe les changements dans les jetons de notification push.

#### Exemple

Pour notre exemple, nous allons créer une classe appelée `LiveActivityManager` qui servira d'interface pour nos objets d'activité en direct. Ensuite, nous définirons le `pushTokenTag` sur `"sports-game-2024-03-15"`.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {
  
  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = SportsActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = SportsActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag.
      // This method returns a Swift background task.
      // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
      let liveActivityObserver: Task = AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "sports-game-2024-03-15",
                                                                                        activity: activity)
    }
  }
  
}
```

Votre widget d'activité en direct affichera ce contenu initial à vos utilisateurs.

![Une activité en direct sur l'écran de verrouillage d'un iPhone avec les scores de deux équipes. Les équipes Wild Bird Fund et Owl Rehab ont toutes deux un score de 0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### Étape 3 : Reprendre le suivi de l'activité {#resume-activity-tracking}

Pour que Braze suive votre activité en direct dès le lancement de l'application :

1. Ouvrez votre fichier `AppDelegate`.
2. Importez le module `ActivityKit` s'il est disponible.
3. Appelez [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) dans `application(_:didFinishLaunchingWithOptions:)` pour tous les types d'`ActivityAttributes` que vous avez enregistrés dans votre application.

Cela permet à Braze de reprendre les tâches de suivi des mises à jour des jetons de notification push pour toutes les activités en direct actives. Notez que si un utilisateur a explicitement fermé l'activité en direct sur son appareil, elle est considérée comme supprimée et Braze ne la suivra plus.

###### Exemple

```swift
import UIKit
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    
    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<SportsActivityAttributes>.self
      )
    }

    return true
  }
}
```

### Étape 4 : Mettre à jour l'activité {#update-the-activity}

![Une activité en direct sur l'écran de verrouillage d'un iPhone avec les scores de deux équipes. Le Wild Bird Fund a 2 points et l'Owl Rehab en a 4.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

L'endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) vous permet de mettre à jour une activité en direct via des notifications push transmises par l'API REST de Braze. Utilisez cet endpoint pour mettre à jour le `ContentState` de votre activité en direct.

Lorsque vous mettez à jour votre `ContentState`, votre widget d'activité en direct affiche les nouvelles informations. Voici à quoi pourrait ressembler le spectacle Superb Owl à la fin de la première mi-temps.

Pour plus de détails, consultez notre article sur l'endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

### Étape 5 : Terminer l'activité {#end-the-activity}

Lorsqu'une activité en direct est active, elle s'affiche à la fois sur l'écran de verrouillage de l'utilisateur et sur Dynamic Island. Pour la terminer via Braze, utilisez l'endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) avec `end_activity` défini sur `true`.

Pour améliorer la fiabilité lors de la fin d'une activité en direct, suivez ces étapes facultatives :

1. Incluez éventuellement `dismissal_date` dans la même requête `update` pour indiquer à iOS quand supprimer l'interface de l'activité en direct.
2. Vérifiez les résultats de distribution dans le [journal des activités liées aux messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

#### Planifier la fermeture automatique

Pour planifier une fermeture automatique, programmez une requête de suivi vers l'endpoint de mise à jour après avoir démarré l'activité en direct.

1. Envoyez une requête `/messages/live_activity/start` avec un `activity_id` que vous pouvez suivre.
2. Stockez cet `activity_id` et votre heure de fin cible dans votre planificateur backend.
3. À l'heure de fin cible, envoyez une requête `/messages/live_activity/update` avec `end_activity` défini sur `true`.
4. Configurez la date de fermeture dans la même requête de mise à jour. Pour plus de détails, consultez l'endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

Notez que le moment de la fermeture est contrôlé par iOS. Même après l'envoi d'une requête de fin valide, la suppression de l'écran de verrouillage ou de Dynamic Island peut être retardée ou se comporter différemment selon les conditions du système d'exploitation.

Une activité en direct peut également se terminer en dehors de Braze :

* **Fermeture par l'utilisateur** : Un utilisateur peut fermer manuellement une activité en direct.
* **Expiration** : Après une durée par défaut de 8 heures, iOS supprimera l'activité en direct de Dynamic Island. Après une durée par défaut de 12 heures, iOS supprimera l'activité en direct de l'écran de verrouillage.

Pour plus de détails, consultez notre article sur l'endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

## Suivi des activités en direct

Les événements d'activité en direct sont disponibles dans Currents, Snowflake Data Sharing et le générateur de requêtes. Les événements suivants peuvent vous aider à comprendre et à surveiller le cycle de vie de vos activités en direct, à suivre la disponibilité des jetons et à diagnostiquer de manière indépendante les problèmes ou à vérifier les statuts de distribution.

- [Modification du jeton push-to-start de l'activité en direct]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/#live-activity-push-to-start-token-change-events) : Enregistre lorsqu'un jeton push-to-start (PTS) est ajouté ou mis à jour dans Braze, vous permettant de suivre les enregistrements et la disponibilité des jetons par utilisateur.
- [Modification du jeton de mise à jour de l'activité en direct]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/#live-activity-update-token-change-events) : Suit l'ajout, la mise à jour ou la suppression des jetons Live Activity Update (LAU).
- [Envoi d'activité en direct]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#live-activity-send-events) : Enregistre chaque fois qu'une activité en direct est démarrée, mise à jour ou terminée par Braze.
- [Résultat de l'activité en direct]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#live-activity-outcome-events) : Indique l'état final de la distribution au service de notification push d'Apple (APNs) pour chaque activité en direct envoyée depuis Braze.

## Foire aux questions (FAQ) {#faq}

### Fonctionnalité et support

#### Quelles plateformes prennent en charge les activités en direct ?

Actuellement, les activités en direct sont une fonctionnalité spécifique à iOS et iPadOS. Par défaut, les activités lancées sur un iPhone ou un iPad seront également affichées sur tout appareil watchOS 11+ ou macOS 26+ appairé.

![Capture d'écran d'une barre de menus macOS affichant une activité en direct sous forme d'alerte.]({% image_buster /assets/img/live-activity-macos.png %}){: style="max-width:60%;"}

L'article sur les activités en direct couvre les [conditions préalables]({{site.baseurl}}/developer_guide/platforms/swift/live_activities/#prerequisites) à la gestion des activités en direct via le SDK Swift de Braze.

#### Les applications React Native prennent-elles en charge les activités en direct ?

Oui, le SDK React Native 3.0.0+ prend en charge les activités en direct via le SDK Swift de Braze. Autrement dit, vous devez écrire du code iOS React Native directement au-dessus du SDK Swift de Braze.

Il n'existe pas d'API JavaScript spécifique à React Native pour les activités en direct, car les fonctionnalités des activités en direct fournies par Apple utilisent des langages non transposables en JavaScript (par exemple, la concurrence Swift, les génériques, SwiftUI).

#### Braze prend-il en charge les activités en direct en tant que campagne ou étape du canvas ?

Non, cela n'est pas pris en charge actuellement.

### Notifications push et activités en direct

#### Que se passe-t-il si une notification push est envoyée alors qu'une activité en direct est active ?

![Écran de téléphone avec une activité sportive en direct « Bulls vs Bears » vers le milieu de l'écran et un texte de notification push lorem ipsum en bas de l'écran.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Les activités en direct et les notifications push occupent des zones d'écran différentes et n'entrent pas en conflit sur l'écran de l'utilisateur.

#### Si les activités en direct exploitent la fonctionnalité de notification push, les notifications push doivent-elles être activées pour recevoir les activités en direct ?

Bien que les activités en direct reposent sur les notifications push pour les mises à jour, elles sont contrôlées par des paramètres utilisateur différents. Un utilisateur peut s'abonner aux activités en direct mais pas aux notifications push, et inversement.

Les jetons de mise à jour de l'activité en direct expirent au bout de huit heures.

#### Les activités en direct nécessitent-elles des amorces de notification push ?

Les [amorces de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) constituent une bonne pratique pour inviter vos utilisateurs à s'abonner aux notifications push de votre application. Cependant, il n'y a pas d'invite système pour s'abonner aux activités en direct. Par défaut, les utilisateurs sont abonnés aux activités en direct pour une application individuelle lorsqu'ils installent cette application sur iOS 16.1 ou une version ultérieure. Cette autorisation peut être désactivée ou réactivée dans les paramètres de l'appareil, application par application.

### Sujets techniques et résolution des problèmes

#### Comment savoir si les activités en direct comportent des erreurs ?

Toute erreur d'activité en direct sera consignée dans le tableau de bord de Braze dans le [journal des activités liées aux messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), où vous pouvez filtrer par « LiveActivity Errors ».

#### Après avoir envoyé une notification push-to-start, pourquoi n'ai-je pas reçu mon activité en direct ?

Tout d'abord, vérifiez que votre PAYLOAD comprend tous les champs obligatoires décrits dans l'endpoint [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start). Les champs `activity_attributes` et `content_state` doivent correspondre aux propriétés définies dans le code de votre projet. Si vous êtes certain que le PAYLOAD est correct, il est possible que votre débit soit limité par les APNs. Cette limite est imposée par Apple et non par Braze.

Pour vérifier que votre notification push-to-start est bien arrivée sur l'appareil mais n'a pas été affichée en raison des limites de débit, vous pouvez déboguer votre projet à l'aide de l'application Console sur votre Mac. Attachez le processus d'enregistrement pour l'appareil souhaité, puis filtrez les journaux par `process:liveactivitiesd` dans la barre de recherche.

#### Après avoir démarré mon activité en direct avec push-to-start, pourquoi ne reçoit-elle pas de nouvelles mises à jour ?

Vérifiez que vous avez correctement implémenté les instructions décrites [ci-dessus](#swift_brazeActivityAttributes). Votre `ActivityAttributes` doit contenir à la fois la conformité au protocole `BrazeLiveActivityAttributes` et la propriété `brazeActivityId`.

Après avoir reçu une notification push-to-start d'activité en direct, vérifiez que vous pouvez voir une requête réseau sortante vers l'endpoint `/push_token_tag` de votre URL Braze et qu'elle contient le bon ID d'activité dans le champ `"tag"`.

Enfin, assurez-vous que le type d'attribut d'activité en direct dans votre PAYLOAD de mise à jour correspond exactement à la chaîne de caractères et à la classe utilisées dans votre appel de méthode SDK vers `registerPushToStart`. Utilisez des constantes pour éviter les erreurs de frappe.

#### Je reçois une réponse « Accès refusé » lorsque j'essaie d'utiliser l'endpoint `live_activity/update`. Pourquoi ?

Les clés API que vous utilisez doivent disposer des autorisations appropriées pour accéder aux différents endpoints de l'API Braze. Si vous utilisez une clé API que vous avez précédemment créée, il est possible que vous ayez omis de mettre à jour ses autorisations. Consultez notre [aperçu de la sécurité des clés API]({{site.baseurl}}/api/basics/#rest-api-key-security) pour en savoir plus.

#### L'endpoint `messages/send` partage-t-il les limites de débit avec l'endpoint `messages/live_activity/update` ?

Par défaut, la limite de débit pour l'endpoint `messages/live_activity/update` est de 250 000 requêtes par heure, par espace de travail et sur plusieurs endpoints. Pour plus d'informations, consultez les [limites de débit de l'API]({{site.baseurl}}/api/api_limits/).