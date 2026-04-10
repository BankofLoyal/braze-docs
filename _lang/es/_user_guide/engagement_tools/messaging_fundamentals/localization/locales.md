---
nav_title: Mensajes multilingües
article_title: Mensajes multilingües
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artículo proporciona los pasos para utilizar las configuraciones regionales en tus mensajes."
---

# Mensajes multilingües

> Después de añadir configuraciones regionales a tu espacio de trabajo, puedes dirigirte a usuarios en diferentes idiomas con un solo push, correo electrónico, banner, mensaje dentro de la aplicación o bloque de contenido.

## Requisitos previos

{% tabs %}
{% tab Multi-language locales %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Message types %}

| Característica | Permisos de usuario requeridos |
| --- | --- |
| Tipos&nbsp;de&nbsp;mensaje | Necesitas estos permisos para añadir configuraciones regionales y traducciones a campañas y Canvas:<br><br> {::nomarkdown}Permisos granulares: <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul> Permisos heredados: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Templates %}

| Característica | Permisos de usuario requeridos |
| --- | --- |
| Plantillas | Necesitas estos permisos para el tipo de plantilla a la que quieras añadir configuraciones regionales y traducciones:<br><br> {::nomarkdown}Permisos granulares: <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul> Permisos heredados: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Usar configuraciones regionales

### Paso 1: Configura las configuraciones regionales

Antes de poder añadir traducciones a un mensaje, primero debes [crear las configuraciones regionales que quieras admitir]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/). Las configuraciones regionales definen las variantes de idioma (y opcionalmente de región) disponibles para la mensajería.

### Paso 2: Marca el contenido para traducción

Envuelve el texto que quieras traducir con las etiquetas de traducción de Liquid {% raw %}`{% translation your_id_here %}` y `{% endtranslation %}`{% endraw %} y asigna un ID de etiqueta. Los ID de las etiquetas de traducción deben ser únicos dentro de un mensaje. Considera usar nombres de ID semánticos que describan claramente el texto, como {% raw %}`{% translation header %}`{% endraw %}.

Aquí tienes un ejemplo de mensaje marcado para traducción: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Resalta el texto que quieras traducir y usa el atajo de teclado **Cmd + Alt + L** (macOS) o **Ctrl + Alt + L** (Windows) para envolverlo en etiquetas de traducción.<br><br> Este atajo funciona en todos los canales que admiten mensajería multilingüe, excepto en los editores de arrastrar y soltar para correo electrónico y bloques de contenido. Para esos, usa el botón **Añadir personalización** en la barra lateral izquierda para añadir etiquetas de traducción.
{% endalert %}

#### Localización de URLs

Al traducir contenido, las URLs requieren un manejo especial para evitar enlaces rotos.

##### URLs estándar (estáticas)

Las URLs estáticas se introducen manualmente en el editor (por ejemplo, `https://example.com`). También recomendamos lo siguiente:

| Recomendación | Razón |
| --- | --- |
| Mantén el protocolo (`https://`) fuera de las etiquetas de traducción. Envuelve solo el dominio y la ruta (por ejemplo, `example.com/en`). | Los traductores pueden alterar o eliminar accidentalmente caracteres especiales, causando enlaces rotos. |
| No incluyas parámetros de consulta dentro de las etiquetas de traducción (por ejemplo, `?utm_source=promo`). | Los traductores pueden alterar o eliminar accidentalmente caracteres especiales, causando enlaces rotos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Una URL estándar que sigue ambas recomendaciones es:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz%}{% endtranslation %}">Click Here</a>
```
{% endraw %}

{% alert important %}
Si estás usando [seguimiento de enlaces de correo electrónico](#email-link-tracking) (aliasing de enlaces o plantillas de enlaces), se requiere configuración adicional cuando las URLs están envueltas en etiquetas de traducción.
{% endalert %}

#### Atributos HTML y estructura

Solo envuelve texto legible por humanos en etiquetas de traducción. Evita envolver atributos HTML (como `class`, `style` o `id`) u otro código estructural. Los atributos HTML controlan el diseño, el estilo y la funcionalidad. Envolverlos en etiquetas de traducción puede romper el formato o los estilos en las versiones localizadas de tu mensaje.

Este texto está correctamente envuelto:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Texto envuelto incorrectamente %}

Este texto está envuelto **incorrectamente**:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### Paso 3: Añade configuraciones regionales a tu mensaje

Después de añadir etiquetas de traducción a tu mensaje, selecciona **Administrar idiomas** en el editor (**Idiomas** en los editores de arrastrar y soltar para correo electrónico y bloques de contenido) y selecciona al menos una configuración regional para la que quieras añadir traducciones.

![El desplegable Añadir configuración regional con opciones para seleccionar la configuración regional predeterminada o atributos personalizados.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Bloques de contenido que contienen traducciones

Si tu mensaje contiene bloques de contenido que ya tienen traducciones guardadas, no necesitas volver a cargar esas traducciones. Las traducciones guardadas se aplican automáticamente cuando el bloque de contenido se añade a tu mensaje.

En el modal **Administrar idiomas**, los bloques de contenido con traducciones guardadas aparecen en la lista, junto con las configuraciones regionales que admiten. Esto te permite ver qué partes de tu mensaje ya están localizadas antes de añadir nuevas traducciones.

![La sección Administrar idiomas con una lista de bloques de contenido que tienen traducciones guardadas.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Asegúrate de que cada bloque de contenido incluya traducciones para cada configuración regional añadida a tu mensaje. Si a un bloque de contenido le faltan traducciones para una de las configuraciones regionales que añadiste, se mostrará en su idioma original para los usuarios de esa configuración regional.
{% endalert %}

### Paso 4: Añade traducciones

Después de seleccionar las configuraciones regionales, añade traducciones a tu mensaje usando uno de los siguientes métodos:

![La pestaña Añadir traducciones con opciones para cargar traducciones por CSV o conectándose con socios de traducción.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Upload CSV template %}

Selecciona **Descargar plantilla** para descargar un CSV que contiene una matriz con los ID de traducción y las configuraciones regionales seleccionadas. Introduce las traducciones para cada configuración regional. Carga el archivo completado y las traducciones se aplicarán a tu mensaje.

{% alert important %}
Para evitar problemas de visualización con caracteres no ingleses, evita usar Excel para tu CSV de traducción.
{% endalert %}

![CSV con etiquetas de traducción para un título, texto de oferta, monto de oferta y CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Use the translation API %}

Usa una API de traducción de un socio para gestionar y actualizar las traducciones en tus campañas y Canvas. Esto es útil si usas un sistema externo para la localización o quieres conectarte directamente con un socio de traducción.

Para usar los puntos de conexión de traducciones con Canvas, incluye los siguientes parámetros:
  - `workflow_id`
  - `step_id`
  - `message_variation_id` 

{% alert note %}
Cuando uses la API de traducción con pasos en Canvas que fueron creados después del lanzamiento del Canvas, el `message_variation_id` que pases a la API estará vacío o en blanco.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Vista previa de las traducciones

Para obtener una vista previa de tu mensaje, selecciona la opción **Usuario multilingüe** en el menú desplegable **Vista previa como usuario**. Esto te permite cambiar entre diferentes definiciones de configuración regional para previsualizar todas las traducciones de tu mensaje.

![Vistas previas de configuraciones regionales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Administrar traducciones

### Duplicar pasos en Canvas o campañas, y traducciones

Cuando duplicas un paso en Canvas, una campaña o una variante, las traducciones se incluyen. Esto también aplica cuando se copian entre espacios de trabajo, siempre y cuando las configuraciones regionales estén definidas en el espacio de trabajo de destino. Asegúrate de revisar y actualizar las traducciones según corresponda cuando realices modificaciones en tu Canvas o campaña.

### Guardar traducciones en bloques de contenido

Los bloques de contenido admiten multilingüe de la misma manera que los mensajes. Al crear o editar bloques de contenido, puedes etiquetar contenido para traducción, añadir configuraciones regionales y cargar traducciones usando un CSV o la [API de traducción]({{site.baseurl}}/api/endpoints/translations/).

Las traducciones guardadas permanecen asociadas al bloque de contenido. Cuando el bloque se añade a un mensaje, sus traducciones se incluyen automáticamente.

### Mensajes de derecha a izquierda

Al rellenar el archivo de traducción para idiomas que se escriben de derecha a izquierda (como el árabe), envuelve la traducción con `span` para que se formatee correctamente:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Seguimiento de enlaces de correo electrónico

En las campañas de correo electrónico, Braze realiza el seguimiento de enlaces añadiendo información de seguimiento (parámetros de consulta) a cada URL. Este comportamiento es compatible tanto con el [aliasing de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) como con las [plantillas de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template).

Cuando una URL está envuelta en etiquetas de traducción, es posible que Braze no pueda determinar dónde añadir esta información de seguimiento. Para asegurar que esto funcione correctamente, debes incluir un carácter especial al final de la URL para indicar dónde debe añadirse el seguimiento.

Las URLs usan dos caracteres especiales para controlar cómo funciona esto:
  - `?` añade seguimiento a una URL que aún no lo tiene.
  - `&` añade seguimiento adicional si ya hay un `?` presente en la URL. Una URL solo puede contener un `?`.

| URL | Contiene&nbsp;`?` | Descripción | Ejemplo |
| --- | --- | --- | --- |
| URL estándar | No | Añade `?` después de la etiqueta de traducción de cierre si la URL aún no contiene uno. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL estándar | Sí | Usa `&` al final de la URL (después de la etiqueta de traducción de cierre) si ya contiene `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Generada por Liquid | No | Usa `?` después de las etiquetas de traducción de cierre si la URL generada aún no contiene uno. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Generada por Liquid | Sí | Usa `&` después de la etiqueta de traducción de cierre si la URL generada ya contiene un `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Configuración de idioma y accesibilidad

Para canales basados en HTML (correo electrónico, mensaje dentro de la aplicación, banners, páginas de inicio y tarjetas de contenido), Braze añade un atributo de idioma de accesibilidad (`lang`) al mensaje renderizado. Este atributo ayuda a las tecnologías de asistencia, como los lectores de pantalla, a interpretar y pronunciar correctamente el texto.

Sin esto, un lector de pantalla asume que el contenido está en el idioma predeterminado que el usuario configuró en su dispositivo durante la configuración inicial. Si el mensaje está en un idioma diferente, es posible que el lector de pantalla no pronuncie todo correctamente.

#### Configurar el idioma de accesibilidad

Puedes establecer el idioma de accesibilidad en dos niveles:

##### Nivel de mensaje

En la configuración de tu mensaje, ve a la sección **Accesibilidad** y selecciona un idioma del menú desplegable o usa Liquid para establecer dinámicamente el idioma de accesibilidad. Esto se aplica a todo el contenido del mensaje.

##### Nivel de configuración regional

Para mensajes multilingües, establece el idioma de accesibilidad en cada configuración regional en **Configuración de localización**. Cuando se crean nuevos mensajes, {% raw %}`{{accessibility_language}}`{% endraw %} se selecciona de forma predeterminada en la sección **Accesibilidad**. Esto mapea el idioma de accesibilidad a tu configuración regional.

#### Estándares

El idioma de accesibilidad se mapea al atributo HTML `lang`, un [requisito de nivel A de WCAG 2.1](https://dequeuniversity.com/rules/axe/4.2/html-has-lang) (Criterio de éxito 3.1.1). Para contenido multilingüe, también puedes establecer el idioma en bloques de contenido individuales usando el atributo `lang` directamente en tu HTML.

## Preguntas frecuentes

#### ¿Cuáles son los límites para las etiquetas de traducción?

Al usar etiquetas de traducción, se aplican los siguientes límites:

- Cada mensaje puede tener hasta 200 etiquetas de traducción.
- Cada texto predeterminado (el contenido entre etiquetas de traducción) puede tener hasta 2000 caracteres.
- Las traducciones por configuración regional pueden tener hasta 409 600 bytes (aproximadamente 409,6&nbsp;KB).

#### ¿Puedo hacer un cambio en la copia traducida de una de mis configuraciones regionales?

Sí. Primero, realiza la edición en el CSV y luego vuelve a cargar el archivo para aplicar el cambio a la copia traducida.

### ¿Braze proporciona traducciones?

No. Debes [proporcionar tus propias traducciones](#step-4-add-translations) ya sea cargando un CSV o usando la API de traducción.

### ¿Puedo anidar etiquetas de traducción?

No.

#### ¿Puedo envolver mensajes HTML completos en una etiqueta de traducción?

No. Como buena práctica, solo debes envolver texto legible por humanos o contenido que necesite ser localizado. Esto ayuda a evitar que se rompan el formato, los enlaces u otros elementos que no son texto.

Además, considera envolver piezas de texto más pequeñas y semánticamente relacionadas para crear traducciones precisas y evitar limitaciones de rendimiento o tamaño.

#### ¿Puedo hacer un cambio en la copia traducida de una de mis configuraciones regionales?

Sí. Si usas un CSV, primero realiza la edición en el archivo y luego vuelve a cargarlo para aplicar el cambio a la copia traducida. Si usas la [API de traducción]({{site.baseurl}}/api/endpoints/translations/), usa los puntos de conexión de actualización para realizar cambios.

#### ¿Qué validaciones o comprobaciones adicionales realiza Braze?

| Escenario | Validación en Braze |
| --- | --- |
| Un mensaje contiene dos o más ID de traducción coincidentes que se mapean a textos diferentes. | Este archivo de traducción no se descargará. |
| A un archivo de traducción le faltan uno o más ID de etiquetas de traducción. | Este archivo de traducción no se cargará. |
| Un archivo de traducción contiene configuraciones regionales que faltan en el mensaje. | Este archivo de traducción no se cargará. |
| Las etiquetas de traducción deben añadirse a un mensaje antes de descargar la plantilla de traducción. | Este archivo de traducción no se descargará. |
| Las etiquetas de traducción encontradas en tu archivo cargado faltan en tu mensaje. | Las traducciones adicionales no se guardarán en el mensaje. |
| {% raw %}Un mensaje contiene una o más etiquetas de Liquid rotas. Para abrir etiquetas usa `{% translation your_id_here %}`, cierra las etiquetas de traducción con `{% endtranslation %}`.{% endraw %} | Este archivo de traducción no se descargará. |
| Un archivo de traducción contiene texto predeterminado que no coincide con lo que hay en el mensaje. | Las traducciones se añaden, pero el texto original del mensaje no se actualiza. |
| Una o más de las configuraciones regionales de un mensaje han sido eliminadas en la configuración y ya no existen. | Las traducciones que ya se han añadido siguen existiendo dentro del mensaje. Si se eliminan del mensaje, las traducciones se pierden. |
| Las etiquetas de traducción contienen URLs completas o URLs generadas por Liquid. | Las etiquetas de traducción que contienen URLs se identifican en caso de que surjan problemas con enlaces rotos o seguimiento de enlaces. |
| Las etiquetas de traducción incluyen parámetros de consulta. | Las etiquetas de traducción que contienen parámetros de consulta se identifican en caso de que surjan problemas con enlaces rotos o seguimiento de enlaces. |
| Las etiquetas de traducción contienen atributos o estructuras HTML. | Las etiquetas de traducción que contienen atributos o estructuras HTML se identifican en caso de que surjan problemas con estilos y formato. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }