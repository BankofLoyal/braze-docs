{% multi_lang_include developer_guide/prerequisites/android.md %}

## 내장 기능

다음 기능들은 Braze Android SDK에 내장되어 있습니다. 다른 푸시 알림 기능을 사용하려면 앱에 [푸시 알림을 설정해야](#android_setting-up-push-notifications) 합니다.

|기능|설명|
|-------|-----------|
|푸시 스토리|Android 푸시 스토리는 기본적으로 Braze Android SDK에 내장되어 있습니다. 자세한 내용은 [푸시 스토리]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)를 참조하세요.|
|푸시 프라이머|푸시 프라이머 캠페인은 사용자가 기기에서 앱에 대한 푸시 알림을 활성화하도록 유도합니다. [노코드 푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)를 사용하면 SDK 커스텀 없이도 이 작업을 수행할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 푸시 알림 수명 주기에 관하여 {#push-notification-lifecycle}

다음 플로우 차트는 Braze가 푸시 알림 수명 주기(예: 권한 요청, 토큰 생성, 메시지 전달)를 처리하는 방식을 보여줍니다.

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

## 푸시 알림 설정

{% alert tip %}
Braze Android SDK를 사용한 FCM 샘플 앱을 확인하려면 [Braze: Firebase 푸시 샘플 앱](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push)을 참조하세요.
{% endalert %}

### 사용량 제한

Firebase 클라우드 메시징(FCM) API의 기본 사용량 제한은 분당 600,000건의 요청입니다. 이 제한에 도달하면 Braze는 몇 분 후에 자동으로 다시 시도합니다. 증액을 요청하려면 [Firebase 지원팀](https://firebase.google.com/support)에 문의하세요.

### 1단계: 프로젝트에 Firebase 추가

먼저 Android 프로젝트에 Firebase를 추가합니다. 단계별 지침은 Google의 [Firebase 설정 가이드](https://firebase.google.com/docs/android/setup)를 참조하세요.

### 2단계: 종속성에 클라우드 메시징 추가

다음으로 프로젝트 종속성에 클라우드 메시징 라이브러리를 추가합니다. Android 프로젝트에서 `build.gradle`을 열고 `dependencies` 블록에 다음 줄을 추가합니다.

```gradle
implementation "google.firebase:firebase-messaging:+"
```

종속성은 다음과 비슷해야 합니다:

```gradle
dependencies {
  implementation project(':android-sdk-ui')
  implementation "com.google.firebase:firebase-messaging:+"
}
```

### 3단계: Firebase 클라우드 메시징 API 활성화

Google Cloud에서 Android 앱이 사용 중인 프로젝트를 선택한 다음, [Firebase 클라우드 메시징 API](https://console.cloud.google.com/apis/library/fcm.googleapis.com)를 활성화합니다.

![Firebase 클라우드 메시징 API 활성화됨]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### 4단계: 서비스 계정 생성 {#service-account}

다음으로 Braze가 FCM 토큰을 등록할 때 승인된 API 호출을 할 수 있도록 새 서비스 계정을 생성합니다. Google Cloud에서 **서비스 계정**으로 이동한 다음 프로젝트를 선택합니다. **서비스 계정** 페이지에서 **서비스 계정 생성**을 선택합니다.

![프로젝트의 서비스 계정 홈 페이지에서 "서비스 계정 생성"이 강조 표시된 상태.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

서비스 계정 이름, ID, 설명을 입력한 다음, **생성 후 계속**을 선택합니다.

!["서비스 계정 세부 정보" 양식.]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

**역할** 필드에서 역할 목록에서 **Firebase Cloud Messaging API Admin**을 찾아 선택합니다. 보다 제한적인 액세스를 원하면 `cloudmessaging.messages.create` 권한으로 [커스텀 역할](https://cloud.google.com/iam/docs/creating-custom-roles)을 생성한 다음, 목록에서 해당 역할을 선택합니다. 완료했으면 **완료**를 선택합니다.

{% alert warning %}
**Firebase Cloud Messaging Admin**이 아닌 **Firebase Cloud Messaging _API_ Admin**을 선택해야 합니다.
{% endalert %}

!["이 서비스 계정에 프로젝트 접근 권한 부여" 양식에서 역할로 "Firebase Cloud Messaging API Admin"이 선택된 상태.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### 5단계: JSON 자격 증명 생성 {#json}

다음으로 FCM 서비스 계정에 대한 JSON 자격 증명을 생성합니다. Google Cloud IAM & Admin에서 **서비스 계정**으로 이동한 후 프로젝트를 선택합니다. [이전에 생성한](#android_service-account) FCM 서비스 계정을 찾은 다음, <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**동작** > **키 관리**를 선택합니다.

![프로젝트의 서비스 계정 홈페이지에 "동작" 메뉴가 열린 상태.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

**키 추가** > **새 키 생성**을 선택합니다.

!["키 추가" 메뉴가 열린 상태의 선택된 서비스 계정.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

**JSON**을 선택한 다음, **생성**을 선택합니다. FCM 프로젝트 ID와 다른 Google Cloud 프로젝트 ID를 사용하여 서비스 계정을 생성한 경우, JSON 파일에서 `project_id`에 할당된 값을 수동으로 업데이트해야 합니다.

키를 다운로드한 위치를 기억해 두세요&#8212;다음 단계에서 필요합니다.

!["JSON"이 선택된 상태에서 비공개 키를 생성하는 양식.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
비공개 키는 유출될 경우 보안 위험을 초래할 수 있습니다. 지금은 JSON 자격 증명을 안전한 위치에 보관하세요&#8212;Braze에 업로드한 후에 키를 삭제합니다.
{% endalert %}

### 6단계: Braze에 JSON 자격 증명 업로드

다음으로 Braze 대시보드에 JSON 자격 증명을 업로드합니다. Braze에서 <i class="fa-solid fa-gear"></i>&nbsp;**설정** > **앱 설정**을 선택합니다.

![Braze에서 "설정" 메뉴가 열리며 "앱 설정"이 강조 표시된 상태.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Android 앱의 **푸시 알림 설정**에서 **Firebase**를 선택한 다음, **JSON 파일 업로드**를 선택하고 [앞서 생성한](#android_json) 자격 증명을 업로드합니다. 완료했으면 **저장**을 선택합니다.

!["푸시 알림 설정" 양식에서 푸시 제공자로 "Firebase"가 선택된 상태.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
비공개 키는 유출될 경우 보안 위험을 초래할 수 있습니다. 키가 Braze에 업로드되었으므로 [이전에 생성한](#android_json) 파일을 삭제하세요.
{% endalert %}

### 7단계: 자동 토큰 등록 설정

사용자가 푸시 알림을 옵트인하면 앱에서 해당 사용자의 기기에 FCM 토큰을 생성해야 푸시 알림을 보낼 수 있습니다. Braze SDK를 사용하면 프로젝트의 Braze 구성 파일에서 각 사용자의 기기에 대한 FCM 토큰 자동 등록을 활성화할 수 있습니다.

먼저 Firebase 콘솔로 이동하여 프로젝트를 연 다음, <i class="fa-solid fa-gear"></i>&nbsp;**설정** > **프로젝트 설정**을 선택합니다.

!["설정" 메뉴가 열린 Firebase 프로젝트.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**클라우드 메시징**을 선택하고 **Firebase 클라우드 메시징 API(V1)**에서 **발신자 ID** 필드의 숫자를 복사합니다.

![Firebase 프로젝트의 "클라우드 메시징" 페이지에서 "발신자 ID"가 강조 표시된 상태.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

그런 다음 Android Studio 프로젝트를 열고 Firebase 발신자 ID를 사용하여 `braze.xml` 또는 `BrazeConfig`에서 FCM 토큰 자동 등록을 활성화합니다.

{% tabs local %}
{% tab Braze.XML %}
FCM 토큰 자동 등록을 구성하려면 `braze.xml` 파일에 다음 줄을 추가합니다:

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

`FIREBASE_SENDER_ID`를 Firebase 프로젝트 설정에서 복사한 값으로 바꿉니다. `braze.xml`은 다음과 비슷해야 합니다:

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
FCM 토큰 자동 등록을 구성하려면 `BrazeConfig`에 다음 줄을 추가합니다:

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

`FIREBASE_SENDER_ID`를 Firebase 프로젝트 설정에서 복사한 값으로 바꿉니다. `BrazeConfig`는 다음과 비슷해야 합니다:

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
FCM 토큰을 수동으로 등록하려면 앱의 [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) 메서드 내에서 [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html)을 호출하면 됩니다.
{% endalert %}
{% endtab %}
{% endtabs %}

### 8단계: 애플리케이션 클래스에서 자동 요청 제거

무음 푸시 알림을 보낼 때마다 Braze가 불필요한 네트워크 요청을 트리거하지 않도록 하려면 `Application` 클래스의 `onCreate()` 메서드에 구성된 모든 자동 네트워크 요청을 제거합니다. 자세한 내용은 [Android 개발자 참조: Application](https://developer.android.com/reference/android/app/Application)을 참조하세요.

## 알림 표시

### 1단계: Braze Firebase 메시징 서비스 등록

새로 생성하거나, 기존의 Firebase 메시징 서비스를 사용하거나, Braze 외 Firebase 메시징 서비스를 사용할 수 있습니다. 특정 요구 사항에 가장 잘 맞는 것을 선택하세요.

{% tabs local %}
{% tab New %}
Braze에는 푸시 수신 및 열기 의도를 처리하는 서비스가 포함되어 있습니다. `BrazeFirebaseMessagingService` 클래스는 `AndroidManifest.xml`에 등록해야 합니다:

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

알림 코드는 `BrazeFirebaseMessagingService`를 사용하여 열기 및 클릭 동작 추적을 처리합니다. 이 서비스가 제대로 작동하려면 `AndroidManifest.xml`에 등록해야 합니다. 또한 Braze는 시스템에서 보낸 알림만 렌더링하도록 알림에 고유한 키를 접두사로 추가합니다. 추가 서비스를 별도로 등록하여 다른 FCM 서비스에서 전송되는 알림을 렌더링할 수 있습니다. Firebase 푸시 샘플 앱에서 [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml)을 확인하세요.

{% alert important %}
Braze SDK 3.1.1 이전에는 `AppboyFcmReceiver`를 사용하여 FCM 푸시를 처리했습니다. `AppboyFcmReceiver` 클래스는 매니페스트에서 제거하고 위의 통합으로 대체해야 합니다.
{% endalert %}
{% endtab %}

{% tab Existing %}
이미 Firebase 메시징 서비스가 등록되어 있는 경우, [`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html)를 통해 [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) 오브젝트를 Braze에 전달할 수 있습니다. 이 메서드는 [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) 오브젝트가 Braze에서 발생한 경우에만 알림을 표시하며, 그렇지 않은 경우 안전하게 무시합니다.

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
사용하려는 다른 Firebase 메시징 서비스가 있는 경우, 애플리케이션이 Braze가 아닌 푸시를 수신할 때 호출할 대체 Firebase 메시징 서비스를 지정할 수 있습니다.

`braze.xml`에서 다음을 지정합니다:

```xml
<bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool>
<string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>
```

또는 [런타임 구성]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)을 통해 설정합니다:

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

### 2단계: 작은 아이콘을 디자인 가이드라인에 맞추기

Android 알림 아이콘에 대한 일반적인 정보는 [알림 개요](https://developer.android.com/guide/topics/ui/notifiers/notifications)를 참조하세요.

Android N부터는 색상이 포함된 작은 알림 아이콘 에셋을 업데이트하거나 제거해야 합니다. Android 시스템(Braze SDK가 아님)은 액션 아이콘과 작은 알림 아이콘에서 알파 및 투명도를 제외한 모든 채널을 무시합니다. 즉, Android는 투명한 영역을 제외한 작은 알림 아이콘의 모든 부분을 흑백으로 변환합니다.

올바르게 표시되는 작은 알림 아이콘 에셋을 만들려면:
- 이미지에서 흰색을 제외한 모든 색상을 제거합니다.
- 에셋의 흰색이 아닌 다른 모든 영역은 투명해야 합니다.

{% alert note %}
부적절한 에셋의 일반적인 증상은 작은 알림 아이콘이 단색 흑백 사각형으로 렌더링되는 것입니다. 이는 Android 시스템이 알림 작은 아이콘 에셋에서 투명한 영역을 찾을 수 없기 때문입니다.
{% endalert %}

다음에 표시된 큰 아이콘과 작은 아이콘은 올바르게 디자인된 아이콘의 예시입니다:

!["Hey I'm on my way to the bar but.."라는 메시지 옆의 큰 아이콘 하단 모서리에 작은 아이콘이 나타납니다.]({% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "Large and Small Notification Icon")

### 3단계: 알림 아이콘 구성 {#configure-icons}

#### braze.xml에서 아이콘 지정

Braze를 사용하면 `braze.xml`에서 drawable 리소스를 지정하여 알림 아이콘을 구성할 수 있습니다:

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

작은 알림 아이콘 설정은 필수입니다. **설정하지 않으면 Braze는 기본적으로 애플리케이션 아이콘을 작은 알림 아이콘으로 사용하며, 이는 최적의 모습이 아닐 수 있습니다.**

큰 알림 아이콘 설정은 선택 사항이지만 권장됩니다.

#### 아이콘 강조 색상 지정

알림 아이콘 강조 색상은 `braze.xml`에서 재정의할 수 있습니다. 색상을 지정하지 않으면 기본 색상은 Lollipop이 시스템 알림에 사용하는 것과 동일한 회색입니다.

```xml
<integer name="com_braze_default_notification_accent_color">0xFFf33e3e</integer>
```

선택적으로 색상 참조를 사용할 수도 있습니다:

```xml
<color name="com_braze_default_notification_accent_color">@color/my_color_here</color>
```

### 4단계: 딥링크 추가

#### 자동 딥링크 열기 활성화

푸시 알림을 클릭할 때 Braze가 앱과 딥링크를 자동으로 열도록 하려면 `braze.xml`에서 `com_braze_handle_push_deep_links_automatically`를 `true`로 설정합니다:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

이 플래그는 [런타임 구성]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)을 통해서도 설정할 수 있습니다:

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

딥링크를 커스텀 처리하려면 Braze에서 푸시 수신 및 열기 의도를 수신 대기하는 푸시 콜백을 만들어야 합니다. 자세한 내용은 [푸시 이벤트에 대한 콜백 사용]({{site.baseurl}}/developer_guide/push_notifications/customization#android_using-a-callback-for-push-events)을 참조하세요.

## 포그라운드 알림 처리

기본적으로 Android에서 앱이 포그라운드에 있을 때 푸시 알림이 도착하면 시스템이 자동으로 표시합니다. Braze가 푸시 알림 페이로드를 처리하도록 하려면(분석 추적, 딥링크 처리 및 커스텀 처리를 위해) `FirebaseMessagingService.onMessageReceived` 메서드 내에서 수신 푸시 데이터를 Braze로 라우팅하세요.

### 작동 방식

`BrazeFirebaseMessagingService.handleBrazeRemoteMessage`를 호출하면 Braze는 페이로드가 Braze 푸시 알림인지 판단하고, 해당하는 경우 `NotificationManagerCompat` 메서드를 통해 알림을 생성 및 표시합니다. iOS와 달리 Android는 앱이 포그라운드에 있든 백그라운드에 있든 상관없이 알림을 표시합니다.

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

자세한 내용은 Braze Android SDK 리포지토리의 [Firebase 통합 샘플](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/java/com/braze/firebasepush/FirebaseMessagingService.kt)을 참조하세요.

### 포그라운드 동작 커스텀

시스템 알림을 억제하거나 대신 인앱 UI를 표시하는 등 커스텀 포그라운드 동작을 원한다면 다음과 같이 할 수 있습니다:

- `subscribeToPushNotificationEvents`를 사용하여 푸시 이벤트에 반응하고 `BrazeNotificationUtils.routeUserWithNotificationOpenedIntent` 메서드로 딥링크를 처리합니다. 자세한 내용은 [Firebase 푸시 샘플](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/java/com/braze/firebasepush/FirebaseApplication.kt)을 참조하세요.
- 커스텀 `IBrazeNotificationFactory`를 사용하여 자체 알림을 구축하고 게시하거나, 처리 경로에서 `notificationManager.notify`를 호출하지 않음으로써 알림을 억제할 수 있습니다.

알림 커스텀에 대한 자세한 내용은 [커스텀 알림 팩토리]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#custom-notification-factory)를 참조하세요.

#### 커스텀 딥링크 만들기

앱에 아직 딥링크를 추가하지 않았다면 [Android 개발자 설명서](http://developer.android.com/training/app-indexing/deep-linking.html)의 딥링킹 관련 지침을 따르세요. 딥링크 개념에 대한 자세한 내용은 [FAQ 문서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)를 참조하세요.

#### 딥링크 추가

Braze 대시보드는 푸시 알림 캠페인과 캔버스에서 알림을 클릭할 때 열릴 딥링크 또는 웹 URL 설정을 지원합니다.

![Braze 대시보드의 '클릭 시 동작' 설정에서 드롭다운 메뉴에서 '앱으로의 딥링크'가 선택된 상태.]({% image_buster /assets/img_archive/deep_link_click_action.png %} "Deep Link Click Action")

#### 백 스택 동작 커스텀

기본적으로 Android SDK는 푸시 딥링크를 따라갈 때 호스트 앱의 기본 런처 액티비티를 백 스택에 배치합니다. Braze를 사용하면 기본 런처 액티비티 대신 백 스택에서 열릴 커스텀 액티비티를 설정하거나 백 스택을 완전히 비활성화할 수 있습니다.

예를 들어 [런타임 구성]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)을 사용하여 `YourMainActivity`라는 액티비티를 백 스택 액티비티로 설정하려면:

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

`braze.xml`에 해당하는 구성을 참조하세요. 클래스 이름은 `Class.forName()`에서 반환하는 것과 동일해야 합니다.

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">true</bool>
<string name="com_braze_push_deep_link_back_stack_activity_class_name">your.package.name.YourMainActivity</string>
```

### 5단계: 알림 채널 정의

Braze Android SDK는 [Android 알림 채널](https://developer.android.com/preview/features/notification-channels.html)을 지원합니다. Braze 알림에 알림 채널 ID가 포함되어 있지 않거나 유효하지 않은 채널 ID가 포함되어 있는 경우, Braze는 SDK에 정의된 기본 알림 채널로 알림을 표시합니다. Braze 사용자는 플랫폼 내에서 [Android 알림 채널]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/)을 사용하여 알림을 그룹화합니다.

기본 Braze 알림 채널의 사용자 대면 이름을 설정하려면 [`BrazeConfig.setDefaultNotificationChannelName()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html)을 사용합니다.

기본 Braze 알림 채널의 사용자 대면 설명을 설정하려면 [`BrazeConfig.setDefaultNotificationChannelDescription()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html)을 사용합니다.

`notification_channel` 필드를 포함하도록 [Android 푸시 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/android_object/) 매개변수를 사용하여 모든 API 캠페인을 업데이트합니다. 이 필드를 지정하지 않으면 Braze는 [대시보드 대체]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel) 채널 ID와 함께 알림 페이로드를 전송합니다.

기본 알림 채널 외에는 Braze에서 어떠한 채널도 생성하지 않습니다. 다른 모든 채널은 호스트 앱에서 프로그래밍 방식으로 정의한 다음 Braze 대시보드에 입력해야 합니다.

기본 채널 이름과 설명은 `braze.xml`에서도 구성할 수 있습니다.

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### 6단계: 알림 표시 및 분석 테스트

#### 표시 테스트

이 시점에서 Braze에서 보낸 알림을 볼 수 있어야 합니다. 이를 테스트하려면 Braze 대시보드의 **캠페인** 페이지로 이동하여 **푸시 알림** 캠페인을 생성합니다. **Android 푸시**를 선택하고 메시지를 디자인합니다. 그런 다음 작성기에서 눈 아이콘을 클릭하여 테스트 발신자를 가져옵니다. 현재 사용자의 사용자 ID 또는 이메일 주소를 입력하고 **테스트 보내기**를 클릭합니다. 기기에 푸시가 표시됩니다.

![Braze 대시보드의 푸시 알림 캠페인 '테스트' 탭.]({% image_buster /assets/img_archive/android_push_test.png %} "Android Push Test")

푸시 표시와 관련된 문제는 [문제 해결 가이드]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)를 참조하세요.

#### 분석 테스트

이 시점에서 푸시 알림 열기에 대한 분석 로깅도 작동해야 합니다. 알림이 도착했을 때 클릭하면 캠페인 결과 페이지의 **직접 열기** 수가 1씩 증가합니다. 푸시 분석에 대한 자세한 내용은 [푸시 보고]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) 문서를 참조하세요.

푸시 분석과 관련된 문제는 [문제 해결 가이드]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)를 참조하세요.

#### 명령줄에서 테스트

명령줄 인터페이스를 통해 인앱 및 푸시 알림을 테스트하려면 터미널에서 cURL 및 [메시징 API]({{site.baseurl}}/api/endpoints/messaging/)를 사용하여 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

- `YOUR_API_KEY` (**설정** > **API 키**로 이동합니다.)
- `YOUR_EXTERNAL_USER_ID` (**사용자 검색** 페이지에서 프로필을 검색합니다.)
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

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

이 예에서는 `US-01` 인스턴스를 사용합니다. 이 인스턴스를 사용하지 않는 경우 `US-01` 엔드포인트를 [사용자의 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)로 바꾸세요.

## 대화 푸시 알림

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

[사람과 대화 이니셔티브](https://developer.android.com/guide/topics/ui/conversations)는 휴대폰의 시스템 표면에서 사람과 대화를 더 부각시키는 것을 목표로 하는 다년간의 Android 이니셔티브입니다. 이 우선순위는 모든 인구 통계에 걸쳐 대부분의 Android 사용자에게 다른 사람들과의 소통 및 상호작용이 여전히 가장 가치 있고 중요한 기능 영역이라는 사실에 기반합니다.

### 사용 요구 사항

- 이 알림 유형에는 Braze Android SDK v15.0.0 이상 및 Android 11 이상 기기가 필요합니다. 
- 지원되지 않는 기기 또는 SDK에서는 표준 푸시 알림으로 대체됩니다.

이 기능은 Braze REST API를 통해서만 사용할 수 있습니다. 자세한 내용은 [Android 푸시 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object)를 참조하세요.

## FCM 할당량 초과 오류

Firebase 클라우드 메시징(FCM)의 한도를 초과하면 Google에서 "할당량 초과" 오류를 반환합니다. FCM의 기본 제한은 분당 600,000건의 요청입니다. Braze는 Google이 권장하는 모범 사례에 따라 재전송을 시도합니다. 그러나 이러한 오류가 대량으로 발생하면 전송 시간이 수 분간 지연될 수 있습니다. 잠재적 영향을 완화하기 위해 Braze는 사용량 제한 초과 알림과 오류를 방지하기 위한 조치 방법을 안내해 드립니다.

현재 한도를 확인하려면 **Google Cloud Console** > **API 및 서비스** > **Firebase 클라우드 메시징 API** > **할당량 및 시스템 제한**으로 이동하거나 [FCM API 할당량 페이지](https://console.cloud.google.com/apis/api/fcm.googleapis.com/quotas)를 방문하세요.

### 모범 사례

이러한 오류 발생량을 낮게 유지하기 위해 다음 모범 사례를 권장합니다.

#### FCM에 사용량 제한 증가 요청

FCM에 대한 사용량 제한 증가를 요청하려면 [Firebase 지원팀](https://firebase.google.com/support)에 직접 문의하거나 다음 단계를 수행하세요:

1. [FCM API 할당량 페이지](https://console.cloud.google.com/apis/api/fcm.googleapis.com/quotas)로 이동합니다.
2. **분당 요청 전송** 할당량을 찾습니다.
3. **할당량 편집**을 선택합니다. 
4. 새 값을 입력하고 요청을 제출합니다.

#### 워크스페이스 사용량 제한 적용

Android 푸시 알림에 대한 워크스페이스 사용량 제한을 적용할 수 있습니다. 이를 통해 발신 메시지의 전달 속도를 조절할 수 있습니다. 자세한 내용은 [워크스페이스 메시징 사용량 제한]({{site.baseurl}}/user_guide/administrative/app_settings/messaging_rate_limits)을 참조하세요.