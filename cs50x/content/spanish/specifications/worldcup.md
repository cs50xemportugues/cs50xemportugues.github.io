Laboratorio 6: Copa Mundial
================

Puede colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante de cualquier grupo contribuya por igual al laboratorio.

Escriba un programa para simular la Copa Mundial de la FIFA.

    $ python tournament.py 2018m.csv
    Bélgica: 20,9% posibilidades de ganar
    Brasil: 20,3% posibilidades de ganar
    Portugal: 14,5% posibilidades de ganar
    España: 13,6% posibilidades de ganar
    Suiza: 10,5% posibilidades de ganar
    Argentina: 6,5% posibilidades de ganar
    Inglaterra: 3,7% posibilidades de ganar
    Francia: 3,3% posibilidades de ganar
    Dinamarca: 2,2% posibilidades de ganar
    Croacia: 2,0% posibilidades de ganar
    Colombia: 1,8% posibilidades de ganar
    Suecia: 0,5% posibilidades de ganar
    Uruguay: 0,1% posibilidades de ganar
    México: 0,1% posibilidades de ganar
    

Antecedentes
----------

En la Copa Mundial de fútbol, la ronda eliminatoria consta de 16 equipos. En cada ronda, cada equipo juega contra otro equipo y los equipos perdedores son eliminados. Cuando solo quedan dos equipos, el ganador del partido final es el campeón.

En el fútbol, a los equipos se les asignan [Puntuaciones FIFA](https://en.wikipedia.org/wiki/FIFA_World_Rankings#Current_calculation_method), que son valores numéricos que representan el nivel de habilidad relativo de cada equipo. Las puntuaciones FIFA más altas indican mejores resultados previos en los partidos y, dadas las puntuaciones FIFA de dos equipos previos, es posible estimar la probabilidad de que cualquiera de los dos equipos gane un partido según sus puntuaciones actuales. Las Puntuaciones FIFA de las dos Copas del Mundo anteriores están disponibles como las [Puntuaciones de Hombres de mayo de 2018 de la FIFA](https://www.fifa.com/fifa-world-ranking/ranking-table/men/rank/id12189/) and [March 2019 Women’s FIFA Ratings](https://www.fifa.com/fifa-world-ranking/ranking-table/women/rank/ranking_20190329/).

Usando esta información, podemos simular todo el torneo simulando repetidamente rondas hasta que solo quede un equipo. Y si queremos estimar cuán probable es que cualquier equipo en particular gane el torneo, podríamos simular el torneo muchas veces (por ejemplo, 1000 simulaciones) y contar cuántas veces cada equipo gana un torneo simulado. 1000 simulaciones pueden parecer muchas, pero con la potencia informática actual podemos llevar acabo esas simulaciones en cuestión de milisegundos. Al final de este laboratorio, experimentaremos qué tan valioso puede ser aumentar el número de simulaciones que realizamos, dada la compensación de tiempo de ejecución.

¡Su tarea en este laboratorio es hacer precisamente eso usando Python!

Comenzando
---------------

Abra [VS Code] (https://code.cs50.io/).

Comience haciendo clic dentro de la ventana del terminal y luego ejecute `cd`. Debería encontrar que su "prompt" se parece al siguiente.

    $
    
Haga clic dentro de esa ventana del terminal y luego ejecute

    wget https://cdn.cs50.net/2022/fall/labs/6/world-cup.zip

seguido de Enter para descargar un archivo ZIP llamado `world-cup.zip` en su espacio de código. ¡Tenga cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter!

Ahora ejecute

    unzip world-cup.zip
    
para crear una carpeta llamada `world-cup`. Ya no necesita el archivo ZIP, así que puede ejecutar 

    rm world-cup.zip
    
y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd world-cup
    
seguido de Enter para moverse (es decir, abrir) ese directorio. Su prompt ahora debería parecerse al siguiente.

    world-cup/ $

Si todo fue exitoso, debería ejecutar

    ls
    
y debería ver los siguientes archivos:

    answers.txt 2018m.csv  2019w.csv  tournament.py

Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.

Comprensión
-------------

Comience por echar un vistazo al archivo `2018m.csv`. Este archivo contiene los 16 equipos en la ronda eliminatoria de la Copa Mundial de la FIFA 2018 para hombres y las clasificaciones para cada equipo. Observe que el archivo CSV tiene dos columnas, una llamada `team` (que representa el nombre del país del equipo) y otra llamada `rating` (que representa la clasificación del equipo).

El orden en que se enumeran los equipos determina qué equipos jugarán entre sí en cada ronda (en la primera ronda, por ejemplo, Uruguay jugará contra Portugal y Francia jugará contra Argentina; en la siguiente ronda, el ganador del partido Uruguay-Portugal jugará contra el ganador del partido Francia-
Argentina). Por lo tanto, ¡asegúrese de no editar el orden en que aparecen los equipos en este archivo!

En Python, podemos representar cada equipo como un diccionario que contiene dos valores: el nombre del equipo y la clasificación. Por ejemplo, Uruguay lo representaríamos en Python como `{"team": "Uruguay", "rating": 976}`.

A continuación, eche un vistazo a `2019w.csv`, que contiene datos formateados de la misma manera para la Copa Mundial Femenina de la FIFA 2019.

Ahora, abra `tournament.py` y vea que ya hemos escrito algo de código para usted. La variable `N` en la parte superior representa cuántas simulaciones de la Copa Mundial se ejecutarán: en este caso, 1000.

La función `simulate_game` acepta dos equipos como entradas (recuerde que cada equipo es un diccionario que contiene el nombre del equipo y la clasificación del equipo) y simula un partido entre ellos. Si el primer equipo gana, la función devuelve `True`; de lo contrario, la función devuelve `False`.

La función `simulate_round` acepta una lista de equipos (en una variable llamada `teams`) como entrada y simula partidos entre cada par de equipos. Luego, la función devuelve una lista de todos los equipos que ganaron la ronda.

En la función `main`, observe que primero aseguramos que `len(sys.argv)` (el número de argumentos de línea de comandos) sea 2. Usaremos argumentos de línea de comandos para decirle a Python qué archivo CSV de equipos usar para ejecutar la simulación de torneo. Luego hemos definido una lista llamada `teams` (que eventualmente será una lista de equipos) y un diccionario llamado `counts` (que asociará los nombres de los equipos con el número de veces que ese equipo ganó un torneo simulado). Por ahora, ambos están vacíos, ¡así que su población depende de usted!

Finalmente, al final de `main`, ordenamos los equipos en orden descendente de cuántas veces ganaron las simulaciones (según `counts`) e imprimimos la probabilidad estimada de que cada equipo gane la Copa Mundial.

¡La población de `teams` y `counts` y la escritura de la función `simulate_tournament` quedan a su cargo!

Detalles de Implementación
----------------------

Completa la implementación de `tournament.py`, de modo que simule una serie de torneos y muestre la probabilidad de ganar de cada equipo.

En primer lugar, en la función `main`, lee los datos del equipo desde un archivo CSV en la memoria del programa, y agrega cada equipo a la lista `teams`.

*   El archivo a utilizar se proporcionará como argumento de línea de comandos. Puedes acceder al nombre del archivo con `sys.argv[1]`.
*   Recuerda que puedes abrir un archivo con `open(filename)`, donde `filename` es una variable que almacena el nombre del archivo.
*   Una vez que tienes un archivo `f`, puedes usar `csv.DictReader(f)` para darle un "lector": un objeto en Python que puedes recorrer para leer el archivo una fila a la vez, tratando cada fila como un diccionario.
*   De forma predeterminada, todos los valores leídos desde el archivo serán cadenas. Asegúrate de convertir primero la `calificación` del equipo a un `int` (puedes usar la función `int` en Python para hacer esto).
*   En última instancia, agrega el diccionario de cada equipo a `teams`. La llamada a la función `teams.append(x)` agregará `x` a la lista `teams`.
*   Recuerda que cada equipo debe ser un diccionario con el nombre del `equipo` y una `calificación`.

A continuación, implementa la función `simulate_tournament`. Esta función debe aceptar como entrada una lista de equipos y simular repetidamente rondas hasta que te quede un equipo. La función debe devolver el nombre de ese equipo.

*   Puedes llamar a la función `simulate_round`, que simula una única ronda, aceptando una lista de equipos como entrada y devolviendo una lista de todos los ganadores.
*   Recuerda que si `x` es una lista, puedes usar `len(x)` para determinar la longitud de la lista.
*   No debes suponer el número de equipos en el torneo, pero puedes asumir que será una potencia de 2.

Finalmente, en la función `main`, ejecuta `N` simulaciones de torneos y realiza un seguimiento de cuántas veces gana cada equipo en el diccionario `counts`.

*   Por ejemplo, si Uruguay gana 2 torneos y Portugal gana 3 torneos, entonces el diccionario `counts` debería ser `{"Uruguay": 2, "Portugal": 3}`.
*   Debes usar tu función `simulate_tournament` para simular cada torneo y determinar al ganador.
*   Recuerda que si `counts` es un diccionario, la sintaxis como `counts[nombre_equipo] = x` asociará la clave almacenada en `nombre_equipo` con el valor almacenado en `x`.
*   Puedes usar la palabra clave `in` en Python para comprobar si un diccionario ya tiene una clave en particular. Por ejemplo, `if "Portugal" in counts:` comprobará si `"Portugal"` ya tiene un valor existente en el diccionario `counts`.

### Guía

<div class="alert" data-alert="primary" role="alert"><p>Este video fue grabado cuando el curso aún usaba el CS50 IDE para escribir código. Aunque la interfaz puede verse diferente a su codespace, el comportamiento de ambos entornos debería ser en gran medida similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/o5Bkc7gtRjo"></iframe>


### Consejos

*   Al leer el archivo, puede encontrar útil esta sintaxis, con `filename` como el nombre de su archivo y `file` como variable. <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">con</span> <span class="nf">open</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="k">como</span> <span class="nb">file</span><span class="p">:</span>
      <span class="n">    reader</span> <span class="o">=</span> <span class="n">csv</span><span class="p">.</span>DiccionarioLector<span class="p">(</span><span class="nb">file</span><span class="p">)</span>
</code></pre></div>    </div>
        
    
*   En Python, para agregar al final de una lista, use la función `.append()`.
    

<details><summary>¿No estás seguro de cómo resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/Fo7Roe8hw3A"></iframe></details>


### Pruebas

Su programa debe comportarse según los ejemplos a continuación. Dado que las simulaciones tienen aleatoriedad dentro de cada una, es probable que su salida no se ajuste perfectamente a los ejemplos a continuación.

    $ python tournament.py 2018m.csv
    Bélgica: 20.9% de posibilidad de ganar
    Brasil: 20.3% de posibilidad de ganar
    Portugal: 14.5% de posibilidad de ganar
    España: 13.6% de posibilidad de ganar
    Suiza: 10.5% de posibilidad de ganar
    Argentina: 6.5% de posibilidad de ganar
    Inglaterra: 3.7% de posibilidad de ganar
    Francia: 3.3% de posibilidad de ganar
    Dinamarca: 2.2% de posibilidad de ganar
    Croacia: 2.0% de posibilidad de ganar
    Colombia: 1.8% de posibilidad de ganar
    Suecia: 0.5% de posibilidad de ganar
    Uruguay: 0.1% de posibilidad de ganar
    México: 0.1% de posibilidad de ganar
    

    $ python tournament.py 2019w.csv
    Alemania: 17.1% de posibilidad de ganar
    Estados Unidos: 14.8% de posibilidad de ganar
    Inglaterra: 14.0% de posibilidad de ganar
    Francia: 9.2% de posibilidad de ganar
    Canadá: 8.5% de posibilidad de ganar
    Japón: 7.1% de posibilidad de ganar
    Australia: 6.8% de posibilidad de ganar
    Países Bajos: 5.4% de posibilidad de ganar
    Suecia: 3.9% de posibilidad de ganar
    Italia: 3.0% de posibilidad de ganar
    Noruega: 2.9% de posibilidad de ganar
    Brasil: 2.9% de posibilidad de ganar
    España: 2.2% de posibilidad de ganar
    China PR: 2.1% de posibilidad de ganar
    Nigeria: 0.1% de posibilidad de ganar
    

*   Es posible que se pregunte qué sucedió realmente en las Copas del Mundo de 2018 y 2019. En la categoría de hombres, Francia ganó, venciendo a Croacia en la final. Bélgica derrotó a Inglaterra para obtener el tercer lugar. En la categoría de mujeres, Estados Unidos ganó, venciendo a los Países Bajos en la final. Inglaterra derrotó a Suecia para obtener el tercer lugar.

Número de simulaciones
---------------------

Una vez que estés seguro/a de que tu código es correcto, ajusta el valor de `N`, la constante que se encuentra al inicio de nuestro archivo, para modificar el número de veces que simularemos el torneo. Un mayor número de simulaciones de torneos nos dará predicciones más precisas (¿por qué?), pero incrementará el tiempo de ejecución.

Podemos medir el tiempo de ejecución de los programas agregando `time` antes de la ejecución en la línea de comando. Por ejemplo, si establecemos `N` en 1000 (valor predeterminado), ejecutamos

    time python tournament.py 2018m.csv
    

o

    time python tournament.py 2019w.csv
    

y deberíamos obtener una salida como esta:

    real    0m0.037s
    user    0m0.028s
    sys     0m0.008s
    

aunque tus tiempos pueden variar.

Presta atención a la métrica **real**, que es el tiempo total que `tournament.py` tardó en ejecutarse. Y observa que el tiempo se muestra en minutos y segundos, con una exactitud de milésimas de segundo.

En `answers.txt`, lleva un registro de cuánto tiempo tardó `tournament.py` en simular...

*   10 (diez) torneos
*   100 (cien) torneos
*   1000 (mil) torneos
*   10000 (diez mil) torneos
*   100000 (cien mil) torneos
*   1000000 (un millón) torneos

Cada vez que ajustes `N`, registra el tiempo **real** en la tarea correspondiente en `answers.txt`, utilizando el formato `0m0.000s`. Después de medir cada escenario, responde las dos preguntas adicionales sobreescribiendo las tareas dadas:

*   ¿Cuáles predicciones, si las hay, resultaron incorrectas al aumentar el número de simulaciones?
*   Suponga que te cobran una tarifa por cada segundo de tiempo de cómputo que use tu programa. ¿Después de cuántas simulaciones llamarías a las predicciones "suficientemente buenas"?

<details><summary>Ver un archivo <code>answers.txt</code> con formato correcto</summary><div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Tiempos:

10 simulaciones: 0m0.028s
100 simulaciones: 0m0.030s
1000 simulaciones: 0m0.041s
10000 simulaciones: 0m0.139s
100000 simulaciones: 0m1.031s
1000000 simulaciones: 0m11.961s

Preguntas:

¿Cuáles predicciones, si las hay, resultaron incorrectas al aumentar el número de simulaciones?:

Con un pequeño número de simulaciones...

Supongamos que te cobran una tarifa por cada segundo de tiempo de cómputo que use tu programa.
¿Después de cuántas simulaciones llamarías a las predicciones "suficientemente buenas"?:

Parece que las predicciones se estabilizaron después de aproximadamente...

</code></pre></div></div></details>

Cómo probar tu código
----------------------

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilar y probarlo tú mismo también!

     check50 cs50/labs/2023/x/worldcup
    

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

     style50 tournament.py
    

Cómo enviar
------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

     submit50 cs50/labs/2023/x/worldcup"

