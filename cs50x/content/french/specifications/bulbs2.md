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