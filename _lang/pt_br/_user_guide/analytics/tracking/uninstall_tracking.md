---
nav_title: Rastreamento de desinstalação
article_title: Uninstall Tracking
page_order: 6
page_type: reference
description: "Este artigo de referência aborda a implementação do rastreamento de desinstalação para estatísticas em nível de campanha e de aplicativo."
tool: Reports

---

# Rastreamento de desinstalação

> Este artigo mostra como você pode visualizar desinstalações agregadas de aplicativos ao longo do tempo para localizar tendências e anomalias e rastrear desinstalações no nível da campanha para determinar se uma campanha específica está impulsionando ou impedindo instalações de aplicativos.

O rastreamento de desinstalação na Braze fornece os seguintes detalhes:

1. Estatísticas diárias de desinstalação no nível do app em um gráfico de série temporal na página **inicial**.
2. Estatísticas de desinstalação em nível de campanha em um gráfico de série temporal na página **Detalhes da campanha** de uma campanha específica. Essa estatística especifica o número de destinatários da campanha que desinstalam a cada dia.

{% alert note %} 
Você deve optar pelo rastreamento de desinstalação no seu dashboard da Braze. Este recurso está disponível para apps no iOS, Android e Fire OS. 
{% endalert %}

## Como funciona

A Braze coleta automaticamente um nível básico de informações de desinstalação de suas campanhas push regulares. No entanto, como a frequência com que diferentes usuários recebem campanhas push pode variar, oferecemos rastreamento de desinstalação para fornecer um instantâneo mais preciso da atividade de desinstalação entre seus usuários.

Quando a Braze detecta uma desinstalação, o usuário é marcado como tendo desinstalado. Se você usar o filtro **Não Desinstalou** em uma campanha, esses usuários marcados serão excluídos. Se um usuário reinstalar o app mas não abri-lo, a tag de desinstalação permanece no perfil. A tag é removida somente quando o usuário inicia uma nova sessão no app reinstalado. Isso significa que um usuário que reinstala mas nunca abre o app continua aparecendo como desinstalado.

Para mais informações sobre como usar o rastreamento de desinstalação, veja nosso post no blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Ativação do rastreamento de desinstalação

Você pode ativar o rastreamento de desinstalação na página **Configurações do aplicativo**, em **Configurações**, para cada app que deseja rastrear.

Quando você ativa o rastreamento de desinstalação para um app, a Braze envia uma mensagem push em segundo plano à noite para usuários que não registraram uma sessão ou não receberam um push nas últimas 24 horas.

### Configuração

Para configurar o rastreamento de desinstalação para seu aplicativo iOS, use um [método utilitário]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Para seu aplicativo Android, use [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Quando a Braze detectar uma desinstalação, seja por rastreamento de desinstalação ou por entrega normal de campanha push, registraremos o melhor horário estimado da desinstalação para o usuário. Esse horário é armazenado no perfil do usuário como um atributo padrão e pode ser usado para definir um segmento de usuários para campanhas de recuperação.

## Filtragem de segmentos por desinstalações

O filtro **Desinstalado** seleciona usuários que desinstalaram seu app dentro de um intervalo de tempo. Como é difícil determinar a hora exata de uma desinstalação, recomendamos que os filtros de desinstalação tenham intervalos de tempo mais amplos para garantir que todos os que desinstalam sejam incluídos no segmento em algum momento.

As estatísticas diárias sobre desinstalações estão na página **inicial**. 

![Segmento de desinstalação.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

O gráfico pode ser dividido por app e segmento, semelhante a outras estatísticas que a Braze fornece. Na seção **Visão geral da performance**, selecione o intervalo de datas e, se desejar, um app. Em seguida, role a tela para baixo até o gráfico **Performance Over Time** e faça o seguinte:

1. No menu suspenso **Statistics For**, selecione **Uninstalls**.
2. No menu suspenso **Breakdown**, selecione **By segment**.
3. No menu suspenso **Breakdown Values**, selecione os segmentos a serem incluídos no gráfico.

{% alert note %}
Os apps sem rastreamento de desinstalação ativado reportarão desinstalações de apenas um subconjunto de seus usuários (aqueles que foram direcionados com notificações por push), portanto, os totais diários de desinstalação podem ser maiores do que o mostrado.
{% endalert %}

## Rastreamento de desinstalação para campanhas

O rastreamento de desinstalação de campanhas mostra o número de usuários que receberam uma campanha específica e, posteriormente, desinstalaram seu app dentro do período de tempo selecionado. Essa ferramenta fornece insight sobre como as campanhas podem estar incentivando comportamentos negativos não intencionais dos usuários e ajuda a medir a eficácia geral da campanha.

As estatísticas de desinstalação de campanhas estão localizadas na página de **análise de dados da campanha** de uma campanha específica. Para campanhas multicanais e multivariantes, as desinstalações podem ser divididas por canal e variante, respectivamente.

![Desinstalação no nível da campanha.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Como funciona

A Braze rastreia as desinstalações observando quando as mensagens push enviadas aos dispositivos dos usuários retornam um sinal do Firebase Cloud Messaging (FCM) ou do serviço de Notificações por Push da Apple (APNs) de que o app não está mais instalado. Se você ativar o Rastreamento Global de Desinstalação para um app, a Braze envia uma mensagem push silenciosa diária para os usuários para detectar se eles desinstalaram. A Braze envia este push "silencioso" para todos os usuários (a menos que o usuário tenha desativado os pushes silenciosos nas configurações do app); o push não aparece para os usuários. Se a Braze detectar que um usuário desinstalou, nós:

* Aumentamos a contagem total de desinstalações do app em um.
* Aumentamos em um a contagem de desinstalações para cada campanha que o usuário recebeu com êxito nas últimas 24 horas.
* Se um usuário receber três campanhas em um período de 24 horas e depois desinstalar, incrementamos a contagem de "desinstalações" para todas as três campanhas.

FCM e APNs impõem restrições ao rastreamento de desinstalação. A Braze incrementa apenas a contagem de desinstalação quando FCM ou APNs nos informam que um usuário desinstalou, mas esses sistemas de terceiros podem nos notificar sobre desinstalações a qualquer momento. Use o rastreamento de desinstalação para detectar tendências direcionais em vez de estatísticas precisas.

## Solução de problemas

### Por que de repente estou vendo um pico de desinstalações?

Se você observar um pico nas desinstalações de aplicativos, isso pode ser devido ao Firebase Cloud Messaging (FCM) e ao serviço de Notificações por Push da Apple (APNs) revogando tokens antigos em uma frequência diferente.

{% alert note %} 
Por razões de privacidade, os provedores de push da Braze podem revogar tokens em intervalos irregulares, o que significa que as contagens de desinstalação podem às vezes aumentar em um determinado período de tempo.<br><br>Para validar essas mudanças, monitore o rastreamento de desinstalação juntamente com uma métrica de ação do usuário, como a taxa de abertura de push direto. Se as desinstalações aumentarem drasticamente, mas as aberturas de push direto permanecerem estáveis, o pico provavelmente reflete um parceiro revogando tokens antigos em vez de um comportamento real do usuário.
{% endalert %}

### Por que o número de desinstalações de apps é diferente do que está no APNs?

A diferença é esperada. 

A Apple usa um cronograma aleatório para atrasar a notificação quando um token push se torna inválido, o que significa que mesmo após um usuário desinstalar um app, o APNs pode continuar a retornar respostas bem-sucedidas para notificações por push por um período de tempo. Esse atraso é intencional e projetado para proteger a privacidade do usuário. Nenhum bounce ou falha será relatado até que o APNs retorne um status `410` para um token inválido.