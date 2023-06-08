# Cifra de César

Para este problema, você implementará um programa que criptografa mensagens usando a cifra de César conforme abaixo.

   $./caesar 13
    plaintext:  HELLO
    ciphertext: URYYB
    

## Como começar

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e execute `cd` sozinho. Você deve encontrar que seu "prompt" se parece com o abaixo.

    $

Clique dentro dessa janela do terminal e, em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/2/caesar.zip

seguido de Enter para baixar um arquivo ZIP chamado `caesar.zip` em seu codespace. Tome cuidado para não esquecer o espaço entre `wget` e o URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip caesar.zip

para criar uma pasta chamada `caesar`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm caesar.zip

e responder com "y" seguido de Enter na solicitação para remover o arquivo ZIP baixado.

Agora digite

    cd caesar

seguido de Enter para entrar (ou seja, abrir) nesse diretório. O prompt agora deve se parecer com o abaixo.

    caesar/ $

Se tudo correu bem, você deve executar

    ls

e verá um arquivo chamado `caesar.c`. Executar `code caesar.c` deve abrir o arquivo em que você digitara o código para este conjunto de problemas. Se não, volte seus passos e veja se você pode determinar onde você errou!## Antecedentes

Supostamente, César (sim, aquele mesmo) costumava "criptografar" (ou seja, ocultar de forma reversível) mensagens confidenciais deslocando cada letra por uma determinada quantidade de posições. Por exemplo, ele poderia escrever A como B, B como C, C como D, ..., e, contornando o alfabeto, Z como A. E assim, para dizer HELLO para alguém, César poderia escrever IFMMP em vez disso. Ao receber tais mensagens de César, os destinatários teriam que "descriptografá-las" deslocando as letras na direção oposta pelo mesmo número de posições.

A segurança desse "criptossistema" dependia apenas de César e dos destinatários conhecerem um segredo, o número de posições pelas quais César havia deslocado suas letras (por exemplo, 1). Não particularmente seguro segundo os padrões modernos, mas, ei, se você é talvez o primeiro do mundo a fazê-lo, é bastante seguro!

O texto não criptografado é geralmente chamado de _plaintext_. O texto criptografado é geralmente chamado de _ciphertext_. E a chave usada é chamada de _key_.

Para deixar claro, aqui está como a criptografia da palavra `HELLO` com uma chave de `1` gera `IFMMP`:

<table>
  <thead>
    <tr>
      <th>plaintext</th>
      <th><code class="language-plaintext highlighter-rouge">H</code></th>
      <th><code class="language-plaintext highlighter-rouge">E</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">O</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+ key</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>= ciphertext</td>
      <td><code class="language-plaintext highlighter-rouge">I</code></td>
      <td><code class="language-plaintext highlighter-rouge">F</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">P</code></td>
    </tr>
  </tbody>
</table>

Mais formalmente, o algoritmo de César (ou seja, cifra) criptografa mensagens "rotacionando" cada letra por `k` posições. Mais formalmente, se `p` é um plaintext (ou seja, uma mensagem não criptografada), <code>p<sub>i</sub></code> é o <code>i<sup>th</sup></code> caractere em `p`, e `k` é uma chave secreta (ou seja, um número inteiro não negativo), então cada letra, <code>c<sub>i</sub></code>, no cipher, `c`, é calculada como

<code>c<sub>i</sub> = (p<sub>i</sub> + k) % 26</code>

em que `% 26` aqui significa "o resto da divisão por 26". Essa fórmula talvez faça a cifra parecer mais complicada do que realmente é, mas é realmente apenas uma maneira concisa de expressar o algoritmo com precisão. De fato, para fins de discussão, pense em A (ou a) como `0`, B (ou b) como `1`, ..., H (ou h) como `7`, I (ou i) como `8`, ..., e Z (ou z) como `25`. Suponha que César só queira dizer `Hi` para alguém confidencialmente usando, desta vez, uma chave, `k`, de 3. E assim, seu plaintext, `p`, é `Hi`, nesse caso, o primeiro caractere no plaintext, <code>p<sub>0</sub></code>, é `H` (também conhecido como 7), e o segundo caractere no plaintext, <code>p<sub>1</sub></code>, é `i` (também conhecido como 8). O primeiro caractere no ciphertext, <code>c<sub>0</sub></code>, é assim `K`, e o segundo caractere no ciphertext, <code>c<sub>i</sub></code>, é assim `L`. Faz sentido?

Vamos escrever um programa chamado `caesar` que permite criptografar mensagens usando a cifra de César. No momento em que o usuário executa o programa, eles devem decidir, fornecendo um argumento de linha de comando, qual será a chave na mensagem secreta que eles fornecerão em tempo de execução. Não devemos assumir necessariamente que a chave do usuário será um número; embora você possa assumir que, se for um número, será um inteiro positivo.

Aqui estão alguns exemplos de como o programa pode funcionar. Por exemplo, se o usuário inserir uma chave de `1` e um plaintext de `HELLO`:

    $ ./caesar 1
    plaintext:  HELLO
    ciphertext: IFMMP

Veja como o programa pode funcionar se o usuário fornecer uma chave de `13` e um plaintext de `hello, world`:

    $ ./caesar 13
    plaintext:  hello, world
    ciphertext: uryyb, jbeyq

Observe que nem a vírgula nem o espaço foram "deslocados" pelo cifra. Apenas os caracteres alfabéticos são rotacionados!

E mais um? Veja como o programa pode funcionar se o usuário fornecer uma chave de `13` novamente, com um plaintext mais complexo:

     $ ./caesar 13
     plaintext:  be sure to drink your Ovaltine
     ciphertext: or fher gb qevax lbhe Binygvar

<details><summary>Por que?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9K4FsAHB-C8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

Observe que a grafia da mensagem original foi preservada. As letras minúsculas permanecem minúsculas e as maiúsculas permanecem maiúsculas.

E se um usuário não cooperar, fornecendo um argumento de linha de comando que não é um número? O programa deve lembrar o usuário como usar o programa:

    $ ./caesar HELLO
    Uso: ./caesar chave

Ou realmente não cooperar, não fornecendo nenhum argumento de linha de comando? O programa deve lembrar o usuário como usar o programa:

    $ ./caesar
    Uso: ./caesar chave

Ou realmente, realmente não cooperar, fornecendo mais de um argumento de linha de comando? O programa deve lembrar o usuário como usar o programa:

    $ ./caesar 1 2 3
    Uso: ./caesar chave

<details><summary>Assista uma Gravação</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script></details>## Especificação

Projete e implemente um programa, `caesar`, que criptografa mensagens usando o cifra de César.

- Implemente seu programa em um arquivo chamado `caesar.c` em um diretório chamado `caesar`.
- Seu programa deve aceitar um único argumento de linha de comando, um inteiro não negativo. Vamos chamá-lo de `k` para fins de discussão.
- Se o seu programa for executado sem nenhum argumento de linha de comando ou com mais de um, seu programa deve imprimir uma mensagem de erro de sua escolha (com `printf`) e retornar de `main` um valor de `1` (que tende a significar um erro) imediatamente.
- Se qualquer um dos caracteres do argumento da linha de comando não for um dígito decimal, seu programa deve imprimir a mensagem `Usage: ./caesar key` e retornar de `main` um valor de `1`.
- Não assuma que `k` será menor ou igual a 26. Seu programa deve funcionar para todos os valores integrais não negativos de `k` menores que <code>2<sup>31</sup> - 26</code>. Em outras palavras, não é necessário se preocupar se o programa eventualmente quebrará se o usuário escolher um valor para `k` que seja grande demais ou quase grande demais para caber em um `int`. (Lembre-se de que um `int` pode estourar.) Mas, mesmo que `k` seja maior que 26, caracteres alfabéticos na entrada do seu programa devem permanecer caracteres alfabéticos na saída do seu programa. Por exemplo, se `k` for `27`, `A` não deve se tornar `\` mesmo que `\` esteja `27` posições distante de `A` em ASCII, de acordo com [asciitable.com](https://www.asciitable.com/); `A` deve se tornar `B`, já que `B` está `27` posições distante de `A`, desde que você retorne ao `Z` indo para `A`.
- Seu programa deve exibir `plaintext:` (com dois espaços, mas sem uma nova linha) e, em seguida, solicitar ao usuário uma `string` de texto simples (usando `get_string`).
- Seu programa deve exibir `ciphertext:` (com um espaço, mas sem uma nova linha), seguida do texto cifrado correspondente ao texto simples, com cada caractere alfabético do texto simples "rotacionado" por _k_ posições; caracteres não alfabéticos devem ser exibidos sem alteração.
- Seu programa deve preservar os caracteres em maiúscula e minúscula: as letras maiúsculas, mesmo rotacionadas, devem permanecer letras maiúsculas; as letras minúsculas, mesmo rotacionadas, devem permanecer letras minúsculas.
- Após exibir o texto cifrado, você deve imprimir uma nova linha. Seu programa deve então sair retornando `0` de `main`.

## Conselho

Como começar? Vamos abordar este problema uma etapa por vez.

### Pseudo-código

Primeiro, tente escrever uma função `main` em `caesar.c` que implementa o programa usando apenas pseudocódigo, mesmo que não tenha certeza de como escrevê-lo em código real.

<details><summary>Dica</summary><p>Há mais de uma maneira de fazer isso, então aqui está apenas uma!</p>

    int main(void)
    {
        // Verifique se o programa foi executado com apenas um argumento de linha de comando

        // Verifique se cada caractere em argv[1] é um dígito

        // Converta argv[1] de uma `string` para um `int`

        // Peça ao usuário o texto simples

        // Para cada caractere no texto simples:

            // Gere a rotação para o caractere, se for uma letra
    }

<p>Está tudo bem editar seu próprio pseudocódigo após ver o nosso aqui, mas não basta copiar/colar o nosso no seu!</p></details>
"### Contagem de Argumentos de Linha de Comando

Seja qual for o seu pseudocódigo, vamos primeiro escrever apenas o código em C que verifica se o programa foi executado com um único argumento de linha de comando antes de adicionar funcionalidades adicionais.

Especificamente, modifique o `main` em `caesar.c` de tal maneira que, se o usuário não fornecer nenhum argumento de linha de comando ou dois ou mais, a função imprime `"Uso: ./caesar chave\n"` e retorna `1`, saindo efetivamente do programa. Se o usuário fornecer exatamente um argumento de linha de comando, o programa não deve imprimir nada e simplesmente retornar `0`. O programa deve se comportar conforme abaixo.

    $ ./caesar
    Uso: ./caesar chave


    $ ./caesar 1 2 3
    Uso: ./caesar chave


    $ ./caesar 1

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se que você pode imprimir com <code class="language-plaintext highlighter-rouge">printf</code>.</li>
  <li data-marker="*">Lembre-se de que uma função pode retornar um valor com <code class="language-plaintext highlighter-rouge">return</code>.</li>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">argc</code> contém o número de argumentos de linha de comando passados para um programa, além do próprio nome do programa.</li>
</ul></details>

### Verificação da Chave

Agora que seu programa está (esperançosamente!) aceitando entrada conforme prescrito, é hora de mais um passo.

Adicione em `caesar.c`, abaixo do `main`, uma função chamada, por exemplo, `only_digits` que recebe uma `string` como argumento e retorna `true` se essa `string` contém apenas dígitos de `0` a `9`, caso contrário retorna `false`. Certifique-se de adicionar o protótipo da função acima do `main` também.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">É provável que você queira um protótipo como:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">only_digits</span><span class="p">(</span><span class="n">string</span> <span class="n">s</span><span class="p">);</span>
</code></pre></div>    </div>
    <p>E certifique-se de incluir o `cs50.h` no topo do seu arquivo, para que o compilador reconheça a `string` (e o `bool`).</p>
  </li>
  <li data-marker="*">Lembre-se de que uma `string` é apenas uma matriz de `char`s.</li>
  <li data-marker="*">Lembre-se de que `strlen`, declarado em `string.h`, calcula o comprimento de uma `string`.</li>
  <li data-marker="*">Você pode achar `isdigit`, declarado em `ctype.h`, útil, conforme <a href="https://manual.cs50.io/">manual.cs50.io</a>. Mas observe que ele verifica apenas um `char` por vez!</li>
</ul></details>


Em seguida, modifique o `main` de tal forma que ele chame `only_digits` em `argv[1]`. Se essa função retornar `false`, então `main` deve imprimir `"Uso: ./caesar chave\n"` e retornar `1`. Caso contrário, `main` deve simplesmente retornar `0`. O programa deve se comportar conforme abaixo:

```
$ ./caesar 42
```
```
$ ./caesar banana
Uso: ./caesar chave
```### Usando a chave

Agora modifique a função `main` para que ela converta `argv[1]` em um `int`. Você pode achar útil a função `atoi`, declarada em `stdlib.h`, conforme indicado em [manual.cs50.io](https://manual.cs50.io/). Em seguida, utilize `get_string` para solicitar ao usuário algum texto simples com o prompt `"texto sem formatação: "`.

Então, implemente uma função chamada, por exemplo, `rotate`, que recebe como entrada um caractere `char` e também um `int`, e rotaciona esse caractere por essa quantidade de posições se ele for uma letra (isto é, alfabético), voltando do `Z` para o `A` (e do `z` para a `a`) conforme necessário. Se o `char` não for uma letra, a função deverá retornar o mesmo `char` sem alterações.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Provavelmente você precisará de um protótipo, como:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">char</span> <span class="nf">rotate</span><span class="p">(</span><span class="kt">char</span> <span class="n">c</span><span class="p">,</span> <span class="kt">int</span> <span class="n">n</span><span class="p">);</span>
</code></pre></div>    </div>
    <p>Uma chamada de função como</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'A'</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>ou até mesmo</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>rotate('A', 27)
</code></pre></div>    </div>
    <p>deve retornar `B`. E uma chamada de função como</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'!'</span><span class="p">,</span> <span class="mi">13</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>deve retornar `!`.</p>
  </li>
  <li data-marker="*">Lembre-se de que você pode “transformar” explicitamente um `char` em um `int` com a sintaxe `(char)` e um `int` em um `char` com a sintaxe `(int)`. Ou você pode fazer isso implicitamente tratando um como o outro.</li>
  <li data-marker="*">Provavelmente você precisará subtrair o valor ASCII de `A` de qualquer letra em maiúsculo, assim pode tratar `A` como `0`, `B` como `1`, e assim por diante, enquanto realiza aritmética. E então adicioná-lo de volta quando terminar.</li>
  <li data-marker="*">Provavelmente você precisará subtrair o valor ASCII de `a` de qualquer letra em minúsculo, assim pode tratar `a` como `0`, `b` como `1`, e assim por diante, enquanto realiza aritmética. E então adicioná-lo de volta quando terminar.</li>
  <li data-marker="*">Você pode achar útil algumas outras funções declaradas em `<ctype.h>`, de acordo com o [manual.cs50.io](https://manual.cs50.io/).</li>
  <li data-marker="*">Provavelmente você encontrará o operador `%` útil quando “envolver” aritmeticamente um valor como `25` para `0`.</li>
</ul></details>

Então, modifique a função `main` de forma que ela imprima `"texto cifrado: "` e depois itere por cada `char` no texto sem formatação do usuário, chamando a função `rotate` em cada um e imprimindo o valor de retorno.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que o `printf` pode imprimir um caractere usando `%c`.</li>
  <li data-marker="*">Se você não estiver vendo nenhuma saída ao chamar `printf`, é provável que seja porque está imprimindo caracteres fora do intervalo ASCII válido de 0 a 127. Tente imprimir temporariamente os caracteres como números (usando `%i` em vez de `%c`) para ver quais valores estão sendo impressos!</li>
</ul></details>## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/V2uusmv2wxI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


## Como Testar Seu Código

Execute o código abaixo para verificar a correção do seu programa usando `check50`. No entanto, não se esqueça de compilar e testá-lo por si mesmo também!


    check50 cs50/problems/2023/x/caesar


Execute o código abaixo para avaliar o estilo do seu código usando `style50`.

    style50 caesar.c

## Como Enviar

No seu terminal, execute o código abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/caesar