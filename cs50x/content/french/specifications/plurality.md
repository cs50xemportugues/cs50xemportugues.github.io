Pluralité
=========

Pour ce programme, vous allez implémenter un programme qui effectue une élection à la pluralité, comme ci-dessous.

    $ ./plurality Alice Bob Charlie
    Nombre d'électeurs : 4
    Vote : Alice
    Vote : Bob
    Vote : Charlie
    Vote : Alice
    Alice
    

Contexte
--------

Les élections prennent toutes sortes de formes et de tailles. Au Royaume-Uni, le [Premier Ministre](https://www.parliament.uk/education/about-your-parliament/general-elections/) est officiellement nommé par le monarque, qui choisit généralement le chef du parti politique qui remporte le plus de sièges à la Chambre des communes. Aux États-Unis, un processus multi-étapes [Collège électoral](https://www.archives.gov/federal-register/electoral-college/about.html) est utilisé, où les citoyens votent sur la manière dont chaque État doit allouer des électeurs qui élisent ensuite le Président.

Le moyen le plus simple de tenir une élection est peut-être une méthode communément appelée "vote à la pluralité" (également connue sous le nom de "premier-passe-partout" ou "tout pour le gagnant"). Dans le vote à la pluralité, chaque électeur a le droit de voter pour un candidat. À la fin de l'élection, le candidat ayant le plus grand nombre de votes est déclaré vainqueur de l'élection.

Mise en route
--------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez voir que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $
    

Exécutez ensuite

    wget https://cdn.cs50.net/2022/fall/psets/3/plurality.zip
    

afin de télécharger un fichier ZIP appelé "plurality.zip" dans votre espace de code.

Ensuite, exécutez

    unzip plurality.zip
    

pour créer un dossier appelé "plurality". Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm plurality.zip
    

et répondre "y", suivi de Enter à la invite pour supprimer le fichier ZIP téléchargé.

Tapez maintenant

    cd plurality
    

puis appuyez sur Enter pour vous déplacer dans ce répertoire (c'est-à-dire l'ouvrir). Votre invite devrait désormais ressembler à ce qui suit :

    plurality/ $
    

Si tout s'est déroulé correctement, vous devez exécuter

    ls
    

et voir un fichier nommé "plurality.c". L'exécution de `code plurality.c` doit ouvrir le fichier où vous allez taper votre code pour cet ensemble de problèmes. Sinon, retracez vos étapes et voyez si vous pouvez déterminer où vous vous êtes trompé!

Compréhension
-------------

Jetons un coup d'œil à "plurality.c" et lisons le code de distribution qui vous a été fourni.

La ligne `#define MAX 9` est une syntaxe utilisée ici pour signifier que `MAX` est une constante (égale à `9`) qui peut être utilisée dans l'ensemble du programme. Ici, il représente le nombre maximum de candidats qu'une élection peut avoir.

Le fichier définit ensuite une `struct` appelée `candidate`. Chaque `candidate` a deux champs : une `string` appelée `name` représentant le nom du candidat et un `int` appelé `votes` représentant le nombre de votes que le candidat a obtenus. Ensuite, le fichier définit un tableau global de `candidates`, où chaque élément est lui-même un `candidate`.

Maintenant, regardez la fonction `main` elle-même. Voyez si vous pouvez trouver où le programme définit la variable globale `candidate_count` représentant le nombre de candidats à l'élection, copie les arguments de ligne de commande dans le tableau `candidates` et demande à l'utilisateur de saisir le nombre d'électeurs. Ensuite, le programme permet à chaque électeur de saisir un vote (voir comment ?), appelant la fonction `vote` pour chaque candidat pour lequel il a voté. Enfin, la `main` appelle la fonction `print_winner` pour imprimer le vainqueur (ou les vainqueurs) de l'élection.

Cependant, si vous regardez plus loin dans le fichier, vous remarquerez que les fonctions `vote` et `print_winner` ont été laissées vides. Cette partie est à vous de la remplir!

Spécification
-------------

Complétez l'implémentation de "plurality.c" de manière à ce que le programme simule une élection à la pluralité.

*   Complétez la fonction `vote`.
    *   `vote` prend un seul argument, une `string` appelée `name`, représentant le nom du candidat pour lequel on a voté.
    *   Si `name` correspond à l'un des noms des candidats à l'élection, alors mettez à jour le nombre de votes du candidat pour prendre en compte le nouveau vote. La fonction `vote` doit alors renvoyer `true` pour indiquer un bulletin de vote réussi.
    *   Si `name` ne correspond pas au nom d'un des candidats à l'élection, aucun total de votes ne doit changer, et la fonction `vote` doit renvoyer `false` pour indiquer un bulletin de vote invalide.
    *   Vous pouvez supposer que aucun candidat n'a le même nom.
*   Complétez la fonction `print_winner`.
    *   La fonction doit imprimer le nom du candidat qui a reçu le plus de votes lors de l'élection, puis imprimer une nouvelle ligne.
    *   Il est possible que l'élection se termine par une égalité si plusieurs candidats ont chacun le nombre maximum de votes. Dans ce cas, vous devriez imprimer les noms de chacun des candidats gagnants, chacun sur une ligne séparée.

Vous ne devez rien modifier d'autre dans "plurality.c" que les implémentations des fonctions `vote` et `print_winner` (et l'inclusion de fichiers d'en-tête supplémentaires, si vous le souhaitez).

Utilisation
-----

Votre programme doit se comporter comme ci-dessous.

    $ ./plurality Alice Bob
    Nombre d'électeurs : 3
    Vote : Alice
    Vote : Bob
    Vote : Alice
    Alice
    

    $ ./plurality Alice Bob
    Nombre d'électeurs : 3
    Vote : Alice
    Vote : Charlie
    Vote invalide.
    Vote : Alice
    Alice
    

    $ ./plurality Alice Bob Charlie
    Nombre d'électeurs : 5
    Vote : Alice
    Vote : Charlie
    Vote : Bob
    Vote : Bob
    Vote : Alice
    Alice
    Bob
    

Guide pas à pas
---------------


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ftOapzDjEb8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Tests
-------

Assurez-vous de tester votre code pour vous assurer qu'il gère...

*   Une élection avec un nombre quelconque de candidats (jusqu'à une `MAX` de `9`)
*   Voter pour un candidat par son nom
*   Des votes invalides pour les candidats qui ne sont pas sur le bulletin de vote
*   L'impression du vainqueur de l'élection s'il n'y en a qu'un
*   L'impression du vainqueur de l'élection s'il y a plusieurs vainqueurs

Exécutez le code ci-dessous pour évaluer la justesse de votre code à l'aide de `check50`. Mais assurez-vous également de le compiler et de le tester vous-même !

    check50 cs50/problems/2023/x/plurality
    

Exécutez le code ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 plurality.c
    

Comment soumettre
-------------

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/plurality"