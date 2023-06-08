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