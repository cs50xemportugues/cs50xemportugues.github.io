Pruebas
-------

Si deseas ver cómo se ve tu sitio mientras trabajas en él, puedes ejecutar `http-server`. Haz clic con el botón derecho o control en el primer enlace presentado por http-server, lo que debería abrir tu página web en una nueva pestaña. Luego deberías poder actualizar la pestaña que contiene tu página para ver tus últimos cambios.

Recuerda también que al abrir las Herramientas de Desarrollo en Google Chrome, puedes _simular_ visitar tu página en un dispositivo móvil dando clic en el ícono con forma de teléfono a la izquierda de **Elementos** en la ventana de herramientas de desarrollo, o, una vez que ya se ha abierto la pestaña de Herramientas de Desarrollo, escribiendo `Ctrl`+`Shift`+`M` en una PC o `Cmd`+`Shift`+`M` en una Mac, ¡en lugar de necesitar visitar tu sitio en un dispositivo móvil por separado!

Evaluación
----------

¡No hay `check50` para esta tarea! En cambio, la corrección de tu sitio se evaluará en función de si cumples con los requisitos de la especificación como se describe anteriormente, y si tu HTML está bien formado y es válido. Para asegurarte de que tus páginas lo estén, puedes usar este [Servicio de Validación de Marcado](https://validator.w3.org/#validate_by_input), copiando y pegando tu HTML directamente en el cuadro de texto provisto. ¡Asegúrate de eliminar cualquier advertencia o error sugerido por el validador antes de enviarlo!

Considera también:

*   si la estética de tu sitio es tal que es intuitivo y sencillo para el usuario navegar;
*   si tu CSS se ha desglosado en un archivo o archivos CSS separados; y
*   si has evitado la repetición y redundancia "cascando" propiedades de estilo desde etiquetas padres.

Lamentablemente, `style50` no es compatible con archivos HTML, por lo que es incumbencia tuya indentar y alinear tus etiquetas HTML con limpieza. También ten en cuenta que puedes crear un comentario HTML con:

    <!-- El comentario va aquí -->
    
pero no es tan imperativo comentar tu código HTML como cuando se comenta código en, por ejemplo, C o Python. También puedes comentar tu CSS, en archivos CSS, usando:

    /* Comentario va aquí */
    

Pistas
-----

Para guías bastante exhaustivas sobre los lenguajes presentados en este problema, revisa estos tutoriales:

*   [HTML](https://www.w3schools.com/html/)
*   [CSS](https://www.w3schools.com/css/)
*   [JavaScript](https://www.w3schools.com/js/)

Cómo enviar
-------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/homepage"