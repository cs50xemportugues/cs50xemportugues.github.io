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