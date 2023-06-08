Commencer
---------------

Ouvrez [VS Code](https://code.cs50.io/).

Commencez en cliquant à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à ce qui suit.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/psets/4/reverse.zip
    

suivi de la touche Entrée pour télécharger un fichier ZIP appelé `reverse.zip` sur votre espace de code. Veillez à ne pas négliger l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Exécutez maintenant

    unzip reverse.zip
    

pour créer un dossier appelé `reverse`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm reverse.zip
    

et répondre par "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd reverse
    

suivi de Entrée pour vous déplacer dans ce répertoire (c'est-à-dire l'ouvrir). Votre invite devrait maintenant ressembler à ceci.

    reverse/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et voir un fichier nommé `reverse.c`. Exécuter `code reverse.c` devrait ouvrir le fichier dans lequel vous allez saisir votre code pour cet ensemble de problèmes. Sinon, revenez sur vos pas et voyez où vous avez commis une erreur !

### Le format de fichier WAV

Remarquez que, dans l'illustration ci-dessous, un fichier WAV est décomposé en trois parties différentes. Chaque partie contient quelques blocs de données.

La première partie contient des informations sur le type de fichier. En particulier, observez comment le bloc "Format de fichier" de la première partie épelle 'W' 'A' 'V' 'E' dans les octets 8 à 11, pour indiquer que le fichier est un fichier WAV.

La deuxième partie contient des informations sur les données audio à venir, y compris le nombre de «canaux» audio présents et le nombre de bits dans chaque «échantillon» audio. Les fichiers audio ont 1 canal lorsqu'ils sont "monophoniques" : si vous portiez des écouteurs, vous entendriez le même audio dans votre oreille gauche et droite. Les fichiers audio ont 2 canaux lorsqu'ils sont "stéréophoniques" : si vous portiez des écouteurs, vous entendriez un audio légèrement différent dans votre oreille gauche et droite, créant une sensation d'espace. Les échantillons sont les morceaux individuels de bits qui composent l'audio que vous entendez. Avec plus de bits par échantillon, un fichier audio peut avoir une plus grande clarté (mais au prix de l'utilisation de plus de mémoire !).

Enfin, la troisième partie contient les données audio elles-mêmes - les échantillons dont nous avons parlé ci-dessus.

Tout ce qui précède les données audio est considéré comme faisant partie de l'en-tête WAV. Rappelez-vous qu'un en-tête de fichier est simplement des métadonnées sur le fichier. Dans ce cas, l'en-tête fait 44 octets de long.

![En-tête WAV](https://cs50.harvard.edu/x/2023/psets/4/reverse/WAV_header.png)

Une explication plus technique des en-têtes WAV peut être trouvée [ici](http://soundfile.sapp.org/doc/WaveFormat/), qui est la ressource à l'origine de cette illustration. Notez que nous avons inclus un fichier `wav.h`, qui implémente tous ces détails pour vous dans une structure appelée` WAVHEADER`.