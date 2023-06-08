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