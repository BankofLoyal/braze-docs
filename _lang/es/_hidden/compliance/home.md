---
nav_title: Documentación de conformidad
article_title: Documentación de conformidad
page_order: 1
permalink: /compliance_documentation/
toc_headers: h2
noindex: true
---

# Documentación de conformidad

_Fecha de revisión: 30 de marzo de 2026_

## ¿Qué incluye la documentación de conformidad?

La documentación de conformidad que figura a continuación establece los términos específicos aplicables a tu producto, canal, característica, funcionalidad o servicio adquiridos:

- Para la funcionalidad de los servicios de Braze que permite a los clientes interactuar con, integrarse con o acceder al producto, sitio web, aplicación o servicio de un proveedor externo, la documentación de conformidad contiene los términos del proveedor externo aplicables a tu uso de dicha funcionalidad; y
- Cualquier práctica y norma general del sector que los clientes de Braze deban cumplir para el uso de dicho producto, canal, característica, funcionalidad o servicio de Braze.

## Actualizaciones de la documentación de conformidad

Puedes suscribirte para recibir actualizaciones de nuestra documentación (incluida la documentación de conformidad) a través del [repositorio de GitHub de Braze](https://github.com/braze-inc/braze-docs).

## Documentación de conformidad para canales, integraciones y características específicos

A continuación se muestra la lista de nuestros productos, canales, características, funcionalidades y servicios que tienen documentación de conformidad aplicable. Si utilizas varios productos, se aplica toda la documentación de conformidad pertinente.

### Términos generales

Sin limitar ninguna obligación del cliente en virtud del acuerdo, y para evitar cualquier duda, el cliente será el único responsable de obtener todos los derechos, consentimientos y autorizaciones necesarios, y de proporcionar avisos de privacidad legalmente adecuados en relación con su uso, así como de obtener todos los consentimientos y autorizaciones legalmente requeridos para el uso de los canales y características que se enumeran a continuación.

## Canales y características

1. [Canal de mensajería móvil](#mobile-messages-channel)
2. [Canal de webhooks](#webhooks-channel)
3. [Documentación de conformidad del canal WhatsApp](#hatsapp-channel-compliance-documentation)
4. [Documentación de conformidad del canal LINE](#line-channel-compliance-documentation)
5. [Documentación de conformidad de la integración con Shopify](#shopify-integration-compliance-documentation)
6. [Documentación de conformidad de Audience Sync](#audience-sync-compliance-documentation)
7. [Documentación de conformidad del archivo de mensajes y cifrado a nivel de campo](#message-archiving-and-field-level-encryption-compliance-documentation)
8. [Documentación de conformidad de la consola de agente](#agent-console-compliance-documentation)
9. [Documentación de conformidad del canal KakaoTalk](#kakaotalk-channel-compliance-documentation)

## 1. Canal de mensajería móvil {#mobile-messages-channel}

Los siguientes términos adicionales se aplican en relación con el uso del canal de mensajería móvil por parte del cliente:

### Definiciones

"**Agregadores**", "**Operadores**" o "**Intermediarios de mensajería móvil**" se refieren a intermediarios externos que (i) transmiten mensajes móviles entre proveedores de mensajería móvil y operadores; (ii) son proveedores de servicios inalámbricos (por ejemplo, T-Mobile, AT\&T, etc.); y/o (iii) participan en la transmisión de mensajes RCS desde proveedores de mensajería móvil a usuarios finales.

**"Proveedores de SMS/MMS" o "Proveedores de mensajería móvil"** se refieren a los subencargados de Braze utilizados en la transmisión de mensajes SMS, MMS y/o RCS, según se identifican en [www.braze.com/subprocessors](http://www.braze.com/subprocessors).

"**Mensajes SMS/MMS**" o "**Mensajes móviles**" se refieren a mensajes SMS, MMS y/o RCS.

### Normas y mejores prácticas aplicables del sector

Al enviar mensajes móviles, los clientes deben cumplir con las políticas de uso aceptable y de mensajería aplicables de los proveedores de mensajería móvil, las normas y directrices aplicables del sector y, cuando corresponda, los códigos del sector y las directrices aplicables de los intermediarios de mensajería móvil para cualquier país donde el cliente pretenda enviar mensajes móviles, como se detalla en la [Política de uso aceptable](https://www.braze.com/company/legal/aup/) de Braze.

Los terceros involucrados en el envío de mensajes móviles, incluidos los intermediarios de mensajería móvil, pueden imponer tarifas o penalizaciones basadas en mensajes móviles enviados en violación de sus términos o de las leyes aplicables. El cliente es responsable de pagar las tarifas y penalizaciones que resulten de la violación por parte del cliente de dichos términos de terceros, independientemente de si dichas tarifas o penalizaciones se imponen al cliente o a Braze.

### Subencargados

Braze puede utilizar cualquier proveedor de mensajería móvil que esté incluido en su lista de subencargados en [www.braze.com/subprocessors](https://www.braze.com/subprocessors/).

Sin perjuicio de lo anterior, en caso de que el cliente envíe mensajes móviles utilizando el modelo "Trae tu propio (BYO) conector SMS", los proveedores de mensajería móvil involucrados en el envío se considerarán proveedores externos (según se define en el acuerdo) y no subencargados de Braze, y las exenciones de responsabilidad que se indican a continuación se aplicarán a dichos proveedores externos.

### Términos de excepción para el uso de webhooks

Aplicable a los clientes que se hayan suscrito a créditos de mensajes a partir del 9 de diciembre de 2024 (según la fecha de entrada en vigor del formulario de pedido): las restricciones descritas en la documentación de conformidad del canal de webhooks no se aplican al uso de webhooks para enviar mensajes móviles a través de una plataforma de proveedor externo.

### Conector SMS propio (BYO)

Los clientes pueden enviar mensajes móviles desde Braze utilizando proveedores externos a través del modelo "BYO SMS Connector". Sin perjuicio de lo anterior, los clientes no utilizarán el modelo BYO SMS Connector para enviar mensajes móviles a Estados Unidos y Canadá.

### Exenciones de responsabilidad

Braze renuncia a cualquier declaración, garantía, responsabilidad y obligación de indemnización con respecto a cualquier proveedor externo o intermediario de mensajería móvil involucrado en el envío o procesamiento de mensajes móviles, incluida la responsabilidad relacionada con la capacidad del sistema, el rendimiento de mensajes o la entrega real al dispositivo de un usuario final.

## 2. Canal de webhooks {#webhooks-channel}

Los siguientes términos adicionales se aplican en relación con el uso del canal de webhooks por parte del cliente:

### Términos de uso del canal de webhooks

A menos que se permita de otro modo en la documentación de conformidad del canal aplicable, (a) el cliente no utilizará webhooks cuando Braze ofrezca capacidades nativas para lograr el mismo resultado, y (b) el cliente no utilizará un webhook para desencadenar el envío de cualquier mensaje a través de una plataforma de proveedor externo en la medida en que Braze proporcione un mecanismo nativo para enviar dichos mensajes a través de los servicios de Braze.

Si Braze pone a disposición general un mecanismo nuevo o actualizado en los servicios de Braze durante el período de suscripción actual del cliente, entonces el cliente tendrá prohibido usar webhooks para desencadenar el envío de mensajes a través de la plataforma de terceros especificada a partir de seis (6) meses después de la fecha de lanzamiento general del nuevo mecanismo o al final del año en curso del período de suscripción del cliente, lo que ocurra más tarde.

### Excepciones a los términos de uso del canal de webhooks

Consulta [Canal de mensajería móvil](#mobile-messages-channel) y [Canal WhatsApp](#whatsapp-channel-compliance-documentation)

### Exención de responsabilidad

Braze renuncia a toda responsabilidad con respecto al uso de webhooks por parte del cliente para desencadenar el envío de cualquier mensaje o cualquier otra acción fuera de los servicios de Braze.

## 3. Documentación de conformidad del canal WhatsApp {#whatsapp-channel-compliance-documentation}

Los siguientes términos adicionales se aplican en relación con el uso del canal WhatsApp por parte del cliente:

### Términos aplicables del proveedor externo

El cliente deberá cumplir con todos los requisitos previos, términos y políticas aplicables al canal WhatsApp, incluidos los términos requeridos por WhatsApp, LLC y sus empresas afiliadas, como se describe en la página de [configuración de WhatsApp](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/overview/) de Braze.

### Términos de excepción para el uso de webhooks

El cliente no podrá usar webhooks para desencadenar el envío de mensajes a través del canal WhatsApp a menos que sea con fines de soporte al cliente, como casos de uso de chat asistido por humanos y/o casos de uso de chatbot.

### Conector WhatsApp propio (BYO)

Los clientes pueden conectar sus cuentas directas de WhatsApp con Braze utilizando el "BYO Whatsapp Connector".

## 4. Documentación de conformidad del canal LINE {#line-channel-compliance-documentation}

Los siguientes términos adicionales se aplican en relación con el uso del canal LINE por parte del cliente:

### Requisitos previos

Para enviar mensajes a través del canal LINE, los clientes deben obtener una cuenta oficial verificada de LINE, que es aprobada y otorgada por LINE a su entera discreción. Los clientes deben asegurarse de obtener una cuenta oficial verificada de LINE antes de adquirir créditos de mensajes de Braze para el uso del canal LINE.

### Términos aplicables del proveedor externo

Al utilizar el canal LINE, el cliente acepta cumplir y quedar vinculado por, según corresponda, todos los términos y políticas requeridos por LY Corporation y sus afiliadas (colectivamente "LINE"), incluidos, entre otros, los Términos de uso de la cuenta oficial de LINE, los Términos de uso de la API de la cuenta oficial, las Directrices de la cuenta oficial de LINE, la Política de datos de usuario de LINE y cualquier política, término, directriz y documentación incorporados por referencia a los mismos (colectivamente, los "Términos de LINE"). Para mayor claridad, el cliente es responsable de: (i) garantizar que cualquier dato procesado en relación con LINE se procese de acuerdo con los Términos de LINE según corresponda; y (ii) cualquier tarifa o pago adeudado a LINE por el uso de los servicios de LINE en relación con el canal LINE.

Sin perjuicio de cualquier disposición en contrario en los Términos de LINE, el cliente sigue siendo el principal responsable de su uso de los servicios de LINE.


## 5. Documentación de conformidad de la integración con Shopify {#shopify-integration-compliance-documentation}

Los siguientes términos adicionales se aplican en relación con el uso de la integración con Shopify por parte del cliente en conexión con los servicios de Braze ("**Integración con Shopify**"):

El cliente acepta cumplir y quedar vinculado por cualquier término y condición, política, directriz y documentación aplicable de Shopify Inc. o cualquiera de sus afiliadas ("**Shopify**") aplicable al uso de la integración con Shopify.

El cliente reconoce que Shopify puede en cualquier momento y a su entera discreción: (i) requerir que Braze deshabilite o bloquee el acceso del cliente a la integración con Shopify; o (ii) dejar de proporcionar, suspender o terminar el acceso del cliente a la integración con Shopify. Braze no tendrá responsabilidad alguna con respecto a que Shopify deje de proporcionar acceso a la integración con Shopify al cliente o a través de los servicios de Braze en general.

## 6. Documentación de conformidad de Audience Sync {audience-sync-compliance-documentation}

Los siguientes términos adicionales se aplican al uso de Audience Sync por parte del cliente.

### Términos aplicables del proveedor externo

El cliente acepta cumplir y quedar vinculado por cualquier término y condición, política, directriz y documentación aplicable de los proveedores externos que el cliente utilice en conexión con cualquier integración de Audience Sync.

El cliente reconoce que los proveedores externos pueden revisar, examinar y/o eliminar cualquier dato, anuncio o contenido utilizado en conexión con sus servicios.

## 7. Documentación de conformidad del archivo de mensajes y cifrado a nivel de campo {#message-archiving-and-field-level-encryption-compliance-documentation}

### Exención de responsabilidad
El cliente reconoce que el uso del archivo de mensajes y/o el cifrado a nivel de campo (cada uno, la "**Característica**") puede afectar la velocidad de envío de los mensajes enviados a través de los servicios de Braze. Braze no será responsable de dicho impacto, y cualquier compromiso de velocidad de envío no se aplicará cuando el cliente esté utilizando la característica. La característica puede utilizarse para respaldar los esfuerzos de cumplimiento del cliente; sin embargo, el cliente reconoce que Braze no hace declaraciones ni garantías con respecto a si el uso de la característica en sí satisface las obligaciones de cumplimiento del cliente, y renuncia a toda responsabilidad en relación con ello.

## 8. Documentación de conformidad de la consola de agente {#agent-console-compliance-documentation}

### Proveedores de LLM como subencargados o proveedores externos

Cuando el cliente utiliza una integración con un modelo de lenguaje grande proporcionado por Braze a través de la opción Braze Auto en los servicios de Braze ("LLM proporcionado por Braze"), el proveedor de dicho LLM proporcionado por Braze actuará como subencargado de Braze, sujeto a los términos del Anexo de procesamiento de datos (DPA) entre el cliente y Braze.

Si el cliente elige traer su propia clave de API para integrarse con la funcionalidad de Braze AI, el proveedor de la suscripción LLM propia del cliente se considerará un proveedor externo, según se define en el contrato entre el cliente y Braze.

## 9. Documentación de conformidad del canal KakaoTalk {#kakaotalk-channel-compliance-documentation}

Los siguientes términos adicionales se aplican en relación con el uso del canal KakaoTalk por parte del cliente:

### Requisitos previos

Para enviar mensajes a través del canal KakaoTalk, los clientes primero deben obtener una cuenta de KakaoTalk y contratar los servicios de KakaoTalk con los proveedores externos involucrados en la provisión de la funcionalidad de KakaoTalk al cliente ("Proveedores externos de KakaoTalk"). Las cuentas de KakaoTalk son aprobadas y otorgadas por dichos proveedores externos de KakaoTalk a su entera discreción.

### Términos aplicables del proveedor externo

Al utilizar el canal KakaoTalk, el cliente acepta cumplir y quedar vinculado por cualquier término y política aplicable de KakaoTalk y de los proveedores externos de KakaoTalk (colectivamente, los "Términos de KakaoTalk") y ser responsable de su uso de los servicios de KakaoTalk. Para mayor claridad, el cliente es responsable de cualquier tarifa o pago adeudado a KakaoTalk y/o a los proveedores externos de KakaoTalk por el uso de dichos servicios de proveedores externos de KakaoTalk en conexión con el canal KakaoTalk.

{% multi_lang_include braze_legal/english_language_governance.md %}