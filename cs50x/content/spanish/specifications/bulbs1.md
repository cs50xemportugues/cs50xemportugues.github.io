Bombillas
=====

Bombillas Que No Están Tan Rotas
-------------------------

En la clase, es posible que hayas notado lo que parecía un "error" en la parte delantera del escenario, donde algunas de las bombillas siempre parecen estar apagadas:

![captura de pantalla de la clase de la semana 2 con una fila de bombillas](https://cs50.harvard.edu/x/2023/psets/2/bulbs/binary_bulbs.jpg)

Cada secuencia de bombillas, sin embargo, codifica un mensaje en _binario_, el lenguaje que hablan las computadoras. ¡Vamos a escribir un programa para hacer mensajes secretos propios, quizás que incluso podamos poner en el escenario!

Comenzando
---------------

Abre [VS Code] (https://code.cs50.io/).

Comienza haciendo clic dentro de tu ventana de terminal y luego ejecuta `cd` por sí solo. Deberías encontrar que su "indicación" se parece a la siguiente.

    $ 
    

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/2/bulbs.zip
    

seguido de Enter para descargar un archivo ZIP llamado `bulbs.zip` en tu espacio de códigos. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter de ese tipo!

Ahora, ejecuta

    unzip bulbs.zip
    

para crear una carpeta llamada `bulbs`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm bulbs.zip
    

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd bulbs
    

seguido de Enter para entrar en (es decir, abrir) ese directorio. Tu indicación debería verse así.

    bulbs/ $ 
    

Si todo fue exitoso, deberías ejecutar

    ls
    

y ver un archivo llamado `bulbs.c`. Ejecutar `code bulbs.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.