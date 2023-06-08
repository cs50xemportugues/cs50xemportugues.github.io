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