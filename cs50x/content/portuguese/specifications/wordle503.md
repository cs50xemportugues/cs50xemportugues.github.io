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