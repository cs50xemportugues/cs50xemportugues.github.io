Legibilidad
===========

Implementar un programa que calcule el nivel aproximado de grado necesario para comprender un texto, como se muestra a continuación:

    $ python readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3
    

Cómo empezar
---------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en la ventana del terminal y ejecute `cd` por sí solo. Su ventana del terminal debería verse así:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-readability.zip
    

para descargar un archivo ZIP llamado `sentimental-readability.zip` en su espacio de códigos.

Luego ejecute

    unzip sentimental-readability.zip
    

para crear una carpeta llamada `sentimental-readability`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm sentimental-readability.zip
    

y responda con "y" seguido de Enter en el símbolo del sistema para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd sentimental-readability
    

seguido de Enter para moverse (es decir, abrir) en ese directorio. Su ventana de terminal ahora debería verse así:

    sentimental-readability/ $
    

Ejecute `ls` por sí solo y debería ver `readability.py`. Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar en qué se equivocó.

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

Pruebas
--------

Aunque `check50` está disponible para este problema, se recomienda que primero pruebes tu código por ti mismo para cada uno de los siguientes.

* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `One fish. Two fish. Red fish. Blue fish.` y pulsa enter. Tu programa debería mostrar `Before Grade 1`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` y pulsa enter. Tu programa debería mostrar `Grade 2`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Congratulations! Today is your day. You're off to Great Places! You're off and away!` y pulsa enter. Tu programa debería mostrar `Grade 3`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` y pulsa enter. Tu programa debería mostrar `Grade 5`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` y pulsa enter. Tu programa debería mostrar `Grade 7`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` y pulsa enter. Tu programa debería mostrar `Grade 8`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` y pulsa enter. Tu programa debería mostrar `Grade 8`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` y pulsa enter. Tu programa debería mostrar `Grade 9`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` y pulsa enter. Tu programa debería mostrar `Grade 10`.
* Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` y pulsa enter. Tu programa debería mostrar `Grade 16+`.

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilar y probarlo tú mismo también!

    check50 cs50/problems/2023/x/sentimental/readability

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 readability.py

Cómo enviar
-------------
 
En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/sentimental/readability

