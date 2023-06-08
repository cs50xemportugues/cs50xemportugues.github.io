Pluralidad
=========

Para este programa, implementarás un programa que ejecute una elección de pluralidad, como se muestra a continuación.

    $ ./plurality Alice Bob Charlie
    Número de votantes: 4
    Voto: Alice
    Voto: Bob
    Voto: Charlie
    Voto: Alice
    Alice
    

Antecedentes
----------

Las elecciones vienen en todas las formas y tamaños. En el Reino Unido, el [primer ministro] (https://www.parliament.uk/education/about-your-parliament/general-elections/) es oficialmente nombrado por el monarca, quien generalmente elige al líder del partido político que gana la mayoría de los escaños en la Cámara de los Comunes. Estados Unidos utiliza un proceso de [Colegio Electoral] (https://www.archives.gov/federal-register/electoral-college/about.html) de múltiples pasos donde los ciudadanos votan sobre cómo debe asignar cada estado electores que luego eligen al Presidente.

Quizás la forma más simple de realizar una elección sea mediante un método conocido comúnmente como "voto pluralidad" (también conocido como "primero el poste" o "el ganador se lo lleva todo"). En la votación de pluralidad, cada votante puede votar por un candidato. Al final de la elección, el candidato con el mayor número de votos es declarado ganador de la elección.

Comenzando
---------------

Inicie sesión en [code.cs50.io] (https://code.cs50.io/), haga clic en la ventana del terminal y ejecute `cd` por sí solo. Debería encontrar que el indicador de su ventana de terminal se parece al siguiente:

    $
    

A continuación, ejecute

     wget https://cdn.cs50.net/2022/fall/psets/3/plurality.zip
    

para descargar un archivo ZIP llamado `plurality.zip` en su espacio de trabajo de código.

Luego ejecute

     unzip plurality.zip
    

para crear una carpeta llamada `plurality`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

     rm plurality.zip
    

y responda con "y" seguido de Enter en el símbolo del sistema para eliminar el archivo ZIP que descargó.

Ahora escriba

     cd plurality
    

seguido de Enter para moverse hacia la dirección. Su indicador ahora debe ser el siguiente:

    plurality/ $
    

Si todo fue exitoso, debería ejecutar

    ls
    

y ver un archivo llamado `plurality.c`. Ejecutar `code plurality.c` debería abrir el archivo donde escribirá su código para este conjunto de problemas. Si no, retome sus pasos y vea si puede determinar dónde se equivocó.

Comprensión
-------------

Echemos un vistazo a `plurality.c` y leamos el código de distribución que se le ha proporcionado.

La línea `#define MAX 9` es una sintaxis utilizada aquí para significar que `MAX` es una constante (igual a `9`) que se puede usar en todo el programa. Aquí, representa el número máximo de candidatos que puede tener una elección.

El archivo luego define una `struct` llamada un `candidate`. Cada `candidate` tiene dos campos: una `cadena` llamada `name` que representa el nombre del candidato y un `int` llamado `votes` que representa el número de votos que tiene el candidato. A continuación, el archivo define una matriz global de `candidates`, donde cada elemento es en sí mismo un `candidate`.

Ahora, eche un vistazo a la función `main` en sí. Vea si puede encontrar dónde el programa establece una variable global `candidate_count` que representa el número de candidatos en la elección, copia los argumentos de línea de comando en la matriz `candidates` y pide al usuario que escriba el número de votantes. Entonces, el programa permite que cada votante escriba un voto (¿ve cómo?), llamando a la función `vote` en cada candidato por el que se votó. Por último, `main` hace una llamada a la función `print_winner` para imprimir al ganador (o ganadores) de la elección.

Si miras más abajo en el archivo, verás que las funciones `vote` y `print_winner` se han dejado en blanco. ¡Esta parte depende de ti para completar!

Especificación
-------------

Complete la implementación de `plurality.c` de tal manera que el programa simule una elección de voto pluralidad.

*   Completa la función `vote`.
    *   `vote` toma un solo argumento, una cadena llamada `name`, que representa el nombre del candidato por el que se votó.
    *   Si `name` coincide con uno de los nombres de los candidatos en la elección, actualice el total de votos de ese candidato para tener en cuenta el nuevo voto. La función de `vote` en este caso debería devolver `true` para indicar una boleta exitosa.
    *   Si `name` no coincide con el nombre de cualquiera de los candidatos en la elección, no deberían cambiar los totales de votos, y la función de `vote` debería devolver `false` para indicar una boleta no válida.
    *   Puede asumir que ningún candidato tendrá el mismo nombre.
*   Completa la función `print_winner`.
    *   La función debe imprimir el nombre del candidato que recibió la mayoría de los votos en la elección, y luego imprimir una nueva línea.
    *   Es posible que la elección termine en un empate si varios candidatos tienen el número máximo de votos. En ese caso, debería imprimir los nombres de cada uno de los candidatos ganadores, cada uno en una línea separada.

No debe modificar nada más en `plurality.c` que las implementaciones de las funciones `vote` y `print_winner` (y la inclusión de archivos de cabecera adicionales, si lo desea).

Uso
-----

Su programa debe comportarse según los ejemplos a continuación.

     $ ./plurality Alice Bob
     Número de votantes: 3
     Voto: Alice
     Voto: Bob
     Voto: Alice
     Alice
    

     $ ./plurality Alice Bob
     Número de votantes: 3
     Voto: Alice
     Voto: Charlie
     Voto inválido.
     Voto: Alice
     Alice
    

     $ ./plurality Alice Bob Charlie
     Número de votantes: 5
     Voto: Alice
     Voto: Charlie
     Voto: Bob
     Voto: Bob
     Voto: Alice
     Alice
     Bob
    

Instrucciones
-----------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/plurality"