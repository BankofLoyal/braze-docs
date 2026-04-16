{% if include.section == "Plan-specific features" %}

## Recursos de IA específicos do plano

A tabela a seguir descreve as diferenças entre a versão gratuita e a versão pro dos tipos de recomendação IA Personalizado, Mais Popular, Mais Recente e Tendências:

| Área                   | Versão gratuita                          | Versão pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Frequência de atualização do usuário<sup>1</sup>   | Semanal                                | Diária                                    |
| Frequência de retreinamento do modelo  | Mensal                               | Semanal                                   |
| Máximo de modelos de recomendação | 1 modelo por tipo<sup>2</sup> | 100 modelos por tipo<sup>2</sup> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<sup>1. Essa é a frequência com que as recomendações de itens específicos do usuário são atualizadas (somente IA Personalizado e Mais Recente). Mais Popular e Tendências são recomendações globais que são atualizadas quando o modelo é retreinado. Por exemplo, se um usuário comprar um item recomendado com base nas recomendações de itens de IA, seus itens recomendados serão atualizados de acordo com essa frequência.</sup><br>
<sup>2. Os tipos de recomendação disponíveis são IA Personalizado, Mais Recente, Mais Popular e Tendências.</sup>

{% endif %}