# Laboratorio 2: Scrabble

<div class="alert" data-alert="warning" role="alert">
  <p>Está permitido colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante de algún grupo contribuya de manera igual al laboratorio.</p>
</div>

Determina cuál de dos palabras de scrabble vale más.

    $ ./scrabble
    Jugador 1: COMPUTADORA
    Jugador 2: ciencia
    ¡El jugador 1 gana!

## Empezando

Abre [VS Code](https://code.cs50.io/).

Haz clic dentro de la ventana de tu terminal y luego ejecuta `cd` por sí solo. Deberías encontrar que su "prompt" se parece a lo siguiente.

    $

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/labs/2/scrabble.zip

seguido de Enter para descargar un archivo ZIP llamado `scrabble.zip` en tu codespace. ¡Asegúrate de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter!

Ahora ejecuta

    unzip scrabble.zip

para crear una carpeta llamada `scrabble`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm scrabble.zip

y responde con "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd scrabble

seguido de Enter para mudarte (es decir, abrir) ese directorio. Deberías tener en tu `prompt` algo como lo siguiente.

    scrabble/ $

Si todo salió bien, deberías ejecutar

    ls

y deberías ver un archivo llamado `scrabble.c`. Abre ese archivo ejecutando lo siguiente:

    code scrabble.c

Si tienes algún problema, sigue estos mismos pasos de nuevo y ve si puedes determinar dónde cometiste un error.

## Contexto

En el juego de [Scrabble](https://scrabble.hasbro.com/en-us/rules), los jugadores crean palabras para obtener puntos, y el número de puntos es la suma de los valores de punto de cada letra en la palabra.

<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
      <th>I</th>
      <th>J</th>
      <th>K</th>
      <th>L</th>
      <th>M</th>
      <th>N</th>
      <th>O</th>
      <th>P</th>
      <th>Q</th>
      <th>R</th>
      <th>S</th>
      <th>T</th>
      <th>U</th>
      <th>V</th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>1</td>
      <td>8</td>
      <td>5</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>10</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>8</td>
      <td>4</td>
      <td>10</td>
    </tr>
  </tbody>
</table>

Por ejemplo, si quisiéramos puntuar la palabra `Codigo`, notaríamos que en general las reglas de Scrabble, la `C` vale `3` puntos, la `o` vale `1` punto, la `d` vale `2` puntos y la `e` vale `1` punto. Sumando estos, obtenemos que `Codigo` vale `3 + 1 + 2 + 1 = 7` puntos.

## Detalles de Implementación

Completa la implementación de `scrabble.c` de tal manera que determine el ganador de un juego corto de Scrabble, en el que dos jugadores ingresan cada uno su palabra y el jugador con la puntuación más alta gana.

- Observa que hemos almacenado los valores de puntos de cada letra del alfabeto en una matriz de enteros llamada `POINTS`.
  - Por ejemplo, `A` o `a` vale 1 punto (representado por `POINTS [0]`), `B` o `b` vale 3 puntos (representado por `POINTS [1]`), etc.
- Observa que hemos creado un prototipo para una función auxiliar llamada `compute_score()` que toma una cadena como entrada y devuelve un `int`. Siempre que deseemos asignar valores de puntos a una palabra en particular, podemos llamar a esta función. Ten en cuenta que este prototipo es requerido para que C sepa que `compute_score()` existe más adelante en el programa.
- En `main()`, el programa pide a los dos jugadores sus palabras usando la función `get_string()`. Estos valores se almacenan dentro de las variables llamadas `word1` y `word2`.
- En `compute_score()`, tu programa debe calcular, usando la matriz `POINTS`, y devolver la puntuación para el argumento de cadena. Los caracteres que no son letras deben tener cero puntos, y las letras mayúsculas y minúsculas deben tener los mismos valores de punto.
  - Por ejemplo, `!` vale `0` puntos mientras que `A` y `a` valen ambos `1` punto.
  - Aunque las reglas de Scrabble normalmente requieren que una palabra esté en el diccionario, ¡no es necesario comprobar esto en este problema!
- En `main()`, tu programa debe imprimir, dependiendo de las puntuaciones de los jugadores, `¡El jugador 1 gana!`, `¡El jugador 2 gana!` o `¡Empate!`.

### Paso a paso

<div class="alert" data-alert="primary" role="alert"><p>¡Este video fue grabado cuando el curso todavía estaba usando CS50 IDE para escribir código! Aunque la interfaz puede verse diferente a la de tu codespace, ¡el comportamiento de ambos entornos debería ser muy similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/RtjxxxlN1gc"></iframe>

### Consejos

- Puedes encontrar útiles las funciones `isupper ()` e `islower ()`. Estas funciones toman un carácter como argumento y devuelven un valor booleano.
- Para encontrar el valor en el índice `n` de una matriz llamada `arr`, podemos escribir `arr [n]`. Esto también lo podemos aplicar a las cadenas, ya que las cadenas son arrays de caracteres.
- Recuerda que las computadoras representan los caracteres mediante [ASCII](https://asciitable.com/), un estándar que representa cada carácter como un número.

<details><summary>¿No estás seguro de cómo resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/USiLkXuXJEg"></iframe></details>

### Cómo probar tu código

Tu programa debe comportarse como se muestra en los ejemplos a continuación.

```
$ ./scrabble
Jugador 1: ¿Pregunta?
Jugador 2: ¿Pregunta?
¡Empate!
```

```
$ ./scrabble
Jugador 1: Oh,
Jugador 2: hai!
¡El jugador 2 gana!
```

```
$ ./scrabble
Jugador 1: COMPUTADORA
Jugador 2: ciencia
¡El jugador 1 gana!
```

```
$ ./scrabble
Jugador 1: Scrabble
Jugador 2: wiNNeR
¡El jugador 1 gana!
```

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilar y probarlo tú mismo también!

    check50 cs50/labs/2023/x/scrabble

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 scrabble.c

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/labs/2023/x/scrabble