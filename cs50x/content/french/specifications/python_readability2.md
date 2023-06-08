Spécification
-------------

*   Écrivez, dans un fichier nommé `readability.py`, un programme qui demande d'abord à l'utilisateur de saisir un texte, puis affiche le niveau de lecture estimé pour ce texte en utilisant la formule Coleman-Liau, exactement comme dans [l'énoncé 2](../../2/), sauf que votre programme cette fois doit être écrit en Python.
    *   Rappelons que l'indice de Coleman-Liau est calculé comme `0,0588 * L - 0,296 * S - 15,8`, où `L` est le nombre moyen de lettres pour 100 mots dans le texte, et `S` est le nombre moyen de phrases pour 100 mots dans le texte.
*   Utilisez `get_string` de la bibliothèque CS50 pour obtenir la saisie de l'utilisateur, et `print` pour afficher votre réponse.
*   Votre programme doit compter le nombre de lettres, de mots et de phrases dans le texte. Vous pouvez supposer qu'une lettre est n'importe quel caractère minuscule de `a` à `z` ou n'importe quel caractère majuscule de `A` à `Z`, que toute séquence de caractères séparés par des espaces doit être considérée comme un mot, et que toute occurrence d'un point, d'un point d'exclamation ou d'un point d'interrogation indique la fin d'une phrase.
*   Votre programme doit imprimer en sortie `"Grade X"`, où `X` est le niveau de lecture estimé par la formule Coleman-Liau, arrondi au nombre entier le plus proche.
*   Si le nombre d'indice obtenu est égal ou supérieur à 16 (correspondant à un niveau de lecture de premier cycle universitaire supérieur), votre programme doit afficher `"Grade 16+"` au lieu de donner le nombre d'indice exact. Si le nombre d'indice est inférieur à 1, votre programme doit afficher `"Before Grade 1"`.

Usage
-----

Votre programme doit se comporter comme l'exemple ci-dessous.

    $ python readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3