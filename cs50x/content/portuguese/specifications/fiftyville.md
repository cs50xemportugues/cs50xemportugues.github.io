Fiftyville
==========

Escreva consultas SQL para resolver um mistério.

Um Mistério em Fiftyville
-----------------------

O pato CS50 foi roubado! A cidade de Fiftyville pediu a sua ajuda para resolver o mistério do pato roubado. As autoridades acreditam que o ladrão roubou o pato e, logo depois, pegou um voo para fora da cidade com a ajuda de um cúmplice. Seu objetivo é identificar:

*   Quem é o ladrão,
*   Qual é a cidade para a qual o ladrão escapou e
*   Quem é o cúmplice do ladrão que o ajudou a escapar.

Tudo o que se sabe é que o roubo **ocorreu em 28 de julho de 2021** e que aconteceu na rua Humphrey.

Como você irá sobre a resolução deste mistério? As autoridades de Fiftyville coletaram alguns registros da cidade na época do roubo e prepararam um banco de dados SQLite para você, `fiftyville.db`, contendo tabelas de dados da cidade. Você pode consultar essa tabela usando consultas SQL `SELECT` para acessar os dados de interesse para você. Usando apenas as informações no banco de dados, sua tarefa é resolver o mistério.

Primeiros Passos
---------------

Faça login em [code.cs50.io](https://code.cs50.io/), clique na janela do seu terminal e execute `cd` sozinho. Você deve ver que o prompt da janela do terminal se parece com o abaixo:

    $
    

A seguir, execute

    wget https://cdn.cs50.net/2022/fall/psets/7/fiftyville.zip
    

para baixar um arquivo ZIP chamado `fiftyville.zip` para o seu espaço de código.

Em seguida, execute

    unzip fiftyville.zip
    

para criar uma pasta chamada `fiftyville`. Você não precisa mais do arquivo ZIP, então execute

    rm fiftyville.zip
    

e responda com "y" seguido de Enter para remover o arquivo ZIP que você baixou.

Agora digite

    cd fiftyville
    

seguido de Enter para mover-se para o diretório. Seu prompt agora deve se parecer com o abaixo.

    fiftyville/ $
    

Execute `ls` sozinho e você deve ver alguns arquivos:

    answers.txt  fiftyville.db  log.sql
    

Se você tiver algum problema, siga esses mesmos passos novamente e veja se consegue determinar onde errou!

Especificação
-------------

Para este problema, igualmente importante para resolver o mistério é o processo que você usa para resolvê-lo. Em `log.sql`, mantenha um registro de todas as consultas SQL que você executar no banco de dados. Acima de cada consulta, rotule cada uma com um comentário (em SQL, os comentários são quaisquer linhas que começam com `--`) descrevendo por que você está executando a consulta e/ou quais informações você espera obter dessa consulta em particular. Você pode usar comentários no arquivo de log para adicionar notas adicionais sobre seu processo de pensamento enquanto resolve o mistério: no final, esse arquivo deve servir como evidência do processo que você usou para identificar o ladrão!

Ao escrever suas consultas, você pode perceber que algumas delas podem se tornar bastante complexas. Para ajudar a manter suas consultas legíveis, consulte os princípios do bom estilo em [sqlstyle.guide](https://www.sqlstyle.guide). A seção de [indentação](https://www.sqlstyle.guide/#indentation) pode ser especialmente útil!

Depois de resolver o mistério, complete cada uma das linhas em `answers.txt` preenchendo o nome do ladrão, a cidade para a qual o ladrão escapou e o nome do cúmplice do ladrão que o ajudou a escapar da cidade. (Certifique-se de não alterar nenhum texto existente no arquivo ou adicionar outras linhas ao arquivo!)

No final, você deve apresentar seus arquivos `log.sql` e `answers.txt`.

Passo a Passo
-----------

Dicas
-----

*   Execute `sqlite3 fiftyville.db` para começar a executar consultas no banco de dados.
    *   Enquanto estiver executando o `sqlite3`, executar `.tables` listará todas as tabelas do banco de dados.
    *   Enquanto estiver executando o `sqlite3`, executar `.schema TABLE_NAME`, em que `TABLE_NAME` é o nome de uma tabela no banco de dados, mostrará o comando `CREATE TABLE` usado para criar a tabela. Isso pode ser útil para saber quais colunas consultar!
*   Você pode achar útil começar com a tabela `crime_scene_reports`. Comece procurando um relatório de cena do crime que corresponda à data e ao local do crime.
*   Veja esta [referência de palavras-chave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para alguma sintaxe SQL que pode ser útil!

Testando
-------

Execute o abaixo para avaliar a correção do seu código usando `check50`.

    check50 cs50/problems/2023/x/fiftyville
    

Como Enviar
-------------

No seu terminal, execute o abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2023/x/fiftyville
    

Reconhecimentos
----------------

Inspirado em outro caso em [SQL City](https://mystery.knightlab.com/).