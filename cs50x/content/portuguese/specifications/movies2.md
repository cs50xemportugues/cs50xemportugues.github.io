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