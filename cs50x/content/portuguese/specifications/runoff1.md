Runoff
======

Neste programa, você irá implementar um programa que simula uma eleição com votação instantânea, conforme abaixo.

    ./ runnoff Alice Bob Charlie
    Número de eleitores: 5
    Classificação 1: Alice
    Classificação 2: Bob
    Classificação 3: Charlie
    
    Classificação 1: Alice
    Classificação 2: Charlie
    Classificação 3: Bob
    
    Classificação 1: Bob
    Classificação 2: Charlie
    Classificação 3: Alice
    
    Classificação 1: Bob
    Classificação 2: Alice
    Classificação 3: Charlie
    
    Classificação 1: Charlie
    Classificação 2: Alice
    Classificação 3: Bob
    
    Alice
    

Contexto
----------

Você já sabe sobre eleições de pluralidade, que seguem um algoritmo muito simples para determinar o vencedor de uma eleição: cada eleitor tem um voto e o candidato com mais votos ganha.

Mas a votação por pluralidade tem algumas desvantagens. O que acontece, por exemplo, em uma eleição com três candidatos, e as cédulas são lançadas da seguinte forma?

![Cinco cédulas, empate entre Alice e Bob](https://cs50.harvard.edu/x/2023/psets/3/fptp_ballot_1.png)

Uma votação por pluralidade declararia um empate entre Alice e Bob, já que cada um tem dois votos. Mas esse é o resultado certo?

Existe outro tipo de sistema de votação conhecido como sistema de votação com classificação. Em um sistema de classificação, os eleitores podem votar em mais de um candidato. Em vez de apenas votar em sua escolha principal, eles podem classificar os candidatos em ordem de preferência. As cédulas resultantes podem parecer assim.

![Três cédulas, com preferências classificadas](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_1.png)

Aqui, cada eleitor, além de especificar o candidato de primeira preferência, também indicou os candidatos de segunda e terceira escolha. E agora, o que anteriormente era uma eleição empatada agora poderia ter um vencedor. A disputa era originalmente entre Alice e Bob, então Charlie estava fora da corrida. Mas o eleitor que escolheu Charlie preferiu Alice a Bob, então Alice poderia ser declarada a vencedora aqui.

A votação por classificação também pode resolver mais uma possível desvantagem da votação por pluralidade. Dê uma olhada nas seguintes cédulas.

![Nove cédulas, com preferências classificadas](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_3.png)

Quem deveria ganhar esta eleição? Em uma votação de pluralidade, onde cada eleitor escolhe apenas sua primeira preferência, Charlie ganha esta eleição com quatro votos, em comparação com apenas três para Bob e dois para Alice. Mas a maioria dos eleitores (5 em 9) ficaria mais feliz com Alice ou Bob em vez de Charlie. Ao considerar preferências classificadas, um sistema de votação pode escolher um vencedor que reflita melhor as preferências dos eleitores.

Um desses sistemas de votação com classificação é o sistema de votação com eliminatória instantânea. Em uma eleição de eliminatória instantânea, os eleitores podem classificar quantos candidatos desejarem. Se algum candidato tiver uma maioria (mais de 50%) dos votos de primeira preferência, esse candidato é declarado o vencedor da eleição.

Se nenhum candidato tiver mais de 50% dos votos, então ocorre uma "eliminatória instantânea". O candidato que recebeu o menor número de votos é eliminado da eleição, e qualquer pessoa que tenha escolhido originalmente aquele candidato como sua primeira preferência agora tem sua segunda preferência considerada. Por que fazer isso? Efetivamente, isso simula o que teria acontecido se o candidato menos popular não tivesse participado da eleição em primeiro lugar.

O processo se repete: se nenhum candidato tiver uma maioria dos votos, o candidato em último lugar é eliminado, e qualquer pessoa que tenha votado nele votará em sua próxima preferência (que ainda não foi eliminada). Uma vez que um candidato tiver uma maioria, esse candidato é declarado o vencedor.

Vamos considerar as nove cédulas acima e examinar como uma eleição com eliminatória instantânea seria realizada.

Alice tem dois votos, Bob tem três votos e Charlie tem quatro votos. Para vencer uma eleição com nove pessoas, é necessária uma maioria (cinco votos). Como ninguém tem maioria, uma votação com eliminação instantânea precisa ser realizada. Alice tem o menor número de votos (apenas dois), então Alice é eliminada. Os eleitores que votaram originalmente em Alice listaram Bob como segunda preferência, então Bob recebe os dois votos extras. Bob agora tem cinco votos, e Charlie ainda tem quatro votos. Bob agora tem maioria, e Bob é declarado o vencedor.

Que casos de limite devemos considerar aqui?

Uma possibilidade é que haja um empate para quem deve ser eliminado. Podemos lidar com esse cenário dizendo que todos os candidatos que estão empatados em último lugar serão eliminados. No entanto, se cada candidato restante tiver exatamente o mesmo número de votos, eliminar os candidatos empatados em último lugar significa eliminar todo mundo! Então, nesse caso, teremos que ter cuidado para não eliminar todos e apenas declarar a eleição empatada entre todos os candidatos restantes.

Algumas eleições com eliminação instantânea não exigem que os eleitores classifiquem todas as suas preferências - então pode haver cinco candidatos em uma eleição, mas um eleitor pode escolher apenas dois. Para fins deste problema, no entanto, ignoraremos esse caso limitado e assumiremos que todos os eleitores classificarão todos os candidatos em sua ordem de preferência.

Parece um pouco mais complicado do que uma votação por pluralidade, não é mesmo? Mas isso tem a vantagem de ser um sistema eleitoral em que o vencedor da eleição representa com mais precisão as preferências dos eleitores.