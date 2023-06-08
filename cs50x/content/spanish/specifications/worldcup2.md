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