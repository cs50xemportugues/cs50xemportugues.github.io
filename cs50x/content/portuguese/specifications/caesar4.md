### Contagem de Argumentos de Linha de Comando

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
```