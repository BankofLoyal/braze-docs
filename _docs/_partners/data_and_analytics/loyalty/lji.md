---
nav_title: GRAVTY®
article_title: GRAVTY® Loyalty Platform
description: "This article outlines the partnership between Braze and GRAVTY®, an enterprise-grade loyalty platform that enables brands to design, manage, and scale data-driven loyalty programs for enhanced customer engagement and retention."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# GRAVTY® Loyalty Platform

> [GRAVTY®](https://www.lji.io/) is an enterprise-grade loyalty platform from Loyalty Juggernaut Inc. (LJI) that enables brands across Retail, Travel, restaurants (including quick-service restaurants), and Financial Services to design, manage, and scale next-generation programs—driving measurable growth in engagement, retention, and customer lifetime value through personalized, data-led experiences.

Built on a flexible, API-first architecture, GRAVTY® supports real-time earn and burn, partner ecosystem management, and integration across channels. Teams can launch faster, iterate on programs, and deliver loyalty experiences at scale.

_This integration is maintained by LJI._

## About the integration

The Braze and GRAVTY® integration connects loyalty data and messaging triggers across both platforms. GRAVTY® sends customer data to Braze as attributes, events, and purchases. Braze stores that data and delivers messages across channels such as SMS, email, and push notifications. You use the synced data for segmentation, personalization, and triggers.

## Prerequisites

Before you start, you need the following:

| Requirement | Description |
| :--- | :--- |
| GRAVTY® account | A GRAVTY® account with permission to configure integrations and manage event subscriptions. |
| Braze account | An active Braze account with API access enabled. |
| Braze REST API key | A REST API key with `campaigns.trigger.send`, `canvas.trigger.send`, and `users.track` permissions.<br><br> Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| Braze API endpoint | Your Braze REST endpoint (for example, `https://rest.fra-01.braze.eu`). For more information, see [Braze instances and endpoints]({{site.baseurl}}/api/basics/#endpoints). |
| Campaign or Canvas IDs | IDs for the **Campaigns** or **Canvas** workflows you trigger from GRAVTY®. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Use cases

This integration supports the following Braze capabilities:

1. **User data sync (`/users/track`)**  
   Sync member attributes, events, and purchases to Braze for segmentation and personalization.

2. **Campaign triggering (`/campaigns/trigger/send`)**  
   Trigger one-time or transactional messages using Braze **Campaigns**.

3. **Canvas triggering (`/canvas/trigger/send`)**  
   Start multi-step journeys and lifecycle messaging using Braze **Canvas**.

4. **Segmentation and personalization**  
   Build targeted audiences and deliver personalized communications from synced data.

## Integration

The GRAVTY® and Braze integration is API-based. It supports real-time data synchronization and communication triggering.

![Flow diagram of GRAVTY® sending data and triggers to Braze APIs, then messages to SMS, email, push, and WhatsApp.]({% image_buster /assets/img/lji/braze-gravty-integration.png %})

### Step 1: Connect Braze with GRAVTY®

1. Go to **Subscriber Setup** in GRAVTY® to manage external integrations.
2. Click **Add New Subscriber**.
3. Select **Braze** as the integration provider.
4. Enter the following:
   * **API URL** (your Braze REST endpoint)
   * **API Key** (your Braze REST API key)
5. Save the configuration and confirm the connection is active.

![GRAVTY® Add Subscriber form with Braze selected, API URL and API key fields, and an active subscriber toggle.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %})

### Step 2: Configure template attribute mapping

After you save the Braze subscriber, GRAVTY® opens the **Template Attribute Mapping** page. Use it to map fields to Braze.

1. Click **Add New Field**.
2. Select a **GRAVTY® attribute** from the list.
3. Enter the **Braze attribute name** (custom attribute) where the value should appear in Braze.

{% alert important %}
You don't need to map `external_id`. GRAVTY® generates and maps it internally by hashing the member ID for consistent identification in Braze.
{% endalert %}

{: start="4"}
4. Repeat steps 1–3 to add more mappings.
5. Click **Save**.

![GRAVTY® Subscription Setup showing entity, GRAVTY attribute, and template attribute columns mapped for Braze sync.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
The integration supports Braze custom attribute data types, including numbers (integer, float), strings, arrays, booleans, objects, arrays of objects, and dates.
{% endalert %}

### Step 3: Test the integration

Trigger a sample event in GRAVTY® to confirm sync, communication triggers, and the end-to-end flow.

![Braze user profile Overview with custom attributes such as tier and tier dates populated from GRAVTY® mapping.]({% image_buster /assets/img/lji/braze-member-profile.png %})

## Support

For integration support or troubleshooting, contact LJI at [support@lji.io](mailto:support@lji.io).
