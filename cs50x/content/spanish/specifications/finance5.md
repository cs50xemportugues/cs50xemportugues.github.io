## Especificación

### `register`

Completa la implementación de `register` de tal forma que permita a un usuario registrarse para obtener una cuenta a través de un formulario.

- Requiere que el usuario ingrese un nombre de usuario, implementado como un campo de texto cuyo `name` es `username`. Envía una disculpa si el input del usuario se encuentra en blanco o el nombre de usuario ya existe.
- Requiere que el usuario ingrese una contraseña, implementada como un campo de texto cuyo `name` es `password`, y luego que vuelva a ingresar la misma contraseña, implementada como un campo de texto cuyo `name` es `confirmation`. Envía una disculpa si cualquiera de los campos está en blanco o las contraseñas no coinciden.
- Envía la información ingresada por el usuario a través de `POST` hacia `/register`.
- `INSERTA` el nuevo usuario dentro de `users`, almacenando un hash de la contraseña del usuario, no la contraseña en sí. Hashea la contraseña del usuario con [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.security.generate_password_hash). Lo más probable es que quieras crear una nueva plantilla (por ejemplo, `register.html`) que sea bastante similar a `login.html`.

Una vez que has implementado `register` correctamente, deberías ser capaz de registrarte para obtener una cuenta e iniciar sesión (ya que `login` y `logout` ya están funcionando). Y deberías ser capaz de ver tus filas vía phpLiteAdmin o `sqlite3`.

### `quote`

Completa la implementación de `quote` de tal forma que permita a un usuario buscar el precio actual de un stock.

- Requiere que el usuario ingrese el símbolo de un stock, implementado como un campo de texto cuyo `name` es `symbol`.
- Envía la información ingresada por el usuario a través de `POST` hacia `/quote`.
- Lo más probable es que quieras crear dos nuevas plantillas (por ejemplo, `quote.html` y `quoted.html`). Cuando un usuario visita `/quote` vía GET, renderiza una de esas plantillas, dentro de la cual debe haber un formulario HTML que envía información a `/quote` vía POST. En respuesta a un POST, `quote` puede renderizar esa segunda plantilla, incrustando dentro de ella uno o más valores de `lookup`.

### `buy`

Completa la implementación de `buy` de tal forma que permita al usuario comprar stocks.

- Requiere que el usuario ingrese el símbolo de un stock, implementado como un campo de texto `name` cuyo es `symbol`. Envía una disculpa si el input está en blanco o el símbolo no existe (según el valor de retorno de `lookup`).
- Requiere que el usuario ingrese un número de acciones, implementado como un campo de texto `name` cuyo es `shares`. Envía una disculpa si el input no es un entero positivo.
- Envía la información ingresada por el usuario a través de `POST` hacia `/buy`.
- Al completar la compra, redirige al usuario a la página principal.
- Lo más probable es que quieras llamar `lookup` para buscar el precio actual del stock.
- Lo más probable es que quieras `SELECT` la cantidad de dinero que el usuario tiene actualmente en `users`.
- Agrega una o más tablas nuevas a `finance.db`, a través de las cuales puedas realizar un seguimiento de la compra. Almacena suficiente información para conocer quién compró qué, a qué precio y cuándo.
  - Utiliza los tipos de SQLite apropiados.
  - Define índices `UNIQUE` en cualquier campo que deba ser único.
  - Define índices (no `UNIQUE`) en cualquier campo a través del cual vayas a buscar (como a través de un `SELECT` con `WHERE`).
- Envía una disculpa, sin completar la compra, si el usuario no tiene suficiente dinero para comprar el número de acciones al precio actual.
- No tienes que preocuparte por las condiciones de carrera (o utilizar transacciones).

Una vez que hayas implementado `buy` correctamente, deberías ser capaz de ver las compras de los usuarios en tu(s) tabla(s) nueva(s) vía phpLiteAdmin o `sqlite3`.