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

Spécification
-------------

Pour chacun des problèmes suivants, vous devez écrire une seule requête SQL qui renvoie les résultats spécifiés par chaque problème. Votre réponse doit prendre la forme d'une seule requête SQL, bien que vous puissiez imbriquer d'autres requêtes dans votre requête. Vous ne devez rien supposer quant aux `id` de chaque film ou de chaque personne: vos requêtes doivent être précises même si l'id de chaque film ou de chaque personne était différent. Enfin, chaque requête doit renvoyer uniquement les données nécessaires pour répondre à la question: si le problème vous demande simplement de renvoyer les titres de films, par exemple, alors votre requête ne doit pas renvoyer également l'année de sortie de chaque film.

Vous pouvez vérifier les résultats de vos requêtes sur [IMDb](https://www.imdb.com/), mais comprenez que les notes sur le site peuvent différer de celles de `movies.db`, car plus de votes peuvent avoir été exprimés depuis que nous avons téléchargé les données!

1. Dans `1.sql`, écrivez une requête SQL pour afficher les titres de tous les films sortis en 2008.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le titre de chaque film.
2. Dans `2.sql`, écrivez une requête SQL pour déterminer l'année de naissance d'Emma Stone.
    * Votre requête doit renvoyer un tableau avec une seule colonne et une seule ligne (sans compter l'en-tête) contenant l'année de naissance d'Emma Stone.
    * Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données avec le nom d'Emma Stone.
3. Dans `3.sql`, écrivez une requête SQL pour afficher les titres de tous les films avec une date de sortie en 2018 ou après, par ordre alphabétique.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le titre de chaque film.
    * Les films sortis en 2018 doivent être inclus, ainsi que les films dont la date de sortie est dans le futur.
4. Dans `4.sql`, écrivez une requête SQL pour déterminer le nombre de films avec une note IMDb de 10,0.
    * Votre requête doit renvoyer un tableau avec une seule colonne et une seule ligne (sans compter l'en-tête) contenant le nombre de films ayant une note de 10,0.
5. Dans `5.sql`, écrivez une requête SQL pour afficher les titres et les années de sortie de tous les films Harry Potter, dans l'ordre chronologique.
    * Votre requête doit renvoyer un tableau avec deux colonnes, une pour le titre de chaque film et une pour l'année de sortie de chaque film.
    * Vous pouvez supposer que le titre de tous les films Harry Potter commencera par les mots "Harry Potter", et que si un titre de film commence par les mots "Harry Potter", il s'agit d'un film Harry Potter.
6. Dans `6.sql`, écrivez une requête SQL pour déterminer la note moyenne de tous les films sortis en 2012.
    * Votre requête doit renvoyer un tableau avec une seule colonne et une seule ligne (sans compter l'en-tête) contenant la note moyenne.
7. Dans `7.sql`, écrivez une requête SQL pour afficher tous les films sortis en 2010 et leurs notes, par ordre décroissant de note. Pour les films avec la même note, ordonnez-les par ordre alphabétique de titre.
    * Votre requête doit renvoyer un tableau avec deux colonnes, une pour le titre de chaque film et une pour la note de chaque film.
    * Les films sans note ne doivent pas être inclus dans le résultat.
8. Dans `8.sql`, écrivez une requête SQL pour afficher les noms de toutes les personnes qui ont joué dans Toy Story.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le nom de chaque personne.
    * Vous pouvez supposer qu'il n'y a qu'un seul film dans la base de données avec le titre Toy Story.
9. Dans `9.sql`, écrivez une requête SQL pour afficher les noms de toutes les personnes qui ont joué dans un film sorti en 2004, trié par année de naissance.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le nom de chaque personne.
    * Les personnes nées la même année peuvent être listées dans n'importe quel ordre.
    * Pas besoin de s'inquiéter des personnes qui n'ont pas d'année de naissance indiquée, tant que celles qui ont une année de naissance sont listées dans l'ordre.
    * Si une personne est apparue dans plus d'un film en 2004, elle ne doit apparaître qu'une fois dans vos résultats.
10. Dans `10.sql`, écrivez une requête SQL pour afficher les noms de toutes les personnes qui ont réalisé un film qui a obtenu une note d'au moins 9,0.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le nom de chaque personne.
    * Si une personne a réalisé plus d'un film qui a obtenu une note d'au moins 9,0, elle ne doit apparaître qu'une fois dans vos résultats.
11. Dans `11.sql`, écrivez une requête SQL pour afficher les titres des cinq films les mieux notés (par ordre) dans lesquels Chadwick Boseman a joué, en commençant par le plus haut.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le titre de chaque film.
    * Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données avec le nom de Chadwick Boseman.
12. Dans `12.sql`, écrivez une requête SQL pour afficher les titres de tous les films dans lesquels Johnny Depp et Helena Bonham Carter ont joué.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le titre de chaque film.
    * Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données avec le nom de Johnny Depp.
    * Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données avec le nom de Helena Bonham Carter.
13. Dans `13.sql`, écrivez une requête SQL pour afficher les noms de toutes les personnes qui ont joué dans un film dans lequel Kevin Bacon a également joué.
    * Votre requête doit renvoyer un tableau avec une seule colonne pour le nom de chaque personne.
    * Il peut y avoir plusieurs personnes nommées Kevin Bacon dans la base de données. Assurez-vous de sélectionner uniquement le Kevin Bacon né en 1958.
    * Kevin Bacon lui-même ne doit pas être inclus dans la liste résultante.

Procédure
---------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accéléromètre; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Utilisation
-----------

Pour tester vos requêtes dans VS Code, vous pouvez interroger la base de données en exécutant

    $ cat nom_fichier.sql | sqlite3 movies.db
    

où `nom_fichier.sql` est le fichier contenant votre requête SQL.

Vous pouvez également exécuter

    $ cat nom_fichier.sql | sqlite3 movies.db > output.txt
    

pour rediriger la sortie de la requête vers un fichier texte appelé `output.txt`. (Cela peut être utile pour vérifier combien de lignes sont retournées par votre requête!)

Indications
-----------

*   Consultez [cette référence de mots-clés SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) pour vous familiariser avec la syntaxe SQL qui peut être utile !
*   Visitez [sqlstyle.guide](https://www.sqlstyle.guide/) pour obtenir des conseils sur le bon style en SQL, surtout lorsque vos requêtes deviennent plus complexes !

Tests
-----

Bien que `check50` soit disponible pour ce problème, il est recommandé de tester votre code vous-même pour chacun des éléments suivants. Vous pouvez exécuter `sqlite3 movies.db` pour exécuter des requêtes supplémentaires sur la base de données et vous assurer que votre résultat est correct.

Si vous utilisez la base de données `movies.db` fournie dans cette distribution de problème, vous devriez constater que :

*   L'exécution de `1.sql` donne une table avec 1 colonne et 10 050 lignes.
*   L'exécution de `2.sql` donne une table avec 1 colonne et 1 ligne.
*   L'exécution de `3.sql` donne une table avec 1 colonne et 88 918 lignes.
*   L'exécution de `4.sql` donne une table avec 1 colonne et 1 ligne.
*   L'exécution de `5.sql` donne une table avec 2 colonnes et 12 lignes.
*   L'exécution de `6.sql` donne une table avec 1 colonne et 1 ligne.
*   L'exécution de `7.sql` donne une table avec 2 colonnes et 7 085 lignes.
*   L'exécution de `8.sql` donne une table avec 1 colonne et 4 lignes.
*   L'exécution de `9.sql` donne une table avec 1 colonne et 18 946 lignes.
*   L'exécution de `10.sql` donne une table avec 1 colonne et 3 392 lignes.
*   L'exécution de `11.sql` donne une table avec 1 colonne et 5 lignes.
*   L'exécution de `12.sql` donne une table avec 1 colonne et 7 lignes.
*   L'exécution de `13.sql` donne une table avec 1 colonne et 182 lignes.

Notez que les nombres de lignes ne comprennent pas les lignes d'en-tête qui n'affichent que les noms de colonnes.

Si votre requête renvoie un nombre de lignes légèrement différent de la sortie attendue, assurez-vous que vous gérez correctement les doublons ! Pour les requêtes demandant une liste de noms, une personne ne doit pas être listée deux fois, mais deux personnes différentes ayant le même nom doivent chacune être listées.

Exécutez ce qui suit pour évaluer la justesse de votre code en utilisant `check50`.

    check50 cs50/problems/2023/x/movies
    

Comment soumettre votre travail
-------------------------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/movies
    

Remerciements
-------------

Informations fournies par IMDb ([imdb.com](https://www.imdb.com)). Utilisée avec permission.

