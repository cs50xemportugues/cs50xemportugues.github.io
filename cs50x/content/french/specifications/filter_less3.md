Commencer
---------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit:

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-less.zip
    

pour télécharger un fichier ZIP appelé `filter-less.zip` dans votre espace de code.

Ensuite, exécutez

    unzip filter-less.zip
    

pour créer un dossier appelé `filter-less`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm filter-less.zip
    

et répondez "y" suivi de la touche Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd filter-less
    

suivi de la touche Entrée pour vous déplacer dans (c'est-à-dire, ouvrir) ce répertoire. Votre invite doit maintenant ressembler à ce qui suit.

    filter-less/ $
    

Exécutez `ls` tout seul, et vous devriez voir quelques fichiers : `bmp.h`, `filter.c`, `helpers.h`, `helpers.c`, et `Makefile`. Vous devriez également voir un dossier appelé `images` avec quatre fichiers BMP. Si vous avez des difficultés, suivez ces mêmes étapes à nouveau et voyez si vous pouvez déterminer où vous avez fait une erreur !