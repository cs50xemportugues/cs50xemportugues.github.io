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