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