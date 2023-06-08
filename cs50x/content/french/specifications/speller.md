Correcteur d'orthographe
=======

<div class="alert" data-alert="danger" role="alert"><p><strong>Assurez-vous de lire cette spécification dans son intégralité avant de commencer pour savoir quoi faire et comment le faire !</strong></p></div>


Pour ce problème, vous allez implémenter un programme qui vérifie l'orthographe d'un fichier à l'aide d'une table de hachage, comme ci-dessous.

    $ ./speller texts/lalaland.txt
    MOTS MAL ÉPELLÉS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    MOTS MAL ÉPELLÉS :
    MOTS DANS LE DICTIONNAIRE :
    MOTS DANS LE TEXTE :
    TEMPS DE CHARGEMENT :
    TEMPS DE VÉRIFICATION :
    TAILLE :
    TEMPS DE DÉCHARGEMENT :
    TEMPS TOTAL :
    

Pour commencer
---------------

Connectez-vous à [code.cs50.io] (https://code.cs50.io/) , cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez voir que l'invite de votre fenêtre de terminal ressemble à celle ci-dessous :

    $
    
Ensuite, exécutez la commande suivante :

   wget https://cdn.cs50.net/2022/fall/psets/5/speller.zip
    
pour télécharger un fichier ZIP appelé `speller.zip` dans votre espace de code.

Ensuite, exécutez

    unzip speller.zip
    
pour créer un dossier appelé `speller`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm speller.zip
    
et répondre "y" suivi de la touche Entrée à l'invite de commande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant tapez

    cd speller
    
suivi de la touche Entrée pour vous déplacer dans ce répertoire. Votre invite de commande doit maintenant ressembler à celle ci-dessous.

    speller/ $

Exécutez `ls` tout seul, et vous devriez voir quelques fichiers et dossiers :

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
    
Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur !

Distribution
------------

### Comprendre

Théoriquement, un algorithme qui a une durée d'exécution de _n_ sur une entrée de taille _n_ est « asymptotiquement équivalent », en termes de _O_, à un algorithme qui a une durée d'exécution de _2n_. En effet, lorsqu'on décrit la durée d'exécution d'un algorithme, on se concentre généralement sur le terme dominant (c'est-à-dire le terme le plus impactant) (_n_ dans ce cas puisque _n_ peut être beaucoup plus grand que 2). Dans le monde réel, cependant, la durée d'exécution de _2n_ semble deux fois plus lente que celle de _n_.

Le défi qui vous attend consiste à implémenter le vérificateur d'orthographe le plus rapide possible ! Par « plus rapide », nous parlons du temps réel d'exécution du programme, pas seulement de son temps asymptotique.

Dans `speller.c`, nous avons mis en place un programme conçu pour vérifier l'orthographe d'un fichier après avoir chargé un dictionnaire de mots du disque en mémoire. Ce dictionnaire, pour sa part, est implémenté dans un fichier appelé `dictionary.c`. (Il pourrait simplement être implémenté dans `speller.c`, mais à mesure que les programmes deviennent plus complexes, il est souvent pratique de les diviser en plusieurs fichiers.) Les prototypes des fonctions dans ces fichiers sont définis dans `dictionary.h` plutôt que dans `dictionary.c` lui-même. De cette façon, `speller.c` et `dictionary.c` peuvent tous deux inclure le fichier. Malheureusement, nous n'avons pas tout à fait réussi à implémenter la partie de chargement. Ou la partie de vérification. Nous vous laissons les deux (et un peu plus) à vous de les implémenter ! Mais d'abord, une visite guidée.

#### `dictionary.h`

Ouvrez `dictionary.h` et vous verrez une nouvelle syntaxe, y compris quelques lignes qui mentionnent `DICTIONARY_H`. Il n'y a pas besoin de s'en préoccuper, mais si vous êtes curieux, ces lignes garantissent que, même si `dictionary.c` et` speller.c` (que vous verrez bientôt) incluent ce fichier, `clang` ne le compilera qu'une seule fois.

Ensuite, remarquez comment nous incluons un fichier appelé` stdbool.h`. C'est le fichier dans lequel `bool` lui-même est défini. Vous n'en aviez pas besoin auparavant, car la bibliothèque CS50 « #include » cela pour vous.

Remarquez également notre utilisation de `#define`, une « directive de préprocesseur » qui définit une « constante » appelée `LENGTH` ayant une valeur de `45`. C'est une constante dans le sens où vous ne pouvez pas le changer (accidentellement) dans votre propre code. En fait, `clang` remplacera toutes les mentions de `LENGTH` dans votre propre code par `45`. En d'autres termes, ce n'est pas une variable, juste un truc de find-and-replace.

Enfin, remarquez les prototypes des cinq fonctions : `check`, `hash`, `load`, `size` et `unload`. Remarquez comment trois d'entre eux prennent un pointeur en argument, comme indiqué par `*` :

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>
    

Rappelez-vous que `char *` est ce que nous utilisions pour appeler `string`. Ainsi, ces trois prototypes sont simplement :

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>

Et `const`, quant à lui, signifie simplement que ces chaînes, lorsqu'elles sont transmises en tant qu'arguments, doivent rester constantes, vous ne pourrez pas les modifier, accidentellement ou autrement!

#### `dictionary.c`

Maintenant, ouvrez `dictionary.c`. Remarquez comment, en haut du fichier, nous avons défini une structure appelée `node` qui représente un nœud dans une table de hachage. Nous avons également déclaré un tableau de pointeurs de type global `table`, qui représentera (bientôt) la table de hachage que vous utiliserez pour suivre les mots dans le dictionnaire. Le tableau contient des pointeurs de nœuds `N`, et nous avons fixé `N` à `26` pour le moment, pour correspondre à la fonction de hachage par défaut décrite ci-dessous. Vous voudrez probablement l'augmenter en fonction de votre propre implémentation de la fonction de hachage.

Ensuite, remarquez que nous avons implémenté `load`, `check`, `size` et `unload`, mais à peine, juste assez pour que le code compile. Remarquez également que nous avons implémenté la fonction de hachage avec un algorithme d'exemple basé sur la première lettre du mot. Votre travail, en fin de compte, est de réimplémenter ces fonctions de la manière la plus intelligente possible afin que ce correcteur d'orthographe fonctionne comme annoncé. Et rapidement!

#### `speller.c`

Ensuite, ouvrez `speller.c` et passez du temps à parcourir le code et les commentaires qui y figurent. Vous n'aurez pas besoin de modifier quoi que ce soit dans ce fichier, et vous n'avez pas besoin de comprendre son intégralité, mais essayez malgré tout de vous faire une idée de sa fonctionnalité. Remarquez comment, au moyen d'une fonction appelée `getrusage`, nous allons "benchmark" (c'est-à-dire chronométrer l'exécution de) vos implémentations de `check`, `load`, `size` et `unload`. Remarquez également comment nous passons `check`, mot par mot, le contenu d'un fichier à vérifier. En fin de compte, nous signalons chaque faute d'orthographe dans ce fichier avec une multitude de statistiques.

Remarquez, au passage, que nous avons défini l'utilisation de `speller` comme suit :

    Usage: speller [dictionary] text

où le dictionnaire est supposé être un fichier contenant une liste de mots en minuscules, un par ligne, et le texte est un fichier à vérifier l'orthographe. Comme le suggèrent les crochets, la fourniture d'un dictionnaire est facultative ; si cet argument est omis, `speller` utilisera `dictionaries/large` par défaut. En d'autres termes, en exécutant

    ./speller text

sera équivalent à l'exécution de

    ./speller dictionaries/large text

où le texte est le fichier que vous souhaitez vérifier l'orthographe. Il va sans dire que la première commande est plus facile à entrer! (Bien sûr, `speller` ne pourra pas charger de dictionnaires tant que vous n'aurez pas implémenté `load` dans `dictionary.c`! Jusque-là, vous verrez `Could not load`.)

Dans le dictionnaire par défaut, il y a 143 091 mots, tous doivent être chargés en mémoire! En fait, jetez un coup d'œil à ce fichier pour avoir une idée de sa structure et de sa taille. Remarquez que chaque mot de ce fichier apparaît en minuscules (même, pour simplifier, les noms propres et les acronymes). Le fichier est trié de haut en bas dans l'ordre lexicographique, avec un seul mot par ligne (chacun se terminant par `\n`). Aucun mot ne dépasse 45 caractères et aucun mot ne se répète. Au cours du développement, vous pouvez trouver utile de fournir à `speller` un dictionnaire contenant beaucoup moins de mots, afin de ne pas vous battre avec une structure autrement énorme en mémoire. Dans `dictionaries/small` se trouve un tel dictionnaire. Pour l'utiliser, exécutez

    ./speller dictionaries/small text

où le texte est le fichier que vous souhaitez vérifier l'orthographe. N'avancez pas avant d'être sûr de comprendre comment fonctionne `speller` lui-même!

Il y a de fortes chances que vous n'ayez pas assez pris le temps de bien parcourir `speller.c`. Allez en arrière et parcourez-le à nouveau!

#### `texts/`

Afin que vous puissiez tester votre implémentation de `speller`, nous vous avons également fourni une grande quantité de textes, dont le script de _La La Land_, le texte de la loi sur les soins abordables, trois millions d'octets issus de Tolstoï, des extraits des _Federalist Papers_ et de Shakespeare, et plus encore. Afin que vous sachiez à quoi vous attendre, ouvrez et parcourez chacun de ces fichiers, qui se trouvent tous dans un répertoire appelé `texts` dans votre répertoire `pset5`.

Maintenant, comme vous devriez le savoir en ayant soigneusement lu `speller.c`, la sortie de `speller`, si elle est exécutée avec, disons,

    ./speller texts/lalaland.txt

ressemblera finalement à ce qui suit.

Voici une partie de la sortie que vous verrez. Pour information, nous avons cité quelques exemples de "mots mal orthographiés". Et afin de ne pas gâcher le plaisir, nous avons omis nos propres statistiques pour le moment.

    MISSPELLED WORDS

    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]

`WORDS MISSPELLED` représente le nombre de mots mal orthographiés. `WORDS IN DICTIONARY` représente le nombre de mots qui ont été correctement chargés dans la mémoire à partir du dictionnaire. `WORDS IN TEXT` représente le nombre total de mots dans le texte. `TIME IN load` représente le nombre de secondes que `speller` passe à exécuter votre implémentation de `load`. `TIME IN check` représente le nombre de secondes que `speller` passe à exécuter votre implémentation de `check`. `TIME IN size` représente le nombre de secondes que `speller` passe à exécuter votre implémentation de `size`. `TIME IN unload` représente le nombre de secondes que `speller` passe à exécuter votre implémentation de `unload`. `TIME IN TOTAL` est la somme de ces quatre mesures.

**Notez que ces temps peuvent varier quelque peu selon les exécutions de `speller`, en fonction de ce que fait par ailleurs votre espace de codage, même si vous ne modifiez pas votre code.**

À titre accessoire, pour être clair, par "mal orthographié", nous entendons simplement qu'un mot ne se trouve pas dans le `dictionnaire` fourni.

#### `Makefile`

Et enfin, souvenez-vous que `make` automatise la compilation de votre code afin que vous n'ayez pas à exécuter `clang` manuellement avec une kyrielle de commutateurs. Cependant, à mesure que vos programmes augmentent en taille, `make` ne pourra plus déduire du contexte la manière de compiler votre code; vous devrez commencer à dire à `make` comment compiler votre programme, notamment lorsqu'il s'agit de plusieurs fichiers source (c'est-à-dire `.c`), comme dans le cas de ce problème. Nous utiliserons donc un `Makefile`, un fichier de configuration qui indique à `make` exactement quoi faire. Ouvrez `Makefile`, et vous devriez voir quatre lignes :

1. La première ligne indique à `make` d'exécuter les lignes suivantes chaque fois que vous exécutez `make speller` (ou simplement `make`).
2. La deuxième ligne indique à `make` comment compiler `speller.c` en code machine (c'est-à-dire `speller.o`).
3. La troisième ligne indique à `make` comment compiler `dictionary.c` en code machine (c'est-à-dire `dictionary.o`).
4. La quatrième ligne indique à `make` de lier `speller.o` et `dictionary.o` dans un fichier appelé `speller`.

**Assurez-vous de compiler `speller` en exécutant `make speller` (ou simplement `make`). L'exécution de `make dictionary` ne fonctionnera pas !**

Spécification
-------------

Bon, le défi qui vous attend maintenant est d'implémenter, dans l'ordre, `load`, `hash`, `size`, `check` et `unload` de la manière la plus efficace possible en utilisant une table de hachage de telle sorte que `TIME IN load`, `TIME IN check`, `TIME IN size` et `TIME IN unload` soient tous minimisés. Il n'est pas évident de savoir ce que cela signifie d'être minimisé, étant donné que ces mesures varieront certainement selon les valeurs que vous donnez à `dictionary` et à `text`. C'est là que réside le défi, si ce n'est pas le plaisir, de ce problème. Ce problème est votre chance de concevoir. Bien que nous vous invitons à minimiser l'espace, votre ennemi ultime est le temps. Mais avant de plonger dedans, voici quelques spécifications de notre part.

* Vous ne pouvez pas modifier `speller.c` ou `Makefile`.
* Vous pouvez modifier `dictionary.c` (et, en fait, vous devez le faire pour pouvoir implémenter `load`, `hash`, `size`, `check` et `unload`), mais vous ne pouvez pas modifier les déclarations (c'est-à-dire les prototypes) de `load`, `hash`, `size`, `check` ou `unload`. Vous pouvez toutefois ajouter de nouvelles fonctions et des variables (locales ou globales) à `dictionary.c`.
* Vous pouvez modifier la valeur de `N` dans `dictionary.c`, de sorte que votre table de hachage peut avoir plus de seaux.
* Vous pouvez modifier `dictionary.h`, mais vous ne pouvez pas modifier les déclarations de `load`, `hash`, `size`, `check` ou `unload`.
* Votre implémentation de `check` doit être insensible à la casse. En d'autres termes, si `foo` est dans le dictionnaire, alors `check` doit retourner vrai pour toute capitalisation qui s'y rapporte; aucun de `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo` et `FOO` ne doivent être considérés comme mal orthographiés.
* Indépendamment de la casse, votre implémentation de `check` doit retourner vrai uniquement pour les mots présents dans le dictionnaire. Faites attention à ne pas coder en dur des mots communs (par exemple, `the`), au cas où nous passerions votre implémentation à un `dictionnaire` sans ces mêmes mots. De plus, les seules formes possives autorisées sont celles qui sont effectivement dans le dictionnaire. En d'autres termes, même si `foo` est dans le dictionnaire, `check` doit renvoyer `false` si `foo's` n'y est pas également.
* Vous pouvez supposer que tout dictionnaire passé à votre programme sera structuré exactement comme le nôtre, trié alphabétiquement de haut en bas avec un mot par ligne, chacun se terminant par `\n`. Vous pouvez également supposer que `dictionary` contiendra au moins un mot, qu'aucun mot ne sera plus long de `LENGTH` (une constante définie dans `dictionary.h`) de caractères, qu'aucun mot n'apparaîtra plus d'une fois, que chaque mot contiendra uniquement des caractères alphabétiques minuscules et éventuellement des apostrophes, et qu'aucun mot ne commencera par une apostrophe.
* Vous pouvez supposer que `check` ne sera passé que des mots contenant des caractères alphabétiques (majuscules ou minuscules) et éventuellement des apostrophes.
* Votre correcteur d'orthographe ne peut prendre que `texte`, et éventuellement `dictionary`, en entrée. Bien que vous soyez tenté (en particulier si vous êtes plus à l'aise) de "pré-traiter" notre dictionnaire par défaut afin de dériver une "fonction de hachage idéale" pour celui-ci, vous ne pouvez pas enregistrer la sortie d'un tel prétraitement sur le disque pour la charger de nouveau en mémoire lors des exécutions ultérieures de votre correcteur d'orthographe afin de gagner un avantage.
* Votre correcteur d'orthographe ne doit pas perdre de mémoire. Assurez-vous de vérifier les fuites avec `valgrind`.
* **La fonction de hachage que vous écrivez devrait être la vôtre, pas une que vous recherchez en ligne.** Il existe de nombreuses façons d'implémenter une fonction de hachage au-delà de l'utilisation du premier caractère (ou des premiers caractères) d'un mot. Considérez une fonction de hachage qui utilise la somme des valeurs ASCII ou la longueur d'un mot. Une bonne fonction de hachage a tendance à réduire les "collisions" et présente une répartition assez uniforme sur les "seaux" de la table de hachage.

Bien, êtes-vous prêts?

* Implémentez `load`.
* Implémentez `hash`.
* Implémentez `size`.
* Implémentez `check`.
* Implémentez `unload`.

Guides pratiques
---------------

Notez qu'il y a 6 vidéos dans la liste de lecture ci-dessous.


<div class="alerte" data-alerte="danger" role="alert"><p>Bien que la vidéo de présentation de Speller indique qu'il est raisonnable d'utiliser une fonction de hachage trouvée en ligne, cette vidéo provient d'une version plus ancienne du problème où nous l'autorisions. Conformément aux spécifications ci-dessus, la fonction de hachage que vous écrivez devrait être la vôtre, et vous <strong>ne pouvezz pas</strong> utiliser une fonction de hachage que vous trouvez en ligne. N'oubliez pas de citer les sources externes que vous avez consultées pour écrire votre fonction de hachage.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>

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

