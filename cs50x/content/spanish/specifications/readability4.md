### Oraciones

La última pieza de información que la fórmula de Coleman-Liau toma en cuenta, además del número de letras y palabras, es el número de oraciones. Determinar el número de oraciones puede ser sorprendentemente complicado. En primer lugar, puede imaginar que una oración es simplemente cualquier secuencia de caracteres que termina con un punto, pero por supuesto las oraciones también pueden terminar con un signo de exclamación o una pregunta. Pero por supuesto, no todos los puntos significan necesariamente que la oración ha terminado. Por ejemplo, considere la siguiente oración:

    Sr. y Sra. Dursley, del número cuatro de Privet Drive, estaban orgullosos de decir que eran perfectamente normales, muchas gracias.

Esta es solo una oración, ¡pero hay tres puntos! Para este problema, le pediremos que ignore esa sutileza: debe considerar cualquier secuencia de caracteres que termine con un `.` o un `!` o un `?` como una oración (así que para la “oración” anterior, debería contarla como tres oraciones). En la práctica, la detección de límites de las oraciones necesita ser un poco más inteligente para manejar estos casos, pero no nos preocuparemos por eso por ahora.

Agregue a `readability.c`, debajo de `main`, una función llamada `count_sentences` que tome un argumento, una cadena de texto, y que devuelva un `int`, el número de oraciones en ese texto. Asegúrese de agregar el prototipo de la función, también en la parte superior de su archivo, para que `main` sepa cómo llamarla. (¡Dejamos su prototipo a su elección!)

Luego llame a esa función en `main` para que su programa también imprima el número de oraciones en el texto.

El programa debe comportarse a continuación:

    $ ./readability
    Texto: Cuando casi cumplió trece años, a mi hermano Jem le rompieron mal el brazo en el codo. Cuando sanó, y los temores de Jem de nunca poder jugar al fútbol fueron calmados, rara vez se sintió cohibido por su lesión. Su brazo izquierdo era un poco más corto que el derecho; cuando estaba de pie o caminaba, el dorso de su mano hacía ángulo recto con su cuerpo, su pulgar paralelo a su muslo.
    295 letras
    70 palabras
    3 oraciones

### Poniéndolo Todo Junto

¡Ahora es el momento de unir todas las piezas! Recuerde que el índice Coleman-Liau se calcula utilizando la fórmula:

    índice = 0,0588 * L - 0,296 * S - 15,8

donde `L` es el número promedio de letras por cada 100 palabras en el texto, y `S` es el número promedio de oraciones por cada 100 palabras en el texto.

Modifique `main` en `readability.c` para que, en lugar de imprimir el número de letras, palabras y oraciones, imprima (solo) el nivel de grado según lo definido por el índice Coleman-Liau (por ejemplo, `"Grado 2"` o `"Grado 8"` o similar). ¡Asegúrate de redondear el número índice resultante al entero más cercano!

<details><summary>Sugerencias</summary> <ul>
  <li data-marker="*"> ¡Recuerda que `round` se declara en `math.h`! </li>
  <li data-marker="*"> Recuerde que, al dividir valores de tipo `int` en C, el resultado también será un valor `int`, con cualquier resto (es decir, dígitos después del punto decimal) descartado. Dicho de otra manera, el resultado será "truncado". ¡Es posible que desee convertir uno o más valores a `float` antes de realizar la división al calcular `L` y `S`! </li>
</ul> </details>

Si el número índice resultante es 16 o superior (equivalente o mayor que un nivel de lectura de pregrado avanzado), su programa debe imprimir `"Grado 16+"` en lugar de imprimir un número índice exacto. Si el número índice es menor que 1, su programa debe imprimir `"Antes del Grado 1"`.