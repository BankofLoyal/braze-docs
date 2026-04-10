---
nav_title: Registrar análisis
article_title: Registrar análisis 
page_order: 1
description: "Este artículo explica cómo registrar manualmente impresiones, clics, descartes y gestionar el comportamiento de clic en tus Tarjetas de contenido personalizadas."
toc_headers: "h2"

---

# Registrar análisis

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Análisis de Tarjetas de contenido faltantes

Si las Tarjetas de contenido aparecen correctamente en tu aplicación pero no recibes ningún análisis de forma consistente (destinatarios únicos, impresiones, clics, etc.), es probable que se trate de un problema de integración de SDK.

- **Vistas personalizadas de Tarjetas de contenido (Android, iOS, Web):** La interfaz predeterminada de Braze registra impresiones y clics automáticamente en todas las plataformas. Si estás utilizando una vista o implementación personalizada de Tarjetas de contenido, debes llamar explícitamente a los métodos de registro apropiados dentro de tu aplicación. Consulta [Registrar análisis]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) para tu plataforma. Para implementaciones Web personalizadas específicamente, asegúrate de que el SDK Web de Braze esté cargado, revisa la consola del navegador en busca de errores y verifica que se estén recibiendo los datos de las tarjetas.
- **Inicialización del SDK e identificación de usuarios:** Asegúrate de que el SDK esté completamente inicializado antes de mostrar las tarjetas. Los eventos se descartan silenciosamente (no se ponen en cola) si el SDK no está inicializado, está en modo de inicialización diferida o tiene el RGPD desactivado. El SDK sí registra análisis para usuarios anónimos, pero las métricas del dashboard como "destinatarios únicos" requieren una identidad de usuario resuelta, así que llama a `changeUser` antes de que se muestren las tarjetas siempre que sea posible.