### Utilisation de la clé

Modifiez `main` de manière à ce qu'il convertisse `argv[1]` en un `int`. Vous pourriez trouver utile d'utiliser `atoi`, déclaré dans `stdlib.h`, comme indiqué dans [manual.cs50.io](https://manual.cs50.io/). Ensuite, utilisez `get_string` pour demander à l'utilisateur un texte en clair avec `"plaintext : "`.

Ensuite, implémentez une fonction appelée, par exemple, `rotate`, qui prend en entrée un `char` et également un `int`, et fait tourner ce `char` de ce nombre de positions s'il s'agit d'une lettre (c'est-à-dire alphabétique), en bouclant de `Z` à `A` (et de `z` à `a`) si nécessaire. Si le `char` n'est pas une lettre, la fonction doit plutôt renvoyer le même `char` inchangé.

<details><summary>Conseils</summary>
<ul>

  <li data-marker="*">Il est probable que vous vouliez un prototype du type :
  
  ```
  char rotate(char c, int n);
  ```
  
  Un appel de fonction comme :
  
  ```
  rotate('A', 1)
  ``` 
  
  ou même 
  
  ```
  rotate('A', 27)
  ``` 
  renverrait donc `'B'`. Et un appel de fonction comme
  
  ```
  rotate('!', 13)
  ``` 
  
  renverrait `'!'`.</li>
  
  <li data-marker="*">Rappelez-vous que vous pouvez « caster » explicitement un `char` en un `int` avec `(char)`, et un `int` en un `char` avec `(int)`. Ou vous pouvez le faire implicitement en traitant simplement l'un comme l'autre.</li>
  
  <li data-marker="*">Il est probable que vous vouliez soustraire la valeur ASCII de 'A' à n'importe quelle lettre majuscule, afin de traiter 'A' comme 0, 'B' comme 1, etc., tout en effectuant l'arithmétique. Et puis l'ajouter à nouveau une fois terminé.</li>
  
  <li data-marker="*">Il est probable que vous vouliez soustraire la valeur ASCII de `'a'` à n'importe quelle lettre minuscule, afin de traiter `'''a'''` comme `'''0'''`, `'''b'''` comme `'''1'''`, etc., tout en effectuant l'arithmétique. Et puis l'ajouter à nouveau une fois terminé.</li>

  <li data-marker="*">Vous pourriez trouver utile que certaines autres fonctions déclarées dans `ctype.h`, telles que présentées dans <a href="https://manual.cs50.io/">manual.cs50.io</a>.</li>

  <li data-marker="*">Il est probable que vous trouviez l'utilisation de `%` utile pour effectuer une « boucle » arithmétiquement avec une valeur comme `25` pour la rendre à `0`.</li>

</ul>
</details>

Modifiez ensuite `main` de manière à ce qu'il imprime `"ciphertext : "` puis itère sur chaque `char` du texte en clair de l'utilisateur, en appelant `rotate` sur chacun et en imprimant la valeur renvoyée.

<details><summary>Conseils</summary>
<ul>
  <li data-marker="*">Rappelez-vous que `printf` peut imprimer un `char` en utilisant `%c`.</li>
  <li data-marker="*">Si vous ne voyez aucun résultat lorsque vous appelez `printf`, il est probable que cela soit dû à l'impression de caractères en dehors de la plage ASCII valide de 0 à 127. Essayez d'imprimer temporairement des caractères en tant que nombres (en utilisant `%i` plutôt que `%c`) pour voir les valeurs que vous imprimez !</li>
</ul>
</details>