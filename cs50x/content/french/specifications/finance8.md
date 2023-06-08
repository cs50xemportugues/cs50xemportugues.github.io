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