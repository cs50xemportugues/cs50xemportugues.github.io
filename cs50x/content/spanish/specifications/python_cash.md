Efectivo
=======

Implemente un programa que calcule la cantidad mínima de monedas necesarias para dar cambio a un usuario.

    $ python cash.py
    Change owed: 0.41
    4
    

Para empezar
------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en su ventana de terminal y ejecute `cd` por sí solo. Su terminal debería verse así:

    $
    
Luego, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-cash.zip
    
para descargar un archivo ZIP llamado `sentimental-cash.zip` en su espacio de código.

A continuación, ejecute

    unzip sentimental-cash.zip
    
para crear una carpeta llamada "sentimental-cash". Ya no necesita el archivo ZIP, así que ejecute

    rm sentimental-cash.zip
    
y responda con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargó.

Ahora escriba 

    cd sentimental-cash
    
seguido de Enter para moverse (es decir, abrirse) en ese directorio. Su prompt debe ser similar al siguiente.

    sentimental-cash/ $
    
Ejecute `ls` por sí solo y debería ver `cash.py`. Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.

Especificaciones
----------------

* Escriba en un archivo llamado `cash.py`, un programa que primero pregunte al usuario cuánto cambio se debe y luego proporcione el número mínimo de monedas con las cuales se puede hacer dicho cambio. Puede hacer esto exactamente como lo hizo en [Problem Set 1](../../1/), con la excepción de que esta vez su programa se escribirá en Python y deberá suponer que el usuario ingresará su cambio en dólares (por ejemplo, 0,50 dólares en lugar de 50 centavos).
* Utilice `get_float` de la biblioteca CS50 para obtener la entrada del usuario e imprima su respuesta utilizando `print`. Asuma que las únicas monedas disponibles son cuartos (25¢), diezmos (10¢), níqueles (5¢) y centavos (1¢).
     * Le pedimos que use `get_float` para poder manejar tanto los dólares como los centavos, aunque sin signo de dólar. En otras palabras, si un cliente debe $9,75 (como en el caso en que un periódico cuesta 25¢ pero el cliente paga con un billete de $10), asuma que la entrada del programa será `9,75` y no `$9,75` ni` 975`. Sin embargo, si un cliente debe exactamente $9, asuma que la entrada del programa será `9,00` o simplemente `9`, pero nuevamente no `$9` ni `900`. Por supuesto, por la naturaleza de los valores de punto flotante, su programa probablemente funcionará con entradas como `9,0` y `9,000` también; no necesita preocuparse por comprobar si la entrada del usuario está "formateada" como debería ser el dinero.
* Si el usuario no proporciona un valor no negativo, su programa debe volver a pedir al usuario una cantidad válida una y otra vez hasta que el usuario cumpla.
* Por cierto, para que podamos automatizar algunas pruebas de su código, pedimos que la última línea de salida de su programa sea solo la cantidad mínima posible de monedas: un número entero seguido de una nueva línea.

Uso
---

Su programa debería comportarse como se indica a continuación.

    $ python cash.py
    Change owed: 0.41
    4
    

Pruebas
-------

Si bien `check50` está disponible para este problema, se recomienda que primero pruebe su código por su cuenta para cada uno de los siguientes casos.

* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `0.41` y presione Enter. Su programa debería generar `4`.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `0.01` y presione Enter. Su programa debería generar `1`.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `0.15` y presione Enter. Su programa debería generar `2`.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `1.60` y presione Enter. Su programa debería generar `7`.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `23` y presione Enter. Su programa debería generar `92`.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `4.2` y presione Enter. Su programa debería generar `18`.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `-1` y presione Enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. Escriba `foo` y presione Enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como `python cash.py` y espere una solicitud de entrada. No escriba nada y presione Enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.

Ejecute el siguiente comando para evaluar la corrección de su código utilizando `check50`. ¡Pero asegúrese de compilarlo y probarlo también!

    check50 cs50/problems/2023/x/sentimental/cash
    

Ejecute el siguiente comando para evaluar el estilo de su código utilizando `style50`.

    style50 cash.py
    

Cómo enviar
-----------

En su terminal, ejecute el siguiente comando para enviar su trabajo.

    submit50 cs50/problems/2023/x/sentimental/cash"