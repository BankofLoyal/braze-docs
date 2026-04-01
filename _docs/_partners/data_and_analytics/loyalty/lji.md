---
nav_title: GRAVTY®
article_title: GRAVTY® Loyalty Platform
description: "Industry’s first cloud-native, enterprise-class, patented technology, reshaping the loyalty program landscape through advanced AI, serverless, and autonomous capabilities."
alias: /partners/gravty/
page_type: partner
search_tag: Partner
---

# GRAVTY® Loyalty Platform

> [GRAVTY®](https://gravty.io/) is an enterprise-grade loyalty technology platform that enables brands to build, manage, and scale next-generation loyalty programs — driving deeper customer engagement through personalized, data-led experiences.

## About the integration

This integration connects GRAVTY® with Braze to enable seamless, multi-channel customer engagement. GRAVTY® acts as the publisher, triggering and syncing customer data and events, while Braze transforms this data into personalized communications across channels such as SMS, email, and push notifications.

1. **Member & Transaction Sync**: Sync member profiles, attributes, and transaction data to Braze using `/users/track` for real-time personalization and segmentation.
2. **Campaign Triggering**: Trigger Braze Campaigns via `/campaigns/trigger/send` to send immediate, single-message communications such as OTPs and alerts.
3. **Canvas Triggering**: Initiate multi-step customer journeys using `/canvas/trigger/send` for lifecycle and engagement use cases.
4.  **Personalization**: Leverage synced attributes like loyalty status, points balance, and behavior to drive targeted messaging.
## Use cases

This integration supports the following scenarios:

1. **Member Profile Sync**: Synchronize member profiles and attributes with Braze whenever a member is created or updated.

2. **Transaction & Event Sync**: Send member transactions and behavioral events to Braze to support segmentation and audience targeting.

3. **Real-time Communication Triggers**: Trigger real-time communications from GRAVTY to Braze based on configured loyalty events—such as points accrual, tier upgrades, and transactions

4. **Lifecycle and Personalized Engagement**: Leverage synchronized loyalty data and events to run lifecycle campaigns (e.g., welcome journeys, re-engagement campaigns) and deliver personalized communications through Braze.

## Prerequisites

Before you start, ensure you have the following:

| Requirement | Description                                                                                                                                                                 |
| :--- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GRAVTY® Account | A GRAVTY® account with the required permissions to configure integrations and manage event subscriptions.                                                                   |
| Braze Account | An active Braze account with API access enabled.                                                                                                                            |
| Braze REST API Key | A REST API key with `campaigns.trigger.send`, `canvas.trigger.send`, and `users.track` permissions.<br><br>Create this key in the Braze dashboard from **Settings > API Keys**. |
| Braze API Endpoint | Your Braze REST endpoint (for example, `https://rest.fra-01.braze.eu`).                                                                                                     |
| Campaign / Canvas IDs | Required for triggering messages from GRAVTY®.                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}


## Integration

The GRAVTY® integration with Braze is API-based and enables real-time data synchronization and communication triggering.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/Users/pavanharish/Documents/braze-docs/assets/img/lji/braze-gravty-integration.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    GRAVTY® integration flow using Braze APIs for data sync and communication delivery
  </figcaption>
</figure>


### Step 1: Connect Braze with GRAVTY®

1. Navigate to **Subscriber Setup** in GRAVTY® (used to manage external integrations).
2. Click **Add New Subscriber**.
3. Select **Braze** as the integration provider.
4. Provide the required details:
   * **API URL** (Braze REST endpoint)
    * **API Key** (Braze REST API key)
5. Save the configuration and ensure the connection is active.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/Users/pavanharish/Documents/braze-docs/assets/img/lji/braze-subscriber-setup.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    Connecting Braze as a subscriber in GRAVTY®
  </figcaption>
</figure>

---

### Step 2: Configure Template Attribute Mapping

After saving the Braze subscriber, you will be redirected to the **Template Attribute Mapping** page in GRAVTY® to configure how data is mapped to Braze.

To configure field mapping in GRAVTY®:

1. Click **Add New Field**.
2. Select the **GRAVTY® attribute** from the dropdown.
3. Enter the corresponding **Braze attribute name** (custom attribute) where the data should be mapped.

{% alert important %}
There is no need to map `external_id`. GRAVTY® automatically generates and maps it internally by hashing the member ID to ensure consistent and secure identification in Braze.
{% endalert %}

4. Repeat steps **1–3** to add additional mappings as needed.
5. Click **Save** to apply the configuration.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/Users/pavanharish/Documents/braze-docs/assets/img/lji/gravty-attribute-mapping.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    Attribute mapping configuration for Braze member sync
  </figcaption>
</figure>

{% alert note %}
The integration supports all Braze custom attribute data types, including numbers (integer, float), strings, arrays, booleans, objects, arrays of objects, and dates.
{% endalert %}

---

### Step 3: Test the Integration

Trigger a sample event  in GRAVTY® to verify that sync, communication triggers, and overall integration are working as expected.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/Users/pavanharish/Documents/braze-docs/assets/img/lji/braze-member-profile.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    The data fields are populated based on the configured field mapping.
  </figcaption>
</figure>

---
## Support

For assistance with integration setup or troubleshooting, contact the LJI support team at **support@lji.io**.

