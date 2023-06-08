ADN
===

Implemente un programa que identifique a una persona en función de su ADN, como se muestra a continuación.

    $ python dna.py databases/large.csv sequences/5.txt
    Lavender
    

Para empezar
---------------

Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en la ventana del terminal y ejecute `cd` por sí solo. Debería ver que la ventana del terminal muestra lo siguiente:

    $
    

A continuación, ejecute

    wget https://cdn.cs50.net/2022/fall/psets/6/dna.zip
    

para descargar un archivo ZIP llamado `dna.zip` en su espacio de trabajo.

Luego, ejecute

    unzip dna.zip
    

para crear una carpeta llamada `dna`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm dna.zip
    

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd dna
    

seguido de Enter para moverse (es decir, abrir) a ese directorio. Su indicador denotaera el siguiente

    dna/ $
    

Ejecute `ls` por sí solo y debería ver algunos archivos y carpetas:

    databases/ dna.py sequences/
    

Si tiene algún problema, siga estos mismos pasos de nuevo y vea si puede determinar dónde se equivocó.

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

Especificación
-------------

En un archivo llamado `dna.py`, implemente un programa que identifique a quién pertenece una secuencia de ADN.

* El programa debe requerir como primer argumento de línea de comandos el nombre de un archivo CSV que contenga los recuentos STR para una lista de individuos y como segundo argumento de línea de comandos el nombre de un archivo de texto que contenga la secuencia de ADN a identificar.
    * Si su programa se ejecuta con el número incorrecto de argumentos de línea de comandos, su programa debe imprimir un mensaje de error de su elección (con `print`). Si se proporciona la cantidad correcta de argumentos, puede suponer que el primer argumento es de hecho el nombre de archivo de un archivo CSV válido y que el segundo argumento es el nombre de archivo de un archivo de texto válido.
* Su programa debe abrir el archivo CSV y leer su contenido en memoria.
    * Puede suponer que la primera fila del archivo CSV será el nombre de las columnas. La primera columna será la palabra `name` y las columnas restantes serán las propias secuencias STR.
* Su programa debe abrir la secuencia de ADN y leer su contenido en memoria.
* Para cada uno de los STR (de la primera línea del archivo CSV), su programa debe calcular la corrida más larga de repeticiones consecutivas del STR en la secuencia de ADN a identificar. ¡Observe que hemos definido una función auxiliar para usted,`longest_match`, que hará exactamente eso!
* Si los recuentos STR coinciden exactamente con cualquiera de los individuos en el archivo CSV, su programa debe imprimir el nombre del individuo coincidente.
    * Puede suponer que los recuentos STR no coincidirán con más de un individuo.
    * Si los recuentos STR no coinciden exactamente con ninguno de los individuos en el archivo CSV, su programa debe imprimir `No match`.

Demostración
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/j84b_EgntcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Uso
-----

Su programa debe comportarse como se muestra a continuación:

<pre>
$ python dna.py databases/large.csv sequences/5.txt
Lavender
</pre>

<pre>
$ python dna.py
Uso: python dna.py data.csv sequence.txt
</pre>

<pre>
$ python dna.py data.csv
Uso: python dna.py data.csv sequence.txt
</pre>

Pistas
-------

* Puede resultar útil el módulo [`csv`](https://docs.python.org/3/library/csv.html) de Python para leer archivos CSV en memoria. Puede aprovechar tanto [`csv.reader`](https://docs.python.org/3/library/csv.html#csv.reader) como [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader).
* Las funciones [`open`](https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files) y [`read`](https://docs.python.org/3.3/tutorial/inputoutput.html#methods-of-file-objects) pueden ser útiles para leer archivos de texto en memoria.
* Considere qué estructuras de datos pueden ser útiles para realizar un seguimiento de la información en su programa. Una [`list`](https://docs.python.org/3/tutorial/introduction.html#lists) o un [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) pueden ser útiles.
* Recuerde que hemos definido una función (`longest_match`) que, dadas una secuencia de ADN y un STR como entradas, devuelve el número máximo de repeticiones del STR. ¡Entonces puede usar esa función en otras partes de su programa!

Pruebas
-------

Si bien `check50` está disponible para este problema, se anima a probar primero su código por cuenta propia para cada una de las siguientes pruebas.

* Ejecute su programa como `python dna.py databases/small.csv sequences/1.txt`. Su programa debería devolver `Bob`.
* Ejecute su programa como `python dna.py databases/small.csv sequences/2.txt`. Su programa debería devolver `No match`.
* Ejecute su programa como `python dna.py databases/small.csv sequences/3.txt`. Su programa debería devolver `No match`.
* Ejecute su programa como `python dna.py databases/small.csv sequences/4.txt`. Su programa debería devolver `Alice`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/5.txt`. Su programa debería devolver `Lavender`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/6.txt`. Su programa debería devolver `Luna`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/7.txt`. Su programa debería devolver `Ron`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/8.txt`. Su programa debería devolver `Ginny`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/9.txt`. Su programa debería devolver `Draco`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/10.txt`. Su programa debería devolver `Albus`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/11.txt`. Su programa debería devolver `Hermione`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/12.txt`. Su programa debería devolver `Lily`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/13.txt`. Su programa debería devolver `No match`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/14.txt`. Su programa debería devolver `Severus`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/15.txt`. Su programa debería devolver `Sirius`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/16.txt`. Su programa debería devolver `No match`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/17.txt`. Su programa debería devolver `Harry`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/18.txt`. Su programa debería devolver `No match`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/19.txt`. Su programa debería devolver `Fred`.
* Ejecute su programa como `python dna.py databases/large.csv sequences/20.txt`. Su programa debería devolver `No match`.

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50/problems/2023/x/dna
    

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 dna.py
    

Cómo Enviar
------------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/dna"

