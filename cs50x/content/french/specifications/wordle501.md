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