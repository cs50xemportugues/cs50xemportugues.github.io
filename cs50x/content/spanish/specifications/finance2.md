## Empezando

Inicia sesión en [code.cs50.io](https://code.cs50.io/), haz clic en la ventana del terminal y ejecuta `cd` por sí solo. Deberías ver que el prompt de tu ventana del terminal se asemeja a lo siguiente:

    $

A continuación, ejecuta:

    wget https://cdn.cs50.net/2022/fall/psets/9/finance.zip

para descargar un archivo ZIP llamado `finance.zip` en tu space de códigos.

Luego ejecuta

    unzip finance.zip

para crear una carpeta llamada `finance`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm finance.zip

y luego responder con "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

     cd finance

seguido de Enter para moverte dentro (es decir, abrir) de ese directorio. Tu prompt debe mostrar ahora lo siguiente:

    finance/ $

Ejecuta `ls` por sí solo y deberías ver algunos archivos y carpetas:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Si te encuentras con algún problema, sigue los mismos pasos de nuevo y trata de determinar dónde te equivocaste.

### Configuración

Antes de comenzar esta tarea, necesitamos registrar una clave API para poder consultar los datos de IEX. Para ello, sigue estos pasos:

- Visita [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
- Selecciona el tipo de cuenta "Individual", luego ingresa tu nombre, dirección de correo electrónico y una contraseña, y haz clic en "Crear cuenta".
- Una vez registrado, desplázate hacia abajo hasta "Comenzar gratis" y haz clic en "Seleccionar Plan de Inicio" para elegir el plan gratuito. _Ten en cuenta que este plan solo funciona durante 30 días a partir del día en que creaste tu cuenta._ ¡Ten esto en cuenta si podrías planear usar esta misma API para tu proyecto final!
- Una vez que hayas confirmado tu cuenta mediante un correo electrónico de confirmación, visita [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
- Copia la clave que aparece bajo la columna _Token_ (debería comenzar con `pk_`).
- En tu ventana del terminal, ejecuta:

<pre>
$ export API_KEY=value
</pre>

donde `value` es el valor pegado (sin ningún espacio inmediatamente antes o después del `=`). También puedes pegar ese valor en un documento de texto en algún lugar, en caso de que lo necesites de nuevo más adelante.