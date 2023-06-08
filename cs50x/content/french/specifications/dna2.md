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