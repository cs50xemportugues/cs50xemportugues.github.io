Getting Started
---------------

Log into [code.cs50.io](https://code.cs50.io/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $
    

Next execute

    wget https://cdn.cs50.net/2022/fall/psets/4/filter-less.zip
    

in order to download a ZIP called `filter-less.zip` into your codespace.

Then execute

    unzip filter-less.zip
    

to create a folder called `filter-less`. You no longer need the ZIP file, so you can execute

    rm filter-less.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd filter-less
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    filter-less/ $
    

Execute `ls` by itself, and you should see a few files: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c`, and `Makefile`. You should also see a folder called `images` with four BMP files. If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!
