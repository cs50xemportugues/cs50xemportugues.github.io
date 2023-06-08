# Laboratorio 9: Cumpleaños

<div class="alert" data-alert="warning" role="alert"><p>Puedes colaborar con uno o dos compañeros en este laboratorio, aunque se espera que todos los estudiantes de dichos grupos contribuyan por igual al laboratorio.</p></div>

Crea una aplicación web para hacer un seguimiento de los cumpleaños de tus amigos.

![captura de pantalla del sitio web de cumpleaños](https://cs50.harvard.edu/x/2023/labs/9/birthdays.png)

## Para Empezar


<div class="alert" data-alert="primary" role="alert"><p>¿Comenzaste CS50x en 2021 o antes y necesitas migrar tu trabajo de CS50 IDE al nuevo VS Code codespace? ¡Asegúrate de consultar nuestras instrucciones sobre cómo <a href="../../new/">migrar</a> tus archivos!</p></div>

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic en tu ventana de terminal y luego ejecuta `cd` por sí solo. Deberías ver que su "prompt" se asemeja al siguiente.

    $

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/labs/9/birthdays.zip

seguido de Enter para descargar un archivo ZIP llamado `birthdays.zip` en tu codespace. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter!

Ahora ejecuta

    unzip birthdays.zip

para crear una carpeta llamada `birthdays`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm birthdays.zip

y responde con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd birthdays

seguido de Enter para moverte (es decir, abrir) a ese directorio. Su prompt debería parecerse al siguiente.

    birthdays/$

Si todo se ha realizado correctamente, debes ejecutar

    ls

y deberías ver los siguientes archivos y carpetas:

    app.py  birthdays.db  static/  templates/

Si tienes algún problema, sigue estos mismos pasos nuevamente y determina dónde te equivocaste.

## Comprendiendo

En `app.py`, encontrarás el inicio de una aplicación web Flask. La aplicación tiene una ruta (`/`) que acepta tanto solicitudes `POST` (después del `if`) como solicitudes `GET` (después del `else`). Actualmente, cuando se solicita la ruta `/` a través de `GET`, se representa la plantilla `index.html`. Cuando se solicita la ruta `/` a través de `POST`, se redirige al usuario de vuelta a `/` a través de `GET`.

`birthdays.db` es una base de datos SQLite con una tabla, `birthdays`, que tiene cuatro columnas: `id`, `name`, `month` y `day`. Hay algunas filas ya presentes en esta tabla, aunque en última instancia, ¡su aplicación web admitirá la capacidad de insertar filas en esta tabla!

En el directorio `static`, hay un archivo `styles.css` que contiene el código CSS para esta aplicación web. No es necesario que edites este archivo, ¡aunque eres bienvenido a hacerlo si lo deseas!

En el directorio `templates`, hay un archivo `index.html` que se representará cuando el usuario vea su aplicación web.

## Detalles de implementación

Complete la implementación de una aplicación web para que los usuarios puedan almacenar y hacer un seguimiento de los cumpleaños.

- Cuando se solicita la ruta `/` a través de `GET`, su aplicación web debe mostrar, en una tabla, a todas las personas en su base de datos junto con sus cumpleaños.
  - Primero, en `app.py`, agrega lógica en la manipulación de tu solicitud GET para consultar la base de datos `birthdays.db` para todos los cumpleaños. Pasa todos esos datos a tu plantilla `index.html`.
  - Luego, en `index.html`, agrega lógica para representar cada cumpleaños como una fila en la tabla. Cada fila debe tener dos columnas: una columna para el nombre de la persona y otra columna para la fecha de nacimiento de la persona.
- Cuando se solicita la ruta `/` a través de `POST`, su aplicación web debe agregar un nuevo cumpleaños a su base de datos y luego volver a representar la página de índice.
  - Primero, en `index.html`, agrega un formulario HTML. El formulario debe permitir a los usuarios escribir un nombre, un mes de cumpleaños y un día de cumpleaños. Asegúrate de que el formulario se envíe a `/` (su "action") con un método de `post`.
  - Luego, en `app.py`, agrega lógica en la manipulación de tu solicitud `POST` para `INSERTAR` una nueva fila en la tabla `birthdays` en función de los datos suministrados por el usuario.

Opcionalmente, también puedes:

- Agregar la capacidad de eliminar y/o editar entradas de cumpleaños.
- Agregar otras características adicionales que desees.

### Tutorial

<div class="alert" data-alert="primary" role="alert"><p>Este video fue grabado cuando el curso todavía usaba CS50 IDE para escribir código. ¡Aunque la interfaz puede verse diferente desde tu codespace, el comportamiento de los dos entornos debería ser en gran parte similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/HXwvj8x1Fcs"></iframe>


### Pistas

- Recuerda que puedes llamar a `db.execute` para ejecutar consultas SQL dentro de `app.py`.
  - Si llamas a `db.execute` para ejecutar una consulta `SELECT`, recuerda que la función te devolverá una lista de diccionarios, donde cada diccionario representa una fila devuelta por tu consulta.
- Es probable que te resulte útil pasar datos adicionales a `render_template()` en tu función `index` para que puedas acceder a los datos de cumpleaños dentro de tu plantilla `index.html`.
- Recuerda que la etiqueta `tr` se puede usar para crear una fila de tabla y la etiqueta `td` se puede utilizar para crear una celda de datos de tabla.
- Recuerda que, con Jinja, puedes crear un [`for` loop](https://jinja.palletsprojects.com/en/2.11.x/templates/#for) dentro de tu archivo `index.html`.
- En `app.py`, puedes obtener los datos `POST`eados por el usuario del formulario al enviar `request.form.get(field)` donde `field` es una cadena que representa el atributo `name` de una entrada de tu formulario.
  - Por ejemplo, si en `index.html`, tuvieras una entrada `<input name="foo" type="text">`, podrías usar `request.form.get("foo")` en `app.py` para extraer la entrada del usuario.

<details><summary>¿No estás seguro de cómo solucionarlo?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/lVwv4o8vmvI"></iframe></details>


### Pruebas

¡No hay `check50` para este laboratorio! Pero asegúrate de probar tu aplicación web agregando algunos cumpleaños y asegurándote de que los datos aparezcan en tu tabla como se espera.

Ejecuta `flask run` en tu terminal mientras estás en tu directorio `birthdays` para iniciar un servidor web que sirva tu aplicación Flask.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/labs/2023/x/birthdays