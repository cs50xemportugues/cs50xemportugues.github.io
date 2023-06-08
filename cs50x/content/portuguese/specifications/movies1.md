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