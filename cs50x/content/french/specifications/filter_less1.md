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