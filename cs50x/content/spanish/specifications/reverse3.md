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