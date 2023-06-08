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