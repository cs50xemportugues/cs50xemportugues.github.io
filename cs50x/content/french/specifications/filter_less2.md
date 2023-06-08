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