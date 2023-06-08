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