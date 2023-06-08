### Consejos

- Si desea volver a solicitar repetidamente al usuario el valor de una variable hasta que se cumpla alguna condición, es posible que desee utilizar un bucle `do... while`. Por ejemplo, recuerde el siguiente código de la conferencia, que solicita al usuario repetidamente hasta que ingresan un número entero positivo. <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">n</span><span class="p">;</span>
  <span class="k">do</span>
  <span class="p">{</span>
  <span class="n">n</span> <span class="o">=</span> <span class="n">get_int</span><span class="p">(</span><span class="s">"Entero positivo: "</span><span class="p">);</span>
  <span class="p">}</span>
  <span class="k">while</span> <span class="p">(</span><span class="n">n</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">);</span>
  </code></pre></div> </div>
  ¿Cómo podría adaptar este código para asegurar un tamaño de inicio de al menos 9 y un tamaño final de al menos el tamaño de inicio?

* Para declarar una nueva variable, asegúrese de especificar su tipo de datos, un nombre para la variable y (opcionalmente) cuál debería ser su valor inicial.
  - Por ejemplo, es posible que desee crear una variable para realizar un seguimiento de cuántos años han pasado.
* ¡Otro bucle podría ayudar a calcular cuántos años tardará la población en alcanzar el tamaño final! Dentro del bucle, probablemente desee actualizar el tamaño de la población de acuerdo con la fórmula en el Antecedente y actualizar la cantidad de años que han pasado.
* Para imprimir un entero `n` en la terminal, recuerde que puede usar una línea de código como <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code> <span class="n">printf</span><span class="p">(</span><span class="s">"El número es %i</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">n</span><span class="p">);</span>
  </code></pre></div> </div>
  para especificar que la variable `n` debe llenar el marcador de posición `%i`.

### Cómo probar su código

Su programa debe comportarse de acuerdo con estos ejemplos a continuación.

    $ ./population
    Tamaño de inicio: 1200
    Tamaño final: 1300
    Años: 1


    $ ./population
    Tamaño de inicio: -5
    Tamaño de inicio: 3
    Tamaño de inicio: 9
    Tamaño final: 5
    Tamaño final: 18
    Años: 8


    $ ./population
    Tamaño de inicio: 20
    Tamaño final: 1
    Tamaño final: 10
    Tamaño final: 100
    Años: 20


    $ ./population
    Tamaño de inicio: 100
    Tamaño final: 1000000
    Años: 115

<details><summary>¿No estás seguro de cómo resolverlo?</summary><iframe allow="acelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/2CcqQnLbGOE"></iframe></details>

Ejecute lo siguiente para evaluar la corrección de su código utilizando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50 / labs / 2023 / x / population

Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`.

    style50 population.c

## Cómo enviar

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50 / labs / 2023 / x / population