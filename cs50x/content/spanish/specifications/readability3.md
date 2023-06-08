### Obtener entrada del usuario

Primero, escribamos un código en C que solo obtiene algunos datos de entrada del usuario y los imprime de nuevo. Específicamente, implemente en `readability.c` una función principal (`main`) que solicite al usuario `" Texto: "` usando `get_string` y luego imprima ese mismo texto usando `printf`. Y recuerde, mientras trabaja en este programa, que si utiliza alguna función de la biblioteca, asegúrese de `#incluir` cualquier archivo de encabezado correspondiente.

El programa debería comportarse de la siguiente manera:

    $ ./readability
    Text: In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
    In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.


### Letras

Ahora que hemos recopilado la entrada del usuario, comencemos a analizar esa entrada contando el número de letras en el texto. Considere las letras como caracteres alfabéticos en mayúscula o minúscula, no como puntuación, dígitos u otros símbolos.

Agregue a `readability.c`, debajo de `main`, una función llamada `count_letters` que tome un argumento, una `cadena` de texto, y que devuelva un `int`, el número de letras en ese texto. Asegúrese de agregar el prototipo de función, también en la parte superior de su archivo, para que `main` sepa cómo llamarla. Es probable que el prototipo se parezca al siguiente :

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">count_letters</span><span class="p">(</span><span class="n">cadena</span> <span class="n">texto</span><span class="p">)</span>
</code></pre></div></div>

Luego, llame a esa función en `main` para que, en lugar de imprimir el propio texto, su programa imprima el número de letras en el texto.

El programa debería comportarse de la siguiente manera:

    $ ./readability
    Text: Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"
    235 letras

<details><summary>Indicación</summary><p>En <code class="language-plaintext highlighter-rouge">ctype.h</code> se declara una función que puede resultar útil, según <a href="https://manual.cs50.io/">manual.cs50.io</a>. Si lo usa, asegúrese de incluir ese archivo de encabezado en su propio código.</p></details>


### Palabras

El índice de Coleman-Liau no solo se preocupa por el número de letras sino también por el número de palabras en una oración. Para este problema, consideraremos cualquier secuencia de caracteres separados por un espacio como una palabra (por lo que una palabra con guion como `" sister-in-law"` se considera una sola palabra, no tres).

Agregue a `readability.c`, debajo de `main`, una función llamada `count_words` que tome un argumento, una `cadena` de texto, y que devuelva un `int`, el número de palabras en ese texto. Asegúrese de agregar el prototipo de función, también en la parte superior de su archivo, para que `main` sepa cómo llamarla. (¡Dejamos su prototipo a su elección!)

Luego, llame a esa función en `main` para que su programa también imprima el número de palabras en el texto.

Se puede asumir que una oración:

- contendrá al menos una palabra;
- no comenzará ni terminará con un espacio; y
- no tendrá múltiples espacios seguidos.

¡Por supuesto, puede intentar una solución que tolerará múltiples espacios entre palabras o, de hecho, sin palabras!

El programa debería funcionar de la siguiente manera:

    $ ./readability
    Text: It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.
    250 letras
    55 palabras