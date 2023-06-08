Filtro
======

Implemente un programa que aplique filtros a los BMP, según se indica a continuación:

    $ ./filter -r IMAGE.bmp REFLECTED.bmp

donde `IMAGE.bmp` es el nombre de un archivo de imagen y `REFLECTED.bmp` es el nombre que se le da a un archivo de imagen de salida, que ahora está reflejado.

Antecedentes
------------

### Mapas de bits o BMP

Quizás la forma más simple de representar una imagen es con una cuadrícula de píxeles (es decir, puntos), cada uno de los cuales puede ser de un color diferente. Para imágenes en blanco y negro, por lo tanto, necesitamos 1 bit por píxel, ya que 0 podría representar negro y 1 podría representar blanco, como se muestra a continuación.

![un mapa de bits simple](https://cs50.harvard.edu/x/2023/psets/4/filter/less/bitmap.png)

En este sentido, entonces, una imagen es solo un mapa de bits (es decir, un mapa de bits). Para imágenes más coloridas, simplemente se necesitan más bits por píxel. Un formato de archivo (como BMP, JPEG o PNG) que admite "color de 24 bits" utiliza 24 bits por píxel. (BMP admite en realidad colores de 1, 4, 8, 16, 24 y 32 bits).

Un BMP de 24 bits usa 8 bits para indicar la cantidad de rojo en el color de un píxel, 8 bits para indicar la cantidad de verde en el color de un píxel y 8 bits para indicar la cantidad de azul en el color de un píxel. Si alguna vez ha oído hablar de un color RGB, bueno, ahí lo tiene: rojo, verde, azul.

Si los valores R, G y B de algún píxel en un BMP son, digamos, `0xff`, `0x00` y `0x00` en hexadecimal, ese píxel es puramente rojo, ya que `0xff` (también conocido como `255` en decimal) implica "mucho rojo", mientras que `0x00` y `0x00` implican "sin verde" y "sin azul", respectivamente.

### Un poco (más técnico) sobre el mapa de bits

Recuerde que un archivo es simplemente una secuencia de bits, organizados de alguna manera. Un archivo BMP de 24 bits, entonces, es esencialmente solo una secuencia de bits, de los cuales casi todos los 24 representan el color de algún píxel. Pero un archivo BMP también contiene algo de "metadatos", información como la altura y el ancho de una imagen. Esa metadata se almacena al principio del archivo en forma de dos estructuras de datos que generalmente se denominan "encabezados", que no deben confundirse con los archivos de encabezado de C. (Por cierto, estos encabezados han evolucionado con el tiempo. Este problema utiliza la última versión del formato BMP de Microsoft, 4.0, que se lanzó con Windows 95.)

El primero de estos encabezados, llamado `BITMAPFILEHEADER`, mide 14 bytes. (Recuerde que 1 byte equivale a 8 bits.) El segundo de estos encabezados, llamado `BITMAPINFOHEADER`, mide 40 bytes. Inmediatamente después de estos encabezados se encuentra el mapa de bits real: una matriz de bytes, triples de los cuales representan el color de un píxel. Sin embargo, BMP almacena estos triples al revés (es decir, como BGR), con 8 bits para azul, seguidos de 8 bits para verde, seguidos de 8 bits para rojo. (Algunos BMP también almacenan todo el mapa de bits al revés, con la fila superior de una imagen al final del archivo BMP. Pero hemos almacenado los BMP de este conjunto de problemas como se describe aquí, con la primera fila de cada mapa de bits primero y la última fila al final). En otras palabras, si convirtiéramos la carita sonriente de 1 bit de arriba en una carita sonriente de 24 bits, sustituyendo el negro por rojo, un BMP de 24 bits almacenaría este mapa de bits de la siguiente manera, donde `0000ff` significa rojo y `ffffff` significa blanco. Hemos resaltado en rojo todas las instancias de `0000ff`.

![una cara sonriente en rojo](https://cs50.harvard.edu/x/2023/psets/4/filter/less/red_smile.png)

Debido a que hemos presentado estos bits de izquierda a derecha, de arriba hacia abajo, en 8 columnas, en realidad puedes ver la cara sonriente en rojo si das un paso atrás.

Para ser claros, recuerde que un dígito hexadecimal representa 4 bits. Por lo tanto, `ffffff` en hexadecimal en realidad significa `111111111111111111111111` en binario.

Observe que se puede representar un mapa de bits como una matriz bidimensional de píxeles: donde la imagen es una matriz de filas, cada fila es una matriz de píxeles. De hecho, así es como hemos elegido representar las imágenes de mapa de bits en este problema.

### Filtrado de imágenes

¿Qué significa filtrar una imagen? Puede pensar en el filtrado de una imagen como tomar los píxeles de una imagen original y modificar cada píxel de tal manera que un efecto particular sea evidente en la imagen resultante.

#### Escala de grises

Un filtro común es el filtro "escala de grises", donde tomamos una imagen y queremos convertirla en blanco y negro. ¿Cómo funciona?

Recuerde que si los valores rojo, verde y azul se establecen en `0x00` (hexadecimal para `0`), entonces el píxel es negro. Y si todos los valores se establecen en `0xff` (hexadecimal para `255`), entonces el píxel es blanco. Mientras los valores rojo, verde y azul sean iguales, el resultado será diferentes tonos de gris a lo largo del espectro blanco-negro, con valores más altos que significan tonos de color más claros (más cercanos al blanco) y valores más bajos que significan tonos de color más oscuros (más cerca del negro).

Así que para convertir un píxel en escala de grises, solo necesitamos asegurarnos de que los valores de rojo, verde y azul sean el mismo valor. Pero, ¿cómo sabemos qué valor hacerlos? Bueno, es probable que sea razonable esperar que si los valores originales de rojo, verde y azul fueran todos bastante altos, entonces el nuevo valor también debería ser bastante alto. Y si los valores originales fueran todos bajos, entonces el nuevo valor también debería ser bajo.

De hecho, para garantizar que cada píxel de la nueva imagen tenga el mismo brillo o oscuridad general que la imagen antigua, podemos tomar el promedio de los valores de rojo, verde y azul para determinar qué tono de gris hacer el nuevo píxel.

Si aplica eso a cada píxel en la imagen, el resultado será una imagen convertida a escala de grises.