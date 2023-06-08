Bonjour
======

Mettez en place un programme qui affiche une salutation simple à l'utilisateur, comme ci-dessous.

    $ python hello.py
    Quel est votre nom ?
    David
    bonjour, David
    

Pour commencer
--------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre terminal et exécutez la commande `cd` seule. Vous devriez voir un invite de commande qui ressemble à ce qui suit :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-hello.zip
    

afin de télécharger un fichier ZIP appelé `sentimental-hello.zip` dans votre espace de travail.

Ensuite, exécutez

    unzip sentimental-hello.zip
    

pour créer un dossier appelé `sentimental-hello`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm sentimental-hello.zip
    

et répondez « y » suivi de Entrée pour supprimer le fichier ZIP téléchargé.

Maintenant, tapez

    cd sentimental-hello
    

suivi de Entrée pour vous déplacer (c'est-à-dire ouvrir) dans ce répertoire. Votre invite de commande devrait ressembler à ce qui suit.

    sentimental-hello/ $
    

Exécutez `ls` seul, et vous devriez voir `hello.py`. Si vous rencontrez des difficultés, suivez ces mêmes étapes à nouveau et voyez si vous pouvez déterminer où vous avez fait une erreur !

Spécification
-------------

Dans un fichier appelé `hello.py`, écrivez un programme qui invite un utilisateur à saisir son nom, puis affiche `bonjour, untel`, où « untel » est le nom fourni, exactement comme vous l'avez fait dans[ Problème 1 ](../../1/), sauf que cette fois, votre programme doit être écrit en Python.

Utilisation
-----------

Votre programme doit se comporter comme dans l'exemple ci-dessous.

    $ python hello.py
    Quel est votre nom ?
    Emma
    bonjour, Emma
    

Test
----

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à d'abord tester votre code vous-même pour chacun des éléments suivants.

*   Exécutez votre programme en tant que `python hello.py`, et attendez une invitation pour la saisie. Tapez « David » et appuyez sur Entrée. Votre programme devrait afficher `bonjour, David`.
*   Exécutez votre programme en tant que `python hello.py`, et attendez une invitation pour la saisie. Tapez « Bernie » et appuyez sur Entrée. Votre programme devrait afficher `bonjour, Bernie`.
*   Exécutez votre programme en tant que `python hello.py`, et attendez une invitation pour la saisie. Tapez « Carter » et appuyez sur Entrée. Votre programme devrait afficher `bonjour, Carter`.

Exécutez le code ci-dessous pour évaluer la validité de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester vous-même également !

    check50 cs50/problems/2023/x/sentimental/hello
    

Exécutez le code ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 hello.py
    

Comment soumettre
-----------------

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/sentimental/hello