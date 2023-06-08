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

Commencer
---------

Ouvrez [VS Code](https://code.cs50.io/).

Commencez en cliquant à l'intérieur de la fenêtre de votre terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à ce qui suit.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/labs/6/world-cup.zip
    

suivi par la touche Entrée pour télécharger un ZIP appelé `world-cup.zip` dans votre espace de code. Attention à ne pas négliger l'espace entre `wget` et l'URL suivante, ou tout autre caractère qui pourrait poser problème!

Maintenant, exécutez

    unzip world-cup.zip
    

pour créer un dossier appelé `world-cup`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm world-cup.zip
    

et répondre "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, saisissez

    cd world-cup
    

suivi de Entrée pour vous déplacer dans (c'est-à-dire, ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    world-cup/ $
    

Si tout a réussi, vous devriez exécuter

    ls
    

et vous devriez voir les fichiers suivants:

    answers.txt  2018m.csv  2019w.csv  tournament.py
    

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur !

Compréhension
-------------

Commencez par jeter un coup d'œil au fichier `2018m.csv`. Ce fichier contient les 16 équipes des huitièmes de finale de la Coupe du monde 2018 et les notes pour chaque équipe. Notez que le fichier CSV a deux colonnes, une appelée `team` (représentant le nom du pays de l'équipe) et une appelée `rating` (représentant la note de l'équipe).

L'ordre dans lequel les équipes sont répertoriées détermine quelles équipes joueront l'une contre l'autre à chaque tour (au premier tour, par exemple, l'Uruguay jouera contre le Portugal et la France jouera contre l'Argentine ; au tour suivant, le vainqueur du match Uruguay-Portugal jouera contre le vainqueur du match France-Argentine). Veillez donc à ne pas modifier l'ordre d'apparition des équipes dans ce fichier !

Finalement, en Python, nous pouvons représenter chaque équipe en tant que dictionnaire contenant deux valeurs: le nom de l'équipe et la note. Uruguay, par exemple, nous voudrions le représenter en Python comme `{"team": "Uruguay", "rating": 976}`.

Ensuite, jetez un coup d'œil à `2019w.csv`, qui contient des données formatées de la même manière pour la Coupe du monde féminine de 2019.

Maintenant, ouvrez `tournament.py` et vous verrez que nous avons déjà écrit du code pour vous. La variable `N` en haut représente le nombre de simulations de la Coupe du monde à exécuter : dans ce cas, 1000.

La fonction `simulate_game` accepte deux équipes en entrée (rappelons que chaque équipe est un dictionnaire contenant le nom de l'équipe et la note de l'équipe) et simule un match entre elles. Si la première équipe gagne, la fonction renvoie `True`; sinon, la fonction renvoie `False`.

La fonction `simulate_round` accepte une liste d'équipes (dans une variable appelée `teams`) en entrée et simule des matchs entre chaque paire d'équipes. La fonction renvoie ensuite une liste de toutes les équipes qui ont remporté la manche.

Dans la fonction `main`, notez d'abord que nous nous assurons que `len(sys.argv)` (nombre d'arguments de ligne de commande) est de 2. Nous utiliserons les arguments de ligne de commande pour indiquer à Python quel fichier CSV d'équipe utiliser pour exécuter la simulation de la Coupe du monde. Nous avons ensuite défini une liste appelée `teams` (qui sera éventuellement une liste d'équipes) et un dictionnaire appelé `counts` (qui associera les noms d'équipes au nombre de fois que cette équipe a gagné une Coupe du monde simulée). Pour l'instant, ils sont tous deux vides, alors la mise en place est laissée à votre charge !

Enfin, à la fin de `main`, nous trions les équipes dans un ordre descendant en fonction du nombre de fois qu'elles ont remporté des simulations (selon `counts`) et imprimons la probabilité estimée que chaque équipe remporte la Coupe du monde.

La mise en place de `teams` et `counts` et de l'écriture de la fonction `simulate_tournament` vous appartient !

Détails de l'implémentation
----------------------

Complétez l'implémentation de `tournament.py` de manière à simuler un certain nombre de tournois et à afficher la probabilité de victoire de chaque équipe.

Tout d'abord, dans `main`, lisez les données de l'équipe à partir du fichier CSV dans la mémoire de votre programme et ajoutez chaque équipe à la liste `teams`.

*  Le fichier à utiliser sera fourni en tant qu'argument de ligne de commande. Vous pouvez accéder au nom du fichier avec `sys.argv[1]`.
*  Rappelez-vous que vous pouvez ouvrir un fichier avec `open(filename)`, où `filename` est une variable contenant le nom du fichier.
*  Une fois que vous avez un fichier `f`, vous pouvez utiliser `csv.DictReader(f)` pour vous donner un "lecteur": un objet en Python que vous pouvez parcourir pour lire le fichier une ligne à la fois, en traitant chaque ligne comme un dictionnaire.
*  Par défaut, toutes les valeurs lues à partir du fichier seront des chaînes de caractères. Assurez-vous donc d'abord de convertir la note de l'équipe en un entier (`int` function en Python peut être utilisée pour cela).
*  En définitive, ajoutez le dictionnaire de chaque équipe à `teams`. L'appel de fonction `teams.append(x)` ajoutera `x` à la liste `teams`.
*  Rappelez-vous que chaque équipe doit être un dictionnaire avec un nom d'équipe et une note.

Ensuite, implémentez la fonction `simulate_tournament`. Cette fonction devrait accepter en entrée une liste d'équipes et devrait simuler des rounds de manière répétée jusqu'à ce qu'il ne reste plus qu'une seule équipe. La fonction devrait ensuite renvoyer le nom de cette équipe.

*  Vous pouvez appeler la fonction `simulate_round`, qui simule un seul tour, en acceptant une liste d'équipes en entrée et en renvoyant une liste de tous les gagnants.
*  Rappelez-vous que si `x` est une liste, vous pouvez utiliser `len(x)` pour déterminer la longueur de la liste.
*  Vous ne devez pas supposer le nombre d'équipes dans le tournoi, mais vous pouvez supposer qu'il sera une puissance de 2.

Enfin, de retour dans la fonction `main`, exécutez `N` simulations de tournoi et suivez le nombre de victoires de chaque équipe dans le dictionnaire `counts`.

*  Par exemple, si l'Uruguay a remporté 2 tournois et le Portugal en a remporté 3, votre dictionnaire `counts` devrait être `{"Uruguay": 2, "Portugal": 3}`.
*  Vous devriez utiliser votre fonction `simulate_tournament` pour simuler chaque tournoi et déterminer le vainqueur.
*  Rappelez-vous que si `counts` est un dictionnaire, la syntaxe `counts[nom_de_l_equipe] = x` associera la clé stockée dans `nom_de_l_equipe` avec la valeur stockée dans `x`.
*  Vous pouvez utiliser le mot clé `in` en Python pour vérifier si un dictionnaire a déjà une clé particulière. Par exemple, `if "Portugal" in counts:` vérifiera si `"Portugal"` a déjà une valeur existante dans le dictionnaire `counts`.

### Guide

<div class="alert" data-alert="primary" role="alert"><p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse paraître différente de celle de votre espace de travail, le comportement des deux environnements devrait être globalement similaire !</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/o5Bkc7gtRjo"></iframe>


### Astuces

*   Lors de la lecture du fichier, vous pouvez trouver cette syntaxe utile, en utilisant `filename` comme nom de votre fichier et `file` comme variable. <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">with</span> <span class="nf">open</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="k">as</span> <span class="nb">file</span><span class="p">:</span>
      <span class="n">    reader</span> <span class="o">=</span> <span class="n">csv</span><span class="p">.</span><span class="nc">DictReader</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span>
</code></pre></div>    </div>
        
    
*   En Python, pour ajouter à la fin d'une liste, utilisez la fonction `.append()`.

    
<details><summary>Vous n'êtes pas sûr de la solution ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/Fo7Roe8hw3A"></iframe></details>


### Tests

Votre programme doit fonctionner comme les exemples ci-dessous. Étant donné que les simulations comportent une part de hasard pour chacune d'entre elles, votre sortie ne correspondra probablement pas parfaitement aux exemples ci-dessous.

    $ python tournament.py 2018m.csv
    Belgique: 20,9 % de chances de gagner
    Brésil: 20,3 % de chances de gagner
    Portugal: 14,5 % de chances de gagner
    Espagne: 13,6 % de chances de gagner
    Suisse: 10,5 % de chances de gagner
    Argentine: 6,5 % de chances de gagner
    Angleterre: 3,7 % de chances de gagner
    France: 3,3 % de chances de gagner
    Danemark: 2,2 % de chances de gagner
    Croatie: 2,0 % de chances de gagner
    Colombie: 1,8 % de chances de gagner
    Suède: 0,5 % de chances de gagner
    Uruguay: 0,1 % de chances de gagner
    Mexique: 0,1 % de chances de gagner
    

    $ python tournament.py 2019w.csv
    Allemagne: 17,1 % de chances de gagner
    États-Unis: 14,8 % de chances de gagner
    Angleterre: 14,0 % de chances de gagner
    France: 9,2 % de chances de gagner
    Canada: 8,5 % de chances de gagner
    Japon: 7,1 % de chances de gagner
    Australie: 6,8 % de chances de gagner
    Pays-Bas: 5,4 % de chances de gagner
    Suède: 3,9 % de chances de gagner
    Italie: 3,0 % de chances de gagner
    Norvège: 2,9 % de chances de gagner
    Brésil: 2,9 % de chances de gagner
    Espagne: 2,2 % de chances de gagner
    Chine PR: 2,1 % de chances de gagner
    Nigeria: 0,1 % de chances de gagner
    

*   Vous vous demandez peut-être ce qui s'est réellement passé lors des Coupes du monde 2018 et 2019 ! Pour les hommes, la France a remporté la victoire en battant la Croatie en finale. La Belgique a vaincu l'Angleterre pour la troisième place. Pour les femmes, les États-Unis ont remporté la victoire en battant les Pays-Bas en finale. L'Angleterre a vaincu la Suède pour la troisième place.

Nombre de simulations
---------------------

Une fois que vous êtes sûr que votre code est correct, ajustez la valeur de `N`, la constante en haut de notre fichier, pour ajuster le nombre de fois que nous simulons le tournoi. Plus nous simulons de tournois, plus nous avons de prévisions précises (pourquoi ?), mais cela prend plus de temps.

Nous pouvons chronométrer des programmes en préfixant leur exécution avec `time` en ligne de commande. Par exemple, avec `N` défini à 1000 (la valeur par défaut), exécutez

    time python tournament.py 2018m.csv
    

ou

    time python tournament.py 2019w.csv
    

qui devrait produire quelque chose comme

    réel    0m0.037s
    utilisateur    0m0.028s
    système     0m0.008s
    

bien que vos propres temps puissent varier.

Faites attention à la mesure **réelle**, qui est le temps total qu'a pris `tournament.py` pour s'exécuter. Et remarquez que vous obtenez le temps en minutes et secondes, avec une précision au millième de seconde.

Dans `answers.txt`, notez le temps qu'il a fallu à `tournament.py` pour simuler...

*   10 (dix) tournois
*   100 (cent) tournois
*   1000 (mille) tournois
*   10 000 (dix mille) tournois
*   100 000 (cent mille) tournois
*   1 000 000 (un million) de tournois

À chaque fois que vous ajustez `N`, enregistrez le temps **réel** dans l'endroit approprié de `answers.txt` en utilisant le même format `0m0.000s`. Après avoir chronométré chaque scénario, répondez aux deux questions de suivi en écrivant sur la même TODO donnée :

*   Quelles prévisions, le cas échéant, se sont avérées incorrectes à mesure que vous augmentiez le nombre de simulations ?
*   Supposez que vous payez des frais pour chaque seconde d'utilisation de calcul par votre programme. Après combien de simulations considéreriez-vous les prévisions comme "suffisamment bonnes" ?

<details><summary>Consultez un fichier <code>answers.txt</code> correctement formaté</summary><div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Temps :

10 simulations : 0m0.028s
100 simulations : 0m0.030s
1000 simulations : 0m0.041s
10 000 simulations : 0m0.139s
100 000 simulations : 0m1.031s
1 000 000 simulations : 0m11.961s

Questions :

Quelles prévisions, le cas échéant, se sont avérées incorrectes à mesure que vous augmentiez le nombre de simulations ? :

Avec un petit nombre de simulations...

Supposez que vous payez des frais pour chaque seconde d'utilisation de calcul par votre programme. Après combien de simulations considéreriez-vous les prévisions comme "suffisamment bonnes" ? :

Il semble que les prévisions se soient stabilisées après environ...

</code></pre></div></div></details>

Comment tester votre code
---------------------

Exécutez ce qui suit pour évaluer la précision de votre code en utilisant `check50`. Mais assurez-vous également de le compiler et de le tester vous-même !

    check50 cs50/labs/2023/x/worldcup
    

Exécutez ce qui suit pour évaluer le style de votre code en utilisant `style50`.

    style50 tournament.py
    

Comment soumettre
-------------

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/labs/2023/x/worldcup"

