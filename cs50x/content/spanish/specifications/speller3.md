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