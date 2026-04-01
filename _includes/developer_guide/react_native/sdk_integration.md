## About the React Native Braze SDK

Integrating the React Native Braze SDK provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with one codebase.

## New Architecture compatibility

The following minimum SDK version is compatible with all apps using [React Native's New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page):

{% sdk_min_versions reactnative:2.0.1 %}

Starting with SDK version 6.0.0, Braze uses a React Native Turbo Module, which is compatible with both the New Architecture and legacy bridge architecture&#8212;meaning no additional setup is required.

{% alert warning %}
If your iOS app conforms to `RCTAppDelegate` and follows our previous `AppDelegate` setup, review the samples in [Complete native setup](#reactnative_step-2-complete-native-setup) to prevent crashes when subscribing to events in the Turbo Module.
{% endalert %}

## Integrating the React Native SDK

### Prerequisites

To integrate the SDK, React Native version 0.71 or later is required. For the full list of supported versions, see our [React Native SDK GitHub repository](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

### Step 1: Integrate the Braze library

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

<a id="step-2-choose-a-setup-option"></a>
<a id="reactnative_step-2-complete-native-setup"></a>
### Step 2: Complete native setup

If your app uses Expo, see [Using the Expo plugin](#reactnative-using-the-expo-plugin). If your app uses pure React Native, see [Using React Native CLI](#reactnative-using-react-native-cli).
Choose one setup method in each version tab: Expo plugin or React Native CLI.

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### Method 1: Using the Expo plugin {#reactnative-using-the-expo-plugin}

##### 2.1 Install the Braze Expo plugin

Ensure that your version of the Braze Expo plugin is at least 4.1.0. For the full list of supported versions, see the [Braze Expo plugin repository](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

The following code snippet shows the command to install the Braze Expo plugin:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Add the plugin to your app.json

In your `app.json`, add the Braze Expo plugin. The API key and endpoint are no longer set here. Provide them at runtime via `Braze.initialize()` from JavaScript. Add the following optional configuration parameters based on your implementation needs:

| Method                                        | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | iOS only. Whether to use Braze to handle push notifications on iOS.                       |
| `enableFirebaseCloudMessaging`                | boolean | Android only. Whether to use Firebase Cloud Messaging for push notifications.             |
| `firebaseCloudMessagingSenderId`              | string  | Android only. Your Firebase Cloud Messaging sender ID.                                    |
| `sessionTimeout`                              | integer | The Braze session timeout for your application in seconds.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Whether to enable the [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature.      |
| `logLevel`                                    | integer | The log level for your application. The default log level is 8 and minimally logs info. To enable verbose logging for debugging, use log level 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | The minimum time interval in seconds between triggers. Defaults to 30 seconds.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Whether automatic location collection is enabled (if the user permits).                                                                                  |
| `enableGeofence`                              | boolean | Whether geofences are enabled.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Whether geofence requests should be made automatically.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOS only. Whether a modal in-app message is dismissed when the user clicks outside of the in-app message.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Android only. Whether the Braze SDK should automatically handle push deep links.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android only. Sets whether the text content in a push notification should be interpreted and rendered as HTML using `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Android only. Sets the Android notification accent color.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Android only. Sets the Android notification large icon.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Android only. Sets the Android notification small icon.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOS only. Whether the user should automatically be prompted for push permissions on app launch.                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOS only. Whether to enable rich push features for iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOS only. Whether to enable Braze Push Stories for iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOS only. The app group used for iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOS only. Whether the device ID uses a randomly generated UUID.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOS only. Specifies if the SDK should automatically recognize and forward universal links to the system methods (default: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

The following code snippet shows an example `app.json` configuration:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ]
    ]
  }
}
```

###### Configuring Android push notification icons {#android-push-icons}

When using `androidNotificationLargeIcon` and `androidNotificationSmallIcon`, follow these best practices for proper icon display:

**Icon placement and format**

To use custom push notification icons with the Braze Expo plugin:

1. Create your icon files following the Icon requirements listed below.
2. Place them in your project's Android native directories at `android/app/src/main/res/drawable-<density>/`.
   For example, use `android/app/src/main/res/drawable-mdpi/` and `android/app/src/main/res/drawable-hdpi/`.
3. Alternatively, if you're managing assets in your React Native directory, you can use Expo's [app.json icon configuration](https://docs.expo.dev/versions/latest/config/app/#icon) or create an [Expo config plugin](https://docs.expo.dev/config-plugins/introduction/) to copy the icons to the Android drawable folders during prebuild.

The Braze Expo plugin references these icons using Android's drawable resource system.

**Icon requirements**

- **Small icon:** Must be a white silhouette on a transparent background (this is an Android platform requirement)
- **Large icon:** Can be a full-color image.
- **Format:** PNG format is recommended.
- **Naming:** Use lowercase letters, numbers, and underscores only (for example, `my_large_icon.png`)

**Configuration in app.json**

The following code snippet shows how to reference Android notification icons in `app.json` using the `@drawable/` prefix:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Do not use relative file paths (such as `src/assets/images/icon.png`) or include the file extension when referencing icons. The Expo plugin requires the `@drawable/` prefix to properly locate the icons in the Android native folders after the prebuild process.
{% endalert %}

**How it works**

The Braze Expo plugin references your icon files from the Android `drawable` directories. When you run `npx expo prebuild`, Expo generates the native Android project structure. Your icons must be present in the Android `drawable` folders (either placed manually or copied through a config plugin) before the build process. The plugin then configures the Braze SDK to use these drawable resources by their names (without path or extension), which is why the `@drawable/` prefix is required in your configuration.

For more information on Android notification icons, see [Android's notification icon guidelines](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Build and run your application

Prebuilding your application generates the native files necessary for the Braze Expo plugin to work.

The following code snippet shows the command to prebuild your application:

```bash
npx expo prebuild
```

Run your application as specified in the [Expo docs](https://docs.expo.dev/workflow/customizing/). If you make changes to the configuration options, prebuild and run the application again.

#### Method 2: Using React Native CLI {#reactnative-using-react-native-cli}

##### Set up Android

**2.1 Add the Kotlin Gradle plugin**

The following code snippet shows how to add the Kotlin Gradle plugin in your top-level project `build.gradle` under `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

This adds Kotlin to your project.

**2.2 Configure the Braze SDK**

Create a `braze.xml` file in your project's `res/values` folder. The API key and endpoint are provided at runtime from JavaScript, so they are not required in this file. The following code snippet shows how to enable delayed initialization with `com_braze_enable_delayed_initialization`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
You can still add other native configuration values to `braze.xml` (such as push, session timeout, and logging settings). These are applied automatically when `Braze.initialize()` is called from JavaScript.
{% endalert %}

The following code snippet shows the required permissions for your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
On Braze Android SDK version 12.2.0 or later, you can automatically pull in the android-sdk-location library by setting `importBrazeLocationLibrary=true` in your `gradle.properties` file.
{% endalert %}

**2.3 Implement user session tracking**

The calls to `openSession()` and `closeSession()` are handled automatically.
The following code snippet shows what to add to the `onCreate()` method of your `MainApplication` class:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4 Handle intent updates**

If your MainActivity has `android:launchMode` set to `singleTask`, the following code snippet shows what to add to your `MainActivity` class:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Set up iOS

**2.5 (Optional) Configure Podfile for dynamic XCFrameworks**

To import certain Braze libraries, such as BrazeUI, into an Objective-C++ file, you must use the `#import` syntax. Starting in version `7.4.0` of the Braze Swift SDK, binaries have an [optional distribution channel as dynamic XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), which are compatible with this syntax.

If you'd like to use this distribution channel, manually override the CocoaPods source locations in your Podfile. Reference the sample below and replace `{your-version}` with the relevant version you wish to import:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Install pods**

Since React Native automatically links the libraries to the native platform, you can install the SDK with the help of CocoaPods.

The following code snippet shows how to install pods from the root folder of the project:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Configure the Braze SDK**

Use `BrazeReactInitializer.configure` in your `AppDelegate` to register native configuration. The closures you provide are stored and applied later when `Braze.initialize(apiKey, endpoint)` is called from JavaScript.

{% subtabs local %}
{% subtab SWIFT %}

The following code snippet shows how to import the Braze SDK at the top of the `AppDelegate.swift` file:

```swift
import BrazeKit
import braze_react_native_sdk
```

In the `application(_:didFinishLaunchingWithOptions:)` method, register your native configuration using `BrazeReactInitializer.configure`. Do not set the API key or endpoint here&#8212;they are provided from JavaScript via `Braze.initialize()`.

- **`configure` closure**: Receives a `Braze.Configuration` and lets you set native configuration properties (logging, push, sessions, and more).
- **`postInitialization` closure** _(optional)_: Receives the live `Braze` instance after creation, for setup that requires the instance (for example, storing a reference or setting delegates).

The following code snippet shows an example `AppDelegate.swift` implementation that uses `BrazeReactInitializer.configure`:

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    BrazeReactInitializer.configure { configuration in
      configuration.logger.level = .info
      configuration.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup

    return true
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

The following code snippet shows how to import the Braze SDK at the top of the `AppDelegate.m` file:

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

In the `application:didFinishLaunchingWithOptions:` method, register your native configuration using `BrazeReactInitializer`. Do not set the API key or endpoint here&#8212;they are provided from JavaScript via `Braze.initialize()`.

The following code snippet shows an example `AppDelegate.m` implementation that uses `BrazeReactInitializer`:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazeReactInitializer configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  } postInitialization:^(Braze *braze) {
    // Store the Braze instance for later use.
  }];

  /* Other configuration */

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazeReactInitializer.configure()` only stores your configuration. No Braze instance exists until `Braze.initialize()` is called from JavaScript, so do not call any Braze SDK methods in the AppDelegate after `configure()`.
When you call `Braze.initialize()` again, the same `configure` and `postInitialization` blocks are applied to the new Braze instance.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 and earlier %}

#### Method 1: Using the Expo plugin

##### Step 2.1: Install the Braze Expo plugin

Ensure that your version of the Braze React Native SDK is at least 1.37.0. For the full list of supported versions, see the [Braze React Native repository](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

The following code snippet shows the command to install the Braze Expo plugin:

```bash
npx expo install @braze/expo-plugin
```

##### Step 2.2: Add the plugin to your app.json

In your `app.json`, add the Braze Expo plugin. You can provide the following configuration options:

| Method                                        | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Required. The [API key]({{site.baseurl}}/api/identifier_types/) for your Android application, located in your Braze dashboard under **Manage Settings**. |
| `iosApiKey`                                   | string  | Required. The [API key]({{site.baseurl}}/api/identifier_types/) for your iOS application, located in your Braze dashboard under **Manage Settings**.     |
| `baseUrl`                                     | string  | Required. The [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application, located in your Braze dashboard under **Manage Settings**.    |
| `enableBrazeIosPush`                          | boolean | iOS only. Whether to use Braze to handle push notifications on iOS. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Android only. Whether to use Firebase Cloud Messaging for push notifications. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Android only. Your Firebase Cloud Messaging sender ID. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | integer | The Braze session timeout for your application in seconds.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Whether to enable the [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature.      |
| `logLevel`                                    | integer | The log level for your application. The default log level is 8 and minimally logs info. To enable verbose logging for debugging, use log level 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | The minimum time interval in seconds between triggers. Defaults to 30 seconds.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Whether automatic location collection is enabled (if the user permits).                                                                                  |
| `enableGeofence`                              | boolean | Whether geofences are enabled.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Whether geofence requests should be made automatically.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOS only. Whether a modal in-app message is dismissed when the user clicks outside of the in-app message.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Android only. Whether the Braze SDK should automatically handle push deep links.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android only. Sets whether the text content in a push notification should be interpreted and rendered as HTML using `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Android only. Sets the Android notification accent color.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Android only. Sets the Android notification large icon.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Android only. Sets the Android notification small icon.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOS only. Whether the user should automatically be prompted for push permissions on app launch.                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOS only. Whether to enable rich push features for iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOS only. Whether to enable Braze Push Stories for iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOS only. The app group used for iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOS only. Whether the device ID will use a randomly generated UUID.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOS only. Specifies if the SDK should automatically recognize and forward universal links to the system methods (default: `false`). When enabled, the SDK will automatically forward universal links to the system methods defined in [Supporting universal links in your app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introduced in React Native SDK v11.1.0 and Expo Plugin v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

The following code snippet shows an example `app.json` configuration:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

###### Configuring Android push notification icons

When using `androidNotificationLargeIcon` and `androidNotificationSmallIcon`, follow these best practices for proper icon display:

**Icon placement and format**

To use custom push notification icons with the Braze Expo plugin:

1. Create your icon files following the Icon requirements listed below.
2. Place them in your project's Android native directories at `android/app/src/main/res/drawable-<density>/` (for example, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/`, or similar.)
3. Alternatively, if you're managing assets in your React Native directory, you can use Expo's [app.json icon configuration](https://docs.expo.dev/versions/latest/config/app/#icon) or create an [Expo config plugin](https://docs.expo.dev/config-plugins/introduction/) to copy the icons to the Android drawable folders during prebuild.

The Braze Expo plugin references these icons using Android's drawable resource system.

**Icon requirements**

- **Small icon:** Must be a white silhouette on a transparent background (this is an Android platform requirement)
- **Large icon:** Can be a full-color image.
- **Format:** PNG format is recommended.
- **Naming:** Use lowercase letters, numbers, and underscores only (for example, `my_large_icon.png`)

**Configuration in app.json**

The following code snippet shows how to reference Android notification icons in `app.json` using the `@drawable/` prefix:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Do not use relative file paths (such as `src/assets/images/icon.png`) or include the file extension when referencing icons. The Expo plugin requires the `@drawable/` prefix to properly locate the icons in the Android native folders after the prebuild process.
{% endalert %}

**How it works**

The Braze Expo plugin references your icon files from the Android `drawable` directories. When you run `npx expo prebuild`, Expo generates the native Android project structure. Your icons must be present in the Android `drawable` folders (either placed manually or copied through a config plugin) before the build process. The plugin then configures the Braze SDK to use these drawable resources by their names (without path or extension), which is why the `@drawable/` prefix is required in your configuration.

For more information on Android notification icons, see [Android's notification icon guidelines](https://developer.android.com/develop/ui/views/notifications#icon).

##### Step 2.3: Build and run your application

Prebuilding your application generates the native files necessary for the Braze Expo plugin to work.

The following code snippet shows the command to prebuild your application:

```bash
npx expo prebuild
```

Run your application as specified in the [Expo docs](https://docs.expo.dev/workflow/customizing/). Keep in mind, if you make any changes to the configuration options, you'll be required to prebuild and run the application again.

#### Method 2: Using React Native CLI

##### Set up Android

**Step 2.1: Add the Kotlin Gradle plugin**

The following code snippet shows how to add the Kotlin Gradle plugin in your top-level project `build.gradle` under `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

This adds Kotlin to your project.

**Step 2.2: Configure the Braze SDK**

To connect to Braze servers, create a `braze.xml` file in your project's `res/values` folder. The following code snippet shows an example `braze.xml` configuration. Replace the API [key]({{site.baseurl}}/api/identifier_types/) and [endpoint]({{site.baseurl}}/api/basics/#endpoints) with your values:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

The following code snippet shows the required permissions for your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
On Braze Android SDK version 12.2.0 or later, you can automatically pull in the android-sdk-location library by setting `importBrazeLocationLibrary=true` in your `gradle.properties` file.
{% endalert %}

**Step 2.3: Implement user session tracking**

The calls to `openSession()` and `closeSession()` are handled automatically.
The following code snippet shows what to add to the `onCreate()` method of your `MainApplication` class:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**Step 2.4: Handle intent updates**

If your MainActivity has `android:launchMode` set to `singleTask`, the following code snippet shows what to add to your `MainActivity` class:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Set up iOS

**Step 2.5: (Optional) Configure Podfile for dynamic XCFrameworks**

To import certain Braze libraries, such as BrazeUI, into an Objective-C++ file, you must use the `#import` syntax. Starting in version `7.4.0` of the Braze Swift SDK, binaries have an [optional distribution channel as dynamic XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), which are compatible with this syntax.

If you'd like to use this distribution channel, manually override the CocoaPods source locations in your Podfile. The following code snippet shows a sample override. Replace `{your-version}` with the relevant version you wish to import:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Step 2.6: Install pods**

Since React Native automatically links the libraries to the native platform, you can install the SDK with the help of CocoaPods.

The following code snippet shows how to install pods from the root folder of the project:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**Step 2.7: Configure the Braze SDK**

{% subtabs local %}
{% subtab SWIFT %}

The following code snippet shows how to import the Braze SDK at the top of the `AppDelegate.swift` file:
```swift
import BrazeKit
import braze_react_native_sdk
```

In the `application(_:didFinishLaunchingWithOptions:)` method, replace the API [key]({{site.baseurl}}/api/identifier_types/) and [endpoint]({{site.baseurl}}/api/basics/#endpoints) with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access.

{% alert note %}
Our example assumes an implementation of [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), which provides a number of abstractions in the React Native setup. If you are using a different setup for your app, be sure to adjust your implementation as needed.
{% endalert %}

The following code snippet shows an example `AppDelegate.swift` setup:

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

The following code snippet shows how to import the Braze SDK at the top of the `AppDelegate.m` file:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

In the `application:didFinishLaunchingWithOptions:` method, replace the API [key]({{site.baseurl}}/api/identifier_types/) and [endpoint]({{site.baseurl}}/api/basics/#endpoints) with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access.

{% alert note %}
Our example assumes an implementation of [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), which provides a number of abstractions in the React Native setup. If you are using a different setup for your app, be sure to adjust your implementation as needed.
{% endalert %}

The following code snippet shows an example `AppDelegate.m` setup:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Step 3: Initialize the SDK

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

The following code snippet shows how to import the library in your React Native code:

```javascript
import Braze from "@braze/react-native-sdk";
```

Then call `Braze.initialize()` with your app identifier API key and SDK endpoint to create the Braze instance. See the options below for where to call this method in your app.

#### Standard initialization

The following code snippet shows how to initialize the SDK when your app starts by calling `Braze.initialize()` in a `useEffect`:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
  }, []);

  return (
    // Your app components
  );
};
```

#### Delayed initialization

The following code snippet shows how to defer SDK initialization until later in the session&#8212;for example, after the user grants consent or completes login:

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
On iOS, push notifications received before `Braze.initialize()` are queued and processed after initialization. On Android, deep links from push notifications do not resolve while the SDK is waiting to be initialized. If your app relies on immediate deep link handling at launch, use [standard initialization](#standard-initialization) instead.
{% endalert %}

#### Platform-specific API keys

The following code snippet shows how to use platform detection when your Android and iOS apps use different API keys:

```javascript
import { Platform } from "react-native";
import Braze from "@braze/react-native-sdk";

const apiKey = Platform.select({
  android: "YOUR-ANDROID-API-KEY",
  ios: "YOUR-IOS-API-KEY",
}) ?? "";

Braze.initialize(apiKey, "YOUR-SDK-ENDPOINT");
```

#### Re-initialization

You can call `Braze.initialize()` multiple times to re-initialize the SDK with a different API key and endpoint mid-session. Each call tears down the previous Braze instance and creates a new one.

{% alert important %}
All SDK method calls made before `Braze.initialize()` are ignored on iOS, so call `Braze.initialize()` before using any other Braze methods.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 and earlier %}

For React Native SDK 19.1.0 and earlier, native initialization happens in Step 2. Import the library in your React Native code to call Braze methods. For more details, check out our [sample project](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Step 4: Test the integration (optional)

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

You can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in the dashboard (in the **Overview** section).

The following code snippet shows how to open a session for a particular user in your app:

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Search for the user with `{some-user-id}` in the dashboard under **Audience** > **Search Users**. There, you can verify that session and device data have been logged.

{% endtab %}
{% tab React Native SDK 19.1.0 and earlier %}

To test your SDK integration, the following code snippet shows how to start a new session on either platform for a user.

```javascript
Braze.changeUser("userId");
```

The following code snippet shows an example of assigning the user ID at app startup:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

In the Braze dashboard, go to [User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) and look for the user with the ID matching `some-user-id`. Here, you can verify that session and device data were logged.

{% endtab %}
{% endtabs %}

## Next steps

After integrating the Braze SDK, you can start implementing common messaging features:

- [Push Notifications]({{site.baseurl}}/developer_guide/push_notifications/): Set up and send push notifications to your users.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/): Display contextual messages within your app.
- [Banners]({{site.baseurl}}/developer_guide/banners/): Show persistent banners in your app interface.
