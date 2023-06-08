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