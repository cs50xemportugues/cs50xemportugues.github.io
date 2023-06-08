
### Running

Start Flask’s built-in web server (within `finance/`):

    $ flask run

Visit the URL outputted by `flask` to see the distribution code in action. You won’t be able to log in or register, though, just yet!

Within `finance/`, run `sqlite3 finance.db` to open `finance.db` with `sqlite3`. If you run `.schema` in the SQLite prompt, notice how `finance.db` comes with a table called `users`. Take a look at its structure (i.e., schema). Notice how, by default, new users will receive $10,000 in cash. But if you run `SELECT * FROM users;`, there aren’t (yet!) any users (i.e., rows) therein to browse.

Another way to view `finance.db` is with a program called phpLiteAdmin. Click on `finance.db` in your codespace’s file browser, then click the link shown underneath the text “Please visit the following link to authorize GitHub Preview”. You should see information about the database itself, as well as a table, `users`, just like you saw in the `sqlite3` prompt with `.schema`.

### Understanding

#### `app.py`

Open up `app.py`. Atop the file are a bunch of imports, among them CS50’s SQL module and a few helper functions. More on those soon.

After configuring [Flask](https://flask.pocoo.org/), notice how this file disables caching of responses (provided you’re in debugging mode, which you are by default in your code50 codespace), lest you make a change to some file but your browser not notice. Notice next how it configures [Jinja](https://jinja.pocoo.org/) with a custom “filter,” `usd`, a function (defined in `helpers.py`) that will make it easier to format values as US dollars (USD). It then further configures Flask to store [sessions](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) on the local filesystem (i.e., disk) as opposed to storing them inside of (digitally signed) cookies, which is Flask’s default. The file then configures CS50’s SQL module to use `finance.db`.

Thereafter are a whole bunch of routes, only two of which are fully implemented: `login` and `logout`. Read through the implementation of `login` first. Notice how it uses `db.execute` (from CS50’s library) to query `finance.db`. And notice how it uses `check_password_hash` to compare hashes of users’ passwords. Also notice how `login` “remembers” that a user is logged in by storing his or her `user_id`, an INTEGER, in `session`. That way, any of this file’s routes can check which user, if any, is logged in. Finally, notice how once the user has successfully logged in, `login` will redirect to `"/"`, taking the user to their home page. Meanwhile, notice how `logout` simply clears `session`, effectively logging a user out.

Notice how most routes are “decorated” with `@login_required` (a function defined in `helpers.py` too). That decorator ensures that, if a user tries to visit any of those routes, he or she will first be redirected to `login` so as to log in.

Notice too how most routes support GET and POST. Even so, most of them (for now!) simply return an “apology,” since they’re not yet implemented.
