Fiftyville
==========

Écrivez des requêtes SQL pour résoudre un mystère.

Un mystère à Fiftyville
---------------------

Le canard CS50 a été volé ! La ville de Fiftyville a fait appel à vous pour résoudre le mystère du canard volé. Les autorités pensent que le voleur a pris le canard et ensuite, peu de temps après, a pris un vol hors de la ville avec l'aide d'un complice. Votre objectif est d'identifier :

- Qui est le voleur,
- Dans quelle ville le voleur s'est échappé, et
- Qui est le complice du voleur qui les a aidés à s'échapper.

Tout ce que vous savez, c'est que le vol a eu lieu **le 28 juillet 2021** et qu'il a eu lieu **sur la rue Humphrey**.

Comment allez-vous résoudre ce mystère ? Les autorités de Fiftyville ont pris certains dossiers de la ville autour du temps du vol et ont préparé une base de données SQLite pour vous, `fiftyville.db`, qui contient des tables de données de la ville. Vous pouvez interroger cette table en utilisant des requêtes SQL `SELECT` pour accéder aux données qui vous intéressent. En utilisant uniquement les informations de la base de données, votre tâche est de résoudre le mystère.

Pour commencer
---------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal, et exécutez `cd`. Vous devriez voir que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/7/fiftyville.zip
    
pour télécharger un ZIP appelé `fiftyville.zip` dans votre environnement de code.

Ensuite, exécutez

    unzip fiftyville.zip
    
pour créer un dossier appelé `fiftyville`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm fiftyville.zip
    
et répondre "y", suivi de Enter, à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd fiftyville
    
puis appuyez sur Enter pour vous déplacer dans ce répertoire (c'est-à-dire l'ouvrir). Votre invite devrait maintenant ressembler à ce qui suit.

    fiftyville/ $
    

Exécutez `ls` et vous devriez voir quelques fichiers :

    answers.txt  fiftyville.db  log.sql
    
Si vous rencontrez des problèmes, suivez à nouveau ces étapes et voyez si vous pouvez déterminer où vous vous êtes trompé !

Spécification
-------------

Pour ce problème, aussi important que de résoudre le mystère lui-même est le processus que vous utilisez pour résoudre le mystère. Dans `log.sql`, gardez une trace de toutes les requêtes SQL que vous exécutez sur la base de données. Au-dessus de chaque requête, étiquetez chacune avec un commentaire (en SQL, les commentaires sont toutes les lignes qui commencent par `--`) décrivant pourquoi vous exécutez la requête et/ou quelle information vous espérez obtenir à partir de cette requête particulière. Vous pouvez utiliser des commentaires dans le fichier journal pour ajouter des notes supplémentaires sur votre processus de réflexion pendant que vous résolvez le mystère : en fin de compte, ce fichier devrait servir de preuve du processus que vous avez utilisé pour identifier le voleur !

En écrivant vos requêtes, vous pouvez constater que certaines d'entre elles peuvent devenir très complexes. Pour aider à maintenir la lisibilité de vos requêtes, consultez les principes de bonne pratique sur [sqlstyle.guide](https://www.sqlstyle.guide). La section [indentation](https://www.sqlstyle.guide/#indentation) peut être particulièrement utile !

Une fois que vous avez résolu le mystère, complétez chacune des lignes de `answers.txt` en remplissant le nom du voleur, la ville dans laquelle le voleur s'est échappé, et le nom du complice du voleur qui les a aidés à quitter la ville. (Assurez-vous de ne pas changer le texte existant dans le fichier ou d'ajouter d'autres lignes au fichier !)

En fin de compte, vous devez soumettre à la fois vos fichiers `log.sql` et `answers.txt`.

Guide pas à pas
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/YHhgEoJMDnU?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Conseils
-----

* Exécutez `sqlite3 fiftyville.db` pour commencer à exécuter des requêtes sur la base de données.
    * Pendant l'exécution de `sqlite3`, l'exécution de `.tables` listera toutes les tables de la base de données.
    * Pendant l'exécution de `sqlite3`, exécuter `.schema NOM_DE_LA_TABLE`, où `NOM_DE_LA_TABLE` est le nom d'une table de la base de données, vous montrera la commande `CREATE TABLE` utilisée pour créer la table. Cela peut être utile pour savoir quelles colonnes interroger !
* Vous pouvez trouver utile de commencer par la table `crime_scene_reports`. Commencez par rechercher un rapport de la scène de crime qui correspond à la date et à l'emplacement du crime.
* Consultez cette [référence des mots clés SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) pour certains syntaxes SQL qui peuvent être utiles!

Testing
-------

Exécutez la commande suivante pour évaluer la justesse de votre code à l'aide de `check50`.

    check50 cs50/problems/2023/x/fiftyville
    
    
Comment soumettre
-------------

Dans votre terminal, exécutez la commande suivante pour soumettre votre travail :

    submit50 cs50/problems/2023/x/fiftyville
    

Remerciements
----------------

Inspiré par un autre cas chez [SQL City](https://mystery.knightlab.com/).