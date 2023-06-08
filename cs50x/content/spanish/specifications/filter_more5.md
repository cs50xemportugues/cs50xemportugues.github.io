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