# Mario

## Empezando

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de la ventana del terminal y a continuación, ejecutar `cd` por sí solo. Debes encontrar que su "prompt" se parece al a continuación.

   $

Haz clic dentro de esa ventana de terminal y luego ejecuta lo siguiente:

   wget https://cdn.cs50.net/2022/fall/psets/1/mario-less.zip

seguido de "Enter" para descargar un ZIP llamado `mario-less.zip` en tu código espacio. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter!

Ahora ejecuta

   unzip mario-less.zip

para crear una carpeta llamada `mario-less`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

  rm mario-less.zip

y responder con "y" seguido de "Enter" en el indicador para eliminar el archivo ZIP que has descargado.

Ahora escribe

   cd mario-less

seguido de "Enter" para moverte al directorio. Tu prompt ahora debería ser como el siguiente.

  mario-less/ $

Si todo fue exitoso, deberías ejecutar

  ls

y ver un archivo llamado `mario.c`. Ejecutar `code mario.c` debería abrir el archivo donde escribirás tu código para este problema. Si no es así, retrocede tus pasos y determina dónde te equivocaste.

## World 1-1

Hacia el final del Mundo 1-1 en Super Mario Bros de Nintendo, Mario debe ascender una pirámide alineada a la derecha de bloques, a la siguiente.

![Captura de pantalla de Mario saltando hacia arriba en una pirámide alineada a la derecha](https://cs50.harvard.edu/x/2023/psets/1/mario/less/pyramid.png)

Recrearemos esa pirámide en C, aunque en texto, usando (`#`) para ladrillos, como se ve a continuación. Cada hash es un poco más alto de lo que es ancho, por lo que la pirámide en sí ​​también será más alta de lo que es ancha.

        #
       ##
      ###
     ####
    #####
   ######
  #######
 ########

El programa que escribiremos se llamará `mario`. Y permitamos al usuario decidir qué tan alta debería ser la pirámide pidiéndoles primero un número entero positivo entre, digamos, 1 y 8, inclusive.

Así es como podría funcionar el programa si el usuario ingresa `8` cuando se le solicite:

    $ ./mario
    Height: 8
        #
       ##
      ###
     ####
    #####
   ######
  #######
 ########

Así es como podría funcionar el programa si el usuario ingresa `4` cuando se le solicite:

    $ ./mario
    Height: 4
      #
     ##
    ###
   ####

Así es como podría funcionar el programa si el usuario ingresa `2` cuando se le solicite:

    $ ./mario
    Height: 2
     #
    ##

Y así es como podría funcionar el programa si el usuario ingresa `1` cuando se le solicite:

    $ ./mario
    Height: 1
    #

Si el usuario no ingresa un número entero positivo entre 1 y 8, inclusive, cuando se le solicite, el programa debe volver a solicitarlo hasta que coopere:

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
      #
     ##
    ###
   ####

¿Cómo comenzar? Abordemos este problema paso a paso.

## Guía

 <div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div> "

## Pseudocódigo

Primero, ejecuta

    cd

para asegurarte de que estás en el directorio predeterminado de tu codespace.

Luego, ejecuta

    cd mario-less

para cambiar al directorio `mario-less`.

A continuación, ejecuta

    code pseudocode.txt

para abrir el archivo llamado `pseudocode.txt` en ese directorio.

Escribe en `pseudocode.txt` algún pseudocódigo que implemente este programa, aunque aún no estés seguro de cómo escribirlo en código. No hay una única manera de escribir pseudocódigo, pero los cortos enunciados en inglés son suficientes. Recuerda cómo escribimos [pseudocódigo para encontrar a alguien en un directorio telefónico](https://docs.google.com/presentation/d/1X3AMSenwZGSE6WxGpzoALAfMg2hmh1LYIJp3N2a1EYI/edit#slide=id.g41907da2bc_0_265). Lo más probable es que tu pseudocódigo utilice (¡o implique el uso!) de una o más funciones, condicionales, expresiones booleanas, bucles y/o variables.

<details><summary>Spoiler</summary><p> ¡Hay más de una forma de hacerlo, así que aquí hay solo una! </p>

<ol>
  <li>Solicita al usuario la altura</li>
  <li>Si la altura es menor que 1 o mayor que 8 (o no es un número entero en absoluto), vuelve un paso</li>
  <li>Itera desde 1 hasta la altura:
    <ol>
      <li>En la iteración <em>i</em>, imprime <em>i</em> almohadillas y luego un salto de línea</li>
    </ol>
  </li>
</ol>

<p>Está bien editar el tuyo después de ver este pseudocódigo, pero ¡no simplemente copiar / pegar el nuestro en el tuyo!</p></details>

## Solicitar entrada

Sea cual sea tu pseudocódigo, primero escribamos solo el código C que solicita (y vuelve a solicitar, si es necesario) al usuario la entrada deseada. Abre el archivo llamado `mario.c` dentro de tu directorio `mario`. (¿Recuerdas cómo?)

Ahora, modifica `mario.c` de tal manera que le solicite al usuario la altura de la pirámide, almacenando su entrada en una variable, volviéndole a solicitar la entrada una y otra vez, si no es un número entero positivo entre 1 y 8, inclusive. Luego, simplemente imprime el valor de esa variable, confirmando (para ti mismo) que has almacenado correctamente la entrada del usuario, como se muestra a continuación.

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
    Almacenado: 4

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que puedes compilar tu programa con <code class="language-plaintext highlighter-rouge">make</code>.</li>
  <li data-marker="*">Recuerda que puedes imprimir un <code class="language-plaintext highlighter-rouge">int</code> con <code class="language-plaintext highlighter-rouge">printf</code> mediante <code class="language-plaintext highlighter-rouge">%i</code>.</li>
  <li data-marker="*">Recuerda que puedes obtener enteros del usuario con <code class="language-plaintext highlighter-rouge">get_int</code>.</li>
  <li data-marker="*">Recuerda que <code class="language-plaintext highlighter-rouge">get_int</code> está declarado en <code class="language-plaintext highlighter-rouge">cs50.h</code>.</li>
  <li data-marker="*">Recuerda que solicitamos un número entero positivo al usuario en la clase usando un bucle <code class="language-plaintext highlighter-rouge">do while</code> en <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight"><code class="language-plaintext highlighter-rouge">mario.c</code></a>.</li>
</ul></details>

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

