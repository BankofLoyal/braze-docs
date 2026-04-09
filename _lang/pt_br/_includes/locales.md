{% if include.section == "multi-language prerequisites" %}

| Recurso | Permissões de usuário obrigatórias |
| --- | --- |
| Localidades multilíngues | Você precisa dessas permissões para criar e gerenciar localidades multilíngues:<br><br> {::nomarkdown}Permissões granulares: <ul><li>Editar Configurações de Localização</li><li>Excluir Configurações de Localização</li></ul> Permissões legadas: <ul><li> Gerenciar Configurações Multilíngues</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if include.section == "Preview" %}

## Faça uma prévia das suas localidades

No dropdown **Prévia da mensagem como usuário** dentro da guia **Teste**, selecione **Usuário personalizado** e insira diferentes idiomas para visualizar a mensagem e verificar se ela é traduzida conforme esperado.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Perguntas frequentes

#### Posso fazer uma alteração no texto traduzido em uma das minhas localidades?
Sim. Primeiro, faça a edição no CSV e depois faça upload do arquivo novamente para alterar o texto traduzido.

#### Posso aninhar tags de tradução?
Não.

#### Posso adicionar estilo HTML nas tags de tradução?
Sim, mas certifique-se de verificar se a formatação HTML não é traduzida junto com o conteúdo.

#### Que validações ou verificações extras a Braze faz?

| Cenário                                                                                                                                                 | Validação na Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Um arquivo de tradução não tem localidades associadas à mensagem atual.                                                                               | Esse arquivo de tradução não será enviado.                                                                       |
| Um arquivo de tradução está sem alguns blocos de texto, como um texto dentro de tags de tradução Liquid, da mensagem de e-mail atual.                                | Esse arquivo de tradução não será enviado.                                                                       |
| O arquivo de tradução inclui o texto padrão que não corresponde aos blocos de texto da mensagem de e-mail atual.                                          | Esse arquivo de tradução não será enviado. Corrija isso no seu CSV antes de tentar fazer upload novamente.               |
| O arquivo de tradução inclui localidades que não existem nas configurações de **Suporte Multilíngue**.                                                           | Essas localidades não serão salvas na Braze.                                                                      |
| O arquivo de tradução inclui blocos de texto que não existem na mensagem atual (como o rascunho atual no momento em que é feito o upload das traduções). | Os blocos de texto que não existirem na sua mensagem atual não serão salvos do arquivo de tradução na Braze. |
| Remoção de uma localidade da mensagem depois que essa localidade já tiver sido enviada para a mensagem como parte do arquivo de tradução.                           | A remoção da localidade removerá todas as traduções associadas à localidade na sua mensagem.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}