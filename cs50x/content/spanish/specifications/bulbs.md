Bombillas
=====

Bombillas Que No Están Tan Rotas
-------------------------

En la clase, es posible que hayas notado lo que parecía un "error" en la parte delantera del escenario, donde algunas de las bombillas siempre parecen estar apagadas:

![captura de pantalla de la clase de la semana 2 con una fila de bombillas](https://cs50.harvard.edu/x/2023/psets/2/bulbs/binary_bulbs.jpg)

Cada secuencia de bombillas, sin embargo, codifica un mensaje en _binario_, el lenguaje que hablan las computadoras. ¡Vamos a escribir un programa para hacer mensajes secretos propios, quizás que incluso podamos poner en el escenario!

Comenzando
---------------

Abre [VS Code] (https://code.cs50.io/).

Comienza haciendo clic dentro de tu ventana de terminal y luego ejecuta `cd` por sí solo. Deberías encontrar que su "indicación" se parece a la siguiente.

    $ 
    

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/bulbs.zip
    

seguido de Enter para descargar un archivo ZIP llamado `bulbs.zip` en tu espacio de códigos. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter de ese tipo!

Ahora, ejecuta

    unzip bulbs.zip
    

para crear una carpeta llamada `bulbs`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm bulbs.zip
    

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd bulbs
    

seguido de Enter para entrar en (es decir, abrir) ese directorio. Tu indicación debería verse así.

    bulbs/ $ 
    

Si todo fue exitoso, deberías ejecutar

    ls
    

y ver un archivo llamado `bulbs.c`. Ejecutar `code bulbs.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.

Detalles de Implementación
--------------------------

Para escribir nuestro programa, primero tenemos que pensar en las **bases**.

### Los fundamentos

La base más simple es la base-1 o _unaria_; para escribir un número, _N_, en base-1, simplemente escribimos _N_ cantidad de `1`s consecutivas. Por lo tanto, el número `4` en base-1 se escribiría como `1111`, y el número `12` como`111111111111`. Piensa en ello como contar en tus dedos o marcar un puntaje con marcas en una pizarra.

Puede entender por qué la base-1 no se usa mucho en la actualidad. (¡Los números se vuelven bastante largos!) En su lugar, una convención común es la base-10 o _decimal_. En base-10, cada _dígito_ se multiplica por alguna potencia de 10, para representar números más grandes. Por ejemplo, `123` es una forma corta de escribir <code>123 = 1 • 10<sup>2</sup> + 2 • 10<sup>1</sup> + 3 • 10<sup>0</sup></code>.

Cambiar de base es tan simple como cambiar el `10` de arriba por un número diferente. Por ejemplo, si escribieras `123` en base-4, el número que realmente estarías escribiendo es <code>123 = 1 • 4<sup>2</sup> + 2 • 4<sup>1</sup> + 3 • 4<sup>0</sup></code>, que es igual al número decimal `27`.

Los ordenadores, por otro lado, usan la base-2 o _binario_. En binario, escribir `123` sería un error, ya que los números binarios solo pueden tener `0`s y `1`s. Pero el proceso de descubrir exactamente qué número decimal representa un número binario es exactamente el mismo. Por ejemplo, el número `10101` en base-2 representa <code>1 • 2<sup>4</sup> + 0 • 2<sup>3</sup> + 1 • 2<sup>2</sup> + 0 • 2<sup>1</sup> + 1 • 2<sup>0</sup></code>, que es igual al número decimal `21`.

### Codificando un Mensaje

Las bombillas solo pueden estar encendidas o apagadas. En otras palabras, las bombillas representan dos estados posibles; o la bombilla está encendida, o la bombilla está apagada, así como los números binarios son 1 o 0. Tendremos que encontrar una forma de codificar texto como una secuencia de números binarios.

Escribamos un programa llamado `bulbs` que tome un mensaje y lo convierta en un conjunto de bombillas que podríamos mostrar a una audiencia desprevenida. Lo haremos en dos pasos:

*   El primer paso consiste en convertir el texto en números decimales. Digamos que queremos codificar el mensaje `HI!`. Por suerte, ya tenemos una convención en su lugar sobre cómo hacer esto, [ASCII](https://asciichart.com/). Observe que `H` se representa por el número decimal `72`, `I` por `73` y `!` por `33`.
*   El siguiente paso implica tomar nuestros números decimales (como `72`, `73` y `33`) y convertirlos en números binarios equivalentes que solo usan 0s y 1s. Para tener una cantidad consistente de bits en cada uno de nuestros números binarios, asumamos que cada número decimal se representa con 8 bits. `72` es `01001000`, `73` es `01001001` y `33` es `00100001`.

Por último, interpretaremos estos números binarios como instrucciones para las bombillas en el escenario; 0 está apagado, 1 está encendido. (En el archivo `bulbs.c` se incluye una función `print_bulb` que se ha implementado para ti, que toma un `0` o `1` y emite un emoji que representa bombillas.)

Aquí hay un ejemplo de cómo podría funcionar el programa completo. A diferencia del escenario de Sanders, imprimiremos un byte por línea para mayor claridad.

    # ./bulbs
    Mensaje: HI!
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫🟡
    

Para verificar nuestro trabajo, podemos leer una bombilla que está encendida (🟡) como un `1` y una bombilla que está apagada (⚫) como un `0`. Entonces `HI!` se convirtió en

    01001000
    01001001
    00100001
    

que es precisamente lo que esperaríamos.

Otro ejemplo:

    # ./bulbs
    Mensaje: HI MOM
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫⚫
    ⚫🟡⚫⚫🟡🟡⚫🟡
    ⚫🟡⚫⚫🟡🟡🟡🟡
    ⚫🟡⚫⚫🟡🟡⚫🟡
    

Observe que se incluyen todos los caracteres en las instrucciones de las bombillas, incluidos los caracteres no alfabéticos como los espacios (`00100000`).

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

Cómo probar tu código
---------------------

Tu programa debería comportarse de acuerdo con los ejemplos anteriores. Puedes comprobar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes, escribiendo lo siguiente en el símbolo `$`. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2023/x/bulbs
    

Para evaluar el estilo de tu código, escribe lo siguiente en el símbolo `$`.

    style50 bulbs.c
    

Cómo enviar
-------------

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2023/x/bulbs"

