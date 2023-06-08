Lab 7 : Chansons
============

<div class = "alerte" data-alerte ="warning" role = "alert"><p>Vous êtes invités à collaborer avec un ou deux camarades de classe sur ce lab, bien qu'il soit attendu que chaque étudiant d'un tel groupe contribue également au labo.</p></div>

Écrivez des requêtes SQL pour répondre à des questions sur une base de données de chansons.

Pour commencer
---------------

Ouvrez [VS Code] (https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à ceci.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/labs/7/songs.zip
    

suivi de Enter pour télécharger un ZIP appelé `songs.zip` dans votre codespace. Faites attention de ne pas manquer l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs!

Maintenant, exécutez

    unzip songs.zip
    

pour créer un dossier appelé `songs`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm songs.zip
    

et répondez "y" suivi de Enter à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd songs
    

suivi de Enter pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ceci.

    songs/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et vous devriez voir 8 fichiers .sql, `songs.db`, et `answers.txt`.

Si vous rencontrez un problème, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous vous êtes trompé!

Compréhension
-------------

Un fichier appelé `songs.db` vous est fourni, une base de données SQLite qui stocke des données de [Spotify] (https://developer.spotify.com/documentation/web-api/) sur des chansons et leurs artistes. Ce jeu de données contient les 100 chansons les plus diffusées sur Spotify en 2018. Dans une fenêtre de terminal, exécutez `sqlite3 songs.db` pour commencer à exécuter des requêtes sur la base de données.

Tout d'abord, lorsque `sqlite3` vous invite à fournir une requête, tapez `.schema` et appuyez sur entrée. Cela affichera les déclarations `CREATE TABLE` qui ont été utilisées pour générer chacune des tables de la base de données. En examinant ces déclarations, vous pouvez identifier les colonnes présentes dans chaque table.

Remarquez que chaque `artiste` a un `id` et un `nom`. Remarquez également que chaque chanson a un `nom`, un `artist_id` (correspondant à l'`id` de l'artiste de la chanson), ainsi que des valeurs pour la danseabilité, l'énergie, la clé, la sonie, la parole (présence de mots parlés dans une piste), la valence, le tempo et la durée de la chanson (mesurée en millisecondes).

Le défi qui vous attend consiste à écrire des requêtes SQL pour répondre à une variété de questions différentes en sélectionnant des données à partir d'une ou plusieurs de ces tables. Après cela, vous réfléchirez aux façons dont Spotify pourrait utiliser ces mêmes données dans leur campagne annuelle [Spotify Wrapped] (https://en.wikipedia.org/wiki/Spotify_Wrapped) pour caractériser les habitudes des auditeurs.

Détails de la mise en œuvre
----------------------

Pour chacun des problèmes suivants, vous devez écrire une seule requête SQL qui produit les résultats spécifiés par chaque problème. Votre réponse doit prendre la forme d'une seule requête SQL, bien que vous puissiez imbriquer d'autres requêtes à l'intérieur de votre requête. Vous ne devez **pas** supposer quoi que ce soit sur les `id` de certaines chansons ou artistes: vos requêtes doivent être précises même si l'`id` de certaines chansons ou personnes étaient différentes. Enfin, chaque requête doit renvoyer uniquement les données nécessaires pour répondre à la question: si le problème vous demande uniquement de sortir les noms de chansons, par exemple, votre requête ne doit pas également sortir le tempo de chaque chanson.

1. Dans `1.sql`, écrivez une requête SQL pour lister les noms de toutes les chansons de la base de données.
    * Votre requête devrait produire une table avec une seule colonne pour le nom de chaque chanson.
2. Dans `2.sql`, écrivez une requête SQL pour lister les noms de toutes les chansons par ordre croissant des tempos.
    * Votre requête devrait produire une table avec une seule colonne pour le nom de chaque chanson.
3. Dans `3.sql`, écrivez une requête SQL pour lister les noms des 5 chansons les plus longues, par ordre décroissant de durée.
    * Votre requête devrait produire une table avec une seule colonne pour le nom de chaque chanson.
4. Dans `4.sql`, écrivez une requête SQL qui liste les noms des chansons ayant une danseabilité, une énergie et une valence supérieures à 0,75.
    * Votre requête devrait produire une table avec une seule colonne pour le nom de chaque chanson.
5. Dans `5.sql`, écrivez une requête SQL qui renvoie l'énergie moyenne de toutes les chansons.
    * Votre requête devrait produire une table avec une seule colonne et une seule ligne contenant l'énergie moyenne.
6. Dans `6.sql`, écrivez une requête SQL qui liste les noms des chansons de Post Malone.
    * Votre requête devrait produire une table avec une seule colonne pour le nom de chaque chanson.
    * Vous ne devez faire aucune supposition sur l' `artist_id` de Post Malone.
7. Dans `7.sql`, écrivez une requête SQL qui renvoie l'énergie moyenne des chansons de Drake.
    * Votre requête devrait produire une table avec une seule colonne et une seule ligne contenant l'énergie moyenne.
    * Vous ne devez faire aucune supposition sur l' `artist_id` de Drake.
8. Dans `8.sql`, écrivez une requête SQL qui liste les noms des chansons avec d'autres artistes.
    * Les chansons avec d'autres artistes comporteront "feat." dans le nom de la chanson.
    * Votre requête doit produire une table avec une seule colonne pour le nom de chaque chanson.

### Procédure

<div class = "alerte" data-alerte ="primary" role = "alert"><p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse être différente de votre codespace, le comportement des deux environnements devrait être largement similaire!</p></div>

<iframe allow = "accéléromètre; lecture automatique; encrypted-media; gyroscope; picture-in-picture" allowfullscreen = "" class ="border" data-video = "" src ="https://video.cs50.io/wgKPUd_95AA"> </iframe>


Utilisation
-----

En plus d'exécuter vos requêtes dans `sqlite3`, vous pouvez tester vos requêtes dans le terminal VS Code en exécutant


    $ cat nomdufichier.sql | sqlite3 songs.db
    

où `filename.sql` est le fichier contenant votre requête SQL.

### Indices

* Voir [cette référence des mots clés SQL] (https://www.w3schools.com/sql/sql_ref_keywords.asp) pour une syntaxe SQL qui peut être utile!


<details> <summary> Pas sûr de savoir comment résoudre? </summary> <iframe allow = "accéléromètre; lecture automatique; encrypted-media; gyroscope; picture-in-picture" allowfullscreen = "" class = "border" data-video = "" src = "https://video.cs50.io/7hydPL9ZswE"> </iframe> </details>


### Spotify Wrapped

[Spotify Wrapped] (https://en.wikipedia.org/wiki/Spotify_Wrapped) est une fonctionnalité présentant les 100 chansons les plus écoutées des utilisateurs de Spotify de l'année écoulée. En 2021, Spotify Wrapped a calculé une ["aura audio"] (https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) pour chaque utilisateur, une "lecture de ses deux humeurs les plus importantes dictées par ses chansons et ses artistes préférés de l'année." Supposons que Spotify détermine une aura audio en regardant l'énergie moyenne, la valence et la danseabilité des 100 meilleures chansons d'une personne de l'année écoulée. Dans `answers.txt`, réfléchissez aux questions suivantes:

* Si `songs.db` contient les 100 meilleures chansons d'un auditeur de 2018, comment caractériseriez-vous son aura audio?
* Faites une hypothèse sur la raison pour laquelle la manière dont vous avez calculé cette aura pourrait ne pas être très représentative de l'auditeur. Qu