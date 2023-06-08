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