Laboratorio 4: Volumen
=============


<div class="alert" data-alert="warning" role="alert"><p>Puedes colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante de dicho grupo contribuya por igual</p></div>

Escribe un programa para modificar el volumen de un archivo de audio.

    $ ./volumen INPUT.wav OUTPUT.wav 2.0
    

Donde `INPUT.wav` es el nombre del archivo de audio original y `OUTPUT.wav` es el nombre del archivo de audio cuyo volumen ha sido escalado por el factor dado (por ejemplo, 2.0).

Archivos WAV
---------

[Archivos WAV](https://docs.fileformat.com/audio/wav/) son un formato de archivo común para representar audio. Los archivos WAV almacenan el audio como una secuencia de "muestras": números que representan el valor de algún señal de audio en un momento determinado. Los archivos WAV comienzan con una "cabecera" de 44 bytes que contiene información sobre el archivo en sí, incluyendo el tamaño del archivo, el número de muestras por segundo y el tamaño de cada muestra. Después de la cabecera, el archivo WAV contiene una secuencia de muestras, cada una es un número entero de 16 bits (2 bytes) que representa la señal de audio en un momento específico.

Escalar cada valor de muestra por un factor dado tiene el efecto de cambiar el volumen del audio. Multiplicar cada valor de muestra por 2.0, por ejemplo, tendrá el efecto de duplicar el volumen del audio original. Por otro lado, la multiplicación de cada muestra por 0.5 tendrá el efecto de reducir el volumen a la mitad.

Tipos
-----

Hasta ahora, hemos visto varios tipos en C, incluyendo `int`, `bool`, `char`, `double`, `float` y `long`. Dentro de un archivo de encabezado llamado `stdint.h` hay declaraciones de varios otros tipos que nos permiten definir con precisión el tamaño (en bits) y el signo (firmado o no) de un entero. Dos tipos en particular nos serán útiles en este laboratorio.

*   `uint8_t` es un tipo que almacena un entero sin signo de 8 bits (es decir, no negativo). Podemos tratar cada byte de la cabecera de un archivo WAV como un valor `uint8_t`.
*   `int16_t` es un tipo que almacena un entero de 16 bits con signo (es decir, positivo o negativo). Podemos tratar cada muestra de audio en un archivo WAV como un valor `int16_t`.

Comencemos
---------------

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de la ventana de tu terminal y luego ejecuta `cd`. Debe aparecer lo siguiente:

    $
    

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/labs/4/volume.zip
    

seguido de Enter para descargar un archivo ZIP llamado `volume.zip` en tu espacio de código. ¡Asegúrate de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter!

Ahora ejecuta

    unzip volume.zip
    

para crear una carpeta llamada `volume`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm volume.zip
    

y responde "y" seguido de Enter en el prompt para eliminar el archivo ZIP que acabas de descargar.

Ahora escribe

    cd volume
    

seguido de Enter para moverte (es decir, abrir) a ese directorio. Tu prompt debería verse así:

    volume/ $
    

Si todo funcionó correctamente, deberías ejecutar

    ls
    

y verás un archivo `volume.c` junto con un archivo `input.wav`.

Si tienes algún problema, sigue estos mismos pasos nuevamente para ver si puedes determinar dónde te equivocaste.

Detalles de implementación
----------------------

Completa la implementación de `volume.c` para que cambie el volumen de un archivo de sonido por un factor determinado.

*   El programa acepta tres argumentos en la línea de comandos: `input` para el nombre del archivo de audio original, `output` para el nombre del nuevo archivo de audio que se debe generar y `factor` es la cantidad por la que se debe escalar el volumen del archivo de audio original.
    *   Por ejemplo, si `factor` es `2.0`, entonces tu programa debería duplicar el volumen del archivo de audio en `input` y guardar el archivo de audio recién generado en `output`.
*   Tu programa debe leer primero la cabecera del archivo de entrada y escribir la cabecera en el archivo de salida. Recuerda que esta cabecera siempre tiene exactamente 44 bytes de longitud.
    *   Ten en cuenta que `volume.c` ya define una variable para ti llamada `HEADER_SIZE`, igual al número de bytes en la cabecera.
*   Tu programa debe luego leer los datos restantes del archivo WAV, una muestra de 16 bits (2 bytes) a la vez. Tu programa debe multiplicar cada muestra por el `factor` y escribir la nueva muestra en el archivo de salida.
    *   Puedes asumir que el archivo WAV usará valores firmados de 16 bits como muestras. En la práctica, los archivos WAV pueden tener números variables de bits por muestra, pero asumiremos muestras de 16 bits para este laboratorio.
*   Tu programa, si usa `malloc` , no debe dejar ningún rastro de memoria.

### Guía


<div class="alert" data-alert="primary" role="alert"><p>¡Este video se grabó cuando el curso aún usaba CS50 IDE para escribir código. Aunque la interfaz puede verse diferente a la de tu espacio de código, el comportamiento de los dos entornos debería ser bastante similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/LiGhjz9ColQ"></iframe>


### Consejos

*   Es probable que desees crear una matriz de bytes para almacenar los datos de la cabecera del archivo WAV que leerás del archivo de entrada. Usando el tipo `uint8_t` para representar un byte, puedes crear una matriz de `n` bytes para tu encabezado escribiendo lo siguiente:

<pre>
uint8_t header[n];
</pre>    

reemplazando `n` por el número de bytes. Luego puedes utilizar `header` como argumento de `fread` o `fwrite` para leer o escribir desde la cabecera.

*   Es probable que desees crear un "búfer" en el que almacenar muestras de audio que leerás del archivo WAV. Usando el tipo `int16_t` para almacenar una muestra de audio, puedes crear una variable de búfer escribiendo lo siguiente:

<pre>
int16_t buffer;
</pre>   

Luego puedes utilizar `&buffer` como argumento de `fread` o `fwrite` para leer o escribir desde el búfer. (Recuerda que el operador `&` se utiliza para obtener la dirección de la variable).

*   Puedes encontrar útil la documentación de [`fread`](https://man.cs50.io/3/fread) y [`fwrite`](https://man.cs50.io/3/fwrite) aquí.
    *   En particular, note que ambas funciones aceptan los siguientes argumentos:
        *   `ptr`: un puntero a la ubicación en memoria para almacenar datos (al leer de un archivo) o desde el cual escribir datos (al escribir datos en un archivo)
        *   `size`: el número de bytes en un elemento de datos
        *   `nmemb`: el número de elementos de datos (cada uno de `size` bytes) para leer o escribir
        *   `stream`: el puntero de archivo que se leerá o escribirá
    *   Según su documentación, `fread` devolverá el número de elementos de datos leídos con éxito. Puedes encontrarlo útil para comprobar cuándo has llegado al final del archivo.


<details><summary>¿No estás seguro de cómo resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-rtZkTAK2gg"></iframe></details>


### Cómo probar tu código

Tu programa debe comportarse como se muestra a continuación.

    $ ./volumen input.wav output.wav 2.0
    

Cuando escuches `output.wav` (haciendo clic con el control en `output.wav` en el navegador de archivos, eligiendo **Descargar** y luego abriendo el archivo en un reproductor de audio en tu computadora), ¡debe ser el doble de fuerte que` input.wav`!

    $ ./volumen input.wav output.wav 0.5
    

Cuando escuches `output.wav`, ¡debe tener la mitad del volumen que `input.wav`!

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`. ¡Pero asegúrate de compilar y probarlo también!

    check50 cs50/labs/2023/x/volume
    

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 volume.c
    

Cómo enviar tu trabajo
-------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/labs/2023/x/volume