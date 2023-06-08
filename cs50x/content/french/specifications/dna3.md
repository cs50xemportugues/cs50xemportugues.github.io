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