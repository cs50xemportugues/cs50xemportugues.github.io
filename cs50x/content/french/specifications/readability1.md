# Lisibilité

Pour ce problème, vous allez implémenter un programme qui calcule le niveau de grade approximatif nécessaire pour comprendre un texte donné, comme indiqué ci-dessous.

    $ ./lisibilite
    Texte: Félicitations ! Aujourd'hui est votre jour. Vous partez vers de grands horizons ! Vous vous envolez loin !
    Niveau de grade 3

## Premiers Pas

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer dans votre fenêtre de terminal, puis exécutez la commande `cd`. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $

Cliquez dans la fenêtre du terminal et exécutez ensuite la commande

    wget https://cdn.cs50.net/2022/fall/psets/2/readability.zip

puis appuyez sur Entrée pour télécharger un fichier ZIP nommé «readability.zip» dans votre espace de code. Faites attention à ne pas omettre l'espace entre «wget» et l'URL suivante, ni aucun autre caractère !

Maintenant, exécutez

    unzip readability.zip

pour créer un dossier nommé «lisibilite». Vous n'avez plus besoin du fichier ZIP, donc vous pouvez exécuter

    rm readability.zip

et répondre par "y" suivi de la touche Entrée à la invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd lisibilite

suivi de la touche Entrée pour vous déplacer dans (ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    lisibilite/ $

Si tout a fonctionné correctement, vous devriez exécuter

    ls

et voir un fichier nommé "readability.c". L'exécution de la commande `code readability.c` devrait ouvrir le fichier où vous allez taper votre code pour cet ensemble de problèmes. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !