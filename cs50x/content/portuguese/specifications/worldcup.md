Laboratório 6: Copa do Mundo
================

Você pode colaborar com um ou dois colegas neste laboratório, mas é esperado que todos os alunos em tal grupo contribuam igualmente para o laboratório.

Escreva um programa para executar simulações da Copa do Mundo da FIFA.

    $ python tournament.py 2018m.csv
    Bélgica: 20,9% de chance de ganhar
    Brasil: 20,3% de chance de ganhar
    Portugal: 14,5% de chance de ganhar
    Espanha: 13,6% de chance de ganhar
    Suíça: 10,5% de chance de ganhar
    Argentina: 6,5% de chance de ganhar
    Inglaterra: 3,7% de chance de ganhar
    França: 3,3% de chance de ganhar
    Dinamarca: 2,2% de chance de ganhar
    Croácia: 2,0% de chance de ganhar
    Colômbia: 1,8% de chance de ganhar
    Suécia: 0,5% de chance de ganhar
    Uruguai: 0,1% de chance de ganhar
    México: 0,1% de chance de ganhar
    

Contexto
----------

Na Copa do Mundo de futebol, a fase eliminatória é composta por 16 equipes. Em cada rodada, cada equipe joga contra outra equipe e as equipes que perdem são eliminadas. Quando restam apenas duas equipes, a equipe vencedora da partida final é campeã.

No futebol, as equipes recebem [FIFA Ratings] (https://en.wikipedia.org/wiki/FIFA_World_Rankings#Current_calculation_method), que são valores numéricos que representam o nível de habilidade relativa de cada equipe. FIFA Ratings mais altos indicam melhores resultados de jogos anteriores e, dado os FIFA Ratings de duas equipes, é possível estimar a probabilidade de que qualquer equipe vença um jogo com base em suas classificações atuais. As FIFA Ratings de duas Copas do Mundo anteriores estão disponíveis como o [May 2018 Men’s FIFA Ratings] e [March 2019 Women’s FIFA Ratings].

Usando essa informação, podemos simular todo o torneio, simulando repetidamente as rodadas até que reste apenas uma equipe. E se quisermos estimar a probabilidade de que qualquer equipe dada vença o torneio, podemos simular o torneio muitas vezes (por exemplo, 1000 simulações) e contar quantas vezes cada equipe ganha um torneio simulado. 1000 simulações podem parecer muitas, mas com o poder de computação de hoje podemos realizar essas simulações em questão de milissegundos. No final deste laboratório, experimentaremos o quão valioso pode ser aumentar o número de simulações que executamos, dada a troca de tempo de execução.

Sua tarefa neste laboratório é fazer isso usando Python!

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

Detalhes da implementação
----------------------

Complete a implementação do `tournament.py`, de modo que simule vários torneios e mostre a probabilidade de vitória de cada equipe.

Primeiro, em `main`, leia os dados da equipe a partir do arquivo CSV para a memória do seu programa, e adicione cada equipe na lista `teams`.

*   O arquivo a ser usado será fornecido como argumento da linha de comando. Você pode acessar o nome do arquivo com `sys.argv[1]`.
*   Lembre-se que você pode abrir um arquivo com `open(filename)`, em que `filename` é uma variável que armazena o nome do arquivo.
*   Depois de ter um arquivo `f`, use `csv.DictReader(f)` para criar um "leitor": um objeto em Python que pode ser utilizado em um loop para ler o arquivo, uma linha de cada vez, tratando cada linha como um dicionário.
*   Por padrão, todos os valores lidos do arquivo serão strings. Por isso, certifique-se de converter o `rating` da equipe em um `int` (você pode usar a função `int` do Python para isso).
*   Por fim, adicione cada dicionário de equipe em `teams`. A chamada de função `teams.append (x)` adicionará `x` na lista de equipes `teams`.
*   Lembre-se que cada equipe deve ser um dicionário com o nome da `equipe` e um `rating`.

Em seguida, implemente a função `simulate_tournament`. Esta função deve aceitar como entrada uma lista de equipes e deve simular repetidamente as rodadas até restar apenas uma equipe. A função deve retornar o nome desta equipe.

*   Você pode chamar a função `simulate_round`, que simula uma única rodada, aceitando uma lista de equipes como entrada e retornando uma lista com todos os vencedores.
*   Lembre-se que se `x` é uma lista, você pode usar `len(x)` para determinar o comprimento da lista.
*   Não se deve assumir o número de equipes no torneio, embora possa ser assumido que seja uma potência de 2.

Finalmente, na função `main`, execute `N` simulações de torneio, e mantenha o controle de quantas vezes cada equipe vence na contagem de dicionários `counts`.

*   Por exemplo, se o Uruguai venceu 2 torneios e Portugal venceu 3 torneios, então seu dicionário `counts` deve ser `{"Uruguai": 2, "Portugal": 3}`.
*   Você deve usar sua função `simulate_tournament` para simular cada torneio e determinar o vencedor.
*   Lembre-se que, se `counts` é um dicionário, a sintaxe como `counts [nome_da_equipe] = x` associará a chave armazenada em `nome_da_equipe` com o valor armazenado em `x`.
*   Pode-se usar a palavra-chave `in` em Python para verificar se um dicionário já tem uma chave específica. Por exemplo,`if "Portugal" in counts:` verificará se `"Portugal"` já tem um valor existente no dicionário `counts`.

### Passo a passo

<div class="alert" data-alert="primary" role="alert"><p>Esse vídeo foi gravado quando o curso ainda usava o IDE CS50 para escrever código. Embora a interface possa parecer diferente do seu codespace, o comportamento dos dois ambientes deve ser amplamente semelhante!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/o5Bkc7gtRjo"></iframe>


### Dicas

*   Ao ler o arquivo, você pode achar essa sintaxe útil, com `nome_arquivo` como o nome do seu arquivo e `arquivo` uma variável: <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">with</span> <span class="nf">open</span><span class="p">(</span><span class="n">nome_arquivo</span><span class="p">)</span> <span class="k">as</span> <span class="nb">arquivo</span><span class="p">:</span>
      <span class="n">    leitor</span> <span class="o">=</span> <span class="n">csv</span><span class="p">.</span><span class="nc">DictReader</span><span class="p">(</span><span class="nb">arquivo</span><span class="p">)</span>
</code></pre></div>    </div>
        
    
*   Em Python, para acrescentar algo ao final de uma lista, use a função `.append()`.
    

<details><summary>Não tem certeza sobre como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/Fo7Roe8hw3A"></iframe></details>


### Testando

Seu programa deve se comportar conforme os exemplos abaixo. Como as simulações têm aleatoriedade em cada uma, a saída provavelmente não corresponderá perfeitamente aos exemplos abaixo.

    $ python tournament.py 2018m.csv
    Bélgica: 20,9% de chance de vencer
    Brasil: 20,3% de chance de vencer
    Portugal: 14,5% de chance de vencer
    Espanha: 13,6% de chance de vencer
    Suíça: 10,5% de chance de vencer
    Argentina: 6,5% de chance de vencer
    Inglaterra: 3,7% de chance de vencer
    França: 3,3% de chance de vencer
    Dinamarca: 2,2% de chance de vencer
    Croácia: 2,0% de chance de vencer
    Colômbia: 1,8% de chance de vencer
    Suécia: 0,5% de chance de vencer
    Uruguai: 0,1% de chance de vencer
    México: 0,1% de chance de vencer
    

    $ python tournament.py 2019w.csv
    Alemanha: 17,1% de chance de vencer
    Estados Unidos: 14,8% de chance de vencer
    Inglaterra: 14,0% de chance de vencer
    França: 9,2% de chance de vencer
    Canadá: 8,5% de chance de vencer
    Japão: 7,1% de chance de vencer
    Austrália: 6,8% de chance de vencer
    Países Baixos: 5,4% de chance de vencer
    Suécia: 3,9% de chance de vencer
    Itália: 3,0% de chance de vencer
    Noruega: 2,9% de chance de vencer
    Brasil: 2,9% de chance de vencer
    Espanha: 2,2% de chance de vencer
    China PR: 2,1% de chance de vencer
    Nigéria: 0,1% de chance de vencer
    

*   Você pode estar se perguntando o que aconteceu de verdade nas Copas do Mundo de 2018 e 2019. No campeonato masculino, a França ganhou, derrotando a Croácia na final. A Bélgica derrotou a Inglaterra para ficar em terceiro lugar. No campeonato feminino, os Estados Unidos ganharam, derrotando os Países Baixos na final. A Inglaterra derrotou a Suécia para ficar em terceiro lugar.

Número de simulações
---------------------

Depois de ter certeza de que seu código está correto, vamos brincar com o valor de `N`, constante no topo do arquivo, para ajustar o número de vezes que simulamos o torneio. Mais simulações de torneios nos darão previsões mais precisas (por quê?), mas ao custo de tempo.

Podemos cronometrar programas adicionando sua execução na linha de comando com `time`. Por exemplo, com `N` ajustado para 1000 (o padrão), execute

    time python tournament.py 2018m.csv
    

ou

    time python tournament.py 2019w.csv
    

o que deve produzir algo como

    real    0m0.037s
    user    0m0.028s
    sys     0m0.008s
    

embora seus próprios tempos possam variar.

Preste atenção na métrica **real**, que é o tempo total que `tournament.py` levou para ser executado. E observe que você recebe o tempo em minutos e segundos, com precisão de milésimos de segundo.

No arquivo `answers.txt`, acompanhe quanto tempo leva para `tournament.py` simular...

*   10 (dez) torneios
*   100 (cem) torneios
*   1000 (mil) torneios
*   10000 (dez mil) torneios
*   100000 (cem mil) torneios
*   1000000 (um milhão) de torneios

Cada vez que você ajustar `N`, registre o tempo **real** na tarefa correspondente em `answers.txt`, usando o mesmo formato `0m0.000s`. Depois de cronometrar cada cenário, responda às duas perguntas de acompanhamento, sobrescrevendo a tarefa fornecida:

*   Quais previsões, se houver, se mostraram incorretas à medida que você aumentou o número de simulações?
*   Suponha que você seja cobrado por cada segundo do tempo de computação que seu programa usa. Depois de quantas simulações você consideraria as previsões "suficientemente boas"?

<details><summary>Veja um arquivo <code>answers.txt</code> formatado corretamente</summary><div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Tempos:

10 simulações: 0m0.028s
100 simulações: 0m0.030s
1000 simulações: 0m0.041s
10000 simulações: 0m0.139s
100000 simulações: 0m1.031s
1000000 simulações: 0m11.961s

Perguntas:

Quais previsões, se houver, se mostraram incorretas à medida que você aumentou o número de simulações?:

Com um pequeno número de simulações...

Suponha que você seja cobrado por cada segundo do tempo de computação que seu programa usa. Depois de quantas simulações você consideraria as previsões "suficientemente boas"?:

Parece que as previsões se estabilizaram depois de cerca de...

</code></pre></div></div></details>

Como Testar Seu Código
---------------------

Execute o abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo você mesmo também!

    check50 cs50/labs/2023/x/worldcup
    
Execute o abaixo para avaliar o estilo do seu código usando `style50`.

    style50 tournament.py
    
Como Enviar

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/labs/2023/x/worldcup"

