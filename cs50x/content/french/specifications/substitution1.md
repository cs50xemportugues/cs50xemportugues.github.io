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