---
nav_title: Crear un mensaje de KakaoTalk
article_title: "Crear un mensaje de KakaoTalk"
description: "Este artículo de referencia describe cómo crear un mensaje de KakaoTalk."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# Crear un mensaje de KakaoTalk

> Usa el [canal de mensajería KakaoTalk]({{site.baseurl}}/kakaotalk/) para llegar directamente a los usuarios a través de la plataforma KakaoTalk. Crea una experiencia de usuario personalizada utilizando Liquid y otro contenido dinámico para construir un entorno que fomente y mejore una experiencia de usuario enriquecida con tu marca.<br><br>Para configurar tu canal de mensajería KakaoTalk, consulta [Configurar KakaoTalk]({{site.baseurl}}/kakaotalk_setup/).

## Paso 1: Elige dónde crear tu mensaje

KakaoTalk es compatible tanto con campañas como con Canvas. Las campañas son más adecuadas para campañas de mensajería únicas, mientras que Canvas te permite orquestar recorridos de usuario multicanal y de varios pasos.

{% tabs local %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **KakaoTalk** para una campaña de un solo canal, o **Campaña multicanal** para una campaña de múltiples canales.

![Panel con opciones para seleccionar el canal de mensajería.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Puedes añadir variantes adicionales a tu campaña, lo que te permite elegir diferentes tipos de mensajes y diseños. Para más información, consulta [Pruebas multivariante y pruebas A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/).

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. Añade un paso de mensaje en el constructor de Canvas y selecciona **KakaoTalk**.

![Selecciones de canal de mensajería en Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## Paso 2: Redacta tu mensaje de KakaoTalk

1. Selecciona el desplegable **Canal de KakaoTalk**, que muestra una lista de canales de KakaoTalk que has configurado a través de la página de socios tecnológicos, y selecciona el canal de KakaoTalk que deseas usar para enviar el mensaje.
2. Selecciona el tipo de mensaje a enviar:
- Texto
- Imagen
- Elemento de lista
    - Estrecho
    - Ancho

![Sección de variantes de KakaoTalk con tres tipos de mensajes para seleccionar.]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

{% tabs local %}
{% tab Text %}

Un mensaje de texto de KakaoTalk es la forma más sencilla de comunicación: un mensaje de texto estándar.

### Especificaciones

| Área | Especificaciones |
| --- | --- |
| Contenido | Contenido de texto, incluyendo emojis y personalización con Liquid |
| Capacidad de texto | Hasta 1000 caracteres |
| Botones | Hasta 5 botones opcionales. Actualmente, solo se pueden usar para abrir una URL al hacer clic. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Un mensaje de texto de KakaoTalk en el compositor.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Image %}

Una imagen es un mensaje que combina un elemento visual con texto de apoyo. Braze gestiona automáticamente la carga de la imagen a los servidores de KakaoTalk.

### Especificaciones generales

| Área | Especificaciones |
| --- | --- |
| Contenido | Una imagen y texto de apoyo |
| Formatos de archivo aceptados | JPEG o PNG |
| Ancho recomendado | 500px |
| Tamaño de archivo | Hasta 500kb |
| Relación de aspecto | Debe estar entre 2:1 (ancho) y 3:4 (alto) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Los mensajes de imagen estrecha y ancha tienen diferentes consideraciones de recuento de caracteres y botones.

{% subtabs %}
{% subtab Narrow image %}

#### Imagen estrecha

Un mensaje de imagen estrecha presenta una imagen ligeramente más alta y estrecha con opciones de texto y botones más extensas.

##### Especificaciones

| Área | Especificaciones |
| --- | --- |
| Contenido | Una imagen y texto de apoyo |
| Capacidad de texto | Hasta 500 caracteres |
| Botones | Hasta 5 botones opcionales |
| Fuente de imagen | Las imágenes se pueden añadir usando la biblioteca de medios de Braze o una URL directa |
| Personalización | Puedes especificar el comportamiento al hacer clic en la imagen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Un mensaje estrecho de KakaoTalk.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Wide image %}

#### Imagen ancha

Un mensaje de imagen ancha presenta una imagen ancha prominente adecuada para comunicación visual de alto impacto, con texto de apoyo mínimo.

##### Especificaciones

| Área | Especificaciones |
| --- | --- |
| Contenido | Una imagen y texto de apoyo |
| Capacidad de texto | Hasta 76 caracteres |
| Botones | Hasta 2 botones opcionales |
| Fuente de imagen | Las imágenes se pueden añadir usando la biblioteca de medios de Braze o una URL directa |
| Personalización | Puedes especificar el comportamiento al hacer clic en la imagen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Un mensaje ancho de KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Añadir imágenes

Puedes añadir imágenes a través de la biblioteca de medios de Braze o pegando una URL que aloje un archivo JPEG o PNG. También puedes especificar el comportamiento al hacer clic en la imagen para redirigir a los usuarios que hagan clic a una URL específica.

Braze gestiona automáticamente todos los requisitos de carga de imágenes de KakaoTalk, lo que significa que **no necesitas** subir imágenes a los proveedores de KakaoTalk antes de enviar mensajes. ¡Solo sube las imágenes y envía el mensaje directamente desde Braze!

![Sección con iconos seleccionados para añadir imagen estrecha.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab List item %}


Un mensaje de lista de elementos de KakaoTalk está diseñado para presentar una lista de elementos de contenido en un formato vertical claro. 

Los mensajes de elementos de lista consisten en un encabezado, una sección de lista de elementos y un área de botones opcional.

#### Especificaciones

| Área | Especificaciones |
| --- | --- |
| Cantidad de elementos | Requiere al menos 2 o 3 elementos |
| Botones | Hasta 5 botones opcionales |
| Encabezado | Hasta 250 caracteres |
| Título del elemento | Hasta 25 caracteres |
| URL del sitio web (por elemento) | Hasta 250 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Un mensaje de lista de elementos de KakaoTalk.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## Paso 3: Configura el seguimiento de clics

Cuando el seguimiento de clics de KakaoTalk está activado, Braze acorta automáticamente tus URLs, añade mecanismos de seguimiento y registra los clics en tiempo real. Estos datos te permiten crear estrategias de segmentación y reorientación más específicas, como segmentar usuarios según su comportamiento de clics y desencadenar mensajes en respuesta a clics específicos.

El seguimiento de clics es compatible con mensajes de texto, imagen y elementos de lista. Admite enlaces dentro de botones y acciones al hacer clic en imágenes. También puedes personalizar URLs usando Liquid y dominios personalizados.

Para habilitar el seguimiento de clics, marca **Seguimiento de clics** en la sección **Opciones de enlace** del compositor. Las URLs se acortarán usando el dominio predeterminado de Braze (`https://brz.ai`) o el dominio personalizado especificado para el grupo de suscripción, y se personalizarán para el usuario.

Para obtener todos los detalles sobre el seguimiento de clics, dominios personalizados, personalización con Liquid en URLs, informes y reorientación, consulta [Seguimiento de clics de KakaoTalk]({{site.baseurl}}/kakaotalk_click_tracking/).

### Reorientar usuarios

Puedes reorientar a los usuarios que han hecho clic en una URL en un mensaje de KakaoTalk usando los siguientes filtros de segmentación y desencadenadores:

- Desencadenadores basados en acciones
    - Interactuar con campaña
    - Interactuar con paso

- Filtros de segmentación
    - Hizo clic/abrió campaña
    - Hizo clic/abrió campaña o Canvas con etiqueta
    - Hizo clic/abrió paso

## Paso 4: Previsualiza y prueba tu mensaje de KakaoTalk

La vista previa del mensaje se actualiza automáticamente a medida que redactas tu mensaje de KakaoTalk. Cuando estés listo para probar, ve a la pestaña **Prueba** para enviar un mensaje de prueba a grupos de prueba de contenido o usuarios individuales, o para previsualizar el mensaje como un usuario existente o personalizado directamente en Braze.

Después de seleccionar tus usuarios de prueba, selecciona **Enviar prueba**. Una notificación indicará los resultados de tu envío de prueba. Para CJ OliveNetworks, recibirás una respuesta "C100". Si ves un error diferente, consulta la [documentación de usuario de CJ KakaoTalk](https://developers.kakao.com/docs/latest/en/index).

![Ventana de vista previa para un mensaje de KakaoTalk.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Para previsualizar y enviar un mensaje de prueba a un usuario existente, debes tener permisos de "Ver PII". Puedes previsualizar y enviar un mensaje de prueba a un usuario personalizado sin esos permisos.
{% endalert %}

Para revisar los resultados de un envío o solucionar problemas, ve a **Configuración** > **Registro de actividad de mensajes**. Para más información, consulta [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

## Paso 5: Construye el resto de tu campaña o Canvas

Consulta las siguientes secciones para obtener detalles sobre cómo usar mejor nuestras herramientas para crear mensajes de KakaoTalk.

### Elige la planificación de entrega o el desencadenador

Los mensajes de KakaoTalk se pueden entregar según un horario planificado, una acción o un desencadenador de API. Para más información sobre opciones de planificación y desencadenadores, consulta [Planifica tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) o [Tipos de planificación de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types) (para tu Canvas).

Puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser elegibles para recibir la campaña, o activar reglas de limitación de frecuencia. Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las horas tranquilas.

### Elige los usuarios objetivo

Segmenta usuarios seleccionando segmentos o filtros para reducir tu audiencia. Por ahora, KakaoTalk solo puede enviar mensajes a amigos del canal. Recomendamos establecer un atributo personalizado para indicar los amigos del canal, de modo que puedas segmentar correctamente a tus usuarios y evitar enviar mensajes de KakaoTalk a usuarios que no pueden recibirlos.

### Elige eventos de conversión

Braze te permite hacer seguimiento de la frecuencia con la que los usuarios realizan acciones específicas (eventos de conversión) después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se cuenta una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu campaña. Por ejemplo, si intentas impulsar a los usuarios a usar tu aplicación, establece el evento de conversión como **Inicia sesión**.

También puedes establecer eventos de conversión personalizados según tu caso de uso específico. Sé creativo y piensa en cómo quieres medir el éxito de tu campaña.

## Paso 6: Revisa y despliega

Después de terminar de construir tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!