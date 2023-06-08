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