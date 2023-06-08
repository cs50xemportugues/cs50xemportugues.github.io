ADN
===

Mettez en place un programme qui identifie une personne en fonction de son ADN, selon les éléments ci-dessous.

    $ python dna.py databases/large.csv sequences/5.txt
    Lavender
    

Pour commencer
--------------

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal, et exécutez simplement la commande `cd`. Votre invite de terminal devrait ressembler à ceci :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/6/dna.zip
    

afin de télécharger un dossier ZIP portant le nom `dna.zip` dans votre espace de code.

Ensuite, exécutez

    unzip dna.zip
    

pour créer un dossier appelé `dna`. Vous n'avez plus besoin du dossier ZIP, vous pouvez donc exécuter

     rm dna.zip
    

et répondre par "y" suivi de la touche Entrée pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant 

    cd dna
    

suivi de la touche Entrée pour rentrer dans (à savoir, ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ceci :

    dna/ $
    

Exécutez simplement `ls`, vous devriez voir quelques fichiers et dossiers :

    databases/ dna.py sequences/
    

Si vous rencontrez des problèmes, refaites les mêmes étapes et voyez où vous avez commis une erreur.

Contexte
----------
L'ADN, porteur d'informations génétiques chez les êtres vivants, est utilisé par les services judiciaires depuis des décennies. Mais comment fonctionne exactement le profilage d'ADN? Comment les enquêteurs peuvent-ils identifier à qui appartient une séquence d'ADN?

En réalité, l'ADN est simplement une séquence de molécules appelées nucléotides, arrangées dans une forme particulière (une double hélice). Chaque cellule humaine contient des milliards de nucléotides arrangés en séquence. Chaque nucléotide d'ADN contient l'une des quatre bases différentes : adénine (A), cytosine (C), guanine (G) ou thymine (T). Certaines parties de cette séquence (c'est-à-dire, le génome) sont les mêmes, ou du moins très similaires, chez presque tous les humains, mais d'autres parties de la séquence présentent une plus grande diversité génétique et varient donc davantage dans la population.

Un endroit où l'ADN a tendance à présenter une grande diversité génétique est dans les répétitions courtes en tandem (STR). Un STR est une courte séquence de bases d'ADN qui a tendance à se répéter consécutivement de nombreuses fois à des emplacements spécifiques à l'intérieur de l'ADN d'une personne. Le nombre de fois qu'un STR particulier se répète varie beaucoup d'un individu à l'autre. Dans les échantillons d'ADN ci-dessous, par exemple, Alice a le STR `AGAT` répété quatre fois dans son ADN, tandis que Bob a le même STR répété cinq fois.

![Exemples de STR](https://cs50.harvard.edu/x/2023/psets/6/dna/strs.png)

Utiliser plusieurs STR plutôt qu'un seul peut améliorer la précision du profilage de l'ADN. Si la probabilité que deux personnes aient le même nombre de répétitions pour un seul STR est de 5 % et que l'analyste examine 10 STR différents, la probabilité que deux échantillons d'ADN correspondent purement par hasard est d'environ 1 sur 1 quadrillion (en supposant que tous les STR sont indépendants les uns des autres). Ainsi, si deux échantillons d'ADN correspondent au nombre de répétitions de chacun des STRs, l'analyste peut être assez confiant qu'ils proviennent de la même personne. CODIS, la base de données ADN du FBI, utilise 20 STR différents dans le cadre de son processus de profilage d'ADN.

A quoi pourrait ressembler une telle base de données d'ADN ? Eh bien, dans sa forme la plus simple, vous pourriez imaginer formater une base de données d'ADN comme un fichier CSV, dans lequel chaque ligne correspond à un individu et chaque colonne correspond à un STR particulier.

    nom,AGAT,AATG,TATC
    Alice,28,42,14
    Bob,17,22,19
    Charlie,36,18,25
    

Les données dans le fichier ci-dessus suggèrent qu'Alice a la séquence `AGAT` répétée 28 fois consécutivement quelque part dans son ADN, la séquence `AATG` répétée 42 fois et `TATC` répétée 14 fois. Bob, quant à lui, a ces mêmes trois STR répétés 17 fois, 22 fois et 19 fois, respectivement. Et Charlie a ces mêmes trois STR répétés 36, 18 et 25 fois, respectivement.

Ainsi, étant donné une séquence d'ADN, comment pouvez-vous identifier à qui elle appartient ? Eh bien, imaginez que vous cherchez dans la séquence d'ADN la séquence consécutive la plus longue de `AGAT` répétée et que vous trouvez que la séquence la plus longue comporte 17 répétitions. Si vous trouvez ensuite que la séquence la plus longue de `AATG` est longue de 22 répétitions et que la séquence la plus longue de `TATC` est longue de 19 répétitions, cela fournirait une preuve assez solide que l'ADN appartient à Bob. Bien sûr, il est également possible qu'une fois que vous avez pris en compte les comptages pour chacun des STR, cela ne corresponde à personne dans votre base de données d'ADN, auquel cas il n'y a pas de correspondance.

En pratique, étant donné que les analystes savent sur quel chromosome et à quel emplacement dans l'ADN un STR sera trouvé, ils peuvent localiser leur recherche à une section étroite de l'ADN. Mais nous ignorerons ce détail pour ce problème.

Votre tâche est d'écrire un programme qui prendra une séquence d'ADN et un fichier CSV contenant des compteurs STR pour une liste d'individus, et qui renverra à qui l'ADN appartient (le plus probablement).

Spécification
-------------

Dans un fichier appelé `dna.py`, implémentez un programme qui identifie à qui appartient une séquence d'ADN.

* Le programme doit requérir en tant que premier argument de ligne de commande le nom d'un fichier CSV contenant les comptages STR pour une liste d'individus, et doit requérir en tant que second argument de ligne de commande le nom d'un fichier texte contenant la séquence d'ADN à identifier.
    * Si le programme est exécuté avec un nombre incorrect d'arguments de ligne de commande, votre programme doit afficher un message d'erreur de votre choix (avec `print`). Si le bon nombre d'arguments est fourni, vous pouvez supposer que le premier argument est en effet le nom d'un fichier CSV valide et que le second argument est le nom d'un fichier texte valide.
* Votre programme doit ouvrir le fichier CSV et lire son contenu en mémoire.
    * Vous pouvez supposer que la première ligne du fichier CSV sera les noms de colonnes. La première colonne sera le mot "name" et les colonnes restantes seront les séquences STR elles-mêmes.
* Votre programme doit ouvrir la séquence d'ADN et lire son contenu en mémoire.
* Pour chacun des STR (à partir de la première ligne du fichier CSV), votre programme doit calculer le plus long parcours de répétitions consécutives de la STR dans la séquence d'ADN à identifier. Notez que nous avons défini une fonction d'aide pour vous, `longest_match`, qui fera exactement cela !
* Si les comptages STR correspondent exactement à l'un des individus du fichier CSV, votre programme doit afficher le nom de l'individu correspondant.
    * Vous pouvez supposer que les comptages STR ne correspondront pas à plus d'un individu.
    * Si les comptages STR ne correspondent pas exactement à l'un des individus du fichier CSV, votre programme doit afficher `No match`.

Walkthrough
-----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/j84b_EgntcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Utilisation
-----

Votre programme doit fonctionner comme l'exemple ci-dessous :

<pre>
$ python dna.py databases/large.csv sequences/5.txt
Lavender
</pre>

<pre>
$ python dna.py
Usage: python dna.py data.csv sequence.txt
</pre>

<pre>
$ python dna.py data.csv
Usage: python dna.py data.csv sequence.txt
</pre>

Conseils
--------

*   Vous pouvez utiliser le module Python [`csv`](https://docs.python.org/3/library/csv.html) pour lire des fichiers CSV en mémoire. Vous pouvez utiliser [`csv.reader`](https://docs.python.org/3/library/csv.html#csv.reader) ou [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader).
*   Les fonctions [`open`](https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files) et [`read`](https://docs.python.org/3.3/tutorial/inputoutput.html#methods-of-file-objects) peuvent être utiles pour lire des fichiers texte en mémoire.
*   Considérez les structures de données qui pourraient être utiles pour suivre l'information dans votre programme. Une [`list`](https://docs.python.org/3/tutorial/introduction.html#lists) ou un [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) peuvent être utiles.
*   Rappelez-vous que nous avons défini une fonction (`longest_match`) qui, étant donné une séquence d’ADN et un STR en entrée, renvoie le nombre maximum de fois que l'STR se répète. Vous pouvez ensuite utiliser cette fonction dans d'autres parties de votre programme!

Tests
-----

Bien que `check50` soit disponible pour ce problème, vous êtes encouragé à tester d'abord votre code pour chacun des éléments suivants.

*   Exécutez votre programme en tant que `python dna.py databases/small.csv sequences/1.txt`. Votre programme devrait afficher `Bob`.
*   Exécutez votre programme en tant que `python dna.py databases/small.csv sequences/2.txt`. Votre programme doit afficher `No match`.
*   Exécutez votre programme en tant que `python dna.py databases/small.csv sequences/3.txt`. Votre programme doit afficher  `No match`.
*   Exécutez votre programme en tant que `python dna.py databases/small.csv sequences/4.txt`. Votre programme doit afficher `Alice`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/5.txt`. Votre programme doit afficher `Lavender`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/6.txt`. Votre programme doit afficher `Luna`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/7.txt`. Votre programme doit afficher `Ron`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/8.txt`. Votre programme doit afficher `Ginny`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/9.txt`. Votre programme doit afficher `Draco`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/10.txt`. Votre programme doit afficher `Albus`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/11.txt`. Votre programme doit afficher `Hermione`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/12.txt`. Votre programme doit afficher `Lily`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/13.txt`. Votre programme doit afficher `No match`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/14.txt`. Votre programme doit afficher `Severus`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/15.txt`. Votre programme doit afficher `Sirius`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/16.txt`. Votre programme doit afficher `No match`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/17.txt`. Votre programme doit afficher `Harry`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/18.txt`. Votre programme doit afficher `No match`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/19.txt`. Votre programme doit afficher `Fred`.
*   Exécutez votre programme en tant que `python dna.py databases/large.csv sequences/20.txt`. Votre programme doit afficher `No match`.

Exécutez ce qui suit pour évaluer la justesse de votre code en utilisant `check50`. Assurez-vous de compiler et de le tester vous-même également!

    check50 cs50/problems/2023/x/dna
    
Exécutez le suivant pour évaluer le style de votre code en utilisant `style50`.

    style50 dna.py
    

Comment soumettre
-----------------

Dans votre terminal, exécutez le suivant pour soumettre votre travail.

    submit50 cs50/problems/2023/x/dna"

