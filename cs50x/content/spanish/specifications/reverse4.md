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