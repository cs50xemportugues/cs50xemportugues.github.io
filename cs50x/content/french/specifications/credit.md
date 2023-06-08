# Crédit

## Premiers pas

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer à l'intérieur de la fenêtre du terminal, puis exécutez `cd` seul. Vous devez constater que sa "invite" ressemble à celle ci-dessous.

```
$
```

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

```
wget https://cdn.cs50.net/2022/fall/psets/1/credit.zip
```

suivi de la touche "Entrée" pour télécharger un ZIP appelé `credit.zip` dans votre espace de codes. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Maintenant, exécutez

```
unzip credit.zip
```

pour créer un dossier appelé `credit`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

```
rm credit.zip
```

et répondre par "y" suivi de la touche "Entrée" à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

```
cd credit
```

suivi de la touche "Entrée" pour vous déplacer dans ce répertoire. Votre invite doit maintenant ressembler à celle ci-dessous.

```
credit/ $
```

Si tout s'est bien passé, vous devez exécuter

```
ls
```

et voir un fichier nommé `credit.c`. En exécutant `code credit.c`, le fichier s'ouvre et vous pouvez taper votre code pour cet ensemble de problèmes. Si ce n'est pas le cas, revenez en arrière et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Cartes de crédit

Une carte de crédit (ou de débit) est une carte en plastique avec laquelle vous pouvez payer des biens et des services. Un numéro imprimé sur cette carte est également stocké quelque part dans une base de données, de sorte que lorsque votre carte est utilisée pour acheter quelque chose, le créancier sait à qui facturer. Il y a beaucoup de personnes avec des cartes de crédit dans ce monde, de sorte que ces numéros sont assez longs : American Express utilise des nombres à 15 chiffres, MasterCard utilise des nombres à 16 chiffres et Visa utilise des nombres à 13 et 16 chiffres. Et ceux-ci sont des nombres décimaux (0 à 9), pas binaires, ce qui signifie, par exemple, qu'American Express pourrait imprimer jusqu'à 10^15 = 1 000 000 000 000 000 cartes uniques ! (C'est, euh, un quadrillion).

En fait, c'est un peu exagéré, car les numéros de carte de crédit ont en réalité une certaine structure. Tous les numéros American Express commencent par 34 ou 37 ; la plupart des numéros MasterCard commencent par 51, 52, 53, 54 ou 55 (ils ont également d'autres numéros de départ possibles qui ne nous concernent pas pour ce problème) ; et tous les numéros Visa commencent par 4. Mais les numéros de carte de crédit ont également une "somme de contrôle" intégrée, une relation mathématique entre au moins un nombre et d'autres. Cette somme de contrôle permet aux ordinateurs (ou aux humains qui aiment les mathématiques) de détecter les fautes de frappe (par exemple, les transpositions), mais pas les numéros frauduleux, sans avoir à interroger une base de données, ce qui peut être lent. Bien sûr, un mathématicien malhonnête pourrait certainement créer un faux numéro qui respecte néanmoins la contrainte mathématique, de sorte qu'une recherche dans une base de données est toujours nécessaire pour des vérifications plus rigoureuses.

## Algorithme de Luhn

Alors, quelle est la formule secrète ? Eh bien, la plupart des cartes utilisent un algorithme inventé par Hans Peter Luhn d'IBM. Selon l'algorithme de Luhn, vous pouvez déterminer si un numéro de carte de crédit est (syntaxiquement) valide comme suit :

1. Multipliez chaque deuxième chiffre par 2, en commençant par l'avant-dernier chiffre du nombre, puis ajoutez les chiffres de ces produits ensemble.
2. Ajoutez la somme à la somme des chiffres qui n'ont pas été multipliés par 2.
3. Si le dernier chiffre du total est 0 (ou, de manière plus formelle, si le total modulo 10 est congruent à 0), le nombre est valable !

C'est un peu confus, alors essayons un exemple avec la carte Visa de David : 4003600000000014.

1. Pour les besoins de la discussion, soulignons d'abord chaque deuxième chiffre, en commençant par l'avant-dernier chiffre du nombre :

    <p><u>4</u>0<u>0</u>3<u>6</u>0<u>0</u>0<u>0</u>0<u>0</u>0<u>0</u>1<u>4</u></p>

    D'accord, multiplions maintenant chacun des chiffres soulignés par 2 :

    1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

    Ce qui nous donne :

    2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

    Maintenant, ajoutons les chiffres de ces produits (c.-à-d. pas les produits eux-mêmes) ensemble :

    2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

2. Ajoutons maintenant cette somme (13) à la somme des chiffres qui n'ont pas été multipliés par 2 (en commençant par la fin) :

    13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

3. Oui, le dernier chiffre de cette somme (20) est 0, donc la carte de David est légale !

Ainsi, la validation des numéros de carte de crédit n'est pas difficile, mais cela devient un peu fastidieux à faire à la main. Écrivons donc un programme.

## Détails de mise en œuvre

Dans le fichier appelé `credit.c` dans le répertoire `credit`, écrivez un programme qui invite l'utilisateur à saisir un numéro de carte de crédit, puis indique (par le biais de `printf`) s'il s'agit d'un numéro de carte American Express, MasterCard ou Visa valide, selon les définitions de chaque format mentionné. Ainsi, pour que nous puissions automatiser certains tests de votre code, nous vous demandons que la dernière ligne de sortie de votre programme soit `AMEX\n` ou `MASTERCARD\n` ou `VISA\n` ou `INVALID\n`, rien de plus, rien de moins. Pour simplifier, vous pouvez supposer que l'entrée de l'utilisateur sera entièrement numérique (c'est-à-dire dépourvue de tirets, comme cela pourrait être imprimé sur une carte réelle) et que cela ne comportera pas de zéros initiaux. Mais ne supposez pas que l'entrée de l'utilisateur pourra être incluse dans un `int` ! Il est préférable d'utiliser `get_long` de la bibliothèque de CS50 pour obtenir les entrées des utilisateurs. (Pourquoi ?)

Considérons l'exemple suivant comme représentatif de la manière dont votre propre programme doit fonctionner lorsqu'on lui passe un numéro de carte de crédit valide (sans tirets).

```
$ ./credit
Number: 4003600000000014
VISA
```

Maintenant, `get_long` rejettera lui-même les tirets (et autres) :

```
$ ./credit
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

Mais c'est à vous de détecter les entrées qui ne sont pas des numéros de carte de crédit (par exemple, un numéro de téléphone), même s'ils sont numériques :

```
$ ./credit
Number: 6176292929
INVALID
```

Testez votre programme avec une série d'entrées, à la fois valides et invalides. (Nous le ferons certainement !) Voici quelques [numéros de carte](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) que PayPal recommande pour les tests.

Si votre programme se comporte incorrectement sur certaines entrées (ou ne se compile pas du tout), c'est le moment du débogage !

### Exemple de parcours

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/dF7wNjsRBjI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Comment tester votre code

Vous pouvez également exécuter la commande suivante pour évaluer la justesse de votre code en utilisant `check50`. Mais assurez-vous aussi de le compiler et de le tester vous-même !

```
check50 cs50/problems/2023/x/credit
```

Exécutez la commande ci-dessous pour évaluer le style de votre code en utilisant `style50`.

```
style50 credit