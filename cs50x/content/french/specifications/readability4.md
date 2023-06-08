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