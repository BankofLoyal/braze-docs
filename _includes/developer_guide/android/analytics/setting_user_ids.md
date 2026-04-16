 
# Setting user IDs
 
> This reference article shows how to set user IDs in your Android or FireOS app, suggested user ID naming conventions, and some best practices.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Suggested user ID naming convention

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Assigning a user ID

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user ID:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**Do not call `changeUser()` when a user logs out. `changeUser()` should only be called when the user logs into the application.** Setting `changeUser()` to a static default value will associate ALL user activity with that default "user" until the user logs in again.
{% endalert %}

Additionally, we recommend **against** changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with re-engagement campaigns. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

Refer to the [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) documentation for more information.

### Subscribing to user change events

Use [`subscribeToChangeUserEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-change-user-events.html) to run logic when your app changes users with `changeUser()`. This method is available in Android SDK 40.0.0 and later.

The subscriber callback runs when a user is changed through `changeUser()` and receives a `BrazeUserChangeEvent`. `BrazeUserChangeEvent` is fired when the current user has changed or when the SDK has just been initialized. The SDK can fire multiple events for the same user, even when no transition occurs.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToChangeUserEvents(new IEventSubscriber<BrazeUserChangeEvent>() {
  @Override
  public void trigger(BrazeUserChangeEvent event) {
    // Add your app logic for user changes, such as refreshing user-scoped state.
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToChangeUserEvents { event ->
  // Add your app logic for user changes, such as refreshing user-scoped state.
}
```

{% endtab %}
{% endtabs %}

## User ID integration best practices and notes

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Aliasing users

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}

