Mario
=====

![screenshot of Mario jumping up pyramid](https://cs50.harvard.edu/x/2023/psets/6/mario/less/pyramid.png)

Implémentez un programme qui imprime une demi-pyramide d'une hauteur spécifiée, selon ce qui suit.

    $ python mario.py
    Height: 4
       #
      ##
     ###
    ####
    

Pour commencer
---------------

Connectez-vous à [code.cs50.io] (https://code.cs50.io/), cliquez sur votre terminal, et exécutez cd tout seul. Votre invite de terminal devrait ressembler à ce qui suit :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-mario-less.zip
    

pour télécharger un fichier ZIP appelé "sentimental-mario-less.zip" dans votre espace de travail.

Ensuite, exécutez

    unzip sentimental-mario-less.zip
    

afin de créer un dossier appelé "sentimental-mario-less". Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm sentimental-mario-less.zip
    

et répondez par "y" suivi de Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd sentimental-mario-less
    

suivi de Entrée pour vous déplacer dans ce répertoire (c'est-à-dire l'ouvrir). Votre invite devrait maintenant ressembler à ce qui suit.

    sentimental-mario-less/ $
    

Exécutez `ls` tout seul, et vous devriez voir un fichier `mario.py`. Si vous rencontrez des problèmes, suivez ces mêmes étapes à nouveau et voyez si vous pouvez déterminer où vous avez fait une erreur !

Spécification
-------------

*   Dans un fichier appelé `mario.py`, écrivez un programme qui recrée la demi-pyramide à l'aide de dièses (` # `) pour les blocs, exactement comme vous l'avez fait dans [Problem Set 1] (../../../1/), sauf que cette fois votre programme doit être écrit en Python.
*   Pour rendre les choses plus intéressantes, invitez d'abord l'utilisateur avec `get_int` pour la hauteur de la demi-pyramide, un nombre entier positif compris entre `1` et `8`, inclusivement.
*   Si l'utilisateur ne fournit pas un entier positif supérieur à 8, vous devez reprompter pour la même chose.
*   Ensuite, générez avec l'aide de `print` et d'une ou plusieurs boucles, la demi-pyramide désirée.
*   Veillez à aligner l'angle inférieur gauche de votre demi-pyramide avec le bord gauche de votre fenêtre de terminal.

Utilisation
-----

Votre programme doit se comporter comme l'exemple ci-dessous.

    $ python mario.py
    Height: 4
       #
      ##
     ###
    ####
    

Tester
-------

Bien que `check50` est disponible pour ce problème, il est recommandé de d'abord tester votre code pour chaque élément suivant.

*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Tapez `-1` et appuyez sur entrée. Votre programme doit rejeter cette entrée comme invalide, en réinvite l'utilisateur à taper un autre nombre.
*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Tapez 0 et appuyez sur entrée. Votre programme doit rejeter cette entrée comme invalide, comme en repromptant l'utilisateur pour taper un autre nombre.
*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Tapez `1` et appuyez sur entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée avec l'angle inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
#
</pre>  

*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Tapez `2` et appuyez sur entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée avec l'angle inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
 #
##
</pre> 

*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Tapez `8` et appuyez sur entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée avec l'angle inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
</pre>

*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Tapez `9` et appuyez sur entrée. Votre programme doit rejeter cette entrée comme invalide, comme en repromptant l'utilisateur pour taper un autre nombre. Tapez ensuite `2` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée avec l'angle inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

<pre>
 #
##
</pre> 

*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Tapez `foo` et appuyez sur entrée. Votre programme doit rejeter cette entrée comme invalide, comme en repromptant l'utilisateur pour taper un autre nombre.
*   Exécutez votre programme comme `python mario.py` et attendez une invite pour une entrée. Ne tapez rien et appuyez sur entrée. Votre programme doit rejeter cette entrée comme invalide, comme en repromptant l'utilisateur pour taper un autre nombre.

Exécutez la commande ci-dessous pour évaluer la justesse du code à l'aide de check50. Mais assurez-vous de le compiler et de le tester vous-même aussi !

    check50 cs50/problems/2023/x/sentimental/mario/less
    

Exécutez la commande ci-dessous pour évaluer le style de votre code à l'aide de style50.

    style50 mario.py
    

Comment soumettre
-------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/sentimental/mario/less"