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