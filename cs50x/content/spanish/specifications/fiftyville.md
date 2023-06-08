Fiftyville 
==========

Escribe consultas SQL para resolver un misterio.

Un misterio en Fiftyville
-----------------------

¡El CS50 Duck ha sido robado! El pueblo de Fiftyville ha solicitado tu ayuda para resolver el misterio del pato robado. Las autoridades creen que el ladrón robó el pato y luego, poco después, tomó un vuelo fuera del pueblo con la ayuda de un cómplice. Tu objetivo es identificar:

* Quién es el ladrón,
* A qué ciudad escapó el ladrón, y
* Quién es el cómplice del ladrón que lo ayudó a escapar.

Todo lo que sabes es que el robo **ocurrió el 28 de julio de 2021** y que ocurrió en **Humphrey Street**.

¿Cómo resolverás este misterio? Las autoridades de Fiftyville han tomado algunos registros del pueblo alrededor del momento del robo y preparado una base de datos SQLite para ti, llamada `fiftyville.db`, que contiene tablas de datos del pueblo. Puedes consultar la tabla utilizando consultas SQL `SELECT` para acceder a los datos de tu interés. Utilizando solo la información de la base de datos, tu tarea es resolver el misterio.

Empezando
---------------

Ingresa a [code.cs50.io](https://code.cs50.io/), haz clic en tu ventana de terminal y ejecuta el comando `cd` por sí solo. Deberías encontrar que la línea de comandos de tu ventana de terminal sea la siguiente:

    $
    

Luego ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/7/fiftyville.zip
    

para descargar un archivo ZIP llamado `fiftyville.zip` en tu espacio de códigos.

Luego ejecuta

    unzip fiftyville.zip
    

para crear una carpeta llamada `"fiftyville"`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm fiftyville.zip
    

y escribe "y" seguido de "Enter" en la ventana de comandos para eliminar el archivo ZIP que descargaste.

Ahora escribe 

    cd fiftyville
    

seguido de Enter para moverte hacia el directorio (es decir, abrir) esa carpeta. Tu ventana de comandos debería ser como la siguiente:

    fiftyville/$
    

Ejecuta `ls` solo y deberías ver algunos archivos:


    answers.txt  fiftyville.db  log.sql
    

Si tienes algún problema, sigue estos mismos pasos de nuevo y verifica donde te has equivocado.

Especificación 
----------------

Para este problema, igual de importante que resolver el misterio es el proceso que uses para resolverlo. En` log.sql`, lleva un registro de todas las consultas de SQL que ejecutes en la base de datos. Arriba de cada consulta, etiquétala con un comentario (en SQL, los comentarios son cualquier línea que empieza con `--`) describiendo el porqué de la consulta y/o qué información esperas obtener de esa consulta en particular. Puedes usar comentarios en el archivo de registro para agregar notas adicionales acerca de tu proceso de pensamiento mientras resuelves el misterio: ¡este archivo servirá como evidencia del proceso que usaste para identificar al ladrón!

Mientras escribas tus consultas, quizás notes que algunas de ellas pueden llegar a ser muy complejas. Para ayudar a mantener tus consultas legibles, consulta los principios de buen estilo en [sqlstyle.guide] (https://www.sqlstyle.guide). ¡La sección de [indentación] (https://www.sqlstyle.guide/#indentation) puede ser particularmente útil!

Una vez que resuelvas el misterio, completa cada línea en `answers.txt` llenando el nombre del ladrón, la ciudad a la que el ladrón escapó y el nombre del cómplice del ladrón quien lo ayudó a escapar del pueblo. (¡Asegúrate de no cambiar ningún texto existente en el archivo o de agregar alguna otra línea al archivo!)

Finalmente, debes enviar tanto tus archivos`log.sql` como `answers.txt`.

Walkthrough
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video=" " src="https://www.youtube.com/embed/YHhgEoJMDnU?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div> 

Sugerencias
-----

* Ejecuta `sqlite3 fiftyville.db` para comenzar a ejecutar consultas en la base de datos.
* Mientras se ejecuta`sqlite3`, ejecutar `.tables` te listará todas las tablas de la base de datos.
* Mientras se ejecuta `sqlite3`, ejecutar `.schema TABLE_NAME`, donde `TABLE_NAME` es el nombre de una tabla en la base de datos, mostrará el comando `CREATE TABLE` usado para crear la tabla. Esto puede ser útil para saber en qué columnas hacer consultas.
* Quizás te resulte útil empezar con la tabla `crime_scene_reports`. Comienza buscando un reporte de la escena del crimen que coincida con la fecha y el lugar del crimen.
* Consulta [esta referencia de palabras clave SQL] (https://www.w3schools.com/sql/sql_ref_keywords.asp) para obtener alguna sintaxis de SQL que pueda ser útil!

Testeos
-------
Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`.

    check50 cs50/problems/2023/x/fiftyville
    

Cómo enviar
--------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/fiftyville
    

Agradecimientos
---------------
Inspirado en otro caso de[SQL City] (https://mystery.knightlab.com/).