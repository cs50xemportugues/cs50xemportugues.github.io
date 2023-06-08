Corrector Ortográfico
=====================

<div class="alert" data-alert="danger" role="alert"><p><strong>¡Asegúrate de leer esta especificación en su totalidad antes de comenzar, para que sepas qué hacer y cómo hacerlo!</strong></p></div>

En este problema, vas a implementar un programa que corrija la ortografía de un archivo usando una tabla hash, similar a esto, a través del siguiente comando.

    $ ./speller texts/lalaland.txt
    PALABRAS MAL ESCRITAS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    PALABRAS MAL ESCRITAS:
    PALABRAS EN EL DICCIONARIO:
    PALABRAS EN TEXTO:
    TIEMPO EN CARGAR:
    TIEMPO EN COMPROBAR:
    TIEMPO EN DIMENSIONAR:
    TIEMPO EN DESCARGAR:
    TIEMPO EN TOTAL:
    

Comencemos
-----------

Inicia sesión en [code.cs50.io](https://code.cs50.io/), haz clic en la ventana de tu terminal y ejecuta `cd`. Deberías ver que el resultado en tu terminal es el siguiente:

    $
    

A continuación, ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/5/speller.zip
    

para descargar un archivo ZIP llamado `speller.zip` en tu espacio de trabajo.

Después, ejecuta 

    unzip speller.zip
    

para crear una carpeta llamada `speller`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm speller.zip
    

y luego "y" seguido de "Enter" para eliminar el archivo ZIP que descargaste.

Ahora escribe 

    cd speller
    

seguido de "Enter" para ingresar (es decir, abrir) esa carpeta. Tu terminal debería ahora ser similar a lo siguiente:

    speller/ $
    

Ejecuta `ls` por si mismo, y deberías ver algunos archivos y carpetas:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
    

Si tienes algún problema, sigue estos mismos pasos nuevamente y determina en qué punto te equivocaste.