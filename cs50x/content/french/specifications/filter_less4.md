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