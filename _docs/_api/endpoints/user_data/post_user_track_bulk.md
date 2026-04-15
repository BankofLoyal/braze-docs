---
nav_title: "POST: Track users (bulk)"
article_title: "POST: Track users (bulk)"
search_tag: Endpoint
page_order: 4.25
layout: api_page
page_type: reference
alias:
  - /unlisted_docs/track_users_bulk_partners/
  - /api/endpoints/user_data/post_user_track_bulk_partners/
description: "This article outlines details about the bulk Track users endpoint."
---
{% api %}
# Track users (bulk)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

Use this endpoint to record custom events and purchases and update user profile attributes in bulk.

{% alert important %}
This endpoint is currently in early access. Contact your Braze customer success manager if you are interested in participating in the early access.
{% endalert %}

## When to use this endpoint

Like the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), you can use this endpoint to update user profiles. This endpoint is better suited for bulk updates:

- **Larger requests:** Send up to 1,000 users per request, so you can make fewer requests for large backfills and syncs.
- **Prioritization:** During peak traffic conditions, requests to `/users/track` are prioritized over requests to `/users/track/bulk`.

Use this endpoint when you're backfilling many user profiles during onboarding, or syncing large volumes of profiles as part of a daily sync.

{% alert note %}
The `/users/track` endpoint request object limits vary by pricing model and configuration. Use `/users/track/bulk` for bulk ingestion.
{% endalert %}

## Prerequisites

To use this endpoint, you must have an [API key]({{site.baseurl}}/api/api_key/) with the `users.track.bulk` permission.

If you're making server-to-server calls behind a firewall, you may need to allowlist your Braze REST endpoint (for example, `rest.iad-01.braze.com`). For more information, see [API endpoints]({{site.baseurl}}/api/basics/#api-definitions).

## Rate limit

For most customers, this endpoint has a base speed limit of 50 requests per second.

Customers on newer contracts may instead have burst (per-second) and steady (per-hour) limits based on contracted monthly active users.

Each `/users/track/bulk` request has a payload limit of 2 MB and can include up to 1,000 objects total across attributes, events, and purchases, depending on your account's bulk rate-limit policy.

Each object can update one user, so a single request can update up to your account's request object limit of different users. Additionally, each request can contain a maximum of 100 objects per user profile across attributes, events, and purchases.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object)
}
```

### Request parameters

{% alert important %}
For each request object, you must include one of `external_id`, `user_alias`, `braze_id`, `email`, or `phone`.
{% endalert %}

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `attributes` | Optional | Array of attributes objects | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array of event objects | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array of purchase objects | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example requests

### Bulk update user profiles in one request

Update up to your account's request object limit of user profiles in one request.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    },
    {
      "external_id": "user2",
      "string_attribute": "vegetables",
      "boolean_attribute_1": false,
      "integer_attribute": 25,
      "array_attribute": [
        "broccoli",
        "asparagus"
      ]
    }
  ]
}'
```

### Send attributes and events in one request

Include attributes and events in the same request, up to your account's total object limit.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    }
  ],
  "events": [
    {
      "external_id": "user2",
      "app_id": "your_app_identifier",
      "name": "rented_movie",
      "time": "2022-12-06T19:20:45+01:00",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}'
```

## Responses

### Successful message

Successful messages return the following response:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}
```

### Successful message with non-fatal errors

If your request is successful but has non-fatal errors (for example, one invalid event object in a large batch), you receive the following response:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### Message with fatal errors

If your request has a fatal error, you receive the following response:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Fatal error response codes

For status codes and associated error messages that Braze returns when your request has a fatal error, see [Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors).

If you receive the error "provided external_id is blacklisted and disallowed", your request may include a "dummy user." For more information, see [Spam blocking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Frequently asked questions

### Should I use this endpoint or `/users/track`?

Use both endpoints based on your use case:

- For large backfills and syncs, use `/users/track/bulk`.
- For real-time use cases, use `/users/track`.

### What identifiers can I use in `/users/track/bulk`?

For each request object, include one of `external_id`, `braze_id`, `user_alias`, `email`, or `phone`.

### Can I include attributes, events, and purchases in one request?

Yes. Include any mix of attributes, events, and purchases, up to your account's combined request object limit.

{% endapi %}
