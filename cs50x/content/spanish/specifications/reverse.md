Reverse
=======

Implemente un programa que invierta un archivo WAV, como se muestra a continuación.

    ./reverse entrada.wav salida.wav
    

Antecedentes
----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/J9iyqMwYtG4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


En la canción "Fire on High" de Electric Light Orchestra, hay algo un poco extraño en el primer minuto o así de la música. Si uno escucha con atención, suena casi como si el audio se estuviera reproduciendo hacia atrás. Resulta que, si uno reproduce la sección inicial de la canción al revés, escuchará lo siguiente:

_“The music is reversible. Time is not. Turn back, turn back!”_

¿Aterrador, verdad? Esta es una técnica llamada "backmasking", o esconder mensajes en la música que solo se pueden escuchar cuando la canción se reproduce hacia atrás. Muchos artistas han usado (o se han sospechado de usar) esta técnica en sus canciones. Para poder hacer nuestra propia investigación sobre el backmasking, ¡les hemos pedido que escriban un programa que pueda invertir archivos WAV para nosotros!

A diferencia de los archivos de audio MP3, los archivos WAV no están comprimidos. Esto hace que los archivos sean mucho más fáciles de editar y manipular, lo que es útil para la tarea en cuestión. Para aprender un poco más sobre los archivos WAV, es necesario examinar de cerca el formato de archivo WAV.

Comenzando
-----------

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de tu ventana terminal y después ejecuta `cd` por sí solo. Deberías ver que su "prompt" se asemeja a lo siguiente.

    $
    

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/4/reverse.zip
    

seguido de la tecla Enter para descargar un archivo ZIP llamado `reverse.zip` en tu espacio de trabajo. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, ni ningún otro carácter!

Ahora ejecuta

    unzip reverse.zip
    

para crear una carpeta llamada 'reverse'. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm reverse.zip
    

y responder con "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd reverse
    

seguido de Enter para moverte dentro (i.e., abrir) de ese directorio. Tu prompt debería parecerse al siguiente.

    reverse/ $
    

Si todo ha salido bien, deberías ejecutar

    ls
    

y ver un archivo llamado 'reverse.c'. Ejecutando `code reverse.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.

### El formato de archivo WAV

Se puede observar que, en la visualización siguiente, un archivo WAV se divide en tres bloques. Cada bloque tiene unos cuantos bloques de datos en su interior.

El primer bloque contiene información sobre el tipo de archivo. En particular, observa cómo el bloque "Formato de archivo" en el primer bloque deletrea 'W' 'A' 'V' 'E' en los bytes 8-11, para indicar que el archivo es un archivo WAV.

El segundo bloque contiene información sobre los datos de audio que vienen a continuación, incluyendo cuántos "canales" de audio están presentes y cuántos bits hay en cada "muestra" de audio. Los archivos de audio tienen 1 canal cuando son "monofónicos": si llevaras auriculares, escucharías el mismo audio en tu oído izquierdo y derecho. Los archivos de audio tienen 2 canales cuando son "estereofónicos": usando auriculares, escucharías un audio ligeramente diferente en tu oído izquierdo y derecho, lo que crea una sensación de amplitud. Las muestras son los fragmentos individuales de bits que conforman el audio que escuchas. Con más bits por muestra, un archivo de audio puede tener una mayor claridad (a costa de usar más memoria).

Finalmente, el tercer bloque contiene los propios datos de audio, es decir, esas muestras que mencionamos anteriormente.

Todo lo que se encuentra antes de los datos de audio se considera parte del "encabezado" WAV. Recuerda que un encabezado de archivo es simplemente algunos metadatos sobre el archivo. En este caso, el encabezado tiene una longitud de 44 bytes.

![Encabezado WAV](https://cs50.harvard.edu/x/2023/psets/4/reverse/WAV_header.png)

Una explicación más técnica de los encabezados WAV se puede encontrar [aquí](http://soundfile.sapp.org/doc/WaveFormat/), que es el recurso por el cual se inspiró esta visualización. Se ha incluido un archivo, `wav.h`, que implementa todos estos detalles para ti en una estructura llamada `WAVHEADER`.

Especificación
-------------

Escribiremos un programa llamado `reverse` que nos permita invertir un archivo WAV proporcionado por el usuario y crear un nuevo archivo WAV que contenga el audio invertido resultante. Por simplicidad, limitaremos los archivos con los que trabajamos al formato WAV. En el momento en que el usuario ejecuta el programa, debe proporcionar, mediante dos argumentos de línea de comando, el nombre del archivo de entrada que se leerá e invertirá y el nombre del archivo de salida en el que le gustaría guardar el audio resultante. Un programa ejecutado correctamente no debe producir ningún texto y debe crear un archivo WAV con el nombre especificado por el usuario que reproduzca el audio del archivo WAV de entrada invertido. Por ejemplo:

    $ ./reverse input.wav output.wav
    

En `reverse.c`, notará que se han incluido algunas bibliotecas útiles, así como un archivo de encabezado, `wav.h`. Es probable que encuentre útiles estos al implementar su programa. Hemos dejado ocho `TODO`s y dos funciones auxiliares para que las complete, y le recomendamos que las aborde del 1 al 8.

*    En el primer `TODO`, deberá asegurarse de que el programa acepte dos argumentos de línea de comando: el nombre del archivo WAV de entrada y el nombre del archivo WAV de salida. Si el programa no cumple con estas condiciones, debe imprimir un mensaje de error apropiado y devolver `1`, terminando el programa.
    <ul>
      <li data-marker="+">Pista
        <ul>
          <li data-marker="*">Recuerde que el número de argumentos de línea de comando se puede encontrar en las variables <code class ="language-plaintext highlighter-rouge">argc</code> que se pasaron a la función <code class ="language-plaintext highlighter-rouge">main</code> cuando se ejecuta el programa.</li>
          <li data-marker="*">Recuerde que <code class ="language-plaintext highlighter-rouge">argv[0]</code> contiene el nombre del programa como el primer argumento de línea de comandos.</li>
        </ul>
      </li>
    </ul>
  
*   En el segundo `TODO`, deberá abrir su archivo de entrada. Necesitaremos abrir el archivo de entrada en modo "solo de lectura", ya que solo leeremos datos del archivo de entrada. Puede ser sabio comprobar que el archivo se ha abierto correctamente. De lo contrario, debe imprimir un mensaje de error apropiado y devolver `1`, saliendo del programa. Sin embargo, deberíamos posponer la apertura del archivo de salida, no sea que creemos un nuevo archivo WAV antes de saber que el archivo de entrada es válido.
    <ul>
      <li data-marker="+">Pista
        <ul>
          <li data-marker="*">Si el primer `TODO` se ha implementado correctamente, es seguro asumir que podemos hacer referencia al nombre del archivo de entrada usando <code class ="language-plaintext highlighter-rouge">argv[1]</code>.</li>
          <li data-marker="*">Recuerde que cualquier archivo que abramos, también debemos cerrarlo cuando hayamos terminado de usarlo. Esto puede significar agregar código en otra parte del programa.</li>
        </ul>
      </li>
    </ul>

*    En el tercer `TODO`, deberá leer el encabezado del archivo de entrada. Recuerde que, en `wav.h`, ya hemos implementado una estructura que puede almacenar el encabezado de un archivo WAV. Dado que hemos escrito `#include "wav.h"` en la parte superior de `reverse.c`, también puede usar la estructura `WAVHEADER`.

*     En el cuarto `TODO`, debe completar la función `check_format`. `check_format` toma un único argumento, un `WAVHEADER` llamado `header`, que representa una estructura que contiene el encabezado del archivo de entrada. Si `header` indica que el archivo es realmente un archivo WAV, la función `check_format` debe devolver `true`. Si no es así, `check_format` debe devolver `false`. Para comprobar si un archivo es del formato WAV, podemos comparar los elementos del encabezado del archivo de entrada con aquellos que esperaríamos de un archivo WAV. Basta con mostrar que los caracteres de marcador "WAVE" se encuentran en el miembro `format` de la estructura `WAVHEADER` (consulte [Antecedentes](#antecedentes) para obtener más detalles sobre los encabezados de los archivos WAV).
    
*    En el quinto `TODO`, ahora puede abrir de forma segura el archivo de salida para la escritura. Todavía sería prudente comprobar que el archivo se ha abierto correctamente.
    <ul>
     <li data-marker="+">Pistas
       <ul>
          <li data-marker="*">Si se ha implementado correctamente el primer <code class ="language-plaintext highlighter-rouge">TODO</code>, es seguro asumir que podemos hacer referencia al nombre del archivo de salida usando <code class ="language-plaintext highlighter-rouge">argv[2]</code>.</li>
          <li data-marker="*">Recuerde que cualquier archivo que abramos, también debemos cerrarlo cuando hayamos terminado de usarlo. Esto puede significar agregar código en otra parte del programa.</li>
        </ul>
      </li>
    </ul>
    
Este puede ser un buen lugar para detenerse y verificar que su programa se comporta según lo esperado. Si se implementa correctamente, su programa debe abrir un nuevo archivo cuando se ejecuta con los argumentos de línea de comando adecuados.

Si en algún momento necesita eliminar un archivo, ejecute el siguiente comando en su directorio de trabajo actual.

    $ rm file_name.wav 
    

Si prefiere no recibir un mensaje de confirmación para cada eliminación, ejecute el siguiente comando en su lugar.

    $ rm -f file_name.wav
    

Sin embargo, tenga cuidado con ese interruptor `-f`, ya que elimina sin solicitar confirmación. 

*     A continuación, ahora que se ha verificado el tipo de archivo, el sexto `TODO` nos dice que debemos escribir el encabezado en el archivo de salida. El archivo WAV invertido seguirá teniendo la misma estructura de archivo subyacente que el archivo de entrada (mismo tamaño, número de canales, bits por muestra, etc.), por lo que es suficiente copiar el encabezado que leímos del archivo de entrada al archivo de salida.

"

*   En el séptimo `TODO`, debes implementar la función `get_block_size`. `get_block_size`, al igual que `check_format`, recibe un único argumento: se trata de un `WAVHEADER` llamado `header`, que representa la estructura que contiene el encabezado del archivo de entrada. `get_block_size` debe devolver un entero que represente el **tamaño del bloque** del archivo WAV dado, en bytes. Podemos pensar en un _bloque_ como una unidad de datos auditivos. Para audio, calculamos el tamaño de cada bloque con el siguiente cálculo: **número de canales** multiplicado por **bytes por muestra**. Afortunadamente, el encabezado contiene toda la información que necesitamos para calcular estos valores. Asegúrate de consultar la sección [Antecedentes](#background) para obtener una explicación más detallada sobre lo que significan estos valores y cómo se almacenan. Consulta también `wav.h`, para determinar qué miembros de `WAVHEADER` pueden ser útiles.
<ul>
<li data-marker="+">Indicaciones
  <ul>
    <li data-marker="*">Ten en cuenta que uno de los miembros de <code class="language-plaintext highlighter-rouge">WAVHEADER</code> es <code class="language-plaintext highlighter-rouge">bitsPerSample</code>. ¡Pero para calcular el tamaño del bloque, necesitarás **bytes** por muestra!</li>
  </ul>
</li>
</ul>

*   El octavo y último `TODO` es donde tiene lugar la reversión real del audio. Para hacer esto, debemos leer cada bloque de datos auditivos empezando por el final del archivo de entrada y moviéndonos hacia atrás, escribiendo simultáneamente cada bloque en el archivo de salida para que se escriban en orden inverso. Primero, deberíamos declarar un array para almacenar cada bloque que leamos. Entonces, depende de ti iterar a través de los datos de audio del archivo de entrada. Querrás asegurarte de leer todo el audio, ¡pero no copiar por error ninguno de los datos del encabezado! Además, a efectos de prueba, nos gustaría mantener el orden de los canales para cada bloque de audio. Por ejemplo, en un archivo WAV con dos canales (sonido estereofónico), queremos asegurarnos de que el primer canal del último bloque de audio de la entrada se convierta en el primer canal del primer bloque de audio de la salida.
<ul>
<li data-marker="+">Indicaciones
    <ul>
      <li data-marker="*">Algunas funciones (y una comprensión detallada de su uso) pueden ser especialmente útiles al completar esta sección - las páginas del manual de CS50 pueden resultar especialmente útiles aquí:
        <ul>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fread"><code class="language-plaintext highlighter-rouge">fread</code></a>: lee desde un archivo a un búfer. La salida de la función auxiliar <code class="language-plaintext highlighter-rouge">get_block_size</code> puede ser útil aquí para decidir qué valores utilizar para el tamaño y el número de datos que se leerán a la vez.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fwrite"><code class="language-plaintext highlighter-rouge">fwrite</code></a>: escribe desde un búfer a un archivo.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fseek"><code class="language-plaintext highlighter-rouge">fseek</code></a>: establece un puntero de archivo en un desplazamiento dado. Puede ser útil experimentar con valores de desplazamiento negativos para mover un puntero de archivo hacia atrás.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/ftell"><code class="language-plaintext highlighter-rouge">ftell</code></a>: devuelve la posición actual de un puntero de archivo. Puede ser útil inspeccionar qué valor devuelve <code class="language-plaintext highlighter-rouge">ftell</code> después de que se haya leído el encabezado de entrada en el tercer `TODO`, además de lo que devuelve mientras se lee el audio.</li>
        </ul>
      </li>
      <li data-marker="*">Ten en cuenta que después de usar <code class="language-plaintext highlighter-rouge">fread</code> para cargar un bloque de datos, el puntero <code class="language-plaintext highlighter-rouge">input</code> apuntará al lugar donde la lectura concluyó. En otras palabras, puede ser necesario mover el puntero <code class="language-plaintext highlighter-rouge">input</code> hacia atrás **dos** tamaños de bloque después de cada <code class="language-plaintext highlighter-rouge">fread</code>, uno para volver al lugar donde comenzó el <code class="language-plaintext highlighter-rouge">fread</code>, y el segundo para pasar al bloque anterior no leído.</li>
    </ul>
</li>
</ul>

*   ¡Por último, asegúrate de cerrar todos los archivos que hayas abierto!

Uso
---

A continuación se presentan algunos ejemplos de cómo debería funcionar el programa. Por ejemplo, si el usuario omite uno de los argumentos de la línea de comandos:

    $ ./reverse input.wav
    Uso: ./reverse input.wav output.wav
    

O si el usuario omite ambos argumentos de la línea de comandos:

    $ ./reverse
    Uso: ./reverse input.wav output.wav
    

Así es como debería funcionar el programa si el usuario proporciona un archivo de entrada que no es un archivo WAV real:

    $ ./reverse image.jpg output.wav
    El archivo de entrada no es un archivo WAV.
    

Se asume que el usuario ingresa un nombre de archivo de salida válido, como `output.wav`.

Un programa ejecutado con éxito no debe producir texto y debe crear un archivo WAV con el nombre especificado por el usuario que reproduzca el audio del archivo WAV de entrada al revés. Por ejemplo:

    $ ./reverse input.wav output.wav
    

Pruebas
-------

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilar y probarlo usted mismo también!

    check50 cs50/problems/2023/x/reverse
    

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 reverse.c
    

Cómo enviar
-----------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/reverse

