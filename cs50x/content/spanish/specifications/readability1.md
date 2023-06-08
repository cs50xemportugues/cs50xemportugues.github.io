# Legibilidad

Para este problema, implementarás un programa que calcula el nivel de grado aproximado necesario para comprender un texto, como se muestra a continuación.

    $ ./readability
    Texto: ¡Felicitaciones! Hoy es tu día. ¡Te diriges a lugares maravillosos! ¡Te vas lejos!
    Grado 3

## Empezando

Abre [VS Code](https://code.cs50.io/).

Empieza haciendo clic dentro de la ventana de tu terminal y luego ejecuta `cd` por si solo. Deberías encontrar que la etiqueta del "prompt" se parece a la siguiente.

    $

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/readability.zip

seguido de Enter para descargar un archivo ZIP llamado `readability.zip` en tu espacio de trabajo de código. Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter, ¡por cierto!

Ahora ejecuta

    unzip readability.zip

para crear una carpeta llamada `readability`. Ya no necesitas el archivo ZIP, así que puedes ejecutar 

    rm readability.zip

y responder con "y" seguido de Enter en el "prompt" para eliminar el archivo ZIP que descargaste.

Ahora escribe 

    cd readability

seguido de Enter para moverte (es decir, abrir) a ese directorio. Tu etiqueta de "prompt" debería parecerse a la siguiente.

    readability/ $

Si todo fue exitoso, deberás ejecutar

    ls

y ver un archivo llamado `readability.c`. Ejecutar `code readability.c` debería abrir el archivo en el que escribirás tu código para este conjunto de problemas. Si eso no sucede, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.