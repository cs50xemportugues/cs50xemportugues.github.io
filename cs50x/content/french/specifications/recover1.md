Récupération
=======

Implémentez un programme qui récupère les fichiers JPEG d'une image numérique, comme suit.

    $ ./recover card.raw
    

Contexte
----------

En prévision de ce problème, nous avons passé les derniers jours à prendre des photos dans le campus, toutes enregistrées sur un appareil photo numérique sous forme de fichiers JPEG sur une carte mémoire. Malheureusement, nous les avons supprimées par erreur ! Heureusement, dans le monde de l'informatique, "supprimé" ne signifie pas vraiment "supprimé" mais plutôt "oublié". Même si l'appareil photo affirme que la carte est maintenant vide, nous sommes assez sûrs que ce n'est pas tout à fait vrai. En effet, nous espérons (euh, nous nous attendons!) que vous pouvez écrire un programme qui récupère les photos pour nous !

Même si les fichiers JPEG sont plus compliqués que les fichiers BMP, ils ont des "signatures", des motifs d'octets qui peuvent les distinguer d'autres formats de fichiers. En particulier, les trois premiers octets des fichiers JPEG sont

     0xff 0xd8 0xff
    

du premier octet au troisième octet, de gauche à droite. Le quatrième octet, quant à lui, est soit `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee` ou` 0xef`. En d'autres termes, les quatre premiers bits du quatrième octet sont `1110`.

Il est probable que si vous trouvez cette signature de quatre octets sur un support connu pour stocker des photos (par exemple, ma carte mémoire), ils indiquent le début d'un JPEG. Pour être juste, vous pourriez rencontrer ces motifs sur un disque par pure chance, donc la récupération de données n'est pas une science exacte.

Heureusement, les appareils photo numériques ont tendance à stocker les photographies contiguëment sur les cartes mémoire, où chaque photo est stockée immédiatement après la photo précédente. Par conséquent, le début d'un JPEG marque généralement la fin d'un autre. Cependant, les appareils photo numériques initialisent souvent des cartes avec un système de fichiers FAT dont la "taille de bloc" est de 512 octets (B). Cette implication est que ces appareils photo n'écrivent sur ces cartes que par unités de 512 B. Une photo d'1 Mo (c'est-à-dire 1 048 576 B) occupe ainsi 1048576 ÷ 512 = 2048 "blocs" sur une carte mémoire. Mais il en est de même pour une photo d'une taille inférieure d'un octet (c'est-à-dire 1 048 575 B) ! L'espace gaspillé sur le disque est appelé "slack space". Les enquêteurs judiciaires examinent souvent l'espace libre pour voir les restes de données suspects.

L'implication de tous ces détails est que vous, l'enquêteur, pouvez probablement écrire un programme qui itère sur une copie de ma carte mémoire, cherchant les signatures de fichiers JPEG. Chaque fois que vous trouvez une signature, vous pouvez ouvrir un nouveau fichier pour l'écriture et commencer à remplir ce fichier avec des octets de ma carte mémoire, en le fermant uniquement une fois que vous rencontrez une autre signature. De plus, plutôt que de lire les octets de ma carte mémoire un par un, vous pouvez en lire 512 à la fois dans un tampon pour des raisons d'efficacité. Grâce à FAT, vous pouvez vous assurer que les signatures de fichiers JPEG seront "alignées sur les blocs". Autrement dit, vous n'avez qu'à chercher ces signatures dans les quatre premiers octets d'un bloc.

Bien entendu, les fichiers JPEG peuvent s'étendre sur des blocs contigus. Sinon, aucun fichier JPEG ne pourrait dépasser 512 B. Mais le dernier octet d'un fichier JPEG pourrait ne pas être situé tout à fait à la fin d'un bloc. Rappelez-vous la possibilité d'espace libre. Mais ne vous inquiétez pas. Comme cette carte mémoire était neuve lorsque j'ai commencé à prendre des photos, il est probable qu'elle ait été "mise à zéro" (c'est-à-dire remplie de 0) par le fabricant, auquel cas tout espace libre sera rempli de 0. Ce n'est pas grave si ces 0 finaux se retrouvent dans les fichiers JPEG que vous récupérez ; ils devraient quand même être visibles.

Maintenant, je n'ai qu'une seule carte mémoire, mais il y a beaucoup d'entre vous ! C'est pourquoi j'ai créé une "image numérique" de la carte, stockant son contenu, octet après octet, dans un fichier appelé `card.raw`. Afin que vous ne perdiez pas de temps à itérer inutilement sur des millions de zéros, j'ai seulement imaginé les premiers mégaoctets de la carte mémoire. Mais vous devriez finalement trouver que l'image contient 50 fichiers JPEG.

Pour commencer
---------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Votre invite de terminal devrait ressembler à ceci:

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/4/recover.zip
    

pour télécharger un fichier ZIP appelé `recover.zip` dans votre espace de travail.

Ensuite, exécutez

    unzip recover.zip
    

pour créer un dossier appelé `recover`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm recover.zip
    

et répondez par "y" suivi de Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant

    cd recover
    

suivi de Entrée pour vous déplacer dans ce répertoire. Votre invité doit maintenant ressembler à ceci.

    recover / $
    

Exécutez `ls` seul, et vous devriez voir deux fichiers: `recover.c` et 'card.raw\'.

Spécifications
-------------

Implémentez un programme appelé `recover` qui récupère les fichiers JPEG d'une image numérique.

*   Implémentez votre programme dans un fichier appelé `recover.c` dans un répertoire appelé `recover`.
*   Votre programme doit accepter exactement un argument de ligne de commande, le nom d'une image numérique à partir de laquelle récupérer les fichiers JPEG.
*   Si votre programme n'est pas exécuté avec exactement un argument de ligne de commande, il doit rappeler à l'utilisateur l'utilisation correcte, et `main` doit renvoyer` 1`.
*   Si l'image numérique ne peut pas être ouverte en lecture, votre programme doit en informer l'utilisateur et `main` doit renvoyer `1`.
*   Les fichiers que vous générez doivent être nommés `###.jpg`, où `###` est un nombre décimal à trois chiffres, en commençant par `000` pour la première image et en comptant vers le haut.
*   Votre programme, s'il utilise `malloc`, ne doit pas libérer de mémoire.