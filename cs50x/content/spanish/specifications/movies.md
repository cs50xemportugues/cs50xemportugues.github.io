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

Especificación
-------------

Para cada uno de los siguientes problemas, debes escribir una sola consulta SQL que produzca los resultados especificados por cada problema. Tu respuesta debe tomar la forma de una sola consulta SQL, aunque puedes anidar otras consultas dentro de tu consulta. **No debes** asumir nada sobre los `id` de cualquier película o persona en particular: tus consultas deben ser precisas incluso si el `id` de cualquier película o persona fuera diferente. Finalmente, cada consulta debe devolver solo los datos necesarios para responder la pregunta: si el problema solo te pide que produzcas los nombres de las películas, por ejemplo, entonces tu consulta no debe producir también el año de lanzamiento de cada película.

Puedes comprobar los resultados de tus consultas en [IMDb](https://www.imdb.com/) en sí mismo, pero ten en cuenta que las calificaciones en el sitio web pueden diferir de las de `movies.db`, ya que puede haber más votos emitidos desde que descargamos los datos.

1.  En `1.sql`, escribe una consulta SQL para listar los títulos de todas las películas lanzadas en el 2008.
    *   Tu consulta debe producir una tabla con una sola columna para el título de cada película.
2.  En `2.sql`, escribe una consulta SQL para determinar el año de nacimiento de Emma Stone.
    *   Tu consulta debe producir una tabla con una sola columna y una sola fila (sin contar el encabezado) que contenga el año de nacimiento de Emma Stone.
    *   Puedes asumir que solo hay una persona en la base de datos con el nombre Emma Stone.
3.  En `3.sql`, escribe una consulta SQL para listar los títulos de todas las películas con una fecha de lanzamiento en o después del 2018, en orden alfabético.
    *   Tu consulta debe producir una tabla con una sola columna para el título de cada película.
    *   Las películas lanzadas en el 2018 deben estar incluidas, al igual que las películas con fechas de lanzamiento en el futuro.
4.  En `4.sql`, escribe una consulta SQL para determinar el número de películas con una calificación de 10.0 en IMDb.
    *   Tu consulta debe producir una tabla con una sola columna y una sola fila (sin contar el encabezado) que contenga el número de películas con una calificación de 10.0.
5.  En `5.sql`, escribe una consulta SQL para listar los títulos y los años de lanzamiento de todas las películas de Harry Potter, en orden cronológico.
    *   Tu consulta debe producir una tabla con dos columnas, una para el título de cada película y otra para el año de lanzamiento de cada película.
    *   Puedes asumir que el título de todas las películas de Harry Potter comenzará con las palabras "Harry Potter", y que si un título de película comienza con las palabras "Harry Potter", es una película de Harry Potter.
6.  En `6.sql`, escribe una consulta SQL para determinar la calificación promedio de todas las películas lanzadas en el 2012.
    *   Tu consulta debe producir una tabla con una sola columna y una sola fila (sin contar el encabezado) que contenga la calificación promedio.
7.  En `7.sql`, escribe una consulta SQL para listar todas las películas lanzadas en el 2010 y sus calificaciones, en orden descendente por calificación. Para las películas con la misma calificación, ordénalas alfabéticamente por título.
    *   Tu consulta debe producir una tabla con dos columnas, una para el título de cada película y otra para la calificación de cada película.
    *   Las películas que no tienen calificaciones no deben incluirse en el resultado.
8.  En `8.sql`, escribe una consulta SQL para listar los nombres de todas las personas que protagonizaron Toy Story.
    *   Tu consulta debe producir una tabla con una sola columna para el nombre de cada persona.
    *   Puedes asumir que solo hay una película en la base de datos con el título Toy Story.
9.  En `9.sql`, escribe una consulta SQL para listar los nombres de todas las personas que protagonizaron una película lanzada en el 2004, ordenados por año de nacimiento.
    *   Tu consulta debe producir una tabla con una sola columna para el nombre de cada persona.
    *   Las personas con el mismo año de nacimiento pueden aparecer en cualquier orden.
    *   No te preocupes por las personas que no tienen un año de nacimiento listado, siempre y cuando aquellas que sí lo tengan estén listadas en orden.
    *   Si una persona apareció en más de una película en el 2004, solo debería aparecer una vez en tus resultados.
10.  En `10.sql`, escribe una consulta SQL para listar los nombres de todas las personas que han dirigido una película que recibió una calificación de al menos 9.0.
    *   Tu consulta debe producir una tabla con una sola columna para el nombre de cada persona.
    *   Si una persona dirigió más de una película que recibió una calificación de al menos 9.0, solo debería aparecer una vez en tus resultados.
11.  En `11.sql`, escribe una consulta SQL para listar los títulos de las cinco películas con las calificaciones más altas (en orden) en las que Chadwick Boseman participó, comenzando con la de calificación más alta.
    *   Tu consulta debe producir una tabla con una sola columna para el título de cada película.
    *   Puedes asumir que solo hay una persona en la base de datos con el nombre de Chadwick Boseman.
12.  En `12.sql`, escribe una consulta SQL para listar los títulos de todas las películas en las que Johnny Depp y Helena Bonham Carter actuaron.
    *   Tu consulta debe producir una tabla con una sola columna para el título de cada película.
    *   Puedes asumir que solo hay una persona en la base de datos con el nombre de Johnny Depp.
    *   Puedes asumir que solo hay una persona en la base de datos con el nombre de Helena Bonham Carter.
13.  En `13.sql`, escribe una consulta SQL para listar los nombres de todas las personas que protagonizaron una película en la que también participó Kevin Bacon.
    *   Tu consulta debe producir una tabla con una sola columna para el nombre de cada persona.
    *   Puede haber varias personas llamadas Kevin Bacon en la base de datos. Asegúrate de seleccionar solo al Kevin Bacon nacido en 1958.
    *   Kevin Bacon en sí mismo no debe incluirse en la lista resultante.

Walkthrough
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Uso
---

Para probar tus consultas en VS Code, puedes consultar la base de datos ejecutando

    $ cat nombre_archivo.sql | sqlite3 peliculas.db
    

donde `nombre_archivo.sql` es el archivo que contiene tu consulta SQL.

También puedes ejecutar

    $ cat nombre_archivo.sql | sqlite3 peliculas.db > output.txt
    

para redirigir la salida de la consulta a un archivo de texto llamado `output.txt`. (¡Esto puede ser útil para verificar cuántas filas devuelve tu consulta!)

Pistas
------

*   ¡Mira [esta referencia de palabras clave de SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para obtener algunas sintaxis de SQL que pueden ser útiles!
*   ¡Mira [sqlstyle.guide](https://www.sqlstyle.guide/) para obtener consejos sobre un buen estilo en SQL, especialmente a medida que tus consultas se hacen más complejas!

Pruebas
-------

Aunque `check50` está disponible para este problema, se recomienda que, en su lugar, compruebes tu código por ti mismo para cada uno de los siguientes. Puede ejecutar `sqlite3 peliculas.db` para ejecutar consultas adicionales en la base de datos para asegurarte de que tu resultado sea correcto.

Si estás utilizando la base de datos `movies.db` proporcionada en el conjunto de problemas de este conjunto, deberías encontrar que

*   Al ejecutar `1.sql` se obtiene una tabla con 1 columna y 10.050 filas.
*   Al ejecutar `2.sql` se obtiene una tabla con 1 columna y 1 fila.
*   Al ejecutar `3.sql` se obtiene una tabla con 1 columna y 88.918 filas.
*   Al ejecutar `4.sql` se obtiene una tabla con 1 columna y 1 fila.
*   Al ejecutar `5.sql` se obtiene una tabla con 2 columnas y 12 filas.
*   Al ejecutar `6.sql` se obtiene una tabla con 1 columna y 1 fila.
*   Al ejecutar `7.sql` se obtiene una tabla con 2 columnas y 7.085 filas.
*   Al ejecutar `8.sql` se obtiene una tabla con 1 columna y 4 filas.
*   Al ejecutar `9.sql` se obtiene una tabla con 1 columna y 18.946 filas.
*   Al ejecutar `10.sql` se obtiene una tabla con 1 columna y 3.392 filas.
*   Al ejecutar `11.sql` se obtiene una tabla con 1 columna y 5 filas.
*   Al ejecutar `12.sql` se obtiene una tabla con 1 columna y 7 filas.
*   Al ejecutar `13.sql` se obtiene una tabla con 1 columna y 182 filas.

Ten en cuenta que las cuentas de filas no incluyen filas de encabezado que solo muestran nombres de columna.

Si tu consulta devuelve un número de filas ligeramente diferente al resultado esperado, ¡asegúrate de manejar correctamente los duplicados! Para las consultas que piden una lista de nombres, no se debe listar dos veces a la misma persona, pero deben aparecer dos personas distintas que tienen el mismo nombre.

Ejecuta el siguiente comando para evaluar la corrección de tu código usando `check50`.

    check50 cs50/problems/2023/x/movies
    

Cómo enviar
-----------

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2023/x/movies
    

Agradecimientos
---------------

Información cortesía de IMDb ([imdb.com](https://www.imdb.com)). Usado con permiso.

