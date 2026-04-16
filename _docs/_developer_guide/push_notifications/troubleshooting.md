---
page_order: 10.9
nav_title: Troubleshooting
article_title: Troubleshoot push notifications for the Braze SDK
channel:
  - push notifications
---

# Troubleshoot push notifications

> Learn how to troubleshoot push notifications for the Braze SDK.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/push_notifications/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}

## Line breaks in push notifications {#push-linebreaks}

When composing push notifications with Liquid tags, line breaks adjacent to Liquid tags are automatically removed before the message is sent. In the [push notification composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/), these line breaks are re-added so your message remains readable while editing. If you notice line breaks around Liquid tags when saving your message, this is expected behavior.

