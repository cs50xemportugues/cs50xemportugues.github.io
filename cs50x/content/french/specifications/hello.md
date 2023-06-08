# Bonjour

## Premiers Pas

Rappelez-vous que Visual Studio Code (alias VS Code) est un environnement de développement intégré (IDE) populaire avec lequel vous pouvez écrire du code. Pour éviter de télécharger, installer et configurer votre propre version de VS Code, nous utiliserons plutôt une version basée sur le cloud, qui contient tout ce dont vous aurez besoin pré-installé.

Connectez-vous à [code.cs50.io](https://code.cs50.io/) en utilisant votre compte GitHub. Une fois que votre "codespace" est chargé, vous devriez voir que, par défaut, VS Code est divisé en trois régions. Vers le haut de VS Code se trouve votre "éditeur de texte", où vous écrirez tous vos programmes. Vers le bas se trouve la "fenêtre de terminal", une interface en ligne de commande (CLI) qui vous permet d'explorer les fichiers et les répertoires (également appelés dossiers) de votre espace de code, de compiler du code et d'exécuter des programmes. Et sur la gauche se trouve votre "explorateur de fichiers", une interface utilisateur graphique (GUI) avec laquelle vous pouvez également explorer les fichiers et les répertoires de votre espace de code.

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` en tant que tel. Vous devriez voir que son "invite" ressemble à ce qui suit.

      $

Cliquez à l'intérieur de cette fenêtre de terminal, puis tapez

      mkdir hello

suivi de la touche Entrée pour créer un répertoire appelé `hello` dans votre espace de code. Faites attention à ne pas oublier l'espace entre `mkdir` et `hello` ou tout autre caractère !

Dès maintenant, exécuter une commande signifie la taper dans une fenêtre de terminal et appuyer sur Entrée. Les commandes sont "sensibles à la casse", donc assurez-vous de ne pas taper en majuscules lorsque vous voulez utiliser des minuscules ou vice versa.

Maintenant, exécutez

      cd hello

pour entrer (ouvrir) ce répertoire. Votre invite doit maintenant ressembler à ce qui suit.

      hello/ $

Si ce n'est pas le cas, rétracez vos étapes et voyez si vous pouvez déterminer où vous avez fait une erreur !

Voulez-vous écrire votre premier programme ? Exécutez

      code hello.c

pour créer un nouveau fichier appelé `hello.c`, qui devrait s'ouvrir automatiquement dans l'éditeur de texte de votre espace de code. Dès que vous avez enregistré le fichier avec Command-S (sur macOS) ou Control-S (sur Windows), il devrait également apparaître dans l'explorateur de fichiers de votre espace de code.

Procédez maintenant à l'écriture de votre premier programme en tapant précisément ces lignes dans `hello.c` :

      #include <stdio.h>
  
      int main(void)
      {
          printf("hello, world\n");
      }

Remarquez comment VS Code ajoute une "coloration syntaxique" (c'est-à-dire, de couleur) lorsque vous tapez, bien que le choix des couleurs de VS Code puisse différer de celui de cet ensemble de problème. Ces couleurs ne sont pas réellement enregistrées dans le fichier lui-même ; elles sont simplement ajoutées par VS Code pour mettre en évidence une syntaxe spécifique. Si vous n'aviez pas enregistré le fichier sous le nom `hello.c` depuis le début, VS Code ne saurait pas (selon l'extension du nom de fichier) que vous écrivez du code C, auquel cas ces couleurs seraient absentes.

## Liste des fichiers

Ensuite, dans votre fenêtre de terminal, juste à droite de l'invite (`hello/ $`), exécutez immédiatement

      ls

Vous ne devriez voir que `hello.c` ? C'est parce que vous n'avez fait que lister les fichiers de votre dossier `hello`. En particulier, vous avez exécuté une commande appelée `ls`, qui est un raccourci pour "list". (C'est une commande tellement fréquemment utilisée que ses auteurs l'ont appelée simplement `ls` pour économiser des frappes.) Cela a-t-il du sens ?

## Compilation de programmes

Maintenant, avant que nous puissions exécuter le programme `hello.c`, il faut rappeler que nous devons _compiler_ avec un _compilateur_, le traduisant du _code source_ en _code machine_ (c'est-à-dire, des zéros et des uns). Exécutez la commande ci-dessous pour faire exactement cela :

      make hello

Et ensuite, exécutez celle-ci à nouveau :

      ls

Cette fois, vous devriez voir non seulement `hello.c`, mais aussi `hello` listé ? Vous avez maintenant traduit le code source de `hello.c` en code machine de `hello`.

Maintenant, exécutez le programme lui-même en exécutant celui-ci-dessous.

      ./hello

Bonjour, monde, en effet !

## Obtenir des entrées utilisateur

Inutile de dire que, peu importe comment vous compilez ou exécutez ce programme, il ne fait qu'imprimer `hello, world`. Personnalisons-le un peu, tout comme nous l'avons fait en classe.

Modifiez ce programme de manière à ce qu'il demande d'abord à l'utilisateur leur nom, puis imprime "hello, untel", où "untel" est leur nom réel.

Comme auparavant, assurez-vous de compiler votre programme avec :

      make hello

Et assurez-vous d'exécuter votre programme, en testant quelques fois avec différentes entrées, avec :

      ./hello

### Guide en vidéo

Voici une "visite guidée" de ce problème, si vous voulez également une vue d'ensemble verbale de ce qu'il faut faire !

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/wSk1KSDUEYA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Conseils

#### Ne vous souvenez pas comment demander le nom de l'utilisateur ?

Souvenez-vous que vous pouvez utiliser `get_string` comme suit, stockant sa _valeur de retour_ dans une variable appelée `name` de type `string`.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">string</span> <span class="n">name</span> <span class="o">=</span> <span class="n">get_string</span><span class="p">(</span><span class="s">"What's your name? "</span><span class="p">);</span>
</code></pre></div></div>

#### Ne vous souvenez pas comment formater une chaîne de caractères ?

Ne vous souvenez pas comment joindre (c'est-à-dire, concaténer) le nom de l'utilisateur avec une salutation ? Souvenez-vous que vous pouvez utiliser `printf` non seulement pour afficher mais aussi pour formater une chaîne de caractères (d'où le `f` dans `printf`), comme ci-dessous, où `name` est une `string`.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">printf</span><span class="p">(</span><span class="s">"hello, %s</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">name</span><span class="p">);</span>
</code></pre></div></div>

#### Utilisation d'un identificateur non déclaré ?

Voyez-vous l'erreur ci-dessous, peut-être au-dessus d'autres erreurs ?

    error: use of undeclared identifier 'string'; did you mean 'stdin'?

Rappelez-vous que, pour utiliser `get_string`, vous devez inclure `cs50.h` (dans lequel `get_string` est _déclaré_) au sommet d'un fichier, comme ceci :

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include</span> <span class="cpf">&lt;cs50.h&gt;</span><span class="cp">
</span></code></pre></div></div>

### Comment tester votre code

Exécutez la commande ci-dessous pour évaluer la justesse de votre code à l'aide de `check50`, un programme en ligne de commande qui affichera des visages heureux chaque fois que votre code passera les tests automatisés de CS50 et des visages tristes chaque fois que cela ne se produira pas ! Mais assurez-vous de le compiler et de le tester vous-même aussi !

      check50 cs50/problems/2023/x/hello

Exécutez la commande ci-dessous pour évaluer le style de votre code à l'aide de `style50`, un programme en ligne de commande qui affichera les ajouts (en vert) et les suppressions (en rouge) que vous devriez apporter à votre programme afin d'améliorer son style. Si vous avez des problèmes pour voir ces couleurs, `style50` prend en charge d'autres [modes](https://cs50.readthedocs.io/style50/) aussi!

      style50 hello.c

## Comment envoyer votre travail

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

      submit50 cs50/problems/2023/x/hello