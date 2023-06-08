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