Conseils
--------

Pour comparer deux chaînes de caractères sans distinction de casse, vous pouvez utiliser [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (déclaré dans `strings.h`) ! Vous voudrez également vous assurer que votre fonction de hachage ne fait pas de distinction de casse, de sorte que `foo` et `FOO` aient la même valeur de hachage.

En fin de compte, veillez à libérer dans `décharger` toute mémoire que vous avez allouée dans `charger` ! Rappelez-vous que `valgrind` est votre nouvel ami. Sachez que `valgrind` recherche des fuites de mémoire pendant l'exécution réelle de votre programme, donc assurez-vous de fournir des arguments en ligne de commande si vous voulez que `valgrind` analyse `speller` lorsque vous utilisez un dictionnaire et/ou un texte particulier, comme ci-dessous. Il vaut mieux utiliser un petit texte, sinon `valgrind` pourrait prendre beaucoup de temps pour s'exécuter.

    valgrind ./speller texts/cat.txt
    

Si vous exécutez `valgrind` sans spécifier de `texte` pour `speller`, vos implémentations de `charger` et `décharger` ne seront pas réellement appelées (et donc pas analysées).

Si vous n'êtes pas sûr de savoir comment interpréter la sortie de `valgrind`, demandez simplement de l'aide à `help50` :

    help50 valgrind ./speller texts/cat.txt
    

Test
----

Comment vérifier si votre programme détecte correctement les mots mal orthographiés ? Vous pouvez consulter les "réponses" qui se trouvent dans le répertoire `keys` qui est à l'intérieur de votre répertoire `speller`. Par exemple, à l'intérieur de `keys/lalaland.txt`, se trouvent tous les mots que votre programme doit considérer comme mal orthographiés.

Vous pouvez donc exécuter votre programme sur un texte dans une fenêtre, comme ci-dessous.

    ./speller texts/lalaland.txt
    

Et vous pouvez ensuite exécuter la solution de l'équipe sur le même texte dans une autre fenêtre, comme ci-dessous.

    ./speller50 texts/lalaland.txt
    

Et vous pouvez ensuite comparer les deux fenêtres visuellement côte à côte. Cela pourrait devenir fastidieux rapidement, cependant. Vous pouvez donc préférer "rediriger" la sortie de votre programme vers un fichier, comme ci-dessous.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt
    

Vous pouvez ensuite comparer les deux fichiers côte à côte dans la même fenêtre avec un programme comme `diff`, comme ci-dessous.

    diff -y student.txt staff.txt
    

Alternativement, pour gagner du temps, vous pouvez simplement comparer la sortie de votre programme (en supposant que vous l'avez redirigée vers, par exemple, `student.txt`) avec l'une des "réponses" sans exécuter la solution de l'équipe, comme ci-dessous.

    diff -y student.txt keys/lalaland.txt
    

Si la sortie de votre programme correspond à celle de l'équipe, `diff` affichera deux colonnes qui devraient être identiques, à l'exception peut-être des temps d'exécution en bas. Si les colonnes diffèrent, vous verrez un `>` ou un `|` là où elles diffèrent. Par exemple, si vous voyez

    MOTS MAL ORTHOGRAPHIÉS                                           MOTS MAL ORTHOGRAPHIÉS
    
    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L
    

cela signifie que votre programme (dont la sortie est à gauche) ne considère pas que `Thelonious` ou `MIA` est mal orthographié, même si la sortie de l'équipe (à droite) le fait, comme le suggère l'absence, par exemple, de `Thelonious` dans la colonne de gauche et la présence de `Thelonious` dans la colonne de droite.

### `check50`

Pour tester votre code de manière moins manuelle (bien que pas exhaustive), vous pouvez également exécuter ce qui suit.

    check50 cs50/problems/2023/x/speller
    

Notez que `check50` vérifiera également les fuites de mémoire, alors assurez-vous d'avoir exécuté `valgrind` également.

### style50

Exécutez ce qui suit pour évaluer le style de votre code à l'aide de `style50`.

    style50 dictionary.c
    

Solution de l'équipe
----------------

Comment évaluer à quelle vitesse (et avec quelle exactitude) votre code fonctionne-t-il ? Eh bien, comme toujours, n'hésitez pas à jouer avec la solution de l'équipe, comme ci-dessous, et à comparer ses résultats aux vôtres.

    ./speller50 texts/lalaland.txt
    

Comment soumettre
-----------------

Dans votre terminal, exécutez le code suivant pour soumettre votre travail.

    submit50 cs50/problems/2023/x/speller"