# Lisibilité

Pour ce problème, vous allez implémenter un programme qui calcule le niveau de grade approximatif nécessaire pour comprendre un texte donné, comme indiqué ci-dessous.

    $ ./lisibilite
    Texte: Félicitations ! Aujourd'hui est votre jour. Vous partez vers de grands horizons ! Vous vous envolez loin !
    Niveau de grade 3

## Premiers Pas

Ouvrez [VS Code](https://code.cs50.io/).

Commencez par cliquer dans votre fenêtre de terminal, puis exécutez la commande `cd`. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $

Cliquez dans la fenêtre du terminal et exécutez ensuite la commande

    wget https://cdn.cs50.net/2022/fall/psets/2/readability.zip

puis appuyez sur Entrée pour télécharger un fichier ZIP nommé «readability.zip» dans votre espace de code. Faites attention à ne pas omettre l'espace entre «wget» et l'URL suivante, ni aucun autre caractère !

Maintenant, exécutez

    unzip readability.zip

pour créer un dossier nommé «lisibilite». Vous n'avez plus besoin du fichier ZIP, donc vous pouvez exécuter

    rm readability.zip

et répondre par "y" suivi de la touche Entrée à la invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd lisibilite

suivi de la touche Entrée pour vous déplacer dans (ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    lisibilite/ $

Si tout a fonctionné correctement, vous devriez exécuter

    ls

et voir un fichier nommé "readability.c". L'exécution de la commande `code readability.c` devrait ouvrir le fichier où vous allez taper votre code pour cet ensemble de problèmes. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Contexte

Selon [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), _Charlotte's Web_ d'E.B. White est adapté à un niveau de lecture de la 2ème à la 4ème année, tandis que _The Giver_ de Lois Lowry est adapté à un niveau de lecture de la 8ème à la 12ème année. Mais qu'est-ce que cela signifie pour un livre d'être à un niveau de lecture particulier ?

Eh bien, dans de nombreux cas, un expert littéraire peut lire un livre et décider du niveau (c.-à-d. de l'année scolaire) pour lequel il est le plus approprié. Mais un algorithme pourrait également probablement déterminer cela !

Alors, quels traits sont caractéristiques de niveaux de lecture plus élevés ? Eh bien, les mots plus longs sont probablement corrélés avec des niveaux de lecture plus élevés. De même, les phrases plus longues sont également corrélées avec des niveaux de lecture plus élevés.

Un certain nombre de "tests de lisibilité" ont été développés au fil des ans pour définir des formules pour le calcul du niveau de lecture d'un texte. Un de ces tests de lisibilité est l'indice de Coleman-Liau. L'indice de Coleman-Liau d'un texte est conçu pour produire le niveau scolaire (U.S.) nécessaire pour comprendre un texte. La formule est la suivante :

    index = 0,0588 * L - 0,296 * S - 15,8

où `L` est le nombre moyen de lettres pour 100 mots dans le texte et `S` est le nombre moyen de phrases pour 100 mots dans le texte.

Écrivons un programme appelé `readability` qui prend un texte et détermine son niveau de lecture. Par exemple, si un utilisateur tape une ligne de texte de Dr. Seuss, le programme devrait fonctionner comme suit :

    $ ./readability
    Texte : Félicitations ! Aujourd'hui est ton jour. Tu pars pour des endroits formidables ! Tu t'en vas !
    Niveau 3

Le texte que l'utilisateur a entré a 65 lettres, 4 phrases et 14 mots. 65 lettres pour 14 mots équivaut à une moyenne d'environ 464,29 lettres pour 100 mots (car 65 / 14 \* 100 = 464,29). Et 4 phrases pour 14 mots équivaut à une moyenne d'environ 28,57 phrases pour 100 mots (car 4 / 14 \* 100 = 28,57). En insérant ces valeurs dans la formule de Coleman-Liau, et en arrondissant à l'entier le plus proche, on obtient une réponse de 3 (car 0,0588 \* 464,29 - 0,296 \* 28,57 - 15,8 = 3) : donc ce passage est adapté à un niveau de lecture de la troisième année.

Essayons-en un autre :

    $ ./readability
    Texte : Harry Potter était un garçon très inhabituel à bien des égards. Pour une chose, il détestait les vacances d'été plus que tout autre moment de l'année. Pour une autre, il voulait vraiment faire ses devoirs, mais était obligé de les faire en secret, en pleine nuit. Et il était également sorcier.
    Niveau 5

Ce texte contient 214 lettres, 4 phrases et 56 mots. Cela donne environ 382,14 lettres pour 100 mots et 7,14 phrases pour 100 mots. En insérant ces valeurs dans la formule de Coleman-Liau, on obtient un niveau de lecture de la cinquième année.

À mesure que le nombre moyen de lettres et de mots par phrase augmente, l'indice de Coleman-Liau donne au texte un niveau de lecture plus élevé. Si vous preniez ce paragraphe, par exemple, qui a des mots et des phrases plus longues que les deux exemples précédents, la formule donnerait un niveau de lecture de la douzième année.

    $ ./readability
    Texte : À mesure que le nombre moyen de lettres et de mots par phrase augmente, l'indice de Coleman-Liau donne au texte un niveau de lecture plus élevé. Si vous preniez ce paragraphe, par exemple, qui a des mots et des phrases plus longues que les deux exemples précédents, la formule donnerait un niveau de lecture de la douzième année.
    Niveau 12

<details><summary>Regarder un enregistrement</summary><script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script></details>

## Spécifications

Concevoir et implémenter un programme, `readability`, qui calcule l'indice de Coleman-Liau d'un texte.

- Implémentez votre programme dans un fichier appelé `readability.c` dans un répertoire appelé `readability`.
- Votre programme doit inviter l'utilisateur à entrer une chaîne de texte en utilisant `get_string`.
- Votre programme doit compter le nombre de lettres, de mots et de phrases dans le texte. Vous pouvez supposer qu'une lettre est n'importe quel caractère en minuscule de `a` à `z` ou n'importe quel caractère en majuscule de `A` à `Z`, toute séquence de caractères séparée par des espaces doit être comptée comme un mot et que toute occurrence d'un point, d'un point d'exclamation ou d'un point d'interrogation indique la fin d'une phrase.
- Votre programme doit imprimer en sortie "Niveau X" où `X` est le niveau de lecture calculé par la formule de Coleman-Liau, arrondi à l'entier le plus proche.
- Si le nombre d'index résultant est de 16 ou plus (équivalent ou supérieur à un niveau de lecture d'étudiant de licence), votre programme doit afficher "Niveau 16+" au lieu de donner le nombre d'index exact. Si le nombre d'index est inférieur à 1, votre programme doit afficher "Avant la 1ère année".

### Obtenir une entrée utilisateur

Commençons par écrire du code en C qui permet simplement d'obtenir une entrée texte de l'utilisateur et de l'afficher . En particulier, implémentez dans `readability.c` une fonction `main` qui invite l'utilisateur avec `"Texte: "` en utilisant `get_string` puis imprime le même texte en utilisant `printf`. Et n'oubliez pas, en travaillant sur ce programme, que si vous utilisez des fonctions de bibliothèque, assurez-vous d'inclure tous les fichiers d'en-tête correspondants.

Le programme doit se comporter comme suit.

    $ ./readability
    Texte: Dans ma jeunesse, plus vulnérable, mon père m'a donné un conseil que je n'ai cessé de ruminer depuis.
    Dans ma jeunesse, plus vulnérable, mon père m'a donné un conseil que je n'ai cessé de ruminer depuis.

### Lettres

Maintenant que vous avez collecté l'entrée de l'utilisateur, commençons par analyser cette entrée en comptant le nombre de lettres dans le texte. Considérez les lettres comme étant des caractères alphabétiques en majuscules ou en minuscules, excluant les signes de ponctuation, les chiffres et autres symboles.

Ajoutez à `readability.c`, en dessous de `main`, une fonction appelée `count_letters` qui prend un argument, une `string` de texte, et qui renvoie un entier, le nombre de lettres dans ce texte. Assurez-vous d'ajouter le prototype de la fonction en haut de votre fichier pour que `main` sache comment l'appeler. Le prototype devrait ressembler à ce qui suit :

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">int</span> <span class="n">count_letters</span><span class="p">(</span><span class="n">string</span> <span class="n">text</span><span class="p">)</span>
</code></pre></div></div>

Appelez ensuite cette fonction dans `main` pour que, au lieu d'imprimer le texte lui-même, votre programme imprime maintenant le nombre de lettres dans le texte.

Le programme doit maintenant se comporter comme suit.

    $ ./readability
    Texte: Alice commençait à se sentir très fatiguée de s'asseoir à côté de sa sœur sur la rive, et de n'avoir rien à faire. Une ou deux fois, elle avait jeté un coup d'œil dans le livre que sa sœur lisait, mais il n'y avait ni images ni conversations, "Et à quoi sert un livre", pensa Alice, "sans images ni conversation?"
    235 lettres

<details><summary>Indice</summary><p>Déclarée dans <code class="language-plaintext highlighter-rouge">ctype.h</code>, une fonction qui peut vous être utile, conformément au guide <a href="https://manual.cs50.io/">manual.cs50.io</a>. Si vous l'utilisez, assurez-vous d'inclure ce fichier d'en-tête en haut de votre propre code !</p></details>

### Mots

L'indice Coleman-Liau ne se préoccupe pas seulement du nombre de lettres, mais aussi du nombre de mots dans une phrase. Pour ce problème, nous considérerons toute séquence de caractères séparés par un espace comme un mot (donc un mot avec un tiret tel que `"belle-sœur"` devrait être considéré comme un seul mot, pas trois).

Ajoutez à `readability.c`, en dessous de `main`, une fonction appelée `count_words` qui prend un paramètre, une `string` de texte, et qui renvoie un entier, le nombre de mots dans ce texte. Assurez-vous d'ajouter le prototype de la fonction en haut de votre fichier pour que `main` sache comment l'appeler. (Nous vous laissons son prototype !)

Ensuite, appelez cette fonction dans `main` pour que votre programme imprime également le nombre de mots dans le texte.

Vous pouvez supposer qu'une phrase :

- contiendra au moins un mot;
- ne commencera ni ne finira par un espace ; et
- n'aura pas plusieurs espaces de suite.

Bien sûr, vous pouvez essayer une solution qui tolère plusieurs espaces entre les mots ou même aucun mot !

Le programme doit maintenant se comporter comme suit.

    $ ./readability
    Texte: C'était un jour froid et lumineux d'avril, et les horloges sonnaient treize heures. Winston Smith, le menton niché dans sa poitrine dans un effort pour échapper au vent vil, passa rapidement à travers les portes vitrées de la Victoire Mansions, bien qu'il ne soit pas assez rapide pour empêcher une tourbillonnante poussière de gravier d'entrer en même temps que lui.
    250 lettres
    55 mots"

### Phrases

La dernière information que la formule de Coleman-Liau prend en compte, en plus du nombre de lettres et de mots, est le nombre de phrases. Déterminer le nombre de phrases peut être étonnamment difficile. Vous pourriez d'abord imaginer qu'une phrase est simplement une séquence de caractères qui se termine par un point, mais bien sûr, les phrases pourraient également se terminer par un point d'exclamation ou un point d'interrogation. Mais bien sûr, tous les points ne signifient pas nécessairement que la phrase est terminée. Par exemple, considérez la phrase ci-dessous.

    M. et Mme Dursley, du 4, Privet Drive, se targuaient d'être parfaitement normaux, merci pour eux.

C'est juste une seule phrase, mais il y a trois points! Pour ce problème, nous vous demanderons d'ignorer cette subtilité: vous devriez considérer toute séquence de caractères se terminant par un `.` ou un `!` ou un `?` comme une phrase (ainsi, pour la "phrase" ci-dessus, vous devriez la compter comme trois phrases). En pratique, la détection des limites de phrase doit être un peu plus intelligente pour gérer ces cas, mais nous ne nous en préoccuperons pas pour le moment.

Ajoutez à `readability.c`, sous `main`, une fonction appelée `count_sentences` qui prend un argument, une chaîne de caractères `string`, et qui renvoie un `int`, le nombre de phrases dans ce texte. Assurez-vous d'ajouter le prototype de la fonction, également au-dessus de votre fichier, afin que `main` sache comment l'appeler. (Nous vous laissons encore une fois son prototype!)

Ensuite, appelez cette fonction dans `main` afin que votre programme affiche également le nombre de phrases dans le texte.

Le programme devrait maintenant se comporter comme ci-dessous.

    $ ./readability
    Text: Quand il avait presque treize ans, mon frère Jem s'est gravement fracturé le bras au coude. Quand il s'est rétabli, et que les craintes de Jem de ne plus jamais pouvoir jouer au football ont été apaisées, il n'était guère conscient de sa blessure. Son bras gauche était un peu plus court que le droit ; lorsqu'il se tenait ou marchait, le dos de sa main était à angle droit par rapport à son corps, son pouce parallèle à sa cuisse.
    295 lettres
    70 mots
    3 phrases

### Mettons tout ensemble

Il est maintenant temps de mettre toutes les pièces ensemble ! Rappelons que l'indice de Coleman-Liau est calculé en utilisant la formule :

    index = 0,0588 * L - 0,296 * S - 15,8

où `L` est le nombre moyen de lettres pour 100 mots dans le texte, et `S` est le nombre moyen de phrases pour 100 mots dans le texte.

Modifiez `main` dans `readability.c` de sorte qu'au lieu de sortir le nombre de lettres, de mots et de phrases, il affiche plutôt (uniquement) le niveau de classe tel que défini par l'indice de Coleman-Liau (par exemple, `"Classe 2"` ou "`Classe 8" ou autre chose). Assurez-vous d'arrondir le numéro d'indice résultant au `int` le plus proche !

<details><summary>Conseils</summary><ul>
  <li data-marker="*">Rappelez-vous que <code class="language-plaintext highlighter-rouge">round</code> est déclaré dans le fichier <code class="language-plaintext highlighter-rouge">math.h</code>, selon le <a href="https://manual.cs50.io/">manuel.cs50.io</a> !</li>
  <li data-marker="*">Rappelez-vous que, lors de la division de valeurs de type <code class="language-plaintext highlighter-rouge">int</code> en C, le résultat sera également un <code class="language-plaintext highlighter-rouge">int</code>, avec tout reste (c'est-à-dire des chiffres après la décimale) supprimé. En d'autres termes, le résultat sera "tronqué". Vous voudrez peut-être convertir une ou plusieurs de vos valeurs en type < code class = "language-plaintext highlighter-rouge">float</code> avant de diviser lorsque vous calculez <code class="language-plaintext highlighter-rouge">L</code> et <code class="language-plaintext highlighter-rouge">S</code> !</li>
</ul></details>

Si le numéro d'indice résultant est supérieur ou égal à 16 (équivalent à un niveau de lecture de premier cycle universitaire ou supérieur), votre programme doit afficher `"Grade 16+"` au lieu de sortir un numéro d'indice précis. Si le numéro d'indice est inférieur à 1, votre programme doit afficher `"Before Grade 1"`.

## Procédure détaillée

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/AOVyZEh9zgE?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester votre code

Essayez d'exécuter votre programme sur les textes suivants pour vérifier que vous obtenez le niveau de lecture souhaité. Assurez-vous de copier uniquement le texte, sans espace supplémentaire.

- `Un poisson. Deux poissons. Poisson rouge. Poisson bleu.` (Avant la 1re année)
- `Les voudriez-vous ici ou là? Je ne les voudrais ni ici ni là. Je ne les voudrais nulle part.` (2e année)
- `Félicitations ! Aujourd'hui est votre jour. Vous partez pour de grands endroits! Vous êtes partis et vous y êtes!` (3e année)
- `Harry Potter était un garçon très inhabituel à bien des égards. Pour une chose, il détestait les vacances d'été plus que tout autre moment de l'année. D'autre part, il voulait vraiment faire ses devoirs, mais il était obligé de le faire en secret, en pleine nuit. Et il se trouvait également être un sorcier.` (5e année)
- `Dans ma jeunesse, mon père m'a donné un conseil que je n'ai cessé de méditer depuis.` (7e année)
- `Alice commençait à être très fatiguée de rester assise auprès de sa sœur sur la berge et de n'avoir rien à faire : elle avait déjà consulté plusieurs fois la boîte de livres de sa sœur, mais elle n'y avait trouvé ni images ni dialogues, « et à quoi bon un livre », pensait Alice, « sans images ni dialogues ? »` (8e année)
- `Quand il avait presque treize ans, mon frère Jem a eu le bras cassé au niveau du coude. Quand cela s'est guéri, et que les craintes de Jem de ne plus pouvoir jouer au football ont été apaisées, il n'était guère gêné par sa blessure. Son bras gauche était un peu plus court que son bras droit ; quand il se tenait debout ou marchait, le dos de sa main était à angle droit par rapport à son corps, son pouce parallèle à sa cuisse.` (8e année)
- `Il y a plus de choses dans le ciel et sur la terre, Horatio, que n'en rêve votre philosophie.` (9e année)
- `C'était un jour froid et lumineux d'avril, et les horloges sonnaient treize heures. Winston Smith, le menton rentré dans sa poitrine pour échapper au vent nauséabond, traversa rapidement les portes vitrées des Maisons de la Victoire, même si ce ne fut pas assez rapide pour empêcher une tourbillon de poussière de s'engouffrer avec lui.` (10e année)
- `Une grande classe de problèmes informatiques implique la détermination de propriétés de graphes, de graphes orientés, d'entiers, de tableaux d'entiers, de familles finies d'ensembles finis, de formules booléennes et d'éléments d'autres domaines dénombrables.` (16+)

Exécutez le code ci-dessous pour évaluer la justesse de votre code en utilisant `check50`. Mais assurez-vous également de le compiler et de le tester vous-même !

    check50 cs50/problems/2023/x/readability

Exécutez le code ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 readability.c

## Comment soumettre

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/readability

