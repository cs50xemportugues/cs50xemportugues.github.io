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