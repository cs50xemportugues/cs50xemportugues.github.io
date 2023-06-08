Spécification
-------------

Complétez l'implémentation de `tideman.c` de manière à simuler une élection Tideman.

*   Complétez la fonction `vote`.
    *   La fonction prend en argument `rank`, `name` et `ranks`. Si `name` correspond au nom d'un candidat valide, vous devez mettre à jour le tableau `ranks` pour indiquer que l'électeur a le candidat comme préférence dans son `rank` (où `0` est la première préférence, `1` la deuxième, etc.)
    *   Rappelons que `ranks[i]` représente ici la `i`ème préférence de l'utilisateur.
    *   La fonction doit renvoyer `true` si le rang a été enregistré avec succès et `false` sinon (par exemple si `name` n'est pas le nom d'un des candidats).
    *   Vous pouvez supposer qu'il n'y aura pas deux candidats avec le même nom.
*   Complétez la fonction `record_preferences`.
    *   La fonction est appelée une fois par électeur et prend en argument le tableau `ranks` (rappelons que `ranks[i]` est la `i`ème préférence de l'électeur, où `ranks[0]` est la première préférence).
    *   La fonction doit mettre à jour le tableau global `preferences` pour ajouter les préférences de l'électeur actuel. Rappelons que `preferences[i][j]` doit représenter le nombre d'électeurs qui préfèrent le candidat `i` au candidat `j`.
    *   Vous pouvez supposer que chaque électeur classera chacun des candidats.
*   Complétez la fonction `add_pairs`.
    *   La fonction doit ajouter toutes les paires de candidats où un candidat est préféré au tableau `pairs`. Une paire de candidats qui sont à égalité (un candidat n'est pas préféré à l'autre) ne doit pas être ajoutée au tableau.
    *   La fonction doit mettre à jour la variable globale `pair_count` pour qu'elle soit le nombre de paires de candidats. (Les paires doivent donc toutes être stockées entre `pairs[0]` et `pairs[pair_count - 1]`, inclusivement).
*   Complétez la fonction `sort_pairs`.
    *   La fonction doit trier le tableau `pairs` dans l'ordre décroissant de la force de la victoire, où la force de la victoire est définie comme le nombre d'électeurs qui préfèrent le candidat préféré. Si plusieurs paires ont la même force de victoire, vous pouvez supposer que l'ordre n'a pas d'importance.
*   Complétez la fonction `lock_pairs`.
    *   La fonction doit créer le graphe `locked`, en ajoutant toutes les arêtes en ordre décroissant de la force de victoire tant que l'arête ne créerait pas de cycle.
*   Complétez la fonction `print_winner`.
    *   La fonction doit afficher le nom du candidat qui est la source du graphe. Vous pouvez supposer qu'il n'y aura pas plus d'une source.

Vous ne devez pas modifier autre chose dans `tideman.c` que les implémentations des fonctions `vote`, `record_preferences`, `add_pairs`, `sort_pairs`, `lock_pairs` et `print_winner` (et l'inclusion de fichiers d'en-tête supplémentaires, si vous le souhaitez). Vous êtes autorisé à ajouter des fonctions supplémentaires à `tideman.c`, à condition de ne pas modifier les déclarations des fonctions existantes.

Pas à pas
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/kb83NwyYI68?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>