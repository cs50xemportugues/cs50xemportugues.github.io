# Cash

## Démarrage

Ouvrez [VS Code] (https://code.cs50.io/).

Commencez par cliquer dans votre fenêtre de terminal, puis exécutez `cd` tout seul. Vous devriez constater que son "invite" ressemble à ce qui suit.

```
$
```

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

```
wget https://cdn.cs50.net/2022/fall/psets/1/cash.zip
```

suivi de la touche Entrée pour télécharger un ZIP appelé `cash.zip` dans votre espace de codes. Veillez à ne pas ignorer l'espace entre "wget" et l'URL suivante, ou tout autre caractère d'ailleurs!

Maintenant, exécutez

```
décompresser cash.zip
```

pour créer un dossier appelé "cash". Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

```
rm cash.zip
```

et répondez par "y" suivi d'Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

```
cd cash
```

suivi d'Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

```
cash/ $
```

Si tout s'est bien passé, vous devriez exécuter

```
ls
```

et voir un fichier nommé `cash.c`. L'exécution de `code cash.c` devrait ouvrir le fichier où vous saisirez votre code pour cet ensemble de problèmes. Sinon, retrouvez vos pas et voyez si vous pouvez déterminer où vous avez fait une erreur!

## Algorithmes voraces

![Pièces américaines](https://cs50.harvard.edu/x/2023/psets/1/cash/coins.jpg)

Lorsque vous rendez la monnaie, il est probable que vous souhaitiez minimiser le nombre de pièces que vous distribuez à chaque client, de peur de tomber à court (ou d'irriter le client!). Heureusement, l'informatique a donné aux caissiers des moyens de minimiser les nombres de pièces à rendre : les algorithmes gloutons.

Selon l'Institut national des standards et de la technologie (NIST), un algorithme glouton est celui qui "prend toujours la meilleure solution immédiate ou locale tout en trouvant une réponse. Les algorithmes gloutons trouvent la solution optimale globale pour certains problèmes d'optimisation, mais peuvent trouver des solutions moins optimales pour certains cas d'autres problèmes".

Que cela signifie-t-il ? Eh bien, supposons qu'un caissier doive rendre de la monnaie à un client et que dans le tiroir-caisse se trouvent des quarts (25¢), des dimes (10¢), des nickels (5¢) et des pennies (1¢). Le problème à résoudre est de décider quelles pièces et combien de chacune à remettre au client. Imaginez un caissier "glouton" comme celui qui veut prendre la plus grosse bouchée de ce problème possible avec chaque pièce qu'il prend dans le tiroir. Par exemple, si un client doit recevoir 41¢, la plus grande bouchée possible (c'est-à-dire la meilleure immédiate ou locale) qui peut être prise est de 25¢. (Cette bouchée est "la meilleure" dans la mesure où elle nous rapproche plus rapidement de 0¢ que toute autre pièce le ferait.) Notez qu'une bouchée de cette taille réduirait un problème de 41¢ à un problème de 16¢, car 41 - 25 = 16. C'est-à-dire que le reste est un problème similaire mais plus petit. Inutile de dire qu'une autre bouchée de 25¢ serait trop grosse (en supposant que le caissier préfère ne pas perdre d'argent), de sorte que notre caissier glouton passerait à une bouchée de taille 10¢, ce qui lui laisserait un problème de 6¢. À ce stade, la cupidité appelle une bouchée de 5¢ suivie d'une bouchée de 1¢, à partir de ce moment, le problème est résolu. Le client reçoit un quarter, une dime, un nickel et un penny : quatre pièces au total.

Il s'avère que cette approche gloutonne (c'est-à-dire l'algorithme) est non seulement localement optimale, mais aussi globalement optimale pour la monnaie américaine (et aussi pour celle de l'Union européenne). C'est-à-dire que tant qu'un caissier a suffisamment de chaque pièce, cette approche du plus grand au plus petit donnera le moins de pièces possible. Combien peu ? Eh bien, c'est à vous de nous le dire!

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

