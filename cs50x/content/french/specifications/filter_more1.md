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