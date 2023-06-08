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