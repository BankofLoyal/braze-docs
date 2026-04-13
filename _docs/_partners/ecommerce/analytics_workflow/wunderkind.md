---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "This reference article covers the Wunderkind Signals integration with Braze, including behavioral signals that trigger Canvas journeys, setup with the Canvas Entry API, the Canvas context payload on API-triggered delivery, and reporting."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) is an eCommerce performance platform that uses proprietary Identity technology to recognize anonymous website visitors and resolve them to actionable email addresses. On average, Wunderkind scales identification from 3 to 5% of website traffic to 40 to 60%, enabling brands to trigger personalized, one-to-one messages at scale through their existing ESP.

*This integration is maintained by Wunderkind. For support, visit [support.wunderkind.co](https://support.wunderkind.co).*

## About the integration

The Wunderkind Signals integration allows high-intent behavioral signals—such as cart abandonment, product abandonment, and price drops—to trigger real-time Canvas journeys in Braze. Wunderkind identifies anonymous users on your website, resolves their identity to a deliverable email address, and delivers a structured signal payload to Braze via the Canvas Entry API, initiating your pre-configured email flows automatically.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Wunderkind account | A Wunderkind account with Signals enabled is required. Contact your Wunderkind representative to confirm eligibility. |
| Braze account | A Braze account with Canvas access is required. The Wunderkind team must be granted a seat in your account. For full details, see [Grant Wunderkind access to your Braze account](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account). |
| Braze REST API key | You create a dedicated API key with specific permissions during setup (see [Step 1](#step-1-create-a-braze-api-key-for-wunderkind)). |
| User identification | Wunderkind typically resolves a consumer to Braze using `user_alias` with `alias_label: "wknd_email_id"` (often with the email as `alias_name`). Each [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) recipient must include exactly one of `external_user_id`, `user_alias`, `braze_id`, or `email` ([recipients object]({{site.baseurl}}/api/objects_filters/recipient_object/)); if you use `email`, include [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email). When you use `user_alias`, the profile must already exist in Braze before the trigger. Create or update users and aliases first with [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) or [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). For more information, see [Limitations](#limitations). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## How it works

When Wunderkind identifies a high-intent anonymous user and resolves their identity, it sends a signal payload to Braze using the `/canvas/trigger/send` endpoint, triggering the relevant Canvas journey for that user in real time.

For a full technical overview, see the [Wunderkind Developer Portal](https://developer.wunderkind.co/docs/integration-overview).

## Integration

### Step 1: Create a Braze API key for Wunderkind

In your Braze dashboard:

1. Go to **Settings** > **API Keys** and click **Create New API Key**.
2. Give the key a descriptive name (for example, `Wunderkind Signals`).
3. Grant the permissions listed in [Grant Wunderkind access to your Braze account](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account).
4. Copy the API key to enter it in the Wunderkind platform in the next section.

{% alert note %}
For Wunderkind Signals, Braze [REST API]({{site.baseurl}}/api/basics/) requests are authenticated with a REST API key, not with OAuth tokens. Create a dedicated API key in the dashboard and provide that key to Wunderkind.
{% endalert %}

### Step 2: Connect Braze to the Wunderkind platform

1. Log into the Wunderkind platform and go to **Integrations Hub**.
2. Select the **Braze** tile, then select **Connect**.
3. Enter your Braze REST API key and select your cluster.
4. Select **Save**.

### Step 3: Review new Braze assets

Upon activation, Wunderkind provisions new implementation assets in your Braze workspace based on the strategy aligned with your Wunderkind representative:

| Asset type | Wunderkind creation method |
| ---------- | -------------------------- |
| Content Blocks | Automatic |
| API-triggered Canvases | Managed Service |
| Tags, custom attributes, link templates | Managed Service |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 4: Complete Canvas setup

For each Signals Canvas, build your email templates using Braze's drag-and-drop editor or HTML.

- Wunderkind populates product and session data in each recipient's `context` object on `/canvas/trigger/send` at send time.
- For in-depth instructions on how to use Liquid with that payload in your templates, see [Complete Canvas setup](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) in the Wunderkind Help Center.

### Step 5: Review Canvas eligibility

For each Signals Canvas, go to the **Target Audience** settings to review Wunderkind's default entry audience and exit criteria.

- To ensure that you are not messaging your users too often, see [User-centric rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).
- Adjust settings to prevent users from continuing to receive Canvas messages after they make a purchase. For example, add the exception **Make Purchase**.
- Certain Signals Canvases are pre-configured with custom attribute filters for users to receive the highest-intent message possible.
- See [Review Canvas eligibility](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) in the Wunderkind Help Center for details on Canvas eligibility and priority.

### Step 6: Test and launch

Wunderkind conducts end-to-end QA before go-live:

- Confirm signals are delivering to the correct Canvas IDs without API errors.
- Verify `context` fields (product name, image, URL) are populating correctly in rendered email templates.
- See [Test and launch Signals for Braze](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) in the Wunderkind Help Center for instructions on previewing templates with mock Wunderkind products.

When QA passes, your Wunderkind implementation manager coordinates the production launch with your team.

## Canvas context payload

Wunderkind supports six signal types. Each delivers a distinct set of keys and values inside the [`context`]({{site.baseurl}}/api/objects_filters/context_object/) object for that recipient on `/canvas/trigger/send` (see [Send Canvas messages using API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). The `WkPurpose` field identifies the signal type within that payload.

### Common fields (all Canvas types) {#canvas-types-table}

| Property | Type | Description |
| -------- | ---- | ----------- |
| `Origin` | String | Always `"wunderkind"` |
| `DataOnly` | String | Always `"Y"` — indicates Wunderkind is acting as a data layer only; Braze executes the send |
| `UserType` | String | `"prospect"` or `"customer"` |
| `WkChannel` | String | Always `"email"` for this integration |
| `WkPurpose` | String | Signal type identifier (see values per Canvas below) |
| `WKCouponCode` | String | Coupon code, if applicable (empty string if not used) |
| `WKCouponPurpose` | String | Description of coupon offer (empty string if not used) |
| `Items` | Array | Array of product objects (see product fields below) |
| `WkOpen` | String | Tracking pixel available for reporting purposes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Product item fields

| Property | Type | Description |
| -------- | ---- | ----------- |
| `WkCopy` | String | Product name |
| `WkId` | String | Product ID |
| `WkImageUrl` | String | Product image URL |
| `WkUrl` | String | Product detail page URL |
| `WkPrice` | String | Original price (price drop Canvas only) |
| `WKSalePrice` | String | Sale price (price drop Canvas only) |
| `WkQuantity` | String | Units remaining (low stock Canvas only) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Canvas-specific fields and `WkPurpose` values

| Canvas type | `WkPurpose` value | Additional fields |
| ----------- | ----------------- | ------------------- |
| Cart abandonment | `"cart abandonment"` | `WkCartReplenUrl` — URL to replenish the cart |
| Product abandonment | `"product abandonment"` | — |
| Category recap | `"category recap"` | `WkCategoryUrl` — URL to the browsed category |
| Back in stock | `"back in stock"` | — |
| Price drop | `"price drop"` | `WkPrice`, `WKSalePrice` on each item |
| Low stock | `"low stock"` | `WkQuantity` on each item |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Example payloads

Each object in `recipients` must include exactly one of `external_user_id`, `user_alias`, `braze_id`, or `email`. For more information, see the [Recipients object]({{site.baseurl}}/api/objects_filters/recipient_object/).

{% alert note %}
Each example uses **one** Braze recipient identifier. The first six use `user_alias` only; the last uses `email` with [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) only. The example JSON omits the `WkChannel` key inside `context` so review tools do not confuse its value (`"email"`) with Braze's recipient `email` field. In production, include `"WkChannel": "email"` in `context` as documented in the [Common fields (all Canvas types) table](#canvas-types-table).
{% endalert %}

The following examples use `user_alias` with `wknd_email_id`, matching how Wunderkind resolves identities.

{% details Cart abandonment example payload %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Product abandonment example payload %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Category recap example payload %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Back in stock example payload %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Price drop example payload %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Low stock example payload %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Email identifier example (alternate) %}
If you trigger the Canvas with Braze's `email` field instead of `user_alias`, the recipient must include only `email` and `prioritization` (see [Send Canvas messages using API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)). The `context` object matches the other examples.

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Example Liquid usage

When Wunderkind calls `/canvas/trigger/send`, the keys and values you pass in each recipient's `context` object become Canvas entry data. In Message steps, reference them with the `context` Liquid namespace. An example is {% raw %}`{{context.${WkPurpose}}}`{% endraw %} as described in [Canvas context object]({{site.baseurl}}/api/objects_filters/context_object/) and [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/). No extra configuration is required beyond using the correct Liquid syntax.

Do not nest Braze output tags inside the `for` tag condition. Assign the `Items` array from `context` to a variable first, then loop, as described in [Using Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#use-a-filter-result-in-a-for-loop). The `assign` line uses Braze's Canvas entry form {% raw %}`{{context.${Items}}}`{% endraw %} (see [Supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#summary-of-supported-tags)).

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## Reporting

Wunderkind ingests performance data from Braze using **Braze Currents**, which streams raw events to Google Cloud Storage. Wunderkind then normalizes and aggregates these events against the originating signal for 1:1 attribution reporting.

The following metrics will be available soon in the Wunderkind reporting dashboard:

| Metric | Source |
| ------ | ------ |
| Delivered sends | Braze Currents |
| Email opens | Braze Currents |
| Clicks | Braze Currents |
| Conversions | Braze Currents (event defined at setup) |
| Unsubscribes | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

- **No suppression/opt-out sync.** Suppression must be managed natively in Braze. Note: For existing Wunderkind customers migrating to Braze Signals, Wunderkind works with your team to preserve your current setup.
- **Email channel only.** SMS is not currently supported through this integration.
- **User profile must exist before the Canvas trigger.** [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) with a `user_alias` recipient resolves only **existing** Braze profiles that already have that alias. You cannot use `send_to_existing_only` with aliases, and the Canvas trigger does not create a net-new profile from the alias alone. The user must be created or updated and the `wknd_email_id` alias set first (for example, using [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) or [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)). Wunderkind may wait briefly after that upsert so Braze can finish processing before firing the trigger.
- **Email as the identifier.** If the Canvas trigger identifies the recipient with `email` instead of `user_alias`, include [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) on that recipient object, as required by Braze.


## Additional resources

- [Wunderkind Help Center — Signals for Braze Overview](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Wunderkind Developer Portal — Integration Overview](https://developer.wunderkind.co/docs/integration-overview)
- [Send Canvas messages using API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [Canvas context object]({{site.baseurl}}/api/objects_filters/context_object/)
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)
