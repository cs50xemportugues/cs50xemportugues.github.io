Commencer
---------

Ouvrez [VS Code](https://code.cs50.io/).

Commencez en cliquant à l'intérieur de la fenêtre de votre terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à ce qui suit.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/labs/6/world-cup.zip
    

suivi par la touche Entrée pour télécharger un ZIP appelé `world-cup.zip` dans votre espace de code. Attention à ne pas négliger l'espace entre `wget` et l'URL suivante, ou tout autre caractère qui pourrait poser problème!

Maintenant, exécutez

    unzip world-cup.zip
    

pour créer un dossier appelé `world-cup`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm world-cup.zip
    

et répondre "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, saisissez

    cd world-cup
    

suivi de Entrée pour vous déplacer dans (c'est-à-dire, ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    world-cup/ $
    

Si tout a réussi, vous devriez exécuter

    ls
    

et vous devriez voir les fichiers suivants:

    answers.txt  2018m.csv  2019w.csv  tournament.py
    

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur !

Compréhension
-------------

Commencez par jeter un coup d'œil au fichier `2018m.csv`. Ce fichier contient les 16 équipes des huitièmes de finale de la Coupe du monde 2018 et les notes pour chaque équipe. Notez que le fichier CSV a deux colonnes, une appelée `team` (représentant le nom du pays de l'équipe) et une appelée `rating` (représentant la note de l'équipe).

L'ordre dans lequel les équipes sont répertoriées détermine quelles équipes joueront l'une contre l'autre à chaque tour (au premier tour, par exemple, l'Uruguay jouera contre le Portugal et la France jouera contre l'Argentine ; au tour suivant, le vainqueur du match Uruguay-Portugal jouera contre le vainqueur du match France-Argentine). Veillez donc à ne pas modifier l'ordre d'apparition des équipes dans ce fichier !

Finalement, en Python, nous pouvons représenter chaque équipe en tant que dictionnaire contenant deux valeurs: le nom de l'équipe et la note. Uruguay, par exemple, nous voudrions le représenter en Python comme `{"team": "Uruguay", "rating": 976}`.

Ensuite, jetez un coup d'œil à `2019w.csv`, qui contient des données formatées de la même manière pour la Coupe du monde féminine de 2019.

Maintenant, ouvrez `tournament.py` et vous verrez que nous avons déjà écrit du code pour vous. La variable `N` en haut représente le nombre de simulations de la Coupe du monde à exécuter : dans ce cas, 1000.

La fonction `simulate_game` accepte deux équipes en entrée (rappelons que chaque équipe est un dictionnaire contenant le nom de l'équipe et la note de l'équipe) et simule un match entre elles. Si la première équipe gagne, la fonction renvoie `True`; sinon, la fonction renvoie `False`.

La fonction `simulate_round` accepte une liste d'équipes (dans une variable appelée `teams`) en entrée et simule des matchs entre chaque paire d'équipes. La fonction renvoie ensuite une liste de toutes les équipes qui ont remporté la manche.

Dans la fonction `main`, notez d'abord que nous nous assurons que `len(sys.argv)` (nombre d'arguments de ligne de commande) est de 2. Nous utiliserons les arguments de ligne de commande pour indiquer à Python quel fichier CSV d'équipe utiliser pour exécuter la simulation de la Coupe du monde. Nous avons ensuite défini une liste appelée `teams` (qui sera éventuellement une liste d'équipes) et un dictionnaire appelé `counts` (qui associera les noms d'équipes au nombre de fois que cette équipe a gagné une Coupe du monde simulée). Pour l'instant, ils sont tous deux vides, alors la mise en place est laissée à votre charge !

Enfin, à la fin de `main`, nous trions les équipes dans un ordre descendant en fonction du nombre de fois qu'elles ont remporté des simulations (selon `counts`) et imprimons la probabilité estimée que chaque équipe remporte la Coupe du monde.

La mise en place de `teams` et `counts` et de l'écriture de la fonction `simulate_tournament` vous appartient !