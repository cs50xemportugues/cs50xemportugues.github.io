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