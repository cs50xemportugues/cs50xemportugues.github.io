### `helpers.h`

Ensuite, regardez le fichier `helpers.h`. Ce fichier est assez court et fournit simplement les prototypes de fonction pour les fonctions que vous avez vues précédemment.

Ici, notez que chaque fonction prend en argument un tableau en 2D appelé `image`, où `image` est un tableau de `height` lignes et chaque ligne est un autre tableau de `width` `RGBTRIPLE`s. Donc, si `image` représente l'image entière, alors `image[0]` représente la première ligne et `image[0][0]` représente le pixel dans le coin supérieur gauche de l'image.

### `helpers.c`

Maintenant, ouvrez `helpers.c`. C'est ici que doivent se trouver les implémentations des fonctions déclarées dans `helpers.h`. Mais notez que, pour l'instant, les implémentations sont manquantes ! Cette partie vous incombe donc.

### `Makefile`

Enfin, regardons le `Makefile`. Ce fichier spécifie ce qui doit se passer lorsque nous exécutons une commande terminal comme `make filter`. Alors que les programmes que vous avez peut-être écrits auparavant étaient confinés à un seul fichier, `filter` semble utiliser plusieurs fichiers : `filter.c` et `helpers.c`. Nous devrons donc dire à `make` comment compiler ce fichier.

Essayez de compiler `filter` vous-même en accédant à votre terminal et en tapant :

$ make filter

Ensuite, vous pouvez exécuter le programme en entrant :

$ ./filter -g images/yard.bmp out.bmp

qui prend l'image `images/yard.bmp` et génère une nouvelle image appelée `out.bmp` après avoir fait passer les pixels à travers la fonction `grayscale`. `grayscale` ne fait cependant rien pour l'instant, donc l'image de sortie devrait ressembler à la cour d'origine.

Spécification
-------------

Implémentez les fonctions dans `helpers.c` de manière à ce qu'un utilisateur puisse appliquer des filtres de noir et blanc, de réflexion, de flou ou de détection de bords à leurs images.

*   La fonction `grayscale` doit prendre une image et la transformer en une version noir et blanc de la même image.
*   La fonction `reflect` doit prendre une image et la réfléchir horizontalement.
*   La fonction `blur` doit prendre une image et la transformer en une version floue en boîte de la même image.
*   La fonction `edges` doit prendre une image et mettre en évidence les bords entre les objets, selon l'opérateur de Sobel.

Vous ne devez pas modifier les signatures de fonction ni aucun autre fichier autre que `helpers.c`.

Walkthrough
-----------

**Veuillez noter qu'il y a 5 vidéos dans cette playlist.**