Mario
=====

![captura de pantalla de Mario saltando por una pirámide](https://cs50.harvard.edu/x/2023/psets/6/mario/less/pyramid.png)

Implementa un programa que imprima una media pirámide de una altura específica, como se muestra a continuación.

    $ python mario.py
    Altura: 4
       #
      ##
     ###
    ####
    

Comenzando
---------------

Ingresa en [code.cs50.io](https://code.cs50.io/), haz clic en tu ventana de terminal y ejecuta `cd`. Deberías encontrar que el indicador de tu ventana de terminal se parece al siguiente:

    $
    

A continuación, ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-mario-less.zip
    

para descargar un archivo ZIP llamado `sentimental-mario-less.zip` en tu espacio de trabajo.

Luego ejecuta

    unzip sentimental-mario-less.zip
    

para crear una carpeta llamada `sentimental-mario-less`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm sentimental-mario-less.zip
    

y responde con "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd sentimental-mario-less
    

seguido por Enter para entrar (es decir, abrir) ese directorio. Tu prompt ahora debería parecerse al siguiente.

    sentimental-mario-less/ $
    

Ejecuta `ls` por sí solo y deberías ver un `mario.py`. Si tienes algún problema, sigue estos mismos pasos de nuevo y ve si puedes determinar dónde estás equivocado.

Especificaciones
-------------

*   Escribe, en un archivo llamado `mario.py`, un programa que recrea la media pirámide usando hashtags (`#`) para los bloques, exactamente como lo hiciste en el [Problem Set 1](../../../1/), excepto que esta vez tu programa deberá estar escrito en Python.
*   Para hacer las cosas más interesantes, primero solicita al usuario con `get_int` la altura de la media pirámide, un entero positivo entre `1` y `8`, inclusive.
*   Si el usuario no proporciona un entero positivo que no sea mayor que `8`, debe mostrar un mensaje pidiendo al usuario que lo haga de nuevo.
*   Luego genera (con la ayuda de `print` y uno o más bucles) la media pirámide deseada.
*   Asegúrate de alinear la esquina inferior izquierda de tu media pirámide con el borde izquierdo de tu ventana de terminal.

Uso
-----

Tu programa debería comportarse como se muestra en el ejemplo siguiente.

    $ python mario.py
    Altura: 4
       #
      ##
     ###
    ####
    

Probando
-------

Si bien `check50` está disponible para este problema, se recomienda que primero pruebes tu código por tu cuenta para cada uno de los siguientes casos.

* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. Escribe `-1` y presiona Enter. Tu programa debería rechazar esta entrada como inválida y pedirle al usuario que escriba otro número.
* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. Escribe `0` y presiona Enter. Tu programa debería rechazar esta entrada como inválida y pedirle al usuario que escriba otro número.
* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. Escribe `1` y presiona Enter. Tu programa debería generar la salida siguiente. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

<pre>
#
</pre>  

* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. Escribe `2` y presiona Enter. Tu programa debería generar la salida siguiente. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

<pre>
 #
##
</pre> 

* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. Escribe `8` y presiona Enter. Tu programa debería generar la salida siguiente. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

<pre>
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
</pre>

* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. Escribe `9` y presiona Enter. Tu programa debería rechazar esta entrada como inválida y pedirle al usuario que escriba otro número. Luego escribe `2` y presiona Enter. Tu programa debería generar la salida siguiente. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

<pre>
 #
##
</pre> 

* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. Escribe `foo` y presiona Enter. Tu programa debería rechazar esta entrada como inválida y pedirle al usuario que escriba otro número.
* Ejecuta tu programa como `python mario.py` y espera a que te solicite la entrada. No escribas nada y presiona Enter. Tu programa debería rechazar esta entrada como inválida y pedirle al usuario que escriba otro número.

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilarlo y probarlo por tu cuenta también!

    check50 cs50/problems/2023/x/sentimental/mario/less
    

Ejecuta lo siguiente para evaluar el estilo de tu código utilizando `style50`.

    style50 mario.py
    

Cómo enviar
-------------

En la terminal, escribe lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/sentimental/mario/less"