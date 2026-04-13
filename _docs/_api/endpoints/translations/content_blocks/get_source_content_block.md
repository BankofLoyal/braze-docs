---
nav_title: "GET: View default source values for Content Block translation tags"
article_title: "GET: View Default Source Values for Content Block Translation Tags"
search_tag: Endpoint
page_order: 0

layout: api_page
page_type: reference
description: "This article outlines details about the Content Block translation source endpoint."
---

{% api %}
# View default source values for a Content Block's translation tags
{% apimethod get %}
/content_blocks/translations/source
{% endapimethod %}

> Use this endpoint to view all the default translation sources for a Content Block's translation tags. These are the values within the {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. See [Locales in messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) for more information about translation features.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `content_blocks.translations.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Query parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`content_block_id`| Required | String | The ID of your Content Block. |
|`locale_id`| Optional | String | A locale UUID to filter the responses. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint's response.
{% endalert %}

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations/source?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

There are four status code responses for this endpoint: `200`, `400`, `404`, and `429`.

### Example success response

The status code `200` could return the following response header and body.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Welcome!",
           "id_1": "Thank you for joining our program"
       }
   },
   "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}
