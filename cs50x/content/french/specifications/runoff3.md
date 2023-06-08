Spécification
-------------

Complétez l'implémentation de `runoff.c` de manière à simuler une élection. Vous devez terminer la mise en œuvre des fonctions `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` et `eliminate`, et vous ne devez rien modifier d'autre dans `runoff.c` (et dans l'inclusion de fichiers d'en-tête supplémentaires si vous le souhaitez).

### `vote`

Complétez la fonction `vote`.

* La fonction prend en argument `voter`, `rank`, et `name`. Si `name` correspond au nom d'un candidat valide, vous devez mettre à jour le tableau de préférences global pour indiquer que l'électeur `voter` a ce candidat comme préférence de rang `rank` (où `0` est la première préférence, `1` est la deuxième préférence, etc.).
* Si la préférence est enregistrée avec succès, la fonction doit retourner `true`; sinon, elle doit retourner `false` (si, par exemple, `name` n'est pas le nom d'un des candidats).
* Vous pouvez supposer que deux candidats n'auront pas le même nom.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous que `candidate_count` stocke le nombre de candidats dans l'élection.</li>
  <li data-marker="*">Rappelez-vous que vous pouvez utiliser <a href="https://man.cs50.io/3/strcmp"><code class="language-plaintext highlighter-rouge">strcmp</code></a> pour comparer deux chaînes de caractères.</li>
  <li data-marker="*">Rappelez-vous que `preferences[i][j]` stocke l'indice du candidat qui est la `j`-ème préférence classée pour l'électeur `i`.</li>
</ul></details>

### `tabulate`

Complétez la fonction `tabulate`.

* La fonction doit mettre à jour le nombre de `votes` de chaque candidat à cette étape du classement.
* Notez que, à chaque étape du classement, chaque électeur vote effectivement pour son candidat le mieux classé qui n'a pas encore été éliminé.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous que `voter_count` stocke le nombre d'électeurs dans l'élection et que, pour chaque électeur de notre élection, nous voulons compter un bulletin de vote.</li>
  <li data-marker="*">Rappelez-vous que, pour un électeur `i`, son candidat de choix est représenté par `preferences[i][0]`, son deuxième choix de candidat par `preferences[i][1]`, etc.</li>
  <li data-marker="*">Rappelez-vous que la structure `candidate` a un champ appelé `eliminated`, qui sera `true` si le candidat a été éliminé de l'élection.</li>
  <li data-marker="*">Rappelez-vous que la structure `candidate` a un champ appelé `votes`, que vous voudrez probablement mettre à jour pour le candidat préféré de chaque électeur.</li>
  <li data-marker="*">Une fois que vous avez voté pour le premier candidat non éliminé d'un électeur, vous voudrez vous arrêter là, et ne pas continuer sur sa liste de préférences ! Rappelez-vous que vous pouvez sortir d'une boucle prématurément en utilisant `break` à l'intérieur d'une condition.</li>
</ul></details>

### `print_winner`

Complétez la fonction `print_winner`.

* Si un candidat a plus de la moitié des voix, son nom devrait être imprimé et la fonction devrait retourner `true`.
* Si personne n'a encore remporté l'élection, la fonction doit renvoyer `false`.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous que `voter_count` stocke le nombre d'électeurs dans l'élection. Étant donné cela, comment exprimeriez-vous le nombre de voix nécessaires pour remporter l'élection ?</li>
</ul></details>

### `find_min`

Complétez la fonction `find_min`.

* La fonction doit renvoyer le nombre de voix minimum pour tout candidat qui est encore dans l'élection.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Vous voudrez probablement parcourir les candidats pour trouver celui qui est encore dans l'élection et qui a le moins de voix. Quelles informations devriez-vous suivre pendant que vous parcourez les candidats ?</li>
</ul></details>

### `is_tie`

Complétez la fonction `is_tie`.

* La fonction prend en argument `min`, qui sera le nombre minimum de voix que quiconque dans l'élection a à ce moment-là.
* La fonction doit renvoyer `true` si tous les candidats restants dans l'élection ont le même nombre de voix et renvoyer `false` sinon.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous qu'une égalité se produit si tous les candidats encore dans l'élection ont le même nombre de voix. Notez également que la fonction `is_tie` prend en argument `min`, qui est le plus petit nombre de voix actuellement obtenu par un candidat. Comment pourriez-vous utiliser cette information pour déterminer si l'élection est une égalité (ou, inversement, pas une égalité) ?</li>
</ul></details>

### `eliminate`

Complétez la fonction `eliminate`.

* La fonction prend en argument `min`, qui sera le nombre minimum de voix que quiconque dans l'élection a à ce moment-là.
* La fonction doit éliminer le candidat (ou les candidats) qui ont `min` nombre de votes.