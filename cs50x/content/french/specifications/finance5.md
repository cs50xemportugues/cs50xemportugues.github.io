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