# Hola

## Empezando

Recuerda que Visual Studio Code (también conocido como VS Code) es un popular "entorno de desarrollo integrado" (IDE) a través del cual puedes escribir código. Para que no tengas que descargar, instalar y configurar tu propia versión de VS Code, en su lugar usaremos una versión basada en la nube que tiene todo lo que necesitas preinstalado.

Inicia sesión en [code.cs50.io] (https://code.cs50.io/) usando tu cuenta de GitHub. Una vez que se cargue su "espacio de código", debería ver que, por defecto, VS Code se divide en tres regiones. Hacia la parte superior de VS Code está tu "editor de texto", donde escribirás todos tus programas. Hacia la parte inferior hay una "ventana de terminal", una interfaz de línea de comandos (CLI) que te permite explorar los archivos y directorios (también conocidos como carpetas) de tu espacio de código, compilar código y ejecutar programas. Y a la izquierda se encuentra tu "explorador de archivos", una interfaz gráfica de usuario (GUI) a través de la cual también puedes explorar los archivos y directorios de tu espacio de código.

Comienza haciendo clic dentro de tu ventana de terminal y luego ejecuta `cd` por sí solo. Deberías encontrar que su "prompt" se parece a continuación.

    $

Haz clic dentro de esa ventana de terminal y luego escribe

    mkdir hello

seguido de Enter para crear un directorio llamado `hello` en tu espacio de código. ¡Ten cuidado de no pasar por alto el espacio entre `mkdir` y `hello` o cualquier otro carácter!

De aquí en adelante, ejecutar (es decir, ejecutar) un comando significa escribirlo en una ventana de terminal y luego presionar Enter. Los comandos son "sensibles a mayúsculas y minúsculas", así que asegúrate de no escribir en mayúsculas cuando quieras minúsculas o viceversa.

Ahora, ejecuta

    cd hello

para moverte a ti mismo dentro (es decir, abrir) ese directorio. Su prompt ahora debería parecerse al siguiente.

    hello/ $

Si no es así, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.

¿Escribimos tu primer programa? Ejecuta

    code hello.c

para crear un nuevo archivo llamado `hello.c`, que debería abrirse automáticamente en el editor de texto de tu espacio de código. Tan pronto como guardes el archivo con el comando-S (en macOS) o control-S (en Windows), también debería aparecer en el explorador de archivos de tu espacio de código.

Procede a escribir tu primer programa escribiendo precisamente estas líneas en `hello.c`:

    #include <stdio.h>

    int main(void)
    {
        printf("hello, world\n");
    }

Observa cómo VS Code agrega "destacado de sintaxis" (es decir, color) a medida que escribes, aunque la elección de colores de VS Code podría diferir de este conjunto de problemas. Esos colores no se guardan realmente dentro del archivo en sí; solo los agrega VS Code para hacer resaltar cierta sintaxis. Si no hubieras guardado el archivo como `hello.c` desde el principio, VS Code no sabría (según la extensión del nombre de archivo) que estás escribiendo código C, en cuyo caso esos colores estarían ausentes.

## Listado de archivos

A continuación, en tu ventana de terminal, inmediatamente a la derecha del prompt (`hello/ $`), ejecuta

    ls

¿Solo ves `hello.c`? Eso se debe a que acabas de listar los archivos en tu carpeta `hello`. En particular, ejecutaste un comando llamado `ls`, que es un atajo para "lista". (Es un comando tan frecuentemente utilizado que sus autores lo llamaron simplemente `ls` para ahorrar pulsaciones de teclas). ¿Tiene sentido?

## Compilando programas

Ahora, antes de poder ejecutar el programa `hello.c`, recuerda que debemos _compilarlo_ con un _compilador_, traduciéndolo del _código fuente_ al _código de máquina_ (es decir, ceros y unos). Ejecuta el siguiente comando para hacer justamente eso.

    make hello

Y luego ejecuta este otro otra vez.

    ls

¿Esta vez ves no solo `hello.c` sino también `hello` en la lista? Ahora has traducido el código fuente en `hello.c` a código de máquina en `hello`.

Ahora ejecuta el propio programa ejecutando lo siguiente.

    ./hello

¡Hola mundo!

## Obtener la entrada del usuario

Basta decir que, independientemente de cómo compile o ejecute este programa, solo imprime `hello, world`. Personalicémoslo un poco, como hicimos en clase.

Modifica este programa de tal manera que primero le pida al usuario su nombre y luego imprima `hello, tal-y-cual`, donde `tal-y-cual` es su nombre real.

Como antes, asegúrate de compilar tu programa con:

    make hello

Y asegúrate de ejecutar tu programa, probándolo varias veces con diferentes entradas, con:

    ./hello

### Paso a paso

¡Aquí hay un "paso a paso" (es decir, una visita guiada) de este problema, si desea una descripción general de lo que debe hacer también!

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/wSk1KSDUEYA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Consejos

#### ¿No recuerda cómo solicitarle al usuario su nombre?

Recuerda que puedes usar `get_string` de la siguiente manera, almacenando su _valor de retorno_ en una variable llamada `name` de tipo `string`.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">string</span> <span class="n">name</span> <span class="o">=</span> <span class="n">get_string</span><span class="p">(</span><span class="s">"What's your name? "</span><span class="p">);</span>
</code></pre></div></div>

#### ¿No recuerda cómo formatear una cadena?

¿No recuerdas cómo unir (es decir, concatenar) el nombre del usuario con un saludo? Recuerda que puedes usar `printf` no solo para imprimir sino para formatear una cadena (de ahí, la `f` en` printf`), como en lo siguiente, donde `name` es una `string`.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">printf</span><span class="p">(</span><span class="s">"hello, %s</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">name</span><span class="p">);</span>
</code></pre></div></div>

#### ¿Uso de un identificador no declarado?

¿Ves lo siguiente, quizás arriba de otros errores?

    error: use of undeclared identifier 'string'; did you mean 'stdin'?

Recuerda que para usar `get_string`, debes incluir `cs50.h` (en el que `get_string` está _declarado_) en la parte superior de un archivo, como con:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include</span> <span class="cpf">&lt;cs50.h&gt;</span><span class="cp">
</span></code></pre></div></div>

### Cómo probar tu código

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`, un programa de línea de comandos que imprimirá caras felices cuando tu código pase las pruebas automatizadas de CS50 y caras tristes cuando no lo haga. ¡Pero asegúrate de compilar y probarlo tú mismo también!

    check50 cs50/problems/2023/x/hello

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`, un programa de línea de comandos que imprimirá adiciones (en verde) y eliminaciones (en rojo) que deberías hacer en tu programa para mejorar su estilo. Si tienes problemas para ver esos colores, `style50` admite otros [modos] (https://cs50.readthedocs.io/style50/) también!

    style50 hello.c

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/hello