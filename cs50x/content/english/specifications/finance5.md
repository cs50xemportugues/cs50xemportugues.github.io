
## Specification

### `register`

Complete the implementation of `register` in such a way that it allows a user to register for an account via a form.

- Require that a user input a username, implemented as a text field whose `name` is `username`. Render an apology if the user’s input is blank or the username already exists.
- Require that a user input a password, implemented as a text field whose `name` is `password`, and then that same password again, implemented as a text field whose `name` is `confirmation`. Render an apology if either input is blank or the passwords do not match.
- Submit the user’s input via `POST` to `/register`.
- `INSERT` the new user into `users`, storing a hash of the user’s password, not the password itself. Hash the user’s password with [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.security.generate_password_hash) Odds are you’ll want to create a new template (e.g., `register.html`) that’s quite similar to `login.html`.

Once you’ve implemented `register` correctly, you should be able to register for an account and log in (since `login` and `logout` already work)! And you should be able to see your rows via phpLiteAdmin or `sqlite3`.

### `quote`

Complete the implementation of `quote` in such a way that it allows a user to look up a stock’s current price.

- Require that a user input a stock’s symbol, implemented as a text field whose `name` is `symbol`.
- Submit the user’s input via `POST` to `/quote`.
- Odds are you’ll want to create two new templates (e.g., `quote.html` and `quoted.html`). When a user visits `/quote` via GET, render one of those templates, inside of which should be an HTML form that submits to `/quote` via POST. In response to a POST, `quote` can render that second template, embedding within it one or more values from `lookup`.

### `buy`

Complete the implementation of `buy` in such a way that it enables a user to buy stocks.

- Require that a user input a stock’s symbol, implemented as a text field whose `name` is `symbol`. Render an apology if the input is blank or the symbol does not exist (as per the return value of `lookup`).
- Require that a user input a number of shares, implemented as a text field whose `name` is `shares`. Render an apology if the input is not a positive integer.
- Submit the user’s input via `POST` to `/buy`.
- Upon completion, redirect the user to the home page.
- Odds are you’ll want to call `lookup` to look up a stock’s current price.
- Odds are you’ll want to `SELECT` how much cash the user currently has in `users`.
- Add one or more new tables to `finance.db` via which to keep track of the purchase. Store enough information so that you know who bought what at what price and when.
  - Use appropriate SQLite types.
  - Define `UNIQUE` indexes on any fields that should be unique.
  - Define (non-`UNIQUE`) indexes on any fields via which you will search (as via `SELECT` with `WHERE`).
- Render an apology, without completing a purchase, if the user cannot afford the number of shares at the current price.
- You don’t need to worry about race conditions (or use transactions).

Once you’ve implemented `buy` correctly, you should be able to see users’ purchases in your new table(s) via phpLiteAdmin or `sqlite3`.
