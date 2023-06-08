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