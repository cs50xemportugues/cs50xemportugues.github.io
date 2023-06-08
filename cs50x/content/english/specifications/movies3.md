
Walkthrough
-----------


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Usage
-----

To test your queries in VS Code, you can query the database by running

    $ cat filename.sql | sqlite3 movies.db
    

where `filename.sql` is the file containing your SQL query.

You can also run

    $ cat filename.sql | sqlite3 movies.db > output.txt
    

to redirect the output of the query to a text file called `output.txt`. (This can be useful for checking how many rows are returned by your query!)

Hints
-----

*   See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!
*   See [sqlstyle.guide](https://www.sqlstyle.guide/) for pointers on good style in SQL, especially as your queries get more complex!

Testing
-------

While `check50` is available for this problem, you’re encouraged to instead test your code on your own for each of the following. You can run `sqlite3 movies.db` to run additional queries on the database to ensure that your result is correct.

If you’re using the `movies.db` database provided in this problem set’s distribution, you should find that

*   Executing `1.sql` results in a table with 1 column and 10,050 rows.
*   Executing `2.sql` results in a table with 1 column and 1 row.
*   Executing `3.sql` results in a table with 1 column and 88,918 rows.
*   Executing `4.sql` results in a table with 1 column and 1 row.
*   Executing `5.sql` results in a table with 2 columns and 12 rows.
*   Executing `6.sql` results in a table with 1 column and 1 row.
*   Executing `7.sql` results in a table with 2 columns and 7,085 rows.
*   Executing `8.sql` results in a table with 1 column and 4 rows.
*   Executing `9.sql` results in a table with 1 column and 18,946 rows.
*   Executing `10.sql` results in a table with 1 column and 3,392 rows.
*   Executing `11.sql` results in a table with 1 column and 5 rows.
*   Executing `12.sql` results in a table with 1 column and 7 rows.
*   Executing `13.sql` results in a table with 1 column and 182 rows.

Note that row counts do not include header rows that only show column names.

If your query returns a number of rows that is slightly different from the expected output, be sure that you’re properly handling duplicates! For queries that ask for a list of names, no one person should be listed twice, but two different people who have the same name should each be listed.

Execute the below to evaluate the correctness of your code using `check50`.

    check50 cs50/problems/2023/x/movies
    

How to Submit
-------------

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/movies
    

Acknowledgements
----------------

Information courtesy of IMDb ([imdb.com](https://www.imdb.com)). Used with permission.