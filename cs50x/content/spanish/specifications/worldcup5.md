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