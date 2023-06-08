Filmes
======

Escreva consultas SQL para responder perguntas sobre um banco de dados de filmes.

Começando
---------------

Faça login no [code.cs50.io] (https://code.cs50.io/) , clique na sua janela de terminal e execute `cd` sozinho. Você deverá encontrar que o prompt da sua janela de terminal se assemelha ao abaixo:

    $
    

A seguir, execute

    wget https://cdn.cs50.net/2022/fall/psets/7/movies.zip
    

para baixar um arquivo ZIP chamado `movies.zip` no seu espaço de códigos.

Em seguida, execute

    unzip movies.zip
    

para criar uma pasta chamada `movies`. Você não precisa mais do arquivo ZIP, portanto, você pode executar

    rm movies.zip
    

e responda com "y" seguida de Enter para remover o arquivo ZIP que você baixou.

Agora digite

    cd movies
    

seguido de Enter para você se mover para (ou seja, abrir) esse diretório. Agora o seu prompt deve se parecer com o abaixo.

    movies/ $
    

Execute `ls` sozinho e você deve ver 13 arquivos .sql, bem como `movies.db`.

Se você tiver algum problema, siga as mesmas etapas novamente e veja se consegue determinar onde errou!

Entendimento
-------------

É fornecido a você um arquivo chamado `movies.db`, um banco de dados SQLite que armazena dados da [IMDb] (https://www.imdb.com/) sobre filmes, as pessoas que os dirigiram e estrelaram e suas avaliações. Em uma janela do terminal, execute `sqlite3 movies.db` para começar a executar consultas no banco de dados.

Primeiramente, quando `sqlite3` solicitar que você forneça uma consulta, digite `.schema` e pressione enter. Isso exibirá as declarações `CREATE TABLE` que foram usadas para gerar cada uma das tabelas no banco de dados. Examinando essas declarações, você pode identificar as colunas presentes em cada tabela.

Observe que a tabela de `movies` tem uma coluna de `id` que identifica exclusivamente cada filme, bem como colunas para o `título` de um filme e o `ano` em que o filme foi lançado. A tabela de `people` também tem uma coluna de `id` e também tem colunas para o `nome` de cada pessoa e o ano de `nascimento`.

As avaliações de filmes, por sua vez, são armazenadas na tabela de `ratings`. A primeira coluna na tabela é `movie_id`: uma chave estrangeira que referencia o `id` da tabela de `movies`. O restante da linha contém dados sobre a `avaliação` de cada filme e o número de `votos` que o filme recebeu no IMDb.

Por fim, as tabelas `stars` e `directors` correspondem às pessoas aos filmes em que atuaram ou dirigiram. (Apenas estrelas e diretores [principais](https://www.imdb.com/interfaces/) são incluídos). Cada tabela tem apenas duas colunas: `movie_id` e `person_id`, que referenciam um filme e uma pessoa específicos, respectivamente.

O desafio à sua frente é escrever consultas SQL para responder a uma variedade de perguntas diferentes, selecionando dados de uma ou mais dessas tabelas.

Especificação
-------------

Para cada um dos problemas seguintes, você deve escrever uma única consulta SQL que produza os resultados especificados por cada problema. Sua resposta deve ser uma única consulta SQL, embora você possa aninhar outras consultas dentro de sua consulta. Você **não deve** assumir nada sobre os `id`s de nenhum filme ou pessoa em particular: suas consultas devem ser precisas mesmo que o `id` de qualquer filme ou pessoa em particular seja diferente. Finalmente, cada consulta deve retornar apenas os dados necessários para responder à pergunta: se o problema apenas solicitar a exibição dos nomes dos filmes, por exemplo, sua consulta não deve exibir também o ano de lançamento de cada filme.

Você pode verificar os resultados de suas consultas no próprio [IMDb](https://www.imdb.com/), mas perceba que as classificações no site podem diferir daquelas em `movies.db`, já que mais votos podem ter sido lançados desde que baixamos os dados!

1.  No arquivo `1.sql`, escreva uma consulta SQL para listar os títulos de todos os filmes lançados em 2008.
    *   Sua consulta deve exibir uma tabela com uma coluna única para o título de cada filme.
2.  No arquivo `2.sql`, escreva uma consulta SQL para determinar o ano de nascimento de Emma Stone.
    *   Sua consulta deve exibir uma tabela com uma única coluna e uma única linha (sem contar o cabeçalho) contendo o ano de nascimento de Emma Stone.
    *   Você pode assumir que há apenas uma pessoa no banco de dados com o nome Emma Stone.
3.  No arquivo `3.sql`, escreva uma consulta SQL para listar os títulos de todos os filmes com uma data de lançamento em ou após 2018, em ordem alfabética.
    *   Sua consulta deve exibir uma tabela com uma única coluna para o título de cada filme.
    *   Filmes lançados em 2018 devem ser incluídos, bem como filmes com datas de lançamento no futuro.
4.  No arquivo `4.sql`, escreva uma consulta SQL para determinar o número de filmes com uma classificação de 10.0 no IMDb.
    *   Sua consulta deve exibir uma tabela com uma única coluna e uma única linha (sem contar o cabeçalho) contendo o número de filmes com uma classificação de 10.0.
5.  No arquivo `5.sql`, escreva uma consulta SQL para listar os títulos e anos de lançamento de todos os filmes de Harry Potter, em ordem cronológica.
    *   Sua consulta deve retornar uma tabela com duas colunas, uma para o título de cada filme e outra para o ano de lançamento de cada filme.
    *   Você pode assumir que o título de todos os filmes de Harry Potter começará com as palavras "Harry Potter" e que, se um título de filme começar com as palavras "Harry Potter", é um filme de Harry Potter.
6.  No arquivo `6.sql`, escreva uma consulta SQL para determinar a classificação média de todos os filmes lançados em 2012.
    *   Sua consulta deve exibir uma tabela com uma única coluna e uma única linha (sem contar o cabeçalho) contendo a classificação média.
7.  No arquivo `7.sql`, escreva uma consulta SQL para listar todos os filmes lançados em 2010 e suas classificações, em ordem decrescente por classificação. Para filmes com a mesma classificação, ordene-os alfabeticamente por título.
    *   Sua consulta deve retornar uma tabela com duas colunas, uma para o título de cada filme e outra para a classificação de cada filme.
    *   Filmes que não possuem classificações não devem ser incluídos no resultado.
8.  No arquivo `8.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que atuaram em Toy Story.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada pessoa.
    *   Você pode assumir que há apenas um filme no banco de dados com o título Toy Story.
9.  No arquivo `9.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que atuaram em um filme lançado em 2004, ordenado por ano de nascimento.
    *   Sua consulta deve exibir uma tabela com uma única coluna para o nome de cada pessoa.
    *   As pessoas com o mesmo ano de nascimento podem ser listadas em qualquer ordem.
    *   Não é necessário se preocupar com pessoas que não têm ano de nascimento listado, desde que aqueles que têm um ano de nascimento sejam listados em ordem.
    *   Se uma pessoa apareceu em mais de um filme em 2004, deve aparecer apenas uma vez nos seus resultados.
10.  No arquivo `10.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que dirigiram um filme que recebeu uma classificação de pelo menos 9,0.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada pessoa.
    *   Se uma pessoa dirigiu mais de um filme que recebeu uma classificação de pelo menos 9,0, ela deve aparecer apenas uma vez nos seus resultados.
11.  No arquivo `11.sql`, escreva uma consulta SQL para listar os títulos dos cinco filmes com classificação mais alta (em ordem) em que Chadwick Boseman atuou, começando pelo com classificação mais alta.
    *   Sua consulta deve exibir uma tabela com uma única coluna para o título de cada filme.
    *   Você pode assumir que há apenas uma pessoa no banco de dados com o nome Chadwick Boseman.
12.  No arquivo `12.sql`, escreva uma consulta SQL para listar os títulos de todos os filmes em que Johnny Depp e Helena Bonham Carter atuaram.
    *   Sua consulta deve exibir uma tabela com uma única coluna para o título de cada filme.
    *   Você pode assumir que há apenas uma pessoa no banco de dados com o nome Johnny Depp.
    *   Você pode assumir que há apenas uma pessoa no banco de dados com o nome Helena Bonham Carter.
13.  No arquivo `13.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que atuaram em um filme em que Kevin Bacon também atuou.
    *   Sua consulta deve exibir uma tabela com uma única coluna para o nome de cada pessoa.
    *   Pode haver várias pessoas com o nome Kevin Bacon no banco de dados. Certifique-se de selecionar apenas o Kevin Bacon nascido em 1958.
    *   Kevin Bacon em si não deve ser incluído na lista resultante.

Passo a Passo
-------------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Uso
-----

Para testar suas consultas no VS Code, você pode consultar o banco de dados executando o comando:

    $ cat filename.sql | sqlite3 movies.db
    

onde `filename.sql` é o arquivo contendo sua consulta SQL.

Você também pode executar

    $ cat filename.sql | sqlite3 movies.db > output.txt
    

para redirecionar a saída da consulta para um arquivo de texto chamado `output.txt`. (Isso pode ser útil para verificar quantas linhas são retornadas pela sua consulta!)

Dicas
-----

*   Verifique [esta referência de palavras-chave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para obter algumas sintaxes SQL que podem ser úteis!
*   Verifique [sqlstyle.guide](https://www.sqlstyle.guide/) para obter orientações sobre estilo adequado em SQL, especialmente à medida que suas consultas ficam mais complexas!

Testes
-------

Embora `check50` esteja disponível para este problema, você é encorajado a testar seu código por conta própria para cada um dos seguintes. Você pode executar `sqlite3 movies.db` para executar consultas adicionais no banco de dados para garantir que seu resultado esteja correto.

Se você estiver usando o banco de dados `movies.db` fornecido na distribuição deste conjunto de problemas, você deverá encontrar que:

*   A execução de `1.sql` resulta em uma tabela com 1 coluna e 10.050 linhas.
*   A execução de `2.sql` resulta em uma tabela com 1 coluna e 1 linha.
*   A execução de `3.sql` resulta em uma tabela com 1 coluna e 88.918 linhas.
*   A execução de `4.sql` resulta em uma tabela com 1 coluna e 1 linha.
*   A execução de `5.sql` resulta em uma tabela com 2 colunas e 12 linhas.
*   A execução de `6.sql` resulta em uma tabela com 1 coluna e 1 linha.
*   A execução de `7.sql` resulta em uma tabela com 2 colunas e 7.085 linhas.
*   A execução de `8.sql` resulta em uma tabela com 1 coluna e 4 linhas.
*   A execução de `9.sql` resulta em uma tabela com 1 coluna e 18.946 linhas.
*   A execução de `10.sql` resulta em uma tabela com 1 coluna e 3.392 linhas.
*   A execução de `11.sql` resulta em uma tabela com 1 coluna e 5 linhas.
*   A execução de `12.sql` resulta em uma tabela com 1 coluna e 7 linhas.
*   A execução de `13.sql` resulta em uma tabela com 1 coluna e 182 linhas.

Observe que as contagens de linhas não incluem linhas de cabeçalho que mostram apenas nomes de colunas.

Se sua consulta retornar um número de linhas ligeiramente diferente do resultado esperado, certifique-se de que está lidando corretamente com duplicatas! Para consultas que solicitam uma lista de nomes, nenhuma pessoa deve ser listada duas vezes, mas duas pessoas diferentes que têm o mesmo nome devem ser listadas.

Execute o que segue para avaliar a correção do seu código usando `check50`.

    check50 cs50/problems/2023/x/movies
    

Como Enviar
-----------

No seu terminal, execute o que segue para enviar o seu trabalho.

    submit50 cs50/problems/2023/x/movies
    

Agradecimentos
----------------

Informações cortesia de IMDb ([imdb.com](https://www.imdb.com)). Usado com permissão.

