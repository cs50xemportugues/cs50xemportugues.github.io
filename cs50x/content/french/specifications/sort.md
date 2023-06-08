Laboratoire 3 : Tri
====================


<div class="alert" data-alert="warning" role="alert"><p>Vous pouvez collaborer avec un ou deux camarades de classe pour ce laboratoire, mais il est attendu que chaque élève du groupe contribue également au laboratoire.</p></div>

Analysez trois programmes de tri pour déterminer quels algorithmes ils utilisent.

Contexte
--------

Rappelez-vous du cours magistral où nous avons vu quelques algorithmes pour trier une séquence de nombres : tri par sélection, tri à bulles et tri fusion.

*   Le tri par sélection itère dans les parties non triées d'une liste, sélectionnant à chaque fois le plus petit élément et le déplaçant à sa position correcte.
*   Le tri à bulles compare progressivement les paires de valeurs adjacentes et les échange si elles ne sont pas dans l'ordre correct. Cela continue jusqu'à ce que la liste soit triée.
*   Le tri fusion divise récursivement la liste en deux et fusionne ensuite les plus petites listes dans une plus grande dans le bon ordre.

Pour commencer
--------------

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $
    

Cliquez dans cette fenêtre de terminal, puis exécutez 

    wget https://cdn.cs50.net/2022/fall/labs/3/sort.zip
    

suivi de Enter pour télécharger un fichier ZIP appelé `sort.zip` dans votre espace de code. Assurez-vous de ne pas ignorer l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Ensuite, exécutez

    unzip sort.zip
    

pour créer un dossier appelé `sort`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm sort.zip
    

et répondez par "y" suivi de Enter à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd sort
    

suivi de Enter pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    sort/ $
    

Si tout s'est bien passé, vous devez exécuter

    ls
    

et vous devez voir une collection de fichiers `.txt` aux côtés des programmes exécutables `sort1`, `sort2` et `sort3`.

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur !

Instructions
------------

Trois programmes C déjà compilés vous sont fournis, `sort1`, `sort2` et `sort3`. Chacun de ces programmes implémente un algorithme de tri différent : tri par sélection, tri à bulles ou tri fusion (mais pas nécessairement dans cet ordre !). Votre tâche consiste à déterminer quel algorithme de tri est utilisé par chaque fichier.

*   `sort1`, `sort2` et `sort3` sont des fichiers binaires, vous ne pourrez donc pas voir le code source C de chacun d'entre eux. Pour évaluer quelle trie implémente quel algorithme, exécutez les tris sur différentes listes de valeurs.
*   Plusieurs fichiers `.txt` vous sont fournis. Ces fichiers contiennent `n` lignes de valeurs, inversées, mélangées ou triées.
    *   Par exemple, `reversed10000.txt` contient 10000 lignes de nombres qui sont inversés de `10000`, tandis que `random10000.txt` contient 10000 lignes de nombres qui sont dans un ordre aléatoire.
*   Pour exécuter les tris sur les fichiers texte, dans le terminal, exécutez `./[program_name] [text_file.txt]`. Assurez-vous d'avoir utilisé `cd` pour vous déplacer dans le répertoire `sort` !
    *   Par exemple, pour trier `reversed10000.txt` avec `sort1`, exécutez `./sort1 reversed10000.txt`.
*   Vous pouvez trouver utile de chronométrer vos tris. Pour cela, exécutez `time ./[sort_file] [text_file.txt]`.
    *   Par exemple, vous pourriez exécuter `time ./sort1 reversed10000.txt` pour exécuter `sort1` sur 10 000 nombres inversés. À la fin de la sortie de votre terminal, vous pouvez regarder le temps "réel" pour voir combien de temps s'est écoulé réellement pendant l'exécution du programme.
*   Enregistrez vos réponses dans `answers.txt`, avec une explication pour chaque programme, en remplissant les blancs marqués `TODO`.

### Guide

<div class="alert" data-alert="primary" role="alert"><p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse être différente de celle de votre espace de code, le comportement des deux environnements devrait être largement similaire !</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-Bhxxw6JKKY"></iframe>


### Astuces

*   Les différents types de fichiers `.txt` peuvent vous aider à déterminer lequel est lequel. Considérez comment chaque algorithme se comporte avec une liste déjà triée. Et avec une liste inversée ? Ou mélangée ? Il peut être utile de travailler sur une liste plus petite de chaque type et de passer en revue chaque processus de tri.

<details><summary>Vous ne savez pas comment faire ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/uOYhrBs37j0"></iframe></details>


### Comment vérifier vos réponses

Exécutez ce qui suit pour évaluer la justesse de vos réponses avec `check50`. Mais n'oubliez pas de remplir également vos explications, que `check50` ne vérifiera pas ici !

    check50 cs50/labs/2023/x/sort
    

Comment soumettre
-----------------

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/labs/2023/x/sort