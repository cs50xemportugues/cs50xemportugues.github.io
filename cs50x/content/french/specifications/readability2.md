## Contexte

Selon [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), _Charlotte's Web_ d'E.B. White est adapté à un niveau de lecture de la 2ème à la 4ème année, tandis que _The Giver_ de Lois Lowry est adapté à un niveau de lecture de la 8ème à la 12ème année. Mais qu'est-ce que cela signifie pour un livre d'être à un niveau de lecture particulier ?

Eh bien, dans de nombreux cas, un expert littéraire peut lire un livre et décider du niveau (c.-à-d. de l'année scolaire) pour lequel il est le plus approprié. Mais un algorithme pourrait également probablement déterminer cela !

Alors, quels traits sont caractéristiques de niveaux de lecture plus élevés ? Eh bien, les mots plus longs sont probablement corrélés avec des niveaux de lecture plus élevés. De même, les phrases plus longues sont également corrélées avec des niveaux de lecture plus élevés.

Un certain nombre de "tests de lisibilité" ont été développés au fil des ans pour définir des formules pour le calcul du niveau de lecture d'un texte. Un de ces tests de lisibilité est l'indice de Coleman-Liau. L'indice de Coleman-Liau d'un texte est conçu pour produire le niveau scolaire (U.S.) nécessaire pour comprendre un texte. La formule est la suivante :

    index = 0,0588 * L - 0,296 * S - 15,8

où `L` est le nombre moyen de lettres pour 100 mots dans le texte et `S` est le nombre moyen de phrases pour 100 mots dans le texte.

Écrivons un programme appelé `readability` qui prend un texte et détermine son niveau de lecture. Par exemple, si un utilisateur tape une ligne de texte de Dr. Seuss, le programme devrait fonctionner comme suit :

    $ ./readability
    Texte : Félicitations ! Aujourd'hui est ton jour. Tu pars pour des endroits formidables ! Tu t'en vas !
    Niveau 3

Le texte que l'utilisateur a entré a 65 lettres, 4 phrases et 14 mots. 65 lettres pour 14 mots équivaut à une moyenne d'environ 464,29 lettres pour 100 mots (car 65 / 14 \* 100 = 464,29). Et 4 phrases pour 14 mots équivaut à une moyenne d'environ 28,57 phrases pour 100 mots (car 4 / 14 \* 100 = 28,57). En insérant ces valeurs dans la formule de Coleman-Liau, et en arrondissant à l'entier le plus proche, on obtient une réponse de 3 (car 0,0588 \* 464,29 - 0,296 \* 28,57 - 15,8 = 3) : donc ce passage est adapté à un niveau de lecture de la troisième année.

Essayons-en un autre :

    $ ./readability
    Texte : Harry Potter était un garçon très inhabituel à bien des égards. Pour une chose, il détestait les vacances d'été plus que tout autre moment de l'année. Pour une autre, il voulait vraiment faire ses devoirs, mais était obligé de les faire en secret, en pleine nuit. Et il était également sorcier.
    Niveau 5

Ce texte contient 214 lettres, 4 phrases et 56 mots. Cela donne environ 382,14 lettres pour 100 mots et 7,14 phrases pour 100 mots. En insérant ces valeurs dans la formule de Coleman-Liau, on obtient un niveau de lecture de la cinquième année.

À mesure que le nombre moyen de lettres et de mots par phrase augmente, l'indice de Coleman-Liau donne au texte un niveau de lecture plus élevé. Si vous preniez ce paragraphe, par exemple, qui a des mots et des phrases plus longues que les deux exemples précédents, la formule donnerait un niveau de lecture de la douzième année.

    $ ./readability
    Texte : À mesure que le nombre moyen de lettres et de mots par phrase augmente, l'indice de Coleman-Liau donne au texte un niveau de lecture plus élevé. Si vous preniez ce paragraphe, par exemple, qui a des mots et des phrases plus longues que les deux exemples précédents, la formule donnerait un niveau de lecture de la douzième année.
    Niveau 12

<details><summary>Regarder un enregistrement</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script></details>

## Spécifications

Concevoir et implémenter un programme, `readability`, qui calcule l'indice de Coleman-Liau d'un texte.

- Implémentez votre programme dans un fichier appelé `readability.c` dans un répertoire appelé `readability`.
- Votre programme doit inviter l'utilisateur à entrer une chaîne de texte en utilisant `get_string`.
- Votre programme doit compter le nombre de lettres, de mots et de phrases dans le texte. Vous pouvez supposer qu'une lettre est n'importe quel caractère en minuscule de `a` à `z` ou n'importe quel caractère en majuscule de `A` à `Z`, toute séquence de caractères séparée par des espaces doit être comptée comme un mot et que toute occurrence d'un point, d'un point d'exclamation ou d'un point d'interrogation indique la fin d'une phrase.
- Votre programme doit imprimer en sortie "Niveau X" où `X` est le niveau de lecture calculé par la formule de Coleman-Liau, arrondi à l'entier le plus proche.
- Si le nombre d'index résultant est de 16 ou plus (équivalent ou supérieur à un niveau de lecture d'étudiant de licence), votre programme doit afficher "Niveau 16+" au lieu de donner le nombre d'index exact. Si le nombre d'index est inférieur à 1, votre programme doit afficher "Avant la 1ère année".