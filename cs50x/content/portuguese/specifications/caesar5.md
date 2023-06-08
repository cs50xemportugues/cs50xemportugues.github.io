### Usando a chave

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
</ul></details>