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