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