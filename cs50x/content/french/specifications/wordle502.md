# Contexte 
----------

Il est probable que si vous êtes utilisateur de Facebook, au moins l'un de vos amis a posté quelque chose qui ressemble à cela, particulièrement au début de l'année 2022, quand tout le monde le faisait:


![Résultats Wordle](https://cs50.harvard.edu/x/2023/psets/2/wordle50/wordle.png)


Si tel est le cas, votre ami a joué à Wordle et partage ses résultats pour ce jour-là! Chaque jour, un nouveau "mot secret" est choisi (le même pour tout le monde) et l'objectif est de deviner quel est le mot secret en six essais. Heureusement, étant donné qu'il y a plus de six mots de cinq lettres dans la langue anglaise, vous pouvez obtenir des indices en cours de route, et l'image ci-dessus montre en fait la progression de votre ami dans ses hypothèses, utilisant ces indices pour essayer de se rapprocher du bon mot. En utilisant un schéma similaire au jeu [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)), si après avoir deviné une lettre elle devient verte, cela signifie non seulement que cette lettre est dans le mot secret de la journée, mais qu'elle est également à la bonne place. Si elle devient jaune, cela signifie que la lettre devinée apparaît _quelque part_ dans le mot, mais pas dans cette position précise. Les lettres qui deviennent grises ne sont pas dans le mot du tout et peuvent être omises pour les futures suppositions.

Terminons l'écriture d'un programme appelé `wordle` qui nous permet de recréer ce jeu et de jouer dans notre terminal. Nous apporterons quelques légères modifications au jeu (par exemple, la façon dont il gère une lettre apparaissant deux fois dans un mot n'est pas la même que la façon dont le vrai jeu le gère, mais pour simplifier, nous opterons pour la facilité de compréhension plutôt qu'une interprétation parfaitement fidèle) et nous utiliserons du texte rouge plutôt que gris pour indiquer les lettres qui ne sont pas du tout dans le mot. Au moment où l'utilisateur exécute le programme, il doit décider, en fournissant un argument de ligne de commande, quelle est la longueur du mot qu'il veut deviner, entre 5 et 8 lettres.

Voici quelques exemples de comment le programme devrait fonctionner. Par exemple, si l'utilisateur n'a pas donné la bonne commande:

    $ ./wordle
    Usage: ./wordle wordsize
    
Si l'utilisateur fournit une clé `5` :

     $ ./wordle 5
     C'est WORDLE50
     Vous avez 6 essais pour deviner le mot de 5 lettres que je pense
     Entrez un mot de 5 lettres:
    
À ce stade, l'utilisateur doit entrer un mot de 5 lettres. Bien sûr, l'utilisateur pourrait être têtu, et nous devons nous assurer qu'il respecte les règles: 

<pre><code>$ ./wordle 5
     <span class="right">C'est WORDLE50</span>
     Vous avez 6 essais pour de deviner le mot de 5 lettres que je pense
     Entrez un mot de 5 lettres: wordle
     Entrez un mot de 5 lettres: ordinateur
     Entrez un mot de 5 lettres: d'accord
     Entrez un mot de 5 lettres: jeux
     Essai 1: <span class="wrong">g</span><span class="close_">a</span><span class="wrong">m</span><span class="close_">e</span><span class="wrong">s</span>
     Entrez un mot de 5 lettres:
 </code></pre>


Remarquez que nous ne comptons même pas ces tentatives invalides comme des essais. Mais dès qu'ils ont fait une tentative légitime, nous l'avons comptée comme une tentative et rapportée sur l'état du mot. Il semble que l'utilisateur ait maintenant quelques indices; il sait que le mot contient un `a` et un `e` quelque part, mais pas aux endroits exacts où ils apparaissent dans le mot `jeux`. Et il sait que les lettres `g`, `m` et `s` n'apparaissent pas dans le mot du tout, donc les futures suppositions peuvent les omettre. Peut-être essayeront-ils, par exemple, `coeur` la prochaine fois! ❤️