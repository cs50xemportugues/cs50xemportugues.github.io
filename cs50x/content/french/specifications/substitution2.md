Spécification
-------------

Concevoir et implémenter un programme nommé `substitution` qui chiffre les messages en utilisant un chiffrement par substitution.

* Implémentez votre programme dans un fichier appelé `substitution.c` dans un répertoire appelé `substitution`.
* Votre programme doit accepter un seul argument en ligne de commande, la clé à utiliser pour la substitution. La clé elle-même doit être insensible à la casse, donc le fait que n'importe quel caractère de la clé soit en majuscule ou en minuscule ne devrait pas affecter le comportement de votre programme.
* Si votre programme est exécuté sans arguments de ligne de commande ou avec plus d'un argument de ligne de commande, votre programme devrait afficher un message d'erreur de votre choix (avec `printf`) et quitter `main` en renvoyant immédiatement une valeur de `1` (qui tend à signifier une erreur).
* Si la clé est invalide (par exemple si elle ne contient pas 26 caractères, si elle contient un caractère qui n'est pas alphabétique, ou si elle ne contient pas chaque lettre exactement une fois), votre programme doit afficher un message d'erreur de votre choix (avec `printf`) et quitter `main` en renvoyant immédiatement une valeur de `1`.
* Votre programme doit afficher `plaintext :` (sans saut de ligne), puis inviter l'utilisateur à saisir une chaîne de `texte en clair` (en utilisant `get_string`).
* Votre programme doit afficher `ciphertext :` (sans saut de ligne), suivi du texte en clair correspondant chiffré, chaque caractère alphabétique dans le texte en clair étant substitué par le caractère correspondant dans le texte chiffré ; les caractères non alphabétiques doivent être affichés inchangés.
* Votre programme doit préserver la casse : les lettres majuscules doivent rester des lettres majuscules ; les lettres minuscules doivent rester des lettres minuscules.
* Après la sortie du texte chiffré, vous devez imprimer une nouvelle ligne. Votre programme doit ensuite quitter en renvoyant `0` de `main`.

Vous pouvez trouver une ou plusieurs fonctions déclarées dans `ctype.h` utiles, selon [manual.cs50.io] (https://manual.cs50.io/).


Marchethé à suivre
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cXAoZAsgxJ4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Comment tester votre code
-------------------------

Exécutez ce qui suit pour évaluer la correction de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester vous-même également !

    check50 cs50/problems/2023/x/substitution


Exécutez ce qui suit pour évaluer le style de votre code en utilisant `style50`.

    style50 substitution.c


<details><summary>Comment utiliser <code>debug50</code></summary><p>Vous souhaitez exécuter `debug50` ? Vous pouvez le faire comme suit, après avoir compilé votre code avec succès avec `make`,</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution KEY
</code></pre></div></div>

<p>où <code class="language-plaintext highlighter-rouge">KEY</code> est la clé que vous donnez en argument de ligne de commande à votre programme. Notez que l'exécution de</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>debug50 ./substitution
</code></pre></div></div>

<p>fera (idéalement !) en sorte que votre programme se termine en invitant l'utilisateur à saisir une clé.</p></details>


Comment soumettre
-----------------

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/substitution