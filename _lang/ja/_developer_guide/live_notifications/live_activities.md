---
nav_title: Swift のライブアクティビティ
article_title: Swift Braze SDK のライブアクティビティ
page_order: 0.2
description: "Swift Braze SDK のライブアクティビティの設定方法について説明します。"
platform: 
  - Swift
---

# Swift のライブアクティビティ

> Swift Braze SDK 用にライブアクティビティを実装する方法について説明します。ライブアクティビティは、ロック画面に直接表示される永続的でインタラクティブな通知で、ユーザーはデバイスのロックを解除することなく、ダイナミックなリアルタイム更新を得ることができます。

## 仕組み

![iPhone ロック画面の配信トラッカーのライブアクティビティ。車のついたステータスバーがほぼ半分まで進んでいる。「ピックアップまであと2分」と表示されている]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

ライブアクティビティは、静的情報と更新可能な動的情報を組み合わせて表示します。たとえば、配達のステータス追跡機能を提供するライブアクティビティを作成できます。このライブアクティビティには、会社名が静的情報として含まれ、さらに配達ドライバーが目的地に近づくにつれて更新される「配達までの時間」が動的情報として含まれます。

開発者は Braze を使用して、ライブアクティビティのライフサイクルを管理し、Braze REST API を呼び出してライブアクティビティの更新を行い、サブスクライブ済みのすべてのデバイスが可能な限り早く更新を受信できるようにすることができます。また、Braze でライブアクティビティを管理しているため、プッシュ通知、アプリ内メッセージ、コンテンツカードなど、その他のメッセージングチャネルと連携させて活用を促進できます。

## シーケンス図 {#sequence-diagram}

{% tabs %}
{% tab Live Activities Sequence Diagram %}
{% details 図を表示 %}
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

## ライブアクティビティの実装

#{% multi_lang_include developer_guide/prerequisites/swift.md %} 以下の項目も完了する必要があります。

- プロジェクトが iOS 16.1 以降をターゲットにしていることを確認します。
- Xcode プロジェクトの**Signing & Capabilities** に `Push Notification` エンタイトルメントを追加します。
- 通知の送信に `.p8` キーが使用されていることを確認します。`.p12` や `.pem` などの古いファイルはサポートされていません。
- Braze Swift SDK のバージョン 8.2.0 以降では、[ライブアクティビティをリモートで登録](#swift_step-2-start-the-activity)できます。この機能を使用するには、iOS 17.2 以降が必要です。

{% alert note %}
ライブアクティビティとプッシュ通知は似ていますが、システム権限は別個のものです。デフォルトでは、すべてのライブアクティビティ機能が有効になっていますが、ユーザーはアプリごとにこの機能を無効にすることができます。
{% endalert %}

{% sdk_min_versions swift:5.11.0 %}

### ステップ 1: アクティビティを作成する {#create-an-activity}

まず、Apple のドキュメントの[ライブアクティビティでライブデータを表示する](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities)手順に従い、iOS アプリケーションにライブアクティビティをセットアップします。このタスクの一部として、`Info.plist` に `NSSupportsLiveActivities` を `YES` に設定して含めてください。

ライブアクティビティの正確な内容はビジネスケースに固有であるため、[Activity](https://developer.apple.com/documentation/activitykit/activityattributes) オブジェクトを設定して初期化する必要があります。以下を定義することが重要です。
* `ActivityAttributes`: このプロトコルは、ライブアクティビティに表示される静的（不変）コンテンツと動的（可変）コンテンツを定義します。
* `ActivityAttributes.ContentState`: この型は、アクティビティの進行に伴って更新される動的データを定義します。

また、SwiftUI を使用して、サポートされているデバイスでロック画面とダイナミックアイランドの UI 表示を作成します。 

ライブアクティビティに関する Apple の[前提条件と制限](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints)をよく理解してください。これらの制約は Braze とは独立しています。

{% alert note %}
同じライブアクティビティに頻繁にプッシュを送信する場合は、`Info.plist` ファイルで `NSSupportsLiveActivitiesFrequentUpdates` を `YES` に設定することで、Apple の予算制限によるスロットリングを回避できます。詳細については、ActivityKit ドキュメントの [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) セクションを参照してください。
{% endalert %}

#### 例

競争している2つの野生動物救助チームに、保護しているフクロウに対してポイントが与えられる Superb Owl ショーの更新をユーザーに提供するライブアクティビティを作成すると想定してみましょう。この例では、`SportsActivityAttributes` という構造体を作成しましたが、`ActivityAttributes` の独自の実装を使用することもできます。

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

### ステップ 2: アクティビティを開始する {#start-the-activity}

まず、アクティビティの登録方法を選択します。

- **リモート:** [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) メソッドをユーザーライフサイクルの早い段階で、push-to-start トークンが必要になる前に呼び出し、[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) エンドポイントを使用してアクティビティを開始します。
- **ローカル:** ライブアクティビティのインスタンスを作成し、[`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) メソッドを使用して、Braze が管理するプッシュトークンを作成します。

{% tabs local %}
{% tab remote %}
{% alert important %}
ライブアクティビティをリモートで登録するには、iOS 17.2 以降が必要です。
{% endalert %}

#### ステップ 2.1: BrazeKit をウィジェット拡張に追加する

Xcode プロジェクトで、アプリの名前を選択し、**General** を選択します。**Frameworks and Libraries** の下に `BrazeKit` がリストされていることを確認します。

![サンプル Xcode プロジェクト内の「Frameworks and Libraries」にある BrazeKit フレームワーク。]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### ステップ 2.2: BrazeLiveActivityAttributes プロトコルを追加する {#brazeActivityAttributes}

`ActivityAttributes` の実装に `BrazeLiveActivityAttributes` プロトコルへの準拠を追加し、属性モデルに `brazeActivityId` プロパティを追加します。

{% alert important %}
iOS は `brazeActivityId` プロパティをライブアクティビティの push-to-start ペイロードの対応するフィールドにマップするため、名前を変更したり、他の値を割り当てたりしないでください。
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

#### ステップ 2.3: push-to-start の登録

次にライブアクティビティのタイプを登録し、そのタイプに関連付けられたすべての push-to-start トークンとライブアクティビティインスタンスを Braze が追跡できるようにします。

{% alert warning %}
iOS オペレーティングシステムは、デバイスが再起動した後の最初のアプリインストール時にのみ push-to-start トークンを生成します。トークンが確実に登録されるようにするには、`didFinishLaunchingWithOptions` メソッドで `registerPushToStart` を呼び出してください。
{% endalert %}

###### 例

次の例では、`LiveActivityManager` クラスがライブアクティビティオブジェクトを処理します。次に、`registerPushToStart` メソッドが `SportsActivityAttributes` を登録します。

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

#### ステップ 2.4: push-to-start 通知を送信する

[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) エンドポイントを使用してリモートの push-to-start 通知を送信します。
{% endtab %}

{% tab local %}
[Apple の ActivityKit フレームワーク](https://developer.apple.com/documentation/activitykit)を使用して、Braze SDK が管理できるプッシュトークンを取得できます。これにより、Braze がバックエンドで Apple プッシュ通知サービス（APNs）にプッシュトークンを送信するため、Braze API を通じてライブアクティビティを更新できます。

1. Apple の ActivityKit API を使用して、ライブアクティビティ実装のインスタンスを作成します。
2. `pushType` パラメータを `.token` に設定します。 
3. 定義したライブアクティビティの `ActivitiesAttributes` と `ContentState` を渡します。 
4. [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class) に渡して、Braze インスタンスにアクティビティを登録します。`pushTokenTag` パラメータは、定義するカスタム文字列です。作成するライブアクティビティごとに一意である必要があります。

ライブアクティビティを登録すると、Braze SDK はプッシュトークンの変化を抽出して監視します。

#### 例

この例では、ライブアクティビティオブジェクトのインターフェイスとして `LiveActivityManager` というクラスを作成します。次に、`pushTokenTag` を `"sports-game-2024-03-15"` に設定します。

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

ライブアクティビティウィジェットによって、この初期コンテンツがユーザーに表示されます。 

![2つのチームのスコアが表示された iPhone ロック画面のライブアクティビティ。Wild Bird Fund と Owl Rehab のスコアはどちらも0。]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### ステップ 3: アクティビティトラッキングを再開する {#resume-activity-tracking}

Braze がアプリ起動時にライブアクティビティを追跡できるようにするには、次の手順を実行します。

1. `AppDelegate` ファイルを開きます。
2. 使用可能な場合は、`ActivityKit` モジュールをインポートします。
3. アプリケーションで登録したすべての `ActivityAttributes` タイプについて、`application(_:didFinishLaunchingWithOptions:)` で [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) を呼び出します。

これにより、Braze はすべてのアクティブなライブアクティビティのプッシュトークン更新を追跡するタスクを再開できます。ユーザーがデバイス上のライブアクティビティを明示的に削除した場合、そのアクティビティは削除されたと見なされ、Braze はそれを追跡しなくなります。

###### 例

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

### ステップ 4: アクティビティを更新する {#update-the-activity}

![2チームのスコアが表示された iPhone ロック画面のライブアクティビティ。Wild Bird Fund は2ポイント、Owl Rehab は4ポイント。]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

[`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) エンドポイントを使用すると、Braze REST API を介して渡されたプッシュ通知を通じてライブアクティビティを更新できます。このエンドポイントを使用して、ライブアクティビティの `ContentState` を更新します。

`ContentState` を更新すると、ライブアクティビティウィジェットに新しい情報が表示されます。前半終了時の Superb Owl ショーの表示例を以下に示します。

詳細については、[`/messages/live_activity/update` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)の記事を参照してください。

### ステップ 5: アクティビティを終了する {#end-the-activity}

ライブアクティビティがアクティブな場合、ユーザーのロック画面とダイナミックアイランドの両方に表示されます。Braze を通じて終了するには、[`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) エンドポイントで `end_activity` を `true` に設定します。

ライブアクティビティの終了の信頼性を向上させるには、以下のオプションの手順を実行します。

1. 同じ `update` リクエストにオプションで `dismissal_date` を含め、iOS がライブアクティビティ UI を削除するタイミングを指定します。
2. [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)で配信結果を確認します。

#### 自動削除の設定

自動削除を設定するには、ライブアクティビティを開始した後に、更新エンドポイントへのフォローアップリクエストをスケジュールします。

1. 追跡可能な `activity_id` を含む `/messages/live_activity/start` リクエストを送信します。
2. その `activity_id` とターゲット終了時刻をバックエンドスケジューラーに保存します。
3. ターゲット終了時刻に、`end_activity` を `true` に設定した `/messages/live_activity/update` リクエストを送信します。
4. 同じ更新リクエストで削除日を設定します。詳細については、[`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) エンドポイントを参照してください。

削除のタイミングは iOS によって制御されることに注意してください。有効な終了リクエストを送信した後でも、ロック画面やダイナミックアイランドからの削除は、OS レベルの条件に基づいて遅延したり、異なる動作をしたりする場合があります。

ライブアクティビティは Braze の外部でも終了できます。

* **ユーザーによる削除**: ユーザーは手動でライブアクティビティを削除できます。
* **タイムアウト**: デフォルトの8時間が経過すると、iOS はユーザーのダイナミックアイランドからライブアクティビティを削除します。デフォルトの12時間が経過すると、iOS はユーザーのロック画面からライブアクティビティを削除します。

詳細については、[`/messages/live_activity/update` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)の記事を参照してください。

## ライブアクティビティのトラッキング

ライブアクティビティのイベントは、Currents、Snowflake Data Sharing、およびクエリビルダーで利用できます。以下のイベントは、ライブアクティビティのライフサイクルの理解と監視、トークンの利用可能性の追跡、問題の独立した診断や配信ステータスの確認に役立ちます。

- [ライブアクティビティの Push To Start トークン変更]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/#live-activity-push-to-start-token-change-events): push-to-start（PTS）トークンが Braze で追加または更新されたタイミングをキャプチャし、ユーザーごとのトークン登録状況と利用可能性を追跡できます。
- [ライブアクティビティ更新トークンの変更]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/#live-activity-update-token-change-events): ライブアクティビティ更新（LAU）トークンの追加、更新、または削除を追跡します。
- [ライブアクティビティ送信]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#live-activity-send-events): Braze によってライブアクティビティが開始、更新、または終了されるたびにログを記録します。
- [ライブアクティビティの結果]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#live-activity-outcome-events): Braze から送信された各ライブアクティビティについて、Apple プッシュ通知サービス（APNs）への最終的な配信ステータスを示します。

## よくある質問（FAQ） {#faq}

### 機能とサポート

#### ライブアクティビティをサポートしているプラットフォームは？

現在、ライブアクティビティは iOS と iPadOS に固有の機能です。デフォルトでは、iPhone や iPad で起動したアクティビティは、ペアリングされた watchOS 11 以降または macOS 26 以降のデバイスにも表示されます。

![macOS のメニューバーにライブアクティビティがアラートとして表示されているスクリーンショット。]({% image_buster /assets/img/live-activity-macos.png %}){: style="max-width:60%;"}

ライブアクティビティの記事では、Braze Swift SDK を使用してライブアクティビティを管理するための[前提条件]({{site.baseurl}}/developer_guide/platforms/swift/live_activities/#prerequisites)について説明しています。

#### React Native アプリはライブアクティビティをサポートしていますか？

はい、React Native SDK 3.0.0 以降は、Braze Swift SDK 経由でライブアクティビティをサポートしています。つまり、Braze Swift SDK の上に直接 React Native iOS のコードを記述する必要があります。 

Apple が提供するライブアクティビティ機能は、JavaScript では変換できない言語機能（Swift Concurrency、generics、SwiftUI など）を使用しているため、ライブアクティビティ用の React Native 固有の JavaScript コンビニエンス API は存在しません。

#### Braze はキャンペーンやキャンバスステップとしてのライブアクティビティをサポートしていますか？

いいえ、現在サポートされていません。

### プッシュ通知とライブアクティビティ

#### ライブアクティビティがアクティブな状態でプッシュ通知が送信された場合はどうなりますか？ 

![ブルズ対ベアーズのスポーツ中継のライブアクティビティが画面中央に、プッシュ通知の lorem ipsum テキストが画面下部に表示された携帯電話の画面。]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

ライブアクティビティとプッシュ通知は異なる画面領域を占有するため、ユーザーの画面上で競合することはありません。

#### ライブアクティビティがプッシュメッセージ機能を活用する場合、ライブアクティビティを受信するためにプッシュ通知を有効にする必要がありますか？

ライブアクティビティは更新にプッシュ通知を利用しますが、異なるユーザー設定によって制御されています。ユーザーはライブアクティビティにオプトインしつつプッシュ通知はオプトアウトでき、その逆も可能です。

ライブアクティビティ更新トークンは8時間後に期限切れになります。

#### ライブアクティビティにはプッシュプライマーが必要ですか？

[プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)は、ユーザーにアプリからのプッシュ通知をオプトインするよう促すベストプラクティスです。しかし、ライブアクティビティにオプトインするためのシステムプロンプトはありません。デフォルトでは、ユーザーが iOS 16.1 以降でアプリをインストールすると、そのアプリのライブアクティビティにオプトインされます。この権限は、アプリごとにデバイス設定で無効化または再有効化できます。

### 技術的なトピックとトラブルシューティング

#### ライブアクティビティにエラーがあるかどうかを確認するには？

ライブアクティビティのエラーは、Braze ダッシュボードの[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)に記録されます。ここで「LiveActivity Errors」でフィルターできます。

#### push-to-start 通知を送信した後、ライブアクティビティを受信できないのはなぜですか？

まず、[`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) エンドポイントで説明されているすべての必須フィールドがペイロードに含まれていることを確認します。`activity_attributes` および `content_state` フィールドは、プロジェクトのコードで定義されているプロパティと一致する必要があります。ペイロードが正しいことが確かな場合は、APNs によってレート制限されている可能性があります。この制限は Braze ではなく Apple によって課されています。

push-to-start 通知がデバイスに正常に届いたがレート制限のために表示されなかったことを確認するには、Mac のコンソールアプリを使用してプロジェクトをデバッグします。目的のデバイスの記録プロセスをアタッチし、検索バーで `process:liveactivitiesd` を使用してログをフィルタリングします。

#### push-to-start でライブアクティビティを開始した後、新しい更新を受信しないのはなぜですか？

[上記](#swift_brazeActivityAttributes)の手順が正しく実装されていることを確認してください。`ActivityAttributes` には、`BrazeLiveActivityAttributes` プロトコルへの準拠と `brazeActivityId` プロパティの両方が含まれている必要があります。

ライブアクティビティの push-to-start 通知を受信したら、Braze URL の `/push_token_tag` エンドポイントへの送信ネットワークリクエストが表示され、`"tag"` フィールドの下に正しいアクティビティ ID が含まれていることを再確認してください。

最後に、更新ペイロード内のライブアクティビティ属性タイプが、SDK メソッド呼び出しの `registerPushToStart` で使用した文字列とクラスに完全に一致していることを確認してください。定数を使用してタイプミスを防いでください。  

#### `live_activity/update` エンドポイントを使用しようとすると、アクセス拒否の応答が返されます。なぜですか？

使用する API キーには、さまざまな Braze API エンドポイントにアクセスするための適切な権限を付与する必要があります。以前に作成した API キーを使用している場合、権限の更新を忘れている可能性があります。[API キーセキュリティの概要]({{site.baseurl}}/api/basics/#rest-api-key-security)を確認してください。

#### `messages/send` エンドポイントは `messages/live_activity/update` エンドポイントとレート制限を共有していますか？ 

デフォルトでは、`messages/live_activity/update` エンドポイントのレート制限は、ワークスペースごとに、複数のエンドポイントにわたって、1時間あたり250,000リクエストです。詳細については、[API レート制限]({{site.baseurl}}/api/api_limits/)を参照してください。