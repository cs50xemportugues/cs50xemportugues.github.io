Especificación
-------------

Diseñe e implemente un programa llamado `bulbs` que convierta texto en instrucciones para la tira de bombillas del escenario de CS50 de la siguiente manera:

*   Implemente su programa en un archivo llamado `bulbs.c`.
*   Su programa primero debe solicitar al usuario un mensaje utilizando `get_string`.
*   Luego, su programa debe convertir la `cadena` dada en una serie de números binarios de 8 bits, uno para cada carácter de la cadena.
*   Puede utilizar la función `print_bulb` proporcionada para imprimir una serie de `0`s y `1`s como una serie de emoji amarillos y negros, que representan bombillas encendidas y apagadas.
*   Cada "byte" de 8 símbolos debe imprimirse en su propia línea cuando se emita una salida; también debe haber un `\n` después del último "byte" de 8 símbolos.

<details><summary>Sugerencias para la conversión de Decimal a Binario</summary><p> Veamos un ejemplo con el número 4. ¿Cómo convertiría 4 a binario? Comience por considerar el bit más a la derecha, ese que, si está activado, agrega 1 al número que estamos representando. ¿Es necesario que esté activado este bit? Divida 4 por 2 para averiguar:</p>

`4 / 2 = 2`

<p>2 se divide uniformemente en 4, lo que nos indica que no hay un resto de 1 en qué preocuparse. Podemos dejar de lado este bit de la derecha con seguridad, entonces:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>0
</code></pre></div></div>

<p>¿Qué pasa con el bit anterior, ahora, el que se encuentra justo a la izquierda de este bit que descubrimos? Para comprobarlo, sigamos un proceso similar, pero comencemos donde lo dejamos. En el paso anterior, dividimos 4 por 2 y obtuvimos 2 ¿Ahora, se divide 2 uniformemente en 2? Sí, lo hace, por lo que no hay resto de 2 en qué preocuparse:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>00
</code></pre></div></div>

<p>Continuemos aún más. Después de dividir 2 por 2, quedamos con 1. Dividir 1 entre 2 deja un resto de 1. Eso significa que tendremos que encender este bit:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>100
</code></pre></div></div>

<p> Y ahora que hemos dividido nuestro número a 0, no necesitamos más bits para representarlo. Observe que descubrimos los bits para representar 4 en el orden opuesto al que necesitamos imprimirlos: es probable que necesitemos una estructura que nos permita almacenar estos bits, para que podamos imprimirlos hacia adelante más tarde. Y, por supuesto, en su código real, estará trabajando con `char`s de 8 bits, por lo que deberá agregar los 0 necesarios en caso de ser necesario. </p>

<p> ¡Al comprobar los restos, el operador módulo (<code class="language-plaintext highlighter-rouge">%</code>) puede ser útil! <code class="language-plaintext highlighter-rouge">4 % 2</code>, por ejemplo, devuelve 0, lo que significa que 2 se divide en 4 con un resto de 0.</p></details>