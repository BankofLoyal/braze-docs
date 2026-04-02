---
nav_title: Mensagens multilíngues
article_title: Mensagens multilíngues
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artigo fornece etapas sobre como usar locais nas suas mensagens."
---

# Mensagens multilíngues

> Depois de adicionar locais ao seu espaço de trabalho, você pode direcionar usuários em diferentes idiomas em um único push, e-mail, banner, mensagem no app ou bloco de conteúdo.

## Pré-requisitos

{% tabs %}
{% tab Multi-language locales %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Message types %}

| Recurso | Permissões de usuário necessárias |
| --- | --- |
| Tipos&nbsp;de&nbsp;mensagem | Você precisa destas permissões para adicionar locais e traduções a campanhas e canvas:<br><br> {::nomarkdown}Permissões granulares: <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul> Permissões legadas: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Templates %}

| Recurso | Permissões de usuário necessárias |
| --- | --- |
| Modelos | Você precisa destas permissões para o tipo de modelo ao qual deseja adicionar locais e traduções:<br><br> {::nomarkdown}Permissões granulares: <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul> Permissões legadas: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Uso de locais

### Etapa 1: Configure os locais

Antes de adicionar traduções a uma mensagem, você deve primeiro [criar os locais que deseja suportar]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/). Os locais definem as variantes de idioma (e opcionalmente região) disponíveis para envio de mensagens.

### Etapa 2: Marque o conteúdo para tradução

Envolva o texto que deseja traduzir com as Liquid tags de tradução {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} e atribua um ID de tag. Os IDs das tags de tradução devem ser únicos dentro de uma mensagem. Considere usar nomes de ID semânticos que descrevam claramente o texto, como {% raw %}`{% translation header %}`{% endraw %}.

Aqui está um exemplo de mensagem marcada para tradução: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Destaque o texto que deseja traduzir e use o atalho de teclado **Cmd + Alt + L** (macOS) ou **Ctrl + Alt + L** (Windows) para envolver nas tags de tradução.<br><br> Esse atalho funciona em todos os canais que suportam envio de mensagens multilíngue, exceto nos editores de arrastar e soltar para e-mail e blocos de conteúdo. Para esses, use o botão **Add personalization** na barra lateral esquerda para adicionar tags de tradução.
{% endalert %}

#### Localizando URLs

Ao traduzir conteúdo, URLs exigem tratamento especial para evitar links quebrados.

##### URLs padrão (estáticas)

URLs estáticas são inseridas manualmente no editor (por exemplo, `https://example.com`). Também recomendamos o seguinte:

| Recomendação | Motivo |
| --- | --- |
| Mantenha o protocolo (`https://`) fora das tags de tradução. Envolva apenas o domínio e o caminho (por exemplo, `example.com/en`). | Tradutores podem acidentalmente alterar ou remover caracteres especiais, causando links quebrados. |
| Não inclua parâmetros de consulta dentro das tags de tradução (por exemplo, `?utm_source=promo`). | Tradutores podem acidentalmente alterar ou remover caracteres especiais, resultando em links quebrados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Uma URL padrão que segue ambas as recomendações é:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz%}{% endtranslation %}">Click Here</a>
```
{% endraw %}

{% alert important %}
Se você estiver usando [rastreamento de links de e-mail](#email-link-tracking) (link aliasing ou modelos de link), é necessária configuração adicional quando URLs estão envolvidas em tags de tradução.
{% endalert %}

#### Atributos e estrutura HTML

Envolva apenas texto legível por humanos nas tags de tradução. Evite envolver atributos HTML (como `class`, `style` ou `id`) ou outro código estrutural. Atributos HTML controlam layout, estilização e funcionalidade. Envolvê-los em tags de tradução pode quebrar a formatação ou os estilos nas versões localizadas da sua mensagem.

Este texto está corretamente envolvido:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Texto envolvido incorretamente %}

Este texto está envolvido **incorretamente**:

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

### Etapa 3: Adicione locais à sua mensagem

Após adicionar tags de tradução à sua mensagem, selecione **Manage languages** no editor (**Languages** nos editores de arrastar e soltar para e-mail e blocos de conteúdo) e selecione pelo menos um local para o qual deseja adicionar traduções.

![O menu suspenso Adicionar local com opções para selecionar o local padrão ou atributos personalizados.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Blocos de conteúdo contendo traduções

Se sua mensagem contém blocos de conteúdo que já possuem traduções salvas, você não precisa fazer upload dessas traduções novamente. As traduções salvas são aplicadas automaticamente quando o bloco de conteúdo é adicionado à sua mensagem.

No modal **Manage languages**, os blocos de conteúdo com traduções salvas aparecem na lista, junto com os locais que suportam. Isso permite que você veja quais partes da sua mensagem já estão localizadas antes de adicionar novas traduções.

![A seção Manage languages com uma lista de blocos de conteúdo que possuem traduções salvas.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Certifique-se de que cada bloco de conteúdo inclua traduções para todos os locais adicionados à sua mensagem. Se um bloco de conteúdo não tiver traduções para um dos locais que você adicionou, ele será exibido no idioma original para os usuários desse local.
{% endalert %}

### Etapa 4: Adicione traduções

Após selecionar os locais, adicione traduções à sua mensagem usando um dos seguintes métodos:

![A guia Adicionar traduções com opções para fazer upload de traduções por CSV ou conectando-se a parceiros de tradução.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Upload CSV template %}

Selecione **Download template** para baixar um CSV contendo uma matriz dos seus IDs de tradução e locais selecionados. Insira as traduções para cada local. Faça upload do arquivo completo e as traduções serão aplicadas à sua mensagem.

{% alert important %}
Para evitar problemas de exibição com caracteres não ingleses, evite usar o Excel para o seu CSV de tradução.
{% endalert %}

![CSV com tags de tradução para título, texto da oferta, valor da oferta e CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Use the translation API %}

Use uma API de tradução de parceiro para gerenciar e atualizar traduções nas suas campanhas e canvas. Isso é útil se você usa um sistema externo para localização ou deseja se conectar diretamente com um parceiro de tradução.

Para usar os endpoints de tradução com canvas, inclua os seguintes parâmetros:
  - `workflow_id`
  - `step_id`
  - `message_variation_id` 

{% alert note %}
Ao usar a API de tradução com etapas do canva que foram criadas após o lançamento do canva, o `message_variation_id` que você passar para a API estará vazio ou em branco.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Visualize as traduções

Para visualizar sua mensagem, selecione a opção **Multi-Language User** no menu suspenso **Preview as User**. Isso permite que você alterne entre diferentes definições de local para visualizar todas as traduções da sua mensagem.

![Prévias de locais]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Gerenciando traduções

### Duplicando etapas do canva ou campanhas, e traduções

Quando você duplica uma etapa do canva, campanha ou variação, as traduções são incluídas. Isso também vale ao copiar entre espaços de trabalho, desde que os locais estejam definidos nesse espaço de trabalho de destino. Certifique-se de revisar e atualizar as traduções ao fazer modificações no seu canva ou campanha.

### Salvando traduções em blocos de conteúdo

Os blocos de conteúdo suportam multilíngue da mesma forma que as mensagens. Ao criar ou editar blocos de conteúdo, você pode marcar conteúdo para tradução, adicionar locais e fazer upload de traduções usando um CSV ou a [API de tradução]({{site.baseurl}}/api/endpoints/translations/).

As traduções salvas permanecem associadas ao bloco de conteúdo. Quando o bloco é adicionado a uma mensagem, suas traduções são incluídas automaticamente.

### Mensagens da direita para a esquerda

Ao preencher o arquivo de tradução para idiomas escritos da direita para a esquerda (como o árabe), envolva a tradução com `span` para que ela seja formatada corretamente:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Rastreamento de links de e-mail

Em campanhas de e-mail, a Braze rastreia links adicionando informações de rastreamento (parâmetros de consulta) a cada URL. Esse comportamento suporta tanto [link aliasing]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) quanto [modelos de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template).

Quando uma URL está envolvida em tags de tradução, a Braze pode não conseguir determinar onde adicionar essas informações de rastreamento. Para garantir que isso funcione corretamente, você deve incluir um caractere especial no final da URL para indicar onde o rastreamento deve ser adicionado.

As URLs usam dois caracteres especiais para controlar como isso funciona:
  - `?` adiciona rastreamento a uma URL que ainda não o possui.
  - `&` adiciona rastreamento adicional se um `?` já estiver presente na URL. Uma URL pode conter apenas um `?`.

| URL | Contém&nbsp;`?` | Descrição | Exemplo |
| --- | --- | --- | --- |
| URL padrão | Não | Adicione `?` após a tag de tradução de fechamento se a URL ainda não contiver um. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL padrão | Sim | Use `&` no final da URL (após a tag de tradução de fechamento) se ela já contiver `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Gerada por Liquid | Não | Use `?` após as tags de tradução de fechamento se a URL gerada ainda não contiver um. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Gerada por Liquid | Sim | Use `&` após a tag de tradução de fechamento se a URL gerada já contiver um `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Configurações de idioma e acessibilidade

Para canais baseados em HTML (e-mail, mensagem no app, banners, landing pages e Cartões de conteúdo), a Braze adiciona um atributo de idioma de acessibilidade (`lang`) à mensagem renderizada. Esse atributo ajuda tecnologias assistivas, como leitores de tela, a interpretar e pronunciar o texto corretamente.

Sem isso, um leitor de tela assume que o conteúdo está no idioma padrão que o usuário definiu no dispositivo durante a configuração. Se a mensagem estiver em um idioma diferente, o leitor de tela pode não pronunciar tudo corretamente.

#### Configurando o idioma de acessibilidade

Você pode definir o idioma de acessibilidade em dois níveis:

##### Nível da mensagem

Nas configurações da sua mensagem, acesse a seção **Accessibility** e selecione um idioma no menu suspenso ou use Liquid para definir dinamicamente o idioma de acessibilidade. Isso se aplica a todo o conteúdo da mensagem.

##### Nível do local

Para mensagens multilíngues, defina o idioma de acessibilidade em cada local nas **Localization Settings**. Quando novas mensagens são criadas, {% raw %}`{{accessibility_language}}`{% endraw %} é selecionado por padrão na seção **Accessibility**. Isso mapeia o idioma de acessibilidade para as configurações do seu local.

#### Padrões

O idioma de acessibilidade é mapeado para o atributo HTML `lang`, um [requisito WCAG 2.1 Nível A](https://dequeuniversity.com/rules/axe/4.2/html-has-lang) (Critério de Sucesso 3.1.1). Para conteúdo multilíngue, você também pode definir o idioma em blocos de conteúdo individuais usando o atributo `lang` diretamente no seu HTML.

## Perguntas frequentes

#### Quais são os limites para tags de tradução?

Ao usar tags de tradução, os seguintes limites se aplicam:

- Cada mensagem pode ter até 200 tags de tradução.
- Cada texto padrão (o conteúdo entre as tags de tradução) pode ter até 2.000 caracteres.
- As traduções por local podem ter até 409.600 bytes (aproximadamente 409,6&nbsp;KB).

#### Posso fazer uma alteração no texto traduzido em um dos meus locais?

Sim. Primeiro, faça a edição no CSV, depois faça upload do arquivo novamente para aplicar a alteração no texto traduzido.

### A Braze fornece traduções?

Não. Você deve [fornecer suas próprias traduções](#step-4-add-translations) fazendo upload de um CSV ou usando a API de tradução.

### Posso aninhar tags de tradução?

Não.

#### Posso envolver mensagens HTML inteiras em uma tag de tradução?

Não. Como boa prática, você deve envolver apenas texto legível por humanos ou conteúdo que precisa ser localizado. Isso ajuda a evitar formatação quebrada, links ou outros elementos não textuais.

Além disso, considere envolver partes menores e semanticamente relacionadas do texto para criar traduções precisas e evitar limitações de performance ou tamanho.

#### Posso fazer uma alteração no texto traduzido em um dos meus locais?

Sim. Se estiver usando um CSV, primeiro faça a edição no arquivo, depois faça upload novamente para aplicar a alteração no texto traduzido. Se estiver usando a [API de tradução]({{site.baseurl}}/api/endpoints/translations/), use os endpoints de atualização para fazer alterações.

#### Que validações ou verificações extras a Braze faz?

| Cenário | Validação na Braze |
| --- | --- |
| Uma mensagem contém dois ou mais IDs de tradução correspondentes que mapeiam para textos diferentes. | Esse arquivo de tradução não será baixado. |
| Um arquivo de tradução está sem um ou mais IDs de tags de tradução. | Esse arquivo de tradução não será carregado. |
| Um arquivo de tradução contém locais que estão ausentes na mensagem. | Esse arquivo de tradução não será carregado. |
| As tags de tradução devem ser adicionadas a uma mensagem antes de baixar o modelo de tradução. | Esse arquivo de tradução não será baixado. |
| Tags de tradução encontradas no arquivo carregado estão ausentes na sua mensagem. | As traduções extras não serão salvas na mensagem. |
| {% raw %}Uma mensagem contém uma ou mais Liquid tags quebradas. Para abrir tags, use `{% translation your_id_here %}`, feche tags de tradução com `{% endtranslation %}`.{% endraw %} | Esse arquivo de tradução não será baixado. |
| Um arquivo de tradução contém texto padrão que não corresponde ao que está na mensagem. | As traduções são adicionadas, mas o texto original da mensagem não é atualizado. |
| Um ou mais locais em uma mensagem foram excluídos nas configurações e não existem mais. | As traduções que já foram adicionadas continuam a existir na mensagem. Se forem excluídas da mensagem, as traduções são perdidas. |
| Tags de tradução contêm URLs completas ou URLs geradas por Liquid. | Tags de tradução contendo URLs são identificadas caso ocorram problemas com links quebrados ou rastreamento de links. |
| Tags de tradução incluem parâmetros de consulta. | Tags de tradução contendo parâmetros de consulta são identificadas caso ocorram problemas com links quebrados ou rastreamento de links. |
| Tags de tradução contêm atributos ou estruturas HTML. | Tags de tradução contendo atributos ou estruturas HTML são identificadas caso ocorram problemas com estilos e formatação. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }