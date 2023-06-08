Introducción
---------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/) y, en su terminal, ejecute el comando `cd` de manera independiente. Debería observar que el prompt de su ventana de terminal se asemejará al siguiente:

    $
    

A continuación, ejecute 

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-more.zip
    

para descargar un archivo ZIP llamado `filter-more.zip` en su entorno de codificación.

Luego, ejecute 

    unzip filter-more.zip
    

para crear una carpeta llamada `filter-more`. Ya no necesita el archivo ZIP, así que ejecute 

    rm filter-more.zip
    

y responda con "y" seguido de Enter para eliminar el archivo ZIP que descargó.

Ahora escriba 

    cd filter-more
    

seguido de Enter para moverse (es decir, abrir) ese directorio. El prompt debería verse de la siguiente manera:

    filter-more/ $
    

Ejecute el comando `ls` y debería ver algunos archivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c`, y `Makefile`. También debería observar una carpeta llamada  `images` con cuatro archivos BMP. Si tiene algún problema, siga estos mismos pasos de nuevo y vea si puede determinar dónde puede haber ocurrido el error.

Comprensión
-------------

Ahora, vamos a echar un vistazo a algunos de los archivos proporcionados como código distribución para comprender qué contienen.

### `bmp.h`

Abra `bmp.h` (dando doble clic en el explorador de archivos) y échele un vistazo.

Verá definiciones de los encabezados mencionados (`BITMAPINFOHEADER` y `BITMAPFILEHEADER`). Además, el archivo define `BYTE`, `DWORD`, `LONG`, y `WORD`, tipos de datos normalmente encontrados en el mundo de la programación de Windows. Note cómo cada uno de ellos es simplemente alias de primitivos con los que (esperamos) ya esté familiarizado. Parece que `BITMAPFILEHEADER` y `BITMAPINFOHEADER` usan estos tipos de datos..

Tal vez lo más importante para usted, este archivo también define una `struct` llamada `RGBTRIPLE`, que de manera sencilla "encapsula" tres bytes: uno azul, uno verde, y uno rojo (el orden en que esperamos encontrar tríos RGB en el disco, recuerde).

¿Por qué son útiles estas `structs`? Bueno, recuerde que un archivo no es más que una secuencia de bytes (o, en última instancia, bits) en el disco. Pero esos bytes están generalmente ordenados de tal forma que los primeros representan algo, los siguientes representan algo más, y así sucesivamente. Los "formatos de archivo" existen porque el mundo ha estandarizado lo que significan los bytes. Ahora bien, podríamos leer un archivo del disco a la memoria como una gran matriz de bytes. Podríamos recordar que el byte en `array[i]` representa una cosa, mientras que el byte en `array[j]` representa otra. Pero ¿por qué no darles nombres a algunos de esos bytes para poder recuperarlos de la memoria con mayor facilidad? Eso es precisamente lo que permiten hacer las `structs` en `bmp.h`. En lugar de pensar en un archivo como una larga secuencia de bytes, podemos pensar en ella como una secuencia de `structs`.

### `filter.c`

Ahora abramos `filter.c`. Este archivo ya ha sido escrito por usted, pero hay un par de puntos importantes que vale la pena señalar.

En primer lugar, observe la definición de `filters` en la línea 10. Esa cadena indica al programa cuáles son los comandos de línea de comandos permitidos: `b`, `e`, `g` y `r`. Cada uno de ellos especifica un filtro diferente que podemos aplicar a nuestras imágenes: desenfoque, detección de bordes, escala de grises y reflexión respectivamente.

Las siguientes líneas abren un archivo de imagen, se aseguran de que sea un archivo BMP, y leen toda la información de los píxeles en una matriz 2D llamada `image`.

Desplácese hacia abajo hasta la declaración `switch` que comienza en la línea 101. Observe que, dependiendo del filtro que hayamos elegido, se llama a una función diferente: si el usuario elige el filtro "b" se llama a la función `blur`; si elige "e" se llama a `edges`; si elige "g" se llama a `grayscale`, y si elige "r", se llama a `reflect`. Observe también que cada una de estas funciones toma como argumentos la altura de la imagen, el ancho de la imagen y la matriz de píxeles 2D.

Estas son las funciones que implementará pronto. Como podrá imaginarse, el objetivo es que cada una de estas funciones edite la matriz 2D de píxeles de manera que el filtro deseado se aplique a la imagen.

Las líneas restantes del programa toman la `image` resultante y la escriben en un nuevo archivo de imagen.