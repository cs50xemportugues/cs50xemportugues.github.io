Mario
=====

![capture d'écran de Mario sautant sur une pyramide](https://cs50.harvard.edu/x/2023/psets/6/mario/more/pyramids.png)

Mettre en place un programme qui affiche une double pyramide de hauteur spécifiée, comme ci-dessous.

    $ python mario.py
    Hauteur : 4
       #  #
      ##  ##
     ###  ###
    ####  ####
    

Pour commencer
--------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Votre invite de terminal ressemblera à ce qui suit :

    $
    

Exécutez ensuite

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-mario-more.zip
    

afin de télécharger un fichier ZIP appelé `sentimental-mario-more.zip` dans votre espace de code.

Ensuite, exécutez

    unzip sentimental-mario-more.zip
    

pour créer un dossier appelé `sentimental-mario-more`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm sentimental-mario-more.zip
    

et répondez "y", puis appuyez sur Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd sentimental-mario-more
    

suivi de Entrée pour vous déplacer dans ce répertoire (i.e., ouvrez ce répertoire). Votre invite devrait maintenant ressembler à ce qui suit.

    sentimental-mario-more/ $
    

Exécutez `ls` tout seul et vous devriez voir `mario.py`. Si vous rencontrez des problèmes, suivez ces mêmes étapes à nouveau et voyez si vous pouvez déterminer où vous avez commis des erreurs!

Spécifications
--------------

*   Écrivez dans le fichier appelé `mario.py` un programme qui recrée ces demi-pyramides en utilisant des `#` pour les blocs, exactement comme vous l'avez fait dans la [Problème Set 1](../../../1/), sauf que cette fois, votre programme doit être écrit en Python.
*   Pour rendre les choses plus intéressantes, demandez d'abord à l'utilisateur avec “get_int” de saisir la hauteur de la demi-pyramide, un entier positif entre `1` et `8`, inclusivement. (La hauteur des demi-pyramides illustrées ci-dessus est de `4`, la largeur de chaque demi-pyramide de `4`, avec une séparation de la taille de `2` les séparant).
*   Si l'utilisateur ne fournit pas un entier positif supérieur à `8`, vous devez le redemander.
*   Ensuite, générez (à l'aide de `print` et d'une ou plusieurs boucles) les demi-pyramides désirées.
*   Faites attention à aligner le coin inférieur gauche de votre pyramide avec le bord gauche de votre fenêtre de terminal et assurez-vous qu'il y a deux espaces entre les deux pyramides et qu'il n'y a pas d'espaces supplémentaires après le dernier ensemble de traits sur chaque ligne.

Usage
-----

Votre programme doit se comporter comme dans l'exemple ci-dessous.

    $ python mario.py
    Taille : 4 
       #  #
      ##  ##
     ###  ###
    ####  ####
    

Tests
-----

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à d'abord tester votre code par vous-même pour chacun des éléments suivants.

*   Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Tapez `-1` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, comme en redemandant à l'utilisateur pour taper un autre nombre.
*   Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Tapez `0` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, comme en redemandant à l'utilisateur pour taper un autre nombre.
*   Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Tapez `1` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée dans le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
#  #
</pre> 

*     Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Type in `2` et press enter. Votre programme devrait générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée dans le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
 #  #
##  ##
</pre>  

*    Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Tapez `8` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée dans le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
</pre>  

*    Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Tapez `9` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, comme en redemandant à l'utilisateur pour taper un autre nombre. Ensuite, tapez `2` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée dans le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
 #  #
##  ##
</pre>

*    Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Tapez `foo` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, comme en redemandant à l'utilisateur pour taper un autre nombre.
*    Exécutez votre programme comme `python mario.py` et attendez une invite pour l'entrée. Ne tapez rien et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, comme en redemandant à l'utilisateur pour taper un autre nombre.

Exécutez la commande ci-dessous pour évaluer la justesse de votre code en utilisant `check50`. Mais assurez-vous de compiler et de tester vous-même votre propre code !

    check50 cs50/problems/2023/x/sentimental/mario/more
    

Exécutez la commande ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 mario.py
    

Comment soumettre
-----------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/sentimental/mario/more"