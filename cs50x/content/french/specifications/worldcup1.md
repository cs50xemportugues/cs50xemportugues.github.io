Laboratoire 6 : Coupe du Monde
================

<div class="alert" data-alert="warning" role="alert"><p>Vous êtes invité à collaborer avec un ou deux camarades de classe pour ce laboratoire, mais chaque étudiant dans un tel groupe est censé contribuer de manière équitable au laboratoire.</p></div>

Écrire un programme pour exécuter des simulations de la Coupe du Monde de la FIFA.

    $ python tournament.py 2018m.csv
    Belgique: 20,9% de chance de gagner
    Brésil: 20,3 % de chance de gagner
    Portugal: 14,5% de chance de gagner
    Espagne : 13,6 % de chance de gagner
    Suisse: 10,5% de chance de gagner
    Argentine: 6,5 % de chance de gagner
    Angleterre: 3,7 % de chance de gagner
    France: 3,3 % de chance de gagner
    Danemark: 2,2 % de chance de gagner
    Croatie: 2,0 % de chance de gagner
    Colombie: 1,8 % de chance de gagner
    Suède: 0,5 % de chance de gagner
    Uruguay: 0,1 % de chance de gagner
    Mexique: 0,1 % de chance de gagner
    

Contexte
----------

Dans la Coupe du Monde de football, le tour éliminatoire se compose de 16 équipes. À chaque tour, chaque équipe affronte une autre équipe et les équipes perdantes sont éliminées. Lorsqu'il ne reste plus que deux équipes, le vainqueur de la finale est champion.

En football, les équipes se voient attribuer des [FIFA Ratings](https://en.wikipedia.org/wiki/FIFA_World_Rankings#Current_calculation_method), qui sont des valeurs numériques représentant le niveau de compétence relatif de chaque équipe. Les FIFA ratings élevés indiquent de meilleurs résultats de matchs précédents, et étant donné les FIFA ratings de deux équipes, il est possible d'estimer la probabilité que l'une ou l'autre équipe remporte un match en fonction de leurs cotes actuelles. Les ratings FIFA de deux Coupes du Monde précédentes sont disponibles sous la forme des [FIFA Ratings pour hommes de mai 2018](https://www.fifa.com/fifa-world-ranking/ranking-table/men/rank/id12189/) et des [FIFA Ratings pour femmes de mars 2019](https://www.fifa.com/fifa-world-ranking/ranking-table/women/rank/ranking_20190329/).

En utilisant ces informations, nous pouvons simuler l'ensemble du tournoi en simulant à plusieurs reprises des tours jusqu'à ce qu'il ne reste qu'une seule équipe. Et si nous voulons estimer la probabilité qu'une équipe donnée remporte le tournoi, nous pourrions simuler le tournoi plusieurs fois (par exemple, 1000 simulations) et compter combien de fois chaque équipe remporte un tournoi simulé. 1000 simulations peuvent sembler nombreuses, mais avec la puissance de calcul d'aujourd'hui, nous pouvons effectuer ces simulations en quelques millisecondes. À la fin de ce laboratoire, nous expérimenterons la valeur d'augmenter le nombre de simulations que nous effectuons, étant donné le compromis du temps d'exécution.

Votre tâche dans ce laboratoire est de faire exactement cela en utilisant Python !