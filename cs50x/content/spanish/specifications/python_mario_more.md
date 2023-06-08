Mario
=====

![Captura de pantalla de Mario saltando una pirámide](https://cs50.harvard.edu/x/2023/psets/6/mario/more/pyramids.png)

Implementar un programa que imprima una doble media pirámide con una altura específica, según se indica a continuación.

    $ python mario.py
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####
    

Empezando
---------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), luego haga clic en la ventana de su terminal y ejecute `cd`. Debería ver que el indicador de su ventana de terminal se parece a lo siguiente:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-mario-more.zip
    

para descargar un archivo ZIP llamado `sentimental-mario-more.zip` en su espacio de codificación.

Luego, ejecute

    unzip sentimental-mario-more.zip
    

para crear una carpeta llamada `sentimental-mario-more`. Ya no necesita el archivo ZIP, así que puede ejecutar

    rm sentimental-mario-more.zip
    

y responda con "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd sentimental-mario-more
    

seguido de Enter para moverse dentro de (es decir, abrir) ese directorio. Su prompt debería parecerse a lo siguiente.

    sentimental-mario-more/ $
    

Ejecute `ls` por sí solo y debería ver `mario.py`. Si encuentra algún problema, siga estos mismos pasos nuevamente y vea si puede determinar en qué se equivocó.

Especificaciones
-------------

*   Escriba, en un archivo llamado `mario.py`, un programa que reemplace estas medias pirámides usando signos de número (`#`) para los bloques, exactamente como lo hizo en [Problem Set 1](../../../1/), excepto que su programa esta vez debe estar escrito en Python.
*   Para hacer las cosas más interesantes, primero solicite al usuario con `get_int` la altura de la media pirámide, un número entero positivo entre `1` y `8`, inclusive. (La altura de las medias pirámides mostradas arriba resulta ser `4`, el ancho de cada media pirámide `4`, con un espacio de tamaño `2` que las separa).
*   Si el usuario no proporciona un número entero positivo no mayor que `8`, debe volver a solicitar lo mismo.
*   Luego, genere (con la ayuda de `print` y uno o más loops) las medias pirámides deseadas.
*   Asegúrese de alinear la esquina inferior izquierda de su pirámide con el borde izquierdo de su ventana de terminal y asegurarse de que haya dos espacios entre las dos pirámides y no hay espacios adicionales después del último conjunto de signos de número en cada fila.

Uso
-----

Su programa debe comportarse según el ejemplo a continuación.

    $ python mario.py
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####
    

Pruebas
-------

Aunque `check50` está disponible para este problema, se recomienda probar primero su código por su cuenta para cada uno de los siguientes casos.

*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. Escriba `-1` y presione enter. Su programa debería rechazar esta entrada como inválida, al volver a solicitar al usuario que escriba otro número.
*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. Escriba `0` y presione enter. Su programa debería rechazar esta entrada como inválida, al volver a solicitar al usuario que escriba otro número.
*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. Escriba `1` y presione enter. Su programa debería generar la siguiente salida. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.

<pre>
#  #
</pre> 

*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. Escriba `2` y presione enter. Su programa debería generar la siguiente salida. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.

<pre>
 #  #
##  ##
</pre>   

*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. Escriba `8` y presione enter. Su programa debería generar la siguiente salida. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.

<pre>
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
</pre>   

*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. Escriba `9` y presione enter. Su programa debería rechazar esta entrada como inválida, al volver a solicitar al usuario que escriba otro número. Luego, escriba `2` y presione enter. Su programa debería generar la siguiente salida. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.

<pre>
 #  #
##  ##
</pre>

*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. Escriba `foo` y presione enter. Su programa debería rechazar esta entrada como inválida, al volver a solicitar al usuario que escriba otro número.
*   Ejecute su programa como `python mario.py` y espere una solicitud de entrada. No escriba nada y presione enter. Su programa debería rechazar esta entrada como inválida, al volver a solicitar al usuario que escriba otro número.

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilar y probarlo usted mismo también!

    check50 cs50/problems/2023/x/sentimental/mario/more
    

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 mario.py
    

Cómo enviar
-------------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/sentimental/mario/more"