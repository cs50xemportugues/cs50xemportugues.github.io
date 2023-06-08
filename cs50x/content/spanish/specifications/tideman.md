Tideman
=======

Para este programa, implementarás un programa que ejecute una elección de Tideman, como se muestra a continuación.

    $ ./tideman Alice Bob Charlie
    Número de votantes: 5
    Rango 1: Alice
    Rango 2: Charlie
    Rango 3: Bob
    
    Rango 1: Alice
    Rango 2: Charlie
    Rango 3: Bob
    
    Rango 1: Bob
    Rango 2: Charlie
    Rango 3: Alice
    
    Rango 1: Bob
    Rango 2: Charlie
    Rango 3: Alice
    
    Rango 1: Charlie
    Rango 2: Alice
    Rango 3: Bob
    
    Charlie
    

Antecedentes
----------

Ya conoces las elecciones de pluralidad, que siguen un algoritmo muy simple para determinar el ganador de una elección: cada votante obtiene un voto y el candidato con la mayoría de los votos gana.

Pero el voto de pluralidad tiene algunas desventajas. ¿Qué sucede, por ejemplo, en una elección con tres candidatos, y se emiten las siguientes boletas?

![Five ballots, tie betweeen Alice and Bob](https://cs50.harvard.edu/x/2023/psets/3/fptp_ballot_1.png)

Una votación de pluralidad declararía un empate entre Alice y Bob aquí, ya que cada uno tiene dos votos. ¿Pero es ese el resultado correcto?

Hay otro tipo de sistema de votación conocido como sistema de votación de rango. En un sistema de votación de rango, los votantes pueden votar por más de un candidato. En lugar de solo votar por su opción principal, pueden clasificar los candidatos en orden de preferencia. Las boletas resultantes podrían verse así.

![Three ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_1.png)

Aquí, cada votante, además de especificar su candidato de primera preferencia, también ha indicado su segunda y tercera opciones. Y ahora, lo que era previamente una elección empatada ahora podría tener un ganador. La carrera estaba originalmente empatada entre Alice y Bob. Pero el votante que eligió a Charlie prefirió a Alice sobre Bob, por lo que Alice podría ser declarada la ganadora aquí.

La votación con opción rankeada también puede resolver otra posible desventaja de la votación de pluralidad. Echa un vistazo a las siguientes boletas.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/condorcet_1.png)

¿Quién debería ganar esta elección? En una votación de pluralidad donde cada votante elige solo su primera preferencia, Charlie gana esta elección con cuatro votos en comparación con solo tres para Bob y dos para Alice. (Tenga en cuenta que, si está familiarizado con el sistema de votación instantánea, Charlie también gana aquí bajo ese sistema). Sin embargo, Alice podría argumentar razonablemente que ella debería ser la ganadora de la elección en lugar de Charlie: después de todo, de los nueve votantes, la mayoría (cinco de ellos) prefirieron a Alice sobre Charlie, por lo que la mayoría estaría más feliz con Alice como ganadora en lugar de Charlie.

Alice es, en esta elección, la llamada "ganadora de Condorcet" de la elección: la persona que habría ganado cualquier enfrentamiento mano a mano contra otro candidato. Si la elección hubiera sido solo Alice y Bob, o solo Alice y Charlie, Alice habría ganado.

El método de votación de Tideman (también conocido como "clasificación de pares") es un método de votación por rango que garantiza producir al ganador de Condorcet de la elección si existe uno.

En general, el método Tideman funciona mediante la construcción de un "grafo" de candidatos, donde una flecha (es decir, un borde) desde el candidato A hasta el candidato B indica que el candidato A gana contra el candidato B en una confrontación mano a mano. El gráfico para la elección anterior se vería así.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/condorcet_graph_1.png)

La flecha de Alice a Bob significa que más votantes prefieren a Alice sobre Bob (5 prefieren a Alice, 4 prefieren a Bob). Del mismo modo, las otras flechas significan que más votantes prefieren a Alice sobre Charlie y que más votantes prefieren a Charlie sobre Bob.

Mirando este gráfico, el método de Tideman dice que el ganador de la elección debería ser la "fuente" del gráfico (es decir, el candidato que no tiene una flecha apuntando hacia él). En este caso, la fuente es Alice, ya que es la única que no tiene una flecha apuntando hacia ella, lo que significa que nadie es preferido mano a mano sobre Alice. Se declara a Alice ganadora de la elección.

Sin embargo, es posible que cuando se tracen las flechas, no haya un ganador de Condorcet. Consideren las siguientes boletas.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/no_condorcet_1.png)

Entre Alice y Bob, Alice es preferida sobre Bob con una margen de 7 a 2. Entre Bob y Charlie, Bob es preferido sobre Charlie con una margen de 5 a 4. Pero entre Charlie y Alice, Charlie es preferido sobre Alice con una margen de 6 a 3. Si dibujamos el gráfico, ¡no hay fuente! Tenemos un ciclo de candidatos, donde Alice vence a Bob que vence a Charlie que vence a Alice (como en el juego de "piedra, papel o tijera"). En este caso, parece que no hay forma de elegir a un ganador.

Para manejar esto, el algoritmo Tideman debe tener cuidado de evitar crear ciclos en el gráfico de candidatos. ¿Cómo lo hace esto? El algoritmo bloquea los bordes más fuertes primero, ya que estos son argumentablemente los más significativos. En particular, el algoritmo Tideman especifica que los bordes del enfrentamiento deben ser "bloqueados" en el gráfico uno por uno, según la "fortaleza" de la victoria (cuantas más personas prefieran a un candidato sobre su oponente, más fuerte será la victoria). Siempre que se pueda bloquear el borde en el gráfico sin crear un ciclo, se agrega el borde; de lo contrario, el borde se ignora.

¿Cómo funcionaría esto en el caso de las votaciones anteriores? Bueno, el margen más grande de victoria para una pareja es Alice venciendo a Bob, ya que 7 votantes prefieren a Alice sobre Bob (ninguna otra confrontación mano a mano tiene un ganador preferido por más de 7 votantes). Por lo tanto, la flecha de Alice-Bob se bloquea primero en el gráfico. El siguiente margen de victoria más grande es la victoria de Charlie por 6-3 sobre Alice, por lo que esa flecha se bloquea a continuación.

Lo siguiente es la victoria de 5-4 de Bob sobre Charlie. Pero, ¿notaron? Si agregamos una flecha de Bob a Charlie ahora, ¡crearemos un ciclo! Como el gráfico no puede permitir ciclos, debemos saltar este borde y no agregarlo al gráfico en absoluto. Si hubiera más flechas para considerar, miraríamos a las próximas, pero ese fue el última flecha, por lo que el gráfico está completo.

Este proceso paso a paso se muestra a continuación, con el gráfico final a la derecha.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/lockin.png)

En función del gráfico resultante, Charlie es la fuente (no hay flecha apuntando hacia Charlie), por lo que se declara a Charlie ganador de esta elección.

Más formalmente, el método de votación de Tideman consta de tres partes:

*   **Conteo**: Una vez que todos los votantes han indicado todas sus preferencias, determina, para cada par de candidatos, quién es el candidato preferido y por qué margen es preferido.
*   **Ordenamiento**: Ordena los pares de candidatos en orden decreciente de la fuerza de la victoria, donde la fuerza de la victoria se define como el número de votantes que prefieren al candidato preferido.
*   **Bloqueo**: Comenzando con el par más fuerte, atraviesa los pares de candidatos en orden y "bloquea" cada par en el gráfico de candidatos, siempre y cuando bloquear ese par no cree un ciclo en el gráfico.

¡Una vez que el gráfico está completo, la fuente del gráfico (la que no tiene bordes que apunten hacia ella) es la ganadora!

Comenzando
---------------

Inicie sesión en [code.cs50.io] (https://code.cs50.io/), haga clic en la ventana de su terminal y ejecute `cd` por sí solo. Debe encontrar que el símbolo del sistema de la ventana de su terminal se asemeja al siguiente:

    $ 
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/3/tideman.zip
    

para descargar un ZIP llamado `tideman.zip` en su espacio de códigos.

Luego ejecute

    unzip tideman.zip
    

para crear una carpeta llamada `tideman`. Ya no necesita el archivo ZIP, así que puede ejecutar

    rm tideman.zip
    

y responder con "y" seguido de Enter en el símbolo del sistema para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd tideman
    

seguido de Enter para moverse (es decir, abrir) ese directorio. Ahora el símbolo del sistema debería parecerse al siguiente.

    tideman/ $
    

Si todo fue exitoso, debería ejecutar

    ls
    

y ver un archivo llamado `tideman.c`. Ejecutar `code tideman.c` debería abrir el archivo donde escribirá su código para este conjunto de problemas. Si no es así, retroceda en sus pasos y vea si puede determinar dónde se equivocó.

Comprensión
-------------

Echemos un vistazo a `tideman.c`.

Primero, observe la matriz bidimensional 'preferences'. El número entero `preferences[i][j]` representará la cantidad de votantes que prefieren al candidato `i` sobre el candidato `j`.

El archivo también define otra matriz bidimensional llamada 'locked', que representará el grafo de candidatos. 'Locked' es una matriz booleana, por lo que 'locked[i][j]' siendo 'true' representa la existencia de una arista que apunta desde el candidato 'i' al candidato 'j'; 'false' significa que no hay borde. (Si tiene curiosidad, esta representación de un grafo se conoce como "matriz de adyacencia").

A continuación, se encuentra una `estructura` llamada `pair`, que se utiliza para representar un par de candidatos: cada par incluye el índice del candidato `ganador` y el índice del candidato `perdedor`.

Los propios candidatos se almacenan en el arreglo `candidates`, que es un arreglo de `string`s que representan los nombres de cada uno de los candidatos. También hay una matriz de `pairs`, que representará todos los pares de candidatos (para los cuales se prefiere uno sobre el otro) en la elección.

El programa también tiene dos variables globales: `pair_count` y `candidate_count`, que representan la cantidad de pares y la cantidad de candidatos en los arreglos `pairs` y `candidates`, respectivamente.

Ahora pasando al `main`. Observe que después de determinar la cantidad de candidatos, el programa recorre el grafo `locked` y establece todos los valores en `falso` inicialmente, lo que significa que nuestro grafo inicial no tendrá bordes.

A continuación, el programa recorre todos los votantes y recopila sus preferencias en una matriz llamada `ranks` (a través de una llamada a `vote`), donde `ranks[i]` es el índice del candidato que es la `i`ª preferencia para el votante. Estos rangos se pasan a la función `record_preference`, cuyo trabajo es tomar esos rangos y actualizar la variable global `preferences`.

Una vez que se han contado todos los votos, los pares de candidatos se agregan al arreglo `pairs` a través de una llamada a `add_pairs`, se ordenan a través de una llamada a `sort_pairs` y se bloquean en el grafo a través de una llamada a `lock_pairs`. ¡Finalmente, se llama a `print_winner` para imprimir el nombre del ganador de la elección!

Más abajo en el archivo, verá que las funciones `vote`, `record_preference`, `add_pairs`,`sort_pairs`, `lock_pairs` y `print_winner` están en blanco. Depende de usted completarlas!

Especificación
-------------

Completa la implementación de `tideman.c` de tal manera que simule una elección tipo "Tideman".

*   Completa la función `vote`.
    *   La función toma los argumentos `rank`, `name` y `ranks`. Si `name` coincide con el nombre de un candidato válido, deberías actualizar el array `ranks` para indicar que el votante tiene al candidato como su preferencia de `rank` (donde `0` es la primera preferencia, `1` es la segunda, etc.).
    *   Recuerda que `ranks[i]` representa la i-ésima preferencia del usuario.
    *   La función debe devolver `true` si la preferencia se registró correctamente y `false` de lo contrario (si, por ejemplo, `name` no es el nombre de ninguno de los candidatos).
    *   Puedes asumir que ningún candidato tendrá el mismo nombre.
*   Completa la función `record_preferences`.
    *   La función se llama una vez por cada votante y toma como argumento el array de `ranks` (recuerda que `ranks[i]` es la i-ésima preferencia del votante, donde `ranks[0]` es la primera preferencia).
    *   La función debe actualizar el array global `preferences` para agregar las preferencias del votante actual. Recuerda que `preferences[i][j]` debe representar el número de votantes que prefieren al candidato `i` sobre el candidato `j`.
    *   Puedes asumir que cada votante clasificará a todos los candidatos.
*   Completa la función `add_pairs`.
    *   La función debe agregar todas las parejas de candidatos donde un candidato es preferido en el array `pairs`. No se debe agregar una pareja de candidatos que estén empatados (uno no es preferido sobre el otro).
    *   La función debe actualizar la variable global `pair_count` para que sea el número de parejas de candidatos. (Las parejas deberán estar todas almacenadas entre `pairs[0]` y `pairs[pair_count - 1]`, ambas inclusive).
*   Completa la función `sort_pairs`.
    *   La función debe ordenar el array `pairs` en orden decreciente de fortaleza de victoria, donde la fortaleza de victoria se define como el número de votantes que prefieren al candidato preferido. Si varias parejas tienen la misma fortaleza de victoria, se puede asumir que el orden no importa.
*   Completa la función `lock_pairs`.
    *   La función debe crear el grafo `locked`, agregando todas las aristas en orden decreciente de la fortaleza de victoria siempre y cuando la arista no cree un ciclo.
*   Completa la función `print_winner`.
    *   La función debe imprimir el nombre del candidato que es la fuente del grafo. Puedes asumir que no habrá más de una fuente.

No debes modificar nada más en `tideman.c` aparte de las implementaciones de las funciones `vote`, `record_preferences`, `add_pairs`, `sort_pairs`, `lock_pairs`, y `print_winner` (y la inclusión de archivos de encabezado adicionales, si lo deseas). Se te permite agregar funciones adicionales a `tideman.c`, siempre y cuando no cambies las declaraciones de las funciones existentes.

Tutorial
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/kb83NwyYI68?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Uso
---

Su programa debe comportarse como se muestra en el ejemplo a continuación:

    ./tideman Alice Bob Charlie
    Número de votantes: 5
    Rango 1: Alice
    Rango 2: Charlie
    Rango 3: Bob
    
    Rango 1: Alice
    Rango 2: Charlie
    Rango 3: Bob
    
    Rango 1: Bob
    Rango 2: Charlie
    Rango 3: Alice
    
    Rango 1: Bob
    Rango 2: Charlie
    Rango 3: Alice
    
    Rango 1: Charlie
    Rango 2: Alice
    Rango 3: Bob
    
    Charlie
    

Prueba
------

Asegúrese de probar su código para verificar que maneje...

*   Una elección con cualquier número de candidatos (hasta un máximo de `9`)
*   Votar por un candidato por su nombre
*   Votos inválidos por candidatos que no están en la lista
*   Imprimir el ganador de la elección

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilarlo y probarlo también!

    check50 cs50/problems/2023/x/tideman
    

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 tideman.c
    

Cómo enviar
-----------

En la terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/tideman

