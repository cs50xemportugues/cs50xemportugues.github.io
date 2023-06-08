Ampoules
========

Ampoules électriques pas si cassées
-------------------------------------

Pendant le cours, vous avez peut-être remarqué ce qui semblait être un "bug" sur la scène, où certaines ampoules semblent toujours éteintes :

![capture d'écran du cours de la semaine 2 avec une bande d'ampoules](https://cs50.harvard.edu/x/2023/psets/2/bulbs/binary_bulbs.jpg)

Chaque séquence d'ampoules, cependant, code un message en _binaire_, le langage que les ordinateurs "parlent". Écrivons un programme pour créer nos propres messages secrets, que nous pourrions même mettre en scène !

Mise en route
-------------

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer dans votre fenêtre de terminal, puis exécutez `cd` tout seul. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $
    

Cliquez dans cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/psets/2/bulbs.zip
    

suivi de Entrée pour télécharger un ZIP appelé `bulbs.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Maintenant, exécutez

    unzip bulbs.zip
    

pour créer un dossier appelé `bulbs`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm bulbs.zip
    

et répondez avec "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd bulbs
    

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    bulbs/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et voir un fichier nommé `bulbs.c`. L'exécution de `code bulbs.c` devrait ouvrir le fichier où vous taperez votre code pour ce problème défini. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous avez commis une erreur !

Détails de mise en œuvre
------------------------

Pour écrire notre programme, nous devrons d'abord réfléchir aux **bases**.

### Les bases

La base la plus simple est la base-1 ou le _unaire_; pour écrire un nombre, _N_, en base-1, nous écririons simplement _N_ `1`s consécutifs. Ainsi, le nombre `4` en base-1 serait écrit comme `1111`, et le nombre `12` comme `111111111111`. C'est comme compter sur vos doigts ou faire des traits sur un tableau.

Vous pourriez comprendre pourquoi la base-1 n'est pas beaucoup utilisée de nos jours. (Les nombres deviennent plutôt longs !) À la place, une convention courante est la base-10, ou _décimale_. En base-10, chaque _chiffre_ est multiplié par une puissance de 10, afin de représenter des nombres plus grands. Par exemple, `123` est abrégé <code>123 = 1 • 10<sup>2</sup> + 2 • 10<sup>1</sup> + 3 • 10<sup>0</sup></code>.

Changer de base est aussi simple que de changer le `10` ci-dessus par un nombre différent. Par exemple, si vous avez écrit `123` en base-4, le nombre que vous écririez vraiment est <code>123 = 1 • 4<sup>2</sup> + 2 • 4<sup>1</sup> + 3 • 4<sup>0</sup></code>, qui est égal au nombre décimal `27`.

Cependant, les ordinateurs utilisent la base-2 ou le _binaire_. En binaire, écrire `123` serait une erreur, car les nombres binaires ne peuvent avoir que des `0` et des `1`. Mais le processus de déterminer exactement quel nombre décimal un nombre binaire représente est exactement le même. Par exemple, le nombre `10101` en base-2 représente <code>1 • 2<sup>4</sup> + 0 • 2<sup>3</sup> + 1 • 2<sup>2</sup> + 0 • 2<sup>1</sup> + 1 • 2<sup>0</sup></code>, qui est égal au nombre décimal `21`.

### Encodage d'un message

Les ampoules ne peuvent être allumées ou éteintes. En d'autres termes, les ampoules représentent deux états possibles ; soit l'ampoule est allumée, soit elle est éteinte, tout comme les nombres binaires ne sont que des 1 ou des 0. Nous devrons trouver un moyen d'encoder le texte sous forme d'une séquence de nombres binaires.

Écrivons un programme appelé `bulbs` qui prend un message et le convertit en un ensemble d'ampoules que nous pourrions montrer à un public non averti. Nous le ferons en deux étapes :

* La première étape consiste à transformer le texte en nombres décimaux. Disons que nous voulons encoder le message `HI!`. Heureusement, nous avons déjà une convention en place pour le faire, [ASCII](https://asciichart.com/). Remarquez que `H` est représenté par le nombre décimal `72`, `I` est représenté par `73`, et `!` est représenté par `33`.
* La prochaine étape consiste à prendre nos nombres décimaux (comme `72`, `73`, et `33`) et à les convertir en nombres binaires équivalents, qui n'utilisent que des 0 et des 1. Pour avoir un nombre constant de bits dans chacun de nos nombres binaires, supposons que chaque décimal est représenté avec 8 bits. `72` est `01001000`, `73` est `01001001`, et `33` est `00100001`.

Enfin, nous interpréterons ces nombres binaires comme des instructions pour les ampoules sur scène ; 0 est éteint, 1 est allumé. (Vous constaterez que le fichier `bulbs.c` comprend une fonction `print_bulb` qui a été implémentée pour vous et qui prend un `0` ou un `1` en entrée et produit des émojis représentant des ampoules.)

Voici un exemple de fonctionnement du programme terminé. Contrairement à la scène de Sanders, nous imprimerons un octet par ligne pour plus de clarté.

    # ./bulbs
    Message: HI!
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫🟡
    

Pour vérifier notre travail, nous pouvons lire une ampoule qui est allumée (🟡) comme un `1` et une ampoule qui est éteinte (⚫) comme un `0`. Ensuite, `HI!` est devenu

    01001000
    01001001
    00100001
    

ce à quoi on pourrait s'attendre.

Un autre exemple :

    # ./bulbs
    Message: HI MOM
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫⚫
    ⚫🟡⚫⚫🟡🟡⚫🟡
    ⚫🟡⚫⚫🟡🟡🟡🟡
    ⚫🟡⚫⚫🟡🟡⚫🟡
    

Remarquez que tous les caractères sont inclus dans les instructions de l'ampoule, y compris les caractères non alphabétiques comme les espaces (`00100000`).

Spécification
-------------

Concevoir et implémenter un programme, `bulbs`, qui convertit du texte en instructions pour la bande de lumières sur la scène de CS50 de la manière suivante :

* Implémentez votre programme dans un fichier appelé `bulbs.c`.
* Votre programme doit d'abord demander à l'utilisateur un message en utilisant la fonction `get_string`.
* Votre programme doit ensuite convertir la `string` donnée en une série de nombres binaires de 8 bits, un pour chaque caractère de la chaîne.
* Vous pouvez utiliser la fonction `print_bulb` fournie pour imprimer une série de `0` et de `1` sous forme de série d'emoji jaunes et noirs, qui représentent des ampoules allumées et éteintes.
* Chaque "octet" de 8 symboles doit être imprimé sur sa propre ligne lorsqu'il est sorti ; il doit y avoir un `\n` après le dernier "octet" de 8 symboles également.

<details><summary>Conseils pour la conversion décimale en binaire</summary><p> Prenons un exemple avec le nombre 4. Comment convertir 4 en binaire ? Commencez par considérer le bit le plus à droite, celui qui, s'il est activé, ajoute 1 au nombre que nous représentons. Avez-vous besoin que ce bit soit activé ? Divisez 4 par 2 pour le savoir :</p>

`4 / 2 = 2`

<p>2 divise uniformément 4, ce qui nous indique qu'il n'y a pas de reste de 1 à s'inquiéter. Nous pouvons donc laisser ce bit le plus à droite inactif :</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>0
</code></pre></div></div>

<p>Et quelle est la situation pour le bit précédent, à gauche de ce bit que nous avons découvert ? Pour vérifier, suivons un processus similaire, mais reprenons où nous nous sommes arrêtés. Dans l'étape précédente, nous avons divisé 4 par 2 et obtenu 2. Maintenant, est-ce que 2 se divise uniformément dans 2 ? C'est le cas, il n'y a donc pas de reste de 2 à s'inquiéter :</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>00
</code></pre></div></div>

<p>Poursuivons encore plus loin. Après avoir divisé 2 par 2, il ne nous reste plus que 1. Division de 1 par 2 laisse un reste de 1. Cela signifie que nous devrons activer ce bit :</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>100
</code></pre></div></div>

<p>Et maintenant que nous avons divisé notre nombre jusqu'à 0, nous n'avons plus besoin de bits supplémentaires pour le représenter. Notez que nous avons découvert les bits pour représenter 4 dans l'ordre inverse dans lequel nous devons les imprimer : il est probable que nous aurons besoin d'une structure qui nous permet de stocker ces bits, afin que nous puissions les imprimer en avant plus tard. Et bien sûr, dans votre code réel, vous travaillerez avec des `chars` de 8 bits, vous voudrez donc préfixer les 0 nécessaires.</p>

<p>Lors de la vérification des restes, l'opérateur modulo (`%`) peut être utile ! <code class="language-plaintext highlighter-rouge">4 % 2</code>, par exemple, renvoie 0, ce qui signifie que 2 divise 4 avec un reste de 0.</p></details>

Comment tester votre code
---------------------

Votre programme doit fonctionner comme les exemples ci-dessus. Vous pouvez vérifier votre code en utilisant `check50`, un programme que CS50 utilisera pour tester votre code lorsque vous le soumettrez, en tapant ce qui suit à l'invite `$`. Mais assurez-vous également de le tester vous-même !

    check50 cs50/problems/2023/x/bulbs
    

Pour évaluer le style de votre code, tapez ce qui suit à l'invite `$`.

    style50 bulbs.c
    

Comment soumettre
-------------

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2023/x/bulbs"

