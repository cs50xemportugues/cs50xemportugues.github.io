Recuperar
=========

Implemente un programa que recupere imágenes JPEG de una imagen forense, como se indica a continuación.

    $ ./recover card.raw
    

Antecedentes
------------

En previsión de este problema, hemos estado tomando fotos alrededor del campus en los últimos días, todas las cuales se guardaron en una cámara digital como JPEG en una tarjeta de memoria. ¡Desafortunadamente, de alguna manera los eliminamos todos! Afortunadamente, en el mundo de la informática, "eliminado" no suele significar "eliminado" tanto como "olvidado". Aunque la cámara insiste en que la tarjeta está ahora en blanco, estamos bastante seguros de que eso no es del todo cierto. De hecho, esperamos (¡o mejor dicho, esperamos!) que puedas escribir un programa que recupere las fotos para nosotros.

Aunque los JPEG son más complicados que los BMP, los JPEG tienen "firmas", patrones de bytes que los pueden distinguir de otros formatos de archivo. Específicamente, los primeros tres bytes de los JPEG son

    0xff 0xd8 0xff
    

del primer byte al tercer byte, de izquierda a derecha. El cuarto byte, por otro lado, es `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee` o `0xef`. En otras palabras, los primeros cuatro bits del cuarto byte son `1110`.

Es probable que, si se encuentra este patrón de cuatro bytes en un medio conocido por almacenar fotos (por ejemplo, mi tarjeta de memoria), estos marquen el inicio de un JPEG. Para ser justos, es posible encontrar estos patrones en un disco simplemente por casualidad, por lo que la recuperación de datos no es una ciencia exacta.

Afortunadamente, las cámaras digitales tienden a almacenar fotografías de manera contigua en tarjetas de memoria, donde cada foto se almacena inmediatamente después de la anterior. Por lo tanto, el inicio de un JPEG generalmente marca el final de otro. Sin embargo, las cámaras digitales a menudo inicializan las tarjetas con un sistema de archivos FAT cuyo "tamaño de bloque" es de 512 bytes (B). La implicación es que estas cámaras solo escriben en esas tarjetas en unidades de 512 B. Una foto que ocupa 1 MB (es decir, 1,048,576 B) ocupa 1048576 ÷ 512 = 2048 "bloques" en una tarjeta de memoria. ¡Pero lo mismo sucede con una foto que es un byte más pequeña (es decir, 1,048,575 B)! El espacio desperdiciado en el disco se llama "espacio muerto". Los investigadores forenses a menudo buscan restos de datos sospechosos en el espacio muerto.

La implicación de todos estos detalles es que usted, el investigador, probablemente pueda escribir un programa que itere sobre una copia de mi tarjeta de memoria, buscando las firmas de los JPEG. Cada vez que encuentre una firma, puede abrir un archivo nuevo para escribir y comenzar a llenar ese archivo con bytes de mi tarjeta de memoria, cerrando ese archivo solo una vez que encuentre otra firma. Además, en lugar de leer los bytes de la tarjeta de memoria uno por uno, puede leer 512 de ellos a la vez en un búfer por eficiencia. Gracias a FAT, puede confiar en que las firmas de los JPEG estarán "alineadas con el bloque". Es decir, solo necesita buscar esas firmas en los primeros cuatro bytes de un bloque.

Por supuesto, como los JPEG pueden abarcar bloques contiguos, el último byte de un JPEG puede no estar al final de un bloque. Recuerde la posibilidad del espacio muerto. Pero no se preocupe. Debido a que esta tarjeta de memoria era nueva cuando comencé a tomar fotos, es probable que el fabricante la haya "cero" (es decir, llenado con 0), por lo que cualquier espacio muerto estará lleno de 0. Está bien si esos 0 finales terminan en los JPEG que recuperas; aún deberían ser visibles.

Ahora, solo tengo una tarjeta de memoria, ¡pero hay muchos de ustedes! Y, por lo tanto, he creado una "imagen forense" de la tarjeta, almacenando su contenido, byte por byte, en un archivo llamado `card.raw`. Para que no pierda tiempo iterando sobre millones de 0 innecesariamente, solo he creado una imagen de los primeros pocos megabytes de la tarjeta de memoria. Pero finalmente deberías encontrar que la imagen contiene 50 JPEG.

Empezando
---------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en su ventana del terminal y ejecute `cd` por sí solo. Debería encontrar que el indicador de la ventana del terminal se parece al siguiente:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/4/recover.zip
    

para descargar un archivo ZIP llamado `recover.zip` en su espacio de código.

Luego ejecute

    unzip recover.zip
    

para crear una carpeta llamada `recover`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm recover.zip
    

y responder con "y" seguido de Enter para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd recover
    

seguido de Enter para moverse (es decir, abrir) en ese directorio. Tu indicador de comando ahora debería parecerse a lo siguiente.

    recover/ $
    

Ejecuta `ls` por sí solo y deberías ver dos archivos: `recover.c` y 'card.raw\`.

Especificaciones
---------------

Implemente un programa llamado `recover` que recupere JPEG de una imagen forense.

*   Implemente su programa en un archivo llamado `recover.c` en un directorio llamado `recover`.
*   Su programa debe aceptar exactamente un argumento de línea de comando, el nombre de una imagen forense de la que recuperar los JPEG.
*   Si su programa no se ejecuta con exactamente un argumento de línea de comando, debe recordar al usuario el uso correcto y `main` debe devolver `1`.
*   Si no se puede abrir la imagen forense para lectura, su programa debe informar al usuario de esto y `main` debe devolver `1`.
*   Los archivos que genere deben tener cada uno el nombre `###.jpg`, donde `###` es un número decimal de tres dígitos, comenzando por `000` para la primera imagen y contando hacia arriba.
*   Si su programa usa `malloc`, no debe perder memoria.