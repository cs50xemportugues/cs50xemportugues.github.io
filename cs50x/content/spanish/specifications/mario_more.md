# Mario

## Empezando

Abre [VS Code](https://code.cs50.io/).

Empieza haciendo clic dentro de la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías encontrar que la "promt" se parece a lo siguiente.

$

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-more.zip

seguido de Enter para descargar un archivo ZIP llamado `mario-more.zip` en tu entorno de código. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter!

Ahora ejecuta

    unzip mario-more.zip

para crear una carpeta llamada `mario-more`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm mario-more.zip

y responder con "y" seguido de Enter en la ventana para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd mario-more

seguido de Enter para moverte(y abrir) ese directorio. Tu promt ahora debería parecerse a esto.

    mario-more/ $

Si todo fue exitoso, deberías ejecutar

    ls

y ver un archivo llamado `mario.c`. Ejecutar `code mario.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.

## Mundo 1-1

Hacia el comienzo del Mundo 1-1 en el juego Super Mario Brothers de Nintendo, Mario debe saltar sobre pirámides adyacentes de bloques, como se muestra a continuación.

![captura de pantalla de Mario saltando sobre pirámides adyacentes](https://cs50.harvard.edu/x/2023/psets/1/mario/more/pyramids.png)

Creemos esas pirámides en C, aunque sea en texto, usando el símbolo `#` para los bloques, a la altura de lo que se muestra a continuación. Cada ladrillo es un poco más alto que ancho, por lo que las propias pirámides serán más altas que anchas.

       #  #
      ##  ##
     ###  ###
    ####  ####

El programa que escribirás se llamará `mario`. Y permitamos al usuario decidir exactamente qué tan alta debería ser la pirámide solicitándoles un número entero positivo entre, digamos, 1 y 8, inclusive.

Así es como podría funcionar el programa si el usuario ingresa `8` cuando se le solicita:

    $ ./mario
    Altura: 8
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########

Así es como podría funcionar el programa si el usuario ingresa `4` cuando se le solicita:

    $ ./mario
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Y así es como podría funcionar el programa si el usuario ingresa `2` cuando se le solicita:

    $ ./mario
    Altura: 2
     #  #
    ##  ##

Y así es como podría funcionar el programa si el usuario ingresa `1` cuando se le solicita:

    $ ./mario
    Altura: 1
    #  #

Si el usuario no ingresa un número entero positivo entre 1 y 8, inclusive, cuando se le solicita, el programa debe solicitar al usuario de nuevo hasta que coopere:

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Observe que el ancho de la "brecha" entre las pirámides adyacentes es igual al ancho de dos símbolos `#`, independientemente de la altura de las pirámides.

¡Abre tu archivo `mario.c` para implementar este problema como se describe!

### Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Cómo probar tu código

¿Tu código funciona según lo prescribe al ingresar

- `-1` (u otros números negativos)?
- `0`?
- `1` a `8`?
- `9` u otros números positivos?
- letras o palabras?
- ¿ninguna entrada en absoluto, cuando solo presionas Enter?

También puedes ejecutar la siguiente línea de comando para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilarlo y probarlo también!

    check50 cs50/problems/2023/x/mario/more

Ejecuta la siguiente línea de comando para evaluar el estilo de tu código usando `style50`.

    style50 mario.c

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/mario/more