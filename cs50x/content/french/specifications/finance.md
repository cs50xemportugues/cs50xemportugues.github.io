# C$50 Finance

<div class="alert" data-alert="warning" role="alert">
    <p>Le code de distribution de cet ensemble de problèmes a récemment été modifié. Si vous avez téléchargé le code de distribution avant le <a data-local="2022-12-01T00:00:00+00:00" href="https://time.cs50.io/20221201T000000Z">1er décembre 2022 à 00:00:00 UTC</a>, exécutez les commandes terminales suivantes dans votre répertoire <code class="language-plaintext highlighter-rouge">finance</code> pour télécharger la dernière version du code de distribution.</p>
 
 <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ rm helpers.py
 $ wget https://cdn.cs50.net/2022/fall/psets/9/finance/helpers.py
 </code></pre></div></div>
</div>


Implémentez un site web via lequel les utilisateurs peuvent "acheter" et "vendre" des actions, de la même manière que ci-dessous.

![C$50 Finance](https://cs50.harvard.edu/x/2023/psets/9/finance/finance.png)

## Contexte

Si vous n'êtes pas tout à fait sûr de ce que cela signifie d'acheter et de vendre des actions (c'est-à-dire des actions d'une entreprise), rendez-vous [ici](https://www.investopedia.com/articles/basics/06/invest1000.asp) pour un tutoriel.

Vous êtes sur le point de mettre en œuvre C$50 Finance, une application web via laquelle vous pouvez gérer des portefeuilles d'actions. Non seulement cet outil vous permettra de vérifier les cours réels des actions et les valeurs des portefeuilles, mais il vous permettra également d'acheter (ok, "acheter") et de vendre (ok, "vendre") des actions en interrogeant [IEX](https://iextrading.com/developer/) pour connaître les prix des actions.

En effet, IEX vous permet de télécharger les citations d'actions via leur API (interface de programmation d'applications) en utilisant des URL comme `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Remarquez comment le symbole Netflix (NFLX) est intégré dans cette URL ; c'est ainsi que IEX sait de quelles données il s'agit. Ce lien ne renverra en réalité aucune donnée car IEX vous demande d'utiliser une clé API (nous en parlerons un peu plus loin), mais si tel était le cas, vous verriez une réponse au format JSON (JavaScript Object Notation) comme celle-ci :

    {
      "avgTotalVolume": 15918066,
      "calculationPrice": "close",
      "change": -8.27,
      "changePercent": -0.03074,
      "close": 260.79,
      "closeSource": "official",
      "closeTime": 1667592000924,
      "companyName": "Netflix Inc.",
      "currency": "USD",
      "delayedPrice": 260.81,
      "delayedPriceTime": 1667591988947,
      "extendedChange": 0.21,
      "extendedChangePercent": 0.00081,
      "extendedPrice": 261,
      "extendedPriceTime": 1667606392772,
      "high": 274.97,
      "highSource": "cours retardé de 15 minutes",
      "highTime": 1667592000831,
      "iexAskPrice": None,
      "iexAskSize": None,
      "iexBidPrice": None,
      "iexBidSize": None,
      "iexClose": 260.85,
      "iexCloseTime": 1667591999754,
      "iexLastUpdated": None,
      "iexMarketPercent": None,
      "iexOpen": 271.67,
      "iexOpenTime": 1667568602197,
      "iexRealtimePrice": None,
      "iexRealtimeSize": None,
      "iexVolume": None,
      "lastTradeTime": 1667591999820,
      "latestPrice": 260.79,
      "latestSource": "Clôturer",
      "latestTime": "4 novembre 2022",
      "latestUpdate": 1667592000924,
      "latestVolume": 11124694,
      "low": 255.32,
      "lowSource": "cours retardé de 15 minutes",
      "lowTime": 1667584872696,
      "marketCap": 115215720136,
      "oddLotDelayedPrice": 260.81,
      "oddLotDelayedPriceTime": 1667591988947,
      "open": 271.9,
      "openTime": 1667568601785,
      "openSource": "official",
      "peRatio": 23.39,
      "previousClose": 269.06,
      "previousVolume": 7057350,
      "primaryExchange": "NASDAQ",
      "symbol": "NFLX",
      "volume": 11124694,
      "week52High": 700.99,
      "week52Low": 162.71,
      "ytdChange": -0.5978504176349512,
      "isUSMarketOpen": False
    }

Remarquez comment, entre les accolades, il y a une liste de paires clé-valeur séparées par des virgules, avec deux points séparant chaque clé de sa valeur.

Tournons maintenant notre attention vers l'obtention du code de distribution de ce problème !

## Pour commencer

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez voir une invite de terminal comme ci-dessous:

    $

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/9/finance.zip

pour télécharger un fichier ZIP appelé `finance.zip` dans votre espace de code.

Ensuite, exécutez

    unzip finance.zip

pour créer un dossier appelé `finance`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm finance.zip

et répondre "y" suivi de Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd finance

suivi de Entrée pour vous déplacer (c.-à-d. ouvrir) ce dossier. Votre invite devrait maintenant ressembler à celle ci-dessous.

    finance/ $

Exécutez `ls` tout seul et vous devriez voir quelques fichiers et dossiers:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur !

### Configuration

Avant de commencer cette affectation, nous devrons nous inscrire pour une clé d'API afin de pouvoir interroger les données d'IEX. Pour ce faire, suivez ces étapes:

- Visitez [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
- Sélectionnez le type de compte "Individual", puis saisissez votre nom, votre adresse e-mail et un mot de passe, et cliquez sur "Créer un compte".
- Une fois inscrit, faites défiler jusqu'à "Commencer gratuitement" et cliquez sur "Sélectionner le plan de démarrage" pour choisir le plan gratuit. _Notez que ce plan ne fonctionne que pendant 30 jours à partir du jour où vous créez votre compte._ Gardez cela à l'esprit si vous envisagez d'utiliser la même API pour votre projet final !
- Une fois que vous avez confirmé votre compte par email de confirmation, visitez [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
- Copiez la clé qui apparaît sous la colonne _Token_ (elle doit commencer par `pk_`).
- Dans votre fenêtre de terminal, exécutez:

<pre>
$ export API_KEY=value
</pre>

où `value` est la valeur collée, sans aucun espace immédiatement avant ou après le signe `=`. Vous pouvez également coller cette valeur dans un document texte quelque part, au cas où vous en auriez besoin ultérieurement.

### Exécution

Démarrez le serveur web intégré de Flask (dans `finance/`):

    $ flask run

Visitez l'URL produite par `flask` pour voir le code de distribution en action. Cependant, vous ne pourrez pas vous connecter ou vous inscrire pour l'instant !

Dans `finance/`, exécutez `sqlite3 finance.db` pour ouvrir `finance.db` avec `sqlite3`. Si vous exécutez `.schema` dans l'invite SQLite, remarquez que `finance.db` est livré avec une table appelée `users`. Jetez un coup d'œil à sa structure (c.-à-d. le schéma). Remarquez comment, par défaut, les nouveaux utilisateurs recevront 10 000 $ en espèces. Mais si vous exécutez `SELECT * FROM users;`, il n'y a pas encore d'utilisateurs (c.-à-d. de lignes) à parcourir.

Une autre façon de visualiser `finance.db` consiste à utiliser un programme appelé phpLiteAdmin. Cliquez sur `finance.db` dans l'explorateur de fichiers de votre espace de code, puis cliquez sur le lien affiché sous le texte "Veuillez visiter le lien suivant pour autoriser l'aperçu GitHub". Vous devriez voir des informations sur la base de données elle-même, ainsi qu'une table, `users`, comme vous l'avez vu dans la promp `sqlite3` avec `.schema`.

### Compréhension

#### `app.py`

Ouvrez `app.py`. En haut du fichier se trouvent plusieurs importations, parmi elles le module SQL de CS50 et quelques fonctions d'aide. Plus sur cela bientôt.

Après avoir configuré [Flask] (https://flask.pocoo.org/), remarquez comment ce fichier désactive la mise en cache des réponses (à condition que vous soyez en mode de débogage, ce qui est le cas par défaut dans votre espace de code code50), de peur que vous ne fassiez une modification à un fichier mais que votre navigateur ne la remarque pas. Remarquez ensuite comment il configure [Jinja] (https://jinja.pocoo.org/) avec un "filtre" personnalisé, `usd`, une fonction (définie dans `helpers.py`) qui facilitera la formatage des valeurs en dollars américains (USD). Il configure ensuite Flask pour stocker les [sessions](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) sur le système de fichiers local (c.-à-d., le disque) plutôt que de les stocker à l'intérieur de cookies (signés numériquement), qui est la valeur par défaut de Flask. Le fichier configure ensuite le module SQL de CS50 pour utiliser `finance.db`.

Ensuite, il y a beaucoup de routes, dont seulement deux sont entièrement implémentées : `login` et `logout`. Lisez d'abord la mise en œuvre de `login`. Remarquez comment il utilise `db.execute` (de la bibliothèque de CS50) pour interroger `finance.db`. Et remarquez comment il utilise `check_password_hash` pour comparer les hachages des mots de passe des utilisateurs. Notez également comment `login` "se souvient" qu'un utilisateur est connecté en stockant son `user_id`, un ENTIER, dans la `session`. Ainsi, toutes les routes de ce fichier peuvent vérifier quel utilisateur, le cas échéant, est connecté. Enfin, remarquez comment une fois que l'utilisateur s'est connecté avec succès, `login` redirigera vers `"/"`, emmenant l'utilisateur sur sa page d'accueil. Pendant ce temps, notez comment `logout` efface simplement la `session`, ce qui déconnecte effectivement un utilisateur.

Notez comment la plupart des routes sont "décorées" avec `@login_required` (une fonction définie dans `helpers.py` également). Ce décorateur garantit que, si un utilisateur essaie de visiter l'une de ces routes, il ou elle sera d'abord redirigé vers `login` pour se connecter.

Notez également comment la plupart des routes prennent en charge GET et POST. Même ainsi, la plupart d'entre elles (pour l'instant !) renvoient simplement des "excuses", car elles ne sont pas encore implémentées.

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

## Spécifications

### `register`

Terminez l'implémentation de `register` de manière à permettre à un utilisateur de s'inscrire via un formulaire.

- Exigez qu'un utilisateur entre un nom d'utilisateur, implémenté comme un champ de texte dont le `name` est `username`. Affichez des excuses si l'entrée de l'utilisateur est vide ou si le nom d'utilisateur existe déjà.
- Exigez qu'un utilisateur entre un mot de passe, implémenté comme un champ de texte dont le `name` est `password`, puis ce même mot de passe à nouveau, implémenté comme un champ de texte dont le `name` est `confirmation`. Affichez des excuses si l'une des entrées est vide ou si les mots de passe ne correspondent pas.
- Soumettez l'entrée de l'utilisateur via `POST` à `/register`.
- `INSERT` le nouvel utilisateur dans `users`, en stockant un hash du mot de passe de l'utilisateur, pas le mot de passe lui-même. Hachez le mot de passe de l'utilisateur avec [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.security.generate_password_hash). Il est probable que vous voudrez créer un nouveau modèle (par exemple, `register.html`) qui est assez similaire à `login.html`.

Une fois que vous avez correctement implémenté `register`, vous devriez être en mesure de vous inscrire et de vous connecter (puisque `login` et `logout` fonctionnent déjà)! Et vous devriez être en mesure de voir vos lignes via phpLiteAdmin ou `sqlite3`.

### `quote`

Terminez l'implémentation de `quote` de manière à permettre à un utilisateur de consulter le prix actuel d'une action.

- Exigez qu'un utilisateur entre le symbole d'une action, implémenté comme un champ de texte dont le `name` est `symbol`.
- Soumettez l'entrée de l'utilisateur via `POST` à `/quote`.
- Il est probable que vous vouliez créer deux nouveaux modèles (par exemple, `quote.html` et `quoted.html`). Lorsqu'un utilisateur visite `/quote` via `GET`, affichez l'un de ces modèles, à l'intérieur duquel devrait figurer un formulaire HTML qui soumet à `/quote` via `POST`. En réponse à une POST, `quote` peut afficher ce deuxième modèle, incorporant en son sein une ou plusieurs valeurs de `lookup`.

### `buy`

Terminez l'implémentation de `buy` de manière à permettre à un utilisateur d'acheter des actions.

- Exigez qu'un utilisateur entre le symbole d'une action, implémenté comme un champ de texte dont le `name` est `symbol`. Affichez des excuses si l'entrée est vide ou si le symbole n'existe pas (selon la valeur de retour de `lookup`).
- Exigez qu'un utilisateur entre un nombre d'actions, implémenté comme un champ de texte dont le `name` est `shares`. Affichez des excuses si l'entrée n'est pas un entier positif.
- Soumettez l'entrée de l'utilisateur via `POST` à `/buy`.
- À la fin, redirigez l'utilisateur vers la page d'accueil.
- Il est probable que vous deviez appeler `lookup` pour consulter le prix actuel d'une action.
- Il est probable que vous deviez `SELECT` pour savoir combien d'argent l'utilisateur a actuellement dans `users`.
- Ajoutez une ou plusieurs nouvelles tables à `finance.db` via lesquelles suivre les achats. Stockez suffisamment d'informations pour savoir qui a acheté quoi, à quel prix et quand.
  - Utilisez des types SQLite appropriés.
  - Définissez des index `UNIQUE` sur les champs qui doivent l'être.
  - Définissez des index (non `UNIQUE`) sur les champs via lesquels vous allez effectuer une recherche (comme via `SELECT` avec `WHERE`).
- Affichez des excuses, sans effectuer un achat, si l'utilisateur ne peut pas se permettre le nombre d'actions au prix actuel.
- Vous n'avez pas besoin de vous soucier des conditions de concurrence (ou d'utiliser des transactions).

Une fois que vous avez correctement implémenté `buy`, vous devriez être en mesure de voir les achats des utilisateurs dans votre(s) nouvelle(s) table(s) via phpLiteAdmin ou `sqlite3`.

### `index`

Complétez l'implémentation de `index` de manière à afficher un tableau HTML récapitulant, pour l'utilisateur actuellement connecté, les actions que l'utilisateur possède, le nombre d'actions, le cours actuel de chaque action et la valeur totale de chaque position (c'est-à-dire le nombre d'actions multiplié par le cours). Affichez également le solde de trésorerie actuel de l'utilisateur ainsi qu'un total général (la valeur totale des actions plus la trésorerie).

- Il est probable que vous deviez exécuter plusieurs `SELECT`. En fonction de la façon dont vous implémentez votre ou vos tables, vous pourriez trouver les clauses [GROUP BY](https://www.google.com/search?q=SQLite+GROUP+BY,), [HAVING](https://www.google.com/search?q=SQLite+HAVING,),  [SUM](https://www.google.com/search?q=SQLite+SUM,) et/ou [WHERE](https://www.google.com/search?q=SQLite+WHERE) intéressantes.
- Il est probable que vous souhaitiez appeler `lookup` pour chaque action.

### `sell`

Complétez l'implémentation de `sell` de manière à permettre à un utilisateur de vendre des actions d'une action (qu'il possède).

- Exigez qu'un utilisateur entre le symbole d'une action, implémenté à l'aide d'un menu de sélection dont le `name` est `symbol`. Affichez des excuses si l'utilisateur omet de sélectionner une action ou si, d'une manière ou d'une autre, une fois soumis, l'utilisateur ne possède aucune action de cette action.
- Exigez qu'un utilisateur entre le nombre d'actions, implémenté à l'aide d'un champ de texte dont le `name` est `shares`. Affichez des excuses si l'entrée n'est pas un entier positif ou si l'utilisateur ne possède pas autant d'actions de l'action.
- Soumettez l'entrée de l'utilisateur via `POST` à `/sell`.
- Après la vente d'actions, redirigez l'utilisateur vers la page d'accueil.
- Vous n'avez pas besoin de vous soucier des conditions de concurrence (ou d'utiliser des transactions).

### `history`

Complétez l'implémentation de `history` de manière à afficher un tableau HTML récapitulant l'ensemble des transactions d'un utilisateur, énumérant ligne par ligne chaque achat et chaque vente.

- Pour chaque ligne, précisez si une action a été achetée ou vendue et incluez le symbole de l'action, le prix (achat ou vente), le nombre d'actions achetées ou vendues, ainsi que la date et l'heure de la transaction.
- Vous devrez peut-être modifier le tableau que vous avez créé pour l'achat ou le compléter avec un tableau supplémentaire. Essayez de minimiser les redondances.

### Touche personnelle

Implémentez au moins une touche personnelle de votre choix :

- Permettez aux utilisateurs de modifier leur mot de passe.
- Permettez aux utilisateurs d'ajouter des fonds supplémentaires à leur compte.
- Permettez aux utilisateurs d'acheter plus d'actions ou de vendre des actions des actions qu'ils possèdent déjà via `index` lui-même, sans avoir à taper les symboles des actions manuellement.
- Exigence qu'un mot de passe d'utilisateur doit comporter un certain nombre de lettres, de chiffres et/ou de symboles.
- Implémentez une autre fonctionnalité de portée comparable.

## Guide


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


## Test

Veillez à tester votre application web manuellement en :

- enregistrant un nouvel utilisateur et en vérifiant que sa page de portefeuille se charge avec les informations correctes,
- demandant un devis en utilisant un symbole d’action valide,
- achetant une action plusieurs fois, en vérifiant que le portefeuille affiche les totaux corrects,
- vendant toutes ou certaines actions, en vérifiant à nouveau le portefeuille, et
- vérifiant que votre page d'historique affiche toutes les transactions pour l'utilisateur connecté.

Testez également certains cas d'utilisation imprévus, tels que :

- saisir des chaînes alphabétiques dans des formulaires lorsqu'il faut uniquement des chiffres,
- saisir des nombres nuls ou négatifs dans des formulaires lorsque seuls des nombres positifs sont attendus,
- saisir des valeurs à virgule flottante dans des formulaires lorsque seuls des entiers sont attendus,
- essayer de dépenser plus d'argent qu'un utilisateur n'en a,
- essayer de vendre plus d'actions qu'un utilisateur n'en a,
- saisir un symbole d'action invalide, et
- inclure des caractères potentiellement dangereux comme `'` et `;` dans les requêtes SQL.

Une fois satisfait, pour tester votre code avec `check50`, exécutez la commande suivante.

    check50 cs50/problems/2023/x/finance

<div class="alert" data-alert="warning" role="alert"><p>Soyez conscients que <code class="language-plaintext highlighter-rouge">check50</code> testera l'ensemble de votre programme.  Si vous l'exécutez <strong>avant</strong> d'avoir terminé toutes les fonctions requises, il est possible qu'il signale des erreurs dans des fonctions qui sont en réalité correctes mais qui dépendent d'autres fonctions.</p></div>


Exécutez la commande suivante pour évaluer le style de vos fichiers Python avec `style50`.

    style50 *.py

## Solution de l'équipe enseignante

Vous pouvez styliser votre propre application de manière différente, mais voici à quoi ressemble la solution de l'équipe d'enseignants !

[https://finance.cs50.net/](https://finance.cs50.net/)

N'hésitez pas à vous inscrire pour un compte et à jouer. Ne **utilisez pas** un mot de passe que vous utilisez sur d'autres sites.

Il est **raisonnable** de regarder le HTML et le CSS de l'équipe enseignante.

## Conseils

- Pour formater une valeur en dollars américains (avec les cents affichés à deux décimales), vous pouvez utiliser le filtre `usd` dans vos templates Jinja (en imprimant les valeurs comme `{{ value | usd }}` au lieu de `{{ value }}`.
- Dans `cs50.SQL`, il y a une méthode `execute` dont le premier argument doit être une chaîne SQL. Si cette chaîne contient des paramètres de point d'interrogation auxquels des valeurs doivent être liées, ces valeurs peuvent être fournies en tant que paramètres nommés supplémentaires à `execute`. Consultez la mise en œuvre de `login` pour un exemple de ce genre. La valeur de retour de `execute` est la suivante :

  - Si la chaîne est un `SELECT`, `execute` renvoie une `list` de zéro ou plusieurs objets `dict`, à l'intérieur desquels se trouvent des clés et des valeurs représentant les champs et les cellules d'une table, respectivement.
  - Si la chaîne est un `INSERT`, et que la table dans laquelle les données ont été insérées contient une `PRIMARY KEY` auto-incrémentée, `execute` renvoie la valeur de la clé primaire de la nouvelle ligne insérée.
  - Si la chaîne est un `DELETE` ou une `UPDATE`, `execute` renvoie le nombre de lignes supprimées ou mises à jour par `str`.

- Rappelons que `cs50.SQL` journalisera dans votre terminal toutes les requêtes que vous exécuterez via `execute` (pour que vous puissiez confirmer qu'elles sont telles que prévues).
- Veillez à utiliser des paramètres liés par des points d'interrogation (c'est-à-dire un [paramètrestyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) de `named`) lors de l'appel de la méthode `execute` de CS50, par exemple`WHERE ?`. N'utilisez **pas** les f-strings, [`format`](https://docs.python.org/3.6/library/functions.html#format,) ou `+` (c'est-à-dire la concaténation), sous peine de risquer une attaque d'injection SQL.
- Si (et seulement si) vous êtes déjà à l'aise avec SQL, vous pouvez utiliser [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) ou [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (c'est-à-dire [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)) au lieu de `cs50.SQL`.
- Vous pouvez ajouter des fichiers statiques supplémentaires à `static/`.
- Il est fort probable que vous souhaitiez consulter la documentation de Jinja [Jinja’s documentation](https://jinja.palletsprojects.com/en/3.1.x/) lors de la mise en œuvre de vos modèles.
- Demander à d'autres de tester (et de déclencher des erreurs sur) votre site est **raisonnable**.
- Vous êtes libre de modifier l'esthétique des sites, par exemple :
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/), et/ou
  - [memegen.link](https://memegen.link/).
- Vous pourriez trouver [la documentation de Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) et [celle de Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) utiles !

## FAQ

### ImportError: No module named ‘application’

Par défaut, `flask` recherche un fichier appelé `app.py` dans votre répertoire de travail actuel (car nous avons configuré la valeur de `FLASK_APP`, une variable d'environnement, pour être `app.py`). Si vous voyez cette erreur, vous avez probablement exécuté `flask` dans le mauvais répertoire.

### OSError: \[Errno 98\] Address already in use

Si, lors de l'exécution de `flask`, vous voyez cette erreur, il est probable que vous (re)ayez `flask` en cours d'exécution dans un autre onglet. Assurez-vous de tuer cet autre processus, avec Ctrl+C par exemple, avant de redémarrer `flask`. Si vous n'avez pas d'autre onglet de ce genre, exécutez `fuser -k 8080/tcp` pour tuer tout processus qui écouterait encore sur le port TCP 8080.

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2023/x/finance
"

