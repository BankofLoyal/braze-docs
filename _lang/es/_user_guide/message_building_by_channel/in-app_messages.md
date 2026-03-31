---
nav_title: "Mensajes dentro de la aplicación"
article_title: Mensajes dentro de la aplicación
page_order: 3
alias: /in-app_messages/
description: "Esta página de inicio alberga todos los mensajes dentro de la aplicación. Aquí encontrarás artículos sobre cómo crear mensajes dentro de la aplicación, el editor de arrastrar y soltar, cómo personalizar tus mensajes, informes y mucho más."
channel:
  - in-app messages
search_rank: 5
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Mensajes dentro de la aplicación

> Los mensajes dentro de la aplicación te ayudan a entregar contenido a tus usuarios sin interrumpir su día con una notificación push, ya que estos mensajes no se entregan fuera de la aplicación del usuario y no invaden su pantalla de inicio. 

Los mensajes personalizados y adaptados dentro de la aplicación mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con una gran variedad de diseños y herramientas de personalización para elegir, los mensajes dentro de la aplicación atraen a tus usuarios más que nunca. Vienen con contexto, tienen menor urgencia y se entregan cuando el usuario está activo dentro de tu aplicación. Para ver ejemplos de mensajes dentro de la aplicación, consulta las [historias de nuestros clientes](https://www.braze.com/customers/).

## Casos de uso

Con el rico nivel de contenido que ofrecen los mensajes dentro de la aplicación, puedes aprovechar este canal para una gran variedad de casos de uso:

| Caso de uso | Explicación |
| --- | --- |
| Preparación para las notificaciones push | Ejecuta una campaña de [preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) utilizando un mensaje enriquecido dentro de la aplicación para mostrar a tus clientes las ventajas de optar por push para tu aplicación o sitio web, y preséntales una solicitud para que concedan permiso push.
| Ventas y promociones | Utiliza mensajes modales dentro de la aplicación para recibir a los clientes con medios visualmente atractivos que contengan códigos promocionales u ofertas estáticas. Incentívalos para que realicen compras o conversiones cuando de otro modo no lo habrían hecho. |
| Fomentar la adopción de características | Anima a los clientes a utilizar otras partes de tu aplicación o a aprovechar un servicio. |
| Campañas altamente personalizadas | Coloca mensajes dentro de la aplicación como lo primero que ven tus clientes cuando entran en tu aplicación o sitio web. Añade algunas características de personalización de Braze, como [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), para impulsar a los usuarios a actuar y, por tanto, hacer que tu difusión sea más eficaz.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Otros casos de uso a tener en cuenta son los siguientes:

- Nuevas características de la aplicación
- Gestión de aplicaciones
- Reseñas
- Mejoras o actualizaciones de la aplicación
- Regalos y sorteos

## Tipos de mensajes estándar

Las siguientes pestañas muestran cómo se ve para tus usuarios al abrir uno de nuestros tipos de mensajes estándar dentro de la aplicación: mensajes de deslizamiento hacia arriba, modales y a pantalla completa dentro de la aplicación.

{% tabs %}
{% tab Deslizamiento hacia arriba %}

Los mensajes de deslizamiento hacia arriba suelen aparecer en la parte superior e inferior de la pantalla de la aplicación (puedes configurarlo al crear tu mensaje). Son ideales para alertar a tus usuarios sobre nuevas condiciones de servicio, cookies y otros fragmentos de información.

![Mensaje de deslizamiento hacia arriba dentro de la aplicación que aparece desde la parte inferior de la pantalla de la aplicación. El deslizamiento hacia arriba incluye una imagen de icono y un breve mensaje.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Los modales aparecen en el centro de la pantalla del dispositivo con una superposición de pantalla que les ayuda a destacarse de tu aplicación en segundo plano. Son perfectos para sugerir de forma no tan sutil que el usuario aproveche una oferta o sorteo.

![Mensaje modal dentro de la aplicación que aparece en el centro de una aplicación y sitio web en forma de diálogo. El modal incluye una imagen, un encabezado, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Pantalla completa %}

Los mensajes a pantalla completa son exactamente lo que esperas: ¡ocupan toda la pantalla del dispositivo! Este tipo de mensaje es ideal cuando realmente necesitas la atención de tu usuario, como en el caso de las actualizaciones obligatorias de la aplicación.

![Mensaje a pantalla completa dentro de la aplicación que ocupa la pantalla de una aplicación. El mensaje a pantalla completa incluye una imagen grande, un encabezado, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Además de estas plantillas de mensajes predeterminadas, también puedes personalizar aún más tu mensajería utilizando mensajes HTML personalizados dentro de la aplicación, ventanas modales web con CSS o formularios web de captura de correo electrónico. Para más información, consulta [Personalización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Mensajes dentro de la aplicación con plantillas

Los mensajes dentro de la aplicación se entregan como mensajes dentro de la aplicación con plantillas cuando se selecciona **Reevaluar la elegibilidad de la campaña antes de mostrarla** o si alguna de las siguientes etiquetas de Liquid existe en el mensaje:

- `canvas_entry_properties`
- `connected_content`
- Variables SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Esto significa que, al inicio de la sesión, el dispositivo recibirá el desencadenante de ese mensaje dentro de la aplicación en lugar del mensaje completo. Cuando el usuario activa el mensaje dentro de la aplicación, el dispositivo del usuario hará una solicitud de red para obtener el mensaje real.

{% alert note %}
El mensaje no se entregará si el dispositivo no tiene acceso a Internet. Es posible que el mensaje no se entregue si la lógica de Liquid tarda demasiado en resolverse.
{% endalert %}

## Comportamiento de cancelación

En Braze, una cancelación ocurre cuando un usuario realiza una acción que lo hace elegible para recibir un mensaje, pero no lo recibe porque la lógica de Liquid lo marca como no elegible. Por ejemplo:

1. Sam realiza una acción que debería desencadenar una campaña por correo electrónico.
2. El cuerpo del correo electrónico contiene una lógica Liquid que indica que si la puntuación de un atributo personalizado es inferior a 50, no se debe enviar este correo electrónico.
3. La puntuación del atributo personalizado de Sam es 20.
4. Braze reconoce que Sam no debería recibir este correo electrónico, por lo que se cancela el envío.
5. Se registra un evento de cancelación.

Sin embargo, dado que los mensajes dentro de la aplicación son un canal de extracción, las cancelaciones funcionan de forma ligeramente diferente en este caso.

### Comportamiento de cancelación de mensajes dentro de la aplicación

Los mensajes dentro de la aplicación son descargados por el dispositivo al inicio de la sesión y almacenados en la caché del dispositivo, por lo que, independientemente de la calidad de la conexión a Internet, el mensaje se puede entregar al usuario al instante. Por ejemplo, si un usuario recibe cinco mensajes dentro de la aplicación durante su sesión, los recibirá todos al inicio de la sesión. Los mensajes se almacenarán en caché localmente y aparecerán cuando se produzcan los eventos desencadenantes definidos (inicio de sesión, el usuario hace clic en un botón que registra un evento personalizado, u otros).

En otras palabras, la lógica que determina si debemos cancelar un mensaje dentro de la aplicación se produce **antes de que** se haya producido el desencadenante. Para demostrarlo, supongamos que Sam, del ejemplo del correo electrónico, está suscrito a las notificaciones push.

1. Sam inicia una sesión abriendo una aplicación basada en Braze en su teléfono.
2. Según los criterios de audiencia de las campañas activas en el espacio de trabajo, Sam podría ser elegible para cinco campañas diferentes. Las cinco se descargan en su teléfono y se almacenan en la caché.
3. Sam **no ha** realizado ninguna acción que pudiera desencadenar estos mensajes, pero podría recibirlos durante la sesión.
4. El Liquid en dos de los mensajes dentro de la aplicación tiene reglas que excluyen a Sam de recibir el mensaje (como que su atributo personalizado de puntuación no sea lo suficientemente alto).
5. A Sam no se le envían los dos mensajes dentro de la aplicación que lo excluyen, pero sí se le envían los otros tres mensajes.
6. No se registran eventos de cancelación.

Braze no registra ningún evento de cancelación en el caso de Sam porque esto no cumple con nuestra definición de cancelación; Sam **no** realizó ninguna acción que pudiera desencadenar los mensajes. En el caso de los mensajes dentro de la aplicación, los usuarios nunca llegan a activar el desencadenante antes de que Braze determine que no deben ver el mensaje.

#### Comportamiento de cancelación de mensajes dentro de la aplicación con plantillas

[Los mensajes dentro de la aplicación con plantillas](#templated-in-app-messages) obligan al SDK a reevaluar si un mensaje debe mostrarse cuando se produce el evento desencadenante. Esto tiene un comportamiento de cancelación diferente. Para demostrarlo, consideremos este ejemplo:

1. Sam inicia una sesión de Braze al abrir una aplicación basada en Braze en su teléfono.
2. Los criterios de audiencia de las campañas activas indican que Sam podría ser elegible para recibir un mensaje dentro de la aplicación con plantilla, por lo que la información del desencadenante se envía a su dispositivo sin la carga útil del mensaje.
3. Sam selecciona un botón que registra un evento personalizado, lo que desencadena el mensaje dentro de la aplicación con plantilla.
4. El dispositivo de Sam realiza una solicitud de red para recuperar el mensaje dentro de la aplicación.
5. La lógica Liquid del mensaje conduce a una cancelación, por lo que Braze lo registra como tal; Sam realizó la acción desencadenante antes de esta evaluación.

##### Comparación del comportamiento de cancelación de mensajes dentro de la aplicación

Esta tabla compara los flujos de mensajes dentro de la aplicación que experimentó Sam:

| Mensaje dentro de la aplicación | Comportamiento de cancelación |
| --- | --- |
| Estándar | No se registró ningún evento de cancelación porque Sam no realizó ninguna acción que desencadenara un mensaje.<br><br>Los mensajes estándar dentro de la aplicación no registran cancelaciones porque la definición de cancelación es «no se vio el mensaje a pesar de realizar la acción desencadenante». Dado que los mensajes dentro de la aplicación se entregan al dispositivo antes de que se produzcan las acciones desencadenantes, no tiene sentido considerar que los mensajes dentro de la aplicación se omiten debido a la lógica de Liquid. |
| Con plantilla | Se registró un evento de cancelación porque Sam realizó la acción desencadenante para activar el mensaje con plantilla dentro de la aplicación, pero recibió una cancelación en la plantilla Liquid. <br><br>Los mensajes con plantilla dentro de la aplicación registran cancelaciones porque la evaluación de Liquid se produce después de que se haya realizado la acción desencadenante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Más recursos

Antes de empezar a crear tus propias campañas de mensajes dentro de la aplicación, o de utilizar mensajes dentro de la aplicación en una campaña multicanal, te recomendamos encarecidamente que consultes nuestra [guía de preparación de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). Esta guía abarca cuestiones de segmentación, contenido y conversión que debes tener en cuenta a la hora de crear mensajes dentro de la aplicación.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}