Especificaciones
--------------

Diseñe e implemente un programa, `substitución`, que cifra mensajes utilizando un cifrado de sustitución.

*   Implemente su programa en un archivo llamado `substitution.c` en un directorio llamado `substitution`.
*   Su programa debe aceptar un solo argumento de línea de comandos: la clave a utilizar para la sustitución. La clave en sí debe ser insensible a mayúsculas y minúsculas, por lo que si cualquier carácter en la clave es mayúscula o minúscula no debe afectar el comportamiento de su programa.
*   Si su programa se ejecuta sin argumentos de línea de comandos o con más de un argumento de línea de comandos, su programa debería imprimir un mensaje de error de su elección (con `printf`) y retornar desde `main` un valor de `1` (que tiende a significar un error) inmediatamente.
*   Si la clave es inválida (por no contener 26 caracteres, contener algún carácter que no sea un carácter alfabético, o no contener cada letra exactamente una vez), su programa deberá imprimir un mensaje de error de su elección (con `printf`) y retornar desde `main` un valor de `1` inmediatamente.
*   Su programa debe emitir `plaintext:` (sin una nueva línea) y luego solicitar al usuario una `string` de texto plano (usando `get_string`).
*   Su programa debe emitir `ciphertext:` (sin una nueva línea) seguido por el texto cifrado correspondiente al texto plano, con cada carácter alfabético en el texto plano sustituido por el carácter correspondiente en el texto cifrado; caracteres no alfabéticos deben ser emitidos sin cambios.
*   Su programa debe preservar mayúsculas y minúsculas: las letras en mayúscula deben permanecer en mayúscula, y las letras en minúscula deben permanecer en minúscula.
*   Después de emitir el texto cifrado, debería imprimir una nueva línea. Su programa debería luego salir retornando `0` desde `main`.

Es posible que encuentre una o más funciones declaradas en `ctype.h` útiles, según [manual.cs50.io](https://manual.cs50.io/).

Paso a paso
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cXAoZAsgxJ4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Cómo probar su código
---------------------

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50/problems/2023/x/substitution

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 substitution.c

<details><summary>Cómo usar <code>debug50</code></summary><p>¿Busca ejecutar `debug50`? Puede hacerlo de la siguiente manera, después de compilar su código con éxito con `make`:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution KEY
</code></pre></div></div>

<p>donde `KEY` es la clave que da como argumento de línea de comandos a su programa. Tenga en cuenta que ejecutar</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution
</code></pre></div></div>

<p>¡debería provocar que su programa termine preguntando al usuario por una clave!</p></details>

Cómo enviar
------------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/substitution"