## Ver análisis

Una vez que hayas lanzado tu campaña, puedes volver a la página de detalles de esa campaña para ver las métricas clave. Ve a la página **Campañas** y selecciona tu campaña para abrir la página de detalles.{% if include.channel != "banner" %} Para {% if include.channel == "Content Card" %}las tarjetas de contenido {% elsif include.channel == "banner" %}los banners {% elsif include.channel == "email" %}los correos electrónicos {% elsif include.channel == "in-app message" %}los mensajes dentro de la aplicación {% elsif include.channel == "KakaoTalk" %}los mensajes de KakaoTalk {% elsif include.channel == "push" %}los mensajes push {% elsif include.channel == "SMS" %}los mensajes SMS {% elsif include.channel == "whatsapp" %}los mensajes de WhatsApp {% elsif include.channel == "webhook" %}los webhooks {% endif %}enviados en Canvas, consulta [Análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).{% endif %}

{% alert tip %}
¿Buscas definiciones de los términos y métricas que aparecen en tu informe? Consulta nuestro 
  {% if include.channel == "email" %}[Glosario de análisis de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "banner" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por banners.
  {% elsif include.channel == "Content Card" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por tarjetas de contenido.
  {% elsif include.channel == "in-app message" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por mensaje dentro de la aplicación.
  {% elsif include.channel == "push" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por push.
  {% elsif include.channel == "SMS" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por SMS/MMS y RCS.
  {% elsif include.channel == "whatsapp" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por WhatsApp.
  {% elsif include.channel == "webhook" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por webhook.{% endif %}
{% endalert %}

Desde la pestaña **Análisis de campaña**, puedes ver tus informes en una serie de paneles. Puede que veas más o menos de los que se enumeran en las secciones siguientes, pero cada uno tiene su propia utilidad.

### Intervalo de fechas

De forma predeterminada, el intervalo de tiempo para **Análisis de campaña** mostrará los últimos 90 días desde el momento actual. Esto significa que si la campaña se lanzó hace más de 90 días, los análisis mostrarán "0" para el intervalo de tiempo indicado. Para ver todos los análisis de campañas anteriores, ajusta el intervalo de tiempo del informe.

### Detalles de la campaña

El panel **Detalles de la campaña** muestra un resumen de alto nivel del rendimiento general de tu
  {% if include.channel == "banner" %}banner. 
  {% elsif include.channel == "Content Card" %}tarjeta de contenido.
  {% elsif include.channel == "email" %}correo electrónico.
  {% elsif include.channel == "in-app message" %}mensaje dentro de la aplicación.
  {% elsif include.channel == "KakaoTalk" %}mensaje de KakaoTalk.
  {% elsif include.channel == "push" %}mensaje push.
  {% elsif include.channel == "SMS" %}SMS, MMS y RCS.
  {% elsif include.channel == "whatsapp" %}mensajes de WhatsApp.
  {% elsif include.channel == "webhook" %}webhook.
  {% endif %}

Revisa este panel para ver métricas generales como el número de mensajes enviados a los destinatarios, la tasa de conversión primaria y los ingresos totales generados por este mensaje. También puedes revisar la configuración de entrega, audiencia y conversión desde esta página.

{% if include.channel == "whatsapp" %}
{% alert note %}
El canal de WhatsApp incluye la tasa de lectura. Esta métrica solo se entrega a los usuarios que tienen activados los recibos de lectura, lo que puede variar.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Panel Detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Panel Detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Panel Detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Panel Detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Panel Detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Panel Detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_iam.png %})

En Canvas, verás el rendimiento de los mensajes dentro de la aplicación mapeado en el Canvas que has creado. Puedes utilizar el panel de control de la parte superior de la página para borrar otros tipos de mensajería (canales) y ver solo los mensajes dentro de la aplicación en tu Canvas.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![La sección Detalles de la campaña.]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![Panel Detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Grupos de control {#cc-control-group}

Para medir el impacto de una tarjeta de contenido individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Detalles de la campaña** de nivel superior no incluye métricas de la variante del grupo de control.

{% elsif include.channel == "SMS" %}

#### Grupos de control {#sms-control-group}

Para medir el impacto de un mensaje SMS, MMS o RCS individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Detalles de la campaña** de nivel superior no incluye métricas de la variante del grupo de control.

{% elsif include.channel == "whatsapp" %}

#### Grupos de control {#whatsapp-control-group}

Para medir el impacto de un mensaje individual de WhatsApp, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Detalles de la campaña** de nivel superior no incluye métricas de la variante del grupo de control.

{% elsif include.channel == "webhook" %}

#### Grupos de control {#webhook-control-group}

Para medir el impacto de un mensaje de webhook individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **Detalles de la campaña** de nivel superior no incluye métricas de la variante del grupo de control.

{% endif %}

#### Cambios desde la última visualización

El número de actualizaciones de la campaña por parte de otros miembros de tu equipo se registra mediante la métrica *Cambios desde la última visualización* en la página de resumen de la campaña. Selecciona **Cambios desde la última visualización** para ver un registro de cambios de las actualizaciones del nombre de la campaña, la planificación, las etiquetas, el mensaje, la audiencia, el estado de aprobación o la configuración de acceso del equipo. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tu campaña.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Rendimiento de la tarjeta de contenido

El panel **Rendimiento de la tarjeta de contenido** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes de las tarjetas de contenido]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### Rendimiento del correo electrónico

El panel **Rendimiento del correo electrónico** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes de correo electrónico]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Rendimiento de los mensajes dentro de la aplicación

El panel **Rendimiento de los mensajes dentro de la aplicación** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes dentro de la aplicación]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Rendimiento de push

El panel **Rendimiento de push** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### Rendimiento de SMS/MMS/RCS

El panel **Rendimiento de SMS/MMS/RCS** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento de SMS/MMS/RCS que incluye una tabla de métricas para un grupo de control, la variante 1 y la variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Rendimiento del banner

El panel **Rendimiento del banner** muestra el rendimiento de tu mensaje en varias dimensiones. Estas métricas varían en función del canal de mensajería y de si estás realizando una prueba multivariante o no.

![Panel de rendimiento de SMS/MMS que incluye una tabla de métricas para un grupo de control, la variante 1 y la variante 2.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### Rendimiento de KakaoTalk

El panel **Rendimiento de KakaoTalk** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

{% elsif include.channel == "webhook" %}
### Rendimiento del webhook

El panel **Rendimiento del webhook** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento de webhooks que incluye una tabla de métricas para un grupo de control y la variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### Rendimiento de WhatsApp

El panel **Rendimiento de WhatsApp** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento de WhatsApp que incluye una tabla de métricas para la variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Si quieres simplificar la vista, haz clic en <i class="fas fa-plus"></i> **Añadir/Eliminar columnas** y desmarca las métricas que desees. De forma predeterminada, se muestran todas las métricas.

{% if include.channel == "email" %}

#### Mapas de calor

Con los mapas de calor, puedes ver el éxito de los distintos enlaces de una misma campaña de correo electrónico. En la sección **Análisis de mensajes**, ve al panel **Rendimiento del correo electrónico**. Selecciona **Vista previa y mapa de calor** para ver una vista previa de tu campaña de correo electrónico y el mapa de calor. También puedes seleccionar el hipervínculo del nombre de la variante para ver el mapa de calor.

En esta vista, puedes usar la opción **Mostrar mapa de calor** para obtener una vista visual de tu correo electrónico que muestre la frecuencia general y la ubicación de los clics dentro de la duración de la campaña. En el panel **Tabla de enlaces por clics totales**, puedes ver todos los enlaces de tu campaña de correo electrónico y ordenarlos por clics totales. Esto puede proporcionar información adicional sobre por dónde navegan tus usuarios. Para guardar una copia del mapa de calor como referencia, selecciona el botón de descarga.

![Ejemplo de la página Vista previa y mapa de calor, que incluye una campaña por correo electrónico y un panel con ejemplos de alias de enlaces con su total de clics.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Imágenes

Te recomendamos habilitar CORS en las URL de tus imágenes para evitar que se rompan en las vistas previas y exportaciones de mapas de calor.

Si faltan imágenes en una exportación, trabaja con tus desarrolladores para que los activos de imagen permitan el acceso entre orígenes: el servidor debe devolver el encabezado `Access-Control-Allow-Origin` con `*` o el dominio de tu dashboard de Braze.

{% endif %}

{% if include.channel == "Content Card" %}

#### Métricas de la tarjeta de contenido

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para ver las definiciones completas de todas las métricas de las tarjetas de contenido, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por tarjetas de contenido.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Mensajes enviados</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                Se calcula de forma diferente según lo que hayas seleccionado para 
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Creación de tarjetas</a>:<br><br>
                <ul>
                    <li><b>En el lanzamiento o en la entrada del paso:</b> El número de tarjetas creadas y disponibles para ver. Esto no cuenta si los usuarios vieron la tarjeta.</li>
                    <li><b>En la primera impresión:</b> El número de tarjetas mostradas a los usuarios.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Impresiones totales</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Esto puede incrementarse varias veces para el mismo usuario.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Impresiones únicas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Este recuento</span> no se incrementa la segunda vez que un usuario ve una tarjeta de contenido.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">Destinatarios únicos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> Dado que un usuario puede ser un destinatario único cada día, es de esperar que esta cifra sea superior a <i>Impresiones únicas</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Clics únicos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Esto incluye los clics en los enlaces para cancelar la suscripción proporcionados por Braze.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Descartes únicos</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
En cuanto a cómo se registran las impresiones, hay algunos matices entre web, Android e iOS. En términos generales, Braze registra una impresión cuando se ve una tarjeta, es decir, después de que un usuario se desplace hasta la tarjeta de contenido específica en su feed.
{% endalert %}

#### Destinatarios únicos frente a impresiones únicas

Hay algunas métricas disponibles que cubren la visibilidad de tu mensaje. Esto incluye _Destinatarios únicos_ e _Impresiones únicas_. Veamos algunos escenarios de ejemplo para comprender mejor estas métricas.

Supongamos que ves una tarjeta de contenido hoy, luego recibes una nueva tarjeta de la misma campaña mañana, y otra más pasado mañana: se te contará como _Destinatario único_ tres veces. Sin embargo, solo se te contabilizará una _Impresión única_. También se te incluirá en el número de _Mensajes enviados_, ya que la tarjeta estaba disponible en tu dispositivo.

Como otro ejemplo, supongamos que ves cinco _Impresiones únicas_ en una campaña de tarjeta de contenido que muestra 150 000 _Mensajes enviados_. Esto significa que la tarjeta se puso a disposición (en el backend) de una audiencia de 150 000 usuarios, pero solo los dispositivos de cinco usuarios realizaron todos los pasos siguientes después de que se produjera ese envío:

1. Iniciaron una sesión o la aplicación solicitó explícitamente una sincronización de tarjetas de contenido (o ambas cosas)
2. Navegaron a la vista de tarjetas de contenido
3. El SDK registró una impresión y la envió al servidor

Tus _Mensajes enviados_ se refieren a las tarjetas de contenido disponibles para ser vistas, mientras que _Destinatarios únicos_ se refiere a las tarjetas de contenido que fueron vistas realmente.

{% elsif include.channel == "banner" %}

### Métricas de los banners

Estas son las métricas clave de seguimiento al revisar el rendimiento de tu campaña de banner. Los clics y las impresiones de los banners se registran automáticamente con el SDK. 

Para obtener las definiciones completas de todas las métricas de banners, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por banners.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impresiones totales</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} En el caso de los banners, las impresiones se registran una vez por sesión de usuario. Si el mismo banner se ve varias veces dentro de la misma sesión, solo se registra una impresión.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impresiones únicas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Cada usuario solo se cuenta una vez.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Clics totales</a></td>
            <td class="no-split"><i>Clics totales</i> es el número total (y el porcentaje) de usuarios que hicieron clic en el mensaje entregado, independientemente de si el mismo usuario hace clic varias veces.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Clics únicos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} Cada usuario solo se cuenta una vez.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Conversiones primarias</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinatarios únicos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> Dado que un espectador puede ser un destinatario único cada día, debes esperar que sea superior a <i>Impresiones únicas</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Ingresos</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Confianza</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Ejemplos de cálculo de métricas de banners

Hay algunas métricas disponibles que cubren la visibilidad de tu mensaje. Esto incluye _Destinatarios únicos_ e _Impresiones únicas_. Veamos algunos escenarios de ejemplo para comprender mejor estas métricas.

Supongamos que ves un banner hoy, luego ves el mismo banner mañana y de nuevo pasado mañana: se te contará como _Destinatario único_ tres veces. Sin embargo, solo se te contabilizará una _Impresión única_.

Como otro ejemplo, supongamos que ves cinco _Impresiones únicas_ en una campaña de banners. Esto significa que solo los dispositivos de cinco usuarios realizaron todos los pasos siguientes:

1. Iniciaron una sesión o la aplicación solicitó explícitamente una sincronización de banners (o ambas cosas)
2. Navegaron a la vista de banners
3. El SDK registró una impresión y la envió al servidor

_Destinatarios únicos_ se refiere a los banners que realmente se vieron.

{% elsif include.channel == "email" %}

#### Métricas de correo electrónico

Aquí tienes algunas métricas clave específicas del correo electrónico que no verás en otros canales. Para ver las definiciones completas de todas las métricas de correo electrónico utilizadas en Braze, consulta nuestro [Glosario de análisis de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Clics únicos</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Este seguimiento se realiza durante un periodo de siete días para el correo electrónico y se mide mediante <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Esto incluye los clics en los enlaces de cancelación de suscripción proporcionados por Braze. Esta cifra debería estar entre el 5-10 %. ¡Todo lo que supere el 10 % es excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Aperturas únicas</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} En el caso del correo electrónico, se realiza un seguimiento durante un periodo de 7 días. Esta cifra debería estar entre el 30-40 %. ¡Todo lo que supere el 40 % es excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Tasa de clics sobre aperturas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Tasa de correo no deseado</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} Si esta métrica es superior a 0,08, podría ser una señal de que el texto de tu mensaje es demasiado comercial o de que deberías reconsiderar tus métodos de recopilación de direcciones de correo electrónico (para confirmar que estás enviando mensajes a personas interesadas en tu correspondencia).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Cancelaciones de suscripción</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Otras aperturas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimación de aperturas reales</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Consulta la siguiente sección para más detalles.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Aperturas automáticas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Rebotes</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Rebote duro</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Rebote blando</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Aplazamiento</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Entregas y rebotes

El dashboard resalta los _Rebotes duros_. Algunos _Rebotes_ pueden ser rebotes blandos y no coincidirán con ese recuento por sí solos. Puedes aproximar los rebotes blandos con esta fórmula:

_Envíos − (Entregas + Rebotes duros) ≈ Rebotes blandos_

Las _Entregas_ pueden aumentar durante las primeras 72 horas a medida que los reintentos tienen éxito, mientras que los _Envíos_ y los rebotes duros de un envío único se mantienen fijos una vez que se completa el envío.

##### Clics sin un evento de apertura

Se puede registrar un clic sin una apertura cuando el píxel de apertura nunca se carga. Por ejemplo, el mensaje está recortado en Gmail o el usuario ha desactivado las imágenes (el píxel de apertura suele estar en el pie de página). Algunos clientes actúan como proxy de las imágenes (como Apple Mail), por lo que la apertura puede registrarse cuando el servidor obtiene el píxel por primera vez, no cuando el usuario lee el correo.

Un clic y una apertura también pueden caer en días diferentes: un usuario podría hacer clic el 16 de mayo con las imágenes desactivadas (sin apertura), y luego abrir en el correo web el 17 de mayo (la apertura se registra entonces).

##### Aplazamientos

Diferido o aplazamiento es cuando un correo electrónico no se entregó inmediatamente, pero Braze reintentará el correo electrónico durante un máximo de 72 horas después de este fallo de entrega temporal para maximizar las posibilidades de entrega exitosa antes de que se detengan los intentos para esa campaña específica. Las razones típicas de los aplazamientos incluyen la limitación de la tasa de volumen de correo electrónico basada en la reputación por parte del proveedor de correo, problemas temporales de conectividad o errores de DNS.

Los _Aplazamientos_ difieren de los _Rebotes blandos_. Si no se entregó correctamente ningún correo electrónico durante este periodo de reintento, Braze enviará un evento de rebote blando por cada intento de envío de campaña. Antes del 25 de febrero de 2025, estos reintentos se contabilizaban como múltiples rebotes blandos para 1 envío de campaña.

Ten en cuenta que los _Aplazamientos_ actualmente solo están disponibles utilizando las características de Currents o Braze Snowflake (como el generador de consultas, segmento SQL, compartir datos de Snowflake). Si quieres incluirlo en los análisis de campaña o Canvas, [envía tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Estimación de la tasa de apertura real {#estimated-real-open-rate}

Esta estadística utiliza un modelo de análisis propio creado por Braze para reconstruir una estimación de la tasa de apertura única de la campaña como si las aperturas automáticas no existieran. Aunque recibimos etiquetas de *Aperturas automáticas* en algunos eventos de apertura de los remitentes de correo electrónico (véase más arriba), estas etiquetas a menudo pueden etiquetar aperturas reales como aperturas automáticas. En otras palabras, las *Otras aperturas* son probablemente una subestimación de las aperturas reales (por usuarios reales). En su lugar, Braze utiliza los datos de clics de cada campaña para deducir la tasa a la que los humanos reales abrieron el mensaje. Esto compensa varios mecanismos de apertura automática, incluido el MPP de Apple.

La _Estimación de la tasa de apertura real_ se calcula 36 horas después del inicio del envío del correo electrónico y se recalcula cada 24 horas a partir de entonces. Si una campaña se repite, la estimación se vuelve a calcular 36 horas después de que se produzca otro envío.

Dado que esta métrica se recalcula de forma continua, el valor de la _Estimación de la tasa de apertura real_ puede cambiar con el tiempo a medida que se reciben nuevas señales de interacción (como aperturas y clics) y se incorporan al modelo. En la práctica, la _Estimación de la tasa de apertura real_ puede seguir actualizándose diariamente mientras la campaña permanezca activa.

Normalmente se necesitan unos 10 000 correos electrónicos entregados para que la estadística se calcule correctamente, aunque ese número puede variar en función de la tasa de clics. Si no se puede calcular la estadística, la columna muestra "--".

###### Limitaciones

La estimación de la tasa de apertura real solo está disponible en campañas y no se informa en eventos de Currents. Esta métrica solo se calcula retroactivamente para las campañas activas lanzadas antes del 14 de noviembre de 2023.

##### Gestión del aumento de las tasas de clics

Las tasas de apertura pueden ser una métrica útil para el seguimiento de tus campañas de correo electrónico. Sin embargo, estas tasas de apertura no son necesariamente indicadores precisos de la interacción humana con las campañas de correo electrónico. Un evento de apertura, por definición, se produce cuando un usuario abre un correo electrónico, lo que significa que se ha descargado correctamente un píxel transparente de seguimiento de apertura. 

Además, el uso de herramientas de escaneo de seguridad puede inflar las tasas de apertura. Algunas de estas herramientas protegen a sus usuarios escaneando los correos electrónicos entrantes en busca de contenido malicioso, haciendo clic en los enlaces para verificar su legitimidad. Estos clics suelen denominarse "clics de bots" o "interacción no humana" (INH). 

En última instancia, una vez que un correo electrónico sale de nuestros servidores, tenemos una visibilidad limitada de lo que ocurre a continuación, pero aquí tienes algunas recomendaciones para gestionar la INH que afecta a tus resultados:

1. Ten en cuenta que esto puede ocurrirle a cualquier remitente y a casi cualquier destinatario. Los clics, al igual que las aperturas, no son indicadores del todo fiables de la interacción humana con tus mensajes, lo que significa que la INH no se puede prevenir.
2. Una mayor interacción positiva tiende a correlacionarse con una INH más baja, por lo que es importante seguir las [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) de mensajería por correo electrónico. Esto incluye obtener el permiso explícito de tus usuarios para enviar correos electrónicos y dar de baja a los suscriptores no comprometidos con una cadencia regular. 
3. Utiliza enlaces HTTPS en tus correos electrónicos siempre que sea posible. La INH es menos frecuente para los remitentes que utilizan enlaces seguros.
4. Si utilizas un proceso para cancelar la suscripción con un solo clic, considera la posibilidad de crear un [centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview) que dirija a los usuarios a una página para editar y administrar sus preferencias de notificación. Esto puede ser útil porque la INH puede cancelar suscripciones de usuarios inadvertidamente.
5. Considera la posibilidad de utilizar [otras métricas]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) para medir el éxito de tu marketing por correo electrónico, como las conversiones, las sesiones de la aplicación o las visitas al sitio web.
6. Añade un enlace oculto en tus campañas de correo electrónico. Este enlace sería algo que un humano no notaría, como texto blanco sobre blanco o un signo de puntuación. Los bots tienden a hacer clic en todos los enlaces, por lo que puedes concluir que los usuarios que generan eventos de clic en el enlace invisible son en realidad el resultado de INH, por lo que la apertura o el clic no indican necesariamente una interacción positiva.

{% elsif include.channel == "in-app message" %}

#### Métricas de mensajes dentro de la aplicación

Aquí tienes algunas métricas clave de los mensajes dentro de la aplicación que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de mensajes dentro de la aplicación utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

{% alert note %}
Los informes sobre _Clics en botón 1_ y _Clics en botón 2_ solo funcionan cuando especificas el **Identificador para informes** como "0" y "1" respectivamente en el mensaje dentro de la aplicación.

![El campo "Identificador para informes" con el valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Clics en el cuerpo</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Clics en botón 1</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Clics en botón 2</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impresiones únicas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impresiones totales</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversiones (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Total de conversiones</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Tasa de conversión</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Cerrar mensaje</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "KakaoTalk" %}

### Métricas de KakaoTalk

Aquí tienes algunas métricas clave de KakaoTalk que puedes ver en tus análisis. Para más detalles, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/).

| Término | Definición |
| --- | --- |
| Audiencia | _Audiencia_ es el porcentaje de usuarios que recibieron un mensaje en particular. <br><br>_(Número de destinatarios en la variante) / (Destinatarios únicos)_ |
| Destinatarios únicos | _Destinatarios únicos_ es el número de destinatarios diarios únicos, o usuarios que recibieron un nuevo mensaje en un día. Para que este recuento se incremente para un usuario más de una vez, el usuario debe recibir un nuevo mensaje en un día diferente. Este número se basa en el `user_id`. Para más detalles, consulta [Destinatarios únicos en el Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/#unique-recipients). |
| Envíos | El número total de mensajes enviados en una campaña. Esto no significa que el mensaje fue recibido o entregado a un dispositivo, solo que el mensaje fue enviado. |
| Clics totales | El número total de veces que los usuarios hicieron clic en los mensajes de KakaoTalk enviados. |
| Errores | _Errores_ es el número de errores devueltos por el proveedor de KakaoTalk (se incrementa durante el proceso de envío). |
| Ingresos | _Ingresos_ son los ingresos en dólares de los destinatarios de la campaña dentro de la ventana de conversión primaria establecida. |
| Conversiones primarias | _Conversiones primarias_ es el número de veces que ocurrió un evento definido después de interactuar con o ver un mensaje recibido de una campaña de Braze. Este evento definido lo determinas tú al crear la campaña. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% elsif include.channel == "push" %}

#### Métricas push

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para ver las definiciones completas de todas las métricas push, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Descripción</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Rebotes</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} Consulta <a href="#bounced-push">Notificaciones push rebotadas</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direct Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Aperturas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> La entrega de notificaciones es un "mejor esfuerzo" por parte de los servicios de notificaciones push de Apple (APNs). No está destinada a entregar datos a tu aplicación, solo a notificar al usuario que hay nuevos datos disponibles. La distinción importante es que mostraremos cuántos mensajes entregamos con éxito a APNs, no necesariamente cuántos APNs entregó con éxito a los dispositivos.

##### Seguimiento de cancelaciones de suscripción

Las cancelaciones de suscripción push no se incluyen como métrica en los análisis de campañas y dependen de las actualizaciones del estado push de los usuarios por parte de proveedores como Apple o Google. Estas actualizaciones pueden ser poco frecuentes e impredecibles. Como resultado, las cancelaciones de suscripción push no se incluyen como métrica en los análisis de las campañas push. 

Sin embargo, el seguimiento manual de las cancelaciones de suscripción push puede proporcionar información valiosa sobre la respuesta de los usuarios a la frecuencia de tus notificaciones y la relevancia del contenido. Aquí tienes dos opciones para realizar el seguimiento de las cancelaciones de suscripción push: usando filtros de segmento o filtros personalizados.

{% tabs local %}
{% tab Segment filters %}

Puedes crear un segmento para identificar a los usuarios que no tienen habilitada la función push, lo que significa que no están suscritos ni han dado su adhesión voluntaria y no tienen un [token de notificaciones push en primer plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens). Por ejemplo, para ver el número de cancelaciones de suscripción en tu aplicación, utilizarías una combinación "O" de los siguientes segmentos: 

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![La sección del generador de segmentos con el filtro "Background or Foreground Push Enabled for App" para una aplicación es falso, y el filtro "Has Uninstalled" están seleccionados.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Ten en cuenta que los filtros de segmentación son aproximados y no pueden vincularse específicamente a una fecha y una campaña.

{% endtab %}
{% tab Custom filters %}

{% alert important %}
Al registrar un evento personalizado para el cambio de suscripción, se registrarán [puntos de datos]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Alternativamente, utiliza filtros de segmento para identificar y dirigirte a los usuarios que no están habilitados para push.
{% endalert %}

Para una solución diferente, también recomendamos crear un evento personalizado para las cancelaciones de suscripción push en función de si el estado de habilitación push de un usuario es `true` o `false`, con el fin de hacer un seguimiento de esta métrica.

{% endtab %}
{% endtabs %}

##### Comprender las aperturas

Aunque _Direct Opens_ e _Influenced Opens_ incluyen la palabra "opens" (aperturas), en realidad son métricas diferentes. _Direct Opens_ se refiere a la apertura directa de una notificación push, como se indica en la tabla anterior. _Influenced Opens_ se refiere a la apertura de una aplicación sin abrir una notificación push dentro de un plazo de tiempo determinado tras recibirla. Por tanto, _Influenced Opens_ se refiere a las aperturas de la aplicación, no a las aperturas de las notificaciones push.

##### Por qué los envíos push pueden superar los destinatarios únicos

El número de _Envíos_ puede superar el número de _Destinatarios únicos_ debido a las siguientes razones:

- **La reelegibilidad está activada:** Cuando se habilita la reelegibilidad en la configuración de tu campaña o Canvas, los usuarios que cumplan los criterios de segmento y entrega pueden recibir la misma notificación push varias veces. El resultado es un mayor número de envíos totales.
- **Los usuarios tienen varios dispositivos:** Si no se habilita la reelegibilidad, la diferencia puede explicarse porque los usuarios tienen varios dispositivos asociados a su perfil. Por ejemplo, un usuario puede tener un smartphone y una tableta, y la notificación push se envía a todos los dispositivos registrados. Cada entrega cuenta como un envío, pero solo se registra un destinatario único.
- **Los usuarios están asignados a varias aplicaciones:** Si los usuarios están asociados a más de una aplicación (como cuando prueban una aplicación nueva), pueden recibir la misma notificación push en cada aplicación. Esto contribuye a un mayor número de envíos.

##### Por qué se producen los rebotes {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

Los rebotes se producen en los servicios de notificaciones push de Apple (APNs) cuando una notificación push intenta entregarse a un dispositivo que no tiene instalada la aplicación prevista. APNs también tiene derecho a cambiar los tokens de los dispositivos arbitrariamente. Si intentas enviar al dispositivo de un usuario en el que su token de notificaciones push ha cambiado entre el momento en que registramos previamente su token (como al principio de cada sesión, cuando registramos a un usuario para obtener un token push) y el momento del envío, se produciría un rebote.

Si un usuario desactiva push en la configuración de su dispositivo, al abrir la aplicación posteriormente el SDK detectará que se ha desactivado push y lo notificará a Braze. En este punto actualizaremos el estado de habilitación de push para que esté deshabilitado. Cuando un usuario deshabilitado recibe una campaña push antes de tener una nueva sesión, la campaña se enviaría correctamente y aparecería como entregada. El push no rebotará para este usuario. Tras una sesión posterior, cuando intentas enviar un push al usuario, Braze ya sabe si tenemos un token de primer plano, por lo que no se envía ninguna notificación.

Las notificaciones push que caducan antes de la entrega no se consideran fallidas y no se registrarán como rebotadas.

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging (FCM) puede rebotar en tres casos:

| Escenario | Descripción |
| -- | -- |
| Aplicaciones desinstaladas | Cuando se intenta entregar un mensaje a un dispositivo y la aplicación prevista está desinstalada en ese dispositivo, el mensaje se descartará y se invalidará el ID de registro del dispositivo. Cualquier intento futuro de mensajería con el dispositivo devolverá un error NotRegistered. |
| Copia de seguridad de la aplicación | Cuando se hace una copia de seguridad de una aplicación, su ID de registro podría dejar de ser válido antes de que se restaure la aplicación. En este caso, FCM dejará de almacenar el ID de registro de la aplicación y esta dejará de recibir mensajes. Por ello, los ID de registro **no** deben guardarse cuando se hace una copia de seguridad de una aplicación. |
| Aplicación actualizada | Cuando se actualiza una aplicación, el ID de registro de la versión anterior puede dejar de funcionar. Como tal, una aplicación actualizada debe sustituir su ID de registro existente. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### Métricas de SMS, MMS y RCS

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para obtener las definiciones completas de todas las métricas de SMS, MMS y RCS, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por SMS/MMS y RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Enviados</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Fallos de entrega</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Entrega confirmada</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rechazos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Cancelación</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Ayuda</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Clics totales</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Métricas del webhook

Aquí tienes algunas métricas clave de webhook que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de webhook utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinatarios únicos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envíos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Errores</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### Métricas de WhatsApp

Aquí tienes algunas métricas clave de WhatsApp que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de WhatsApp utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envíos</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Entregas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Lecturas</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Errores</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Métricas de bloqueo e informes de usuarios finales

Se puede acceder a métricas adicionales a través del [panel del administrador de WhatsApp](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx), aunque es necesario [confirmar tu acceso](https://www.facebook.com/business/help/218116047387456) para acceder a toda la información disponible. 

{% endif %}

### Rendimiento histórico

El panel **Rendimiento histórico** te permite ver las métricas del panel **Rendimiento de mensajes** como un gráfico a lo largo del tiempo. Utiliza los filtros de la parte superior del panel para modificar las estadísticas y los canales que aparecen en el gráfico. El intervalo de tiempo de este gráfico siempre reflejará el intervalo de tiempo especificado en la parte superior de la página. 

Para obtener un desglose día a día, haz clic en el menú hamburguesa <i class="fas fa-bars"></i> y selecciona **Descargar CSV** para recibir una exportación CSV del informe.

![Gráfico del panel Rendimiento histórico con estadísticas de ejemplo para un correo electrónico desde febrero de 2021 hasta mayo de 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Si seleccionas enviar solo a usuarios que puedan ver la última versión de Braze de mensajes dentro de la aplicación (Generación 3), tu **Audiencia objetivo** no se ajusta para reflejar tu elección.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Respuestas a palabras clave

El panel **Respuestas a palabras clave** te muestra una cronología de las palabras clave entrantes con las que los usuarios respondieron tras recibir tu mensaje.  

![Panel de respuestas a palabras clave SMS/MMS/RCS a nivel de campaña que incluye un gráfico lineal de la distribución de palabras clave a lo largo del tiempo y una sección de categorías de palabras clave con casillas de verificación seleccionadas para adhesión voluntaria, cancelación de suscripción, ayuda, otros, más y asesoramiento.]({% image_buster /assets/img/sms/keyword_responses.png %})

Aquí también puedes ver la distribución de la respuesta de cada categoría de palabras clave para determinar los próximos pasos para [reorientar]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) y [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) cómodamente.

![La tabla situada debajo del gráfico de líneas tiene columnas para Categoría de palabras clave, Distribución de respuestas y Reorientación, donde se te ofrece la opción de crear un segmento con la categoría de palabras clave.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Detalles del evento de conversión

El panel **Detalles del evento de conversión** te muestra el rendimiento de los eventos de conversión de tu campaña. Para más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results).

![El panel Detalles del evento de conversión.]({% image_buster /assets/img/cc-conversion.png %})

### Correlación de conversión

El panel **Correlación de conversión** te da información sobre qué atributos y comportamientos de los usuarios ayudan o perjudican los resultados que estableces para las campañas. Para más información, consulta [Correlación de conversión]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/).

![El panel Correlación de conversión con un análisis de los atributos y el comportamiento de los usuarios a partir del evento de conversión primaria - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## Generador de informes

También puedes usar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para crear informes personalizados para tus campañas de KakaoTalk. Al crear un informe, puedes filtrar para incluir solo campañas de KakaoTalk seleccionando **KakaoTalk** en **Canales**, o filtrando por cualquier etiqueta que hayas aplicado a tus campañas de KakaoTalk.

{% endif %}

{% if include.channel == "whatsapp" %}

### Análisis de Meta

Además de los análisis de Braze, se puede acceder a los análisis a nivel de plantilla en el administrador de WhatsApp Business. Para más información, consulta [la documentación de Meta](https://www.facebook.com/business/help/218116047387456).

{% endif %}

{% if include.channel == "SMS" %}

### Eventos SMS de Currents

Al igual que el correo electrónico, Braze recibe eventos a nivel de usuario relacionados con un mensaje SMS a medida que hace su recorrido hasta un usuario. Cualquier evento SMS entrante también se enviará como evento de Currents a través del evento [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events). Esto te permite realizar acciones adicionales o informes sobre los mensajes que envían tus usuarios fuera de la plataforma Braze. 

{% alert note %}
Los mensajes entrantes se truncan a partir de 1600 caracteres.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Informe de retención

Los informes de retención muestran las tasas a las que tus usuarios han realizado un evento de retención seleccionado a lo largo de períodos de tiempo en una campaña específica{% if include.channel != "banner" %} o Canvas{% endif %}. Para más información, consulta [Informes de retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

## Informe de embudo

Los informes de embudo ofrecen un informe visual que te permite analizar los recorridos que realizan tus clientes después de recibir una campaña{% if include.channel != "banner" %} o Canvas{% endif %}. Si tu campaña {% if include.channel != "banner" %}o Canvas {% endif %}utiliza un grupo de control o varias variantes, podrás comprender cómo las diferentes variantes han influido en el embudo de conversión a un nivel más detallado y optimizar en función de estos datos.

Para más información, consulta [Informes de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

{% endif %}