# C$50 Finance

<div class="alert" data-alert="warning" role="alert"><p>O código de distribuição desse conjunto de problemas foi recentemente alterado. Se você baixou o código de distribuição antes de <a data-local="2022-12-01T00:00:00+00:00" href="https://time.cs50.io/20221201T000000Z">2022-12-01T00:00:00+00:00</a>, execute os seguintes comandos no terminal no diretório <code class="language-plaintext highlighter-rouge">finance</code> para baixar a última versão do código de distribuição.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ rm helpers.py
$ wget https://cdn.cs50.net/2022/fall/psets/9/finance/helpers.py

</code></pre></div></div></div>

Implemente um site através do qual os usuários possam "comprar" e "vender" ações, como abaixo.

![C$50 Finance](https://cs50.harvard.edu/x/2023/psets/9/finance/finance.png)

## Contexto

Se você não tem certeza do que significa comprar e vender ações (ou seja, ações de uma empresa), vá [aqui](https://www.investopedia.com/articles/basics/06/invest1000.asp) para um tutorial.

Você está prestes a implementar o C$50 Finance, um aplicativo web através do qual você pode gerenciar portfólios de ações. Essa ferramenta não só permitirá que você verifique os preços reais das ações e os valores de portfólio, mas também permitirá que você compre (ok, "compre") e venda (ok, "venda") ações pesquisando [IEX](https://iextrading.com/developer/) para os preços das ações.

De fato, a IEX permite que você baixe cotações de ações por meio de sua API (interface de programação de aplicativos) usando URLs como `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Observe como o símbolo da Netflix (NFLX) está incorporado a este URL; é assim que a IEX sabe de quem dados retornar. Esse link não retornará nenhum dado porque a IEX exige que você use uma chave API (mais sobre isso daqui a pouco), mas se retornasse, você veria uma resposta no formato JSON (JavaScript Object Notation) como este:

    {
      "avgTotalVolume": 15918066,
      "calculationPrice": "close",
      "change": -8.27,
      "changePercent": -0.03074,
      "close": 260.79,
      "closeSource": "official",
      "closeTime": 1667592000924,
      "companyName": "Netflix Inc.",
      "currency": "USD",
      "delayedPrice": 260.81,
      "delayedPriceTime": 1667591988947,
      "extendedChange": 0.21,
      "extendedChangePercent": 0.00081,
      "extendedPrice": 261,
      "extendedPriceTime": 1667606392772,
      "high": 274.97,
      "highSource": "15 minute delayed price",
      "highTime": 1667592000831,
      "iexAskPrice": None,
      "iexAskSize": None,
      "iexBidPrice": None,
      "iexBidSize": None,
      "iexClose": 260.85,
      "iexCloseTime": 1667591999754,
      "iexLastUpdated": None,
      "iexMarketPercent": None,
      "iexOpen": 271.67,
      "iexOpenTime": 1667568602197,
      "iexRealtimePrice": None,
      "iexRealtimeSize": None,
      "iexVolume": None,
      "lastTradeTime": 1667591999820,
      "latestPrice": 260.79,
      "latestSource": "Close",
      "latestTime": "Nov 4, 2022",
      "latestUpdate": 1667592000924,
      "latestVolume": 11124694,
      "low": 255.32,
      "lowSource": "15 minute delayed price",
      "lowTime": 1667584872696,
      "marketCap": 115215720136,
      "oddLotDelayedPrice": 260.81,
      "oddLotDelayedPriceTime": 1667591988947,
      "open": 271.9,
      "openTime": 1667568601785,
      "openSource": "official",
      "peRatio": 23.39,
      "previousClose": 269.06,
      "previousVolume": 7057350,
      "primaryExchange": "NASDAQ",
      "symbol": "NFLX",
      "volume": 11124694,
      "week52High": 700.99,
      "week52Low": 162.71,
      "ytdChange": -0.5978504176349512,
      "isUSMarketOpen": false
    }

Observe como, entre as chaves, há uma lista separada por vírgulas de pares chave-valor, com dois pontos separando cada chave de seu valor.

Vamos agora direcionar nossa atenção para obter o código de distribuição deste problema!

## Começando

Faça login em [code.cs50.io](https://code.cs50.io/), clique na sua janela de terminal e execute `cd` por si só. Você deverá ver que o prompt da sua janela de terminal se parece com o abaixo:

     $

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/9/finance.zip

para baixar um ZIP chamado `finance.zip` para o seu espaço de códigos.

Depois execute

     unzip finance.zip

para criar uma pasta chamada `finance`. Você não precisa mais do arquivo ZIP, por isso você pode executar

     rm finance.zip

e responda com "y" seguido de Enter para remover o arquivo ZIP que você baixou.

Agora digite

    cd finance

seguido de Enter para se mover para dentro (ou seja, abrir) desse diretório. Seu prompt deverá se parecer com o abaixo.

    finance/ $

Execute `ls` por si só e você deverá ver alguns arquivos e pastas:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se você pode determinar onde errou!

### Configurando

Antes de começar nesta tarefa, você precisará se registrar em uma chave de API para poder consultar os dados da IEX. Para fazer isso, siga estas etapas:

- Visite [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
- Selecione o tipo de conta “Individual”, insira seu nome, endereço de e-mail e uma senha e clique em "Criar conta".
- Depois de registrada, role para baixo até “Comece de graça” e clique em “Selecionar plano inicial” para escolher o plano gratuito. _Observe que este plano só funciona por 30 dias a partir do dia em que você cria sua conta._ Mantenha isso em mente se você pretende usar esta mesma API para o seu projeto final!
- Depois de confirmar sua conta por meio de um email de confirmação, visite [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
- Copie a chave que aparece na coluna _Token_ (deve começar com `pk_`).
- Na sua janela de terminal, execute:

<pre>
$ export API_KEY=value
</pre>

onde `value` é o valor colado, sem nenhum espaço imediatamente antes ou depois do `=`. Você também pode querer colar esse valor em um documento de texto em algum lugar, caso precise dele novamente mais tarde.

### Execução

Inicie o servidor web incorporado do Flask (dentro do diretório `finance/`):

    $ flask run

Visite a URL retornada pelo `flask` para ver o código de distribuição em ação. No entanto, ainda não é possível fazer login ou se registrar!

Dentro do diretório `finance/`, execute `sqlite3 finance.db` para abrir o arquivo `finance.db` com o `sqlite3`. Se você executar o comando `.schema` no prompt do SQLite, notará que `finance.db` vem com uma tabela chamada `users`. Dê uma olhada na estrutura (ou seja, esquema) dela. Note que, por padrão, novos usuários receberão $ 10.000 em dinheiro. Mas se você executar `SELECT * FROM users;`, ainda não haverá (ou seja, linhas) nenhum usuário para navegar.

Outra maneira de visualizar `finance.db` é com um programa chamado phpLiteAdmin. Clique em `finance.db` no navegador de arquivos do seu espaço de codificação e, em seguida, clique no link mostrado abaixo do texto “Please visit the following link to authorize GitHub Preview”. Você deve ver informações sobre o banco de dados em si, bem como uma tabela, `users`, assim como você viu no prompt `sqlite3` com `.schema`.

### Compreensão

#### `app.py`

Abra o arquivo `app.py`. No topo do arquivo, há um monte de importações, entre elas o módulo SQL da CS50 e algumas funções auxiliares. Mais sobre isso em breve.

Após configurar o [Flask](https://flask.pocoo.org/), note como este arquivo desativa o cache de respostas (desde que esteja no modo de depuração, que é o caso por padrão no seu espaço de codificação do code50), para evitar o caso de fazer uma alteração em algum arquivo, mas o navegador não perceber. Observe a seguir como ele configura o [Jinja](https://jinja.pocoo.org/) com um “filtro” personalizado, `usd`, uma função (definida em `helpers.py`) que facilitará a formatação dos valores como dólares americanos (USD). Em seguida, ele configura ainda mais o Flask para armazenar [sessões](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) no sistema de arquivos local (ou seja, disco) em vez de armazená-los dentro de cookies (assinados digitalmente), que é o padrão do Flask. O arquivo, em seguida, configura o módulo SQL da CS50 para usar `finance.db`.

Depois disso, há um monte de rotas, apenas duas das quais estão totalmente implementadas: `login` e `logout`. Leia a implementação do `login` primeiro. Observe como ele usa o `db.execute` (da biblioteca CS50) para consultar o `finance.db`. E observe como ele usa o `check_password_hash` para comparar os hashes das senhas dos usuários. Observe também como o `login` “lembra” que um usuário está logado, armazenando seu `user_id`, um INTEIRO, na `session`. Dessa forma, qualquer rota deste arquivo pode verificar qual usuário, se houver algum, está logado. Por fim, observe como, uma vez que o usuário tenha feito login com sucesso, o `login` redirecionará para `"/"`, levando o usuário à sua página inicial. Enquanto isso, observe como o `logout` simplesmente limpa a `session`, efetivamente fazendo logout do usuário.

Observe como a maioria das rotas é “decorada” com `@ login_required` (uma função definida em `helpers.py` também). Esse decorador garante que, se um usuário tentar visitar qualquer uma dessas rotas, ele ou ela será redirecionado primeiro para `login` para fazer login.

Observe também como a maioria das rotas suporta GET e POST. Mesmo assim, a maioria deles (por enquanto!) simplesmente retorna um "pedido de desculpas", uma vez que eles ainda não foram implementados.

#### `helpers.py`

Em seguida, dê uma olhada no arquivo `helpers.py`. Ah, lá está a implementação do `apology`. Note como ele, em última instância, renderiza um modelo, o `apology.html`. Ele também define, dentro de si mesmo, outra função, `escape`, que é simplesmente usada para substituir caracteres especiais em desculpas. Definindo `escape` dentro de `apology`, limitamos o seu escopo apenas a este último; nenhuma outra função poderá chamar (ou precisará chamar) essa função.

Em seguida, no arquivo, há o `login_required`. Sem problemas se este for um pouco criptico para você, mas se você já se perguntou como uma função pode retornar outra função, aqui está um exemplo!

Em seguida, temos o `lookup`, uma função que, dada um símbolo (por exemplo, NFLX), retorna uma cotação de ações para uma determinada empresa na forma de um dicionário com três chaves: `name`, cujo valor é uma `str`, o nome da empresa; `price`, cujo valor é um `float` e `symbol`, cujo valor é uma `str`, uma versão canônica (em maiúsculas) do símbolo da ação, independentemente de como esse símbolo foi capitalizado quando passado para `lookup`.

Finalmente, no final do arquivo, temos a função `usd`, uma pequena função que simplesmente formata um número do tipo `float` como USD (por exemplo, `1234.56` é formatado como `$ 1,234.56`).

#### `requirements.txt`

Em seguida, dê uma rápida olhada em `requirements.txt`. Esse arquivo simplesmente fornece as dependências de pacotes necessárias para a aplicação.

#### `static/`

Olhe também para a pasta `static/`, onde se encontra o arquivo `styles.css`. Ali está onde fica o CSS inicial. Você pode alterá-lo como achar melhor.

#### `templates/`

Agora, dê uma olhada na pasta de templates `templates/`. No arquivo `login.html`, essencialmente, há apenas um formulário HTML, estilizado com [Bootstrap](https://getbootstrap.com/). Já em `apology.html`, há um modelo para um pedido de desculpas. Lembre-se de que o `apology` em `helpers.py` tem dois argumentos: `message`, que foi passado para `render_template` como o valor de `bottom`, e, opcionalmente, `code`, que foi passado para `render_template` como o valor de `top`. Veja como esses valores são usados ​​no arquivo `apology.html`! E [aqui está o porquê](https://github.com/jacebrowning/memegen) 0:-)

Por fim, temos o arquivo `layout.html`. Ele é um pouco maior do que o usual, mas isso ocorre principalmente porque ele vem com uma barra de navegação móvel-chique, baseada no Bootstrap. Observe como ele define um bloco chamado `main`, dentro de qual os modelos (incluindo `apology.html` e` login.html`) devem ser incluídos. Ele também inclui suporte para o recurso de mensagens intermitentes do Flask [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing), para que você possa passar mensagens de uma rota para outra para o usuário ver.

## Especificação

### `register`

Complete a implementação do `register` de tal forma que permita que um usuário faça o registro de uma conta através de um formulário.

- Exija que o usuário insira um nome de usuário, implementado como um campo de texto cujo o `name` é `username`. Renderize um pedido de desculpas se o usuário deixar o campo em branco ou se o nome de usuário já existir.
- Exija que o usuário insira uma senha, implementado como um campo de texto cujo o `name` é `password`, e depois que repita a mesma senha, implementado como um campo de texto cujo o `name` é `confirmation`. Renderize um pedido de desculpas se qualquer um dos campos estiver em branco ou se as senhas não correspondem.
- Submeta o input do usuário via `POST` para `/register`.
- Insira o novo usuário em `users`, armazenando o hash da senha do usuário, e não a senha em si. Hasheie a senha do usuário com [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.security.generate_password_hash). É bem provável que você irá precisar criar um template novo (e.g., `register.html`) que seja bem similar ao `login.html`.

Após implementar o `register` corretamente, você deverá ser capaz de registrar uma conta e fazer login (já que `login` e `logout` já funcionam)! E você deverá ser capaz de ver as suas linhas via phpLiteAdmin ou `sqlite3`.

### `quote`

Complete a implementação de `quote` de tal forma que permita que um usuário pesquise o preço atual de uma ação.

- Exija que o usuário insira o símbolo da ação, implementado como um campo de texto cujo o `name` é `symbol`.
- Submeta o input do usuário via `POST` para `/quote`.
- É bem provável que você irá precisar criar dois templates novos (e.g., `quote.html` e `quoted.html`). Quando o usuário visitar `/quote` via GET, renderize um desses templates, dentro dele deverá existir um formulário HTML que será submetido à `/quote` via POST. Em resposta ao POST, `quote` pode renderizar o segundo template, incorporando um ou mais valores de `lookup`.

### `buy`

Complete a implementação do `buy` de tal forma que permita que um usuário compre ações.

- Exija que o usuário insira o símbolo da ação, implementado como um campo de texto cujo o `name` é `symbol`. Renderize um pedido de desculpas se o campo estiver em branco ou se o símbolo não existir (de acordo com o valor de retorno de `lookup`).
- Exija que o usuário insira um número de ações, implementado como um campo de texto cujo o `name` é `shares`. Renderize um pedido de desculpas se o input não for um inteiro positivo.
- Submeta o input do usuário via `POST` para `/buy`.
- Após conclusão, redirecione o usuário para a página principal.
- É bem provável que você irá precisar chamara o `lookup` para buscar o preço atual de uma ação.
- É bem provável que você irá precisar fazer uma `SELECT` para descobrir quanto de dinheiro o usuário tem em `users`.
- Adicione uma ou mais tabelas novas ao `finance.db` por onde possa rastrear a compra. Armazene informação suficiente para saber quem comprou, o quê comprou, por qual preço e quando.
  - Utilize tipos SQLite apropriados.
  - Defina índices `UNIQUE` em campos que precisarem ser únicos.
  - Defina índices (não-`UNIQUE`) em campos pelos quais você irá realizar pesquisas (por exemplo, via `SELECT` com `WHERE`).
- Renderize um pedido de desculpas, sem completar a compra, caso o usuário não consiga pagar pelo número de ações no preço atual.
- Você não precisa se preocupar com condições de corrida (ou utilizar transações).

Após implementar o `buy` corretamente, você deverá ser capaz de ver as compras dos usuários em sua(s) nova(s) tabela(s) via phpLiteAdmin ou `sqlite3`.

### `índice`

Complete a implementação do `índice` de forma a exibir uma tabela HTML que resume as ações que o usuário atualmente logado possui. A tabela deve apresentar o número total de ações possuídas pelo usuário, o preço atual de cada ação, o valor total de cada ação (ou seja, quantidade de ações vezes o preço) e o saldo atual em dinheiro do usuário. Apresente também o valor total do portfólio do usuário (valor total das ações mais saldo em dinheiro).

- É provável que seja necessário executar múltiplas consultas SELECT. Dependendo de como as tabelas são implementadas, pode ser interessante o uso de [GROUP BY](https://www.google.com/search?q=SQLite+GROUP+BY), [HAVING](https://www.google.com/search?q=SQLite+HAVING), [SUM](https://www.google.com/search?q=SQLite+SUM) e/ou [WHERE](https://www.google.com/search?q=SQLite+WHERE).
- É provável que seja necessário chamar a função `lookup` para cada ação.

### `venda`

Complete a implementação da `venda` de forma a permitir que o usuário venda as ações que possui.

- É preciso exigir que o usuário insira o símbolo da ação que deseja vender, que deve ser apresentado como um selecionador (`select`) com `name` igual a "symbol". Apresente uma mensagem de erro caso o usuário não selecione uma ação ou não possua ações dessa ação.
- Também é preciso exigir que o usuário informe a quantidade de ações que deseja vender, que deve ser apresentada como um campo de texto (`text`) com `name` igual a "shares". Apresente uma mensagem de erro caso o valor inserido não seja um número inteiro positivo ou caso o usuário não possua a quantidade selecionada de ações daquela ação.
- Os dados do usuário devem ser enviados via `POST` para `/sell`.
- Após a conclusão da transação, o usuário deve ser redirecionado para a página principal.
- Não é necessário se preocupar com condições especiais devido a múltiplos acessos simultâneos (ou usar transações).

### `histórico`

Complete a implementação da `histórico` de forma a exibir uma tabela HTML que resume todas as transações de um usuário. A tabela deve listar, linha por linha, todas as compras e vendas realizadas pelo usuário.

- Para cada linha, deve ficar claro se a ação foi comprada ou vendida, deve ser incluído o símbolo da ação, o preço de compra/venda, a quantidade de ações compradas/vendidas e a data/hora em que a transação foi efetuada.
- Pode ser necessário alterar a tabela criada para a implementação da `compra` ou complementá-la com uma tabela adicional. Tente minimizar redundâncias.

### Personalização

Implemente, no mínimo, uma personalização à sua escolha:

- Permita que os usuários alterem suas senhas.
- Permita que os usuários adicionem mais dinheiro em sua conta.
- Permita que os usuários comprem mais ações ou vendam ações que já possuem diretamente pelo `índice`, sem precisar escrever o símbolo da ação manualmente.
- Exija que as senhas dos usuários contenham um número mínimo de letras, números e/ou símbolos.
- Implemente outra funcionalidade de escopo comparável.

## Passo a Passo


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


## Testes

Certifique-se de testar manualmente o seu aplicativo da web, por exemplo:

- registrando um novo usuário e verificando se sua página de portfólio carrega com as informações corretas,
- solicitando uma cotação usando um símbolo de ações válido,
- comprando uma ação várias vezes, verificando se o portfólio exibe totais corretos,
- vendendo tudo ou parte de uma ação, verificando novamente o portfólio, e
- verificando se a página de histórico mostra todas as transações para o usuário que está logado.

Também teste alguns usos inesperados, por exemplo:

- inserindo cadeias alfabéticas em formulários quando apenas números são esperados,
- inserindo números zero ou negativos em formulários quando apenas números positivos são esperados,
- inserindo valores de ponto flutuante em formulários quando apenas inteiros são esperados,
- tentando gastar mais dinheiro do que um usuário tem,
- tentando vender mais ações do que um usuário tem,
- inserindo um símbolo de ação inválido e
- incluindo caracteres potencialmente perigosos como `'` e `;` em consultas SQL.

Uma vez satisfeito, para testar seu código com `check50`, execute o seguinte.

    check50 cs50/problems/2023/x/finance

<div class="alert" data-alert="warning" role="alert"><p>Esteja ciente de que <code class="language-plaintext highlighter-rouge">check50</code> testará todo o seu programa como um todo. Se você executá-lo <strong>antes</strong> de concluir todas as funções necessárias, ele poderá relatar erros em funções que estão corretas, mas dependem de outras funções.</p></div>


Execute o seguinte para avaliar o estilo de seus arquivos Python usando `style50`.

    style50 *.py

## Solução da Equipe

Você pode estilizar seu próprio aplicativo de forma diferente, mas aqui está como é a solução da equipe!

[https://finance.cs50.net/](https://finance.cs50.net/)

Sinta-se à vontade para criar uma conta e mexer no aplicativo. Não use uma senha que você use em outros sites.

É **razoável** olhar o HTML e CSS da equipe.

## Sugestões

- Para formatar um valor como valor de dólar americano (com centavos listados com duas casas decimais), você pode usar o filtro 'usd' em seus modelos Jinja (imprimindo valores como `{{ valor | usd }}` em vez de `{{ valor }}`) .
- Dentro de `cs50.SQL` existe um método `execute`, cujo primeiro argumento deve ser uma `str` de SQL. Se essa `str` contiver parâmetros de ponto de interrogação aos quais os valores devem ser vinculados, esses valores podem ser fornecidos como parâmetros nomeados adicionais para `execute`. Veja a implementação de `login` para um exemplo desses. O valor de retorno de `execute` é o seguinte:

   - Se a `str` for um `SELECT`, então `execute` retorna uma lista de zero ou mais objetos `dict`, dentro dos quais existem chaves e valores representando os campos e células de uma tabela, respectivamente.
   - Se a `str` for um `INSERT`, e a tabela na qual os dados foram inseridos contiver uma `PRIMARY KEY` autoincrementável, então `execute` retorna o valor da chave primária da linha recém-inserida.
   - Se a `str` for um `DELETE` ou um `UPDATE`, então `execute` retorna o número de linhas excluídas ou atualizadas por `str`.

- Lembre-se de que `cs50.SQL` registrará em sua janela de terminal quaisquer consultas que você executar por meio de `execute` (para que você possa confirmar se elas estão como pretendido).
- Certifique-se de usar parâmetros vinculados a ponto de interrogação (ou seja, um [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) de `named`) ao chamar o método `execute` do CS50, como` WHERE?`. Não use f-string, [`format`](https://docs.python.org/3.6/library/functions.html#format) ou `+` (ou seja, concatenação), para não correr o risco de sofrer um ataque de injeção SQL.
- Se (e somente se) já se sentir confortável com o SQL, você pode utilizar o [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) ou o [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (ou seja, [SQLAlchemy ORM] (https://docs.sqlalchemy.org/en/latest/index.html)) em vez do `cs50.SQL`.
- Você pode adicionar arquivos estáticos adicionais a `static /`.
- É provável que você deseje consultar a documentação do [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) ao implementar seus modelos.
- É **razoável** pedir a outras pessoas para experimentar (e tentar provocar erros em) seu site.
- Você é bem-vindo para alterar a estética do site, como através de
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/) e / ou
  - [memegen.link](https://memegen.link/).
- Você pode achar a documentação do [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) e do [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) úteis!

## Perguntas frequentes

### ImportError: No module named ‘application’

Por padrão, o `flask` procura um arquivo chamado `app.py` em seu diretório de trabalho atual (porque configuramos o valor de` FLASK_APP`, uma variável de ambiente, para ser `app.py`). Se você vir esse erro, provavelmente executou o `flask` no diretório errado!

### OSError: \ [Errno 98 \] Endereço já em uso

Se, ao executar o `flask`, você vir este erro, é provável que você (ainda) tenha o `flask` em execução em outra guia. Certifique-se de interromper esse outro processo, como com ctrl-c, antes de iniciar o `flask` novamente. Se você não tiver nenhuma outra guia, execute `fuser -k 8080/tcp` para encerrar os processos que ainda estão ouvindo na porta TCP 8080.

## Como enviar

Em seu terminal, execute o que segue para enviar seu trabalho.

    submit50 cs50/problems/2023/x/finance
"

