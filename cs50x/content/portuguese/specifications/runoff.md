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

Começando
---------------

Faça login no [code.cs50.io] (https://code.cs50.io/), clique na janela do terminal e execute `cd` por si só. Você deve ver que o prompt da janela do terminal se parece com o abaixo:

    $
    

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/3/runoff.zip
    

para baixar um ZIP chamado `runoff.zip` em seu espaço de código.

Em seguida, execute

    unzip runoff.zip
    

para criar uma pasta chamada `runoff`. Você não precisa mais do arquivo ZIP, portanto, execute

    rm runoff.zip
    

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd runoff
    

seguido de Enter para se mover para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    runoff/ $
    

Se tudo ocorreu conforme o esperado, você deve executar

    ls
    

e ver um arquivo chamado `runoff.c`. A execução de `code runoff.c` deve abrir o arquivo onde você digitará seu código para este problema definido. Caso contrário, volte seus passos e veja se pode determinar onde saiu errado!

Entendendo
-------------

Vamos dar uma olhada em `runoff.c`. Estamos definindo duas constantes: `MAX_CANDIDATES` para o número máximo de candidatos na eleição e `MAX_VOTERS` para o número máximo de eleitores na eleição.

Em seguida, temos uma matriz bidimensional `preferences`. A matriz `preferences [i]` representará todas as preferências para o eleitor número `i` e o número inteiro `preferences [i] [j]` aqui armazenará o índice do candidato que é a j-ésima preferência para o eleitor 'i'.

Em seguida, temos uma `struct` chamada `candidate`. Cada `candidate` tem um campo de `string` para o seu `nome`, e um `int` representando o número de `votes` que eles têm no momento, e um valor `bool` chamado `eliminated` que indica se o candidato foi eliminado da eleição. A matriz `candidates` acompanhará todos os candidatos na eleição.

O programa também tem duas variáveis globais: `voter_count` e `candidate_count`.

Agora no `main`. Observe que, após determinar o número de candidatos e o número de eleitores, o loop de votação principal começa, dando a cada eleitor uma chance de votar. À medida que o eleitor insere suas preferências, a função `vote` é chamada para acompanhar todas as preferências. Se em algum momento a cédula for considerada inválida, o programa é encerrado.

Depois que todas as votos forem feitas, outro loop começa: este vai manter a repetição do processo de votação até que haja um vencedor, verificando o último candidato.

A primeira chamada aqui é para uma função chamada `tabulate`, que deve procurar todas as preferências dos eleitores e calcular os totais de votos atuais, verificando o candidato da escolha principal de cada eleitor que ainda não foi eliminado. Em seguida, a função `print_winner` deve imprimir o vencedor, se houver um; se houver, o programa acabou. Mas caso contrário, o programa precisa determinar o menor número de votos que qualquer pessoa ainda na eleição recebeu (por meio da chamada à função `find_min`). Se for descoberto que todas as pessoas na eleição empataram com o mesmo número de votos (como determinado pela função `is_tie`), a eleição é declarada um empate; caso contrário, o candidato (ou candidatos) em último lugar é eliminado da eleição por meio de uma chamada à função `eliminate`.

Se você olhar um pouco mais abaixo no arquivo, verá que essas funções - `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` e `eliminate` - ficam todas a seu cargo para serem concluídas!

Especificação
-------------

Complete a implementação do `runoff.c` de forma a simular uma eleição de segundo turno. Você deve completar as implementações das funções `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` e `eliminate`, e não deve modificar nada mais no `runoff.c` (e a inclusão de arquivos de cabeçalho adicionais, se desejar).

### `vote`

Complete a função `vote`.

*   A função recebe como argumentos `voter`, `rank` e `name`. Se `name` for uma correspondência com o nome de um candidato válido, você deve atualizar a matriz global de preferências para indicar que o eleitor `voter` tem aquele candidato como sua preferência de `rank` (onde `0` é a primeira preferência, `1` é a segunda preferência, e assim por diante).
*   Se a preferência for registrada com sucesso, a função deve retornar `true`; caso contrário, a função deve retornar `false` (se, por exemplo, `nome` não é o nome de um dos candidatos).
*   Você pode assumir que nenhum dois candidatos terá o mesmo nome.


<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">candidate_count</code> armazena o número de candidatos na eleição.</li>
  <li data-marker="*">Lembre-se de que você pode usar <a href="https://man.cs50.io/3/strcmp"><code class="language-plaintext highlighter-rouge">strcmp</code></a> para comparar duas strings.</li>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">preferences[i][j]</code> armazena o índice do candidato que é a preferência classificada como <code class="language-plaintext highlighter-rouge">j</code> para o eleitor <code class="language-plaintext highlighter-rouge">i</code>.</li>
</ul></details>

### `tabulate`

Complete a função `tabulate`.

*   A função deve atualizar o número de `votes` que cada candidato tem nesta fase da eleição.
*   Lembre-se de que, em cada fase da eleição, cada eleitor vota efetivamente no candidato de sua preferência que ainda não foi eliminado.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">voter_count</code> armazena o número de eleitores na eleição e que, para cada eleitor em nossa eleição, queremos contar uma cédula.</li>
  <li data-marker="*">Lembre-se de que, para um eleitor <code class="language-plaintext highlighter-rouge">i</code>, seu candidato de primeira escolha é representado por <code class="language-plaintext highlighter-rouge">preferences[i][0]</code>, seu candidato de segunda escolha por <code class="language-plaintext highlighter-rouge">preferences[i][1]</code>, etc.</li>
  <li data-marker="*">Lembre-se de que a <code class="language-plaintext highlighter-rouge">struct</code> <code class="language-plaintext highlighter-rouge">candidate</code> tem um campo chamado <code class="language-plaintext highlighter-rouge">eliminated</code>, que será <code class="language-plaintext highlighter-rouge">true</code> se o candidato foi eliminado da eleição.</li>
  <li data-marker="*">Lembre-se de que a <code class="language-plaintext highlighter-rouge">struct</code> <code class="language-plaintext highlighter-rouge">candidate</code> tem um campo chamado <code class="language-plaintext highlighter-rouge">votes</code>, que você provavelmente desejará atualizar para o candidato preferido de cada eleitor.</li>
  <li data-marker="*">Depois que você votou no primeiro candidato não eliminado de um eleitor, desejará parar ali, não continuar em sua cédula! Lembre-se de que você pode sair de um loop mais cedo usando <code class="language-plaintext highlighter-rouge">break</code> dentro de uma condicional.</li>
</ul></details>

### `print_winner`

Complete a função `print_winner`.

*   Se algum candidato tiver mais da metade dos votos, seu nome deve ser impresso e a função deve retornar `true`.
*   Se ninguém ganhou a eleição ainda, a função deve retornar `false`.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">voter_count</code> armazena o número de eleitores na eleição. Dado isso, como você expressaria o número de votos necessários para vencer a eleição?</li>
</ul></details>

### `find_min`

Complete a função `find_min`.

*   A função deve retornar o total mínimo de votos para qualquer candidato que ainda esteja na eleição.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Provavelmente, você desejará percorrer os candidatos para encontrar aquele que ainda está na eleição e tem o menor número de votos. Que informações você deve controlar enquanto percorre os candidatos?</li>
</ul></details>

### `is_tie`

Complete a função `is_tie`.

*   A função leva um argumento `min`, que será o número mínimo de votos que alguém na eleição atualmente tem.
*   A função deve retornar `true` se todo candidato que ainda está na eleição tiver o mesmo número de votos e deve retornar `false` caso contrário.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que uma gravata acontece se todo candidato ainda na eleição tiver o mesmo número de votos. Repare também que a função <code class="language-plaintext highlighter-rouge">is_tie</code> pega um argumento <code class="language-plaintext highlighter-rouge">min</code>, que é o menor número de votos que qualquer candidato tem atualmente. Como você pode usar essa informação para determinar se a eleição é uma gravata (ou, inversamente, não é uma gravata)?</li>
</ul></details>

### `eliminate`

Complete a função `eliminate`.

*   A função leva um argumento `min`, que será o número mínimo de votos que alguém na eleição atualmente tem.
*   A função deve eliminar o candidato (ou candidatos) que tem `min` número de votos.

Passo a passo
------------

<div class="ratio ratio-16x9" data-video=""><iframe allow="acelerômetro; autoplay; encrypted-media; giroscópio; imagem em imagem" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Uso
---

Seu programa deve se comportar como no exemplo abaixo:

    ./runoff Alice Bob Charlie
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
    
    Alice
    

Teste
-----

Certifique-se de testar seu código para verificar se ele lida com ...

*   Uma eleição com qualquer número de candidatos (até o `MAX` de `9`)
*   Votando em um candidato pelo nome
*   Votos inválidos para candidatos que não estão na cédula
*   Imprimir o vencedor da eleição se houver apenas um
*   Não eliminar ninguém no caso de um empate entre todos os candidatos restantes

Execute o seguinte para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testá-lo por si mesmo também!

    check50 cs50/problems/2023/x/runoff
    

Execute o abaixo para avaliar o estilo do seu código usando `style50`.

    style50 runoff.c
    

Como Enviar
-----------

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/runoff

