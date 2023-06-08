Laboratorio 7: Canciones
============

<div class="alert" data-alert="warning" role="alert"><p>Puedes colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante de cualquier grupo contribuya igualmente al laboratorio.</p></div>

Escriba consultas SQL para responder preguntas sobre una base de datos de canciones.

Comenzando
---------------

Abra [VS Code](https://code.cs50.io/).

Comience haciendo clic en su ventana de terminal y luego ejecute `cd` por sí solo. Debería encontrar que su "prompt" se parece al siguiente.

     $
     

Haga clic dentro de esa ventana de terminal y luego ejecute

     wget https://cdn.cs50.net/2022/fall/labs/7/songs.zip
     

seguido de Enter para descargar un ZIP llamado `songs.zip` en su espacio de código. ¡Asegúrese de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter!

Ahora ejecute

     unzip songs.zip
     

para crear una carpeta llamada `songs`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

     rm songs.zip
     

y responda con "yº seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.

Ahora escriba

     cd songs
     

seguido de Enter para moverse (es decir, abrir) en ese directorio. Su indicador debe parecerse al siguiente.

     songs/ $
     

Si todo ha sido exitoso, debería ejecutar

     ls
     

y deberías ver 8 archivos .sql, `songs.db` y `answers.txt`.

Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.

Comprensión
-------------

Se proporciona un archivo llamado `songs.db`, una base de datos SQLite que almacena datos de [Spotify](https://developer.spotify.com/documentation/web-api/) sobre canciones y sus artistas. Este conjunto de datos contiene las 100 canciones más sonadas en Spotify en 2018. En una ventana de terminal, ejecute `sqlite3 songs.db` para comenzar a ejecutar consultas en la base de datos.

Primero, cuando `sqlite3` le pida que proporcione una consulta, escriba `.schema` y presione enter. Esto mostrará las declaraciones `CREATE TABLE` que se utilizaron para generar cada una de las tablas en la base de datos. Al examinar esas declaraciones, puede identificar las columnas presentes en cada tabla.

Observe que cada `artista` tiene un `id` y un `nombre`. También observe que cada canción tiene un `nombre`, un `id_artista` (correspondiente al `id` del artista de la canción), así como valores para la capacidad de baile, energía, clave, volumen, cantabilidad (presencia de palabras habladas en una pista), valencia, tempo y la duración de la canción (medida en milisegundos).

El desafío que tiene por delante es escribir consultas SQL para responder una variedad de preguntas diferentes seleccionando datos de una o más de estas tablas. Después de hacerlo, reflexionará sobre las formas en que Spotify podría usar los mismos datos en su campaña anual de [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) para caracterizar los hábitos de los oyentes.

Detalles de implementación
----------------------

Para cada uno de los siguientes problemas, debe escribir una sola consulta SQL que produzca los resultados que cada problema especifica. Su respuesta debe tomar la forma de una sola consulta SQL, aunque puede anidar otras consultas dentro de su consulta. No debe asumir nada sobre los `id` de ninguna canción o artista en particular: sus consultas deben ser precisas incluso si el `id` de alguna canción o persona en particular fueran diferentes. Finalmente, cada consulta debe devolver solo los datos necesarios para responder la pregunta: si el problema solo le pide que emita los nombres de las canciones, por ejemplo, entonces su consulta no debe emita también el tempo de cada canción.

1.  En `1.sql`, escriba una consulta SQL para listar los nombres de todas las canciones en la base de datos.
    *   Su consulta debe producir una tabla con una sola columna para el nombre de cada canción.
2.  En `2.sql`, escriba una consulta SQL para listar los nombres de todas las canciones en orden creciente de tempo.
    *   Su consulta debe producir una tabla con una sola columna para el nombre de cada canción.
3.  En `3.sql`, escriba una consulta SQL para listar los nombres de las 5 canciones más largas, en orden descendente de longitud.
    *   Su consulta debe producir una tabla con una sola columna para el nombre de cada canción.
4.  En `4.sql`, escriba una consulta SQL que enumere los nombres de cualquier canción que tenga una capacidad de baile, energía y valencia superior a 0,75.
    *   Su consulta debe producir una tabla con una sola columna para el nombre de cada canción.
5.  En `5.sql`, escriba una consulta SQL que devuelva la energía promedio de todas las canciones.
    *   Su consulta debe producir una tabla con una sola columna y una sola fila que contenga la energía promedio.
6.  En `6.sql`, escriba una consulta SQL que enumere los nombres de las canciones que son de Post Malone.
    *   Su consulta debe producir una tabla con una sola columna para el nombre de cada canción.
    *   No debe hacer suposiciones sobre cuál es el `id_artista` de Post Malone.
7.  En `7.sql`, escriba una consulta SQL que devuelva la energía promedio de las canciones que son de Drake.
    *   Su consulta debe producir una tabla con una sola columna y una sola fila que contenga la energía promedio.
    *   No debe hacer suposiciones sobre cuál es el `id_artista` de Drake.
8.  En `8.sql`, escriba una consulta SQL que enumere los nombres de las canciones que tienen otros artistas.
    *   Las canciones que tienen otros artistas incluirán "feat." en el nombre de la canción.
    *   Su consulta debe producir una tabla con una sola columna para el nombre de cada canción.

### Tutorial

<div class="alert" data-alert="primary" role="alert"><p>Este video fue grabado cuando el curso todavía estaba usando CS50 IDE para escribir código. ¡Aunque la interfaz puede verse diferente a su espacio de código, el comportamiento de los dos entornos debería ser bastante similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/wgKPUd_95AA"></iframe>


Uso
-----

Además de ejecutar sus consultas en `sqlite3`, puede probar sus consultas en la terminal de VS Code ejecutando

     $ cat filename.sql | sqlite3 songs.db
     

donde `filename.sql` es el archivo que contiene su consulta SQL.

### Consejos

*   Consulte esta [referencia de palabras clave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para obtener información sobre la sintaxis SQL que puede ser útil.


<details><summary>¿No está seguro de cómo resolverlo?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/7hydPL9ZswE"></iframe></details>


### Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) es una función que presenta las 100 canciones más tocadas de los usuarios de Spotify del año pasado. En 2021, Spotify Wrapped calculó un ["Aura de audio"](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) para cada usuario, una "lectura de los dos estados de ánimo más prominentes de su narrador dictados por sus canciones y artistas principales del año ". Supongamos que Spotify determina un aura de audio mirando la energía promedio, valencia y capacidad de baile de las 100 mejores canciones de una persona del año pasado. En `answers.txt`, reflexione sobre las siguientes preguntas:

*   Si `songs.db` contiene las 100 mejores canciones de un oyente de 2018, ¿cómo caracterizaría su aura de audio?
*   Hipotetice sobre por qué la forma en que ha calculado este aura podría _no_ ser muy representativa del oyente. ¿Qué mejores formas de calcular este aura propondría?

¡Asegúrese de enviar `answers.txt` junto con cada uno de sus archivos `.sql`!

### Pruebas

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`.

     check50 cs50/labs/2023/x/songs
     

Cómo presentar
-------------

En su terminal, ejecute lo siguiente para enviar su trabajo.

     submit50 cs50/labs/2023/x/songs
     

Agradecimientos
----------------

Conjunto de datos de [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).