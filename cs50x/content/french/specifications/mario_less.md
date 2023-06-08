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

## Pseudocode

Tout d'abord, exécutez 

    cd 

pour vous assurer que vous êtes dans le répertoire par défaut de votre espace de codes. 

Ensuite, exécutez

    cd mario-less 

pour changer de répertoire vers votre répertoire `mario-less`.

Ensuite, exécutez

    code pseudocode.txt 

pour ouvrir le fichier appelé `pseudocode.txt` dans ce répertoire.

Écrivez dans `pseudocode.txt` du pseudocode qui implémente ce programme, même si vous ne savez pas encore comment l'écrire en code. Il n'y a pas une seule façon de rédiger du pseudocode, mais des courtes phrases en anglais suffisent. Rappelez-vous comment nous avons écrit du pseudocode pour trouver quelqu'un dans un annuaire téléphonique. Il est probable que votre pseudocode utilisera (ou impliquera l'utilisation!) de une ou plusieurs fonctions, conditions, expressions booléennes, boucles et/ou variables.

<details><summary>Solution</summary><p>Il y a plus d'une façon de le faire, voici juste une manière!</p>

<ol>
  <li>Demander à l'utilisateur la hauteur</li>
  <li>Si la hauteur est inférieure à 1 ou supérieure à 8 (ou pas un entier du tout), retourner à l'étape précédente</li>
  <li>Parcourir de 1 à hauteur: 
    <ol>
      <li>Pour l'itération<i>i</i>, imprimez <i>i</i> hashtags et ensuite un retour à la ligne</li>
    </ol>
  </li>
</ol>

<p>C'est correct de modifier le votre après avoir consulté ce pseudocode, mais ne faites pas simplement un copier/coller du nôtre!</p></details>

## Demande d'entrée utilisateur

Peu importe votre pseudocode, commençons par écrire uniquement le code en C qui invite (et réinvite, si nécessaire) l'utilisateur à saisir des données. Ouvrez le fichier nommé `mario.c` dans votre répertoire `mario`. (Souvenez-vous comment ?)

Modifiez maintenant `mario.c` de manière à ce qu'il invite l'utilisateur à saisir la hauteur de la pyramide, stockant leur entrée dans une variable et invitant à nouveau l'utilisateur encore et encore si leur entrée n'est pas un entier positif entre 1 et 8, inclusivement. Ensuite, il suffit d'imprimer la valeur de cette variable, en confirmant ainsi (pour vous-même) que vous avez effectivement stocké l'entrée de l'utilisateur avec succès, comme suit.

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
    Stored: 4

<details><summary>Astuces</summary><ul>
  <li data-marker="*">Souvenez-vous que vous pouvez compiler votre programme avec <code class="language-plaintext highlighter-rouge">make</code>.</li>
  <li data-marker="*">Souvenez-vous que vous pouvez imprimer un <code class="language-plaintext highlighter-rouge">int</code> avec <code class="language-plaintext highlighter-rouge">printf</code> en utilisant <code class="language-plaintext highlighter-rouge">%i</code>.</li>
  <li data-marker="*">Souvenez-vous que vous pouvez obtenir un entier de l'utilisateur avec <code class="language-plaintext highlighter-rouge">get_int</code>.</li>
  <li data-marker="*">Souvenez-vous que <code class="language-plaintext highlighter-rouge">get_int</code> est déclaré dans <code class="language-plaintext highlighter-rouge">cs50.h</code>.</li>
  <li data-marker="*">Souvenez-vous que nous avons invité l'utilisateur à saisir un entier positif pendant la leçon en utilisant une boucle <code class="language-plaintext highlighter-rouge">do-while</code> dans <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight"><code class="language-plaintext highlighter-rouge">mario.c</code></a>.</li>
</ul></details>

## Construire l'opposé

Maintenant que votre programme accepte l'entrée prescrite (espérons-le !), il est temps pour une autre étape.

Il s'avère qu'il est un peu plus facile de construire une pyramide alignée à gauche qu'à droite, comme ci-dessous.

    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########

Construisons d'abord une pyramide alignée à gauche, puis, une fois que cela fonctionne, alignons-la à droite !

Modifiez `mario.c` afin qu'il n'imprime plus simplement l'entrée de l'utilisateur, mais plutôt une pyramide alignée à gauche de cette taille.

<details>
  <summary>Indices</summary>
  <ul>
    <li data-marker="*">Rappelez-vous qu'un dièse n'est qu'un caractère comme un autre, vous pouvez donc l'imprimer avec <code class="language-plaintext highlighter-rouge">printf</code>.</li>
    <li data-marker="*">Tout comme Scratch a un bloc de <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">répétition</code></a>, C possède une boucle <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">for</code></a>, via laquelle vous pouvez itérer un certain nombre de fois. Peut-être, à chaque itération, <em>i</em>, pourriez-vous imprimer autant de dièses ?</li>
    <li data-marker="*">
      <p>Vous pouvez en fait "imbriquer" des boucles, itérant avec une variable (par exemple, <code class="language-plaintext highlighter-rouge">i</code>) dans la boucle "externe" et une autre (par exemple, <code class="language-plaintext highlighter-rouge">j</code>) dans la boucle "interne". Par exemple, voici comment vous pourriez imprimer un carré de hauteur et de largeur <code class="language-plaintext highlighter-rouge">n</code>, ci-dessous. Bien sûr, ce n'est pas un carré que vous voulez imprimer !</p>

      <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  for (int i = 0; i &lt; n; i++)

      {
      for (int j = 0; j &lt; n; j++)
      {
      printf("#");
      }
      printf("\n");
      }
      </code></pre></div> </div>

</li>
  </ul>
</details>

## Aligner à droite avec des points

Alignons maintenant cette pyramide à droite en poussant ses dièses vers la droite en les préfixant avec des points (c'est-à-dire des périodes), comme ci-dessous.

    .......#
    ......##
    .....###
    ....####
    ...#####
    ..######
    .#######
    ########

Modifiez `mario.c` de manière à ce qu'il fasse exactement cela !

<details><summary>Indice</summary><p>Remarquez comment le nombre de points nécessaires sur chaque ligne est l' "opposé" du nombre de dièses de cette ligne. Pour une pyramide de hauteur 8, comme celle ci-dessus, la première ligne n'a qu'un dièse et donc 7 points. La ligne du bas, quant à elle, a 8 dièses et donc 0 points. Via quelle formule (ou arithmétique, en réalité) pourriez-vous imprimer autant de points ?</p></details>

### Comment tester votre code

Votre code fonctionne-t-il comme prescrit lorsque vous entrez

- `-1` (ou d'autres nombres négatifs) ?
- `0` ?
- de `1` à `8` ?
- `9` ou d'autres nombres positifs ?
- des lettres ou des mots ?
- aucune entrée du tout, lorsque vous appuyez seulement sur Entrée ?

## Suppression des points

Il ne reste maintenant plus qu'une touche finale ! Modifiez `mario.c` de manière à imprimer des espaces à la place de ces points !

### Comment tester votre code

Exécutez ce qui suit pour évaluer la correction de votre code en utilisant `check50`. Assurez-vous cependant de le compiler et de le tester vous-même également !

    check50 cs50/problems/2023/x/mario/less

Exécutez le suivant pour évaluer le style de votre code à l'aide de `style50`.

     style50 mario.c 

<details><summary>Indice</summary><p>Un espace est juste une pression de votre barre d'espace, tout comme un point est juste une pression de sa touche ! Souvenez-vous simplement que <code class="language-plaintext highlighter-rouge">printf</code> nécessite que vous entouriez les deux avec des guillemets doubles !</p></details>

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2023/x/mario/less

