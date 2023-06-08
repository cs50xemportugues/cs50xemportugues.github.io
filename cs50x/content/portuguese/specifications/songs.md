Laboratório 7: Músicas
============

Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que cada aluno em qualquer grupo contribua igualmente para o laboratório.

Escreva consultas SQL para responder a perguntas sobre um banco de dados de músicas.

Iniciando
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e execute `cd` por si só. Você deve encontrar que o "prompt" é semelhante ao abaixo.

    $
    

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/labs/7/songs.zip
    

seguido de Enter para baixar um ZIP chamado `songs.zip` em seu espaço de código. Tenha cuidado para não ignorar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere, na verdade!

Agora execute

    unzip songs.zip
    

para criar uma pasta chamada `songs`. Você não precisa mais do arquivo ZIP; portanto, execute

    rm songs.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd songs
    

seguido de Enter para se mover para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    songs/ $
    

Se tudo correu bem, você deve executar

    ls
    

e você deve ver 8 arquivos .sql, `songs.db` e `answers.txt`.

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se pode determinar onde errou!

Entendimento
-------------

Foi fornecido um arquivo chamado `songs.db`, um banco de dados SQLite que armazena dados sobre músicas e seus artistas do [Spotify](https://developer.spotify.com/documentation/web-api/). Este conjunto de dados contém as 100 músicas mais tocadas no Spotify em 2018. Em uma janela do terminal, execute `sqlite3 songs.db` para poder começar a executar consultas no banco de dados.

Primeiro, quando o `sqlite3` solicitar uma consulta, digite `.schema` e pressione Enter. Isso exibirá as declarações `CREATE TABLE` que foram usadas para gerar cada uma das tabelas no banco de dados. Examinando essas declarações, você pode identificar as colunas presentes em cada tabela.

Observe que cada `artista` tem um `id` e um `nome`. Observe também que cada música tem um `nome`, um `artist_id` (correspondente ao `id` do artista da música), assim como valores de danceabilidade, energia, chave, volume, fala (presença de palavras faladas em uma faixa), valência, tempo e duração da música (medida em milissegundos).

O desafio é escrever consultas SQL para responder a uma variedade de perguntas diferentes selecionando dados de uma ou mais dessas tabelas. Depois de fazer isso, você refletirá sobre as maneiras pelas quais o Spotify pode usar esses mesmos dados em sua campanha anual [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) para caracterizar os hábitos dos ouvintes.

Detalhes de implementação
----------------------

Para cada um dos seguintes problemas, você deve escrever uma única consulta SQL que gere os resultados especificados por cada problema. Sua resposta deve estar na forma de uma única consulta SQL, embora você possa aninhar outras consultas dentro de sua consulta. Você **não deve** assumir nada sobre os `id`s de qualquer música ou artista em particular: suas consultas devem ser precisas mesmo se o `id` de qualquer música ou pessoa fosse diferente. Finalmente, cada consulta deve retornar apenas os dados necessários para responder à pergunta: se o problema solicitá-lo, por exemplo, apenas para fornecer os nomes das músicas, sua consulta não deve fornecer o tempo de cada música.

1.  Em `1.sql`, escreva uma consulta SQL para listar os nomes de todas as músicas do banco de dados.
    *   Sua consulta deve produzir uma tabela com uma única coluna para o nome de cada música.
2.  Em `2.sql`, escreva uma consulta SQL para listar os nomes de todas as músicas em ordem crescente de tempo.
    *   Sua consulta deve produzir uma tabela com uma única coluna para o nome de cada música.
3.  Em `3.sql`, escreva uma consulta SQL para listar os nomes das 5 músicas mais longas, em ordem decrescente de duração.
    *   Sua consulta deve produzir uma tabela com uma única coluna para o nome de cada música.
4.  Em `4.sql`, escreva uma consulta SQL que liste os nomes de quaisquer músicas que tenham danceabilidade, energia e valência maiores que 0,75.
    *   Sua consulta deve produzir uma tabela com uma única coluna para o nome de cada música.
5.  Em `5.sql`, escreva uma consulta SQL que retorne a energia média de todas as músicas.
    *   Sua consulta deve produzir uma tabela com uma única coluna e uma única linha contendo a energia média.
6.  Em `6.sql`, escreva uma consulta SQL que liste os nomes das músicas que são de Post Malone.
    *   Sua consulta deve produzir uma tabela com uma única coluna para o nome de cada música.
    *   Você não deve fazer nenhuma suposição sobre qual é o `artist_id` de Post Malone.
7.  Em `7.sql`, escreva uma consulta SQL que retorne a energia média das músicas que são de Drake.
    *   Sua consulta deve produzir uma tabela com uma única coluna e uma única linha contendo a energia média.
    *   Você não deve fazer nenhuma suposição sobre qual é o `artist_id` do Drake.
8.  Em `8.sql`, escreva uma consulta SQL que liste os nomes das músicas que apresentam outros artistas.
    *   As músicas que apresentam outros artistas incluirão "feat." no nome da música.
    *   Sua consulta deve produzir uma tabela com uma única coluna para o nome de cada música.

### Walkthrough

Este vídeo foi gravado quando o curso ainda usava o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu espaço de código, o comportamento dos dois ambientes deve ser amplamente semelhante!

Uso
-----

Além de executar suas consultas no `sqlite3`, você pode testar suas consultas no terminal do VS Code executando

    $ cat filename.sql | sqlite3 songs.db
    

onde `filename.sql` é o arquivo contendo sua consulta SQL.

### Sugestões

*   Consulte [este guia de referência de palavras-chave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para obter uma sintaxe SQL que possa ajudar!

Não sabe como resolver?

### Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) é um recurso que apresenta as 100 músicas mais reproduzidas do Spotify do usuário no ano passado. Em 2021, o Spotify Wrapped calculou uma [“Aura Áudio”](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) para cada usuário, uma “leitura das \[suas\] duas emoções mais proeminentes ditadas pelas \[suas\] principais músicas e artistas do ano”. Suponha que o Spotify determine uma aura de áudio olhando para a energia média, valência e danceabilidades das 100 músicas principais de uma pessoa do ano passado. Em `answers.txt`, reflita sobre as seguintes perguntas:

*   Se `songs.db` contém as 100 principais músicas de um ouvinte de 2018, como você caracterizaria sua aura de áudio?
*   Hipotetize por que a maneira como você calculou essa aura pode _não_ ser muito representativa do ouvinte. Que maneiras melhores de calcular essa aura você proporia?

Certifique-se de enviar `answers.txt` juntamente com cada um dos seus arquivos `.sql`!

### Teste

Execute o abaixo para avaliar a correção do seu código usando `check50`.

    check50 cs50/labs/2023/x/songs
    

Como enviar
-------------

Em seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/labs/2023/x/songs
    

Reconhecimentos
----------------

Conjunto de dados do [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).