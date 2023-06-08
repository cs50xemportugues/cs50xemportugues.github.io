
## Getting Started

Log into [code.cs50.io](https://code.cs50.io/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2022/fall/psets/9/finance.zip

in order to download a ZIP called `finance.zip` into your codespace.

Then execute

    unzip finance.zip

to create a folder called `finance`. You no longer need the ZIP file, so you can execute

    rm finance.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd finance

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    finance/ $

Execute `ls` by itself, and you should see a few files and folders:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

### Configuring

Before getting started on this assignment, we’ll need to register for an API key in order to be able to query IEX’s data. To do so, follow these steps:

- Visit [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
- Select the “Individual” account type, then enter your name, email address, and a password, and click “Create account”.
- Once registered, scroll down to “Get started for free” and click “Select Start plan” to choose the free plan. _Note that this plan only works for 30 days from the day you create your account._ Keep this in mind if you might plan to use this same API for your final project!
- Once you’ve confirmed your account via a confirmation email, visit [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
- Copy the key that appears under the _Token_ column (it should begin with `pk_`).
- In your terminal window, execute:

<pre>
$ export API_KEY=value
</pre>

where `value` is that (pasted) value, without any space immediately before or after the `=`. You also may wish to paste that value in a text document somewhere, in case you need it again later.
