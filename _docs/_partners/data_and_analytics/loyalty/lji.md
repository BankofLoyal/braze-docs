---
nav_title: GRAVTY®
article_title: GRAVTY® Loyalty Platform
description: "This article outlines the partnership between Braze and GRAVTY®, an enterprise-grade loyalty platform that enables brands to design, manage, and scale data-driven loyalty programs for enhanced customer engagement and retention."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# GRAVTY® Loyalty Platform

> [GRAVTY®](https://www.lji.io/) is an enterprise-grade loyalty platform from Loyalty Juggernaut Inc. (LJI) that enables brands across retail, travel, restaurants (including quick-service restaurants), and financial services to design, manage, and scale next-generation programs—driving measurable growth in engagement, retention, and customer lifetime value through personalized, data-led experiences.

Built on a flexible, API-first architecture, GRAVTY® supports real-time earn and burn, partner ecosystem management, and integration across channels. Teams can launch faster, iterate on programs, and deliver loyalty experiences at scale.

_This integration is maintained by LJI._

## About the integration

The Braze and GRAVTY® integration connects loyalty data and messaging triggers across both platforms. GRAVTY® sends user data to Braze as attributes, events, and purchases. Braze stores that data and delivers messages across channels such as SMS, email, and push notifications. You use the synced data for segmentation, personalization, and triggers.

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

- **User data sync (`/users/track`):** Sync member attributes, events, and purchases to Braze for segmentation and personalization.
- **Campaign triggering (`/campaigns/trigger/send`):** Trigger one-time or transactional messages using Braze campaigns.
- **Canvas triggering (`/canvas/trigger/send`):** Start multi-step journeys and lifecycle messaging using Braze **Canvas**.
- **Segmentation and personalization:** Build targeted audiences and deliver personalized communications from synced data.

## Integration

The GRAVTY® and Braze integration is API-based. It supports real-time data synchronization and communication triggering.

![Flow diagram of GRAVTY® sending data and triggers to Braze APIs, then messages to SMS, email, push, and WhatsApp.]({% image_buster /assets/img/lji/braze-gravty-integration.png %})

### Step 1: Connect Braze with GRAVTY®

1. Go to **Subscriber Setup** in GRAVTY® to manage external integrations.
2. Select **Add New Subscriber**.
3. Select **Braze** as the integration provider.
4. Enter the following:
   * **API URL** (your Braze REST endpoint)
   * **API Key** (your Braze REST API key)
5. Save the configuration and confirm the connection is active.

![GRAVTY® Add Subscriber form with Braze selected, API URL and API key fields, and an active subscriber toggle.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### Step 2: Configure Event Trigger

Create an event in GRAVTY® that will trigger when a transaction is created or updated for a member based on defined conditions.

1. Navigate to the **Events** section in GRAVTY®.
2. Click **Create Event**.
3. Define the event conditions (for example, transaction created, points earned, or tier upgrade).
4. Configure the rules that determine when the event should be triggered.
5. Attach the Braze subscriber to the event to enable communication triggers.
6. Save the event configuration.

The following is an example of an event configured to trigger when a member is enrolled into the program:

![Connecting Braze as a subscriber in GRAVTY®.]({% image_buster /assets/img/lji/event_configuration.png %})

### Step 3: Configure Template Attribute Mapping

After configuring the event, complete the subscriber configuration to enable data sync and communication triggers:

1. Select the **Braze subscriber** created in Step 1 from the subscriber dropdown.
2. Choose the appropriate **channel** (**Campaign** or **Canvas**) based on your use case. For data sync–only scenarios, the channel can be left unselected.
3. Enter the corresponding **Campaign ID** or **Canvas ID** in the **Template Name** field, as applicable.
4. Configure the communication type to support sync and/or trigger-based messaging.

To configure field mapping in GRAVTY®:

1. Click **Add New Field**.
2. Select the **GRAVTY® attribute** from the dropdown.
3. Enter the corresponding **Braze attribute name** where the data should be mapped.

{% alert important %}
There is no need to map `external_id`. GRAVTY® automatically generates and maps it internally by hashing the member ID, which serves as the unique identifier for members within GRAVTY®.
{% endalert %}

4. Repeat steps **1–3** to add additional mappings as needed.
5. Click **Save** to apply the configuration.

![Attribute mapping configuration for Braze member sync.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
The integration supports all Braze custom attribute data types, including numbers (integer, float), strings, arrays, booleans, objects, arrays of objects, and dates.
{% endalert %}

### Step 4: Test the Integration

Trigger a sample event in GRAVTY® to verify that sync, communication triggers, and overall integration are working as expected.

* Member data is synced to Braze and reflected in the member profile.

![The data fields are populated based on the configured field mapping.]({% image_buster /assets/img/lji/braze-member-profile.png %})

* Communication is triggered based on the configured Campaign or Canvas.

![Example of an email triggered from Braze.]({% image_buster /assets/img/lji/braze-email-example.png %})

## Support

For integration support or troubleshooting, contact LJI at [support@lji.io](mailto:support@lji.io).
