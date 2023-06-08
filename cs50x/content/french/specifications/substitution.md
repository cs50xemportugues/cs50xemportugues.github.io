Substitution
============

Pour ce problème, vous écrirez un programme qui implémente un chiffrement par substitution, tel qu'illustré ci-dessous.

    $ ./ substitution JTREKYAVOGDXPSNCUIZLFBMWHQ
    plaintext:  HELLO
    ciphertext: VKXXN
    

Pour commencer
--------------

Ouvrez [VS Code] (https://code.cs50.io/).

En commençant par cliquer à l'intérieur de la fenêtre de votre terminal, exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/psets/2/substitution.zip
    

suivi de Entrée pour télécharger un fichier ZIP appelé `substitution.zip` dans votre espace de code. Veillez à ne pas manquer l'espace entre `wget` et l'URL suivante, ni aucun autre caractère !

Maintenant, exécutez

    unzip substitution.zip
    

pour créer un dossier appelé `substitution`. Vous n'avez plus besoin du fichier ZIP, alors vous pouvez exécuter

    rm substitution.zip
    

et répondez "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd substitution
    

suivi de Entrée pour vous déplacer (c'est-à-dire ouvrir) dans ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    substitution/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et voir un fichier nommé `substitution.c`. En exécutant `code substitution.c`, vous devriez ouvrir le fichier dans lequel vous saisirez votre code pour cet ensemble de problèmes. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !

Contexte
----------

Dans un chiffrement par substitution, nous "chiffrons" (c'est-à-dire que nous dissimulons de manière réversible) un message en remplaçant chaque lettre par une autre lettre. Pour ce faire, nous utilisons une _clé_ : dans ce cas, un mappage de chacune des lettres de l'alphabet à la lettre à laquelle elle doit correspondre lors du chiffrement. Pour "décrypter" le message, le destinataire du message aurait besoin de connaître la clé afin de pouvoir inverser le processus : traduire le texte chiffré (généralement appelé _chiffré_) en le message original (généralement appelé _texte en clair_).

Une clé, par exemple, pourrait être la chaîne `NQXPOMAFTRHLZGECYJIUWSKDVB`. Cette clé de 26 caractères signifie que `A` (la première lettre de l'alphabet) doit être convertie en `N` (le premier caractère de la clé), `B` (la deuxième lettre de l'alphabet) doit être convertie en `Q` (le deuxième caractère de la clé), et ainsi de suite.

Un message comme `HELLO`, serait alors crypté sous la forme de `FOLLE`, remplaçant chacune des lettres selon le mappage déterminé par la clé.

Écrivons un programme appelé `substitution` qui vous permet de crypter des messages en utilisant un chiffrement par substitution. Au moment où l'utilisateur exécute le programme, il doit décider, en fournissant un argument de ligne de commande, de la clé qui doit être dans le message secret qu'il fournira à l'exécution.

Voici quelques exemples de fonctionnement possible du programme. Par exemple, si l'utilisateur entre une clé `YTNSHKVEFXRBAUQZCLWDMIPGJO` et un texte brut de `HELLO` :

    $ ./ substitution YTNSHKVEFXRBAUQZCLWDMIPGJO
    plaintext: HELLO
    ciphertext: EHBBQ
    

Voici comment le programme pourrait fonctionner si l'utilisateur fournit une clé `VCHPRZGJNTLSKFBDQWAXEUYMOI` et un texte clair de `hello, world` :

    $ ./ substitution VCHPRZGJNTLSKFBDQWAXEUYMOI
    plaintext: hello, world
    ciphertext: jrssb, ybwsp
    

Notez que ni la virgule ni l'espace n'ont été remplacés par le chiffrement. Remplacez uniquement les caractères alphabétiques ! Notez également que la casse du message d'origine a été préservée. Les lettres minuscules restent minuscules et les lettres majuscules restent majuscules.

Que les caractères de la clé sont eux-mêmes en majuscules ou en minuscules n'a pas d'importance. Une clé `VCHPRZGJNTLSKFBDQWAXEUYMOI` est identique à une clé de `vchprzgjntlskfbdqwaxeuymoi` (et aussi, en passant, à `VcHpRzGjNtLsKfBdQwAxEuYmOi`).

Et que se passe-t-il si un utilisateur ne fournit pas une clé valide ? Le programme devrait expliquer avec un message d'erreur :

    $ ./ substitution ABC
    Key must contain 26 characters.
    

Ou ne coopère vraiment pas, ne fournissant aucun argument de ligne de commande ? Le programme devrait rappeler à l'utilisateur comment utiliser le programme :

    $ ./ substitution
    Usage: ./substitution key
    

Ou vraiment, vraiment ne coopère pas, en fournissant trop d'arguments de ligne de commande ? Le programme devrait également rappeler à l'utilisateur comment utiliser le programme :

    $ ./ substitution 1 2 3
    Usage: ./substitution key
    

<details><summary>Regardez un enregistrement</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-HWzT4fngSv4KtdNFgfgpdLxZY" src="https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY.js"></script></details>

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

