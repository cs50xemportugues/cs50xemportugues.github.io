## Antecedentes

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

<details><summary>Assista uma Gravação</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script></details>