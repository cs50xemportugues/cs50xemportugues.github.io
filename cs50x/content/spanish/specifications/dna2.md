Antecedentes
----------

El ADN, el portador de la información genética en los seres vivos, ha sido utilizado en la justicia criminal durante décadas. Pero, ¿cómo funciona exactamente el perfilado de ADN? Dada una secuencia de ADN, ¿cómo pueden los investigadores forenses identificar a quién pertenece?

Bueno, el ADN es realmente solo una secuencia de moléculas llamadas nucleótidos, dispuestas en una forma particular (una doble hélice). Cada célula humana tiene miles de millones de nucleótidos dispuestos en secuencia. Cada nucleótido del ADN contiene una de las cuatro bases diferentes: adenina (A), citosina (C), guanina (G) o timina (T). Algunas partes de esta secuencia (es decir, genoma) son iguales, o al menos muy similares, en casi todos los humanos, pero otras partes de la secuencia tienen una mayor diversidad genética y, por lo tanto, varían más en la población.

Un lugar donde el ADN tiende a tener una alta diversidad genética es en las Repeticiones de Tándem Corto (STR). Un STR es una breve secuencia de bases de ADN que tiende a repetirse consecutivamente numerosas veces en ubicaciones específicas dentro del ADN de una persona. El número de veces que se repite cada STR particular varía mucho entre los individuos. En las muestras de ADN a continuación, por ejemplo, Alice tiene la secuencia "AGAT" repetida cuatro veces en su ADN, mientras que Bob tiene el mismo STR repetido cinco veces.

![STRs de muestra](https://cs50.harvard.edu/x/2023/psets/6/dna/strs.png)

El uso de múltiples STR, en lugar de solo uno, puede mejorar la precisión del perfilado de ADN. Si la probabilidad de que dos personas tengan el mismo número de repeticiones para un solo STR es del 5%, y el analista observa 10 STR diferentes, entonces la probabilidad de que dos muestras de ADN coincidan solo por casualidad es de aproximadamente 1 en un billón (suponiendo que todos los STR son independientes entre sí). Entonces, si dos muestras de ADN coinciden en el número de repeticiones para cada uno de los STR, el analista puede estar bastante seguro de que provienen de la misma persona. CODIS, la base de datos de ADN del FBI, utiliza 20 STR diferentes como parte de su proceso de perfilado de ADN.

¿Cómo podría ser una base de datos de ADN? Bueno, en su forma más simple, se podría imaginar un formato de base de datos de ADN como un archivo CSV, donde cada fila corresponde a un individuo y cada columna corresponde a un STR en particular.

    nombre,AGAT,AATG,TATC
    Alice,28,42,14
    Bob,17,22,19
    Charlie,36,18,25
    

Los datos en el archivo anterior indicarían que Alice tiene la secuencia "AGAT" repetida 28 veces consecutivamente en alguna parte de su ADN, la secuencia "AATG" repetida 42 veces, y "TATC" repetida 14 veces. Mientras tanto, Bob tiene esos mismos tres STR repetidos 17, 22 y 19 veces, respectivamente. Y Charlie tiene esos mismos tres STR repetidos 36, 18 y 25 veces, respectivamente.

Entonces, dada una secuencia de ADN, ¿cómo podríamos identificar a quién pertenece? Bueno, imagina que buscamos en la secuencia de ADN la secuencia consecutiva más larga de "AGATs" y descubrimos que la secuencia más larga tiene 17 repeticiones. Si luego encontramos que la secuencia más larga de "AATG" tiene 22 repeticiones y que la secuencia más larga de "TATC" tiene 19 repeticiones, eso proporcionaría evidencia bastante buena de que el ADN era de Bob. Por supuesto, también es posible que, una vez que tomemos el recuento para cada uno de los STR, no coincida con ninguna persona en nuestra base de datos de ADN, en cuyo caso no hay coincidencia.

En la práctica, ya que los analistas saben en qué cromosoma y en qué ubicación del ADN se encontrará un STR, pueden localizar su búsqueda en solo una sección estrecha del ADN. Pero ignoraremos ese detalle para este problema.

Su tarea es escribir un programa que tome una secuencia de ADN y un archivo CSV que contenga recuentos de STR para una lista de individuos y luego indique a quién (probablemente) pertenece el ADN.