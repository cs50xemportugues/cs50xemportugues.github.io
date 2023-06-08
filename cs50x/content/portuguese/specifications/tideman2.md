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