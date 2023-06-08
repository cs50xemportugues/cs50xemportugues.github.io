Tideman
=======

Para este programa, você implementará um programa que executa uma eleição Tideman, como abaixo.

    $ ./tideman Alice Bob Charlie
    Number of voters: 5
    Rank 1: Alice
    Rank 2: Charlie
    Rank 3: Bob
    
    Rank 1: Alice
    Rank 2: Charlie
    Rank 3: Bob
    
    Rank 1: Bob
    Rank 2: Charlie
    Rank 3: Alice
    
    Rank 1: Bob
    Rank 2: Charlie
    Rank 3: Alice
    
    Rank 1: Charlie
    Rank 2: Alice
    Rank 3: Bob
    
    Charlie
    

Contexto
----------

Você já sabe sobre eleições plurais, que seguem um algoritmo muito simples para determinar o vencedor de uma eleição: cada eleitor recebe um voto, e o candidato com mais votos ganha.

Mas a votação plural tem algumas desvantagens. O que acontece, por exemplo, em uma eleição com três candidatos, e os votos abaixo são lançados?

![Five ballots, tie betweeen Alice and Bob](https://cs50.harvard.edu/x/2023/psets/3/fptp_ballot_1.png)

Uma votação de pluralidade aqui declararia um empate entre Alice e Bob, já que cada um tem dois votos. Mas essa é a saída correta?

Existe outro tipo de sistema de votação conhecido como sistema de votação por classificação. Em um sistema de classificação, os eleitores podem votar em mais de um candidato. Em vez de votar apenas em sua primeira escolha, eles podem classificar os candidatos em ordem de preferência. As cédulas resultantes podem ser, portanto, como as abaixo.

![Three ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_1.png)

Aqui, cada eleitor, além de especificar seu candidato de primeira preferência, também indicou sua segunda e terceira escolhas. E agora, o que antes era uma eleição empatada agora pode ter um vencedor. A corrida estava originalmente empatada entre Alice e Bob. Mas o eleitor que escolheu Charlie preferiu Alice a Bob, então Alice poderia aqui ser declarada a vencedora.

A votação por classificação também pode resolver outra possível desvantagem da votação de pluralidade. Dê uma olhada nas seguintes cédulas.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/condorcet_1.png)

Quem deve ganhar esta eleição? Em uma votação de pluralidade em que cada eleitor escolhe apenas sua primeira preferência, Charlie ganha esta eleição com quatro votos em comparação com apenas três para Bob e dois para Alice. (Observe que, se você estiver familiarizado com o sistema de votação de segunda rodada instantânea, Charlie também ganha aqui sob esse sistema). Alice, no entanto, pode justificadamente argumentar que ela deveria ser a vencedora da eleição em vez de Charlie: afinal, dos nove eleitores, a maioria (cinco deles) preferiu Alice a Charlie, então a maioria das pessoas ficaria mais feliz com Alice como vencedora em vez de Charlie.

Alice é, nesta eleição, a chamada "vencedora de Condorcet" da eleição: a pessoa que teria vencido qualquer confronto cabeça a cabeça contra outro candidato. Se a eleição tivesse sido apenas Alice e Bob, ou apenas Alice e Charlie, Alice teria vencido.

O método de votação Tideman (também conhecido como "pares classificados") é um método de votação por classificação que garante produzir o vencedor de Condorcet da eleição, se houver um.

Em termos gerais, o método Tideman funciona construindo um "gráfico" de candidatos, onde uma seta (ou seja, uma borda) de um candidato A para um candidato B indica que o candidato A vence contra o candidato B em um confronto cabeça a cabeça. O gráfico para a eleição acima, então, seria como abaixo.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/condorcet_graph_1.png)

A seta de Alice para Bob significa que mais eleitores preferem Alice a Bob (5 preferem Alice, 4 preferem Bob). Da mesma forma, as outras setas significam que mais eleitores preferem Alice a Charlie, e mais eleitores preferem Charlie a Bob.

Olhando para este gráfico, o método Tideman diz que o vencedor da eleição deve ser a "fonte" do gráfico (ou seja, o candidato que não tem nenhuma seta apontando para eles). Neste caso, a fonte é Alice - Alice é a única que não tem nenhuma seta apontando para ela, o que significa que ninguém é preferido cabeça a cabeça sobre Alice. Alice é assim declarada a vencedora da eleição.

No entanto, é possível que, quando as setas são desenhadas, não haja vencedor de Condorcet. Considere as cédulas abaixo.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/no_condorcet_1.png)

Entre Alice e Bob, Alice é preferida por Bob por uma margem de 7 a 2. Entre Bob e Charlie, Bob prefere Charlie por uma margem de 5 a 4. Mas, entre Charlie e Alice, Charlie prefere Alice por uma margem de 6 a 3. Se desenharmos o gráfico, não há fonte! Temos um ciclo de candidatos, onde Alice derrota Bob, que derrota Charlie, que derrota Alice (como um jogo de pedra-papel-tesoura). Neste caso, parece que não há como escolher um vencedor.

Para lidar com isso, o algoritmo Tideman deve ter cuidado para evitar criar ciclos no gráfico de candidatos. Como ele faz isso? O algoritmo bloqueia primeiro as bordas mais fortes, já que essas são, em geral, as mais significativas. Em particular, o algoritmo Tideman especifica que as bordas de confronto devem ser "bloqueadas" no gráfico, uma a uma, com base na "força" da vitória (quanto mais pessoas preferem um candidato sobre seu oponente, mais forte é a vitória). Desde que a borda possa ser bloqueada no gráfico sem criar um ciclo, a borda é adicionada; caso contrário, a borda é ignorada.

Como isso funcionaria no caso dos votos acima? Bem, a maior margem de vitória para um par é Alice batendo Bob, já que 7 eleitores preferem Alice a Bob (nenhum outro confronto cabeça a cabeça tem um vencedor preferido por mais de 7 eleitores). Então, a seta de Alice-Bob é bloqueada no gráfico primeiro. A próxima maior margem de vitória é 6-3 de Charlie sobre Alice, então essa seta é bloqueada em seguida.

A próxima é a vitória de Bob, por 5-4 sobre Charlie. Mas note: se adicionarmos uma seta de Bob para Charlie agora, criaríamos um ciclo! Como o gráfico não pode permitir loops, devemos pular esta borda e não adicioná-la ao gráfico. Se houvesse mais setas a serem consideradas, olharíamos para as próximas, mas essa foi a última seta, então o gráfico está completo.

Este processo é mostrado passo a passo abaixo, com o gráfico final à direita.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/lockin.png)

Com base no gráfico resultante, Charlie é a fonte (não há nenhuma seta apontando para Charlie), assim, Charlie é declarado o vencedor desta eleição.

Mais formalmente, o método de votação Tideman consiste em três partes:

*   **Totalização**: uma vez que todos os eleitores indicaram todas as suas preferências, determine, para cada par de candidatos, quem é o candidato preferido e por qual margem eles são preferidos.
*   **Ordenação**: ordene os pares de candidatos em ordem decrescente de força da vitória, onde a força da vitória é definida como o número de eleitores que preferem o candidato preferido.
*   **Bloqueio**: começando com o par mais forte, passe pelos pares de candidatos em ordem e "trave" cada par no gráfico de candidatos, desde que trancar esse par não crie um ciclo no gráfico.

Uma vez que o gráfico está completo, a fonte do gráfico (aquele com nenhuma seta apontando para ele) é o vencedor!

Começando
---------------

Faça login em [code.cs50.io](https://code.cs50.io/), clique na janela do seu terminal e execute `cd` por si só. Você deve encontrar que o prompt da janela do seu terminal se parece com o abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/3/tideman.zip
    

para baixar um ZIP chamado `tideman.zip` no seu espaço de código.

Então execute

    unzip tideman.zip
    

para criar uma pasta chamada `tideman`. Você não precisa mais do arquivo ZIP, então pode executar

    rm tideman.zip
    

e responder com "y" seguido de Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd tideman
    

seguido de Enter para mover-se para dentro (ou seja, abrir) do diretório. Seu prompt agora deve se assemelhar ao abaixo.

    tideman/ $
    

Se tudo correu bem, você deve executar

    ls
    

e ver um arquivo chamado `tideman.c`. Executar `code tideman.c` deve abrir o arquivo onde você digitará seu código para este conjunto de problemas. Se não, retraçar seus passos e ver se você pode determinar onde você errou!

Compreendendo
-------------

Vamos dar uma olhada em `tideman.c`.

Primeiro, observe a matriz bidimensional `preferences`. O inteiro `preferences[i][j]` representará o número de eleitores que preferem o candidato `i` ao candidato `j`.

O arquivo também define outra matriz bidimensional, chamada `locked`, que representará o grafo de candidatos. `locked` é uma matriz booleana, então `locked[i][j]` sendo `true` representa a existência de uma borda apontando do candidato `i` para o candidato `j`; `false` significa que não há borda. (Se curioso, essa representação de um grafo é conhecida como uma "matriz de adjacência").

Em seguida, temos uma `struct` chamada `pair`, usada para representar um par de candidatos: cada par inclui o índice do candidato vencedor e o índice do candidato perdedor.

Os próprios candidatos são armazenados no array `candidates`, que é um array de `strings` representando os nomes de cada um dos candidatos. Há também um array de `pairs`, que representará todos os pares de candidatos (para os quais um é preferido em relação ao outro) na eleição.

O programa também tem duas variáveis globais: `pair_count` e `candidate_count`, representando o número de pares e o número de candidatos em arrays `pairs` e `candidates`, respectivamente.

Agora vamos para `main`. Observe que depois de determinar o número de candidatos, o programa percorre o grafo `locked` e define inicialmente todos os valores como `false`, o que significa que nosso grafo inicial não terá bordas nele.

Em seguida, o programa percorre todos os eleitores e coleta suas preferências em um array chamado `ranks` (por meio de uma chamada a `vote`), onde `ranks[i]` é o índice do candidato que é a `i`ª preferência para o eleitor. Essas classificações são passadas para a função `record_preference`, cuja função é pegar essas classificações e atualizar a variável global `preferences`.

Depois que todos os votos são dados, os pares de candidatos são adicionados ao array `pairs` por meio de uma chamada a `add_pairs`, classificados por meio de uma chamada a `sort_pairs` e trancados no grafo por meio de uma chamada a `lock_pairs`. Finalmente, `print_winner` é chamado para imprimir o nome do vencedor da eleição!

Mais abaixo no arquivo, você verá que as funções `vote`, `record_preference`, `add_pairs`, `sort_pairs`, `lock_pairs` e `print_winner` estão em branco. Isso é com você!

Especificação
-------------

Complemente a implementação de `tideman.c` de forma que simule uma eleição de Tideman.

*   Complete a função `vote`.
    *   A função recebe os argumentos `rank`, `name` e `ranks`. Se `name` corresponder ao nome de um candidato válido, você deve atualizar o vetor `ranks` para indicar que o eleitor tem o candidato como sua preferência na posição `rank` (onde `0` é a primeira preferência, `1` é a segunda preferência, etc.).
    *   Lembre-se que `ranks[i]` representa a `i`-ésima preferência do usuário.
    *   A função deve retornar `true` se a classificação foi registrada com sucesso e `false` caso contrário (por exemplo, se `name` não for o nome de um dos candidatos).
    *   É possível assumir que nenhum dos candidatos terá o mesmo nome.
*   Complete a função `record_preferences`.
    *   A função é chamada uma vez para cada eleitor e recebe como argumento o vetor `ranks` (lembre-se de que `ranks[i]` é a `i`-ésima preferência do eleitor, onde `ranks[0]` é a primeira preferência).
    *   A função deve atualizar o vetor de `preferências` global para adicionar as preferências do eleitor atual. Lembre-se que `preferências[i][j]` deve representar o número de eleitores que preferem o candidato `i` ao candidato `j`.
    *   É possível assumir que cada eleitor classificará todos os candidatos.
*   Complete a função `add_pairs`.
    *   A função deve adicionar todos os pares de candidatos em que um candidato é preferido no vetor `pairs`. Um par de candidatos que empatam (um não é preferido em relação ao outro) não deve ser adicionado ao vetor.
    *   A função deve atualizar a variável global `pair_count` para ser o número total de pares de candidatos. (Os pares devem ser armazenados em `pairs[0]` até `pairs[pair_count - 1]`, inclusive).
*   Complete a função `sort_pairs`.
    *   A função deve classificar o vetor `pairs` em ordem decrescente de força de vitória, onde a força da vitória é definida como o número de eleitores que preferem o candidato preferido. Se vários pares tiverem a mesma força de vitória, é possível assumir que não importa a ordem.
*   Complete a função `lock_pairs`.
    *   A função deve criar o grafo "locked", adicionando todas as arestas em ordem decrescente de força de vitória, desde que a aresta não crie ciclo.
*   Complete a função `print_winner`.
    *   A função deve imprimir o nome do candidato que é a fonte do grafo. É possível assumir que não haverá mais de uma fonte.

Você não deve modificar nada além das implementações das funções `vote`, `record_preferences`, `add_pairs`, `sort_pairs`, `lock_pairs` e `print_winner` em `tideman.c` (e a inclusão de arquivos header adicionais, se desejar). É permitido adicionar funções adicionais em `tideman.c`, desde que não sejam alteradas as declarações das funções existentes.

Passo a passo
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/kb83NwyYI68?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Uso
---

Seu programa deve se comportar como no exemplo abaixo:

    ./tideman Alice Bob Charlie
    Número de eleitores: 5
    Classificação 1: Alice
    Classificação 2: Charlie
    Classificação 3: Bob
    
    Classificação 1: Alice
    Classificação 2: Charlie
    Classificação 3: Bob
    
    Classificação 1: Bob
    Classificação 2: Charlie
    Classificação 3: Alice
    
    Classificação 1: Bob
    Classificação 2: Charlie
    Classificação 3: Alice
    
    Classificação 1: Charlie
    Classificação 2: Alice
    Classificação 3: Bob
    
    Charlie
    

Testando
--------

Certifique-se de testar seu código para verificar se ele lida com...

*   uma eleição com qualquer número de candidatos (até o `MAX` de `9`)
*   votar em um candidato pelo nome
*   votos inválidos para candidatos que não estão na cédula
*   imprimir o vencedor da eleição

Execute o seguinte para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testar por conta própria também!

    check50 cs50/problems/2023/x/tideman
    

Execute o seguinte para avaliar o estilo do seu código usando `style50`.

    style50 tideman.c
    

Como Enviar
-----------

Em seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2023/x/tideman"

