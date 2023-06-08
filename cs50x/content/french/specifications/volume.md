Lab 4: Volume
=============

<div class = "alert" data-alert= "warning" role = "alert"> <p> Vous pouvez collaborer avec un ou deux camarades de classe sur ce laboratoire, bien qu'il soit attendu que chaque étudiant de ce groupe contribue également au laboratoire. </p> </div>

Écrivez un programme pour modifier le volume d'un fichier audio.

    $ ./volume INPUT.wav OUTPUT.wav 2.0
    

Où `INPUT.wav` est le nom d'un fichier audio original et `OUTPUT.wav` est le nom d'un fichier audio dont le volume a été augmenté par le facteur donné (par exemple 2,0).

Fichiers WAV
---------

Les fichiers WAV sont un format de fichier commun pour représenter l'audio. Les fichiers WAV stockent l'audio sous forme de séquence d'échantillons : des nombres qui représentent la valeur d'un signal audio à un moment donné. Les fichiers WAV commencent par un "en-tête" de 44 octets qui contient des informations sur le fichier lui-même, y compris la taille du fichier, le nombre d'échantillons par seconde et la taille de chaque échantillon. Après l'en-tête, le fichier WAV contient une séquence d'échantillons, chacun étant un entier signé sur 2 octets (16 bits) représentant le signal audio à un moment donné.

Le fait de multiplier chaque valeur d'échantillon par un facteur donné a pour effet de changer le volume de l'audio. Par exemple, multiplier chaque valeur d'échantillon par 2.0 aura pour effet de doubler le volume de l'audio d'origine. Multiplier chaque échantillon par 0,5 aura quant à lui pour effet de diviser le volume par deux.

Types 
-----

Jusqu'à présent, nous avons vu plusieurs types en C, notamment `int`, `bool`, `char`, `double`, `float` et `long`. À l'intérieur d'un fichier d'en-tête appelé `stdint.h` se trouvent les déclarations de plusieurs autres types qui nous permettent de définir très précisément la taille (en bits) et le signe (signé ou non signé) d'un entier. Deux types en particulier nous seront utiles dans ce laboratoire.

*  `uint8_t` est un type qui stocke un entier non signé (c'est-à-dire pas négatif) de 8 bits. Nous pouvons traiter chaque octet de l'en-tête d'un fichier WAV comme une valeur `uint8_t`.
*  `int16_t` est un type qui stocke un entier signé de 16 bits (c'est-à-dire positif ou négatif). Nous pouvons traiter chaque échantillon de l'audio dans un fichier WAV comme une valeur `int16_t`.

Pour commencer
---------------

Ouvrez [VS Code] (https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` simplement. Vous devriez constater que son "invite de commande" ressemble à ce qui suit :

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/labs/4/volume.zip
    

suivi de la touche Entrée pour télécharger un fichier ZIP appelé `volume.zip` dans votre environnement de codage. Veillez à ne pas négliger l'espace entre `wget` et l'URL suivante, ou tout autre caractère !

Exécutez maintenant

    unzip volume.zip
    

pour créer un dossier appelé `volume`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm volume.zip
    

et répondre par "y" suivi de Entrée à la demande de suppression du fichier ZIP que vous avez téléchargé.

Tapez maintenant

    cd volume
    

suivi de Entrée pour vous déplacer (c'est-à-dire ouvrir) dans ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    volume/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et vous devriez voir un fichier `volume.c` à côté d'un fichier `input.wav`.

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez fait une erreur !

Détails de la mise en œuvre
Détailler la réalisation de volume.c pour qu'il modifie le volume d'un fichier sonore selon un facteur donné.

*  Le programme accepte trois arguments de ligne de commande : `input` représente le nom du fichier audio d'origine, `output` représente le nom du nouveau fichier audio qui doit être généré, et `factor` est la valeur par laquelle le volume du fichier audio d'origine doit être augmenté.
     * Par exemple, si `factor` est `2.0`, votre programme devrait doubler le volume du fichier audio dans `input` et enregistrer le nouveau fichier audio généré dans `output`.
*  Votre programme doit d'abord lire l'en-tête du fichier d'entrée et écrire l'en-tête dans le fichier de sortie. Rappelez-vous que cet en-tête mesure toujours exactement 44 octets.
     * Notez que `volume.c` définit déjà une variable pour vous appelée `HEADER_SIZE`, qui correspond au nombre d'octets dans l'en-tête.
*  Votre programme doit ensuite lire le reste des données du fichier WAV, un échantillon de 16 bits (2 octets) à la fois. Votre programme doit multiplier chaque échantillon par le facteur et écrire le nouvel échantillon dans le fichier de sortie.
    * Vous pouvez supposer que le fichier WAV utilisera des valeurs signées sur 16 bits en tant qu'échantillons. En pratique, les fichiers WAV peuvent avoir des nombres variables de bits par échantillon, mais nous supposerons des échantillons de 16 bits pour ce laboratoire.
*  Votre programme, s'il utilise `malloc`, ne doit pas perdre de mémoire.

### Comment faire?

*   Vous voudrez probablement créer un tableau d'octets pour stocker les données de l'en-tête WAV que vous lirez depuis le fichier d'entrée. En utilisant le type `uint8_t` pour représenter un octet, vous pouvez créer un tableau de `n` octets pour votre en-tête avec une syntaxe comme

<pre>
uint8_t header[n];
</pre>    

en remplaçant `n` par le nombre d'octets. Vous pouvez ensuite utiliser `header` comme argument pour `fread` ou `fwrite` pour lire dans l'en-tête ou écrire depuis l'en-tête.

*   Vous voudrez probablement créer un "tampon" dans lequel stocker les échantillons audio que vous lirez depuis le fichier WAV. En utilisant le type `int16_t` pour stocker un échantillon audio, vous pouvez créer une variable tampon avec une syntaxe comme

<pre>
int16_t buffer;
</pre>   

Vous pouvez ensuite utiliser `& buffer` comme argument pour `fread` ou `fwrite` pour lire dans le tampon ou écrire depuis le tampon. (Rappelez-vous que l'opérateur `&` est utilisé pour obtenir l'adresse de la variable.)

*   Vous pouvez trouver la documentation de [`fread`] (https://man.cs50.io/3/fread) et [`fwrite`] (https://man.cs50.io/3/fwrite) utile ici.
     * En particulier, notez que les deux fonctions acceptent les arguments suivants :
         * `ptr` : un pointeur vers l'emplacement en mémoire où stocker les données (lorsqu'on lit à partir d'un fichier) ou à partir desquelles écrire les données (lorsqu'on écrit des données dans un fichier)
         * `size` : le nombre d'octets dans une valeur
         * `nmemb` : le nombre de valeurs (chaque valeur étant composée de `size` octets) à lire ou à écrire
         * `stream` : le pointeur de fichier à lire ou à écrire
     * Selon sa documentation, `fread` renverra le nombre de valeurs réussies. Vous pouvez trouver cela utile pour vérifier lorsque vous avez atteint la fin du fichier !

<details><summary>Vous ne savez pas comment résoudre cela?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-rtZkTAK2gg"></iframe></details>


### Comment tester votre code?

Votre programme doit répondre aux exemples ci-dessous.

    $ ./volume input.wav output.wav 2.0
    

Lorsque vous écoutez `output.wav` (en contrôlant le clic sur `output.wav` dans le navigateur de fichiers, en choisissant **Télécharger**, puis en ouvrant le fichier dans un lecteur audio sur votre ordinateur), il doit être deux fois plus fort que `input.wav` !

    $ ./volume input.wav output.wav 0.5
    

Lorsque vous écoutez `output.wav`, il doit être deux fois moins fort que `input.wav` !

Exécutez le code ci-dessous pour évaluer la validité de votre code à l'aide de `check50`. Mais n'oubliez pas de le compiler et de le tester vous-même également !

    check50