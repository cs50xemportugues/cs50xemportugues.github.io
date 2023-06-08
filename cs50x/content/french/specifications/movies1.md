Films
======

Rédigez des requêtes SQL pour répondre à des questions sur une base de données de films.

Commencer
---------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez voir que l'invite de votre fenêtre de terminal ressemble à ce qui suit:

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/7/movies.zip
    

pour télécharger un fichier ZIP appelé «movies.zip» dans votre espace de codes.

Ensuite, exécutez

    unzip movies.zip
    

pour créer un dossier appelé «movies». Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm -rm movies.zip
    

et répondez par "y" suivi de "Enter" pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd movies
    

puis "Enter" pour vous déplacer dans ce répertoire (ouvert). Votre invite devrait maintenant ressembler à ceci.

    movies/ $
    

Exécutez `ls` par lui-même et vous devriez voir 13 fichiers .sql ainsi que `movies.db`.

Si vous avez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous vous êtes trompé !

Compréhension
-------------

Un fichier appelé `movies.db`, une base de données SQLite qui stocke des données de [IMDb](https://www.imdb.com/) sur les films, les personnes qui les ont dirigées et joué dedans, et leurs notes vous est fourni. Dans une fenêtre de terminal, exécutez `sqlite3 movies.db` pour commencer à exécuter des requêtes sur la base de données.

Tout d'abord, lorsque `sqlite3` vous demande de fournir une requête, tapez `.schema` et appuyez sur Entrée. Cela produira les déclarations `CREATE TABLE` qui ont été utilisées pour générer chacune des tables de la base de données. En examinant ces déclarations, vous pouvez identifier les colonnes présentes dans chaque table.

Remarquez que la table `movies` a une colonne `id` qui identifie de manière unique chaque film, ainsi que des colonnes pour le `titre` d'un film et l'année de `sortie` du film. La table de `people` a également une colonne `id`, ainsi que des colonnes pour le `nom` de chaque personne et son année de `naissance`.

Les notes de films, quant à elles, sont stockées dans la table de `ratings`. La première colonne de la table est `movie_id`: une clé étrangère qui fait référence à l'`id` de la table `movies`. Le reste de la ligne contient des données sur la `note` pour chaque film et le nombre de `votes` que le film a reçus sur IMDb.

Enfin, les tables `stars` et `directors` associent les personnes aux films dans lesquels elles ont joué ou dirigé. (Seuls les acteurs et les réalisateurs [principaux](https://www.imdb.com/interfaces/) sont inclus.) Chaque table a seulement deux colonnes: `movie_id` et `person_id`, qui font référence à un film et à une personne spécifique, respectivement.

Le défi qui vous attend est d'écrire des requêtes SQL pour répondre à une variété de questions différentes en sélectionnant des données à partir d'une ou plusieurs de ces tables.