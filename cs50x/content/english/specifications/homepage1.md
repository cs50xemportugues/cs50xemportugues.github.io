Homepage
========

Build a simple homepage using HTML, CSS, and JavaScript.

Background
----------

The internet has enabled incredible things: we can use a search engine to research anything imaginable, communicate with friends and family members around the globe, play games, take courses, and so much more. But it turns out that nearly all pages we may visit are built on three core languages, each of which serves a slightly different purpose:

1.  HTML, or _HyperText Markup Language_, which is used to describe the content of websites;
2.  CSS, _Cascading Style Sheets_, which is used to describe the aesthetics of websites; and
3.  JavaScript, which is used to make websites interactive and dynamic.

Create a simple homepage that introduces yourself, your favorite hobby or extracurricular, or anything else of interest to you.

Getting Started
---------------

Log into [code.cs50.io](https://code.cs50.io/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $
    

Next execute

    wget https://cdn.cs50.net/2022/fall/psets/8/homepage.zip
    

in order to download a ZIP called `homepage.zip` into your codespace.

Then execute

    unzip homepage.zip
    

to create a folder called `homepage`. You no longer need the ZIP file, so you can execute

    rm homepage.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd homepage
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    homepage/ $
    

Execute `ls` by itself, and you should see a few files:

    index.html  styles.css
    

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong! You can immediately start a server to view your site by running

    http-server
    

in the terminal window. Then, command-click (if on Mac) or control-click (if on PC) on the first link that appears:

    http-server running on LINK
    

Where LINK is the address of your server.
