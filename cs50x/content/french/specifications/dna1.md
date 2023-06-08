ADN
===

Mettez en place un programme qui identifie une personne en fonction de son ADN, selon les éléments ci-dessous.

    $ python dna.py databases/large.csv sequences/5.txt
    Lavender
    

Pour commencer
--------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal, et exécutez simplement la commande `cd`. Votre invite de terminal devrait ressembler à ceci :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/6/dna.zip
    

afin de télécharger un dossier ZIP portant le nom `dna.zip` dans votre espace de code.

Ensuite, exécutez

    unzip dna.zip
    

pour créer un dossier appelé `dna`. Vous n'avez plus besoin du dossier ZIP, vous pouvez donc exécuter

     rm dna.zip
    

et répondre par "y" suivi de la touche Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant 

    cd dna
    

suivi de la touche Entrée pour rentrer dans (à savoir, ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ceci :

    dna/ $
    

Exécutez simplement `ls`, vous devriez voir quelques fichiers et dossiers :

    databases/ dna.py sequences/
    

Si vous rencontrez des problèmes, refaites les mêmes étapes et voyez où vous avez commis une erreur.