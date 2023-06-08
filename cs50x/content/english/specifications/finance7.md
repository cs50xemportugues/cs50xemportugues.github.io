
## Walkthrough


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


## Testing

Be sure to test your web app manually, as by

- registering a new user and verifying that their portfolio page loads with the correct information,
- requesting a quote using a valid stock symbol,
- purchasing one stock multiple times, verifying that the portfolio displays correct totals,
- selling all or some of a stock, again verifying the portfolio, and
- verifying that your history page shows all transactions for your logged in user.

Also test some unexpected usage, as by

- inputting alphabetical strings into forms when only numbers are expected,
- inputting zero or negative numbers into forms when only positive numbers are expected,
- inputting floating-point values into forms when only integers are expected,
- trying to spend more cash than a user has,
- trying to sell more shares than a user has,
- inputting an invalid stock symbol, and
- including potentially dangerous characters like `'` and `;` in SQL queries.

Once satisfied, to test your code with `check50`, execute the below.

    check50 cs50/problems/2023/x/finance

<div class="alert" data-alert="warning" role="alert"><p>Be aware that <code class="language-plaintext highlighter-rouge">check50</code> will test your entire program as a whole.  If you run it <strong>before</strong> completing all required functions, it may report errors on functions that are actually correct but depend on other functions.</p></div>


Execute the below to evaluate the style of your Python files using `style50`.

    style50 *.py

## Staff’s Solution

You’re welcome to stylize your own app differently, but here’s what the staff’s solution looks like!

[https://finance.cs50.net/](https://finance.cs50.net/)

Feel free to register for an account and play around. Do **not** use a password that you use on other sites.

It is **reasonable** to look at the staff’s HTML and CSS.
