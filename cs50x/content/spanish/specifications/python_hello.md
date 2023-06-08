Hola
====

Implemente un programa que imprima un saludo simple al usuario, como se muestra a continuación.

    $ python hello.py
    ¿Cuál es tu nombre?
    David
    hello, David
    

Empezando
---------

Ingrese a [code.cs50.io](https://code.cs50.io/), haga clic en su ventana de terminal y ejecute `cd` por sí solo. Debería encontrar que la ventana del terminal se asemeja a la siguiente:

     $
     

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-hello.zip
    

Para descargar un archivo ZIP llamado `sentimental-hello.zip` en su entorno de código.

Luego ejecute

    unzip sentimental-hello.zip
    

Para crear una carpeta llamada `sentimental-hello`. Ya no necesita el archivo ZIP, así que puede ejecutar:

    rm sentimental-hello.zip
    

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd sentimental-hello
    

seguido de Enter para entrar (es decir, abrir) ese directorio. Su símbolo de sistema debe parecerse al siguiente.

    sentimental-hello/ $
     

Ejecute `ls` por sí solo y debería ver `hello.py`. Si tiene algún problema, siga estos mismos pasos de nuevo y vea si puede determinar dónde se equivocó.

Especificación
--------------

Escriba, en un archivo llamado `hello.py`, un programa que solicite al usuario su nombre y luego imprima `hello, so-and-so`, donde `so-and-so` es el nombre proporcionado, exactamente como lo hizo en [Problema Set 1](. /../../1/), excepto que su programa esta vez debe estar escrito en Python.

Uso
---

Su programa debe comportarse de acuerdo con el siguiente ejemplo.

    $ python hello.py
    ¿Cuál es tu nombre?
    Emma
    hello, Emma
    

Pruebas
-------

Mientras `check50` esté disponible para este problema, se recomienda que primero pruebe su código por su cuenta para cada uno de los siguientes casos.

*   Ejecute su programa como `python hello.py` y espere una indicación de entrada. Escriba `David` y presione enter. Su programa debería mostrar `hello, David`.
*   Ejecute su programa como `python hello.py` y espere una indicación de entrada. Escriba `Bernie` y presione enter. Su programa debería mostrar `hello, Bernie`.
*   Ejecute su programa como `python hello.py` y espere una indicación de entrada. Escriba `Carter` y presione enter. Su programa debería mostrar `hello, Carter`.

Ejecute el siguiente código para evaluar la corrección de su código utilizando `check50`. ¡Pero asegúrese de compilar y probarlo usted mismo también!

    check50 cs50/problems/2023/x/sentimental/hello
    

Ejecute el siguiente código para evaluar el estilo de su código utilizando `style50`.

    style50 hello.py
    

Cómo enviar
-----------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/sentimental/hello