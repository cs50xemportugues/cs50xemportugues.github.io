# Lab 2: Scrabble

<div class="alert" data-alert="warning" role="alert"><p>Vous pouvez collaborer avec un ou deux camarades sur ce labo, mais il est attendu que chaque étudiant de ce groupe contribue également au labo.</p></div>

Déterminez quel mot du Scrabble vaut le plus.

    $ ./scrabble
    Joueur 1 : COMPUTEUR
    Joueur 2 : science
    Le joueur 1 gagne !

## Introduction

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` tout seul. Vous devriez trouver que son "invite" ressemble à ce qui suit.

    $

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2023/print/fr/labs/2/scrabble.zip

suivi de Entrée pour télécharger un fichier ZIP appelé `scrabble.zip` dans votre espace de code. Assurez-vous de ne pas manquer l'espace entre `wget` et l'URL suivante, ou tout autre caractère en général !

Exécutez maintenant

    unzip scrabble.zip 

pour créer un dossier appelé "scrabble". Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter 

    rm scrabble.zip

et répondre "y" suivi de Entrée à la commande pour supprimer le fichier ZIP que vous venez de télécharger.

Tapez maintenant

    cd scrabble

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    scrabble/ $

Si tout a réussi, vous devriez exécuter 

    ls

et vous devriez voir un fichier appelé `scrabble.c`. Ouvrez ce fichier en exécutant la commande suivante :

    code scrabble.c

Si vous rencontrez des problèmes, suivez ces mêmes étapes à nouveau et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Contexte

Dans le jeu de [Scrabble](https://scrabble.hasbro.com/en-us/rules), les joueurs créent des mots pour marquer des points, et le nombre de points est la somme de la valeur de chaque lettre dans le mot.

<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
      <th>I</th>
      <th>J</th>
      <th>K</th>
      <th>L</th>
      <th>M</th>
      <th>N</th>
      <th>O</th>
      <th>P</th>
      <th>Q</th>
      <th>R</th>
      <th>S</th>
      <th>T</th>
      <th>U</th>
      <th>V</th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>1</td>
      <td>8</td>
      <td>5</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>10</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>8</td>
      <td>4</td>
      <td>10</td>
    </tr>
  </tbody>
</table>

Par exemple, si nous voulions marquer le mot `Code`, nous noterions que dans les règles générales du Scrabble, le `C` vaut `3` points, le `o` vaut `1` point, le `d` vaut `2` points et le `e` vaut `1` point. En ajoutant ces nombres, nous obtenons que `Code` vaut `3+1+2+1 = 7` points.

## Détails d'implémentation

Complétez la mise en œuvre de `scrabble.c`, de sorte à ce qu'elle détermine le gagnant d'un jeu de Scrabble-like court, où deux joueurs saisissent chacun leur mot et où le joueur ayant le score le plus élevé gagne.

- Notez que nous avons stocké les valeurs de points de chaque lettre de l'alphabet dans un tableau d'entiers nommé `POINTS`.
  - Par exemple, `A` ou `a` vaut 1 point (représenté par `POINTS[0]`), `B` ou `b` vaut 3 points (représenté par `POINTS[1]`), etc.
- Remarquez que nous avons créé un prototype pour une fonction auxiliaire appelée `compute_score()` qui prend une chaîne de caractères en entrée et renvoie un nombre entier. Chaque fois que nous voulons attribuer des valeurs de point à un mot particulier, nous pouvons appeler cette fonction. Notez que ce prototype est nécessaire pour que C sache que `compute_score()` existe plus tard dans le programme.
- Dans `main()`, le programme demande aux deux joueurs d'entrer leur mot en utilisant la fonction `get_string()`. Ces valeurs sont stockées dans des variables nommées `mot1` et `mot2`.
- Dans `compute_score()`, votre programme doit calculer, en utilisant le tableau `POINTS`, et renvoyer le score pour l'argument de chaîne. Les caractères qui ne sont pas des lettres doivent avoir une valeur nulle, et les lettres majuscules et minuscules doivent avoir les mêmes valeurs de points.
  - Par exemple, `!` vaut `0` point tandis que `A` et `a` valent tous deux `1` point.
  - Bien que les règles du Scrabble exigent normalement qu'un mot soit dans le dictionnaire, pas besoin de le vérifier dans ce problème !
- Dans `main()`, votre programme doit imprimer, en fonction des scores des joueurs, `Joueur 1 gagne !`, `Joueur 2 gagne !`, ou `Match nul !`.

### Astuces

- Vous pouvez trouver les fonctions `isupper()` et `islower()` utiles. Ces fonctions prennent un caractère comme argument et renvoient un booléen.
- Pour trouver la valeur à l'index "n" d'un tableau appelé "arr", nous pouvons écrire `arr[n]`. Nous pouvons également appliquer cela aux chaînes de caractères, car les chaînes de caractères sont des tableaux de caractères.
- Rappelez-vous que les ordinateurs représentent les caractères en utilisant [ASCII](https://asciitable.com/), un standard qui représente chaque caractère par un nombre.

<details><summary>Pas sûr de savoir comment résoudre?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/USiLkXuXJEg"></iframe></details>

### Comment tester votre code

Votre programme devrait se comporter conformément aux exemples ci-dessous.

```
$ ./scrabble
Joueur 1 : Question ?
Joueur 2 : Question !
Match nul !
```

```
$ ./scrabble
Joueur 1 : Oh,
Joueur 2 : hai!
Le joueur 2 gagne !
```

```
$ ./scrabble
Joueur 1 : COMPUTEUR
Joueur 2 : science
Le joueur 1 gagne !
```

```
$ ./scrabble
Joueur 1 : Scrabble
Joueur 2 : wiNNeR
Le joueur 1 gagne !
```

Exécutez la commande ci-dessous pour évaluer la justesse de votre code en utilisant "check50". Mais assurez-vous de le compiler et de le tester vous-même !

    check50 cs50/labs/2023/x/scrabble

Exécutez la commande ci-dessous pour évaluer le style de votre code en utilisant "style50".

    style50 scrabble.c

## Comment soumettre

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/labs/2023/x/scrabble