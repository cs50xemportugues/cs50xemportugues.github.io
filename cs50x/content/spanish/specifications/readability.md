# Legibilidad

Para este problema, implementarás un programa que calcula el nivel de grado aproximado necesario para comprender un texto, como se muestra a continuación.

    $ ./readability
    Texto: ¡Felicitaciones! Hoy es tu día. ¡Te diriges a lugares maravillosos! ¡Te vas lejos!
    Grado 3

## Empezando

Abre [VS Code](https://code.cs50.io/).

Empieza haciendo clic dentro de la ventana de tu terminal y luego ejecuta `cd` por si solo. Deberías encontrar que la etiqueta del "prompt" se parece a la siguiente.

    $

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/readability.zip

seguido de Enter para descargar un archivo ZIP llamado `readability.zip` en tu espacio de trabajo de código. Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter, ¡por cierto!

Ahora ejecuta

    unzip readability.zip

para crear una carpeta llamada `readability`. Ya no necesitas el archivo ZIP, así que puedes ejecutar 

    rm readability.zip

y responder con "y" seguido de Enter en el "prompt" para eliminar el archivo ZIP que descargaste.

Ahora escribe 

    cd readability

seguido de Enter para moverte (es decir, abrir) a ese directorio. Tu etiqueta de "prompt" debería parecerse a la siguiente.

    readability/ $

Si todo fue exitoso, deberás ejecutar

    ls

y ver un archivo llamado `readability.c`. Ejecutar `code readability.c` debería abrir el archivo en el que escribirás tu código para este conjunto de problemas. Si eso no sucede, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.

## Contexto

Según [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), _Charlotte’s Web_ de E.B. White corresponde a un nivel de lectura entre segundo y cuarto grado, mientras que _The Giver_ de Lois Lowry corresponde a un nivel de lectura entre octavo y duodécimo grado. ¿Qué significa, sin embargo, que un libro esté en un nivel de lectura en particular?

Bueno, en muchos casos, un experto humano podría leer un libro y tomar una decisión sobre el grado (es decir, el año escolar) para el que cree que el libro es más apropiado. ¡Pero un algoritmo también podría descifrarlo!

Entonces, ¿qué tipos de características son características de niveles de lectura más altos? Bueno, probablemente palabras más largas se correlacionan con un nivel de lectura más alto. Del mismo modo, las frases más largas probablemente se correlacionen con niveles de lectura más altos también. 

Un número de "pruebas de legibilidad" se han desarrollado a lo largo de los años que definen fórmulas para calcular el nivel de lectura de un texto. Una de estas pruebas de legibilidad es el _índice Coleman-Liau_. El índice Coleman-Liau de un texto está diseñado para imprimir (el nivel de grado estadounidense) que se necesita para comprender algún texto. La fórmula es

    index = 0,0588 * L - 0,296 * S - 15,8

donde `L` es el número promedio de letras por cada 100 palabras del texto, y `S` es el número promedio de frases por cada 100 palabras del texto.

Escribamos un programa llamado `readability` que tome un texto y determine su nivel de lectura. Por ejemplo, si el usuario escribe una línea de texto de Dr. Seuss, el programa debería comportarse de la siguiente manera:

    $ ./readability
    Texto: ¡Felicidades! Hoy es tu día. ¡Te vas a grandes lugares! ¡Te vas y te alejas!
    Grado 3

El texto ingresado por el usuario tiene 65 letras, 4 frases y 14 palabras.  65 letras por cada 14 palabras es un promedio de alrededor de 464,29 letras por cada 100 palabras (porque 65/14 * 100 = 464,29). Y 4 frases por cada 14 palabras es un promedio de alrededor de 28,57 frases por cada 100 palabras (porque 4/14 * 100 = 28,57). Al aplicar la fórmula Coleman-Liau, y redondeando al entero más cercano, obtenemos una respuesta de 3 (porque 0,0588 * 464,29 - 0,296 * 28,57 - 15,8 = 3): por lo tanto, este pasarje se encuentra en un nivel de lectura de tercer grado.

Intentemos con otro ejemplo:

    $ ./readability
    Texto: Harry Potter era un chico muy inusual en muchos sentidos. Por una cosa, él odiaba las vacaciones de verano más que cualquier otra época del año. Por otra parte, él realmente quería hacer su tarea, pero fue obligado a hacerlo en secreto, en medio de la noche. Y también, resultó ser un mago.
    Grado 5

Este texto tiene 214 letras, 4 frases y 56 palabras. Eso da alrededor de 382,14 letras por cada 100 palabras, y 7,14 frases por cada 100 palabras. Al aplicar la fórmula Coleman-Liau, obtenemos un nivel de lectura de quinto grado.

A medida que el número promedio de letras y palabras por frase aumenta, el índice Coleman-Liau da al texto un nivel de lectura más alto. Si tomaras este párrafo, por ejemplo, que tiene palabras y frases más largas que cualquiera de los ejemplos anteriores, la fórmula daría al texto un nivel de lectura de décimo segundo grado.

    $ ./readability
    Texto: A medida que el número promedio de letras y palabras por frase aumenta, el índice Coleman-Liau da al texto un nivel de lectura más alto. Si tomaras este parráfo, por ejemplo, que tiene palabras y frases más largas que cualquiera de los ejemplos anteriores, la fórmula daría al texto un nivel de lectura de décimo segundo grado.
    Grado 12

<details><summary>Mira una grabación</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script></details>

## Especificaciones

Diseña e implementa un programa, `readability`, que calcule el índice Coleman-Liau de un texto.

- Implementa tu programa en un archivo llamado `readability.c` en un directorio llamado `readability`.
- Tu programa debe solicitar al usuario una `cadena` de texto usando `get_string`.
- Tu programa debería contar el número de letras, palabras y frases en el texto. Puedes suponer que una letra es cualquier carácter en minúscula desde `a` hasta `z` o cualquier carácter en mayúscula desde `A` a `Z`, cualquier secuencia de caracteres separados por espacio debería contar como una palabra, y que cualquier aparición de un punto, signo de exclamación o interrogación indica el final de una sentencia.
- Tu programa debería imprimir como resultado `"Grado X"`, donde `X` es el nivel de grado calculado por la fórmula Coleman-Liau, redondeado al entero más cercano.
- Si el número de índice resultante es 16 o mayor (equivale a o es mayor que el nivel de lectura de un estudiante universitario mayor), tu programa debería devolver `"Grado 16+"` en lugar de dar el número de índice exacto. Si el número de índice es menor que 1, tu programa debería devolver `"Antes del grado 1"`.

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

### Oraciones

La última pieza de información que la fórmula de Coleman-Liau toma en cuenta, además del número de letras y palabras, es el número de oraciones. Determinar el número de oraciones puede ser sorprendentemente complicado. En primer lugar, puede imaginar que una oración es simplemente cualquier secuencia de caracteres que termina con un punto, pero por supuesto las oraciones también pueden terminar con un signo de exclamación o una pregunta. Pero por supuesto, no todos los puntos significan necesariamente que la oración ha terminado. Por ejemplo, considere la siguiente oración:

    Sr. y Sra. Dursley, del número cuatro de Privet Drive, estaban orgullosos de decir que eran perfectamente normales, muchas gracias.

Esta es solo una oración, ¡pero hay tres puntos! Para este problema, le pediremos que ignore esa sutileza: debe considerar cualquier secuencia de caracteres que termine con un `.` o un `!` o un `?` como una oración (así que para la “oración” anterior, debería contarla como tres oraciones). En la práctica, la detección de límites de las oraciones necesita ser un poco más inteligente para manejar estos casos, pero no nos preocuparemos por eso por ahora.

Agregue a `readability.c`, debajo de `main`, una función llamada `count_sentences` que tome un argumento, una cadena de texto, y que devuelva un `int`, el número de oraciones en ese texto. Asegúrese de agregar el prototipo de la función, también en la parte superior de su archivo, para que `main` sepa cómo llamarla. (¡Dejamos su prototipo a su elección!)

Luego llame a esa función en `main` para que su programa también imprima el número de oraciones en el texto.

El programa debe comportarse a continuación:

    $ ./readability
    Texto: Cuando casi cumplió trece años, a mi hermano Jem le rompieron mal el brazo en el codo. Cuando sanó, y los temores de Jem de nunca poder jugar al fútbol fueron calmados, rara vez se sintió cohibido por su lesión. Su brazo izquierdo era un poco más corto que el derecho; cuando estaba de pie o caminaba, el dorso de su mano hacía ángulo recto con su cuerpo, su pulgar paralelo a su muslo.
    295 letras
    70 palabras
    3 oraciones

### Poniéndolo Todo Junto

¡Ahora es el momento de unir todas las piezas! Recuerde que el índice Coleman-Liau se calcula utilizando la fórmula:

    índice = 0,0588 * L - 0,296 * S - 15,8

donde `L` es el número promedio de letras por cada 100 palabras en el texto, y `S` es el número promedio de oraciones por cada 100 palabras en el texto.

Modifique `main` en `readability.c` para que, en lugar de imprimir el número de letras, palabras y oraciones, imprima (solo) el nivel de grado según lo definido por el índice Coleman-Liau (por ejemplo, `"Grado 2"` o `"Grado 8"` o similar). ¡Asegúrate de redondear el número índice resultante al entero más cercano!

<details><summary>Sugerencias</summary> <ul>
  <li data-marker="*"> ¡Recuerda que `round` se declara en `math.h`! </li>
  <li data-marker="*"> Recuerde que, al dividir valores de tipo `int` en C, el resultado también será un valor `int`, con cualquier resto (es decir, dígitos después del punto decimal) descartado. Dicho de otra manera, el resultado será "truncado". ¡Es posible que desee convertir uno o más valores a `float` antes de realizar la división al calcular `L` y `S`! </li>
</ul> </details>

Si el número índice resultante es 16 o superior (equivalente o mayor que un nivel de lectura de pregrado avanzado), su programa debe imprimir `"Grado 16+"` en lugar de imprimir un número índice exacto. Si el número índice es menor que 1, su programa debe imprimir `"Antes del Grado 1"`.

## Recorrido

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/AOVyZEh9zgE?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo probar tu código

Intenta ejecutar tu programa en los siguientes textos, para asegurarte de ver el nivel de grado especificado. Asegúrate de copiar solo el texto, sin espacios adicionales.

- `One fish. Two fish. Red fish. Blue fish.` (Antes del grado 1)
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (Grado 2)
- `Congratulations! Today is your day. You're off to Great Places! You're off and away!` (Grado 3)
- `Harry Potter era un chico muy inusual en muchos aspectos. Para empezar, odiaba las vacaciones de verano más que cualquier otra época del año. Por otra parte, realmente quería hacer su tarea, pero se veía obligado a hacerlo en secreto, en plena noche. Y además, también resultó ser un mago.` (Grado 5)
- `En mis años más jóvenes y vulnerables, mi padre me dio un consejo que he estado meditando desde entonces.` (Grado 7)
- `Alicia empezaba a estar bastante cansada de estar sentada junto a su hermana a la orilla del río y de no tener nada que hacer. Varias veces había mirado en el libro que su hermana estaba leyendo, pero no tenía dibujos ni diálogos: « ¿De qué sirve un libro», se preguntaba Alicia, «sin dibujos ni diálogos? ». ` (Grado 8)
- `Cuando tenía casi trece años, a mi hermano Jem le rompieron muy mal el brazo en el codo. Cuando sanó, y los temores de Jem de no poder jugar al fútbol se aliviaron, él rara vez se sintió cohibido por su lesión. Su brazo izquierdo era algo más corto que el derecho; cuando se paraba o caminaba, la parte posterior de su mano estaba en ángulo recto con su cuerpo, el pulgar paralelo a su muslo.` (Grado 8)
- `Hay más cosas en el cielo y en la tierra, Horacio, de las que puede pensar tu filosofía.` (Grado 9)
- `Era un día frío y brillante de abril, y los relojes daban las trece. Winston Smith, con el mentón hundido en el pecho en un esfuerzo por escapar del vil viento, se deslizó rápidamente a través de las puertas de vidrio de Victory Mansions, aunque no lo suficientemente rápido como para evitar que una nube de polvo entrara con él.` (Grado 10)
- `Una gran cantidad de problemas computacionales implican la determinación de propiedades de gráficos, digrafos, enteros, matrices de enteros, familias finitas de conjuntos finitos, fórmulas booleanas y elementos de otros dominios contables.` (Grado 16+)

Ejecuta el siguiente comando para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilar y probarlo tú mismo también!

    check50 cs50/problems/2023/x/readability

Ejecuta el siguiente comando para evaluar el estilo de tu código usando `style50`.

    style50 readability.c

## Cómo hacer la entrega

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2023/x/readability


