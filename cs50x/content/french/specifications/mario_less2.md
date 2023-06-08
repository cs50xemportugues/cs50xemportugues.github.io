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