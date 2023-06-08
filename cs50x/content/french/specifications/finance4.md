#### `helpers.py`

Ensuite, jetons un coup d'œil à `helpers.py`. Ah, voilà l'implémentation de `apology`. Remarquez comment elle affiche finalement un modèle, `apology.html`. Elle définit également une autre fonction, `escape`, de manière interne, qu'elle utilise simplement pour remplacer des caractères spéciaux dans les excuses. En définissant `escape` à l'intérieur de `apology`, nous avons limité sa portée à cette dernière ; aucune autre fonction ne pourra l'appeler (ou en aura besoin).

Ensuite dans le fichier, il y a `login_required`. Pas de soucis si celui-ci est un peu cryptique, mais si vous vous êtes déjà demandé comment une fonction peut retourner une autre fonction, en voici un exemple !

Ensuite, il y a `lookup`, une fonction qui, étant donné un `symbol` (par exemple, NFLX), renvoie une citation boursière pour une entreprise sous la forme d'un `dict` avec trois clés : `name`, dont la valeur est une chaîne de caractères, le nom de l'entreprise ; `price`, dont la valeur est un `float` ; et `symbol`, dont la valeur est une chaîne de caractères, une version canonisée (en majuscules) du symbole d'une action, quel que soit le capitalisation de ce symbole au moment de sa transmission à `lookup`.

Enfin, dans le fichier, il y a `usd`, une courte fonction qui formate simplement un `float` en USD (par exemple : `1234,56` est formaté comme `$1,234.56`).

#### `requirements.txt`

Ensuite, jetez rapidement un coup d'œil à `requirements.txt`. Ce fichier prescrit simplement les packages sur lesquels cette application dépendra.

#### `static/`

Regardez également `static/`, où se trouve `styles.css`. C'est là que vit un peu de CSS. Vous êtes invité à le modifier comme bon vous semble.

#### `templates/`

Maintenant, regardons `templates/`. Dans `login.html`, il y a essentiellement juste un formulaire HTML, stylisé avec [Bootstrap](https://getbootstrap.com/). Dans `apology.html`, quant à elle, se trouve un modèle pour des excuses. Rappelez-vous que `apology` dans `helpers.py` a pris deux arguments : `message`, qui a été transmis à `render_template` en tant que valeur de `bottom`, et, éventuellement, `code`, qui a été transmis à `render_template` en tant que valeur de `top`. Remarquez dans `apology.html` comment ces valeurs sont finalement utilisées ! Et [voici pourquoi](https://github.com/jacebrowning/memegen) 0:-)

Enfin, il y a `layout.html`. Il est un peu plus grand que d'habitude, mais c'est surtout parce qu'il est livré avec une "navbar" (barre de navigation) mobile et élégante, également basée sur Bootstrap. Notez comment il définit un bloc, `main`, à l'intérieur duquel les modèles (y compris `apology.html` et `login.html`) doivent être placés. Il inclut également la prise en charge du "message flashing" de Flask afin que vous puissiez transmettre des messages d'une route à une autre pour que l'utilisateur puisse les voir.