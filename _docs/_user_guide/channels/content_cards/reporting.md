---
nav_title: Reporting
article_title: Content Card Reporting
page_order: 21
description: "This reference article provides an overview of the different Content Card reporting metrics and analytics options provided in the Braze dashboard."
channel:
  - content cards
tool:
  - Reports
  
---

# Content Card reporting

> This reference article provides an overview of the different Content Card reporting metrics and analytics options provided in the Braze dashboard.

## When sends are logged

The timing of a _Sent_ event for Content Cards depends on the delivery type and **Card Creation** setting.

### Scheduled delivery

For scheduled Content Cards, the timing of a _Sent_ event depends on the **Card Creation** setting:

- **At campaign launch:** The send is logged at the scheduled send time, when the card is written to the user's feed. This happens regardless of whether the user has opened the app or viewed the card.
- **At first impression:** The send is logged the first time the app requests the card after the scheduled send time, when the card is created on demand.

If your campaign is configured to use **At first impression** (recommended), the _Sent_ count in campaign analytics grows gradually as individual apps request the card. If the app never requests a card (such as, a user never opens the app) before the card expires, no send is recorded, and the card is never delivered. If your campaign is configured to use **At campaign launch**, the _Sent_ count in campaign analytics spikes at the scheduled time.

### Action-based delivery

For action-based Content Cards, the send is logged shortly after the user performs the triggering action, when the card is written to their feed. This happens regardless of whether the user has viewed the card.

### Campaigns Received and retargeting filters

Regardless of the delivery type or **Card Creation** setting, a Content Card campaign appears in the user's profile under **Campaigns Received** only after they have actually viewed the card in the app. The **Last Received Any Message** and **Last Received Campaign** retargeting filters update at view time for the same reason.

{% multi_lang_include analytics/campaign_analytics.md channel="Content Card" %}
