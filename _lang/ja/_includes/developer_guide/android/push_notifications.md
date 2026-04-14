{% multi_lang_include developer_guide/prerequisites/android.md %}

## 内蔵機能

以下の機能は Braze Android SDK に組み込まれています。その他のプッシュ通知機能を利用するには、アプリ向けに[プッシュ通知を設定](#android_setting-up-push-notifications)する必要があります。

|機能|説明|
|-------|-----------|
|Push Stories|Android の Push Stories は、Braze Android SDK にデフォルトで組み込まれています。詳しくは [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/) を参照してください。|
|プッシュプライマー|プッシュプライマーキャンペーンでは、アプリのデバイスでプッシュ通知を有効にするようユーザーに促します。これは、[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## プッシュ通知のライフサイクルについて {#push-notification-lifecycle}

以下のフローチャートは、Braze がプッシュ通知のライフサイクル（許可プロンプト、トークン生成、メッセージ配信など）をどのように処理するかを示しています。

{% tabs local %}
{% tab Granting permissions %}
```mermaid
---
config:
  theme: neutral
---
flowchart TD

%% Permission flow
subgraph Permission[Push Permissions]
    B{Android version of the device?}
    B -->|Android 13+| C["requestPushPermissionPrompt() called"]
    B -->|Android 12 and earlier| D[No permissions required]
    
    %% Connect Android 12 path to Braze state
    D --> H3[Braze: user subscription state]
    H3 --> J3[Defaults to 'subscribed' when user profile created]
    
    C --> E{Did the user grant push permission?}
    E -->|Yes| F[POST_NOTIFICATIONS permission granted]
    E -->|No| G[POST_NOTIFICATIONS permission denied]
    
    %% Braze subscription state updates
    F --> H1[Braze: user subscription state]
    G --> H2[Braze: user subscription state]
    
    H1 --> I1{Automatically opt in after permission granted?}
    I1 -->|true| J1[Set to 'opted-in']
    I1 -->|false| J2[Remains 'subscribed']
    
    H2 --> K1[Remains 'subscribed'<br/>or 'unsubscribed']
    
    %% Subscription state legend
    subgraph BrazeStates[Braze subscription states]
        L1['Subscribed' - default state<br/>when user profile created]
        L2['Opted-in' - user explicitly<br/>wants push notifications]
        L3['Unsubscribed' - user explicitly<br/>opted out of push]
    end
    
    %% Note about user-level states
    note1[Note: These states are user-level<br/>and apply across all devices for the user]
    
    %% Connect states to legend
    J1 -.-> L2
    J2 -.-> L1
    J3 -.-> L1
    K1 -.-> L3
    note1 -.-> BrazeStates
end

%% Styling
classDef permissionClass fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
classDef tokenClass fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
classDef sdkClass fill:#fff3e0,stroke:#e65100,stroke-width:2px
classDef configClass fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
classDef displayClass fill:#ffebee,stroke:#c62828,stroke-width:2px
classDef deliveryClass fill:#fce4ec,stroke:#c2185b,stroke-width:2px
classDef brazeClass fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px

class A,B,C,E,F,G permissionClass
class H,I tokenClass
class J,K sdkClass
class N,O,P configClass
class R,S,S1,T,U,V displayClass
class W,X,X1,X2,Y,Z deliveryClass
class H1,H2,H3,I1,J1,J2,J3,K1,L1,L2,L3,note1 brazeClass
```
{% endtab %}

{% tab Generating push tokens %}
```mermaid
---
config:
  theme: neutral
---
flowchart TD

%% Token generation flow
subgraph Token[Token Generation]
    H["Braze SDK initialized"] --> Q{Is FCM auto-registration enabled?}
    Q -->|Yes| L{Is required configuration present?}
    Q -->|No| M[No FCM token generated]
    L -->|Yes| I[Generate FCM token]
    L -->|No| M
    I --> K[Register token with Braze]

    %% Configuration requirements
    subgraph Config[Required configuration]
        N['google-services.json' file is present]
        O['com.google.firebase:firebase-messaging' in gradle]
        P['com.google.gms.google-services' plugin in gradle]
    end

    %% Connect config to check
    N -.-> L
    O -.-> L
    P -.-> L
end

%% Styling
classDef permissionClass fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
classDef tokenClass fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
classDef sdkClass fill:#fff3e0,stroke:#e65100,stroke-width:2px
classDef configClass fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
classDef displayClass fill:#ffebee,stroke:#c62828,stroke-width:2px
classDef deliveryClass fill:#fce4ec,stroke:#c2185b,stroke-width:2px
classDef brazeClass fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px

class A,B,C,E,F,G permissionClass
class H,I tokenClass
class J,K sdkClass
class N,O,P configClass
class R,S,S1,T,U,V displayClass
class W,X,X1,X2,Y,Z deliveryClass
class H1,H2,H3,I1,J1,J2,J3,K1,L1,L2,L3,note1 brazeClass
```
{% endtab %}

{% tab Displaying notifications %}
```mermaid
---
config:
  theme: neutral
  fontSize: 10
---
flowchart TD

subgraph Display[Push Display]
    %% Push delivery flow
    W[Push sent to FCM servers] --> X{Did FCM receive push?}
    X -->|App is terminated| Y[FCM cannot deliver push to the app]
    X -->|Delivery conditions met| X1[App receives push from FCM]
    X1 --> X2[Braze SDK receives push]
    X2 --> R[Push type?]

    %% Push Display Flow
    R -->|Standard push| S{Is push permission required?}
    R -->|Silent push| T[Braze SDK processes silent push]
    S -->|Yes| S1{Did the user grant push permission?}
    S -->|No| V[Notification is shown to the user]
    S1 -->|Yes| V
    S1 -->|No| U[Notification is not shown to the user]
end

%% Styling
classDef permissionClass fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
classDef tokenClass fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
classDef sdkClass fill:#fff3e0,stroke:#e65100,stroke-width:2px
classDef configClass fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
classDef displayClass fill:#ffebee,stroke:#c62828,stroke-width:2px
classDef deliveryClass fill:#fce4ec,stroke:#c2185b,stroke-width:2px
classDef brazeClass fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px

class A,B,C,E,F,G permissionClass
class H,I tokenClass
class J,K sdkClass
class N,O,P configClass
class R,S,S1,T,U,V displayClass
class W,X,X1,X2,Y,Z deliveryClass
class H1,H2,H3,I1,J1,J2,J3,K1,L1,L2,L3,note1 brazeClass
```
{% endtab %}
{% endtabs %}

## プッシュ通知の設定

{% alert tip %}
Braze Android SDK で FCM を使用するサンプルアプリを確認するには、[Braze: Firebase Push サンプルアプリ](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push)を参照してください。
{% endalert %}

### レート制限

Firebase Cloud Messaging（FCM）API には、1分あたり 600,000 リクエストというデフォルトのレート制限があります。この制限に達した場合、Braze は数分後に自動的に再試行します。引き上げをリクエストするには、[Firebase サポート](https://firebase.google.com/support)にお問い合わせください。

### ステップ 1: Firebase をプロジェクトに追加する

まず、Firebase を Android プロジェクトに追加します。手順については、Google の [Firebase セットアップガイド](https://firebase.google.com/docs/android/setup)を参照してください。

### ステップ 2: Cloud Messaging を依存関係に追加する

次に、Cloud Messaging ライブラリーをプロジェクトの依存関係に追加します。Android プロジェクトで `build.gradle` を開き、`dependencies` ブロックに次の行を追加します。

```gradle
implementation "google.firebase:firebase-messaging:+"
```

依存関係は次のようになります。

```gradle
dependencies {
  implementation project(':android-sdk-ui')
  implementation "com.google.firebase:firebase-messaging:+"
}
```

### ステップ 3: Firebase Cloud Messaging API を有効にする

Google Cloud で、Android アプリが使用しているプロジェクトを選択し、[Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com) を有効にします。

![有効化された Firebase Cloud Messaging API]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### ステップ 4: サービスアカウントを作成する {#service-account}

次に、新しいサービスアカウントを作成し、FCM トークンの登録時に Braze が許可された API 呼び出しを行えるようにします。Google Cloud で [**サービスアカウント**] に移動し、プロジェクトを選択します。[**サービスアカウント**] ページで [**サービスアカウントの作成**] を選択します。

![プロジェクトのサービスアカウントのホームページで、「サービスアカウントを作成」が強調表示されている。]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

サービスアカウント名、ID、説明を入力して、[**作成して続行**] を選択します。

![「サービスアカウントの詳細」のフォーム。]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

[**ロール**] フィールドで、ロールのリストから [**Firebase Cloud Messaging API 管理者**] を見つけて選択します。アクセスをより制限する場合は、`cloudmessaging.messages.create` 権限を持つ[カスタムロール](https://cloud.google.com/iam/docs/creating-custom-roles)を作成し、代わりにリストからそれを選択します。完了したら、[**完了**] を選択します。

{% alert warning %}
[**Firebase Cloud Messaging 管理者**] ではなく、[**Firebase Cloud Messaging _API_ 管理者**] を選択してください。
{% endalert %}

![「このサービスアカウントにプロジェクトへのアクセスを許可する」フォームで、「Firebase Cloud Messaging API 管理者」がロールとして選択されている。]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### ステップ 5: JSON 認証情報を生成する {#json}

次に、FCM サービスアカウントの JSON 認証情報を生成します。Google Cloud IAM & Admin で [**サービスアカウント**] に移動し、プロジェクトを選択します。[先ほど作成した](#android_service-account) FCM サービスアカウントを見つけて、<i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;[**アクション**] > [**キーの管理**] を選択します。

![プロジェクトのサービスアカウントのホームページで、「アクション」メニューが開いている状態。]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

[**キーの追加**] > [**新しいキーを作成**] を選択します。

![「キーを追加」メニューが開いている状態で選択されたサービスアカウント。]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

[**JSON**] を選択し、[**作成**] を選択します。FCM プロジェクト ID とは異なる Google Cloud プロジェクト ID を使用してサービスアカウントを作成した場合は、JSON ファイルで `project_id` に割り当てられた値を手動で更新する必要があります。

キーをどこにダウンロードしたかを覚えておいてください。次のステップで必要になります。

![「JSON」を選択した状態で秘密キーを作成するフォーム。]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。JSON の認証情報は安全な場所に保存しておいてください。キーは Braze にアップロードした後で削除します。
{% endalert %}

### ステップ 6: JSON の認証情報を Braze にアップロードする

次に、JSON 認証情報を Braze ダッシュボードにアップロードします。Braze で、<i class="fa-solid fa-gear"></i>&nbsp;[**設定**] > [**アプリの設定**] を選択します。

![「設定」メニューが Braze で開かれ、「アプリの設定」がハイライト表示されている。]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Android アプリの [**プッシュ通知設定**] で [**Firebase**] を選択し、[**JSON ファイルのアップロード**] を選択して、[先ほど生成した](#android_json)認証情報をアップロードします。完了したら、[**保存**] を選択します。

![プッシュ通知プロバイダーとして「Firebase」が選択された「プッシュ通知設定」フォーム。]({% image_buster /assets/img/android/push_integration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。キーが Braze にアップロードされたので、[先に生成した](#android_json)ファイルを削除してください。
{% endalert %}

### ステップ 7: トークンの自動登録を設定する

ユーザーがプッシュ通知をオプトインした場合、アプリはそのユーザーにプッシュ通知を送信する前に、ユーザーのデバイス上で FCM トークンを生成する必要があります。Braze SDK を使用すると、プロジェクトの Braze 設定ファイルで各ユーザーのデバイスの FCM トークン自動登録を有効にすることができます。

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>&nbsp;[**設定**] > [**プロジェクト設定**] を選択します。

![「設定」メニューが開いている Firebase プロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

[**Cloud Messaging**] を選択し、[**Firebase Cloud Messaging API (V1)**] で [**送信者 ID**] フィールドの数字をコピーします。

![Firebase プロジェクトの「Cloud Messaging」ページで「送信者 ID」が強調表示されている。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

次に、Android Studio プロジェクトを開き、Firebase 送信者 ID を使用して、`braze.xml` または `BrazeConfig` 内で FCM トークンの自動登録を有効にします。

{% tabs local %}
{% tab Braze.XML %}
FCM トークンの自動登録を設定するには、`braze.xml` ファイルに以下の行を追加します。

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

`FIREBASE_SENDER_ID` を Firebase プロジェクトの設定からコピーした値に置き換えます。`braze.xml` は次のようになります。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">12345ABC-6789-DEFG-0123-HIJK456789LM</string>
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">603679405392</string>
</resources>
```
{% endtab %}

{% tab BrazeConfig %}
FCM トークンの自動登録を設定するには、`BrazeConfig` に以下の行を追加します。

{% subtabs local %}
{% subtab JAVA %}
```java
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% endsubtabs %}

`FIREBASE_SENDER_ID` を Firebase プロジェクトの設定からコピーした値に置き換えます。`BrazeConfig` は次のようになります。

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build();
Braze.configure(this, brazeConfig);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
val brazeConfig = BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
代わりに FCM トークンを手動で登録する場合は、アプリの [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) メソッド内で [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) を呼び出すことができます。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ 8: アプリケーションクラスの自動リクエストを削除する

サイレントプッシュ通知を送信するたびに Braze が不要なネットワークリクエストをトリガーするのを防ぐには、`Application` クラスの `onCreate()` メソッドで設定されている自動ネットワークリクエストをすべて削除してください。詳細については、[Android 開発者リファレンス: Application](https://developer.android.com/reference/android/app/Application) を参照してください。

## 通知を表示する

### ステップ 1: Braze Firebase メッセージングサービスを登録する

新規、既存、または Braze 以外の Firebase メッセージングサービスを作成できます。特定のニーズに最も合うものを選択してください。

{% tabs local %}
{% tab New %}
Braze には、プッシュ受信インテントと開封インテントを処理するサービスが含まれています。`BrazeFirebaseMessagingService` クラスは `AndroidManifest.xml` に登録する必要があります。

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

通知コードでは、`BrazeFirebaseMessagingService` を使用して、オープンアクションとクリックアクションのトラッキングも処理します。このサービスが正しく機能するには、`AndroidManifest.xml` に登録する必要があります。また、Braze はシステムからの通知に固有のキーをプレフィックスとして付加するため、Braze のシステムから送信された通知のみをレンダリングします。他の FCM サービスから送信される通知を表示するために、追加のサービスを個別に登録することもできます。Firebase プッシュサンプルアプリの [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml) を参照してください。

{% alert important %}
Braze SDK 3.1.1 より前では、FCM プッシュを処理するために `AppboyFcmReceiver` が使用されていました。マニフェストから `AppboyFcmReceiver` クラスを削除し、前述の統合に置き換える必要があります。
{% endalert %}
{% endtab %}

{% tab Existing %}
Firebase Messaging Service がすでに登録されている場合は、[`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) オブジェクトを [`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html) 経由で Braze に渡すことができます。このメソッドは [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) オブジェクトが Braze から発信された場合にのみ通知を表示し、そうでない場合は安全に無視します。

{% subtabs %}
{% subtab JAVA %}

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
  override fun onMessageReceived(remoteMessage: RemoteMessage?) {
    super.onMessageReceived(remoteMessage)
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Non-Braze %}
使用したい別の Firebase メッセージングサービスがある場合は、アプリケーションが Braze からではないプッシュを受信した場合に呼び出すフォールバック Firebase メッセージングサービスを指定することもできます。

`braze.xml` で次のように指定します。

```xml
<bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool>
<string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>
```

または、[ランタイム設定]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)で設定します。

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 2: 小さなアイコンをデザインガイドラインに準拠させる

Android 通知アイコンの一般的な情報については、[通知の概要](https://developer.android.com/guide/topics/ui/notifiers/notifications)をご覧ください。

Android N 以降、色を使った小さな通知アイコンアセットは更新または削除する必要があります。Android システム（Braze SDK ではない）は、アクションアイコンと小さな通知アイコンの非アルファチャネルと透明チャネルをすべて無視します。つまり、Android は小さな通知アイコンの透明領域を除くすべての部分をモノクロに変換します。

正しく表示される通知用小さなアイコンアセットを作成するには：
- 画像から白以外のすべての色を削除します。
- アセットの他のすべての非白色領域は透明にする必要があります。

{% alert note %}
不適切なアセットでよく見られる症状の 1 つは、小さな通知アイコンが単色の正方形としてレンダリングされることです。これは、Android システムが小さな通知アイコンアセットで透明領域を見つけられないことが原因です。
{% endalert %}

次の図の大小アイコンは、適切にデザインされたアイコンの例です。

![大きなアイコンの隅に小さなアイコンが表示され、その横に「Hey I'm on my way to the bar but..」というメッセージが表示されている]({% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "Large and Small Notification Icon")

### ステップ 3: 通知アイコンを設定する {#configure-icons}

#### braze.xml でアイコンを指定する

Braze では、`braze.xml` 内で drawable リソースを指定することで、通知アイコンを設定できます。

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

小さな通知アイコンの設定は必須です。**設定しない場合、Braze はデフォルトでアプリケーションアイコンを小さな通知アイコンとして使用しますが、最適に表示されない可能性があります。**

大きな通知アイコンの設定は任意ですが、推奨されます。

#### アイコンのアクセントカラーを指定する

通知アイコンのアクセントカラーは、`braze.xml` でオーバーライドできます。色を指定しない場合、デフォルトの色は Lollipop がシステム通知に使用するのと同じグレーになります。

```xml
<integer name="com_braze_default_notification_accent_color">0xFFf33e3e</integer>
```

オプションでカラーリファレンスを使用することもできます。

```xml
<color name="com_braze_default_notification_accent_color">@color/my_color_here</color>
```

### ステップ 4: ディープリンクを追加する

#### ディープリンクの自動オープンを有効にする

プッシュ通知がクリックされたときに Braze がアプリとディープリンクを自動的に開くようにするには、`braze.xml` で `com_braze_handle_push_deep_links_automatically` を `true` に設定します。

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

このフラグは、[ランタイム設定]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)で設定することもできます。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

ディープリンクをカスタムで処理する場合は、Braze からのプッシュ受信およびオープンインテントをリッスンするプッシュコールバックを作成する必要があります。詳細については、[プッシュイベントのコールバックの使用]({{site.baseurl}}/developer_guide/push_notifications/customization#android_using-a-callback-for-push-events)を参照してください。

## フォアグラウンド通知の処理

Android では、アプリがフォアグラウンドにあるときにプッシュ通知が届くと、デフォルトでシステムが自動的に表示します。Braze にプッシュ通知のペイロードを処理させる場合（分析トラッキング、ディープリンク処理、カスタム処理のため）、`FirebaseMessagingService.onMessageReceived` メソッド内で受信したプッシュデータを Braze にルーティングしてください。

### 仕組み

`BrazeFirebaseMessagingService.handleBrazeRemoteMessage` を呼び出すと、Braze はペイロードが Braze プッシュ通知かどうかを判断し、該当する場合は `NotificationManagerCompat` メソッドで通知を作成して表示します。iOS とは異なり、Android はアプリがフォアグラウンドにあるかバックグラウンドにあるかを問わず通知を表示します。

{% tabs %}
{% tab JAVA %}
```java
package com.example.push;

import com.braze.push.BrazeFirebaseMessagingService;
import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {
    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);
        
        // Let Braze process the payload and display the notification
        if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
            // Braze successfully handled the push notification
        } else {
            // Handle non-Braze messages
        }
    }
}
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
package com.example.push

import com.braze.push.BrazeFirebaseMessagingService
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        super.onMessageReceived(remoteMessage)
        
        // Let Braze process the payload and display the notification
        if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
            // Braze successfully handled the push notification
        } else {
            // Handle non-Braze messages
        }
    }
}
```
{% endtab %}
{% endtabs %}

詳細については、Braze Android SDK リポジトリ内の [Firebase 統合サンプル](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/java/com/braze/firebasepush/FirebaseMessagingService.kt)を参照してください。

### フォアグラウンド動作のカスタマイズ

カスタムのフォアグラウンド動作を実装したい場合（システム通知を抑制したり、代わりにアプリ内 UI を表示したりするなど）、以下の方法があります。

- `subscribeToPushNotificationEvents` を使用してプッシュイベントに反応し、`BrazeNotificationUtils.routeUserWithNotificationOpenedIntent` メソッドでディープリンクを処理します。詳細については、[Firebase プッシュサンプル](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/java/com/braze/firebasepush/FirebaseApplication.kt)を参照してください。
- カスタムの `IBrazeNotificationFactory` を使用して独自の通知を構築して投稿するか、処理パスで `notificationManager.notify` を呼び出さないことで通知を抑制します。

通知のカスタマイズに関する詳細は、[カスタム通知ファクトリ]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#custom-notification-factory)を参照してください。

#### カスタムディープリンクの作成

アプリにまだディープリンクを追加していない場合は、[Android 開発者ドキュメント](http://developer.android.com/training/app-indexing/deep-linking.html)に記載されているディープリンクに関する手順に従ってください。ディープリンクの詳細については、[FAQ の記事]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)を参照してください。

#### ディープリンクの追加

Braze ダッシュボードは、通知がクリックされたときに開くプッシュ通知キャンペーンとキャンバスでのディープリンクまたは Web URL の設定をサポートしています。

![Braze ダッシュボードの「クリック時の動作」設定で、ドロップダウンから「アプリケーションへのディープリンク」を選択している状態。]({% image_buster /assets/img_archive/deep_link_click_action.png %} "Deep Link Click Action")

#### バックスタック動作のカスタマイズ

Android SDK のデフォルトでは、プッシュのディープリンクを辿ると、ホストアプリのメインのランチャーアクティビティがバックスタックに配置されます。Braze では、メインのランチャーアクティビティの代わりにバックスタックで開くカスタムアクティビティを設定したり、バックスタックを完全に無効にしたりすることができます。

たとえば、[ランタイム設定]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)を使用して、`YourMainActivity` というアクティビティをバックスタックアクティビティとして設定するには、次のようにします。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

`braze.xml` の同等の設定を参照してください。クラス名は `Class.forName()` で返されるものと同じでなければならないことに注意してください。

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">true</bool>
<string name="com_braze_push_deep_link_back_stack_activity_class_name">your.package.name.YourMainActivity</string>
```

### ステップ 5: 通知チャネルを定義する

Braze Android SDK は [Android 通知チャネル](https://developer.android.com/preview/features/notification-channels.html)をサポートしています。Braze の通知に通知チャネルの ID が含まれていない場合、または Braze の通知に無効なチャネル ID が含まれている場合、Braze は SDK で定義されているデフォルトの通知チャネルで通知を表示します。Braze ユーザーはプラットフォーム内で [Android 通知チャネル]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/)を使用して通知をグループ化します。

デフォルトの Braze 通知チャネルのユーザー向けの名前を設定するには、[`BrazeConfig.setDefaultNotificationChannelName()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html) を使用します。

デフォルトの Braze 通知チャネルのユーザー向けの説明を設定するには、[`BrazeConfig.setDefaultNotificationChannelDescription()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html) を使用します。

[Android プッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/android_object/)パラメータを使用して API キャンペーンを更新し、`notification_channel` フィールドを含めます。このフィールドが指定されていない場合、Braze は[ダッシュボードフォールバック]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel)チャネル ID を持つ通知ペイロードを送信します。

デフォルトの通知チャネル以外、Braze はチャネルを作成しません。他のすべてのチャネルは、ホストアプリでプログラムで定義してから、Braze ダッシュボードに入力する必要があります。

デフォルトのチャネル名と説明も `braze.xml` で設定できます。

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### ステップ 6: 通知の表示と分析をテストする

#### 表示のテスト

この時点で、Braze から送信された通知を表示できるはずです。これをテストするには、Braze ダッシュボードの [**キャンペーン**] ページにアクセスし、**プッシュ通知**キャンペーンを作成します。[**Android プッシュ**] を選択し、メッセージをデザインします。次に、作成画面で目のアイコンをクリックしてテスト送信者を取得します。現在のユーザーのユーザー ID またはメールアドレスを入力し、[**テストを送信**] をクリックします。デバイスにプッシュが表示されます。

![Braze ダッシュボード内のプッシュ通知キャンペーンの「テスト」タブ。]({% image_buster /assets/img_archive/android_push_test.png %} "Android Push Test")

プッシュ表示に関する問題については、[トラブルシューティングガイド]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)を参照してください。

#### 分析のテスト

この時点で、プッシュ通知の開封に関する分析ログも記録されているはずです。届いた通知をクリックすると、キャンペーン結果ページの [**直接開封数**] の値が 1 増えます。プッシュ分析の内訳については、[プッシュレポート]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/)の記事をご覧ください。

プッシュ分析に関する問題については、[トラブルシューティングガイド]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)を参照してください。

#### コマンドラインからのテスト

コマンドラインインターフェイスを介してアプリ内通知とプッシュ通知をテストする場合は、cURL と[メッセージング API]({{site.baseurl}}/api/endpoints/messaging/) を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY`（[**設定**] > [**API キー**] に移動）
- `YOUR_EXTERNAL_USER_ID`（[**ユーザーを検索**] ページでプロファイルを検索）
- `YOUR_KEY1`（省略可能）
- `YOUR_VALUE1`（省略可能）

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }  
  }
}' https://rest.iad-01.braze.com/messages/send
```

この例では、`US-01` インスタンスを使用しています。このインスタンスを使用していない場合は、`US-01` エンドポイントを[自分のエンドポイント]({{site.baseurl}}/api/basics/#endpoints)に置き換えてください。

## 会話プッシュ通知

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

[人と会話のイニシアチブ](https://developer.android.com/guide/topics/ui/conversations)は、スマートフォンのシステムサーフェスで人との会話を向上させることを目的とした、複数年にわたる Android の取り組みです。この優先順位は、他のユーザーとのコミュニケーションや対話が、あらゆるユーザー層にわたる大多数の Android ユーザーにとって、依然として最も価値のある重要な機能分野であるという事実に基づいています。

### 使用要件

- この通知タイプには、Braze Android SDK v15.0.0 以降と Android 11 以降のデバイスが必要です。
- サポートされていないデバイスや SDK は、標準のプッシュ通知にフォールバックします。

この機能は Braze REST API 経由でのみ利用できます。詳細については、[Android プッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object)を参照してください。

## FCM のクォータ超過エラー

Firebase Cloud Messaging（FCM）の制限を超過すると、Google は「クォータ超過」エラーを返します。FCM のデフォルトの制限は、1分あたり 600,000 リクエストです。Braze は Google が推奨するベストプラクティスに従って送信を再試行します。しかし、こうしたエラーが大量に発生すると、送信時間が数分間長引くことがあります。潜在的な影響を軽減するために、Braze はレート制限を超えていることを示すアラートと、エラーを防ぐために実行できるステップを送信します。

現在の制限を確認するには、**Google Cloud コンソール** > **API とサービス** > **Firebase Cloud Messaging API** > **クォータとシステム制限**に移動するか、[FCM API クォータのページ](https://console.cloud.google.com/apis/api/fcm.googleapis.com/quotas)にアクセスしてください。

### ベストプラクティス

これらのエラー発生量を低く抑えるために、以下のベストプラクティスを推奨します。

#### FCM にレート制限の引き上げをリクエストする

FCM のレート制限の引き上げをリクエストするには、[Firebase サポート](https://firebase.google.com/support)に直接連絡するか、以下の手順を実行します。

1. [FCM API のクォータページ](https://console.cloud.google.com/apis/api/fcm.googleapis.com/quotas)に移動します。
2. **1分あたりのリクエスト送信**クォータを確認します。
3. **クォータの編集**を選択します。
4. 新しい値を入力し、リクエストを送信します。

#### ワークスペースのレート制限を適用する

Android プッシュ通知にワークスペースのレート制限を適用できます。これにより、送信メッセージの配信レートを調整できます。詳細については、[ワークスペースのメッセージングレート制限]({{site.baseurl}}/user_guide/administrative/app_settings/messaging_rate_limits)を参照してください。