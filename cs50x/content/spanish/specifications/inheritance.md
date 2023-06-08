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

Detalles de Implementación
----------------------

Completa la implementación de `inheritance.c`, de manera que crees una familia de un tamaño de generación específico y le asignes alelos de tipo sanguíneo a cada miembro de la familia. La generación más antigua tendrá alelos asignados al azar.

*   La función `create_family` toma un número entero (`generaciones`) como entrada y debe asignar memoria (a través de `malloc`) a la cantidad de miembros de la familia de ese número de generaciones, devolviendo un puntero a la persona de la generación más joven.
    *   Por ejemplo, `create_family ( 3 )` debería devolver un puntero a una persona con dos padres, donde cada padre también tiene dos padres.
    *   A cada persona se le debe asignar`alelos`. La generación más antigua debería tener alelos elegidos al azar (llamando a la función `alelo_aleatorio`), y las generaciones más jóvenes deberían heredar un alelo (elegido al azar) de cada padre.
    *   A cada persona se le deben asignar `padres`. La generación más antigua debería tener ambos `padres` establecidos como `NULL`, y las generaciones más jóvenes deberían tener `padres` como una matriz de dos punteros, cada uno apuntando a un padre diferente.

Hemos dividido la función `create_family` en algunos `TODO`s para que puedas completarla.

*   Primero, debes asignar memoria para una nueva persona. Recuerda que puedes usar `malloc` para asignar memoria y `sizeof (person)` para obtener el número de bytes para asignar.
*   A continuación, hemos incluido una condición para comprobar si `generations> 1`.
    *   Si `generations> 1`, entonces hay más generaciones que aún necesitan ser asignadas. Ya hemos creado dos nuevos `padres`, `padre0` y `padre1`, llamando de forma recursiva a `create_family`. Tu función `create_family` debe establecer los punteros de los padres de la persona nueva que creaste. Finalmente, asigne ambos `alelos` a la nueva persona eligiendo aleatoriamente un alelo de cada padre.
    *   De lo contrario (si `generations == 1`), entonces no habrá datos de los padres para esta persona. Ambos `padres` de tu nueva persona deben establecerse como `NULL`, y cada `alelo` debe generarse al azar.
*   Finalmente, tu función debe devolver un puntero para la `persona` que fue asignada.

La función `free_family` debe aceptar como entrada un puntero a una `persona`, liberar la memoria para esa persona y luego liberar de forma recursiva la memoria para todos sus ancestros.

*   Como está es una función recursiva, debes manejar primero el caso base. Si la entrada en la función es`NULL `, entonces no hay nada que liberar, por lo que tu función puede regresar inmediatamente.
*   De lo contrario, debe liberar de forma recursiva ambos padres de la persona antes de liberar al niño.

### Recorrido

<div class="alert" data-alert="primary" role="alert"><p>Este video fue grabado cuando el curso todavía estaba usando el CS50 IDE para escribir el código. ¡Aunque la interfaz puede verse diferente de su codespace, el comportamiento de los dos ambientes debería ser muy similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/9p7ddI3ozTY"></iframe>


### Consejos

*   Podrías encontrar útil la función `rand()` para asignar alelos al azar. Esta función devuelve un entero entre `0` y `RAND_MAX`, o `2147483647`.
    *   En particular, para generar un número pseudoaleatorio que sea `0` o `1`, puedes usar la expresión `rand() % 2`.
*   Recuerda que para asignar memoria a una persona determinada, podemos usar `malloc(n)`, que toma un tamaño como argumento y asignará `n` bytes de memoria.
*   Recuerda que para acceder a una variable a través de un puntero, podemos usar la notación de flecha.
    *   Por ejemplo, si `p` es un puntero a una persona, entonces se puede acceder a un puntero al primer padre de esta persona mediante `p->parents [0]`.

<details><summary>¿No estás seguro de cómo resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/H7LULatPwcQ"></iframe></details>


### Cómo probar tu código

Al ejecutar `./inheritance`, tu programa debería adherirse a las reglas descritas en la introducción. El niño debería tener dos alelos, uno de cada padre. Los padres deberían tener dos alelos cada uno, uno de cada uno de sus padres.

Por ejemplo, en el siguiente ejemplo, el niño de la Generación 0 recibió un alelo O de ambos padres de la Generación 1. El primer padre recibió una A del primer abuelo y un O del segundo abuelo. Similarmente, el segundo padre recibió un O y un B de sus abuelos.

    $ ./inheritance
    Child (Generation 0): blood type OO
        Parent (Generation 1): blood type AO
            Grandparent (Generation 2): blood type OA
            Grandparent (Generation 2): blood type BO
        Parent (Generation 1): blood type OB
            Grandparent (Generation 2): blood type AO
            Grandparent (Generation 2): blood type BO
    
    

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilarlo y probarlo por ti mismo también!

    check50 cs50/labs/2023/x/inheritance
    

Ejecute lo siguiente para evaluar el estilo de su código con `style50`.

    style50 inheritance.c
    

Cómo enviar
-------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/labs/2023/x/inheritance"

