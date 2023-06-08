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