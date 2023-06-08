Crédito
=======

Implementa un programa que determine si un número de tarjeta de crédito proporcionado es válido según el algoritmo de Luhn.

     $ python credit.py
     Número: 378282246310005
     AMEX

Cómo empezar
------------

Accede a [code.cs50.io](https://code.cs50.io/), haz clic en la ventana de la terminal y ejecuta solo `cd`. Deberías ver que la ventana del terminal muestra lo siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-credit.zip

para descargar un archivo ZIP llamado `sentimental-credit.zip` en tu espacio de códigos. 

Luego ejecuta

    unzip sentimental-credit.zip

para crear una carpeta llamada "sentimental-credit". Ya no necesitas el archivo ZIP, así que ejecuta

    rm sentimental-credit.zip

y responde con "y" seguido de Enter para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd sentimental-credit

seguido de Enter para moverte (es decir, abrir) a ese directorio. Tu indicador debería mostrar lo siguiente:

    sentimental-credit/ $

Ejecuta `ls` y verás `credit.py`. Si tienes algún problema, sigue estos mismos pasos y ve si puedes determinar dónde puede estar el fallo.

Especificaciones
----------------

+ En `credit.py`, escribe un programa que solicite al usuario un número de tarjeta de crédito y luego informe (a través de `print`) si es una tarjeta American Express, MasterCard o Visa válida, exactamente como lo hiciste en el [Problema 1](../../1/), excepto que esta vez tu programa debe estar escrito en Python.
+ Para que podamos automatizar algunas pruebas de tu código, pedimos que la última línea de salida de tu programa sea `AMEX\n` o `MASTERCARD\n` o `VISA\n` o `INVALID\n`, nada más, nada menos.
+ Para simplificar, puedes suponer que la entrada del usuario será completamente numérica (es decir, sin guiones, como se imprime en una tarjeta real).
+ Es mejor usar `get_int` o `get_string` de la biblioteca CS50 para obtener la entrada del usuario, dependiendo de cómo decidas implementar este programa.

Uso
---

Tu programa debería comportarse de la siguiente manera:

    $ python credit.py
    Número: 378282246310005
    AMEX

Pistas
-----

+ Es posible utilizar expresiones regulares para validar la entrada del usuario. Podrías usar el módulo [`re`](https://docs.python.org/3/library/re.html) de Python, por ejemplo, para verificar si la entrada del usuario es, de hecho, una secuencia de dígitos de la longitud correcta.

Probando
--------

Mientras `check50` está disponible para este problema, se recomienda que primero pruebes tu código por tu cuenta para cada uno de los siguientes casos:

+ Ejecuta tu programa como `python credit.py` y espera una solicitud de entrada. Escribe `378282246310005` y presiona Enter. Tu programa debe mostrar `AMEX`.
+ Ejecuta tu programa como `python credit.py` y espera una solicitud de entrada. Escribe `371449635398431` y presiona Enter. Tu programa debe mostrar `AMEX`.
+ Ejecuta tu programa como `python credit.py` y espera una solicitud de entrada. Escribe `5555555555554444` y presiona Enter. Tu programa debe mostrar `MASTERCARD`.
+ Ejecuta tu programa como `python credit.py` y espera una solicitud de entrada. Escribe `5105105105105100` y presiona Enter. Tu programa debe mostrar `MASTERCARD`.
+ Ejecuta tu programa como `python credit.py` y espera una solicitud de entrada. Escribe `4111111111111111` y presiona Enter. Tu programa debe mostrar `VISA`.
+ Ejecuta tu programa como `python credit.py` y espera una solicitud de entrada. Escribe `4012888888881881` y presiona Enter. Tu programa debe mostrar `VISA`.
+ Ejecuta tu programa como `python credit.py` y espera una solicitud de entrada. Escribe `1234567890` y presiona Enter. Tu programa debe mostrar `INVALID`.

Ejecuta el siguiente comando para evaluar la corrección de tu código mediante `check50`. ¡Pero asegúrate de compilarlo y probarlo tú mismo también!

    check50 cs50/problems/2023/x/sentimental/credit

Ejecuta el siguiente comando para evaluar el estilo de tu código mediante `style50`.

    style50 credit.py

Cómo enviar
-------------

En la terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2023/x/sentimental/credit