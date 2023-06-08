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