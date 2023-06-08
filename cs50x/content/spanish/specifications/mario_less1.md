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