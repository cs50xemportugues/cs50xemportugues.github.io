Runoff
======

Pour ce programme, vous allez implémenter un programme qui organise une élection à deux tours, conformément à ce qui suit.

    ./runoff Alice Bob Charlie
    Nombre de votants : 5
    Rang 1 : Alice
    Rang 2 : Bob
    Rang 3 : Charlie
    
    Rang 1 : Alice
    Rang 2 : Charlie
    Rang 3 : Bob
    
    Rang 1 : Bob
    Rang 2 : Charlie
    Rang 3 : Alice
    
    Rang 1 : Bob
    Rang 2 : Alice
    Rang 3 : Charlie
    
    Rang 1 : Charlie
    Rang 2 : Alice
    Rang 3 : Bob
    
    Alice
    

Contexte
--------

Vous connaissez déjà le système de vote majoritaire qui suit un algorithme très simple pour déterminer le vainqueur de l'élection : chaque électeur a un vote et le candidat avec le plus de votes remporte l’élection.

Mais le système de vote majoritaire à également quelques inconvénients. Que se passe-t-il, par exemple, lorsqu'une élection a trois candidats, et que les bulletins de vote ci-dessous sont exprimés ?

![Cinq bulletins de vote, ex-aequo entre Alice et Bob](https://cs50.harvard.edu/x/2023/psets/3/fptp_ballot_1.png)

Un vote majoritaire déclare un match nul entre Alice et Bob, car chacun a deux votes. Mais est-ce le résultat approprié ?

Il existe un autre type de système de vote connu sous le nom de vote préférentiel. Dans un système de vote préférentiel, les électeurs peuvent voter pour plus d'un candidat. Au lieu de simplement voter pour leur premier choix, ils peuvent classer les candidats par ordre de préférence. Les bulletins de vote résultants pourraient ressembler à ce qui suit.

![Trois bulletins de vote, avec des préférences classées](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_1.png)

Ici, chaque électeur, en plus de spécifier leur candidat préféré, a également indiqué leurs deuxième et troisième choix. Et maintenant, ce qui était auparavant une élection nulle pourrait désormais avoir un vainqueur. La course était à égalité entre Alice et Bob, alors que Charlie était hors de concours. Mais l'électeur qui a choisi Charlie a préféré Alice à Bob, donc Alice est déclarée vainqueur.

Le vote préférentiel peut également résoudre un autre inconvénient potentiel du vote majoritaire. Jetez un coup d'œil aux bulletins de vote suivants.

![Neuf bulletins de vote, avec des préférences classées](https://cs50.harvard.edu/x/2023/psets/3/ranked_ballot_3.png)

Qui devrait gagner cette élection ? Avec un vote majoritaire où chaque électeur ne choisit que son premier choix, Charlie remporte l'élection avec quatre votes contre trois pour Bob et deux pour Alice. Mais la majorité des électeurs (5 sur 9) préférerait plutôt Alice ou Bob plutôt que Charlie. En considérant les préférences classées, un système de vote peut être en mesure de choisir un vainqueur qui reflète mieux les préférences des électeurs.


L'un de ces système de vote préférentiel est le système de vote à deux tours. Dans une élection à deux tours, les électeurs peuvent classer autant de candidats qu'ils le souhaitent. Si un candidat a la majorité (plus de 50 %) des premiers choix, ce candidat est déclaré vainqueur de l'élection.

Si aucun candidat n'a plus de 50% des votes, un "deuxième tour" est organisé. Le candidat ayant reçu le plus petit nombre de votes est éliminé de l'élection et tous ceux qui ont initialement choisi ce candidat comme premier choix ont maintenant leur deuxième choix considéré. Pourquoi faire cela ? En effet, cela simule ce qui se serait passé si le candidat le moins populaire n'était pas en lice pour commencer.

Le processus se répète : si aucun candidat n'a la majorité des votes, le candidat en dernière position est éliminé et tous ceux qui ont voté pour lui voteront plutôt pour leur choix suivant (qui n'a pas déjà été éliminé). Une fois qu'un candidat a la majorité, ce candidat est déclaré vainqueur.

Prenons les neuf bulletins de vote ci-dessus et examinons comment se déroulerait un vote à deux tours.

Alice a deux votes, Bob a trois votes et Charlie a quatre votes. Pour remporter une élection avec neuf personnes, une majorité (cinq votes) est requise. Etant donné qu'aucun candidat n'a de majorité, un deuxième tour est nécessaire. Alice a le plus petit nombre de voix (avec seulement deux voix), donc Alice est éliminée. Les électeurs qui ont initialement voté pour Alice ont choisi Bob comme deuxième choix, donc Bob obtient les deux voix supplémentaires. Maintenant, Bob a cinq voix et Charlie en a toujours quatre. Bob a maintenant la majorité et Bob est déclaré vainqueur.

Quels sont les cas particuliers que nous devons considérer ici ?

Il est possible que deux candidats soient à égalité et qu'ils soient tous deux éliminés. Nous pouvons gérer ce cas en disant que tous les candidats à égalité pour la dernière place seront éliminés. Si chaque candidat restant a exactement le même nombre de votes, éliminer tous les candidats à égalité pour la dernière place signifie éliminer tout le monde ! Dans ce cas, nous devrons être prudents de ne pas éliminer tout le monde et simplement déclarer une égalité entre tous les candidats restants.

Certains scrutins à deux tours ne nécessitent pas que les électeurs classent toutes leurs préférences - il pourrait donc y avoir cinq candidats dans une élection, mais un électeur pourrait n'en choisir que deux. À des fins de résolution de ce problème, cependant, nous ignorerons ce cas particulier et supposerons que tous les électeurs classeront tous les candidats dans leur ordre de préférence préféré.

Cela semble un peu plus compliqué qu'un vote majoritaire, n'est-ce pas ? Mais cela a sans doute l'avantage d'être un système électoral où le vainqueur des élections représente plus fidèlement les préférences des électeurs.

Débuter
-------

Connectez-vous à [code.cs50.io] (https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit:

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/3/runoff.zip
    

afin de télécharger un fichier ZIP appelé `runoff.zip` dans votre espace de code.

Ensuite, exécutez

    unzip runoff.zip
    

pour créer un dossier appelé `runoff`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm runoff.zip
    

et répondre "y" suivi de Entrée à la invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd runoff
    

suivi de Entrée pour vous déplacer dans ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    runoff/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et voir un fichier nommé `runoff.c`. Exécuter `code runoff.c` devrait ouvrir le fichier dans lequel vous allez taper votre code pour cette série de problèmes. Sinon, retracez vos étapes et voyez si vous pouvez déterminer où vous vous êtes trompé !

Compréhension
--------------

Jetons un coup d'œil à `runoff.c`. Nous définissons deux constantes: `MAX_CANDIDATES` pour le nombre maximum de candidats à l'élection et `MAX_VOTERS` pour le nombre maximum de votants à l'élection.

Ensuite, il y a un tableau bidimensionnel `preferences`. Le tableau `preferences[i]` représentera toutes les préférences pour l'électeur numéro `i`, et l'entier `preferences[i][j]` stockera l'indice du candidat qui est la `j`ème préférence pour l'électeur `i`.

Ensuite, il y a une structure appelée `candidate`. Chaque `candidate` a un champ `string` pour son `name`, un entier représentant le nombre de `votes` qu'il a actuellement, et une valeur `bool` appelée `eliminated` qui indique si le candidat a été éliminé de l'élection. Le tableau `candidates` suivra tous les candidats à l'élection.

Le programme contient également deux variables globales: `voter_count` et `candidate_count`.

Passons maintenant à `main`. Remarquez qu'après avoir déterminé le nombre de candidats et le nombre de votants, la boucle principale de vote commence, donnant à chaque votant une chance de voter. Lorsque l'électeur entre ses préférences, la fonction `vote` est appelée pour suivre toutes les préférences. Si à un moment donné, le bulletin de vote est considéré comme non valide, le programme se termine.

Une fois tous les votes enregistrés, une autre boucle commence: celle-ci va parcourir le processus de vote en votant jusqu'à trouver un gagnant et en éliminant le candidat en dernière position jusqu'à ce qu'il y ait un gagnant.

Le premier appel ici est à une fonction appelée `tabulate`, qui devrait examiner toutes les préférences des électeurs et calculer les totaux de vote actuels, en examinant le candidat préféré de chaque électeur qui n'a pas encore été éliminé. Ensuite, la fonction `print_winner` doit afficher le vainqueur s'il y en a un; si c'est le cas, le programme est terminé. Sinon, le programme doit déterminer le nombre de votes le plus faible que quiconque encore dans l'élection a reçu (via un appel à `find_min`). S'il s'avère que tout le monde dans l'élection est à égalité avec le même nombre de votes (tel que déterminé par la fonction `is_tie`), l'élection est déclarée en égalité; sinon, le candidat ou les candidats en dernière position sont éliminés de l'élection via un appel à la fonction `eliminate`.

Si vous regardez un peu plus loin dans le fichier, vous verrez que ces fonctions - `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` et `eliminate` - sont toutes laissées à votre sauce pour compléter!

Spécification
-------------

Complétez l'implémentation de `runoff.c` de manière à simuler une élection. Vous devez terminer la mise en œuvre des fonctions `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` et `eliminate`, et vous ne devez rien modifier d'autre dans `runoff.c` (et dans l'inclusion de fichiers d'en-tête supplémentaires si vous le souhaitez).

### `vote`

Complétez la fonction `vote`.

* La fonction prend en argument `voter`, `rank`, et `name`. Si `name` correspond au nom d'un candidat valide, vous devez mettre à jour le tableau de préférences global pour indiquer que l'électeur `voter` a ce candidat comme préférence de rang `rank` (où `0` est la première préférence, `1` est la deuxième préférence, etc.).
* Si la préférence est enregistrée avec succès, la fonction doit retourner `true`; sinon, elle doit retourner `false` (si, par exemple, `name` n'est pas le nom d'un des candidats).
* Vous pouvez supposer que deux candidats n'auront pas le même nom.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous que `candidate_count` stocke le nombre de candidats dans l'élection.</li>
  <li data-marker="*">Rappelez-vous que vous pouvez utiliser <a href="https://man.cs50.io/3/strcmp"><code class="language-plaintext highlighter-rouge">strcmp</code></a> pour comparer deux chaînes de caractères.</li>
  <li data-marker="*">Rappelez-vous que `preferences[i][j]` stocke l'indice du candidat qui est la `j`-ème préférence classée pour l'électeur `i`.</li>
</ul></details>

### `tabulate`

Complétez la fonction `tabulate`.

* La fonction doit mettre à jour le nombre de `votes` de chaque candidat à cette étape du classement.
* Notez que, à chaque étape du classement, chaque électeur vote effectivement pour son candidat le mieux classé qui n'a pas encore été éliminé.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous que `voter_count` stocke le nombre d'électeurs dans l'élection et que, pour chaque électeur de notre élection, nous voulons compter un bulletin de vote.</li>
  <li data-marker="*">Rappelez-vous que, pour un électeur `i`, son candidat de choix est représenté par `preferences[i][0]`, son deuxième choix de candidat par `preferences[i][1]`, etc.</li>
  <li data-marker="*">Rappelez-vous que la structure `candidate` a un champ appelé `eliminated`, qui sera `true` si le candidat a été éliminé de l'élection.</li>
  <li data-marker="*">Rappelez-vous que la structure `candidate` a un champ appelé `votes`, que vous voudrez probablement mettre à jour pour le candidat préféré de chaque électeur.</li>
  <li data-marker="*">Une fois que vous avez voté pour le premier candidat non éliminé d'un électeur, vous voudrez vous arrêter là, et ne pas continuer sur sa liste de préférences ! Rappelez-vous que vous pouvez sortir d'une boucle prématurément en utilisant `break` à l'intérieur d'une condition.</li>
</ul></details>

### `print_winner`

Complétez la fonction `print_winner`.

* Si un candidat a plus de la moitié des voix, son nom devrait être imprimé et la fonction devrait retourner `true`.
* Si personne n'a encore remporté l'élection, la fonction doit renvoyer `false`.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous que `voter_count` stocke le nombre d'électeurs dans l'élection. Étant donné cela, comment exprimeriez-vous le nombre de voix nécessaires pour remporter l'élection ?</li>
</ul></details>

### `find_min`

Complétez la fonction `find_min`.

* La fonction doit renvoyer le nombre de voix minimum pour tout candidat qui est encore dans l'élection.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Vous voudrez probablement parcourir les candidats pour trouver celui qui est encore dans l'élection et qui a le moins de voix. Quelles informations devriez-vous suivre pendant que vous parcourez les candidats ?</li>
</ul></details>

### `is_tie`

Complétez la fonction `is_tie`.

* La fonction prend en argument `min`, qui sera le nombre minimum de voix que quiconque dans l'élection a à ce moment-là.
* La fonction doit renvoyer `true` si tous les candidats restants dans l'élection ont le même nombre de voix et renvoyer `false` sinon.

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous qu'une égalité se produit si tous les candidats encore dans l'élection ont le même nombre de voix. Notez également que la fonction `is_tie` prend en argument `min`, qui est le plus petit nombre de voix actuellement obtenu par un candidat. Comment pourriez-vous utiliser cette information pour déterminer si l'élection est une égalité (ou, inversement, pas une égalité) ?</li>
</ul></details>

### `eliminate`

Complétez la fonction `eliminate`.

* La fonction prend en argument `min`, qui sera le nombre minimum de voix que quiconque dans l'élection a à ce moment-là.
* La fonction doit éliminer le candidat (ou les candidats) qui ont `min` nombre de votes.

Guide

-----

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Utilisation
-----------

Votre programme doit fonctionner comme dans l'exemple ci-dessous:

    ./runoff Alice Bob Charlie
    Nombre de votants: 5
    Rang 1: Alice
    Rang 2: Charlie
    Rang 3: Bob
    
    Rang 1: Alice
    Rang 2: Charlie
    Rang 3: Bob
    
    Rang 1: Bob
    Rang 2: Charlie
    Rang 3: Alice
    
    Rang 1: Bob
    Rang 2: Charlie
    Rang 3: Alice
    
    Rang 1: Charlie
    Rang 2: Alice
    Rang 3: Bob
    
    Alice
    

Tester
-------

Assurez-vous de tester votre code pour vous assurer qu'il prend en compte...

*   Une élection avec n'importe quel nombre de candidats (jusqu'à un maximum de `9`)
*   Voter pour un candidat en le nommant nommé
*   Des votes invalides pour les candidats qui ne sont pas sur le bulletin de vote
*   L'impression du gagnant de l'élection s'il y en a un seul
*   Ne pas éliminer personne en cas d'égalité entre tous les candidats restants

Exécutez la commande suivante pour évaluer la correction de votre code en utilisant `check50`. Mais n'oubliez pas de le compiler et de le tester vous-même !

    check50 cs50/problems/2023/x/runoff
    

Exécutez la commande suivante pour évaluer le style de votre code à l'aide de `style50`.

    style50 runoff.c
    

Comment soumettre
-----------------

Dans votre terminal, exécutez la commande suivante pour soumettre votre travail.

    submit50 cs50/problems/2023/x/runoff"

