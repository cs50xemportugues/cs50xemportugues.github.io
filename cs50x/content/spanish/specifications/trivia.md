Lab 8: Trivia
=============

<div class="alert" data-alert="warning" role="alert"><p>Está permitido colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante de dicho grupo contribuya igualmente al laboratorio.</p></div>


Escriba una página web que permita a los usuarios responder preguntas de trivia.

![screenshot of trivia questions](https://cs50.harvard.edu/x/2023/labs/8/questions.png)

Antes de Empezar
---------------

<div class="alert" data-alert="primary" role="alert"><p>¿Comenzó CS50x en 2021 o anteriormente y necesita migrar su trabajo de CS50 IDE al nuevo codespace de VS Code? Asegúrese de revisar nuestras instrucciones sobre cómo <a href="../../new/">migrar</a> sus archivos!</p></div>

Abra [VS Code](https://code.cs50.io/).

Comience haciendo clic dentro de su ventana de terminal y luego ejecute `cd` por sí solo. Debería encontrar que su "prompt" se asemeja a lo siguiente.

    $
    

Haga clic dentro de esa ventana de terminal y luego ejecute

    wget https://cdn.cs50.net/2022/fall/labs/8/trivia.zip
    

seguido por Enter para descargar un archivo ZIP llamado `trivia.zip` en su codespace. ¡Asegúrese de no dejar de lado el espacio entre `wget` y la URL siguiente, o cualquier otro carácter!

Ahora ejecute

    unzip trivia.zip
    

para crear una carpeta llamada `trivia`. Ya no necesita el archivo ZIP, así que puede ejecutar

    rm trivia.zip
    

y responda con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargó.

Ahora escriba

    cd trivia
    

seguido por Enter para ingresar (es decir, abrir) ese directorio. Su "prompt" ahora debería parecerse a lo siguiente.

    trivia/ $
    

Si todo salió bien, debería ejecutar

    ls
    

y debería ver un archivo `index.html` y un archivo `styles.css`.

Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.

Detalles de Implementación
----------------------

Diseñe una página web usando HTML, CSS, y JavaScript para permitir a los usuarios responder preguntas de trivia.

*   En `index.html`, agregue debajo de "Parte 1" una pregunta de trivia a elección múltiple con HTML.
    *   Debería usar una etiqueta `h3` para el texto de su pregunta.
    *   Debería tener un `button` para cada una de las posibles opciones de respuesta. Debería haber al menos tres opciones de respuesta, de las cuales exactamente una debería ser correcta.
*   Usando JavaScript, agregue lógica para que los botones cambien de color cuando un usuario haga clic en ellos.
    *   Si un usuario hace clic en un botón con una respuesta incorrecta, el botón debería ponerse rojo y debajo de la pregunta debería aparecer un texto que diga "Incorrecto".
    *   Si un usuario hace clic en un botón con la respuesta correcta, el botón debería ponerse verde y debajo de la pregunta debería aparecer un texto que diga "¡Correcto!".
*   En `index.html`, agregue debajo de "Parte 2" una pregunta de respuesta libre basada en texto de su elección con HTML.
    *   Debería usar una etiqueta `h3` para el texto de su pregunta.
    *   Debería usar un campo de `input` para permitir que el usuario escriba una respuesta.
    *   Debería utilizar un `button` para permitir que el usuario confirme su respuesta.
*   Usando JavaScript, agregue lógica para que el campo de texto cambie de color cuando un usuario confirma su respuesta.
    *   Si el usuario escribe una respuesta incorrecta y presiona el botón de confirmación, el campo de texto debería volverse rojo y debajo de la pregunta debería aparecer un texto que diga "Incorrecto".
    *   Si el usuario escribe la respuesta correcta y presiona el botón de confirmación, el campo de entrada debería volverse verde y debajo de la pregunta debería aparecer un texto que diga "¡Correcto!".

Opcionalmente, también puede:

*   Editar `styles.css` para cambiar el CSS de su página web.
*   ¡Agregar preguntas de trivia adicionales a su cuestionario de trivia si lo desea!

### Tutorial

<div class="alert" data-alert="primary" role="alert"><p>Este video fue grabado cuando el curso todavía usaba CS50 IDE para escribir código. Aunque la interfaz puede verse diferente a su codespace, ¡el comportamiento de los dos entornos debería ser en gran medida similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/WGd0Jx7rxUo"></iframe>


### Concejos

*   Use [`document.querySelector`](https://developer.mozilla.org/es/docs/Web/API/Document/querySelector) para buscar un elemento HTML único.
*   Use [`document.querySelectorAll`](https://developer.mozilla.org/es/docs/Web/API/Document/querySelectorAll) para buscar varios elementos HTML que coinciden con una consulta. La función devuelve una matriz con todos los elementos coincidentes.


<details><summary>¿No estás seguro de cómo resolverlo?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/FLlI7rSSV_M"></iframe></details>


### Probando

No hay `check50` para este laboratorio, ¡ya que las implementaciones variarán según sus preguntas! Pero asegúrese de probar tanto las respuestas incorrectas como las correctas para cada una de sus preguntas para asegurarse de que su página web responda adecuadamente.

Ejecute `http-server` en su terminal mientras se encuentra en su directorio `lab8` para iniciar un servidor web que sirva su página web.

Cómo Entregar
-------------

En su terminal, ejecute lo siguiente para entregar su trabajo.

    submit50 cs50/labs/2023/x/trivia"