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