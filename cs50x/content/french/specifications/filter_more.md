Filtrer
=======

Implémentez un programme qui applique des filtres à des BMP, comme décrit ci-dessous.

    $ ./filter -r IMAGE.bmp REFLECTED.bmp
    

où IMAGE.bmp est le nom du fichier image d'entrée et REFLECTED.bmp est le nom donné au fichier image de sortie qui est reflété.

Contexte
--------

### Bitmaps

La représentation la plus simple d'une image est peut-être une grille de pixels (c'est-à-dire des points), chacun pouvant avoir une couleur différente. Pour les images en noir et blanc, nous avons donc besoin d'un bit par pixel, 0 pouvant représenter le noir et 1 pouvant représenter le blanc, comme ci-dessous.

![Un exemple de bitmap simple](https://cs50.harvard.edu/x/2023/psets/4/filter/more/bitmap.png)

En ce sens, une image est simplement un bitmap (c'est-à-dire une carte de bits). Pour des images plus colorées, vous avez simplement besoin de plus de bits par pixel. Un format de fichier (comme [BMP](https://fr.wikipedia.org/wiki/Windows_bitmap), [JPEG](https://fr.wikipedia.org/wiki/Joint_Photographic_Experts_Group) ou [PNG](https://fr.wikipedia.org/wiki/Portable_Network_Graphics)) qui prend en charge la "couleur 24 bits" utilise 24 bits par pixel (BMP prend en charge 1, 4, 8, 16, 24 et 32 bits couleur).

Un BMP 24 bits utilise 8 bits pour indiquer la quantité de rouge dans la couleur d'un pixel, 8 bits pour indiquer la quantité de vert dans la couleur d'un pixel, et 8 bits pour indiquer la quantité de bleu dans la couleur d'un pixel. Si les valeurs R, G et B d'un pixel dans un BMP sont, par exemple, `0xff`, `0x00` et `0x00` en hexadécimal, ce pixel est purement rouge, car `0xff` (également connu sous le nom de `255` en décimal) implique "beaucoup de rouge", tandis que `0x00` et `0x00` impliquent "aucun vert" et "aucun bleu", respectivement.

### Un peu plus technique (bitmap)

Rappelez-vous qu'un fichier n'est qu'une séquence de bits, disposés d'une certaine manière. Un fichier BMP 24 bits est donc essentiellement une séquence de bits, dont chaque groupement de 24 bits représente la couleur de certains pixels. Mais un fichier BMP contient également des "métadonnées", comme les dimensions de l'image. Ces métadonnées sont stockées au début du fichier sous la forme de deux structures de données généralement appelées "en-tête", à ne pas confondre avec les fichiers d'en-tête de C. (Ces en-têtes ont évolué avec le temps. Ce problème utilise la dernière version du format BMP de Microsoft, 4.0, qui a fait ses débuts avec Windows 95.)

Le premier de ces en-têtes, appelé `BITMAPFILEHEADER`, fait 14 octets de long (rappelons qu'un octet est égal à 8 bits). Le second de ces en-têtes, appelé `BITMAPINFOHEADER`, fait 40 octets de long. Immédiatement après ces en-têtes se trouve le bitmap réel : un tableau d'octets, dont chaque triplet représente la couleur d'un pixel. Cependant, les BMP stockent ces triplets à l'envers (c'est-à-dire en BGR), avec 8 bits pour le bleu, suivis de 8 bits pour le vert, puis de 8 bits pour le rouge. (Certains BMP stockent également le bitmap entier en inversé, avec la première ligne de l'image à la fin du fichier BMP. Mais nous avons stocké les BMP de cet ensemble de problèmes tels que décrits ici, avec la première rangée du bitmap en haut et la dernière en bas.) En d'autres termes, si nous convertissons le smiley en 1-bit ci-dessus en smiley en 24 bits, en remplaçant le noir par le rouge, un BMP 24 bits stockera ce bitmap comme suit, où `0000ff` signifie rouge et `ffffff` signifie blanc; nous avons surligné en rouge toutes les occurrences de `0000ff`.

![Un sourire rouge](https://cs50.harvard.edu/x/2023/psets/4/filter/more/red_smile.png)

Comme nous avons présenté ces bits de gauche à droite, de haut en bas, en 8 colonnes, vous pouvez réellement voir le smiley rouge si vous prenez un peu de recul.

Pour être clair, rappelons qu'un chiffre hexadécimal représente 4 bits. Par conséquent, `ffffff` en hexadécimal signifie en réalité `111111111111111111111111` en binaire.

Remarquez que vous pourriez représenter un bitmap en tant que tableau bidimensionnel de pixels : où l'image est un tableau de lignes, et chaque ligne est un tableau de pixels. C'est d'ailleurs ainsi que nous avons choisi de représenter les images bitmap dans ce problème.

### Filtrage d'images

Que signifie filtrer une image? Vous pouvez penser à filtrer une image en prenant les pixels d'une image originale et en modifiant chaque pixel de manière à ce qu'un effet particulier soit apparent dans l'image résultante.

#### Niveau de Gris

Un filtre courant est le filtre "niveau de gris", où nous prenons une image et voulons la convertir en noir et blanc. Comment cela fonctionne-t-il?

Rappelez-vous que si les valeurs rouge, verte et bleue sont toutes définies sur `0x00` (hexadécimal pour `0`), le pixel est noir. Et si toutes les valeurs sont définies sur `0xff` (hexadécimal pour `255`), le pixel est blanc. Tant que les valeurs rouge, verte et bleue sont toutes égales, le résultat sera des nuances de gris le long du spectre noir-blanc, avec des valeurs plus élevées signifiant des nuances plus claires (plus proches du blanc) et des valeurs inférieures signifiant des nuances plus sombres (plus proches du noir).

Pour convertir un pixel en niveau de gris, nous devons simplement nous assurer que les valeurs rouge, verte et bleue ont toutes la même valeur. Mais comment savons-nous quelle valeur leur donner? Eh bien, il est probablement raisonnable de s'attendre à ce que si les valeurs rouge, verte et bleue d'origine étaient toutes assez élevées, la nouvelle valeur devrait également être assez élevée. Et si les valeurs d'origine étaient toutes faibles, la nouvelle valeur devrait également être faible.

En fait, pour s'assurer que chaque pixel de la nouvelle image a toujours la même luminosité générale ou la même obscurité que l'ancienne image, nous pouvons prendre la moyenne des valeurs rouge, verte et bleue pour déterminer quelle nuance de gris faire pour le nouveau pixel.

Si vous appliquez cela à chaque pixel de l'image, le résultat sera une image convertie en niveau de gris.

#### Réflexion

Certains filtres peuvent également déplacer les pixels autour. Réfléchir une image, par exemple, est un filtre où l'image résultante est ce que vous obtiendriez en plaçant l'image d'origine devant un miroir. Donc, tous les pixels du côté gauche de l'image doivent se retrouver à droite et vice versa.

Notez que tous les pixels d'origine de l'image d'origine seront toujours présents dans l'image réfléchie, il se peut simplement que ces pixels se soient réarrangés pour être à un endroit différent dans l'image.

#### Flou

Il existe plusieurs façons de créer l'effet de flou ou d'adoucissement d'une image. Pour ce problème, nous utiliserons le "flou de boîte", qui consiste à prendre chaque pixel et, pour chaque valeur de couleur, à lui donner une nouvelle valeur en moyennant les valeurs de couleur des pixels voisins.

Considérons la grille de pixels suivante, où nous avons numéroté chaque pixel.

![une grille de pixels](https://cs50.harvard.edu/x/2023/psets/4/filter/more/grid.png)

La nouvelle valeur de chaque pixel serait la moyenne des valeurs de tous les pixels qui se trouvent dans 1 rangée et une colonne du pixel d'origine (formant une boîte 3x3). Par exemple, chacune des valeurs de couleur pour le pixel 6 serait obtenue en moyennant les valeurs de couleur d'origine des pixels 1, 2, 3, 5, 6, 7, 9, 10 et 11 (notez que le pixel 6 lui-même est inclus dans la moyenne). De même, les valeurs de couleur pour le pixel 11 seraient obtenues en moyennant les valeurs de couleur des pixels 6, 7, 8, 10, 11, 12, 14, 15 et 16.

Pour un pixel le long du bord ou du coin, comme le pixel 15, nous chercherions toujours tous les pixels dans 1 rangée et une colonne: dans ce cas, les pixels 10, 11, 12, 14, 15 et 16.

#### Arêtes

Dans les algorithmes d'intelligence artificielle pour le traitement d'images, il est souvent utile de détecter les arêtes dans une image : les lignes de l'image qui créent une limite entre deux objets. Une façon d'obtenir cet effet est d'appliquer l'[opérateur de Sobel](https://en.wikipedia.org/wiki/Sobel_operator) à l'image.

Comme le flou d'image, la détection de contours fonctionne également en prenant chaque pixel, et en le modifiant en fonction de la grille de pixels 3x3 qui entoure ce pixel. Mais au lieu de simplement prendre la moyenne des neuf pixels, l'opérateur de Sobel calcule la nouvelle valeur de chaque pixel en prenant une somme pondérée des valeurs des pixels environnants. Et comme les arêtes entre les objets peuvent avoir lieu dans les directions verticale et horizontale, vous calculerez en fait deux sommes pondérées : une pour détecter les arêtes dans la direction x et une pour détecter les arêtes dans la direction y. En particulier, vous utiliserez les deux "noyaux" suivants :

! [Noyaux de Sobel](https://cs50.harvard.edu/x/2023/psets/4/filter/more/sobel.png)

Comment interpréter ces noyaux? En bref, pour chacune des trois valeurs de couleur pour chaque pixel, nous calculerons deux valeurs `Gx` et `Gy`. Pour calculer `Gx` pour la valeur de canal rouge d'un pixel, par exemple, nous prendrons les valeurs rouges d'origine des neuf pixels qui forment une boîte 3x3 autour du pixel, nous les multiplierons chacune par la valeur correspondante dans le noyau `Gx` et nous prendrons la somme des valeurs résultantes.

Pourquoi ces valeurs particulières pour le noyau? Dans la direction `Gx`, par exemple, nous multiplions les pixels à droite du pixel cible par un nombre positif et les pixels à gauche du pixel cible par un nombre négatif. Lorsque nous prenons la somme, si les pixels à droite sont d'une couleur similaire aux pixels à gauche, le résultat sera proche de 0 (les nombres s'annulent). Mais si les pixels à droite sont très différents des pixels à gauche, alors la valeur résultante sera très positive ou très négative, indiquant un changement de couleur qui est probablement le résultat d'une limite entre les objets. Et un argument similaire est vrai pour le calcul des arêtes dans la direction `y`.

En utilisant ces noyaux, nous pouvons générer une valeur `Gx` et `Gy` pour chacun des canaux rouge, vert et bleu d'un pixel. Mais chaque canal ne peut prendre qu'une seule valeur, pas deux : nous avons donc besoin d'un moyen de combiner `Gx` et `Gy` en une seule valeur. L'algorithme du filtre de Sobel combine `Gx` et `Gy` en une valeur finale en calculant la racine carrée de `Gx^2 + Gy^2`. Et puisque les valeurs de canal ne peuvent prendre que des valeurs entières de 0 à 255, assurez-vous que la valeur résultante est arrondie à l'entier le plus proche et limitée à 255 !

Et que dire de la gestion des pixels à la bordure ou dans le coin de l'image ? Il existe de nombreuses façons de gérer les pixels à la bordure, mais pour les besoins de ce problème, nous vous demandons de considérer l'image comme s'il y avait une bordure noire solide de 1 pixel autour de l'image: donc, essayer d'accéder à un pixel au-delà de la bordure de l'image doit être traité comme un pixel noir solide (valeurs de 0 pour chacun des canaux rouge, vert et bleu). Cela ignorera efficacement ces pixels de nos calculs de `Gx` et `Gy`.

Démarrage
---------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-more.zip
    

afin de télécharger un ZIP appelé `filter-more.zip` dans votre espace de codes.

Ensuite, exécutez

    unzip filter-more.zip
    

pour créer un dossier appelé `filter-more`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm filter-more.zip
    

et répondre "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd filter-more
    

suivi de la touche Entrée pour vous déplacer dans ce répertoire (c'est-à-dire l'ouvrir). Votre invite devrait maintenant ressembler à ceci.

    filter-more/ $
    

Exécutez `ls` tout seul et vous devriez voir quelques fichiers : `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` et `Makefile`. Vous devriez également voir un dossier appelé "images" contenant quatre fichiers BMP. Si vous rencontrez des difficultés, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez fait une erreur !

Compréhension
-------------

Jetons maintenant un coup d'œil à certains des fichiers fournis en tant que code de distribution pour comprendre ce qu'ils contiennent.

### `bmp.h`

Ouvrez `bmp.h` (en double-cliquant dessus dans le navigateur de fichiers) et jetez-y un coup d'œil.

Vous verrez des définitions des en-têtes que nous avons mentionnés (`BITMAPINFOHEADER` et `BITMAPFILEHEADER`). De plus, ce fichier définit `BYTE`, `DWORD`, `LONG` et `WORD`, des types de données couramment utilisés dans le monde de la programmation Windows. Remarquez comment ils ne sont que des alias pour les types de données primitives avec lesquels vous êtes (espérons-le) déjà familier(e). Il semble que `BITMAPFILEHEADER` and `BITMAPINFOHEADER` utilisent ces types.

Le plus important pour vous, ce fichier définit également une "structure" appelée `RGBTRIPLE` qui, assez simplement, "encapsule" trois octets : un bleu, un vert, et un rouge (l'ordre, rappelons-le, dans lequel nous nous attendons à trouver les triplets RVB sur le disque).

Pourquoi sont ces structures utiles ? Eh bien, rappelez-vous qu'un fichier est juste une séquence d'octets (ou, en fin de compte, de bits) sur le disque. Mais ces octets sont généralement ordonnés de telle manière que les premiers représentent quelque chose, les suivants représentent quelque chose d'autre, et ainsi de suite. Les "formats de fichier" existent parce que le monde a standardisé ce que représentent ces octets. Maintenant, nous pourrions simplement lire un fichier du disque dans la RAM sous forme d'un tableau d'octets. Et nous pourrions simplement nous souvenir que l'octet à `array[i]` représente une chose, tandis que l'octet à `array[j]` représente une autre. Mais pourquoi ne pas donner des noms à certains de ces octets pour que nous puissions les récupérer plus facilement depuis la mémoire ? C'est précisément ce que les structures dans `bmp.h` nous permettent de faire. Au lieu de penser à un fichier comme une longue séquence d'octets, nous pouvons plutôt le considérer comme une séquence de structures.

### `filter.c`

Maintenant, ouvrons `filter.c`. Ce fichier a déjà été écrit pour vous, mais il y a quelques points importants à noter ici.

Tout d'abord, remarquez la définition de `filters` à la ligne 10. Cette chaîne de caractères indique au programme quels sont les arguments de ligne de commande autorisés pour le programme : `b`, `e`, `g` et `r`. Chacun d'eux spécifie un filtre différent que nous pouvons appliquer à nos images : flou, détection de bordure, niveaux de gris et réflexion.

Les lignes suivantes ouvrent un fichier image, s'assurent qu'il s'agit bien d'un fichier BMP, et lisent toutes les informations de pixels dans un tableau 2D appelé `image`.

Faites défiler jusqu'à l'instruction `switch` qui commence à la ligne 101. Remarquez que, selon le filtre que nous avons choisi, une fonction différente est appelée : si l'utilisateur choisit le filtre `b`, le programme appelle la fonction `blur`; si `e`, alors `edges` est appelé ; si `g`, alors `grayscale` est appelé ; et si `r`, alors `reflect` est appelé. Notez également que chacune de ces fonctions prend en argument la hauteur de l'image, la largeur de l'image et le tableau 2D de pixels.

Ce sont les fonctions que vous allez (bientôt !) implémenter. Comme vous pouvez l'imaginer, l'objectif est que chacune de ces fonctions modifie le tableau 2D de pixels de manière à appliquer le filtre souhaité à l'image.

Les lignes restantes du programme prennent l'image résultante et l'écrivent dans un nouveau fichier image.

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

Utilisation
-----------

Votre programme doit se comporter comme les exemples ci-dessous. `INFILE.bmp` est le nom de l'image d'entrée et `OUTFILE.bmp` est le nom de l'image résultante après l'application d'un filtre.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -e INFILE.bmp OUTFILE.bmp
```

Conseils
--------

* Les valeurs des composantes `rgbtRed`, `rgbtGreen` et `rgbtBlue` d'un pixel sont toutes des nombres entiers, assurez-vous donc d'arrondir tout nombre à virgule flottante au nombre entier le plus proche lors de leur affectation à une valeur de pixel !

Tests
-----

Assurez-vous de tester tous vos filtres sur les fichiers bitmap d'exemple fournis !

Exécutez ce qui suit pour évaluer la justesse de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester vous-même également !

    check50 cs50/problems/2023/x/filter/more
    

Exécutez ce qui suit pour évaluer le style de votre code en utilisant `style50`.

    style50 helpers.c
    

Comment soumettre
-----------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/filter/more"

