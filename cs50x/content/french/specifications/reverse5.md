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