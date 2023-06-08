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