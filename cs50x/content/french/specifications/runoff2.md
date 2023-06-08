Débuter
-------

Connectez-vous à [code.cs50.io] (https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit:

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/3/runoff.zip
    

afin de télécharger un fichier ZIP appelé `runoff.zip` dans votre espace de code.

Ensuite, exécutez

    unzip runoff.zip
    

pour créer un dossier appelé `runoff`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm runoff.zip
    

et répondre "y" suivi de Entrée à la invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd runoff
    

suivi de Entrée pour vous déplacer dans ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    runoff/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et voir un fichier nommé `runoff.c`. Exécuter `code runoff.c` devrait ouvrir le fichier dans lequel vous allez taper votre code pour cette série de problèmes. Sinon, retracez vos étapes et voyez si vous pouvez déterminer où vous vous êtes trompé !

Compréhension
--------------

Jetons un coup d'œil à `runoff.c`. Nous définissons deux constantes: `MAX_CANDIDATES` pour le nombre maximum de candidats à l'élection et `MAX_VOTERS` pour le nombre maximum de votants à l'élection.

Ensuite, il y a un tableau bidimensionnel `preferences`. Le tableau `preferences[i]` représentera toutes les préférences pour l'électeur numéro `i`, et l'entier `preferences[i][j]` stockera l'indice du candidat qui est la `j`ème préférence pour l'électeur `i`.

Ensuite, il y a une structure appelée `candidate`. Chaque `candidate` a un champ `string` pour son `name`, un entier représentant le nombre de `votes` qu'il a actuellement, et une valeur `bool` appelée `eliminated` qui indique si le candidat a été éliminé de l'élection. Le tableau `candidates` suivra tous les candidats à l'élection.

Le programme contient également deux variables globales: `voter_count` et `candidate_count`.

Passons maintenant à `main`. Remarquez qu'après avoir déterminé le nombre de candidats et le nombre de votants, la boucle principale de vote commence, donnant à chaque votant une chance de voter. Lorsque l'électeur entre ses préférences, la fonction `vote` est appelée pour suivre toutes les préférences. Si à un moment donné, le bulletin de vote est considéré comme non valide, le programme se termine.

Une fois tous les votes enregistrés, une autre boucle commence: celle-ci va parcourir le processus de vote en votant jusqu'à trouver un gagnant et en éliminant le candidat en dernière position jusqu'à ce qu'il y ait un gagnant.

Le premier appel ici est à une fonction appelée `tabulate`, qui devrait examiner toutes les préférences des électeurs et calculer les totaux de vote actuels, en examinant le candidat préféré de chaque électeur qui n'a pas encore été éliminé. Ensuite, la fonction `print_winner` doit afficher le vainqueur s'il y en a un; si c'est le cas, le programme est terminé. Sinon, le programme doit déterminer le nombre de votes le plus faible que quiconque encore dans l'élection a reçu (via un appel à `find_min`). S'il s'avère que tout le monde dans l'élection est à égalité avec le même nombre de votes (tel que déterminé par la fonction `is_tie`), l'élection est déclarée en égalité; sinon, le candidat ou les candidats en dernière position sont éliminés de l'élection via un appel à la fonction `eliminate`.

Si vous regardez un peu plus loin dans le fichier, vous verrez que ces fonctions - `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` et `eliminate` - sont toutes laissées à votre sauce pour compléter!