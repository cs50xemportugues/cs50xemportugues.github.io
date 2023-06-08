### Ejecución

Inicie el servidor web integrado de Flask (dentro de `finance/`):

    $ flask run

Visite la URL que imprime `flask` para ver el código de distribución en acción. Aunque aún no podrá iniciar sesión ni registrarse.

Dentro de `finance/`, ejecute `sqlite3 finance.db` para abrir `finance.db` con `sqlite3`. Si ejecuta `.schema` en el intérprete de SQLite, note cómo `finance.db` viene con una tabla llamada `users`. Eche un vistazo a su estructura (es decir, su esquema). Observe cómo, de forma predeterminada, los nuevos usuarios recibirán $10,000 en efectivo. Pero si ejecuta `SELECT * FROM users;`, aún no hay usuarios (es decir, filas) para navegar.

Otra forma de ver `finance.db` es con un programa llamado phpLiteAdmin. Haga clic en `finance.db` en el navegador de archivos de su espacio de código, luego haga clic en el enlace que se muestra debajo del texto "Visite el siguiente enlace para autorizar la vista previa de GitHub". Debería ver información sobre la base de datos en sí, así como una tabla, `users`, igual que la que vio en el intérprete de `sqlite3` con `.schema`.

### Comprensión

#### `app.py`

Abra `app.py`. En la parte superior del archivo hay una serie de importaciones, entre ellas, el módulo SQL de CS50 y algunas funciones de ayuda. Más sobre eso pronto.

Después de configurar [Flask](https://flask.pocoo.org/), observe que este archivo desactiva el almacenamiento en caché de las respuestas (si está en modo de depuración, que es el valor predeterminado en su espacio de código code50), para evitar que se realice un cambio en algún archivo y que el navegador no lo note. Observe a continuación cómo configura [Jinja](https://jinja.pocoo.org/) con un "filtro" personalizado, `usd`, una función (definida en `helpers.py`) que facilitará la formateo valores como dólares estadounidenses (USD). Luego configura Flask para almacenar [sesiones](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) en el sistema de archivos local (es decir, disco) en lugar de almacenarlas en cookies (firmadas digitalmente), que es el valor predeterminado de Flask. Después, configura el módulo SQL de CS50 para usar `finance.db`.

Luego encontramos una gran cantidad de rutas, solo dos de las cuales están completamente implementadas: `login` y `logout`. Primero lea la implementación de `login`. Observe cómo usa `db.execute` (de la biblioteca CS50) para consultar `finance.db`. Y observe cómo usa `check_password_hash` para comparar hashes de contraseñas de los usuarios. También observe cómo `login` "recuerda" que un usuario ha iniciado sesión almacenando su `user_id`, un INTEGER, en `session`. De esta manera, cualquier ruta de este archivo puede verificar qué usuario, si hay alguno, ha iniciado sesión. Finalmente, observe cómo una vez que el usuario haya iniciado sesión correctamente, `login` redirigirá a `"/"`, llevando al usuario a su página de inicio. Mientras tanto, observe cómo `logout` simplemente borra `session`, lo que efectivamente cierra la sesión de un usuario.

Observe cómo la mayoría de las rutas están "decoradas" con `@login_required` (una función también definida en `helpers.py`). Ese decorador asegura que, si un usuario intenta visitar cualquiera de esas rutas, primero se redirigirá a `login` para iniciar sesión.

Observe también cómo la mayoría de las rutas admiten GET y POST. Aún así, ¡la mayoría de ellas devuelven una "disculpa", ya que aún no están implementadas!