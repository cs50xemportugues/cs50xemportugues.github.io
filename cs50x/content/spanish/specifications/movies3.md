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