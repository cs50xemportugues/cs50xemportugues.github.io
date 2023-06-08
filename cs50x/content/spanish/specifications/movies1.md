Películas
=======

Escribe consultas SQL para responder preguntas sobre una base de datos de películas.

Empezando
----------

Inicia sesión en [code.cs50.io](https://code.cs50.io/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que la indicación de tu ventana de terminal se asemeja a la siguiente:

    $
    

A continuación ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/7/movies.zip
    

para descargar un archivo ZIP llamado `movies.zip` a tu espacio de trabajo.

Luego ejecuta

    unzip movies.zip
    

para crear una carpeta llamada `movies`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm movies.zip
    

y responde con "y" seguido de Enter cuando se te pida para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd movies
    

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu indicación debería asemejarse a la siguiente.

    movies/ $
    

Ejecuta `ls` por sí solo y deberías ver 13 archivos .sql, así como `movies.db`.

Si tienes algún problema, sigue estos mismos pasos de nuevo y determina dónde te equivocaste.

Comprensión
-----------

Se te proporciona un archivo llamado `movies.db`, una base de datos SQLite que almacena datos de [IMDb](https://www.imdb.com/) sobre películas, las personas que las dirigieron y protagonizaron, y sus calificaciones. En una ventana de terminal, ejecuta `sqlite3 movies.db` para que puedas comenzar a ejecutar consultas en la base de datos.

En primer lugar, cuando `sqlite3` te solicite que proporciones una consulta, escribe `.schema` y presiona enter. Esto imprimirá las declaraciones `CREATE TABLE` que se utilizaron para generar cada una de las tablas en la base de datos. Al examinar esas declaraciones, puedes identificar las columnas presentes en cada tabla.

Observa que la tabla `movies` tiene una columna `id` que identifica de manera única cada película, así como columnas para el `título` de una película y el `año` en que se lanzó la película. La tabla `people` también tiene una columna `id`, y también tiene columnas para el `nombre` de cada persona y el año `de nacimiento`.

Las calificaciones de las películas, por otro lado, se almacenan en la tabla `ratings`. La primera columna en la tabla es `movie_id`: una clave externa que hace referencia al `id` de la tabla `movies`. El resto de la fila contiene datos sobre la `calificación` de cada película y el número de `votos` que ha recibido la película en IMDb.

Por último, las tablas `stars` y `directors` relacionan personas con las películas en las que actuaron o dirigieron. (Solo se incluyen las estrellas y directores principales). Cada tabla tiene sólo dos columnas: `movie_id` y `person_id`, que hacen referencia a una película específica y a una persona, respectivamente.

El desafío que tienes por delante es escribir consultas SQL para responder a una variedad de preguntas diferentes seleccionando datos de una o más de estas tablas.