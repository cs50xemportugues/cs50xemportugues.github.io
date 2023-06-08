# Mario

## Pour commencer

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer dans votre fenêtre de terminal, puis entrez `cd` seul. Vous devriez constater que sa "invite" ressemble à celle-ci.

    $

Cliquez dans cette fenêtre de terminal et exécutez ensuite

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-more.zip

suivi de la touche Entrée pour télécharger un fichier ZIP appelé `mario-more.zip` dans votre espace de code. Faites attention à ne pas négliger l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Maintenant, exécutez

    unzip mario-more.zip

pour créer un dossier appelé `mario-more`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm mario-more.zip

et répondez "y" suivi de la touche Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd mario-more

suivi de la touche Entrée pour vous déplacer dans ce répertoire. Votre invite devrait maintenant ressembler à ceci.

    mario-more/ $

Si tout s'est bien passé, vous devriez exécuter

    ls

et voir un fichier nommé `mario.c`. L'exécution de `code mario.c` devrait ouvrir le fichier dans lequel vous taperez votre code pour ce problème. Sinon, revenez en arrière et voyez où vous avez fait une erreur !

## Monde 1-1

Au début du monde 1-1 de Super Mario Bros de Nintendo, Mario doit sauter par-dessus des pyramides de blocs adjacents, comme ci-dessous.

![capture d'écran de Mario sautant par-dessus des pyramides adjacentes](https://cs50.harvard.edu/x/2023/psets/1/mario/more/pyramids.png)

Recréons ces pyramides en C, mais en texte, en utilisant des dièses (`#`) pour les briques, à la manière de ce qui suit. Chaque dièse est un peu plus haut que large, les pyramides elles-mêmes seront donc plus hautes que larges.

       #  #
      ##  ##
     ###  ###
    ####  ####

Le programme que nous écrirons s'appellera `mario`. Et permettons à l'utilisateur de décider de la hauteur des pyramides en leur demandant d'abord un entier positif compris entre, disons, 1 et 8 inclus.

Voici comment le programme pourrait fonctionner si l'utilisateur entre `8` lorsqu'on lui demande :

    $ ./mario
    Height: 8
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########

Voici comment le programme pourrait fonctionner si l'utilisateur entre `4` lorsqu'on lui demande :

    $ ./mario
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Voici comment le programme pourrait fonctionner si l'utilisateur entre `2` lorsqu'on lui demande :

    $ ./mario
    Height: 2
     #  #
    ##  ##

Et voici comment le programme pourrait fonctionner si l'utilisateur entre `1` lorsqu'on lui demande :

    $ ./mario
    Height: 1
    #  #

Si l'utilisateur n'entre pas effectivement un entier positif compris entre 1 et 8 inclus lorsqu'on lui demande, le programme doit lui redemander jusqu'à ce qu'il coopère :

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Remarquez que la largeur de l'espace "vide" entre les pyramides adjacentes est égale à la largeur de deux dièses, indépendamment de la hauteur des pyramides.

Ouvrez votre fichier `mario.c` pour implémenter ce problème comme décrit !

### Guide

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Comment tester votre code

Votre code fonctionne-t-il comme prescrit lorsque vous entrez

- `-1` (ou d'autres nombres négatifs) ?
- `0`?
- de `1` à `8`?
- `9` ou d'autres nombres positifs?
- des lettres ou des mots ?
- aucune entrée du tout, lorsque vous appuyez simplement sur Entrée ?

Vous pouvez également exécuter le code suivant pour évaluer la justesse de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester vous-même également !

    check50 cs50/problems/2023/x/mario/more

Exécutez le code suivant pour évaluer le style de votre code en utilisant `style50`.

    style50 mario.c

## Comment soumettre

Dans votre terminal, exécutez le code suivant pour soumettre votre travail.

    submit50 cs50/problems/2023/x/mario/more