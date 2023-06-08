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