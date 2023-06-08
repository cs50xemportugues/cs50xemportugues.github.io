Laboratorio 4: Smiley
=============

Objetivos de aprendizaje
--------------

*   Aprender a trabajar con imágenes.
*   Practicar la manipulación de píxeles.

Antecedentes
----------

![Smiley](https://cs50.harvard.edu/x/2023/labs/4/smiley/smiley_spec_image.png)

En clase, viste un poco sobre cómo se almacenan las imágenes en una computadora. En este laboratorio, practicarás trabajando con un archivo BMP, en realidad la cara sonriente que se muestra aquí, y cambiarás todos los píxeles negros a un color de tu elección.

Sin embargo, la cara sonriente con la que trabajarás no está hecha solo de 0 y 1, o píxeles en blanco y negro, sino que consta de 24 bits por píxel. Usa ocho bits para representar los valores de rojo, ocho bits para verde y ocho bits para azul. Como cada color utiliza ocho bits o un byte, podemos usar un número en el rango de 0 a 255 para representar su valor de color. En hexadecimal, esto se representa por `0x00` a `0xff`. Mezclando estos valores de rojo, verde y azul, podemos crear millones de colores posibles.

Si miras el archivo `bmp.h`, uno de los archivos auxiliares en el código de distribución, verás cómo cada `RGB triple` se representa por una `struct` como:

    typedef struct
    {
        BYTE rgbtBlue;
        BYTE rgbtGreen;
        BYTE rgbtRed;
    }
    RGBTRIPLE;
    

donde `BYTE` está definido como un entero de 8 bits.

Notarás varios archivos provistos en el código de distribución para manejar la lectura y escritura de un archivo de imagen, así como el manejo de los metadatos o "encabezados" de la imagen. Completarás la función `colorize` en `helpers.c`, que ya tiene como parámetros de entrada la altura de la imagen, el ancho y una matriz bidimensional de `RGBTRIPLE` que crean la imagen en sí misma.

*   Consejos
    *   Si guardamos el primer píxel como `RGBTRIPLE pixel = image[0][0]`, luego podemos acceder a cada uno de los colores individuales de `pixel` como `pixel.rgbtBlue`, `pixel.rgbtGreen` y `pixel.rgbtRed`.

Demo
----

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-vSNSSp3y9K4fvpMUghBaX2sl4" src="https://asciinema.org/a/vSNSSp3y9K4fvpMUghBaX2sl4.js"></script>

Para empezar
---------------

Abre [VS Code](https://code.cs50.io/).

Haz clic dentro de tu ventana de terminal y luego ejecuta `cd` por sí solo. Deberías encontrar que su "prompt" se parece al siguiente.

    $
    

Haz clic dentro de esa ventana de la terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/labs/4/smiley.zip
    

seguido de Enter para descargar un archivo ZIP llamado `smiley.zip` en tu espacio de códigos. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter!

Ahora ejecuta

    unzip smiley.zip
    

para crear una carpeta llamada `smiley`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm smiley.zip
    

y responde con "y" seguido de Enter en la indicación para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd smiley
    

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu prompt debería parecerse al siguiente.

    smiley/ $
    

Si todo ha sido exitoso, debes ejecutar

    ls
    

y deberías ver `bmp.h`, `colorize.c`, `helpers.c`, `helpers.h`, `Makefile` y `smiley.bmp`.

¡Si tienes algún problema, sigue estos mismos pasos de nuevo y ve si puedes determinar dónde te equivocaste!

Detalles de implementación
----------------------

Abre `helpers.c` y observa que la función `colorize` está incompleta. Ten en cuenta que la altura de la imagen, su ancho y una matriz bidimensional de píxeles se configuran como parámetros de entrada para esta función. Debes implementar esta función para cambiar todos los píxeles negros en la imagen a un color de su elección.

Puedes compilar tu código simplemente escribiendo `make` en el prompt `$`.

Luego ejecutas el programa escribiendo:

    ./colorize smiley.bmp outfile.bmp
    

donde `outfile.bmp` es el nombre del nuevo BMP que estás creando.

Pregunta reflexiva
----------------

*   ¿Cómo crees que representarías un pixel negro al usar un archivo BMP de 24 bits de color?
*   ¿Es lo mismo o diferente al mezclar pinturas para representar varios colores?

Cómo probar tu código
---------------------

Tu programa debe comportarse según los ejemplos a continuación.

    smiley/ $ ./colorize smiley.bmp smiley_out.bmp
    

Cuando tu programa esté funcionando correctamente, deberías ver un nuevo archivo, `smiley_out.bmp`, en tu directorio `smiley`. Ábrelo y ve si los píxeles negros ahora son del color que especificaste.

Puedes verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes, escribiendo lo siguiente en el prompt `$`. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/labs/2023/x/smiley
    

Para evaluar que el estilo de tu código (indentaciones y espacios) sea correcto, escribe lo siguiente en el prompt `$`.

    style50 helpers.c
    
"

Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/labs/2023/x/smiley
    

<details><summary>¿Quieres ver la solución del personal?</summary><div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include</span> <span class="cpf">"helpers.h"</span><span class="cp">
</span>
<span class="kt">void</span> <span class="nf">colorize</span><span class="p">(</span><span class="kt">int</span> <span class="n">height</span><span class="p">,</span> <span class="kt">int</span> <span class="n">width</span><span class="p">,</span> <span class="n">RGBTRIPLE</span> <span class="n">image</span><span class="p">[</span><span class="n">height</span><span class="p">][</span><span class="n">width</span><span class="p">])</span>
<span class="p">{</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">height</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span>
    <span class="p">{</span>
        <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">width</span><span class="p">;</span> <span class="n">j</span><span class="o">++</span><span class="p">)</span>
        <span class="p">{</span>
            <span class="c1">// Hacer que los píxeles negros se conviertan en rojos</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtRed</span> <span class="o">==</span> <span class="mh">0x00</span> <span class="o">&amp;&amp;</span> <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtGreen</span> <span class="o">==</span> <span class="mh">0x00</span> <span class="o">&amp;&amp;</span> <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtBlue</span> <span class="o">==</span> <span class="mh">0x00</span><span class="p">)</span>
            <span class="p">{</span>
                <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtRed</span> <span class="o">=</span> <span class="mh">0xff</span><span class="p">;</span>
            <span class="p">}</span>
        <span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>
</code></pre></div></div></details>

