Correcteur d'orthographe
=======

<div class="alert" data-alert="danger" role="alert"><p><strong>Assurez-vous de lire cette spécification dans son intégralité avant de commencer pour savoir quoi faire et comment le faire !</strong></p></div>


Pour ce problème, vous allez implémenter un programme qui vérifie l'orthographe d'un fichier à l'aide d'une table de hachage, comme ci-dessous.

    $ ./speller texts/lalaland.txt
    MOTS MAL ÉPELLÉS
    
    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]
    
    MOTS MAL ÉPELLÉS :
    MOTS DANS LE DICTIONNAIRE :
    MOTS DANS LE TEXTE :
    TEMPS DE CHARGEMENT :
    TEMPS DE VÉRIFICATION :
    TAILLE :
    TEMPS DE DÉCHARGEMENT :
    TEMPS TOTAL :
    

Pour commencer
---------------

Connectez-vous à [code.cs50.io] (https://code.cs50.io/) , cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez voir que l'invite de votre fenêtre de terminal ressemble à celle ci-dessous :

    $
    
Ensuite, exécutez la commande suivante :

   wget https://cdn.cs50.net/2022/fall/psets/5/speller.zip
    
pour télécharger un fichier ZIP appelé `speller.zip` dans votre espace de code.

Ensuite, exécutez

    unzip speller.zip
    
pour créer un dossier appelé `speller`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm speller.zip
    
et répondre "y" suivi de la touche Entrée à l'invite de commande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant tapez

    cd speller
    
suivi de la touche Entrée pour vous déplacer dans ce répertoire. Votre invite de commande doit maintenant ressembler à celle ci-dessous.

    speller/ $

Exécutez `ls` tout seul, et vous devriez voir quelques fichiers et dossiers :

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
    
Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur !