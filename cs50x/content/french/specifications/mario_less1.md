# Mario

## Commencer

Ouvrez [VS Code](https://code.cs50.io/).

Commencez en cliquant à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez la commande:

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-less.zip

suivie de la touche Entrée pour télécharger un fichier ZIP appelé `mario-less.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL qui suit, ou tout autre caractère !

Maintenant, exécutez

    unzip mario-less.zip

pour créer un dossier appelé `mario-less`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter la commande

    rm mario-less.zip

puis répondez par "y" suivi de la touche Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Ensuite, tapez la commande:

    cd mario-less

suivie de la touche Entrée pour vous déplacer (c'est-à-dire ouvrir) dans ce répertoire. Votre invite doit maintenant ressembler à celle ci-dessous.

    mario-less/ $

Si tout s'est bien passé, vous devriez exécuter la commande

    ls

et voir un fichier appelé `mario.c`. L'exécution de `code mario.c` devrait ouvrir le fichier où vous taperez votre code pour ce problème. Si ce n'est pas le cas, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Monde 1-1

Vers la fin du monde 1-1 dans le jeu Super Mario Bros de Nintendo, Mario doit monter une pyramide de blocs alignée à droite, comme ci-dessous.

![capture d'écran de Mario sautant sur une pyramide alignée à droite](https://cs50.harvard.edu/x/2023/psets/1/mario/less/pyramid.png)

Reproduisons cette pyramide en C, bien que sous forme de texte, en utilisant des hashtags (`#`) pour les briques, comme ci-dessous. Chaque hashtag est un peu plus haut que large, donc la pyramide elle-même sera également plus haute que large.

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Le programme que nous écrirons s'appellera `mario`. Et permettons à l'utilisateur de décider de la hauteur de la pyramide en lui demandant d'abord un entier positif compris entre, disons, 1 et 8, inclus.

Voici comment le programme pourrait fonctionner si l'utilisateur saisit `8` lorsqu'il est invité :

    $ ./mario
    Hauteur : 8
           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Voici comment le programme pourrait fonctionner si l'utilisateur saisit `4` lorsqu'il est invité :

    $ ./mario
    Hauteur : 4
       #
      ##
     ###
    ####

Voici comment le programme pourrait fonctionner si l'utilisateur saisit `2` lorsqu'il est invité :

    $ ./mario
    Hauteur : 2
     #
    ##

Et voici comment le programme pourrait fonctionner si l'utilisateur saisit `1` lorsqu'il est invité :

    $ ./mario
    Hauteur : 1
    #

Si l'utilisateur ne saisit pas effectivement un entier positif compris entre 1 et 8, inclus, lorsqu'il est invité, le programme doit l'inviter à nouveau jusqu'à ce qu'il coopère :

    $ ./mario
    Hauteur : -1
    Hauteur : 0
    Hauteur : 42
    Hauteur : 50
    Hauteur : 4
       #
      ##
     ###
    ####

Comment commencer ? Approchons ce problème une étape à la fois.

## Tutoriel

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>