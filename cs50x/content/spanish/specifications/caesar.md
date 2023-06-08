# Cifrado César

Para este problema, implementarás un programa que cifra mensajes usando el cifrado César, tal como se muestra a continuación.

    $ ./caesar 13
    texto plano: HELLO
    texto cifrado: URYYB

## Empezando

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de la ventana de tu terminal, luego ejecuta `cd` por sí solo. Deberías ver que la "terminal" se parece al siguiente ejemplo.

    $

Haz clic dentro de la ventana de la terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/caesar.zip

seguido de Enter para descargar un archivo ZIP llamado `caesar.zip` en tu espacio de códigos. ¡Asegúrate de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter que pueda haber!

Ahora ejecuta

    unzip caesar.zip

para crear una carpeta llamada `caesar`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm caesar.zip

y responde con "y" seguido de Enter para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd caesar

seguido de Enter para entrar (i.e., abrir) en ese directorio. Tu terminal debería tener el siguiente aspecto:

    caesar/ $

Si todo fue exitoso, ejecuta

    ls

y verás un archivo llamado `caesar.c`. Ejecutar `code caesar.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no es así, vuelve a seguir tus pasos y ve si puedes determinar en qué punto te equivocaste.

## Antecedentes

Supuestamente, César (sí, ese César) solía "encriptar" (es decir, ocultar de manera reversible) mensajes confidenciales desplazando cada letra del mensaje un cierto número de lugares. Por ejemplo, podría escribir A como B, B como C, C como D, ..., y, se envuelve alfabéticamente, Z como A. Por lo tanto, para decirle HOLA a alguien, César podría escribir IFMMP en su lugar. Al recibir esos mensajes, los destinatarios tendrían que "descifrarlos" desplazando las letras en dirección opuesta por el mismo número de lugares.


La seguridad de este "criptosistema" dependía de que solo César y los destinatarios conocieran un secreto, el número de lugares por los que César había desplazado sus letras (por ejemplo, 1). No es particularmente seguro según los estándares modernos, pero si eres posiblemente el primero en hacerlo en el mundo, ¡bastante seguro!


El texto sin encriptar se llama comúnmente _plaintext_. El texto encriptado se llama comúnmente _ciphertext_. Y el secreto utilizado se llama _key_.


Entonces, para ser claro, así es como se hace una encriptación de `HELLO` con una clave de `1`:

<table>
  <thead>
    <tr>
      <th>plaintext</th>
      <th><code class="language-plaintext highlighter-rouge">H</code></th>
      <th><code class="language-plaintext highlighter-rouge">E</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">O</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+ clave</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>= ciphertext</td>
      <td><code class="language-plaintext highlighter-rouge">I</code></td>
      <td><code class="language-plaintext highlighter-rouge">F</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">P</code></td>
    </tr>
  </tbody>
</table>


De manera más formal, el algoritmo (es decir, cifrado) de César encripta los mensajes "rotando" cada letra por `k` posiciones. Formalmente, si `p` es un determinado _plaintext_ (es decir, un mensaje sin encriptar), <code>p<sub>i</sub></code> es el  <code>i<sup>th</sup></code> carácter en `p`, y `k` es una clave secreta (es decir, un número entero no negativo), entonces cada letra,  <code>c<sub>i</sub></code>, en el _ciphertext_ `c`, se calcula como


<code>c<sub>i</sub> = (p<sub>i</sub> + k) % 26</code>


donde el "% 26" aquí significa "resto de la división".

Incluso, para hablarlo como discusión, piense en A (o a) como `0`, B (o b) como `1`, ..., H (o h) como `7`, I (o i) como `8`, ..., y Z (o z) como `25`. Supongamos que César solo desea decir `Hola` a alguien de manera confidencial, usando, esta vez, una clave `k` de 3. Y así, su _plaintext_, `p`, es `Hola`, en cuyo caso el primer carácter de su _plaintext_, <code>p<sub>0</sub></code>, es `H`, y el segundo carácter de su _plaintext_,<code>p<sub>1</sub></code>, es `i`. El primer carácter de su _ciphertext_, <code>c<sub>0</sub></code>, es por lo tanto  `K`, y el segundo carácter de su _ciphertext_, <code>c<sub>i</sub></code>, es por lo tanto `L`.

Escribamos un programa llamado `caesar` que te permita encriptar mensajes usando el cifrado de César. En el momento en que el usuario ejecute el programa, deberían decidir, proporcionando un argumento de línea de comandos, cuál debería ser la clave en el mensaje secreto que proporcionarán en tiempo de ejecución. No deberíamos asumir necesariamente que la clave del usuario va a ser un número; aunque puede asumir que, si es un número, será un entero positivo.

Aquí hay algunos ejemplos de cómo podría funcionar el programa. Por ejemplo, si el usuario introduce una clave de `1` y un _plaintext_ de `HELLO`:


    $ ./caesar 1
    plaintext:  HELLO
    ciphertext: IFMMP


Aquí es cómo podría funcionar el programa si el usuario proporciona una clave de `13` y un _plaintext_ de `hola, mundo`:

    $ ./caesar 13
    plaintext:  hello, world
    ciphertext: uryyb, jbeyq

Observe que ni la coma ni el espacio fueron "desplazados" por el cifrado. ¡Solo se rotan caracteres alfabéticos!

¿Cómo quedará si el usuario proporciona una clave de `13` otra vez, pero con un _plaintext_ más complejo?:

    $ ./caesar 13
    plaintext:  be sure to drink your Ovaltine 
    ciphertext: or fher gb qevax lbhe Binygvar
    
<details><summary>¿Por qué?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9K4FsAHB-C8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

Observe que la mayúscula y la minúscula del mensaje original se han conservado. Las letras minúsculas permanecen minúsculas y las letras mayúsculas permanecen mayúsculas.


Y si el usuario no coopera, proporcionando un argumento de línea de comandos que no es un número, el programa debe recordarle al usuario cómo usar el programa:

    $ ./caesar HELLO
    Usage: ./caesar key

¿Qué sucede si el usuario no coopera realmente, no proporcionando un argumento de línea de comandos en absoluto? El programa debe recordarle al usuario cómo usar el programa:

    $ ./caesar
    Usage: ./caesar key

O no coopera realmente, proporcionando más de un argumento de línea de comandos? El programa debe recordarle al usuario cómo usar el programa:

    $ ./caesar 1 2 3
    Usage: ./caesar key


<details><summary>Ver una grabación</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script></details>

## Especificación

Diseña e implementa un programa, `caesar`, que cifre mensajes usando el cifrado de César.

- Implementa tu programa en un archivo llamado `caesar.c` dentro de un directorio llamado `caesar`.
- Tu programa debe aceptar un solo argumento de línea de comandos, un número entero no negativo. Llamémosle `k` por conveniencia.
- Si tu programa se ejecuta sin argumentos de línea de comandos o con más de un argumento de línea de comandos, tu programa debe imprimir un mensaje de error de tu elección (con `printf`) y salir de `main` devolviendo un valor de `1` (que indica un error) inmediatamente.
- Si alguno de los caracteres del argumento de línea de comandos no es un dígito decimal, tu programa debe imprimir el mensaje `Uso: ./caesar key` y salir de `main` devolviendo un valor de `1`.
- No asumas que `k` será menor o igual que 26. Tu programa debe funcionar para todos los valores enteros no negativos de `k` menores que <code>2<sup>31</sup> - 26</code>. En otras palabras, no es necesario que te preocupes si tu programa eventualmente falla si el usuario elige un valor para `k` que sea demasiado grande o casi demasiado grande para caber en un `int`. (Recuerda que un `int` puede desbordarse.) Pero incluso si `k` es mayor que `26`, los caracteres alfabéticos de la entrada de tu programa deben seguir siendo caracteres alfabéticos en la salida de tu programa. Por ejemplo, si `k` es `27`, `A` no debe convertirse en `\` aunque `\` esté a `27` posiciones de `A` en ASCII, según [asciitable.com](https://www.asciitable.com/); `A` debe convertirse en `B`, ya que `B` está a `27` posiciones de `A`, siempre y cuando se haga la vuelta a `Z` a `A`.
- Tu programa debe imprimir `plaintext:` (con dos espacios pero sin un salto de línea) y luego solicitar al usuario una `cadena` de texto sin formato (utilizando `get_string`).
- Tu programa debe imprimir `ciphertext:` (con un espacio pero sin un salto de línea) seguido del cifrado correspondiente de la cadena sin formato, con cada carácter alfabético de la cadena sin formato "rotado" por _k_ posiciones; los caracteres no alfabéticos deben imprimirse sin cambios.
- Tu programa debe preservar el uso del mayúsculas: las letras mayúsculas, aunque rotadas, deben seguir siendo letras mayúsculas; las letras minúsculas, aunque rotadas, deben seguir siendo letras minúsculas.
- Después de imprimir el cifrado, debes imprimir un salto de línea. Tu programa debe salir devolviendo `0` de `main`.

## Consejos

¿Cómo empezar? Abordemos este problema paso a paso.

### Pseudocódigo

Primero, intenta escribir una función `main` en `caesar.c` que implemente el programa utilizando solo pseudocódigo, incluso si no estás (¡todavía!) seguro de cómo escribirlo en código real.

<details><summary>Pista</summary><p>Hay más de una manera de hacer esto, aquí hay solo una!</p>

    int main(void)
    {
        // Asegúrate de que el programa se haya ejecutado con un solo argumento de línea de comandos

        // Asegúrate de que cada carácter en argv[1] sea un dígito

        // Convierte argv[1] de una `cadena` a un `int`

        // Solicita al usuario el texto en claro

        // Para cada carácter en el texto plano:

            // Rota el carácter si es una letra
    }

<p>Está bien editar tu propio pseudocódigo después de ver el nuestro aquí, ¡pero no copies y pegues el nuestro en el tuyo!</p></details>

### Contando los argumentos de línea de comandos

Sea cual sea el pseudocódigo, primero escribamos solo el código C que verifica si el programa se ejecutó con un solo argumento de línea de comandos antes de agregar funcionalidades adicionales.

Específicamente, modifique `main` en `caesar.c` de tal manera que, si el usuario no proporciona argumentos de línea de comandos, o dos o más, la función imprime `"Usage: ./caesar key\n"` y luego devuelve `1`, lo que significa que el programa ha terminado de ejecutarse. Si el usuario proporciona exactamente un argumento de línea de comandos, el programa no debería imprimir nada y simplemente regresar `0`. El programa debería comportarse así:

    $ ./caesar
    Usage: ./caesar key


    $ ./caesar 1 2 3
    Usage: ./caesar key


    $ ./caesar 1

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerde que puede imprimir con <code class="language-plaintext highlighter-rouge">printf</code>.</li>
  <li data-marker="*">Recuerde que una función puede devolver un valor con <code class="language-plaintext highlighter-rouge">return</code>.</li>
  <li data-marker="*">Recuerde que <code class="language-plaintext highlighter-rouge">argc</code> contiene la cantidad de argumentos de línea de comandos que se le pasaron a un programa, más el propio nombre del programa.</li>
</ul></details>

### Verificando la Key

Ahora que su programa está aceptando la entrada según lo prescrito, es hora de dar otro paso.

Agregue a `caesar.c', debajo de `main`, una función llamada, p. ej., `only_digits` que toma un `string` como argumento y devuelve `true` si ese `string` contiene solo dígitos, del `0` al `9`, de lo contrario devuelve `false`. Asegúrese de agregar el prototipo de la función sobre `main` también.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Probablemente necesitará un prototipo parecido a:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">only_digits</span><span class="p">(</span><span class="n">string</span> <span class="n">s</span><span class="p">);</span>
</code></pre></div>    </div>
     <p>Y asegúrese de incluir <code class="language-plaintext highlighter-rouge">cs50.h</code> en la parte superior de su archivo, para que el compilador reconozca<span class="language-plaintext highlighter-rouge">string</span> (y <code class="language-plaintext highlighter-rouge">bool</code>).</p>
  </li>
  <li data-marker="*">Recuerde que un <code class="language-plaintext highlighter-rouge">string</code> es solo una matriz de <code class="language-plaintext highlighter-rouge">char</code>s.</li>
  <li data-marker="*">Recuerde que <code class="language-plaintext highlighter-rouge">strlen</code>, declarado en <code class="language-plaintext highlighter-rouge">string.h</code>, calcula la longitud de un <code class="language-plaintext highlighter-rouge">string</code>.</li>
  <li data-marker="*">Puede encontrar útil <code class="language-plaintext highlighter-rouge">isdigit</code>, declarado en <code class="language-plaintext highlighter-rouge">ctype.h</code>, según <a href="https://manual.cs50.io/">manual.cs50.io</a>. ¡Pero tenga en cuenta que solo verifica un <code class="language-plaintext highlighter-rouge">char</code> a la vez!</li>
</ul></details>


Luego, modifique `main` de tal manera que llame a `only_digits` en `argv [1]`. Si esa función devuelve `false`, entonces `main` debe imprimir `"Usage: ./caesar key\n"` y devolver `1`. De lo contrario, `main` debe simplemente devolver `0`. El programa debería comportarse así:

```
$ ./caesar 42
```
```
$ ./caesar banana
Usage: ./caesar key
```

### Usando la Clave

Modifica ahora la función `main` de tal manera que convierta `argv[1]` en un `int`. Puedes encontrar la función `atoi`, declarada en `stdlib.h`, útil para esto, según [manual.cs50.io](https://manual.cs50.io/). Luego, usa `get_string` para preguntarle al usuario por algún texto plano con `"plaintext: "`.

Luego, implementa una función llamada, por ejemplo, `rotate`, que tome un `char` como entrada y un `int`, y gire ese `char` por esa cantidad de posiciones si es una letra (es decir, alfabética), envolviéndose de `Z` a `A` (y de `z` a `a`) según sea necesario. Si el `char` no es una letra, la función en su lugar debería devolver el mismo `char` sin cambios.


<details><summary>Sugerencias</summary><ul>
  <li data-marker="*">Probablemente quieras un prototipo como el siguiente:
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">char</span> <span class="nf">rotate</span><span class="p">(</span><span class="kt">char</span> <span class="n">c</span><span class="p">,</span> <span class="kt">int</span> <span class="n">n</span><span class="p">);</span>
</code></pre></div>    </div>
    <p>Una llamada a la función como</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'A'</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>o incluso</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>rotate('A', 27)
</code></pre></div>    </div>
    <p>debe devolver <code class="language-plaintext highlighter-rouge">'B'</code>. Y una llamada a la función como</p>
    <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">rotate</span><span class="p">(</span><span class="sc">'!'</span><span class="p">,</span> <span class="mi">13</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>debe devolver <code class="language-plaintext highlighter-rouge">'!'</code>.</p>
  </li>
  <li data-marker="*">Recuerda que puedes convertir explícitamente un `char` en un `int` con `(char)`, y un `int` en un `char` con `(int)`. O puedes hacerlo implícitamente tratando uno como el otro.</li>
  <li data-marker="*">Probablemente quieras restar el valor ASCII de <code class="language-plaintext highlighter-rouge">'A'</code> de cualquier letra mayúscula, para tratar <code class="language-plaintext highlighter-rouge">'A'</code> como <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">'B'</code> como <code class="language-plaintext highlighter-rouge">1</code>, y así sucesivamente, mientras realizas aritmética. Y luego añadirlo cuando termines con lo mismo.</li>
  <li data-marker="*">Probablemente quieras restar el valor ASCII de <code class="language-plaintext highlighter-rouge">'a'</code> de cualquier letra minúscula, para tratar <code class="language-plaintext highlighter-rouge">'a'</code> como <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">'b'</code> como <code class="language-plaintext highlighter-rouge">1</code>, y así sucesivamente, mientras realizas aritmética. Y luego añadirlo cuando termines con lo mismo.</li>
  <li data-marker="*">Podrías encontrar útiles algunas otras funciones declaradas en <code class="language-plaintext highlighter-rouge">ctype.h</code>, según [manual.cs50.io](https://manual.cs50.io/).</li>
  <li data-marker="*">Probablemente te resulte útil el operador `%` al hacer aritmética "envolvente" desde un valor como `25` a `0`.</li>
</ul></details>

Luego, modifica `main` de tal manera que imprima `"ciphertext: "` y luego itere sobre cada `char` en el texto plano del usuario, llamando a `rotate` en cada uno, e imprimiendo el valor de retorno de ésta.

<details><summary>Sugerencias</summary><ul>
  <li data-marker="*">Recuerda que `printf` puede imprimir un `char` usando `%c`.</li>
  <li data-marker="*">Si no ves ninguna salida cuando llamas a `printf`, puede ser porque estás imprimiendo caracteres fuera del rango ASCII válido de 0 a 127. ¡Intenta imprimir caracteres temporales como números (usando `%i` en lugar de `%c`) para ver qué valores estás imprimiendo!</li>
</ul></details>

## Descripción detallada

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/V2uusmv2wxI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo probar tu código

Ejecuta el siguiente comando para evaluar la corrección de tu código utilizando `check50`. ¡Pero asegúrate de compilar y probarlo por tu cuenta también!

    check50 cs50/problems/2023/x/caesar

Ejecuta el siguiente comando para evaluar el estilo de tu código utilizando `style50`.

    style50 caesar.c

## Cómo enviar tu trabajo

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2023/x/caesar

