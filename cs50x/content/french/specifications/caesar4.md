### Comptabiliser les Arguments de la Ligne de Commande

Quel que soit votre pseudocode, commençons par écrire uniquement le code C qui vérifie si le programme a été exécuté avec un seul argument de ligne de commande avant d'ajouter des fonctionnalités supplémentaires.

Modifiez spécifiquement `main` dans `caesar.c` de manière à ce que, si l'utilisateur ne fournit aucune argument de ligne de commande ou deux arguments ou plus, la fonction imprime `"Usage: ./caesar key\n"` et retourne `1`, ce qui quitte effectivement le programme. Si l'utilisateur fournit exactement un argument de ligne de commande, le programme ne doit rien imprimer et simplement retourner `0`. Le programme doit donc se comporter comme suit.

    $ ./caesar
    Usage: ./caesar key


    $ ./caesar 1 2 3
    Usage: ./caesar key


    $ ./caesar 1

<details><summary>Indices</summary><ul>
  <li data-marker="*">Rappelez-vous que vous pouvez imprimer avec <code class =" language-plaintext highlighter-rouge ">printf</code>.</li>
  <li data-marker="*">Rappelez-vous qu'une fonction peut renvoyer une valeur avec <code class =" language-plaintext highlighter-rouge ">return</code>.</li>
  <li data-marker="*">Rappelez-vous que <code class =" language-plaintext highlighter-rouge ">argc</code> contient le nombre d'arguments de ligne de commande passés à un programme, plus le nom du programme lui-même.</li>
</ul></details>

### Vérification de la Clé

Maintenant que votre programme accepte (espérons-le!) une entrée conforme, il est temps pour une autre étape.

Ajoutez à `caesar.c`, en dessous de `main`, une fonction appelée, par exemple, `only_digits` qui prend une `string` en argument et renvoie `true` si cette `string` contient uniquement des chiffres, de `0` à `9`, sinon elle renvoie `false`. Assurez-vous d'ajouter le prototype de fonction au-dessus de `main`.

<details><summary>Indices</summary><ul>
  <li data-marker="*">Il est probable que vous souhaitiez un prototype comme celui-ci :
    <div class =" language-c highlighter-rouge "> <div class ="highlight"> <pre class =" highlight "> <code> <span class ="n">bool</span> <span class ="nf">only_digits</span> <span class ="p">(</span> <span class ="n">string</span> <span class ="n">s</span> <span class ="p">);</span>
</code> </pre> </div> </div>
    <p>Et assurez-vous d'inclure <code class =" language-plaintext highlighter-rouge ">cs50.h</code> en haut de votre fichier, afin que le compilateur reconnaissez <code class =" language-plaintext highlighter-rouge ">string</code> (et <code class =" language-plaintext highlighter-rouge ">bool</code>).</p>
  </li>
  <li data-marker="*">Rappelez-vous qu'une <code class =" language-plaintext highlighter-rouge ">string</code> est simplement un tableau de <code class =" language-plaintext highlighter-rouge ">char</code>s.</li>
  <li data-marker="*">Rappelez-vous que <code class =" language-plaintext highlighter-rouge ">strlen</code>, déclaré dans <code class =" language-plaintext highlighter-rouge ">string.h</code>, calcule la longueur d'une <code class =" language-plaintext highlighter-rouge ">string</code>.</li>
  <li data-marker="*">Vous pouvez trouver <code class =" language-plaintext highlighter-rouge ">isdigit</code>, déclaré dans <code class =" language-plaintext highlighter-rouge ">ctype.h</code>, utile, selon <a href="https://manual.cs50.io/">manual.cs50.io</a>. Mais notez qu'il ne vérifie qu'un seul <code class =" language-plaintext highlighter-rouge ">char</code> à la fois!</li>
</ul></details>


Modifiez ensuite `main` de telle sorte qu'elle appelle `only_digits` sur `argv[1]`. Si cette fonction renvoie `false`, alors `main` devrait imprimer `"Usage: ./caesar key\n"` et retourner `1`. Sinon, `main` doit simplement renvoyer `0`. Le programme doit donc se comporter comme suit :

```
$ ./caesar 42
```

```
$ ./caesar banana
Usage: ./caesar key
```