# Lab 9: Aniversários

<div class="alert" data-alert="warning" role="alert"><p>Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que todos os alunos do grupo contribuam igualmente para o laboratório.</p></div>

Crie uma aplicação web para registrar os aniversários de seus amigos.

![captura de tela do site de aniversários](https://cs50.harvard.edu/x/2023/labs/9/birthdays.png)

## Começando

Comece o CS50x em 2021 ou antes e precisa migrar seu trabalho do IDE CS50 para o novo espaço de códigos do VS Code? Não deixe de conferir nossas instruções sobre como [migrar](../../new/) seus arquivos!

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e execute `cd` por si só. Você deve constatar que seu "prompt" se assemelha ao abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/labs/9/birthdays.zip

seguido de Enter para baixar o arquivo ZIP chamado `birthdays.zip` no seu espaço de códigos. Tome cuidado para não ignorar o espaço entre `wget` e a URL, ou qualquer outro caractere!

Agora execute

    unzip birthdays.zip

para criar uma pasta chamada `birthdays`. Você não precisa mais do arquivo ZIP, portanto execute

    rm birthdays.zip

e responda "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd birthdays

seguido de Enter para mover-se para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se assemelhar ao abaixo.

    birthdays/ $

Se tudo ocorreu bem, você deve executar

    ls

e verá os seguintes arquivos e pastas:

    app.py  birthdays.db  static/  templates/

Se encontrar algum problema, siga novamente esses mesmos passos e veja se pode determinar onde errou!

## Compreensão

No `app.py`, você encontrará o início de uma aplicação web Flask. A aplicação tem uma rota (`/`) que aceita solicitações `POST` (após o `if`) e solicitações `GET` (após o `else`). Atualmente, quando a rota `/` é solicitada via `GET`, o modelo `index.html` é renderizado. Quando a rota `/` é solicitada via `POST`, o usuário é redirecionado de volta para `/` via `GET`.

`birthdays.db` é um banco de dados SQLite com uma tabela, `birthdays`, que tem quatro colunas: `id`, `name`, `month` e `day`. Já existem algumas linhas nesta tabela, embora, em última instância, sua aplicação web irá permitir a inserção de novas linhas nesta tabela!

No diretório `static` há um arquivo `styles.css` contendo o código CSS para esta aplicação web. Não há necessidade de editar este arquivo, embora você possa fazê-lo se quiser!

No diretório `templates`, há um arquivo `index.html` que será renderizado quando o usuário visualizar sua aplicação web.

## Detalhes da Implementação

Complete a implementação de uma aplicação web que permita aos usuários armazenar e acompanhar aniversários.

- Quando a rota `/` é solicitada via `GET`, sua aplicação web deve exibir, em uma tabela, todas as pessoas em seu banco de dados, juntamente com seus aniversários.
  - Primeiro, em `app.py`, adicione lógica no tratamento de solicitações `GET` para consultar o banco de dados `birthdays.db` para todos os aniversários. Passe todos esses dados para o modelo `index.html`.
  - Em seguida, em `index.html`, adicione lógica para renderizar cada aniversário como uma linha na tabela. Cada linha deve ter duas colunas: uma coluna para o nome da pessoa e outra coluna para o aniversário da pessoa.
- Quando a rota `/` é solicitada via `POST`, sua aplicação web deve adicionar um novo aniversário ao seu banco de dados e, em seguida, renderizar novamente a página de índice.
  - Primeiro, em `index.html`, adicione um formulário HTML. O formulário deve permitir que os usuários digitem um nome, um mês de aniversário e um dia de aniversário. Certifique-se de que o formulário envie para `/` (sua "ação") com um método de `post`.
  - Em seguida, em `app.py`, adicione lógica no tratamento de solicitações `POST` para `INSERT` uma nova linha na tabela `birthdays` com base nos dados fornecidos pelo usuário.

Opcionalmente, você também pode:

- Adicionar a capacidade de excluir e/ou editar entradas de aniversário.
- Adicionar quaisquer recursos adicionais de sua escolha!

### Demonstração

Este vídeo foi gravado quando o curso ainda usava o IDE CS50 para escrever o código. Embora a interface possa parecer diferente do seu espaço de códigos, o comportamento dos dois ambientes deve ser em grande parte semelhante!

### Dicas

- Lembre-se de que você pode chamar `db.execute` para executar consultas SQL dentro do `app.py`.
  - Se você chamar `db.execute` para executar uma consulta `SELECT`, lembre-se de que a função retornará uma lista de dicionários, onde cada dicionário representa uma linha retornada por sua consulta.
- Você provavelmente achará útil passar dados adicionais para `render_template()` em sua função `index` para que possa acessar dados de aniversário dentro do modelo `index.html`.
- Lembre-se de que a tag `tr` pode ser usada para criar uma linha de tabela e a tag `td` pode ser usada para criar uma célula de dados de tabela.
- Lembre-se de que, com Jinja, você pode criar um [`loop for`](https://jinja.palletsprojects.com/en/2.11.x/templates/#for) dentro do seu arquivo `index.html`.
- Em `app.py`, você pode obter os dados `POSTados` pela submissão do formulário do usuário via `request.form.get(field)`, onde `field` é uma string que representa o atributo `name` de uma entrada do seu formulário.
  - Por exemplo, se em `index.html`, você tivesse uma entrada `<input name="foo" type="text">`, você poderia usar `request.form.get("foo")` em `app.py` para extrair a entrada do usuário.

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/2CcqQnLbGOE"></iframe></details>

### Testando

Não há `check50` para este laboratório! Mas certifique-se de testar sua aplicação web adicionando alguns aniversários e garantindo que os dados apareçam em sua tabela conforme o esperado.

Execute `flask run` em seu terminal enquanto estiver no diretório `birthdays` para iniciar um servidor web que serve sua aplicação Flask.

## Como Submeter

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/labs/2023/x/birthdays