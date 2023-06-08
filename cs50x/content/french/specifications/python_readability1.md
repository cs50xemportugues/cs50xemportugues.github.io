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