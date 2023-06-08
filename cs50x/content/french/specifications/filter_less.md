Filtre
======

Implémentez un programme qui applique des filtres à BMP, comme ci-dessous.

    $ ./filter -r IMAGE.bmp REFLECTED.bmp
    

où `IMAGE.bmp` est le nom d'un fichier image et `REFLECTED.bmp` est le nom donné à un fichier image de sortie, maintenant réfléchi.

Contexte
----------

### Bitmaps

Peut-être la façon la plus simple de représenter une image est avec une grille de pixels (c'est-à-dire, des points), chacun pouvant être d'une couleur différente. Pour les images en noir et blanc, nous avons donc besoin de 1 bit par pixel, car 0 peut représenter le noir et 1 peut représenter le blanc, comme dans l'exemple ci-dessous.

![une bitmap simple](https://cs50.harvard.edu/x/2023/psets/4/filter/less/bitmap.png)

Dans ce sens, une image est simplement une bitmap (c'est-à-dire, une carte de bits). Pour les images plus colorées, vous avez simplement besoin de plus de bits par pixel. Un format de fichier (comme [BMP](https://fr.wikipedia.org/wiki/BMP_(format_d%27image)) ,[JPEG](https://fr.wikipedia.org/wiki/JPEG) ou [PNG](https://fr.wikipedia.org/wiki/Portable_Network_Graphics)) qui prend en charge une couleur "24 bits" utilise 24 bits par pixel. (BMP prend en charge 1, 4, 8, 16, 24 et 32 bits de couleur.)

Un BMP 24 bits utilise 8 bits pour indiquer la quantité de rouge dans la couleur d'un pixel, 8 bits pour indiquer la quantité de vert dans la couleur d'un pixel et 8 bits pour indiquer la quantité de bleu dans la couleur d'un pixel. Si les valeurs R, G et B de certains pixels dans un BMP sont, disons, `0xff`, `0x00` et `0x00` en hexadécimal, ce pixel est purement rouge, car `0xff` (également connu sous le nom de `255` décimal) implique « beaucoup de rouge », tandis que `0x00` et `0x00` impliquent « pas de vert » et « pas de bleu », respectivement.

### Un Peu Plus Technique (bitmap)

Rappelez-vous qu'un fichier est simplement une séquence de bits, disposés de quelque manière que ce soit. Un fichier BMP 24 bits est donc essentiellement une séquence de bits, dont presque toutes les 24 parties représentent la couleur d'un pixel. Mais un fichier BMP contient également des "métadonnées", des informations telles que la hauteur et la largeur d'une image. Ces métadonnées sont stockées au début du fichier sous la forme de deux structures de données généralement appelées «entêtes», à ne pas confondre avec les fichiers d'en-tête en C. (Incidentalement, ces en-têtes ont évolué au fil du temps. Ce problème utilise la dernière version du format BMP de Microsoft, 4.0, qui a été lancée avec Windows 95.)

Le premier de ces en-têtes, appelé `BITMAPFILEHEADER`, mesure 14 octets de long. (Rappelez-vous qu'1 octet est égal à 8 bits.) Le second de ces en-têtes, appelé `BITMAPINFOHEADER`, fait 40 octets de long. Immédiatement après ces en-têtes se trouve la bitmap réelle: un tableau d'octets, dont les triplets représentent la couleur d'un pixel. Cependant, les BMP stockent ces triplets à l'envers (c'est-à-dire, BGR), avec 8 bits pour le bleu, suivis de 8 bits pour le vert, suivis de 8 bits pour le rouge. (Certaines BMP stockent également la bitmap entière à l'envers, avec la rangée supérieure d'une image à la fin du fichier BMP. Mais nous avons stocké les BMP de ce problème comme décrit ici, avec la première rangée de chaque bitmap en haut et la dernière rangée en bas.) En d'autres termes, si nous voulions convertir le smiley à 1 bit ci-dessus en un smiley à 24 bits, en remplaçant le noir par le rouge, un BMP 24 bits stockerait cette bitmap comme suit, où `0000ff` signifie rouge et `ffffff` signifie blanc; nous avons mis en surbrillance en rouge toutes les occasions de `0000ff`.

![sourire rouge](https://cs50.harvard.edu/x/2023/psets/4/filter/less/red_smile.png)

Parce que nous avons présenté ces bits de gauche à droite, de haut en bas, en 8 colonnes, vous pouvez réellement voir le smiley rouge si vous prenez du recul.

Pour être clair, rappelez-vous qu'un chiffre hexadécimal représente 4 bits. Par conséquent, `ffffff` en hexadécimal signifie en fait `111111111111111111111111` en binaire.

Notez que vous pourriez représenter une bitmap comme un tableau 2D de pixels: où l'image est un tableau de rangées, chaque rangée est un tableau de pixels. En effet, c'est ainsi que nous avons choisi de représenter les images bitmap dans ce problème.

### Filtrage d'images

Que signifie même filtrer une image? Vous pouvez penser au filtrage d'une image comme prendre les pixels d'une image originale et modifier chaque pixel de sorte qu'un effet particulier soit apparent dans l'image résultante.

#### Niveaux de Gris

Un filtre commun est le filtre «niveaux de gris», où nous prenons une image et voulons la convertir en noir et blanc. Comment cela fonctionne-t-il?

Rappelez-vous que si les valeurs de rouge, vert et bleu sont toutes fixées à `0x00` (hexadécimal pour `0`), alors le pixel est noir. Et si toutes les valeurs sont fixées à `0xff` (hexadécimal pour `255`), alors le pixel est blanc. Tant que les valeurs de rouge, vert et bleu sont toutes égales, le résultat sera des nuances de gris le long du spectre noir-blanc, avec des valeurs plus élevées signifiant des nuances plus claires (plus proches du blanc) et des valeurs plus basses signifiant des nuances plus sombres (plus proches du noir).

Ainsi, pour convertir un pixel en niveaux de gris, nous devons simplement nous assurer que les valeurs de rouge, vert et bleu sont toutes la même valeur. Mais comment savons-nous quelle valeur leur donner ? Eh bien, il est raisonnable de s'attendre à ce que si les valeurs de rouge, de vert et de bleu originales étaient toutes assez élevées, alors la nouvelle valeur devrait également être assez élevée. Et si les valeurs originales étaient toutes basses, alors la nouvelle valeur devrait également être basse.

En fait, pour s'assurer que chaque pixel de la nouvelle image a toujours la même luminosité générale ou la même obscurité que l'ancienne image, nous pouvons prendre la moyenne des valeurs de rouge, de vert et de bleu pour déterminer quelle nuance de gris donner au nouveau pixel.

Si vous appliquez cela à chaque pixel de l'image, le résultat sera une image convertie en niveaux de gris.

#### Sépia

La plupart des logiciels de retouche d'image prennent en charge un filtre "sépia", qui donne aux images un aspect ancien en les colorant d'une teinte rouge-brun.

Une image peut être convertie en sépia en prenant chaque pixel et en calculant de nouvelles valeurs rouge, verte et bleue en fonction des valeurs originales des trois.

Il existe plusieurs algorithmes pour convertir une image en sépia, mais pour ce problème, nous vous demanderons d'utiliser l'algorithme suivant. Pour chaque pixel, les valeurs de couleur sépia doivent être calculées en fonction des valeurs de couleur d'origine selon les instructions ci-dessous.

      sepiaRouge = 0,393 * originalRouge + 0,769 * originalVert + 0,189 * originalBleu
      sepiaVert = 0,349 * originalRouge + 0,686 * originalVert + 0,168 * originalBleu
      sepiaBleu = 0,272 * originalRouge + 0,534 * originalVert + 0,131 * originalBleu
    

Bien sûr, le résultat de chacune de ces formules peut ne pas être un entier, mais chaque valeur pourrait être arrondie à l'entier le plus proche. Il est aussi possible que le résultat de la formule soit un nombre supérieur à 255, la valeur maximale pour une valeur de couleur sur 8 bits. Dans ce cas, les valeurs rouge, verte et bleue doivent être limitées à 255. En conséquence, nous pouvons garantir que les valeurs de rouge, verte et bleue obtenues seront des nombres entiers compris entre 0 et 255 inclus.

#### Réflexion

Certains filtres peuvent également déplacer des pixels. La réflexion d'une image, par exemple, est un filtre où l'image résultante est celle que vous obtiendriez en plaçant l'image originale devant un miroir. Ainsi, tous les pixels du côté gauche de l'image se retrouveront à droite, et vice versa.

Notez que tous les pixels originaux de l'image originale seront toujours présents dans l'image réfléchie, c'est juste qu'ils peuvent être repositionnés dans un endroit différent dans l'image.

#### Flou

Il existe plusieurs façons de créer l'effet de flou ou d'adoucir une image. Pour ce problème, nous utiliserons le "flou de boîte", qui consiste à prendre chaque pixel et à donner à chaque valeur de couleur une nouvelle valeur en faisant la moyenne des valeurs de couleur des pixels voisins.

Considérons la grille de pixels suivante, où nous avons numéroté chaque pixel.

![a grid of pixels](https://cs50.harvard.edu/x/2023/psets/4/filter/less/grid.png)

La nouvelle valeur de chaque pixel serait la moyenne des valeurs de tous les pixels qui sont dans une même rangée et colonne qui l'entourent (formant une boîte de 3x3). Par exemple, chacune des valeurs de couleur du pixel 6 serait obtenue en faisant la moyenne des valeurs de couleur d'origine des pixels 1, 2, 3, 5, 6, 7, 9, 10 et 11 (notez que le pixel 6 lui-même est inclus dans la moyenne). De même, les valeurs de couleur du pixel 11 seraient obtenues en faisant la moyenne des valeurs de couleur des pixels 6, 7, 8, 10, 11, 12, 14, 15 et 16.

Pour un pixel le long d'un bord ou d'un coin, comme le pixel 15, nous chercherions toujours tous les pixels dans une même rangée et colonne : dans ce cas, les pixels 10, 11, 12, 14, 15, et 16.

Commencer
---------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit:

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-less.zip
    

pour télécharger un fichier ZIP appelé `filter-less.zip` dans votre espace de code.

Ensuite, exécutez

    unzip filter-less.zip
    

pour créer un dossier appelé `filter-less`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm filter-less.zip
    

et répondez "y" suivi de la touche Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd filter-less
    

suivi de la touche Entrée pour vous déplacer dans (c'est-à-dire, ouvrir) ce répertoire. Votre invite doit maintenant ressembler à ce qui suit.

    filter-less/ $
    

Exécutez `ls` tout seul, et vous devriez voir quelques fichiers : `bmp.h`, `filter.c`, `helpers.h`, `helpers.c`, et `Makefile`. Vous devriez également voir un dossier appelé `images` avec quatre fichiers BMP. Si vous avez des difficultés, suivez ces mêmes étapes à nouveau et voyez si vous pouvez déterminer où vous avez fait une erreur !

Compréhension
-------------

Jetons un coup d'œil à certains des fichiers fournis en tant que code de distribution pour comprendre ce qu'ils contiennent.

### `bmp.h`

Ouvrez `bmp.h` (en double-cliquant dessus dans le navigateur de fichiers) et jetez-y un coup d'œil.

Vous y trouverez les définitions des en-têtes que nous avons mentionnés (`BITMAPINFOHEADER` et `BITMAPFILEHEADER`). En outre, ce fichier définit les types de données `BYTE`, `DWORD`, `LONG` et` WORD`, que l'on trouve normalement dans le monde de la programmation Windows. Remarquez comment ils ne sont que des alias pour les primitives que vous connaissez déjà. `BITMAPFILEHEADER` et `BITMAPINFOHEADER` utilisent apparemment ces types.

Ce fichier définit également une `struct` appelée `RGBTRIPLE` qui "encapsule" simplement trois octets : un bleu, un vert et un rouge (l'ordre, rappelons-le, dans lequel nous nous attendons à trouver les triples RGB sur le disque).

Pourquoi ces `structs` sont-elles utiles ? Eh bien, rappelons-nous qu'un fichier n'est qu'une séquence d'octets (ou, en fin de compte, de bits) sur le disque. Mais ces octets sont généralement ordonnés de manière à ce que les premiers représentent quelque chose, les suivants représentent autre chose, et ainsi de suite. Les "formats de fichier" existent parce que le monde a normalisé la signification des octets. Nous pourrions simplement lire un fichier du disque dans la RAM en tant qu'un seul grand tableau d'octets. Et nous pourrions simplement nous rappeler que l'octet à `array[i]` représente une chose, tandis que l'octet à `array[j]` en représente une autre. Mais pourquoi ne pas donner des noms à certains de ces octets pour que nous puissions les récupérer plus facilement de la mémoire ? C'est précisément ce que nous permettent de faire les `structs` dans `bmp.h`. Au lieu de penser à un fichier comme une longue séquence d'octets, nous pouvons plutôt le considérer comme une séquence de `structs`.

### `filter.c`

Maintenant, ouvrez `filter.c`. Ce fichier vous est déjà fourni, mais il y a quelques points importants à noter.

Tout d'abord, notez la définition de `filters` à la ligne 10. Cette chaîne de caractères indique au programme quels sont les arguments de ligne de commande autorisés : `b`,`g`,`r` et `s`. Chacun d'eux spécifie un filtre différent que nous pouvons appliquer à nos images : flou, niveau de gris, réflexion et sépia.

Les lignes suivantes ouvrent un fichier image, s'assurent qu'il s'agit bien d'un fichier BMP, et lisent toutes les informations de pixel dans un tableau 2D appelé `image`.

Faites défiler jusqu'à la déclaration `switch` qui commence à la ligne 101. Remarquez que, selon le filtre que nous avons choisi, une fonction différente est appelée : si l'utilisateur choisit le filtre `b`, le programme appelle la fonction `blur` ; si `g`, alors `grayscale` est appelé ; si `r`, alors `reflect` est appelé ; et si `s`, alors `sepia` est appelé. Remarquez également que chacune de ces fonctions prend comme arguments la hauteur de l'image, la largeur de l'image et le tableau 2D de pixels.

Ce sont les fonctions que vous allez bientôt implémenter. Comme vous pouvez l'imaginer, le but est que chacune de ces fonctions modifie le tableau 2D de pixels de manière à ce que le filtre désiré soit appliqué à l'image.

Les lignes restantes du programme prennent l'image résultante et les écrivent dans un nouveau fichier image.

### `helpers.h`

Ensuite, jetons un coup d'œil à `helpers.h`. Ce fichier est assez court et ne fournit que les prototypes de fonctions pour les fonctions que vous avez vues plus tôt.

Notez ici que chaque fonction prend un tableau 2D appelé `image` en argument, où `image` est un tableau de `height` lignes, et chaque ligne est elle-même un autre tableau de `width` `RGBTRIPLE`s. Donc, si `image` représente l'ensemble de l'image, alors `image[0]` représente la première ligne, et `image[0][0]` représente le pixel dans le coin supérieur gauche de l'image.

### `helpers.c`

Maintenant, ouvrez `helpers.c`. C'est ici que l'implémentation des fonctions déclarées dans `helpers.h` se trouve. Mais notez que, pour l'instant, les implémentations sont manquantes ! Cette partie dépend de vous.

### `Makefile`

Enfin, regardons `Makefile`. Ce fichier spécifie ce qui doit se passer lorsque nous exécutons une commande de terminal comme `make filter`. Alors que les programmes que vous avez pu écrire auparavant étaient limités à un seul fichier, `filter` semble utiliser plusieurs fichiers : `filter.c` et `helpers.c`. Nous devrons donc dire à `make` comment compiler ce fichier.

Essayez de compiler `filter` vous-même en allant dans votre terminal et en exécutant 

    $ make filter
    

Ensuite, vous pouvez exécuter le programme en exécutant :

    $ ./filter -g images/yard.bmp out.bmp
    

qui prend l'image à `images/yard.bmp`, et génère une nouvelle image appelée `out.bmp` après avoir exécuté les pixels à travers la fonction `grayscale`. Les `grayscale` ne font rien pour l'instant, donc l'image de sortie devrait ressembler à l'image originale de la cour.

Spécification
-------------

Implémentez les fonctions dans `helpers.c` de telle sorte qu'un utilisateur puisse appliquer des filtres de niveaux de gris, de sépia, de réflexion ou de flou à ses images.

*   La fonction `grayscale` doit prendre une image et la transformer en une version noir et blanc de la même image.
*   La fonction `sepia` doit prendre une image et la transformer en une version sépia de la même image.
*   La fonction `reflect` doit prendre une image et la refléter horizontalement.
*   Enfin, la fonction `blur` doit prendre une image et la transformer en une version floue en boite de la même image.

Vous ne devez pas modifier les signatures des fonctions, ni modifier d'autres fichiers que `helpers.c`.

Procédure pas à pas
--------------------

**Veuillez noter qu'il y a 5 vidéos dans cette playlist.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/K0v9byp9jd0?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut"></iframe></div>


Utilisation
-----------

Votre programme doit fonctionner comme dans les exemples ci-dessous. `INFILE.bmp` est le nom de l'image d'entrée et `OUTFILE.bmp` est le nom de l'image résultante après l'application d'un filtre.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -s INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```

Conseils
--------

* Les valeurs des composantes `rgbtRed`, `rgbtGreen` et `rgbtBlue` d'un pixel sont toutes des entiers, assurez-vous donc d'arrondir tous les nombres à virgule flottante au nombre entier le plus proche lors de leur attribution à une valeur de pixel !
* Lorsque vous implémentez la fonction `grayscale`, vous devrez faire la moyenne des valeurs de 3 entiers. Pourquoi pourriez-vous vouloir diviser la somme de ces entiers par 3,0 et non par 3 ?
* Dans la fonction `reflect`, vous devrez échanger les valeurs des pixels des côtés opposés d'une ligne. Rappelez-vous de la façon dont nous avons implémenté l'échange de deux valeurs à l'aide d'une variable temporaire en cours de lecture. Pas besoin d'utiliser une fonction distincte pour l'échange, à moins que vous ne le souhaitiez !
* Comment une fonction qui retourne le moindre de deux entiers pourrait-elle être utile lors de la mise en œuvre de `sepia`, en particulier lorsque vous devez vous assurer que la valeur d'une couleur ne dépasse pas 255 ?
* Lors de la mise en œuvre de la fonction `blur`, vous pourriez constater qu'un flou d'un pixel finit par affecter le flou d'un autre pixel. Vous pourriez peut-être créer une copie de l'image (le troisième argument de la fonction) en déclarant un nouveau tableau (bidimensionnel) avec du code comme `RGBTRIPLE copy[height][width];` et en copiant `image` dans `copy`, pixel par pixel, avec des boucles `for` imbriquées ? Et puis lire les couleurs des pixels à partir de `copy` mais écrire (c'est-à-dire, changer) les couleurs des pixels dans `image` ?

Tests
-----

Assurez-vous de tester tous les filtres sur les fichiers bitmap d'exemple fournis !

Exécutez les commandes ci-dessous pour évaluer la justesse de votre code avec `check50`. Mais assurez-vous également de le compiler et de le tester vous-même !

    check50 cs50/problems/2023/x/filter/less
    

Exécutez les commandes ci-dessous pour évaluer le style de votre code avec `style50`.

    style50 helpers.c
    

Comment soumettre
-----------------

Dans votre terminal, exécutez la commande suivante pour soumettre votre travail.

    submit50 cs50/problems/2023/x/filter/less"

