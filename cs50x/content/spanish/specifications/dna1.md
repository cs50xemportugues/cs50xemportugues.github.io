ADN
===

Implemente un programa que identifique a una persona en función de su ADN, como se muestra a continuación.

    $ python dna.py databases/large.csv sequences/5.txt
    Lavender
    

Para empezar
---------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en la ventana del terminal y ejecute `cd` por sí solo. Debería ver que la ventana del terminal muestra lo siguiente:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/6/dna.zip
    

para descargar un archivo ZIP llamado `dna.zip` en su espacio de trabajo.

Luego, ejecute

    unzip dna.zip
    

para crear una carpeta llamada `dna`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm dna.zip
    

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd dna
    

seguido de Enter para moverse (es decir, abrir) a ese directorio. Su indicador denotaera el siguiente

    dna/ $
    

Ejecute `ls` por sí solo y debería ver algunos archivos y carpetas:

    databases/ dna.py sequences/
    

Si tiene algún problema, siga estos mismos pasos de nuevo y vea si puede determinar dónde se equivocó.