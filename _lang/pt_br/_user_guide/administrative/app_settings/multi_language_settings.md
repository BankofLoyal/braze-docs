---
nav_title: Configurações de localização
article_title: Configurações de localização
alias: "/multi_language_support/"
page_order: 5.5
description: "Este artigo fornece uma visão geral das configurações multilíngues no dashboard da Braze e como usar localidades no seu envio de mensagens."
---

# Configurações de localização

> O recurso multilíngue permite que você use [tags de tradução]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para direcionar usuários em diferentes idiomas e locais, tudo dentro de uma única mensagem.

## Pré-requisitos

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## Adicionar uma localidade

1. Acesse **Configurações** > **Configurações de Localização**.
2. Selecione **Add locale** e, em seguida, selecione **Default locale** ou **Custom Attributes**.

![O menu suspenso "Add locale" com opções para selecionar a localidade padrão ou atributos personalizados.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}

{: start="3"}
3. Digite um nome para a localidade.
4. [Selecione um idioma para acessibilidade]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/#language-settings-and-accessibility). Essa configuração permite que tecnologias assistivas, como leitores de tela, pronunciem o texto corretamente.
5. Selecione os respectivos atributos do usuário para a opção de localidade escolhida. Ao configurar uma localidade, você pode selecionar idiomas nos atributos padrão do usuário ou nos atributos personalizados. Não é possível selecionar de ambos.

{% tabs %}
{% tab Default locale %}

Para **Localidade padrão**, use os menus suspensos para selecionar o idioma a ser adicionado e, opcionalmente, o país a ser associado ao idioma.

![Uma janela chamada "Adicionar localidade - Idioma e País Padrão" para especificar o idioma e o país.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

Para **Atributos personalizados**, use o menu suspenso para selecionar o atributo personalizado associado e, no campo de texto, insira o valor.

![Uma janela chamada "Adicionar localidade - Atributos Personalizados" para especificar o atributo personalizado e o valor.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Selecione **Add locale**.

Para saber como usar essas localidades nas suas mensagens, consulte [Mensagens multilíngues]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

## Considerações

- É possível selecionar até dois atributos personalizados em uma única localidade ou até dois idiomas padrão de atributos de usuário. Em ambos os casos, o segundo atributo é opcional.
- Ao fazer edições nos valores traduzidos no arquivo CSV, evite modificar quaisquer valores padrão no arquivo.
- A chave de localidade no arquivo enviado deve corresponder àquela nas suas configurações multilíngues.

### Suporte e priorização

- Se um usuário corresponder tanto a uma localidade definida por atributos personalizados quanto a uma definida por atributos padrão do usuário, a localidade de atributo personalizado será priorizada.
- Atributos personalizados aceitam valores de texto (string) com correspondência exata.
- Se um atributo personalizado for excluído ou seu tipo for alterado, o usuário não poderá mais se enquadrar nessa localidade e irá descer na lista de prioridades das localidades às quais pertence ou receberá as traduções de marketing padrão.
- Se uma localidade for inválida (o atributo personalizado foi alterado ou excluído), o erro aparecerá na página **Multi-Language Support**.

## Perguntas frequentes

#### Quantas localidades posso adicionar?

Você pode adicionar até 200 localidades.

#### Onde os arquivos de tradução são armazenados na Braze?

Os arquivos de tradução são armazenados no nível da campanha, o que significa que cada variante de mensagem deve ter traduções enviadas. As traduções também podem ser armazenadas em Content Blocks. Quando o bloco é adicionado a uma mensagem, suas traduções são incluídas automaticamente.

#### O nome da localidade precisa seguir um padrão ou formato específico?

Não. Você pode usar sua convenção de nomenclatura preferida. O nome da localidade é usado ao selecionar a localidade no editor e estará nos cabeçalhos do arquivo que você baixar com os IDs de tradução.