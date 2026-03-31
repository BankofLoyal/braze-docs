---
nav_title: Preferencias de correo electrónico
article_title: Preferencias de correo electrónico
page_type: reference
page_order: 14
description: "Este artículo de referencia trata sobre las preferencias de correo electrónico en el panel de Braze, incluidas las configuraciones de envío, los píxeles de seguimiento de apertura, la página de suscripción y los pies de página, etc."
tool: Dashboard
channel: email
toc_headers: h2

---

# Preferencias de correo electrónico

> Preferencias de correo electrónico es donde puedes establecer la configuración específica del correo electrónico saliente, como pies de página personalizados, páginas de adhesión voluntaria y de exclusión personalizadas, etc. Incluir estas opciones en tus correos electrónicos salientes proporciona una experiencia fluida y coherente a tus usuarios.

**Las preferencias de correo electrónico** se encuentran en la sección **Configuración** del dashboard.

## Configuración de envío

Los ajustes de correo electrónico en la sección **Configuración de envío** determinan qué detalles se incluyen en tus campañas de correo electrónico. En concreto, estos ajustes están relacionados principalmente con lo que el usuario ve cuando recibe un correo electrónico de Braze.

### Configuración del correo electrónico saliente

Al configurar tus ajustes de correo electrónico, tus ajustes de correo electrónico saliente identifican qué nombre y direcciones de correo electrónico se utilizan cuando Braze envía correos electrónicos a tus usuarios.

{% tabs local %}
{% tab Display Name Address %}

En esta sección, puedes añadir los nombres y las direcciones de correo electrónico que puedes utilizar cuando Braze envía correos electrónicos a tus usuarios. Los nombres para mostrar y las direcciones de correo electrónico están disponibles en las opciones **Editar información de envío** mientras redactas tu campaña de correo electrónico. Ten en cuenta que las actualizaciones realizadas en la configuración del correo electrónico saliente no afectan retroactivamente a los envíos existentes.

![Sección «Configuración del correo electrónico saliente» con campos para diferentes nombres de usuario y dominios.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Personalización con Liquid

También puedes utilizar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) en los campos **De: nombre para mostrar**, **Parte local** y **Dominio** para crear plantillas dinámicas del nombre del remitente y la dirección de correo electrónico basadas en atributos personalizados. Ten en cuenta que para usar Liquid en el campo **Dominio**, debes ir a las opciones de **Información de envío** de una campaña de correo electrónico y seleccionar la casilla **Personalizar nombre para mostrar + dirección del remitente**.

![Configuración de envío con campos para personalizar el nombre para mostrar del remitente, la dirección y el dominio.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

Por ejemplo, puedes utilizar la lógica condicional para enviar desde diferentes marcas o regiones:

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

Si añades una dirección de correo electrónico en esta sección, podrás seleccionarla como dirección de respuesta para tu campaña de correo electrónico. También puedes hacer que una dirección de correo electrónico sea la predeterminada seleccionando **Hacer predeterminada**. Estas direcciones de correo electrónico estarán disponibles en las opciones de **Editar información de envío** cuando redactes tu campaña de correo electrónico.

![Sección «Dirección para responder a» con campos para introducir varias direcciones para responder a mensajes.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Personalización con Liquid

También puedes utilizar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) en el campo **Dirección de respuesta** para crear dinámicamente una plantilla de la dirección de respuesta basada en atributos personalizados. Por ejemplo, puedes utilizar la lógica condicional para enviar respuestas a diferentes regiones o departamentos:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@company.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@company.com" %}
{% else %}
{% assign address = "global-support@company.com" %}{% endif %}{{address}}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

Esta sección te permite administrar las direcciones CCO que puedes añadir a los mensajes de correo electrónico salientes enviados desde Braze. Al añadir una dirección CCO a un mensaje de correo electrónico, se envía una copia idéntica del mensaje que recibe el usuario a tu buzón de entrada CCO. Esta es una herramienta útil para conservar copias de los mensajes que has enviado a tus usuarios por motivos de cumplimiento normativo o cuestiones relacionadas con la atención al cliente. Los correos electrónicos CCO no se incluyen en los informes ni en los análisis de correo electrónico.

Las direcciones CCO solo están disponibles para SendGrid y SparkPost. Como alternativa a las direcciones CCO, recomendamos utilizar [el archivado de mensajería]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) para guardar una copia de los mensajes enviados a los usuarios con fines de archivo o cumplimiento normativo.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

![Sección «Dirección CCO» de la pestaña «Configuración del correo electrónico».]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Después de añadir una dirección, esta estará disponible para seleccionarla al redactar un correo electrónico, ya sea en campañas o en pasos en Canvas. Selecciona **Establecer como predeterminada** junto a una dirección para establecer que esta dirección se seleccione por defecto al iniciar una nueva campaña de correo electrónico o componente Canvas. Para anular esta opción a nivel de mensaje, puedes seleccionar **Sin CCO** al configurar el mensaje.

Si necesitas que todos los mensajes de correo electrónico enviados desde Braze incluyan una dirección CCO, puedes alternar la opción **Requerir una dirección CCO para todas tus campañas de correo electrónico**. Para ello, deberás seleccionar una dirección predeterminada, que se seleccionará automáticamente en las nuevas campañas de correo electrónico o en los pasos en Canvas. La dirección predeterminada también se añadirá automáticamente a todos los mensajes activados a través de nuestra API REST. No es necesario modificar la solicitud API existente para incluir la dirección.

#### CCO dinámico

Con el CCO dinámico, puedes utilizar Liquid en tu dirección CCO. Ten en cuenta que esta característica solo está disponible en **Preferencias de correo electrónico** y no se puede configurar en la propia campaña. Solo se permite una dirección CCO por destinatario de correo electrónico.

Por ejemplo, puedes añadir {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} como dirección CCO para los correos electrónicos de tu equipo de soporte.

![Sección «Dirección CCO» de la pestaña «Configuración de correo electrónico» con una dirección CCO utilizando Liquid.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Píxel de seguimiento de apertura

[![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

El píxel de seguimiento de apertura de correo electrónico es una imagen invisible de 1 x 1&nbsp;px que se inserta automáticamente en el HTML de tu correo electrónico. Este píxel ayuda a Braze a detectar si tus usuarios han abierto tu correo electrónico. Cuando el cliente de correo electrónico de un usuario realiza una solicitud a nuestro píxel de seguimiento, la solicitud puede contener información como la dirección IP, el agente de usuario y la marca de tiempo. La información sobre las aperturas de correo electrónico puede ser muy útil, ya que te ayuda a determinar estrategias de marketing eficaces al comprender las tasas de apertura correspondientes.

### Colocación del píxel de seguimiento

El comportamiento predeterminado de Braze es añadir el píxel de seguimiento en la parte inferior del correo electrónico. Para la mayoría de los usuarios, este es el lugar ideal para colocar el píxel. Aunque el píxel ya está diseñado para provocar los menores cambios visuales posibles, cualquier cambio visual involuntario sería lo menos visible en la parte inferior de un correo electrónico. Este es también el valor predeterminado para los proveedores de correo electrónico como SendGrid y SparkPost.

### Cambiar la ubicación del píxel de seguimiento

Actualmente, Braze permite anular la ubicación predeterminada del píxel de seguimiento de apertura del ESP (la última etiqueta en el `<body>` de un correo electrónico) para moverlo a la primera etiqueta en el `<body>`.
  
![Sección «Píxel de seguimiento de apertura» con las opciones de mover para SendGrid, SparkPost o Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Para cambiar la ubicación:

1. En Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona una de las siguientes opciones: **Mover para SendGrid**, **Mover para SparkPost** o **Mover para Amazon SES**
3. Selecciona **Guardar**.

Después de guardar, Braze envía instrucciones especiales al ESP para colocar el píxel de seguimiento de apertura en la parte superior de todos los correos electrónicos HTML.
  
{% alert important %} 
La habilitación de SSL envuelve la URL del píxel de seguimiento con HTTPS en lugar de HTTP. Si tu SSL está mal configurado, puede afectar a la eficacia del píxel de seguimiento. 
{% endalert %}

## Encabezado de cancelar suscripción a la lista {#list-unsubscribe}

{% alert note %}
Desde el 15 de febrero de 2024, las nuevas empresas tienen habilitado de forma predeterminada el encabezado «list-unsubscribe» (con cancelación de suscripción con un solo clic).
{% endalert %}

El uso de un encabezado de cancelación de suscripción a la lista permite a los destinatarios darse de baja fácilmente de los correos electrónicos de marketing mostrando un botón de **Cancelar suscripción** en la interfaz de usuario del buzón, y no en el cuerpo del mensaje.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Cuando un destinatario selecciona **Cancelar suscripción**, el proveedor de correo electrónico envía la solicitud de cancelación de suscripción al destino definido en el encabezado del correo electrónico.

Habilitar la cancelación de suscripción a la lista es una práctica recomendada de capacidad de entrega y un requisito de algunos de los principales proveedores de buzones de correo. Anima a los usuarios finales a eliminar de forma segura los mensajes no deseados, en lugar de pulsar el botón de correo no deseado en un cliente de correo electrónico, lo que perjudica la reputación del remitente y la capacidad de entrega de los correos electrónicos.

Al [administrar tus suscripciones en Gmail](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC), Gmail también puede extraer el enlace para cancelar la suscripción del cuerpo del mensaje, pero da prioridad al list-unsubscribe si aparece en el encabezado.

### Soporte del proveedor de buzones

La siguiente tabla resume la compatibilidad del proveedor de buzones con el encabezado "mailto:", la URL de cancelar suscripción a la lista y la cancelación de suscripción con un solo clic ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Encabezado de cancelar suscripción a la lista | Mailto: encabezado | URL de cancelación de suscripción | Cancelar suscripción con un clic (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Compatible* | Compatible | Compatible |
| Gmail móvil | No compatible | No compatible | No compatible |
| Apple Mail | Compatible | No compatible | No compatible |
| Outlook.com | Compatible | No compatible | No compatible |
| Yahoo! Mail | Compatible* | No compatible | Compatible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_*Yahoo y Gmail van a dejar de usar el encabezado "mailto:" y solo admitirán el clic único._

La visualización del encabezado la determina en última instancia el proveedor del buzón. Para comprobar si el encabezado de cancelación de suscripción está incluido en el correo electrónico sin formato (texto) del destinatario en Gmail, haz lo siguiente:

1. Selecciona **Mostrar original** en el correo electrónico. Esto abre una nueva pestaña con la versión sin procesar del correo electrónico y sus encabezados.
2. Busca "List-Unsubscribe".

Si el encabezado está en la versión sin procesar del correo electrónico pero no se muestra, el proveedor del buzón ha decidido no mostrar la opción para cancelar la suscripción, lo que significa que no tenemos más información sobre por qué el proveedor del buzón no muestra el encabezado. Ver el encabezado de cancelar suscripción a la lista se basa, en última instancia, en la reputación. En la mayoría de los casos, cuanto mejor sea tu reputación del remitente ante el proveedor de correo electrónico, más probable será que aparezca el encabezado list-unsubscribe.

### Encabezado de cancelación de suscripción de correo electrónico en los espacios de trabajo

![Seleccionar los «usuarios suscriptores o que han realizado una adhesión voluntaria» a los que enviar el mensaje.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Cuando la característica de encabezado para cancelar la suscripción al correo electrónico está activada, esta configuración se aplica a todo el espacio de trabajo, no a nivel de empresa. Se añade a las campañas y Canvas que se configuran para enviarse a los usuarios suscriptores o que han dado su adhesión voluntaria, o a los usuarios que han dado su adhesión voluntaria en el paso **Audiencia objetivo** de los creadores de campañas y Canvas.

Cuando se utiliza la «configuración predeterminada del espacio de trabajo», Braze no añade el encabezado para cancelar la suscripción con un solo clic para las campañas que se consideran transaccionales, las cuales están configuradas para «enviar a todos los usuarios, incluidos los usuarios que han cancelado la suscripción». Para anular esto y añadir el encabezado de cancelación de suscripción con un solo clic al enviar mensajes a usuarios que se han dado de baja, puedes seleccionar **Cancelar suscripción globalmente de todos los correos electrónicos** en la configuración de cancelación de suscripción con un solo clic a nivel de mensaje.

### Encabezado predeterminado de cancelación de suscripción a la lista

{% alert important %}
Gmail pretende que los remitentes implementen la cancelación de suscripción con un solo clic para todos sus mensajes comerciales y promocionales salientes a partir del 1 de junio de 2024. Para obtener más información, consulta [las directrices para remitentes de Gmail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) y [las preguntas frecuentes sobre directrices para remitentes de correo electrónico de Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo anunció un plazo de principios de 2024 para los requisitos de actualización. Para obtener más información, consulta [Más seguridad, menos correo no deseado: aplicación de las normas de correo electrónico para mejorar la experiencia](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Para utilizar la característica de cancelación de suscripción de Braze y procesar las cancelaciones directamente, selecciona **Incluir un encabezado de correo electrónico de cancelación de suscripción con un solo clic (mailto y HTTP) para los correos electrónicos enviados a usuarios suscritos o que hayan dado su adhesión voluntaria**, y selecciona **Braze predeterminado** como la URL y el correo electrónico estándar de Braze. 

![Opción para incluir automáticamente un encabezado para cancelar la suscripción a la lista en los correos electrónicos enviados a usuarios suscriptores o que han dado su adhesión voluntaria.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze admite las siguientes versiones del encabezado list-unsubscribe:

| Versión de cancelar suscripción a la lista | Descripción | 
| ----- | --- |
| Un clic (RFC 8058) | Ofrece a los destinatarios una forma sencilla de darse de baja de los correos electrónicos con un solo clic. Este es un requisito de Yahoo y Gmail para los remitentes masivos. |
| URL o HTTPS para cancelar suscripción a la lista | Proporciona a los destinatarios un enlace que les dirige a una página web donde pueden darse de baja. |
| Mailto | Especifica una dirección de correo electrónico como destino para el mensaje de solicitud de cancelación de suscripción que el destinatario enviará a la marca. <br><br> _Para procesar las solicitudes de cancelación de suscripción a listas de correo, dichas solicitudes deben incluir la dirección de correo electrónico almacenada en Braze del usuario final que desea cancelar la suscripción. Esto puede proporcionarse mediante la «dirección de origen» del correo electrónico desde el que el usuario final cancela la suscripción, el asunto codificado o el cuerpo codificado del correo electrónico recibido por el usuario final del que cancela la suscripción. En casos muy limitados, algunos proveedores de buzones de entrada no cumplen con el protocolo [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), lo que provoca que la dirección de correo electrónico no se transmita correctamente. Esto puede provocar que una solicitud de cancelación de suscripción no pueda procesarse en Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cuando Braze recibe una solicitud de cancelación de suscripción de un usuario a través de cualquiera de los métodos anteriores, el estado global de suscripción de correo electrónico de este usuario se establece como cancelado. Si no hay ninguna coincidencia, Braze no procesa esta solicitud.

### Cancelar suscripción con un clic

El uso de la cancelación de suscripción con un solo clic para el encabezado list-unsubscribe ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) se centra en proporcionar a los destinatarios una forma sencilla de darse de baja de los correos electrónicos.

### Cancelación de suscripción con un solo clic a nivel de mensaje

La configuración de cancelación de suscripción con un solo clic a nivel de mensaje anula la característica de encabezado de cancelación de suscripción de correo electrónico establecida para los espacios de trabajo. Aplica el comportamiento de cancelación de suscripción con un solo clic por campaña o paso en Canvas para los siguientes usos:

- Añadir una cancelación de suscripción con un clic de Braze para un grupo de suscripción específico para admitir múltiples marcas/listas dentro de un espacio de trabajo
- Alternar entre la URL de cancelación de suscripción predeterminada de Braze o la personalizada
- Añadir tu URL personalizada de cancelación de suscripción con un solo clic
- Omitir la cancelación de suscripción con un clic en este mensaje

{% alert note %}
La configuración para cancelar la suscripción con un solo clic a nivel de mensaje solo está disponible cuando se utiliza el editor de arrastrar y soltar y el editor HTML actualizado. Si utilizas el editor HTML anterior, cambia al editor HTML actualizado para usar esta función.
{% endalert %}

En tu editor de correo electrónico, ve a **Configuración de envío** > **Información de envío**. Selecciona una de las siguientes opciones:

- **Usar el espacio de trabajo predeterminado**: Utiliza la configuración del **Encabezado de cancelación de suscripción de correo electrónico** establecida en **Preferencias de correo electrónico**. Cualquier cambio que realices en esta configuración se aplicará a todos los mensajes.
- **Cancelar suscripción globalmente de todos los correos electrónicos**: Utiliza el encabezado predeterminado de Braze para cancelar suscripción con un clic. Los usuarios que hacen clic en el botón para cancelar la suscripción tienen su estado de suscripción global de correo electrónico establecido en «Cancelada».
- **Cancelar suscripción de un grupo de suscripción específico**: Utiliza el grupo de suscripción especificado. Braze cancela la suscripción de los usuarios que hacen clic en el botón de cancelación de suscripción del grupo de suscripción seleccionado.
    - Al seleccionar un grupo de suscripción, añade el filtro **Grupo de suscripción** en **Audiencia objetivo** para dirigirte únicamente a los usuarios suscritos a este grupo específico. El grupo de suscripción seleccionado para cancelar la suscripción con un clic debe coincidir con el grupo de suscripción al que te diriges. Si hay una discrepancia en el grupo de suscripción, corres el riesgo de enviar mensajes a un usuario que está intentando cancelar la suscripción a un grupo de suscripción del que ya se ha dado de baja.

{% alert important %}
La configuración **Cancelar suscripción de un grupo de suscripción específico** solo se aplica al encabezado de cancelación de suscripción con un solo clic. El encabezado mailto list-unsubscribe no se ve afectado al seleccionar esta opción. Esto significa que un destinatario que cancela la suscripción utilizando este método registra una cancelación global, no una cancelación del grupo de suscripción específico. Para excluir el encabezado mailto list-unsubscribe de la cancelación global de suscripción de los usuarios, cuando selecciones esta configuración, ponte en contacto con [soporte]({{site.baseurl}}/support_contact/).
{% endalert %}

- **Personalizado:** Añade tu URL personalizada de cancelación de suscripción con un solo clic para que puedas procesar las cancelaciones directamente.
- **Excluir cancelación de suscripción**

{% alert important %}
La exclusión de la cancelación de suscripción con un solo clic o de cualquier mecanismo de cancelación de suscripción solo debe hacerse para la mensajería transaccional, como el restablecimiento de contraseñas, los recibos y los correos electrónicos de confirmación.
{% endalert %}

Al ajustar esta configuración, se anula el comportamiento predeterminado para cancelar la suscripción a la lista con un solo clic en este correo electrónico.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Requisitos

Si envías correos electrónicos utilizando tu propia funcionalidad de cancelación de suscripción personalizada, debes cumplir los siguientes requisitos para asegurarte de que la URL de cancelación de suscripción con un solo clic que has configurado cumple con la RFC 8058:

* La URL debe poder gestionar las solicitudes POST de cancelación de suscripción.
* La URL debe empezar por `https://`.
* La URL no debe devolver una redirección HTTPS ni un cuerpo. Los enlaces para darse de baja con un solo clic que dirigen a una página de destino u otro tipo de página web no cumplen con la RFC 8058.
* Las solicitudes POST no deben establecer cookies.

Selecciona **Encabezado de cancelación de suscripción de lista personalizado** para añadir tu propio punto de conexión de cancelación de suscripción con un solo clic configurado y un "mailto:" opcional. Braze requiere una entrada para la URL para admitir un encabezado de cancelación de suscripción personalizado porque la cancelación de suscripción HTTP con un solo clic es un requisito de Yahoo y Gmail para los remitentes masivos.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Añadir texto a las líneas de asunto del correo electrónico

Usa el botón para incluir "[TEST]" y "[SEED]" en las líneas del asunto de tus correos electrónicos de prueba y semilla. Esto puede ayudar a identificar cualquier campaña de correo electrónico enviada como prueba.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## CSS en línea en los nuevos correos electrónicos por defecto

El CSS en línea es una técnica que aplica automáticamente estilos CSS en línea para tus correos electrónicos y nuevos correos. En algunos clientes de correo electrónico, esto puede mejorar la presentación de tus correos electrónicos.

Cambiar esta configuración no afecta a ninguno de tus mensajes de correo electrónico o plantillas existentes. Puedes sustituir este valor predeterminado en cualquier momento mientras creas mensajes o plantillas. Para obtener más información, consulta [CSS en línea]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/).

## Volver a suscribir a los usuarios cuando cambie su dirección de correo electrónico

Puedes volver a suscribir automáticamente a los usuarios cuando cambien su dirección de correo electrónico. Por ejemplo, si un usuario del espacio de trabajo que había cancelado la suscripción cambia su dirección de correo electrónico por otra que no figura en la lista de cancelación de suscripción de Braze, se volverá a suscribir automáticamente.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Páginas de suscripción y pies de página

{% tabs local %}
{% tab Custom Footer %}

En el caso de los correos electrónicos comerciales, la [Ley CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que todos los correos comerciales incluyan una opción para darse de baja. Con la configuración personalizada del pie de página, puedes seguir cumpliendo con la normativa CAN-SPAM a la vez que personalizas tu pie de página de exclusión de correo electrónico. Para seguir cumpliendo la normativa, debes añadir tu pie de página personalizado a todos los correos electrónicos enviados como parte de las campañas de este espacio de trabajo.

Ten en cuenta los siguientes requisitos al crear un pie de página personalizado para tus mensajes de correo electrónico:
- Debe incluir una URL para darse de baja y una dirección postal física.
- Debe ser inferior a 100 KB.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Para obtener más información sobre las plantillas personalizadas para el pie de página con Liquid, consulta nuestra documentación sobre [Pies de página personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze te permite configurar una **Página de cancelación de suscripción personalizada** con tu propio HTML. Esta página aparece después de que un usuario haya seleccionado cancelar la suscripción en la parte inferior de un correo electrónico. Ten en cuenta que esta página debe ocupar menos de 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Obtén más información sobre las mejores prácticas para la gestión de listas de correo electrónico en [Gestión de suscripciones de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

Puedes crear una página de adhesión voluntaria personalizada utilizando tu propio HTML. Incluir esto en tu correo electrónico puede ser especialmente beneficioso si deseas que tu marca y tu mensaje permanezcan coherentes durante todo el ciclo de vida del usuario. Ten en cuenta que esta página debe ocupar menos de 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Obtén más información sobre las mejores prácticas para la gestión de listas de correo electrónico en [Gestión de suscripciones de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

{% alert tip %}
En la sección **Vista previa** de una página de suscripción o pie de página, selecciona **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestra cómo se ve el pie de página del correo electrónico, la página para cancelar la suscripción o la página de adhesión voluntaria para un usuario aleatorio. El enlace tiene una validez de siete días antes de que sea necesario volver a generarlo.
{% endalert %}

## Preguntas frecuentes

### Cancelar suscripción con un clic

{% details ¿Puede la URL de cancelación de suscripción con un clic (a través del encabezado list-unsubscribe) enlazar a un centro de preferencias? %}
No, eso no se ajusta a la RFC 8058, lo que significa que no cumplirás el requisito de cancelar suscripción con un clic de Yahoo y Gmail.
{% enddetails %}

{% details ¿Por qué recibo el mensaje de error "El cuerpo de tu correo electrónico no incluye un enlace para cancelar la suscripción" al redactar mi centro de preferencias? %}
Un centro de preferencias no se considera un enlace para cancelar suscripción. Los destinatarios de tus correos electrónicos deben tener la opción de darse de baja de cualquier correo electrónico comercial para seguir cumpliendo la normativa CAN-SPAM.
{% enddetails %}

{% details ¿Necesito editar las campañas de correo electrónico y Canvas anteriores para aplicar la configuración de cancelación de suscripción con un solo clic después de habilitarla? %}
Si no tienes ninguno de los casos de uso para la configuración de cancelación de suscripción con un solo clic a nivel de mensaje, no es necesario realizar ninguna acción siempre que la configuración esté activada en **Preferencias de correo electrónico**. Braze añade automáticamente encabezados para cancelar la suscripción con un solo clic a todos los mensajes promocionales y de marketing salientes. Sin embargo, si necesitas configurar la función de cancelación de suscripción con un solo clic para cada mensaje, tendrás que actualizar las campañas anteriores y los pasos en Canvas con el correo electrónico correspondiente.
{% enddetails %}

{% details Puedo ver el encabezado list-unsubscribe y de cancelación de suscripción con un solo clic en el mensaje original o en los datos sin procesar, pero ¿por qué no veo el botón Cancelar suscripción en Gmail o Yahoo? %}
Gmail y Yahoo deciden en última instancia si mostrar o no el encabezado de cancelación de suscripción a la lista o con un solo clic. En el caso de los nuevos remitentes o de los remitentes con baja reputación del remitente, esto puede provocar en ocasiones que no se muestre el botón para cancelar la suscripción. 
{% enddetails %}

{% details ¿El encabezado personalizado de cancelación de suscripción con un solo clic admite Liquid? %}
Sí, Liquid y la lógica condicional son compatibles para permitir URL dinámicas de cancelación de suscripción con un solo clic para el encabezado.
{% enddetails %}

{% alert tip %}
Si añades lógica condicional, evita que los valores de salida añadan espacios en blanco a tu URL, ya que Braze no elimina estos espacios en blanco.
{% endalert %}

### Cancelación de suscripción con un solo clic a nivel de mensaje

{% details Si añado manualmente los encabezados de correo electrónico para un solo clic y tengo activado el encabezado de cancelación de suscripción de correo electrónico, ¿cuál es el comportamiento esperado? %}
Los encabezados de correo electrónico añadidos para cancelar la suscripción con un solo clic se aplican a todos los envíos futuros de esta campaña.
{% enddetails %}

{% details ¿Por qué los grupos de suscripción deben coincidir en todas las variantes de mensaje para poder lanzar la campaña? %}
Para una campaña con pruebas A/B, Braze envía aleatoriamente a un usuario una de las variantes. Si tienes dos grupos de suscripción diferentes configurados en la misma campaña (la variante A está configurada para el grupo de suscripción A y la variante B está configurada para el grupo de suscripción B), no podemos garantizar que los usuarios que solo están suscritos al grupo de suscripción B reciban la variante B. Puede darse el caso de que los usuarios cancelen la suscripción a un grupo de suscripción del que ya se han dado de baja.
{% enddetails %}

{% details La configuración del encabezado de cancelación de suscripción de correo electrónico está desactivada en Preferencias de correo electrónico, pero en la información de envío de mi campaña, la configuración de cancelación de suscripción con un solo clic está establecida en "Usar el espacio de trabajo predeterminado". ¿Es un error? %}
No. Si la configuración del espacio de trabajo está desactivada y la configuración de mensajes está establecida en **Usar el espacio de trabajo predeterminado**, Braze sigue lo que está configurado en **Preferencias de correo electrónico**. Esto significa que no añadimos el encabezado para cancelar la suscripción con un solo clic para la campaña.
{% enddetails %}

{% details ¿Qué sucede si se archiva un grupo de suscripción? ¿Esto afecta a la cancelación de suscripción con un solo clic en los correos electrónicos enviados? %}
Si se archiva un grupo de suscripción al que se hace referencia en **Información de envío** para un solo clic, Braze sigue procesando las cancelaciones de suscripción de un solo clic. El grupo de suscripción ya no aparece en el dashboard (filtro de segmentos, perfil de usuario y áreas similares).
{% enddetails %}

{% details ¿La configuración de cancelación de suscripción con un solo clic está disponible para las plantillas de correo electrónico? %}
No, actualmente no tenemos planes de añadir esta función a las plantillas de correo electrónico, ya que estas plantillas no están asignadas a un dominio de envío. Si te interesa esta función para las plantillas de correo electrónico, envía [comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details ¿Esta función comprueba que la URL de cancelación de suscripción con un solo clic añadida a la opción personalizada sea válida? %}
No, no comprobamos ni validamos ningún enlace en el dashboard de Braze. Asegúrate de probar correctamente tu URL antes del lanzamiento.
{% enddetails %}