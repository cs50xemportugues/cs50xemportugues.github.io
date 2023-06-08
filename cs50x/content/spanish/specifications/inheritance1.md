Laboratorio 5: Herencia
==================

<div class = "alert" data-alert = "warning" role="alert"> <p> Puedes colaborar con uno o dos compañeros en este laboratorio, aunque se espera que todos los estudiantes de dichos grupos contribuyan igualmente en él. </p> </div>

Simular la herencia de tipos de sangre para cada miembro de una familia.

    $./herencia
    Hijo (Generación 0): tipo de sangre OO
        Padre (Generación 1): tipo de sangre AO
            Abuelo (Generación 2): tipo de sangre OA
            Abuela (Generación 2): tipo de sangre BO
         Padre (Generación 1): tipo de sangre OB
             Abuelo (Generación 2): tipo de sangre AO
             Abuela (Generación 2): tipo de sangre BO
    
    
Antecedentes 
----------

El tipo de sangre de una persona está determinado por dos alelos, es decir, diferentes formas de un gen. Los tres alelos posibles son A, B y O, de los cuales cada persona tiene dos (posiblemente iguales, posiblemente diferentes). Cada uno de los padres de un hijo pasa al azar uno de sus dos alelos de tipo de sangre a su hijo. Las posibles combinaciones de tipos de sangre son: OO, OA, OB, AO, AA, AB, BO, BA y BB.

Por ejemplo, si un padre tiene tipo de sangre AO y el otro tipo de sangre BB, los posibles tipos de sangre del hijo serían AB y OB, dependiendo de qué alelo se reciba de cada padre. Del mismo modo, si un padre tiene tipo de sangre AO y el otro tipo de sangre OB, los posibles tipos de sangre del hijo serían AO, OB, AB y OO.

Empezando
---------------

Abre CodeRunner.

Comienza haciendo clic dentro de tu ventana de terminal, luego ejecuta `cd` solo. Deberías encontrar que su "prompt" se parece al siguiente.

    $
    

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/labs/5/inheritance.zip
    

seguido de Enter para descargar un ZIP llamado `inheritance.zip` en tu codespace. ¡Ten cuidado de no pasar por alto el espacio entre`wget` y la URL siguiente, o cualquier otro carácter en este  caso!

Ahora ejecuta

    unzip inheritance.zip
    

para crear una carpeta llamada `inheritance`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm inheritance.zip
    

y responde con "y", seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd inheritance
    

seguido de Enter para moverte a ti mismo dentro (es decir, abrir) ese directorio. Su prompt debería tener ahora un aspecto similar al siguiente.

    herencia/ $
    

Si todo ha funcionado correctamente, deberías ejecutar

    ls
    

y deberías ver `herencia.c`.

Si tiene problemas, sigue los mismos pasos nuevamente y ve si puedes determinar dónde te equivocaste.

Entendiendo 
-------------

Echa un vistazo al código de distribución en `herencia.c`.

Ten en cuenta la definición de un tipo llamado `persona`. Cada persona tiene una matriz de dos `parent`, cada uno de los cuales es un puntero a otra estructura `persona`. Cada persona también tiene una matriz de dos alelos, cada uno de los cuales es un `char` (ya sea `'A'`, `'B'` o `'O'`).

Ahora, echa un vistazo a la función `main`. El programa comienza por "sembrar" (es decir, proporcionar algún input inicial) a un generador de números aleatorios, que utilizaremos más adelante para generar alelos aleatorios. La función `main` luego llama a la función `create_family` para simular la creación de estructuras de `persona` para una familia de 3 generaciones (es decir, una persona, sus padres y sus abuelos). Luego llamamos a `print_family` para imprimir cada uno de los miembros de la familia y sus tipos de sangre. Finalmente, la función llama a `free_family` para `liberar` cualquier memoria que se haya asignado previamente con `malloc`.

¡Te toca escribir las funciones `create_family` y `free_family!`