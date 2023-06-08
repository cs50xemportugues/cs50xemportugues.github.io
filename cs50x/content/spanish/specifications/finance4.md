#### `helpers.py`

A continuación, eche un vistazo a `helpers.py`. Ahí está la implementación de `apology`. Observe cómo finalmente presenta una plantilla, `apology.html`. También sucede que define dentro de sí misma otra función, `escape`, que simplemente usa para reemplazar caracteres especiales en las disculpas. Al definir `escape` dentro de `apology`, hemos acotado la primera a la última; ninguna otra función podrá (ni necesitará) llamarla.

A continuación en el archivo está `login_required`. No se preocupe si este es un poco críptico, ¡pero si alguna vez se ha preguntado cómo una función puede devolver otra función, aquí tiene un ejemplo!

A continuación está `lookup`, una función que, dada un `símbolo` (por ejemplo, NFLX), devuelve una cotización de acciones para una empresa en forma de un `dict` con tres claves: `name`, cuyo valor es una cadena (`str`), el nombre de la empresa; `price`, cuyo valor es un número de coma flotante (`float`); y `símbolo`, cuyo valor es una cadena (`str`), una versión canonizada (en mayúsculas) del símbolo de una acción, independientemente de cómo se haya capitalizado ese símbolo cuando se pasó a `lookup`.

Por último en el archivo está `usd`, una función corta que simplemente formatea un número de coma flotante (`float`) como USD (por ejemplo, `1234,56` se formatea como `$1.234,56`).

#### `requirements.txt`

A continuación, eche un vistazo rápido a `requirements.txt`. Ese archivo simplemente prescribe los paquetes en los que dependerá esta aplicación.

#### `static/`

Eche un vistazo también a `static/`, dentro del cual está `styles.css`. Ahí es donde vive un poco de CSS inicial. Usted es libre de modificarlo como considere oportuno.

#### `templates/`

Ahora revise `templates/`. En `login.html`, existe, básicamente, un formulario HTML, estilizado con [Bootstrap](https://getbootstrap.com/). En `apology.html`, por otro lado, hay una plantilla para una disculpa. Recuerde que `apology` en `helpers.py` tomó dos argumentos: `message`, que se pasó a `render_template` como el valor de `bottom`, y, opcionalmente, `code`, que se pasó a `render_template` como el valor de `top`. ¡Observe cómo se usan finalmente esos valores en `apology.html`! Y [aquí está la razón](https://github.com/jacebrowning/memegen) 0:-)

Por último está `layout.html`. Es un poco más grande de lo habitual, pero eso se debe principalmente a que viene con una elegante "navbar" (barra de navegación) que es compatible con dispositivos móviles, también basada en Bootstrap. Observe cómo define un bloque, `main`, dentro del cual se colocarán plantillas (incluyendo `apology.html` y `login.html`). También incluye soporte para el [mensaje intermitente](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing) de Flask para que pueda transmitir mensajes de una ruta a otra para que los vea el usuario.