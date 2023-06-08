Página principal
========

Construye una página principal sencilla utilizando HTML, CSS y JavaScript.

Antecedentes
----------

Internet ha permitido cosas increíbles: podemos usar un motor de búsqueda para investigar absolutamente cualquier cosa, comunicarnos con amigos y familiares de todo el mundo, jugar juegos, tomar cursos y mucho más. Pero resulta que casi todas las páginas que visitamos se construyen con tres lenguajes principales, cada uno de los cuales sirve para un propósito ligeramente diferente:

1.  HTML o _HyperText Markup Language_, que se utiliza para describir el contenido de los sitios web;
2.  CSS, _Cascading Style Sheets_, que se utiliza para describir la estética de los sitios web; y
3.  JavaScript, que se utiliza para hacer que los sitios web sean interactivos y dinámicos.

Crea una página principal sencilla que te presente, que hable de tu pasatiempo o actividad extracurricular favorita, o cualquier otra cosa que te resulte interesante.

Cómo comenzar
---------------

Inicia sesión en [code.cs50.io](https://code.cs50.io/), haz clic en la ventana del terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

     $
    

A continuación, ejecuta:

    wget https://cdn.cs50.net/2022/fall/psets/8/homepage.zip
    

para descargar un archivo ZIP llamado `homepage.zip` en tu espacio de trabajo.

Luego ejecuta:

    unzip homepage.zip
    

para crear una carpeta llamada `homepage`. Ya no necesitas el archivo ZIP, así que ejecuta:

    rm homepage.zip
    

y responde con "y" seguido de Enter para eliminar el archivo ZIP que descargaste.

Ahora escribe:

    cd homepage
    

seguido de Enter para moverte (es decir, abrir) a ese directorio. Tu indicador ahora debe parecerse a este:

    homepage/ $
    

Ejecuta `ls` por sí solo y deberías ver algunos archivos:

    index.html  styles.css
    

Si tienes algún problema, repite los mismos pasos y ve si puedes determinar dónde te equivocaste. Puedes iniciar inmediatamente un servidor para ver tu sitio ejecutando

    http-server
    

en la ventana terminal. Luego haz clic en la opción "Command-click" (si usas un Mac) o "Control-click" (si usas un PC) en el primer enlace que aparece:

    http-server running on LINK
    
  
donde "LINK" es la dirección de tu servidor.

Especificaciones
---------------

Implementa en tu directorio `homepage` un sitio web que debe cumplir lo siguiente:

*   Debe contener al menos cuatro páginas diferentes `.html`, una de las cuales es `index.html` (la página principal de tu sitio web), y debería ser posible ir desde cualquier página de tu sitio web a cualquier otra página siguiendo uno o más enlaces.
*   Utiliza al menos diez (10) etiquetas HTML distintas además de `<html>`, `<head>`, `<body>` y `<title>`. ¡Usar alguna etiqueta (por ejemplo, `<p>`) varias veces cuenta como sólo uno (1) de esos diez!
*   Integra una o más funciones de Bootstrap en tu sitio. Bootstrap es una librería popular (que trae muchas clases de CSS y más) mediante la cual puedes embellecer tu sitio. Consulta la [documentación de Bootstrap](https://getbootstrap.com/docs/5.2/) para comenzar. En particular, es posible que te interese algunos de los [componentes de Bootstrap](https://getbootstrap.com/docs/5.2/components/). Para agregar Bootstrap a tu sitio, es suficiente con incluir <div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">href=</span><span class="s">"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"</span> <span class="na">integrity=</span><span class="s">"sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;</span>
<span class="nt">&lt;script </span><span class="na">src=</span><span class="s">"https://code.jquery.com/jquery-3.5.1.slim.min.js"</span> <span class="na">integrity=</span><span class="s">"sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;&lt;/script&gt;</span>
<span class="nt">&lt;script </span><span class="na">src=</span><span class="s">"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"</span> <span class="na">integrity=</span><span class="s">"sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;&lt;/script&gt;</span>
</code></pre></div></div> en el `<head>` de tus páginas, debajo del cual también puedes incluir <div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;link</span> <span class="na">href=</span><span class="s">"styles.css"</span> <span class="na">rel=</span><span class="s">"stylesheet"</span><span class="nt">&gt;</span>
</code></pre></div>    </div>

    para enlazar tu propio CSS.
    
*   Debes tener al menos un archivo de hoja de estilos de tu propia creación, `styles.css`, que use al menos cinco (5) selectores CSS distintos (por ejemplo, etiqueta (`ejemplo`), clase (`.ejemplo`) o ID (`#ejemplo`)), y dentro del cual uses en total al menos cinco (5) propiedades CSS distintas, como `font-size` o `margin`; y
*   Integre una o más características de JavaScript en su sitio para hacerlo más interactivo. Por ejemplo, puedes usar JavaScript para agregar alertas, tener un efecto a intervalos recurrentes, o agregar interactividad a botones, menús desplegables o formularios. ¡Siéntete libre de ser creativo!
*   Asegúrate de que tu sitio se vea bien tanto en los navegadores de dispositivos móviles como en los de portátiles y equipos de escritorio.

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

