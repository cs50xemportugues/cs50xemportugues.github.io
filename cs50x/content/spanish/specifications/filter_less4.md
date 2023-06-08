Entendiendo
------------

Ahora, echemos un vistazo a algunos de los archivos que se proporcionan como código de distribución para que puedas comprender lo que hay dentro de ellos.

### `bmp.h`

Abre `bmp.h` (al hacer doble clic en él en el navegador de archivos) y revisa.

Verás definiciones de los encabezados que hemos mencionado (`BITMAPINFOHEADER` y `BITMAPFILEHEADER`). Además, ese archivo define `BYTE`, `DWORD`, `LONG` y `WORD`, tipos de datos que se encuentran normalmente en el mundo de la programación de Windows. Observa cómo son solo alias para primitivas que ya conoces (con suerte). Parece que `BITMAPFILEHEADER` y `BITMAPINFOHEADER` utilizan estos tipos.

Quizás lo más importante para ti, este archivo también define una `struct` llamada `RGBTRIPLE` que, simplemente, "encapsula" tres bytes: uno azul, uno verde y uno rojo (el orden, recuerda, en el que esperamos encontrar triples RGB en el disco).

¿Por qué son útiles estas `struct`? Bueno, recuerda que un archivo es solo una secuencia de bytes (o, en última instancia, bits) en el disco. Pero esos bytes suelen estar ordenados de tal manera que los primeros representan algo, los siguientes representan otra cosa, y así sucesivamente. Los "formatos de archivo" existen porque el mundo ha estandarizado qué bytes significan qué. Ahora, podríamos simplemente leer un archivo del disco en RAM como un gran conjunto de bytes. Y podríamos recordar que el byte en `array[i]` representa una cosa, mientras que el byte en `array[j]` representa otra. ¿Pero por qué no darle nombres a algunos de esos bytes para que podamos recuperarlos de la memoria más fácilmente? Eso es precisamente lo que las `struct` en `bmp.h` nos permiten hacer. En lugar de pensar en algún archivo como una larga secuencia de bytes, podemos pensar en ella como una secuencia de `struct`.

### `filter.c`

Ahora, abramos `filter.c`. Este archivo ya está escrito para ti, pero hay un par de puntos importantes que vale la pena señalar aquí.

En primer lugar, observa la definición de `filters` en la línea 10. Esa cadena le indica al programa cuáles son los argumentos permitidos en la línea de comando: `b`, `g`, `r`, y `s`. Cada uno de ellos especifica un filtro diferente que podríamos aplicar a nuestras imágenes: desenfoque, escala de grises, reflejo y sepia.

Las siguientes líneas abren un archivo de imagen, se aseguran de que sea un archivo BMP y leen toda la información de píxeles en una matriz 2D llamada `image`.

Desplázate hacia abajo hasta el `switch` que comienza en la línea 101. Observa que, dependiendo de qué filtro hayamos elegido, se llama a una función diferente: si el usuario elige el filtro `b`, el programa llama a la función `blur`; si `g`, entonces se llama a `grayscale`; si `r`, entonces se llama a `reflect`; y si `s`, entonces se llama a `sepia`. Observa, también, que cada una de estas funciones toma como argumentos la altura de la imagen, el ancho de la imagen y la matriz 2D de píxeles.

Estas son las funciones que implementarás pronto. Como puedes imaginar, el objetivo es que cada una de estas funciones edite la matriz 2D de píxeles de tal manera que se aplique el filtro deseado a la imagen.

Las últimas líneas del programa toman la `image` resultante y las escriben en un nuevo archivo de imagen.

### `helpers.h`

A continuación, revisa `helpers.h`. Este archivo es bastante corto y solo proporciona los prototipos de función para las funciones que viste antes.

Aquí, ten en cuenta que cada función toma una matriz 2D llamada `image` como argumento, donde `image` es una matriz de `height` muchas filas, y cada fila es a su vez otra matriz de `width` muchos `RGBTRIPLE`s. Entonces, si `image` representa la imagen completa, entonces `image[0]` representa la primera fila, y `image[0][0]` representa el píxel en la esquina superior izquierda de la imagen.

### `helpers.c`

Ahora, abre `helpers.c`. Aquí es donde pertenece la implementación de las funciones declaradas en `helpers.h`. Pero ten en cuenta que, ¡ahora mismo, faltan las implementaciones! Esta parte depende de ti.

### `Makefile`

Finalmente, echemos un vistazo a `Makefile`. Este archivo especifica qué debería pasar cuando ejecutamos un comando de terminal como `make filter`. Mientras que los programas que hayas escrito antes estaban confinados a un solo archivo, `filter` parece usar varios archivos: `filter.c` y `helpers.c`. Entonces, tendremos que decirle a `make` cómo compilar este archivo.

Intenta compilar `filter` por ti mismo yendo a la terminal y ejecutando

    $ make filter
    

Luego, puedes ejecutar el programa:

    $ ./filter -g images/yard.bmp out.bmp
    

lo que toma la imagen en `images/yard.bmp` y genera una nueva imagen llamada `out.bmp` después de pasar los píxeles a través de la función `grayscale`. Sin embargo, `grayscale` no hace nada todavía, por lo que la imagen de salida debería verse igual que el patio original.