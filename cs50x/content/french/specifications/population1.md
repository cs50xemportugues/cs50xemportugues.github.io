# Lab 1 : Croissance de la population

<div class="alert" data-alert="warning" role="alert"><p>Vous pouvez collaborer avec un ou deux camarades pour ce laboratoire, mais il est attendu que chaque étudiant dans un tel groupe contribue également au laboratoire.</p></div>

Déterminez le temps nécessaire pour qu'une population atteigne une taille particulière.

    $ ./population
    Taille de départ : 100
    Taille finale : 200
    Années : 9

## Contexte

Supposons que nous ayons une population de `n` lamas. Chaque année, `n / 3` nouveaux lamas naissent et `n / 4` lamas décèdent.

Par exemple, si nous commençons avec `n = 1200` lamas, alors la première année, `1200 / 3 = 400` nouveaux lamas naîtront et `1200 / 4 = 300` lamas mourront. À la fin de cette année, nous aurons `1200 + 400 - 300 = 1300` lamas.

Pour prendre un autre exemple, si nous commençons avec `n = 1000` lamas, à la fin de l'année, nous aurons `1000 / 3 = 333,33` nouveaux lamas. Nous ne pouvons pas avoir une partie décimale d'un lama, nous tronquerons donc la décimale pour avoir `333` nouveaux lamas. `1000 / 4 = 250` lamas mourront, donc nous aurons au total `1000 + 333 - 250 = 1083` lamas à la fin de l'année.

## Pour commencer

Rappelez-vous que Visual Studio Code (alias VS Code) est un « environnement de développement intégré » (IDE) populaire via lequel vous pouvez écrire du code. Afin que vous n'ayez pas à télécharger, installer et configurer votre propre copie de VS Code, nous utiliserons plutôt une version basée sur le cloud qui a tout ce dont vous aurez besoin pré-installé.

1. Connectez-vous à [code.cs50.io](https://code.cs50.io/) en utilisant votre compte GitHub et suivez les instructions à l'écran pour configurer votre propre « espace de code » pour Visual Studio Code. Une fois votre espace de code chargé, vous devriez voir que, par défaut, VS Code est divisé en trois régions. Vers le haut de VS Code se trouve votre « éditeur de texte », où vous écrirez tous vos programmes. Vers le bas se trouve une « fenêtre de terminal », une interface de ligne de commande (CLI) qui permet d'explorer les fichiers et répertoires (alias dossiers) de votre espace de code, de compiler du code et d'exécuter des programmes. Et à gauche se trouve votre « explorateur de fichiers », une interface utilisateur graphique (GUI) via laquelle vous pouvez également explorer les fichiers et répertoires de votre espace de code.
2. Une fois votre espace de code chargé, fermez tous les onglets **Welcome** qui pourraient s'ouvrir par défaut
3. Connectez-vous à [submit.cs50.io](https://submit.cs50.io) en utilisant votre compte GitHub et cliquez sur **Authorize cs50** pour activer `check50`.
4. Exécutez `update50` dans votre fenêtre de terminal pour vous assurer que votre espace de code est à jour et, si cela est demandé, cliquez sur **Rebuild now**.

Une fois terminé, commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez constater que son « invite » ressemble à ce qui suit.

    $

Cliquez à l'intérieur de cette fenêtre de terminal, puis tapez

    mkdir population

suivi de Entrée pour créer un répertoire appelé `population` dans votre espace de code. Veillez à ne pas oublier l'espace entre `mkdir` et `population` ou tout autre caractère, également !

Désormais, exécuter (c'est-à-dire, exécuter) une commande signifie la taper dans une fenêtre de terminal et appuyer sur Entrée. Les commandes sont sensibles à la casse, donc assurez-vous de ne pas taper en majuscules lorsque vous voulez écrire en minuscules, ou vice versa.

Exécutez maintenant

    cd population

pour vous déplacer (à savoir, ouvrir) dans ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    population/ $

Cliquez à l'intérieur de cette fenêtre de terminal, puis tapez

    wget https://cdn.cs50.net/2022/fall/labs/1/population.c

suivi de Entrée pour télécharger un fichier modèle appelé `population.c` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère ! Si tout s'est bien passé, vous devez exécuter

    ls

et voir un fichier nommé `population.c`. L'exécution de `code population.c` doit ouvrir le fichier où vous saisirez votre code pour ce laboratoire. Sinon, retracez vos pas et voyez si vous pouvez déterminer où vous avez mal fait !

## Détails de l'implémentation

Complétez la mise en œuvre de `population.c`, de manière à ce qu'elle calcule le nombre d'années nécessaires à la croissance de la population depuis la taille de départ jusqu'à la taille finale.

- Votre programme doit d'abord demander à l'utilisateur une taille de population de départ.
  - Si l'utilisateur entre un nombre inférieur à 9 (la taille minimale autorisée de la population), l'utilisateur doit être invité à entrer une taille de population de départ jusqu'à ce qu'il entre un nombre qui est supérieur ou égal à 9. (Si nous commençons avec moins de 9 lamas, la population de lamas deviendra rapidement stagnant !)
- Votre programme doit ensuite demander à l'utilisateur une taille de population finale.
  - Si l'utilisateur entre un nombre inférieur à la taille de population de départ, l'utilisateur doit être invité à entrer une taille de population finale jusqu'à ce qu'il entre un nombre qui est supérieur ou égal à la taille de population de départ. (Après tout, nous voulons que la population de lamas se développe !)
- Votre programme doit ensuite calculer le nombre d'années nécessaires à la population pour atteindre au moins la taille de la valeur finale (entier).
- Enfin, votre programme doit imprimer le nombre d'années nécessaires à la population de lamas pour atteindre cette taille finale, en imprimant sur le terminal `Years: n`, où `n` est le nombre d'années.

### Guide

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/dZmtRHHUB1M"></iframe>