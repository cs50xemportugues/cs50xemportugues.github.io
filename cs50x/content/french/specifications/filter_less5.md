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