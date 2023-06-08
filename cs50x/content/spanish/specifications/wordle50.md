<style>.wrong { background-color: red } .right { background-color: green; } .close_ { background-color: yellow; }</style>

Wordle50
========

En este problema, implementarás un programa que se comporta de manera similar al popular juego diario de palabras [Wordle](https://www.nytimes.com/games/wordle/index.html).

<pre><code> $ ./wordle 5
<span class="right">This is WORDLE50</span>
Tienes 6 intentos para adivinar la palabra de 5 letras que estoy pensando
Ingresa una palabra de 5 letras: crash
Intento 1: <span class="close_">c</span><span class="wrong">ra</span><span class="close_">s</span><span class="wrong">h</span>
Ingresa una palabra de 5 letras: scone
Intento 2: <span class="right">s</span><span class="close_">c</span><span class="wrong">o</span><span class="close_">n</span><span class="right">e</span>
Ingresa una palabra de 5 letras: since
Intento 3: <span class="right">since</span>
¡Ganaste!
</code></pre>


Comenzando
---------------

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de la ventana del terminal y luego ejecuta `cd` por sí solo. Deberías ver que su "prompt" se parece al siguiente.

    $
    
Haz clic dentro de esa ventana del terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/wordle.zip
    

seguido de Enter para descargar un ZIP llamado `wordle.zip` en tu espacio de códigos. ¡Tenga cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter!

Ahora ejecuta

    unzip wordle.zip
    

para crear una carpeta llamada `wordle`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm wordle.zip
    

y responda con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargó.

Ahora escribe

    cd wordle
    

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu prompt ahora debería verse como el siguiente.

    wordle/ $
    

Si todo fue exitoso, deberías ejecutar

    ls
    

y ver un archivo llamado `wordle.c`, así como `5.txt`, `6.txt`, `7.txt` y `8.txt`. Ejecutar `code wordle.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. De lo contrario, retrocede tus pasos y ve si puedes determinar dónde te equivocaste. Si intentas compilar el juego ahora, lo hará sin errores, pero cuando intentes ejecutarlo, verás este error:

    Error opening file 0.txt.
    

Es normal, no obstante, ya que aún no has implementado parte del código que necesitamos para que ese mensaje de error desaparezca!

Fondo
----------

Es probable que, si eres usuario de Facebook, al menos uno de tus amigos haya publicado algo así, especialmente a principios de 2022 cuando estaba muy de moda:

![Resultados de Wordle](https://cs50.harvard.edu/x/2023/psets/2/wordle50/wordle.png)

Si es así, tu amigo ha jugado a Wordle y está compartiendo sus resultados para ese día. Cada día se elige una nueva "palabra secreta" (la misma para todos) y el objetivo es adivinar cuál es la palabra secreta en seis intentos. Afortunadamente, dado que existen más de seis palabras de cinco letras en el idioma inglés, puede obtener algunas pistas en el camino y la imagen de arriba muestra en realidad la progresión de tu amigo a través de sus conjeturas, utilizando esas pistas para intentar acercarse a la palabra correcta. Usando un esquema similar al juego [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)), si después de adivinar, la letra se vuelve verde, significa que no solo esa letra está en la palabra secreta de ese día, sino que también está en la posición correcta. Si se vuelve amarillo, significa que la letra adivinada aparece _en alguna parte_ en la palabra, pero no en ese lugar. Las letras que se vuelven grises no están en la palabra en absoluto y pueden omitirse en futuras conjeturas.

Terminemos de escribir un programa llamado `wordle` que nos permita recrear este juego y jugarlo en nuestro terminal. Haremos algunos cambios pequeños en el juego (por ejemplo, la forma en que maneja que una letra aparezca dos veces en una palabra no es la misma que cómo lo maneja el juego real, pero por simplicidad, optaremos por la facilidad de comprensión en lugar de una interpretación perfectamente fiel), y usaremos texto rojo en lugar de gris para indicar las letras que no están en la palabra en absoluto. En el momento en que el usuario ejecuta el programa, debe decidir, proporcionando un argumento de línea de comandos, la longitud de la palabra que desea adivinar, entre 5 y 8 letras.

Aquí hay algunos ejemplos de cómo debería funcionar el programa. Por ejemplo, si el usuario omite un argumento de línea de comandos por completo:

     $ ./wordle
     Uso: ./wordle wordsize
    

Si en su lugar proporciona un argumento de línea de comandos, pero no está en el rango correcto:

     $ ./wordle 4
     Error: wordsize debe ser 5, 6, 7 u 8
    

Así es como podría funcionar el programa si el usuario proporciona una clave de `5`:

     $ ./wordle 5
     Esto es WORDLE50
     Tienes 6 intentos para adivinar la palabra de 5 letras que estoy pensando
     Ingresa una palabra de 5 letras:
    

En este punto, el usuario debe ingresar una palabra de 5 letras. Por supuesto, el usuario podría ser terco, y deberíamos asegurarnos de que está siguiendo las reglas:

    
<pre><code>$ ./wordle 5
<span class="right">Esto es WORDLE50</span>
Tienes 6 intentos para adivinar la palabra de 5 letras que estoy pensando
Ingresa una palabra de 5 letras: wordle
Ingresa una palabra de 5 letras: equipo
Ingresa una palabra de 5 letras: vale
Ingresa una palabra de 5 letras: juegos
Conjetura 1: <span class="wrong">g</span><span class="close_">a</span><span class="wrong">m</span><span class="close_">e</span><span class="wrong">s</span>
Ingresa una palabra de 5 letras:
</code></pre>
    

Observa que no contamos ninguno de esos intentos inválidos como conjeturas. Pero tan pronto como hicieron un intento legítimo, lo contamos como una conjetura e informamos sobre el estado de las letras. Parece que el usuario tiene algunas pistas ahora; saben que la palabra contiene una `a` y una `e` en algún lugar, pero no en los lugares exactos en los que aparecen en la palabra `juegos`. Y saben que `g`, `m` y `s` no aparecen en la palabra en absoluto, por lo que las conjeturas futuras pueden omitirlos. ¡Tal vez intenten, digamos, `heart` la próxima vez! ❤️

Especificación
-------------

Diseña e implementa un programa llamado `wordle` que complete la implementación de nuestro clon de Wordle50 (del juego). Notarás que algunas partes importantes de este programa ya han sido escritas para ti y no se te permite modificar ninguna de esas partes del programa. En lugar de eso, tu trabajo debe estar limitado a los siete `TODOs` (cosas por hacer) que hemos dejado para que los completes. Cada parte de ellos resuelve un problema específico, por lo que recomendamos que los abordes en el orden del 1 al 7. Cada `TODO` numerado corresponde al mismo elemento de la lista siguiente.

1. En el primer `TODO`, debes asegurarte de que el programa acepte un solo argumento de línea de comandos. Llamémoslo `k` por razones de discusión. Si el programa no se ejecuta con un único argumento de línea de comandos, debes imprimir el mensaje de error como lo mostramos arriba y devolver `1`, terminando el programa.
2. En el segundo `TODO`, asegúrate de que `k` sea uno de los valores aceptables (5, 6, 7 u 8) y almacena ese valor en `wordsize`. Lo necesitaremos más adelante. Si el valor de `k` no es exactamente uno de esos cuatro valores, debes imprimir el mensaje de error como lo hicimos anteriormente y devolver `1`, terminando el programa.

Después de eso, el personal ya ha escrito un código que abrirá la lista de palabras para la longitud de la palabra que el usuario quiere adivinar y seleccionará aleatoriamente una de las 1000 opciones disponibles. No te preocupes por entender todo este código, no es importante para este trabajo. Veremos algo similar en una tarea posterior y tendrás más sentido entonces. Este es un buen lugar para detenerse y probar, antes de pasar al siguiente `TODO`, que tu código se comporte como se espera. ¡Siempre es más fácil depurar programas si lo haces de forma metódica!

3. Para el tercer `TODO`, debes ayudar a defender contra usuarios obstinados asegurándote de que su suposición tenga la longitud correcta. Para ello, debemos centrarnos en la función `get_guess`, que necesitarás implementar por completo. Debes pedir al usuario (mediante `get_string`) que escriba una palabra de `k` letras (recuerda que ese valor se pasa como parámetro a `get_guess`) y si proporcionan una con una longitud incorrecta, deben volver a ser solicitados (como en [Mario](../../1/mario/less/)), hasta que proporcionen exactamente el valor que esperamos de ellos. Ahora mismo, el código de distribución no hace eso, y deberás arreglarlo. Ten en cuenta que, a diferencia de la versión real de Wordle, realmente no comprobamos si la suposición del usuario es una palabra real, por lo que en ese sentido, el juego es quizás un poco más fácil. Todas las suposiciones en este juego deben estar en caracteres **minúsculos**, y puedes asumir que el usuario no será tan obstinado como para proporcionar algo que no sean caracteres en minúsculas al hacer una suposición. Una vez que se haya obtenido una suposición legítima, puedes devolverla.
4. A continuación, para el cuarto `TODO`, necesitamos realizar un seguimiento de la "puntuación" del usuario en el juego. Lo hacemos tanto por letra, asignando una puntuación de 2 (que hemos definido como `EXACT`) a una letra en el lugar correcto, 1 (que hemos definido como`CLOSE`) a una letra que está en la palabra pero en el lugar equivocado, o 0 (que hemos definido como `WRONG`), como a nivel de palabra, para ayudarnos a detectar cuándo podríamos haber activado el final del juego al ganar. Usaremos las puntuaciones de letras individuales cuando coloreemos la impresión. Para almacenar esas puntuaciones, necesitamos un array al que hemos llamado `status`. Al comienzo del juego, con ninguna suposición realizada, debe contener solo 0.

Este es otro buen lugar para detenerte y probar tu código, ¡particularmente en lo que respecta al elemento 3 de arriba! Notarás que en este punto, cuando finalmente ingreses una suposición legítima (es decir, una que tenga la longitud correcta), es probable que tu programa se vea algo como esto:

    Ingresa una palabra de 5 letras: computadora
    Ingresa una palabra de 5 letras: juegos
    Suposición 1:
    Ingresa una palabra de 5 letras:
    

¡Pero eso es normal! Implementar `print_word` es el número 6 de nuestra lista `TODO`, por lo que no debemos esperar que el programa realice ningún procesamiento de esa suposición en este momento. Por supuesto, siempre puedes agregar llamadas adicionales a `printf` (asegúrate de eliminarlas antes de enviar el trabajo) como parte de tu estrategia de depuración.

5. El quinto `TODO` es definitivamente el más grande y posiblemente el más desafiante. Dentro de la función `check_word`, debes comparar cada una de las letras de la suposición con cada una de las letras de la `choice` (que, como recordarás, es la "palabra secreta" de este juego) y asignar las puntuaciones. Si las letras coinciden, otorga 2 puntos a `EXACT` y `break` (rompe) el bucle; no hay necesidad de seguir bucleando si ya determinó que la letra está en el lugar correcto. Técnicamente, si esa letra aparece dos veces en la palabra, esto podría resultado en un pequeño error, pero arreglar ese error complica un poco más este problema de lo que queremos ahora, ¡así que vamos a aceptarlo como una característica de nuestra versión! Si descubres que la letra está en la palabra pero no en el lugar correcto, otorga 1 punto a `CLOSE`, pero ¡no uses el `break`! Después de todo, esa letra podría aparecer más tarde en el lugar correcto en la palabra `choice`, y si rompes demasiado pronto, ¡el usuario nunca lo sabrá! Realmente no necesitas establecer explícitamente los puntos `WRONG` (0) aquí, ya que los manejamos al principio del paso 4. Sin embargo, también debes sumar la puntuación total de la palabra cuando lo sepas, porque eso es lo que se supone que esta función debe devolver en última instancia. De nuevo, ¡no tengas miedo de usar `debug50` y/o `printf`s según sea necesario para ayudarte a encontrar los valores de diferentes variables en este punto! Hasta que implementes `print_word`, más abajo, el programa no te ofrecerá mucho en términos de verificación visual.

6. Para el sexto `TODO`, completarás la implementación de `print_word`. Esa función debe revisar los valores que hayas poblado en el array `status` e imprimir, letra por letra, cada letra de la suposición con el código de color correcto. Es posible que hayas notado algunos `#define` (¡que parecen aterradores!) en la parte superior del archivo donde proporcionamos una forma más sencilla de representar lo que se llama un [código de color ANSI] (https://en.wikipedia.org/wiki/ANSI_escape_code#Colors), que es básicamente un comando para cambiar el color del texto en la terminal. No necesitas preocuparte por cómo implementar esos cuatro valores (`GREEN`, `YELLOW`, `RED` y `RESET`, este último simplemente devuelve la fuente predeterminada del terminal) o exactamente lo que significan. En su lugar, puedes simplemente usarlos (¡el poder de la abstracción!). Ten en cuenta también que proporcionamos un ejemplo en el código de distribución arriba, donde imprimimos algún texto en verde y luego restablecemos el color, como parte de la introducción del juego. En consecuencia, siéntete libre de usar la siguiente línea de código como inspiración sobre cómo podrías intentar cambiar los colores:
    
    printf(GREEN"Este es WORDLE50"RESET"\n");

Por supuesto, a diferencia de nuestro ejemplo, probablemente no quieras imprimir un salto de línea después de cada letra de la palabra (en su lugar, solo quieres un salto de línea al final, también restableciendo el color de la fuente), no sea que termine pareciéndose a esto:

    Ingresa una palabra de 5 letras: juegos
    Suposición 1: <span class="wrong">g</span>
    <span class="close_">a</span>
    <span class="wrong">m</span>
    <span class="close_">e</span>
    <span class="wrong">s</span>
    Ingresa una palabra de 5 letras:

7. Por último, el séptimo `TODO` es solo un poco de limpieza antes de que el programa termine. Ya sea que el bucle principal haya terminado de manera normal, porque el usuario se quedó sin suposiciones, o porque salimos de él al acertar la palabra exactamente, ya es hora de informar al usuario sobre el resultado del juego. Si el usuario ganó el juego, un sencillo `¡Ganaste!` es suficiente para imprimir aquí. De lo contrario, debe imprimir un mensaje diciéndole

Cómo probar tu código
---------------------

Ejecuta lo siguiente para evaluar la corrección de tu código utilizando `check50`. ¡Pero asegúrate de compilar y probarlo tú mismo también!

    check50 cs50/problems/2023/x/wordle
    

Ejecuta lo siguiente para evaluar el estilo de tu código utilizando `style50`.

    style50 wordle.c
    

Cómo enviar
-------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/wordle"

