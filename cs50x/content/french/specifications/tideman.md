Tideman
=======

Pour ce programme, vous allez mettre en place un programme qui exécute une élection Tideman, selon l'exemple ci-dessous.

    $ ./tideman Alice Bob Charlie
    Nombre de votants : 5
    Rang 1 : Alice
    Rang 2 : Charlie
    Rang 3 : Bob
    
    Rang 1 : Alice
    Rang 2 : Charlie
    Rang 3 : Bob
    
    Rang 1 : Bob
    Rang 2 : Charlie
    Rang 3 : Alice
    
    Rang 1 : Bob
    Rang 2 : Charlie
    Rang 3 : Alice
    
    Rang 1 : Charlie
    Rang 2 : Alice
    Rang 3 : Bob
    
    Charlie
    

Contexte
----------

Vous connaissez déjà les élections de pluralité, qui suivent un algorithme très simple pour déterminer le vainqueur d'une élection : chaque votant a un vote et le candidat ayant le plus de votes gagne.

Mais le vote de pluralité a quelques inconvénients. Que se passe-t-il, par exemple, dans une élection avec trois candidats et les bulletins de vote ci-dessous sont tels que :

![Five ballots, tie betweeen Alice and Bob](https://cs50.harvard.edu/x/2023/psets/3/fptp_ballot_1.png)

Un vote de pluralité déclarerait ici une égalité entre Alice et Bob, car chacun a deux voix. Mais est-ce le résultat idéal ?

Il existe un autre type de système de vote appelé système de vote par choix classé. Dans un système de vote classé, les électeurs peuvent voter pour plusieurs candidats. Au lieu de ne voter que pour leur choix préféré, ils peuvent classer les candidats par ordre de préférence. Les bulletins de vote qui en résultent pourraient ressembler à cela.

![Three ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_1.png)

Ici, chaque électeur, en plus de spécifier son premier choix de candidat, a également indiqué son deuxième et troisième choix. Et maintenant, ce qui était auparavant une élection serrée pourrait avoir un vainqueur. La course était à l'origine à égalité entre Alice et Bob. Mais l'électeur qui a choisi Charlie a préféré Alice à Bob, de sorte qu'Alice pourrait alors être déclarée la gagnante.

Le vote par choix classé peut également résoudre un autre inconvénient potentiel du vote de pluralité. Jetez un coup d'œil aux bulletins de vote suivants.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/condorcet_1.png)

Qui devrait gagner cette élection ? Dans un vote de pluralité où chaque électeur ne choisit que son premier choix, Charlie remporte cette élection avec quatre voix contre seulement trois pour Bob et deux pour Alice. (Notez que si vous êtes familier avec le système de vote instantané, Charlie remporte également cette élection sous ce système). Alice pourrait cependant faire valoir à juste titre qu'elle devrait être la gagnante de l'élection au lieu de Charlie : après tout, des neuf électeurs, une majorité (cinq d'entre eux) ont préféré Alice à Charlie, donc la plupart des gens seraient plus heureux si Alice était la gagnante et pas Charlie.

Alice est, dans cette élection, le prétendant "Condorcet" à la victoire de l'élection : la personne qui aurait remporté chaque confrontation tête-à-tête contre un autre candidat. Si l'élection n'avait été qu'entre Alice et Bob, ou qu'entre Alice et Charlie, Alice aurait gagné.

La méthode de vote de Tideman (également connue sous le nom de "classement par paires") est une méthode de vote par choix classé garantissant que le vainqueur de l'élection est le gagnant de Condorcet si un tel vainqueur existe.

En général, la méthode de Tideman fonctionne en construisant un « graphique » de candidats, où une flèche (c'est-à-dire un bord) du candidat A au candidat B indique que le candidat A bat le candidat B dans un match tête-à-tête. Le graphique de l'élection ci-dessus ressemblerait donc au suivant.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/condorcet_graph_1.png)

La flèche d'Alice vers Bob signifie que plus d'électeurs préfèrent Alice à Bob (5 préférant Alice, 4 préférant Bob). De même, les autres flèches signifient que plus d'électeurs préfèrent Alice à Charlie et plus d'électeurs préfèrent Charlie à Bob.

En regardant ce graphique, la méthode de Tideman dit que le gagnant de l'élection doit être la « source » du graphique (c'est-à-dire le candidat qui n'a pas de flèche pointant sur lui). Dans ce cas, la source est Alice. Alice est la seule personne qui n'a pas de flèche pointant sur elle, ce qui signifie que personne n'est préféré au premier choix que Alice. Alice est donc déclarée gagnante de l'élection.

Il est possible, cependant, que lors de la création de flèches, il n'y ait pas de vainqueur Condorcet. Considérez les bulletins de vote suivants.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/no_condorcet_1.png)

Entre Alice et Bob, Alice est préférée à Bob par une marge de 7 à 2. Entre Bob et Charlie, Bob est préféré à Charlie par une marge de 5 à 4. Mais entre Charlie et Alice, Charlie est préféré à Alice par une marge de 6 à 3. Si nous dessinons le graphique, il n'y a pas de source ! Nous avons un cycle de candidats, où Alice bat Bob qui bat Charlie qui bat Alice (tout comme un jeu de pierre-papier-ciseaux). Dans ce cas, il semble qu'il n'y ait pas de moyen de choisir un gagnant.

Pour y remédier, l'algorithme de Tideman doit être prudent pour éviter de créer des cycles dans le graphique des candidats. Comment fait-il cela ? L'algorithme verrouille d'abord les bords les plus forts, car ils sont les plus significatifs. En particulier, l'algorithme de Tideman précise que les bords de match doivent être « verrouillés » sur le graphique un par un, en fonction de la « force » de la victoire (plus de personnes préférant un candidat à son adversaire, plus la victoire est forte). Tant que le bord peut être verrouillé dans le graphique sans créer de cycle, le bord est ajouté ; sinon, le bord est ignoré.

Comment cela fonctionnerait-il dans le cas des votes ci-dessus ? Eh bien, la marge de victoire la plus importante pour une paire est Alice battant Bob, car 7 électeurs préfèrent Alice à Bob (aucun autre match tête-à-tête n'a un vainqueur préféré par plus de 7 électeurs). Donc, la flèche d'Alice à Bob est verrouillée en premier dans le graphique. La prochaine marge de victoire la plus importante est la victoire de Charlie de 6-3 sur Alice, donc cette flèche est verrouillée ensuite.

Ensuite, il y a la victoire de Bob de 5 à 4 sur Charlie. Mais remarquez bien : si nous ajoutions une flèche de Bob à Charlie maintenant, nous créerions un cycle ! Puisque le graphique ne peut pas contenir de cycles, nous devrions sauter cette flèche et ne pas l'ajouter du tout. S'il y avait plus de flèches à considérer, nous aurions cherché ensuite parmi celles-ci, mais c'était la dernière flèche, donc le graphique est complet.

Ce processus étape par étape est montré ci-dessous, avec le graphique final à droite.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2023/psets/3/lockin.png)

Sur la base du graphique résultant, Charlie est la source (il n'y a pas de flèche pointant vers Charlie), donc Charlie est déclaré vainqueur de cette élection.

Plus formellement, la méthode de vote de Tideman se compose de trois parties :

*   **Décompte** : Une fois que tous les votants ont indiqué toutes leurs préférences, déterminez, pour chaque paire de candidats, le candidat préféré et la marge par laquelle il est préféré.
*   **Classement** : Triez les paires de candidats dans l'ordre décroissant de la force de la victoire, où la force de la victoire est définie comme le nombre de votants qui préfèrent le candidat préféré.
*   **Verrouiller** : À partir de la paire la plus forte, passez en revue les paires de candidats dans l'ordre et "verrouillez" chaque paire dans le graphique des candidats, tant que le verrouillage de cette paire ne crée pas de cycle dans le graphique.

Lorsque le graphique est complet, la source du graphique (celui sans bords pointant vers lui) est le gagnant !

Pour commencer
--------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez la commande `cd`. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ceci :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/3/tideman.zip
    

afin de télécharger un fichier ZIP appelé `tideman.zip` dans votre espace de code.

Ensuite, exécutez

    unzip tideman.zip
    

pour créer un dossier appelé `tideman`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm tideman.zip
    

et répondre "y" suivi de la touche Entrée à la invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd tideman
    

suivi de Entrée pour vous déplacer dans ce répertoire. Votre invite devrait maintenant ressembler à ceci :

    tideman/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et voir un fichier appelé `tideman.c`. L'exécution de la commande `code tideman.c` devrait ouvrir le fichier où vous taperez votre code pour cet ensemble de problèmes. Sinon, retracez vos pas et essayez de déterminer où vous vous êtes trompé !

Compréhension
-------------

Jetons un coup d'œil à `tideman.c`.

Tout d'abord, remarquez le tableau bidimensionnel `preferences`. L'entier `preferences[i][j]` représentera le nombre d'électeurs qui préfèrent le candidat `i` au candidat `j`.

Le fichier définit également un autre tableau bidimensionnel, appelé `locked`, qui représentera le graphique des candidats. `locked` est un tableau booléen, alors que `locked[i][j]` étant `true` représente l'existence d'un bord pointant du candidat `i` au candidat `j` ; `false` signifie qu'il n'y a pas de bord. (Si vous êtes curieux, cette représentation d'un graphique est connue sous le nom de «matrice d'adjacence»).

Ensuite, il y a une `struct` appelée `pair`, utilisée pour représenter une paire de candidats : chaque paire comprend l'index du candidat `gagnant` et l'index du candidat `perdant`.

Les candidats eux-mêmes sont stockés dans le tableau `candidates`, qui est un tableau de chaînes de caractères représentant les noms de chacun des candidats. Il y a également un tableau de `pairs`, qui représentera toutes les paires de candidats (pour lesquelles l'un est préféré à l'autre) dans l'élection.

Le programme a également deux variables globales : `pair_count` et `candidate_count`, représentant le nombre de paires et le nombre de candidats dans les tableaux `pairs` et `candidates`, respectivement.

Passons maintenant à `main`. Remarquez qu'après avoir déterminé le nombre de candidats, le programme boucle à travers le graphique `locked` et initialise initialement toutes les valeurs à `false`, ce qui signifie que notre graphique initial n'aura aucun bord.

Ensuite, le programme boucle sur tous les votants et recueille leurs préférences dans un tableau appelé `ranks` (via un appel à `vote`), où `ranks[i]` est l'index du candidat qui est la `i`ème préférence pour l'électeur. Ces classements sont passés à la fonction `record_preference`, dont le travail est de prendre ces classements et de mettre à jour la variable globale `preferences`.

Une fois que tous les votes sont comptabilisés, les paires de candidats sont ajoutées au tableau `pairs` via un appel à `add_pairs`, triées via un appel à `sort_pairs` et verrouillées dans le graphique via un appel à `lock_pairs`. Enfin, `print_winner` est appelé pour afficher le nom du gagnant de l'élection !

Plus bas dans le fichier, vous verrez que les fonctions `vote`, `record_preference`, `add_pairs`, `sort_pairs`, `lock_pairs` et `print_winner` sont laissées en blanc. C'est à vous de les remplir !

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

Utilisation
-----------

Votre programme doit se comporter comme l'exemple ci-dessous :

    ./tideman Alice Bob Charlie
    Nombre de votants : 5
    Rang 1 : Alice
    Rang 2 : Charlie
    Rang 3 : Bob
    
    Rang 1 : Alice
    Rang 2 : Charlie
    Rang 3 : Bob
    
    Rang 1 : Bob
    Rang 2 : Charlie
    Rang 3 : Alice
    
    Rang 1 : Bob
    Rang 2 : Charlie
    Rang 3 : Alice
    
    Rang 1 : Charlie
    Rang 2 : Alice
    Rang 3 : Bob
    
    Charlie
    

Test
----

Assurez-vous de tester votre code pour vous assurer qu'il gère...

*   Une élection avec un nombre quelconque de candidats (jusqu'au MAX de 9)
*   Voter pour un candidat par son nom
*   Des votes invalides pour les candidats qui ne sont pas sur le bulletin de vote
*   L'impression du vainqueur de l'élection

Exécutez ci-dessous pour évaluer la correction de votre code en utilisant `check50`. Mais assurez-vous également de le compiler et de le tester vous-même !

    check50 cs50/problems/2023/x/tideman
    

Exécutez ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 tideman.c
    

Comment soumettre
-----------------

Dans votre terminal, exécutez ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/tideman"

