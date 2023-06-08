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