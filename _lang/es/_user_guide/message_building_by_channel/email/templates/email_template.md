---
nav_title: Crear una plantilla de correo electrónico
article_title: Crear una plantilla de correo electrónico
page_order: 0
description: "Este artículo de referencia explica cómo crear, personalizar y gestionar plantillas de correo electrónico."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Crear una plantilla de correo electrónico

> El panel de Braze cuenta con un editor de plantillas de correo electrónico que te permite crear correos personalizados y llamativos y guardarlos para utilizarlos posteriormente en campañas. También puedes cargar tu propia [plantilla de correo electrónico HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/).

## Paso 1: Navega al editor de plantillas de correo electrónico

Ve a **Plantillas** > **Plantillas de correo electrónico**.

## Paso 2: Selecciona tu experiencia de edición 

Selecciona entre **el editor de arrastrar y soltar** o **el editor HTML** para tu experiencia de edición. 

A continuación, puedes elegir entre plantillas prediseñadas de Braze, crear una plantilla nueva o editar una plantilla existente (simple o [receptiva para móviles]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)).

![Una plantilla de correo electrónico para las rebajas de primavera de una empresa con opciones para seleccionar el editor de arrastrar y soltar o el editor HTML, o para seleccionar entre las plantillas de Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Cualquier plantilla HTML personalizada existente tendrá que volver a crearse utilizando el editor de arrastrar y soltar.
{% endalert %}

## Paso 3: Personaliza tu plantilla

Después de seleccionar tu experiencia de edición, esta es tu oportunidad para ser creativo con la personalización de tu plantilla de correo electrónico. Puedes utilizar HTML para crear y emular tu marca en el editor HTML, o incluir una variedad de [detalles creativos]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) en el editor de arrastrar y soltar.

### Incluir un enlace para cancelar suscripción

Cuando diseñes tu plantilla de correo electrónico, si no incluyes un enlace de cancelación de suscripción, Braze te pedirá que lo añadas en tu correo electrónico, ya que es obligatorio por ley en todos los correos electrónicos de marketing. Puedes añadir este enlace de cancelación de suscripción como pie de página en la parte inferior de tus correos electrónicos utilizando la etiqueta de Liquid {% raw %}``${email_footer}``{% endraw %}, o [personalizando el pie de página]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) en tu plantilla.

## Paso 4: Comprueba si hay errores en el correo electrónico

Los errores de correo electrónico se presentan en la pestaña **Redactar** del flujo de trabajo del mensaje. Los errores te impiden avanzar. Las "advertencias" indican recordatorios para ayudarte a seguir las mejores prácticas. Dependiendo de tu negocio, puedes optar por ignorarlas.

![Lista de errores y advertencias de un correo electrónico de ejemplo.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Aquí tienes una lista de errores que se tienen en cuenta en nuestro editor:

- Sintaxis incorrecta de Liquid
- [Cuerpos de correo electrónico superiores a 400 kb; se recomienda encarecidamente que los cuerpos sean inferiores a 102 kb]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- Plantillas sin enlace para cancelar suscripción
- Correos electrónicos con el **cuerpo** o el **asunto** en blanco
- Correos electrónicos sin enlace para cancelar suscripción

## Paso 5: Previsualiza y prueba tu mensaje

Cuando termines de componer tu plantilla, puedes probarla antes de enviarla.

En la parte inferior de la pantalla de resumen, selecciona **Vista previa y prueba**. Aquí puedes previsualizar cómo aparecerá tu correo electrónico en el buzón de entrada de un cliente. Con la opción **Previsualizar como usuario** seleccionada, puedes previsualizar tu correo electrónico como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto te permite comprobar que tu contenido conectado y las llamadas de personalización funcionan como deberían. 

A continuación, puedes **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario cualquiera. El enlace durará siete días antes de que sea necesario regenerarlo.

También puedes alternar entre las vistas de escritorio, móvil y texto sin formato para hacerte una idea de cómo aparecerá tu mensaje en diferentes contextos.

{% alert tip %}
¿Tienes curiosidad por saber cómo se ve tu correo electrónico para los usuarios del modo oscuro? Selecciona el conmutador **Vista previa en modo oscuro** situado en la sección **Vista previa y prueba** (solo en el editor de arrastrar y soltar).
{% endalert %}

Cuando estés listo para una comprobación final, selecciona **Probar envío** y envía un mensaje de prueba a ti mismo o a un grupo de evaluadores de contenido para asegurarte de que tu correo electrónico se muestra correctamente en una variedad de dispositivos y clientes de correo electrónico.

![Ejemplo de vista previa de correo electrónico que se enviará para realizar pruebas.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si ves algún problema con tu plantilla o quieres hacer algún cambio, selecciona **Editar correo electrónico** para volver al editor.

## Paso 6: Guarda tu plantilla

Asegúrate de guardar tu plantilla seleccionando **Guardar plantilla**. Ahora estás listo para utilizar esta plantilla en cualquier campaña o componente Canvas que elijas. Para acceder a tu plantilla, selecciona la experiencia de edición con la que la creaste y, a continuación, selecciónala en la lista de plantillas disponibles.

{% alert note %}
Si modificas una plantilla existente, los cambios no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

### Gestión de plantillas

Puedes ver las plantillas de correo electrónico en **Plantillas** > **Plantillas de correo electrónico**, filtrando por estado, tipo o etiquetas, o buscando por nombre. Necesitas el permiso **Acceder a campañas, Canvas, Content Cards, bloques de contenido, conmutadores de características, segmentos, biblioteca de medios, ubicaciones, códigos promocionales y centros de preferencias** (o el permiso granular equivalente, como **Ver plantillas de correo electrónico**) para ver estas plantillas. Para más detalles, consulta [Permisos de usuario]({{site.baseurl}}/user_guide/administrative/access_braze/user_permissions/).

A medida que crees más plantillas de correo electrónico, podrás [duplicarlas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) y [archivarlas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Obtén más información en [Plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Utilización de tus plantillas en campañas API

Para utilizar tu correo electrónico en una campaña API, necesitas un `email_template_id`, que puedes encontrar en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

![Identificador de API situado en la parte inferior de una plantilla de correo electrónico.]({% image_buster /assets/img/email_templates/template5.png %})

### Comentarios sobre las plantillas de correo electrónico

Puedes colaborar y comentar plantillas de correo electrónico en el editor de arrastrar y soltar. 

1. Selecciona el bloque de contenido o la fila del cuerpo del correo electrónico que quieras comentar.
2. Selecciona el icono de comentario <i class="fas fa-comment"></i>.
3. Introduce tu comentario en la barra lateral y, a continuación, selecciona **Enviar**.
4. Después de introducir tus comentarios, selecciona **Hecho**.
5. Selecciona **Guardar plantilla** para guardar tus comentarios.

Una vez guardada la plantilla, los usuarios pueden ver iconos sobre los comentarios sin resolver. Selecciona **Resolver** para resolver estos comentarios.

![Un comentario de plantilla de correo electrónico que dice "Me parece bien".]({% image_buster /assets/img/email_templates/template_comment.png %})

Para obtener respuestas a las preguntas más frecuentes sobre plantillas de correo electrónico, consulta nuestras [Preguntas frecuentes sobre plantillas]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).