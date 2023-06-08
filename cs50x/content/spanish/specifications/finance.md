# Finanzas de C$50

<div class = "alert" data-alert = "warning" role = "alert"> <p> El código de distribución de este conjunto de problemas ha cambiado recientemente. Si descargó el código de distribución antes del<a data-local="2022-12-01T00:00:00+00:00" href="https://time.cs50.io/20221201T000000Z"> 2022-12-01T00:00:00+00:00 </a>, ejecute los siguientes comandos del terminal en su directorio de <code class = "language-plaintext highlighter-rouge "> finanzas </code> para descargar la última versión del código de distribución.</p>

<div class = "language-plaintext highlighter-rouge"> <div class = "highlight"> <pre class = "highlight"> <code> $ rm helpers.py
$ wget https://cdn.cs50.net/2022/fall/psets/9/finance/helpers.py

</code> </pre> </div> </div> </div>


Implementa un sitio web a través del cual los usuarios puedan "comprar" y "vender" acciones, como en la imagen a continuación.

![Finanzas de C$50](https://cs50.harvard.edu/x/2023/psets/9/finance/finance.png)

## Antecedentes

Si no estás seguro de lo que significa comprar y vender acciones (es decir, acciones de una empresa), dirígete [aquí](https://www.investopedia.com/articles/basics/06/invest1000.asp) para un tutorial.

Estás a punto de implementar C$50 Finanzas, una aplicación web a través de la cual puedes administrar carteras de acciones. No solo te permitirá verificar los precios reales de las acciones y el valor de las carteras, sino que también te permitirá "comprar" (bueno, "comprar") y "vender" (bueno, "vender") acciones mediante la consulta de [IEX](https://iextrading.com/developer/) por los precios de las acciones.

De hecho, IEX te permite descargar cotizaciones de acciones a través de su API (interfaz de programación de aplicaciones) utilizando URL como `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Observa cómo el símbolo de Netflix (NFLX) está incrustado en esta URL; así es como IEX sabe a quién devolver los datos. Ese enlace no devolverá realmente ningún dato porque IEX requiere que uses una clave de API (más sobre eso en un momento), pero si lo hiciera, verías una respuesta en formato JSON (Notación de Objeto de JavaScript) como esta:

    {
      "avgTotalVolume": 15918066,
      "calculationPrice": "close",
      "change": -8.27,
      "changePercent": -0.03074,
      "close": 260.79,
      "closeSource": "official",
      "closeTime": 1667592000924,
      "companyName": "Netflix Inc.",
      "currency": "USD",
      "delayedPrice": 260.81,
      "delayedPriceTime": 1667591988947,
      "extendedChange": 0.21,
      "extendedChangePercent": 0.00081,
      "extendedPrice": 261,
      "extendedPriceTime": 1667606392772,
      "high": 274.97,
      "highSource": "15 minute delayed price",
      "highTime": 1667592000831,
      "iexAskPrice": None,
      "iexAskSize": None,
      "iexBidPrice": None,
      "iexBidSize": None,
      "iexClose": 260.85,
      "iexCloseTime": 1667591999754,
      "iexLastUpdated": None,
      "iexMarketPercent": None,
      "iexOpen": 271.67,
      "iexOpenTime": 1667568602197,
      "iexRealtimePrice": None,
      "iexRealtimeSize": None,
      "iexVolume": None,
      "lastTradeTime": 1667591999820,
      "latestPrice": 260.79,
      "latestSource": "Close",
      "latestTime": "November 4, 2022",
      "latestUpdate": 1667592000924,
      "latestVolume": 11124694,
      "low": 255.32,
      "lowSource": "15 minute delayed price",
      "lowTime": 1667584872696,
      "marketCap": 115215720136,
      "oddLotDelayedPrice": 260.81,
      "oddLotDelayedPriceTime": 1667591988947,
      "open": 271.9,
      "openTime": 1667568601785,
      "openSource": "official",
      "peRatio": 23.39,
      "previousClose": 269.06,
      "previousVolume": 7057350,
      "primaryExchange": "NASDAQ",
      "symbol": "NFLX",
      "volume": 11124694,
      "week52High": 700.99,
      "week52Low": 162.71,
      "ytdChange": -0.5978504176349512,
      "isUSMarketOpen": False
    }

Observa cómo, entre las llaves, hay una lista de pares clave-valor separados por comas, con dos puntos separando cada clave de su valor.

¡Ahora centrémonos en obtener el código de distribución de este conjunto de problemas!

## Empezando

Inicia sesión en [code.cs50.io](https://code.cs50.io/), haz clic en la ventana del terminal y ejecuta `cd` por sí solo. Deberías ver que el prompt de tu ventana del terminal se asemeja a lo siguiente:

    $

A continuación, ejecuta:

    wget https://cdn.cs50.net/2022/fall/psets/9/finance.zip

para descargar un archivo ZIP llamado `finance.zip` en tu space de códigos.

Luego ejecuta

    unzip finance.zip

para crear una carpeta llamada `finance`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm finance.zip

y luego responder con "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

     cd finance

seguido de Enter para moverte dentro (es decir, abrir) de ese directorio. Tu prompt debe mostrar ahora lo siguiente:

    finance/ $

Ejecuta `ls` por sí solo y deberías ver algunos archivos y carpetas:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Si te encuentras con algún problema, sigue los mismos pasos de nuevo y trata de determinar dónde te equivocaste.

### Configuración

Antes de comenzar esta tarea, necesitamos registrar una clave API para poder consultar los datos de IEX. Para ello, sigue estos pasos:

- Visita [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
- Selecciona el tipo de cuenta "Individual", luego ingresa tu nombre, dirección de correo electrónico y una contraseña, y haz clic en "Crear cuenta".
- Una vez registrado, desplázate hacia abajo hasta "Comenzar gratis" y haz clic en "Seleccionar Plan de Inicio" para elegir el plan gratuito. _Ten en cuenta que este plan solo funciona durante 30 días a partir del día en que creaste tu cuenta._ ¡Ten esto en cuenta si podrías planear usar esta misma API para tu proyecto final!
- Una vez que hayas confirmado tu cuenta mediante un correo electrónico de confirmación, visita [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
- Copia la clave que aparece bajo la columna _Token_ (debería comenzar con `pk_`).
- En tu ventana del terminal, ejecuta:

<pre>
$ export API_KEY=value
</pre>

donde `value` es el valor pegado (sin ningún espacio inmediatamente antes o después del `=`). También puedes pegar ese valor en un documento de texto en algún lugar, en caso de que lo necesites de nuevo más adelante.

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

## Tutorial

<div class = "ratio ratio-16x9" data-video = ""> <iframe allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen = "" class = "border" data-video = "" src = "https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding = 0 & rel = 0 & showinfo = 0"> </iframe> </div>

## Pruebas

Asegúrate de probar manualmente tu aplicación web, como por ejemplo

- registrando un nuevo usuario y verificando que su página de cartera cargue con la información correcta,
- solicitar una cotización utilizando un símbolo de stock válido,
- comprar una acción varias veces, verificando que la cartera muestre los totales correctos,
- vender todas o algunas de las acciones, volviendo a verificar la cartera, y 
- verificando que tu página de historial muestre todas las transacciones para el usuario registrado.

También prueba algunos usos inesperados, como por ejemplo

- ingresar cadenas alfabéticas en los formularios cuando solo se esperan números,
- ingresar cero o números negativos en los formularios cuando solo se esperan números positivos,
- ingresar valores de punto flotante en los formularios cuando solo se esperan números enteros,
- intentar gastar más dinero del que tiene el usuario,
- intentar vender más acciones de las que tiene el usuario,
- ingresar un símbolo de stock inválido, y
- incluyendo caracteres potencialmente peligrosos como `'` y `;` en consultas de SQL.

Una vez satisfecho, para probar tu código con `check50`, ejecuta lo siguiente:

    check50 cs50/problems/2023/x/finance

<div class="alert" data-alert="warning" role="alert"><p>Ten en cuenta que <code class="language-plaintext highlighter-rouge">check50</code> probará todo el programa en su conjunto. Si lo ejecutas <strong>antes</strong> de completar todas las funciones requeridas, puede informar errores en funciones que en realidad son correctas pero dependen de otras funciones. </p> </div>

Ejecuta lo siguiente para evaluar el estilo de tus archivos de Python usando `style50`.

    style50 *. py

## Solución del personal

Eres libre de estilizar tu aplicación como desees, pero aquí te mostramos cómo luce la solución del personal!

[https://finance.cs50.net/](https://finance.cs50.net/)

Siéntete libre de registrarte para obtener una cuenta y jugar con ella. **No** utilices una contraseña que uses en otros sitios.

Es **razonable** ver el HTML y CSS del personal.

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

