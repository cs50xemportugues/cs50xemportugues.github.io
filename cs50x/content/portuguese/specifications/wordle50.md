<style>.wrong { background-color: red } .right { background-color: green; } .close_ { background-color: yellow; }</style>

Wordle50
========

Para este problema, você implementará um programa que se comporta de maneira semelhante ao popular jogo de palavras diário [Wordle](https://www.nytimes.com/games/wordle/index.html).

<pre><code> $ ./wordle 5
<span class="right">Isto é Wordle50</span>
Você tem 6 tentativas para adivinhar a palavra de 5 letras que estou pensando
Digite uma palavra de 5 letras: crash
Palpite 1: <span class="close_">c</span><span class="wrong">ra</span><span class="close_">s</span><span class="wrong">h</span>
Digite uma palavra de 5 letras: scone
Palpite 2: <span class="right">s</span><span class="close_">c</span><span class="wrong">o</span><span class="close_">n</span><span class="right">e</span>
Digite uma palavra de 5 letras: since
Palpite 3: <span class="right">since</span>
Você ganhou!
</code></pre>


Começando
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da sua janela do terminal, execute  `cd` sozinho. Você deve ver o "prompt" dela abaixo.

    $
    

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/psets/2/wordle.zip
    

seguido de Enter para baixar um ZIP chamado `wordle.zip` no seu espaço de código. Tome cuidado para não deixar passar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip wordle.zip
    

para criar uma pasta chamada `wordle`. Você não precisa mais do arquivo ZIP, então execute

    rm wordle.zip
    

e responda com "y" e Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd wordle
    

seguido de Enter para se mover para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve ser semelhante ao abaixo.

    wordle/ $
    

Se tudo tiver sido bem sucedido, você deve executar

    ls
    

e ver um arquivo chamado `wordle.c`, bem como `5.txt`, `6.txt`, `7.txt` e `8.txt`. Executar `code wordle.c` deverá abrir o arquivo onde você digitará seu código para este problema. Caso não tenha sucesso, volte seus passos e veja se consegue determinar onde você errou! Se você tentar compilar o jogo agora, fará sem erros, mas quando você tentar executá-lo, verá esta mensagem de erro:

    Error opening file 0.txt.
    

No entanto, isso é normal, pois você ainda não implementou parte do código necessário para fazer essa mensagem de erro desaparecer!

Background
----------

É provável que, se você for um usuário do Facebook, pelo menos um dos seus amigos tenha postado algo parecido com isso, especialmente no início de 2022, quando era a grande tendência:

![Wordle results](https://cs50.harvard.edu/x/2023/psets/2/wordle50/wordle.png)

Se sim, seu amigo jogou Wordle e está compartilhando seus resultados daquele dia! Todos os dias, uma nova "palavra secreta" é escolhida (a mesma para todos) e o objetivo é adivinhar qual a palavra secreta em seis tentativas. Felizmente, dado que há mais de seis palavras de cinco letras na língua inglesa, você pode ter algumas dicas ao longo do caminho, e a imagem acima, na verdade, mostra a progressão do seu amigo por suas suposições, usando essas dicas para tentar chegar a palavra correta. Usando um esquema semelhante ao jogo [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)), se depois de você adivinhar aquela letra, ela ficar verde, isso significa não só que aquela letra está na palavra secreta daquele dia, mas também na posição correta. Se ficar amarelo, significa que a letra adivinhada aparece _em algum lugar_ na palavra, mas não naquele local específico. Letras que ficam cinzas não estão na palavra e podem ser omitidas em tentativas futuras.

Vamos terminar de escrever um programa chamado "wordle" que nos permita recriar este jogo e jogá-lo no nosso terminal. Faremos algumas pequenas mudanças no jogo (por exemplo, a maneira como ele lida com uma letra aparecendo duas vezes em uma palavra não é a mesma que o jogo real lida com isso), mas para simplificar, iremos usar texto vermelho ao invés de cinza claro para indicar as letras que não estão na palavra em absoluto. No momento em que o usuário executar o programa, eles devem decidir, fornecendo um argumento de linha de comando, qual é o comprimento da palavra que eles querem adivinhar, entre 5 e 8 letras.

Aqui estão alguns exemplos de como o programa deve funcionar. Se o usuário omitir um argumento de linha de comando inteiramente:

  $ ./wordle
  Uso: ./wordle tamanho_da_palavra

Se o usuário fornecer um argumento de linha de comando, mas não estiver na faixa correta:

  $ ./wordle 4
  Erro: o tamanho da palavra deve ser de 5, 6, 7 ou 8

Veja como o programa pode ser utilizado quando o usuário escolhe 5:

  $ ./wordle 5
  This is WORDLE50
  Você tem 6 tentativas para adivinhar a palavra de 5 letras que estou pensando
  Insira uma palavra de 5 letras:

Nesse ponto, o usuário deve digitar uma palavra de 5 letras. Claro, o usuário pode ser teimoso, e devemos garantir que eles estejam seguindo as regras:

    
<pre><code>$ ./wordle 5
<span class="right">This is WORDLE50</span>
Você tem 6 tentativas para adivinhar a palavra de 5 letras que estou pensando
Insira uma palavra de 5 letras: wordle
Insira uma palavra de 5 letras: computer
Insira uma palavra de 5 letras: okay
Insira uma palavra de 5 letras: games
Tentativa 1: <span class="wrong">g</span><span class="close_">a</span><span class="wrong">m</span><span class="close_">e</span><span class="wrong">s</span>
Insira uma palavra de 5 letras:
</code></pre>
    

Observe que não contamos nenhuma dessas tentativas inválidas como tentativas. Mas assim que eles fizeram uma tentativa legítima, a contamos como uma tentativa e informamos o status da palavra. Parece que o usuário tem algumas pistas agora; eles sabem que a palavra contém um `a` e um `e` em algum lugar, mas não nos pontos exatos em que aparecem na palavra `games`. E eles sabem que `g`, `m` e `s` não aparecem na palavra em nenhum lugar, então as tentativas futuras podem omiti-los. Talvez eles tentem, digamos, `heart` a seguir! ❤️

Especificação
-------------

Projete e implemente um programa, `wordle`, que conclui a implementação do nosso clone do jogo Wordle50. Você vai notar que algumas das principais partes deste programa já foram escritas para você - você não pode modificar nenhuma dessas partes do programa. Em vez disso, seu trabalho deve ser limitado aos sete TODOS que deixamos para você preencher. Cada um desses itens resolve um problema específico e recomendamos que você os aborde na ordem de 1 a 7. Cada TODO numerado corresponde ao mesmo item na lista abaixo.

1. No primeiro TODO, você deve garantir que o programa aceite um único argumento de linha de comando. Vamos chamá-lo de `k` para discutir. Se o programa não foi executado com um único argumento de linha de comando, você deve imprimir a mensagem de erro como demonstramos acima e retornar 1, encerrando o programa.
2. No segundo TODO, você deve garantir que `k` seja um dos valores aceitáveis (5, 6, 7 ou 8), e armazenar esse valor em `wordsize`; precisaremos fazer uso disso mais tarde. Se o valor de `k` não for um desses quatro valores exatamente, você deve imprimir a mensagem de erro como demonstramos acima e retornar 1, encerrando o programa.

Depois disso, a equipe já escreveu algum código que percorrerá e abrirá a lista de palavras para o comprimento da palavra que o usuário deseja adivinhar e selecionará aleatoriamente uma das 1000 opções disponíveis. Não se preocupe necessariamente em entender todo esse código, pois não é importante para este trabalho. Veremos algo semelhante em uma tarefa posterior, e isso fará muito mais sentido depois! Este é um bom lugar para parar e testar, antes de prosseguir para o próximo TODO, que seu código se comporta como esperado. É sempre mais fácil depurar programas se você fizer isso metodicamente!

3. No terceiro TODO, você deve ajudar a defender os usuários teimosos garantindo que seu palpite seja do comprimento correto. Para isso, dedicaremos nossa atenção à função `get_guess`, que você precisará implementar completamente. Um usuário deve ser solicitado (como via `get_string`) a digitar uma palavra com `k` letras (lembre-se de que esse valor é passado como parâmetro para `get_guess`) e, se fornecerem um palpite do comprimento errado, eles devem ser solicitados novamente (como em [Mario](../../1/mario/less/)) até que forneçam exatamente o valor que você espera deles. Atualmente, o código de distribuição não faz isso, então você terá que corrigi-lo! Observe que, ao contrário do Wordle real, nós na verdade não verificamos se o palpite do usuário é uma palavra real, então nesse sentido o jogo é talvez um pouco mais fácil. Todos os palpites neste jogo devem estar em caracteres **minúsculos** e é aceitável supor que o usuário não será tão teimoso a ponto de fornecer algo diferente de caracteres minúsculos ao fazer um palpite. Depois que um palpite legítimo for obtido, ele poderá ser `retornado`.
4. Em seguida, no quarto TODO, precisamos acompanhar a "pontuação" do usuário no jogo. Fazemos isso tanto em uma base por letra - atribuindo uma pontuação de 2 (que definimos como `EXACT`) para uma letra no lugar correto, 1 (que definimos como `CLOSE`) para uma letra que está na palavra, mas no lugar errado, ou 0 (que definimos como`WRONG`), e uma base por palavra, para nos ajudar a detectar quando potencialmente acionamos o final do jogo vencendo. Usaremos as pontuações de letra individuais quando codificarmos as cores de impressão. Para armazenar essas pontuações, precisamos de uma matriz, que chamamos de `status`. No início do jogo, sem nenhum palpite tendo sido feito, ele deve conter todos os 0s.

Este é outro bom lugar para parar e testar seu código, especialmente no que diz respeito ao item 3, acima! Você notará que, a esse ponto, quando finalmente inserir um palpite legítimo (ou seja, aquele com o comprimento correto), seu programa provavelmente ficará parecido com o abaixo:

    Input a 5-letter word: computer
    Input a 5-letter word: games
    Guess 1:
    Input a 5-letter word:

Isso é normal, no entanto! Implementar `print_word` é o TODO número 6, então não devemos esperar que o programa processe esse palpite neste momento. Claro, você sempre pode adicionar chamadas adicionais de `printf` (apenas certifique-se de removê-las antes de enviar) como parte de sua estratégia de depuração!

5. O quinto TODO é definitivamente o maior e provavelmente o mais desafiador. Dentro da função `check_word`, cabe a você comparar cada uma das letras do `palpite` com cada uma das letras da `escolha` (que, lembre-se, é a "palavra secreta" para este jogo) e atribuir pontuações. Se as letras corresponderem, atribua 2 pontos `EXACT` e `break` no loop - não há necessidade de continuar o loop se você já determinou que a letra está no lugar certo. Tecnicamente, se essa letra aparecer na palavra duas vezes, isso poderá resultar em um pequeno erro, mas corrigir esse erro sobrecarrega um pouco mais esse problema do que queremos agora, por isso vamos aceitar isso como uma característica da nossa versão! Se você descobrir que a letra está na palavra, mas não está no lugar certo, pontue 1 ponto como `CLOSE`, mas não `break`! Afinal, aquela letra pode aparecer mais tarde no lugar certo na palavra `escolha` e, se `break`mos cedo demais, o usuário nunca saberia disso! Você não precisa definir explicitamente os pontos `WRONG` (0) aqui, pois você lidou com isso no Step 4. Por fim, você também deve estar somando a pontuação total da palavra quando a souber, porque é isso que essa função deve retornar. Novamente, não tenha medo de usar `debug50` e / ou `printf`s conforme necessário para ajudá-lo a descobrir quais são os valores de diferentes variáveis neste ponto - até implementar `print_word`, abaixo, o programa não oferecerá muito em termos de um checkpoint visual!

6. No sexto TODO, você concluirá a implementação de `print_word`. Essa função deve verificar os valores com os quais você preencheu a matriz `status` e imprimir, letra por letra, cada letra do `palpite` com o código de cor correto. Você pode ter notado algumas (assustadoras!) definições `#define` no topo do arquivo onde fornecemos uma maneira mais simples de representar o que é chamado de um [código de cor ANSI] (https://en.wikipedia.org/wiki/ANSI_escape_code#Colors), que é basicamente um comando para alterar a cor da fonte do terminal. Você não precisa se preocupar com como implementar esses quatro valores (`GREEN`,` YELLOW`, `RED` e `RESET`, este último simplesmente retorna à fonte padrão do terminal) ou exatamente o que eles significam; em vez disso, você pode apenas usá-los (o poder da abstração!). Observe também que fornecemos um exemplo no código de distribuição onde imprimimos algum texto verde e depois redefinimos a cor, como parte da introdução do jogo. Consequentemente, você deve se sentir à vontade para usar a linha de código abaixo para se inspirar em como você pode tentar alternar as cores:

```
printf(GREEN"Este é o WORDLE50"RESET"\n");
```

Claro, ao contrário do nosso exemplo, você provavelmente não quer imprimir uma nova linha após cada caractere da palavra (em vez disso, você quer apenas uma nova linha no final, também redefinindo a cor da fonte!), Caso contrário, pode acabar parecendo o abaixo:

    
<pre><code>
Input a 5-letter word: games
Guess 1: <span class="wrong">g</span>
<span class="close_">a</span>
<span class="wrong">m</span>
<span class="close_">e</span>
<span class="wrong">s</span>
Input a 5-letter word:
</code></pre>
    

7. Por último, o sétimo TODO é apenas uma pequena limpeza antes que o programa termine. Se o loop principal tiver terminado normalmente, porque o usuário ficou sem palpites, ou porque saímos dele por ter conseguido acertar a palavra exatamente, é hora de informar o usuário sobre o resultado do jogo. Se o usuário ganhar o jogo, um simples `Você ganhou!` é suficiente para imprimir aqui. Caso contrário, você deve imprimir uma mensagem informando ao usuário qual era a palavra-alvo, para que saibam que o jogo estava sendo honesto com eles (e para que você tenha um meio de depurar se olhar para trás e perceber que o seu código estava fornecendo pistas inadequadas ao longo do caminho!)".

Como Testar Seu Código
---------------------

Execute o código abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo você mesmo!

    check50 cs50/problems/2023/x/wordle
    

Execute o código abaixo para avaliar o estilo do seu código usando `style50`.

    style50 wordle.c
    

Como Enviar
-------------

No seu terminal, execute o código abaixo para submeter seu trabalho.

    submit50 cs50/problems/2023/x/wordle"

