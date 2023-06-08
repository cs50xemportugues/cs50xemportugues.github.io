Filtrar
======

Implemente un programa que aplique filtros a archivos BMP, como se muestra a continuación.

    $ ./filter -r IMAGE.bmp REFLECTED.bmp
    

donde `IMAGE.bmp` es el nombre del archivo de imagen y `REFLECTED.bmp` es el nombre del archivo de imagen de salida, reflejado.

Antecedentes
----------

### Mapas de bits

Quizás la forma más simple de representar una imagen sea con una cuadrícula de píxeles (es decir, puntos), cada uno de los cuales puede tener un color diferente. Para imágenes en blanco y negro, necesitamos 1 bit por píxel, ya que 0 puede representar negro y 1 puede representar blanco, como se muestra a continuación.

![un mapa de bits simple](https://cs50.harvard.edu/x/2023/psets/4/filter/more/bitmap.png)

En este sentido, una imagen es simplemente un mapa de bits (es decir, un mapa de bits). Para imágenes más coloridas, simplemente se necesitan más bits por píxel. Un formato de archivo (como [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG) o [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) que admite "color de 24 bits" utiliza 24 bits por píxel (BMP admite en realidad 1, 4, 8, 16, 24 y 32 bits por color).

Un archivo BMP de 24 bits usa 8 bits para indicar la cantidad de rojo en el color de un píxel, 8 bits para indicar la cantidad de verde en el color de un píxel y 8 bits para indicar la cantidad de azul en el color de un píxel. Si alguna vez ha oído hablar del color RGB, bueno, ahí lo tiene: rojo, verde, azul.

Si los valores R, G y B de algún píxel en un BMP son, por ejemplo, `0xff`, `0x00` y `0x00` en hexadecimal, ese píxel es simplemente rojo, ya que `0xff` (también conocido como `255` en decimal) implica "mucho rojo", mientras que `0x00` y `0x00` significan "no verde" y "no azul", respectivamente.

### Un Poco (más técnico) sobre Mapas de Bits

Recuerde que un archivo es simplemente una secuencia de bits, ordenados de alguna manera. Un archivo BMP de 24 bits, entonces, es esencialmente una secuencia de bits, (casi) cada 24 de los cuales suelen representar el color de algún píxel. Pero un archivo BMP también contiene algunos "metadatos", información como la altura y el ancho de una imagen. Estos metadatos se almacenan al comienzo del archivo en forma de dos estructuras de datos generalmente denominadas "encabezados", que no deben confundirse con los archivos de encabezado de C. (Por cierto, estos encabezados han evolucionado con el tiempo. Este problema usa la última versión del formato BMP de Microsoft, 4.0, que debutó con Windows 95).

El primero de estos encabezados, llamado `BITMAPFILEHEADER`, tiene una longitud de 14 bytes. (Recuerde que 1 byte equivale a 8 bits). El segundo de estos encabezados, llamado `BITMAPINFOHEADER`, tiene una longitud de 40 bytes. Inmediatamente después de estos encabezados se encuentra el mapa de bits real: una matriz de bytes, triples de los cuales representan el color de un píxel. Sin embargo, BMP almacena estos triples al revés (es decir, como BGR), con 8 bits para azul, seguidos de 8 bits para verde y, finalmente, 8 bits para rojo. (Algunos BMP también almacenan todo el mapa de bits del revés, con la fila superior de una imagen al final del archivo BMP. Pero hemos almacenado los BMP de este conjunto de problemas como se describe aquí, con la fila superior de cada mapa de bits al principio y la inferior al final). En otras palabras, si convirtiéramos el emoticón de 1 bit anterior en un emoticón de 24 bits, sustituyendo el rojo por el negro, un BMP de 24 bits almacenaría este mapa de bits de la siguiente manera, donde `0000ff` significa rojo y `ffffff` significa blanco; hemos destacado en rojo todas las instancias de `0000ff`.

![una sonrisa roja](https://cs50.harvard.edu/x/2023/psets/4/filter/more/red_smile.png)

Debido a que hemos presentado estos bits de izquierda a derecha, de arriba a abajo, en 8 columnas, realmente puede ver el emoticono rojo si da un paso atrás.

Para ser claros, recuerde que un dígito hexadecimal representa 4 bits. Por lo tanto, `ffffff` en hexadecimal realmente significa `111111111111111111111111` en binario.

Observe que se podría representar un mapa de bits como una matriz bidimensional de píxeles: donde la imagen es una matriz de filas, cada fila es una matriz de píxeles. De hecho, eso es lo que hemos elegido para representar imágenes BMP en este problema.

### Filtrado de Imágenes

¿Qué significa filtrar una imagen? Se puede pensar que al filtrar una imagen se toman los píxeles de una imagen original y se modifica cada píxel de tal manera que un efecto particular es evidente en la imagen resultante.

#### Escala de Grises

Un filtro común es el filtro de "escala de grises", en el que tomamos una imagen y queremos convertirla a blanco y negro. ¿Cómo funciona?

Recuerda que si los valores rojo, verde y azul están todos establecidos en `0x00` (hexadecimal para `0`), entonces el píxel es negro. Y si todos los valores están establecidos en `0xff` (hexadecimal para `255`), entonces el píxel es blanco. Mientras los valores de rojo, verde y azul estén iguales, el resultado será tonos de gris que van desde el espectro de blanco a negro, con valores más altos que indican tonos más claros (más cerca del blanco) y valores más bajos que indican tonos más oscuros (más cerca del negro).

Por lo tanto, para convertir un píxel a tono de gris, solo necesitamos asegurarnos de que los valores de rojo, verde y azul sean iguales. Pero, ¿cómo sabemos qué valor darles? Bueno, probablemente es razonable esperar que si los valores de rojo, verde y azul originales eran bastante altos, entonces el nuevo valor también debería ser bastante alto. Y si los valores originales eran bajos, entonces el nuevo valor también debería ser bajo.

De hecho, para garantizar que cada píxel de la nueva imagen tenga el mismo brillo o oscuridad general que la vieja imagen, podemos tomar el promedio de los valores de rojo, verde y azul para determinar qué tono de gris hacer para el nuevo píxel.

Al aplicar eso a cada píxel en la imagen, el resultado será una imagen convertida a escala de grises.

#### Reflejo

Algunos filtros también pueden mover los píxeles. Reflejar una imagen, por ejemplo, es un filtro en el que la imagen resultante es lo que se obtendría al colocar la imagen original frente a un espejo. Así que cualquier píxel en el lado izquierdo de la imagen terminaría en el lado derecho, y viceversa.

Note que todos los píxeles originales de la imagen original seguirán presentes en la imagen reflejada, solo que esos píxeles pueden haberse rearrangeado a otro lugar en la imagen.

#### Difuminado

Hay varias maneras de crear el efecto de difuminado o suavizado en una imagen. Para este problema, usaremos el "difuminado de caja", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor promediando los valores de color de los píxeles adyacentes.

Considera la siguiente cuadrícula de píxeles, donde hemos numerado cada píxel.

![a grid of pixels](https://cs50.harvard.edu/x/2023/psets/4/filter/more/grid.png)

El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que están dentro de 1 fila y columna del píxel original (formando una caja 3x3). Por ejemplo, cada uno de los valores de color del píxel 6 se obtendría promediando los valores de color originales de los píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (note que el píxel 6 en sí está incluido en el promedio). De igual manera, los valores de color del píxel 11 se obtendrían promediando los valores de color de los píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.

Para un píxel a lo largo del borde o la esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.

#### Bordes

En algoritmos de inteligencia artificial para procesamiento de imágenes, a menudo es útil detectar bordes en una imagen: líneas en la imagen que crean un límite entre un objeto y otro. Una forma de lograr este efecto es mediante la aplicación del [operador Sobel](https://en.wikipedia.org/wiki/Sobel_operator) a la imagen.

Al igual que con el desenfoque de imágenes, la detección de bordes también funciona tomando cada píxel y modificándolo según la matriz de 3x3 píxeles que rodea ese píxel. Pero en lugar de tomar solo el promedio de los nueve píxeles, el operador Sobel calcula el nuevo valor de cada píxel tomando una suma ponderada de los valores para los píxeles circundantes. Y ya que los bordes entre objetos podrían ocurrir tanto en una dirección vertical como horizontal, realmente se calcularán dos sumas ponderadas: una para detectar bordes en la dirección x, y otra para detectar bordes en la dirección y. En particular, se utilizarán los siguientes dos "núcleos":

![Núcleos Sobel](https://cs50.harvard.edu/x/2023/psets/4/filter/more/sobel.png)

¿Cómo interpretar estos núcleos? En resumen, por cada uno de los tres valores de color para cada píxel, calcularemos dos valores `Gx` e `Gy`. Para calcular `Gx` del valor del canal rojo de un píxel, por ejemplo, tomaremos los valores rojos originales de los nueve píxeles que forman una caja de 3x3 alrededor del píxel, los multiplicaremos cada uno por el valor correspondiente del núcleo `Gx`, y tomaremos la suma de los valores resultantes.

¿Por qué estos valores particulares para el núcleo? En la dirección `Gx`, por ejemplo, estamos multiplicando los píxeles a la derecha del píxel objetivo por un número positivo, y multiplicando los píxeles a la izquierda del píxel objetivo por un número negativo. Cuando tomamos la suma, si los píxeles a la derecha tienen un color similar a los píxeles a la izquierda, el resultado estará cerca de 0 (los números se cancelan). Pero si los píxeles a la derecha son muy diferentes de los píxeles a la izquierda, entonces el valor resultante será muy positivo o muy negativo, indicando un cambio de color que probablemente sea el resultado de un límite entre objetos. Y un argumento similar es válidos para calcular bordes en la dirección `y`.

Usando estos núcleos, podemos generar un valor `Gx` e `Gy` para cada uno de los canales rojo, verde y azul de un píxel. Pero cada canal solo puede tener un valor, no dos: así que necesitamos una forma de combinar `Gx` y `Gy` en un solo valor. El algoritmo del filtro Sobel combina `Gx` e `Gy` en un valor final calculando la raíz cuadrada de `Gx^2 + Gy^2`. Y ya que los valores de los canales solo pueden tomar valores enteros de 0 a 255, asegúrate de que el valor resultante sea redondeado al número entero más cercano y limitado a 255.

¿Y qué pasa con el manejo de píxeles en el borde o en la esquina de la imagen? Hay muchas formas de manejar los píxeles en el borde, pero para los propósitos de este problema, te pediremos que trates la imagen como si hubiera un borde negro sólido de 1 píxel alrededor del borde de la imagen: por lo tanto, intentar acceder a un píxel más allá del borde de la imagen debe ser tratado como un píxel negro sólido (valores de 0 para cada uno de rojo, verde y azul). Esto efectivamente ignorará esos píxeles de nuestros cálculos de `Gx` y `Gy`.

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

### `helpers.h`

A continuación, echemos un vistazo a `helpers.h`. Este archivo es bastante corto y solo proporciona los prototipos de función para las funciones que vimos anteriormente.

Aquí, tenga en cuenta el hecho de que cada función toma como argumento una matriz 2D llamada `image`, donde `image` es una matriz de `height` filas y cada fila es a su vez otra matriz de `width` `RGBTRIPLE`s. Entonces, si `image` representa toda la imagen, entonces `image [0]` representa la primera fila y `image [0] [0]` representa el píxel en la esquina superior izquierda de la imagen.

### `helpers.c`

Ahora, abra `helpers.c`. Aquí es donde debe ir la implementación de las funciones declaradas en `helpers.h`. Pero tenga en cuenta que, en este momento, ¡faltan las implementaciones! Esta parte depende de ti.

### `Makefile`

Finalmente, veamos `Makefile`. Este archivo especifica qué debe suceder cuando ejecutamos un comando de terminal como `make filter`. Mientras que los programas que puede haber escrito antes estaban limitados a solo un archivo, `filter` parece usar múltiples archivos: `filter.c` y `helpers.c`. Entonces, deberemos decirle a `make` cómo compilar este archivo.

Intenta compilar `filter` por ti mismo yendo a tu terminal y ejecutando

    $ make filter
    

Luego, puede ejecutar el programa ejecutando:

    $ ./filter -g images/yard.bmp out.bmp
    

lo que lleva la imagen en `images/yard.bmp` y genera una nueva imagen llamada `out.bmp` después de pasar los píxeles a través de la función `grayscale`. Sin embargo, `grayscale` aún no hace nada, por lo que la imagen de salida debería verse igual que el patio original.

Especificación
-------------

Implemente las funciones en `helpers.c` para que un usuario pueda aplicar filtros de escala de grises, reflexión, desenfoque o detección de bordes a sus imágenes.

*   La función `grayscale` debe tomar una imagen y convertirla en una versión en blanco y negro de la misma imagen.
*   La función `reflect` debe tomar una imagen y reflejarla horizontalmente.
*   La función `blur` debe tomar una imagen y convertirla en una versión desenfocada de la misma imagen.
*   La función `edges` debe tomar una imagen y resaltar los bordes entre objetos, según el operador Sobel.

No debe modificar ninguna de las estructuras de función ni ninguna otro archivo que no sea `helpers.c`.

Recorrido
-----------

**Tenga en cuenta que hay 5 videos en esta lista de reproducción.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/vsOsctDernw?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382OwvMbZuaMGtD9wZkhnhYj"></iframe></div>

Uso
---

Su programa debería comportarse según los ejemplos a continuación. `INFILE.bmp` es el nombre de la imagen de entrada y `OUTFILE.bmp` es el nombre de la imagen resultante después de que se haya aplicado un filtro.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -e INFILE.bmp OUTFILE.bmp
```

Sugerencias
-----------

*   Los valores de los componentes `rgbtRed`, `rgbtGreen` y `rgbtBlue` de un píxel son todos números enteros, así que asegúrese de redondear cualquier número de punto flotante al entero más cercano al asignarlos a un valor de píxel.

Pruebas
-------

¡Asegúrese de probar todos sus filtros en los archivos de mapa de bits de muestra proporcionados!

Ejecute lo siguiente para evaluar la corrección de su código utilizando `check50`. Pero asegúrese de compilarlo y probarlo usted mismo también.

    check50 cs50/problems/2023/x/filter/more
    

Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`.

    style50 helpers.c
    

Cómo enviar
-----------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50 / problems / 2023 / x / filter / more

