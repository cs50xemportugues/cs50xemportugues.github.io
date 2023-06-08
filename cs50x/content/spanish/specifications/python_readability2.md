Especificación
-------------

* Escriba un programa llamado `readability.py`, que primero pide al usuario que escriba un texto y luego devuelva el nivel de grado del texto, según la fórmula de Coleman-Liau, exactamente como lo hizo en [Problem Set 2](../../2/), excepto que esta vez el programa debe estar escrito en Python.
    * Recuerde que el índice de Coleman-Liau se calcula como `0.0588 * L - 0.296 * S - 15.8`, donde `L` es el número promedio de letras por cada 100 palabras en el texto y `S` es el número promedio de oraciones por cada 100 palabras en el texto.
* Utilice `get_string`de la biblioteca CS50 para obtener la entrada del usuario y `print` para mostrar su respuesta.
* Su programa debe contar el número de letras, palabras y oraciones en el texto. Se puede asumir que una letra es cualquier carácter en minúscula de `a` a `z` o cualquier carácter en mayúscula de `A` a `Z`, cualquier secuencia de caracteres separados por espacios debe contarse como una palabra y que cualquier aparición de un punto, signo de exclamación o signo de interrogación indica el final de una oración.
* Su programa deberá mostrar `"Grado X"` como resultado, donde `X` es el nivel de grado calculado por la fórmula de Coleman-Liau, redondeado al entero más cercano.
* Si el índice resultante es 16 o superior (equivalente o superior a un nivel de lectura de pregrado avanzado), su programa deberá mostrar `"Grado 16+"` en lugar de dar el índice exacto. Si el índice es inferior a 1, su programa deberá mostrar `"Antes del grado 1"`.

Modo de uso
-----

Su programa deberá mostrarse como el ejemplo a continuación.

    $ python readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grado 3