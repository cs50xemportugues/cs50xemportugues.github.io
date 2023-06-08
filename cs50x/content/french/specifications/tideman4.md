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