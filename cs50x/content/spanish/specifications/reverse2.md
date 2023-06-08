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