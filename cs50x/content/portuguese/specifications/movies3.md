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