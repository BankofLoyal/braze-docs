Before creating WhatsApp templates, you must complete the [WhatsApp setup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) and have:
- An active WhatsApp Business Account (WABA) connected to Braze
- Appropriate subscription groups configured within your WABA
- Media assets (images or videos) ready for upload
- Braze permissions for non-admin users
    - For users to create new templates in the Template Builder:
        - "View WhatsApp Message Templates"
        - "Edit WhatsApp Message Templates"
    - For users to compose campaigns or Canvases with carousel templates:
        - "View WhatsApp Message Templates"
- An understanding of Liquid templating (optional, for dynamic content)

{% alert important %}
All phone numbers and subscription groups within the same WhatsApp Business Account (WABA) share templates. If you have multiple subscription groups within one WABA, they can all access the same carousel templates; however, templates are not shared across different WABAs.
{% endalert %}