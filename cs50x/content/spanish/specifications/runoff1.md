Runoff
======

En este programa, implementarás un programa que lleva a cabo una elección de desempate (runoff en inglés), tal como se muestra a continuación.

    ./runoff Alice Bob Charlie
    Número de votantes: 5
    Rango 1: Alice
    Rango 2: Bob
    Rango 3: Charlie
    
    Rango 1: Alice
    Rango 2: Charlie
    Rango 3: Bob
    
    Rango 1: Bob
    Rango 2: Charlie
    Rango 3: Alice
    
    Rango 1: Bob
    Rango 2: Alice
    Rango 3: Charlie
    
    Rango 1: Charlie
    Rango 2: Alice
    Rango 3: Bob
    
    Alice
    

Antecedentes
----------

Ya conoces las elecciones por pluralidad, que siguen un algoritmo muy simple para determinar el ganador de una elección: cada votante obtiene un voto y el candidato con la mayoría de votos gana.

Pero la votación por pluralidad tiene algunas desventajas. ¿Qué sucede, por ejemplo, en una elección con tres candidatos, y se emiten las siguientes papeletas?

![Five ballots, tie betweeen Alice and Bob](https://cs50.harvard.edu/x/2023/psets/3/fptp_ballot_1.png)

Una elección por pluralidad declararía un empate entre Alice y Bob, ya que cada uno tiene dos votos. Pero, ¿es ese el resultado correcto?

Existe otro tipo de sistema de votación conocido como sistema de votación ponderada por rango. En un sistema de votación ponderada por rango, los votantes pueden votar por más de un candidato. En lugar de votar solo por su candidato favorito, pueden clasificar los candidatos en orden de preferencia. Las papeletas resultantes podrían verse así:

![Three ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_1.png)

Aquí, cada votante, además de especificar su candidato de primera preferencia, también ha indicado sus segundas y terceras opciones. Y ahora, lo que antes era una elección empatada podría tener un ganador. La carrera estaba originalmente empatada entre Alice y Bob, así que Charlie quedó fuera de la contienda. Pero el votante que eligió a Charlie prefirió a Alice sobre Bob, por lo que aquí Alice podría ser declarada la ganadora.

La votación ponderada por rango también puede resolver otra posible desventaja de la votación por pluralidad. Observa las siguientes papeletas.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_3.png)

¿Quién debería ganar esta elección? En una elección por pluralidad en la que cada votante elige solo su primera preferencia, Charlie gana esta elección con cuatro votos en comparación con solo tres para Bob y dos para Alice. Pero la mayoría de los votantes (5 de los 9) estarían más felices con Alice o Bob que con Charlie. Al considerar las preferencias ponderadas, un sistema de votación puede elegir un ganador que refleje mejor las preferencias de los votantes.

Uno de estos sistemas de votación ponderada por rango es el sistema de votación por desempate inmediato. En una elección por desempate inmediato, los votantes pueden clasificar tantos candidatos como deseen. Si algún candidato tiene una mayoría (más del 50%) de los votos de primera preferencia, ese candidato es declarado el ganador de la elección.

Si ningún candidato tiene más del 50% de los votos, entonces se lleva a cabo un "desempate inmediato". Se elimina el candidato que recibió la menor cantidad de votos, y se considera la segunda preferencia de cualquiera que eligió a ese candidato como su primera preferencia. ¿Por qué hacerlo de esta manera? Efectivamente, esto simula lo que hubiera sucedido si el candidato menos popular no hubiera estado en la elección desde un principio.

El proceso se repite: si ningún candidato tiene una mayoría de los votos, se elimina al candidato en último lugar, y aquellos que votaron por él votarán por su próxima preferencia (que no se haya eliminado). Una vez que un candidato tiene la mayoría, ese candidato es declarado ganador.

Consideremos las nueve papeletas anteriores y examinemos cómo se llevaría a cabo una elección de desempate.

Alice tiene dos votos, Bob tiene tres y Charlie tiene cuatro votos. Para ganar una elección con nueve personas, se requiere una mayoría (cinco votos). Como nadie tiene la mayoría, se debe realizar un desempate. Alice tiene la menor cantidad de votos (solo dos), por lo que se elimina. Los votantes que originalmente votaron por Alice eligieron a Bob como segunda opción, así que Bob obtiene dos votos extra. Bob ahora tiene cinco votos y Charlie todavía tiene cuatro. Bob ahora tiene una mayoría y es declarado ganador.

¿Qué casos especiales debemos considerar aquí?

Una posibilidad es que haya un empate para saber quién debe ser eliminado. Podemos manejar ese escenario diciendo que todos los candidatos empatados en último lugar serán eliminados. Sin embargo, si cada candidato restante tiene exactamente la misma cantidad de votos, ¡eliminar a los candidatos empatados en último lugar significa eliminar a todos! Entonces, en ese caso, tendremos que tener cuidado de no eliminar a todos y simplemente declarar la elección como un empate entre todos los candidatos restantes.

Algunas elecciones por desempate inmediato no requieren que los votantes clasifiquen todas sus preferencias, por lo que puede haber cinco candidatos en una elección, pero un votante podría elegir solo dos. Sin embargo, para los propósitos de este problema, ignoraremos ese caso particular y asumiremos que todos los votantes clasificarán a todos los candidatos en su orden de preferencia.

¿Suena un poco más complicado que una votación por pluralidad, no es así? Pero tiene la ventaja de ser un sistema de votación en el que el ganador de la elección representa con mayor precisión las preferencias de los votantes.