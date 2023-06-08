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