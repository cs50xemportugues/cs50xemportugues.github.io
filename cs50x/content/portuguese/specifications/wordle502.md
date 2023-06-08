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