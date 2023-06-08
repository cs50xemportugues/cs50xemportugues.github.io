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