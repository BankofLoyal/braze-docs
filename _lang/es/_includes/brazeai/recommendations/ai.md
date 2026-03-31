{% if include.section == "Plan-specific features" %}

## Características de IA específicas del plan

En la tabla siguiente se describen las diferencias entre la versión gratuita y la pro de los tipos de recomendación AI Personalizado, Más popular, Más reciente y Tendencias:

| Área                   | Versión gratuita                          | Versión pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Frecuencia de actualización de usuarios<sup>1</sup>   | Semanal                                | Diaria                                    |
| Frecuencia de reentrenamiento del modelo  | Mensual                               | Semanal                                   |
| Modelos de recomendación máximos | 1 modelo por tipo<sup>2</sup> | 100 modelos por tipo<sup>2</sup> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<sup>1. Es la frecuencia con la que se actualizan las recomendaciones de artículos específicas del usuario (solo AI Personalizado y Más reciente). Más popular y Tendencias son recomendaciones globales que se actualizan cuando el modelo se vuelve a entrenar. Por ejemplo, si un usuario compra un artículo recomendado basándose en las recomendaciones de artículos de IA, sus artículos recomendados se actualizarán según esta frecuencia.</sup><br>
<sup>2. Los tipos de recomendación disponibles son AI Personalizado, Más reciente, Más popular y Tendencias.</sup>

{% endif %}