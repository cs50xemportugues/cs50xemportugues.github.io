Archivo de guía

----
Paso a seguir
-----

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

How to utilizar
---------------

Tu programa debe comportarse con ejemplos:

    $ ./recover
    Usage: ./recover IMAGE
    

donde `IMAGE` es el nombre de la imagen forense. Por ejemplo:

    $ ./recover card.raw
    

Sugerencia
----------

Ten en cuenta que puedes abrir `card.raw` de forma programática con `fopen`, como se muestra a continuación, siempre que exista `argv[1]`.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class =" kt ">FILE</span><span class =" o "> * </span><span class =" n ">file </span><span class =" o "> = </span><span class =" n ">fopen </span><span class =" p ">( </span><span class =" n ">argv </span><span class =" p ">[</span><span class =" mi ">1</span><span class =" p ">], </span><span class =" s "> "r" </span><span class =" p ">); </span>
</code></pre></div></div>

Cuando se ejecuta, tu programa debe recuperar todas las imágenes JPEG de `card.raw`, almacenando cada una como un archivo separado en el directorio de trabajo actual. Tu programa debe numerar los archivos que genera nombrando cada uno como `###.jpg`, donde `###` es un número decimal de tres dígitos a partir de `000`. Amistase con [`sprintf`](https://man.cs50.io/3/sprintf) y tenga en cuenta que `sprintf` almacena una cadena formateada en una ubicación de memoria. Dado el formato prescrito `###.jpg` para el nombre de archivo de JPEG, ¿cuántos bytes debe asignar para esa cadena? (¡No olvides el carácter NUL!)

No es necesario que intentes recuperar los nombres originales de las imágenes JPEG. Para verificar si las imágenes JPEG que produce tu programa son correctas, simplemente haz doble clic y echa un vistazo. ¡Si cada foto parece intacta, es probable que tu operación haya tenido éxito!

Lo más probable es que, sin embargo, las imágenes JPEG que genera el primer borrador de tu código no sean correctas. (Si los abres y no ves nada, ¡probablemente no son correctos!) Ejecute el comando de abajo para eliminar todos los archivos JPEG en el directorio de trabajo actual.

    $ rm *.jpg
    

Si prefieres no ser solicitado a confirmar cada eliminación, ejecuta el siguiente comando en su lugar.

    $ rm -f *.jpg
    

Solo ten cuidado con ese interruptor `-f`, ya que "forza" la eliminación sin preguntarte.

Si te gustaría crear un nuevo tipo para almacenar un byte de datos, puedes hacerlo a través del siguiente código, que define un nuevo tipo llamado `BYTE` como `uint8_t` (un tipo definido en `stdint.h`, que representa un entero sin signo de 8 bits).

    typedef uint8_t BYTE;
    

Ten en cuenta también que puedes leer datos de un archivo usando [`fread`](https://man.cs50.io/3/fread), que leerá datos de un archivo en una ubicación de memoria. Según su [página manual](https://man.cs50.io/3/fread), `fread` devuelve el número de bytes que ha leído, en cuyo caso debería devolver `512` o `0`, dado que `card.raw` contiene algún número de bloques de 512 bytes. Para leer cada bloque de `card.raw`, después de abrirlo con `fopen`, debe ser suficiente usar un bucle como este:

   
<pre class="highlight">
<span class="k">while</span> (fread(buffer, <span class ="mi">1</span>, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
{


}
</pre>
De esa manera, tan pronto como `fread` devuelva `0` (que es efectivamente `false`), tu bucle finalizará.

Pruebas
-------

Ejecute el siguiente código para evaluar la corrección de su código utilizando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50/problems/2023/x/recover
    

Ejecute el siguiente código para evaluar el estilo de su código con `style50`.


    style50 recover.c
    

Cómo enviar
-----------

En tu terminal, ejecuta el siguiente código para enviar tu tarea.

    submit50 cs50/problems/2023/x/recover"