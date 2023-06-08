Cash
====

Implémentez un programme qui calcule le nombre minimum de pièces nécessaire pour rendre la monnaie à un utilisateur.

    $ python cash.py
    Change owed: 0.41
    4
    

Premiers pas
---------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre terminal et exécutez simplement `cd`. Vous devriez voir ce qui suit dans le terminal:

    $
    

Ensuite, exécutez la commande suivante:

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-cash.zip
    

pour télécharger un fichier ZIP appelé `sentimental-cash.zip` dans votre espace de travail.

Ensuite, exécutez

    unzip sentimental-cash.zip
    

pour créer un dossier appelé `sentimental-cash`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm sentimental-cash.zip
    

et répondez "y" suivi de "Enter" pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd sentimental-cash
    

suivi de "Enter" pour vous déplacer dans ce répertoire. Votre invite de commande doit maintenant ressembler à ce qui suit:

    sentimental-cash/ $
    

Exécutez `ls` pour voir si le fichier `cash.py` est bien présent. Si vous rencontrez des problèmes, suivez les mêmes étapes à nouveau et essayez de déterminer où vous avez commis une erreur!

Spécification
-------------

*   Écrivez, dans un fichier appelé `cash.py`, un programme qui demande d'abord à l'utilisateur combien de monnaie est due, puis affiche le nombre minimum de pièces nécessaires pour rendre cette somme. Vous pouvez faire exactement la même chose que dans le [Problème 1](../../1/), sauf que votre programme doit cette fois être écrit en Python, et vous devez supposer que l'utilisateur entrera la somme due en dollars (par exemple, 0,50 dollars au lieu de 50 cents).
*   Utilisez `get_float` de la bibliothèque CS50 pour obtenir la saisie de l'utilisateur et `print` pour afficher votre réponse. Supposez que seules les pièces de vingt-cinq cents (25¢), de dix cents (10¢), de cinq cents (5¢) et de un cent (1¢) sont disponibles.
    *   Nous demandons que vous utilisiez `get_float` pour que vous puissiez gérer les dollars et les cents, même si le signe dollar n'est pas présent. En d'autres termes, si le client doit payer 9,75 $ (comme dans le cas où un journal coûte 25¢, mais le client paie avec un billet de 10 $), supposez que la saisie pour votre programme sera `9,75` et non `$9,75` ou `975`. Cependant, si le client doit payer exactement 9 $, supposez que la saisie pour votre programme sera `9,00` ou simplement `9', mais pas `$9` ou `900`. Bien sûr, en raison de la nature des valeurs à virgule flottante, votre programme fonctionnera probablement avec des entrées telles que `9,0` et `9.000` également; vous n'avez pas à vous soucier de savoir si la saisie de l'utilisateur est « formatée » comme de l'argent.
*   Si l'utilisateur fournit une valeur qui n'est pas supérieure ou égale à zéro, votre programme doit re-prompter l'utilisateur pour qu'il saisisse une somme valide encore et encore jusqu'à ce que l'utilisateur se conforme à la demande.
*   Il est à noter que pour que nous puissions automatiser des tests sur votre code, nous vous demandons que la dernière ligne de sortie de votre programme ne contienne que le nombre minimum de pièces possible: un nombre entier suivi d'un retour à la ligne.

Utilisation
-----

Votre programme devrait se comporter comme dans l'exemple ci-dessous.

    $ python cash.py
    Change owed: 0.41
    4
    

Tests
-------

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à tester d'abord votre code par vous-même pour chacun des tests suivants.

*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `0,41` et appuyez sur "Entrée". Votre programme doit afficher `4`.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `0,01` et appuyez sur "Entrée". Votre programme doit afficher `1`.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `0,15` et appuyez sur "Entrée". Votre programme doit afficher `2`.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `1,60` et appuyez sur "Entrée". Votre programme doit afficher `7`.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `23` et appuyez sur "Entrée". Votre programme doit afficher `92`.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `4,2` et appuyez sur "Entrée". Votre programme doit afficher `18`.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `-1` et appuyez sur "Entrée". Votre programme doit rejeter cette entrée comme invalide, et redemander à l'utilisateur d'entrer un autre nombre.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Saisissez `foo` et appuyez sur "Entrée". Votre programme doit rejeter cette entrée comme invalide, et redemander à l'utilisateur d'entrer un autre nombre.
*   Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour entrer une valeur. Ne saisissez rien et appuyez sur "Entrée". Votre programme doit rejeter cette entrée comme invalide, et redemander à l'utilisateur d'entrer un autre nombre.

Exécutez les commandes ci-dessous pour évaluer la correction de votre code avec `check50` et pour vérifier le style de votre code avec `style50`.

    check50 cs50/problems/2023/x/sentimental/cash
    style50 cash.py
    

Comment soumettre
-------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/sentimental/cash"