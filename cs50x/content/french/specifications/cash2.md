## Détails de mise en œuvre

Dans `cash.c`, nous avons implémenté la plupart (mais pas tout!) d'un programme qui demande à l'utilisateur le nombre de cents que doit un client et qui imprime ensuite le plus petit nombre de pièces avec lesquelles cette monnaie peut être faite. En effet, `main` est déjà implémenté pour vous. Mais notez comment `main` appelle plusieurs fonctions qui ne sont pas encore implémentées! L'une de ces fonctions, `get_cents`, ne prend pas d'arguments (comme indiqué par `void`) et renvoie un `int`. Le reste des fonctions prend toutes un argument, un `int`, et renvoie également un `int`. Toutes renvoient actuellement `0` afin que le code puisse être compilé. Mais vous voudrez remplacer chaque `TODO` et chaque `return 0;` par votre propre code. Spécifiquement, complétez la mise en œuvre de ces fonctions comme suit :

- Implémentez `get_cents` de manière à ce que la fonction demande à l'utilisateur un nombre de cents en utilisant `get_int` et renvoie ensuite ce nombre sous forme d'un `int`. Si l'utilisateur entre un `int` négatif, votre code doit demander à l'utilisateur à nouveau. (Mais vous n'avez pas besoin de vous soucier du fait que l'utilisateur entre, par exemple, une `string`, car `get_int` s'en chargera pour vous.) Il est fort probable que vous trouverez une boucle `do while` utile, comme dans [`mario.c`](https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight)!
- Implémentez `calculate_quarters` de manière à ce que la fonction calcule (et renvoie sous forme d'un `int`) combien de quartiers un client doit recevoir s'il est dû un certain nombre de cents. Par exemple, si `cents` est `25`, alors `calculate_quarters` doit renvoyer `1`. Si `cents` est `26` ou `49` (ou quelque chose entre les deux), alors `calculate_quarters` doit également renvoyer `1`. Si `cents` est `50` ou `74` (ou quelque chose entre les deux), alors `calculate_quarters` doit renvoyer `2`. Et ainsi de suite.
- Implémentez `calculate_dimes` de manière à ce que la fonction calcule la même chose pour les dixièmes.
- Implémentez `calculate_nickels` de manière à ce que la fonction calcule la même chose pour les nickels.
- Implémentez `calculate_pennies` de manière à ce que la fonction calcule la même chose pour les pennies.

Remarquez que, contrairement aux fonctions qui n'ont que des effets secondaires, les fonctions qui renvoient une valeur doivent le faire explicitement avec `return` ! Veillez à ne pas modifier votre code, et à remplacer uniquement les `TODO` et la valeur de `return` suivante ! Remarquez également que, en rappelant l'idée d'abstraction, chacune de vos fonctions de calcul devrait accepter n'importe quelle valeur de `cents`, pas seulement celles que l'algorithme glouton pourrait suggérer. Si `cents` est de 85, par exemple, `calculate_dimes` devrait renvoyer 8.

<details><summary>Indice</summary><ul>
  <li data-marker="*">Rappelez-vous qu'il existe plusieurs programmes d'exemple dans le <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/">Code source</a> de la semaine 1 qui illustrent comment les fonctions peuvent renvoyer une valeur.</li>
</ul></details>

Votre programme devrait se comporter comme les exemples ci-dessous.

```
$ ./cash
Change owed: 41
4
```
```
$ ./cash
Change owed: -41
Change owed: foo
Change owed: 41
4
```

### Comment tester votre code

Pour ce programme, essayez de tester votre code manuellement - c'est une bonne pratique :

- Si vous entrez `-1`, votre programme vous invite-t-il à nouveau ?
- Si vous entrez `0`, votre programme affiche-t-il `0` ?
- Si vous entrez `1`, votre programme affiche-t-il `1` (c'est-à-dire une pièce de un cent) ?
- Si vous entrez `4`, votre programme affiche-t-il `4` (c'est-à-dire quatre pièces de un cent) ?
- Si vous entrez `5`, votre programme affiche-t-il `1` (c'est-à-dire un nickel) ?
- Si vous entrez `24`, votre programme affiche-t-il `6` (c'est-à-dire deux dixièmes et quatre pièces de un cent) ?
- Si vous entrez`25`, votre programme affiche-t-il `1` (c'est-à-dire un quart) ?
- Si vous entrez `26`, votre programme affiche-t-il `2` (c'est-à-dire un quart et un cent) ?
- Si vous entrez `99`, votre programme affiche-t-il `9` (c'est-à-dire trois quarts, deux dixièmes et quatre pièces de un cent) ?

Vous pouvez également exécuter la commande ci-dessous pour évaluer la correction de votre code à l'aide de `check50`. Mais assurez-vous de le compiler et de le tester vous-même également !

```
check50 cs50/problems/2023/x/cash
```

<details><summary><code>check50</code> échoue-t-il à compiler votre code ?</summary><p>Assurez-vous de n'avoir modifié que les parties du programme marquées comme <code class="language-plaintext highlighter-rouge">TODO</code>.  Si vous modifiez la fonction <code class="language-plaintext highlighter-rouge">main</code> ou si vous ajoutez des variables globales, par exemple, votre code peut <strong>échouer à la compilation</strong>.  La commande <code class="language-plaintext highlighter-rouge">check50</code> testera vos cinq fonctions indépendamment, au-delà de la simple vérification de la réponse finale.</p></details>

Et exécutez la commande ci-dessous pour évaluer le style de votre code avec `style50`.

```
style50 cash.c
```

## Comment soumettre

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

```
submit50 cs50/problems/2023/x/cash
```