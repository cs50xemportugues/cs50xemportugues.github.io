# Lab 9: Birthdays

<div class="alert" data-alert="warning" role="alert"><p>You are welcome to collaborate with one or two classmates on this lab, though it is expected that every student in any such group contribute equally to the lab.</p></div>

Create a web application to keep track of friends’ birthdays.

![screenshot of birthdays website](https://cs50.harvard.edu/x/2023/labs/9/birthdays.png)

## Getting Started


<div class="alert" data-alert="primary" role="alert"><p>Started CS50x in 2021 or prior and need to migrate your work from CS50 IDE to the new VS Code codespace? Be sure to check out our instructions on how to <a href="../../new/">migrate</a> your files!</p></div>

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/labs/9/birthdays.zip

followed by Enter in order to download a ZIP called `birthdays.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip birthdays.zip

to create a folder called `birthdays`. You no longer need the ZIP file, so you can execute

    rm birthdays.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd birthdays

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    birthdays/ $

If all was successful, you should execute

    ls

and you should see the following files and folders:

    app.py  birthdays.db  static/  templates/

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

## Understanding

In `app.py`, you’ll find the start of a Flask web application. The application has one route (`/`) that accepts both `POST` requests (after the `if`) and `GET` requests (after the `else`). Currently, when the `/` route is requested via `GET`, the `index.html` template is rendered. When the `/` route is requested via `POST`, the user is redirected back to `/` via `GET`.

`birthdays.db` is a SQLite database with one table, `birthdays`, that has four columns: `id`, `name`, `month`, and `day`. There are a few rows already in this table, though ultimately your web application will support the ability to insert rows into this table!

In the `static` directory is a `styles.css` file containing the CSS code for this web application. No need to edit this file, though you’re welcome to if you’d like!

In the `templates` directory is an `index.html` file that will be rendered when the user views your web application.
