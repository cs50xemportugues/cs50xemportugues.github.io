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

Empezando
----------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en su ventana de terminal y ejecute `cd` por sí solo. Debería encontrar que el símbolo del sistema de su ventana de terminal se asemeja al siguiente:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/3/runoff.zip
    

para descargar un archivo ZIP llamado `runoff.zip` en su espacio de programación.

Luego ejecute

    unzip runoff.zip
    

para crear una carpeta llamada `runoff`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm runoff.zip
    

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que ha descargado.

Ahora escriba

    cd runoff
    

seguido de Enter para moverse (es decir, abrir) a ese directorio. Su símbolo del sistema debería parecerse al siguiente.

    runoff/ $
    

Si todo se realizó con éxito, debería ejecutar

    ls
    

y ver un archivo llamado `runoff.c`. Ejecutar `code runoff.c` debería abrir el archivo donde escribirá su código para este conjunto de problemas. Si no, vuelva sobre sus pasos y vea si puede determinar dónde se equivocó.

Entendiendo
-----------

Echemos un vistazo a `runoff.c`. Estamos definiendo dos constantes: `MAX_CANDIDATES` para el número máximo de candidatos en la elección, y `MAX_VOTERS` para el número máximo de votantes en la elección.

A continuación, tenemos un array bidimensional llamado `preferences`. El array `preferences[i]` representará todas las preferencias del votante número `i`, y el número entero `preferences[i][j]` aquí almacenará el índice del candidato que es la `j`-ésima preferencia del votante `i`.

Luego, tenemos una estructura llamada `candidate`. Cada `candidate` tiene un campo `string` para su `nombre`, un `int` que representa el número de `votos` que tienen actualmente y un valor `bool` llamado `eliminated` que indica si el candidato ha sido eliminado de la elección. El array `candidates` llevará un registro de todos los candidatos en la elección.

El programa también tiene dos variables globales: `voter_count` y `candidate_count`.

Ahora, sobre `main`. Observe que después de determinar el número de candidatos y el número de votantes, comienza el bucle principal de votación, dando a cada votante la oportunidad de votar. A medida que el votante ingresa sus preferencias, se llama a la función `vote` para llevar un registro de todas las preferencias. Si en algún momento, se determina que la boleta es inválida, el programa se detiene.

Una vez que se hayan emitido todos los votos, comienza otro bucle que mantendrá la secuencia de las votaciones para verificar al ganador y eliminar al candidato en último lugar hasta que haya un ganador.

La primera llamada aquí es a una función llamada `tabulate`, que debería mirar todas las preferencias de los votantes y calcular los totales de votos actuales, mirando al candidato preferido de cada votante que aún no ha sido eliminado. A continuación, la función `print_winner` debería imprimir al ganador si lo hay; si lo hay, se termina el programa. Pero de lo contrario, el programa necesita determinar la cantidad más baja de votos que recibió cualquier persona que aún esté en la elección (a través de una llamada a `find_min`). Si resulta que todos los que están en la elección están empatados con el mismo número de votos (como lo determina la función `is_tie`), la elección se declara empatada; de lo contrario, se elimina al candidato (o candidatos) en último lugar de la elección a través de una llamada a la función `eliminate`.

Si mira un poco más abajo en el archivo, verá que estas funciones: `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` y `eliminate` se dejan todas a su cargo para completar!

Especificación
-------------

Completa la implementación de `runoff.c` de tal manera que simule una elección de desempate. Debes completar las implementaciones de las funciones `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` y `eliminate`, y no debes modificar nada más en `runoff.c` (y la inclusión de archivos de cabecera adicionales, si lo deseas).

### `voto`

Completa la función `vote`.

*   La función toma los argumentos `votante`, `clasificación` y `nombre`. Si `nombre` es una coincidencia con el nombre de un candidato válido, entonces debes actualizar la matriz global de preferencias para indicar que el votante `votante` tiene ese candidato como su preferencia de `clasificación` (donde `0` es la primera preferencia, `1` es la segunda preferencia, etc.). 
*   Si se registra la preferencia correctamente, la función debe devolver `true`; la función debe devolver `false` de lo contrario (por ejemplo, si `nombre` no es el nombre de uno de los candidatos).
*   Se puede asumir que ningún candidato tendrá el mismo nombre.


<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que `candidate_count` almacena el número de candidatos en la elección.</li>
  <li data-marker="*">Recuerda que puedes utilizar <a href="https://man.cs50.io/3/strcmp"><code class="language-plaintext highlighter-rouge">strcmp</code></a> para comparar dos cadenas.</li>
  <li data-marker="*">Recuerda que `preferences[i][j]` almacena el índice del candidato que es la preferencia clasificada como número <code class="language-plaintext highlighter-rouge">j</code> para el votante <code class="language-plaintext highlighter-rouge">i</code>.</li>
</ul></details>

### `tabulate`

Completa la función `tabulate`.

*   La función debe actualizar el número de `votos` que tiene cada candidato en esta etapa de la elección.
*   Recuerda que en cada etapa del proceso, cada votante vota efectivamente por su candidato mejor clasificado que aún no haya sido eliminado.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que `voter_count` almacena el número de votantes en la elección y que, por cada votante en nuestra elección, queremos contar un voto.</li>
  <li data-marker="*">Recuerda que para un votante <code class="language-plaintext highlighter-rouge">i</code>, el candidato de su preferencia principal está representado por <code class="language-plaintext highlighter-rouge">preferences[i][0]</code>, su segundo candidato de preferencia por <code class="language-plaintext highlighter-rouge">preferences[i][1]</code>, etc.</li>
  <li data-marker="*">Recuerda que la estructura <code class="language-plaintext highlighter-rouge">candidato</code> tiene un campo llamado `eliminado`, que será verdadero si el candidato ha sido eliminado de la elección.</li>
  <li data-marker="*">Recuerda que la estructura `candidato` tiene un campo llamado `votos`, que probablemente querrás actualizar para el candidato preferido de cada votante.</li>
  <li data-marker="*">Una vez que has emitido un voto para el primer candidato no eliminado del votante, probablemente querrás detenerte allí, ¡no continuar en su voto! Recuerda que puedes salir de un ciclo temprano usando `break` dentro de una condicional.</li>
</ul></details>

### `print_winner`

Completa la función `print_winner`.

*   Si algún candidato tiene más de la mitad de los votos, su nombre debe ser impreso y la función debe devolver `true`.
*   Si nadie ha ganado la elección todavía, la función debe devolver `false`.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que `voter_count` almacena el número de votantes en la elección. Dado eso, ¿cómo expresarías el número de votos necesarios para ganar la elección?</li>
</ul></details>

### `find_min`

Completa la función `find_min`.

*   La función debería devolver el total mínimo de votos para cualquier candidato que aún esté en la elección.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Probablemente querrás recorrer los candidatos para encontrar al que todavía está en la elección y tiene el menor número de votos. ¿Qué información deberías tener en cuenta mientras recorres los candidatos?</li>
</ul></details>

### `is_tie`

Completa la función `is_tie`.

*   La función toma un argumento `min`, que será el número mínimo de votos que alguien en la elección tiene actualmente.
*   La función debe devolver `true` si cada candidato que permanece en la elección tiene el mismo número de votos, y debe devolver `false` de lo contrario.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que un empate ocurre si cada candidato que todavía está en la elección tiene el mismo número de votos. Además, la función `is_tie` toma un argumento `min`, que es la cantidad más pequeña de votos que cualquier candidato tiene actualmente. ¿Cómo podrías usar esa información para determinar si la elección es un empate o, por el contrario, no es un empate?</li>
</ul></details>

### `eliminate`

Completa la función `eliminate`.

*   La función toma un argumento `min`, que será el número mínimo de votos que alguien en la elección tenga actualmente.
*   La función debería eliminar al candidato (o candidatos) que tengan un número `min` de votos.

Paseo
------


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Uso
---

Su programa debería comportarse como se muestra en el siguiente ejemplo:

    ./runoff Alice Bob Charlie
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
    
    Alice
    

Prueba
------

Asegúrese de probar su código para asegurarse de que maneja...

*  Una elección con cualquier número de candidatos (hasta un máximo de "9" )
*   Votación por nombre de candidato
*   Votos inválidos para candidatos que no están en la boleta
*   Imprimir al ganador de la elección si hay solamente uno
*   No eliminar a nadie en caso de un empate entre todos los candidatos restantes

Ejecute el siguiente comando para evaluar la exactitud de su código utilizando "check50". Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50/problems/2023/x/runoff
    

Ejecute el siguiente comando para evaluar el estilo de su código utilizando "style50".

    style50 runoff.c
    

Cómo enviar
-----------

En su terminal, ejecute el siguiente comando para enviar su trabajo.

    submit50 cs50/problems/2023/x/runoff"

