Corrector Ortográfico
=====================

<div class="alert" data-alert="danger" role="alert"><p><strong>¡Asegúrate de leer esta especificación en su totalidad antes de comenzar, para que sepas qué hacer y cómo hacerlo!</strong></p></div>

En este problema, vas a implementar un programa que corrija la ortografía de un archivo usando una tabla hash, similar a esto, a través del siguiente comando.

    $ ./speller texts/lalaland.txt
    PALABRAS MAL ESCRITAS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    PALABRAS MAL ESCRITAS:
    PALABRAS EN EL DICCIONARIO:
    PALABRAS EN TEXTO:
    TIEMPO EN CARGAR:
    TIEMPO EN COMPROBAR:
    TIEMPO EN DIMENSIONAR:
    TIEMPO EN DESCARGAR:
    TIEMPO EN TOTAL:
    

Comencemos
-----------

Inicia sesión en [code.cs50.io](https://code.cs50.io/), haz clic en la ventana de tu terminal y ejecuta `cd`. Deberías ver que el resultado en tu terminal es el siguiente:

    $
    

A continuación, ejecuta

    wget https://cdn.cs50.net/2022/fall/psets/5/speller.zip
    

para descargar un archivo ZIP llamado `speller.zip` en tu espacio de trabajo.

Después, ejecuta 

    unzip speller.zip
    

para crear una carpeta llamada `speller`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm speller.zip
    

y luego "y" seguido de "Enter" para eliminar el archivo ZIP que descargaste.

Ahora escribe 

    cd speller
    

seguido de "Enter" para ingresar (es decir, abrir) esa carpeta. Tu terminal debería ahora ser similar a lo siguiente:

    speller/ $
    

Ejecuta `ls` por si mismo, y deberías ver algunos archivos y carpetas:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
    

Si tienes algún problema, sigue estos mismos pasos nuevamente y determina en qué punto te equivocaste.

Distribución 
------------

### Comprensión 

Teóricamente, con una entrada de tamaño _n_, un algoritmo con un tiempo de ejecución de _n_ es "asintóticamente equivalente", en términos de _O_, a un algoritmo con un tiempo de ejecución de _2n_. De hecho, al describir el tiempo de ejecución de un algoritmo, generalmente nos enfocamos en el término dominante (es decir, el más impactante) (es decir, _n_ en este caso, ya que _n_ podría ser mucho más grande que 2). En el mundo real, sin embargo, el hecho es que _2n_ se siente dos veces más lento que _n_.

¡El desafío que tienes por delante es implementar el verificador ortográfico más rápido posible! Pero cuando decimos "más rápido", nos referimos al tiempo real (de reloj), no al asintótico.

En `speller.c`, hemos creado un programa que está diseñado para verificar la ortografía de un archivo después de cargar un diccionario de palabras en la memoria desde el disco. Ese diccionario, por su parte, está implementado en un archivo llamado `dictionary.c`. (Podría implementarse solo en `speller.c`, pero a medida que los programas se vuelven más complejos, a menudo es conveniente dividirlos en varios archivos). En cambio, los prototipos de las funciones se definen no en `dictionary.c`, sino en `dictionary.h`. De esa manera, tanto `speller.c` como `dictionary.c` pueden incluir el archivo `#`. Desafortunadamente, no logramos implementar la carga de datos ni la verificación. ¡Ambos (y un poco más) los dejamos para ti! Pero primero, un recorrido.

#### `dictionary.h`

Abre `dictionary.h`, y verás una nueva sintaxis, incluyendo algunas líneas que mencionan `DICTIONARY_H`. No es necesario preocuparse por eso, pero, si estás interesado, esas líneas aseguran que, aunque `dictionary.c` y `speller.c` (que verás en un momento) incluyen este archivo, `clang` solo lo compilará una vez.

Luego, note cómo incluimos un archivo llamado `stdbool.h`. Ahí es donde se define `bool`. No lo habías necesitado antes, ya que se incluía mediante la `#include` de la biblioteca CS50.

También note nuestro uso de `#define`, una "directiva del preprocesador" que define una "constante" llamada `LENGTH` que tiene un valor de `45`. Es una constante en el sentido de que no puede (accidentalmente) cambiarlo en su propio código. De hecho, `clang` reemplazará cualquier mención de `LENGTH` en su propio código con, literalmente, `45`. En otras palabras, no es una variable, solo un truco de búsqueda y reemplazo.

Finalmente, observe los prototipos de cinco funciones: `check`, `hash`, `load`, `size` y `unload`. Observe cómo tres de ellos toman un puntero como argumento, según el `*`:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code>bool check(const char *word);
unsigned int hash(const char *word);
bool load(const char *dictionary);
</code></pre></div></div>

Recuerda que `char *` es lo que solíamos llamar `string`. Por lo tanto, esos tres prototipos son esencialmente:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code>bool check(const string word);
unsigned int hash(const string word);
bool load(const string dictionary);
</code></pre></div></div>

Y `const`, mientras tanto, solo dice que esas cadenas, cuando se pasan como argumentos, deben permanecer constantes; ¡no podrá cambiarlos, accidental o intencionalmente!

#### `dictionary.c`

Ahora abre `dictionary.c`. Observa como en la parte superior del archivo, hemos definido una estructura llamada `node` que representa un nodo en una tabla hash. Y hemos declarado una matriz de punteros globales, `table`, que pronto representará la tabla hash que usarás para realizar un seguimiento de las palabras en el diccionario. La matriz contiene `N` punteros de nodo, y hemos establecido `N` igual a `26` por ahora, para que coincida con la función hash predeterminada descrita a continuación. Es probable que desees aumentar esto dependiendo de tu propia implementación de `hash`.

A continuación, observa que hemos implementado `load`, `check`, `size` y `unload`, pero solo lo suficiente para que el código compile. También observa que hemos implementado `hash` con un algoritmo de muestra basado en la primera letra de la palabra. Tu trabajo, en última instancia, es re-implementar esas funciones de la manera más inteligente posible para que este corrector ortográfico funcione como se anuncia. ¡Y rápido!

#### `speller.c`

Bueno, a continuación abre `speller.c` y dedica un tiempo a examinar el código y los comentarios que contiene. No necesitarás cambiar nada en este archivo, y no necesitas entender su totalidad, pero intenta tener una idea de su funcionalidad de todos modos. Observa cómo, a través de una función llamada `getrusage`, mediremos el tiempo de ejecución de tus implementaciones de `check`, `load`, `size` y `unload`. También observa cómo pasamos `check`, palabra por palabra, el contenido de algún archivo para su revisión ortográfica. En última instancia, informamos cada error ortográfico en ese archivo junto con un montón de estadísticas.

Observa, incidentalmente, que hemos definido el uso de `speller` como

    Usage: speller [dictionary] text
    

donde se supone que `dictionary` es un archivo que contiene una lista de palabras en minúsculas, una por línea, y `text` es un archivo para revisar la ortografía. Como sugieren los corchetes, proporcionar un `dictionary` es opcional; si omites este argumento, `speller` usará `dictionaries/large` de manera predeterminada. En otras palabras, correr

    ./speller text
    

será equivalente a correr

    ./speller dictionaries/large text
    

donde `text` es el archivo que deseas revisar la ortografía. Por supuesto, ¡`speller` no podrá cargar ningún diccionario hasta que implementes `load` en` dictionary.c`! Hasta entonces, verás `Could not load`.

Dentro del diccionario predeterminado, hay 143.091 palabras, ¡todas las cuales deben cargarse en la memoria! De hecho, echa un vistazo a ese archivo para tener una idea de su estructura y tamaño. Observa que todas las palabras en ese archivo aparecen en minúsculas (incluso, por simplicidad, nombres propios y acrónimos). De arriba a abajo, el archivo está ordenado lexicográficamente, con solo una palabra por línea (cada una de las cuales termina con `\n`). Ninguna palabra tiene más de 45 caracteres y ninguna palabra aparece más de una vez. Durante el desarrollo, puede resultarte útil proporcionar a `speller` tu propio `dictionary` que contenga muchas menos palabras, para que no tengas problemas para depurar una estructura, de lo contrario, enorme en memoria. En `dictionaries/small` se encuentra un diccionario de este tipo. Para usarlo, ejecuta

    ./speller dictionaries/small text
    

donde `text` es el archivo que deseas revisar la ortografía. ¡No avances hasta que estés seguro de entender cómo funciona `speller` en sí!

Lo más probable es que no hayas dedicado suficiente tiempo a examinar cuidadosamente `speller.c`. ¡Vuelve una sección y recorre el código nuevamente!

#### `texts/`

Para que puedas probar tu implementación de `speller`, también te hemos proporcionado una gran cantidad de textos, entre ellos el guión de _La La Land_, el texto del Acta de Cuidado de Salud Asequible, tres millones de bytes de Tolstoi, extractos de _The Federalist Papers_ y Shakespeare, y más. Para que sepas qué esperar, abre y ojea cada uno de esos archivos, todos los cuales se encuentran en un directorio llamado `texts` dentro de tu directorio de `pset5`.

Ahora, como deberías saber al haber leído detenidamente `speller.c`, la salida de `speller`, si se ejecuta con, por ejemplo,

    ./speller texts/lalaland.txt
    

eventualmente se parecerá a lo siguiente.

A continuación se muestra parte de la salida que verás. Por razones de información, hemos extraído algunos ejemplos de "errores ortográficos". Y para no estropear la diversión, hemos omitido nuestras propias estadísticas por ahora.

    MISSPELLED WORDS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    WORDS MISSPELLED:
    WORDS IN DICTIONARY:
    WORDS IN TEXT:
    TIME IN load:
    TIME IN check:
    TIME IN size:
    TIME IN unload:
    TIME IN TOTAL:
    

`TIME IN load` representa el número de segundos que `speller` tarda en ejecutar tu implementación de `load`. `TIME IN check` representa el número de segundos que `speller` pasa, en total, ejecutando tu implementación de `check`. `TIME IN size` representa la cantidad de segundos que `speller` tarda en ejecutar tu implementación de `size`. `TIME IN unload` representa la cantidad de segundos que `speller` tarda en ejecutar tu implementación de `unload`. `TIME IN TOTAL` es la suma de esas cuatro mediciones.

**Ten en cuenta que estos tiempos pueden variar ligeramente en ejecuciones de `speller`, dependiendo de lo que esté haciendo tu espacio de código, incluso si no cambias tu código.**

Por cierto, para ser claros, por "mal escrito" simplemente queremos decir que alguna palabra no está en el diccionario proporcionado.

#### `Makefile`

Y, por último, recuerda que `make` automatiza la compilación de tu código para que no tengas que execute `clang` manualmente junto con un montón de conmutadores. Sin embargo, a medida que tus programas aumenten de tamaño, `make` ya no podrá inferir del contexto cómo compilar tu código; deberás empezar a decirle a `make` cómo compilar tu programa, especialmente cuando involucren múltiples archivos de origen (es decir, `.c`), como en el caso de este problema. Y así utilizaremos un `Makefile`, un archivo de configuración que le dice a `make` exactamente qué hacer. Abre `Makefile` y verás cuatro líneas:

1.  La primera línea le dice a `make` que ejecute las líneas siguientes siempre que ejecutes `make speller` (o simplemente `make`).
2.  La segunda línea le dice a `make` cómo compilar `speller.c` en código de máquina (es decir, `speller.o`).
3.  La tercera línea le dice a `make` cómo compilar `dictionary.c` en código de máquina (es decir, `dictionary.o`).
4.  La cuarta línea le dice a `make` que enlace `speller.o` y `dictionary.o` en un archivo llamado `speller`.

**Asegúrate de compilar `speller` ejecutando `make speller` (o simplemente `make`). ¡Ejecutar `make dictionary` no funcionará!**

Especificación
-------------

Bien, el desafío que tienes ante ti ahora es implementar, en orden, `load`, `hash`, `size`, `check` y `unload` de la manera más eficiente posible usando una tabla hash de tal manera que se minimice `TIEMPO EN carga`, `TIEMPO EN revisión`, `TIEMPO EN tamaño` y `TIEMPO EN desactivar`. Asegurándote, no es obvio lo que significa minimizar, en la medida en que estas pruebas variarán seguramente a medida que alimentas `speller` diferentes valores para `diccionario` y para `texto`. Pero ahí radica el desafío, si no la diversión, de este problema. Este problema es tu oportunidad de diseño. Aunque te invitamos a minimizar el espacio, tu enemigo final es el tiempo. Pero antes de empezar, algunas especificaciones:

*   No puedes alterar `speller.c` o `Makefile`.
*   Puedes cambiar `dictionary.c` (y, de hecho, debes hacerlo para completar las implementaciones de `load`, `hash`, `size`,`check` y `unload`) pero no puedes alterar las declaraciones (es decir, los prototipos) de `load`,`hash`, `size`, `check` o `unload`. Sin embargo, puedes agregar nuevas funciones y variables (locales o globales) a `dictionary.c`.
*   Puedes cambiar el valor de `N` en `dictionary.c`, para que tu tabla hash tenga más cubetas.
*   Puedes alterar `dictionary.h`, pero no puedes alterar las declaraciones de `load`,`hash`, `size`, `check` o `unload`.
*   Tu implementación de `check` debe ser insensible a mayúsculas y minúsculas. En otras palabras, si `foo` está en el diccionario, entonces `check` debería devolver verdadero dado cualquier capitalización de ello; ninguna de `foo`,`foO`,`fOo`,`fOO`,`fOO`,`Foo`,`FoO`,`FOo` y `FOO` debe considerarse mal escrita.
*  Dejando a un lado la capitalización, tu implementación de `check` solo debe devolver `verdadero` para las palabras que realmente estén en `dictionary`. Ten cuidado de no codificar en duro palabras comunes (p. ej., `the`), no sea que le pasemos tu implementación un `diccionario` sin las mismas palabras. Además, solo se permiten los posesivos que realmente estén en `dictionary`. En otras palabras, incluso si `foo` está en el diccionario, `check` debería devolver `falso` dado `foo's` si `foo's` no está también en `dictionary`.
*   Puedes asumir que cualquier `dictionary` que pase tu programa tendrá la estructura exactamente igual a la nuestra, ordenado alfabéticamente de arriba hacia abajo con una palabra por línea, cada una de las cuales termina con `\n`. También puedes asumir que `dictionary` contendrá al menos una palabra, que ninguna palabra será más larga que `LONGITUD` (una constante definida en `dictionary.h`) caracteres, que ninguna palabra aparecerá más de una vez, que cada palabra contendrá caracteres alfabéticos minúsculos y posiblemente apóstrofes, y que ninguna palabra comenzará con un apóstrofe.
*   Puedes asumir que `check` solo recibirá palabras que contengan caracteres alfabéticos (mayúsculas o minúsculas) y posiblemente apóstrofes.
*   Tu corrector ortográfico solo puede aceptar `texto` y, opcionalmente, `dictionary` como entrada. Aunque podrías estar inclinado (especialmente si estás entre aquellos más cómodos) a "preprocesar" nuestro diccionario predeterminado para derivar una "función hash ideal" para él, no puedes guardar la salida de tal preprocesamiento en disco para cargarla de vuelta en la memoria en ejecuciones posteriores de tu corrector ortográfico a fin de obtener una ventaja.
*   Tu corrector ortográfico no debe perder memoria. Asegúrate de verificar las pérdidas de memoria con `valgrind`.
*   **La función hash que escribas debe ser la tuya, no una que busques en línea.** Hay muchas formas de implementar una función hash más allá del uso del primer carácter (o caracteres) de una palabra. Considera una función hash que usa la suma de los valores ASCII o la longitud de una palabra. Una buena función hash tiende a reducir las "colisiones" y tiene una distribución bastante uniforme en los "cubos" de la tabla hash.

¡Listo para empezar!

*   Implementar `load`.
*   Implementar `hash`.
*   Implementar `size`.
*   Implementar `check`.
*   Implementar `unload`.

Paseos
------------

Ten en cuenta que hay 6 videos en la lista de reproducción.

<div class="alert" data-alert="danger" role="alert"><p>Aunque el paseo por Speller indica que es razonable usar una función hash encontrada en línea, este video es de una versión anterior del problema donde lo permitimos. Según la especificación anterior, la función hash que escribas debe ser la tuya; no puedes usar una función hash que encuentres en línea. Asegúrate de citar cualquier fuente externa que hayas consultado al escribir tu función hash.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>

Sugerencias
-------

Para comparar dos cadenas de caracteres sin distinguir entre mayúsculas y minúsculas, ¡puede ser útil utilizar [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (declarada en `strings.h`)! También es probable que desee asegurarse de que su función hash no distingue entre mayúsculas y minúsculas, de modo que `foo` y `FOO` tengan el mismo valor hash.

¡Asegúrate de liberar toda la memoria que hayas asignado en `load` en `unload` usando `free`! Recuerda que `valgrind` es tu mejor amigo. Ten en cuenta que `valgrind` supervisa las fugas mientras tu programa se está ejecutando, por lo que asegúrate de proporcionar argumentos de línea de comandos si deseas que `valgrind` analice `speller` mientras usa un diccionario y/o texto específico, como en el siguiente ejemplo. Es mejor utilizar un texto pequeño, de lo contrario `valgrind` podría tardar bastante tiempo en ejecutarse.

    valgrind ./speller texts/cat.txt
    

Si ejecutas `valgrind` sin especificar un `texto` para `speller`, tus implementaciones de `load` y `unload` no se ejecutarán (y, por lo tanto, no serán analizadas).

Si no estás seguro de cómo interpretar la salida de `valgrind`, simplemente pídele ayuda a `help50`:

    help50 valgrind ./speller texts/cat.txt
    

Pruebas
-------

¿Cómo puedes comprobar si tu programa está detectando las palabras mal escritas correctas? Puedes consultar las soluciones propuestas que se encuentran dentro del directorio `keys` que está dentro de tu directorio `speller`. Por ejemplo, dentro de `keys/lalaland.txt` se encuentran todas las palabras que tu programa _debería_ considerar como mal escritas.

Por lo tanto, podrías ejecutar tu programa en algún texto en una ventana, como se muestra a continuación.

    ./speller texts/lalaland.txt
    

Y podrías ejecutar la solución del equipo docente en el mismo texto en otra ventana, como se muestra a continuación.

    ./speller50 texts/lalaland.txt
    

Y podrías comparar las ventanas visualmente lado a lado. Eso podría volverse tedioso rápidamente. Por lo tanto, podrías querer "redirigir" la salida de tu programa a un archivo, como se muestra a continuación.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt
    

Luego puedes comparar ambos archivos lado a lado en la misma ventana con un programa como `diff`, como se muestra a continuación.

    diff -y student.txt staff.txt
    

Alternativamente, para ahorrar tiempo, podrías simplemente comparar la salida de tu programa (asumiendo que la redirigiste, por ejemplo, a `student.txt`) con una de las soluciones que se encuentran en `keys` sin ejecutar la solución del equipo docente, como se muestra a continuación.

    diff -y student.txt keys/lalaland.txt
    

Si la salida de tu programa coincide con la del equipo docente, `diff` mostrará dos columnas que deberían ser idénticas, excepto, tal vez, los tiempos de ejecución en la parte inferior. Sin embargo, si las columnas son diferentes, verás un `>` o `|` donde difieren. Por ejemplo, si ves

    MISSPELLED WORDS                                                MISSPELLED WORDS
    
    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L
    

eso significa que tu programa (cuya salida está a la izquierda) no considera que `Thelonious` o `MIA` están mal escritas, aunque la salida del equipo docente (a la derecha) sí lo hace, como se deduce de la ausencia, por ejemplo, de `Thelonious` en la columna izquierda y de la presencia de `Thelonious` en la columna derecha.

### `check50`

Para probar tu código de manera menos manual (aunque no exhaustiva), también puedes ejecutar lo siguiente.

    check50 cs50/problems/2023/x/speller
    

Ten en cuenta que `check50` también verificará la existencia de fugas de memoria, así que asegúrate de haber ejecutado `valgrind`.

### style50

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 dictionary.c
    

Solución del equipo docente
--------------------------

¿Cómo puedes evaluar qué tan rápida (y correcta) es tu código? Bueno, como siempre, siéntete libre de jugar con la solución del equipo docente, como se muestra a continuación, y comparar sus números con los tuyos.

    ./speller50 texts/lalaland.txt
    

Cómo enviarlo
-------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/speller"

