---
nav_title: Configuración de localización
article_title: Configuración de localización
alias: "/multi_language_support/"
page_order: 5.5
description: "Este artículo ofrece un resumen de la configuración multilingüe en el panel de Braze y cómo utilizar las configuraciones regionales en tu mensajería."
---

# Configuración de localización

> La característica multilingüe te permite utilizar [etiquetas de traducción]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para dirigirte a usuarios de diferentes idiomas y ubicaciones, todo ello en un solo mensaje.

## Requisitos previos

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## Añadir una configuración regional

1. Ve a **Configuración** > **Configuración de localización**.
2. Selecciona **Añadir configuración regional** y, a continuación, selecciona **Configuración regional predeterminada** o **Atributos personalizados**.

![El desplegable "Añadir configuración regional" con opciones para seleccionar la configuración regional predeterminada o atributos personalizados.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}

{: start="3"}
3. Introduce un nombre para la configuración regional.
4. [Selecciona un idioma para accesibilidad]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/#language-settings-and-accessibility). Esta configuración permite que las tecnologías de asistencia, como los lectores de pantalla, pronuncien correctamente el texto.
5. Selecciona los atributos de usuario correspondientes a la opción de configuración regional que hayas elegido. Al configurar una configuración regional, puedes seleccionar idiomas a partir de los atributos de usuario predeterminados o de atributos personalizados. No puedes seleccionar de ambos.

{% tabs %}
{% tab Default locale %}

En **Configuración regional predeterminada**, utiliza los desplegables para seleccionar el idioma que se va a añadir y, opcionalmente, el país que se va a asociar al idioma.

![Una ventana llamada «Añadir configuración regional - Idioma y país predeterminados» para especificar el idioma y el país.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

Para **Atributos personalizados**, utiliza el desplegable para seleccionar el atributo personalizado asociado y, en el campo de texto, introduce el valor.

![Una ventana llamada «Añadir configuración regional - Atributos personalizados» para especificar el atributo personalizado y el valor.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Selecciona **Añadir configuración regional**.

Para conocer los pasos para utilizar estas configuraciones regionales en tus mensajes, consulta [Mensajes multilingües]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

## Consideraciones

- Puedes seleccionar hasta dos atributos personalizados en una única configuración regional, o hasta dos idiomas predeterminados para atributos de usuario. En ambos casos, el segundo atributo es opcional.
- Al editar los valores traducidos en el archivo CSV, evita modificar los valores predeterminados del archivo.
- La clave de configuración regional del archivo que has subido debe coincidir con la de tu configuración multilingüe.

### Soporte y priorización

- Si un usuario coincide tanto con una configuración regional definida por atributos personalizados como con una definida por atributos de usuario predeterminados, la configuración regional del atributo personalizado tiene prioridad.
- Los atributos personalizados admiten valores de texto (cadena) con coincidencia exacta.
- Si se elimina un atributo personalizado o se cambia su tipo, el usuario ya no podrá pertenecer a esa configuración regional y pasará a la siguiente en la lista de prioridades de configuraciones regionales a las que pertenece, o recibirá las traducciones de marketing predeterminadas.
- Si una configuración regional no es válida (el atributo personalizado ha cambiado o se ha eliminado), el error aparecerá en la página de **Soporte multilingüe**.

## Preguntas más frecuentes

#### ¿Cuántas configuraciones regionales puedo añadir?

Puedes añadir hasta 200 configuraciones regionales.

#### ¿Dónde se almacenan los archivos de traducción en Braze?

Los archivos de traducción se almacenan a nivel de campaña, lo que significa que cada variante de mensaje debe tener traducciones cargadas. Las traducciones también se pueden almacenar en bloques de contenido. Cuando el bloque se añade a un mensaje, sus traducciones se incluyen automáticamente.

#### ¿El nombre de la configuración regional tiene que seguir un patrón o formato específico?

No. Puedes utilizar la convención de nomenclatura que prefieras. El nombre de la configuración regional se utiliza al seleccionar la configuración regional en el editor y aparecerá en los encabezados del archivo que descargues con los ID de traducción.