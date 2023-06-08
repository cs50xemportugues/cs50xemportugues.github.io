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