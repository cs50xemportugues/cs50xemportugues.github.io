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