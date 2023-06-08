Especificación
-------------

Completa la implementación de `tideman.c` de tal manera que simule una elección tipo "Tideman".

*   Completa la función `vote`.
    *   La función toma los argumentos `rank`, `name` y `ranks`. Si `name` coincide con el nombre de un candidato válido, deberías actualizar el array `ranks` para indicar que el votante tiene al candidato como su preferencia de `rank` (donde `0` es la primera preferencia, `1` es la segunda, etc.).
    *   Recuerda que `ranks[i]` representa la i-ésima preferencia del usuario.
    *   La función debe devolver `true` si la preferencia se registró correctamente y `false` de lo contrario (si, por ejemplo, `name` no es el nombre de ninguno de los candidatos).
    *   Puedes asumir que ningún candidato tendrá el mismo nombre.
*   Completa la función `record_preferences`.
    *   La función se llama una vez por cada votante y toma como argumento el array de `ranks` (recuerda que `ranks[i]` es la i-ésima preferencia del votante, donde `ranks[0]` es la primera preferencia).
    *   La función debe actualizar el array global `preferences` para agregar las preferencias del votante actual. Recuerda que `preferences[i][j]` debe representar el número de votantes que prefieren al candidato `i` sobre el candidato `j`.
    *   Puedes asumir que cada votante clasificará a todos los candidatos.
*   Completa la función `add_pairs`.
    *   La función debe agregar todas las parejas de candidatos donde un candidato es preferido en el array `pairs`. No se debe agregar una pareja de candidatos que estén empatados (uno no es preferido sobre el otro).
    *   La función debe actualizar la variable global `pair_count` para que sea el número de parejas de candidatos. (Las parejas deberán estar todas almacenadas entre `pairs[0]` y `pairs[pair_count - 1]`, ambas inclusive).
*   Completa la función `sort_pairs`.
    *   La función debe ordenar el array `pairs` en orden decreciente de fortaleza de victoria, donde la fortaleza de victoria se define como el número de votantes que prefieren al candidato preferido. Si varias parejas tienen la misma fortaleza de victoria, se puede asumir que el orden no importa.
*   Completa la función `lock_pairs`.
    *   La función debe crear el grafo `locked`, agregando todas las aristas en orden decreciente de la fortaleza de victoria siempre y cuando la arista no cree un ciclo.
*   Completa la función `print_winner`.
    *   La función debe imprimir el nombre del candidato que es la fuente del grafo. Puedes asumir que no habrá más de una fuente.

No debes modificar nada más en `tideman.c` aparte de las implementaciones de las funciones `vote`, `record_preferences`, `add_pairs`, `sort_pairs`, `lock_pairs`, y `print_winner` (y la inclusión de archivos de encabezado adicionales, si lo deseas). Se te permite agregar funciones adicionales a `tideman.c`, siempre y cuando no cambies las declaraciones de las funciones existentes.

Tutorial
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/kb83NwyYI68?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>