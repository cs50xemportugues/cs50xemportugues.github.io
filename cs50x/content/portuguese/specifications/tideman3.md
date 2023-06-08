Especificação
-------------

Complemente a implementação de `tideman.c` de forma que simule uma eleição de Tideman.

*   Complete a função `vote`.
    *   A função recebe os argumentos `rank`, `name` e `ranks`. Se `name` corresponder ao nome de um candidato válido, você deve atualizar o vetor `ranks` para indicar que o eleitor tem o candidato como sua preferência na posição `rank` (onde `0` é a primeira preferência, `1` é a segunda preferência, etc.).
    *   Lembre-se que `ranks[i]` representa a `i`-ésima preferência do usuário.
    *   A função deve retornar `true` se a classificação foi registrada com sucesso e `false` caso contrário (por exemplo, se `name` não for o nome de um dos candidatos).
    *   É possível assumir que nenhum dos candidatos terá o mesmo nome.
*   Complete a função `record_preferences`.
    *   A função é chamada uma vez para cada eleitor e recebe como argumento o vetor `ranks` (lembre-se de que `ranks[i]` é a `i`-ésima preferência do eleitor, onde `ranks[0]` é a primeira preferência).
    *   A função deve atualizar o vetor de `preferências` global para adicionar as preferências do eleitor atual. Lembre-se que `preferências[i][j]` deve representar o número de eleitores que preferem o candidato `i` ao candidato `j`.
    *   É possível assumir que cada eleitor classificará todos os candidatos.
*   Complete a função `add_pairs`.
    *   A função deve adicionar todos os pares de candidatos em que um candidato é preferido no vetor `pairs`. Um par de candidatos que empatam (um não é preferido em relação ao outro) não deve ser adicionado ao vetor.
    *   A função deve atualizar a variável global `pair_count` para ser o número total de pares de candidatos. (Os pares devem ser armazenados em `pairs[0]` até `pairs[pair_count - 1]`, inclusive).
*   Complete a função `sort_pairs`.
    *   A função deve classificar o vetor `pairs` em ordem decrescente de força de vitória, onde a força da vitória é definida como o número de eleitores que preferem o candidato preferido. Se vários pares tiverem a mesma força de vitória, é possível assumir que não importa a ordem.
*   Complete a função `lock_pairs`.
    *   A função deve criar o grafo "locked", adicionando todas as arestas em ordem decrescente de força de vitória, desde que a aresta não crie ciclo.
*   Complete a função `print_winner`.
    *   A função deve imprimir o nome do candidato que é a fonte do grafo. É possível assumir que não haverá mais de uma fonte.

Você não deve modificar nada além das implementações das funções `vote`, `record_preferences`, `add_pairs`, `sort_pairs`, `lock_pairs` e `print_winner` em `tideman.c` (e a inclusão de arquivos header adicionais, se desejar). É permitido adicionar funções adicionais em `tideman.c`, desde que não sejam alteradas as declarações das funções existentes.

Passo a passo
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/kb83NwyYI68?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>