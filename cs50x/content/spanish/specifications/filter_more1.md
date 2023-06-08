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