Ampoules
========

Ampoules électriques pas si cassées
-------------------------------------

Pendant le cours, vous avez peut-être remarqué ce qui semblait être un "bug" sur la scène, où certaines ampoules semblent toujours éteintes :

![capture d'écran du cours de la semaine 2 avec une bande d'ampoules](https://cs50.harvard.edu/x/2023/psets/2/bulbs/binary_bulbs.jpg)

Chaque séquence d'ampoules, cependant, code un message en _binaire_, le langage que les ordinateurs "parlent". Écrivons un programme pour créer nos propres messages secrets, que nous pourrions même mettre en scène !

Mise en route
-------------

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer dans votre fenêtre de terminal, puis exécutez `cd` tout seul. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $
    

Cliquez dans cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/psets/2/bulbs.zip
    

suivi de Entrée pour télécharger un ZIP appelé `bulbs.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Maintenant, exécutez

    unzip bulbs.zip
    

pour créer un dossier appelé `bulbs`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm bulbs.zip
    

et répondez avec "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd bulbs
    

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    bulbs/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et voir un fichier nommé `bulbs.c`. L'exécution de `code bulbs.c` devrait ouvrir le fichier où vous taperez votre code pour ce problème défini. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous avez commis une erreur !