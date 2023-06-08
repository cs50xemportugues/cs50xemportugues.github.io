## Construyendo el opuesto

Ahora que (¡esperemos!) tu programa está aceptando correctamente las entradas, es hora de dar otro paso.

Resulta que es un poco más fácil construir una pirámide alineada a la izquierda que a la derecha, como la siguiente:

    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########

¡Así que primero construyamos una pirámide alineada a la izquierda y luego, una vez que eso funcione, la alineamos a la derecha!

Modifica `mario.c` de manera que ya no imprima simplemente la entrada del usuario, sino que imprima una pirámide alineada a la izquierda de la altura dada.

<details>
  <summary>Pistas</summary>
  <ul>
    <li data-marker="*">Recuerda que un símbolo # es solo un carácter como cualquier otro, así que puedes imprimirlo con `printf`.</li>
    <li data-marker="*">Al igual que Scratch tiene un bloque de repetición, `repeat`, C tiene un ciclo `for`, que permite iterar algunas veces. ¿Podrías imprimir en cada iteración, `i`, tantos símbolos # como `i`?</li>
    <li data-marker="*">
      <p>De hecho, puedes "anidar" ciclos, iterando con una variable (por ejemplo,`i`) en el ciclo "externo" y otra (por ejemplo, `j`) en el ciclo "interno". Por ejemplo, así es como podrías imprimir un cuadrado de altura y ancho `n`. Por supuesto, ¡no es un cuadrado lo que quieres imprimir!</p>

      <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  for (int i = 0; i &lt; n; i++)

      {
      for (int j = 0; j &lt; n; j++)
      {
      printf("#");
      }
      printf("\n");
      }
      </code></pre></div> </div>

</li>
  </ul>
</details>

## Alineando a la derecha con puntos

Ahora alineemos a la derecha esa pirámide, moviendo los símbolos# hacia la derecha y precediéndolos con puntos (es decir, períodos), como se muestra a continuación:

    .......#
    ......##
    .....###
    ....####
    ...#####
    ..######
    .#######
    ########

Modifica `mario.c` de tal manera que alinee a la derecha la pirámide tal y como se muestra arriba.

<details><summary>Pista</summary><p>Observa cómo la cantidad de puntos necesarios en cada línea es el "opuesto" del número de símbolos#, en esa línea. Para una pirámide de altura 8, como la de arriba, la primera línea sólo tiene 1 símbolo# y por lo tanto necesita 7 puntos. Mientras que la línea inferior tiene 8 símbolos# y, por lo tanto, no necesita puntos. ¿Qué fórmula (o aritmética, en realidad) podrías usar para imprimir tantos puntos como sea necesario?</p></details>

### Cómo probar tu código

¿Funciona tu código como se prescribe cuando introduces:

- `-1` (u otros números negativos)?
- `0`?
- `1` a `8`?
- `9` u otros número positivos?
- letras o palabras?
- ninguna entrada en absoluto cuando solo presionas Enter?

## Quitando los puntos

¡Todo lo que queda ahora es un toque final! Modifica `mario.c` de manera que imprima espacios en lugar de puntos.

### Cómo probar tu código

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilar y probarlo también por tu cuenta!

    check50 cs50/problems/2023/x/mario/less

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 mario.c

<details><summary>Pista</summary><p>Un espacio es simplemente un toque de la barra espaciadora, así como un punto es simplemente un toque de su tecla. ¡Solo recuerda que `printf` requiere que los dos se rodeen con comillas dobles!</p></details>

## Cómo enviar tu trabajo

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

   submit50 cs50/problems/2023/x/mario/less