# Laboratorio 1: Crecimiento Poblacional

<div class="alert" data-alert="warning" role="alert"><p> Puedes colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante en cualquiera de estos grupos contribuya equitativamente con el laboratorio. </p></div>

Determina cuánto tiempo se tarda en alcanzar un tamaño específico de población.

    $ ./population 
    Tamaño inicial: 100 
    Tamaño final: 200 
    Años: 9 

## Trasfondo

Digamos que tenemos una población de `n` llamas. Cada año, `n / 3` nuevas llamas nacen, y `n / 4` llamas mueren.

Por ejemplo, si empezáramos con `n = 1200` llamas, entonces en el primer año, `1200 / 3 = 400` nuevas llamas nacerían y `1200 / 4 = 300` llamas morirían. Al finalizar ese año, tendríamos `1200 + 400 - 300 = 1300` llamas.

Para poner otro ejemplo, si comenzáramos con `n = 1000` llamas, al final del año, tendríamos `1000 / 3 = 333.33` nuevas llamas. No podemos tener una porción decimal de llama, así que truncamos el decimal para obtener `333` nuevas llamas nacidas. `1000 / 4 = 250` llamas morirán, por lo que terminaremos con un total de `1000 + 333 - 250 = 1083` llamas al final del año.

## Para Empezar

Recuerda que Visual Studio Code (también conocido como VS Code) es un popular "entorno de desarrollo integrado" (IDE) a través del cual puedes escribir código. Para que no tengas que descargar, instalar y configurar tu propia copia de VS Code, usaremos una versión basada en la nube que tiene todo lo que necesitarás ya preinstalado.

1. Inicia sesión en [code.cs50.io](https://code.cs50.io/) con tu cuenta de GitHub y sigue las instrucciones en pantalla para configurar tu propio "espacio de código" (codespace) para Visual Studio Code. Una vez que cargue tu espacio de código, verás que, por defecto, VS Code se divide en tres regiones. Hacia la parte superior de VS Code está tu "editor de texto", donde escribirás todos tus programas. Hacia la parte inferior hay una "ventana de terminal", una interfaz de línea de comandos (CLI) que te permite explorar los archivos y directorios (también conocidos como carpetas) de tu espacio de código, compilar código y ejecutar programas. Y a la izquierda está el "explorador de archivos", una interfaz gráfica de usuario (GUI) a través de la cual también puedes explorar los archivos y directorios de tu espacio de código.

2. Una vez que tu espacio de código cargue, cierra cualquier pestaña de **Bienvenida** que se haya abierto por defecto.
3. Inicia sesión en [submit.cs50.io](https://submit.cs50.io) con tu cuenta de GitHub y haz clic en **Authorize cs50** para activar `check50`.
4. Ejecuta el comando `update50` en la ventana de la terminal de tu espacio de código para asegurarte de que está actualizado y, si es necesario, haz clic en **Rebuild now**.

Una vez completado, comienza haciendo clic dentro de la ventana de tu terminal y luego ejecuta `cd` por sí solo. Verás que su "prompt" se parece al siguiente.

    $

Haz clic dentro de esa ventana de terminal y luego escribe

    mkdir population

seguido de Enter para crear un directorio llamado `population` en tu espacio de código. ¡Ten cuidado de no pasar por alto el espacio entre `mkdir` y `population`, o cualquier otro carácter!

De ahora en adelante, ejecutar (es decir, ejecutar) un comando significa escribirlo en una ventana de terminal y luego presionar Enter. Los comandos distinguen entre mayúsculas y minúsculas, así que asegúrate de no escribir en mayúscula cuando quieres minúscula, o viceversa.

Ahora ejecuta

    cd population
para moverte al (es decir, abrir) ese directorio. Tu "prompt" debería parecerse al siguiente:

    population/ $

Haz clic dentro de esa ventana de terminal y luego escribe

    wget https://cdn.cs50.net/2022/fall/labs/1/population.c

seguido de Enter para descargar un archivo de plantilla llamado` population.c` en tu espacio de código. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter! Si todo fue exitoso, deberías ejecutar

    ls

y se verá un archivo llamado `population.c`. Ejecutar `code population.c` abrirá el archivo donde escribirás tu código para este laboratorio. Si no es así, retrocede y trata de determinar dónde te equivocaste.

## Detalles de Implementación

Completa la implementación de `population.c`, de modo que calcule el número de años necesarios para que la población crezca desde el tamaño inicial hasta el tamaño final.

- Tu programa debería primero pedirle al usuario un tamaño de población inicial.
  - Si el usuario ingresa un número menor de 9 (el tamaño de población mínimo permitido), deberá volver a preguntarse por un tamaño de población inicial hasta que ingrese un número mayor o igual a 9. (¡Si comenzamos con menos de 9 llamas, la población de llamas pronto se volverá estancada!)
- Tu programa debería solicitarle al usuario un tamaño de población final.
  - Si el usuario ingresa un número menor que el tamaño de población inicial, deberá volver a preguntarse por un tamaño de población final hasta que ingrese un número mayor o igual al tamaño de población inicial. (¡Después de todo, queremos que la población de llamas crezca!)
- Tu programa debería luego calcular la cantidad (entera) de años necesarios para que la población alcance al menos el valor final.
- Finalmente, el programa debería imprimir la cantidad de años necesarios para que la población de llamas alcance ese tamaño final, imprimiendo en la terminal `Años: n`, donde `n` es el número de años.

### Tutorial

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/dZmtRHHUB1M"></iframe>

### Consejos

- Si desea volver a solicitar repetidamente al usuario el valor de una variable hasta que se cumpla alguna condición, es posible que desee utilizar un bucle `do... while`. Por ejemplo, recuerde el siguiente código de la conferencia, que solicita al usuario repetidamente hasta que ingresan un número entero positivo. <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">n</span><span class="p">;</span>
  <span class="k">do</span>
  <span class="p">{</span>
  <span class="n">n</span> <span class="o">=</span> <span class="n">get_int</span><span class="p">(</span><span class="s">"Entero positivo: "</span><span class="p">);</span>
  <span class="p">}</span>
  <span class="k">while</span> <span class="p">(</span><span class="n">n</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">);</span>
  </code></pre></div> </div>
  ¿Cómo podría adaptar este código para asegurar un tamaño de inicio de al menos 9 y un tamaño final de al menos el tamaño de inicio?

* Para declarar una nueva variable, asegúrese de especificar su tipo de datos, un nombre para la variable y (opcionalmente) cuál debería ser su valor inicial.
  - Por ejemplo, es posible que desee crear una variable para realizar un seguimiento de cuántos años han pasado.
* ¡Otro bucle podría ayudar a calcular cuántos años tardará la población en alcanzar el tamaño final! Dentro del bucle, probablemente desee actualizar el tamaño de la población de acuerdo con la fórmula en el Antecedente y actualizar la cantidad de años que han pasado.
* Para imprimir un entero `n` en la terminal, recuerde que puede usar una línea de código como <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code> <span class="n">printf</span><span class="p">(</span><span class="s">"El número es %i</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">n</span><span class="p">);</span>
  </code></pre></div> </div>
  para especificar que la variable `n` debe llenar el marcador de posición `%i`.

### Cómo probar su código

Su programa debe comportarse de acuerdo con estos ejemplos a continuación.

    $ ./population
    Tamaño de inicio: 1200
    Tamaño final: 1300
    Años: 1


    $ ./population
    Tamaño de inicio: -5
    Tamaño de inicio: 3
    Tamaño de inicio: 9
    Tamaño final: 5
    Tamaño final: 18
    Años: 8


    $ ./population
    Tamaño de inicio: 20
    Tamaño final: 1
    Tamaño final: 10
    Tamaño final: 100
    Años: 20


    $ ./population
    Tamaño de inicio: 100
    Tamaño final: 1000000
    Años: 115

<details><summary>¿No estás seguro de cómo resolverlo?</summary><iframe allow="acelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/2CcqQnLbGOE"></iframe></details>

Ejecute lo siguiente para evaluar la corrección de su código utilizando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50 / labs / 2023 / x / population

Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`.

    style50 population.c

## Cómo enviar

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50 / labs / 2023 / x / population

