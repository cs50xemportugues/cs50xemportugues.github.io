### `index`

Completa la implementación de `index` de tal manera que muestre una tabla HTML que resuma, para el usuario actualmente conectado, qué acciones son propiedad del usuario, el número de acciones que posee, el precio actual de cada acción y el valor total de cada posesión (es decir, acciones por precio). También muestre el saldo en efectivo actual del usuario junto con el gran total (es decir, el valor total de las acciones más el efectivo).

- Es posible que desees ejecutar múltiples `SELECT`. Dependiendo de cómo implementes tu(s) tabla(s), es posible que te resulten útiles [GROUP BY](https://www.google.com/search?q=SQLite+GROUP+BY), [HAVING](https://www.google.com/search?q=SQLite+HAVING), [SUM](https://www.google.com/search?q=SQLite+SUM) y/o [WHERE](https://www.google.com/search?q=SQLite+WHERE).
- Es posible que desees llamar a `lookup` para cada acción.

### `sell`

Completa la implementación de `sell` de tal manera que permita al usuario vender acciones de una acción (que tenga en posesión).

- Requiere que el usuario introduzca el símbolo de una acción, que se implementa como un menú `select` cuyo nombre es `symbol`. Muestra una disculpa si el usuario no selecciona una acción o si (de alguna manera, después de haberse enviado) el usuario no tiene ninguna acción de esa clase.
- Requiere que el usuario introduzca un número de acciones, implementado como un campo de texto cuyo nombre es `shares`. Muestra una disculpa si la entrada no es un número entero positivo o si el usuario no posee tantas acciones de esa clase.
- Envía la entrada del usuario a través de un `POST` a `/sell`.
- Al completar, redirige al usuario a la página de inicio.
- No es necesario preocuparse por condiciones de carrera (o utilizar transacciones).

### `history`

Completa la implementación de `history` de tal manera que muestre una tabla HTML que resuma todas las transacciones de un usuario, listando fila por fila cada compra y cada venta.

- Para cada fila, deja claro si una acción se compró o se vendió e incluye el símbolo de la acción, el precio de compra o venta, el número de acciones compradas o vendidas y la fecha y hora en que se realizó la transacción.
- Es posible que debas modificar la tabla que creaste para `buy` o complementarla con una tabla adicional. Intenta minimizar las redundancias.

### Toque personal

Implementa al menos un toque personal de tu elección:

- Permitir a los usuarios cambiar sus contraseñas.
- Permitir a los usuarios agregar efectivo adicional a su cuenta.
- Permitir a los usuarios comprar o vender más acciones de acciones que ya poseen a través de `index` itself, sin tener que escribir los símbolos de las acciones manualmente.
- Requiere que las contraseñas de los usuarios tengan cierto número de letras, números y/o símbolos.
- Implementa otra función de alcance comparable.