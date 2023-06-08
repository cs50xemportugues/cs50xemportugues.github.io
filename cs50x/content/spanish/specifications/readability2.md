## Contexto

Según [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), _Charlotte’s Web_ de E.B. White corresponde a un nivel de lectura entre segundo y cuarto grado, mientras que _The Giver_ de Lois Lowry corresponde a un nivel de lectura entre octavo y duodécimo grado. ¿Qué significa, sin embargo, que un libro esté en un nivel de lectura en particular?

Bueno, en muchos casos, un experto humano podría leer un libro y tomar una decisión sobre el grado (es decir, el año escolar) para el que cree que el libro es más apropiado. ¡Pero un algoritmo también podría descifrarlo!

Entonces, ¿qué tipos de características son características de niveles de lectura más altos? Bueno, probablemente palabras más largas se correlacionan con un nivel de lectura más alto. Del mismo modo, las frases más largas probablemente se correlacionen con niveles de lectura más altos también. 

Un número de "pruebas de legibilidad" se han desarrollado a lo largo de los años que definen fórmulas para calcular el nivel de lectura de un texto. Una de estas pruebas de legibilidad es el _índice Coleman-Liau_. El índice Coleman-Liau de un texto está diseñado para imprimir (el nivel de grado estadounidense) que se necesita para comprender algún texto. La fórmula es

    index = 0,0588 * L - 0,296 * S - 15,8

donde `L` es el número promedio de letras por cada 100 palabras del texto, y `S` es el número promedio de frases por cada 100 palabras del texto.

Escribamos un programa llamado `readability` que tome un texto y determine su nivel de lectura. Por ejemplo, si el usuario escribe una línea de texto de Dr. Seuss, el programa debería comportarse de la siguiente manera:

    $ ./readability
    Texto: ¡Felicidades! Hoy es tu día. ¡Te vas a grandes lugares! ¡Te vas y te alejas!
    Grado 3

El texto ingresado por el usuario tiene 65 letras, 4 frases y 14 palabras.  65 letras por cada 14 palabras es un promedio de alrededor de 464,29 letras por cada 100 palabras (porque 65/14 * 100 = 464,29). Y 4 frases por cada 14 palabras es un promedio de alrededor de 28,57 frases por cada 100 palabras (porque 4/14 * 100 = 28,57). Al aplicar la fórmula Coleman-Liau, y redondeando al entero más cercano, obtenemos una respuesta de 3 (porque 0,0588 * 464,29 - 0,296 * 28,57 - 15,8 = 3): por lo tanto, este pasarje se encuentra en un nivel de lectura de tercer grado.

Intentemos con otro ejemplo:

    $ ./readability
    Texto: Harry Potter era un chico muy inusual en muchos sentidos. Por una cosa, él odiaba las vacaciones de verano más que cualquier otra época del año. Por otra parte, él realmente quería hacer su tarea, pero fue obligado a hacerlo en secreto, en medio de la noche. Y también, resultó ser un mago.
    Grado 5

Este texto tiene 214 letras, 4 frases y 56 palabras. Eso da alrededor de 382,14 letras por cada 100 palabras, y 7,14 frases por cada 100 palabras. Al aplicar la fórmula Coleman-Liau, obtenemos un nivel de lectura de quinto grado.

A medida que el número promedio de letras y palabras por frase aumenta, el índice Coleman-Liau da al texto un nivel de lectura más alto. Si tomaras este párrafo, por ejemplo, que tiene palabras y frases más largas que cualquiera de los ejemplos anteriores, la fórmula daría al texto un nivel de lectura de décimo segundo grado.

    $ ./readability
    Texto: A medida que el número promedio de letras y palabras por frase aumenta, el índice Coleman-Liau da al texto un nivel de lectura más alto. Si tomaras este parráfo, por ejemplo, que tiene palabras y frases más largas que cualquiera de los ejemplos anteriores, la fórmula daría al texto un nivel de lectura de décimo segundo grado.
    Grado 12

<details><summary>Mira una grabación</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script></details>

## Especificaciones

Diseña e implementa un programa, `readability`, que calcule el índice Coleman-Liau de un texto.

- Implementa tu programa en un archivo llamado `readability.c` en un directorio llamado `readability`.
- Tu programa debe solicitar al usuario una `cadena` de texto usando `get_string`.
- Tu programa debería contar el número de letras, palabras y frases en el texto. Puedes suponer que una letra es cualquier carácter en minúscula desde `a` hasta `z` o cualquier carácter en mayúscula desde `A` a `Z`, cualquier secuencia de caracteres separados por espacio debería contar como una palabra, y que cualquier aparición de un punto, signo de exclamación o interrogación indica el final de una sentencia.
- Tu programa debería imprimir como resultado `"Grado X"`, donde `X` es el nivel de grado calculado por la fórmula Coleman-Liau, redondeado al entero más cercano.
- Si el número de índice resultante es 16 o mayor (equivale a o es mayor que el nivel de lectura de un estudiante universitario mayor), tu programa debería devolver `"Grado 16+"` en lugar de dar el número de índice exacto. Si el número de índice es menor que 1, tu programa debería devolver `"Antes del grado 1"`.