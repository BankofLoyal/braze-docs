---
nav_title: GRAVTY®
article_title: GRAVTY® Loyalty Cloud
description: "Industry’s first cloud-native, enterprise-class, patented technology, reshaping the loyalty program landscape through advanced AI, serverless, and autonomous capabilities."
alias: /partners/gravty/
page_type: partner
search_tag: Partner
---

# GRAVTY® Loyalty Cloud

> [GRAVTY®](https://gravty.io/) is an enterprise-grade loyalty technology platform that enables brands to build, manage, and scale next-generation loyalty programs — driving deeper customer engagement through personalized, data-led experiences.

## About the integration

This integration connects GRAVTY® with Braze to enable seamless, multi-channel customer engagement. GRAVTY® acts as the publisher, triggering and syncing customer data and events, while Braze transforms this data into personalized communications across channels such as SMS, email, and push notifications.

* **Member & Transaction Sync**: Sync member profiles, attributes, and transaction data to Braze using `/users/track` for real-time personalization and segmentation.
* **Campaign Triggering**: Trigger Braze Campaigns via `/campaigns/trigger/send` to send immediate, single-message communications such as OTPs and alerts.
* **Canvas Triggering**: Initiate multi-step customer journeys using `/canvas/trigger/send` for lifecycle and engagement use cases.
* **Personalization**: Leverage synced attributes like loyalty status, points balance, and behavior to drive targeted messaging.
* **Real-time Engagement**: Enable instant communication based on member actions and events occurring in GRAVTY®.

## Use cases

This integration supports the following scenarios:

1. **Member Data Synchronization**  
   Sync member profiles and attributes to Braze on member creation or updates.

2. **Transaction & Event Sync**  
   Send member purchases and behavioral events to Braze for segmentation and targeting.

3. **Real-time Communication Triggers**  
   Trigger messages when key events occur (for example, points earned, tier upgrades, or transactions).

4. **Lifecycle Engagement**  
   Initiate campaigns such as welcome emails after enrollment or re-engagement journeys based on member activity.

5. **Personalized Messaging**  
   Use synced loyalty data and attributes to deliver targeted and relevant communications.

## Prerequisites

Before you start, ensure you have the following:

| Requirement | Description |
| :--- | :--- |
| GRAVTY® Account | A GRAVTY® account with the required permissions to configure integrations and manage event subscriptions. |
| Braze Account | An active Braze account with API access enabled. |
| Braze REST API Key | A REST API key with `campaigns.trigger.send`, `canvas.trigger.send`, and `users.track` permissions. |
| Braze API Endpoint | Your Braze REST endpoint (for example, `https://rest.fra-01.braze.eu`). |
| Campaign / Canvas IDs | Required for triggering messages from GRAVTY®. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}


## Integration

The GRAVTY® integration with Braze is API-based and enables real-time data synchronization and communication triggering.

### Step 1: Connect Braze with GRAVTY®

1. Navigate to **Subscriber Setup** in GRAVTY® (used to manage external integrations).
2. Click **Add New Subscriber**.
3. Select **Braze** as the integration provider.
4. Provide the required details:
   * **API URL** (Braze REST endpoint)
   * **API Key** (Braze REST API key)
5. Save the configuration and ensure the connection is active.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/assets/img/lji/braze-subscriber-setup.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    Connecting Braze as a subscriber in GRAVTY®
  </figcaption>
</figure>

---

### Step 2: Configure Attribute Mapping

After saving the Braze subscriber, you will be redirected to the **Attribute Mapping** page in GRAVTY® to configure field mapping for data synchronization.

To configure field mapping in GRAVTY®:

1. Click **Add New Field**.
2. Select the GRAVTY® attribute from the dropdown.
3. Enter the corresponding Braze attribute name (custom attribute) where the data should be mapped.
4. Repeat the steps to add additional mappings as needed.
5. Save the configuration.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/assets/img/lji/gravty-attribute-mapping.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    Attribute mapping configuration for Braze member sync
  </figcaption>
</figure>

* Attribute mapping is used to construct the Braze `/users/track` payload for syncing data, including member attributes, events, purchases, and their properties.
* This configuration is primarily used for **data synchronization (User Sync)** and is not required for Campaign or Canvas triggers.
* A prefix-based naming convention (for example, `event__`, `purchase__`, `purchaseproperty__`) is used to identify the type of data being synced.
* Supports configurable sync behavior through a **"Sync Only Updated Attributes"** toggle:
  * When enabled, only modified attributes are sent
  * Otherwise, full member data including attributes, events, and purchases are synced

---

### Example: Member Sync and Triggered Communication

* Member data synced from GRAVTY® is available in Braze user profiles.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/assets/img/lji/braze-member-profile.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    Example of a synced member profile in Braze
  </figcaption>
</figure>

* Events such as tier upgrades can trigger communications using Campaigns or Canvas.

<figure style="text-align:center; padding: 16px 0;">
  <img src="/assets/img/lji/braze-trigger-example.png" style="width:70%; border-radius:12px;" />
  <figcaption style="font-size:14px; color:#666;">
    Example of a triggered communication in Braze
  </figcaption>
</figure>

---
## Data Handling and Request Behavior

* Uses `external_id` as the unique identifier in Braze, generated by hashing the GRAVTY® member ID to ensure secure and consistent identity mapping.
* Supports Braze-compatible data types as defined in Braze documentation.
* Includes a `User-Agent` header (`partner-LoyaltyJuggernaut-GRAVTY/<version>`) in API requests to help identify the integration source.
* Requests are batched when payloads exceed Braze limits; purchases are sent in chunks of up to 75 items per request to ensure compliance with payload size and rate limits.
* Exponential backoff retry logic is implemented to gracefully handle transient failures, with increasing wait intervals between retries to reduce load and improve reliability.