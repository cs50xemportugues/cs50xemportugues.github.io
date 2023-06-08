# César

Pour ce problème, vous allez implémenter un programme qui chiffre les messages en utilisant le chiffre de César, selon le chiffrement ci-dessous.

    $./caesar 13
    texte en clair : HELLO
    texte chiffré : URYYB

## Pour commencer

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez obtenir une invite qui ressemble à celle ci-dessous.

    $

Cliquez dans la fenêtre de terminal et exécutez

    wget https://cdn.cs50.net/2022/fall/psets/2/caesar.zip

puis appuyez sur Entrée pour télécharger un fichier ZIP appelé `caesar.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Maintenant, exécutez

    unzip caesar.zip

pour créer un dossier appelé `caesar`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm caesar.zip

et répondez "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd caesar

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    caesar/ $

Si tout s'est bien passé, vous devriez exécuter

    ls

et voir un fichier appelé `caesar.c`. Exécuter `code caesar.c` devrait ouvrir le fichier où vous taperez votre code pour ce jeu de problèmes. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Contexte

Apparemment, César (oui, ce César) utilisait pour "crypter" (cacher de manière réversible) des messages confidentiels en décalant chaque lettre de certains nombres de places. Par exemple, il pourrait écrire A comme B, B comme C, C comme D, ..., et de manière circulaire, Z comme A. ainsi, pour dire HELLO à quelqu'un, César pourrait écrire IFMMP à la place. Les destinataires devraient donc "décrypter" ces messages en décalant chaque lettre dans le sens inverse avec le même nombre de places.

L'efficacité de ce "système de cryptage" repose sur le fait que seuls César et les destinataires connaissent un secret, le nombre de places par lesquelles César avait décalé ses lettres (par exemple, 1). Ce système n'est pas particulièrement sûr selon les normes modernes, mais s'il est peut-être le premier au monde à l'utiliser, il est sûr!

Le texte non crypté est généralement appelé _plaintext_. Le texte crypté est généralement appelé _ciphertext_. Et la clé utilisée est appelée _key_.

Pour être clair, voici comment crypter `HELLO` avec une clé de `1` donne `IFMMP`:

<table>
  <thead>
    <tr>
      <th>plaintext</th>
      <th><code class="language-plaintext highlighter-rouge">H</code></th>
      <th><code class="language-plaintext highlighter-rouge">E</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">L</code></th>
      <th><code class="language-plaintext highlighter-rouge">O</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+ key</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>= ciphertext</td>
      <td><code class="language-plaintext highlighter-rouge">I</code></td>
      <td><code class="language-plaintext highlighter-rouge">F</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">M</code></td>
      <td><code class="language-plaintext highlighter-rouge">P</code></td>
    </tr>
  </tbody>
</table>

Plus formellement, l'algorithme (c'est-à-dire le chiffrement) de César crypte les messages en "rotant" chaque lettre de `k` positions. Plus formellement, si `p` est un texte en clair (c'est-à-dire un message non crypté), <code>p<sub>i</sub></code> est le <code>i<sup>ème</sup></code> caractère de `p` et `k` est une clé secrète (c'est-à-dire un entier positif), alors chaque lettre, <code>c<sub>i</sub></code>, dans le texte crypté, `c`, est calculé comme

<code>c<sub>i</sub> = (p<sub>i</sub> + k) % 26</code>

où `% 26` ici signifie «reste de la division par 26». Cette formule peut sembler plus compliquée qu'elle ne l'est, mais elle est en réalité une façon concise d'exprimer l'algorithme de manière précise. En effet, pour les besoins de la discussion, on considère que A (ou a) est `0`, B (ou b) est `1`, ..., H (ou h) est `7`, I (ou i) est `8`, ..., et Z (ou z) est `25`. Supposons que César souhaite dire `Hi` à quelqu'un de manière confidentielle en utilisant, cette fois-ci, une clé, `k`, de 3. Ainsi, son texte non crypté, `p`, est `Hi`, dans lequel le premier caractère du texte non crypté de César, <code>p<sub>0</sub></code>, est `H` (aka 7), et le deuxième caractère du texte non crypté de César, <code>p<sub>1</sub></code>, est `i` (aka 8). Le premier caractère du texte crypté de César, <code>c<sub>0</sub></code>, est donc `K`, et le deuxième caractère du texte crypté de César, <code>c<sub>i</sub></code>, est donc `L`. Cela a du sens ?

Écrivons un programme appelé `caesar` qui vous permet de crypter des messages en utilisant le chiffre de César. Au moment où l'utilisateur exécute le programme, il doit décider, en fournissant un argument en ligne de commande, quelle sera la clé du message secret qu'il fournira lors de l'exécution. On ne devrait pas nécessairement supposer que la clé de l'utilisateur sera un nombre ; bien que l'on puisse supposer que si c'est un nombre, c'est un entier positif.

Voici quelques exemples de fonctionnement du programme. Par exemple, si l'utilisateur entre une clé de `1` et un texte en clair `HELLO` :

    $ ./caesar 1
    plaintext:  HELLO
    ciphertext: IFMMP

Voici comment le programme pourrait fonctionner si l'utilisateur fournit une clé de `13` et un texte en clair `hello, world` :

    $ ./caesar 13
    plaintext:  hello, world
    ciphertext: uryyb, jbeyq

Remarquez que ni la virgule ni l'espace n'ont été "décalés" par le chiffrement. Seuls les caractères alphabétiques ont été décalés !

Comment cela fonctionnerait-il si l'utilisateur fournissait une clé de `13` de plus avec un texte en clair plus complexe :

    $ ./caesar 13
    plaintext:  soyez sûr de boire votre Ovaltine
    ciphertext: be fher gb qevax lbhe Binygvar

<details><summary>Pourquoi ?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9K4FsAHB-C8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

Remarquez que la casse du message original a été préservée. Les caractères minuscules restent minuscules et les caractères majuscules restent majuscules.

Et si un utilisateur ne coopère pas, en fournissant un argument en ligne de commande qui n'est pas un nombre ? Le programme devrait rappeler à l'utilisateur comment utiliser le programme :

    $ ./caesar HELLO
    Usage: ./caesar key

Ou s'il ne coopère pas vraiment, en ne fournissant pas d'argument en ligne de commande du tout ? Le programme devrait rappeler à l'utilisateur comment utiliser le programme :

    $ ./caesar
    Usage: ./caesar key

Ou vraiment, s'il fournit plus d'un argument en ligne de commande? Le programme devrait rappeler à l'utilisateur comment utiliser le programme :

    $ ./caesar 1 2 3
    Usage: ./caesar key

<details><summary>Regarder un enregistrement</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script></details>

## Spécification

Concevez et implémentez un programme, `caesar`, qui chiffre des messages en utilisant le chiffre de César.

- Implémentez votre programme dans un fichier appelé `caesar.c` dans un répertoire appelé `caesar`.
- Votre programme doit accepter un seul argument en ligne de commande, un entier positif. Appelons-le `k` pour la discussion.
- Si votre programme est exécuté sans aucun argument en ligne de commande ou avec plus d'un argument en ligne de commande, votre programme doit afficher un message d'erreur de votre choix (avec `printf`) et retourner de `main` une valeur de `1` (ce qui tend à indiquer une erreur) immédiatement.
- Si l'un des caractères de l'argument en ligne de commande n'est pas un chiffre décimal, votre programme doit afficher le message `Usage: ./caesar key` et retourner de `main` une valeur de `1`.
- Ne supposez pas que `k` sera inférieur ou égal à 26. Votre programme doit fonctionner pour toutes les valeurs intégrales non négatives de `k` inférieures à <code>2<sup>31</sup> - 26</code>. En d'autres termes, vous n'avez pas besoin de vous inquiéter si votre programme finit par se briser si l'utilisateur choisit une valeur pour `k` qui est trop grande ou presque trop grande pour tenir dans un `int`. (Rappelez-vous qu'un `int` peut déborder.) Mais même si `k` est supérieur à `26`, les caractères alphabétiques dans l'entrée de votre programme doivent rester des caractères alphabétiques dans la sortie de votre programme. Par exemple, si `k` est `27`, `A` ne doit pas devenir `\` même si `\` est à `27` positions de `A` dans ASCII, selon [asciitable.com](https://www.asciitable.com/); `A` doit devenir `B`, car `B` est à `27` positions de `A`, à condition de revenir à `Z` à `A`.
- Votre programme doit produire une sortie `plaintext:` (avec deux espaces mais sans saut de ligne) puis demander à l'utilisateur une `chaîne` de texte brut (en utilisant `get_string`).
- Votre programme doit produire une sortie `ciphertext:` (avec un espace mais sans saut de ligne), suivie du texte brut correspondant au texte chiffré, avec chaque caractère alphabétique dans le texte brut "tourné" de _k_ positions; les caractères non alphabétiques doivent être affichés sans changement.
- Votre programme doit conserver la casse: les lettres majuscules, bien que tournées, doivent rester des lettres majuscules; les lettres minuscules, bien que tournées, doivent rester des lettres minuscules.
- Après avoir affiché le texte chiffré, vous devez imprimer un saut de ligne. Votre programme doit ensuite se terminer en retournant la valeur `0` de `main`.

## Conseils

Par où commencer ? Abordons ce problème une étape à la fois.

### Pseudo-code

Tout d'abord, essayez d'écrire une fonction `main` dans `caesar.c` qui implémente le programme en utilisant simplement le pseudo-code, même si vous n'êtes pas (encore!) sûr de savoir comment l'écrire en code réel.

<details><summary>Indice</summary><p>Il y a plus d'une façon de faire cela, voici donc juste l'une d'entre elles !</p>

    int main(void)
    {
        // Vérifiez que le programme a été exécuté avec un seul argument en ligne de commande

        // Vérifiez que chaque caractère de argv[1] est un chiffre

        // Convertit argv[1] d'une `chaîne` à un `entier`.

        // Demande à l'utilisateur un texte brut

        // Pour chaque caractère du texte brut :

            // Tourne le caractère s'il s'agit d'une lettre
    }

<p>Il est possible d'éditer votre propre pseudo-code après avoir vu le nôtre ici, mais ne vous contentez pas simplement de copier/coller le nôtre dans le vôtre !</p></details>

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

### Utilisation de la clé

Modifiez `main` de manière à ce qu'il convertisse `argv[1]` en un `int`. Vous pourriez trouver utile d'utiliser `atoi`, déclaré dans `stdlib.h`, comme indiqué dans [manual.cs50.io](https://manual.cs50.io/). Ensuite, utilisez `get_string` pour demander à l'utilisateur un texte en clair avec `"plaintext : "`.

Ensuite, implémentez une fonction appelée, par exemple, `rotate`, qui prend en entrée un `char` et également un `int`, et fait tourner ce `char` de ce nombre de positions s'il s'agit d'une lettre (c'est-à-dire alphabétique), en bouclant de `Z` à `A` (et de `z` à `a`) si nécessaire. Si le `char` n'est pas une lettre, la fonction doit plutôt renvoyer le même `char` inchangé.

<details><summary>Conseils</summary>
<ul>

  <li data-marker="*">Il est probable que vous vouliez un prototype du type :
  
  ```
  char rotate(char c, int n);
  ```
  
  Un appel de fonction comme :
  
  ```
  rotate('A', 1)
  ``` 
  
  ou même 
  
  ```
  rotate('A', 27)
  ``` 
  renverrait donc `'B'`. Et un appel de fonction comme
  
  ```
  rotate('!', 13)
  ``` 
  
  renverrait `'!'`.</li>
  
  <li data-marker="*">Rappelez-vous que vous pouvez « caster » explicitement un `char` en un `int` avec `(char)`, et un `int` en un `char` avec `(int)`. Ou vous pouvez le faire implicitement en traitant simplement l'un comme l'autre.</li>
  
  <li data-marker="*">Il est probable que vous vouliez soustraire la valeur ASCII de 'A' à n'importe quelle lettre majuscule, afin de traiter 'A' comme 0, 'B' comme 1, etc., tout en effectuant l'arithmétique. Et puis l'ajouter à nouveau une fois terminé.</li>
  
  <li data-marker="*">Il est probable que vous vouliez soustraire la valeur ASCII de `'a'` à n'importe quelle lettre minuscule, afin de traiter `'''a'''` comme `'''0'''`, `'''b'''` comme `'''1'''`, etc., tout en effectuant l'arithmétique. Et puis l'ajouter à nouveau une fois terminé.</li>

  <li data-marker="*">Vous pourriez trouver utile que certaines autres fonctions déclarées dans `ctype.h`, telles que présentées dans <a href="https://manual.cs50.io/">manual.cs50.io</a>.</li>

  <li data-marker="*">Il est probable que vous trouviez l'utilisation de `%` utile pour effectuer une « boucle » arithmétiquement avec une valeur comme `25` pour la rendre à `0`.</li>

</ul>
</details>

Modifiez ensuite `main` de manière à ce qu'il imprime `"ciphertext : "` puis itère sur chaque `char` du texte en clair de l'utilisateur, en appelant `rotate` sur chacun et en imprimant la valeur renvoyée.

<details><summary>Conseils</summary>
<ul>
  <li data-marker="*">Rappelez-vous que `printf` peut imprimer un `char` en utilisant `%c`.</li>
  <li data-marker="*">Si vous ne voyez aucun résultat lorsque vous appelez `printf`, il est probable que cela soit dû à l'impression de caractères en dehors de la plage ASCII valide de 0 à 127. Essayez d'imprimer temporairement des caractères en tant que nombres (en utilisant `%i` plutôt que `%c`) pour voir les valeurs que vous imprimez !</li>
</ul>
</details>

## Procédure détaillée

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/V2uusmv2wxI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


## Comment tester votre code

Exécutez ce qui suit pour évaluer la justesse de votre code en utilisant `check50`. N'oubliez pas de le compiler et de le tester vous-même également !

    check50 cs50/problems/2023/x/caesar

Exécutez le contenu suivant pour évaluer le style de votre code en utilisant `style50`.

    style50 caesar.c

## Comment soumettre

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/caesar

