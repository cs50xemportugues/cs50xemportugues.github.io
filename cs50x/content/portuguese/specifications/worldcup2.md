Começando
----------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e, em seguida, execute `cd`. Você deve encontrar que seu "prompt" se assemelha ao abaixo.

    $
    
Clique dentro dessa janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/labs/6/world-cup.zip
    
seguido de

    Enter

para fazer o download de um arquivo ZIP chamado `world-cup.zip` em seu espaço de códigos. Tome cuidado para não ignorar o espaço entre wget e a URL a seguir, ou qualquer outro caractere, para esse assunto!

Agora execute

    unzip world-cup.zip
    
para criar uma pasta chamada `world-cup`. Você não precisa mais do arquivo ZIP, portanto, execute

    rm world-cup.zip
    
e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd world-cup
    
seguido de Enter para se mover para o diretório (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    world-cup/ $
    
Se tudo ocorreu bem, execute

    ls
    
e você deve ver os seguintes arquivos:

    answers.txt  2018m.csv  2019w.csv  tournament.py
    
Se você tiver problemas, siga essas mesmas etapas novamente e veja se consegue determinar onde errou!

Entendendo
-----------

Comece dando uma olhada no arquivo `2018m.csv`. Este arquivo contém as 16 equipes na fase eliminatória da Copa do Mundo de 2018 e as classificações de cada equipe. Observe que o arquivo CSV tem duas colunas, chamadas `team` (representando o nome do país da equipe) e `rating` (representando a classificação da equipe).

A ordem em que as equipes aparecem determina quais equipes jogarão entre si em cada rodada (na primeira rodada, por exemplo, o Uruguai jogará contra Portugal e a França jogará contra Argentina; na próxima rodada, o vencedor da partida Uruguai-Portugal jogará contra o vencedor da partida França-Argentina). Portanto, certifique-se de não editar a ordem em que as equipes aparecem neste arquivo!

Finalmente, em Python, podemos representar cada equipe como um dicionário que contém duas chaves: o nome da equipe e a classificação. Uruguai, por exemplo, gostaríamos de representar em Python como `{"team": "Uruguai", "rating": 976}`.

Em seguida, dê uma olhada no arquivo `2019w.csv`, que contém dados formatados da mesma maneira para a Copa do Mundo Feminina de 2019.

Agora, abra o arquivo `tournament.py` e veja que escrevemos algum código para você. A variável `N` no topo representa quantas simulações da Copa do Mundo serão executadas: neste caso, 1000.

A função `simulate_game` aceita duas equipes como entradas (lembre-se de que cada equipe é um dicionário que contém o nome da equipe e a classificação da equipe) e simula uma partida entre elas. Se a primeira equipe vencer, a função retornará `True`; caso contrário, a função retornará `False`.

A função `simulate_round` aceita uma lista de equipes (em uma variável chamada `teams`) como entrada e simula jogos entre cada par de equipes. A função então retorna uma lista de todas as equipes que venceram a rodada.

Na função `main`, observe que primeiro garantimos que `len(sys.argv)` (o número de argumentos na linha de comando) seja 2. Usaremos argumentos na linha de comando para informar ao Python qual arquivo CSV de equipe usar para executar a simulação do torneio. Então, definimos uma lista chamada `teams` (que eventualmente será uma lista de equipes) e um dicionário chamado `counts` (que associará nomes de equipes ao número de vezes que a equipe venceu um torneio simulado). Agora, a população deles está nas suas mãos!

Finalmente, no final de `main`, classificamos as equipes em ordem decrescente de quantas vezes elas venceram simulações (de acordo com `counts`) e imprimimos a probabilidade estimada de cada equipe vencer a Copa do Mundo.

A população de `teams` e `counts` e a escrita da função `simulate_tournament` estão a cargo de você!