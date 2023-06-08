# Cifrado César

Para este problema, implementarás un programa que cifra mensajes usando el cifrado César, tal como se muestra a continuación.

    $ ./caesar 13
    texto plano: HELLO
    texto cifrado: URYYB

## Empezando

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de la ventana de tu terminal, luego ejecuta `cd` por sí solo. Deberías ver que la "terminal" se parece al siguiente ejemplo.

    $

Haz clic dentro de la ventana de la terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/caesar.zip

seguido de Enter para descargar un archivo ZIP llamado `caesar.zip` en tu espacio de códigos. ¡Asegúrate de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter que pueda haber!

Ahora ejecuta

    unzip caesar.zip

para crear una carpeta llamada `caesar`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm caesar.zip

y responde con "y" seguido de Enter para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd caesar

seguido de Enter para entrar (i.e., abrir) en ese directorio. Tu terminal debería tener el siguiente aspecto:

    caesar/ $

Si todo fue exitoso, ejecuta

    ls

y verás un archivo llamado `caesar.c`. Ejecutar `code caesar.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no es así, vuelve a seguir tus pasos y ve si puedes determinar en qué punto te equivocaste.