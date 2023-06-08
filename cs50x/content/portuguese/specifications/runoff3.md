Especificação
-------------

Complete a implementação do `runoff.c` de forma a simular uma eleição de segundo turno. Você deve completar as implementações das funções `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` e `eliminate`, e não deve modificar nada mais no `runoff.c` (e a inclusão de arquivos de cabeçalho adicionais, se desejar).

### `vote`

Complete a função `vote`.

*   A função recebe como argumentos `voter`, `rank` e `name`. Se `name` for uma correspondência com o nome de um candidato válido, você deve atualizar a matriz global de preferências para indicar que o eleitor `voter` tem aquele candidato como sua preferência de `rank` (onde `0` é a primeira preferência, `1` é a segunda preferência, e assim por diante).
*   Se a preferência for registrada com sucesso, a função deve retornar `true`; caso contrário, a função deve retornar `false` (se, por exemplo, `nome` não é o nome de um dos candidatos).
*   Você pode assumir que nenhum dois candidatos terá o mesmo nome.


<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">candidate_count</code> armazena o número de candidatos na eleição.</li>
  <li data-marker="*">Lembre-se de que você pode usar <a href="https://man.cs50.io/3/strcmp"><code class="language-plaintext highlighter-rouge">strcmp</code></a> para comparar duas strings.</li>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">preferences[i][j]</code> armazena o índice do candidato que é a preferência classificada como <code class="language-plaintext highlighter-rouge">j</code> para o eleitor <code class="language-plaintext highlighter-rouge">i</code>.</li>
</ul></details>

### `tabulate`

Complete a função `tabulate`.

*   A função deve atualizar o número de `votes` que cada candidato tem nesta fase da eleição.
*   Lembre-se de que, em cada fase da eleição, cada eleitor vota efetivamente no candidato de sua preferência que ainda não foi eliminado.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">voter_count</code> armazena o número de eleitores na eleição e que, para cada eleitor em nossa eleição, queremos contar uma cédula.</li>
  <li data-marker="*">Lembre-se de que, para um eleitor <code class="language-plaintext highlighter-rouge">i</code>, seu candidato de primeira escolha é representado por <code class="language-plaintext highlighter-rouge">preferences[i][0]</code>, seu candidato de segunda escolha por <code class="language-plaintext highlighter-rouge">preferences[i][1]</code>, etc.</li>
  <li data-marker="*">Lembre-se de que a <code class="language-plaintext highlighter-rouge">struct</code> <code class="language-plaintext highlighter-rouge">candidate</code> tem um campo chamado <code class="language-plaintext highlighter-rouge">eliminated</code>, que será <code class="language-plaintext highlighter-rouge">true</code> se o candidato foi eliminado da eleição.</li>
  <li data-marker="*">Lembre-se de que a <code class="language-plaintext highlighter-rouge">struct</code> <code class="language-plaintext highlighter-rouge">candidate</code> tem um campo chamado <code class="language-plaintext highlighter-rouge">votes</code>, que você provavelmente desejará atualizar para o candidato preferido de cada eleitor.</li>
  <li data-marker="*">Depois que você votou no primeiro candidato não eliminado de um eleitor, desejará parar ali, não continuar em sua cédula! Lembre-se de que você pode sair de um loop mais cedo usando <code class="language-plaintext highlighter-rouge">break</code> dentro de uma condicional.</li>
</ul></details>

### `print_winner`

Complete a função `print_winner`.

*   Se algum candidato tiver mais da metade dos votos, seu nome deve ser impresso e a função deve retornar `true`.
*   Se ninguém ganhou a eleição ainda, a função deve retornar `false`.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que <code class="language-plaintext highlighter-rouge">voter_count</code> armazena o número de eleitores na eleição. Dado isso, como você expressaria o número de votos necessários para vencer a eleição?</li>
</ul></details>

### `find_min`

Complete a função `find_min`.

*   A função deve retornar o total mínimo de votos para qualquer candidato que ainda esteja na eleição.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Provavelmente, você desejará percorrer os candidatos para encontrar aquele que ainda está na eleição e tem o menor número de votos. Que informações você deve controlar enquanto percorre os candidatos?</li>
</ul></details>

### `is_tie`

Complete a função `is_tie`.

*   A função leva um argumento `min`, que será o número mínimo de votos que alguém na eleição atualmente tem.
*   A função deve retornar `true` se todo candidato que ainda está na eleição tiver o mesmo número de votos e deve retornar `false` caso contrário.

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que uma gravata acontece se todo candidato ainda na eleição tiver o mesmo número de votos. Repare também que a função <code class="language-plaintext highlighter-rouge">is_tie</code> pega um argumento <code class="language-plaintext highlighter-rouge">min</code>, que é o menor número de votos que qualquer candidato tem atualmente. Como você pode usar essa informação para determinar se a eleição é uma gravata (ou, inversamente, não é uma gravata)?</li>
</ul></details>

### `eliminate`

Complete a função `eliminate`.

*   A função leva um argumento `min`, que será o número mínimo de votos que alguém na eleição atualmente tem.
*   A função deve eliminar o candidato (ou candidatos) que tem `min` número de votos.