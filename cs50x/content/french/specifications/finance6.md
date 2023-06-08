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