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