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