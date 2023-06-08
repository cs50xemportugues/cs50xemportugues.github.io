# César

Pour ce problème, vous allez implémenter un programme qui chiffre les messages en utilisant le chiffre de César, selon le chiffrement ci-dessous.

    $./caesar 13
    texte en clair : HELLO
    texte chiffré : URYYB

## Pour commencer

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez obtenir une invite qui ressemble à celle ci-dessous.

    $

Cliquez dans la fenêtre de terminal et exécutez

    wget https://cdn.cs50.net/2022/fall/psets/2/caesar.zip

puis appuyez sur Entrée pour télécharger un fichier ZIP appelé `caesar.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Maintenant, exécutez

    unzip caesar.zip

pour créer un dossier appelé `caesar`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm caesar.zip

et répondez "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd caesar

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    caesar/ $

Si tout s'est bien passé, vous devriez exécuter

    ls

et voir un fichier appelé `caesar.c`. Exécuter `code caesar.c` devrait ouvrir le fichier où vous taperez votre code pour ce jeu de problèmes. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !