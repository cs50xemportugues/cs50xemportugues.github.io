Distribution
------------

### Comprendre

Théoriquement, un algorithme qui a une durée d'exécution de _n_ sur une entrée de taille _n_ est « asymptotiquement équivalent », en termes de _O_, à un algorithme qui a une durée d'exécution de _2n_. En effet, lorsqu'on décrit la durée d'exécution d'un algorithme, on se concentre généralement sur le terme dominant (c'est-à-dire le terme le plus impactant) (_n_ dans ce cas puisque _n_ peut être beaucoup plus grand que 2). Dans le monde réel, cependant, la durée d'exécution de _2n_ semble deux fois plus lente que celle de _n_.

Le défi qui vous attend consiste à implémenter le vérificateur d'orthographe le plus rapide possible ! Par « plus rapide », nous parlons du temps réel d'exécution du programme, pas seulement de son temps asymptotique.

Dans `speller.c`, nous avons mis en place un programme conçu pour vérifier l'orthographe d'un fichier après avoir chargé un dictionnaire de mots du disque en mémoire. Ce dictionnaire, pour sa part, est implémenté dans un fichier appelé `dictionary.c`. (Il pourrait simplement être implémenté dans `speller.c`, mais à mesure que les programmes deviennent plus complexes, il est souvent pratique de les diviser en plusieurs fichiers.) Les prototypes des fonctions dans ces fichiers sont définis dans `dictionary.h` plutôt que dans `dictionary.c` lui-même. De cette façon, `speller.c` et `dictionary.c` peuvent tous deux inclure le fichier. Malheureusement, nous n'avons pas tout à fait réussi à implémenter la partie de chargement. Ou la partie de vérification. Nous vous laissons les deux (et un peu plus) à vous de les implémenter ! Mais d'abord, une visite guidée.

#### `dictionary.h`

Ouvrez `dictionary.h` et vous verrez une nouvelle syntaxe, y compris quelques lignes qui mentionnent `DICTIONARY_H`. Il n'y a pas besoin de s'en préoccuper, mais si vous êtes curieux, ces lignes garantissent que, même si `dictionary.c` et` speller.c` (que vous verrez bientôt) incluent ce fichier, `clang` ne le compilera qu'une seule fois.

Ensuite, remarquez comment nous incluons un fichier appelé` stdbool.h`. C'est le fichier dans lequel `bool` lui-même est défini. Vous n'en aviez pas besoin auparavant, car la bibliothèque CS50 « #include » cela pour vous.

Remarquez également notre utilisation de `#define`, une « directive de préprocesseur » qui définit une « constante » appelée `LENGTH` ayant une valeur de `45`. C'est une constante dans le sens où vous ne pouvez pas le changer (accidentellement) dans votre propre code. En fait, `clang` remplacera toutes les mentions de `LENGTH` dans votre propre code par `45`. En d'autres termes, ce n'est pas une variable, juste un truc de find-and-replace.

Enfin, remarquez les prototypes des cinq fonctions : `check`, `hash`, `load`, `size` et `unload`. Remarquez comment trois d'entre eux prennent un pointeur en argument, comme indiqué par `*` :

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>
    

Rappelez-vous que `char *` est ce que nous utilisions pour appeler `string`. Ainsi, ces trois prototypes sont simplement :

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>

Et `const`, quant à lui, signifie simplement que ces chaînes, lorsqu'elles sont transmises en tant qu'arguments, doivent rester constantes, vous ne pourrez pas les modifier, accidentellement ou autrement!