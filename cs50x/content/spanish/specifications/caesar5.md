### Usando la Clave

Modifica ahora la función `main` de tal manera que convierta `argv[1]` en un `int`. Puedes encontrar la función `atoi`, declarada en `stdlib.h`, útil para esto, según [manual.cs50.io](https://manual.cs50.io/). Luego, usa `get_string` para preguntarle al usuario por algún texto plano con `"plaintext: "`.

Luego, implementa una función llamada, por ejemplo, `rotate`, que tome un `char` como entrada y un `int`, y gire ese `char` por esa cantidad de posiciones si es una letra (es decir, alfabética), envolviéndose de `Z` a `A` (y de `z` a `a`) según sea necesario. Si el `char` no es una letra, la función en su lugar debería devolver el mismo `char` sin cambios.


<details><summary>Sugerencias</summary><ul>
  <li data-marker="*">Probablemente quieras un prototipo como el siguiente:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">char</span> <span class="nf">rotate</span><span class="p">(</span><span class="kt">char</span> <span class="n">c</span><span class="p">,</span> <span class="kt">int</span> <span class="n">n</span><span class="p">);</span>
</code></pre></div>    </div>
    <p>Una llamada a la función como</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'A'</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>o incluso</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>rotate('A', 27)
</code></pre></div>    </div>
    <p>debe devolver <code class="language-plaintext highlighter-rouge">'B'</code>. Y una llamada a la función como</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'!'</span><span class="p">,</span> <span class="mi">13</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>debe devolver <code class="language-plaintext highlighter-rouge">'!'</code>.</p>
  </li>
  <li data-marker="*">Recuerda que puedes convertir explícitamente un `char` en un `int` con `(char)`, y un `int` en un `char` con `(int)`. O puedes hacerlo implícitamente tratando uno como el otro.</li>
  <li data-marker="*">Probablemente quieras restar el valor ASCII de <code class="language-plaintext highlighter-rouge">'A'</code> de cualquier letra mayúscula, para tratar <code class="language-plaintext highlighter-rouge">'A'</code> como <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">'B'</code> como <code class="language-plaintext highlighter-rouge">1</code>, y así sucesivamente, mientras realizas aritmética. Y luego añadirlo cuando termines con lo mismo.</li>
  <li data-marker="*">Probablemente quieras restar el valor ASCII de <code class="language-plaintext highlighter-rouge">'a'</code> de cualquier letra minúscula, para tratar <code class="language-plaintext highlighter-rouge">'a'</code> como <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">'b'</code> como <code class="language-plaintext highlighter-rouge">1</code>, y así sucesivamente, mientras realizas aritmética. Y luego añadirlo cuando termines con lo mismo.</li>
  <li data-marker="*">Podrías encontrar útiles algunas otras funciones declaradas en <code class="language-plaintext highlighter-rouge">ctype.h</code>, según [manual.cs50.io](https://manual.cs50.io/).</li>
  <li data-marker="*">Probablemente te resulte útil el operador `%` al hacer aritmética "envolvente" desde un valor como `25` a `0`.</li>
</ul></details>

Luego, modifica `main` de tal manera que imprima `"ciphertext: "` y luego itere sobre cada `char` en el texto plano del usuario, llamando a `rotate` en cada uno, e imprimiendo el valor de retorno de ésta.

<details><summary>Sugerencias</summary><ul>
  <li data-marker="*">Recuerda que `printf` puede imprimir un `char` usando `%c`.</li>
  <li data-marker="*">Si no ves ninguna salida cuando llamas a `printf`, puede ser porque estás imprimiendo caracteres fuera del rango ASCII válido de 0 a 127. ¡Intenta imprimir caracteres temporales como números (usando `%i` en lugar de `%c`) para ver qué valores estás imprimiendo!</li>
</ul></details>