Lisibilité
===========

Implémentez un programme qui calcule le niveau de lecture approximatif nécessaire pour comprendre un texte, comme indiqué ci-dessous.

    $ python readability.py
    Texte: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Niveau scolaire 3
    

Premiers pas
---------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez remarquer que l'invite de votre fenêtre de terminal ressemble à ceci :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-readability.zip
    

pour télécharger un fichier ZIP appelé `sentimental-readability.zip` dans votre espace code.

Ensuite, exécutez

    unzip sentimental-readability.zip
    

pour créer un dossier appelé `sentimental-readability`. Vous n'avez plus besoin du fichier ZIP, alors vous pouvez exécuter

    rm sentimental-readability.zip
    

et répondez par "y" suivi de la touche Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd sentimental-readability
    

suivi de la touche Entrée pour vous déplacer dans ce répertoire. Votre invite doit maintenant ressembler à ceci.

    sentimental-readability/ $
    

Exécutez `ls`, et vous devriez voir `readability.py`. Si vous rencontrez des problèmes, suivez les mêmes étapes à nouveau et essayez de déterminer où vous vous êtes trompé !

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

Tests
-----

Bien que `check50` soit disponible pour ce problème, vous êtes encouragé à tester d'abord votre code en utilisant les étapes suivantes.

*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `One fish. Two fish. Red fish. Blue fish.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Before Grade 1`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 2`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `Congratulations! Today is your day. You're off to Great Places! You're off and away!` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 3`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 5`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 7`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 8`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 8`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 9`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 10`.
*   Exécutez votre programme comme ceci : `python readability.py`, et attendez une invitation pour entrer un texte. Entrez : `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` et appuyez sur la touche Entrée. Votre programme doit produire la sortie `Grade 16+`.

Exécutez la commande suivante pour évaluer la correction de votre code à l'aide de `check50`. Mais veillez à le compiler et à le tester vous-même également !

    check50 cs50/problems/2023/x/sentimental/readability
    

Exécutez la commande suivante pour évaluer le style de votre code à l'aide de `style50`.

    style50 readability.py
    "

Comment soumettre
------------------

Dans votre terminal, exécutez les commandes suivantes pour soumettre votre travail.

    submit50 cs50/problems/2023/x/sentimental/readability

