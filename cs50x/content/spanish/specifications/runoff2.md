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