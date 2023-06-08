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