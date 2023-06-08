Especificación
-------------

Completa la implementación de `runoff.c` de tal manera que simule una elección de desempate. Debes completar las implementaciones de las funciones `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` y `eliminate`, y no debes modificar nada más en `runoff.c` (y la inclusión de archivos de cabecera adicionales, si lo deseas).

### `voto`

Completa la función `vote`.

*   La función toma los argumentos `votante`, `clasificación` y `nombre`. Si `nombre` es una coincidencia con el nombre de un candidato válido, entonces debes actualizar la matriz global de preferencias para indicar que el votante `votante` tiene ese candidato como su preferencia de `clasificación` (donde `0` es la primera preferencia, `1` es la segunda preferencia, etc.). 
*   Si se registra la preferencia correctamente, la función debe devolver `true`; la función debe devolver `false` de lo contrario (por ejemplo, si `nombre` no es el nombre de uno de los candidatos).
*   Se puede asumir que ningún candidato tendrá el mismo nombre.


<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que `candidate_count` almacena el número de candidatos en la elección.</li>
  <li data-marker="*">Recuerda que puedes utilizar <a href="https://man.cs50.io/3/strcmp"><code class="language-plaintext highlighter-rouge">strcmp</code></a> para comparar dos cadenas.</li>
  <li data-marker="*">Recuerda que `preferences[i][j]` almacena el índice del candidato que es la preferencia clasificada como número <code class="language-plaintext highlighter-rouge">j</code> para el votante <code class="language-plaintext highlighter-rouge">i</code>.</li>
</ul></details>

### `tabulate`

Completa la función `tabulate`.

*   La función debe actualizar el número de `votos` que tiene cada candidato en esta etapa de la elección.
*   Recuerda que en cada etapa del proceso, cada votante vota efectivamente por su candidato mejor clasificado que aún no haya sido eliminado.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que `voter_count` almacena el número de votantes en la elección y que, por cada votante en nuestra elección, queremos contar un voto.</li>
  <li data-marker="*">Recuerda que para un votante <code class="language-plaintext highlighter-rouge">i</code>, el candidato de su preferencia principal está representado por <code class="language-plaintext highlighter-rouge">preferences[i][0]</code>, su segundo candidato de preferencia por <code class="language-plaintext highlighter-rouge">preferences[i][1]</code>, etc.</li>
  <li data-marker="*">Recuerda que la estructura <code class="language-plaintext highlighter-rouge">candidato</code> tiene un campo llamado `eliminado`, que será verdadero si el candidato ha sido eliminado de la elección.</li>
  <li data-marker="*">Recuerda que la estructura `candidato` tiene un campo llamado `votos`, que probablemente querrás actualizar para el candidato preferido de cada votante.</li>
  <li data-marker="*">Una vez que has emitido un voto para el primer candidato no eliminado del votante, probablemente querrás detenerte allí, ¡no continuar en su voto! Recuerda que puedes salir de un ciclo temprano usando `break` dentro de una condicional.</li>
</ul></details>

### `print_winner`

Completa la función `print_winner`.

*   Si algún candidato tiene más de la mitad de los votos, su nombre debe ser impreso y la función debe devolver `true`.
*   Si nadie ha ganado la elección todavía, la función debe devolver `false`.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que `voter_count` almacena el número de votantes en la elección. Dado eso, ¿cómo expresarías el número de votos necesarios para ganar la elección?</li>
</ul></details>

### `find_min`

Completa la función `find_min`.

*   La función debería devolver el total mínimo de votos para cualquier candidato que aún esté en la elección.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Probablemente querrás recorrer los candidatos para encontrar al que todavía está en la elección y tiene el menor número de votos. ¿Qué información deberías tener en cuenta mientras recorres los candidatos?</li>
</ul></details>

### `is_tie`

Completa la función `is_tie`.

*   La función toma un argumento `min`, que será el número mínimo de votos que alguien en la elección tiene actualmente.
*   La función debe devolver `true` si cada candidato que permanece en la elección tiene el mismo número de votos, y debe devolver `false` de lo contrario.

<details><summary>Pistas</summary><ul>
  <li data-marker="*">Recuerda que un empate ocurre si cada candidato que todavía está en la elección tiene el mismo número de votos. Además, la función `is_tie` toma un argumento `min`, que es la cantidad más pequeña de votos que cualquier candidato tiene actualmente. ¿Cómo podrías usar esa información para determinar si la elección es un empate o, por el contrario, no es un empate?</li>
</ul></details>

### `eliminate`

Completa la función `eliminate`.

*   La función toma un argumento `min`, que será el número mínimo de votos que alguien en la elección tenga actualmente.
*   La función debería eliminar al candidato (o candidatos) que tengan un número `min` de votos.