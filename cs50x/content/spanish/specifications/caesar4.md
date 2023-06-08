### Contando los argumentos de línea de comandos

Sea cual sea el pseudocódigo, primero escribamos solo el código C que verifica si el programa se ejecutó con un solo argumento de línea de comandos antes de agregar funcionalidades adicionales.

Específicamente, modifique `main` en `caesar.c` de tal manera que, si el usuario no proporciona argumentos de línea de comandos, o dos o más, la función imprime `"Usage: ./caesar key\n"` y luego devuelve `1`, lo que significa que el programa ha terminado de ejecutarse. Si el usuario proporciona exactamente un argumento de línea de comandos, el programa no debería imprimir nada y simplemente regresar `0`. El programa debería comportarse así:

    $ ./caesar
    Usage: ./caesar key


    $ ./caesar 1 2 3
    Usage: ./caesar key


    $ ./caesar 1

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerde que puede imprimir con <code class="language-plaintext highlighter-rouge">printf</code>.</li>
  <li data-marker="*">Recuerde que una función puede devolver un valor con <code class="language-plaintext highlighter-rouge">return</code>.</li>
  <li data-marker="*">Recuerde que <code class="language-plaintext highlighter-rouge">argc</code> contiene la cantidad de argumentos de línea de comandos que se le pasaron a un programa, más el propio nombre del programa.</li>
</ul></details>

### Verificando la Key

Ahora que su programa está aceptando la entrada según lo prescrito, es hora de dar otro paso.

Agregue a `caesar.c', debajo de `main`, una función llamada, p. ej., `only_digits` que toma un `string` como argumento y devuelve `true` si ese `string` contiene solo dígitos, del `0` al `9`, de lo contrario devuelve `false`. Asegúrese de agregar el prototipo de la función sobre `main` también.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Probablemente necesitará un prototipo parecido a:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">only_digits</span><span class="p">(</span><span class="n">string</span> <span class="n">s</span><span class="p">);</span>
</code></pre></div>    </div>
     <p>Y asegúrese de incluir <code class="language-plaintext highlighter-rouge">cs50.h</code> en la parte superior de su archivo, para que el compilador reconozca<span class="language-plaintext highlighter-rouge">string</span> (y <code class="language-plaintext highlighter-rouge">bool</code>).</p>
  </li>
  <li data-marker="*">Recuerde que un <code class="language-plaintext highlighter-rouge">string</code> es solo una matriz de <code class="language-plaintext highlighter-rouge">char</code>s.</li>
  <li data-marker="*">Recuerde que <code class="language-plaintext highlighter-rouge">strlen</code>, declarado en <code class="language-plaintext highlighter-rouge">string.h</code>, calcula la longitud de un <code class="language-plaintext highlighter-rouge">string</code>.</li>
  <li data-marker="*">Puede encontrar útil <code class="language-plaintext highlighter-rouge">isdigit</code>, declarado en <code class="language-plaintext highlighter-rouge">ctype.h</code>, según <a href="https://manual.cs50.io/">manual.cs50.io</a>. ¡Pero tenga en cuenta que solo verifica un <code class="language-plaintext highlighter-rouge">char</code> a la vez!</li>
</ul></details>


Luego, modifique `main` de tal manera que llame a `only_digits` en `argv [1]`. Si esa función devuelve `false`, entonces `main` debe imprimir `"Usage: ./caesar key\n"` y devolver `1`. De lo contrario, `main` debe simplemente devolver `0`. El programa debería comportarse así:

```
$ ./caesar 42
```
```
$ ./caesar banana
Usage: ./caesar key
```