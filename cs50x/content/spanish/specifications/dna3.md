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