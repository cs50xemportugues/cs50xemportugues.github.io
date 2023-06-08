# Mario

## Começando

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e, em seguida, execute `cd` sozinho. Você deve ver que o "prompt" se parece com o abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-less.zip

seguido de Enter para baixar um arquivo ZIP chamado `mario-less.zip` em seu espaço de código. Tome cuidado para não ignorar o espaço entre "wget" e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip mario-less.zip

para criar uma pasta chamada `mario-less`. Você não precisa mais do arquivo ZIP, então execute

    rm mario-less.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd mario-less

seguido de Enter para entrar nesse diretório. O seu prompt agora deve se parecer com o abaixo.

    mario-less/ $

Se tudo correu bem, você deve digitar

    ls

e ver um arquivo chamado "mario.c". Ao executar "code mario.c", o arquivo deverá ser aberto para que você possa digitar seu código para este problema. Caso contrário, refaça seus passos e veja se consegue determinar onde você errou!

## World 1-1

No final do World 1-1 do jogo Super Mario Brothers da Nintendo, Mario deve subir uma pirâmide alinhada à direita, como mostrado abaixo.

![captura de tela de Mario subindo uma pirâmide alinhada à direita](https://cs50.harvard.edu/x/2023/psets/1/mario/less/pyramid.png)

Vamos recriar aquela pirâmide em C, embora em texto, usando hashtags (`#`) para representar tijolos, como mostrado abaixo. Cada hashtag é um pouco mais alta do que é larga, então a própria pirâmide também será mais alta do que é larga.

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

O programa que escreveremos será chamado de `mario`. E vamos permitir que o usuário decida qual deve ser a altura da pirâmide, solicitando inicialmente um número inteiro positivo entre, digamos, 1 e 8, inclusive.

Veja como o programa pode funcionar se o usuário informar `8` quando solicitado:

    $ ./mario
    Altura: 8
           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Veja como o programa pode funcionar se o usuário informar `4` quando solicitado:

    $ ./mario
    Altura: 4
       #
      ##
     ###
    ####

Veja como o programa pode funcionar se o usuário informar `2` quando solicitado:

    $ ./mario
    Altura: 2
     #
    ##

E veja como o programa pode funcionar se o usuário informar `1` quando solicitado:

    $ ./mario
    Altura: 1
    #

Se o usuário não informar um número inteiro positivo entre 1 e 8, inclusive, quando solicitado, o programa deverá solicitar novamente até que o usuário colabore:

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
       #
      ##
     ###
    ####

Como começar? Vamos abordar este problema um passo de cada vez.

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Pseudocódigo

Primeiramente, execute o comando

    cd

para garantir que você esteja no diretório padrão do seu codespace.

Em seguida, execute o comando

    cd mario-less

para mudar para o diretório `mario-less`.

Depois, execute o comando

    code pseudocode.txt

para abrir o arquivo `pseudocode.txt` dentro desse diretório.

No arquivo `pseudocode.txt`, escreva um pseudocódigo que implemente este programa, mesmo que você não saiba ainda como escrevê-lo em código. Não há apenas uma maneira certa de escrever pseudocódigo, mas frases curtas em inglês são suficientes. Lembre-se de como escrevemos [pseudocódigo para encontrar alguém em uma lista telefônica](https://docs.google.com/presentation/d/1X3AMSenwZGSE6WxGpzoALAfMg2hmh1LYIJp3N2a1EYI/edit#slide=id.g41907da2bc_0_265). É provável que seu pseudocódigo use (ou implique o uso de!) uma ou mais funções, condicionais, expressões booleanas, loops e/ou variáveis.

<details><summary>Dica</summary><p>Há mais de uma maneira de fazer isso, então aqui está apenas uma!</p>

<ol>
  <li>Pergunte ao usuário a altura desejada</li>
  <li>Se a altura for menor que 1 ou maior que 8 (ou não for um número inteiro), volte para a etapa anterior</li>
  <li>Itere de 1 a altura:
    <ol>
      <li>Sobre a iteração <em>i</em>, imprima <em>i</em> símbolos de hashtag e, em seguida, uma nova linha</li>
    </ol>
  </li>
</ol>

<p>Tudo bem editar o seu próprio pseudocódigo depois de ver este exemplo aqui, mas não simplesmente copie e cole o nosso no seu!</p></details>

## Solicitando entrada

Independentemente do pseudocódigo, vamos primeiro escrever apenas o código C que solicita (e re-solicita, se necessário) a entrada do usuário. Abra o arquivo chamado `mario.c` dentro do diretório `mario`. (Lembre-se como fazê-lo?)

Agora, modifique `mario.c` de forma que solicite a altura da pirâmide ao usuário, armazenando a entrada em uma variável, solicitando novamente a entrada do usuário, quantas vezes for necessário, se a entrada não for um número inteiro positivo entre 1 e 8, inclusive. Em seguida, basta imprimir o valor dessa variável, confirmando assim que você de fato armazenou com sucesso a entrada do usuário, como abaixo.

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
    Armazenado: 4

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que você pode compilar seu programa com <code class="language-plaintext highlighter-rouge">make</code>.</li>
  <li data-marker="*">Lembre-se de que você pode imprimir um <code class="language-plaintext highlighter-rouge">int</code> com <code class="language-plaintext highlighter-rouge">printf</code> usando <code class="language-plaintext highlighter-rouge">%i</code>.</li>
  <li data-marker="*">Lembre-se de que você pode obter um número inteiro do usuário com <code class="language-plaintext highlighter-rouge">get_int</code>.</li>
  <li data-marker="*">Lembre-se de que o <code class="language-plaintext highlighter-rouge">get_int</code> é declarado em <code class="language-plaintext highlighter-rouge">cs50.h</code>.</li>
  <li data-marker="*">Lembre-se de que solicitamos um número inteiro positivo ao usuário em aula usando um loop <code class="language-plaintext highlighter-rouge">do while</code> em <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight"><code class="language-plaintext highlighter-rouge">mario.c</code></a>.</li>
</ul></details>

## Construindo o Contrário

Agora que seu programa está (esperançosamente!) aceitando a entrada como prescrita, é hora de dar outro passo.

Acontece que é um pouco mais fácil construir uma pirâmide alinhada à esquerda do que à direita, como abaixo.

    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########

Então, vamos construir uma pirâmide alinhada à esquerda primeiro e, depois que funcionar, alinhá-la à direita!

Modifique o arquivo `mario.c` de forma que não imprima mais a entrada do usuário, mas em vez disso imprima uma pirâmide de altura alinhada à esquerda.

<details>
  <summary>Dicas</summary>
  <ul>
    <li data-marker="*">Lembre-se de que um hash é apenas um caractere como qualquer outro, portanto, você pode imprimi-lo com <code class="language-plaintext highlighter-rouge">printf</code>.</li>
    <li data-marker="*">Assim como o Scratch tem um bloco <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">repeat</code></a>, o C também tem um loop <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">for</code></a>, por meio do qual você pode iterar algumas vezes. Talvez em cada iteração, <em>i</em>, você pudesse imprimir tantos hashes?</li>
    <li data-marker="*">
      <p>Na verdade, você pode “aninhar” loops, iterando com uma variável (por exemplo, <code class="language-plaintext highlighter-rouge">i</code>) no loop "externo" e outra (por exemplo, <code class="language-plaintext highlighter-rouge">j</code>) no loop "interno". Por exemplo, aqui está como você pode imprimir um quadrado de altura e largura <code class="language-plaintext highlighter-rouge">n</code>, abaixo. Claro, não é um quadrado que você deseja imprimir!</p>

      <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  for (int i = 0; i &lt; n; i++)

      {
      for (int j = 0; j &lt; n; j++)
        {
          printf("#");
        }
        printf("\n");
      }
      </code></pre></div> </div>

</li>
  </ul>
</details>

## Alinhando à Direita com Pontos

Agora vamos alinhar à direita essa pirâmide empurrando seus hashes para a direita, prefixando-os com pontos (ou seja, períodos), como abaixo.

    .......#
    ......##
    .....###
    ....####
    ...#####
    ..######
    .#######
    ########

Modifique `mario.c` de forma que ele faça exatamente isso!

<details><summary>Dica</summary><p>Observe como o número de pontos necessários em cada linha é o “oposto” do número de hashes daquela linha. Para uma pirâmide de altura 8, como a acima, a primeira linha tem apenas 1 hash e, portanto, 7 pontos. Enquanto isso, a linha inferior tem 8 hashes e assim 0 pontos. Através de que fórmula (ou aritmética, realmente) você poderia imprimir tantos pontos?</p></details>

### Como Testar seu Código

O seu código funciona conforme prescrito quando você insere:

- `-1` (ou outros números negativos)?
- `0`?
- De `1` a `8`?
- `9` ou outros números positivos?
- letras ou palavras?
- nenhuma entrada, quando você só pressiona Enter?

## Removendo os Pontos

Tudo o que resta agora é um acabamento! Modifique `mario.c` de tal maneira que ele imprima espaços em vez desses pontos!

### Como Testar seu Código

Execute o abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo também!

    check50 cs50/problems/2023/x/mario/less

Execute o abaixo para avaliar o estilo do seu código usando `style50`.

    style50 mario.c

<details><summary>Dica</summary><p>Um espaço é apenas uma tecla pressionada em sua barra de espaço, assim como um ponto é apenas uma tecla pressionada em sua tecla! Mas lembre-se de que <code class="language-plaintext highlighter-rouge">printf</code> requer que você envolva as duas com aspas duplas!</p></details>

## Como Enviar

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/mario/less
"

