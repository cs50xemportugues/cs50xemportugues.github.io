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