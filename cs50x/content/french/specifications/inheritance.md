Lab 5 : Héritage
==================

<div class="alert" data-alert="warning" role="alert"><p>Vous pouvez collaborer avec un ou deux camarades sur ce lab, mais il est attendu que chaque élève de ce groupe contribue de manière égale au lab.</p></div>

Simuler l'héritage des groupes sanguins pour chaque membre d'une famille. 

    $./inheritance
    Enfant (Génération 0) : groupe sanguin OO 
        Parent (Génération 1) : groupe sanguin AO 
            Grand-parent (Génération 2) : groupe sanguin OA 
            Grand-parent (Génération 2): groupe sanguin BO 
        Parent (Génération 1) : groupe sanguin OB
            Grand-parent (Génération 2) : groupe sanguin AO 
            Grand-parent (Génération 2) : groupe sanguin BO 


Contexte
--------

Le groupe sanguin d'une personne est déterminé par deux allèles (différentes formes d'un gène). Les trois allèles possibles sont A, B et O, dont chaque personne a deux (qui peuvent être identiques ou différents). Chacun des parents d'un enfant transmet au hasard l'un de leurs deux allèles de groupe sanguin à leur enfant. Les combinaisons possibles de groupes sanguins sont donc : OO, OA, OB, AO, AA, AB, BO, BA et BB.

Par exemple, si un parent a le groupe sanguin AO et l'autre parent a le groupe sanguin BB, alors les groupes sanguins possibles de l'enfant seraient AB et OB, en fonction de l'allèle reçu de chaque parent. De même, si un parent a le groupe sanguin AO et l'autre parent a le groupe sanguin OB, alors les groupes sanguins possibles de l'enfant seraient AO, OB, AB et OO.

Pour commencer
---------------

Ouvrez [VS Code] (https://code.cs50.io/).

Commencez en cliquant dans votre fenêtre de terminal, puis exécutez `cd`. Vous devriez voir que son "invite" ressemble à ce qui suit.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal et exécutez ensuite

    wget https://cdn.cs50.net/2022/fall/labs/5/inheritance.zip
    

suivi de la touche Entrée pour télécharger un fichier ZIP appelé `inheritance.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère pour cette question!

Maintenant, exécutez

    unzip inheritance.zip
    

pour créer un dossier appelé `inheritance`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm inheritance.zip
    

et répondre par "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant

    cd inheritance
    

suivi de Entrée pour vous déplacer (c'est-à-dire ouvrir) dans ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    inheritance/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et vous devriez voir `inheritance.c`.

Si vous rencontrez des problèmes, suivez ces mêmes étapes et voyez si vous pouvez déterminer où vous vous êtes trompé!

Compréhension
-------------

Regardez le code de distribution dans `inheritance.c`.

Remarquez la définition d'un type appelé "personne". Chaque personne a un tableau de deux "parents", chacun étant un pointeur vers une autre structure "personne". Chaque personne a également un tableau de deux "allèles", chacun étant un "char" (soit `'A'`, `'B'` ou `'O'`).

Maintenant, jetez un coup d'œil à la fonction "main". La fonction commence par "initialiser" (c'est-à-dire fournir une entrée initiale à) un générateur de nombres aléatoires, que nous utiliserons plus tard pour générer des allèles aléatoires. La fonction `main` appelle ensuite la fonction `create_family` pour simuler la création de structures "personne" pour une famille de 3 générations (c'est-à-dire une personne, ses parents et ses grands-parents). Nous appelons ensuite `print_family` pour imprimer chacun de ces membres de la famille et leurs groupes sanguins. Enfin, la fonction appelle `free_family` pour "libérer" toute la mémoire qui a été précédemment allouée avec `malloc`.

Les fonctions `create_family` et `free_family` sont à vous d'écrire!

Détails de mise en œuvre
----------------------

Complétez la mise en œuvre de `inheritance.c`, de sorte qu'elle crée une famille d'une taille de génération spécifiée et assigne des allèles de groupes sanguins à chaque membre de la famille. La génération la plus ancienne aura des allèles attribués au hasard.

*   La fonction `create_family` prend un entier (`generations`) en entrée et doit allouer (via `malloc`) une personne pour chaque membre de la famille de ce nombre de générations, renvoyant un pointeur vers la personne de la plus jeune génération.
    *   Par exemple, `create_family(3)` devrait renvoyer un pointeur vers une personne avec deux parents, où chaque parent a également deux parents.
    *   Chaque `personne` doit avoir des `allèles` qui leur sont assignés. La génération la plus ancienne devrait avoir des allèles choisis au hasard (en appelant la fonction `random_allele`), et les générations plus jeunes devraient hériter d'un allèle (choisi au hasard) de chaque parent.
    *   Chaque `personne` doit avoir des `parents` qui leur sont assignés. La génération la plus ancienne devrait avoir `parents` réglés sur `NULL`, et les générations plus jeunes devraient avoir `parents` soit un tableau de deux pointeurs, chacun pointant vers un parent différent.

Nous avons divisé la fonction `create_family` en quelques `TODO` pour que vous puissiez les compléter.

*   Tout d'abord, vous devez allouer de la mémoire pour une nouvelle personne. Rappelez-vous que vous pouvez utiliser `malloc` pour allouer de la mémoire et `sizeof(personne)` pour obtenir le nombre d'octets à allouer.
*   Ensuite, nous avons inclus une condition pour vérifier si `generations > 1`.
    *   Si `generations > 1`, alors il y a plus de générations qui doivent encore être allouées. Nous avons déjà créé deux nouveaux `parents`, `parent0` et `parent1`, en appelant récursivement `create_family`. Votre fonction `create_family` devrait ensuite régler les pointeurs du parent de la nouvelle personne que vous avez créée. Enfin, assignez les deux `allèles` pour la nouvelle personne en choisissant au hasard un allèle de chaque parent.
    *   Sinon (si `generations == 1`), il n'y aura pas de données parentales pour cette personne. Les deux `parents` de votre nouvelle personne devraient être réglés sur `NULL`, et chaque `allèle` devrait être généré au hasard.
*   Enfin, votre fonction devrait renvoyer un pointeur pour la `personne` qui a été allouée.

La fonction `free_family` devrait accepter en entrée un pointeur vers une `personne`, libérer la mémoire pour cette personne et ensuite libérer récursivement la mémoire pour tous leurs ancêtres.

*   Étant donné que c'est une fonction récursive, vous devriez d'abord traiter le cas de base. Si l'entrée de la fonction est `NULL`, il n'y a rien à libérer, donc votre fonction peut retourner immédiatement.
*   Sinon, vous devriez libérer récursivement les deux parents de la personne avant de libérer l'enfant.

### Démonstration

<div class="alert" data-alert="primary" role="alert"><p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse être différente de votre espace de code, le comportement des deux environnements devrait être largement similaire!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/9p7ddI3ozTY"></iframe>


### Indices

*   Vous pouvez trouver la fonction `rand()` utile pour affecter les allèles au hasard. Cette fonction renvoie un entier entre `0` et `RAND_MAX`, ou `2147483647`.
    *   En particulier, pour générer un nombre pseudo-aléatoire qui est soit `0` ou `1`, vous pouvez utiliser l'expression `rand() % 2`.
*   Souvenez-vous, pour allouer de la mémoire pour une personne particulière, nous pouvons utiliser `malloc(n)`, qui prend une taille en argument et allouera `n` octets de mémoire.
*   Souvenez-vous, pour accéder à une variable via un pointeur, nous pouvons utiliser la notation de flèche.
    *   Par exemple, si `p` est un pointeur vers une personne, alors un pointeur vers le premier parent de cette personne peut être accédé par `p->parents[0]`.

<details><summary>Pas sûr comment faire?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border"data-video="" src="https://video.cs50.io/H7LULatPwcQ"></iframe></details>


### Comment tester votre code

Après exécution de `./inheritance`, votre programme devrait suivre les règles décrites dans le contexte. L'enfant devrait avoir deux allèles, un de chaque parent. Les parents devraient chacun avoir deux allèles, un de chacun de leurs parents.

Par exemple, dans l'exemple ci-dessous, l'enfant de la Génération 0 a reçu un allèle O de chaque parent de la Génération 1. Le premier parent a reçu un A du premier grand-parent et un O du deuxième grand-parent. De même, le deuxième parent a reçu un O et un B de ses grands-parents.

    $ ./inheritance
    Child (Generation 0): blood type OO
        Parent (Generation 1): blood type AO
            Grandparent (Generation 2): blood type OA
            Grandparent (Generation 2): blood type BO
        Parent (Generation 1): blood type OB
            Grandparent (Generation 2): blood type AO
            Grandparent (Generation 2): blood type BO
    
    

Exécutez le code ci-dessous pour évaluer la correction de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester vous-même également!

    check50 cs50/labs/2023/x/inheritance
    

Exécutez le code ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 inheritance.c
    

Comment soumettre
-------------

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

    submit50 cs50/labs/2023/x/inheritance"

