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