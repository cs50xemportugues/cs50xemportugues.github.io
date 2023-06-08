Legibilidad
===========

Implementar un programa que calcule el nivel aproximado de grado necesario para comprender un texto, como se muestra a continuación:

    $ python readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3
    

Cómo empezar
---------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en la ventana del terminal y ejecute `cd` por sí solo. Su ventana del terminal debería verse así:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-readability.zip
    

para descargar un archivo ZIP llamado `sentimental-readability.zip` en su espacio de códigos.

Luego ejecute

    unzip sentimental-readability.zip
    

para crear una carpeta llamada `sentimental-readability`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm sentimental-readability.zip
    

y responda con "y" seguido de Enter en el símbolo del sistema para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd sentimental-readability
    

seguido de Enter para moverse (es decir, abrir) en ese directorio. Su ventana de terminal ahora debería verse así:

    sentimental-readability/ $
    

Ejecute `ls` por sí solo y debería ver `readability.py`. Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar en qué se equivocó.