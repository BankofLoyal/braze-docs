---
nav_title: Nested custom attributes
article_title: Nested Custom Attributes
alias: "/nested_custom_attribute_support/"
page_order: 3
page_type: reference
description: "This reference article covers using nested custom attributes as a data type for custom attributes, including limitations and usage examples."
---

# Nested custom attributes

> This page covers nested custom attributes, which allow you to define a set of attributes as a property of another attribute. In other words, when you define a custom attribute object, you can define a set of additional attributes for that object.

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Considerations

- Nested custom attributes are intended for custom attributes sent through the Braze SDK or API. 
- Objects have a maximum size of 100&nbsp;KB. If an update causes the object to exceed 100&nbsp;KB, Braze drops the update, and the attribute is unchanged.
- Key names and string values have a size limit of 255 characters.
- Key names cannot contain spaces.
- Periods (`.`) and dollar signs (`$`) aren't supported characters in an API payload if you're attempting to send a nested custom attribute to a user profile.
- Not all Braze Partners support nested custom attributes. Refer to the [Partner documentation]({{site.baseurl}}/partners/home) to confirm if specific partner integrations support this feature.
- Nested custom attributes cannot be used as a filter when making a Connected Audience API call.

## API example

{% tabs local %}
{% tab Create %}
The following is a `/users/track` example with a "Most Played Song" object. To capture the properties of the song, we'll send an API request that lists `most_played_song` as an object, along with a set of object properties.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
To update an existing object, send a POST to `users/track` with the `_merge_objects` parameter in the request. This will deep merge your update with the existing object data. Deep merging ensures that all levels of an object are merged into another object instead of only the first level. In this example, we already have a `most_played_song` object in Braze, and now we're adding a new field, `year_released`, to the `most_played_song` object.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

After this request is received, the custom attribute object will now look like the following:

```json
{"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}}
```

{% alert warning %}
You must set `_merge_objects` to `true`, or your objects will be overwritten. `_merge_objects` is `false` by default.
{% endalert %}

{% endtab %}
{% tab Delete %}
To delete a custom attribute object, send a POST to `users/track` with the custom attribute object set to `null`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
This approach can't be used to delete a nested key inside an [array of objects]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/).
{% endalert %}

{% endtab %}
{% endtabs %}

## SDK example

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**Create**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Update**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Delete**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Create**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Update**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Delete**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**Create**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Update**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Delete**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Capturing dates as object properties

To capture dates as object properties, you must use the `$time` key. In the following example, an "Important Dates" object is used to capture the set of object properties, `birthday` and `wedding_anniversary`. The value for these dates is an object with a `$time` key, which cannot be a null value.

{% alert note %}
If you haven't captured dates as object properties initially, we recommend resending this data using the `$time` key for all users. Otherwise, this may result in incomplete segments when using the `$time` attribute. However, if the value for `$time` in a nested custom attribute isn't formatted correctly, the entire nested custom attribute won't be updated.
{% endalert %}

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
For nested custom attributes, if the year is less than 0 or greater than 3000, Braze doesn't store these values on the user.
{% endalert %}

## Liquid templating

The following Liquid templating example shows how to reference the custom attribute object properties saved from the preceding API request and use them in your messaging.

Use the `custom_attribute` personalization tag and dot notation to access properties on an object. Specify the name of the object (and position in array if referencing an array of objects), followed by a dot (period), followed by the property name.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

![Using Liquid to template a song name and the number of times a listener has played that song into a message]({% image_buster /assets/img_archive/nca_liquid_2.png %})

### Personalization

Using the **Add Personalization** modal, you can also insert nested custom attributes into your messaging. Select **Nested Custom Attributes** as the personalization type. Next, select the top-level attribute and attribute key. 

For example, in the personalization modal below, this inserts the nested custom attribute of a local neighborhood office based on a user's preferences.

![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
Check that a schema has been generated if you don't see the option to insert nested custom attributes.
{% endalert %}

## Regenerate schemas {#regenerate-schema}

After a schema has been generated, it can be regenerated once every 24 hours. This section describes how to regenerate your schema. For more detailed information on schemas, see [Generate a schema using the nested object explorer]({{site.base}}/user_guide/audience/segments/segment_with_nested_custom_attributes/#generate-schema).

To regenerate the schema for your nested custom attribute:

1. Go to **Data Settings** > **Custom Attributes**.
2. Search for your nested custom attribute.
3. In the **Attribute Name** column for your attribute, select <i class="fas fa-plus"></i> to manage the schema.
4. A modal will appear. Select **Regenerate Schema**.

The option to regenerate schema will be disabled if it has been less than 24 hours since the schema was last regenerated. Regenerating the schema will only detect new objects and will not delete objects that currently exist in the schema.

{% alert important %}
To reset the schema for an object array with an existing object, you need to create a new custom attribute. Schema regeneration doesn't delete existing objects.
{% endalert %}

If data doesn't appear as expected after regenerating the schema, the attribute may not be ingested often enough. User data is sampled on previous data sent to Braze for the given nested attribute. If the attribute isn't ingested enough, it won't be picked up for the schema.

## Trigger nested custom attribute changes

You can trigger when a nested custom attribute object changes. This option isn't available for changes to object arrays. If you don't see an option to view the path explorer, check that you've generated a schema.

For example, in an action-based campaign, you can add a new trigger action for **Change Custom Attribute Value** to target users who have changed their neighborhood office preferences.

![Action-based campaign delivery settings with a Change Custom Attribute Value trigger for nested preferences.]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

## Segmentation behavior with arrays of objects

When you use multiple `Nested Custom Attribute` filters with AND logic to segment on an array of objects, each filter is evaluated independently across all items in the array. A user qualifies for the segment if _any_ item in the array satisfies each individual filter—the filters don't have to match the _same_ item.

For example, suppose a user has the following array:

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

A segment with the following AND filters:

- `orders[].price` is greater than 50
- `orders[].price` is less than 30

This user would qualify because the first filter matches the "Shoes" item (80 > 50) and the second filter matches the "Hat" item (25 < 30). Even though no single item satisfies both conditions, the user still enters the segment.

If you need all conditions to match the same item within an array, use [multi-criteria segmentation](#multi-criteria-segmentation) on the same path, or restructure your data to avoid cross-item matching.

## Data points

Any key that is sent consumes a data point. For example, this object initialized in the user profile counts as seven (7) data points:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
Updating a custom attribute object to `null` also consumes a data point.
{% endalert %}

