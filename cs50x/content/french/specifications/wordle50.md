<style>.wrong { background-color: red } .right { background-color: green; } .close_ { background-color: yellow; }</style>

Wordle50
========

Pour ce problème, vous allez implémenter un programme qui se comporte de manière similaire au célèbre jeu quotidien de mots [Wordle](https://www.nytimes.com/games/wordle/index.html).

<pre><code> $ ./wordle 5
<span class="right">Ceci est WORDLE50</span>
Vous avez 6 tentatives pour deviner le mot de 5 lettres auquel je pense
Entrez un mot de 5 lettres : crash
Essai 1 : <span class="close_">c</span><span class="wrong">ra</span><span class="close_">s</span><span class="wrong">h</span>
Entrez un mot de 5 lettres : scone
Essai 2 : <span class="right">s</span><span class="close_">c</span><span class="wrong">o</span><span class="close_">n</span><span class="right">e</span>
Entrez un mot de 5 lettres : since
Essai 3 : <span class="right">since</span>
Vous avez gagné !
</code></pre>

Pour commencer
--------------

Ouvrez [VS Code](https://code.cs50.io/). 

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à ce qui suit : 

    $

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez 

    wget https://cdn.cs50.net/2022/fall/psets/2/wordle.zip
   
suivi d'Entrée pour télécharger un ZIP appelé `wordle.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère. 

Exécutez maintenant 

    unzip wordle.zip
    
pour créer un dossier appelé `wordle`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter 

    rm wordle.zip
    
et répondre par "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé. 

Tapez maintenant 

    cd wordle
    
suivi de Entrée pour vous déplacer vers (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ceci : 

    wordle/ $
    
Si tout s'est bien passé, vous devez exécuter 

    ls
    
et voir un fichier nommé `wordle.c`, ainsi que `5.txt`, `6.txt`, `7.txt` et `8.txt`. L'exécution de `code wordle.c` devrait ouvrir le fichier dans lequel vous allez taper votre code pour cet ensemble de problèmes. Sinon, retrouvez vos traces et voyez si vous pouvez déterminer où vous avez fait une erreur ! Si vous essayez de compiler le jeu maintenant, il le fera sans erreur, mais lorsque vous essayez de l'exécuter, vous verrez cette erreur :

    Error opening file 0.txt.
    
Cependant, c'est normal, car vous n'avez pas encore implémenté une partie du code dont nous avons besoin pour faire disparaître ce message d'erreur.

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

Spécification
-------------

Concevoir et implémenter un programme, `wordle`, qui finalisera l'implémentation de notre clone Wordle50 du jeu. Vous remarquerez que certaines parties importantes de ce programme ont déjà été écrites pour vous - vous n'êtes pas autorisé à modifier ces parties du programme. Votre travail doit être limité aux sept `TODO`s que nous avons laissés pour vous. Chacune de ces parties résout un problème spécifique, et nous vous recommandons de les aborder dans l'ordre de 1 à 7. Chaque `TODO` numéroté correspond au même élément dans la liste ci-dessous.

1. Dans le premier `TODO`, vous devez vous assurer que le programme accepte un unique argument de ligne de commande. Appelons-le `k` pour la discussion. Si le programme n'a pas été exécuté avec un seul argument de ligne de commande, vous devez imprimer le message d'erreur comme nous le démontrons ci-dessus et retourner `1`, ce qui met fin au programme.
2. Dans le deuxième `TODO`, vous devez vous assurer que `k` est l'une des valeurs acceptables (5, 6, 7 ou 8), et stocker cette valeur dans `wordsize`; nous en aurons besoin plus tard. Si la valeur de `k` n'est pas l'une de ces quatre valeurs exactement, vous devez imprimer le message d'erreur comme nous le démontrons ci-dessus et retourner `1`, ce qui met fin au programme.

Ensuite, le personnel a déjà écrit du code qui va parcourir et ouvrir la liste de mots pour la longueur du mot que l'utilisateur veut deviner et en sélectionner un au hasard parmi les 1000 options disponibles. Ne vous inquiétez pas de comprendre tout ce code, ce n'est pas important pour cet exercice. Nous verrons quelque chose de similaire dans un exercice ultérieur, et cela aura beaucoup plus de sens ! C'est un bon endroit pour s'arrêter et tester que votre code se comporte comme prévu. Il est toujours plus facile de déboguer les programmes si vous le faites de manière méthodique !

3. Dans le troisième `TODO`, vous devez aider à défendre contre les utilisateurs têtus en vous assurant que leur réponse a une longueur correcte. Pour cela, nous allons nous concentrer sur la fonction `get_guess`, que vous devrez implémenter en totalité. Un utilisateur doit être invité (via `get_string`) à taper un mot de `k` lettres (rappelez-vous que cette valeur est passée en paramètre à `get_guess`) et si le mot n'a pas la bonne longueur, l'utilisateur doit être invité à fournir à nouveau une réponse (comme dans [Mario](../../1/mario/less/)), jusqu'à ce qu'il fournisse exactement la valeur que vous attendez de lui. Pour l'instant, le code de distribution ne le fait pas, vous devrez donc corriger cela ! Notez qu'à la différence du vrai Wordle, nous ne vérifions pas si le mot de l'utilisateur est un mot réel, de sorte que le jeu peut être un peu plus facile de ce point de vue. Toutes les réponses de ce jeu doivent être en caractères **minuscules**, et il est acceptable de supposer que l'utilisateur ne sera pas assez têtu pour fournir autre chose que des caractères minuscules lorsqu'il fait deviner un mot. Une fois qu'une devinette légitime a été obtenue, elle peut être `return`ée.

4. Ensuite, pour le quatrième `TODO`, nous devons suivre le "score" de l'utilisateur dans le jeu. Nous le faisons à la fois sur une base par lettre - en attribuant un score de 2 (que nous avons défini avec `#define` comme `EXACT`) à une lettre à la place correcte, 1 (que nous avons défini avec `#define` comme `CLOSE`) à une lettre qui est dans le mot mais pas à la bonne place, ou 0 (que nous avons défini avec `#define` comme `WRONG`) - et sur une base par mot, pour nous aider à détecter quand nous avons potentiellement déclenché la fin du jeu en gagnant. Nous utiliserons les scores individuels de lettre lors de la mise en couleur de l'impression. Pour stocker ces scores, nous avons besoin d'un array, que nous avons appelé `status`. Au début du jeu, sans aucune réponse, il devrait contenir uniquement des 0.

C'est un autre endroit où il est bon de s'arrêter et de tester votre code, en particulier en ce qui concerne l'élément 3 ci-dessus ! Vous remarquerez qu'à ce stade, lorsque vous entrez enfin une devinette légitime (c'est-à-dire une qui a la bonne longueur), votre programme ressemblera probablement à ce qui suit :

    Entrez un mot de 5 lettres : ordinateur
    Entrez un mot de 5 lettres :
    
C'est normal, cependant ! L'implémentation de `print_word` est le numéro 6 de `TODO`, donc nous ne devrions pas nous attendre à ce que le programme traite cette réponse à ce moment-là. Bien sûr, vous pouvez toujours ajouter des appels `printf` supplémentaires (assurez-vous simplement de les supprimer avant de soumettre) dans le cadre de votre stratégie de débogage !

5. Le cinquième `TODO` est certainement le plus grand et le plus difficile. À l'intérieur de la fonction `check_word`, il vous appartient de comparer chacune des lettres de la réponse avec chacune des lettres du choix (qui, rappelons-le, est le "mot secret" de ce jeu), et d'attribuer des scores. Si les lettres correspondent, attribuez 2 points `EXACT` et `break` en sortant de la boucle - il n'est pas nécessaire de continuer à boucler si vous avez déjà déterminé que la lettre est au bon endroit. Techniquement, si cette lettre apparaît deux fois dans le mot, cela pourrait entraîner un bug, mais corriger ce bug complique un peu le problème plus que nous ne le voulons maintenant, nous allons donc l'accepter comme une fonctionnalité de notre version ! Si vous trouvez que la lettre est dans le mot mais pas au bon endroit, attribuez 1 point `CLOSE` mais ne `break`z pas ! Après tout, cette lettre pourrait plus tard apparaître à la bonne place dans le mot de choix, et si nous «break»ons trop tôt, l'utilisateur ne le saura jamais ! Vous n'avez pas réellement besoin de définir explicitement les points `WRONG` (0) ici, car vous les avez traités plus tôt à l'étape 4. En fin de compte, vous devez également sommer le score total du mot lorsque vous le connaissez, car c'est ce que cette fonction doit finalement retourner. Encore une fois, n'hésitez pas à utiliser `debug50` et/ou `printf` au besoin pour vous aider à comprendre les valeurs de différentes variables à ce stade - jusqu'à ce que vous implémentiez `print_word`, ci-dessous, le programme ne vous offrira pas beaucoup de point de référence visuel !

6. Pour le sixième `TODO`, vous allez mener à bien la mise en œuvre de `print_word`. Cette fonction devrait parcourir les valeurs que vous avez stockées dans l'array `status` et imprimer, caractère par caractère, chaque lettre de la réponse avec le code de couleur correct. Vous avez peut-être remarqué certains `#define` (effrayants !) en haut du fichier où nous fournissons une manière plus simple de représenter ce qu'on appelle un [code de couleur ANSI](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors), qui est essentiellement une commande pour changer la couleur de la police du terminal. Vous n'avez pas à vous soucier de la manière de mettre en œuvre ces quatre valeurs (`GREEN`, `YELLOW`, `RED`, et `RESET`, ce dernier permettant simplement de revenir à la police par défaut du terminal) ou exactement ce qu'elles signifient ; vous pouvez simplement les utiliser (le pouvoir de l'abstraction !). Notez également que nous fournissons un exemple dans le code de distribution lorsque nous imprimons un texte vert puis réinitialisons la couleur, dans le cadre de l'introduction du jeu. En conséquence, vous pouvez vous sentir libre d'utiliser la ligne de code ci-dessous pour vous inspirer de la manière dont vous pourriez essayer de basculer les couleurs :

```
printf(GREEN"C'est le WORDLE50"RESET"\n");
```

Bien sûr, contrairement à notre exemple, vous ne voulez probablement pas imprimer un saut de ligne après chaque caractère du mot (au lieu de cela, vous voulez juste un seul saut de ligne à la fin, en réinitialisant également la couleur de la police !), sinon cela risque de ressembler à ce qui suit :

    
<pre><code>
Entrez un mot de 5 lettres : jeux
Essai 1: <span class="wrong">g</span>
<span class="close_">a</span>
<span class="wrong">m</span>
<span class="close_">e</span>
<span class="wrong">s</span>
Entrez un mot de 5 lettres :
</code></pre>
    
7. Enfin, le

Comment tester votre code
-------------------------

Exécutez les commandes ci-dessous pour évaluer la précision de votre code en utilisant `check50`. Assurez-vous toutefois de le compiler et de le tester vous-même !

    check50 cs50/problems/2023/x/wordle
    

Exécutez la commande ci-dessous pour évaluer le style de votre code avec `style50`.

    style50 wordle.c
    

Comment soumettre votre travail
-------------------------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/wordle"

