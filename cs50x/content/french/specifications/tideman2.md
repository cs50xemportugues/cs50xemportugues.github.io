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