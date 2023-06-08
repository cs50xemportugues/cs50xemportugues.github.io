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