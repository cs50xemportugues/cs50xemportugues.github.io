Substitución
============

Para este problema, escribirás un programa que implemente un cifrado de sustitución, como se muestra a continuación.

    $ ./substitution JTREKYAVOGDXPSNCUIZLFBMWHQ
    plaintext:  HELLO
    ciphertext: VKXXN
    

Comenzando
---------------

Abre [VS Code](https://code.cs50.io/).

Haz clic dentro de tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que su "invitación" se asemeja a lo siguiente.

    $
    

Haz clic dentro de esa ventana de terminal y después ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/substitution.zip
    

seguido de la tecla Enter para descargar un archivo ZIP llamado `substitution.zip` en tu espacio de codificación. Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter por ese asunto.

Ahora ejecuta

    unzip substitution.zip
    

para crear una carpeta llamada `substitution`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm substitution.zip
    

y responder con "y" seguido de Enter en el símbolo del sistema para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd substitution
    

seguido de Enter para ingresar (es decir, abrir) ese directorio. Su indicación debería parecerse a lo siguiente.

    substitution/ $
    

Si todo fue exitoso, debes ejecutar

    ls
    

y ver un archivo llamado `substitution.c`. Ejecutar `code substitution.c` debería abrir el archivo en el que escribirás tu código para este conjunto de problemas. Si no es así, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.

Contexto
----------

En un cifrado de sustitución, "ciframos" (es decir, ocultamos de manera reversible) un mensaje reemplazando cada letra por otra letra. Para hacerlo, usamos una _clave_: en este caso, una asignación de cada una de las letras del alfabeto a la letra a la que debe corresponder cuando la cifremos. Para "descifrar" el mensaje, el receptor del mensaje tendría que conocer la clave, para que pueda revertir el proceso: traducir el texto cifrado (generalmente llamado _ciphertext_) de vuelta al mensaje original (generalmente llamado _plaintext_).

Una clave, por ejemplo, podría ser la cadena `NQXPOMAFTRHLZGECYJIUWSKDVB`. Esta clave de 26 caracteres significa que `A` (la primera letra del alfabeto) debe convertirse en `N` (el primer carácter de la clave), `B` (la segunda letra del alfabeto) debe convertirse en `Q` (el segundo carácter de la clave), y así sucesivamente.

Un mensaje como `HELLO`, entonces, se cifraría como `FOLLE`, reemplazando cada una de las letras según la asignación determinada por la clave.

Escribamos un programa llamado `substitution` que te permita cifrar mensajes usando un cifrado de sustitución. En el momento en que el usuario ejecuta el programa, deben decidir, proporcionando un argumento en línea de comandos, cuál debería ser la clave en el mensaje secreto que proporcionarán en tiempo de ejecución.

Aquí hay algunos ejemplos de cómo podría funcionar el programa. Por ejemplo, si el usuario ingresa una clave de `YTNSHKVEFXRBAUQZCLWDMIPGJO` y un plaintext de `HELLO`:

    $ ./substitution YTNSHKVEFXRBAUQZCLWDMIPGJO
    plaintext:  HELLO
    ciphertext: EHBBQ
    

Aquí es cómo podría funcionar el programa si el usuario proporciona una clave de `VCHPRZGJNTLSKFBDQWAXEUYMOI` y un plaintext de `hello, world`:

    $ ./substitution VCHPRZGJNTLSKFBDQWAXEUYMOI
    plaintext:  hello, world
    ciphertext: jrssb, ybwsp
    

Ten en cuenta que ni la coma ni el espacio fueron reemplazados por el cifrado. ¡Solo sustituye caracteres alfabéticos! También se observa que se ha preservado el caso del mensaje original. Las letras minúsculas siguen siendo minúsculas y las letras mayúsculas siguen siendo mayúsculas.

No importa si los caracteres en la propia clave están en mayúsculas o minúsculas. Una clave de `VCHPRZGJNTLSKFBDQWAXEUYMOI` es funcionalmente idéntica a una clave de `vchprzgjntlskfbdqwaxeuymoi` (de la misma manera que lo es `VcHpRzGjNtLsKfBdQwAxEuYmOi`).

Y si un usuario no proporciona una clave válida? El programa debe explicar con un mensaje de error:

    $ ./substitution ABC
    Key must contain 26 characters.
    

¿O realmente no cooperar, no proporcionando ningún argumento en línea de comandos en absoluto? El programa debe recordar al usuario cómo usar el programa:

    $ ./substitution
    Usage: ./substitution key
    

¿O realmente, realmente no cooperar, proporcionando demasiados argumentos de línea de comandos? El programa también debe recordar al usuario cómo usar el programa:

    $ ./substitution 1 2 3
    Usage: ./substitution key
    

<details><summary>Mira una grabación</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-HWzT4fngSv4KtdNFgfgpdLxZY" src="https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY.js"></script></details>

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

