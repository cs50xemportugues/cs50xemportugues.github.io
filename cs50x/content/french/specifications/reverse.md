Reverse
=======

Implémentez un programme qui inverse un fichier WAV, comme indiqué ci-dessous.

    ./reverse input.wav output.wav
    

Contexte
----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/J9iyqMwYtG4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Dans "Fire on High" d'Electric Light Orchestra, il y a quelque chose d'un peu étrange dans la première minute ou presque de la musique. Si vous y prêtez attention, cela semble presque comme si l'audio était joué à l'envers. En fait, si vous jouez la section du début de la chanson à l'envers, vous entendrez ce qui suit :

_«The music is reversible. Time is not. Turn back, turn back !»_

Effrayant, non ? Cette technique s'appelle le « backmasking », ou la dissimulation de messages dans la musique que l'on peut entendre uniquement lorsque la chanson est jouée à l'envers. De nombreux artistes ont utilisé (ou ont été soupçonnés d'utiliser) cette technique dans leurs chansons. Pour être en mesure de mener notre propre enquête sur le backmasking, nous vous avons demandé d'écrire un programme qui peut inverser des fichiers WAV pour nous !

Contrairement aux fichiers audio MP3, les fichiers WAV ne sont pas compressés. Cela rend les fichiers beaucoup plus faciles à éditer et à manipuler, ce qui est utile pour la tâche à accomplir. Pour en savoir un peu plus sur les fichiers WAV, nous devons examiner de plus près le format de fichier WAV.

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

Spécification
-------------

Écrivons un programme appelé `reverse` qui nous permet de retourner un fichier WAV fourni par l'utilisateur et de créer un nouveau fichier WAV contenant l'audio inversé résultant. Pour simplifier, nous limiterons les fichiers que nous traitons au format WAV. Au moment où l'utilisateur exécute le programme, il doit fournir, à l'aide de deux arguments de ligne de commande, le nom du fichier d'entrée qui doit être lu et inversé et le nom du fichier de sortie dans lequel l'audio résultant doit être enregistré. Un programme exécuté avec succès ne devrait pas produire de texte et devrait créer un fichier WAV avec le nom spécifié par l'utilisateur qui lit l'audio du fichier WAV d'entrée en sens inverse. Par exemple :

    $ ./reverse input.wav output.wav
    

Dans le fichier `reverse.c`, vous remarquerez que quelques bibliothèques utiles ont été incluses, ainsi qu'un fichier d'en-tête, `wav.h`. Vous trouverez probablement cela utile lors de la mise en œuvre de votre programme. Nous avons laissé huit `TODO` et deux fonctions d'aide pour que vous les remplissiez, et nous vous recommandons de les aborder dans l'ordre de 1 à 8.

*   Dans le premier `TODO`, vous devez vous assurer que le programme accepte deux arguments de ligne de commande : le nom du fichier WAV d'entrée et le nom du fichier WAV de sortie. Si le programme ne répond pas à ces conditions, vous devez afficher un message d'erreur approprié et renvoyer `1`, mettant fin au programme.
    <ul>
      <li data-marker="+">Indice
        <ul>
          <li data-marker="*">N'oubliez pas que le nombre d'arguments de ligne de commande peut être trouvé dans les variables `argc` passées à la fonction `main` lorsque le programme est exécuté.</li>
          <li data-marker="*">N'oubliez pas que `argv[0]` contient le nom du programme en tant que premier argument de ligne de commande.</li>
        </ul>
      </li>
    </ul>
*   Dans le deuxième `TODO`, vous devez ouvrir votre fichier d'entrée. Nous devrons ouvrir le fichier d'entrée en mode "lecture seule", car nous ne lirons que des données à partir du fichier d'entrée. Il peut être judicieux de vérifier que le fichier a été ouvert avec succès. Sinon, vous devez afficher un message d'erreur approprié et renvoyer `1`, en quittant le programme. Nous devons toutefois attendre pour ouvrir le fichier de sortie, afin de ne pas créer un nouveau fichier WAV avant de savoir si le fichier d'entrée est valide !
    <ul>
      <li data-marker="+">Indice
        <ul>
          <li data-marker="*">Si le premier `TODO` a été implémenté correctement, nous pouvons supposer en toute sécurité que nous pouvons faire référence au nom du fichier d'entrée en utilisant `argv [1]`.</li>
          <li data-marker="*">N'oubliez pas que tout fichier que nous ouvrons, nous devons également le fermer lorsque nous avons fini de l'utiliser. Cela peut impliquer d'ajouter du code ailleurs dans le programme.</li>
        </ul>
      </li>
    </ul>
*   Dans le troisième `TODO`, vous devez lire l'en-tête du fichier d'entrée. Rappelez-vous que, dans `wav.h`, nous avons déjà implémenté une structure qui peut stocker l'en-tête d'un fichier WAV. Étant donné que nous avons écrit `#include "wav.h"` en haut de `reverse.c`, vous pouvez également utiliser la structure `WAVHEADER`.
    
*   Dans le quatrième `TODO`, vous devez compléter la fonction `check_format`. `check_format` prend un seul argument appelé `header`, qui est un `WAVHEADER` représentant une structure contenant l'en-tête du fichier d'entrée. Si `header` indique que le fichier est effectivement un fichier WAV, la fonction `check_format` doit renvoyer `true`. Si ce n'est pas le cas, `check_format` doit renvoyer `false`. Pour vérifier si un fichier est au format WAV, nous pouvons comparer les éléments de l'en-tête du fichier d'entrée à ceux que nous attendons d'un fichier WAV. Il suffit de montrer que les caractères de l'indicateur "WAVE" se trouvent dans le membre `format` de la structure `WAVHEADER` (voir [Background](#background) pour plus de détails sur les en-têtes de fichier WAV).
    
*   Dans le cinquième `TODO`, vous pouvez maintenant ouvrir en toute sécurité le fichier de sortie pour l'écriture. Il serait sage de vérifier que le fichier a été ouvert avec succès.
    <ul>
      <li data-marker="+">Indice
        <ul>
          <li data-marker="*">Si le premier `TODO` a été implémenté correctement, nous pouvons supposer en toute sécurité que nous pouvons faire référence au nom du fichier de sortie en utilisant `argv [2]`.</li>
          <li data-marker="*">N'oubliez pas que tout fichier que nous ouvrons, nous devons également le fermer lorsque nous avons fini de l'utiliser. Cela peut impliquer d'ajouter du code ailleurs dans le programme.</li>
        </ul>
      </li>
    </ul>

C'est peut-être un bon endroit pour arrêter et tester que votre programme fonctionne comme prévu. Si elle est correctement mise en œuvre, votre programme doit ouvrir un nouveau fichier lorsqu'il est exécuté avec les bons arguments de ligne de commande.

Si vous trouvez à un moment donné nécessaire de supprimer un fichier, exécutez la commande suivante dans votre répertoire de travail actuel.

    $ rm file_name.wav
    

Si vous préférez ne pas être invité à confirmer chaque suppression, exécutez plutôt la commande ci-dessous.

    $ rm -f file_name.wav
    

Soyez simplement prudent avec ce commutateur `-f`, car il "force" la suppression sans vous demander votre avis.

*   Ensuite, maintenant que le type de fichier a été vérifié, le sixième `TODO` nous dit d'écrire l'en-tête dans le fichier de sortie. Le fichier WAV inversé aura toujours la même structure de fichier sous-jacente que le fichier d'entrée (même taille, nombre de canaux, bits par échantillon, etc.), il suffit donc de copier l'en-tête que nous avons lu à partir du fichier d'entrée dans le troisième `TODO` dans le fichier de sortie.

* Dans le septième `TODO`, vous devriez implémenter la fonction `get_block_size`. `get_block_size`, comme `check_format`, prend un seul argument : c'est un `WAVHEADER` appelé `header`, représentant la structure contenant l'en-tête du fichier d'entrée. `get_block_size` devrait retourner un entier représentant la taille de **blocs** du fichier WAV donné, en octets. Nous pouvons considérer un _bloc_ comme une unité de données auditives. Pour l'audio, nous calculons la taille de chaque bloc avec le calcul suivant : **nombre de canaux** multiplié par **nombre d'octets par échantillon**. Heureusement, l'en-tête contient toutes les informations dont nous avons besoin pour calculer ces valeurs. Assurez-vous de référencer la section [Background](#background) pour une explication plus approfondie de ce que signifient ces valeurs et comment elles sont stockées. Consultez également `wav.h`, pour déterminer quels membres de `WAVHEADER` pourraient être utiles.
<ul>
<li data-marker="+">Conseils
  <ul>
    <li data-marker="*">Remarquez qu'un des membres de la structure `WAVHEADER` est `bitsPerSample`. Mais pour calculer la taille de bloc, vous aurez besoin d'octets par échantillon!</li>
  </ul>
</li>
</ul>

* Le huitième et dernier `TODO` est où le renversement de l'audio a lieu. Pour cela, nous devons lire chaque bloc de données auditives à partir de la fin du fichier d'entrée et avancer de manière rétrograde, en écrivant simultanément chaque bloc vers le fichier de sortie afin qu'ils soient écrits dans l'ordre inverse. Tout d'abord, nous devons déclarer un tableau pour stocker chaque bloc que nous lisons. Ensuite, c'est à vous d'itérer à travers les données audio du fichier d'entrée. Vous voudrez être sûr que vous lisez tout l'audio, mais ne copiez pas par erreur aucune des données de l'en-tête ! De plus, à des fins de test, nous aimerions maintenir l'ordre des canaux pour chaque bloc audio. Par exemple, dans un fichier WAV avec deux canaux (son stéréophonique), nous voulons nous assurer que le premier canal du dernier bloc audio en entrée devient le premier canal du premier bloc audio en sortie.

<ul>
<li data-marker="+">Conseils
    <ul>
      <li data-marker="*">Quelques fonctions (et une compréhension approfondie de leur utilisation) peuvent être particulièrement utiles pour cette section - les pages du manuel CS50 peuvent s'avérer particulièrement utiles ici :
        <ul>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fread"><code class="language-plaintext highlighter-rouge">fread</code></a> : lit à partir d'un fichier et écrit vers un buffer. La sortie de la fonction auxiliaire <code class="language-plaintext highlighter-rouge">get_block_size</code> peut être utile ici pour décider des valeurs à utiliser pour la taille et le nombre de données à lire à chaque fois.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fwrite"><code class="language-plaintext highlighter-rouge">fwrite</code></a> : écrit à partir d'un buffer vers un fichier.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fseek"><code class="language-plaintext highlighter-rouge">fseek</code></a> : définit un pointeur de fichier sur un décalage donné. Il peut être utile d'expérimenter avec des valeurs de décalage négatives pour déplacer un pointeur de fichier vers l'arrière.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/ftell"><code class="language-plaintext highlighter-rouge">ftell</code></a> : retourne la position courante d'un pointeur de fichier. Il peut être utile d'inspecter quelle valeur <code class="language-plaintext highlighter-rouge">ftell</code> renvoie après que l'en-tête d'entrée est lu dans le troisième `TODO`, en plus de ce qu'elle renvoie pendant que les données audio sont lues.</li>
        </ul>
      </li>
      <li data-marker="*">Gardez à l'esprit qu'après avoir utilisé `fread` pour charger un bloc de données, le pointeur d'entrée pointerait à l'emplacement où la lecture s'est terminée. En d'autres termes, le pointeur d'entrée doit être déplacé de retour de deux tailles de bloc après chaque `fread`, une pour revenir à l'endroit où `fread` a commencé, et la seconde pour passer au bloc non lu précédent. </li>
    </ul>
</li>
</ul>

* Enfin, assurez-vous de fermer tous les fichiers que vous avez ouverts !

Utilisation
-----

Voici quelques exemples de comment le programme devrait fonctionner. Par exemple, si l'utilisateur omet un des arguments de la ligne de commande :

    $ ./reverse input.wav
    Utilisation : ./reverse input.wav output.wav
    

Ou si l'utilisateur omet les deux arguments de la ligne de commande :

    $ ./reverse
    Utilisation : ./reverse input.wav output.wav
    

Voici comment le programme devrait fonctionner si l'utilisateur fournit un fichier d'entrée qui n'est pas un véritable fichier WAV :

    $ ./reverse image.jpg output.wav
    L'entrée n'est pas un fichier WAV.
    

Vous pouvez supposer que l'utilisateur saisira un nom de fichier de sortie valide, tel que `output.wav`.

Un programme exécuté avec succès ne doit afficher aucun texte et doit créer un fichier WAV avec le nom spécifié par l'utilisateur qui joue l'audio du fichier WAV d'entrée à l'envers. Par exemple :

    $ ./reverse input.wav output.wav
    

Test
-------

Exécutez ce qui suit pour évaluer la correction de votre code en utilisant "check50". Mais assurez-vous de le compiler et de le tester vous-même aussi !

    check50 cs50/problems/2023/x/reverse
    

Exécutez ce qui suit pour évaluer le style de votre code en utilisant "style50".

    style50 reverse.c
    

Comment soumettre
-------------

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2023/x/reverse"

