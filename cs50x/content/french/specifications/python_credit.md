Crédit
======

Implémentez un programme qui détermine si un numéro de carte de crédit donné est valide selon l’algorithme de Luhn.

    $ python credit.py
    Number: 378282246310005
    AMEX
    

Premier pas
-----------

Connectez-vous sur [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez voir une fenêtre de terminal qui ressemble à celle-ci :

    $
    

Ensuite, exécutez la commande 

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-credit.zip
    

pour télécharger un fichier ZIP appelé `sentimental-credit.zip` dans votre espace de code.

Ensuite, exécutez 

    unzip sentimental-credit.zip
    

pour créer un dossier appelé `sentimental-credit`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm sentimental-credit.zip
    

et répondez par "y" suivi de Entrée à la commande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd sentimental-credit
    

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite de commande devrait ressembler à celle-ci.

    sentimental-credit/ $
    

Executez simplement la commande `ls`, vous devriez voir`credit.py`. Si vous rencontrez un problème, suivez ces mêmes étapes de nouveau et essayez de déterminer où vous vous êtes trompé !

Spécification
--------------

* Dans `credit.py`, écrivez un programme qui demande à l'utilisateur un numéro de carte de crédit et signale ensuite (via `print`) si c'est une carte American Express, Mastercard ou Visa valide, exactement comme vous l'avez fait dans [Problème Set 1](../../1/), à l'exception que votre programme cette fois-ci devrait être écrit en Python.
* Afin que nous puissions automatiser certains tests de votre code, nous vous demandons que la dernière ligne de sortie de votre programme soit `AMEX\n` ou`MASTERCARD\n` ou`VISA\n` ou`INVALID\n`, rien de plus, rien de moins.
* Pour simplifier, vous pouvez supposer que l'entrée de l'utilisateur sera entièrement numérique (c'est-à-dire dépourvue de tirets, comme pourrait l'être une carte réelle).
* Il est préférable d'utiliser `get_int` ou `get_string` de la bibliothèque CS50 pour obtenir l'entrée de l'utilisateur, en fonction de la façon dont vous avez décidé de mettre en œuvre cela.

Utilisation
----------

Votre programme doit se comporter comme l'exemple ci-dessous.

    $ python credit.py
    Number: 378282246310005
    AMEX
    

Indices
-------

* Il est possible d'utiliser des expressions régulières pour valider les entrées utilisateur. Vous pouvez utiliser le module [`re`](https://docs.python.org/3/library/re.html) de Python, par exemple, pour vérifier si l'entrée de l'utilisateur est effectivement une séquence de chiffres de la longueur correcte.

Test
----

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à d'abord tester votre code vous-même pour chacun des éléments suivants.

* Exécutez votre programme en tant que `python credit.py` et attendez une invite pour l'entrée. Tapez `378282246310005` et appuyez sur Entrée. Votre programme devrait produire `AMEX`.
* Exécutez votre programme en tant que `python credit.py` et attendez une invite pour l'entrée. Tapez `371449635398431` et appuyez sur Entrée. Votre programme devrait produire `AMEX`.
* Exécutez votre programme en tant que `python credit.py` et attendez une invite pour l'entrée. Tapez `5555555555554444` et appuyez sur Entrée. Votre programme devrait produire `MASTERCARD`.
* Exécutez votre programme en tant que `python credit.py` et attendez une invite pour l'entrée. Tapez `5105105105105100` et appuyez sur Entrée. Votre programme devrait produire `MASTERCARD`.
* Exécutez votre programme en tant que `python credit.py` et attendez une invite pour l'entrée. Tapez `4111111111111111` et appuyez sur Entrée. Votre programme devrait produire `VISA`.
* Exécutez votre programme en tant que `python credit.py` et attendez une invite pour l'entrée. Tapez `4012888888881881` et appuyez sur Entrée. Votre programme devrait produire `VISA`.
* Exécutez votre programme en tant que `python credit.py` et attendez une invite pour l'entrée. Tapez `1234567890` et appuyez sur Entrée. Votre programme devrait produire `INVALID`.

Exécutez la commande ci-dessous pour évaluer la justesse de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester également vous-même !

    check50 cs50/problems/2023/x/sentimental/credit
    

Exécutez la commande ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 credit.py
    

Comment soumettre
-----------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/sentimental/credit"