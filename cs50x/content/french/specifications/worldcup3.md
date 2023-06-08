Détails de l'implémentation
----------------------

Complétez l'implémentation de `tournament.py` de manière à simuler un certain nombre de tournois et à afficher la probabilité de victoire de chaque équipe.

Tout d'abord, dans `main`, lisez les données de l'équipe à partir du fichier CSV dans la mémoire de votre programme et ajoutez chaque équipe à la liste `teams`.

*  Le fichier à utiliser sera fourni en tant qu'argument de ligne de commande. Vous pouvez accéder au nom du fichier avec `sys.argv[1]`.
*  Rappelez-vous que vous pouvez ouvrir un fichier avec `open(filename)`, où `filename` est une variable contenant le nom du fichier.
*  Une fois que vous avez un fichier `f`, vous pouvez utiliser `csv.DictReader(f)` pour vous donner un "lecteur": un objet en Python que vous pouvez parcourir pour lire le fichier une ligne à la fois, en traitant chaque ligne comme un dictionnaire.
*  Par défaut, toutes les valeurs lues à partir du fichier seront des chaînes de caractères. Assurez-vous donc d'abord de convertir la note de l'équipe en un entier (`int` function en Python peut être utilisée pour cela).
*  En définitive, ajoutez le dictionnaire de chaque équipe à `teams`. L'appel de fonction `teams.append(x)` ajoutera `x` à la liste `teams`.
*  Rappelez-vous que chaque équipe doit être un dictionnaire avec un nom d'équipe et une note.

Ensuite, implémentez la fonction `simulate_tournament`. Cette fonction devrait accepter en entrée une liste d'équipes et devrait simuler des rounds de manière répétée jusqu'à ce qu'il ne reste plus qu'une seule équipe. La fonction devrait ensuite renvoyer le nom de cette équipe.

*  Vous pouvez appeler la fonction `simulate_round`, qui simule un seul tour, en acceptant une liste d'équipes en entrée et en renvoyant une liste de tous les gagnants.
*  Rappelez-vous que si `x` est une liste, vous pouvez utiliser `len(x)` pour déterminer la longueur de la liste.
*  Vous ne devez pas supposer le nombre d'équipes dans le tournoi, mais vous pouvez supposer qu'il sera une puissance de 2.

Enfin, de retour dans la fonction `main`, exécutez `N` simulations de tournoi et suivez le nombre de victoires de chaque équipe dans le dictionnaire `counts`.

*  Par exemple, si l'Uruguay a remporté 2 tournois et le Portugal en a remporté 3, votre dictionnaire `counts` devrait être `{"Uruguay": 2, "Portugal": 3}`.
*  Vous devriez utiliser votre fonction `simulate_tournament` pour simuler chaque tournoi et déterminer le vainqueur.
*  Rappelez-vous que si `counts` est un dictionnaire, la syntaxe `counts[nom_de_l_equipe] = x` associera la clé stockée dans `nom_de_l_equipe` avec la valeur stockée dans `x`.
*  Vous pouvez utiliser le mot clé `in` en Python pour vérifier si un dictionnaire a déjà une clé particulière. Par exemple, `if "Portugal" in counts:` vérifiera si `"Portugal"` a déjà une valeur existante dans le dictionnaire `counts`.