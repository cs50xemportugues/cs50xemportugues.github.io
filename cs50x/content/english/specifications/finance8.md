
## Hints

- To format a value as a US dollar value (with cents listed to two decimal places), you can use the `usd` filter in your Jinja templates (printing values as `{{ value | usd }}` instead of `{{ value }}`.
- Within `cs50.SQL` is an `execute` method whose first argument should be a `str` of SQL. If that `str` contains question mark parameters to which values should be bound, those values can be provided as additional named parameters to `execute`. See the implementation of `login` for one such example. The return value of `execute` is as follows:

  - If `str` is a `SELECT`, then `execute` returns a `list` of zero or more `dict` objects, inside of which are keys and values representing a table’s fields and cells, respectively.
  - If `str` is an `INSERT`, and the table into which data was inserted contains an autoincrementing `PRIMARY KEY`, then `execute` returns the value of the newly inserted row’s primary key.
  - If `str` is a `DELETE` or an `UPDATE`, then `execute` returns the number of rows deleted or updated by `str`.

- Recall that `cs50.SQL` will log to your terminal window any queries that you execute via `execute` (so that you can confirm whether they’re as intended).
- Be sure to use question mark-bound parameters (i.e., a [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) of `named`) when calling CS50’s `execute` method, a la `WHERE ?`. Do **not** use f-strings, [`format`](https://docs.python.org/3.6/library/functions.html#format,) or `+` (i.e., concatenation), lest you risk a SQL injection attack.
- If (and only if) already comfortable with SQL, you’re welcome to use [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) or [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (i.e., [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)) instead of `cs50.SQL`.
- You’re welcome to add additional static files to `static/`.
- Odds are you’ll want to consult [Jinja’s documentation](https://jinja.palletsprojects.com/en/3.1.x/) when implementing your templates.
- It is **reasonable** to ask others to try out (and try to trigger errors in) your site.
- You’re welcome to alter the aesthetics of the sites, as via
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/), and/or
  - [memegen.link](https://memegen.link/).
- You may find [Flask’s documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and [Jinja’s documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/) helpful!

## FAQs

### ImportError: No module named ‘application’

By default, `flask` looks for a file called `app.py` in your current working directory (because we’ve configured the value of `FLASK_APP`, an environment variable, to be `app.py`). If seeing this error, odds are you’ve run `flask` in the wrong directory!

### OSError: \[Errno 98\] Address already in use

If, upon running `flask`, you see this error, odds are you (still) have `flask` running in another tab. Be sure to kill that other process, as with ctrl-c, before starting `flask` again. If you haven’t any such other tab, execute `fuser -k 8080/tcp` to kill any processes that are (still) listening on TCP port 8080.

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/finance
