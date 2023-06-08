Comenzando
---------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/) y haga clic en su ventana de terminal. Ejecute `cd` por sí solo y debería notar que el indicador de su ventana de terminal se parece al siguiente:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-less.zip
    

para descargar un archivo ZIP llamado `filter-less.zip` a su espacio de trabajo.

Luego ejecute

    unzip filter-less.zip
    

para crear una carpeta llamada `filter-less`. Ya no necesita el archivo ZIP, así que puede ejecutar

    rm filter-less.zip
    

y responder "y" seguido de Enter en el cuadro de diálogo para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd filter-less
    

seguido de Enter, para moverse (es decir, abrir) ese directorio. Debería notar que el indicador se parece al siguiente:

    filter-less/ $
    

Ejecute `ls` por sí solo y debería ver algunos archivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` y `Makefile`. También debería ver una carpeta llamada `images` con cuatro archivos BMP. ¡Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó!