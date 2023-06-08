Especificación
-------------

Bien, el desafío que tienes ante ti ahora es implementar, en orden, `load`, `hash`, `size`, `check` y `unload` de la manera más eficiente posible usando una tabla hash de tal manera que se minimice `TIEMPO EN carga`, `TIEMPO EN revisión`, `TIEMPO EN tamaño` y `TIEMPO EN desactivar`. Asegurándote, no es obvio lo que significa minimizar, en la medida en que estas pruebas variarán seguramente a medida que alimentas `speller` diferentes valores para `diccionario` y para `texto`. Pero ahí radica el desafío, si no la diversión, de este problema. Este problema es tu oportunidad de diseño. Aunque te invitamos a minimizar el espacio, tu enemigo final es el tiempo. Pero antes de empezar, algunas especificaciones:

*   No puedes alterar `speller.c` o `Makefile`.
*   Puedes cambiar `dictionary.c` (y, de hecho, debes hacerlo para completar las implementaciones de `load`, `hash`, `size`,`check` y `unload`) pero no puedes alterar las declaraciones (es decir, los prototipos) de `load`,`hash`, `size`, `check` o `unload`. Sin embargo, puedes agregar nuevas funciones y variables (locales o globales) a `dictionary.c`.
*   Puedes cambiar el valor de `N` en `dictionary.c`, para que tu tabla hash tenga más cubetas.
*   Puedes alterar `dictionary.h`, pero no puedes alterar las declaraciones de `load`,`hash`, `size`, `check` o `unload`.
*   Tu implementación de `check` debe ser insensible a mayúsculas y minúsculas. En otras palabras, si `foo` está en el diccionario, entonces `check` debería devolver verdadero dado cualquier capitalización de ello; ninguna de `foo`,`foO`,`fOo`,`fOO`,`fOO`,`Foo`,`FoO`,`FOo` y `FOO` debe considerarse mal escrita.
*  Dejando a un lado la capitalización, tu implementación de `check` solo debe devolver `verdadero` para las palabras que realmente estén en `dictionary`. Ten cuidado de no codificar en duro palabras comunes (p. ej., `the`), no sea que le pasemos tu implementación un `diccionario` sin las mismas palabras. Además, solo se permiten los posesivos que realmente estén en `dictionary`. En otras palabras, incluso si `foo` está en el diccionario, `check` debería devolver `falso` dado `foo's` si `foo's` no está también en `dictionary`.
*   Puedes asumir que cualquier `dictionary` que pase tu programa tendrá la estructura exactamente igual a la nuestra, ordenado alfabéticamente de arriba hacia abajo con una palabra por línea, cada una de las cuales termina con `\n`. También puedes asumir que `dictionary` contendrá al menos una palabra, que ninguna palabra será más larga que `LONGITUD` (una constante definida en `dictionary.h`) caracteres, que ninguna palabra aparecerá más de una vez, que cada palabra contendrá caracteres alfabéticos minúsculos y posiblemente apóstrofes, y que ninguna palabra comenzará con un apóstrofe.
*   Puedes asumir que `check` solo recibirá palabras que contengan caracteres alfabéticos (mayúsculas o minúsculas) y posiblemente apóstrofes.
*   Tu corrector ortográfico solo puede aceptar `texto` y, opcionalmente, `dictionary` como entrada. Aunque podrías estar inclinado (especialmente si estás entre aquellos más cómodos) a "preprocesar" nuestro diccionario predeterminado para derivar una "función hash ideal" para él, no puedes guardar la salida de tal preprocesamiento en disco para cargarla de vuelta en la memoria en ejecuciones posteriores de tu corrector ortográfico a fin de obtener una ventaja.
*   Tu corrector ortográfico no debe perder memoria. Asegúrate de verificar las pérdidas de memoria con `valgrind`.
*   **La función hash que escribas debe ser la tuya, no una que busques en línea.** Hay muchas formas de implementar una función hash más allá del uso del primer carácter (o caracteres) de una palabra. Considera una función hash que usa la suma de los valores ASCII o la longitud de una palabra. Una buena función hash tiende a reducir las "colisiones" y tiene una distribución bastante uniforme en los "cubos" de la tabla hash.

¡Listo para empezar!

*   Implementar `load`.
*   Implementar `hash`.
*   Implementar `size`.
*   Implementar `check`.
*   Implementar `unload`.

Paseos
------------

Ten en cuenta que hay 6 videos en la lista de reproducción.

<div class="alert" data-alert="danger" role="alert"><p>Aunque el paseo por Speller indica que es razonable usar una función hash encontrada en línea, este video es de una versión anterior del problema donde lo permitimos. Según la especificación anterior, la función hash que escribas debe ser la tuya; no puedes usar una función hash que encuentres en línea. Asegúrate de citar cualquier fuente externa que hayas consultado al escribir tu función hash.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>