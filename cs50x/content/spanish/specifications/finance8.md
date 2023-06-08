## Consejos

- Para formatear un valor como un valor en dólares estadounidenses (con centavos listados a dos decimales), puede utilizar el filtro `usd` en sus plantillas de Jinja (imprimiendo valores como `{{ value | usd }}` en lugar de `{{ value }}`.
- Dentro de `cs50.SQL` hay un método `execute` cuyo primer argumento debe ser una `str` de SQL. Si esa `str` contiene parámetros de signos de interrogación a los que se deben asignar valores, esos valores se pueden proporcionar como parámetros con nombre adicionales a `execute`. Vea la implementación de `login` para ejemplos de esto. El valor de retorno de `execute` es el siguiente:

  - Si `str` es un `SELECT`, entonces `execute` devuelve una lista de cero o más objetos `dict`, en los que hay claves y valores que representan los campos y celdas de una tabla, respectivamente.
  - Si `str` es un `INSERT` y la tabla en la que se insertaron los datos contiene una `PRIMARY KEY` autoincrementable, entonces `execute` devuelve el valor de la clave primaria de la nueva fila insertada.
  - Si `str` es un `DELETE` o un `UPDATE`, entonces `execute` devuelve el número de filas eliminadas o actualizadas por `str`.

- Recuerde que `cs50.SQL` registrará en la ventana de su terminal cualquier consulta que ejecute a través de `execute` (para que pueda confirmar si están como se pretendía).
- Asegúrese de utilizar parámetros vinculados con signo de interrogación (es decir, un [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) con nombre) al llamar al método `execute` de CS50, como `WHERE ?`. No use f-strings, [`format`](https://docs.python.org/3.6/library/functions.html#format,) o `+` (es decir, concatenación), de lo contrario corre el riesgo de un ataque de inyección de SQL.
- Si (y solo si) ya se siente cómodo con SQL, puede utilizar [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) o [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (es decir, [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)) en lugar de `cs50.SQL`.
- Puede agregar archivos estáticos adicionales a `static/`.
- Probablemente querrá consultar la documentación de [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) al implementar sus plantillas.
- Es **razonable** pedir a otros que prueben (e intenten provocar errores en) su sitio.
- Puede cambiar la estética de los sitios web, por ejemplo, mediante:
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/) y/o
  - [memegen.link](https://memegen.link/).
- Es posible que encuentre útiles la documentación de [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) y la documentación de [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/)!

## Preguntas frecuentes

### ImportError: No module named ‘application’

De forma predeterminada, `flask` busca un archivo llamado `app.py` en el directorio de trabajo actual (porque hemos configurado el valor de `FLASK_APP`, una variable de entorno, en `app.py`). Si ve este error, ¡es probable que haya ejecutado `flask` en el directorio incorrecto!

### OSError: \[Errno 98\] Address already in use

Si, al ejecutar `flask`, ve este error, es probable que aún tenga `flask` en ejecución en otra pestaña. Asegúrese de matar ese otro proceso, como con Ctrl-c, antes de volver a iniciar `flask`. Si no tiene ninguna otra pestaña, ejecute `fuser -k 8080/tcp` para matar cualquier proceso que siga escuchando en el puerto TCP 8080.

## Cómo enviar

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/finance
"