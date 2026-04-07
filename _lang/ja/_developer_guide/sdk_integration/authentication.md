---
page_order: 1.2
nav_title: 認証
article_title: Braze SDKの認証を設定する
description: "この参考記事では、SDK 認証と、Braze SDK でこの機能を有効にする方法について説明します。"
platform:
  - iOS
  - Android
  - Web
  
---

# SDK認証を設定する

> SDK 認証を使用すると、ログインしているユーザーの代わりに行われた SDK リクエストに対して（サーバー側で生成された）暗号証明を提供できます。

## 仕組み

アプリでこの機能を有効にした後、無効または欠落しているJSON Web Token（JWT）を含むリクエストを拒否するようにBrazeダッシュボードを設定できます。これには次のものが含まれます。

- カスタムイベント、属性、購入、セッションデータの送信
- Brazeワークスペースでの新規ユーザーの作成
- 標準ユーザープロファイル属性の更新
- メッセージの受信またはトリガー

認証されていないログインユーザーが、アプリのSDK APIキーを使って悪意のあるアクション（他のユーザーになりすますなど）を行うのを防げるようになります。

## 認証のセットアップ

### ステップ1:サーバーのセットアップ {#server-side-integration}

#### ステップ1.1：公開鍵と秘密鍵のペアを生成する {#generate-keys}

RSA256公開鍵/秘密鍵ペアを生成します。公開キーは最終的にBrazeのダッシュボードに追加されますが、秘密キーはサーバーに安全に保管する必要があります。

RS256 JWTアルゴリズムで使用する2048ビットのRSA鍵を推奨します。

{% alert warning %}
秘密キーは必ず_非公開_にしてください。アプリやWebサイトに秘密鍵を公開したり、ハードコードしたりしてはなりません。あなたの秘密キーを知っている人なら誰でも、あなたのアプリケーションに代わってユーザーになりすましたり、ユーザーを作成したりすることができます。
{% endalert %}

#### ステップ1.2：現在のユーザーのJSON Web Tokenを作成する {#create-jwt}

秘密キーが手に入ったら、サーバー側のアプリケーションはそれを使って、現在ログインしているユーザーのアプリまたはWebサイトにJWTを返す必要があります。

通常、このロジックは、アプリが通常現在のユーザーのプロファイルをリクエストする任意の場所に配置できます。たとえば、ログインエンドポイントや、アプリが現在のユーザープロファイルを更新する場所などです。

JWTを生成する際には、以下のフィールドが必要です：

**JWTヘッダー**

| フィールド | 必須 | 説明                         |
| ----- | -------- | ----------------------------------- |
| `alg` | はい  | サポートされているアルゴリズムは`RS256`です。 |
| `typ` | はい  | タイプは`JWT`と同じでなければなりません。        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**JWTペイロード**

| フィールド | 必須 | 説明                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | はい  | 「subject」は、`changeUser`の呼び出し時にBraze SDKに指定したユーザーIDと同じである必要があります。  |
| `exp` | はい | このトークンをいつ期限切れにするかの「有効期限」。                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
JSON Web Tokenについての詳細や、この署名プロセスを簡素化する多くのオープンソースライブラリを参照するには、[https://jwt.io](https://jwt.io)をチェックしてください。
{% endalert %}

### ステップ2:SDKの設定 {#sdk-integration}

この機能は以下の[SDKバージョン]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)から利用可能です：

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOS統合については、このページでBraze Swift SDKのステップを詳しく説明します。レガシーAppboyKit iOS SDKでの使用例については、[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m)と[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)を参照してください。
{% endalert %}

#### ステップ2.1:Braze SDKで認証を有効にする

この機能が有効な場合、Braze SDKは、Brazeサーバーに対して行われたネットワークリクエストに、現在のユーザーの最新の既知のJWTを追加します。

{% alert note %}
このオプションだけで初期化しても、Brazeダッシュボード内で[認証の適用を](#braze-dashboard)開始するまでは、データ収集には何の影響もないのでご心配なく。
{% endalert %}

{% tabs %}
{% tab Web %}
`initialize`を呼び出す際には、オプションの`enableSdkAuthentication`プロパティを`true`に設定します。
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
ネイティブSDKの初期化時に、SDK認証を有効にする必要があります。ネイティブのiOSおよびAndroidコードに以下の設定を追加してください：

**iOS (AppDelegate.swift)**

```swift
import BrazeKit
import braze_react_native_sdk

let configuration = Braze.Configuration(
  apiKey: "{YOUR-BRAZE-API-KEY}",
  endpoint: "{YOUR-BRAZE-ENDPOINT}"
)
configuration.api.sdkAuthentication = true
let braze = BrazeReactBridge.perform(
  #selector(BrazeReactBridge.initBraze(_:)),
  with: configuration
).takeUnretainedValue() as! Braze
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以下のステップに示すReact Native JavaScriptメソッドを使用できます。
{% endtab %}
{% tab Java %}
Brazeインスタンスを設定するときは、`setIsSdkAuthenticationEnabled`を`true`に設定します。
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

あるいは、braze.xmlに`<bool name="com_braze_sdk_authentication_enabled">true</bool>`を追加することもできます。
{% endtab %}
{% tab KOTLIN %}
Brazeインスタンスを設定するときは、`setIsSdkAuthenticationEnabled`を`true`に設定します。
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

あるいは、braze.xmlに`<bool name="com_braze_sdk_authentication_enabled">true</bool>`を追加することもできます。
{% endtab %}
{% tab Objective-C %}
SDK認証を有効にするには、Brazeインスタンスを初期化する前に、`BRZConfiguration`オブジェクトの`configuration.api.sdkAuthentication`プロパティを`YES`に設定します：

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
SDK認証を有効にするには、SDKを初期化する際に、`Braze.Configuration`オブジェクトの`configuration.api.sdkAuthentication`プロパティを`true`に設定します：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
現在、SDK認証は、iOSとAndroidのネイティブコードでSDKを初期化する際に有効にする必要があります。Flutter SDKでSDK認証を有効にするには、他のタブのiOSとAndroidの統合に従ってください。SDK認証を有効にした後、残りの機能をDartに統合することができます。
{% endtab %}
{% tab Flutter %}
ネイティブのiOSおよびAndroidコードにおいて、SDKの初期化の一環としてSDK認証を有効にする必要があります。ネイティブレイヤーで有効にすると、Flutter SDKのメソッドを使ってJWT署名を渡すことができます。

**iOS**

SDK認証を有効にするには、ネイティブiOSコードで`configuration.api.sdkAuthentication`プロパティを`true`に設定します：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以下のステップで示すFlutter SDKメソッドを使用できます。
{% endtab %}
{% tab Unity %}
ネイティブSDKの初期化時に、SDK認証を有効にする必要があります。ネイティブのiOSおよびAndroidコードに以下の設定を追加してください：

**iOS**

設定ファイルで`SDKAuthenticationEnabled`プロパティを`true`に設定します：

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以下のステップで示すUnity C#メソッドを使用できます。
{% endtab %}
{% tab Cordova %}
ネイティブSDKの初期化時に、SDK認証を有効にする必要があります。ネイティブのiOSおよびAndroidコードに以下の設定を追加してください：

**iOS**

SDK認証を有効にするには、`config.xml`で`enableSDKAuthentication`プロパティを`true`に設定します：

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以下のステップで示すCordova JavaScriptメソッドを使用できます。
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
ネイティブSDKの初期化時に、SDK認証を有効にする必要があります。iOSとAndroidではSDK認証を別々に設定します：

**iOS**

SDK認証を有効にするには、SDKを初期化する際に`configuration.Api.SdkAuthentication`プロパティを`true`に設定します：

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

SDK認証を有効にした後、以下のステップで示す.NET MAUIメソッドを使用できます。
{% endtab %}
{% tab Expo %}
Braze Expoプラグインを使用する際は、アプリ設定で`enableSdkAuthentication`プロパティを`true`に設定します。これにより、手動でのネイティブコードの変更を必要とせずに、ネイティブのiOSおよびAndroidレイヤーでSDK認証が自動的に設定されます。

**app.jsonあるいはapp.config.js**

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "enableSdkAuthentication": true
        }
      ]
    ]
  }
}
```

アプリ設定でSDK認証を有効にした後、React Nativeタブに表示されているReact Native JavaScriptメソッドを使用して、以下のステップを実行できます。

{% alert note %}
完全な実装例については、GitHub上の[Braze Expoプラグインサンプルアプリ](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

#### ステップ2.2:現在のユーザーのJWTを設定する

アプリがBrazeの`changeUser`メソッドを呼び出すたびに、[サーバー側で生成された](#braze-dashboard)JWTも指定します。

また、トークンが現在のユーザーのセッションの途中でリフレッシュされるように設定することもできます。

{% alert note %}
`changeUser`は、ユーザーIDが_実際に変更された_場合にのみ呼び出す必要があることに注意してください。ユーザーIDが変更されていない場合は、このメソッドを認証トークン（JWT）の更新手段として使用しないでください。
{% endalert %}

{% tabs %}
{% tab Web %}
[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)の呼び出し時にJWTを指定します：

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

[`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser)の呼び出し時にJWTを指定します：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)の呼び出し時にJWTを指定します：

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)の呼び出し時にJWTを指定します：

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))の呼び出し時にJWTを指定します：

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))の呼び出し時にJWTを指定します：

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)の呼び出し時にJWTを指定します：

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

`changeUser`の呼び出し時にJWTを指定します：

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

`ChangeUser`の呼び出し時にJWTを指定します：

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

`changeUser`の呼び出し時にJWTを指定します：

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

`ChangeUser`の呼び出し時にJWTを指定します：

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

Braze Expoプラグインを使用する際は、同じReact Native SDKメソッドを使います。`changeUser`の呼び出し時にJWTを指定します：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### ステップ2.3:無効なトークンのコールバック関数を登録する {#sdk-callback}

この機能が[必須](#enforcement-options)に設定されている場合、以下のシナリオでSDKリクエストがBrazeによって拒否されます：
- Braze APIが受信した時点でJWTの有効期限が切れていた
- JWTが空または欠落していた
- Brazeダッシュボードにアップロードした公開鍵でJWTの検証に失敗した

`subscribeToSdkAuthenticationFailures`を使用して、これらのいずれかの理由でSDKリクエストが失敗したときに通知を受け取るようにサブスクライブできます。コールバック関数には、関連する[`errorCode`](#error-codes)、エラーの`reason`、リクエストの`userId`（ユーザーは匿名にはなれません）、およびエラーを引き起こした認証トークン（JWT）を含むオブジェクトが渡されます。

失敗したリクエストは、アプリが新しい有効なJWTを提供するまで、定期的に再試行されます。そのユーザーがまだログインしている場合、このコールバックをサーバーに新しいJWTを要求する機会として使用し、この新しい有効なトークンをBraze SDKに提供することができます。

認証エラーが発生した場合は、エラー内の`userId`が現在ログイン中のユーザーと一致するか確認し、サーバーから新しい署名を取得してBraze SDKに提供してください。これらのエラーを監視サービスやエラーレポートサービスに記録することもできます。

{% alert tip %}
これらのコールバックメソッドは、独自の監視サービスやエラーログサービスを追加して、Brazeリクエストが拒否される頻度を追跡するのに最適な場所です。
{% endalert %}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToSdkAuthenticationFailures((error) => {
  console.error("SDK authentication failed:", error);
  console.log("Error code:", error.errorCode);
  console.log("User ID:", error.userId);
  // Note: Do not log error.signature as it contains sensitive authentication credentials
  
  // Verify the error.userId matches the currently logged-in user
  // Fetch a new token from your server and set it
  fetchNewSignature(error.userId).then((newSignature) => {
    braze.setSdkAuthenticationSignature(newSignature);
  });
});
```
{% endtab %}
{% tab React Native %}
```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("Invalid SDK Authentication Token.");
  final newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Flutter %}
```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();

braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.");
  
  String newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Unity %}
**iOS**

ネイティブのiOS実装でSDK認証デリゲートを設定します：

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Debug.Log("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    BrazeBinding.SetSdkAuthenticationSignature(newSignature);
  }
}
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.subscribeToSdkAuthenticationFailures((error) => {
  console.log(`SDK Authentication for ${error.user_id} failed with error code ${error.error_code}.`);
  
  const newSignature = getNewTokenSomehow(error);
  BrazePlugin.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
**iOS**

`Braze`インスタンスにSDK認証デリゲートを設定します：

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public override void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Console.WriteLine("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    Braze.SharedInstance?.SetSDKAuthenticationSignature(newSignature);
  }
}

// Set the delegate during initialization
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
braze.SdkAuthDelegate = new SdkAuthDelegate();
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Expo %}
Braze Expoプラグインを使用する際は、同じReact Native SDKメソッドを使います：

```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% endtabs %}

### ステップ3:ダッシュボードで認証を有効にする {#braze-dashboard}

次に、前に設定したアプリのBrazeダッシュボードで認証を有効にできます。

BrazeダッシュボードでアプリのSDK認証設定が**必須**に設定されていない限り、SDKリクエストは認証なしで通常どおり処理され続けることに注意してください。

統合に何か問題が発生した場合（例えば、アプリがSDKにトークンを不正に渡している、またはサーバーが無効なトークンを生成している）、Brazeダッシュボードでこの機能を無効にすると、データは検証なしで通常通り流れるようになります。

#### 適用オプション {#enforcement-options}

ダッシュボードの**設定の管理**ページでは、各アプリに3つのSDK認証ステートがあり、Brazeがどのようにリクエストを検証するかを制御します。

| 設定| 説明|
| ------ | ---------- |
| **無効** | Brazeは、ユーザーに提供されたJWTを検証しません。（デフォルト設定）|
| **オプション** | Brazeは、ログインしているユーザーのリクエストを検証しますが、無効なリクエストは拒否しません。 |
| **必須** | Brazeは、ログインしているユーザーのリクエストを検証し、無効なJWTは拒否します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

**オプション**設定は、この機能がアプリのSDKトラフィックに与える潜在的な影響を監視するのに便利な方法です。

無効なJWTは**オプション**と**必須**の両方の状態で報告されますが、**必須**状態でのみSDKリクエストが拒否され、アプリは再試行して新しいJWTをリクエストします。

## 公開鍵を管理する {#key-management}

### 公開鍵を追加する

アプリごとに、プライマリ、セカンダリ、ターシャリの最大3つの公開キーを追加できます。必要に応じて、同じキーを複数のアプリに追加することもできます。公開鍵を追加するには：

1. Brazeのダッシュボードに行き、**設定** > **アプリ設定**を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. **SDK認証**で、**公開キーを追加**を選択します。
4. オプションの説明を入力し、公開キーを貼り付け、**公開キーを追加**を選択します。

### 新しいプライマリキーを割り当てる

セカンダリキーまたはターシャリキーを新しいプライマリキーとして割り当てるには：

1. Brazeのダッシュボードに行き、**設定** > **アプリ設定**を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. **SDK認証**でキーを選択し、**管理** > **プライマリキーに設定**を選択します。

### キーを削除する

プライマリキーを削除するには、まず[新たなプライマリキーを割り当て](#assign-a-new-primary-key)、それからキーを削除します。非プライマリキーを削除するには：

1. Brazeのダッシュボードに行き、**設定** > **アプリ設定**を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. **SDK認証**でプライマリキー以外のキーを選択し、**管理** > **公開キーを削除**を選択します。

## 分析 {#analytics}

各アプリには、この機能が**オプション**状態と**必須**状態にある間に収集されたSDK認証エラーの内訳が表示されます。

データはリアルタイムで入手でき、チャート上のポイントにカーソルを合わせると、指定した日付のエラーの内訳を見ることができます。

![認証エラーの発生件数を示すグラフ。また、エラーの総数、エラーの種類、調整可能な日付範囲も表示されます。]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## エラーコード {#error-codes}

| エラーコード| エラーの理由 | 説明 | 解決手順 |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | Brazeを使用する場合、有効期限は必須フィールドです。| JWT生成ロジックに`exp`または有効期限フィールドを追加してください。 |
| 20 | `DECODING_ERROR` | 公開鍵が一致しないか、一般的な捕捉不能エラーが発生しました。| JWTをJWTテストツールにコピーして、JWTが無効な形式である理由を診断してください。 |
| 21 | `SUBJECT_MISMATCH` | 期待されるサブジェクトと実際のサブジェクトが一致しません。| `sub`フィールドは、SDKの`changeUser`メソッドに渡されたユーザーIDと同じである必要があります。 |
| 22 | `EXPIRED` | 提供されたトークンの有効期限が切れています。| 有効期限を延長するか、トークンが期限切れになる前に定期的に更新してください。 |
| 23 | `INVALID_PAYLOAD` | トークンのペイロードが無効です。| JWTをJWTテストツールにコピーして、JWTが無効な形式である理由を診断してください。 |
| 24 | `INCORRECT_ALGORITHM` | トークンのアルゴリズムはサポートされていません。| JWTを`RS256`暗号化方式に変更してください。その他のタイプはサポートされていません。 |
| 25 | `PUBLIC_KEY_ERROR` | 公開鍵が適切な形式に変換できませんでした。| JWTをJWTテストツールにコピーして、JWTが無効な形式である理由を診断してください。 |
| 26 | `MISSING_TOKEN` | リクエストにトークンが指定されていません。| `changeUser(id, token)`を呼び出す際にトークンを渡していることを確認し、そのトークンが空白でないことを確認してください。|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | 提供されたトークンに一致する公開鍵がありませんでした。| JWTで使用されている秘密キーは、アプリに設定されている公開キーのいずれとも一致しません。このAPIキーに対応するワークスペース内の正しいアプリに公開キーを追加したことを確認してください。|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | リクエストのペイロード内のユーザーIDがすべて、要求通りに一致しているわけではありません。| これは予期しないエラーであり、不正なペイロードを引き起こす可能性があります。サポートチケットを開いてお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## よくある質問（FAQ） {#faq}

#### この機能はすべてのアプリで同時に有効にする必要がありますか？ {#faq-app-by-app}

いいえ、この機能は特定のアプリに対して有効にすることができ、すべてのアプリで一度に使用する必要はありません。

#### アプリの古いバージョンを使っているユーザーはどうなりますか？ {#faq-sdk-backward-compatibility}

この機能を適用し始めると、古いバージョンのアプリによるリクエストはBrazeによって拒否され、SDKによって再試行されます。ユーザーがアプリをサポートされたバージョンにアップグレードすると、キューに入れられたリクエストは再び受け入れられるようになります。

可能であれば、他の必須アップグレードと同様に、ユーザーにアップグレードを勧めてください。あるいは、許容できる割合のユーザーがアップグレードしたことを確認するまで、この機能を[オプション](#enforcement-options)にしておくこともできます。

#### JWTを生成するときには、どのような有効期限を使用する必要がありますか？ {#faq-expiration}

平均セッション期間、セッションCookie/トークンの有効期限、またはアプリケーションが現在のユーザープロファイルを更新する頻度のうち、高い方の値を使用することをお勧めします。

#### ユーザーのセッションの途中でJWTの有効期限が切れた場合はどうなりますか？ {#faq-jwt-expiration}

ユーザーのトークンがセッション中に期限切れになると、SDKは[コールバック関数](#sdk-callback)を呼び出して、Brazeにデータを送信し続けるために新しいJWTが必要であることをアプリに知らせます。

#### サーバー側の統合が壊れ、JWTを作成できなくなった場合はどうなりますか？ {#faq-server-downtime}

サーバーがJWTを提供できない場合、または統合に問題がある場合は、Brazeダッシュボードでいつでも機能を無効にできます。

一度無効にすると、保留中の失敗したSDKリクエストは最終的にSDKによって再試行され、Brazeによって受け入れられます。

#### なぜこの機能では、共有シークレットではなく公開キー/秘密キーを使うのでしょうか？ {#faq-shared-secrets}

共有シークレットを使う場合、Brazeのダッシュボードページなど、その共有シークレットにアクセスできる人なら誰でも、トークンを生成してエンドユーザーになりすますことができます。

代わりに、公開キーと秘密キーを使用します。これにより、Brazeの従業員でさえ（ましてや御社のユーザーは言うまでもなく）あなたの秘密キーにアクセスできません。

#### 拒否されたリクエストはどのように再試行されますか？ {#faq-retry-logic}

認証エラーが原因でリクエストが拒否されると、SDKはユーザーのJWTを更新するために使用されるコールバックを呼び出します。

リクエストは指数バックオフアプローチを使用して定期的に再試行されます。50回連続で失敗すると、次のセッション開始まで再試行は一時停止されます。各SDKには、手動でデータフラッシュをリクエストするメソッドもあります。

#### 匿名ユーザーに対してSDK認証は使えますか？ {#faq-anonymous-users}

いいえ。SDK認証はWebサイトが誰かのIDを主張することで機能するため、識別済みのユーザーにのみ適用されます。匿名ユーザーの場合、主張するIDがありません。

適用は`changeUser`が呼び出された後に開始されます。ユーザーが識別される前（例えば、サインアップ前に匿名で閲覧している間）は、SDKはJWTなしでBrazeにデータを送信できます。`changeUser`が呼び出された後、その識別済みプロファイルに対するリクエストには有効なJWTが必要になります。

つまり、一般的なユーザージャーニーは次のようになります：

1. ユーザーがWebサイトにアクセスするか、アプリを匿名で開きます。BrazeはJWTなしでこのアクティビティを収集します。
2. ユーザーがサインアップまたはログインし、アプリが`external_id`を指定して`changeUser`を呼び出します。
3. Brazeはそのユーザーのアクティビティの収集を続け、その識別済みプロファイルに対するリクエストにはSDK認証が適用されます。

#### SDK認証はユーザーエイリアスで機能しますか？ {#faq-aliases}

いいえ。SDK認証には`external_id`が必要です。`braze_id`または`alias_id`のみが利用可能な場合は設定できないため、エイリアスのみのプロファイルではSDK認証を使用できません。

#### SDK認証を有効にすると、未認証のアクティビティ収集がブロックされますか？ {#faq-unauthenticated-collection}

いいえ。SDK認証は正当な匿名アクティビティの収集をブロックしません。`changeUser`でプロファイルが識別された後にのみ適用されます。