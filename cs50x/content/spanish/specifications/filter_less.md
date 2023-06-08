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

#### Sepia

La mayoría de los programas de edición de imágenes tienen un filtro de "sepia", que le da a las imágenes un aspecto antiguo al hacer que toda la imagen se vea un poco rojizo-marrón.

Una imagen se puede convertir en sepia tomando cada píxel y calculando nuevos valores de rojo, verde y azul en función de los valores originales de los tres.

Existen varios algoritmos para convertir una imagen en sepia, pero para este problema, te pediremos que uses el siguiente algoritmo. Para cada píxel, los valores de color de sepia deben calcularse en función de los valores de color originales según lo indicado a continuación.

      sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
      sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
      sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue

Por supuesto, el resultado de cada una de estas fórmulas puede no ser un número entero, pero cada valor se puede redondear al número entero más cercano. También es posible que el resultado de la fórmula sea un número mayor que 255, el valor máximo de un valor de color de 8 bits. En ese caso, los valores de rojo, verde y azul deben estar limitados a 255. Como resultado, podemos garantizar que los valores de rojo, verde y azul resultantes serán números enteros entre 0 y 255, inclusive.

#### Reflexión

Algunos filtros también pueden mover los píxeles. Reflejar una imagen, por ejemplo, es un filtro en el que la imagen resultante es lo que obtendrías colocando la imagen original frente a un espejo. Así, cualquier píxel en el lado izquierdo de la imagen debería estar en el lado derecho, y viceversa.

Ten en cuenta que todos los píxeles originales de la imagen original seguirán presentes en la imagen reflejada, solo que esos píxeles pueden haberse reorganizado para estar en un lugar diferente en la imagen.

#### Difuminado

Existen varias formas de lograr el efecto de difuminado o suavizado de una imagen. Para este problema, usaremos el "difuminado de cuadro", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor promediando los valores de color de los píxeles vecinos.

Considera la siguiente malla de píxeles, donde hemos numerado cada píxel.

![una malla de píxeles](https://cs50.harvard.edu/x/2023/psets/4/filter/less/grid.png)

El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que estén dentro de 1 fila y columna del píxel original (formando un cuadrado de 3x3). Por ejemplo, cada uno de los valores de color para el píxel 6 se obtendría promediando los valores de color originales de los píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (note que el píxel 6 en sí mismo está incluido en la promedio). Del mismo modo, los valores de color para el píxel 11 se obtendrían promediando los valores de color de los píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.

Para un píxel en el borde o la esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.

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

Especificación
-------------

Implemente las funciones en `helpers.c` de manera que el usuario pueda aplicar filtros de escala de grises, sepia, reflexión o desenfoque a sus imágenes.

*   La función `grayscale` debe tomar una imagen y convertirla en una versión en blanco y negro de la misma imagen.
*   La función `sepia` debe tomar una imagen y convertirla en una versión sepia de la misma imagen.
*   La función `reflect` debe tomar una imagen y reflejarla horizontalmente.
*   Por último, la función `blur` debe tomar una imagen y convertirla en una versión desenfocada de la misma imagen.

No se deben modificar ninguna de las firmas de las funciones, ni se deben modificar ningún otro archivo que no sea `helpers.c`.

Aplicación
-----

El programa debe comportarse según los siguientes ejemplos. `INFILE.bmp` es el nombre de la imagen de entrada y `OUTFILE.bmp` es el nombre de la imagen resultante después de que se ha aplicado un filtro.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -s INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```

Pistas
-----

*  Los valores de los componentes `rgbtRed`, `rgbtGreen` y `rgbtBlue` de un píxel son todos enteros, por lo que asegúrese de redondear cualquier número de punto flotante al entero más cercano al asignarlo a un valor de píxel.
*  Al implementar la función `grayscale`, deberá promediar los valores de 3 enteros. ¿Por qué podría querer dividir la suma de estos enteros por 3.0 y no por 3?
*  En la función `reflect`, deberá intercambiar los valores de los píxeles en lados opuestos de una fila. Recuerde de la clase cómo implementamos el intercambio de dos valores con una variable temporal. ¡No hay necesidad de usar una función separada para el intercambio a menos que quiera!
*  ¿Cómo podría serle útil una función que devuelva el menor de dos enteros al implementar `sepia`, particularmente cuando necesita asegurarse de que el valor de un color no sea mayor a 255?
*  Al implementar la función `blur`, puede descubrir que el desenfoque de un píxel termina afectando el desenfoque de otro píxel. ¿Quizás crear una copia de `image` (el tercer argumento de la función) declarando una nueva matriz (bidimensional) con código como `RGBTRIPLE copy[height][width];` y copiar `image` en `copy`, píxel por píxel, con bucles `for` anidados? ¿Y luego leer los colores de los píxeles desde `copy` pero escribir (es decir, cambiar) los colores de los píxeles en `image`?

Pruebas
-------

Asegúrese de probar todos sus filtros en los archivos de mapa de bits de muestra proporcionados.

Ejecute lo siguiente para evaluar la corrección de su código utilizando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50/problems/2023/x/filter/less
    

Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`.

    style50 helpers.c
    

Cómo enviar
-------------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/filter/less"

